// Lecture de fr/site/ et rendu en HTML : filtrage éditorial, pastilles, typographie.
import fs from 'node:fs';
import path from 'node:path';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import remarkRehype from 'remark-rehype';
import rehypeStringify from 'rehype-stringify';
import { visit } from 'unist-util-visit';
import { REPO, CHIP, resolveChip, resolveAmount, dataMeta, amountOf, amountFromShareCalcs, textMentions, otherUnits, frText, subjectLabel } from './data.mjs';
import { typography, unitStats, NBSP } from './format.mjs';

const SITE_DIR = path.join(REPO, 'fr', 'site');
const TOKEN = /(\d+)/g;

// Même repérage que validate.py (_strip_comments_and_code) : pas de pastille dans les commentaires HTML ni le code.
const PROTECTED = /<!--[\s\S]*?-->|```[\s\S]*?```|`[^`\n]*`/g;
const FRONT_MATTER = /^---\n[\s\S]*?\n---\n/;
// Titres de sections éditoriales (validate.py NOTES_HEADING, complété par « Notes pour l’équipe »).
const NOTES_HEADING = /^(?:Notes|Annexe|Journal|Points? (?:à trancher|ouverts?)|Relecture|Audit|Contrôle|Liste des identifiants|Sources et pastilles)/i;

export const report = { chips: 0, chipsDisplayed: 0, warnings: [], relativeLinksDropped: 0, hiddenNotes: [] };

/** Remplace chaque pastille par un jeton privé avant l'analyse Markdown (les « * » des jokers ne cassent pas l'emphase). */
function maskChips(text, file, chips, errors) {
  const lineOf = (offset) => text.slice(0, offset).split('\n').length;
  let pos = 0;
  let out = '';
  const handle = (segment, base) => segment.replace(CHIP, (m, kind, ref, off) => {
    const res = resolveChip(kind, ref);
    report.chips++;
    if (!res.ok) { errors.push(`${file}:${lineOf(base + off)}: ${res.error}`); return ''; }
    if (res.warn) report.warnings.push(`${file}:${lineOf(base + off)}: ${res.warn}`);
    chips.push(res.entry);
    return `${chips.length - 1}`;
  });
  for (const m of text.matchAll(PROTECTED)) {
    out += handle(text.slice(pos, m.index), pos) + m[0];
    pos = m.index + m[0].length;
  }
  return out + handle(text.slice(pos), pos);
}

const slugify = (s) => s.normalize('NFD').replace(/[̀-ͯ]/g, '').toLowerCase().replace(/[^a-z0-9]+/g, '-').replace(/^-|-$/g, '');
const textOf = (node) => (node.value ?? (node.children || []).map(textOf).join(''));

/** Chapitres : ne garder que le texte affiché (blocs « > »), avec leurs titres. Tout le reste est de la spécification.
 *  Pages de réponse : seuls les blocs « > » sont affichés (titres compris, écrits dans les blocs) ; une section
 *  de notes hors bloc (« ## Notes… ») arrête l'affichage, comme Page.notes_from dans validate.py. */
function editorialFilter(file, mode) {
  return (tree) => {
    if (mode === 'answer') {
      const out = [];
      let hidden = 0;
      for (const node of tree.children) {
        if (node.type === 'heading' && node.depth <= 3 && NOTES_HEADING.test(textOf(node))) {
          report.hiddenNotes.push(`${file}: « ${textOf(node)} »`);
          break;
        }
        if (node.type === 'blockquote') out.push(...node.children);
        else hidden++;
      }
      report.hidden = (report.hidden || 0) + hidden;
      tree.children = out;
      return;
    }
    if (mode !== 'chapter') return;
    const out = [];
    let pending = null;
    let hidden = 0;
    let skipping = false; // section éditoriale (notes) : ignorée jusqu'à la prochaine étape
    for (const node of tree.children) {
      if (node.type === 'heading' && node.depth <= 3) {
        const t = textOf(node);
        if (node.depth === 1 || /^Étape/.test(t)) skipping = false;
        else if (NOTES_HEADING.test(t) || /^Notes pour l[’']équipe/i.test(t)) {
          if (!skipping) report.hiddenNotes.push(`${file}: « ${t} »`);
          skipping = true;
          pending = null;
          continue;
        }
        if (skipping) continue;
        if (node.depth === 1 || /^Étape/.test(t)) { out.push(node); pending = null; }
        else pending = node; // titre ordinaire (ex. « Pour aller plus loin ») : gardé seulement si du texte affiché suit
        continue;
      }
      if (skipping) continue;
      if (node.type === 'blockquote') {
        if (pending) { out.push(pending); pending = null; }
        out.push(...node.children);
      } else hidden++;
    }
    report.hidden = (report.hidden || 0) + hidden;
    tree.children = out;
  };
}

/** Liens vers les fichiers du dépôt : .md des chapitres -> pages du site ; autres liens relatifs -> texte seul. */
function rewriteLinks(tree) {
  visit(tree, 'link', (node, index, parent) => {
    const url = node.url || '';
    if (/^(https?:|mailto:|#|\/)/.test(url)) return;
    const m = url.match(/(?:^|\/)chapitres\/([\w-]+)\.md(#.*)?$/);
    if (m) { node.url = `/chapitres/${m[1]}/${m[2] || ''}`; return; }
    if (/(^|\/)debats\.md(#.*)?$/.test(url)) { node.url = '/debats/'; return; }
    const r = url.match(/(?:^|\/)reponses\/([a-z0-9-]+)\.md(#.*)?$/);
    if (r) { node.url = `/reponses/${r[1]}/${r[2] || ''}`; return; }
    report.relativeLinksDropped++;
    parent.children.splice(index, 1, ...node.children);
    return index;
  });
}

function typographyPlugin() {
  return (tree) => visit(tree, 'text', (node) => { node.value = typography(node.value); });
}

function headingIds(headings) {
  return () => (tree) => {
    const seen = new Map();
    visit(tree, 'heading', (node) => {
      let id = slugify(textOf(node).replace(TOKEN, '')) || 'section';
      const n = seen.get(id) || 0;
      seen.set(id, n + 1);
      if (n) id += `-${n}`;
      node.data = { ...(node.data || {}), hProperties: { id } };
      headings.push({ depth: node.depth, id, text: textOf(node).replace(TOKEN, '') });
    });
  };
}

/** Remplace les jetons par des renvois numérotés vers la liste « Chiffres et sources » en bas de page.
 *  Sans JavaScript, le renvoi est un simple lien vers la liste ; avec, il ouvre un encadré sous le paragraphe. */
function chipPlugin(chips, used) {
  return () => (tree) => visit(tree, 'text', (node, index, parent) => {
    if (!TOKEN.test(node.value)) return;
    TOKEN.lastIndex = 0;
    const parts = [];
    let last = 0;
    for (const m of node.value.matchAll(TOKEN)) {
      // Espace insécable avant le renvoi : le numéro ne passe jamais seul à la ligne.
      if (m.index > last) parts.push({ type: 'text', value: node.value.slice(last, m.index).replace(/\s+$/, NBSP) });
      const entry = chips[Number(m[1])];
      if (!used.has(entry.key)) used.set(entry.key, { n: used.size + 1, entry });
      const n = used.get(entry.key).n;
      report.chipsDisplayed++;
      parts.push({ type: 'link', url: `#pastille-${n}`, children: [{ type: 'text', value: String(n) }],
        data: { hName: 'a', hProperties: { href: `#pastille-${n}`, className: ['pastille'], 'aria-label': `Chiffre et source n° ${n}`, 'data-n': String(n), 'data-chip': entry.key } } });
      last = m.index + m[0].length;
    }
    if (last < node.value.length) parts.push({ type: 'text', value: node.value.slice(last) });
    parent.children.splice(index, 1, ...parts);
    return index + parts.length;
  });
}

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const KIND_LABEL = { fig: 'chiffre', yard: 'étalon', prop: 'proposition', src: 'source', calc: 'calcul', quiz: 'quiz' };

