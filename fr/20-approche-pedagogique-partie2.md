# 20 - Approche pédagogique : comment expliquer honnêtement les finances publiques françaises (2e partie, §5 à la fin)

*Traduction française de la seconde partie (§5 au §11, journal de vérification et sources) du fichier anglais [`20-pedagogical-approach.md`](../research/20-pedagogical-approach.md), dans sa version du 25 octobre 2026. En cas d’écart, les chiffres de [`../platform/data/figures.json`](../platform/data/figures.json) et de [`research/00-reference-figures.md`](../research/00-reference-figures.md) prévalent. La terminologie, la typographie et les titres des sources suivent [`glossaire-et-conventions.md`](glossaire-et-conventions.md). Les renvois aux §0 à §4 visent la première partie du fichier (traduction : [`20-approche-pedagogique.md`](20-approche-pedagogique.md) ; version anglaise : [`../research/20-pedagogical-approach.md`](../research/20-pedagogical-approach.md)) ; « fichier NN » désigne le fichier `NN-….md` de [`../research/`](../research/README.md) et « ligne NN du fichier 00 » une ligne du tableau de [`00-reference-figures.md`](../research/00-reference-figures.md). Les chemins `data/…` s’entendent par rapport à `research/`.*

---

## 5. « Équilibrez vous-même le budget » : spécification du simulateur

### 5.1 Objectifs de conception

1. **Enseigner des arbitrages, pas une bonne réponse.** Pas de « score ». L’utilisateur voit les conséquences : la dette en 2032, le taux de PO, le ratio de dépense publique, qui est concerné (par décile quand on le sait) et le degré de confiance.
2. **Chaque montant en euros vient de la base de recherche**, avec une pastille source et une fourchette. Aucun levier ne porte une valeur absente de la base de recherche. Les valeurs manquantes sont affichées « non chiffré » et le levier est désactivé, ou autorisé seulement en mode « personnalisé » avec un avertissement.
3. **Menu symétrique** : autant de leviers de recettes que de leviers de dépenses, plus des leviers « croissance et réformes structurelles », et des propositions marquées à gauche et à droite également visibles. *(Note du 25 octobre 2026, synchronisation 15-18 : les leviers « cibles souvent citées » S13 à S19 forment un seul groupe repliable, « Cibles souvent citées », placé au même niveau et avec la même visibilité que le groupe de recettes « Taxer les très hauts patrimoines » (R1 à R5), pour que le menu principal reste équilibré.)*
4. **Les effets de bouclage macroéconomique sont montrés, pas cachés.** L’effet d’une mesure sur la croissance se répercute sur le déficit (§5.4). Par défaut, le simulateur applique les multiplicateurs publiés par instrument, avec des fourchettes (fichier 17, §8) ; l’utilisateur peut les désactiver pour voir le chiffre statique.

### 5.2 Objectifs que l’utilisateur peut choisir

| Objectif | Md€ à trouver (base 2025, statique) | Calcul | Source |
|---|---|---|---|
| A. Empêcher le ratio de dette de monter | **≈ 90** | Écart avec le solde primaire stabilisant la dette, 3,0 pts de PIB | Cour des comptes, juin 2026[^cour26] |
| B. Atteindre la limite de 3 % de Maastricht | **≈ 62** | 151,6 − 3 % × 2 991,1 = 151,6 − 89,7 | Calcul d’après [^ref] |
| C. Équilibrer le budget | **151,6** | Totalité du déficit | [^ref] |
| D. Stabiliser durablement la dette d’ici 2032 (avancé) | **≈ 125** par rapport à l’évolution tendancielle à politique inchangée | Excédent primaire de 0,8 % du PIB | Mission de l’IGF, juillet 2026[^igf] |
| Option « vent contraire automatique » (activée par défaut) | **+25** | Intérêts de 65,7 à 91 Md€ (de 2025 à 2027) | [^ref] lignes 39-40 |
| Options de pression (désactivées par défaut) | Défense à 3,5 % (OTAN) : +44 ; climat (part publique) : de +25 à +34 | | fichier 08[^f08] |
| Effets de bouclage macroéconomique (activés par défaut, §5.4) : mesures brutes nécessaires | Objectif B : **≈ 94** de mesures pour obtenir 62 nets avec m = 0,6 ; objectif A : ≈ 137 pour obtenir 90 nets | 61,9 / (1 − 0,6 × 0,57) = 61,9 / 0,658 = 94,1 ; 90 / 0,658 = 136,8. Le chiffre réel dépend de la combinaison de leviers (chaque levier a son propre multiplicateur) | ligne 62 du fichier 00 ; fichier 17, §8[^f17] |

*La version 1 est un simulateur statique sur une seule année, en base 2025 (clairement étiqueté « si appliqué à 2025 »). La version 2 (après la publication de l’Insee de mars 2027) ajoute une trajectoire 2027-2032 fondée sur la trajectoire du HCFP et de l’IGF, avec des profils de montée en charge pour les retraites et les effets de comportement.*

### 5.3 Liste des leviers (version 1)

Positif = améliore le solde. « Statique » = rendement mécanique ; « Comportemental » = après les effets de comportement documentés. La confiance suit le fichier 07 : H (haute) / M (moyenne) / L (faible).

**A. Leviers de recettes**

| N° | Levier | Plage du réglage | Statique (Md€) | Après effets de comportement ou contraintes juridiques (Md€) | Conf. | Source | Notes affichées à l’utilisateur |
|---|---|---|---|---|---|---|---|
| R1 | Taxe Zucman (impôt plancher de 2 % au-delà de 100 M€) | oui/non | 20 (15 à 25) | 5 (2 à 6) | L | fichier 07, §3.1 | Signal de risque constitutionnel ; l’assiette est concentrée (trois départs la diviseraient par deux) |
| R2 | Rétablir l’ISF (net de l’IFI) | oui/non | 3 à 4,5 brut / 2 à 3 net | plus faible (non quantifié) | M | fichier 07 | Ne peut pas être cumulé en totalité avec R1 (assiettes qui se recoupent) : l’outil plafonne la combinaison R1+R2 à la fourchette du fichier 07, §5 (3 à 10) |
| R3 | Supprimer le prélèvement forfaitaire unique (PFU, « *flat tax* ») | oui/non | de 3,2 (Montaigne) à 9 (chiffre annoncé par LFI) | — | M/L | fichier 07 | Afficher les deux ; 3,2 par défaut |
| R4 | Réforme des droits de succession visant les gros patrimoines | 0 à 3 positions | 3 à 10 | non chiffré | L | fichier 07, §5 | « Aucun chiffrage indépendant trouvé » |
| R5 | Renforcer la CDHR | oui/non | 0,5 à 1 | base observée | H | fichier 07 | Le test grandeur nature de la taxation des hauts revenus |
| R6 | Surtaxe d’impôt sur les sociétés pour les grandes entreprises (reconduite) | oui/non | 8,0 (ponctuelle en 2025) | — | H | fichier 07 | Ponctuelle en 2025 ; la reconduire est un choix |
| R7 | TVA, tous les taux | −1 à +2 pts | 8,2 net par point (13 brut) | — | M/H | fichier 07 | Régressive : l’Insee estime que les prélèvements sur la consommation accroissent les inégalités de 3,9 points de Gini |
| R8 | « Année blanche » (gel du barème de l’IR, des pensions et des prestations) | oui/non | 4,4 à 5,7 | — | M/H | IPP via le fichier 07 | Régressive dans l’ensemble (IPP) |
| R9 | Dépenses fiscales (« niches fiscales ») : réduire de x % les 91,8 Md€ | 0 à 30 % | x % × 91,8 | plus faible ; non modélisé | M | fichier 05, §7.1 | 474 mesures ; coût réel connu pour 55 % seulement ; les postes les plus importants sont listés (CIR 7,1 ; crédit d’impôt pour l’emploi d’un salarié à domicile 7,1 ; abattement de 10 % sur les pensions 5,6 ; pacte Dutreil 3,8) |
| R10 | Plafonner l’abattement de 10 % sur les pensions à 3 000 € | oui/non | 1,4 | — | M | PLF 2027 via le fichier 07 | |
| R11 | Allègements généraux de cotisations patronales (environ 75 Md€) | suppression de 0 à 100 % | linéaire, jusqu’à 75 | jusqu’à environ 48 nets à 100 %, avec **−980 000 emplois (ETP)** | M | Bozio-Wasmer via le fichier 08 | Compteur des pertes d’emplois affiché à côté |
| R12 | Plan de lutte contre la fraude | oui/non | 1 à 3 | — | M | fichier 07 | Étiquette « non crédible » au-delà de 3 (HCFP) |
| R13 | Recettes annoncées par les partis (taxe sur les rachats d’actions 8,4 ; « ISF climatique » 10 ; taxe sur les multinationales…) | personnalisé | chiffre annoncé | divisé par deux (convention, fichier 11, §5.1) | L | fichiers 07, 11 | Affiché sous « chiffres annoncés », en gris |

**B. Leviers de dépenses**

| N° | Levier | Plage | Statique (Md€) | Comportement / macroéconomie | Conf. | Source | Notes |
|---|---|---|---|---|---|---|---|
| S1 | Âge légal de départ à la retraite | 60 ↔ 66 | de 64 à 63 ans : −5,8 (système de retraite) / −13 (ensemble des finances publiques, 2035) ; à 62 ans : de −10 à −17 (système), environ −26 avec les recettes induites ; à 60 ans (retour général) : de −43 à −58 *(corrigé le 25 octobre 2026, c’était de −35 à −58 ; fichier 00, ligne 44)*. +1 an : de +0,3 à +0,65 pt de PIB (≈ de +9 à +19) en 10 à 20 ans | Montée en charge en 2 à 4 ans ; modèles de la DG Trésor et de l’OFCE | M | fichier 03, §4 | Bascule court terme / long terme |
| S2 | Revalorisation des pensions (mesure du PLFSS 2027 : pensions, de base et complémentaires, revalorisées en totalité jusqu’à 1 260 € par mois seulement, moins au-delà ; une sous-indexation partielle, pas un gel) *(libellé corrigé le 25 octobre 2026, point 5 de REVIEW.md : était « gel d’un an des pensions de base, plus petites pensions protégées »)* | oui/non | environ 4,1 (économies du PLFSS 2027 : 3,0 pour les régimes de base + 1,1 pour l’État, nettes de CSG et de CASA) | — | M/H | fichier 03 | Recoupe R8 (l’outil empêche le double compte) |
| S3 | Point d’indice de la fonction publique | de −1 à +10 % par rapport au gel | 2,1 à 2,4 par point | — | M | fichier 07, §3.6 | Chaque borne a sa propre source *(ajouté le 25 octobre 2026, point 2 de REVIEW.md)* : **2,4** = cabinet du ministre, juillet 2026, rapporté par *Acteurs publics* et Selectra (presse ; étiquette « chiffre du cabinet du ministre, tel que rapporté ») ; **2,1** = calcul de la plateforme : la hausse de 1,5 % de juillet 2023 a coûté environ 3,2 en année pleine pour les trois versants (presse citant la fiche d’impact du décret), et 3,2 / 1,5 = 2,13 ; cohérent avec les 20 de l’Institut Montaigne pour +10 % (2 par point). Recoupement officiel partiel : le coût de la hausse de 2023 pour le versant de l’État, 1,5, est confirmé par le Sénat (avis n° 134 sur le PLF 2024). Pas de source primaire de la DGAFP ; la ventilation à 2,07 (⚠) n’est pas utilisée |
| S4 | Effectifs publics | curseur | **non chiffré dans la base de recherche** | — | — | — | Désactivé en v1 ; la v2 a besoin d’un coût moyen par ETP fourni par la DGAFP |
| S5 | Progression de l’Ondam (santé) | 0 à 5 % ; **+3,4 % par défaut** | 0,27 par tranche de 0,1 pt (sur 273,3 Md€), mesuré à partir de la valeur par défaut | Arbitrage entre qualité et accès aux soins | M (calculé) | fichier 02, §4.3 ; fichier 12, §7.2 | Affiche des indicateurs d’accès (pénurie de médecins généralistes : 29 % de la population). **Valeur par défaut et repères** *(fixés le 25 octobre 2026, point 4 de REVIEW.md)* : le curseur part de la **progression tendancielle 2027 de +3,4 %** (CCSS, telle qu’indiquée dans le PLFSS 2027), situation de référence à politique inchangée : le rendement par défaut est donc nul. Repères étiquetés : **+2,0 %** = objectif du PLFSS 2027 (278,7 Md€, projet de loi n° 3211, art. 43) ; **de 2 à 2,5 %** = la trajectoire « plus exigeante » demandée par la Cour des comptes (RALFSS, mai 2026). Contrôle : de 3,4 % à 2,0 % = 14 × 0,27 ≈ 3,8 Md€, proche des 3,9 Md€ d’économies nettes sur l’Ondam du PLFSS 2027 selon la Cour des comptes |
| S6 | Restructuration du système de santé (administration, soins peu pertinents) | oui/non | **gisement, pas rendement** : écart de frais administratifs ≈ 6 ; soins peu pertinents 22 (Cour des comptes, extrapolé) | Pluriannuel, incertain | L | fichier 12 | Affiché comme « potentiel, pas un chiffre budgétaire » |
| S7 | Aides publiques aux entreprises ciblées (périmètre 1 du Haut-commissariat à la Stratégie et au Plan, 82 Md€) | réduction de 0 à 30 % | linéaire | Effets inconnus (faute d’évaluation) | L | fichier 08 | |
| S8 | Prestations familiales / minima sociaux | réduction de 0 à 10 % | x % × (famille 65,8 + pauvreté 34,0, Drees 2024) | Effet sur le taux de pauvreté non modélisé ; alerte sur la pauvreté des enfants | M | fichier 02, §3.2 | Périmètre Drees (tous régimes) : signalé |
| S9 | Gels de prix et TVA sur l’énergie | oui/non | TVA à 5,5 % sur l’énergie : environ −11, une borne basse (Institut Montaigne 2024 : « plus de 11 » ; chiffre propre du RN −12,2) ; les −17,4 de francebudget.fr ne sont pas retenus (fichier 07, §3.5). Carburant à 1,70 € : de 0 à −26,5 (curseur du prix du pétrole). *(Corrigé le 25 octobre 2026, point 2 de REVIEW.md : la TVA sur l’énergie était « de −11 à −17,4 ».)* | Non ciblé (Cour des comptes) | M | fichiers 07, 11 | |
| S10 | Smic porté entre 1 600 et 1 700 € net | oui/non | de −1,8 à −4 : 1 600 € net, environ de −1,8 à −2,2 ; 1 700 € net, environ de −3,5 à −4 (mise à l’échelle, par la plateforme, du chiffrage de l’Institut Montaigne de 2024 au Smic en vigueur depuis juin 2026 ; fichier 11) *(corrigé le 25 octobre 2026, point 3 de REVIEW.md : était « de −3,5 à −4 »)* | Effet sur l’emploi non chiffré | M | fichiers 07, 11 | Signalé « illustratif » (calcul de la plateforme) |
| S11 | Économies liées à l’immigration (chiffres annoncés) | oui/non | de +8 (RN 2024) à +15,1 (RN 2027) annoncés ; LR +10 | Fragilité juridique (décision du Conseil constitutionnel n° 2024-6 RIP) ; 92 % du bloc RN « non documenté ou juridiquement fragile » (Institut de l’Entreprise) | L | fichier 07 ; fichier 15, §6 | « Chiffre annoncé » en gris. Pastille de contexte : contribution budgétaire nette de +1,02 % à −0,85 % du PIB (ligne 55 du fichier 00) ; AME 1,34 Md€ (ligne 54 du fichier 00). Recoupe S19 (la ligne AME → AMU fait partie du bloc RN) |
| S12 | Plafonnement de la contribution à l’UE à 5 Md€ | oui/non | +11,1 annoncés (2027). **Plafond même si c’était légal : de 1,4 à 4,5** (solde net de 6,4 ou 9,5, moins 5) | Conflit avec les traités : décision relative au système des ressources propres (unanimité, ratifiée) ; rendement légal d’une mesure unilatérale ≈ 0 | Très faible | fichier 07 ; fichier 16, §3 ; ligne 52 du fichier 00 | « Chiffre annoncé » en gris ; le réglage affiche la barre du chiffre annoncé à côté du plafond de 1,4 à 4,5 et de la contribution nette vérifiée (9,5 / 6,4). *(Mis à jour le 25 octobre 2026, synchronisation 15-18.)* |

