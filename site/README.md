# Site (squelette technique Astro)

Site statique construit avec [Astro](https://astro.build) 7.3.8. Mise en page selon la charte (`fr/conception/03-identite-visuelle.md`) et le format des pages de réponse (`fr/conception/05-pages-de-reponse.md`).

## Commandes

À lancer depuis `site/` (Node 22.23.4 ou plus récent).

```
npm install     # une seule fois (versions exactes dans package.json, verrou dans package-lock.json)
npm run dev     # serveur local, http://localhost:4321
npm run build   # génère dist/ ; échoue si une pastille est inconnue
npm run check   # vérification des types Astro/TypeScript
npm run preview # sert dist/ après un build
```

Les scripts doivent être lancés depuis `site/` : les chemins vers `../fr/` et `../platform/data/` en dépendent.

## Ce que le site lit (sans rien déplacer ni modifier)

| Source | Page produite |
|---|---|
| `fr/site/chapitres/*.md` | `/chapitres/<nom-du-fichier>/` (par exemple `/chapitres/01-combien/`) |
| `fr/site/debats.md` | `/debats/` |
| `platform/data/*.json` | résolution des pastilles à la construction |

La page d’accueil liste les chapitres.

## Pastilles

La grammaire reprend celle de `platform/data/validate.py` (`[[type:id]]`, option `|contexte`). Chaque pastille est vérifiée à la construction ; **une pastille inconnue fait échouer le build** (la liste des erreurs, avec fichier et ligne, s’affiche). Les pastilles placées dans les commentaires HTML ou le code ne comptent pas, comme dans `validate.py`.

| Pastille | Rendu |
|---|---|
| `[[fig:id]]` | renvoi numéroté ; en bas de page, valeur formatée en français avec son unité, libellé, année et lien vers la source (`figures.json`, puis `sources.json`) |
| `[[yard:id]]` | idem, valeur de l’étalon et formule (`yardsticks.json`) |
| `[[prop:id]]` | idem, montant annoncé et chiffrages indépendants (`proposals.json`) |
| `[[src:id]]` | titre, date et lien de la source (`sources.json`) |
| `[[calc:formule = résultat]]` | calcul « illustratif » ; les identifiants de la formule doivent exister |
| `[[quiz:id]]` | renvoi vers la banque du quiz (identifiant vérifié) |

Le nombre reste écrit dans le texte, comme dans les sources rédigées ; la pastille est un petit renvoi numéroté. Sans JavaScript, c’est un lien vers la liste « Chiffres et sources » (repliable, ouverte par défaut) ; avec, un toucher ouvre un encadré sous le paragraphe (valeur, libellé, année, source).

## Texte affiché et notes de l’équipe

Dans les chapitres, seuls les blocs de citation (`> …`, le « texte affiché » de `fr/LISEZMOI-site.md`) et les titres d’étape sont publiés. Sont masqués : les commentaires, les spécifications (visuels, interactions, « Pastilles source »), les tableaux de spécification et toute section « Notes… » (relecture, équipe, annexes) jusqu’à l’étape suivante. La page « Débats » est rendue en entier.

## Mise en forme

Le filtre typographique du glossaire §2.1 (espaces insécables, guillemets, apostrophe, points de suspension) s’applique aux textes ; les nombres des pastilles sont formatés (virgule décimale, espace fine insécable des milliers, vrai signe moins).

## Fichiers

- `src/lib/data.mjs` : chargement des données, résolution des pastilles, montants des pages de réponse, sources lisibles ;
- `src/lib/format.mjs` : formatage des valeurs et typographie ;
- `src/lib/render.mjs` : lecture des fichiers, filtrage éditorial, rendu HTML, découpage des pages de réponse (« En bref », sections) ;
- `src/lib/site.mjs` : ordre des cartes « Oui, mais… » (par montant, milieu de fourchette ; sans montant ensuite, par ordre alphabétique), parts du déficit, barre de fourchette ;
- `src/components/` : `LogoMark.astro` (**généré** par `npm run logo` à partir de `research/scripts/make_logo.py`, ne pas modifier à la main), `AnswerCard.astro`, `RangeBar.astro`, `Pager.astro` ;
- `src/styles/` : `tokens.css` (jetons, thèmes clair et sombre), `base.css`, `components.css` ;
- `src/scripts/site.ts` : amélioration progressive (bouton de thème gardé en `localStorage`, encadrés des pastilles, liste des sources repliée) ;
- `src/pages/` : accueil, `/reponses/` et pages de réponse, `/chapitres/` et chapitres, `/debats/`.

## Site Astro (31 octobre 2026)

### Structure

| Dossier | Rôle |
|---|---|
| `src/layouts/Base.astro` | gabarit commun : en-tête collant (une ligne de 56 px, logo seul sous 560 px), pied de page (logo monochrome : un seul logo tricolore par écran), bouton de thème |
| `src/pages/` | accueil, `/reponses/` (cartes « Oui, mais… »), `/reponses/<slug>/`, `/chapitres/`, `/chapitres/<slug>/`, `/debats/` |
| `src/components/` | `AnswerCard` (carte et mini-barre), `RangeBar` (bloc « Combien » : chiffre en grand, barre de fourchette, « Lecture : », « Source : »), `Pager`, `LogoMark` (généré) |
| `src/lib/render.mjs` | lecture de `fr/site/**.md`, filtrage éditorial, pastilles, typographie, liste « Chiffres et sources » |
| `src/lib/data.mjs` | lecture de `platform/data/*.json`, résolution des pastilles, montants, traductions des textes anglais du jeu de données |
| `src/lib/site.mjs` | ordre des cartes, parts du déficit, données de la barre de fourchette |
| `src/lib/format.mjs` | nombres et unités en français, filtre typographique |
| `src/styles/` | `tokens.css` (couleurs, thèmes clair et sombre), `base.css`, `components.css` |
| `src/scripts/site.ts` | seul JavaScript : thème (gardé dans `localStorage`, avec `try/catch`), encadré des pastilles, liste repliée |
| `scripts/gen_logo.py` | régénère `LogoMark.astro` depuis `research/scripts/make_logo.py` (`npm run logo`) ; ne pas dessiner le logo à la main |

### Lancer

```
npm run dev      # http://localhost:4321
npm run build    # dist/ ; échoue sur toute pastille inconnue
npm run preview  # sert dist/
```

### Pages de réponse

Chaque `fr/site/reponses/<slug>.md` (hors `_*.md`) commence par un commentaire `<!-- page … -->` (`slug`, `phrase`, `sujets`, `montant`, `levier`, `debats`). Seuls les blocs `> …` sont affichés ; le titre de niveau 1 devient l'en-tête, « **En bref.** » est isolé, puis chaque `##` devient un bloc numéroté (« 1 · Ce qui est vrai », « 2 · Combien »…).

Le montant de la carte et de la barre se calcule ainsi :
1. l'identifiant `montant:` (figure ou étalon en Md€ ; un solde négatif devient un déficit) s'il est cité dans le résumé de la carte ;
2. sinon, les pastilles « part du déficit » du « En bref » (`[[calc:X / deficit_2025_eur_bn * 100 = …]]`) : le numérateur `X` est évalué depuis `platform/data/` ; c'est le cas des propositions aux chiffrages multiples (`gel-prix-carburant`, `tva-energie`, `non-remplacement`) ;
3. sinon, l'identifiant `montant:` s'il est cité ailleurs dans le « En bref » ; sinon aucun montant (« sans montant chiffré »).

Le build affiche un avertissement quand `montant:` ne correspond pas au texte (aujourd'hui : `train-de-vie-ministeres`, dont le `montant:` vaut 1,16 Md€ alors que le « En bref » dit 29,4 Md€).

### Pastilles

Chaque `[[type:id]]` devient un petit renvoi numéroté, collé au mot précédent par une espace insécable. Sans JavaScript, c'est un lien vers la liste « Chiffres et sources » (titre visible, liste ouverte) ; avec, un toucher ouvre un encadré sous le paragraphe. Les montants en Md€ y portent aussi leurs autres unités (part du déficit de 2025, jours de dépense publique, « calcul du site »). Les calculs s'affichent sous forme lisible (« 12 ÷ 151,6 = 7,9 % »). Les dates sont en français, et les auteurs et institutions anglais du jeu de données passent par une table de traduction (`data.mjs`).

### Limites connues

- Composant « Et ailleurs ? » (une barre par pays, France en encre, rang après la mesure) : pas encore construit, la section reste en texte. Il faut d'abord savoir quelle série de `figures.json` correspond à chaque page.
- `age-65` n'a pas de montant (aucun identifiant vérifié) : pas de barre.
- Les unités anglaises listées par l'avertissement « unités sans traduction exacte » sont réduites à « % ».
