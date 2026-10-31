// Chargement de platform/data/*.json et résolution des pastilles ([[type:id]]).
// La grammaire reprend celle de platform/data/validate.py (CHIP, CALC_ID, pools par type).
import fs from 'node:fs';
import path from 'node:path';
import { formatValue, formatNumber, decimalsOf, typography, NBSP } from './format.mjs';

// Les scripts npm s'exécutent depuis site/ : le dépôt est le dossier parent.
export const REPO = path.resolve(process.cwd(), '..');
const DATA = path.join(REPO, 'platform', 'data');
const load = (n) => JSON.parse(fs.readFileSync(path.join(DATA, n), 'utf8'));

const figuresJson = load('figures.json');
const yardJson = load('yardsticks.json');
const propsJson = load('proposals.json');
const sourcesJson = load('sources.json');
const quizJson = load('quiz.json');

const figs = new Map(figuresJson.figures.map((f) => [f.id, f]));
const tables = new Map((figuresJson.rating_tables || []).map((t) => [t.id, t]));
const yards = new Map(yardJson.yardsticks.map((y) => [y.id, y]));
const params = new Map((yardJson.parameters || []).map((p) => [p.id, p]));
const props = new Map(propsJson.proposals.map((p) => [p.id, p]));
const sources = new Map(Object.entries(sourcesJson.sources));
const quiz = new Map([
  ...quizJson.questions.map((q) => [q.id, q]),
  ...quizJson.misperceptions.map((m) => [m.id, m]),
]);

// Identifiants utilisables dans [[calc:]] : figures, étalons, paramètres, bornes __low/__high.
const calcPool = new Set([...figs.keys(), ...yards.keys(), ...params.keys()]);
for (const f of figs.values()) if (f.range) { calcPool.add(`${f.id}__low`); calcPool.add(`${f.id}__high`); }