**B2. Groupe « Cibles souvent citées » (ajouté le 25 octobre 2026, synchronisation 15-18 ; fichier 16)** *(Libellé corrigé le 25 octobre 2026, point 10 de REVIEW.md : « Cibles populaires » pouvait se lire « cibles des classes populaires ».)*

| N° | Levier | Plage | Statique (Md€) | Comportement / contraintes juridiques | Conf. | Source | Notes |
|---|---|---|---|---|---|---|---|
| S13 | Mission budgétaire *Aide publique au développement* (programmes 110, 209, 365, 370, 384) | réduction de 0 à 100 % de 3,17 (CP du PLF 2027) | x % × 3,17 | Engagements internationaux ; réduire la mission ne réduit pas l’APD au sens de l’OCDE (12,9) à due proportion | H (ligne budgétaire) | fichier 16, §2 ; ligne 53 du fichier 00 | Le PLF 2027 intègre déjà une baisse de 0,40 par rapport à la LFI 2026. Recoupement : 0,20 des financements de l’État aux associations relèvent de l’aide (S18) |
| S14 | Opérateurs et agences de l’État | 3 positions : réforme structurelle du Sénat / baisse de 8 % de tous les effectifs et frais de fonctionnement / chiffre du gouvernement de 2025 | 0,54 / 2,2 / 2 à 3 | 2,2 n’est « pas à missions constantes » (Sénat) ; 2 à 3 n’a pas de méthode publiée | M / L / « chiffre annoncé » en gris | fichier 16, §4 | Lien vers la carte proportionnelle (*treemap*) : l’essentiel des financements va aux universités, à la recherche, à la formation et au logement |
| S15 | Conseil en stratégie et organisation | 0 à 100 % | 0,06 au maximum | — | H | fichier 16, §5 | Le maximum du curseur montre combien la ligne est désormais petite (Sénat 2021 : 1,07 sur un périmètre plus large) |
| S16 | Mission *Pouvoirs publics* + cabinets ministériels | réduction de 0 à 50 % de 1,3 | 0,65 au maximum | Les budgets du Parlement et du Conseil constitutionnel sont fixés par ces institutions elles-mêmes | H | fichier 16, §6 | Présidence 0,123 ; Parlement 0,98 |
| S17 | Audiovisuel public | réduction de 0 à 100 % de 3,82 ; ou « privatisation » du RN (chiffre annoncé 1,6) | x % × 3,82 / 1,6 annoncé | Une privatisation rapporte un prix de cession ponctuel, pas une économie récurrente ; faisabilité « incertaine » (Montaigne) | M / « chiffre annoncé » en gris | fichier 16, §7 | L’audiovisuel extérieur (France Médias Monde, TV5) et l’INA resteraient probablement publics |
| S18 | Financements de l’État aux associations | réduction de 0 à 20 % de 10,5 | x % × 10,5 (10 % = 1,05) | Réductions de services rendus (hébergement, accueil des demandeurs d’asile, aide juridique) | M | fichier 16, §8 | Les 1,6 de l’iFRAP incluent les collectivités territoriales (hors de ce levier). Recoupe S13 (0,20) et S11 (associations liées à l’immigration 0,94) |
| S19 | AME | réduction de 0 à 100 % de 1,34 (dépense 2025) ; ou « AME → AMU » du RN (chiffre annoncé 1,3) | x % × 1,34 / 1,3 annoncé | Aucun chiffrage officiel d’un dispositif limité à l’urgence ; les soins urgents (0,07) et les créances irrécouvrables des hôpitaux demeurent ; le rapport Évin-Stefanini déconseille le remplacement | L / « chiffre annoncé » en gris | ligne 54 du fichier 00 ; fichier 15, §6.1 | Les crédits de 1,208 (action AME, PLF 2027) sont inférieurs à la dépense réelle : la ligne est chroniquement sous-budgétée. Recoupe S11 |

**Correspondance des effets de bouclage macroéconomique par levier (version 1, année 1 ; les valeurs « années 3 à 5 » servent dans l’onglet « 2032 »).** Valeurs tirées du fichier 17, §8 (positif = perte de PIB par euro de redressement ; même valeur de signe opposé pour les mesures qui augmentent la dépense ou baissent les impôts). « Correspondance » = la catégorie du fichier 17 à laquelle nous rattachons le levier ; quand le fichier 17 n’a pas de catégorie, la v1 utilise la valeur officielle de 0,6 pour un ensemble de mesures mixte (ligne 62 du fichier 00) avec une fourchette de ±50 % (fichier 17, §0, point 9), signalée « valeur de repli ».

| Leviers | Catégorie du fichier 17 | Année 1 par défaut (fourchette) | Années 3 à 5 par défaut (fourchette) | Note |
|---|---|---|---|---|
| R1, R2, R4 | Impôt sur les très grandes fortunes | 0,1 (0,0 à 0,3) | 0,2 (0,0 à 0,5) | ⚠ approximation d’experts, pas d’estimation directe (fichier 17, §7) ; R4 (successions) rattaché ici par nous, signalé |
| R3, R5, R6 | Surtaxe d’IS, impôts sur les revenus du capital (et les hauts revenus) | 0,3 (0,1 à 0,4) | 0,4 (0,2 à 0,8), avertissement sur le long terme | Valeurs implicites de l’OFCE : surtaxe sur les grandes entreprises 0,29 ; CDHR ≈ 0 |
| R7 ; S9 (baisse de TVA sur l’énergie, gel du prix des carburants : signe opposé) | TVA | 0,3 (0,1 à 0,5) | 0,5 (0,1 à 0,8) | Plus fort désaccord entre modèles ; afficher en alternative le gain sur le solde issu du modèle lui-même (fichier 17, §8). Le rattachement du gel du prix des carburants à la TVA est le nôtre, signalé |
| R9, R10 | Impôt sur le revenu ou CSG | 0,4 (0,1 à 0,5) | 0,8 (0,4 à 0,9) | Le rattachement de R9 est le nôtre (la plupart des grosses dépenses fiscales réduisent l’impôt sur le revenu ou l’impôt sur les sociétés) |
| R8 (« année blanche ») | Mélange : impôt sur le revenu 0,4 / indexation des pensions 0,3 / prestations en espèces 0,5 | 0,4 (0,3 à 0,5), notre point médian des composantes | 0,7 (0,6 à 0,8), notre point médian | Signalé comme composite de notre fait |
| R11 | Cotisations patronales ou impôts de production | 0,3 (0,2 à 0,4) | 0,7 (0,6 à 1,0), en hausse à long terme | Quand l’option « effets de comportement » affiche le rendement net de Bozio-Wasmer (48, avec −980 000 ETP), l’option macroéconomique n’ajoute pas un second effet sur l’emploi |
| S3, S14, S15, S16, S17 | Dépenses de fonctionnement et masse salariale publique | 0,8 (0,5 à 1,1) | 0,7 (0,4 à 1,0) | |
| S5, S6, S19 | Santé et autres transferts sociaux en nature | 0,8 (0,5 à 1,0) | 0,7 (0,4 à 0,9) | |
| S8 | Prestations sociales en espèces (âge actif, sous condition de ressources) | 0,5 (0,3 à 1,0) | 0,7 (0,4 à 0,9) | Les transferts aux ménages modestes se situent en haut de la fourchette |
| S2 | Sous-indexation ou gel des pensions | 0,3 (0,2 à 0,5) | 0,6 (0,3 à 0,8) | |
| S7 | Impôts et subventions des entreprises (notre rattachement : lignes cotisations patronales / IS) | 0,3 (0,1 à 0,4) | de 0,4 à 0,7 | Signalé comme rattachement de notre fait |
| S18 | Dépenses de fonctionnement / transferts sociaux en nature (notre rattachement) | 0,8 (0,5 à 1,0) | 0,7 (0,4 à 0,9) | Les associations rendent des services : signalé |
| S12, S13 | Contribution à l’UE ; aide au développement | 0 (0 à 0,2) | 0 | OFCE : « nul ou très faible » pour la contribution à l’UE et l’aide au développement (fichier 17, §3.3) |
| S1 | Âge de départ à la retraite (mesure d’offre) | effet sur le PIB 0,0 (de −0,1 à +0,1) | PIB +0,3 % à 10 ans (de −0,1 % à +1,1 %) ; gain sur le solde de +0,4 pt pendant 2 ans (de +0,1 à +0,9) | Appliqué aux seuls chiffres du système de retraite : les chiffres « ensemble des finances publiques » du fichier 03 incluent déjà les effets induits |
| R12, R13, S10, S11 | aucune | 0,6 (0,3 à 0,9), valeur de repli | 0,6 (0,3 à 0,9), valeur de repli | R13 et S11 sont des chiffres annoncés : le multiplicateur ne s’applique au montant annoncé que si l’option 3 est activée |
| G1, G2 | sans objet | — | — | Leviers de croissance et scénarios de risque : pas de multiplicateur |

**C. Leviers de croissance et réformes structurelles (long terme, affichés dans un onglet « 2032 » distinct)**

| N° | Levier | Plage | Effet | Source | Notes |
|---|---|---|---|---|---|
| G1 | Taux d’emploi | combler de 0 à 100 % de l’écart avec l’Allemagne (en ETP) | jusqu’à +38 Md€ de prélèvements (illustratif ; jusqu’à 84 dans le scénario en nombre de personnes) | DG Trésor via le fichier 08 | Interpolation linéaire signalée ; les politiques permettant d’y parvenir ne sont pas chiffrées |
| G2 | Choc de taux d’intérêt | de −100 à +200 pb | +3,4 Md€ la 1re année, +8,1 Md€ la 2e année par tranche de +100 pb | HCFP, §116 | Présenté comme un risque, pas comme un choix |

### 5.4 Fourchettes d’incertitude et options

- **Chaque levier porte un triplet (bas, central, haut).** La barre de synthèse affiche le total sous forme de fourchette, pas d’un chiffre unique. Exemple : R1 + R7 (+1 pt) + S1 (âge à 63 ans) = statique 20 + 8,2 − 13 = **+15,2** ; après effets de comportement 5 + 8,2 − 13 = **+0,2**. Avec l’option macroéconomique activée (valeurs par défaut de l’année 1 ; S1 est une mesure d’offre sans multiplicateur la 1re année) : statique 20 × (1 − 0,1 × 0,57) + 8,2 × (1 − 0,3 × 0,57) − 13 = 18,9 + 6,8 − 13 = **+12,7** ; après effets de comportement 5 × 0,943 + 8,2 × 0,829 − 13 = 4,7 + 6,8 − 13 = **−1,5**. *(Exemple complété le 25 octobre 2026, synchronisation 15-18.)*
- **Option 1, « effets de comportement » :** passe des valeurs statiques aux valeurs après effets de comportement là où la base de recherche les fournit (R1, R2, R5, R11). Ailleurs, elle affiche « aucune estimation des effets de comportement disponible ».
- **Option 2, « court terme / long terme » :** âge de départ à la retraite, allègements de cotisations, emploi.
- **Option 3, « inclure les chiffres annoncés par les partis non chiffrés de façon indépendante » :** désactivée par défaut.
- **Option 4, « effets de bouclage macroéconomique » (activée par défaut en v1 ; remplace « aucun multiplicateur appliqué en v1 », 25 octobre 2026, synchronisation 15-18).** Source : fichier 17, §8, vérifié dans les sources primaires de ce fichier[^f17].
  - **Règle :** amélioration nette du déficit = mesure × (1 − m × 0,57), où *m* est le multiplicateur de l’année 1 du levier (tableau de correspondance du §5.3) et 0,57 la semi-élasticité du déficit à l’écart de production (CAE, *Focus* n° 108 ; ligne 62 du fichier 00). La même règle, de signe opposé, s’applique aux mesures qui augmentent la dépense ou baissent les impôts.
  - **Valeurs par défaut (année 1, fourchette) :** dépenses de fonctionnement et rémunérations publiques 0,8 (0,5 à 1,1) ; investissement public 1,0 (0,6 à 1,4) ; santé et autres transferts sociaux en nature 0,8 (0,5 à 1,0) ; prestations en espèces aux personnes d’âge actif 0,5 (0,3 à 1,0) ; indexation des pensions 0,3 (0,2 à 0,5) ; TVA 0,3 (0,1 à 0,5) ; impôt sur le revenu et CSG 0,4 (0,1 à 0,5) ; cotisations patronales 0,3 (0,2 à 0,4) ; impôt sur les sociétés et impôts sur les revenus du capital 0,3 (0,1 à 0,4) ; impôt sur la fortune 0,1 (0,0 à 0,3, approximation) ; contribution à l’UE et aide au développement 0 (0 à 0,2) ; âge de départ à la retraite : PIB 0,0 la 1re année, +0,3 % à 10 ans (de −0,1 % à +1,1 %). Les leviers sans catégorie dans le fichier 17 utilisent la valeur officielle de 0,6 pour un ensemble de mesures mixte, avec une fourchette de ±50 % (0,3 à 0,9).
  - **Affichage :** l’indicateur de solde affiche trois nombres : le total statique (ou après effets de comportement), le **solde net après bouclage macroéconomique (valeur centrale)** et la fourchette calculée avec les multiplicateurs bas et haut. Une ligne indique l’effet sur le PIB (« votre plan réduit le PIB de 2027 d’environ X % », X = 100 × Σ mesure × m / 2 991,1). Exemple : 30 milliards d’euros de baisse des dépenses de fonctionnement rapportent net 30 × (1 − 0,8 × 0,57) = **16,3** (fourchette de 11,2 à 21,5 pour m = 1,1 à 0,5).
  - **Exceptions signalées à l’utilisateur :** pour la TVA et les cotisations patronales, la règle et les modèles divergent (gain sur le solde la 1re année par point de PIB : Mésange, cotisations patronales, règle 0,89 contre modèle 0,72 ; e-mod.fr, TVA, règle 0,89 contre modèle 0,5) ; la fiche du levier affiche en alternative le gain sur le solde issu du modèle (fichier 17, §8).
  - **Ordre des opérations :** le multiplicateur s’applique au rendement *attendu* (après effets de comportement), pas au rendement mécanique (fichier 17, §9, point 5). Quand l’option 1 est désactivée, la fiche avertit : « effets de bouclage macroéconomique appliqués à un rendement statique ».
  - **Formulation à l’écran :** « Les baisses de dépenses comme les hausses d’impôts ralentissent la croissance à court terme ; les données ne montrent pas qu’un des deux types de mesures soit indolore » (synthèse 2026 de la Cour des comptes, fichier 10, §6), reprise de la v1, désormais avec les chiffres.
  - **Ce que le simulateur ne doit pas faire (fichier 17, §8) :** présenter un multiplicateur comme une constante connue ; afficher une baisse « autofinancée » (aucune source ne justifie un m supérieur à 1/0,57 ≈ 1,75 en temps normal) ; appliquer à 2027 des valeurs de période de crise (1,5 à 2). La fourchette du FMI dans les *Perspectives de l’économie mondiale* (WEO) de 2012 (0,9 à 1,7) est ⚠ non vérifiée dans le fichier 17 et n’est pas affichée.
  - **Options de contexte (v2) :** récession ou taux plancher (multiplicateurs de dépense × environ 1,4 ; variante zone euro du SEBC de 0,98 à 1,39) ; « trajectoire crédible annoncée à l’avance » (affiche la borne du multiplicateur nul retenue dans le PSMT de 2024, jugée « très favorable » par la mission de l’IGF) ; mesures concentrées en début de période ou progressives (perte de PIB cumulée). La hausse en période de ralentissement selon Gechert-Rannenberg est ⚠ non vérifiée et n’est pas utilisée.
