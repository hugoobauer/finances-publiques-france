# Chapitre 4. Pourquoi le déficit ?

<!--
NOTES POUR L’ÉQUIPE ÉDITORIALE (non affichées sur le site)

Statut : version finalisée, 25 octobre 2026 (passe « finalisation » ; voir Notes de relecture). À relire (relecture contradictoire et audit de symétrie, fichier 20 §7.1).
Plan suivi : research/20-pedagogical-approach.md §2.1 (Ch. 4), §1 P1-P10, §3 (étalons), §4.11 (baisses d’impôts depuis 2017), §4.8 (déficit). Termes, typographie et ton : fr/glossaire-et-conventions.md.
Seuls les blocs « Texte affiché », les fiches chiffre, les encadrés et la liste « Pour aller plus loin » sont publics ; le reste est de la spécification.

Syntaxe des pastilles source :
- [[fig:id]]   valeur de platform/data/figures.json
- [[yard:id]]  étalon de platform/data/yardsticks.json (yardsticks[], puis parameters[])
- [[prop:id]]  conversions publiées de platform/data/proposals.json
- [[src:id]]   source sans chiffre (citation, texte), id de platform/data/sources.json
- [[calc:…]]   calcul de la plateforme (illustratif) à partir d’identifiants existants

Plus aucune pastille provisoire : les 14 chiffres « à créer » du premier jet existent dans figures.json
(passe données du 25 octobre 2026, platform/data/REVIEW.md, « Data pass for the chapters, second pass »).

Écart de vocabulaire : la consigne parle de « Devinez d’abord » ; le glossaire (§1.13) fixe « Estimez d’abord ».

Hors champ volontaire (renvoyé au chapitre 7) : le test de faisabilité du Haut-commissariat à la Stratégie
et au Plan (fichier 10 §6.3), qui porte sur le remède et non sur la cause.
-->

---

## Étape 0. Ouverture

**Texte affiché**

> Le dernier excédent des comptes publics de la France remonte à 1974 [[fig:last_surplus_year]].
>
> Pourquoi le déficit s’est-il creusé ces dernières années ? Deux récits s’opposent. Pour le premier, il vient surtout des baisses d’impôts. Pour le second, surtout de la hausse des dépenses.
>
> Ce chapitre montre que les deux s’appuient sur des chiffres exacts. Ce qui les sépare, c’est surtout la période choisie : l’année de départ, mais aussi l’année d’arrivée.
>
> Durée de lecture : environ 8 minutes.

**Visuel / animation.** « Recettes » à gauche, « Dépenses » à droite, même taille, deux couleurs neutres (aucune couleur de parti), un point d’interrogation entre les deux.

**Pastilles source.** [[fig:last_surplus_year]] (Insee, série longue par sous-secteur, 28 août 2026).

---

## Étape 1. Estimez d’abord

**Texte affiché**

> De 2018 à 2023, les gouvernements successifs ont décidé des baisses d’impôts et de cotisations sociales.
>
> **Selon vous, combien coûtent-elles chaque année, en jours de dépense publique ?**
>
> *(Une journée de dépense publique : ce que dépensent toutes les administrations publiques, État, Sécurité sociale et collectivités, en un jour moyen.)*

**Estimez d’abord (question 1, notée).** Curseur de 0 à 60 jours, pas de 1 jour, départ à 30. Bouton « Valider mon estimation ». Réponse masquée avant validation.

**Texte affiché après validation**

> **Réponse : 13,2 jours** [[prop:tax_cuts_2018_2023]]. La Cour des comptes (juridiction financière) chiffre ces baisses à 62 milliards d’euros par an, en 2023 [[fig:tax_cuts_2018_2023_eur_bn]]. Une journée de dépense publique représente 4,70 milliards d’euros en 2025 [[yard:one_day_spending_eur_bn]].
>
> À titre de comparaison, la hausse des dépenses depuis 2019 représente 2,0 points de produit intérieur brut (PIB), soit 12,7 jours (notre calcul) [[fig:te_change_2019_2025_pp]] [[yard:te_change_2019_2025_days]]. Nous revenons sur les deux chiffres aux étapes 4 et 5.
>
> Votre estimation : {X} jours. Estimation moyenne des participants : {Y} jours.

**Estimez d’abord (question 2, non notée).**

> **Selon vous, qu’est-ce qui explique surtout la hausse du déficit ces dernières années ?**
> ○ La baisse des recettes (impôts, cotisations)
> ○ La hausse des dépenses
> ○ Les deux, à parts à peu près égales
> ○ Je ne sais pas
>
> *Il n’y a pas de mauvaise réponse. Nous revenons sur votre choix à l’étape 6.*

**Visuel / animation.** Frise de 365 jours (calendrier du chapitre 2). À la validation, un bloc de 13,2 jours se colore à côté de l’estimation de l’utilisateur, puis de la moyenne des participants.

**Pastilles source.** [[fig:tax_cuts_2018_2023_eur_bn]] (Cour des comptes, *La situation et les perspectives des finances publiques*, 15 juillet 2024) ; [[yard:one_day_spending_eur_bn]] (calcul de la plateforme d’après Eurostat, 21 octobre 2026) ; [[prop:tax_cuts_2018_2023]] ; [[fig:te_change_2019_2025_pp]] [[yard:te_change_2019_2025_days]] (calcul de la plateforme, illustratif).

---

## Étape 2. Le point de départ, l’année 2025

**Texte affiché**

> Point de départ : en 2025, les administrations publiques ont dépensé 1 714,1 milliards d’euros [[fig:te_2025_eur_bn]] et perçu 1 562,5 milliards [[fig:total_revenue_2025_eur_bn]]. L’écart, le déficit public, atteint 151,6 milliards d’euros, soit 5,1 % du PIB [[fig:deficit_2025_eur_bn]] [[fig:deficit_2025_pct_gdp]] (chapitre 1).

**Visuel / animation.** La frise se remplit au défilement ; une bande rouge couvre les derniers jours de l’année, comme au chapitre 1 (sans nouveau chiffre affiché).

**Pastilles source.** [[fig:te_2025_eur_bn]] [[fig:total_revenue_2025_eur_bn]] [[fig:deficit_2025_eur_bn]] [[fig:deficit_2025_pct_gdp]] (Eurostat, notification d’octobre 2026 ; Insee, 28 août 2026).

---

## Étape 3. Un déficit, c’est l’écart entre deux courbes

**Texte affiché**

> En 2025, les dépenses publiques représentent 57,3 % du PIB [[fig:te_2025_pct_gdp]] et les recettes publiques 52,2 % du PIB [[fig:total_revenue_2025_pct_gdp]].
>
> Les dépenses comprennent les intérêts de la dette : 65,7 milliards d’euros en 2025 [[fig:interest_2025_eur_bn]]. Hors intérêts, le déficit (« solde primaire ») est de 85,9 milliards d’euros, soit 2,9 % du PIB [[fig:primary_balance_2025_eur_bn]] [[fig:primary_balance_2025_pct_gdp]].
>
> Le déficit se creuse si les dépenses montent ou si les recettes baissent. Voyons les deux récits.

**Visuel / animation.** Lignes 2005-2025, axe « en % du PIB » : dépenses et recettes totales, écart grisé « déficit », fine bande « intérêts » au bas des dépenses. Repères discrets sur 2017 et 2019. Données : `research/data/debates/computed_fr_vs_eu27_fiscal_series.csv` (Eurostat gov_10a_main, S13, PC_GDP, 21 octobre 2026).

**Pastilles source.** [[fig:te_2025_pct_gdp]] [[fig:total_revenue_2025_pct_gdp]] [[fig:interest_2025_eur_bn]] [[fig:primary_balance_2025_eur_bn]] [[fig:primary_balance_2025_pct_gdp]].

---

## Étape 4. Premier récit, « le déficit vient des baisses d’impôts »

**Texte affiché**

