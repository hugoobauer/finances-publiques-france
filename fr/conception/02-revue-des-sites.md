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

**Revus sur téléphone le 31 octobre 2026 (§7) ; budget.gouv.fr, economie.gouv.fr et Les Décodeurs sont restés bloqués (captcha) :** budget.gouv.fr, impots.gouv.fr (« à quoi servent mes impôts »), Insee « en bref », Les Décodeurs, une page Wikidébats, le *Debt Fixer* et Our World in Data.

## 7. Revue sur téléphone (navigateur, 31 octobre 2026)

**Méthode.** Écran de 390 × 844 px, navigateur puppeteer, 2 à 5 captures par site. Trois sites sont restés fermés : budget.gouv.fr (hCaptcha), economie.gouv.fr (Cloudflare) et Les Décodeurs (captcha avec image). Nous n'avons pas essayé de contourner ces contrôles. Seuls les 5 autres sites ont été vus, et ce qui suit se limite à ce que les captures montrent. La page « Dette et déficit publics » d'Insee est un cas à part : elle est lisible, mais ce n'est pas une page « en bref ».

### 1. budget.gouv.fr
**Bloqué.** Page « Additional security check is required » (Imperva, hCaptcha). Rien à dire sur le site lui-même.
- *Leçon indirecte :* un site public qui exige un captcha à un lecteur sur téléphone le perd avant la première phrase. Notre site ne doit rien demander avant le contenu.

### 2. impots.gouv.fr, « à quoi servent mes impôts »
- **Vu.** L'adresse devinée donne une page 404 correcte : message en phrases simples, gros bouton « Page d'accueil ». Le menu est réduit à une loupe et un bouton. Sur la page d'erreur, un widget flottant masque le bas de l'écran. La recherche interne a mal interprété la requête (résultat pour « 1 », 167 pages). Le lien de la page « À quoi servent mes impôts ? » renvoie vers economie.gouv.fr/aqsmi, qui est bloqué par Cloudflare. Le contenu n'a donc pas pu être vu.
- **À reprendre :**
  1. une page d'erreur qui dit quoi faire, avec un grand bouton pleine largeur ;
  2. le thème sombre appliqué automatiquement, lisible sur téléphone.
- **À éviter :** un parcours qui sort du site vers un autre domaine sans l'annoncer, et un moteur de recherche qui ne comprend pas une question en français.

### 3. Insee, dette et déficit publics
Deux pages vues : « Dette et déficit publics au sens de Maastricht en 2025 » (28/08/2026, tableaux) et la page de chiffres clés « Dette des administrations publiques au sens de Maastricht ».
- **Vu.**
  - **En-tête :** bandeau bleu avec titre, type de page (« Chiffres détaillés »), date de parution et lien « Imprimer ». Le menu est replié, et un menu déroulant « Consulter » ou « Graphique » change de vue.
  - **Page de tableaux :** une longue liste de cartes, chacune avec un intitulé (« 3.106 – Déficit des administrations publiques… ») et un bouton de téléchargement xlsx de 21 à 205 Ko. Aucun chiffre n'est lisible sans ouvrir un fichier, ce qui est très peu adapté à un téléphone.
  - **Chiffres clés :** une courbe pleine largeur (dette en % du PIB, de 2004 à 2026) avec un axe vertical lisible. Elle monte de 67 % à 119 %. La note sous le graphique est longue, mais le mot « dette » et le mot « PIB » sont en pointillés, ce qui suggère une définition au toucher, non testée.
  - **Source et lecture :** une phrase « Lecture : à la fin du 2e trimestre 2026, la dette publique de Maastricht représente 119,0 % du PIB », puis « Champ : France » et « Sources : Banque de France, DGFiP, Insee », avec lien. Suit un bloc « Pour en savoir plus ».
- **À reprendre :**
  1. la phrase « Lecture », qui traduit le graphique en un chiffre daté ;
  2. la ligne « Champ » plus « Sources » juste sous le graphique.
- **À éviter :** des tableaux livrés uniquement en fichiers xlsx ; une note de méthode d'un seul bloc dense au-dessus de la phrase qui compte.

### 4. Les Décodeurs (Le Monde)
**Bloqué** par un captcha à caractères déformés. Aucune page d'article n'a pu être vue ; le format du verdict reste non vu.