- **Règles contre le double compte :** R1×R2 (assiettes de patrimoine qui se recoupent), R8×S2 (gel des pensions), R9×R10 (l’abattement de 10 % est une dépense fiscale) ; ajoutées le 25 octobre 2026 : S11×S19 (la ligne AME → AMU fait partie du bloc immigration du RN), S13×S18 (0,20 milliard d’euros d’aide transitent par des associations), S11×S18 (0,94 milliard d’euros de financements aux associations liés à l’immigration), R11 comportemental × macroéconomie (pas de second effet sur l’emploi), S1 « ensemble des finances publiques » × macroéconomie (inclut déjà les effets induits).

### 5.5 Résultats affichés

| Résultat | Contenu |
|---|---|
| Indicateur de solde | Part de l’écart comblée par rapport à l’objectif choisi, sous forme de fourchette ; valeurs statique / après effets de comportement et **nette après bouclage macroéconomique** côte à côte (§5.4) |
| Effet sur la croissance | Effet du plan sur le PIB la 1re année, sous forme de fourchette (Σ mesure × m, multiplicateurs bas et haut), étiqueté « illustratif, fondé sur des modèles » |
| Étalons | Total en jours de dépense publique, en euros par habitant, en % du PIB |
| Indicateurs de structure | Taux de PO après les choix (base 43,6 %) ; ratio de dépense publique (base 57,3 %), avec la position de l’utilisateur marquée dans la distribution de l’UE-27 |
| Qui est concerné | Étiquettes qualitatives par levier (retraités, actifs, 1 % les plus aisés, entreprises, familles, tous les consommateurs) ; déciles seulement quand une estimation distributive de l’IPP ou de l’Insee existe |
| Confiance | Part du total provenant des leviers H, M ou L |
| Panneau des sources | Liste de toutes les sources utilisées dans le scénario, exportable |
| Carte de partage | « Mon plan dégage de X à Y milliards d’euros : Z jours de dépense publique », avec un lien vers le scénario exact (encodé dans l’URL) |
| Comparer avec les campagnes | Superposition, pour chaque programme 2027, du total annoncé et des totaux indépendants |

### 5.6 Points de comparaison

Renvoyer, dans l’Espace confiance, vers les simulateurs existants et expliquer les différences : le simulateur socio-fiscal de l’IPP (microsimulation), les comparateurs de l’OFCE et de l’iFRAP (fichier 11, §7). Ne pas reprendre leurs chiffres sans les citer.

---

## 6. Le quiz « Ordres de grandeur »

### 6.1 Conception

- **Mécanique :** un curseur numérique ou un choix multiple → révélation de la réponse → histogramme « ce qu’ont répondu les autres » → « pourquoi c’est important » (2 lignes) → pastille source → « Le meilleur contre-argument » (1 ligne).
- **Modes :** découverte (3 questions), complet (25), classe (résultat agrégé anonyme du groupe), « par électorat » (proximité partisane déclarée, facultative, utilisée seulement pour des travaux de recherche agrégés, avec consentement).
- **Notation :** un score fondé sur la distance logarithmique, parce que les ordres de grandeur comptent plus que les décimales. Une estimation comprise entre la valeur réelle divisée et multipliée par 1,25 obtient tous les points.
- **Règle de symétrie :** les 25 questions sont équilibrées. Des nombres à peu près égaux de questions corrigent des perceptions erronées qui servent des récits de gauche (rendement d’un impôt sur la fortune, taille des aides aux entreprises), des récits de droite (fraude, immigration, « assistanat », « train de vie de l’État », nombre de fonctionnaires) et le pessimisme général (retraités, faillite, mobilité sociale).
- **Collecte des données :** les réponses sont conservées de façon anonyme, avec consentement au titre du RGPD (lignes directrices de la CNIL). On constitue ainsi le **premier jeu de données français d’estimations chiffrées sur le budget**, qui comble la principale lacune relevée dans le fichier 14, §10. Publier les résultats chaque trimestre avec la méthode, en précisant que les répondants se sont sélectionnés eux-mêmes (échantillon non représentatif).

### 6.2 Perceptions erronées documentées sur lesquelles s’appuie le quiz (sondages)

| N° | Croyance ou réponse | Enquête (commanditaire, institut, terrain, effectif) | Valeur réelle | Écart | Source |
|---|---|---|---|---|---|
| 1 | **Dette estimée en moyenne à 76 % du PIB** ; 37 % « ne savent pas » ; 25 % seulement répondent « plus de 100 % » | Ipsos, **18-21 janvier 2021, n = 1 000**, panel en ligne, méthode des quotas. Client : **MINEFI** (ministère de l’Économie et des Finances), « pour nourrir la réflexion de la *Commission sur l’avenir des finances publiques* » installée par le Premier ministre le 4 décembre 2020 (rapport Ipsos, diapositives « Rappel des objectifs »). Publiée comme *pièce jointe n° 4* du rapport de la commission Arthuis (remis le 18 mars 2021), rapport 279092 de vie-publique.fr. *(Vérifié le 25 octobre 2026 : la mention était auparavant « commanditaire probable… non confirmé ».)* | 98,2 % (fin 2019) ; 114,9 % (fin 2020, millésime actuel) | Sous-estimée d’environ 22 à 39 points | [^ipsos21] ; `data/insee_dette_maastricht_1978_2025_by_subsector.csv` |
| 2 | 73 % se sentent mal informés sur le niveau et le coût de la dette | idem | — | — | [^ipsos21] |
| 3 | Causes de la dette (jusqu’à 3 réponses) : « mauvais choix politiques » 54 %, « crises » 50 %, « mauvaise gestion des administrations et des collectivités » 45 % ; « niveau élevé de protection sociale » **30 %** ; « pertes de recettes dues à certaines réformes » **21 %** | idem | Protection sociale + santé = 57 % des dépenses publiques ; baisses d’impôts et de cotisations décidées de 2018 à 2023 = 62 Md€ par an | Les deux explications structurelles (dépenses sociales et baisses d’impôts) sont sous-citées | [^ipsos21] ; [^ref] |
| 4 | Principal responsable de la dette : l’État 55 %, la sécurité sociale 22 %, les collectivités territoriales 8 % | idem | Part de la dette au sens de Maastricht fin 2020 : **État 78 %**, administrations de sécurité sociale 10 %, administrations publiques locales 8,5 % (calcul : 2 089 / 273 / 228 sur 2 664 Md€) | **Ici, le public a globalement raison.** Le présenter comme un moment « vous aviez vu juste » | [^ipsos21] ; `data/insee_dette_maastricht_1978_2025_by_subsector.csv` |
| 5 | Dépenses à réduire en priorité : « train de vie » de l’État et des services publics 67 %, prestations sociales y compris retraites 14 %, collectivités territoriales 8 % | idem | Protection sociale 41,5 % + santé 15,6 % des dépenses publiques | Les préférences de réduction portent sur les postes les plus petits | [^ipsos21] |
| 6 | Classement des réductions : famille 34 %, aides aux entreprises 33 %, chômage 30 % … retraites 7 %, santé 6 %, éducation 5 % | Elabe pour *Les Echos*, 1er-2 septembre 2026, n = 1 005 | Famille 4,0 %, chômage 2,9 %, vieillesse 23,4 %, santé 15,6 %, enseignement 8,9 % des dépenses publiques (COFOG 2024) | Les postes les plus cités (famille + chômage) ≈ 7 % des dépenses publiques (aides aux entreprises exclues : pas de ligne COFOG) ; les postes protégés (vieillesse + santé + enseignement) ≈ 48 % des dépenses publiques. *Vieillesse + santé seules = 39 %, le chiffre utilisé dans la synthèse du fichier 14 : nommer les postes chaque fois que l’un ou l’autre chiffre est affiché.* | [^elabe26] ; fichier 14 |
| 7 | 79 % / 74 % jugent « efficace » contre la dette de taxer les grandes entreprises / les plus aisés | Elabe pour *Les Echos* et l’Institut Montaigne, 1er-2 octobre 2024, n = 1 007 | Impôts sur la fortune : de 0,1 à 0,8 pt de PIB, pour un besoin d’ajustement de 4,4 pts | Poids surestimé | fichier 14 |
| 8 | **47 %** pensent que le niveau de vie des retraités est inférieur à la moyenne de la population (57 % des 18-24 ans) ; **18 %** pensent que le système français fonctionne par capitalisation, 9 % ne savent pas ; **50 %** pensent que les cotisations actuelles permettront de verser aux actifs d’aujourd’hui des pensions au moins aussi élevées que celles d’aujourd’hui | **Toluna-Harris Interactive pour l’Observatoire Hexagone** (groupe de réflexion favorable à un pilier par capitalisation : signaler son orientation), **en ligne, 21-24 février 2025**, n = 1 101 adultes de 18 ans et plus, quotas et redressement ; publié le 24 mars 2025 *(dates de terrain vérifiées le 25 octobre 2026 dans le rapport de l’institut, p. 3)* | 100,2 % (COR, 2023) ; le système fonctionne par répartition ; le COR projette une baisse du niveau de vie relatif des retraités à environ 90 % d’ici 2070 | Pessimisme sur les retraités actuels ; optimisme sur les pensions futures | [^hexagone] ; [^f03] |
| 9 | 44 % pensent que les retraités vivent moins bien | Drees, *Baromètre*, octobre-décembre 2025, n = 4 000, en face à face | 100,2 % | — | fichier 14 |
| 10 | 72 % pensent que les impôts ont augmenté depuis 2017 | Elabe pour BFMTV, 4-5 novembre 2025, n = 1 000 | Taux de PO de 45,3 à 43,6 % du PIB ; +25,7 % en euros courants ; +2,5 % après inflation | Faux en ratio, exact en euros | fichier 14, §7.1 |
| 11 | 59 % contribuent plus qu’ils ne reçoivent | Elabe pour BFMTV, 2-3 décembre 2025 | 56 % sont bénéficiaires nets (Insee, 2023) | Perception contre comptabilité | fichier 14 |
| 12 | 60 % « proche de la faillite » | Odoxa pour l’iFRAP (libéral), 3-4 septembre 2025 | Écart de taux avec l’Allemagne (*spread*) 97 pb ; notes A+/Aa3 | Imminence surestimée | fichier 14 |
| 13 | 84 % / 82 % disent que la fraude sociale / fiscale n’est pas assez combattue | Elabe pour BFMTV, novembre 2025 | Rendement marginal réaliste de 1 à 3 Md€ | Gisement récupérable surestimé | fichier 14 |
| 14 | Part perçue des immigrés 28,8 % contre 12,2 % en réalité | Alesina-Miano-Stantcheva, terrain 2018, France n = 4 000 | — | ×2,4 | fichier 14 |

*Note sur les deux nouvelles sources (lignes 1 à 5 et 8) :* les PDF sont enregistrés dans `data/raw/20_perception/vp_279092_pj4.pdf` (avec le texte UTF-8 dans `vp_utf8.txt`) et `data/raw/20_perception/hexagone_retraites_2025-02.pdf`, ainsi que le rapport complet de l’institut `data/raw/20_perception/toluna/toluna_harris_hexagone_retraites.pdf` (page de méthode et graphiques de résultats). L’enquête Ipsos est la **seule enquête française représentative trouvée qui demande une estimation chiffrée du budget**. Elle date de cinq ans : le quiz doit la citer comme « la dernière fois que la question a été posée » et utiliser les données propres de la plateforme (§6.4) pour la mettre à jour. Le rapport Hexagone reprend aussi l’affirmation selon laquelle « les retraites expliquent la moitié de la hausse de la dette » (J.-P. Beaufret ; F. Bayrou, janvier 2025). C’est la **thèse A** du débat contesté sur le « déficit caché » (fichier 03, §5). Ne pas la citer sans la thèse B.

### 6.3 Banque de questions (25 questions ; valeurs réelles tirées de la base de recherche)