> Ce récit est défendu notamment par des instituts de recherche et des associations. Parmi eux, l’OFCE (Observatoire français des conjonctures économiques ; Sciences Po, sensibilité keynésienne) et Attac (association altermondialiste) [[src:f10]]. Son point de départ : 2017.
>
> De 2017 à 2024, les recettes publiques passent de 54,3 % à 51,2 % du PIB [[fig:total_revenue_2017_pct_gdp]] [[fig:total_revenue_2024_pct_gdp]]. C’est une baisse de 3,1 points de PIB [[fig:total_revenue_change_2017_2024_pp]]. Après des hausses d’impôts (étape 7), elles remontent à 52,2 % du PIB en 2025 [[fig:total_revenue_2025_pct_gdp]]. C’est encore 2,1 points de moins qu’en 2017 [[calc:total_revenue_2025_pct_gdp − total_revenue_2017_pct_gdp = −2,1]].
>
> L’Insee (Institut national de la statistique et des études économiques) mesure aussi les prélèvements obligatoires (impôts et cotisations). Ils passent de 45,3 % du PIB en 2017 à 42,7 % du PIB en 2024 [[fig:po_2017_pct_gdp]] [[fig:po_2024_pct_gdp]]. Ils remontent à 43,6 % du PIB en 2025 [[fig:po_2025_pct_gdp]].
>
> Ce recul vient en partie de choix politiques [[src:f20:cour24]]. L’impôt sur les sociétés, les impôts de production et les cotisations sociales ont baissé ; la taxe d’habitation a été supprimée [[src:f20:cour24]].
>
> La Cour des comptes chiffre les baisses décidées de 2018 à 2023 à 62 milliards d’euros par an, en 2023 [[fig:tax_cuts_2018_2023_eur_bn]]. Cela représente 2,2 points de PIB [[fig:tax_cuts_2018_2023_pts]]. Selon elle, ces baisses ont été « non compensées par des économies en dépenses » [[src:f20:cour24]]. Elles ont donc été financées par l’emprunt.
>
> La Cour ne chiffre pas à part les mesures de 2018 sur le capital. Remplacer l’impôt de solidarité sur la fortune (ISF) par l’impôt sur la fortune immobilière (IFI) coûte de 3 à 4,5 milliards d’euros par an [[fig:isf_repeal_mechanical_loss_eur_bn]]. C’est l’estimation du Conseil d’analyse économique, avant effets de comportement.
>
> Pour le prélèvement forfaitaire unique (PFU), le comité d’évaluation de France Stratégie (2023) n’a pas détecté d’effet sur l’investissement ou les salaires [[src:f08]]. Il juge ce résultat fragile. Selon lui, la hausse des dividendes a autofinancé la mesure ses premières années [[src:f08]].

**Fiche chiffre « 62 milliards d’euros, en ordres de grandeur »** (estimé, Cour des comptes, coût en 2023)

| Étalon | Valeur |
|---|---|
| Jours de dépense publique (2025) | 13,2 jours [[prop:tax_cuts_2018_2023]] |

> *Une partie de ces baisses a été reprise depuis (étape 7).*

**Visuel / animation.** La courbe des recettes de l’étape 3 passe au premier plan ; flèche « −3,1 points de PIB » sur 2017-2024, puis remontée en 2025 ; puis un bloc de 13,2 jours se pose sur la frise.

**Encadré** (contre-argument au premier récit)

<!-- box-side: droite -->
> **Le meilleur contre-argument**
>
> **« 2017 est un sommet, pas une année ordinaire. »**
>
> En 2017, les recettes publiques atteignent 54,3 % du PIB, leur plus haut niveau de la série [[fig:total_revenue_2017_pct_gdp]] [[src:f10]]. Selon la Cour des comptes (juridiction financière), ce pic suit les hausses d’impôts de 2010 à 2014 : 3,8 points de PIB [[fig:tax_hikes_2010_2014_pts]].
>
> De plus, une partie de la baisse est comptable. Le crédit d’impôt pour la compétitivité et l’emploi (CICE) était compté comme une dépense jusqu’en 2018. En 2019, il a été remplacé par une baisse de cotisations, qui réduit les recettes. Ce n’est pas une baisse d’impôt nouvelle [[src:f09]] [[src:f01]].
>
> Enfin, selon la Cour des comptes, des recettes plus dynamiques que l’économie ont compensé ces baisses jusqu’en 2022. Le taux de prélèvements obligatoires est ainsi resté proche de celui de 2017. Il n’a nettement baissé qu’en 2023, surtout parce que ce dynamisme s’est retourné [[src:f20:cour24]].
>
> *Sources :* Cour des comptes (juridiction financière), *La situation et les perspectives des finances publiques*, 15 juillet 2024 et 25 juin 2026 ; Insee (institut public de statistique), *Le blog de l’Insee*, 24 octobre 2025. [[src:f10]] [[src:f20:cour24]] [[src:f20:cour26]] [[src:f09]]
>
> **Ce qu’on peut répondre**
>
> Même en partant d’un sommet, les baisses décidées depuis 2018 n’ont pas été financées par des économies de dépense (point d’accord, étape 7) [[src:f10]]. Et le CICE n’explique pas tout. Les prélèvements obligatoires mesurés par l’Insee (institut public de statistique) retirent déjà les crédits d’impôt. Ils ont eux aussi baissé de 2,6 points de PIB de 2017 à 2024 [[fig:po_change_2017_2024_pts]].