### 5. CRFB, Debt Fixer
- **Vu.**
  - **Introduction :** un titre, trois paragraphes courts, puis deux objectifs en gros chiffres côte à côte (« 100 % en 10 ans » et « 60 % d'ici 2050 »). Le déficit actuel est donné en phrase avec le chiffre en rouge (« 3 % of GDP »).
  - **Navigation :** une barre d'onglets en haut, avec flèches < >, un onglet par poste (Introduction, Défense…). En bas de chaque étape, trois boutons : Back, Next, Done.
  - **Choix :** boutons radio pour les niveaux (« select one ») et interrupteurs pour les mesures isolées. Les cibles de toucher sont assez grandes. Un choix coché passe en gras avec un point bleu.
  - **Compteur :** il n'est pas affiché pendant les choix. Après notre sélection, rien ne montrait l'effet à l'écran. Il n'apparaît qu'au bas de la page de résultat : « $9,190 BILLION TO GO. Your goal is to cut $9,870 billion… », sous un graphique en deux barres (121 % en 2036, 143 % en 2050).
  - **Sources :** les infobulles « i » (près de 600 éléments dans la page) contiennent des phrases du type « Defense spending will total around $900 billion in FY 2026 ». Sur téléphone, il faut les toucher une par une.
- **À reprendre :**
  1. une étape par poste de dépense, avec Back / Next / Done toujours au même endroit ;
  2. la phrase « il reste X à trouver » en encadré contrasté, avec l'objectif rappelé dans la même phrase.
- **À éviter :** un compteur invisible pendant le jeu. Cela contredit le principe retenu au §6 (compteur permanent) : sur téléphone, il faudra le fixer en bas de l'écran.

### 6. Our World in Data, Government spending
- **Vu.**
  - **Haut de page :** titre, sous-titre en question (« What do governments spend their financial resources on? »), auteurs, boutons « Cite this work » et « Reuse this work », date de première publication.
  - **Cookies :** un bandeau jaune couvre le tiers de l'écran au chargement, avec « Reject » et « Accept » aussi visibles l'un que l'autre.
  - **Graphique :** il tient dans la largeur. Son titre dit la mesure (« Government spending as share of GDP, 1830 to 2024 »). Les pays sont étiquetés au bout des courbes (pas de légende séparée), il y a un curseur temporel avec bouton lecture, et les icônes télécharger / partager / plein écran. La source est écrite dessous (« International Monetary Fund (2025) ») avec la licence « CC BY ».
  - **Texte :** après le graphique, des paragraphes courts, et des intertitres qui sont des phrases complètes (« Public spending growth in early-industrialised countries was largely driven by social spending »). Un bouton « Contents » flottant recouvre parfois le texte lu.
  - **Lisibilité :** les 5 courbes sont serrées entre 30 % et 50 % après 1950. Sur 390 px, seules les deux guerres se lisent nettement.
- **À reprendre :**
  1. titre de graphique qui dit la mesure et la période, puis source et licence juste dessous ;
  2. étiquettes directes au bout des courbes, sans légende à décoder.
- **À éviter :** un bouton flottant qui masque des lignes de texte, et des courbes qui se confondent sur petit écran.

### 7. Full Fact
- **Vu.**
  - **Liste :** des cartes avec une grande image, une pastille d'étiquette (« QUICK CHECK ») et la date. Des filtres en boutons (Latest, Fact Checks, Comment, Analysis).
  - **Article :** pastille « QUICK CHECK », date, titre qui reprend l'affirmation testée, auteur, temps de lecture (« 1 min ») et boutons de partage. Le texte commence par l'affirmation : « A Facebook post wrongly claims that… ». Les liens sources sont soulignés en turquoise dans les phrases.
  - **Verdict :** il n'est pas en tête. Il apparaît plus bas, dans un grand encadré turquoise : « we've rated this claim as partly false because income tax and several other taxes… existed 100 years ago ». « partly false » est souligné comme un lien. Un cookie bandeau reste collé en bas de l'écran.
  - **Fin :** une bannière jaune « Was this helpful? ».
- **À reprendre :**
  1. étiquette de format, date et temps de lecture sous le titre ;
  2. verdict en une phrase dans un encadré de couleur, avec la raison dans la même phrase.
- **À éviter :** placer le verdict après la lecture. Pour nous, la réponse courte doit venir avant le détail.

### 8. Fipeco, une fiche
- **Vu.**
  - **Accueil :** « Comprendre les finances publiques et l'économie. », bouton « Dernière analyse », lien « Explorer l'encyclopédie ».
  - **Fiche (prélèvements obligatoires) :** fil d'Ariane (« Accueil / Encyclopédie / … »), un « Sommaire » replié, boutons de partage, date (« FIPECO, le 28.10.2026 »), lien « PDF à lire et imprimer ».
  - **Texte :** une corps de texte justifié, qui crée de grands espaces blancs dans les lignes (très visible dans la première ligne « Les fiches de l'encyclopédie »). Les paragraphes sont longs (8 à 10 lignes). Un bouton rond « retour en haut » flotte à droite et recouvre parfois la fin des lignes. Les intertitres numérotés (« A) », « 1) ») sont en bleu et bien visibles.
  - **Sources :** dans les captures, les renvois sont des numéros entre crochets (« [1] »). Nous n'avons pas vu la liste des sources.
- **À reprendre :**
  1. le sommaire replié en haut de page ;
  2. la date visible avant le texte, et le PDF imprimable en option.
- **À éviter :** le texte justifié, qui devient illisible sur 390 px, et les longs paragraphes sans chiffre en gras.

## Synthèse : 5 leçons pour un site mobile B1

1. **Un chiffre, une phrase de lecture, la source dessous.** Le modèle d'Insee (« Lecture : à la fin du 2e trimestre 2026… ») et d'OWID (titre = mesure et période) fonctionne sur téléphone. Le graphique seul, sans phrase, ne suffit pas.
2. **Réponse courte avant le détail.** Full Fact met le verdict en fin d'article et Insee met la note de méthode avant la phrase de lecture : dans les deux cas, le lecteur cherche. Chez nous, la réponse est en tête, le détail est replié.
3. **Le compteur du simulateur doit être fixé à l'écran.** Dans le Debt Fixer, le total n'est visible qu'à la fin. Sur téléphone, une barre fixe en bas (« il reste X Md€ ») est indispensable, et elle ne doit pas masquer les boutons.
4. **Pas de pièges de lecture.** Aucun texte justifié (Fipeco), aucun bouton flottant qui recouvre le texte (OWID, Fipeco), aucun bandeau cookie qui reste collé (Full Fact), aucun captcha ni fichier xlsx comme seule porte d'entrée (budget.gouv.fr, Les Décodeurs, Insee).
5. **Étiquettes directes et gros boutons.** Pays écrits au bout des courbes (OWID), pastilles de format et de date (Full Fact), cibles de toucher larges et boutons Back / Next / Done stables (CRFB). Moins de 5 séries par graphique sur 390 px.

**À refaire.** Budget.gouv.fr, economie.gouv.fr/aqsmi et un article des Décodeurs n'ont pas pu être vus ; le contrôle doit être fait à la main, depuis un vrai téléphone.
