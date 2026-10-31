# Conception du site, étape 3 : identité visuelle

*Document de travail, 31 octobre 2026. Il suit `01-parcours-et-architecture.md` et `02-revue-des-sites.md` (§6 et §7). Le spécimen correspondant est `prototypes/identite-visuelle.html` (un seul fichier, thèmes clair et sombre, vérifié à 390 et 1 280 px).*

**Consigne du porteur du projet.** « Sobre et discret, avec de petites touches élégantes, un peu start-up. Par exemple, des drapeaux français dessinés en traits fins. »

## 1. Principes

1. **Le chiffre est le héros.** La page met en valeur un nombre, une phrase et une source. Le reste (couleurs, filets, typographie) s'efface.
2. **Neutre, et pas officiel.** Le site ne doit pas ressembler à un site de l'État : pas de Marianne, pas de bloc « République française », pas de police Marianne, pas d'imitation du système de design de l'État (DSFR), pas de bleu `#000091`. Le tricolore n'apparaît qu'en un filet fin, une fois par écran, comme une signature.
3. **Aucune couleur ne prend parti.** Le bleu et le rouge ne codent jamais un camp, ni le vert et le rouge un « bien » et un « mal ». Les graphiques n'utilisent que l'encre, le gris et l'ocre.
4. **Le téléphone d'abord.** Tout est conçu pour 390 px de large, puis élargi. Lecteur visé : niveau B1, lecture rapide, pouce sur l'écran.
5. **Moins d'éléments, mieux finis.** Un seul accent d'interaction, deux rayons d'angle, une grille d'espacement. Le côté « start-up » vient du soin des détails (chiffres en police à chasse fixe, filets de 1 px, en-tête translucide), pas de l'ornement.

## 2. Logotype et nom (à choisir)

**Retour du porteur du projet (31 octobre 2026).** Le nom « ordres de grandeur » est rejeté, même comme nom provisoire. Le logo aux trois graduations tricolores « a de l'idée mais n'est pas assez travaillé ». Le drapeau est « trop » présent : la rubrique active perd son soulignement tricolore.

**Pistes.** `prototypes/nom-et-logo.html` présente huit noms dont le domaine en .fr était libre le 31 octobre 2026 (vérification `whois`, registre AFNIC ; marques INPI non vérifiées) et six logos dessinés sur une grille de 32 px, avec une version redessinée pour 16 px :

| Logo | Idée | Nom associé |
|---|---|---|
| A. Règle logarithmique | graduations 1 à 10 à leur vraie position logarithmique, en encre | Mille milliards |
| B. Cote | ligne de cote d'architecte, deux flèches | Mètre étalon |
| C. Grille de cent | cent cases, vingt-quatre remplies (part des retraites) | Sur cent |
| D. Drapeau en trois traits | trois barres obliques bleu, blanc, rouge ; seule piste tricolore | (tous) |
| E. Fléau de balance | balance réduite au fléau, légèrement penchée | Le Poids |
| F. Dix puissance n | monogramme « 10ⁿ » en chasse fixe | Mille milliards |

**Décision du 31 octobre 2026 : nom « Mille milliards ».** Le porteur du projet retient le nom et le clin d'œil au capitaine Haddock (« mille milliards de mille sabords » : un navire si percé qu'il devrait couler), « avec une certaine mesure ». **Signature retenue (31 octobre 2026) : « Mille milliards de mille sabords ! »** (juron du capitaine Haddock ; forme citée dans *Les 7 Boules de cristal*, Casterman, 1948, p. 6, d'après le Wiktionnaire, à vérifier sur l'album ; « mille » invariable). Écartées : « Ni naufrage, ni croisière », « On compte, vous jugez », etc. Précautions : **avis d'un juriste avant mise en ligne** (la signature reprend mot pour mot une réplique de Hergé ; recherche INPI du 31 octobre : aucune marque « mille sabords », recherche « mille milliards » bloquée) ; ne rien emprunter d'autre à l'univers de Tintin (dessin, personnage, navire) ; vérifier la marque à l'INPI avant de réserver `millemilliards.fr` et `.com` (libres le 31 octobre 2026).

**Logo retenu : la grille aux couleurs du drapeau, en 6 × 6** (demande du porteur du projet). Spécimen : `prototypes/logo-mille-milliards.html`.