| N° | Question (traduction de travail ; formulation définitive à valider) | Type de réponse | Valeur réelle | Meilleur contre-argument / nuance affichée ensuite | Camp interpellé | Source |
|---|---|---|---|---|---|---|
| 1 | Sur 100 € de dépense publique, combien vont aux retraites (vieillesse) ? | curseur de 0 à 60 | **23,4** (COFOG 2024) ; 24,3 (périmètre COR, 2025) | Les retraites sont aussi en partie financées par des cotisations liées au travail passé | Général | [^cofog] |
| 2 | … à la santé ? | curseur | **15,6** | Les résultats de santé sont bons | Général | [^cofog] |
| 3 | … à l’enseignement ? | curseur | **8,9** | — | Général | [^cofog] |
| 4 | … à la défense ? | curseur | **3,2** | Elle doit augmenter (OTAN) | Général | [^cofog] |
| 5 | … aux intérêts de la dette ? | curseur | **3,8** (2025, SEC) | Pas encore exceptionnel dans l’UE | Général | [^ref] |
| 6 | … à l’aide économique extérieure ? | curseur | **0,3** (COFOG GF0102, 4,9 Md€, 2024) | Ce n’est pas l’APD au sens de l’OCDE (plus large : 12,9 Md€ = 0,42 % du RNB en 2025, CAD de l’OCDE ; ligne 53 du fichier 00, fichier 16) *(corrigé le 25 octobre 2026, passe de l’index : la mention était « non vérifié »)* | Droite | fichier 14, §9 |
| 7 | … au RSA et à la prime d’activité ? | curseur | **2,2** (GF1007) | La pauvreté des enfants est élevée | Droite | [^cofog] |
| 8 | Combien de jours de dépense publique le déficit représente-t-il ? | curseur de 0 à 120 | **32** | — | Général | [^conv] |
| 9 | La dette publique en % du PIB ? | curseur de 0 à 200 | **115,7** (fin 2025) ; 119,0 (T2 2026) | Ipsos 2021 : estimation moyenne de 76 % | Général | [^ref] |
| 10 | La dette par habitant ? | choix | **≈ 50 000 €** | Le patrimoine net est positif (+750 Md€) | Général | [^ref] |
| 11 | La taxe Zucman financerait combien de jours de dépense publique ? | curseur de 0 à 60 | **de 0,4 à 4,3** | La justice fiscale est une autre question ; les tout plus aisés paient des taux effectifs plus bas (IPP) | Gauche | [^conv] |
| 12 | Quelle part du déficit un ensemble de mesures « taxer les riches » comblerait-il ? | choix | **de 7 à 16 %** | Ce n’est pas négligeable : de 2 à 6 fois une « année blanche » | Gauche | fichier 07, §5 |
| 13 | Combien coûte chaque année un retour général de la retraite à 60 ans ? | choix | **de 43 à 58 Md€** *(corrigé le 25 octobre 2026, c’était de 35 à 58)* | L’abrogation seule de la réforme de 2023 coûte de 16 à 17 Md€ (2030-2032) ; les versions partielles de type RN, avec 60 ans pour les carrières longues, de 26 à 35 Md€ ; le chiffre du RN lui-même pour son plan 2027 est d’environ 9 *(les deux fourchettes affichées, 25 octobre 2026)* | Gauche/RN | [^f03] ; [^f11] |
| 14 | Rang de la France dans l’UE pour la dépense publique en % du PIB ? | choix | **2e** (1re de 2014 à 2023) | 8e par habitant en SPA | Général | [^ref] |
| 15 | Depuis 2017, les prélèvements obligatoires (en % du PIB) ont-ils augmenté ou baissé ? | choix | **Baissé (de 45,3 à 43,6)** | En hausse en euros, à peu près stables après inflation | Anti-impôts | fichier 14, §7.1 |
| 16 | Quelle part des foyers fiscaux paie effectivement l’impôt sur le revenu (impôt net positif) ? | curseur | **47,2 %** | Tout le monde paie la CSG et la TVA | Droite | [^f05] |
| 17 | Part de l’ensemble des prélèvements payée par les 10 % les plus aisés ? | curseur | **33,3 %** (2023) | Les impôts indirects pèsent davantage sur les plus modestes (64 % contre 48 % du revenu, 2022) | Les deux | [^f05] |
| 18 | Part des personnes qui reçoivent plus qu’elles ne paient (services publics compris) ? | curseur | **56 %** | Une partie est financée par la dette | Anti-impôts | [^f14] |
| 19 | Niveau de vie des retraités par rapport à la moyenne ? | choix | **À peu près égal (100,2 %)** | Projeté en baisse à environ 90 % d’ici 2070 | Pessimisme | [^f03] |
| 20 | Part des emplois dans la fonction publique ? | curseur | **≈ 20 %** (19,8 %, DGAFP/Insee, périmètre de la fonction publique, contrats aidés compris, 2024 ; 20,7 %, OCDE, définition des administrations publiques, 2023) *(corrigé le 25 octobre 2026, point 6 de REVIEW.md : était « 19,8 % SIASP »)* | Suède 28 %, Allemagne 11,5 % (définitions différentes) | Droite | [^f04] |
| 21 | Rendement supplémentaire réaliste d’un nouveau plan de lutte contre la fraude, par an ? | choix | **de 1 à 3 Md€** | La fraude sociale est estimée à environ 13 Md€ (12,98, HCFiPS 2024), environ 14 Md€ dans la mise à jour de décembre 2025 (ligne 59 du fichier 00) ; la part récupérable est faible | Droite | [^f07] |
| 22 | À combien s’élèvent les « aides aux entreprises » ? | choix, dont « ça dépend » | **« Ça dépend » : de 45 à 211 Md€** | Définitions | Gauche | [^f08] |
| 23 | Quel est le rang de la France pour les heures travaillées par habitant ? | choix | **Dernière sur 27** | Les heures par personne en emploi sont plus élevées qu’en Allemagne et aux Pays-Bas | Pessimisme / gauche | [^f08] |
| 24 | En 2027, lequel est le plus élevé : la charge de la dette de l’État ou l’enveloppe de la loi de programmation militaire (LPM) ? | choix | **La charge de la dette de l’État (72,9 contre 63)** | Comptabilité budgétaire, État seul | Général | [^f06] |
| 25 | Qu’est-ce qui explique l’essentiel de l’écart de dépense de la France avec la zone euro ? | choix | **Protection sociale + santé (environ deux tiers)** | Par habitant, l’écart est plus faible | Droite (« bureaucratie ») | [^ref] |

**Réserve de rotation (questions 26 à 40 ; questions 26 à 35 ajoutées le 25 octobre 2026 lors de la synchronisation 15-18, questions 36 à 40 ajoutées le même jour pour équilibrer la réserve).** Le quiz complet compte toujours 25 questions ; elles sont tirées de la banque de 40 questions (`platform/data/quiz.json` : 25 de base + 15 de rotation) selon la règle de symétrie (§6.1) : chaque tirage contient exactement autant de questions marquées à gauche que de questions marquées à droite (`draw_rule` dans quiz.json). Les questions 26 à 32 sont surtout marquées à droite, parce que les fichiers 15 et 16 portent sur des cibles marquées à droite ; les questions 33 à 35 et les questions 36 à 40, marquées à gauche, rééquilibrent l’ensemble.

| N° | Question | Type de réponse | Valeur réelle | Meilleur contre-argument / nuance affichée ensuite | Camp interpellé | Source |
|---|---|---|---|---|---|---|
| 26 | Combien la France verse-t-elle au budget de l’UE, déduction faite de ce qu’elle en reçoit (2025) ? | choix | **9,5 Md€** (méthode comptable) ; 6,4 Md€ (méthode de la Commission) | 2e contributeur net en euros ; le prélèvement brut est de 23,0 Md€ (2025) et de 30,9 Md€ (PLF 2027). Un plafond de 5 Md€ ferait économiser au plus de 1,4 à 4,5 Md€, même s’il était légal | Droite (souverainiste) | ligne 52 du fichier 00 ; fichier 16, §3 |
| 27 | Sur 1 000 € de dépense publique, combien vont à l’aide médicale de l’État pour les étrangers en situation irrégulière (AME) ? | curseur de 0 à 50 | **environ 0,8 €** (1,34 Md€ = 0,08 % des dépenses publiques, 2025) | Les crédits sont sous-budgétés (1,208 Md€ au PLF 2027 contre 1,34 Md€ dépensés) ; 454 111 bénéficiaires | Droite | ligne 54 du fichier 00 ; fichier 15 |
| 28 | Combien coûtent chaque année la Présidence, le Parlement et l’ensemble des cabinets ministériels ? | choix | **environ 1,3 Md€** (0,08 % des dépenses publiques ; 19 € par habitant) | Rémunérations brutes seulement ; pas de chiffre officiel en coût complet | Populiste (des deux bords) | fichier 16, §6 |
| 29 | Combien une réorganisation des agences de l’État pourrait-elle faire économiser chaque année, selon la commission d’enquête du Sénat ? | choix | **environ 0,54 Md€** (chiffre annoncé par le gouvernement en 2025 : de 2 à 3 Md€, méthode non publiée) | Les opérateurs reçoivent 72,6 Md€, mais surtout pour les universités, la recherche, la formation et le logement | Droite | fichier 16, §4 |
| 30 | L’aide publique au développement de la France en % du revenu national, et son rang parmi 33 donateurs ? | curseur de 0 à 2 % + choix | **0,42 % du RNB, 11e sur 33** (2025, CAD de l’OCDE) | La mission budgétaire ne représente que 3,17 Md€ ; l’APD comprend des prêts, la quote-part de l’UE et les coûts d’accueil des réfugiés | Droite | ligne 53 du fichier 00 ; fichier 16, §2 |
| 31 | Les immigrés coûtent-ils ou rapportent-ils aux finances publiques françaises ? | choix, dont « ça dépend » | **« Cela dépend de la convention » : de +1,02 % à −0,85 % du PIB par an** (OCDE, 2006-2018) | Par tête, les personnes nées à l’étranger contribuent moins que les personnes nées en France ; selon la convention la moins favorable, les personnes nées en France apparaissent plus déficitaires au total (années de déficit) | Droite (et les affirmations pro-immigration d’un fort excédent) | ligne 55 du fichier 00 ; fichier 15 |
| 32 | Le poids des prélèvements en France est-il de 42,7 %, 43,5 % ou 44,3 % du PIB ? | choix, dont « les trois » | **Les trois, selon la définition** (PO de l’Insee 2024 / OCDE 2024 / concept SEC-OCDE 2025, Cour des comptes) | +0,7 pt = crédits d’impôt restituables comptés en dépense ; ne jamais classer le chiffre de l’Insee parmi ceux de l’OCDE | Général (méthode) | fichier 18, §1 |
| 33 | Combien l’État a-t-il dépensé en conseil en stratégie en 2025 ? | choix | **environ 60 M€** (271,5 M€ en 2021) | Le chiffre du Sénat, « plus d’un milliard d’euros » (2021), couvrait l’ensemble des prestations intellectuelles | Gauche (polémique de 2022 sur les cabinets de conseil) | fichier 16, §5 |
| 34 | La contribution différentielle sur les hauts revenus (CDHR, impôt minimal de 20 %) avait été annoncée à environ 2 Md€. Combien a-t-elle rapporté en 2025 ? | choix | **moins de 0,4 Md€** | Des effets de calendrier pourraient accroître les rendements ultérieurs (IPP) | Gauche | fichier 07 (§4.10 de la 1re partie) |
| 35 | Une baisse de 30 Md€ des dépenses de fonctionnement : de combien le déficit baisse-t-il la 1re année ? | choix | **environ 16 Md€** (multiplicateur 0,8, fourchette de 11 à 21) | Les hausses d’impôts ralentissent aussi la croissance ; les modèles français et les études narratives divergent sur ce qui coûte le plus | Les deux (« les baisses de dépenses sont indolores » et « les hausses d’impôts sont indolores ») | fichier 17, §8 ; §4.18 |
| 36 | Les baisses d’impôts et de cotisations décidées de 2018 à 2023 (62 Md€ par an, valorisées en 2023) : quelle part du déficit de 2025 représentent-elles ? | choix | **environ 41 %** (62 / 151,6) | Si l’on part de 2017, la baisse des recettes explique toute la hausse du déficit (recettes −3,1 points de PIB, déficit +2,4 points, Eurostat 2017-2024) ; une partie des baisses a depuis été compensée (Rexecode : 36,7 Md€ de prélèvements nouveaux de 2024 à 2026) | Gauche (« les baisses d’impôts depuis 2017 expliquent tout le déficit ») | lignes 28 et 31 du fichier 00 ; fichiers 08 et 10 |
| 37 | De 2019 à 2025, les dépenses publiques ont-elles augmenté ou baissé en proportion du PIB ? | choix | **Augmenté de 2,0 points de PIB** (recettes −0,8 point ; Eurostat) | La réponse dépend de l’année de départ : de 2017 à 2024, dépenses −0,7 point et recettes −3,1 points ; un ratio au PIB monte aussi quand la croissance ralentit | Gauche (« la dépense publique a été réduite ») | fichier 10 (K10) |
| 38 | Rétablir l’ISF tel qu’il était en 2017 : combien de jours de dépense publique financerait-il chaque année ? | choix | **Moins de 1 jour** (de 3 à 4,5 Md€ bruts, CAE ; de 0,64 à 0,96 jour) | Le rendement n’est pas le seul argument (équité au sommet) ; le CAE trouve des départs pour motif fiscal limités après 2013 | Gauche (« rétablir l’ISF rétablirait les finances publiques ») | fichier 07 [S5] |
| 39 | De 2024 à 2026, quel montant de prélèvements obligatoires nouveaux a été décidé (décompte de Rexecode) ? | choix | **36,7 Md€** (1,2 point de PIB) ; Cour des comptes : 23,0 Md€ de hausses pour la seule année 2025 | Le mouvement inverse reste partiel : 1,2 des 2,7 points de PIB de baisses depuis 2014 selon le même décompte ; les 62 Md€ de baisses 2018-2023 chiffrées par la Cour sont plus importants | Gauche (« les baisses depuis 2017 n’ont jamais été compensées ») | fichier 08 ; Cour des comptes[^cour26] |
| 40 | En comptant tous les impôts directs (y compris l’IS des entreprises qu’ils détiennent), quel taux effectif payaient les 0,1 % des foyers les plus aisés en 2016 ? | choix | **environ 46 %** (IPP, données 2016) | Environ 26 % pour les quelque 75 foyers les plus riches (IPP) ; F. Geerolf (OFCE, critique non évaluée par des pairs) le conteste : 25,1 % pour les milliardaires contre 26,8 % au seuil des 10 % les plus aisés, sur une base homogène | Gauche (« les riches paient peu d’impôts ») | fichier 05 |

### 6.4 Commander une enquête représentative d’estimations chiffrées (recommandé)

- **Échantillon :** n ≥ 2 000, échantillon par quotas ou probabiliste, de préférence en deux vagues (avant la campagne, puis après le premier tour en avril 2027).
- **Questions :** les questions 1 à 13 ci-dessus, plus « cela équilibrerait-il le budget ? » pour chaque proposition.
- **Bras d’information aléatoire :** la moitié de l’échantillon voit l’étalon avant de répondre aux questions de politique publique. Cela reproduit pour la France Kuziemko et al. (2015).
- **Publication :** préenregistrer le protocole ; publier le questionnaire, les microdonnées et les résultats, quels qu’ils soient.
- **Valeur attendue :** l’enquête comble la lacune du fichier 14, §10 et constitue un bien public publiable, cité par les médias.

---

## 7. Garde-fous de crédibilité

### 7.1 Mécanismes

