# Conception du site, étape 2 : revue des sites existants

*Document de travail, 31 octobre 2026. Revue de 13 sites ou outils, faite par recherche web. Elle complète `01-parcours-et-architecture.md`.*

**Limites de la méthode.** Les pages ont été lues par des outils qui renvoient du texte. Le rendu visuel et le comportement sur téléphone n'ont été vus nulle part. Plusieurs sites n'ont pas pu être ouverts : budget.gouv.fr, economie.gouv.fr, impots.gouv.fr, Insee « en bref », Les Décodeurs, Polis, des pages d'Our World in Data et d'USAFacts. Les points marqués **[inféré]** ou **[non vu]** sont des hypothèses. Avant la charte graphique, il faut revoir ces sites dans un vrai navigateur, sur téléphone (voir §6).

## 1. Simulateurs de budget

**CRFB, *Debt Fixer*** (crfb.org/debtfixer). Un jeu en étapes, un choix par section (défense, santé, retraites, impôts…).
- *À reprendre :*
  - un compteur « il reste X milliards à trouver », visible pendant tous les choix ;
  - l'effet de chaque choix, montré au fur et à mesure ;
  - un message de fin gradué, avec un objectif de court terme et un de long terme ;
  - le partage du résultat.
- *À éviter :*
  - aucune source, hypothèse ou incertitude affichée ;
  - le cadrage d'une organisation militante pour la réduction du déficit ;
  - des données personnelles (code postal, parti) demandées en fin de parcours.

**New York Times, *You Fix the Budget*** (2010, connu par des comptes rendus de presse). Un menu d'environ 40 mesures (baisses de dépenses, hausses d'impôts) pour combler le déficit à deux horizons.
- *À reprendre :*
  - pas de recommandation du journal ;
  - chaque option montre son poids, ce qui fait voir lesquelles sont une « goutte d'eau » ;
  - deux horizons de temps.
- *À éviter :* le menu a été critiqué comme orienté : peu d'options d'impôts, des postes exclus. **Chaque omission devient un biais perçu.**

**Institut Montaigne, *Atelier des finances publiques*** (2013 ; description seule, l'outil n'a pas pu être vérifié en ligne). Il permet de modifier des hypothèses en temps réel et de partager sa simulation. *À éviter :* il n'affiche ni scénario de référence ni hypothèses.

**Cyberbudget** (ministère du Budget, 2006 ; description seule). Un jeu où l'on joue le ministre, pour faire comprendre la difficulté des arbitrages. *À éviter :* un jeu institutionnel est vite perçu comme de la communication d'État.

## 2. Explicatifs de données