/** Liste « Chiffres et sources », repliable. Ouverte dans le HTML (lisible sans JavaScript) ; le script la replie. */
function sourcesList(used) {
  if (!used.size) return '';
  const items = [...used.values()].map(({ n, entry: e }) => {
    const year = e.year && !String(e.label).includes(e.year) ? ` <span class="cs-y">(${esc(typography(String(e.year)))})</span>` : '';
    const value = e.value ? `<p class="cs-v"><span class="num">${esc(e.value)}</span></p>` : '';
    const srcText = e.source ? typography(String(e.source)) : '';
    const src = e.url
      ? `<a href="${esc(e.url)}" rel="noopener" target="_blank">${esc(srcText || 'Document')}<span class="visually-hidden"> (nouvel onglet)</span> ↗</a>`
      : esc(srcText);
    const units = otherUnits(e.raw);
    return `<li id="pastille-${n}"><span class="cs-n" aria-hidden="true">${n}</span><div class="cs-body">`
      + `<span class="cs-kind">${esc(KIND_LABEL[e.kind] || e.kind)}</span>${value}<p class="cs-l">${esc(typography(frText(String(e.label))))}${year}</p>`
      + (units ? `<p class="cs-u">${esc(typography(units))}</p>` : '')
      + (src ? `<p class="cs-s">${esc(e.sourcePrefix || 'Source')}${NBSP}: ${src}</p>` : '') + `</div></li>`;
  });
  const count = `${used.size} renvoi${used.size > 1 ? 's' : ''}`;
  return `<section class="sources-wrap" aria-labelledby="sources-titre"><h2 id="sources-titre" class="sources-title">Chiffres et sources</h2>`
    + `<details class="sources" id="chiffres-et-sources" open><summary><span class="when-closed">Afficher les ${count}</span><span class="when-open">Masquer les ${count}</span></summary>`
    + `<ol aria-labelledby="sources-titre">${items.join('')}</ol></details></section>`;
}