| Garde-fou | Mise en œuvre |
|---|---|
| **Une source pour chaque chiffre** | Le composant « fiche chiffre » ne peut pas s’afficher sans `source_id`, `data_year`, `denominator` et `vintage`. Les pastilles source renvoient directement au tableau (databrowser d’Eurostat, page de l’Insee, ancre de page du PDF). |
| **Fichier canonique** | Un seul fichier lisible par machine, `reference_figures.json`, généré à partir de [`00-reference-figures.md`](../research/00-reference-figures.md). Les pages y puisent leurs valeurs ; rien n’est saisi à la main dans une page. La liste des « valeurs remplacées » (fichier 00, §4) est appliquée par un contrôle au moment de la compilation, qui échoue si une valeur remplacée apparaît. |
| **Pages de méthode** | Une par concept : SEC 2010 contre comptabilité budgétaire ; PO contre recettes fiscales en % du PIB (OCDE) contre recettes publiques totales (SEC) (pont : §4.17) ; les trois chiffres d’intérêts (65,7 / 64,7 / 51,6, §4.17) ; santé COFOG contre SHA (§4.17) contre comptes de la protection sociale de la Drees contre Sespros ; SPA ; ZE20 contre ZE21 ; SOCX brutes contre nettes ; chiffrage statique contre chiffrage après effets de comportement contre chiffrage avec bouclage macroéconomique (§4.18, §5.4) ; « les conventions décident du signe » pour la contribution budgétaire nette de l’immigration (§4.15). |
| **Versions** | Chaque page affiche « données au [date], millésime [X] ». Un dépôt Git public contient les données, les scripts et le journal des modifications. Chaque publication est étiquetée (par exemple `2027.03-insee-first-estimate`), et les anciennes versions restent accessibles. |
| **Fourchettes** | Les chiffrages contestés utilisent toujours la barre de fourchette, avec les auteurs à chaque bout. |
| **Désaccords** | Une page « Débats » et un encadré « Le meilleur contre-argument » dans le corps de la page. Étiquettes d’orientation : OFCE (Sciences Po, sensibilité keynésienne), Rexecode (institut financé par des organisations patronales), Institut Montaigne (financé par des entreprises, libéral-centriste), iFRAP (libéral), Terra Nova (centre gauche), Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire), Observatoire Hexagone (favorable à un pilier de retraite par capitalisation), Institut de l’Entreprise (financé par des entreprises), Attac (association altermondialiste), Clersé pour l’IRES et la CGT (étude commandée par un syndicat). |
| **Hygiène des sondages** | Ne jamais citer un sondage commandé sans son commanditaire, la formulation des questions, l’effectif et les dates de terrain (fichier 14, §9). |
| **Droit de réponse** | Avant de publier une fiche programme, envoyer le chiffrage à l’équipe de campagne avec un délai de réponse de 7 jours. Publier la réponse telle quelle (dans une limite de longueur). |
| **Registre des corrections** | Une page publique qui liste chaque erreur, sa date, sa correction et son incidence. Aucune correction n’est silencieuse. |
| **Comité scientifique** | 4 à 6 économistes d’écoles différentes (par exemple OFCE, IPP, anciens du CAE, un ancien magistrat de la Cour des comptes, un économiste de marché), nommés publiquement. Ils relisent la méthode, pas chaque phrase. |
| **Relecture contradictoire** | Avant le lancement, deux relecteurs, l’un plutôt de gauche, l’autre plutôt de droite, cherchent des biais. Leurs rapports sont publiés. |
| **Transparence du financement** | Liste de tous les financeurs au-delà d’un seuil ; aucun financement par un parti, une campagne ou un intérêt unique ; une politique de prévention des conflits d’intérêts pour les auteurs. |
| **Guide de vocabulaire neutre** | Employer « dépense », pas « gaspillage » ; « prélèvements », pas « matraquage fiscal » ; « dépenses fiscales », pas « cadeaux fiscaux » ; « les très hauts patrimoines », pas « les parasites » ni « les créateurs d’emplois ». |
| **Audit de symétrie** | Un décompte trimestriel du nombre de pages qui contestent des affirmations marquées à gauche et à droite, publié dans l’Espace confiance. |
| **Degrés de certitude** | Une échelle fixe : « mesuré » (statistique officielle), « estimé » (estimation institutionnelle), « prévu » (prévision), « annoncé » (parti), « illustratif » (calcul de la plateforme). |

### 7.2 Charte éditoriale (projet, 10 articles)

1. Nous publions des ordres de grandeur, pas des consignes de vote.
2. Chaque chiffre est sourcé, daté et accompagné de son dénominateur.
3. Les statistiques officielles (Insee, Eurostat, OCDE, Drees, Cour des comptes, HCFP, COR) passent en premier. Les groupes de réflexion sont cités avec leur orientation.
4. Quand les experts divergent, nous montrons la fourchette et nommons les auteurs.
5. Chaque message clé est publié avec le meilleur contre-argument que nous connaissons.
6. Nous traitons les propositions de tous les partis avec la même méthode et le même gabarit.
7. Nous distinguons les faits (tailles, rendements) des valeurs (justice, priorités), et nous ne tranchons pas les questions de valeurs.
8. Nous corrigeons nos erreurs publiquement et rapidement.
9. Nous accordons un droit de réponse aux équipes de campagne.
10. Nos données et notre code sont ouverts.

### 7.3 Prévenir les accusations de partialité (attaques prévisibles et réponses)

| Attaque | Réponse préventive sur le site |
|---|---|
| « Propagande néolibérale contre le modèle social » | Les encadrés « Le meilleur contre-argument » sur les dépenses sociales nettes (SOCX), la réduction de la pauvreté, les classements en SPA et les baisses d’impôts depuis 2017 sont visibles dès les premiers écrans, pas enfouis. La thèse est formulée ainsi : « la dépense doit contribuer substantiellement », et non « la dépense est le seul levier » (conclusion du Haut-commissariat à la Stratégie et au Plan). |
| « Gauchistes : vous attaquez les chiffres du RN et de LR » | Le même traitement s’applique à la taxe Zucman, à l’ISF et aux aides aux entreprises ; un audit de symétrie est publié. |
| « Vos chiffres sont faux » | Pastilles source, données ouvertes, registre des corrections, millésimes canoniques. |
| « Vous choisissez 2017 à dessein » | Curseur de l’année de base (§4.11). |
| « Financé par X » | Page sur le financement. |

---

## 8. Accessibilité et mobile

| Domaine | Exigence |
|---|---|
| Référentiel | **RGAA 4.1** (référentiel général d’amélioration de l’accessibilité, fondé sur les WCAG 2.1 AA) comme cible, avec une page de déclaration d’accessibilité. |
| Graphiques | Chaque graphique a (a) un résumé textuel de son message en une phrase, (b) un bouton « voir les données » qui affiche un tableau, (c) un CSV téléchargeable. Ne jamais coder l’information par la seule couleur : utiliser des motifs et des étiquettes directes. Utiliser une palette adaptée aux daltoniens (validée), avec un contraste ≥ 4,5:1 pour le texte et ≥ 3:1 pour les éléments graphiques. |
| Interactions | Les curseurs se manipulent au clavier (flèches, Page précédente / Page suivante), avec un texte de valeur ARIA qui lit la valeur mise en forme (« 20 milliards d’euros, 4,3 jours de dépense publique »). Cible tactile minimale de 44 × 44 px. Les états de focus sont visibles. |
| Animations | Respecter `prefers-reduced-motion` : la narration au défilement devient une suite de panneaux statiques. Pas de lecture automatique. |
| Langue | Français clair (cible : niveau de lecture B1 pour le texte principal). Un résumé *FALC* (*facile à lire et à comprendre*) pour chaque chapitre. Une infobulle de glossaire pour chaque terme technique (PO, COFOG, Ondam, AOD…). |
| Nombres | Mise en forme française (*1 714 milliards d’euros* ; virgule décimale), et une formulation des « milliards » jamais ambiguë (« milliard » et non « billion »). Toujours arrondir de façon cohérente (une décimale pour les % du PIB). |
| Mobile | Conception mobile d’abord : narration verticale au défilement ; un graphique par écran ; graphiques simplifiés aux 8 premiers postes plus « autres » ; un simulateur avec un indicateur de solde fixé en bas de l’écran ; des leviers regroupés dans des accordéons repliables. |
| Performance | Poids initial de la page < 1 Mo, graphiques chargés à la demande, fonctionne en 3G ; texte rendu côté serveur, pour que le contenu soit lisible sans JavaScript. |
| Partage | Cartes de partage (images) générées automatiquement, qui **intègrent la source et la date dans l’image**, pour que les captures d’écran restent sourcées. |
| Classe | Fiches d’exercices en PDF imprimables ; quiz en « mode classe » sans connexion. |

---

## 9. Plan de maintenance

### 9.1 Calendrier de mise à jour des données (récurrent)

| Mois | Publication | Ce qui change sur le site | Action du responsable |
|---|---|---|---|
| **Fin mars** | Première estimation des comptes des APU par l’Insee (déficit, dette, PO, dépenses publiques de l’année N-1) ; dette trimestrielle de l’Insee (T4) | Chiffres phares, constantes des étalons, métaphore du ménage | Régénérer `reference_figures.json` ; nouvelle étiquette de millésime |
| **Vers le 22 avril** | Notification PDE d’avril d’Eurostat | Classements européens pour le déficit et la dette | Relancer les scripts Eurostat |
| **Fin mai** | Publication détaillée du compte des APU par l’Insee (*compte des APU*, millésime de mai, révisions) | Ratio dépenses publiques/PIB, intérêts et PO révisés | Vérifier la liste des valeurs remplacées |
| **Juin** | Rapport annuel du COR ; *La situation et les perspectives des finances publiques* de la Cour des comptes (fin juin) ; dette trimestrielle de l’Insee (T1) | Page retraites, écart avec le solde stabilisant la dette (objectif A du simulateur) | Mettre à jour le levier S1 si le COR modifie ses projections |
| **Juillet** | Pauvreté selon l’Insee (ERFS) ; rapports de l’IGF et du Haut-commissariat à la Stratégie et au Plan (variable) ; chiffres de défense de l’OTAN | Résultats, pression sur la défense | |
| **Fin septembre** | Comptes de la santé de la Drees ; *Regards sur l’éducation* de l’OCDE ; dette trimestrielle de l’Insee (T2) ; avis du HCFP sur le PLF | Pages santé et enseignement | |
| **Vers le 1er octobre** | **PLF et PLFSS** (projets de loi de finances et de financement de la sécurité sociale) ; rapport de la CCSS ; PAP du programme 183 (AME) ; avis du HCFP (hypothèse de multiplicateur) | Prévisions N et N+1, trajectoire des intérêts, taille de l’ensemble de mesures, schéma d’emplois, AME, valeur de travail pour le bouclage macroéconomique | Grande mise à jour de la situation de référence du simulateur |
| **Mi-octobre** | *Jaunes* du PLF (relations financières avec l’UE, opérateurs, conseil, cabinets ministériels, associations) | Fiches « économies faciles » et leviers S12 à S19 | Enregistrer les PDF et les annexes xlsx (téléchargeables seulement depuis un navigateur) |
| **Vers le 21 octobre** | Notification PDE d’octobre d’Eurostat ; estimations précoces Sespros | Déficit et dette canoniques (millésime d’octobre) | Nouvelle étiquette de millésime |
| **Novembre** | *Panorama des pensions* de l’OCDE (tous les deux ans, années impaires) ; statistiques de l’impôt sur le revenu de la DGFiP | Comparaison internationale des retraites, concentration de l’IR | |
| **Décembre** | ***La protection sociale en France et en Europe* de la Drees** ; ***Statistiques des recettes publiques* de l’OCDE** ; tableaux COFOG de l’Insee (N-1) ; dette trimestrielle de l’Insee (T3) | Protection sociale, classement des recettes fiscales en % du PIB, COFOG provisoire | |
| **Février-mars** | Publication COFOG d’Eurostat ; rapport public annuel de la Cour des comptes | Calendrier de la dépense publique, ventilation de 1 000 €, décomposition de l’écart | |
| **Avril** | *Taxing Wages* de l’OCDE ; *Taxation Trends* de la DG TAXUD (fin mars) ; données provisoires d’APD du CAD de l’OCDE | Coin fiscal et social ; fiche aide au développement et question 30 du quiz | |
| **Irrégulier** | PISA (prochain cycle après 2025) ; TIMSS/PIRLS ; CEPEJ (octobre des années paires) ; *Panorama des administrations publiques* de l’OCDE (années impaires) ; *Ageing Report* de la Commission européenne (tous les trois ans) | Bandeaux « Ce que l’on obtient » | |

### 9.2 Plan pour la période de campagne (d’octobre 2026 à mai 2027)

| Période | Rythme |
|---|---|
| D’aujourd’hui à mars 2027 | Une fiche programme est mise à jour dans les 7 jours suivant toute annonce chiffrée ; une synthèse hebdomadaire du « vérificateur de promesses » |
| Mars 2027 | Première estimation de l’Insee pour 2026 → mise à jour complète des chiffres **avant** le premier tour (avril 2027) |
| Deux semaines avant chaque tour | Gel des contenus, sauf corrections, pour qu’aucun nouveau chiffrage ne paraisse sans laisser le temps de répondre |
| Après l’élection | Archiver les fiches programmes 2027 (liens permanents conservés) |

### 9.3 Processus

- **Collectes automatisées** (API SDMX d’Eurostat et de l’OCDE) exécutées en intégration continue. Un rapport de différences signale tout changement de valeur supérieur à 0,1 point ou à 1 %, et une personne vérifie avant publication.
- **Règle des quatre yeux :** toute modification de chiffre requiert un auteur et un relecteur.
- **Audit trimestriel des contenus :** vérification des liens (beaucoup d’URL de PDF changent), audit de symétrie et audit d’accessibilité.
- **Revue annuelle de la méthode** avec le comité scientifique.

---

## 10. Inventaire des données de la plateforme (par page)