- 36 cases, deux colonnes par couleur, qui **se remplissent par le bas** (ligne par ligne, de gauche à droite) ; les cases vides restent grises (choix du porteur du projet, 31 octobre 2026).
- **Le logo est un dessin, pas un graphique** (décision du porteur du projet, 31 octobre 2026) : il ne représente aucun chiffre et n'a pas à être mis à jour.
- Sur fond clair, les cases blanches remplies sont blanches avec un filet gris fin ; les cases vides sont gris clair (`#E6E4DD`). Sur fond sombre : blanc cassé et `#2A2D34`.
- **Motif retenu (31 octobre 2026) : grille 6 × 6 (deux colonnes par couleur), 4 lignes pleines moins 1 case à droite.** Préférée au 9 × 9, dont les cases faisaient moins de 2 px dans l'en-tête (24 px) ; en 6 × 6, environ 3,5 px. Ni case isolée, ni case à moitié remplie. Icône de 16 px : 3 × 3, 2 lignes moins 1 case. Générateur : `research/scripts/make_logo.py`.
- Variantes : grille pleine (sans chiffre) et version une couleur. La variante « avec sabords » (cases ouvertes) est abandonnée.
- Usage dans le site, distinct du logo : des grilles 9 × 9 chiffrées (une case = 1/81 du PIB, 1,2 point) avec légende et source (retraites 11 cases, déficit 4 cases, dette : la grille déborde).
- Le logo porte le tricolore : le filet sous l'en-tête devient un trait gris de 1 px (un seul tricolore par écran, §6).

## 3. Couleurs

Une page en papier chaud et encre presque noire. Un seul accent, l'indigo, réservé à l'interaction (liens, focus). L'ocre marque l'emprunt et le déficit, sans jugement. Les trois couleurs du drapeau sont isolées dans des jetons à part (`--f-*`) que les graphiques n'ont pas le droit d'utiliser.

| Jeton | Rôle | Clair | Sombre |
|---|---|---|---|
| `--paper` | fond de page | `#F7F6F2` | `#0F1013` |
| `--surface` | cartes, graphiques | `#FFFFFF` | `#17191E` |
| `--ink` | texte, France, mesure | `#16181D` | `#ECEAE4` |
| `--muted` | texte secondaire, sources | `#5A5F69` | `#A3A7AF` |
| `--line` | filets, bordures | `#DEDCD5` | `#2C2F36` |
| `--accent` | liens, focus | `#3A3FB8` | `#A5A9FF` |
| `--accent-soft` | fond d'un lien actif | `#E8E8F7` | `#24264A` |
| `--bar` | barres de comparaison | `#767B84` | `#6C717B` |
| `--track` | fond des barres (piste) | `#E9E8E3` | `#25282E` |
| `--ochre` / `--ochre-bar` | emprunt, déficit (texte / aplat) | `#8A5A00` / `#9E6C0A` | `#E8B04F` / `#D69B33` |
| `--f-bleu` | filet tricolore | `#0055A4` | `#5B8FE0` |
| `--f-blanc` (+ filet `#B9B7AF`) | filet tricolore | `#FFFFFF` | `#F4F3EF` |
| `--f-rouge` | filet tricolore | `#EF4135` | `#F0605A` |

**Contrastes vérifiés.** Ratios WCAG 2.1 calculés par un script (formule de luminance relative) le 31 octobre 2026. Seuils : 4,5 pour le texte courant, 3 pour les éléments graphiques et les filets. Aucune paire sous le seuil.

| Paire | Clair | Sombre | Seuil |
|---|---|---|---|
| encre sur papier | 16,42 | 15,81 | 4,5 |
| encre sur surface | 17,76 | 14,62 | 4,5 |
| texte secondaire sur papier | 5,93 | 7,89 | 4,5 |
| texte secondaire sur surface | 6,41 | 7,29 | 4,5 |
| indigo sur surface | 8,13 | 8,14 | 4,5 |
| indigo sur fond d'accent | 6,70 | 6,70 | 4,5 |
| ocre (texte) sur surface | 5,93 | 9,01 | 4,5 |
| surface sur encre (bouton) | 17,76 | 14,62 | 4,5 |
| encre sur piste | 14,47 | 12,28 | 3 |
| barre grise sur surface | 4,25 | 3,59 | 3 |
| barre grise sur piste | 3,47 | 3,01 | 3 |
| barre ocre sur surface | 4,56 | 7,20 | 3 |
| barre ocre sur piste | 3,72 | 6,05 | 3 |
| filet bleu sur papier | 6,85 | 5,84 | 3 |
| filet rouge sur papier | 3,55 | 5,91 | 3 |

Le gris de comparaison en thème sombre (3,01 sur la piste) est juste au seuil : ne pas l'éclaircir sans refaire le calcul.

## 4. Typographie

Trois familles, toutes sur Google Fonts :

