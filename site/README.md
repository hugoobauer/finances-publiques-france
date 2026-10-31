# Site (squelette technique Astro)

Site statique construit avec [Astro](https://astro.build) 7.3.8. Ce dossier ne contient que la chaîne de rendu ; la mise en page et l’identité visuelle restent à définir (la feuille de style `src/styles/site.css` est volontairement minimale).

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

Le nombre reste écrit dans le texte du chapitre, comme dans les sources rédigées ; la pastille est un renvoi `[n]` vers la liste « Chiffres et sources » du chapitre (le titre au survol donne la valeur).

## Texte affiché et notes de l’équipe

Dans les chapitres, seuls les blocs de citation (`> …`, le « texte affiché » de `fr/LISEZMOI-site.md`) et les titres d’étape sont publiés. Sont masqués : les commentaires, les spécifications (visuels, interactions, « Pastilles source »), les tableaux de spécification et toute section « Notes… » (relecture, équipe, annexes) jusqu’à l’étape suivante. La page « Débats » est rendue en entier.

## Mise en forme

Le filtre typographique du glossaire §2.1 (espaces insécables, guillemets, apostrophe, points de suspension) s’applique aux textes ; les nombres des pastilles sont formatés (virgule décimale, espace fine insécable des milliers, vrai signe moins).

## Fichiers

- `src/lib/data.mjs` : chargement des données et résolution des pastilles ;
- `src/lib/format.mjs` : formatage des valeurs et typographie ;
- `src/lib/render.mjs` : lecture des fichiers, filtrage éditorial, rendu HTML ;
- `src/pages/` : accueil, chapitres, débats ; `src/layouts/Base.astro` ; `src/styles/site.css`.