**Our World in Data, *Government spending*.**
- *À reprendre :*
  - un graphique suivi d'un court texte, chaque graphique ouvrant une version interactive ;
  - les précautions écrites dans le texte ;
  - des repères dans le temps (10 % du PIB à la fin du XIXe siècle, près de 50 % aujourd'hui) ;
  - une citation prête à l'emploi et une licence CC BY.
- *À éviter :* une page dense, sans points clés en tête, trop technique pour le niveau B1 **[inféré]**.

**USAFacts, *State of the Union*.**
- *À reprendre :*
  - une neutralité affichée et définie (« les données, l'interprétation au lecteur ») ;
  - l'organisme source nommé sous chaque graphique ;
  - les limites des données signalées ;
  - des unités précises (euros courants ou constants, année de base) ;
  - un sous-titre qui définit la mesure.
- *À éviter :* une suite de fiches sans parcours guidé.

**The Pudding.** Seul l'index a pu être lu ; un filtre « Your Input » signale des articles où le lecteur participe. Format non vu **[non vu]**.

## 3. Explicatifs institutionnels français

**Cour des comptes, *Situation et perspectives des finances publiques*.**
- *À reprendre :* des intertitres qui sont des phrases complètes (« des économies réelles mais bien inférieures à celles annoncées ») et des téléchargements classés (synthèse, rapport, données).
- *À éviter :* pas de résumé grand public, des PDF lourds pour un téléphone, aucun graphique sur la page.

**Fipeco** (fipeco.fr).
- *À reprendre :*
  - un repère de niveau par couleur (essentiel, spécialisé, approfondissement) ;
  - une date de mise à jour sur chaque fiche ;
  - des fiches qui se lisent seules ;
  - une séparation nette entre fiches factuelles et notes d'opinion signées ;
  - des QCM.
- *À éviter :* aucune politique éditoriale affichée, des sources peu visibles, des fiches longues pour un téléphone **[inféré]**.

**budget.gouv.fr, economie.gouv.fr, impots.gouv.fr, Insee « en bref » :** non ouverts, rien à en dire pour l'instant.

## 4. Vérification des faits

**Full Fact** (fullfact.org).
- *À reprendre :*
  - le titre est l'affirmation testée ou une question ;
  - un verdict en une phrase dans le résumé ;
  - une étiquette de format (vérification rapide, vérification, analyse), une date, un temps de lecture ;
  - des pages sur l'impartialité et le financement ;
  - des affirmations venues de tous les camps.
- *Non vu :* l'échelle de notation, car l'article complet n'a pas pu être ouvert.

**Les Décodeurs** (Le Monde ; site non ouvert). D'après un évaluateur du réseau international de vérificateurs (2018), la règle est « des sources accessibles en un clic ». Format actuel **[non vu]**.

## 5. Débat et cartographie d'arguments

**Kialo.**
- *À reprendre :* une thèse formulée en question, puis des arguments pour et contre, chacun avec ses sous-arguments.
- *À éviter :*
  - une arborescence profonde, lourde sur téléphone **[inféré]** ;
  - un tri par votes, qui fait remonter ce que les gens veulent croire **[inféré]**.

**Polis** (lu via Wikipédia).
- *À reprendre :* la participation anonyme et la mise en avant des idées qui rassemblent plusieurs camps.
- *À éviter :* il faut un grand nombre de participants, que le site n'aura pas.

**Wikidébats :** rien trouvé.

## 6. Ce que nous en retenons

| # | Modèle | Où dans notre site | Statut |
|---|---|---|---|
| 1 | Compteur permanent « il reste X Md€ à trouver », message de fin gradué | Simulateur | Retenu |
| 2 | Pas de recommandation ; chaque levier montre son poids (« goutte d'eau » ou non) | Simulateur, cartes « Oui, mais… » | Retenu ; c'est déjà le principe des pages de réponse |
| 3 | Menu équilibré, et liste publique des leviers écartés avec la raison | Simulateur (34 leviers dans `simulator-levers.json`) | Retenu ; ajouter une page « leviers non retenus » |
| 4 | Intertitres en phrases complètes | Chapitres, pages de sujet | Retenu pour les intertitres. **Pas pour les titres des pages de réponse**, qui restent la phrase entendue : un verdict en titre contredirait la règle « un fait, pas un verdict » (étape 1, §2). |
| 5 | Étiquette de niveau et de format, date de mise à jour, temps de lecture | Toutes les pages | Retenu |
| 6 | Source et limites écrites sous chaque graphique, unité précisée | Composants « fiche chiffre » et « pastille source » | Déjà prévu (fichier 20, §2.3) |
| 7 | Neutralité montrée par la méthode : page méthode et financement, affirmations de tous les camps | Espace « Confiance » | Déjà prévu |
| 8 | Repères dans le temps et fourchettes plutôt que points | « Et ailleurs ? », barres de fourchette | Retenu |
| 9 | Thèse → objections → sous-arguments, sur un ou deux niveaux, sans vote | Pages de sujet et de réponse | Retenu, limité à deux niveaux |

**Pièges à éviter :**

1. **Des chiffres sans hypothèses.** Le simulateur affiche sa base (année, déficit de référence, croissance, lois en vigueur) avant le premier choix.
2. **Un menu qui oriente.** Toute absence d'un levier est expliquée publiquement.
3. **Une page dense ou un PDF.** Pour le niveau B1 sur téléphone : un chiffre, une phrase, puis le détail replié.
4. **Un outil qui disparaît.** Chaque outil affiche la date de ses données et sa version ; les anciennes versions restent consultables.
5. **Des données personnelles.** Le site ne demande jamais ni parti ni code postal.

**À voir dans un vrai navigateur, sur téléphone, avant la charte graphique :** budget.gouv.fr, impots.gouv.fr (« à quoi servent mes impôts »), Insee « en bref », Les Décodeurs, une page Wikidébats, le *Debt Fixer* et Our World in Data.
