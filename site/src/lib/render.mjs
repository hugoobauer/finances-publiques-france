// Lecture de fr/site/ et rendu en HTML : filtrage éditorial, pastilles, typographie.
import fs from 'node:fs';
import path from 'node:path';
import { unified } from 'unified';
import remarkParse from 'remark-parse';
import remarkGfm from 'remark-gfm';
import remarkRehype from 'remark-rehype';
import rehypeStringify from 'rehype-stringify';
import { visit } from 'unist-util-visit';
import { REPO, CHIP, resolveChip, dataMeta } from './data.mjs';
import { typography, unitStats } from './format.mjs';

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

/** Chapitres : ne garder que le texte affiché (blocs « > »), avec leurs titres. Tout le reste est de la spécification. */
function editorialFilter(file, mode) {
  return (tree) => {
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

/** Remplace les jetons par des renvois numérotés « [n] » vers la liste des sources en bas de page. */
function chipPlugin(chips, used) {
  return () => (tree) => visit(tree, 'text', (node, index, parent) => {
    if (!TOKEN.test(node.value)) return;
    TOKEN.lastIndex = 0;
    const parts = [];
    let last = 0;
    for (const m of node.value.matchAll(TOKEN)) {
      if (m.index > last) parts.push({ type: 'text', value: node.value.slice(last, m.index) });
      const entry = chips[Number(m[1])];
      if (!used.has(entry.key)) used.set(entry.key, { n: used.size + 1, entry });
      const n = used.get(entry.key).n;
      report.chipsDisplayed++;
      parts.push({ type: 'link', url: `#pastille-${n}`, children: [{ type: 'text', value: String(n) }],
        data: { hName: 'a', hProperties: { href: `#pastille-${n}`, className: ['pastille'], title: entry.value ? `${entry.label} : ${entry.value}` : entry.label, 'data-chip': entry.key } } });
      last = m.index + m[0].length;
    }
    if (last < node.value.length) parts.push({ type: 'text', value: node.value.slice(last) });
    parent.children.splice(index, 1, ...parts);
    return index + parts.length;
  });
}

const esc = (s) => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

function sourcesList(used) {
  if (!used.size) return '';
  const items = [...used.values()].map(({ n, entry: e }) => {
    const head = e.value ? `<strong>${esc(e.value)}</strong> · ${esc(e.label)}` : esc(e.label);
    const src = e.url ? `<a href="${esc(e.url)}" rel="noopener">${esc(e.source || 'Source')}</a>` : esc(e.source || '');
    return `<li id="pastille-${n}"><span class="kind">${esc(e.kind)}</span> ${head}${e.year && !String(e.label).includes(e.year) ? ` (${esc(e.year)})` : ''}<br><span class="src">${src}</span></li>`;
  });
  return `<section class="sources" aria-labelledby="sources-titre"><h2 id="sources-titre">Chiffres et sources</h2><ol>${items.join('')}</ol></section>`;
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
    html += sourcesList(used);
  }
  return { html, errors, headings };
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
    return { slug, title, minutes, html: r.html, headings: r.headings };
  });
  const debats = renderFile('debats.md', 'page');
  errors.push(...debats.errors);
  if (errors.length) {
    throw new Error(`Pastilles invalides (${errors.length}) :\n  ` + errors.join('\n  '));
  }
  console.log(`[pastilles] ${report.chips} pastilles vérifiées (${report.chipsDisplayed} affichées), 0 inconnue ; ${report.hiddenNotes.length} section(s) de notes masquée(s) ; ${report.relativeLinksDropped} lien(s) relatif(s) vers le dépôt réduit(s) à leur texte`);
  for (const w of report.warnings) console.warn(`[pastilles] avertissement : ${w}`);
  if (unitStats.approximated.size) console.warn(`[pastilles] unités sans traduction exacte : ${[...unitStats.approximated].map(([u, n]) => `${u} (${n})`).join(' ; ')}`);
  cache = { chapters, debats: { html: debats.html, headings: debats.headings }, report, unitStats, dataMeta };
  return cache;
}
