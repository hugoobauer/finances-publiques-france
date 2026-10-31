# Conception du site, étape 5 : format des pages de réponse

*Document de travail, 31 octobre 2026. Suit `01-parcours-et-architecture.md` (§6, §7.2, §8) et `04-sujets-et-objections.md` (§5 : les 15 premières pages). Modèle visuel : pages `#taxer-riches` et `#fraude` de `prototypes/retraites.html`.*

## 1. Fichiers

- Un fichier par page : `fr/site/reponses/<slug>.md` (slug de `04-sujets-et-objections.md`).
- Même convention que les chapitres : **seules les lignes de citation (`> `) sont affichées** ; le reste (commentaires HTML, notes) est de la spécification. Les pastilles `[[fig:]]`, `[[yard:]]`, `[[prop:]]`, `[[src:]]`, `[[calc:]]` suivent la syntaxe des chapitres et passent par `platform/data/validate.py --strict`.
- En tête de fichier, un commentaire de métadonnées lu par le site :

```
<!-- page
slug: taxer-riches
phrase: Il suffit de faire payer les plus riches
sujets: impots, retraites, deficit
montant: tax_rich_package_eur_bn
levier: R1, R2, R3, R4, R5
debats: 3.7, 3.8, 3.9, 3.14
-->
```

Puis un commentaire `NOTES POUR L’ÉQUIPE` (sources lues, données manquantes, choix faits).

## 2. Texte affiché, dans cet ordre

```
> # « Il suffit de faire payer les plus riches »
>
> **En bref.** Une phrase de réponse, avec le montant et sa part du déficit.
>
> ## Ce qui est vrai
> ## Combien
> ## Les limites
> ## Qui dit quoi
> ## Et ailleurs ?
```

1. **Titre** : la phrase entendue, entre guillemets français, sans attribution ni étiquette de camp.
2. **En bref** : la réponse courte d'abord (leçon de la revue des sites, `02-revue-des-sites.md` §7) ; une ou deux phrases ; un fait, pas un verdict.
3. **Ce qui est vrai** : toujours présent, jamais vide. Ce que la phrase a de juste, chiffré.
4. **Combien** : le montant annuel (fourchette si les estimations divergent), puis sa part du **déficit de référence : le déficit 2025 notifié, 151,6 Md€** (`deficit_2025_eur_bn`). Les prévisions ne servent que dans le simulateur. Une seule unité principale par page : milliards d'euros par an et part du déficit ; les autres unités (% du PIB, € par habitant) seulement en complément, une fois.
5. **Les limites** : ce qui rend le chiffre incertain ou non additionnable (réactions des contribuables, montée en charge, risque juridique, double compte, effet sur la croissance).
6. **Qui dit quoi** : auteurs nommés avec l'étiquette d'organisme du glossaire (§1.13), mot pour mot, montant et date. Au moins deux lectures quand elles existent ; si une seule position publiée a été trouvée, l'écrire.
7. **Et ailleurs ?** : la comparaison UE-27 / zone euro / OCDE / panel (DE, IT, ES, NL, BE, SE, DK), et, quand les données existent dans `figures.json`, le **rang après la mesure** (« Même après cette mesure, la France resterait Xe sur 27 »), sans commentaire. Monde hors Europe si une source existe (OIT, OCDE).

Le bouton « Ajouter à mon budget » est généré par le site à partir de `levier:` ; il n'est pas écrit dans le texte.

## 3. Règles de rédaction

- **Aucune étiquette gauche/droite sur une idée ou une objection** ; les organismes gardent leur étiquette du glossaire (« Fondation iFRAP (libérale) »). Les partis peuvent être nommés comme auteurs d'un chiffrage (« le programme de LFI »), pas comme camp.
- **Un fait, pas un verdict** : pas de « il faut », « irréaliste », « démagogique » ; pas de titre-verdict.
- **Tout chiffre affiché a sa pastille** vers `figures.json`, `yardsticks.json`, `proposals.json` ou un `[[calc:]]`. Aucun chiffre inventé ; aucun chiffre lu seulement dans un fichier de recherche sans identifiant. Un chiffre qui manque est **omis** du texte affiché et consigné dans les notes (« Données manquantes »), jamais remplacé par une estimation.
- Niveau B1 : phrases de 25 mots au plus, paragraphes de 60 mots au plus ; sigle développé à la première occurrence ; typographie française du glossaire §2.
- **Longueur** : 300 à 900 mots affichés (cible 450 à 700).
- **Symétrie** : la même grille s'applique aux promesses de recettes et d'économies.

## 4. Contrôle

`python3 -I platform/data/validate.py --strict` vérifie aussi `fr/site/reponses/` (pastilles, chiffres affichés, sigles, longueurs ; bornes de mots propres aux pages de réponse ; sections obligatoires dans l'ordre). Le site Astro les publie sous `/reponses/<slug>/`.