| Page / outil | Fichiers (dans `research/data/`) | Sources primaires |
|---|---|---|
| Étalons et vue « ménage » | `20_pedagogical_conversions.csv` ; `eurostat_gov_10a_main.csv` ; `eurostat_tps00001_population.csv` | Eurostat, Insee |
| Calendrier de la dépense publique, ventilation de 1 000 € | `eurostat_gov_10a_exp_pctot.csv`, `eurostat_gov_10a_exp_mioeur.csv`, `00_reconcile_cofog_gap_2024_EA20_EA21.csv` | Eurostat COFOG |
| Comparaison européenne | `09_intl_*.csv`, `09_intl_fr_gap_timeseries.csv`, `eurostat_nama_10_pc_gdp_pps_per_capita.csv` | Eurostat, OCDE |
| Protection sociale | `eurostat_spr_exp_func.csv`, `esspros_*.csv`, `oecd_socx_totals.csv` | Drees, Eurostat, OCDE |
| Retraites | `pensions_*.csv`, `08_eurostat_proj_23ndbi.csv` | COR, Eurostat, OCDE |
| Santé | `12_*.csv` | Eurostat SHA, OCDE, OMS, Drees |
| Fonction publique et enseignement | `13_*.csv`, `04_*.csv` | DGAFP, OCDE, Eurostat, IEA |
| Fiscalité et reçu des impôts | `insee_t_3216_T_3216.csv`, `insee_t_3217_T_3217.csv`, `insee_taux_prelevements_obligatoires_1959_2025.csv`, `oecd_revenue_statistics_2025_pct_gdp.csv`, `14_factcheck_PO_2017_2025_real.csv` | Insee, OCDE |
| Déficit, dette, intérêts | `insee_dette_maastricht_1978_2025_by_subsector.csv`, `derived_06_*.csv`, `eurostat_gov_10dd_edpt1_deficit_debt_interest.csv`, `eurostat_irt_lt_mcby_m_10y_yields_monthly.csv` | Insee, Eurostat, Cour des comptes, HCFP |
| Curseur de l’année de base | `debates/computed_fr_vs_eu27_fiscal_series.csv` | Eurostat |
| Leviers du simulateur | `11_candidate_measures.csv` ; tableaux des fichiers 03, 05, 07, 08, 11, 12 | selon le levier |
| Quiz | `14_perception_surveys.csv` ; `raw/20_perception/*` | Instituts de sondage indiqués |
| Emploi | `08_eurostat_lfsi_emp_a.csv`, `08_eurostat_nama_10_lp_ulc.csv` | Eurostat, OCDE |
| Immigration et AME (§4.15) | `15_oecd_fiscal_immigration_stats.csv`, `15_conversions_eur_2025.csv`, `15_eurostat_foreign_born_share.csv` ; `raw/15/` ; `raw/16_factcheck/evin_stefanini_292122.pdf` | *Perspectives des migrations internationales 2021* de l’OCDE, CEPII, PAP 2027 du programme 183, rapport Évin-Stefanini |
| Cibles d’« économies faciles » (§4.16, S13 à S19) | tableaux du fichier 16 ; `raw/14_verify2/oda_*.xlsx` ; `raw/11_verify2/ec_eu_budget_2000-2025.xlsx` ; `raw/16/browser_extracts_2026-10-25.txt` (*Jaunes* transcrits lors d’une session de navigation) | CAD de l’OCDE, PLF 2027 et ses *Jaunes*, Commission européenne, rapports du Sénat n° 578 et n° 807 |
| Ponts méthodologiques (§4.17) | `18_po_vs_oecd_bridge_2024.csv`, `18_interest_bridge.csv`, `18_cofog_vs_sha_health_2024.csv` ; `raw/18/` | Tableaux 3.201 à 3.217 de l’Insee, Eurostat, OCDE |
| Bouclage macroéconomique (§4.18, §5.4) | tableau des valeurs par défaut du fichier 17, §8 (pas encore de CSV) ; `raw/17_multipliers/` | HCFP, CAE, Mésange, OFCE, SEBC, Banque de France |

---

## 11. Lacunes et points à vérifier avant publication

1. ~~**Attribution du commanditaire de l’enquête Ipsos 2021.**~~ **Résolu le 25 octobre 2026 :** le rapport Ipsos désigne le MINEFI comme client et les travaux de la Commission sur l’avenir des finances publiques comme objet, et vie-publique.fr le répertorie comme pièce jointe n° 4 du rapport de la commission Arthuis (voir le journal de vérification).
2. **« 24,3 % des dépenses publiques » selon le COR contre 24,6 % calculés** (422,2 / 1 714,1) : dénominateur non élucidé (fichier 03). Le site doit utiliser 23,4 % (COFOG vieillesse, 2024) pour la « part du budget » et 14,1 % du PIB pour le périmètre COR, et éviter 24,3 % sauf à expliquer le dénominateur.
3. **Levier des effectifs publics (S4).** Il faut un coût moyen complet par ETP (DGAFP/Insee), absent de la base de recherche.
4. ~~**Multiplicateurs macroéconomiques** pour la v2 du simulateur : à lire dans Guajardo-Leigh-Pescatori et dans la synthèse 2026 de la Cour des comptes, avec des valeurs vérifiées.~~ **Résolu le 25 octobre 2026 (synchronisation 15-18) :** le fichier 17 les a lus dans les sources primaires ; les valeurs par défaut par instrument figurent désormais dans la v1 (correspondance du §5.3, option 4 du §5.4). Réserves restantes : le multiplicateur de l’impôt sur la fortune est une approximation d’experts (pas d’estimation directe) ; la fourchette des *Perspectives de l’économie mondiale* (WEO) du FMI de 2012 (0,9 à 1,7) et la hausse en période de ralentissement selon Gechert-Rannenberg sont ⚠ non vérifiées et non affichées ; la semi-élasticité propre de la Commission européenne pour la France n’a pas été relue (fichier 17, §8-§9).
5. ~~**Coût budgétaire net de l’immigration** et **APD au sens du CAD de l’OCDE** : non vérifiés.~~ Résolu le 25 octobre 2026 (passe de l’index) : les deux sont désormais vérifiés dans les sources primaires (lignes 53 et 55 du fichier 00 ; fichiers 14, 15, 16).
6. **Sommes des dépenses fiscales du PLF 2027 :** les sommes de l’annexe 1 (91,7 / 92,0 / 83,9 Md€, 459 mesures) ont été vérifiées par le fichier 05 sur le tableur téléchargé à nouveau (25 octobre 2026), mais ce sont des sommes de lignes, pas un total officiel. Garder comme chiffre phare le total de la Cour des comptes, 91,83 Md€ (2025) (ligne 56 du fichier 00). *(Mis à jour lors de la passe de l’index : la mention était « ⚠ non vérifié, fichier brut non enregistré ».)*
7. ~~**Données de marché d’octobre 2026** (OAT au-dessus de 5 %, écart de taux d’environ 170 pb) : à remplacer par les données de clôture de la Banque de France ou de l’AFT avant publication (fichier 06).~~ **Résolu (passe de l’index, journal n° 29 du fichier 00) :** les valeurs officielles sont désormais canoniques : 5,126 % le 22 octobre 2026, écart de taux de 169 pb (22 octobre) / 166 pb (23 octobre) (ligne 43 du fichier 00).
8. **COFOG 2025 de l’Insee** (décembre 2026) remplacera toutes les parts fonctionnelles de 2024 ; le calendrier de la dépense publique devra alors être régénéré.
9. **Édition 2026 des comptes de la protection sociale de la Drees** (attendue en décembre 2026) : elle remplacera les chiffres 31,9 % / 2024 par des données 2025.
10. **Chiffrages des programmes :** aucun n’est encore indépendant. Consulter chaque mois l’IPP, l’OFCE, l’Institut Montaigne, Fipeco et la Cour des comptes.
11. *(ajouté le 25 octobre 2026, synchronisation 15-18)* **Jaunes du fichier 16 transcrits lors d’une session de navigation** (opérateurs, cabinets, dont la somme de 154,7 M€ calculée par la base, conseil, associations, UE p. 149-158) : enregistrer les PDF et les xlsx avant de publier les fiches du §4.16 et les leviers S14 à S18 (fichier 16, §14).
12. *(ajouté le 25 octobre 2026)* **AME :** le chiffre de presse « environ 1,2 Md€ (2023) » reste inutilisé (utiliser le RAP 2023 du programme 183) ; la réduction de 200 M€ de l’AME votée par le Sénat lors du débat sur le PLF 2026 n’apparaît pas dans les crédits de la LFI 2026 (⚠ à confirmer avec le texte de la LFI 2026) ; les votes en commission d’octobre 2026 sur les crédits de l’AME rapportés par la presse sont ⚠ non vérifiés (fichier 15, §10).
13. *(ajouté le 25 octobre 2026)* **Il n’existe pas de total officiel des prestations non contributives versées aux étrangers**, si bien que les économies de la « préférence nationale » ne peuvent pas être chiffrées (fichier 15, §6.3, §10). Le levier S11 reste un « chiffre annoncé » en gris.
14. *(ajouté le 25 octobre 2026)* **`data/20_pedagogical_conversions.csv`** ne contient pas encore les lignes ajoutées au §3.4 (synchronisation 15-18) ni la correspondance des effets de bouclage macroéconomique (§5.3) ; le régénérer avant que le contrôle de compilation (§7.1) ne s’appuie dessus.
15. *(ajouté le 25 octobre 2026, passe REVIEW.md)* **Résolu ici :** la source de chaque borne de S3, la valeur par défaut de S5 (+3,4 %, avec repères) et les deux fourchettes de la carte `rn_back_to_62` (voir le journal de vérification). **Encore ouvert :** pas de source primaire de la DGAFP pour le coût du point d’indice ; la note de la Cnav à l’origine du coût de l’abrogation (15,7 Md€ en 2032) n’est pas publique et n’est citée qu’au travers du rapport n° 613 de l’Assemblée nationale ; `platform/data/simulator-levers.json` (la valeur `default` de S5 est encore nulle) et l’affichage de la carte `rn_back_to_62` doivent être mis à jour par leurs responsables.

---

## Journal de vérification

### Passe du 25 octobre 2026 (suites des §7 et §8 du README)

**A. Points ⚠ du §7 du README (ligne 20)**

| Point | Résultat | Preuve |
|---|---|---|
| Commanditaire de l’enquête Ipsos 2021 (Commission sur l’avenir des finances publiques) | **Confirmé.** Le client est le MINEFI, et l’enquête a été commandée « pour nourrir la réflexion de la *Commission sur l’avenir des finances publiques* » (rapport Ipsos, « Rappel des objectifs » ; pied de page « © Ipsos \| MINEFI »). Le PDF est la *pièce jointe n° 4* du rapport de la commission Arthuis (remis le 18 mars 2021). Le titre figurant dans les métadonnées du PDF est « PJ N4-1 Etude d’opinion », créé le 19 mars 2021. | `data/raw/20_perception/vp_utf8.txt` (lignes 824 à 845 environ) ; page du rapport https://www.vie-publique.fr/rapport/279092-commission-sur-lavenir-des-finances-publiques (lue dans le navigateur de l’ordinateur portable ; l’ancienne URL courte /rapport/279092 renvoie désormais une erreur 404) |
| Dates de terrain du sondage de l’Observatoire Hexagone | **Confirmé : en ligne, 21-24 février 2025**, n = 1 101, quotas et redressement. L’institut s’appelle désormais Toluna-Harris Interactive. Les chiffres phares ont été revérifiés dans les graphiques de l’institut : 47 % « moins bon » (57 % chez les 18-24 ans), 18 % « système par capitalisation », 9 % « ne sait pas », et 72 % qui décrivent correctement la répartition. | Rapport Toluna-Harris p. 3, 9-10 ; `data/raw/20_perception/toluna/toluna_harris_hexagone_retraites.pdf` |

**B. Signaux ⚠ levés dans d’autres fichiers et vérifiés ici**

| Point | Statut dans ce fichier |
|---|---|
| Ifop 86 % (taxe Zucman) | Confirmé dans le fichier 14 (Ifop n° 121870, 10-11 septembre 2025, n = 1 000). Citation ajoutée au §4.10. |
| PISA 2025 (458 contre 463, 29e sur 38) | Déjà canonique (ligne 49 du fichier 00 ; fichier 13). Aucune modification nécessaire. |
| Schéma d’emplois du PLF 2027 (+8 025 / +4 742 ETP) | Confirmé dans le fichier 13 au regard du projet de loi n° 3210, art. 63. Note ajoutée au §4.6. |
| « 87 % mal utilisé / pas transparent » (§0, point 5, auparavant sans source ici) | Confirmé dans le fichier 14 (Elabe/BFMTV, 2-3 décembre 2025, n = 1 000). Citation ajoutée. |

**C. Alignement sur le fichier 00 (§8 du README et mêmes contrôles appliqués à ce fichier)**

| Emplacement | Modification |
|---|---|
| §4.2 GF02 Défense | 1,9 % → **1,8 % du PIB** (§8 n° 5 ; ligne 15 du fichier 00). |
| §4.1 message clé | L’année (2025) et l’agrégat (ZE21, avec ZE20 entre crochets) sont désormais indiqués pour l’écart de 7,6 pts / 227 Md€. La répartition « deux tiers / un tiers » est désormais présentée comme la décomposition **COFOG 2024** d’un écart de 7,8 pts (logique du §8 n° 1-2 ; lignes 7 à 9 du fichier 00). L’année des données SOCX est désormais indiquée (2021). |
| §4.3 message clé | La source (Drees 31,9 % contre Eurostat 32,0 %), l’année, l’agrégat UE-27 (27,4 %) et les rangs (2e en 2024, 3e en 2025 estimé) sont désormais indiqués (§8 n° 3, n° 7 ; lignes 20-21 du fichier 00). |
| §4.4 | La part de la vieillesse dans l’écart se lit désormais « +2,5 des 7,8 pts par rapport à la ZE21, COFOG 2024 ». |
| §4.8 | L’écart de dette se lit désormais « −2,0 (2005) → +28,4 pts (2025) par rapport à la ZE21 ; ZE20 −2,1 / +28,0 » (ligne 38 du fichier 00). |
| §4.11 | Périodes désormais étiquetées : recettes publiques totales (SEC) −3,1 pts sur **2017-2024** ; dépenses +2,0 / recettes −0,8 sur **2019-2025**. |
| §6.2 ligne 6 | Les postes derrière « ≈ 7 % » et « ≈ 48 % » sont désormais nommés, et la variante à 39 % est expliquée (§8 n° 8). |
| Déjà cohérent | Dépense publique par habitant 23 330 SPA, 8e (2025) ; PISA 2025 ; déficit 151,6 Md€ ; dette 3 460,1 Md€ ; intérêts 65,7 Md€ ; PO 2024 42,7 %. |

**D. Points encore ouverts (traités ailleurs)** : les sommes des dépenses fiscales du PLF 2027 (fichier 05). Recommandation : les remplacer par le total de la Cour des comptes, 91,83 Md€. Les données de marché intrajournalières d’octobre 2026 (fichier 06) ne sont pas utilisées dans les chiffres de ce fichier. `data/20_pedagogical_conversions.csv` n’a pas été modifié lors de cette passe, et aucune de ses valeurs n’a changé.

### Passe du 25 octobre 2026 – synchronisation avec les fichiers 15 à 18

*Périmètre : les fichiers 15, 16, 17, 18 et le fichier 00 (lignes 52 à 62, journal n° 23 à 37, valeurs remplacées du §4) ont été lus ; ce fichier a été passé au crible (grep) pour chaque valeur remplacée du §4 du fichier 00 et pour chaque ligne canonique 52 à 62. Seul ce fichier a été modifié. Les étalons dérivés utilisent : jours = Md€ / 4,696 (1 714,1 / 365) ; % du déficit = Md€ / 151,6 ; euros par habitant = Md€ × 1 000 / 68,998.*

**A. Corrections de valeurs (remplacées ou imprécises)**