export const CHIP = /\[\[([a-z][a-z-]*):([^\]]*)\]\]/g;
const CALC_ID = /(?<![\w:*])(?:yd:|yard:|fig:)?([a-z][a-z0-9]*(?:_(?:[a-z0-9]+|\*))+)(?![\w*(])/g;

function wildcardMatch(pattern) {
  const re = new RegExp('^' + pattern.replace(/[.+?^${}()|[\]\\]/g, '\\$&').replace(/\*/g, '[a-z0-9_]+') + '$');
  return [...calcPool].some((k) => re.test(k));
}

const firstUrl = (f) => f.url || sources.get(f.source_id)?.urls?.[0] || null;

/**
 * Résout une pastille. Retourne { ok: true, entry } ou { ok: false, error }.
 * entry : { key, kind, id, label, value, source, url, note }
 */
export function resolveChip(kind, rawRef) {
  let ref = rawRef.trim();
  let context = false;
  if (kind !== 'calc' && ref.includes('|')) { // [[fig:id|contexte]] : l'identifiant ne marque pas un nombre affiché
    context = ref.split('|').slice(1).join('|').trim() === 'contexte';
    ref = ref.split('|')[0].trim();
  } else if (kind === 'calc' && /\|\s*contexte\s*$/.test(ref)) {
    context = true;
    ref = ref.replace(/\|\s*contexte\s*$/, '').trim();
  }
  const key = `${kind}:${ref}`;
  const base = { key, kind, id: ref, context };

  if (kind === 'fig-a-creer') return { ok: false, error: `espace réservé [[fig-a-creer:${ref}]] encore présent` + (figs.has(ref) ? ` (l’id existe : utiliser [[fig:${ref}]])` : '') };

  if (kind === 'fig') {
    const f = figs.get(ref);
    if (f) {
      const v = f.value !== null && f.value !== undefined ? f.value : f.range;
      const fs_ = figureSource(ref);
      const srcText = fs_ ? `${fs_.name}${fs_.date ? `, ${fs_.date}` : ''}` : null;
      return { ok: true, entry: { ...base, label: f.label_fr, value: v === null ? null : formatValue(v, f.unit, f.display_decimals ?? undefined) + (f.value != null && f.range ? ` (fourchette${NBSP}: ${formatValue(f.range, f.unit)})` : ''), year: f.year, source: srcText, url: firstUrl(f), status: f.status, raw: rawOf(f, ref) } };
    }
    const t = tables.get(ref);
    if (t) return { ok: true, entry: { ...base, label: t.label_fr, value: null, source: `Tableau de notes${NBSP}: ` + t.figure_ids.map((i) => figs.get(i)?.label_fr || i).join(' ; '), url: null } };
    return { ok: false, error: `[[fig:${ref}]] ne se résout pas` + (yards.has(ref) || params.has(ref) ? ' (c’est un étalon : utiliser [[yard:…]])' : '') };
  }

  if (kind === 'yard' || kind === 'yd') {
    const y = yards.get(ref) || params.get(ref);
    if (!y) return { ok: false, error: `[[${kind}:${ref}]] ne se résout pas` + (figs.has(ref) ? ' (c’est une figure : utiliser [[fig:…]])' : '') };
    const value = y.value === null || y.value === undefined ? null : formatValue(y.value, y.unit, y.display_decimals ?? (y.value % 1 === 0 ? 0 : decimalsOf(y.value)));
    return { ok: true, warn: kind === 'yd' ? `préfixe non canonique [[yd:${ref}]], utiliser [[yard:${ref}]]` : null,
      entry: { ...base, key: `yard:${ref}`, kind: 'yard', label: y.label_fr, value, source: y.formula ? `Calcul du site${NBSP}: ${readableFormula(y.formula)}` : 'Paramètre du site', url: null, raw: rawOf(y) } };
  }

  if (kind === 'prop') {
    const p = props.get(ref);
    if (!p) return { ok: false, error: `[[prop:${ref}]] ne se résout pas` };
    const c = p.claimed || {};
    const claimed = c.central != null ? formatValue(c.central, 'EUR bn') : c.low != null && c.high != null ? formatValue({ low: c.low, high: c.high }, 'EUR bn') : null;
    const ests = (p.estimates || []).filter((e) => e.central != null || (e.low != null && e.high != null))
      .map((e) => `${frAuthor(e)}${NBSP}: ${e.central != null ? formatValue(e.central, 'EUR bn') : formatValue({ low: e.low, high: e.high }, 'EUR bn')}`);
    const srcIds = [...new Set((p.estimates || []).flatMap((e) => e.source_ids || []))];
    const url = srcIds.map((i) => sources.get(i)?.urls?.[0]).find(Boolean) || null;
    return { ok: true, entry: { ...base, label: frText(p.measure_fr), value: claimed ? `chiffrage annoncé${NBSP}: ${claimed}` : null, source: ests.join(' ; ') || `Chiffrages indépendants${NBSP}: voir la page Débats`, url } };
  }

  if (kind === 'src') {
    const s = sources.get(ref);
    if (!s) return { ok: false, error: `[[src:${ref}]] ne se résout pas` };
    if (s.type === 'research_file' || /^\d{2}-[\w-]+\.md\b/.test(s.title || '')) {
      return { ok: true, entry: { ...base, label: 'Estimation du site (synthèse de plusieurs études)', value: null, source: null, url: null } };
    }
    const title = [frInstitution(s.institution), cleanTitle(s.title)].filter(Boolean).join(', ');
    const date = frDate(s.date);
    const url = s.urls?.[0] || null;
    return { ok: true, entry: { ...base, label: title, value: null, source: url ? (date ? `Document du ${date}` : 'Document') : date, sourcePrefix: url ? 'Lien' : 'Date', url } };
  }

  if (kind === 'quiz') {
    if (!quiz.has(ref)) return { ok: false, error: `[[quiz:${ref}]] ne se résout pas` };
    return { ok: true, entry: { ...base, label: `Question ou perception ${ref} du quiz`, value: null, source: 'Questions du quiz du site', url: null } };
  }

  if (kind === 'calc') {
    const unknown = [...new Set([...ref.matchAll(CALC_ID)].map((m) => m[1]).filter((i) => !calcPool.has(i) && !(i.includes('*') && wildcardMatch(i))))];
    if (unknown.length) return { ok: false, error: `[[calc:]] utilise des identifiants inconnus : ${unknown.join(', ')}` };
    const names = [...new Set([...ref.matchAll(CALC_ID)].map((m) => m[1]))]
      .map((id) => frText(figs.get(id)?.label_fr || yards.get(id)?.label_fr || params.get(id)?.label_fr)).filter(Boolean);
    return { ok: true, entry: { ...base, key: `calc:${ref}`, label: `Calcul du site${NBSP}: ${readableFormula(ref)}`, value: null,
      source: names.length ? names.join(' ; ') : null, sourcePrefix: 'Données utilisées', url: null } };
  }

  return { ok: false, error: `type de pastille inconnu [[${kind}:${ref}]]` };
}

export const dataMeta = { figures: figs.size, yardsticks: yards.size, proposals: props.size, sources: sources.size };

/** Montant d'une page de réponse (`montant:` du commentaire <!-- page -->) : figure, étalon, paramètre ou proposition. */
export function resolveAmount(id) {
  if (figs.has(id)) return resolveChip('fig', id);
  if (yards.has(id) || params.has(id)) return resolveChip('yard', id);
  if (props.has(id)) return resolveChip('prop', id);
  return { ok: false, error: 'identifiant absent de figures.json, yardsticks.json et proposals.json' };
}

// ---------------------------------------------------------------------------
// Accès aux valeurs brutes pour les composants (barre de fourchette, cartes, accueil).
// Aucun nombre n'est écrit en dur dans les pages : tout est lu ici, depuis platform/data/.

/** Figure brute de figures.json (ou null). */
export const figure = (id) => figs.get(id) || null;

const MONTHS = { jan: 'janvier', feb: 'février', mar: 'mars', apr: 'avril', may: 'mai', jun: 'juin', june: 'juin',
  jul: 'juillet', july: 'juillet', aug: 'août', sep: 'septembre', sept: 'septembre', oct: 'octobre', nov: 'novembre', dec: 'décembre' };
/** « 21 Oct 2026 » -> « 21 octobre 2026 » ; « Oct 2026 » -> « octobre 2026 » ; « 2026-10-25 » -> « 25 octobre 2026 ». Sinon null. */
export function frDate(s) {
  if (!s) return null;
  const first = String(s).split(';')[0].trim();
  let m = first.match(/^(\d{1,2})\s+([A-Za-z]+)\.?\s+(\d{4})$/);
  if (m && MONTHS[m[2].toLowerCase()]) return `${m[1] === '1' ? '1er' : m[1]} ${MONTHS[m[2].toLowerCase()]} ${m[3]}`;
  m = first.match(/^([A-Za-z]+)\.?\s+(\d{4})$/);
  if (m && MONTHS[m[1].toLowerCase()]) return `${MONTHS[m[1].toLowerCase()]} ${m[2]}`;
  m = first.match(/^(\d{4})-(\d{2})-(\d{2})$/);
  if (m) { const k = ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct', 'nov', 'dec'][Number(m[2]) - 1]; return k ? `${Number(m[3]) === 1 ? '1er' : Number(m[3])} ${MONTHS[k]} ${m[1]}` : null; }
  if (/^\d{4}$/.test(first)) return first;
  return null;
}

// Noms d'organisme lisibles pour les domaines des liens de source (repli : le domaine lui-même).
const HOSTS = {
  'ec.europa.eu': 'Eurostat', 'ccomptes.fr': 'Cour des comptes', 'cor-retraites.fr': 'Conseil d’orientation des retraites (COR)',
  'assemblee-nationale.fr': 'Assemblée nationale', 'senat.fr': 'Sénat', 'insee.fr': 'Insee', 'institutmontaigne.org': 'Institut Montaigne',
  'vie-publique.fr': 'Vie publique', 'oecd.org': 'OCDE', 'budget.gouv.fr': 'Direction du budget', 'economie.gouv.fr': 'Ministère de l’Économie',
  'banque-france.fr': 'Banque de France', 'imf.org': 'FMI', 'fipeco.fr': 'Fipeco', 'hcfp.fr': 'Haut Conseil des finances publiques',
  'strategie.gouv.fr': 'France Stratégie', 'cae-eco.fr': 'Conseil d’analyse économique', 'ipp.eu': 'Institut des politiques publiques',
  'ofce.sciences-po.fr': 'OFCE', 'securite-sociale.fr': 'Sécurité sociale', 'legifrance.gouv.fr': 'Légifrance',
};
function hostLabel(url) {
  try {
    const h = new URL(url).hostname.replace(/^www\./, '');
    const k = Object.keys(HOSTS).find((d) => h === d || h.endsWith('.' + d));
    return k ? HOSTS[k] : h;
  } catch { return null; }
}

/** Source lisible d'une figure : { name, date, url } ; synthèse interne si la source est un dossier de recherche. */
export function figureSource(id) {
  const f = figs.get(id);
  if (!f) return null;
  const s = sources.get(f.source_id);
  if (s?.type === 'research_file') {
    const n = (s.research_file || '').match(/^(\d+)/)?.[1];
    return { name: 'estimation du site (synthèse de plusieurs études)', date: null, url: null, internal: true };
  }
  const url = firstUrl(f);
  const name = frInstitution(s?.institution) || (url ? hostLabel(url) : null) || 'voir «\u202fChiffres et sources\u202f»';
  return { name, date: frDate(f.vintage) || frDate(s?.date), url, internal: false };
}

/**
 * Montant d'une page de réponse, sous forme numérique : figure ou étalon en milliards d'euros,
 * valeur positive ou fourchette. Les propositions (chiffrages multiples) et les soldes négatifs
 * ne donnent pas de montant de mesure : retourne null.
 */
export function amountOf(id) {
  const f = figs.get(id);
  const y = f ? null : yards.get(id) || params.get(id);
  const d = f || y;
  if (!d || !String(d.unit || '').startsWith('EUR bn')) return null;
  let low, high;
  if (d.value !== null && d.value !== undefined) { low = high = d.value; }
  else if (d.range) { low = d.range.low; high = d.range.high; }
  else return null;
  let negative = false;
  if (low < 0 && high < 0) { negative = true; [low, high] = [-high, -low]; } // solde négatif : montant du déficit
  if (!(low > 0) || !(high > 0)) return null;
  return makeAmount({
    id, origin: f ? 'fig' : 'yard', low, high, negative,
    label: frText(negative ? d.label_fr.replace(/^Solde\b/, 'Déficit') : d.label_fr), year: f?.year ?? null,
    source: f ? figureSource(id) : { name: 'calcul du site', date: null, url: null, internal: true, formula: d.formula ? readableFormula(d.formula) : undefined },
  });
}

/** Une décimale au plus, sans zéro inutile (« 12 », « 26,5 », « 1,3 »). */
const short = (x) => formatNumber(x, Math.round(x * 10) % 10 === 0 ? 0 : 1);

function makeAmount(a) {
  const bare = a.low === a.high ? `${short(a.low)}${NBSP}Md€` : `${short(a.low)} à ${short(a.high)}${NBSP}Md€`;
  return { ...a, mid: (a.low + a.high) / 2, unit: 'EUR bn', text: bare, textBare: bare };
}

// Valeurs numériques des identifiants (fourchette = [bas, haut]) pour évaluer un [[calc:]].
function valuesOf(id) {
  const m = id.match(/^(.*)__(low|high)$/);
  const d = figs.get(m ? m[1] : id) || yards.get(id) || params.get(id);
  if (!d) return null;
  if (m && d.range) return [d.range[m[2]], d.range[m[2]]];
  if (d.value !== null && d.value !== undefined) return [d.value, d.value];
  if (d.range) return [d.range.low, d.range.high];
  return null;
}

/** Évalue une expression arithmétique de pastille [[calc:]] (identifiants, nombres, + − × ÷, parenthèses). [bas, haut] ou null. */
function evalExpr(expr) {
  let ok = true;
  const ids = [];
  const sub = (k) => expr.replace(CALC_ID, (m, id) => {
    const v = valuesOf(id);
    if (!v) { ok = false; return '0'; }
    ids.push(id);
    return `(${v[k]})`;
  }).replace(/(\d),(\d)/g, '$1.$2').replace(/×/g, '*').replace(/÷/g, '/').replace(/−/g, '-');
  const lo = sub(0), hi = sub(1);
  if (!ok || !/^[\d\s.+\-*/()]+$/.test(lo)) return null;
  try {
    const a = Function(`"use strict";return (${lo});`)(), b = Function(`"use strict";return (${hi});`)();
    return Number.isFinite(a) && Number.isFinite(b) ? { low: Math.min(a, b), high: Math.max(a, b), ids: [...new Set(ids)] } : null;
  } catch { return null; }
}

/**
 * Montant tiré des pastilles « part du déficit » d'un « En bref » ([[calc:X / deficit_2025_eur_bn * 100 = …]]) :
 * le numérateur X est évalué depuis platform/data/. Sert quand l'identifiant `montant:` n'a pas de montant numérique
 * (proposition aux chiffrages multiples) ou quand il ne correspond pas au chiffre du résumé.
 */
export function amountFromShareCalcs(refs, montantId) {
  let low = Infinity, high = -Infinity;
  const ids = new Set();
  for (const ref of refs) {
    for (const part of ref.split(';')) {
      const m = part.match(/^\s*(.+?)\s*\/\s*(?:fig:)?deficit_2025_eur_bn\b/);
      if (!m) continue;
      const v = evalExpr(m[1]);
      if (!v) continue;
      low = Math.min(low, v.low); high = Math.max(high, v.high);
      v.ids.forEach((i) => ids.add(i));
    }
  }
  if (!(low > 0) || !(high > 0)) return null;
  const only = ids.size === 1 ? [...ids][0] : null;
  let source;
  if (only && figs.has(only)) source = figureSource(only);
  else if (ids.size) source = { name: 'calcul du site', date: null, url: null, internal: true, formula: [...ids].map((i) => frText(figs.get(i)?.label_fr || yards.get(i)?.label_fr || i)).join(' + ') };
  else source = propSource(montantId);
  const label = only ? (figs.get(only)?.label_fr || yards.get(only)?.label_fr) : (props.get(montantId)?.measure_fr ? frText(props.get(montantId).measure_fr) : null);
  return makeAmount({ id: only || montantId, origin: 'calc', low, high, negative: false, label: label || '', year: only ? figs.get(only)?.year ?? null : null, source });
}

function propSource(id) {
  const p = props.get(id);
  if (!p) return { name: 'calcul du site', date: null, url: null, internal: true };
  const ests = p.estimates || [];
  if (ests.some((e) => e.computed_by_us)) return { name: 'estimation du site (synthèse de plusieurs études)', date: null, url: null, internal: true };
  const names = [...new Set(ests.filter((e) => !/non-institutional|flagged/i.test(e.author)).map(frAuthor))];
  if (p.claimed) names.unshift('chiffrage annoncé par le programme');
  return { name: names.join(' ; ') || 'voir «\u202fChiffres et sources\u202f»', date: null, url: null, internal: false };
}

/** Le résumé de la carte cite-t-il ce nombre (à la précision des données, à une décimale ou arrondi) ? */
export function textMentions(text, x) {
  const forms = new Set([formatNumber(x, decimalsOf(x), { grouping: false }), formatNumber(x, 1), formatNumber(x, 0), short(x)]);
  const flat = text.replace(/[\u202f\u00a0]/g, '');
  return [...forms].some((f) => new RegExp(`(?<![\\d,])${f.replace(',', ',')}(?![\\d]|,\\d)`).test(flat));
}

// ---------------------------------------------------------------------------
// Formules lisibles et textes anglais du jeu de données traduits pour l'affichage.

function fmtId(id) {
  const v = valuesOf(id);
  if (!v) return id;
  const d = figs.get(id) || yards.get(id) || params.get(id);
  const dec = (x) => Math.min(d?.display_decimals ?? decimalsOf(x), 2);
  return v[0] === v[1] ? formatNumber(v[0], dec(v[0])) : `(${formatNumber(v[0], dec(v[0]))} à ${formatNumber(v[1], dec(v[1]))})`;
}

/** « 12 / deficit_2025_eur_bn * 100 = 7,9 » -> « 12 ÷ 151,6 = 7,9 % » : identifiants remplacés par leurs valeurs. */
export function readableFormula(ref) {
  let pct = false;
  return ref.split(/\s*;\s*/).map((seg) => {
    let t = seg.replace(CALC_ID, (m, id) => fmtId(id)).replace(/(\d)\.(\d)/g, '$1,$2');
    if (/[*×]\s*100\s*=/.test(t)) { pct = true; t = t.replace(/\s*[*×]\s*100\s*=\s*(.+)$/, ' = $1 %'); }
    else if (pct && !t.includes('=')) t = `${t} %`;
    return t.replace(/\s*\/\s*/g, ' ÷ ').replace(/\s*\*\s*/g, ' × ').replace(/(\d) %/g, `$1${NBSP}%`).replace(/\s+/g, ' ').trim();
  }).join(' ; ');
}

const MONTH_EN = { Jan: 'janvier', Feb: 'février', Mar: 'mars', Apr: 'avril', May: 'mai', Jun: 'juin', June: 'juin', Jul: 'juillet', July: 'juillet',
  Aug: 'août', Sep: 'septembre', Oct: 'octobre', Nov: 'novembre', Dec: 'décembre', December: 'décembre' };
const AUTHOR_FR = {
  'Realized cost': 'coût constaté',
  'Observed (December 2025 down-payment)': 'constaté (acompte de décembre 2025)',
  'Expected 2026 (2026 Finance Act: 650 M)': 'attendu en 2026 (loi de finances pour 2026 : 650 M€)',
  'Senate inquiry report no. 807 (structural reform)': 'Sénat, rapport d’enquête n° 807 (réforme de structure)',
  '8% cut of all staff and running costs (not at constant missions)': 'baisse de 8 % des effectifs et du fonctionnement (sans garder toutes les missions)',
  'Cour des comptes (15 Mar 2024): 72 gross / 36 net over four years': 'Cour des comptes (15 mars 2024) : 72 brut, 36 net sur quatre ans',
  'francebudget.fr (non-institutional citizen simulator, flagged)': 'francebudget.fr (simulateur citoyen non institutionnel, à prendre avec prudence)',
  'Institut Montaigne 2022 (LFI 2022 version, pension schemes only, 2027)': 'Institut Montaigne 2022 (version LFI de 2022, régimes de retraite seuls, horizon 2027)',
  "LFI's own 2022 counter-costing of the 60/40 item": 'contre-chiffrage de LFI (2022) pour la mesure 60 ans et 40 annuités',
  'Senate benchmark': 'repère du Sénat',
  'Institut Montaigne (NFP package incl. a general return)': 'Institut Montaigne (programme du NFP, retour général compris)',
  'Senate inquiry (without abolishing the policies themselves)': 'commission d’enquête du Sénat (sans supprimer les politiques elles-mêmes)',
  'Cour des comptes RSPFP (15 Jul 2024)': 'Cour des comptes, RSPFP (15 juillet 2024)',
};
const INSTITUTION_FR = {
  'Government (info.gouv.fr)': 'Gouvernement (info.gouv.fr)',
  'International Monetary Fund (IMF)': 'Fonds monétaire international (FMI)',
  'Mission on public-finance transparency (Jaravel, Ragot, Tavernier, Valla), hosted by the IGF': 'Mission sur la transparence des finances publiques (Jaravel, Ragot, Tavernier, Valla), IGF',
  'A. Bozio and É. Wasmer (report to the Prime Minister)': 'A. Bozio et É. Wasmer (rapport au Premier ministre)',
  'C. Évin and P. Stefanini, with IGA and IGAS (government-commissioned)': 'C. Évin et P. Stefanini, avec l’IGA et l’IGAS (rapport commandé par le gouvernement)',
};

/** Petites traductions génériques : mois anglais, « EUR », « and ». */
export function frText(t) {
  if (!t) return t;
  return t
    .replace(/\b(\d{1,2}) (Jan|Feb|Mar|Apr|May|Jun|June|Jul|July|Aug|Sep|Oct|Nov|Dec|December) (\d{4})\b/g, (m, d, mo, y) => `${d === '1' ? '1er' : d} ${MONTH_EN[mo]} ${y}`)
    .replace(/\b(Jan|Feb|Mar|Apr|May|Jun|June|Jul|July|Aug|Sep|Oct|Nov|Dec|December) (\d{4})\b/g, (m, mo, y) => `${MONTH_EN[mo]} ${y}`)
    .replace(/\s*\((?:synthèse du |synthèse des )?fichiers? \d+[^)]*\)/g, '').replace(/\bEUR\/l\b/g, '€/l').replace(/\bMd EUR\b/g, 'Md€').replace(/\bEUR\b/g, '€');
}
function frAuthor(e) {
  const a = (e.author || '').trim();
  if (AUTHOR_FR[a]) return AUTHOR_FR[a];
  if (e.computed_by_us || /^Own\b/i.test(a)) return 'calcul du site';
  if (/^File \d+.*synthesis|^File \d+ §/i.test(a)) return 'estimation du site (synthèse de plusieurs études)';
  if (/^Government\b/.test(a)) return frText(a.replace(/^Government/, 'Gouvernement'));
  return frText(a);
}
function frInstitution(i) {
  if (!i) return null;
  if (INSTITUTION_FR[i]) return INSTITUTION_FR[i];
  return frText(i.replace(/\s*\(corrected[^)]*\)/g, '').replace(/^Government\b/, 'Gouvernement'));
}
function cleanTitle(t) {
  if (!t) return null;
  return t.split(/,\s*https?:|\s*\(local:|;\s*press coverage|\s*\(primary\b/)[0].trim();
}

/** Autres unités d'un montant en Md€ (fr/conception/01 §5) : part du déficit de référence, jours de dépense publique. */
export function otherUnits(raw) {
  if (!raw || raw.unit !== 'EUR bn' || raw.lo == null) return null;
  const D = figs.get('deficit_2025_eur_bn'), TE = figs.get('te_2025_eur_bn'), days = params.get('days_in_year')?.value ?? 365;
  if (!D || !TE) return null;
  const share = (x) => formatNumber((100 * x) / D.value, 1);
  const day = (x) => formatNumber((x * days) / TE.value, 1);
  const r = (f) => (raw.lo === raw.hi ? f(raw.lo) : `${f(raw.lo)} à ${f(raw.hi)}`);
  const dayWord = (raw.hi * days) / TE.value < 2 ? 'jour' : 'jours';
  const daysText = `${r(day)}${NBSP}${dayWord} de dépense publique de ${TE.year}`;
  if (raw.id === D.id) return `soit ${daysText} (calcul du site)`;
  return `soit ${r(share)}${NBSP}% du déficit public de ${D.year} et ${daysText} (calcul du site)`;
}
function rawOf(d, id = d.id) {
  if (!String(d.unit || '').match(/^EUR bn( per year)?$/)) return null;
  if (d.value != null) return { id, lo: Math.abs(d.value), hi: Math.abs(d.value), unit: 'EUR bn' };
  if (d.range) return { id, lo: d.range.low, hi: d.range.high, unit: 'EUR bn' };
  return null;
}

/** Déficit de référence des pages de réponse (fr/conception/01 §8.3). */
export function referenceDeficit() {
  const f = figs.get('deficit_2025_eur_bn');
  return { id: f.id, value: f.value, year: f.year, text: formatValue(f.value, f.unit, f.display_decimals ?? undefined), source: figureSource(f.id) };
}

/** Valeur formatée d'une figure (texte français, unité comprise). */
export function figureText(id) {
  const f = figs.get(id);
  if (!f || f.value === null || f.value === undefined) return null;
  return formatValue(f.value, f.unit, f.display_decimals ?? undefined);
}

// Libellés des sujets (« ### Sujet N : Libellé (`slug`) » dans fr/conception/04-sujets-et-objections.md).
let subjectMap;
export function subjectLabel(slug) {
  if (!subjectMap) {
    subjectMap = new Map();
    try {
      const t = fs.readFileSync(path.join(REPO, 'fr', 'conception', '04-sujets-et-objections.md'), 'utf8');
      for (const m of t.matchAll(/^###\s+Sujet\s+\d+\s*:\s*(.+?)\s*\(`([a-z0-9-]+)`\)\s*$/gm)) subjectMap.set(m[2], m[1]);
    } catch { /* fichier absent : on affiche le slug */ }
  }
  return subjectMap.get(slug) || slug;
}
