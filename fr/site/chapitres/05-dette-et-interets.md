---
chapitre: 5
titre: « La dette et ses intérêts »
parcours: Le récit (chapitre 5 sur 7)
duree_lecture: environ 9 minutes
niveau: B1 (encadrés et notes de méthode : B2)
donnees: platform/data/figures.json et yardsticks.json, version du 25 octobre 2026 (second passage de données)
statut: brouillon pour relecture éditoriale (25 octobre 2026, passe de finalisation)
---

# Chapitre 5. La dette et ses intérêts

**Conventions de ce script**

- Les blocs cités (« Texte affiché », encadrés, « Ce qu’on peut répondre », note de méthode, « Pour aller plus loin ») sont le seul texte public. Le reste (visuel, interaction, pastilles, notes) est destiné à l’équipe.
- `[[fig:id]]` = pastille source d’un chiffre de `figures.json` (ou d’un tableau de `rating_tables`). `[[yard:id]]` = étalon de `yardsticks.json` (la pastille affiche la formule et les chiffres d’origine). `[[calc:…]]` = conversion faite avec les formules de `yardsticks.json` (`conversions`), affichée avec la mention « illustratif ».
- Les montants de 2026 et 2027 convertis en jours ou en euros par mois utilisent les dénominateurs de 2025 : ordres de grandeur, et la pastille le dit.
- Mentions de certitude : glossaire, §4.5.

---

## Étape 1. Ouverture : estimez d’abord

**Texte affiché**

> **Combien la France doit-elle ?**
>
> Avant de lire la suite, faites une estimation. Selon vous, que représentait la dette publique française fin 2025, en % du produit intérieur brut (PIB), la richesse produite en un an ?
>
> Durée de lecture : environ 9 minutes.

<!-- estimez-réponse: debt_2025_pct_gdp -->
**Estimez d’abord** : curseur de 0 à 200 % du PIB (pas de 5), sans valeur présélectionnée ; « Voir la réponse » s’active après un déplacement. Ensuite, trois repères sur la même jauge : votre estimation, la médiane des visiteurs (n affiché), la valeur mesurée **115,7 % du PIB** [[fig:debt_2025_pct_gdp]]. Retour neutre, en points de PIB (« Vous étiez proche » à moins de 10 points, sinon « sous-estimée » / « surestimée »).

**Visuel** : jauge horizontale « en % du PIB », trait à 100 % (« une année entière de richesse produite »).

---

## Étape 2. Le stock : 3 460 milliards d’euros

**Texte affiché**

> Fin 2025, la dette publique s’élevait à **3 460,1 milliards d’euros** [[fig:debt_2025_eur_bn]], soit **115,7 % du PIB** [[fig:debt_2025_pct_gdp]]. Cela fait **50 065 € par habitant** [[yard:debt_per_capita_eur]], ou **2,2 années** de recettes publiques (tous les impôts, cotisations et autres ressources publiques) [[yard:debt_to_revenue_years]].
>
> Ne confondez pas deux mots. Le **déficit** est ce qui manque chaque année. La **dette** est ce qui reste dû : en gros, l’accumulation des déficits passés, diminuée des rares excédents.

**Visuel** : 69 millions de silhouettes qui se réduisent à une personne étiquetée « 50 065 € » ; puis une baignoire (la dette) remplie par un robinet (le déficit annuel).

**Pastilles source** : [[fig:debt_2025_eur_bn]] [[fig:debt_2025_pct_gdp]] [[yard:debt_per_capita_eur]] (dénominateur : [[fig:population_2026_01_01_m]]) [[yard:debt_to_revenue_years]] (dénominateur : [[fig:total_revenue_2025_eur_bn]])

---

## Étape 3. Comment elle se remplit : le déficit de 2025

**Texte affiché**

> Chaque année, le déficit remplit la baignoire : 151,6 milliards d’euros en 2025, soit 5,1 % du PIB [[fig:deficit_2025_eur_bn]] [[fig:deficit_2025_pct_gdp]] (chapitre 4). Le dernier excédent des administrations publiques remonte à 1974 [[fig:last_surplus_year]].

**Visuel** : la baignoire de l’étape 2, robinet ouvert (pas de ruban calendrier : le bloc « 32,3 jours » appartient au chapitre 1). Compteur discret : « … € dépensés de plus que reçus pendant votre lecture (moyenne de 2025) », sur la base d’**environ 4 800 € par seconde** [[yard:deficit_per_second_eur]], mention « illustratif ».

**Pastilles source** : [[fig:deficit_2025_eur_bn]] [[fig:deficit_2025_pct_gdp]] [[yard:deficit_per_second_eur]] (visuel seulement, « illustratif ») [[fig:last_surplus_year]]

---

## Étape 4. La trajectoire : la dette continue de monter

**Texte affiché**

> Fin juin 2026, la dette atteignait **3 595,5 milliards d’euros**, soit **119,0 % du PIB** [[fig:debt_2026q2_eur_bn]] [[fig:debt_2026q2_pct_gdp]]. Selon la prévision du gouvernement, elle serait de **119,3 % du PIB** fin 2026 et de **121,7 % du PIB** fin 2027 [[fig:debt_2026f_pct_gdp]] [[fig:debt_2027f_pct_gdp]].
>
> Le Haut Conseil des finances publiques (HCFP) estime que la prévision de croissance du gouvernement pour 2027 « apparaît comme optimiste ». Si la croissance est plus faible, la dette sera plus élevée que prévu. Le FMI (Fonds monétaire international ; organisation internationale) prévoit lui aussi une dette encore en hausse en 2028 [[src:f06:imf_aiv2026]].
>
> Le gouvernement vise un déficit de **5,0 % du PIB** en 2027 [[fig:deficit_2027f_pct_gdp]]. Même atteint, ce déficit ne stabiliserait pas la dette (étape 11).

**Visuel** : courbe « en % du PIB », 1978-2025 en trait plein, 2026-2027 en pointillé « prévu » ; annotations sans chiffre : 2008-2009, 2020, 2022. Données : `research/data/insee_dette_maastricht_1978_2025_by_subsector.csv`.