| Emplacement | Avant | Désormais | Fondement |
|---|---|---|---|
| §4.14 Administrations publiques locales (déficit par sous-secteur) | administrations de sécurité sociale **6,7** | **5,8** ; parts ajoutées (État 84,5 %, ODAC 1,5 %, APUL 10,3 %, ASSO 3,8 % = 5,8 / 151,6) ; la somme des parties fait 151,7 du fait des arrondis | §4 et journal n° 27 du fichier 00 ; fichier 06, ligne 4 |
| §4.10 fiche sur le plafonnement de la contribution à l’UE ; §5.3 S12 | « 11,1 (2027) annoncés » ; pas de chiffre net vérifié ; encadré « Le meilleur contre-argument » vide | chiffre annoncé de 11,1 → 19,5 expliqué (tout le bloc « UE » du RN) ; **solde net de 9,5 / 6,4 Md€ (2025)** ; **plafond de 1,4 à 4,5 Md€ même si c’était légal** (6,4 − 5 ; 9,5 − 5) ; étalons 2,4 jours / 7,3 % / 161 € (chiffre annoncé) contre 0,3 à 1,0 jour / 0,9 à 3,0 % / 20 à 65 € (plafond) ; meilleur contre-argument ajouté | ligne 52 et journal n° 31 du fichier 00 ; fichier 16, §3 ; fichier 11 |
| §4.10 fiche Immigration | « 8 (lecture des chiffres annoncés par Montaigne) » ; AME 1,34 seulement | 8 = le chiffre du RN lui-même pour 2024, tel que rapporté par Montaigne ; chiffres annoncés détaillés (11,9 ; 15,1 → 29,0 ; LR 10) ; **AME 968 M€ (2022, source primaire Évin-Stefanini)**, crédits de 1,208 Md€ (action) / 1,216 Md€ (programme 183), 454 111 bénéficiaires ; contribution nette en euros (de +30,5 à −25,3 Md€, illustratif) ; pastille juridique 2024-6 RIP | lignes 54-55 et journal n° 32 du fichier 00 ; fichier 15, §0, §4, §6 |
| §4.10 fiche Lutte contre la fraude ; question 21 du quiz | « environ 13 Md€ (HCFiPS, source secondaire) » | environ 13 Md€ (12,98 = 7,25 + 5,73, source primaire), environ 14 Md€ (décembre 2025) ; les erreurs ne sont pas additionnées | ligne 59 du fichier 00 |
| §4.3 Protection sociale | 932,5 Md€ sans mention de millésime | 932,5 conservé comme valeur publiée par la Drees ; chiffre semi-définitif de 933,2 Md€ (31,8 % sur le PIB actuel) signalé ; 199 jours recalculés sur les deux (198,6 / 198,7) | ligne 20 et journal n° 25 du fichier 00 |
| §5.4 Bouclage macroéconomique | « Aucun multiplicateur n’est appliqué en v1 » | Option 4 activée par défaut, valeurs par défaut et fourchettes par instrument, règle × (1 − m × 0,57), exemple recalculé (+12,7 statique, −1,5 après effets de comportement) | ligne 62 du fichier 00 ; fichier 17, §8 |
| §11 points 4 et 7 | ouverts | résolus (fichier 17 ; ligne 43 / journal n° 29 du fichier 00) | |
| §0 point 4(c), §0 point 5 | simulateur sans bouclage macroéconomique ; liste symétrique sans la contribution à l’UE ni l’aide au développement | mis à jour | |

**B. Ajouts**

| Emplacement | Ajout | Source |
|---|---|---|
| §0 point 7 | Synthèse de la synchronisation 15-18 | fichiers 15 à 18 |
| §2.1, §7.1 | Périmètre des pages de méthode étendu (chiffres d’intérêts, COFOG contre SHA, bouclage macroéconomique, conventions sur l’immigration) | fichier 18 ; fichier 17 ; fichier 15 |
| §3.1 | Constantes : 1 pt de PIB ≈ 30 Md€ ; règle de bouclage macroéconomique (× 0,658 avec m = 0,6) | ligne 62 du fichier 00 ; fichier 17 |
| §3.4 | 18 nouvelles lignes de conversion (UE, APD, AME, immigration, opérateurs, agences, conseil, *Pouvoirs publics*, audiovisuel public, associations, le total de 29,4 Md€, fraude sociale, l’écart d’intérêts de 14,1 Md€) | fichiers 15, 16, 18 ; lignes 52 à 59 du fichier 00 |
| §4.2 GF07 | Écart SHA (+1,06 à +1,10) et formulation « 1 à 1,5 point » | fichier 18, §3 ; journal n° 35 du fichier 00 |
| §4.4 | Fourchette macroéconomique de l’âge de départ (PIB de −0,1 % à +1,1 % ; solde de +0,1 à +0,9 pt) | fichier 17, §3.5 |
| §4.7 | Pont en une ligne entre PO et OCDE ; ne jamais classer les PO de l’Insee parmi les chiffres de l’OCDE (cela donnerait le 4e rang au lieu du 2e) ; concept SEC/OCDE 2025 de 44,2 à 44,3 % | fichier 18, §1 ; journal n° 33 du fichier 00 |
| §4.9 | Trois chiffres d’intérêts (65,7 / 64,7 / 51,6) et la sous-estimation de 14,1 Md€ | fichier 18, §2 ; ligne 39 et journal n° 34 du fichier 00 |
| §4.15 | Fiche Immigration et AME | fichier 15 ; lignes 54-55 du fichier 00 |
| §4.16 | Fiches « économies faciles » : APD, UE, opérateurs, cabinets de conseil, responsables politiques, audiovisuel public, associations, AME | fichier 16 |
| §4.17 | Page de méthode : trois ponts | fichier 18 |
| §4.18 | Explication du bouclage macroéconomique | fichier 17 |
| §5.1 à §5.3 | Objectif de conception 4 ; ligne d’objectif « mesures brutes nécessaires » (≈ 94 pour l’objectif B : 61,9 / 0,658) ; leviers S13 à S19 ; tableau de correspondance macroéconomique pour chaque levier | fichiers 16, 17 |
| §5.4-§5.5 | Spécification de l’option 4 ; nouvelles règles contre le double compte ; résultat « effet sur la croissance » | fichier 17 |
| §6.3 | Réserve de rotation, questions 26 à 40 (36 à 40 ajoutées le 25 octobre 2026, marquées à gauche), avec une règle de symétrie pour les tirages | fichiers 15 à 18, 07, 05, 08, 10 ; `platform/data/quiz.json` |
| §9.1 | *Jaunes* du PLF (mi-octobre), PAP 183, CAD de l’OCDE (avril) | fichier 16 |
| §10, §11 | Lignes de l’inventaire des données ; lacunes 11 à 14 | fichiers 15 à 18 |

**C. Vérifié et inchangé**

| Valeur dans ce fichier | Contrôle |
|---|---|
| Déficit 151,6 Md€, dette 3 460,1 Md€, intérêts 65,7 Md€, PO 2024 42,7 %, dépenses publiques 2025 57,3 % / 2024 57,0 %, écarts de 7,6 pts / 227 Md€ et de 7,8 pts, dépense publique par habitant 23 330 SPA (8e), SOCX 32,0 %, protection sociale COFOG 23,6 %, défense 1,8 %, UE-27 27,4 %, PISA 2025, part détenue par les non-résidents 59,7 %, OAT 169 pb | Recherche (grep) des valeurs du §4 du fichier 00 : aucune valeur remplacée ne subsiste (le 64,7 du §4.4 correspond aux impôts affectés aux retraites, pas aux intérêts ; 64,7 au sens des intérêts n’apparaît plus qu’avec son étiquette Sifim aux §4.9 et §4.17) |
| Étalons des §3.1 à §3.4 (une journée 4,70 Md€ ; 32,3 jours ; 24 843 € ; intérêts 14,0 jours / 43,3 % / 952 € ; hausse des intérêts 25,3 = 5,4 jours / 16,7 % / 367 € ; Zucman de 0,4 à 4,3 jours) | Recalculés sur 1 714,1 / 151,6 / 68,998 : inchangés |
| Aide économique extérieure COFOG (question 6 du quiz : 0,3 % des dépenses publiques, 4,9 Md€) | Conforme au fichier 16, §2 (4,88 Md€ = 0,29 % des dépenses publiques) |

### Passe du 25 octobre 2026 – relecture des données de la plateforme (`platform/data/REVIEW.md`) et points ouverts du site

*Périmètre : les dix corrections et les quatre points éditoriaux de `platform/data/REVIEW.md`, et les points ouverts du §5.1 de `fr/LISEZMOI-site.md` (points 2, 3 et 5) qui portent sur des valeurs ou des libellés de ce fichier. Les valeurs ont été relues dans les fichiers 00, 02, 03, 04, 07, 11 et 12 ; aucun chiffre nouveau n’a été introduit. Les étalons sont calculés comme au §3.4 (jours = Md€ / 4,696 ; % du déficit = Md€ / 151,6 ; euros par habitant = Md€ × 1 000 / 68,998). Les deux parties de la traduction ont été mises à jour en même temps que le fichier anglais.*

**A. Corrections de valeurs et de libellés**

| Emplacement | Avant | Désormais | Fondement |
|---|---|---|---|
| §4.10 carte TVA sur l’énergie | « −11 à −17,4 » ; 2,3 à 3,7 jours | Coût « supérieur à 11 » (Institut Montaigne 2024, borne basse et seul chiffrage indépendant) ; les 12,2 du RN présentés comme chiffre annoncé ; les 17,4 de francebudget.fr ne sont pas retenus ; plus de 2,3 jours, 7,3 % du déficit, 159 € par habitant | REVIEW n° 1 ; fichier 07, §3.5 (17,4 « ne doit pas servir de référence » : assiette sans les carburants) ; fichier 11, §4.2 |
| §5.3 S9 | TVA sur l’énergie « de −11 à −17,4 » | Environ −11, une borne basse ; RN −12,2 ; 17,4 non retenu | REVIEW n° 2 ; idem |
| §4.10 carte Smic ; §5.3 S10 | « −3,5 à −4 » pour toute la fourchette 1 600-1 700 ; 0,7 à 0,9 jour | De −1,8 à −4 : 1 600 € net, environ de −1,8 à −2,2 (+8,3 % par rapport au Smic en vigueur depuis le 1er juin 2026) ; 1 700 € net, environ de −3,5 à −4 (+15 %) ; mise à l’échelle par la plateforme, signalée ; 0,4 à 0,9 jour | REVIEW n° 3-4 ; fichier 07, §3.6 (Smic relevé de 2,41 % le 1er juin 2026) ; fichier 11, §4.1 (1 700) et §4.6 (1 600) |
| §5.3 libellé de S2 | « gel d’un an des pensions de base, plus petites pensions protégées » | Sous-indexation partielle du PLFSS 2027 (revalorisation complète jusqu’à 1 260 € par mois seulement, moindre au-delà) ; valeur 4,1 inchangée (3,0 régimes de base + 1,1 État) | REVIEW n° 5 ; fichier 03 (chronologie, 1er octobre 2026, et tableau de vérification) |
| §6.3 question 20 | « 19,8 % SIASP » | 19,8 % DGAFP/Insee (périmètre de la fonction publique, estimations d’emploi de l’Insee, contrats aidés compris, 2024) ; 20,7 % OCDE (2023) | REVIEW n° 6 ; fichier 04, K7 et §4, point 4 |
| §6.3 questions 16 et 24 (traduction seulement) | « paient un impôt sur le revenu net » ; « budget de la programmation militaire » | « paie effectivement l’impôt sur le revenu (impôt net positif) » ; « charge de la dette de l’État » contre « enveloppe de la loi de programmation militaire (LPM) », comme dans `quiz.json` | REVIEW n° 7-8 ; glossaire (charge de la dette de l’État, LPM) |
| §5.1 point 3, §5.3 groupe B2, §4.16 (traduction seulement) | « Cibles populaires » | « Cibles souvent citées » | REVIEW n° 10 |
| §4.2 GF04 | renvoi au « §4.14 (aides aux entreprises) » dans le fichier anglais (signalé jusqu’ici par une note de traduction) | §4.12 dans les deux versions ; note de traduction supprimée | Renvoi interne |

**B. Points ouverts résolus**

| Point | Résolution | Fondement |
|---|---|---|
| S3, source de la borne basse (REVIEW, point 2 ; LISEZMOI-site §5.1, point 3) | 2,4 = chiffre du cabinet du ministre (juillet 2026, presse), étiqueté comme tel. 2,1 = calcul de la plateforme, 3,2 Md€ (coût en année pleine de la hausse de 1,5 % de juillet 2023, presse citant la fiche d’impact du décret) / 1,5 = 2,13 ; cohérent avec les 20 Md€ de l’Institut Montaigne pour +10 % (2 par point). Recoupement officiel partiel : versant de l’État 1,5 Md€ (Sénat, avis n° 134, PLF 2024). La ventilation à 2,07 (⚠) reste inutilisée. Fourchette inchangée ; chaque borne porte désormais sa source au §4.10 et au §5.3 | Fichier 07, §3.6 et tableau des divergences ; fichier 07 [S15], [S33], [S47] |
| Carte `rn_back_to_62` (REVIEW, point 3) | La carte et la question 13 affichent désormais les deux fourchettes indépendantes : abrogation seule de 16 à 17 Md€ (Cnav citée dans le rapport n° 613 de l’Assemblée nationale : 15,7 en 2032 ; Fipeco : 17 en 2030) et versions partielles de type RN de 26 à 35 Md€ (fichier 00, ligne 44) ; aucune n’est un chiffrage du plan 2027 ; chiffre annoncé par le RN environ 9 (9,5 en 2031 dans son annexe) | Fichier 11, §4.2 ; fichier 03, §4.1 et sa ligne Cnav ; fichier 00, ligne 44 |
| Taux par défaut de S5 (REVIEW, point 4 ; LISEZMOI-site §5.1, point 3) | Valeur par défaut +3,4 % (progression tendancielle 2027, situation de référence, rendement nul) ; repères +2,0 % (objectif du PLFSS 2027) et de 2 à 2,5 % (Cour des comptes). Contrôle : (3,4 − 2,0) × 10 × 0,27 ≈ 3,8 Md€, contre 3,9 Md€ d’économies nettes sur l’Ondam selon la Cour | Fichier 02, §4.3 (projet de loi n° 3211, art. 43 ; tendanciel +3,4 % ; Cour 3,9 Md€ nets) ; fichier 12, §7.2 (RALFSS 2026) |
| Titre du chapitre 1 (LISEZMOI-site §5.1, point 2) | Le titre du fichier du chapitre est retenu : « Combien ? ». Plan du §2.1 mis à jour ; les chapitres 5 et 6 reprennent aussi les titres de leurs fichiers (« La dette et ses intérêts », « Qu’obtient-on en échange ? ») | `site/chapitres/01-combien.md`, `05-dette-et-interets.md`, `06-ce-que-l-on-obtient.md` |
| En-tête de la 1re partie (LISEZMOI-site §5.1, point 5) | Il renvoie désormais à cette 2e partie pour les §5 à §11, le journal et les sources | – |

**C. Vérifié et inchangé**

| Point | Contrôle |
|---|---|
| Le point 1 de REVIEW situe le chiffre de 17,4 au « §3.4 » | Le §3.4 n’a pas de ligne TVA sur l’énergie ; la valeur figurait seulement dans la carte du §4.10 et dans S9 au §5.3, toutes deux corrigées |
| §4.4 (« retour à 62 ans : de 10 à 17 milliards… jusqu’à environ 26 milliards ») et §5.3 S1 (« à 62 ans : de −10 à −17 (système), environ −26 ») | Cohérents avec les deux fourchettes ci-dessus (fichier 03, §4.1) |
| §4.5 et S5 « 0,27 par tranche de 0,1 pt » | 0,001 × 273,3 = 0,273 (Ondam 2026, fichier 02, ligne 24) : inchangé |
| Synchronisation 15-18 | Comparaison section par section des nombres de la version anglaise et de la traduction : la traduction reprenait déjà toute la passe 15-18 ; seules les dates (format ISO dans la version anglaise) diffèrent |
| Non modifiés | `data/20_pedagogical_conversions.csv` (toujours à régénérer, §11, point 14) et `platform/data/*` (gérés ailleurs) |