- **Instrument Sans** (texte et interface) : grotesque contemporaine, chiffres nets, grande hauteur d'x, bonne lecture à 17 px. Elle évite les choix trop vus (Inter, Roboto, Space Grotesk) sans perdre en lisibilité. Repli possible si les tests de lecture B1 sont mauvais : Atkinson Hyperlegible Next.
- **Instrument Serif** (titres 1 et 2 seulement, à partir de 28 px) : un empattement fin qui donne le ton « éditorial » et élégant. Jamais en dessous de 28 px, jamais pour un chiffre.
- **Geist Mono** (tous les chiffres affichés) : chasse fixe, donc les colonnes de chiffres s'alignent et un chiffre qui change ne fait pas bouger la ligne.

| Niveau | Police | Taille (téléphone → bureau) | Interlignage |
|---|---|---|---|
| Titre 1 | Instrument Serif 400 | 36 → 60 px | 1,05 |
| Titre 2 | Instrument Serif 400 | 28 → 40 px | 1,1 |
| Titre 3 | Instrument Sans 600 | 20 px | 1,3 |
| Chapeau | Instrument Sans 400 | 19 px | 1,55 |
| Texte | Instrument Sans 400 | 17 px | 1,6 |
| Petit (sources, légendes) | Instrument Sans 400 | 14 px | 1,5 |
| Surtitre | Instrument Sans 500, capitales, +0,06 em | 13 px | 1,4 |
| Chiffre-clé | Geist Mono 500 | 24 → 44 px | 1,05 |

Règles : texte aligné à gauche, jamais justifié ; 64 caractères par ligne au plus ; typographie française (espace insécable avant « : », espace fine avant « ; ! ? », guillemets « », `151,6 Md€` avec espace insécable).

## 5. Espacements et rayons

- **Grille d'espacement** : 4, 8, 12, 16, 24, 32, 48, 72 px. Marge latérale de 16 px sur téléphone (plus la zone de sécurité de l'écran).
- **Rayons** : 4 px (petits éléments), 8 px (cartes, graphiques, boutons), pilule pour les pastilles. Rien d'autre.
- **Filets** : 1 px partout ; 2 px seulement pour le tricolore et pour le bord gauche du bloc « Ce qui est vrai ».
- **Cibles tactiles** : 48 px de haut au moins pour les boutons, 44 px pour les pastilles et les leviers du simulateur.

## 6. Le tricolore en filets

| Oui (il signe le site) | Jamais (il porterait un sens) |
|---|---|
| Le logotype (grille 6 × 6 remplie par le bas) et l'icône de l'onglet (grille 3 × 3). | Dans un graphique, une barre, une légende ou une carte de pays. |
| ~~Un filet de 2 px sous l'en-tête~~ : remplacé par un trait gris de 1 px, puisque le logo porte déjà le tricolore. | Sur un bouton, une carte « Oui, mais… » ou une réponse. |
| Jamais la rubrique active de la navigation (retirée le 31 octobre 2026). | Pour opposer deux idées, deux camps, une hausse et une baisse. |
| Un filet en bas de l'image de partage sur les réseaux sociaux. | En aplat, en drapeau dessiné, en cocarde, avec une Marianne. |

**Le blanc.** Sur fond clair, le segment blanc reçoit un filet gris de 0,5 px (`#B9B7AF`) pour rester visible ; sur fond sombre, il est en blanc cassé sans filet. **Dosage (revu le 31 octobre 2026)** : un seul tricolore par écran. C'est le logo (grille 6 × 6) ; le filet d'en-tête est gris et la rubrique active est soulignée d'un filet d'encre de 1 px.

## 7. Graphiques

**Couleurs.** Encre pour la France ou la mesure dont parle la page ; gris pour les points de comparaison ; ocre hachuré pour l'emprunt et le déficit ; piste claire pour « le reste ». Ni bleu ni rouge.

**Règles communes :**

1. Un titre qui dit la mesure, l'unité et l'année ; un sous-titre qui dit le champ.
2. Étiquettes directes au bout des barres, pas de légende séparée.
3. Cinq séries au plus ; au-delà, couper le graphique.
4. Sous chaque graphique, une phrase **« Lecture : »** qui traduit le dessin en un chiffre daté, puis une ligne **« Source : »** (organisme, base, date) ; « calcul du site » quand le chiffre est dérivé.
5. Axe à zéro pour toute barre ; trois ou quatre graduations au plus.
6. SVG dessinés à la largeur réelle de l'écran (pas d'image réduite) : le texte reste à 12-14 px sur téléphone.

**Les quatre formes de base :**

