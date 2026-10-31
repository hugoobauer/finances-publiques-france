// Chargement de platform/data/*.json et résolution des pastilles ([[type:id]]).
// La grammaire reprend celle de platform/data/validate.py (CHIP, CALC_ID, pools par type).
import fs from 'node:fs';
import path from 'node:path';
import { formatValue, decimalsOf } from './format.mjs';

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
      return { ok: true, entry: { ...base, label: f.label_fr, value: v === null ? null : formatValue(v, f.unit, f.display_decimals ?? undefined) + (f.value != null && f.range ? ` (fourchette : ${formatValue(f.range, f.unit)})` : ''), year: f.year, source: f.source, url: firstUrl(f), status: f.status } };
    }
    const t = tables.get(ref);
    if (t) return { ok: true, entry: { ...base, label: t.label_fr, value: null, source: 'Tableau de notes : ' + t.figure_ids.join(', '), url: null } };
    return { ok: false, error: `[[fig:${ref}]] ne se résout pas` + (yards.has(ref) || params.has(ref) ? ' (c’est un étalon : utiliser [[yard:…]])' : '') };
  }

  if (kind === 'yard' || kind === 'yd') {
    const y = yards.get(ref) || params.get(ref);
    if (!y) return { ok: false, error: `[[${kind}:${ref}]] ne se résout pas` + (figs.has(ref) ? ' (c’est une figure : utiliser [[fig:…]])' : '') };
    const value = y.value === null || y.value === undefined ? null : formatValue(y.value, y.unit, y.display_decimals ?? (y.value % 1 === 0 ? 0 : decimalsOf(y.value)));
    return { ok: true, warn: kind === 'yd' ? `préfixe non canonique [[yd:${ref}]], utiliser [[yard:${ref}]]` : null,
      entry: { ...base, key: `yard:${ref}`, kind: 'yard', label: y.label_fr, value, source: y.formula ? `Calcul de la plateforme : ${y.formula}` : 'Paramètre de la plateforme', url: null } };
  }

  if (kind === 'prop') {
    const p = props.get(ref);
    if (!p) return { ok: false, error: `[[prop:${ref}]] ne se résout pas` };
    const c = p.claimed || {};
    const claimed = c.central != null ? formatValue(c.central, 'EUR bn') : c.low != null && c.high != null ? formatValue({ low: c.low, high: c.high }, 'EUR bn') : null;
    const ests = (p.estimates || []).filter((e) => e.central != null || (e.low != null && e.high != null))
      .map((e) => `${e.author} : ${e.central != null ? formatValue(e.central, 'EUR bn') : formatValue({ low: e.low, high: e.high }, 'EUR bn')}`);
    const srcIds = [...new Set((p.estimates || []).flatMap((e) => e.source_ids || []))];
    const url = srcIds.map((i) => sources.get(i)?.urls?.[0]).find(Boolean) || null;
    return { ok: true, entry: { ...base, label: p.measure_fr, value: claimed ? `chiffrage annoncé : ${claimed}` : null, source: ests.join(' ; ') || 'Chiffrages indépendants : voir la page Débats', url } };
  }

  if (kind === 'src') {
    const s = sources.get(ref);
    if (!s) return { ok: false, error: `[[src:${ref}]] ne se résout pas` };
    const title = [s.institution, s.title].filter(Boolean).join(', ');
    return { ok: true, entry: { ...base, label: title, value: null, source: s.date ? `${title} (${s.date})` : title, url: s.urls?.[0] || null } };
  }

  if (kind === 'quiz') {
    if (!quiz.has(ref)) return { ok: false, error: `[[quiz:${ref}]] ne se résout pas` };
    return { ok: true, entry: { ...base, label: `Question ou perception ${ref} du quiz`, value: null, source: 'Banque du quiz (platform/data/quiz.json)', url: null } };
  }

  if (kind === 'calc') {
    const unknown = [...new Set([...ref.matchAll(CALC_ID)].map((m) => m[1]).filter((i) => !calcPool.has(i) && !(i.includes('*') && wildcardMatch(i))))];
    if (unknown.length) return { ok: false, error: `[[calc:]] utilise des identifiants inconnus : ${unknown.join(', ')}` };
    const readable = ref.replace(CALC_ID, (m, id) => figs.get(id)?.label_fr || yards.get(id)?.label_fr || params.get(id)?.label_fr || id);
    return { ok: true, entry: { ...base, key: `calc:${ref}`, label: 'Calcul illustratif de la plateforme', value: null, source: `${ref}  (${readable})`, url: null } };
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