**Pastilles source** : [[fig:debt_2026q2_eur_bn]] [[fig:debt_2026q2_pct_gdp]] [[fig:debt_2026f_pct_gdp]] [[fig:debt_2027f_pct_gdp]] [[fig:deficit_2027f_pct_gdp]] ; avis du HCFP sans chiffre : pastille texte « HCFP, avis n° HCFP-2026-5 relatif aux PLF et PLFSS pour 2027, 25 septembre 2026, synthèse » (https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf), même URL que [[fig:debt_2027f_pct_gdp]] ; prévision du FMI sans chiffre affiché : [[src:f06:imf_aiv2026]] (communiqué de presse 26/255 du 22 juillet 2026 : dette de 121,1 % du PIB en 2028 ; https://www.imf.org/en/news/articles/2026/07/22/pr26255-france-imf-executive-board-concludes-2026-article-iv-consultation). Afficher 121,1 % seulement après création d’une fiche dans `figures.json`.

---

## Étape 5. Comparaison européenne

**Texte affiché**

> Une dette élevée n’est pas propre à la France, mais l’écart s’est creusé. On parle de taux d’endettement : la dette en % du PIB.
>
> En 2005, la France était **2,0 points de PIB en dessous** de la zone euro à 21 pays (ZE21, Bulgarie comprise) [[fig:debt_gap_ea21_2005_pp]]. En 2025, il était **28,4 points au-dessus** [[fig:debt_gap_ea21_2025_pp]] : **115,7 % du PIB**, contre **87,3 % du PIB** pour la ZE21 [[fig:ea21_debt_2025_pct_gdp]].
>
> Dans l’Union européenne, la France avait en 2025 le **3e** taux d’endettement le plus élevé **sur 27**, après la Grèce et l’Italie [[fig:debt_eu_rank_2025]]. Son déficit public a dépassé celui de l’ensemble de la zone euro chaque année de 2007 à 2025.
>
> Depuis 2019, la plupart des pays touchés par la crise de la zone euro de 2010 à 2012 ont stabilisé ou réduit leur taux d’endettement. Il s’agit de la Grèce, du Portugal, de l’Irlande et, dans une moindre mesure, de l’Italie et de l’Espagne.
>
> Ces pays ont dégagé des excédents primaires, c’est-à-dire un solde positif hors intérêts. Entre 2019 et 2025, seules la Roumanie et la Finlande ont vu leur taux d’endettement augmenter davantage que celui de la France.
>
> *Groupes de comparaison : ZE21, calcul de la plateforme d’après Eurostat, 2005 et 2025 ; Union européenne, Eurostat, 2025. Déficits de 2007 à 2025 et évolutions de 2019 à 2025 : même calcul, même résultat avec ou sans la Bulgarie.*

**Visuel** : courbes France et ZE21, 2005-2025, axe « en % du PIB », zone d’écart colorée (« −2,0 pts » en 2005, « +28,4 pts » en 2025). Bouton vers le comparateur de pays (dette, % du PIB, 2025). Données : `research/data/derived_06_france_vs_ea_deficit_primary_debt_1995_2025.csv`.

**Pastilles source** : [[fig:debt_gap_ea21_2005_pp]] [[fig:debt_gap_ea21_2025_pp]] [[fig:ea21_debt_2025_pct_gdp]] [[fig:debt_2025_pct_gdp]] [[fig:debt_eu_rank_2025]]. Les deux phrases ajoutées le 25 octobre 2026 (déficit 2007-2025, évolution 2019-2025) n’affichent aucun chiffre ; pastille texte « Eurostat `gov_10dd_edpt1`, calcul de la plateforme (fichier 06, §0 et §4.2) » (https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10dd_edpt1). Afficher les valeurs (+17,5 points, 3e rang, 19 années sur 19, écart moyen) seulement après création des fiches listées dans les notes pour l’équipe.

---

## Étape 6. Si la France était un ménage

**Texte affiché**

> Imaginons un ménage qui gagne **3 000 € par mois** [[yard:household_monthly_income_eur]]. Nous avons ramené les comptes publics de 2025 à cette taille : ses revenus correspondent aux recettes publiques [[yard:household_scale_eur_per_month_per_bn|contexte]].
>
> - Il dépense **3 291 €** par mois [[yard:household_spending_month_eur]].
> - Il emprunte donc **291 €** chaque mois [[yard:household_borrowing_month_eur]].
> - Il doit **79 700 €** au total [[yard:household_debt_eur]].
> - Il paie **126 €** d’intérêts par mois [[yard:household_interest_month_eur]].
>
> *Autre périmètre, à ne pas comparer directement : défense, budget de l’État (loi de programmation militaire) : **98 €** par mois [[yard:household_defense_month_eur]]. Pour une comparaison sur le même périmètre, voir l’étape 8.*

**Visuel** : relevé de compte stylisé, lignes ajoutées une à une, mention « illustratif ». La ligne défense est placée **sous le relevé**, dans un cadre séparé, sans barre ni alignement avec la ligne « intérêts » (même règle qu’à l’étape 8 : deux périmètres jamais comparés visuellement). Note : « Défense : loi de programmation militaire, budget de l’État (comptabilité budgétaire). Intérêts : toutes administrations publiques (comptabilité nationale). Périmètres différents. »

**Encadré « Les limites de l’image »** (obligatoire, même écran ; ce n’est pas un encadré « Le meilleur contre-argument », qui reste à l’étape 12)

> **Les limites de l’image**
>
> - Un État ne part pas à la retraite. Il n’a pas besoin de rembourser toute sa dette : il la renouvelle en empruntant de nouveau.
> - Ce renouvellement est lent : en moyenne, la dette négociable de l’État arrive à échéance en **8,4 ans** (30 septembre 2026) [[fig:avg_maturity_state_debt_2026_years]]. Une hausse des taux ne pèse donc que peu à peu sur les intérêts (étape 10).
> - Ses recettes augmentent avec la taille de l’économie. Le taux d’endettement peut rester stable malgré un déficit chaque année, si l’économie croît assez vite (étape 11).
> - L’État possède aussi des biens : bâtiments, routes, réseaux, participations dans des entreprises. Une partie de la dette les a financés. En 2025, les administrations publiques ont investi **4,4 % du PIB** [[fig:public_gfcf_2025_pct_gdp]] (investissement brut, avant usure des équipements).
> - Si l’on retire les actifs financiers les plus liquides des administrations publiques, la dette nette atteint **108,5 % du PIB** fin 2025 [[fig:net_debt_2025_pct_gdp]].
>
> *Sources :* Cour des comptes (juridiction financière), *La situation et les perspectives des finances publiques*, 25 juin 2026 ; Insee (Institut national de la statistique et des études économiques), comptes de patrimoine et comptes des administrations publiques, 29 mai 2026 ; Eurostat, comptes des administrations publiques, 21 octobre 2026 ; Agence France Trésor, *Encours de la dette négociable au 30 septembre 2026*.

**Où l’image tient** (sous l’encadré)

> Sur un point, l’image tient : les intérêts doivent être payés quoi qu’il arrive, et leur prix dépend des prêteurs (étape 10).

**Pastilles source** : [[yard:household_monthly_income_eur]] [[yard:household_scale_eur_per_month_per_bn]] (dénominateur : [[fig:total_revenue_2025_eur_bn]]) [[yard:household_spending_month_eur]] [[yard:household_borrowing_month_eur]] [[yard:household_debt_eur]] [[yard:household_interest_month_eur]] [[yard:household_defense_month_eur]] (montant : [[fig:lpm_2025_eur_bn]]) ; encadré : [[fig:public_gfcf_2025_pct_gdp]] (Eurostat `gov_10a_main`, investissement brut ; comparateur ZE20 de 3,7 % sans fiche, non affiché) [[fig:net_debt_2025_pct_gdp]] (Insee, 29 mai 2026) [[fig:avg_maturity_state_debt_2026_years]] (AFT, 1er octobre 2026 ; « 8 ans et 158 jours »)

---

## Étape 7. Les intérêts : estimez d’abord

**Texte affiché (avant la réponse)**

> **Selon vous, combien de jours de dépense publique faut-il, chaque année, pour payer les intérêts de la dette ?**

**Estimez d’abord** : curseur de 0 à 60 jours, sans valeur présélectionnée. Réponse : **14 jours** [[calc:interest_2025_eur_bn / yard:one_day_spending_eur_bn = 14,0]], affichée sur le ruban calendrier (bloc de 14 cases « intérêts »).

**Texte affiché (après la réponse)**

> En 2025, les administrations publiques ont payé **65,7 milliards d’euros** d’intérêts [[fig:interest_2025_eur_bn]] : **2,2 % du PIB** [[fig:interest_2025_pct_gdp]], ou **3,8 % des dépenses publiques** [[fig:interest_2025_pct_te]].
>
> Cela fait **14 jours** de dépense publique [[calc:interest_2025_eur_bn / yard:one_day_spending_eur_bn = 14,0]], environ **952 € par habitant** [[calc:interest_2025_eur_bn × 1000 / population_2025_m = 952]] et l’équivalent de **43 %** du déficit de 2025 [[calc:interest_2025_eur_bn / deficit_2025_eur_bn = 43 %]].

**Note de méthode (repliable, B2)**

> Vous verrez aussi **51,6 milliards d’euros** : c’est la charge de la dette de l’État seul, en comptabilité budgétaire [[fig:state_debt_charge_2025_eur_bn]]. Elle exclut la Sécurité sociale et les collectivités locales (écart : **14,1 milliards d’euros** [[yard:interest_concepts_gap_2025_eur_bn]]). Sur ce site, « intérêts » désigne la charge d’intérêts de toutes les administrations publiques, sauf mention contraire.

**Pastilles source** : [[fig:interest_2025_eur_bn]] [[fig:interest_2025_pct_gdp]] [[fig:interest_2025_pct_te]] [[yard:one_day_spending_eur_bn]] [[fig:population_2025_m]] [[fig:deficit_2025_eur_bn]] [[fig:state_debt_charge_2025_eur_bn]] [[yard:interest_concepts_gap_2025_eur_bn]]

---

## Étape 8. Intérêts, éducation, défense

**Texte affiché**

> **En % du PIB**, les intérêts (**2,2 %** en 2025) [[fig:interest_2025_pct_gdp]] dépassent la défense (**1,8 %** en 2024) [[fig:cofog_defense_2024_pct_gdp]], mais restent inférieurs à l’éducation (**5,1 %** en 2024) [[fig:cofog_education_2024_pct_gdp]]. En montant, ils représentent **44 %** des dépenses d’éducation [[yard:interest_vs_education_pct]].
>
> Dans le seul budget de l’État, la charge de la dette est prévue à **72,9 milliards d’euros** en 2027 [[fig:state_debt_charge_2027_eur_bn]]. Les crédits de la loi de programmation militaire sont prévus à **63 milliards** [[fig:lpm_2027_eur_bn]].

**Visuel** : deux panneaux séparés et titrés par périmètre, jamais comparés visuellement entre eux.
- **A : toutes administrations publiques, comptabilité nationale, en % du PIB** : intérêts 2025 (2,2), défense 2024 (1,8), éducation 2024 (5,1), étiquette d’année sur chaque barre. Bascule « % des dépenses publiques » : 3,8 [[fig:interest_2025_pct_te]], 3,2 [[fig:cofog_defense_2024_pct_te]], 8,9 [[fig:cofog_education_2024_pct_te]].
- **B : budget de l’État, comptabilité budgétaire, Md€, prévision 2027** : 72,9 et 63 ; différence 9,9 [[yard:state_interest_minus_lpm_2027_eur_bn]].

**Pastilles source** : [[fig:interest_2025_pct_gdp]] [[fig:cofog_defense_2024_pct_gdp]] [[fig:cofog_education_2024_pct_gdp]] [[yard:interest_vs_education_pct]] (montants : [[fig:interest_2025_eur_bn]] [[fig:cofog_education_2024_eur_bn]]) [[fig:state_debt_charge_2027_eur_bn]] [[fig:lpm_2027_eur_bn]]

---

## Étape 9. Une charge qui augmente vite

**Texte affiché**

> Selon la prévision du gouvernement, les intérêts passeraient de **65,7 milliards d’euros** en 2025 [[fig:interest_2025_eur_bn]] à **79,2 milliards** en 2026 [[fig:interest_2026f_eur_bn]]. Ils atteindraient **environ 91 milliards** en 2027 [[fig:interest_2027f_eur_bn]]. C’est **25,3 milliards d’euros** de plus en deux ans [[yard:interest_rise_2025_2027_eur_bn]], **5,4 jours** de dépense publique [[calc:interest_rise_2025_2027_eur_bn / yard:one_day_spending_eur_bn = 5,4]]. Pour notre ménage, de **126 €** à environ **175 €** par mois [[calc:interest_2027f_eur_bn × yard:household_scale_eur_per_month_per_bn = 175]].
>
> Cette hausse sert d’étalon pour juger les promesses de tous les camps : le chapitre 7 les passe toutes à la même règle.

**Visuel** : barres 2025, 2026 (prév.), 2027 (prév.) en Md€ ; la hausse (25,3) devient une barre étalon (les promesses sont comparées à cet étalon au chapitre 7, pas ici). Mention : « 2026 et 2027 : prévisions du gouvernement (PLF 2027). Conversions avec les dénominateurs de 2025 : ordre de grandeur. »

**Pastilles source** : [[fig:interest_2025_eur_bn]] [[fig:interest_2026f_eur_bn]] [[fig:interest_2027f_eur_bn]] [[yard:interest_rise_2025_2027_eur_bn]] [[yard:one_day_spending_eur_bn]] [[yard:household_scale_eur_per_month_per_bn]] [[yard:household_interest_month_eur]]

---

## Étape 10. Les marchés : taux, écart avec l’Allemagne, notation

**Texte affiché**

> En septembre 2026, l’État empruntait à 10 ans à **4,44 %** en moyenne [[fig:oat10y_sep2026_pct]]. L’écart avec l’Allemagne, l’emprunteur jugé le plus sûr de la zone euro, s’appelle l’**écart de taux** (*spread*). Il était de **97 points de base** ce mois-là, soit 0,97 point de pourcentage [[fig:oat_bund_spread_sep2026_bp]].
>
> Le 22 octobre 2026, le taux à 10 ans a clôturé à **5,13 %** [[fig:oat10y_22oct2026_pct]]. Ce jour-là, l’écart a atteint ponctuellement environ **169 points de base** [[fig:oat_bund_spread_22oct2026_bp]], contre **97 points** en moyenne en septembre [[fig:oat_bund_spread_sep2026_bp]]. C’est une valeur d’un jour, calculée de façon approximative par la plateforme à partir de deux séries.
>
> En moyenne mensuelle, le maximum depuis 1993 reste celui de novembre 2011 : **154 points de base** [[fig:oat_bund_spread_peak_nov2011_bp]]. En septembre 2026, à la même échéance, la France empruntait un peu plus cher que l’Italie et plus cher que l’Espagne (moyennes mensuelles, Eurostat).
>
> Une hausse des taux touche d’abord les nouveaux emprunts, dont ceux qui remplacent la dette arrivée à échéance. Selon le gouvernement, 1 point de plus sur tous les taux coûterait **3,4 milliards d’euros** la première année [[fig:interest_shock_100bp_y1_eur_bn]] et **8,1 milliards** la deuxième [[fig:interest_shock_100bp_y2_eur_bn]].
>
> Les agences de notation évaluent le risque qu’un emprunteur ne rembourse pas. En 2025, Fitch (12 septembre) et S&P (17 octobre) ont abaissé la note de la France d’un cran, de AA- à A+ [[fig:credit_ratings_oct2026]]. Le 24 octobre 2025, Moody’s a placé sa note sous perspective négative (l’agence envisage de l’abaisser) [[fig:credit_ratings_oct2026]].
>
> En octobre 2026, la France est notée **Aa3** par Moody’s, perspective négative, et **A+** par S&P et par Fitch, perspective stable [[fig:credit_ratings_oct2026]]. C’est **3 niveaux** sous la meilleure note chez Moody’s [[fig:rating_moodys_oct2026_notches]] et **4 niveaux** chez S&P [[fig:rating_sp_oct2026_notches]] et Fitch [[fig:rating_fitch_oct2026_notches]].

**Visuel**
- Courbe mensuelle de l’écart OAT-Bund (Eurostat, 1993 à septembre 2026), axe « en points de base », ligne pointillée à 154 ; le 22 octobre 2026 (169) en **losange distinct**, légende « valeur d’un jour (clôture), pas une moyenne mensuelle : comparaison indicative ». Le losange porte une barre d’incertitude seulement quand la marge (fichier 06, §3.4 : environ 5 points de base entre séries) aura une fiche dans `figures.json`. Données : `research/data/eurostat_irt_lt_mcby_m_10y_yields_monthly.csv`.
- Mini-curseur « +0 à +2 points sur tous les taux », coût proportionnel aux deux valeurs du gouvernement, mention « approximation linéaire, illustratif ».
- Échelle de notation verticale (AAA/Aaa en haut, 0 cran) : un repère par agence (lettre, perspective, date de la dernière décision), alimenté par `credit_ratings_oct2026` ; la valeur numérique (crans) sert seulement à placer le repère.

**Pastilles source** : [[fig:oat10y_sep2026_pct]] [[fig:oat_bund_spread_sep2026_bp]] [[fig:oat10y_22oct2026_pct]] [[fig:oat_bund_spread_22oct2026_bp]] [[fig:oat_bund_spread_peak_nov2011_bp]] [[fig:interest_shock_100bp_y1_eur_bn]] [[fig:interest_shock_100bp_y2_eur_bn]] [[fig:credit_ratings_oct2026]] [[fig:rating_moodys_oct2026_notches]] [[fig:rating_sp_oct2026_notches]] [[fig:rating_fitch_oct2026_notches]] ; comparaison avec l’Italie et l’Espagne (sans chiffre) : pastille texte « Eurostat `irt_lt_mcby_m`, septembre 2026 » (https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/irt_lt_mcby_m).

---

## Étape 11. L’effet boule de neige et l’effort pour stabiliser la dette

**Texte affiché**

> Le poids de la dette (en % du PIB) dépend de trois choses. La première est le taux d’intérêt moyen payé sur la dette (« r »). La deuxième est la croissance de l’économie, inflation comprise (« g »). La troisième est le solde primaire, c’est-à-dire le solde public hors intérêts.
>
> Si r dépasse g, la dette grossit d’elle-même, comme une boule de neige : il faut alors un excédent primaire pour l’arrêter.
>
> En 2025, selon la Cour des comptes, r était de **2,0 %** [[fig:apparent_interest_rate_2025_pct]] et g de **1,9 %** [[fig:nominal_gdp_growth_2025_pct]]. Le taux r dépassait donc g de **0,1 point** [[yard:r_minus_g_2025_pp]], pour la première fois depuis la crise sanitaire. Pour stabiliser la dette, il aurait fallu un léger excédent primaire de **0,1 % du PIB** [[fig:debt_stabilizing_primary_balance_2025_pct_gdp]].
>
> Or la France avait un **déficit primaire de 2,9 % du PIB** [[fig:primary_balance_2025_pct_gdp]]. L’écart est de **3,0 points de PIB** [[fig:debt_stabilizing_gap_2025_pts]], soit **89,6 milliards d’euros** [[fig:debt_stabilizing_gap_2025_eur_bn]], **19,1 jours** de dépense publique [[calc:debt_stabilizing_gap_2025_eur_bn / yard:one_day_spending_eur_bn = 19,1]]. D’ici 2032, une mission de l’Inspection générale des finances (IGF) estime l’ajustement nécessaire à **environ 125 milliards d’euros** par rapport à la tendance [[fig:igf_adjustment_2032_eur_bn]].
>
> Attention : économiser 1 euro ne réduit pas le déficit de 1 euro la première année, car moins de dépense ou plus d’impôts freine l’activité. Le chapitre 7 explique pourquoi, et combien de mesures il faut vraiment.

**Interaction « Faites rouler la boule de neige »** : trois curseurs, r, g et solde primaire (% du PIB) ; sortie : dette en % du PIB sur 10 ans, à partir de **115,7 %** [[fig:debt_2025_pct_gdp]]. Valeurs de départ (2025, Cour des comptes, mention « mesuré ») : r **2,0** [[fig:apparent_interest_rate_2025_pct]], g **1,9** [[fig:nominal_gdp_growth_2025_pct]], solde primaire **−2,9** [[fig:primary_balance_2025_pct_gdp]]. Repère sur le curseur du solde : « stabilise la dette en 2025 : +0,1 » [[fig:debt_stabilizing_primary_balance_2025_pct_gdp]]. Formule dans « Comment est-ce calculé ? » : variation du ratio ≈ (r − g) / (1 + g) × dette − solde primaire, « illustratif, hors ajustements comptables ». Lien : « Trouvez ces 89,6 milliards d’euros vous-même » (simulateur, objectif A).

**Pastilles source** : [[fig:apparent_interest_rate_2025_pct]] [[fig:nominal_gdp_growth_2025_pct]] [[yard:r_minus_g_2025_pp]] [[fig:debt_stabilizing_primary_balance_2025_pct_gdp]] [[fig:primary_balance_2025_pct_gdp]] [[fig:debt_stabilizing_gap_2025_pts]] [[fig:debt_stabilizing_gap_2025_eur_bn]] [[yard:one_day_spending_eur_bn]] [[fig:igf_adjustment_2032_eur_bn]]

---

## Étape 12. Le débat : faut-il s’inquiéter ?

**Texte affiché**

> Le HCFP (organisme indépendant placé auprès de la Cour des comptes) parle d’un risque d’« effet boule de neige ». Nous décrivons la situation comme un **coût qui augmente**, pas comme une faillite imminente. Un État de la zone euro n’est pas liquidé comme une entreprise.
>
> Cela ne veut pas dire qu’il n’y a aucun risque. Le plus concret : plus la dette coûte cher, moins il reste pour le reste, et plus l’effort pour la stabiliser est grand.

**Encadré** (même écran, jamais replié)

<!-- box-side: gauche -->
> **Le meilleur contre-argument**
>
> **« Tant que la croissance dépasse le taux d’intérêt, la dette n’est pas un fardeau. »**
>
> L’économiste Olivier Blanchard (ancien économiste en chef du FMI) l’a soutenu en 2019, dans son discours de président de l’American Economic Association. Quand le taux d’intérêt reste durablement plus bas que la croissance, le poids de la dette baisse tout seul, sans excédent. La France a connu cette situation pendant la plupart des années 2015 à 2024.
>
> Deuxième argument : la hausse récente des taux français coïncide avec une période d’instabilité politique (dissolution de 2024, chutes de gouvernements, budgets difficiles à voter). L’agence de notation Moody’s cite elle-même la « fragmentation » du paysage politique (notre traduction). Selon cette lecture, la stabilité politique ferait plus baisser les taux qu’un plan d’économies.
>
> *Sources :* Olivier Blanchard (ancien économiste en chef du FMI), « Public Debt and Low Interest Rates », *American Economic Review*, 2019 ; Moody’s (agence de notation), communiqué du 24 octobre 2025 (via Reuters).
>
> **Ce qu’on peut répondre**
> En 2025, r a de nouveau dépassé g, de peu (étape 11). Sur les nouveaux emprunts, l’écart est plus net. En septembre 2026, l’État empruntait à 10 ans à **4,44 %** [[fig:oat10y_sep2026_pct]]. Pour 2026, la Cour des comptes (juridiction financière) prévoyait une croissance de **2,2 %** en valeur [[fig:nominal_gdp_growth_2026f_pct]].
>
> Blanchard précise que son raisonnement vaut pour des taux bas **et stables**. Sur ce point, l’objection tient à court terme pour la dette déjà émise. Elle s’affaiblit à mesure que cette dette est renouvelée aux taux actuels, sauf si la hausse de 2026 est passagère.
>
> La Cour des comptes (juridiction financière) ajoute qu’un ajustement choisi coûte moins cher qu’un ajustement imposé par les marchés. Elle cite les exemples du Portugal et de l’Italie.
>
> Les deux lectures ne s’excluent pas : la politique peut faire monter les taux, et un déficit élevé rend le pays plus sensible à ces hausses.

**Visuel** : aucun graphique ; texte et encadré tiennent sur un défilement court sur mobile.

**Pastilles source** : sources nommées dans l’encadré (`sources.json`, fichier 06 §7). « Ce qu’on peut répondre » : [[fig:oat10y_sep2026_pct]] [[fig:nominal_gdp_growth_2026f_pct]] (statut « caveat », prévision : mention « prévu » sur la pastille) ; Cour des comptes, ajustement « choisi » contre ajustement « imposé par les marchés » (fichier 06 §7, point 2 ; fichier 10 §7.2), pastille texte à rattacher au rapport exact de la Cour (le fichier 06 ne précise pas lequel ; à vérifier avant publication).

---

## Étape 13. Ce qu’il faut retenir

**Texte affiché**

> - Fin 2025, la dette atteignait **115,7 % du PIB**, soit **50 065 € par habitant** [[fig:debt_2025_pct_gdp]] [[yard:debt_per_capita_eur]], et elle a continué de monter en 2026.
> - Les intérêts coûtaient **14 jours** de dépense publique en 2025 [[calc:interest_2025_eur_bn / yard:one_day_spending_eur_bn = 14,0]] et pourraient augmenter de **25,3 milliards d’euros** d’ici 2027, selon la prévision du gouvernement [[yard:interest_rise_2025_2027_eur_bn]].
> - Pour arrêter la hausse de la dette, il manquait **89,6 milliards d’euros** en 2025 (Cour des comptes) [[fig:debt_stabilizing_gap_2025_eur_bn]]. Les trouver en dépenses ou en impôts est un choix politique, que ce site ne fait pas à votre place.

**Pour aller plus loin**

> - Page thématique « Déficit et dette » : trajectoire depuis 1978, détail par administration, écarts avec la zone euro à 20 pays.
> - Page thématique « La charge d’intérêts » : qui détient la dette de l’État, sensibilité aux taux, historique des notes souveraines.
> - Méthode : « Les trois chiffres des intérêts ».
> - Explication : « Pourquoi 1 euro d’économies ne réduit pas le déficit de 1 euro ».
> - Page « Les économies faciles » : les cibles citées par tous les camps, traitées de la même façon (chapitre 7).

---

## Étape 14. Transition

**Texte affiché**

> Vous savez maintenant ce que coûte la dette. Reste une question : que reçoit-on en échange des dépenses publiques ?
>
> **→ Chapitre 6 : Qu’obtient-on en échange ?** (pauvreté, santé, éducation, justice)
>
> **Ou passez à l’action → « Équilibrez vous-même le budget »** : trouvez les 89,6 milliards d’euros [[fig:debt_stabilizing_gap_2025_eur_bn]] qui auraient stabilisé la dette en 2025, avec vos propres choix.

**Visuel** : deux cartes (empilées sur mobile) ; le simulateur s’ouvre sur l’objectif A (« Stabiliser la dette »), option « hausse automatique des intérêts » activée.

---

## Notes pour l’équipe éditoriale (non publiées)

**1. Chiffres encore absents de `figures.json`** (non utilisés dans le texte affiché ; à créer seulement si l’on veut les afficher, procédure du `platform/data/README.md`, §4) :

| Id proposé | Contenu | Source dans la base |
|---|---|---|
| `ec_dsm_debt_2036_pct_gdp` | Projection de référence de la Commission européenne pour 2036, risque à moyen terme | fichier 06, §3.5 |
| `gg_net_worth_2025_eur_bn`, `net_investment_2025_pct_gdp` (0,6 % du PIB, 23e sur 27) | Actif net des APU, investissement net : contrepoids de l’investissement brut (4,4 %) désormais affiché à l’étape 6 | fichier 08, ligne 29 et tableau §6 |
| `avg_maturity_state_debt_2026_years` (environ 8,4 ans au 30 septembre 2026 ; 8,5 = fin 2025) | Maturité moyenne de la dette de l’État, prévue pour une quatrième puce de l’étape 6 ; le site de l’AFT refuse l’accès automatique (403) : à confirmer dans un navigateur | fichier 06 et fichier 10, §7.1 |
| `ea20_public_gfcf_2025_pct_gdp` (3,7) | Comparateur ZE20 de l’investissement public brut (étape 6) | fichier 08, ligne 28 |
| `imf_debt_2028f_pct_gdp` (121,1) | Prévision de dette du FMI pour 2028 (étape 4 : texte qualitatif en attendant) | fichier 06, §1 ; `f06:imf_aiv2026` |
| `ea20_debt_gap_2005_pp`, `ea20_debt_gap_2025_pp` | Écarts avec la ZE20 (convention du fichier 00) | fichier 06, §0 |
| `oat_btp_spread_sep2026_bp` (+8), `oat_bono_spread_sep2026_bp` (+51) | Écart OAT-BTP et OAT-Bono à 10 ans, moyenne de septembre 2026 (étape 10 : texte qualitatif en attendant) | fichier 06, résumé ; Eurostat `irt_lt_mcby_m` |
| `debt_change_2019_2025_pp` (+17,5) et son rang dans l’UE (3e, après la Roumanie et la Finlande) | Évolution du taux d’endettement 2019-2025 (étape 5 : texte qualitatif en attendant) | fichier 06, §4.2 ; Eurostat `gov_10dd_edpt1` |
| `deficit_worse_than_ea_years_2007_2025` (19 sur 19 ; écart moyen −1,8 point) | Années où le déficit français dépasse celui de la zone euro (étape 5 : texte qualitatif en attendant) | fichier 06, résumé et §0 ; Eurostat `gov_10dd_edpt1` |
| `debt_2035_hcsp_pct_gdp` | Dette à politique inchangée, projection du HCSP (Focus du 17 juillet 2026) ; à afficher avec la mention « projection à politique inchangée » | fichier 10, §7.2 (à vérifier dans le document primaire) |
| marge du calcul de l’écart OAT-Bund journalier (environ ±5 pb) | Note de la fiche `oat_bund_spread_22oct2026_bp` | fichier 06, §3.4 |

**2. Choix de rédaction.**
- « Estimez d’abord » (glossaire §1.13), et non « Devinez d’abord ».
- Intérêts 2025 comparés à des données par fonction 2024 : étiquettes d’année obligatoires jusqu’aux données Insee 2025 par fonction (décembre 2026).
- Écart de taux : 169 pb est une valeur d’un jour, calculée par la plateforme, 154 pb une moyenne mensuelle ; le texte dit « ponctuellement », donne la moyenne de septembre (97 pb) pour l’échelle et « en moyenne mensuelle, le maximum depuis 1993 reste… », jamais « record ».
- Notation : la valeur numérique (crans sous AAA/Aaa) est une convention d’affichage de la plateforme ; le texte affiche la lettre et la perspective (libellé de la fiche).
- Chiffres de marché et notation datés de la semaine du 22 octobre 2026 : à actualiser à chaque version des données (prochaine revue S&P : 27 novembre 2026, d’après l’AFT).

---

## Notes de relecture (25 octobre 2026, non publiées)

### Passe « ids de données créés » (25 octobre 2026)

- Étape 6, « Les limites de l’image » : **appliqué**. Puce sur la durée de vie moyenne de la dette négociable de l’État, **8,4 ans** au 30 septembre 2026 (`avg_maturity_state_debt_2026_years`, AFT, lu dans un navigateur ; « 8 ans et 158 jours »), avec renvoi à l’étape 10 ; ligne de source et pastilles mises à jour. Restent ouverts : `net_investment_2025_pct_gdp` et le comparateur ZE20 (`ea20_public_gfcf_2025_pct_gdp`), toujours absents de `figures.json`.

### Passe de finalisation (25 octobre 2026)

Décisions suivies : D-data-pass, D-labels (glossaire §1.13), D-boxes (glossaire §4.6), D-vocabulary (glossaire §2.7), D-rounding, D-ownership, D-reading-time.

1. **Nouveaux chiffres (D-data-pass, étape 6) : appliqué en partie.** Troisième puce de « Les limites de l’image » : investissement public brut **4,4 % du PIB** (`public_gfcf_2025_pct_gdp`, Eurostat), avec la mention « investissement brut, avant usure des équipements ». Quatrième puce : dette nette **108,5 % du PIB** fin 2025 (`net_debt_2025_pct_gdp`, Insee, 29 mai 2026), définie comme la dette brute diminuée des actifs financiers liquides (fichier 06, tableau des définitions). **Non ajouté :** la maturité moyenne (`avg_maturity_state_debt_2026_years`), parce que la fiche n’a pas été créée (AFT inaccessible aux scripts) ; même chose pour le comparateur ZE20 de l’investissement (3,7 %, sans fiche). Porte de publication (D-data-symmetry) : l’investissement brut est affiché sans l’investissement net (0,6 % du PIB, 23e sur 27, fichier 08), qui va dans l’autre sens ; il faut créer `net_investment_2025_pct_gdp` et l’ajouter dans la même puce, ou retirer le 4,4 %, avant la mise en ligne. Le retour à 60 ans (43 à 58 milliards) n’apparaît pas dans ce chapitre.
2. **Étiquettes (D-labels) : appliqué.** Cour des comptes (juridiction financière) à sa première mention (source de l’encadré de l’étape 6) et dans « Ce qu’on peut répondre » ; FMI (Fonds monétaire international ; organisation internationale) à sa première mention, à l’étape 4, avec une phrase qualitative sur la prévision du FMI (dette encore en hausse en 2028, pastille `[[src:f06:imf_aiv2026]]`, sans chiffre affiché). Cette mention règle le cas « Olivier Blanchard (ancien économiste en chef du FMI) » signalé par le responsable du glossaire : le FMI est déjà nommé avec son étiquette avant l’encadré. Blanchard porte l’étiquette exacte ; Moody’s (agence de notation) dans la ligne de source ; le HCFP (organisme indépendant placé auprès de la Cour des comptes) à l’étape 12, où il représente l’un des camps du débat.
3. **Encadré de l’étape 12 (D-boxes, §4.6) : appliqué.** Titre affiché `**Le meilleur contre-argument**` ; thèse en gras entre guillemets ; auteur avec étiquette ; ligne « *Sources :* » qui reprend les étiquettes ; `box-side: gauche` conservé ; « Ce qu’on peut répondre » placé dans le bloc affiché. La réponse ne traite que de la thèse de l’encadré, cite la Cour avec son étiquette et dit où l’objection tient (« à court terme pour la dette déjà émise »). L’intertitre interne ne porte plus le titre entre guillemets.
4. **Sigles (§2.7) : appliqué.** « produit intérieur brut (PIB) » à l’étape 1 ; Insee développé dans la ligne de source de l’étape 6 ; FMI à l’étape 4 ; « zone euro à 21 pays (ZE21, Bulgarie comprise) » devient la première mention de la zone euro (étape 5), ce qui règle le résidu signalé lors de la passe transversale.
5. **Lisibilité et typographie : appliqué.** 18 phrases de plus de 25 mots et 8 paragraphes de plus de 60 mots découpés, sans retrait d’information sourcée. Fourchettes « 2010-2012 », « 2007-2025 », « 2019-2025 » écrites « de … à … ». Nombres sans pastille retirés : « à 10 ans » (comparaison avec l’Italie et l’Espagne, remplacé par « à la même échéance »), « 27 » et « 20 ou 21 » de la ligne de comparaison, « 30 milliards » de « Pour aller plus loin » (remplacé par « 1 euro »). Pastille d’échelle du ménage marquée `|contexte`. Notation : « 3 niveaux » (Moody’s) et « 4 niveaux » (S&P, Fitch), chacun avec sa pastille, au lieu de « 3 à 4 niveaux ». Bloc « Estimez d’abord » de l’étape 1 : `<!-- estimez-réponse: debt_2025_pct_gdp -->`.
6. **Doublons et listes d’« économies faciles » (D-ownership) : appliqué.** Le chapitre 5 ne porte plus de liste de cibles. La ligne « Pour aller plus loin » qui citait seulement la contribution à l’Union européenne et les agences renvoie maintenant aux cibles de tous les camps (chapitre 7). Les 980 000 emplois, l’AME, la fraude sociale et le paquet de 10 à 25 milliards n’apparaissent pas dans ce chapitre.
7. **Contrôles.** `python3 -I validate.py --strict` : 0 erreur et 0 avertissement pour ce chapitre. Les deux avertissements transversaux « Cour des comptes » et « FMI » viennent des chapitres 2 et 7. Texte visible : 2 045 mots (cible de 1 500 à 2 200) ; durée de lecture portée à environ 9 minutes (2 045 / 240 = 8,5).

Reste ouvert : maturité moyenne (confirmation AFT dans un navigateur) ; investissement net (voir point 1) ; rapport exact de la Cour pour la pastille « ajustement choisi / imposé » ; titres définitifs des pages « Pour aller plus loin ».

### Passe transversale (plan de site) : corrections transversales (25 octobre 2026)

Décisions de site suivies : D-ownership, D-rounding, D-titles-and-transitions, D-boxes, D-labels, D-data-pass, D-reading-time, D-vocabulary.

1. **Titres d’étape et durée de lecture : appliqué.** 14 titres passés de « Étape N – » à « Étape N. ». Ligne affichée « Durée de lecture : environ 8 minutes. » ajoutée à l’étape 1 ; `duree_lecture` alignée (1 861 mots visibles, soit 7,8 minutes à 240 mots par minute).
2. **Étape 3, bloc déficit (propriété du chapitre 1) : appliqué.** Texte remplacé par une phrase de rappel (151,6 milliards ; 5,1 % du PIB ; renvoi au chapitre 4) et l’année 1974. Ruban « 32,3 jours » retiré du visuel ; compteur conservé avec [[yard:deficit_per_second_eur]], visuel seulement, « illustratif ». Pastilles `borrowed_one_euro_in`, `deficit_days`, `borrowing_starts_day` retirées.
3. **Étape 4, « 121,7 % du PIB » : appliqué.**
4. **Étape 5, « 87,3 % du PIB » et « zone euro à 21 pays (ZE21, Bulgarie comprise) » ; « Bulgarie comprise » dans la ligne de comparaison : appliqué.** Résidu : la première occurrence de « zone euro » sur la page reste la phrase précédente de l’étape 5 (« celui de la zone euro ») ; l’intitulé complet arrive une phrase plus loin, à l’emplacement fixé par le plan.
5. **Étape 6, image du ménage (propriétaire avec le chapitre 1) : appliqué en partie.** « Il doit 79 700 € » ; encadré converti en « Les limites de l’image » (ce n’est plus un encadré « Le meilleur contre-argument ») avec titre affiché ; trois puces conservées ; titre de la source déjà en italique ; « Ce qu’on peut répondre » renommé « Où l’image tient ». **Quatrième puce (dette nette 108,5 %, maturité moyenne environ 8,4 ans) et chiffre d’investissement public dans la troisième puce : non ajoutés**, car `net_debt_2025_pct_gdp`, `avg_maturity_state_debt_2026_years`, `public_gfcf_2025_pct_gdp` et le comparateur ZE20 n’existent pas encore dans `figures.json`. Porte de publication (D-data-symmetry) : le chapitre 5 ne peut pas être mis en ligne avant leur création et l’ajout de la puce.
6. **Étape 9 : appliqué.** « 5,4 jours » (au lieu de « environ 5 jours ») ; liste des promesses (taxe Zucman, contribution à l’Union européenne, agences) remplacée par un renvoi au chapitre 7, ce qui supprime aussi la fuite de l’estimation Zucman avant la question du chapitre 7 ; barres de fourchette retirées du visuel ; pastilles `zucman_*`, `eu_net_contribution_*`, `agencies_senate_saving_eur_bn` et note de symétrie retirées.
7. **Étape 10 : appliqué.** « 5,13 % » ; « (l’agence envisage de l’abaisser) » ; « 3 à 4 niveaux » au lieu de « crans » (texte affiché ; « crans » reste dans les consignes internes de visuel).
8. **Étape 11 : appliqué.** Première phrase découpée (moins de 25 mots par phrase) ; « 19,1 jours » ; paragraphe sur le multiplicateur et les 136 milliards remplacé par un renvoi au chapitre 7 (propriétaire du multiplicateur) ; pastilles `gross_measures_goal_a_eur_bn`, `multiplier_mixed_y1`, `deficit_semi_elasticity`, `macro_feedback_factor_mixed` retirées.
9. **Étape 12, encadré Blanchard (contre-argument de gauche conservé) : appliqué.** Étiquette « ancien économiste en chef du Fonds monétaire international, FMI » ; « L’agence de notation Moody’s » ; *American Economic Review* en italique. Le point ouvert « étiquette d’orientation absente » du passage « chapitres » est clos.
10. **Étapes 13 et 14 : appliqué.** Étape 13 inchangée (25,3 milliards, 14 jours) ; transition « **→ Chapitre 6 : Qu’obtient-on en échange ?** ».
11. **Contrôles : appliqué.** `python3 -I validate.py` : 0 erreur, 0 avertissement. Texte visible (lignes `>` avant les notes, pastilles retirées) : 1 861 mots (cible 1 500 à 2 200). Arrondis alignés sur D-rounding : 5,4 jours ; 19,1 jours ; 5,13 %.

Rejeté : aucun. Chiffres demandés mais absents de `platform/data` (texte écrit sans eux) : `net_debt_2025_pct_gdp` (108,5), `avg_maturity_state_debt_2026_years` (environ 8,4, à vérifier contre l’AFT, 30 septembre 2026), `public_gfcf_2025_pct_gdp` et son comparateur ZE20.

### Passage « audit croisé » (25 octobre 2026, lectures gauche, droite, chiffres)

Règle suivie : là où les lectures « gauche » et « droite » s’opposent, le texte expose les faits et les définitions, attribue les jugements (HCFP, Cour des comptes, Blanchard) et ne tranche pas. Aucun chiffre nouveau sans pastille : les valeurs proposées par l’audit qui n’ont pas encore de fiche dans `platform/data` sont rendues en phrases qualitatives et listées dans le tableau « Chiffres encore absents ».

1. **Étape 10, valeur d’un jour à côté d’un maximum mensuel (lecture gauche, faible) : appliqué en partie.** « ponctuellement environ 169 points de base (valeur d’un jour, calcul approximatif de la plateforme à partir de deux séries) », moyenne de septembre (97 pb, `oat_bund_spread_sep2026_bp`) dans la même phrase, puis « En moyenne mensuelle, le maximum depuis 1993 reste celui de novembre 2011 : 154 points ». La marge « ±5 points » n’est pas affichée : elle figure au fichier 06 §3.4 mais pas dans `figures.json` ; demande d’ajout dans la note de la fiche `oat_bund_spread_22oct2026_bp` (tableau des chiffres absents).
2. **Étape 12, réponse trop faible à l’argument de Blanchard (lecture droite, moyenne) : appliqué.** Réponse réécrite : r > g en 2025 ; nouveaux emprunts à 4,44 % (`oat10y_sep2026_pct`) contre une croissance en valeur de 2,2 % prévue par la Cour pour 2026 (`nominal_gdp_growth_2026f_pct`, au lieu de la fourchette « 2-2,5 % » du fichier 10, sans fiche) ; l’argument « tient à court terme pour la dette déjà émise » et s’affaiblit au renouvellement (fichier 10 §7.2, sans les horizons chiffrés « 2-3 ans » / « 10 ans », non présents dans les données) ; position de la Cour (ajustement « choisi » contre « imposé par les marchés », fichier 06 §7). Pour l’équilibre, la condition « sauf si la hausse de 2026 est passagère » (fichier 06 §7) et la phrase « Les deux lectures ne s’excluent pas » sont conservées. Reste à confirmer le rapport exact de la Cour pour la pastille.
3. **Étapes 5 et 10, faits comparatifs absents (lecture droite, moyenne) : appliqué en partie.** Ajouts vérifiés dans le fichier 06 (résumé, §0, §4.2) : déficit plus élevé que la zone euro chaque année de 2007 à 2025 ; depuis 2019, stabilisation ou baisse de la dette des pays touchés par la crise de 2010-2012, par des excédents primaires ; seules la Roumanie et la Finlande avec une hausse plus forte que la France entre 2019 et 2025 ; en septembre 2026, la France emprunte « un peu plus cher que l’Italie et plus cher que l’Espagne ». Les valeurs (+8 pb, +51 pb, +17,5 points, 3e rang, 19 années sur 19, −1,8 point) ne sont **pas** affichées : ce chapitre ne peut pas créer de fiches dans `figures.json` (hors périmètre de ce passage) ; ids proposés ajoutés au tableau. La phrase du fichier 10 (« les marchés intègrent désormais un risque budgétaire français ») n’est pas reprise comme voix du site : c’est une interprétation, et l’encadré de l’étape 12 garde la lecture « instabilité politique ».
4. **Étape 4, prévision de dette sans l’avis du HCFP (lecture droite, moyenne) : appliqué.** Ajout : le HCFP estime que la prévision de croissance pour 2027 « apparaît comme optimiste » (citation du texte primaire, fichier 10 §7.2 [S47]) ; conséquence formulée au conditionnel (« si la croissance est plus faible, la dette serait plus élevée que prévu »). Le chiffre de 1,0 % et l’écart de 0,1-0,3 point des autres prévisionnistes ne sont pas affichés (pas de fiche). Volet optionnel (HCSP, 140 % en 2035) non appliqué : pas de fiche ; `debt_2035_hcsp_pct_gdp` ajouté au tableau.
5. **Étape 6, intérêts toutes APU comparés à la défense LPM (chiffres, moyenne) : appliqué.** « plus que » supprimé ; la ligne défense devient une mention séparée « Autre périmètre, à ne pas comparer directement », avec renvoi à l’étape 8 (comparaison COFOG en % du PIB) ; consigne visuelle alignée sur l’étape 8.
6. **Arrondis d’un même indicateur entre chapitres (chiffres, faible) : rejeté pour ce fichier.** Le chapitre 5 affiche déjà 32,3 jours et 25,3 milliards, les formes retenues ; les corrections portent sur les chapitres 2, 3, 6 et 7, hors du périmètre de ce passage.
7. **Pastilles `calc:` sans résultat au chapitre 2 (chiffres, faible) : rejeté pour ce fichier.** Toutes les pastilles `calc:` du chapitre 5 portent déjà « = résultat » ; la correction concerne le chapitre 2.

**Contrôles.** `python3 -I validate.py` : 0 erreur, 0 avertissement. Texte public (lignes `>`, pastilles retirées, même méthode qu’au passage précédent) : 2 194 mots, dans la cible de 1 500 à 2 200, mais en limite haute : toute addition future appelle une coupe. `duree_lecture` portée à environ 9 minutes.

### Passage « chapitres » (25 octobre 2026, après le second passage de données)

**Volume.** Texte public mesuré par script (lignes citées `>` avant les notes, pastilles et balises retirées) : **1 936 mots avant**, **1 721 mots après** (cible : 1 500 à 2 200). Le comptage inclut la note de méthode repliable et « Pour aller plus loin » ; il exclut visuels, pastilles et notes.

**Blocs provisoires remplacés (2 blocs, 4 lignes signalées par `validate.py`, dont 2 dans les notes).**
1. Étape 10, bloc « Notation » : texte réécrit avec les notes d’octobre 2026 (`rating_moodys_oct2026_notches`, `rating_sp_oct2026_notches`, `rating_fitch_oct2026_notches`) et le tableau `credit_ratings_oct2026` (décisions de 2025 : Fitch 12 septembre et S&P 17 octobre, AA- → A+ ; Moody’s 24 octobre, perspective négative). « Deux agences ont abaissé… une troisième… » est maintenant chiffré et daté. Les crans (3 et 4) sont affichés « 3 à 4 crans ».
2. Étape 11, curseurs r et g : valeurs de départ `apparent_interest_rate_2025_pct` (2,0), `nominal_gdp_growth_2025_pct` (1,9), repère `debt_stabilizing_primary_balance_2025_pct_gdp` (+0,1). Le texte affiché utilise aussi ces valeurs et l’étalon `r_minus_g_2025_pp` (0,1 point), ce qui relie le constat « r > g » à l’écart de 3,0 points.
3. Étape 5 : ajout du rang dans l’UE (`debt_eu_rank_2025`, 3e sur 27, Eurostat 2025), précédemment dans la liste des chiffres à créer.
4. Préfixe `yd:` remplacé par `yard:` partout (47 avertissements) ; ajout de la pastille `household_monthly_income_eur` (paramètre) sur « 3 000 € ».

**Non utilisés, et passages réécrits pour s’en passer.**
- Décisions de notation 2023-2024 (non vérifiées) : le texte ne parle que des décisions de 2025, et dit « d’un cran, de AA- à A+ » sans dire comment la note était arrivée à AA-.
- Perspective au moment des abaissements de Fitch et S&P (inconnue) : non mentionnée ; seule la perspective actuelle est affichée.
- Nature des décisions des 10 avril, 29 mai et 28 août 2026 (inconnue) : non mentionnée.
- Confirmation de Moody’s du 23 octobre 2026 (source presse, statut « caveat ») : non mentionnée dans le texte ; la note affichée (Aa3, négative) est celle de la page de l’AFT. La fiche Moody’s est elle-même en statut « caveat » : afficher la mention correspondante sur sa pastille.
- r et g 2026 (prévision de la Cour ; 2,2 dans le texte de la Cour, 2,5 dans l’extraction du tableau 18) : non utilisés.

**Vérification des pastilles.** Toutes les pastilles `fig:` et `yard:` existent (`python3 -I validate.py` : 0 erreur, 0 avertissement pour ce chapitre). Valeurs affichées contrôlées une à une contre les fichiers, au format français et à l’arrondi `display_decimals` : 3 460,1 ; 115,7 ; 50 065 € ; 2,2 années ; 151,6 ; 5,1 ; 1 sur 11 ; 32,3 jours ; 29 novembre (jour 332,7) ; 4 800 €/s ; 1974 ; 3 595,5 ; 119,0 ; 119,3 ; 121,7 ; 5,0 ; −2,0 ; 28,4 ; 87,3 ; 3e sur 27 ; 3 000 ; 3 291 ; 291 ; 79 700 ; 126 ; 98 ; 65,7 ; 2,2 ; 3,8 ; 51,6 ; 14,1 ; 1,8 ; 5,1 ; 44 % ; 3,2 ; 8,9 ; 72,9 ; 63 ; 9,9 ; 79,2 ; 91 ; 25,3 ; 15-25 ; 2-6 ; 6,4 ; 9,5 ; 0,54 ; 4,44 ; 97 ; 5,126 ; 169 ; 154 ; 3,4 ; 8,1 ; Aa3/A+/A+ (3/4/4 crans) ; 2,0 ; 1,9 ; 0,1 ; +0,1 ; −2,9 ; 3,0 ; 89,6 ; 125 ; 136. Conversions recalculées : 14,0 jours ; 952 € ; 43 % ; 5,4 jours ; 175 € ; 19,1 jours.

**Coupes (sans perte d’information sourcée).**
- Étape 3 : phrases fusionnées. Étape 6 : la ligne « il gagne 3 000 € » (doublon de l’introduction) retirée ; « Ce qu’on peut répondre » renvoie à l’étape 10 au lieu de répéter le taux de 4,44 %.
- Étape 7 : « 4,2 % des recettes publiques » (`interest_to_revenue_pct`) retiré, quatrième conversion du même chiffre ; note de méthode raccourcie.
- Étape 10 : part des non-résidents (59,7 % de la dette négociable de l’État, `nonresident_share_state_debt_2026q2_pct`) déplacée vers « Pour aller plus loin » (page « La charge d’intérêts »).
- Étape 12 : la phrase sur r > g de « Ce qu’on peut répondre » renvoie à l’étape 11 au lieu de répéter le constat.
- Étape 13 : quatre puces ramenées à trois ; l’ajustement IGF d’ici 2032 reste à l’étape 11.
- Visuels et interactions condensés (mêmes consignes, moins de mots). Titre d’étape 9 : « La dépense qui augmente le plus vite » (sans chiffre comparatif dans `figures.json`) remplacé par « Une charge qui augmente vite ».
- Ajout d’un bloc « Pour aller plus loin » (liens vers les pages thématiques et de méthode du fichier 20, §4).
- `duree_lecture` corrigée : environ 8 minutes pour environ 1 720 mots (l’ancienne mention « 2 minutes » ne correspondait pas au volume).

**Points restant ouverts.**
- Encadré de l’étape 12 : le glossaire (§4.6) demande une « étiquette d’orientation » ; l’encadré nomme les auteurs et les sources, sans étiquette explicite. À trancher avec l’équipe (aucune étiquette n’existe dans la base pour Blanchard).
- Pages « Pour aller plus loin » : titres provisoires, à aligner sur les URL définitives des pages thématiques.

### Relecture précédente (25 octobre 2026, chiffres, neutralité, français)

Relecture en trois volets contre `figures.json` et `yardsticks.json` v1.0.0. Corrections faites alors (résumé) : ruban du 29 novembre et compteur de l’étape 3 ; renvois vers l’étape 11 ; « environ 50 065 € » ; définition de la dette ; pastilles de dénominateurs ; contribution à l’UE présentée en deux méthodes nommées ; « valeur de travail » du HCFP ; distinction entre l’écart de 2025 et l’ajustement IGF ; mention « calcul de la plateforme » pour la ZE21 ; réfutation sortie de l’encadré de l’étape 6 ; vocabulaire neutre (« non-résidents », « postes de la dépense publique ») ; formulation symétrique de la taxe Zucman ; phrase sur la « faillite » nuancée ; typographie conforme au glossaire (§2.1).
