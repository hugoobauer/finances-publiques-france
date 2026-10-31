// Mise en forme française des valeurs (glossaire §2.1 : espaces insécables, virgule décimale,
// vrai signe moins). Aucune valeur n'est calculée ici : on ne fait que formater.

export const NBSP = ' ';
export const NNBSP = ' ';
const MINUS = '−';

/** Nombre de décimales d'un nombre écrit en JSON (1714.1 -> 1). */
export function decimalsOf(x) {
  const s = String(x);
  if (/e/i.test(s)) return 0;
  const i = s.indexOf('.');
  return i < 0 ? 0 : s.length - i - 1;
}

export function formatNumber(x, decimals, { grouping = true } = {}) {
  const abs = Math.abs(x);
  const fixed = abs.toFixed(Math.max(decimals, 0));
  let [int, dec] = fixed.split('.');
  if (grouping && int.length > 3) int = int.replace(/\B(?=(\d{3})+(?!\d))/g, NNBSP);
  return (x < 0 && Number(fixed) !== 0 ? MINUS : '') + int + (dec ? ',' + dec : '');
}

// Unité anglaise du jeu de données -> suffixe français (précédé d'une espace insécable).
// `null` = nombre seul. Les unités absentes de la table sont signalées (voir `unitStats`).
const UNIT_EXACT = {
  'EUR bn': 'Md€',
  'EUR bn per year': 'Md€ par an',
  'EUR bn per year (cost)': 'Md€ par an',
  'EUR bn per day': 'Md€ par jour',
  EUR: '€',
  'EUR per month': '€ par mois',
  'EUR per inhabitant': '€ par habitant',
  'EUR per inhabitant per year': '€ par habitant et par an',
  'EUR per inhabitant per day': '€ par habitant et par jour',
  'EUR per second': '€ par seconde',
  'EUR per month per EUR bn': '€ par mois et par Md€',
  'PPS per inhabitant': 'SPA par habitant',
  '% of GDP': '% du PIB',
  '% of GDP (deficit)': '% du PIB',
  '% of GDP per year': '% du PIB par an',
  '% of total public expenditure': '% des dépenses publiques',
  '% of population': '% de la population',
  '% of GNI': '% du RNB',
  '% of the stock': '% du stock',
  '% of tax households': '% des foyers fiscaux',
  '% of total employment': '% de l’emploi total',
  '% of population 15-64': '% des 15-64 ans',
  '% of population 65+': '% des 65 ans et plus',
  '% of total revenue': '% des recettes',
  '% (yield)': '%',
  '% (average apparent interest rate on debt)': '%',
  '% per year, volume (excluding inflation)': '% par an en volume',
  '% change over the previous year (current prices)': '%',
  '% change (current euros)': '%',
  '% change (constant euros, deflated by the HICP)': '%',
  '%': '%',
  'percentage points of GDP': 'points de PIB',
  'points of GDP': 'points de PIB',
  'percentage points': 'points',
  'percentage points of population': 'points de population',
  'basis points': 'pb',
  years: 'ans',
  days: 'jours',
  'days of 2025 public spending': 'jours de dépense publique',
  'days elapsed since 1 January': 'jours depuis le 1er janvier',
  'million persons': 'millions de personnes',
  persons: 'personnes',
  'FTE jobs': 'emplois en équivalent temps plein',
  'judges per 100,000 inhabitants': 'juges pour 100 000 habitants',
  'hours per inhabitant per year': 'heures par habitant et par an',
  'multiple of the SMIC': '× le SMIC',
  'notches below the top rating (AAA / Aaa = 0)': 'niveaux sous la meilleure note',
  'index, EU-27 = 100 (PPS)': '(indice UE-27 = 100, en SPA)',
  year: null,
  N: null,
  score: null,
  measures: 'mesures',
  // Ratios sans dimension : le libellé de la figure porte le sens.
  'GDP loss per unit of consolidation': null,
  'deficit change per unit of GDP change': null,
  'net deficit improvement per EUR of measures': null,
};

export const unitStats = { approximated: new Map() };

function frUnit(unit) {
  if (!unit) return null;
  if (Object.hasOwn(UNIT_EXACT, unit)) return UNIT_EXACT[unit];
  if (unit.startsWith('rank')) return 'RANK';
  // Repli : on garde un symbole sûr quand l'unité commence par « % » ou « EUR bn », sinon l'unité brute.
  unitStats.approximated.set(unit, (unitStats.approximated.get(unit) || 0) + 1);
  if (unit.startsWith('%')) return '%';
  if (unit.startsWith('EUR bn')) return 'Md€';
  return `[${unit}]`;
}

/** Formate une valeur avec son unité. `value` peut être un nombre ou { low, high } (fourchette). */
export function formatValue(value, unit, decimals) {
  const fu = frUnit(unit);
  const grouping = unit !== 'year';
  const num = (v, d) => formatNumber(v, d, { grouping });
  if (value && typeof value === 'object') {
    const d = decimals ?? Math.max(decimalsOf(value.low), decimalsOf(value.high));
    const text = `${num(value.low, d)} à ${num(value.high, d)}`;
    return fu && fu !== 'RANK' ? `${text}${NBSP}${fu}` : text;
  }
  const d = decimals ?? decimalsOf(value);
  const text = num(value, d);
  if (fu === 'RANK') return `rang${NBSP}${text}`;
  return fu ? `${text}${NBSP}${fu}` : text;
}

/** Filtre typographique (glossaire §2.1), appliqué aux seuls nœuds de texte. */
export function typography(s) {
  return s
    .replace(/'/g, '’')
    .replace(/\.\.\./g, '…')
    .replace(/« +/g, `«${NNBSP}`)
    .replace(/ +»/g, `${NNBSP}»`)
    .replace(/ +:/g, `${NBSP}:`)
    .replace(/ +([;?!])/g, `${NNBSP}$1`)
    .replace(/(\d) +(%|€|Md€|M€|pt|pb|SPA|ans)(?![\p{L}])/gu, `$1${NBSP}$2`);
}