- **Barres de comparaison** (« Et ailleurs ? ») : une ligne par pays, nom au-dessus de la barre (lisible à 390 px), France en encre et en gras, écart signalé par une accolade en pointillé. Exemple du spécimen : dépense publique 2025, France 57,3 % du PIB, zone euro 49,7 %, écart de 7,6 points, 2e de l'UE.
- **Barre de fourchette** (pages de réponse) : la piste représente le déficit de référence (151,6 Md€ en 2025) ; la partie sûre en encre, le reste de la fourchette en encre à 35 %, deux traits verticaux aux bornes. Exemple : « taxer les plus aisés », 10 à 25 Md€, soit 7 à 16 % du déficit.
- **Calendrier** (accueil, pages de sujet) : une année de 365 jours en une barre, initiales des mois dessous, le poste en encre, l'emprunt hachuré en ocre à partir du 29 novembre. Exemple : vieillesse, 23,4 % de la dépense, environ 85 jours (COFOG 2024).
- **Mini-barre** (cartes « Oui, mais… ») : 6 px de haut, part du déficit, sans axe.

## 8. Composants

- **Carte « Oui, mais… ».** Surtitre en chasse fixe (« Oui, mais… · 10 à 25 Md€ »), la phrase entendue en Instrument Serif entre guillemets, une ligne de réponse, la mini-barre, « Lire la réponse → ». Aucune étiquette de camp. Les cartes sont classées par montant ; la règle est écrite sous la liste.
- **Blocs de la page de réponse.** Blocs numérotés, de même style : « Ce qui est vrai » (toujours premier, bord gauche de 2 px en encre), « Combien » (le chiffre en grand), « Les limites », « Qui dit quoi », « Et ailleurs ? ». Pas de couleur de verdict.
- **Pastille chiffre.** Le chiffre en chasse fixe, souligné en pointillé. Au toucher, un encadré s'ouvre sous la ligne (pas d'infobulle flottante) avec les autres unités et la source.
- **Pastille source.** Organisme et date en pilule (« Eurostat 21.10.2026 ↗ »), qui ouvre la source. Les étiquettes d'organisme reprennent mot pour mot le glossaire (« Fondation iFRAP (libérale) », « Terra Nova (centre gauche) »).
- **Compteur du simulateur.** Barre en encre pleine, collée en bas de l'écran (`position: sticky`), avec « Il reste à trouver » et le montant en grand, plus une jauge fine. C'est le seul élément autorisé à recouvrir le contenu (leçon du *Debt Fixer*, étape 2, §7.5) ; il ne doit jamais masquer les boutons Retour / Suivant.
- **Boutons.** Plein (encre) pour l'action principale, contour pour l'action secondaire ; 48 px de haut.
- **En-tête.** Fixé en haut, translucide (flou d'arrière-plan), logotype, navigation (masquée sous 720 px ; rubrique active soulignée d'un filet d'encre de 1 px), bouton de thème, filet tricolore.

## 9. Mouvement

Minimal et utile. Une barre peut se remplir une fois à l'apparition (0,6 s) ; la jauge du compteur suit les choix (0,3 s). Survol : changement de bordure, sans déplacement. Tout mouvement est coupé si le lecteur a demandé à réduire les animations (`prefers-reduced-motion`). Rien ne tourne, rien ne clignote, rien ne défile tout seul.

## 10. Thèmes clair et sombre

Le site suit le réglage du téléphone (`prefers-color-scheme`) et propose un bouton pour le forcer ; le choix est gardé dans le navigateur. Les deux thèmes partagent les mêmes jetons : aucun composant ne fixe de couleur en dur.

## 11. À éviter

1. **Tout ce qui fait « site de l'État »** : Marianne, bloc-marque, police Marianne, grille et composants du DSFR, bleu `#000091`, rouge `#E1000F`.
2. **Bleu contre rouge, vert contre rouge**, ou tout code couleur qui désigne un camp ou un verdict.
3. **Les pièges vus à l'étape 2** : texte justifié, bouton flottant sur le texte, bandeau cookie collé, infobulles à toucher une par une, légendes à décoder.
4. **Les effets de mode** : dégradés, ombres portées marquées, verre dépoli hors de l'en-tête, illustrations 3D, émojis.
5. **Un chiffre sans source** : tout nombre affiché vient de `platform/data/figures.json` et passe par `validate.py --strict`.

## 12. Points à trancher

1. **Nom et logo** : « Mille milliards » et grille 6 × 6, 4 lignes moins 1 (dessin, sans chiffre), retenus le 31 octobre 2026 ; reste à vérifier la marque (INPI), réserver domaine et comptes.
2. **Polices** : confirmer Instrument Sans après un test de lecture sur téléphone auprès de quelques lecteurs B1 ; repli possible, Atkinson Hyperlegible Next.
3. **Indigo d'interaction** : il reste éloigné du bleu du drapeau, mais un lecteur pourrait y voir du bleu. Variante possible : liens en encre soulignés.
4. **Calendrier** : il combine une part par fonction (COFOG 2024) et le déficit 2025 ; à aligner sur le même millésime quand l'Insee publiera la COFOG 2025 (décembre 2026).
