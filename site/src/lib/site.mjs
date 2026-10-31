// Calculs d'affichage partagés par les pages (cartes « Oui, mais… », barre de fourchette).
// Toutes les valeurs viennent de platform/data/ via data.mjs ; les parts du déficit sont des « calculs du site ».
import { renderAll } from './render.mjs';
import { referenceDeficit } from './data.mjs';
import { formatNumber, NBSP, typography } from './format.mjs';

export const deficit = referenceDeficit();

/** « 6,6 % » ou « 6,6 à 16,5 % » : part du déficit de référence, une décimale. */
export function deficitShare(a) {
  const lo = (100 * a.low) / deficit.value;
  const hi = (100 * a.high) / deficit.value;
  const f = (x) => formatNumber(x, 1);
  return a.low === a.high ? `${f(lo)}${NBSP}%` : `${f(lo)} à ${f(hi)}${NBSP}%`;
}

/** Pourcentages pour dessiner une mini-barre : échelle = le plus grand du déficit et du haut de la fourchette
 *  (comme la barre de fourchette) ; `def` = position du déficit quand la fourchette le dépasse. */
export function shareWidths(a) {
  const scale = Math.max(deficit.value, a.high);
  const p = (x) => Math.max(0, Math.min(100, (100 * x) / scale));
  return { lo: p(a.low), hi: p(a.high), track: p(deficit.value), overflow: a.high > deficit.value };
}

const collator = new Intl.Collator('fr', { sensitivity: 'base', ignorePunctuation: true });
const sortKey = (a) => (a.phrase || a.title).replace(/^[«\s  ]+/, '');

/**
 * Ordre des cartes (fr/conception/01-parcours-et-architecture.md §8.2) : par montant, du plus grand au plus petit,
 * milieu de la fourchette ; les cartes sans montant ensuite, par ordre alphabétique de la phrase.
 */
export function sortedAnswers() {
  const { answers } = renderAll();
  const withAmount = answers.filter((a) => a.amount).sort((a, b) => b.amount.mid - a.amount.mid || collator.compare(sortKey(a), sortKey(b)));
  const without = answers.filter((a) => !a.amount).sort((a, b) => collator.compare(sortKey(a), sortKey(b)));
  return [...withAmount, ...without];
}

export const ORDER_RULE = typography('Cartes classées par montant annuel, du plus grand au plus petit (pour une fourchette, son milieu). '
  + 'Les cartes sans montant chiffré suivent, par ordre alphabétique. '
  + `La barre indique la part du déficit public de ${deficit.year} (${deficit.text}).`);


/** Données de la barre de fourchette (page de réponse) : géométrie, phrase « Lecture : » et ligne « Source : ». */
export function rangeBar(answer) {
  const a = answer.amount;
  if (!a) return null;
  const D = deficit.value;
  const scale = Math.max(D, a.high);
  const pct = (x) => (100 * x) / scale;
  const share = deficitShare(a);
  const single = a.low === a.high;
  const src = a.source;
  const amountSrc = src.internal
    ? (src.formula ? `calcul du site (${src.formula.replace(/\s+/g, ' ')})` : src.name)
    : `${src.name}${src.date ? `, ${src.date}` : ''}`;
  const defSrc = `${deficit.source.name}${deficit.source.date ? `, ${deficit.source.date}` : ''}`;
  return {
    deficitText: deficit.text,
    deficitYear: deficit.year,
    amountText: a.textBare,
    share,
    overflow: a.high > D,
    geom: { track: pct(D), lo: pct(a.low), hi: pct(a.high) },
    single,
    negative: Boolean(a.negative),
    title: typography(a.negative ? `${a.label.replace(/\s*\([^)]*\)\s*$/, '')}, face au déficit public de ${deficit.year}` : `${answer.title}, face au déficit public de ${deficit.year}`),
    sub: typography(`Montant annuel, en milliards d’euros. La piste grise représente le déficit public de ${deficit.year} (${deficit.text}).`),
    lecture: typography(a.negative
      ? `${a.label.replace(/\s*\([^)]*\)\s*$/, '')} : ${a.text}, soit ${share} du déficit public de ${deficit.year} (${deficit.text}).`
      : `${answer.title} : ${a.text} par an, soit ${single ? '' : 'de '}${share} du déficit public de ${deficit.year} (${deficit.text}).`),
    deficitLabel: typography(`Déficit ${deficit.year} : ${deficit.text}`),
    source: { amount: typography(amountSrc), amountUrl: src.url, deficit: typography(defSrc), deficitUrl: deficit.source.url },
    aria: `${a.textBare} face à un déficit de ${deficit.text}, soit ${share} du déficit`,
  };
}