**Pastilles source.** [[fig:total_revenue_2017_pct_gdp]] [[fig:total_revenue_2024_pct_gdp]] [[fig:total_revenue_change_2017_2024_pp]] (Eurostat gov_10a_main, 21 octobre 2026) ; [[fig:total_revenue_2025_pct_gdp]] [[calc:total_revenue_2025_pct_gdp − total_revenue_2017_pct_gdp = −2,1]] (calcul de la plateforme d’après Eurostat gov_10a_main) ; [[fig:po_2017_pct_gdp]] [[fig:po_2024_pct_gdp]] [[fig:po_2025_pct_gdp]] [[fig:po_change_2017_2024_pts]] (Insee) ; [[fig:isf_repeal_mechanical_loss_eur_bn]] (Conseil d’analyse économique, *Focus* n° 118, juillet 2025 ; estimation mécanique) ; [[src:f08]] (comité d’évaluation des réformes de la fiscalité du capital, France Stratégie, octobre 2023) ; [[fig:tax_cuts_2018_2023_eur_bn]] [[fig:tax_cuts_2018_2023_pts]] [[src:f20:cour24]] ; [[fig:tax_hikes_2010_2014_pts]] (Cour des comptes, 25 juin 2026) ; [[src:f20:cour24]] (taux de prélèvements obligatoires 2017-2023, Cour des comptes, 15 juillet 2024) ; [[src:f01]] [[src:f09]] [[src:f10]]. Financement de l’OFCE : « Financé par une subvention publique versée par l’État à la Fondation nationale des sciences politiques (site de l’OFCE). » (https://www.ofce.fr/ofce/statuts.html).

---

## Étape 5. Second récit, « le déficit vient de la hausse des dépenses »

**Texte affiché**

> Ce récit est défendu notamment par des institutions publiques et internationales chargées de la surveillance budgétaire. Parmi elles, la Cour des comptes, le FMI (Fonds monétaire international ; organisation internationale) et l’OCDE (Organisation de coopération et de développement économiques ; organisation internationale).
>
> L’Institut Montaigne (libéral-centriste) et la Fondation iFRAP (libérale) le défendent aussi [[src:f10]]. Son point de départ : 2019, la dernière année avant la crise du Covid.
>
> De 2019 à 2025, les dépenses publiques augmentent de 2,0 points de PIB [[fig:te_change_2019_2025_pp]]. Les recettes reculent de 0,8 point de PIB [[fig:total_revenue_change_2019_2025_pp]].
>
> La Cour des comptes parle d’un « effet de cliquet » [[src:f20:cour26]]. Gonflées par les crises (Covid, puis énergie), les dépenses ne sont jamais revenues à leur niveau d’avant, en part du PIB. *La même Cour chiffre aussi le coût des baisses d’impôts : les deux récits ne s’excluent pas.*

**Fiche chiffre « 2,0 points de PIB, en ordres de grandeur »** (calcul de la plateforme, illustratif, au PIB de 2025)

| Étalon | Valeur |
|---|---|
| En milliards d’euros | environ 60 milliards d’euros [[calc:te_change_2019_2025_pp × one_point_gdp_eur_bn = 59,8]] |
| Jours de dépense publique (2025) | 12,7 jours [[yard:te_change_2019_2025_days]] |

> *C’est la variation d’un ratio, qui dépend aussi du PIB : on ne peut pas l’opposer terme à terme aux 62 milliards d’euros de baisses décidées [[fig:tax_cuts_2018_2023_eur_bn]].*

**Visuel / animation.** Même graphique ; la courbe des dépenses passe au premier plan, flèche « +2,0 points de PIB » sur 2019-2025, étiquettes sur les pics 2020 (Covid) et 2022 (énergie), pointillé horizontal au niveau de 2019.

**Encadré** (contre-argument au second récit)

<!-- box-side: gauche -->
> **Le meilleur contre-argument**
>
> **« Partir de 2019, c’est partir juste avant les crises. »**
>
> Si l’on part de 2017, les dépenses publiques ont même un peu baissé : de 0,4 point de PIB entre 2017 et 2025 [[calc:te_change_2017_2024_pp + te_2025_pct_gdp − te_2024_pct_gdp = −0,4]]. La baisse atteint 0,7 point si l’on s’arrête en 2024 [[fig:te_change_2017_2024_pp]]. Dans le même temps, les recettes ont reculé de 2,1 points de PIB [[calc:total_revenue_2025_pct_gdp − total_revenue_2017_pct_gdp = −2,1]].
>
> L’OFCE (Sciences Po, sensibilité keynésienne) étudie la période de 2017 à 2024. Pour lui, la hausse du déficit vient donc de la baisse des prélèvements. Celle-ci n’a pas été accompagnée des économies annoncées.
>
> *Source :* OFCE (Sciences Po, sensibilité keynésienne), « Quelles trajectoires pour les finances publiques de la France ? », *Policy Brief* n° 146, 11 juillet 2025. [[src:f10]] [[src:f08]]
>
> **Ce qu’on peut répondre**
>
> Une partie de cette baisse des dépenses est comptable : la transformation du CICE (étape 4) a fait disparaître des subventions des comptes publics. L’OFCE (Sciences Po, sensibilité keynésienne) le signale lui-même : cet effet corrigé, la baisse des dépenses qu’il mesure devient faible [[src:f08]]. Sur la baisse des recettes depuis 2017, en revanche, l’objection tient.

**Pastilles source.** [[fig:te_change_2019_2025_pp]] [[fig:total_revenue_change_2019_2025_pp]] [[fig:te_change_2017_2024_pp]] (calcul de la plateforme d’après Eurostat gov_10a_main, 21 octobre 2026) ; [[calc:te_change_2017_2024_pp + te_2025_pct_gdp − te_2024_pct_gdp = −0,4]] [[calc:total_revenue_2025_pct_gdp − total_revenue_2017_pct_gdp = −2,1]] (calcul de la plateforme, mêmes séries) ; [[yard:one_point_gdp_eur_bn]] [[yard:te_change_2019_2025_days]] ; [[src:f20:cour26]] ; [[src:f10]] ; [[src:f08]]. Financement : « Financé par des contributions privées de plus de 200 entreprises, chacune à moins de 1,2 % du budget (site de l’Institut Montaigne). » (https://www.institutmontaigne.org/qui-sommes-nous) ; « Financée intégralement par des dons privés ; n’accepte ni subvention publique ni financement de parti (site de la Fondation iFRAP). » (https://www.ifrap.org/qui-sommes-nous).

---

## Étape 6. Les deux périodes, côte à côte

**Texte affiché**

> Les deux récits utilisent les mêmes statistiques, mais pas la même année de départ. Ici, les deux périodes s’arrêtent en 2025.

| Période | Dépenses publiques | Recettes publiques | Solde public | Lecture |
|---|---|---|---|---|
| De 2017 à 2025 | −0,4 pt de PIB [[calc:te_change_2017_2024_pp + te_2025_pct_gdp − te_2024_pct_gdp = −0,4]] | −2,1 pts de PIB [[calc:total_revenue_2025_pct_gdp − total_revenue_2017_pct_gdp = −2,1]] | −1,7 pt de PIB [[calc:(total_revenue_2025_pct_gdp − total_revenue_2017_pct_gdp) − (te_change_2017_2024_pp + te_2025_pct_gdp − te_2024_pct_gdp) = −1,7]] | Surtout les recettes |
| De 2019 à 2025 | +2,0 pts de PIB [[fig:te_change_2019_2025_pp]] | −0,8 pt de PIB [[fig:total_revenue_change_2019_2025_pp]] | −2,7 pts de PIB [[fig:balance_change_2019_2025_pp]] | Surtout les dépenses |

*En points de PIB. Un solde en baisse signifie un déficit plus grand. Arrondis à 0,1 point près.*

> **Depuis 2017 : surtout les recettes. Depuis 2019 : surtout les dépenses.**
>
> L’année d’arrivée compte aussi. De 2019 à 2024, les deux effets sont à peu près égaux. Les dépenses augmentent de 1,7 point de PIB [[calc:te_change_2019_2025_pp − (te_2025_pct_gdp − te_2024_pct_gdp) = 1,7]], les recettes baissent de 1,8 point [[calc:total_revenue_change_2019_2025_pp − (total_revenue_2025_pct_gdp − total_revenue_2024_pct_gdp) = −1,8]].
>
> La hausse des impôts de 2025 réduit la baisse des recettes mesurée depuis 2019. Depuis 2005, dépenses et recettes ont toutes deux augmenté en points de PIB, les dépenses nettement plus [[src:f10]].
>
> Selon la période choisie, on ne voit qu’une partie de l’histoire.
>
> À l’étape 1, vous avez répondu : {réponse}. Les deux récits sont exacts : ils ne répondent pas à la même question.

**Interaction : curseur d’année de référence** (composant de la fiche « Les baisses d’impôts depuis 2017 », spécification research/20 §4.11).

> *Choisissez vous-même l’année de départ et l’année d’arrivée.*

- Poignées : départ 2005-2019, arrivée jusqu’à 2025 ; par défaut 2017 → 2025.
- Cascade « en points de PIB » : dépenses hors intérêts, intérêts, recettes (signe de l’effet sur le solde), solde.
- Titre dynamique : « Depuis {année} : surtout les recettes » / « surtout les dépenses » / « les deux, à parts à peu près égales » (écart des deux effets inférieur à 0,3 point).
- Données : `computed_fr_vs_eu27_fiscal_series.csv` ; tests de non-régression : les deux lignes du tableau, 2017 → 2024 (« surtout les recettes ») et 2019 → 2024 (« les deux, à parts à peu près égales », écart de 0,1 point).

**Pastilles source.** [[calc:te_change_2017_2024_pp + te_2025_pct_gdp − te_2024_pct_gdp = −0,4]] [[calc:total_revenue_2025_pct_gdp − total_revenue_2017_pct_gdp = −2,1]] [[calc:(total_revenue_2025_pct_gdp − total_revenue_2017_pct_gdp) − (te_change_2017_2024_pp + te_2025_pct_gdp − te_2024_pct_gdp) = −1,7]] [[calc:te_change_2019_2025_pp − (te_2025_pct_gdp − te_2024_pct_gdp) = 1,7]] [[calc:total_revenue_change_2019_2025_pp − (total_revenue_2025_pct_gdp − total_revenue_2024_pct_gdp) = −1,8]] (calcul de la plateforme à partir des pastilles existantes, recoupé avec `computed_fr_vs_eu27_fiscal_series.csv`) ; [[fig:te_change_2017_2024_pp]] [[fig:total_revenue_change_2017_2024_pp]] [[fig:te_change_2019_2025_pp]] [[fig:total_revenue_change_2019_2025_pp]] [[fig:balance_change_2019_2025_pp]] (calcul de la plateforme d’après Eurostat gov_10a_main, 21 octobre 2026) ; [[src:f10]].

---

## Étape 7. Un point d’accord, et ce qui a changé depuis 2024

**Texte affiché**

> Les deux lectures partagent un constat : les baisses d’impôts de 2018 à 2023 n’ont pas été financées par les économies de dépense annoncées. L’OFCE, la Cour des comptes et Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire) l’écrivent tous trois [[src:f10]].
>
> Depuis 2024, le mouvement s’est en partie inversé. Rexecode (institut de conjoncture proche des organisations patronales) compte 36,7 milliards d’euros de prélèvements nouveaux de 2024 à 2026 [[fig:rexecode_levies_2024_2026_eur_bn]]. C’est 1,2 point de PIB [[fig:rexecode_levies_2024_2026_pts]], soit 7,8 jours de dépense publique (notre calcul) [[yard:rexecode_levies_2024_2026_days]].
>
> En 2025, selon la Cour des comptes, la baisse du déficit s’explique « exclusivement » par des hausses d’impôts et de cotisations de 23,0 milliards d’euros [[fig:cour_2025_tax_increases_eur_bn]]. Les dépenses, elles, ont continué d’augmenter un peu plus vite que l’économie [[src:f20:cour26]].
>
> Sur le remède, les avis divergent. Pour la Cour des comptes et le FMI, le niveau déjà élevé des prélèvements réduit les marges du côté des recettes [[src:f20:cour26]] [[src:f10]]. Ils orientent donc l’ajustement plutôt vers la dépense. Les économistes du premier récit jugent naturel de revenir sur une partie des baisses décidées depuis 2017.
>
> Terra Nova (centre gauche) juge justifié de taxer davantage les plus fortunés, mais pour une petite partie seulement de l’ajustement [[src:f10]].
>
> Revenir sur les baisses d’impôts, réduire les dépenses, ou les deux ? C’est un choix politique, que nous ne tranchons pas. Le chapitre 7 chiffre chaque option.

**Visuel / animation.** Balance à deux plateaux : « baisses décidées de 2018 à 2023 » (13,2 jours) ; « prélèvements nouveaux 2024-2026 (Rexecode) » (7,8 jours). Elle ne revient pas à l’équilibre. Légende : « Ordres de grandeur ; sources et méthodes différentes (Cour des comptes, coût en 2023 ; Rexecode, mesures nouvelles cumulées). »

**Pastilles source.** [[src:f10]] ; [[fig:rexecode_levies_2024_2026_eur_bn]] [[fig:rexecode_levies_2024_2026_pts]] (Rexecode, document de travail n° 105, septembre 2026) ; [[yard:rexecode_levies_2024_2026_days]] ; [[fig:cour_2025_tax_increases_eur_bn]] [[src:f20:cour26]] (Cour des comptes, 25 juin 2026) ; FMI, déclaration de fin de mission au titre de l’article IV, 21 mai 2026 (notre traduction, via [[src:f10]]) ; Terra Nova, note de G. Hannezo, 20 septembre 2024 (via [[src:f10]]). Financement : « Financé par ses adhérents, une soixantaine d’entreprises et d’organisations professionnelles, dont le Medef, l’UIMM et France Industrie (site de Rexecode). » (https://www.rexecode.fr/l-institut/nos-adherents) ; « Financé par du mécénat, des adhésions et des dons (site de Terra Nova). » (https://tnova.fr/qui-sommes-nous/).

---

## Étape 8. Qui porte le déficit ?

**Texte affiché**

> En 2025, l’État porte 128,1 des 151,6 milliards d’euros de déficit, soit 84,5 % (notre calcul) [[fig:deficit_state_2025_eur_bn]] [[fig:deficit_2025_eur_bn]] [[yard:deficit_state_share_pct]].
>
> **Attention à la lecture.** Ces soldes dépendent des transferts entre administrations. La taxe d’habitation a été supprimée et des cotisations ont baissé. Pour compenser, l’État a cédé une part de la taxe sur la valeur ajoutée (TVA) aux collectivités et à la Sécurité sociale.
>
> Selon la Cour des comptes, ces baisses « ont creusé le déficit de l’État et accru sa dette » [[src:f20:cour24]]. Un petit déficit ne signifie donc pas, à lui seul, une gestion plus économe.

**Fiche chiffre « Le déficit 2025 par sous-secteur »** (mesuré, Insee ; conversions : notre calcul)

| Sous-secteur | Déficit 2025 | Jours de dépense publique | Part du déficit |
|---|---|---|---|
| État | 128,1 Md€ [[fig:deficit_state_2025_eur_bn]] | 27,3 jours [[calc:deficit_state_2025_eur_bn / one_day_spending_eur_bn = 27,3]] | 84,5 % [[yard:deficit_state_share_pct]] |
| Administrations publiques locales (APUL) | 15,6 Md€ [[fig:deficit_apul_2025_eur_bn]] | 3,3 jours [[calc:deficit_apul_2025_eur_bn / one_day_spending_eur_bn = 3,3]] | 10,3 % [[calc:deficit_apul_2025_eur_bn / deficit_2025_eur_bn = 10,3 %]] |
| Administrations de sécurité sociale (ASSO) | 5,8 Md€ [[fig:deficit_asso_2025_eur_bn]] | 1,2 jour [[calc:deficit_asso_2025_eur_bn / one_day_spending_eur_bn = 1,2]] | 3,8 % [[calc:deficit_asso_2025_eur_bn / deficit_2025_eur_bn = 3,8 %]] |
| Organismes divers d’administration centrale (ODAC) | 2,2 Md€ [[fig:deficit_odac_2025_eur_bn]] | 0,5 jour [[calc:deficit_odac_2025_eur_bn / one_day_spending_eur_bn = 0,5]] | 1,5 % [[calc:deficit_odac_2025_eur_bn / deficit_2025_eur_bn = 1,5 %]] |
| **Total des administrations publiques** | **151,6 Md€** [[fig:deficit_2025_eur_bn]] | **32,3 jours** [[yard:deficit_days]] | **100 %** |

*« L’État » au sens de la comptabilité nationale, pas du budget voté. Somme des sous-secteurs : 151,7 Md€ (arrondis).*

**Visuel / animation.** Une barre rouge de 151,6 Md€ se découpe en quatre segments proportionnels (État, APUL, ASSO, ODAC) qui glissent sur la frise. Une flèche « part de TVA » relie l’État aux APUL et aux ASSO pendant « Attention à la lecture ».

**Pastilles source.** [[fig:deficit_state_2025_eur_bn]] [[fig:deficit_odac_2025_eur_bn]] [[fig:deficit_apul_2025_eur_bn]] [[fig:deficit_asso_2025_eur_bn]] (Insee, *Capacité ou besoin de financement des administrations publiques au sens de Maastricht par sous-secteur, 1949-2025*, 28 août 2026) ; [[fig:deficit_2025_eur_bn]] ; [[yard:deficit_state_share_pct]] [[yard:deficit_days]] [[yard:one_day_spending_eur_bn]] ; [[src:f20:cour24]] ; [[src:f08]] ; [[src:f06]].

---

## Étape 9. Et chez nos voisins ?

**Texte affiché**

> La France dépense 7,6 points de PIB de plus que la zone euro à 21 pays (ZE21, Bulgarie comprise) [[fig:spending_gap_ea21_2025_pp]] (chapitre 1). Elle prélève aussi davantage : 2e sur 36 pays de l’OCDE en 2024 [[fig:oecd_tax_to_gdp_2024_rank]] (chapitre 3).
>
> La France dépense beaucoup plus que la moyenne de ses voisins, et prélève aussi beaucoup plus. Son déficit, c’est l’écart entre les deux : il n’a pas été comblé depuis 1974 [[fig:last_surplus_year]].

**Visuel / animation.** Deux panneaux côte à côte, même style, sans couleur d’alerte et sans nouveau chiffre : « Dépenses : France plus haut que la ZE21 (chapitre 1) » ; « Prélèvements : France 2e de l’OCDE (chapitre 3) ». Chaque panneau affiche l’année et le groupe de pays.

**Pastilles source.** [[fig:spending_gap_ea21_2025_pp]] (calcul de la plateforme d’après Eurostat gov_10a_main, 21 octobre 2026) ; [[fig:oecd_tax_to_gdp_2024_rank]] (OCDE, *Statistiques des recettes publiques 2025*, décembre 2025) ; [[fig:last_surplus_year]] (Insee, 28 août 2026).

---

## Étape 10. Ce qu’il faut retenir, et la suite

**Texte affiché**

> **À retenir**
> - En 2025, le déficit public atteint 151,6 milliards d’euros, soit 32,3 jours de dépense publique [[fig:deficit_2025_eur_bn]] [[yard:deficit_days]].
> - En points de PIB, le creusement vient surtout des recettes de 2017 à 2025. Il vient surtout des dépenses de 2019 à 2025, et des deux à parts à peu près égales de 2019 à 2024.
> - Les baisses d’impôts décidées de 2018 à 2023 coûtent 62 milliards d’euros par an, soit 13,2 jours de dépense publique [[fig:tax_cuts_2018_2023_eur_bn]] [[prop:tax_cuts_2018_2023]]. Les économies annoncées pour les financer n’ont pas été réalisées, selon la Cour des comptes, l’OFCE et Fipeco (point d’accord).
> - La hausse des dépenses de 2019 à 2025 atteint 2,0 points de PIB [[fig:te_change_2019_2025_pp]]. C’est environ 60 milliards d’euros au PIB de 2025, soit 12,7 jours de dépense publique [[calc:te_change_2019_2025_pp × one_point_gdp_eur_bn = 59,8]] [[yard:te_change_2019_2025_days]].
> - Depuis 2024, les prélèvements remontent en partie, mais les dépenses augmentent encore un peu plus vite que l’économie [[src:f20:cour26]].
> - L’État porte l’essentiel du déficit, en partie parce qu’il finance les autres administrations.
>
> Chaque année de déficit s’ajoute à la dette. Et la dette entraîne des intérêts, dont la charge augmente.
>
> **→ Chapitre 5 : La dette et ses intérêts**

**Pour aller plus loin** (liens vers les fiches thématiques)

- *Les baisses d’impôts depuis 2017* : toutes les mesures et leurs effets.
- *Déficit et dette* : chaque administration.
- *Méthode* : les prélèvements selon l’OCDE et l’Insee.
- *Débats* : contre-arguments, auteurs et orientations.

**Boutons secondaires**

- « Choisissez votre année de référence » (curseur de l’étape 6 en plein écran).
- « Équilibrez vous-même le budget » (simulateur ; baisses d’impôts et économies de dépense au même niveau de menu).
- « Vérifiez une promesse » (toute mesure convertie en jours, en part du déficit et en euros par habitant).

**Visuel / animation.** La bande rouge de 32,3 jours se transforme en un trait qui monte : la courbe de la dette, qui ouvre le chapitre 5.

**Pastilles source.** [[fig:deficit_2025_eur_bn]] [[yard:deficit_days]] [[fig:tax_cuts_2018_2023_eur_bn]] [[prop:tax_cuts_2018_2023]] [[fig:te_change_2019_2025_pp]] [[yard:one_point_gdp_eur_bn]] [[yard:te_change_2019_2025_days]] [[src:f20:cour26]].

---

## Notes de relecture

### Passe « finalisation » du 25 octobre 2026

Décisions de site suivies : D-data-pass, D-return60, D-labels, D-boxes, D-ownership, D-rounding, D-vocabulary, D-reading-time. Validateur (`python3 -I validate.py --strict --details`) : **0 erreur et 0 avertissement propres au chapitre 4**. Trois avertissements transversaux citent encore le chapitre 4, mais ils viennent d’autres chapitres : arrondi de `po_2025_pct_gdp` (« environ 44 » au chapitre 3, ligne 43) ; étiquettes manquantes ou anciennes de la Cour des comptes (chapitres 2 et 7), du FMI (chapitre 7) et de l’Institut Montaigne (chapitre 7). Texte visible (comptage du validateur) : **1 836 mots avant, 1 918 mots après** ; « Durée de lecture : environ 8 minutes. » inchangée (1 918 / 240 = 8,0).

1. *D-data-pass et D-return60.* **Sans objet.** Aucun des 19 nouveaux identifiants n’est affecté au chapitre 4 ; le chapitre n’affiche pas le retour à 60 ans. Aucun chiffre ajouté.
2. *D-labels (glossaire §1.13, recopié mot pour mot).* **Appliqué.** Première mention de la page : « La Cour des comptes (juridiction financière) » (étape 1) ; « le FMI (Fonds monétaire international ; organisation internationale) » et « l’OCDE (Organisation de coopération et de développement économiques ; organisation internationale) » (étape 5, l’OCDE y étant l’un des camps du débat). OFCE, Attac, Institut Montaigne, Fondation iFRAP, Fipeco, Rexecode et Terra Nova étaient déjà conformes. Dans les deux encadrés et leurs réponses, chaque organisme porte son étiquette : Cour des comptes, Insee (institut public de statistique), OFCE. Financement vérifié sur le site de l’organisme, ajouté aux pastilles source (texte et URL du glossaire) : OFCE (étape 4) ; Institut Montaigne et Fondation iFRAP (étape 5) ; Rexecode et Terra Nova (étape 7). Attac et Fipeco : aucune mention (financement non détaillé sur leur site).
3. *D-boxes (glossaire §4.6).* **Appliqué** aux deux encadrés (étape 4, `box-side: droite` ; étape 5, `box-side: gauche` ; total du chapitre : 1 droite, 1 gauche). Titre affiché exact `**Le meilleur contre-argument**` dans le bloc cité ; l’ancien intertitre « ### Encadré « Le meilleur contre-argument » (…) » devient une ligne de spécification « **Encadré** (…) ». Thèse en gras entre guillemets ; auteur nommé avec son étiquette dans le corps (« Selon la Cour des comptes (juridiction financière) » ; « L’OFCE (Sciences Po, sensibilité keynésienne) étudie… ») ; ligne de source en italique commençant par « *Source(s) :* », qui reprend l’étiquette, titres de publication en italique (*La situation et les perspectives des finances publiques*, *Le blog de l’Insee*, *Policy Brief*) ; « , OFCE, » en double retiré de la ligne de source de l’étape 5. « Ce qu’on peut répondre » est passé dans le bloc cité, juste après l’encadré. Réponse de l’étape 5 : « Sur la baisse des recettes depuis 2017, en revanche, l’objection tient. » ajouté (règle §4.6 : dire ce qui résiste ; les recettes baissent de 2,1 points de PIB de 2017 à 2025, chiffre déjà affiché).
4. *D-ownership.* **Sans changement.** Le chapitre 4 reste propriétaire des 62 milliards / 13,2 jours (étapes 1 et 4) et du constat Cour/FMI sur le remède (étape 7). Aucun doublon de la liste (AME, contribution à l’UE, fraude sociale, aides aux entreprises, paquet de 10 à 25 milliards, CDHR, 980 000 emplois) n’apparaît dans le chapitre. Étape 9 : renvois « (chapitre 1) » et « (chapitre 3) » placés après chaque chiffre rappelé.
5. *Équilibre des listes d’« économies faciles ».* **Sans objet** : le chapitre 4 n’en contient pas.
6. *Validateur, avertissements du chapitre.* **Appliqué.**
   - Étape 1 : la pastille `[[prop:tax_cuts_2018_2023]]` est placée dans la phrase des 13,2 jours (avertissements `unchipped` et `chip-no-number`).
   - Étape 5 : pastille `[[fig:tax_cuts_2018_2023_eur_bn]]` ajoutée aux « 62 milliards d’euros » de la note de la fiche chiffre.
   - Étape 6 : « la période 2019-2024 » devient « de 2019 à 2024 » (`typo-range`) ; dans l’encadré de l’étape 5, « qui étudie 2017-2024 » devient « la période de 2017 à 2024 ».
   - Ligne de source de l’étape 4 : titres en italique (`typo-italics`).
   - Phrases de plus de 25 mots (20) et paragraphes de plus de 60 mots (8) : tous découpés, sans changer le sens ni les chiffres. Liste « À retenir » : tirets « – » remplacés par « - » (puces de liste), pour que chaque point compte comme un paragraphe.
7. *Sigles (§2.7).* **Appliqué.** « PIB » développé à sa première occurrence (étape 1, « produit intérieur brut (PIB) ») : le validateur ne le signalait pas parce que la première occurrence était entre parenthèses. « Insee » développé à sa première occurrence affichée (étape 4). « ISF » : développement corrigé en « impôt de solidarité sur la fortune » (le texte disait « impôt sur la fortune »). Tableau de l’étape 8 : « Administrations publiques locales (APUL) ».
8. *Références internes.* « via le fichier 08 » retiré d’une pastille de l’étape 4 ; la spécification du curseur (étape 6) renvoie à la fiche « Les baisses d’impôts depuis 2017 ».

**Points ouverts (hors périmètre du chapitre 4)**
- Le chapitre 3 (ligne 43) affiche `po_2025_pct_gdp` à la fois en « 43,6 % » et en « environ 44 % » : à aligner sur 43,6 %.
- Le chapitre 7 doit recopier les étiquettes « Cour des comptes (juridiction financière) », « FMI (… ; organisation internationale) » et « Institut Montaigne (libéral-centriste) » ; le chapitre 2 doit recopier celle de la Cour des comptes.
- Les `[[calc:]]` des fenêtres 2017-2025 et 2019-2024 restent en place tant que `te_change_2017_2025_pp`, `total_revenue_change_2017_2025_pp`, `balance_change_2017_2025_pp`, `te_change_2019_2024_pp` et `total_revenue_change_2019_2024_pp` n’existent pas ; `po_2022_pct_gdp` (encadré de l’étape 4) et la ligne 2005-2025 (étape 6) attendent aussi la passe données.
- Étape 7 : la pastille FMI cite la déclaration de fin de mission du 21 mai 2026 via `f10`. La nouvelle entrée `f06:imf_aiv2026` correspond au communiqué de presse du conseil d’administration (22 juillet 2026), un autre document : elle n’est pas substituée.

### Passe « corrections transversales » du 25 octobre 2026 (passe transversale, plan de site)

Décisions de site appliquées : D-ownership, D-rounding, D-titles-and-transitions, D-boxes, D-labels, D-reading-time, D-vocabulary. Validateur (`python3 -I validate.py`) : PASS, 0 erreur, 0 avertissement (1 061 pastilles de chapitres vérifiées). Texte visible (script de comptage : titres, blocs « Texte affiché », fiches chiffre, tableaux, encadrés et réponses, « Pour aller plus loin » ; hors commentaires, visuels, pastilles, spécifications et notes) : **2 298 mots avant, 2 165 mots après**, sous la cible de 2 200.

1. *Durée de lecture.* **Appliqué.** Ligne isolée « Durée de lecture… Niveau : B1 » supprimée ; « Durée de lecture : environ 9 minutes. » ajoutée en fin d’étape 0 (2 165 mots / 240 mots par minute = 9,0). « Niveau : B1 » n’est plus affiché.
2. *Titres d’étape.* **Appliqué.** Onze titres « ## Étape N : Titre » → « ## Étape N. Titre ».
3. *Étape 1, propriétaire des 62 milliards / 13,2 jours et de la question notée.* **Sans changement** (conforme).
4. *Étape 2, bloc déficit 2025 (propriétaire : chapitre 1).* **Appliqué.** Texte remplacé par une phrase de rappel avec renvoi « (chapitre 1) » ; encart « Si la France était un ménage » supprimé (pas de ligne « ménage » au chapitre 4) ; pile de 11 pièces retirée du visuel, frise et bande rouge gardées sans chiffre affiché ; pastilles `borrowed_one_euro_in`, `borrowing_starts_day`, `household_monthly_income_eur`, `household_spending_month_eur`, `household_borrowing_month_eur` retirées (`deficit_days` reste à l’étape 8 et à l’étape 10).
5. *Étape 4, signes dans le texte courant.* **Appliqué.** « une baisse de 3,1 points de PIB » ; « soit 2,1 points de moins qu’en 2017 » (les `[[calc:]]` gardent leur résultat signé). Ajout « Elles ont donc été financées par l’emprunt. » après la citation de la Cour. La flèche du visuel garde « −3,1 points de PIB » (étiquette de graphique, pas texte courant).
6. *Étape 4, encadré (contre-argument de droite « 2017 est un sommet », conservé).* **Appliqué.** Titres en italique dans la ligne de sources (*La situation et les perspectives des finances publiques* ; *Le blog de l’Insee*).
7. *Étape 5, étiquettes et encadré (contre-argument de gauche, OFCE, conservé).* **Appliqué.** Institut Montaigne → « (libéral-centriste) » ; par cohérence avec D-labels, « l’iFRAP (libéral) » → « la Fondation iFRAP (libérale) ». Encadré : « de 0,4 point de PIB » et « de 0,7 point » sans signe ; *Policy Brief* en italique. Le glossaire §424 n’était pas encore mis à jour au moment de la passe : étiquettes reprises de la décision D-labels, à vérifier mot pour mot une fois le glossaire publié. Le financement (passé de l’étiquette visible à la pastille source) n’est pas ajouté aux pastilles : la vérification sur le site de chaque organisme relève du propriétaire du glossaire.
8. *Étape 7, Rexecode.* **Appliqué.** « institut de conjoncture proche des organisations patronales » (même libellé qu’aux chapitres 3 et 7). Paragraphe « Sur le remède » conservé : le chapitre 4 en est propriétaire (le chapitre 7, étape 10, y renvoie).
9. *Étape 9, écart international (chapitre 1) et comparaison OCDE (chapitre 3).* **Appliqué.** Trois premiers paragraphes remplacés par deux phrases de rappel (7,6 points de PIB, ZE21 développée à la première occurrence de la page ; 2e sur 36 pays de l’OCDE) ; dernier paragraphe conservé. Visuel réduit à deux panneaux sans nouveau chiffre ; pastilles réduites à `spending_gap_ea21_2025_pp`, `oecd_tax_to_gdp_2024_rank`, `last_surplus_year`. Retirés du chapitre : 57,3 % / 49,7 %, rang UE, 227 milliards, environ 48 jours, 10,4 points en 2017, 43,5 % / 34,1 %.
10. *Étape 10.* **Appliqué.** Troisième puce : « selon la Cour des comptes, l’OFCE et Fipeco (point d’accord) ». Transition « **→ Chapitre 5 : La dette et ses intérêts** ».
11. *Validation, comptage et durée.* **Appliqué.** Voir en-tête de cette passe. Le point ouvert de longueur (2 331 mots à la passe précédente, autre méthode de comptage) est **clos** : 2 165 mots.

Corrections complémentaires (D-vocabulary) : étape 6, « dépenses +1,7 point de PIB, recettes −1,8 point » → « une hausse des dépenses de 1,7 point de PIB, une baisse des recettes de 1,8 point » ; étape 8, « TVA » développée à la première occurrence (« taxe sur la valeur ajoutée (TVA) »). Tableaux (étapes 6 et 8) : signes conservés, conformément au glossaire §2.2.

Aucun chiffre ajouté ; aucune édition rejetée. Aucun chiffre absent de `platform/data` n’a été nécessaire.

### Passe « audit gauche / droite / chiffres » du 25 octobre 2026 (troisième passage)

Principe suivi quand les lectures « lecteur de gauche » et « lecteur de droite » se contredisaient : montrer les deux bornes (même année d’arrivée, et la variante qui change la conclusion), attribuer chaque thèse à ses auteurs, décrire les deux camps de façon parallèle. Aucun chiffre sans pastille : les fenêtres demandées absentes de `figures.json` sont des `[[calc:]]` construits sur des identifiants existants, recoupés avec `research/data/debates/computed_fr_vs_eu27_fiscal_series.csv` (Eurostat gov_10a_main, 21 octobre 2026) : 2017 → 2025 = −0,4 / −2,1 / −1,7 (57,7 → 57,3 ; 54,3 → 52,2 ; −3,4 → −5,1) ; 2019 → 2024 = +1,7 / −1,8 (55,3 → 57,0 ; 53,0 → 51,2). Validateur (`python3 -I validate.py`) : 0 erreur, 0 avertissement. Texte visible : 2 123 → 2 331 mots (même méthode de comptage que la passe précédente).

**Constats traités**
1. *Fenêtres de fin différente (lecteur de gauche, élevé ; étape 6, étape 0, étape 10, Q37).* **Appliqué en partie.** Option A : les deux lignes du tableau s’arrêtent en 2025 (ligne « 2017 → 2025 » en `[[calc:]]`). Phrase ajoutée sous le tableau sur 2019-2024 (« les deux effets à parts à peu près égales », +1,7 / −1,8, en `[[calc:]]`) et sur la hausse d’impôts de 2025. Puce 2 de l’étape 10 réécrite (trois périodes). Curseur : départ par défaut 2017 → 2025 ; 2017 → 2024 et 2019 → 2024 ajoutés aux tests de non-régression. Non fait ici : explication de Q37 (`quiz.json`, hors de mon périmètre) ; création des identifiants `te_change_2017_2025_pp`, `total_revenue_change_2017_2025_pp`, `balance_change_2017_2025_pp` (`figures.json`, hors périmètre) : à créer par la passe données, puis remplacer les `[[calc:]]` par des `[[fig:]]`.
2. *Baisses d’impôts sur le capital absentes (lecteur de gauche, élevé ; étape 4).* **Appliqué en partie.** Étape 4 : paragraphe ISF-IFI (3 à 4,5 milliards d’euros par an, `[[fig:isf_repeal_mechanical_loss_eur_bn]]`, estimation mécanique du CAE ; la formulation proposée attribuait la fourchette à France Stratégie, corrigé) et PFU (aucun effet détecté sur l’investissement ou les salaires, France Stratégie 2023), avec les deux réserves du fichier 08 l. 117 et l. 86 : résultat jugé fragile par le comité, mesure autofinancée les premières années par la hausse des dividendes. Non fait : figures IPP n° 81 et chapitre 3 (hors périmètre).
3. *Réponse de l’étape 5 hors sujet ; étiquettes asymétriques (lecteur de gauche, moyen).* **Appliqué.** Dernière phrase de « Ce qu’on peut répondre » (étape 5) supprimée. Attributions parallèles : « des instituts de recherche et des associations » (étape 4) / « des institutions publiques et internationales chargées de la surveillance budgétaire » (étape 5), étiquettes d’orientation du glossaire §424 conservées pour les instituts des deux côtés.
4. *Fenêtres 2017-2024 / 2019-2025 et longue période (lecteur de droite, élevé).* **Appliqué en partie.** Ligne 2017 → 2025 dans le tableau ; étape 5 : « −0,4 point de PIB entre 2017 et 2025 », avec « −0,7 point jusqu’en 2024 », fenêtre de l’OFCE ; étape 4 : recettes 2017 → 2025 (−2,1) à côté de 2017 → 2024 (−3,1), et prélèvements obligatoires 2025 (43,6 %). Étape 0 : « surtout la période choisie : l’année de départ, mais aussi l’année d’arrivée ». Ligne 2005 → 2025 **non ajoutée** : aucun identifiant de niveau 2005 n’existe pour construire une pastille ; le fait est donné sans chiffre (« depuis 2005, dépenses et recettes ont toutes deux augmenté en points de PIB, les dépenses nettement plus », `[[src:f10]]`). À ajouter quand `te_change_2005_2025_pp` (+3,0), `total_revenue_change_2005_2025_pp` (+1,4) et `balance_change_2005_2025_pp` (−1,6) existeront. La phrase de l’étape 0 proposée (« sur vingt ans, les dépenses ont augmenté plus que les recettes ») n’est pas reprise en ouverture : placée à l’étape 6, à côté des autres fenêtres, pour ne pas donner la conclusion d’un camp dès l’accroche.
5. *Remède institutionnel absent (lecteur de droite, élevé ; étape 7).* **Appliqué** (partie chapitre 4). Paragraphe « Sur le remède » : position de la Cour des comptes (RSPFP 2026) et du FMI (article IV, 21 mai 2026) en paraphrase, sans guillemets, car le texte français exact de la Cour n’est pas dans la base de recherche (fichier 10 §4.3 le donne en anglais) ; position inverse attribuée aux « économistes du premier récit » et non nommément à l’OFCE, la base ne documentant pas une telle recommandation de l’OFCE ; Terra Nova en position intermédiaire. Chapitre 7 : hors périmètre.
6. *Étiquettes d’orientation asymétriques (lecteur de droite, élevé ; glossaire, ch. 3, 4, 7).* **Rejeté pour le chapitre 4, en attente du glossaire.** Le glossaire §424 est contraignant et fixe « Rexecode (institut financé par des organisations patronales) » et « Institut Montaigne (financé par des entreprises, libéral-centriste) » ; je les garde à l’identique. Si le glossaire change, reporter ici (étapes 5 et 7). Ch. 3 et 7 : hors périmètre.
7. *Fipeco enrôlé dans le premier récit ; pas d’institut ni de concession pour le second (lecteur de droite, moyen).* **Appliqué en partie.** Fipeco retiré de l’attribution de l’étape 4 et de la réponse de l’étape 4 ; il reste au point d’accord de l’étape 7, avec son étiquette (première occurrence). Étape 5 : Institut Montaigne et iFRAP ajoutés ; étape 4 : Attac ajouté (symétrie demandée par la note « option non retenue » du passage précédent). Non repris : le chiffre de 140 milliards d’euros de Montaigne (aucune pastille dans `figures.json`) et la tournure « Même Terra Nova… », qui reproduisait l’effet « même l’autre camp le dit » reproché à Fipeco ; Terra Nova est placé au paragraphe « Sur le remède » (étape 7), en position intermédiaire, comme Fipeco l’est sur la cause.
8. *Encadré « 2017 est un sommet » incomplet (lecteur de droite, moyen).* **Appliqué en partie.** Troisième paragraphe : selon la Cour (RSPFP 2024), le taux de prélèvements obligatoires est resté proche de celui de 2017 jusqu’en 2022 et n’a nettement baissé qu’en 2023, surtout par moindre dynamisme spontané (fichier 08 l. 99 : −1,8 point en 2023, dont −1,6 spontané ; la formulation proposée « les baisses n’apparaissent dans le taux qu’à partir de 2023 » aurait attribué ce recul aux mesures, corrigé). Sans chiffre : `po_2022_pct_gdp` (45,0) n’existe pas dans `figures.json` ; à créer, puis afficher « 45,0 % en 2022 ». Solde net Rexecode depuis 2010 (option) non ajouté : pas de pastille.
9. *Conversions seulement côté recettes (lecteur de droite, moyen ; étape 10).* **Appliqué** (partie chapitre 4). Puce ajoutée : hausse des dépenses 2019-2025, 2,0 points de PIB, environ 60 milliards d’euros, 12,7 jours. Ligne « Part du déficit 2025 » (40,9 %) retirée de la fiche « 62 milliards » : c’était la seule conversion en part du déficit, sans équivalent pour l’autre récit. La mention « économies annoncées non réalisées » est gardée et marquée « point d’accord ». Chapitre 3 : hors périmètre.
10. *Années d’arrivée différentes (chiffres et cohérence, moyen).* **Appliqué** (option A, voir constat 1).
11. *Arrondis transversaux (faible).* **Sans objet pour le chapitre 4** : il affiche déjà 32,3 jours, 1 714,1 milliards et 13,2 jours. Les autres chapitres sont hors périmètre.
12. *Durée de lecture (faible).* **Appliqué** : « environ 8 minutes ». Point ouvert de la passe précédente clos.
13. *Pastilles `[[calc:]]` du chapitre 2 (faible).* **Sans objet** (chapitre 2, hors périmètre). Les nouvelles pastilles `[[calc:]]` du chapitre 4 portent toutes leur résultat.

**Coupes pour tenir la longueur** : étape 8, paragraphe des quatre sous-secteurs (les noms passent dans la fiche) et note de la fiche raccourcie ; étape 4, fiche « 62 milliards » réduite aux jours (euros par habitant et ménage retirés, toujours dans le vérificateur de promesses) ; étape 6, note du tableau ; étape 7, renvoi au simulateur ; « Pour aller plus loin » raccourci (la « règle d’or » des collectivités reste dans la fiche *Déficit et dette*). **Point ouvert** : 2 331 mots, au-dessus de la cible d’environ 2 200 ; les ajouts demandés par l’audit (environ 330 mots) l’expliquent. Coupes possibles si nécessaire : encart « Si la France était un ménage » (étape 2) ou rangs européens et OCDE (étape 9, à couper ensemble).

**À transmettre** : passe données (`figures.json`) : `te_change_2017_2025_pp`, `total_revenue_change_2017_2025_pp`, `balance_change_2017_2025_pp`, `te_change_2019_2024_pp`, `total_revenue_change_2019_2024_pp`, `te_change_2005_2025_pp`, `total_revenue_change_2005_2025_pp`, `balance_change_2005_2025_pp`, `po_2022_pct_gdp` ; quiz Q37 (nuance 2019-2024) ; glossaire §424 (constat 6).

### Passe « pastilles et longueur » du 25 octobre 2026 (deuxième passage)

Mesure du texte visible (script de comptage : hors commentaires HTML, visuels, pastilles, blocs « Pastilles source », spécifications d’interaction et de boutons, notes de relecture ; titres, fiches chiffre, encadrés et « Pour aller plus loin » inclus) : **2 638 mots avant, 2 109 mots après**.

**Pastilles provisoires remplacées (34 occurrences, 14 identifiants)**
- `[[fig-a-creer:…]]` → `[[fig:…]]` pour : `te_change_2017_2024_pp` (−0,7), `balance_change_2017_2024_pp` (−2,4), `te_change_2019_2025_pp` (+2,0), `total_revenue_change_2019_2025_pp` (−0,8), `balance_change_2019_2025_pp` (−2,7), `tax_hikes_2010_2014_pts` (3,8), `rexecode_levies_2024_2026_eur_bn` (36,7), `rexecode_levies_2024_2026_pts` (1,2), `cour_2025_tax_increases_eur_bn` (23,0), `deficit_state_2025_eur_bn` (128,1), `deficit_odac_2025_eur_bn` (2,2), `deficit_apul_2025_eur_bn` (15,6), `deficit_asso_2025_eur_bn` (5,8). Valeurs identiques à celles du premier jet.
- Conversions jusque-là non sourcées, désormais rattachées à un étalon ou à un `[[calc:]]` : 12,7 jours → `[[yard:te_change_2019_2025_days]]` (étapes 1 et 5) ; 7,8 jours → `[[yard:rexecode_levies_2024_2026_days]]` ; part de l’État → `[[yard:deficit_state_share_pct]]` (84,5 %, et non plus « environ 85 % ») ; 59,8 Md€, 119 €/mois, 48,3 jours, jours et parts des sous-secteurs → `[[calc:…]]` ; 3 000 € → `[[yard:household_monthly_income_eur]]` (paramètre, choix éditorial).
- Aucun bloc d’attente de données dans ce chapitre. Aucune valeur déclarée invérifiable par la passe données ne concerne le chapitre 4.

**Vérification des valeurs affichées** (script comparant chaque nombre du texte à la valeur de la pastille, format français)
- Correction : « 1 714 milliards » → « 1 714,1 milliards » (`te_2025_eur_bn` = 1 714,1) ; « 23 milliards » → « 23,0 milliards » (forme du fichier et du PDF de la Cour).
- Arrondis assumés, signalés par « environ » : « 1 euro sur 11 » (11,3), « environ 60 milliards » (59,8), « environ 48 jours » (48,3).
- `rexecode_levies_*` ont le statut `caveat` dans figures.json : l’étiquette d’orientation (institut financé par des organisations patronales) reste au contact du chiffre.

**Coupes (contenu déplacé ou retiré du texte visible)**
- Étape 2 : déficit par habitant (2 200 €) retiré (redondant avec la fiche « 62 milliards » et le vérificateur de promesses).
- Étape 4 : ISF-IFI et PFU (non chiffrés à part par la Cour) → « Pour aller plus loin » (fiche *Les baisses d’impôts depuis 2017*, fichier 20 §4.11). Paragraphe OCDE de l’encadré retiré : il répétait l’étape 9 ; le contre-argument garde ses deux arguments les plus forts (2017 = sommet après les hausses de 2010-2014 ; CICE). La source FMI disparaît donc de l’encadré.
- Étape 6 : reformulation des deux questions supprimée (redite du titre en gras).
- Étape 7 : intérêts 2025-2026 et déficit 2026 prévus retirés (traités au chapitre 5, qui suit) ; les pastilles `interest_2026f_eur_bn` et `deficit_2026f_pct_gdp` ne figurent plus dans ce chapitre.
- Étape 8 : énumération des APUL et ASSO raccourcie ; « règle d’or » des collectivités → « Pour aller plus loin » (fiche *Déficit et dette*, §4.8) ; la phrase-clé (« un petit déficit ne signifie pas une gestion plus économe ») est conservée.
- Étape 9 : écart de 2005 (7,1 points de PIB) retiré du texte, conservé dans la mini-courbe du visuel ; encadré 43,5 % / 42,7 % → « Pour aller plus loin » (page *Méthode*, §4.17).
- Visuels et spécifications d’interaction resserrés (même contenu).
- Ajout d’une liste « Pour aller plus loin » (quatre fiches thématiques, sans chiffre).

**Symétrie après coupes** : chaque récit garde son exposé, sa fiche chiffre en jours (13,2 / 12,7), son encadré « Le meilleur contre-argument » et sa réponse ; l’étape 7 garde le point d’accord et la contrepartie depuis 2024 (Rexecode, Cour 2025).

**Points ouverts**
- Durée de lecture : « environ 2 minutes » reste affichée ; 2 109 mots représentent plutôt 8 à 10 minutes. Décision transversale (même remarque au chapitre 2), à trancher avec le plan du fichier 20 (environ 12 minutes pour les sept chapitres).
- « Pour aller plus loin » : les intitulés renvoient aux fiches du fichier 20 §4 ; les URL restent à poser quand les fiches existeront.
- Option non retenue : citer aussi l’Institut Montaigne et l’iFRAP (second récit) ou Attac (premier récit), présents au fichier 10 §4.1. Si l’un est ajouté, ajouter l’autre côté.

### Premier passage du 25 octobre 2026 (archive ; certaines étapes citées ont été raccourcies depuis)

Relecture du 25 octobre 2026 (chiffres, neutralité, français). Tous les nombres ont été recoupés avec `platform/data/figures.json`, `yardsticks.json` et `proposals.json` (valeur, unité, % du PIB ou % des dépenses, année). Les calculs dérivés ont été refaits : 4,696 Md€ par jour ; 32,28 jours ; 1 euro sur 11,3 ; 29 novembre (jour 332,7) ; 3 291 et 291 € ; 2 197 € par habitant ; 13,20 jours, 40,9 %, 899 € et 119 € pour les 62 Md€ ; 2,0 × 29,9 = 59,8 Md€ = 12,7 jours ; 36,7 Md€ = 7,8 jours et 1,23 point de PIB ; sous-secteurs 27,3 / 3,3 / 1,2 / 0,5 jours et 84,5 / 10,3 / 3,8 / 1,5 % (somme 151,7 Md€) ; 7,6 × 29,9 = 227 Md€ = 48,3 jours ; soldes du tableau de l’étape 6 (−3,1 − (−0,7) = −2,4 ; −0,8 − 2,0 = −2,8, publié −2,7, écart d’arrondi signalé). Les valeurs des pastilles `fig-a-creer` ont été vérifiées dans les fichiers de recherche (10 §4.2, 06 tableau clé ligne 4, 08 §3.2) ; elles restent BLOQUANTES tant que les entrées de `figures.json` n’existent pas.

**Chiffres**
- Étapes 2 et 10 : « 32 jours » → « 32,3 jours » (arrondi de `deficit_days`, même arrondi que le chapitre 1). Étape 2, visuel : la bande compte 32 cases entières (30 novembre-31 décembre) plus trois dixièmes de la case du 29 novembre.
- Étapes 1 et 10 : « environ 13 jours » / « 13 jours » → « 13,2 jours » (même arrondi que la fiche chiffre et `prop:tax_cuts_2018_2023`).
- Étape 1 : précision « en 2023 » (le coût de 62 Md€ est valorisé en 2023) et pastille de conversion ajoutée.
- Étape 4 : liste des mesures corrigée. La Cour des comptes (RSPFP 2024) cite l’impôt sur les sociétés, la CVAE, la taxe d’habitation et les cotisations sociales ; elle ne chiffre pas à part l’ISF-IFI ni le PFU (correction déjà notée au fichier 01). Les cotisations sociales, absentes de la liste, y figurent désormais.
- Étape 4, encadré : date et nature de la source FMI ajoutées (déclaration de fin de mission, 21 mai 2026) ; date de l’édition OCDE ajoutée ; « 36 pays de l’OCDE » conforme à `rank_of`.
- Étape 5, fiche chiffre : la phrase « ordre de grandeur proche des 62 milliards […] c’est pourquoi le débat est si serré » rapprochait une variation de ratio (qui dépend aussi du PIB) et un coût de mesures décidées. Remplacée par une mise en garde.
- Étape 7 : « environ 8 jours » → « environ 7,8 jours » (cohérent avec le visuel) et pastille `one_day_spending_eur_bn` ajoutée ; intérêts 2026 et déficit 2026 marqués comme prévisions (« atteindrait »).
- Étape 9 : « 7,1 points » et « 10,4 points » → « points de PIB » ; « 48 jours » → « environ 48 jours » (48,3) ; explication de l’écart 43,5 % / 42,7 % précisée d’après le fichier 18 (crédits d’impôt remboursables), pastille `src:f18` ajoutée.
- Citation de la Cour sur 2025 (« exclusivement ») vérifiée dans les fichiers 06 et 08 (texte primaire). Citation « non compensées par des économies en dépenses » vérifiée (fichiers 01 et 08).

**Neutralité**
- Étape 0 : « Le premier accuse… le second accuse… » → formulation descriptive (« Pour le premier, il vient surtout de… »).
- Étape 1 : la seule question notée portait sur le coût des baisses d’impôts, ce qui pouvait orienter le lecteur vers le premier récit. Ajout, dans la réponse, de l’ordre de grandeur symétrique de la hausse des dépenses depuis 2019 (12,7 jours), avec renvoi aux étapes 4 et 5.
- Étape 2 : l’image « à partir du 29 novembre, tout est payé à crédit » est présentée comme une image (l’emprunt finance une part des dépenses toute l’année). Limites du ménage rendues symétriques (l’État paie aussi des intérêts).
- Étape 4 : Fipeco (orthodoxie budgétaire) ajouté aux défenseurs du premier récit pour 2017-2022 (fichier 10 §4.1), avec son étiquette d’orientation dès la première occurrence. La liste de mesures ne met plus en avant l’ISF et le PFU, que la Cour ne chiffre pas à part.
- Étape 4, « Le meilleur contre-argument » : ajout de l’argument du CICE (une partie de la baisse des recettes est un changement d’écriture comptable, fichiers 01 et 09). C’est l’objection la plus forte au point de départ 2017 ; elle manquait. « Ce qu’on peut répondre » en donne la limite (les prélèvements obligatoires au sens de l’Insee, nets des crédits d’impôt, baissent aussi de 2,6 points de PIB).
- Étape 5 : ajout que la Cour des comptes chiffre aussi le coût des baisses d’impôts, pour ne pas présenter les institutions publiques comme un seul camp. « Leur niveau d’avant » précisé « rapportées au PIB ».
- Étape 5, « Ce qu’on peut répondre » : l’argument du CICE précise désormais, d’après l’OFCE lui-même (fichier 08), qu’une fois cet effet corrigé la baisse des dépenses devient faible ; aucun chiffre nouveau.
- Étape 7 : titre « Ce sur quoi tout le monde s’accorde » → « Un point d’accord » (règle P10 : pas de « tout le monde s’accorde ») ; « les deux camps » → « les deux lectures ».
- Étape 8 : la « règle d’or » des collectivités est attribuée à leurs associations d’élus, comme dans le fichier 08.
- Étape 9 : ajout de la raison principale de la baisse de l’écart depuis 2017 (hausse de la dépense ailleurs dans la zone euro, fichier 09), pour ne pas la présenter comme un effort français ; « que ses voisins » → « que la moyenne de ses voisins ».
- Étape 10 : la puce sur les baisses d’impôts nomme les deux faces du constat (économies annoncées non réalisées) ; ajout d’une puce symétrique sur la période depuis 2024 (prélèvements en hausse, dépenses plus rapides que l’économie). « De plus en plus chers » → « dont la charge augmente ».

**Français**
- « Sans ces intérêts, le déficit aurait été de » → « Hors intérêts, le déficit est de » (le conditionnel suggérait un scénario).
- « L’année de départ décide de la moitié de l’histoire que l’on voit » → « Selon l’année de départ choisie, on ne voit que la moitié de l’histoire ».
- Note du tableau de l’étape 6 reformulée (« une variation négative du solde » ; écart d’arrondi expliqué).
- « Sécurité sociale » → « administrations de sécurité sociale » pour les ASSO (glossaire : les ASSO sont plus larges que la Sécurité sociale) ; ISF et CVAE développés à la première occurrence ; titre complet du Policy Brief n° 146 de l’OFCE.
- « depuis la crise du Covid » → « depuis la veille de la crise du Covid » (le point de départ est 2019).
- Libellé du curseur harmonisé avec la question 2 (« les deux, à parts à peu près égales »).
- Typographie vérifiée : apostrophes typographiques, guillemets « », virgule décimale, signe moins dans les tableaux, « milliards » en toutes lettres dans le texte et « Md€ » dans les fiches ; les espaces insécables sont posées par le filtre du site (glossaire §2.1).