function renderFile(file, mode) {
  const raw = fs.readFileSync(path.join(SITE_DIR, file), 'utf8').replace(FRONT_MATTER, '');
  const chips = [];
  const errors = [];
  const used = new Map();
  const headings = [];
  const masked = maskChips(raw, file, chips, errors);
  let html = '';
  if (!errors.length) {
    const proc = unified()
      .use(remarkParse)
      .use(remarkGfm)
      .use(() => editorialFilter(file, mode))
      .use(() => rewriteLinks)
      .use(typographyPlugin)
      .use(headingIds(headings))
      .use(chipPlugin(chips, used))
      .use(remarkRehype)
      .use(rehypeStringify);
    html = String(proc.processSync(masked));
  }
  return { html, sourcesHtml: errors.length ? '' : sourcesList(used), errors, headings, used };
}

const decodeEntities = (s) => s.replace(/&#x([0-9a-f]+);/gi, (m, h) => String.fromCodePoint(parseInt(h, 16)))
  .replace(/&#(\d+);/g, (m, d) => String.fromCodePoint(Number(d))).replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
const decode = (s) => s.replace(/&#x27;/g, '’').replace(/&quot;/g, '"').replace(/&lt;/g, '<').replace(/&gt;/g, '>').replace(/&amp;/g, '&');
/** Texte brut d'un fragment HTML rendu, sans les renvois numérotés. */
export function plainText(html) {
  return decode(html.replace(/<a [^>]*class="pastille"[^>]*>[\s\S]*?<\/a>/g, '').replace(/<[^>]+>/g, ''))
    .replace(/[ \t\r\n]+/g, ' ').replace(/[ \u00a0\u202f]+([.,)])/g, '$1').trim(); // garde les autres espaces insécables
}

/** Premier titre de niveau 1 retiré du corps (affiché dans l'en-tête de page). */
function pullTitle(html) {
  const m = html.match(/^\s*<h1[^>]*>([\s\S]*?)<\/h1>\s*/);
  return m ? { titleHtml: m[1], body: html.slice(m[0].length) } : { titleHtml: '', body: html };
}

/** Page de réponse : titre retiré (affiché à part), « En bref » isolé, sections coupées aux titres de niveau 2. */
function splitAnswer(html, file, errors) {
  let body = html.replace(/^\s*<h1[^>]*>[\s\S]*?<\/h1>\s*/, '');
  let brief = null;
  const m = body.match(/^<p><strong>En bref\.?<\/strong>\s*([\s\S]*?)<\/p>\s*/);
  if (m) { brief = m[1]; body = body.slice(m[0].length); }
  else errors.push(`${file}: paragraphe « En bref. » absent sous le titre`);
  const chunks = body.split(/(?=<h2 id=")/);
  const sections = [];
  let intro = '';
  for (const c of chunks) {
    const h = c.match(/^<h2 id="([^"]+)">([\s\S]*?)<\/h2>\s*/);
    if (!h) { intro += c; continue; }
    sections.push({ id: h[1], titleHtml: h[2], title: plainText(h[2]), html: c.slice(h[0].length) });
  }
  if (intro.trim()) sections.unshift({ id: 'introduction', titleHtml: '', title: '', html: intro });
  return { brief, briefText: brief ? plainText(brief) : '', sections };
}

/** Réponse en une ligne pour les cartes : phrases entières du « En bref » tant que le total reste court. */
function summaryOf(text, max = 200) {
  if (!text) return '';
  // Coupe après . ! ? suivis d'une majuscule ; pas après une initiale (« P. Aghion »).
  const sentences = text.split(/(?<=(?<![\s(][A-Z])[.!?…])\s+(?=[A-ZÀÂÉÈÊÎÔÛÇ«])/u);
  let out = sentences[0];
  for (const s2 of sentences.slice(1)) {
    if ((out + ' ' + s2).length > max) break;
    out += ' ' + s2;
  }
  if (out.length > max + 40) {
    const cut = out.slice(0, max);
    out = cut.slice(0, cut.lastIndexOf(' ')).replace(/[\s,;:]+$/, '') + '…';
  }
  return out;
}

// Métadonnées des pages de réponse : commentaire « <!-- page … --> » en tête de fichier (05-pages-de-reponse.md §1).
const ANSWER_META = /^\s*<!--\s*page\b([\s\S]*?)-->/;
const splitList = (v) => (v || '').split(/[\s,]+/).filter(Boolean);

function parseAnswerMeta(file) {
  const raw = fs.readFileSync(path.join(SITE_DIR, file), 'utf8');
  const m = raw.match(ANSWER_META);
  if (!m) return null;
  const meta = {};
  for (const line of m[1].split('\n')) {
    const kv = line.match(/^\s*([a-z_]+)\s*:\s*(.*?)\s*$/);
    if (kv) meta[kv[1]] = kv[2];
  }
  return meta;
}

/** Pages de réponse (fr/site/reponses/*.md, sauf les modèles « _*.md ») ; aucune page = liste vide. */
function renderAnswers(errors) {
  const dir = path.join(SITE_DIR, 'reponses');
  if (!fs.existsSync(dir)) return [];
  const files = fs.readdirSync(dir).filter((f) => f.endsWith('.md') && !f.startsWith('_')).sort();
  return files.map((f) => {
    const file = path.join('reponses', f);
    const slug = f.replace(/\.md$/, '');
    const meta = parseAnswerMeta(file);
    if (!meta) errors.push(`${file}: commentaire <!-- page … --> absent en tête de fichier`);
    else if (meta.slug !== slug) errors.push(`${file}: slug « ${meta.slug ?? ''} » différent du nom du fichier`);
    const r = renderFile(file, 'answer');
    errors.push(...r.errors);
    let montant = null;
    if (meta?.montant) {
      const res = resolveAmount(meta.montant);
      if (!res.ok) errors.push(`${file}: montant « ${meta.montant} » : ${res.error}`);
      else montant = res.entry;
    }
    const h1 = r.headings.find((h) => h.depth === 1);
    const parts = r.html ? splitAnswer(r.html, file, errors) : { brief: null, briefText: '', sections: [] };
    // Montant de la carte et de la barre : l'identifiant `montant:` s'il a une valeur en Md€ citée dans le résumé ;
    // sinon les pastilles « part du déficit » du « En bref » (le chiffre que la page affiche vraiment).
    const summary = summaryOf(parts.briefText);
    const briefCalcs = [...(parts.brief || '').matchAll(/data-chip="calc:([^"]*)"/g)].map((m) => decodeEntities(m[1]));
    const mentions = (t, x) => textMentions(t, x.low) && textMentions(t, x.high);
    let amount = meta?.montant ? amountOf(meta.montant) : null;
    let kept = null; // montant cité dans le « En bref » mais pas dans le résumé : gardé faute de mieux
    if (amount && !mentions(summary, amount)) {
      kept = mentions(parts.briefText, amount) ? amount : null;
      if (!kept) report.warnings.push(`${file}: montant « ${meta.montant} » (${amount.textBare}) absent du « En bref » ; repli sur la part du déficit`);
      amount = null;
    }
    let montantN = meta?.montant ? [...r.used.values()].find((u) => u.entry.id === meta.montant)?.n ?? null : null;
    if (!amount && briefCalcs.length) {
      amount = amountFromShareCalcs(briefCalcs, meta?.montant);
      const firstShare = [...r.used.values()].find((u) => u.entry.kind === 'calc' && briefCalcs.includes(u.entry.id) && /deficit_2025_eur_bn/.test(u.entry.id));
      if (amount && !(amount.id && [...r.used.values()].some((u) => u.entry.id === amount.id))) montantN = firstShare?.n ?? montantN;
      else if (amount) montantN = [...r.used.values()].find((u) => u.entry.id === amount.id)?.n ?? montantN;
    }
    if (!amount && kept) amount = kept;
    return {
      slug,
      title: h1 ? h1.text : (meta?.phrase ? `« ${meta.phrase} »` : slug),
      phrase: meta?.phrase ?? null,
      sujets: splitList(meta?.sujets).map((s) => ({ slug: s, label: typography(subjectLabel(s)) })),
      leviers: splitList(meta?.levier),
      debats: splitList(meta?.debats),
      montant,
      montantId: meta?.montant || null,
      montantN,
      amount,
      brief: parts.brief,
      briefText: parts.briefText,
      summary,
      sections: parts.sections,
      sourcesHtml: r.sourcesHtml,
      html: r.html + r.sourcesHtml,
      headings: r.headings,
    };
  });
}

let cache;
/** Rend tous les contenus ; échoue (build) à la moindre pastille inconnue. */
export function renderAll() {
  if (cache) return cache;
  const chapDir = path.join(SITE_DIR, 'chapitres');
  const files = fs.readdirSync(chapDir).filter((f) => f.endsWith('.md')).sort();
  const errors = [];
  const chapters = files.map((f) => {
    const r = renderFile(path.join('chapitres', f), 'chapter');
    errors.push(...r.errors);
    const slug = f.replace(/\.md$/, '');
    const h1 = r.headings.find((h) => h.depth === 1);
    const title = h1 ? h1.text : slug;
    const minutes = r.html.match(/Durée de lecture\s*:\s*environ (\d+)\s*minutes/i)?.[1] ?? null;
    const { titleHtml, body } = pullTitle(r.html);
    const html = body.replace(/<p>Durée de lecture\s*:\s*environ \d+\s*minutes\.?<\/p>\s*/i, '');
    return { slug, title, titleHtml, minutes, html, sourcesHtml: r.sourcesHtml, headings: r.headings };
  });
  const debatsR = renderFile('debats.md', 'page');
  const debatsT = pullTitle(debatsR.html);
  const debats = { ...debatsR, html: debatsT.body, titleHtml: debatsT.titleHtml, title: plainText(debatsT.titleHtml) };
  errors.push(...debats.errors);
  const answers = renderAnswers(errors);
  if (errors.length) {
    throw new Error(`Pastilles invalides (${errors.length}) :\n  ` + errors.join('\n  '));
  }
  console.log(`[réponses] ${answers.length} page(s) de réponse`);
  console.log(`[pastilles] ${report.chips} pastilles vérifiées (${report.chipsDisplayed} affichées), 0 inconnue ; ${report.hiddenNotes.length} section(s) de notes masquée(s) ; ${report.relativeLinksDropped} lien(s) relatif(s) vers le dépôt réduit(s) à leur texte`);
  for (const w of report.warnings) console.warn(`[pastilles] avertissement : ${w}`);
  if (unitStats.approximated.size) console.warn(`[pastilles] unités sans traduction exacte : ${[...unitStats.approximated].map(([u, n]) => `${u} (${n})`).join(' ; ')}`);
  cache = { chapters, answers, debats: { html: debats.html, titleHtml: debats.titleHtml, title: debats.title, sourcesHtml: debats.sourcesHtml, headings: debats.headings }, report, unitStats, dataMeta };
  return cache;
}
