// Amélioration progressive : les pages se lisent sans ce script (renvois = liens vers la liste des sources,
// liste ouverte, thème du système). Avec lui : bouton de thème, encadré des pastilles, liste repliée.

const root = document.documentElement;

// ---------- Thème : réglage du système, ou choix gardé dans le navigateur ----------
const toggle = document.getElementById('theme-toggle') as HTMLButtonElement | null;
const label = toggle?.querySelector('.toggle-label');
const mq = window.matchMedia ? window.matchMedia('(prefers-color-scheme: dark)') : null;
const currentTheme = () => root.getAttribute('data-theme') || (mq && mq.matches ? 'dark' : 'light');
function syncToggle() {
  if (!toggle) return;
  const dark = currentTheme() === 'dark';
  if (label) label.textContent = dark ? 'Clair' : 'Sombre'; // l'action proposée, pas l'état actuel
  toggle.setAttribute('aria-label', dark ? 'Passer au thème clair' : 'Passer au thème sombre');
}
if (toggle) {
  toggle.hidden = false;
  syncToggle();
  toggle.addEventListener('click', () => {
    const next = currentTheme() === 'dark' ? 'light' : 'dark';
    root.setAttribute('data-theme', next);
    try { localStorage.setItem('theme', next); } catch { /* stockage indisponible : le choix vaut pour cette page */ }
    syncToggle();
  });
  mq?.addEventListener?.('change', syncToggle);
}

// ---------- Liste « Chiffres et sources » : repliée, sauf si l'on arrive sur un renvoi ----------
const list = document.getElementById('chiffres-et-sources') as HTMLDetailsElement | null;
const isChipHash = () => location.hash.startsWith('#pastille-');
if (list && !isChipHash()) list.open = false;
window.addEventListener('hashchange', () => { if (list && isChipHash()) list.open = true; });

// ---------- Pastilles : encadré sous le paragraphe (pas d'infobulle flottante) ----------
let uid = 0;
const INSIDE = /^(LI|TD|TH|DD)$/;

function popFor(block: Element): HTMLElement | null {
  if (INSIDE.test(block.tagName)) return block.querySelector(':scope > .chip-pop');
  const next = block.nextElementSibling;
  return next && next.classList.contains('chip-pop') ? (next as HTMLElement) : null;
}

function closePop(pop: HTMLElement, focusMarker = false) {
  const owner = document.getElementById(pop.dataset.owner || '');
  owner?.setAttribute('aria-expanded', 'false');
  pop.remove();
  if (focusMarker) (owner as HTMLElement | null)?.focus();
}

function fillPop(pop: HTMLElement, n: string, item: Element) {
  const body = item.querySelector('.cs-body')?.cloneNode(true) as HTMLElement | null;
  pop.replaceChildren();
  const head = document.createElement('div');
  head.className = 'pop-head';
  const title = document.createElement('span');
  title.className = 'cs-kind';
  title.textContent = `Renvoi n°\u00a0${n}`;
  const close = document.createElement('button');
  close.type = 'button';
  close.className = 'pop-close';
  close.textContent = 'Fermer';
  close.addEventListener('click', () => closePop(pop, true));
  head.append(title, close);
  pop.append(head);
  if (body) {
    body.querySelector('.cs-kind')?.remove();
    pop.append(...Array.from(body.childNodes));
  }
  const more = document.createElement('a');
  more.className = 'pop-more';
  more.href = `#pastille-${n}`;
  more.textContent = 'Voir dans la liste des chiffres et sources';
  pop.append(more);
}

document.addEventListener('click', (e) => {
  if ((e.target as Element | null)?.closest?.('.pop-more') && list) list.open = true;
  const marker = (e.target as Element | null)?.closest?.('a.pastille') as HTMLAnchorElement | null;
  if (!marker) return;
  const n = marker.dataset.n;
  const item = n ? document.getElementById(`pastille-${n}`) : null;
  if (!n || !item) return; // pas de liste : le lien suit son cours
  e.preventDefault();
  if (!marker.id) marker.id = `renvoi-${++uid}`;
  const block = marker.closest('p, li, td, th, dd, h1, h2, h3, h4, figcaption') || marker.parentElement!;
  let pop = popFor(block);
  if (pop && pop.dataset.owner === marker.id) { closePop(pop); return; }
  if (pop) document.getElementById(pop.dataset.owner || '')?.setAttribute('aria-expanded', 'false');
  else {
    pop = document.createElement('div');
    pop.className = 'chip-pop';
    pop.id = `encadre-${++uid}`;
    pop.setAttribute('role', 'region');
    if (INSIDE.test(block.tagName)) block.append(pop); else block.after(pop);
  }
  pop.dataset.owner = marker.id;
  pop.setAttribute('aria-label', `Renvoi n°\u00a0${n}`);
  fillPop(pop, n, item);
  marker.setAttribute('aria-controls', pop.id);
  marker.setAttribute('aria-expanded', 'true');
});

document.addEventListener('keydown', (e) => {
  if (e.key !== 'Escape') return;
  const pop = (document.activeElement as Element | null)?.closest?.('.chip-pop') as HTMLElement | null;
  const marker = document.activeElement as HTMLElement | null;
  if (pop) closePop(pop, true);
  else if (marker?.matches?.('a.pastille[aria-expanded="true"]')) {
    const p = document.getElementById(marker.getAttribute('aria-controls') || '');
    if (p) closePop(p, true);
  }
});