---

## Sources

[^ref]: [`00-reference-figures.md`](../research/00-reference-figures.md) (valeurs canoniques, 25 octobre 2026), et les sources listées dans son tableau : Eurostat `gov_10a_main` et `gov_10dd_edpt1` (21 octobre 2026) https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table ; Insee, « Le compte des administrations publiques en 2025 », *Insee Première* n° 2106 (29 mai 2026) https://www.insee.fr/fr/statistiques/8997691 ; Insee, série « Taux de prélèvements obligatoires rapportés au produit intérieur brut » https://www.insee.fr/fr/statistiques/2381412 ; HCFP, *Avis n° HCFP-2026-5 relatif aux projets de lois de finances et de financement de la sécurité sociale pour l’année 2027* (25 septembre 2026) https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf ; COR, *Évolutions et perspectives des retraites en France – Rapport annuel* (juin 2026) https://www.cor-retraites.fr/sites/default/files/2026-06/RA_2026_def.pdf
[^cofog]: Eurostat `gov_10a_exp`, COFOG, administrations publiques, 2024 provisoire (21 octobre 2026). https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table ; fichiers `data/eurostat_gov_10a_exp_pctot.csv`, `data/eurostat_gov_10a_exp_mioeur.csv` ; fichier 01, §4.1.
[^conv]: Calcul de la plateforme, `data/20_pedagogical_conversions.csv` (25 octobre 2026), à partir des valeurs canoniques du fichier 00.
[^f01]: [`01-spending-overview.md`](../research/01-spending-overview.md) (Insee, « Usage de l’argent public : les dépenses publiques par fonction en 2024 », *Insee Première* n° 2093, février 2026 ; Eurostat COFOG).
[^f02]: [`02-social-protection.md`](../research/02-social-protection.md) (Drees, *La protection sociale en France et en Europe en 2024 – Résultats des comptes de la protection sociale*, 17 décembre 2025, https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/panoramas-de-la-drees/251217-protection-sociale-france-europe-2024 ; Drees, *Les dépenses de santé en 2025 – Résultats des comptes de la santé – Édition 2026* ; Commission des comptes de la sécurité sociale, *Les comptes de la Sécurité sociale – Résultats 2025, prévisions 2026 et 2027*, octobre 2026).
[^f03]: [`03-pensions.md`](../research/03-pensions.md) (COR, juin 2026 ; Cour des comptes, *Situation financière et perspectives du système de retraites*, février 2025 ; Fipeco, juin 2024 ; Institut Montaigne, 3 juillet 2024).
[^f04]: [`04-civil-service-and-outcomes.md`](../research/04-civil-service-and-outcomes.md) (DGAFP, *Rapport annuel sur l’état de la fonction publique – édition 2026* ; Eurostat `gov_10a_main`, `crim_just_job` ; OCDE, *Panorama des administrations publiques 2025* ; OCDE, *Regards sur l’éducation 2026*).
[^f05]: [`05-taxation.md`](../research/05-taxation.md) (Insee, tableaux 3.216/3.217, « Dépenses et recettes des administrations publiques en 2025 », 28 août 2026 ; OCDE, *Statistiques des recettes publiques 2025* ; OCDE, *Taxing Wages 2026* ; DGFiP, *Statistiques* n° 41 ; Insee, « Revenus des ménages élargis à l’ensemble de l’économie en 2023 », *Insee Analyses* n° 118, 16 avril 2026 ; IPP, *Note* n° 92 ; Cour des comptes, *Analyse de l’exécution budgétaire 2025 – Dépenses fiscales*).
[^f06]: [`06-deficit-and-debt.md`](../research/06-deficit-and-debt.md) (Insee ; Eurostat, notification PDE ; Cour des comptes, *La situation et les perspectives des finances publiques*, juin 2026 ; *Projet de loi de finances pour 2027* (n° 3210) https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf ; HCFP, avis 2026-5 ; Commission européenne, *Debt Sustainability Monitor 2025*).
[^f07]: [`07-proposals-costing.md`](../research/07-proposals-costing.md) (Sénat, rapport n° 689 (2024-2025) sur la proposition de loi instaurant un impôt plancher de 2 % sur le patrimoine des ultrariches, 4 juin 2025 ; IPP, juin 2026 ; Institut Montaigne, 2024 ; CAE, *Focus* n° 118 ; Cour des comptes, *La situation et les perspectives des finances publiques*, 15 juillet 2024, et *Les mesures exceptionnelles de lutte contre la hausse des prix de l’énergie*, 15 mars 2024).
[^f08]: [`08-revenue-cuts-since-2017-and-structural.md`](../research/08-revenue-cuts-since-2017-and-structural.md) (OFCE, *Policy Brief* n° 146 ; Rexecode, document de travail n° 105 ; Sénat, rapport n° 808 ; Haut-commissariat à la Stratégie et au Plan, *Les aides aux entreprises : définition, périmètres, cadre de suivi et d’évaluation*, juillet 2026 ; A. Bozio et É. Wasmer, *Les politiques d’exonérations de cotisations sociales : une inflexion nécessaire*, 2024 ; note de la DG Trésor pour le HCFiPS, août 2024 ; Eurostat `lfsi_emp_a`, `nama_10_lp_ulc` ; Insee, comptes de patrimoine de la Nation, 30 juillet 2026 ; OTAN, juillet 2026 ; J. Pisani-Ferry et S. Mahfouz, *Les incidences économiques de l’action pour le climat*, 2023).
[^f09]: [`09-international-comparison-tables.md`](../research/09-international-comparison-tables.md) (Eurostat, OCDE ; statistiques de groupes calculées).
[^f10]: [`10-counterarguments-and-debates.md`](../research/10-counterarguments-and-debates.md) (Haut-commissariat à la Stratégie et au Plan, juillet 2026 ; OFCE ; Cour des comptes ; FMI ; séries calculées d’Eurostat).
[^f11]: [`11-2027-candidate-programs-costing.md`](../research/11-2027-candidate-programs-costing.md) (LFI, 14 octobre 2026 ; RN, 6 octobre 2026 ; LR, 12 octobre 2026 ; Institut de l’Entreprise via PGE ; IPP, *Note* n° 125 ; bulletin hebdomadaire des prix des carburants de la DGEC, 16 octobre 2026).
[^f12]: [`12-health-hospital-outcomes-international.md`](../research/12-health-hospital-outcomes-international.md) (Eurostat SHA `hlth_sha11_*` ; OCDE, *Panorama de la santé 2025* ; OMS, GHED ; Drees ; Cour des comptes, avril 2026).
[^f13]: [`13-civil-service-and-education-intl-completion.md`](../research/13-civil-service-and-education-intl-completion.md) (OCDE, *Résultats du PISA 2025 (Volume I)*, 8 septembre 2026, https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report.html ; IEA, TIMSS 2023, PIRLS 2021 ; schéma d’emplois du PLF 2027).
[^f14]: [`14-public-perception-orders-of-magnitude.md`](../research/14-public-perception-orders-of-magnitude.md) (Elabe, Ifop, Odoxa, Drees *Baromètre*, Cevipof ; littérature académique).
[^f15]: [`15-immigration-and-public-finances.md`](../research/15-immigration-and-public-finances.md) (OCDE, *Perspectives des migrations internationales 2021*, chap. 4, https://www.oecd.org/en/publications/international-migration-outlook-2021_29f23e9d-en/full-report/component-8.html ; CEPII, *La Lettre du CEPII* n° 311 et n° 394 ; PAP 2027 du programme 183, https://www.budget.gouv.fr/documentation/file-download/33907 ; C. Évin et P. Stefanini, *Rapport sur l’aide médicale de l’État*, décembre 2023, https://www.vie-publique.fr/files/rapport/pdf/292122.pdf ; décision du Conseil constitutionnel n° 2024-6 RIP ; contre-budgets du RN ; Institut de l’Entreprise, 6 octobre 2026).
[^f16]: [`16-oda-eu-contribution-and-other-popular-targets.md`](../research/16-oda-eu-contribution-and-other-popular-targets.md) (données provisoires 2025 du CAD de l’OCDE, 9 avril 2026 ; PLF 2027 et ses *Jaunes*, dont *Relations financières avec l’Union européenne*, https://www.budget.gouv.fr/documentation/file-download/34459 ; rapports du Sénat n° 578 (2022) et n° 807 (2025) ; Commission européenne, *EU spending and revenue 2000-2025* ; iFRAP ; Institut Montaigne).
[^f17]: [`17-fiscal-multipliers-for-simulator.md`](../research/17-fiscal-multipliers-for-simulator.md) (HCFP, avis HCFP-2026-5, §36, 25 septembre 2026 ; CAE, *Focus* n° 108, 24 juillet 2024, https://www.cae-eco.fr/static/pdf/focus-108-240712-en.pdf ; DG Trésor/Insee, Mésange 2017 ; OFCE, e-mod.fr pour le HCFiPS, 2021, et *Policy Brief* n° 154, 2026 ; BCE, WP 1760 ; Banque de France, WP 883 ; Cour des comptes, *La situation et les perspectives des finances publiques*, juin 2026, et *Situation financière et perspectives du système de retraites*, février 2025 ; Guajardo-Leigh-Pescatori ; Alesina-Favero-Giavazzi ; mission de l’IGF, juillet 2026).
[^f18]: [`18-po-vs-oecd-and-interest-bridges.md`](../research/18-po-vs-oecd-and-interest-bridges.md) (Insee, tableaux des comptes nationaux 3.201 à 3.217, mai 2026, https://www.insee.fr/fr/statistiques/8988845 ; Eurostat `gov_10a_taxag`, `gov_10a_main`, `hlth_sha11_hf` ; OCDE, *Statistiques des recettes publiques 2025* ; Cour des comptes, *La situation et les perspectives des finances publiques*, juin 2026 ; PLF 2027).
[^cour24]: Cour des comptes, *La situation et les perspectives des finances publiques* (15 juillet 2024). https://www.ccomptes.fr/sites/default/files/2024-09/20240715-RSPFP-2024.pdf
[^cour26]: Cour des comptes, *La situation et les perspectives des finances publiques* (25 juin 2026). https://www.ccomptes.fr/sites/default/files/2026-07/20260625_RSPFP-2026.pdf
[^cour-bouclier]: Cour des comptes, *Les mesures exceptionnelles de lutte contre la hausse des prix de l’énergie* (15 mars 2024), via le fichier 07 [S12] et le fichier 11 [S19].
[^igf]: *Mission sur la transparence des finances publiques : situation tendancielle à horizon 2030* (Jaravel, Ragot, Tavernier, Valla), IGF, juillet 2026. https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/Transparence-finances-publiques.pdf
[^hcsp-aides]: Haut-commissariat à la Stratégie et au Plan, *Les aides aux entreprises : définition, périmètres, cadre de suivi et d’évaluation*, rapport au Premier ministre (juillet 2026), via le fichier 08.
[^cae118]: CAE, « Fiscalité du capital : quels sont les effets de l’exil fiscal sur l’économie ? », *Focus* n° 118 (juillet 2025). https://cae-eco.fr/static/pdf/Focus_118_emigration_fiscale_250725_v2.pdf
[^ipp125]: IPP, *Note* n° 125, Chapelle et Fack (mai 2026), via le fichier 11 [S18].
[^elabe26]: Elabe pour *Les Echos*, *Les Français et la dette publique* (terrain 1er-2 septembre 2026, n = 1 005). https://elabe.fr/fichier-pdf/13231-20260903_elabe_les-echos_les-francais-et-la-dette-publique/
[^ipsos21]: Ipsos (M. Gallard, L. Boisson), *Enquête sur la perception de la dette publique par les Français*, terrain 18-21 janvier 2021, n = 1 000 adultes de 18 ans et plus, panel en ligne, méthode des quotas. Publiée comme pièce jointe n° 4 du rapport 279092 de vie-publique.fr : https://www.vie-publique.fr/files/rapports/fichiers_joints/279092-pi%C3%A8ce%20jointe%204.pdf (téléchargée le 25 octobre 2026 dans `data/raw/20_perception/vp_279092_pj4.pdf`). Client : MINEFI, pour la *Commission sur l’avenir des finances publiques* (rapport Ipsos, « Rappel des objectifs (1/2) » : « Une enquête pour nourrir la réflexion de la Commission sur l’avenir des finances publiques »). Rapport principal : *Rapport de la Commission sur l’avenir des finances publiques*, J. Arthuis, remis le 18 mars 2021, https://www.vie-publique.fr/rapport/279092-commission-sur-lavenir-des-finances-publiques (page lue dans le navigateur le 25 octobre 2026 ; elle répertorie « Annexes - Pièce jointe n° 4 »).
[^hexagone]: Observatoire Hexagone, *Système de retraites : les Français divisés mais réformistes* (24 mars 2025), sondage Harris Interactive, n = 1 101. https://observatoire-hexagone.org/wp-content/uploads/2025/03/20250224_Hexagone_Retraites-2.pdf (téléchargé dans `data/raw/20_perception/hexagone_retraites_2025-02.pdf`). Terrain : en ligne, 21-24 février 2025, n = 1 101 adultes de 18 ans et plus, quotas (sexe, âge, profession, région, taille d’agglomération) et redressement, selon Toluna-Harris Interactive, *Les Français et le système de retraite* (mars 2025), p. 3 : https://observatoire-hexagone.org/wp-content/uploads/2025/03/Rapport-Toluna-Harris-Les-Francais-et-le-systeme-de-retraite-Hexagone.pdf (téléchargé dans `data/raw/20_perception/toluna/toluna_harris_hexagone_retraites.pdf`). *(Vérifié le 25 octobre 2026 : la mention était « dates de terrain non indiquées (⚠) ».)* Orientation : défend un système mixte, par répartition et par capitalisation.
[^kns]: Kuziemko, Norton, Saez, Stantcheva (2015), « How Elastic Are Preferences for Redistribution? », *American Economic Review* 105(4) : 1478-1508 (via le fichier 14).
[^stantcheva]: Stantcheva (2021), « Understanding Tax Policy: How do People Reason? », *Quarterly Journal of Economics* 136(4) : 2309-2369 (via le fichier 14).
[^douenne]: Douenne et Fabre (2022), « Yellow Vests, Pessimistic Beliefs, and Carbon Tax Aversion », *AEJ: Economic Policy* 14(1) : 81-110 (via le fichier 14).
[^ciani]: Ciani, Fréget, Manfredi (2021), *OECD Papers on Well-being and Inequalities*, méta-analyse d’expériences d’information (via le fichier 14).
