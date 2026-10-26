---
chapitre: 7
titre: « Les choix »
sous-titre: Vieillissement, emploi, taille de l’effort et poids des promesses
statut: projet pour relecture éditoriale et relecture contradictoire (passe de finalisation)
date: 2026-10-25
données: platform/data/figures.json, yardsticks.json et proposals.json (passe de données du 25 octobre 2026, D-data-pass et D-return60 appliquées)
durée de lecture visée: environ 9 minutes (2 189 mots affichés mesurés par validate.py ; 240 mots par minute)
---

# Chapitre 7. Les choix

## Notes pour l’équipe (non affichées)

- **Pastilles source.** `[[fig:id]]` renvoie à `figures.json` ; `[[yard:id]]` renvoie à `yardsticks.json` (étalons, puis paramètres). `[[prop:id]]` renvoie à `proposals.json` ; `[[src:id]]` à `sources.json`. `[[calc:…]]` signale un calcul de la plateforme (mention « illustratif ») écrit avec les ids et des opérateurs explicites, selon `yardsticks.json → conversions` : jours = x / `one_day_spending_eur_bn` (4,6962 Md€) ; part du déficit = x / `deficit_2025_eur_bn` × 100 ; par habitant = x × 1 000 / `population_2025_m` ; ménage = x × `household_scale_eur_per_month_per_bn` (1,92 € par mois pour 1 Md€). Pour une fourchette, le calcul est fait sur chaque borne. Les montants 2026-2032 sont rapportés aux dénominateurs 2025 : ce sont des ordres de grandeur.
- **Aucun chiffre hors de `platform/data`** dans le texte affiché. Les montants annoncés par les partis viennent de `figures.json` (`rn_2026_pension_plan_cost_eur_bn`) ou de `proposals.json` (pastille `[[prop:…]]`) et portent toujours la mention « annoncé » ; ils sont montrés des deux côtés (RN à l’étape 6 ; Les Républicains et Horizons aux étapes 6 et 9).
- **Propriété des contenus (D-ownership).** Tailles des cibles d’« économies faciles » en jours : chapitre 2, étape 9. Rendements et verdicts : ce chapitre, étapes 8 et 9. Ensemble de hausses d’impôts sur les plus aisés (10 à 25 milliards), CDHR et effets sur l’emploi des allègements (980 000 emplois) : chapitre 3. Ici, une ligne et un renvoi.
- **Symétrie.** Les étapes 8 et 9 ont le même gabarit : une question « Estimez d’abord » sur un rendement, cinq puces (dont un « test réel » en deuxième position), un « Au total » et la même conclusion. L’audit de symétrie doit les comparer côte à côte.
- **Pyramide des âges (étape 5).** Le rapport entre personnes de 20 à 64 ans et de 65 ans et plus, et le taux d’emploi des 60-64 ans, ne sont pas dans `figures.json` : aucune valeur affichée tant qu’ils n’y sont pas.

---

## Étape 1. Ouverture : la taille du défi

**Texte affiché**

> Le chapitre 5 l’a montré. Pour que la dette cesse d’augmenter par rapport au produit intérieur brut (PIB), il faudrait trouver **89,6 milliards d’euros par an** [[fig:debt_stabilizing_gap_2025_eur_bn]]. C’est 3,0 points de PIB selon la Cour des comptes (juridiction financière), base 2025 [[fig:debt_stabilizing_gap_2025_pts]]. C’est la mesure d’un effort, pas l’annonce d’une faillite. Reste la question de la campagne : comment ?
>
> Durée de lecture : environ 9 minutes.

*Pas de curseur à cette étape : l’estimation de l’écart stabilisant la dette appartient au chapitre 5 (étape 11). Les interactions « Estimez d’abord » de ce chapitre sont aux étapes 8 et 9.*

**Pastilles source :** Cour des comptes, *La situation et les perspectives des finances publiques*, 25 juin 2026 [[fig:debt_stabilizing_gap_2025_eur_bn]].

---

## Étape 2. La taille de l’effort

**Texte affiché**

> Trois objectifs sont possibles (base 2025, avant effets sur la croissance) :
>
> - **Revenir à un déficit de 3 % du PIB** (la règle européenne) [[yard:maastricht_deficit_limit_pct]] : **61,9 milliards d’euros** [[yard:gap_to_3pct_eur_bn]]. Par coïncidence, c’est aussi l’ordre de grandeur des baisses d’impôts de 2018 à 2023 (chapitre 4), qui mesurent autre chose.
> - **Stabiliser la dette** par rapport au PIB : **89,6 milliards** [[fig:debt_stabilizing_gap_2025_eur_bn]].
> - **Équilibrer le budget** : tout le déficit, soit **151,6 milliards** [[fig:deficit_2025_eur_bn]].
>
> Stabiliser la dette, c’est **19,1 jours de dépense publique** [[calc:debt_stabilizing_gap_2025_eur_bn / one_day_spending_eur_bn = 19,1]] et **59 % du déficit 2025** [[calc:debt_stabilizing_gap_2025_eur_bn / deficit_2025_eur_bn × 100 = 59,1]].
>
> **Si la France était un ménage** gagnant 3 000 € par mois [[yard:household_monthly_income_eur]], il devrait trouver environ **172 € par mois** pour stabiliser sa dette [[calc:debt_stabilizing_gap_2025_eur_bn × household_scale_eur_per_month_per_bn = 172,0]]. (image illustrative, voir ses limites au chapitre 1)

**Visuel** : calendrier de la dépense publique (ruban des chapitres 1 et 2) ; la bande rouge « argent emprunté » couvre les 32,3 derniers jours [[yard:deficit_days]]. Trois marqueurs depuis le 31 décembre : 13,2 jours (étiquette « 61,9 Md€ (3 %) »), 19,1 jours (dette stable), 32,3 jours (équilibre). Bascule « vue ménage ». Données : `gap_to_3pct_eur_bn`, `debt_stabilizing_gap_2025_eur_bn`, `deficit_2025_eur_bn`, `one_day_spending_eur_bn`, `deficit_days`, `household_borrowing_month_eur`, `household_scale_eur_per_month_per_bn`.

**Pastilles source :** Eurostat, gov_10a_main, 21 octobre 2026 [[fig:deficit_2025_eur_bn]] ; Cour des comptes, 25 juin 2026 [[fig:debt_stabilizing_gap_2025_eur_bn]] ; calculs de la plateforme [[yard:gap_to_3pct_eur_bn]].

---

## Étape 3. Le vent contraire : ce qui augmente déjà

**Texte affiché**

> Trois postes poussent déjà la dépense vers le haut :
>
> - **Les intérêts de la dette** : 65,7 milliards en 2025, environ 91 milliards prévus en 2027 [[fig:interest_2025_eur_bn]] [[fig:interest_2027f_eur_bn]]. C’est **25,3 milliards de plus** [[yard:interest_rise_2025_2027_eur_bn]], soit 5,4 jours de dépense publique [[calc:interest_rise_2025_2027_eur_bn / one_day_spending_eur_bn = 5,4]].
> - **La défense** : la nouvelle cible de l’Organisation du traité de l’Atlantique nord (OTAN) coûterait environ **44 milliards par an** de plus d’ici 2035 [[fig:nato_35_gap_eur_bn]].
> - **Le climat** : de **25 à 34 milliards par an** d’investissement public supplémentaire d’ici 2030, selon Jean Pisani-Ferry et Selma Mahfouz (rapport remis au gouvernement) [[fig:climate_public_need_eur_bn]].
>
> Ces montants n’ont pas le même horizon : nous ne les additionnons pas.

**Visuel** : « jauge de pression », trois barres séparées (pas empilées), chacune avec son horizon (2027, 2035, 2030) et sa certitude (prévu, estimé, estimé) ; barre de fourchette pour le climat. Données : `interest_2025_eur_bn`, `interest_2027f_eur_bn`, `interest_rise_2025_2027_eur_bn`, `nato_35_gap_eur_bn`, `climate_public_need_eur_bn`.

**Pastilles source :** HCFP, avis n° HCFP-2026-5, et PLF 2027 [[fig:interest_2027f_eur_bn]] ; OTAN, juillet 2026 [[fig:nato_35_gap_eur_bn]] ; J. Pisani-Ferry et S. Mahfouz, *Les incidences économiques de l’action pour le climat*, mai 2023 [[fig:climate_public_need_eur_bn]].

---

## Étape 4. Pourquoi 1 € d’économie ne réduit pas le déficit de 1 €

**Texte affiché**

> Baisser une dépense ou augmenter un impôt freine l’activité la première année, donc les recettes.
>
> Le Haut Conseil des finances publiques (HCFP) retient un **multiplicateur budgétaire d’environ 0,6** la première année pour un ensemble de mesures mixte [[fig:multiplier_mixed_y1]]. Avec les recettes perdues [[fig:deficit_semi_elasticity|contexte]], **1 € de mesures réduit le déficit d’environ 0,66 €** la première année [[yard:macro_feedback_factor_mixed]].
>
> Avec cette règle moyenne, revenir à 3 % du PIB [[yard:maastricht_deficit_limit_pct]] demande environ **94 milliards d’euros de mesures** [[yard:gross_measures_goal_b_eur_bn]], et non le seul écart de l’étape 2. Couper 1 point de PIB (environ 30 milliards) [[yard:one_point_gdp_eur_bn]] dans les dépenses de fonctionnement pèse plus sur l’activité : le multiplicateur est d’environ 0,8 [[fig:multiplier_operating_spending_y1]]. Le déficit ne baisse alors que d’environ **16 milliards** la première année [[yard:example_cut_net_y1_eur_bn]].
>
> La Cour des comptes juge « comparables » les coûts des différents types de mesures (juin 2026) [[src:f17:S5]] : aucun n’est indolore.

<!-- box-side: droite -->
> **Le meilleur contre-argument**
>
> **« Un plan crédible, annoncé à l’avance, peut coûter très peu en croissance. »**
>
> Il rassure ménages, entreprises et prêteurs. Le gouvernement a retenu un multiplicateur nul en octobre 2024. Quand les marchés doutent de la dette, la Cour des comptes juge préférable de concentrer l’effort au début [[src:f17:S5]].
>
> *Sources : gouvernement, plan budgétaire et structurel à moyen terme, octobre 2024, cité par une mission de l’Inspection générale des finances (corps d’inspection du ministère de l’Économie), juillet 2026 ; Cour des comptes (juridiction financière), juin 2026.*
>
> **Ce qu’on peut répondre**
>
> La mission accueillie par l’Inspection générale des finances (corps d’inspection du ministère de l’Économie) parle d’une « hypothèse extrême » [[src:f17:S15]]. Le HCFP (organisme indépendant placé auprès de la Cour des comptes) retient environ 0,6 [[fig:multiplier_mixed_y1]]. Personne ne sait quelle valeur se réalisera : le simulateur montre une fourchette.

**Visuel** : curseur « multiplicateur » de 0 à 1,5 à côté d’une barre fixe de 30 Md€ d’économies (1 point de PIB) ; le gain net se recalcule en direct. Repères : 0 (hypothèse de 2024), 0,3-0,4 (« TVA, IR/CSG, 1re année, modèles français », classes `vat` et `income_tax_csg`), 0,6 (HCFP), 0,8 (dépenses de fonctionnement, `multiplier_operating_spending_y1`, fourchette 0,5-1,1), zone grisée à partir de 1,5 « valeurs de crise, pas 2027 ». Ne jamais afficher de « mesure qui s’autofinance ». Données : `multiplier_mixed_y1`, `multiplier_operating_spending_y1`, `deficit_semi_elasticity`, `macro_feedback_factor_mixed`, `one_point_gdp_eur_bn`, `example_cut_eur_bn`, `example_cut_net_y1_eur_bn`, `gross_measures_goal_b_eur_bn` ; classes de multiplicateurs de `simulator-levers.json`.

**Pastilles source :** HCFP, avis n° HCFP-2026-5, 25 septembre 2026, §36 [[fig:multiplier_mixed_y1]] ; CAE, *Focus* n° 108, 24 juillet 2024 [[fig:deficit_semi_elasticity]] ; OFCE, *Policy Brief* n° 154, et modèle Mésange (valeur par défaut du simulateur) [[fig:multiplier_operating_spending_y1]] ; Cour des comptes, *La situation et les perspectives des finances publiques*, 25 juin 2026, p. 139-140 [[src:f17:S5]] ; mission sur la transparence des finances publiques accueillie par l’Inspection générale des finances, juillet 2026 [[src:f17:S15]] ; calculs de la plateforme [[yard:example_cut_net_y1_eur_bn]] [[yard:gross_measures_goal_b_eur_bn]].

---

## Étape 5. Le vieillissement : le premier poste du budget

**Texte affiché**

> Les retraites sont le premier poste de la dépense publique : **422,2 milliards d’euros en 2025**, soit **14,1 % du PIB** (chapitre 2) [[fig:pensions_cor_2025_eur_bn]] [[fig:pensions_cor_2025_pct_gdp]].
>
> Selon le Conseil d’orientation des retraites (COR), cette dépense resterait stable en % du PIB jusqu’en 2045 (**14,2 %**) [[fig:pensions_cor_2045f_pct_gdp]], puis atteindrait **15,3 %** en 2070 [[fig:pensions_cor_2070f_pct_gdp]] (projections).

<!-- box-side: droite -->
> **Le meilleur contre-argument**
>
> **« Les retraites pèsent trop lourd : il faut ajuster la dépense, pas seulement les ressources. »**
>
> La vieillesse explique environ un tiers de l’écart de dépense avec la zone euro à 21 pays (ZE21, Bulgarie comprise) en 2024 [[fig:gap2024_old_age_share]]. Par habitant, en standards de pouvoir d’achat (SPA), la France est 5e sur 27 dans l’UE pour la dépense de retraite [[fig:pension_exp_per_capita_pps_2024_rank]]. Le FMI (Fonds monétaire international ; organisation internationale) recommande un mécanisme d’ajustement automatique des retraites.
>
> *Sources : FMI (organisation internationale), déclaration de fin de mission au titre de l’article IV, 21 mai 2026 (notre traduction) ; calcul de la plateforme d’après Eurostat (office statistique de l’Union européenne).* [[src:f20:f10]]
>
> **Ce qu’on peut répondre**
>
> Le COR (instance d’études et de concertation sur les retraites) projette une dépense stable en % du PIB jusqu’en 2045. Le déficit projeté viendrait d’abord de la baisse des ressources [[src:f07:S28]].
>
> Cette dépense achète aussi un résultat (chapitre 6). La pauvreté des personnes âgées est parmi les plus basses de l’OCDE (Organisation de coopération et de développement économiques ; organisation internationale). La plateforme ne dit pas s’il faut dépenser moins pour les retraites.

**Visuel** : (a) le calendrier se remplit de bleu jusqu’au 26 mars (COFOG 2024) ; (b) pyramide des âges animée 2005 → 2025 → 2070, sans valeur chiffrée tant que les données manquent ; (c) barre empilée de l’écart de 7,8 points avec la ZE21 (vieillesse 2,5, santé 1,5, autre protection sociale, reste), axe « en points de PIB ». Données : `pensions_cor_2025_*`, `calendar_days_old_age`, `household_pensions_month_eur`, `spending_gap_ea21_2024_pp`, `gap2024_old_age_pp`, `gap2024_old_age_share`, `gap2024_health_pp`, `pension_exp_per_capita_pps_2024_rank`, `cofog_old_age_2024_pct_te`. Projections du COR (2045, 2070) : aucune valeur affichée tant qu’elles ne sont pas dans `figures.json`. La contribution d’équilibre de l’État (`pension_state_balancing_contribution_2025_eur_bn`) et la convention de solde appartiennent au chapitre 2, étape 7.

**Pastilles source :** COR, rapport annuel, juin 2026 [[fig:pensions_cor_2025_eur_bn]] [[fig:pensions_cor_2045f_pct_gdp]] [[fig:pensions_cor_2070f_pct_gdp]] (projections, scénario de référence) ; Eurostat, `gov_10a_exp` (COFOG 2024) [[fig:gap2024_old_age_pp]] ; Eurostat, `spr_exp_pens`, 7 octobre 2026 [[fig:pension_exp_per_capita_pps_2024_rank]] ; FMI, déclaration de fin de mission au titre de l’article IV, 21 mai 2026 [[src:f20:f10]] ; COR, synthèse du rapport annuel, juin 2026 [[src:f07:S28]].

---

## Étape 6. La retraite à 60 ans : ce que pèse la promesse

**Texte affiché**

> La réforme de 2023 relève progressivement l’âge légal de départ à 64 ans. La loi de financement de la sécurité sociale pour 2026 a suspendu cette hausse jusqu’en janvier 2028 [[prop:pension_suspension|contexte]] [[src:f03]].
>
> Le retour général à 60 ans figurait dans le programme du Nouveau Front populaire en 2024 [[prop:retirement_60_general_nfp|contexte]]. La France insoumise propose la retraite à 60 ans avec 40 années de cotisation, comme objectif du mandat [[prop:lfi_retirement_60_40|contexte]].
>
> Un retour général à 60 ans coûterait **de 43 à 58 milliards d’euros par an** [[fig:return_60_general_cost_eur_bn]]. Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire) l’estime à environ 43 milliards [[fig:return_60_general_cost_eur_bn]]. L’Institut Montaigne (libéral-centriste) chiffre à 58 milliards le programme de retraite du Nouveau Front populaire [[fig:return_60_general_cost_eur_bn]]. Aucun chiffrage officiel récent n’existe.
>
> C’est de 9,2 à 12,4 jours de dépense publique [[calc:return_60_general_cost_eur_bn / one_day_spending_eur_bn = 9,2 à 12,4]] et de 28 % à 38 % du déficit 2025 [[calc:return_60_general_cost_eur_bn / deficit_2025_eur_bn × 100 = 28,4 à 38,3]]. Pour le ménage à 3 000 € par mois [[yard:household_monthly_income_eur]], c’est de 83 € à 111 € par mois [[calc:return_60_general_cost_eur_bn × household_scale_eur_per_month_per_bn = 83 à 111]] (image illustrative, voir ses limites au chapitre 1).
>
> Un retour réservé aux carrières longues coûterait **de 26 à 35 milliards** [[fig:return_60_partial_cost_eur_bn]]. Le Rassemblement national annonce environ **9 milliards** pour son plan (62 ans, 60 ans pour les carrières longues) [[fig:rn_2026_pension_plan_cost_eur_bn]] : un chiffre annoncé.
>
> À l’inverse, Les Républicains annoncent environ **42 milliards** d’économies [[prop:lr_pensions]] et Horizons environ **30 milliards** (45 annuités, 65 ans) [[prop:horizons_pensions_45y_65]] : des chiffres annoncés, eux aussi.

<!-- box-side: gauche -->
> **Le meilleur contre-argument**
>
> **« L’âge de départ est d’abord un choix de société. »**
>
> Son coût peut être financé autrement, par exemple par des cotisations plus élevées. Les modèles ne s’accordent pas non plus sur l’effet d’un recul de l’âge sur la croissance [[src:f17:S10]].
>
> *Sources : programmes de La France insoumise (2027) et du Nouveau Front populaire (2024) ; Cour des comptes (juridiction financière), rapport sur le système de retraites, 20 février 2025.*
>
> **Ce qu’on peut répondre**
>
> C’est exact : la plateforme ne dit pas quel âge choisir. Mais financer ce coût par des cotisations relèverait le coût du travail. Pour un salarié célibataire au salaire moyen, les prélèvements atteignent 47,2 % du coût du travail, le 3e niveau de l’OCDE (organisation internationale) [[fig:oecd_tax_wedge_single_2025_pct]] [[fig:oecd_tax_wedge_single_2025_rank]].

**Visuel** : barre de fourchette 43–58 Md€ (sources nommées dessous : Fipeco, 25 juin 2024, environ 43 ; Institut Montaigne, 3 juillet 2024, 58), barre 26–35 Md€ (retour partiel), points gris « annoncé » à 9 Md€ (RN, coût), 42 Md€ (LR, économie) et 30 Md€ (Horizons, économie), et, même style, étiquettes grises « programme » pour le Nouveau Front populaire (2024) et La France insoumise (sans montant annoncé dans `proposals.json` : étiquette sans point chiffré), même échelle, coûts à gauche et économies à droite de l’axe ; le calendrier se recolore (9,2 à 12,4 jours). Données : `return_60_general_cost_eur_bn`, `return_60_general_cost_pct_gdp`, `return_60_partial_cost_eur_bn`, `rn_2026_pension_plan_cost_eur_bn`, `one_day_spending_eur_bn`, `household_scale_eur_per_month_per_bn` ; `proposals.json` : `lr_pensions`, `horizons_pensions_45y_65`, `retirement_60_general_nfp`, `lfi_retirement_60_40`, `pension_suspension`.

**Pastilles source :** Institut Montaigne, 3 juillet 2024 (financé par des contributions privées de plus de 200 entreprises, chacune à moins de 1,2 % du budget, selon le site de l’Institut Montaigne) ; Fipeco, 25 juin 2024 [[fig:return_60_general_cost_eur_bn]] ; chiffre annoncé par le RN [[fig:rn_2026_pension_plan_cost_eur_bn]] ; chiffres annoncés par LR et Horizons (presse) [[prop:lr_pensions]] [[prop:horizons_pensions_45y_65]] ; programmes du Nouveau Front populaire (2024) et de La France insoumise [[prop:retirement_60_general_nfp]] [[prop:lfi_retirement_60_40]] ; loi de financement de la sécurité sociale pour 2026 [[prop:pension_suspension]] ; Cour des comptes, *Situation financière et perspectives du système de retraites*, 20 février 2025, p. 65-67 [[src:f17:S10]] ; OCDE, *Les impôts sur les salaires* [[fig:oecd_tax_wedge_single_2025_pct]].

---

## Étape 7. L’emploi et les heures travaillées

**Texte affiché**

> La France compte peu d’heures travaillées par habitant, surtout parce que les jeunes et les seniors ont moins souvent un emploi (chapitre 6).
>
> La direction générale du Trésor (administration économique) a fait un calcul « purement illustratif », sur la base de 2022. Si la France avait le taux d’emploi de l’Allemagne, les prélèvements obligatoires rapporteraient environ **38 milliards de plus par an** [[fig:employment_germany_levies_eur_bn]]. C’est **8,1 jours de dépense publique** [[calc:employment_germany_levies_eur_bn / one_day_spending_eur_bn = 8,1]] et **un quart du déficit 2025** [[calc:employment_germany_levies_eur_bn / deficit_2025_eur_bn × 100 = 25,1]].

<!-- box-side: gauche -->
> **Le meilleur contre-argument**
>
> **« Ceux qui ont un emploi en France travaillent plus d’heures qu’en Allemagne ou aux Pays-Bas. »**
>
> Dans ces pays, le temps partiel est fréquent. Les nouveaux entrants dans l’emploi seraient en moyenne moins productifs. Par heure travaillée, la France est 8e sur 27 dans l’UE, à l’indice 114,6 en SPA (moyenne de l’UE = 100) [[fig:productivity_per_hour_pps_2025]] [[fig:productivity_per_hour_pps_2025_rank]].
>
> *Sources : DG Trésor (administration économique), note d’août 2024 ; Eurostat (office statistique de l’Union européenne), `nama_10_lp_ulc`, 22 octobre 2026.* [[src:f08:es-lp]]
>
> **Ce qu’on peut répondre**
>
> Le calcul de la DG Trésor (administration économique) compte déjà en postes à temps plein, avec des nouveaux emplois moins productifs. La productivité horaire est aussi élevée parce que les moins productifs sont plus souvent sans emploi. Elle a d’ailleurs reculé depuis 2019 [[src:f20:f08]]. C’est un ordre de grandeur, pas une prévision.

**Visuel** : (les points du taux d’emploi appartiennent au chapitre 6 et ne sont plus repris ici) ; curseur « réduire de X % l’écart d’emploi avec l’Allemagne » (approximation linéaire, « illustratif »). Données : `employment_germany_levies_eur_bn`, `employment_germany_levies_headcount_eur_bn`, `productivity_per_hour_pps_2025`, `productivity_per_hour_pps_2025_rank`.

**Pastilles source :** DG Trésor, note pour le Haut Conseil du financement de la protection sociale, août 2024 [[fig:employment_germany_levies_eur_bn]] ; Eurostat, `nama_10_lp_ulc`, 22 octobre 2026 [[fig:productivity_per_hour_pps_2025]] [[fig:productivity_per_hour_pps_2025_rank]] ; recul depuis 2019 [[src:f20:f08]].

---

## Étape 8. Ce que pèsent les promesses d’« argent facile » (1) : les plus aisés et les entreprises

*Gabarit identique à l’étape 9. Ces pistes sont surtout portées par la gauche.*

**Interaction « Estimez d’abord »**
> **Selon vous, combien rapporterait chaque année la taxe Zucman** (un impôt minimum sur les très grands patrimoines) ?
<!-- estimez-réponse: zucman_proponents_eur_bn, zucman_critics_eur_bn -->

**Texte affiché (après la réponse)**

> - **Taxe Zucman.** Selon ses promoteurs (députées écologistes, proposition de loi n° 768), de 15 à 25 milliards par an avant effets de comportement [[fig:zucman_proponents_eur_bn]]. Selon ses critiques, de 2 à 6 milliards après ces effets [[fig:zucman_critics_eur_bn]]. Ces critiques : le Sénat (commission des finances), sept économistes dont Philippe Aghion, une étude commandée par le collectif de chefs d’entreprise « Trop, c’est trop ! ».
> - **Un test réel.** La contribution différentielle sur les hauts revenus, annoncée à environ 2 milliards, a rapporté moins de 0,4 milliard à son premier acompte (chapitre 3) [[fig:cdhr_announced_eur_bn]] [[fig:cdhr_observed_2025_eur_bn]].
> - **Fraude fiscale.** Selon la Cour des comptes, personne ne sait si elle est plus proche de 30 ou de 130 milliards par an [[fig:tax_gap_cour_range_eur_bn]] : aucune estimation robuste n’existe. En 2024, le contrôle fiscal a notifié 20,1 milliards et encaissé 11,4 milliards [[fig:tax_audit_assessed_2024_eur_bn]] [[fig:tax_audit_collected_2024_eur_bn]]. Le rendement d’un nouveau plan de lutte est à l’étape 9.
> - **Aides aux entreprises.** Elles vont de 45 à 211 milliards selon la définition (chapitre 2) [[fig:business_aid_range_eur_bn]] : c’est une assiette, pas un rendement. Supprimer les allègements généraux de cotisations rapporterait environ 48 milliards net [[fig:contribution_relief_abolition_net_eur_bn]], au prix de nombreux emplois (chapitre 3). Selon le rapport Bozio-Wasmer (rapport remis au gouvernement), un recentrage sur les bas salaires en coûterait beaucoup moins [[src:f08:bw2024]].
> - **Niches fiscales.** Elles coûtent 91,8 milliards en 2025 (chapitre 3) [[fig:tax_expenditures_2025_eur_bn]] : c’est aussi une assiette, pas un rendement.
>
> **Au total**, un ensemble de hausses d’impôts sur les plus aisés rapporterait de 10 à 25 milliards, selon notre synthèse (chapitre 3) [[fig:tax_rich_package_eur_bn]] : une estimation, pas une recette garantie.
>
> **Juste, ou suffisant ?** C’est une question de valeurs. La plateforme dit seulement si cela suffit.

**Visuel** : barres de fourchette horizontales, échelle commune de 0 à 100 Md€, ligne verticale à 89,6 Md€ (« dette stable ») ; auteur et orientation à chaque bout de barre ; aides aux entreprises et niches fiscales en barres grisées « assiette, pas un rendement » (45-211 ; 91,8), avec lien vers « Construisez votre définition », et, séparée, la barre de rendement « suppression des allègements généraux : 48 Md€ net » avec renvoi « emplois : chapitre 3 » ; fraude fiscale en barre grisée « incertitude : 30 ou 130 ? » (sans valeur centrale), à côté de la barre « contrôle fiscal 2024 : 20,1 notifiés, 11,4 encaissés » ; même gabarit que la fraude sociale à l’étape 9. Données : `zucman_proponents_eur_bn`, `zucman_critics_eur_bn`, `zucman_andrews_central_eur_bn`, `tax_rich_package_eur_bn`, `cdhr_announced_eur_bn`, `cdhr_observed_2025_eur_bn`, `tax_gap_cour_range_eur_bn`, `tax_audit_assessed_2024_eur_bn`, `tax_audit_collected_2024_eur_bn`, `business_aid_range_eur_bn`, `contribution_relief_abolition_net_eur_bn`, `tax_expenditures_2025_eur_bn`, `debt_stabilizing_gap_2025_eur_bn` ; montants des partis dans `proposals.json` (`zucman_tax`, `tax_rich_package`, `cdhr`).

**Pastilles source :** proposition de loi n° 768 déposée par des députées de gauche (Écologistes), 7 janvier 2025 [[fig:zucman_proponents_eur_bn]] ; étude de P. Andrews commandée par le collectif de chefs d’entreprise « Trop, c’est trop ! », juin 2026, et autres estimations publiées [[fig:zucman_critics_eur_bn]] ; synthèse de la plateforme ; composante succession sans chiffrage indépendant [[fig:tax_rich_package_eur_bn]] ; IPP et Cour des comptes, juin 2026 [[fig:cdhr_observed_2025_eur_bn]] ; Cour des comptes, *La lutte contre la fraude fiscale*, 16 décembre 2025 [[fig:tax_gap_cour_range_eur_bn]] [[fig:tax_audit_assessed_2024_eur_bn]] [[fig:tax_audit_collected_2024_eur_bn]] ; A. Bozio et É. Wasmer, *Les politiques d’exonérations de cotisations sociales : une inflexion nécessaire*, octobre 2024 [[src:f08:bw2024]] [[fig:contribution_relief_abolition_net_eur_bn]] ; Haut-commissariat à la Stratégie et au Plan, juillet 2026, et Sénat [[fig:business_aid_range_eur_bn]] ; Cour des comptes et PLF 2027, *Voies et moyens* [[fig:tax_expenditures_2025_eur_bn]].

---

## Étape 9. Ce que pèsent les promesses d’« argent facile » (2) : fraude, immigration, Europe, agences

*Gabarit identique à l’étape 8. Ces pistes sont surtout portées par la droite.*

**Interaction « Estimez d’abord »**
> **Selon vous, combien rapporterait chaque année un nouveau plan de lutte contre la fraude** (sociale et fiscale) ?
<!-- estimez-réponse: antifraud_marginal_yield_eur_bn -->

**Texte affiché (après la réponse)**

> - **Fraude sociale.** Les pertes estimées sont d’environ 14 milliards par an (chapitre 2) [[fig:social_fraud_hcfips_dec2025_eur_bn]]. Un nouveau plan de lutte, fiscal et social, rapporterait de façon réaliste **de 1 à 3 milliards** de plus par an [[fig:antifraud_marginal_yield_eur_bn]].
> - **Un test réel.** Le HCFP avait jugé non crédible la mesure antifraude de **1,5 milliard** du budget 2026 [[fig:antifraud_2026_announced_eur_bn]], qui a disparu de la prévision. Le projet de budget 2027 en attend 1 milliard [[prop:antifraud_plan]].
> - **Immigration et aide médicale de l’État (AME).** Le solde budgétaire des personnes nées à l’étranger dépend de la convention (OCDE, moyenne de 2006 à 2018). Il va d’un gain de 1,02 % du PIB par an à un coût de 0,85 % du PIB [[fig:immig_net_contrib_individual_pct_gdp]] [[fig:immig_net_contrib_all_public_goods_pct_gdp]]. L’AME a coûté 1,34 milliard en 2025 (chapitre 2) [[fig:ame_2025_eur_bn]].
> - **Contribution à l’Union européenne.** Elle atteint 9,5 milliards net en 2025 selon la méthode comptable, 6,4 milliards selon la Commission européenne (chapitre 2) [[fig:eu_net_contribution_2025_accounting_eur_bn]] [[fig:eu_net_contribution_2025_operating_eur_bn]]. La plafonner à 5 milliards économiserait **de 1,4 à 4,5 milliards au plus** [[calc:eu_net_contribution_2025_operating_eur_bn − 5 = 1,4 ; eu_net_contribution_2025_accounting_eur_bn − 5 = 4,5]]. Il faudrait changer la règle de financement du budget de l’UE, qui exige l’accord des 27 pays.
> - **État et agences.** Le Sénat estime l’économie réaliste d’une réorganisation des agences à **0,54 milliard par an** [[fig:agencies_senate_saving_eur_bn]]. Les Républicains annoncent 25 milliards du non-remplacement de 400 000 agents publics [[prop:lr_non_replacement_400k]]. Notre calcul (illustratif) donne de 12,6 à 25,3 milliards [[prop:lr_non_replacement_400k]].
>
> **Au total**, les cibles d’« économies faciles » pèsent environ **29 milliards**, même supprimées entièrement [[calc:eu_net_contribution_2025_accounting_eur_bn + oda_mission_plf2027_eur_bn + pouvoirs_publics_mission_eur_bn + public_broadcasting_plf2027_eur_bn + state_payments_associations_2025_eur_bn + ame_action_plf2027_eur_bn + strategy_consulting_2025_eur_bn = 29,4]]. Elle additionne la contribution à l’UE, l’aide au développement, la mission *Pouvoirs publics*, l’audiovisuel public, les associations, l’AME et les cabinets de conseil.
>
> **Juste, ou suffisant ?** C’est une question de valeurs. La plateforme dit seulement si cela suffit.

**Visuel** : mêmes barres, même échelle (0 à 100 Md€), même ligne à 89,6 Md€ qu’à l’étape 8. Bascule « Choisissez la convention » pour l’immigration (+1,02 %, +0,25 %, −0,85 % du PIB, équivalent en Md€ au PIB 2025 « illustratif », rang OCDE). Cascade UE : ressources propres 25,9 → dépenses de l’UE en France 16,4 → solde net 9,5 ; option « méthode de la Commission » (6,4) ; pastille juridique « décision relative aux ressources propres, adoptée à l’unanimité ». Données : `social_fraud_hcfips_dec2025_eur_bn`, `antifraud_marginal_yield_eur_bn`, `immig_net_contrib_*`, `gdp_2025_eur_bn`, `ame_2025_eur_bn`, `eu_net_contribution_2025_*`, `eu_own_resources_2025_eur_bn`, `eu_spending_in_france_2025_eur_bn`, `operators_public_funding_eur_bn`, `agencies_senate_saving_eur_bn` ; montants des partis dans `proposals.json` (`lr_non_replacement_400k` en point gris « annoncé » à 25 et barre « notre calcul » 12,6-25,3 ; `antifraud_plan` ; `rn_immigration_2027`, `lr_immigration`, `rn_ame_to_amu`, `rn_eu_cap`, `rn_fraud`, `lr_fraud`, `rn_agencies`, `lr_agencies`, `agencies_reform`).
- Somme des cibles (pastille `calc` ci-dessus) = `eu_net_contribution_2025_accounting_eur_bn` + `oda_mission_plf2027_eur_bn` + `pouvoirs_publics_mission_eur_bn` + `public_broadcasting_plf2027_eur_bn` + `state_payments_associations_2025_eur_bn` + `ame_action_plf2027_eur_bn` + `strategy_consulting_2025_eur_bn` = 29,4 Md€ (montants 2025 et PLF 2027 rapportés aux dénominateurs 2025 : ordre de grandeur ; l’AME y est comptée au PLF 2027).

**Pastilles source :** Haut Conseil du financement de la protection sociale, note adoptée le 4 décembre 2025 [[fig:social_fraud_hcfips_dec2025_eur_bn]] ; Cour des comptes et HCFP [[fig:antifraud_marginal_yield_eur_bn]] ; HCFP, avis n° HCFP-2026-5, §68 [[fig:antifraud_2026_announced_eur_bn]] ; OCDE, *Perspectives des migrations internationales 2021*, chap. 4 [[fig:immig_net_contrib_rank]] ; PAP 2027, programme 183 [[fig:ame_2025_eur_bn]] ; direction du Budget, *Jaune* « Relations financières avec l’Union européenne », PLF 2027 [[fig:eu_net_contribution_2025_accounting_eur_bn]] ; Sénat, rapport n° 807, 1er juillet 2025 [[fig:agencies_senate_saving_eur_bn]] ; PLF 2027 et *Jaunes* budgétaires ; HCFP, avis n° HCFP-2026-5 (mesure antifraude de 2026), et PLF 2027 [[prop:antifraud_plan]] ; programme de LR (presse) [[prop:lr_non_replacement_400k]].

---

## Étape 10. Toutes les pistes sur la même règle

**Texte affiché**

> Face à l’objectif de stabiliser la dette (89,6 milliards [[fig:debt_stabilizing_gap_2025_eur_bn]]), aucune promesse d’« argent facile », à gauche comme à droite, ne comble seule l’écart.
>
> Seuls les grands postes s’en approchent : retraites, masse salariale et fonctionnement, emploi, prestations sociales, impôts payés par tous. S’y ajoute le retour sur une partie des baisses d’impôts et de cotisations décidées depuis 2018, ou sur les dépenses fiscales.
>
> Le choix porte donc aussi sur **qui fait l’effort** : retraités, actifs, ménages les plus aisés, entreprises, consommateurs, usagers des services publics.

<!-- box-side: les-deux -->
> **Le meilleur contre-argument**
>
> **« Il existe une piste sérieuse : revenir sur les baisses d’impôts, ou rapprocher la dépense de celle de nos voisins. »**
>
> Côté recettes, la Cour des comptes chiffre les baisses d’impôts et de cotisations décidées de 2018 à 2023 à **62 milliards par an** (chapitre 4) [[fig:tax_cuts_2018_2023_eur_bn]]. Côté dépenses, la France dépense **57,3 % de son PIB** en 2025 [[fig:te_2025_pct_gdp]], 7,6 points de PIB de plus que la ZE21 (chapitre 1) [[fig:spending_gap_ea21_2025_pp]].
>
> *Sources : Cour des comptes (juridiction financière), rapport du 15 juillet 2024 ; Eurostat (office statistique de l’Union européenne), `gov_10a_main`, 21 octobre 2026.*
>
> **Ce qu’on peut répondre**
>
> Les prélèvements obligatoires représentent **43,6 % du PIB** en 2025 [[fig:po_2025_pct_gdp]] : la France est 2e de l’OCDE (organisation internationale) en 2024 (chapitre 3) [[fig:oecd_tax_to_gdp_2024_rank]]. Mais par habitant en SPA, elle est 9e sur 27 dans l’UE pour les recettes fiscales et 8e sur 27 pour la dépense (rangs estimés) [[fig:tax_revenue_per_capita_pps_2024_rank]] [[fig:te_per_capita_pps_2025_rank]].
>
> Sa dépense sociale nette, public et privé additionnés, est proche de celle des États-Unis (chapitre 2) [[fig:socx_net_total_2021_pct_gdp|contexte]] [[fig:us_socx_net_total_2021_pct_gdp|contexte]]. Sur le remède, la Cour des comptes (juridiction financière) et les économistes qui attribuent le déficit aux baisses d’impôts divergent (chapitre 4).

**Visuel** : toutes les barres des étapes 6 à 9 sur une seule échelle (0 à 160 Md€), en trois familles de même visibilité (« Grands postes », « Plus aisés et entreprises », « Fraude, immigration, Europe, agences ») ; « Grands postes » comprend, avec la même visibilité que les retraites et l’emploi : `tax_cuts_2018_2023_eur_bn` (62, « coût en 2023, plafond brut »), `tax_expenditures_2025_eur_bn` (91,8, « pas une recette disponible telle quelle »), `contribution_relief_abolition_net_eur_bn` (48, « emplois : chapitre 3 »), `annee_blanche_eur_bn` (4,4-5,7) et `pension_indexation_plfss2027_eur_bn` (4,1) ; trois lignes verticales : 61,9 Md€ (3 %), 89,6 Md€ (dette stable), 151,6 Md€ (équilibre). Légende : « Les lignes 61,9 Md€ (3 %) et la barre 62 Md€ (baisses d’impôts) ont la même taille par coïncidence. » Barres de coût vers la gauche d’un axe central, barres de rendement vers la droite ; couleurs neutres (aucune couleur associée à un camp). Données : ids des étapes 6 à 9, plus `tax_cuts_2018_2023_eur_bn`, `te_2025_pct_gdp`, `spending_gap_ea21_2025_pp`, `po_2025_pct_gdp`, `oecd_tax_to_gdp_2024_rank`, `tax_revenue_per_capita_pps_2024_rank`, `te_per_capita_pps_2025_rank`, `socx_net_total_2021_pct_gdp`, `us_socx_net_total_2021_pct_gdp`, `annee_blanche_eur_bn`, `pension_indexation_plfss2027_eur_bn`, `gap_to_3pct_eur_bn`, `deficit_2025_eur_bn`.

**Pastilles source :** Cour des comptes, *La situation et les perspectives des finances publiques*, 15 juillet 2024 [[fig:tax_cuts_2018_2023_eur_bn]] ; Eurostat, `gov_10a_main`, 21 octobre 2026 [[fig:spending_gap_ea21_2025_pp]] ; Insee, *Insee Première* n° 2106, 29 mai 2026 [[fig:po_2025_pct_gdp]] ; OCDE, *Statistiques des recettes publiques 2025* [[fig:oecd_tax_to_gdp_2024_rank]] ; Eurostat, calculs de la plateforme en SPA [[fig:te_per_capita_pps_2025_rank]] [[fig:tax_revenue_per_capita_pps_2024_rank]] ; OCDE, SOCX [[fig:socx_net_total_2021_pct_gdp]].

---

## Étape 11. Transition : à vous de choisir

**Texte affiché**

> Vous avez les ordres de grandeur. À vous de choisir.
>
> Dans le simulateur **« Équilibrez vous-même le budget »**, choisissez un objectif : 3 % du PIB [[yard:maastricht_deficit_limit_pct]], dette stable ou budget équilibré. Combinez ensuite les leviers : retraites, impôts, dépenses, emploi, cibles d’« économies faciles ». Chaque montant y figure en fourchette, effets sur la croissance compris.
>
> Pour vérifier une promesse de la campagne, utilisez le **vérificateur de promesses**.

**Boutons** : « Ouvrir le simulateur » (objectif « dette stable » présélectionné, effets de bouclage macroéconomique activés) ; « Vérifier une promesse » ; « Tester mes ordres de grandeur » (quiz).

**Visuel** : le graphique de l’étape 10 se réduit et devient la jauge du simulateur (« écart comblé : 0 sur 89,6 Md€ ») ; rappel en petit : « Avec les effets sur la croissance, il faut environ 136 Md€ de mesures pour gagner 89,6 Md€ net la 1re année » [[yard:gross_measures_goal_a_eur_bn]]. Carte de partage : « J’avais estimé X milliards. La Cour des comptes dit 89,6 milliards, soit 19,1 jours de dépense publique. »

**Pastilles source :** calculs de la plateforme [[yard:gross_measures_goal_a_eur_bn]].

---

## Pour aller plus loin

**Texte affiché**

> Fiches thématiques : retraites, emploi, multiplicateurs, aides aux entreprises, fraude, immigration, « économies faciles ».

*Liens vers les fiches du fichier 20, §4.4, §4.13, §4.18, §4.12, §4.11, §4.15, §4.16 et §4.10.*

---

## Notes de relecture (non affichées)

### Passe du 25 octobre 2026 : ids de données créés

- Étape 5 : projections du COR affichées (14,2 % du PIB en 2045, 15,3 % en 2070 ; `pensions_cor_2045f_pct_gdp`, `pensions_cor_2070f_pct_gdp`, statut « caveat », présentées comme projections).
- Étape 9, « Un test réel » : montant de la mesure antifraude du budget 2026, 1,5 milliard (`antifraud_2026_announced_eur_bn`, HCFP, avis n° HCFP-2026-5, §68).
- Retour à 60 ans : la borne basse vaut désormais 43 dans `figures.json` ; le texte de la décision D-return60 est affiché (43 à 58 ; 9,2 à 12,4 jours ; 28 % à 38 % ; 83 € à 111 €). Les mentions « 35 à 58 » du point 8 ci-dessous sont historiques.
- `pension_resources_2025_pct_gdp` et `pension_resources_2070f_pct_gdp` existent désormais mais ne sont pas affichés (encadré de l’étape 5) : le chapitre est à 2 198 mots affichés (plafond 2 200), tout ajout demande une coupe (décision éditoriale). Encore absents : productivité horaire 2019-2025, pyramide des âges, taux d’emploi des 60-64 ans.

### Passe du 25 octobre 2026 : finalisation

Prérequis reçus : D-return60 appliquée dans les données (fourchette 43 à 58), passe de données (19 ids, dont `tax_gap_cour_range_eur_bn`, `tax_audit_*_2024_eur_bn`, `multiplier_operating_spending_y1`, `productivity_per_hour_pps_2025` et son rang), CDHR retirée de `tax_rich_package_eur_bn`, glossaire §1.13 (étiquettes D-labels), §2.7 (sigles) et §4.6 (encadrés). `python3 -I validate.py --strict` : 0 erreur sur ce chapitre (3 erreurs `calc-value` de la ligne 135 corrigées, erreur `acronym` PIB et erreur `word-count` corrigées). Longueur mesurée par le validateur : 2 406 mots affichés avant, 2 189 après ; durée de lecture « environ 9 minutes » (2 189 / 240 = 9,1). Copie de la version précédente : (copie locale, non versionnée).

1. **Nouveaux chiffres (D-data-pass) : appliqué.** Étape 4 : multiplicateur d’environ 0,8 pour les dépenses de fonctionnement [[fig:multiplier_operating_spending_y1]] ; l’exemple de 30 milliards est présenté comme « 1 point de PIB (environ 30 milliards) » avec `[[yard:one_point_gdp_eur_bn]]` (supprime la collision `same-number-ids` avec le chapitre 1). Étape 7 : 8e sur 27, indice 114,6 en SPA [[fig:productivity_per_hour_pps_2025]] [[fig:productivity_per_hour_pps_2025_rank]], dans l’encadré. Étape 8 : « 30 ou 130 milliards » présenté comme l’incertitude, pas comme une estimation (note de l’id), 20,1 milliards notifiés et 11,4 encaissés en 2024. Non utilisés ici (attribués à d’autres chapitres par D-data-pass) : 49,3 milliards et convention de solde (chapitre 2), seuil de 2,5 SMIC (chapitre 3).
2. **Retraite à 60 ans (D-return60) : appliqué.** 43 à 58 milliards ; environ 43 selon Fipeco, 58 selon l’Institut Montaigne ; 9,2 à 12,4 jours ; 28 % à 38 % du déficit ; 83 € à 111 € par mois avec la ligne « (image illustrative, voir ses limites au chapitre 1) » (D-ownership) ; visuel 43–58 Md€. Calculs refaits : 43 / 4,6962 = 9,16 ; 58 / 4,6962 = 12,35 ; 43 / 151,6 = 28,4 % ; 58 / 151,6 = 38,3 % ; 43 × 1,92 = 82,6 ; 58 × 1,92 = 111,4.
3. **Étiquettes (D-labels) : appliqué, mot pour mot.** Cour des comptes (juridiction financière) à la première mention (étape 1) et dans chaque ligne de source d’encadré ; FMI (Fonds monétaire international ; organisation internationale) ; Institut Montaigne (libéral-centriste), sans « financé par… » dans le texte ; le financement vérifié sur le site de l’Institut Montaigne passe dans la pastille de l’étape 6 ; Fipeco (libellé inchangé) ; direction générale du Trésor et DG Trésor (administration économique) ; Jean Pisani-Ferry et Selma Mahfouz, rapport Bozio-Wasmer (rapport remis au gouvernement) ; dans les encadrés et leurs réponses : COR, OCDE, HCFP, Inspection générale des finances et Eurostat avec leur étiquette de statut. « T. Wasmer » corrigé en « É. Wasmer » (pastille de l’étape 8). HCSP et HCFiPS écrits en toutes lettres dans les pastilles.
4. **Encadrés (D-boxes, glossaire §4.6) : appliqué aux quatre encadrés de position et à celui des deux sens.** Titre exact, thèse en gras entre guillemets, paragraphe d’appui séparé, ligne *Sources :* en italique avec l’étiquette, réponse limitée à la thèse, étiquette `box-side` conservée (étape 4 droite, 5 droite, 6 gauche, 7 gauche, 10 les deux). Étape 4 : ajout d’un appui vérifié (Cour des comptes, juin 2026, p. 140 : concentrer l’effort au début quand la soutenabilité est mise en doute) ; « très favorable » (citation française non vérifiée) remplacé par « hypothèse extrême » (fichier 17, mission accueillie par l’Inspection générale des finances). Étape 6 : source réécrite (programmes de La France insoumise et du Nouveau Front populaire ; Cour des comptes, 20 février 2025, pour le désaccord des modèles [[src:f17:S10]]) ; « il monte progressivement, sur deux à quatre ans » retiré (non sourcé). Étape 10 : thèse en gras ajoutée ; titre de la Cour retiré de la ligne de source en italique (italique imbriqué illisible) et gardé dans la pastille ; renvoi au chapitre 4 pour le remède (D-ownership).
5. **Doublons (D-ownership) : appliqué.** Étape 5 : 422,2 milliards et 14,1 % suivis de « (chapitre 2) », « un euro sur quatre » retiré. Étape 7 : rangs d’emploi et d’heures (chapitre 6) remplacés par une ligne. Étape 8 : ensemble de 10 à 25 milliards et CDHR en une ligne chacun avec « (chapitre 3) », sans conversions ni prévision 2026 ; 980 000 emplois : **gardés au chapitre 3** (étape 11, niches sociales et rapport Bozio-Wasmer, déjà cible du renvoi du chapitre 2) ; ici « au prix de nombreux emplois (chapitre 3) » ; visuels des étapes 8 et 10 alignés. Aides aux entreprises, fraude sociale, AME et contribution à l’UE : montants rappelés avec « (chapitre 2) », sans conversion en jours (taille propriété du chapitre 2) ; « 0,3 jour (environ 7 heures) » de l’AME et les jours de la fraude sociale retirés. Conversions en jours de la taxe Zucman et du total de l’étape 9 retirées pour garder le même traitement des deux côtés et tenir la longueur.
6. **Symétrie des étapes 8 et 9 : appliqué, 5 puces de chaque côté.** Même ordre : la piste principale, « Un test réel » en deuxième, puis trois cibles, un « Au total » et « Juste, ou suffisant ? ». Gauche : taxe Zucman, CDHR, fraude fiscale, aides aux entreprises, niches fiscales (ajoutée : `tax_expenditures_2025_eur_bn`, « une assiette, pas un rendement », comme les aides aux entreprises). Droite : fraude sociale, mesure antifraude 2026, immigration et AME (fusionnées), contribution à l’UE, État et agences (agences et non-remplacement de 400 000 agents fusionnés). Les deux « Estimez d’abord » portent sur un rendement annuel : taxe Zucman (`<!-- estimez-réponse: zucman_proponents_eur_bn, zucman_critics_eur_bn -->`) et nouveau plan antifraude (`<!-- estimez-réponse: antifraud_marginal_yield_eur_bn -->`) ; pour éviter la fuite, le rendement du plan antifraude n’apparaît plus à l’étape 8 (renvoi « à l’étape 9 »). L’ancienne question sur l’AME en jours est retirée (taille propriété du chapitre 2). Test réel de droite : 1 milliard attendu au projet de budget 2027 [[prop:antifraud_plan]] ; le 1,5 milliard de 2026 n’est plus affiché (pas d’id). Rang de l’immigration (21e sur 25) retiré du texte pour la longueur, conservé au visuel.
7. **Alertes du validateur : traitées.** Pastilles sans nombre marquées `|contexte` (`deficit_semi_elasticity`, `pension_suspension`, `retirement_60_general_nfp`, `lfi_retirement_60_40`, SOCX) ; `pensions_cor_2025_pct_te` retiré ; 1,2 milliard de l’AME au PLF 2027 retiré du texte (ordre de grandeur dans la note de calcul) ; « 2006-2018 » écrit « de 2006 à 2018 » ; titre de publication en italique ; phrases de plus de 25 mots et paragraphes de plus de 60 mots découpés ; PIB développé à sa première occurrence ; OTAN au format du glossaire (« Atlantique nord »).
8. **Alertes restantes (hors de ce fichier).** (a) `rounding` l. 43 : `yardsticks.json` donne `display_decimals` 0 à `gap_to_3pct_eur_bn`, alors que D-rounding impose « 61,9 milliards » (jamais 62) : le propriétaire des données doit passer `display_decimals` à 1. (b) `same-number-ids` 25 Md€ : le haut de la fourchette des promoteurs de la taxe Zucman et celui de l’ensemble de 10 à 25 milliards sont tous deux exacts ; collision structurelle, à accepter ou à exempter dans le validateur. (c) `same-number-ids` 47,2 % : coïncidence entre le coin fiscal de l’OCDE (ce chapitre) et la part des foyers imposables (chapitre 3) ; exemption à prévoir dans le validateur ou mention « coïncidence » au chapitre 3.

### Passe du 25 octobre 2026 : corrections transversales (plan de site)

Passe transversale (plan de site) : décisions D-ownership, D-rounding, D-titles-and-transitions, D-boxes, D-labels, D-return60, D-data-pass, D-reading-time et D-vocabulary appliquées au chapitre 7. `python3 -I validate.py` : PASS, 0 erreur, 0 alerte. Longueur mesurée par script (lignes `>` hors pastilles, avant les notes) : 2 358 mots avant la passe, 2 357 après (2 482 titres compris).

1. **Titres d’étape « ## Étape N. Titre » et durée de lecture : appliqué.** 11 titres convertis ; front matter aligné (environ 10 minutes).
2. **Étape 1, rappel de l’écart stabilisant la dette (propriété du chapitre 5, étape 11) : appliqué, N = 10 et non 9.** Bloc unique, sans curseur ; ligne « Durée de lecture : environ 10 minutes. » calculée sur 2 357 mots / 240 (9,8). Les interactions « Estimez d’abord » restent aux étapes 8 et 9.
3. **Étape 2, 61,9 contre 62 : appliqué.** 61,9 milliards avec la note « coïncidence » ; 89,6 milliards ; 19,1 jours ; ligne ménage remplacée par « (image illustrative, voir ses limites au chapitre 1) » ; marqueur 13,2 jours étiqueté « 61,9 Md€ (3 %) » ; bande « argent emprunté » à 32,3 jours. En plus, pour la longueur : « environ 1 300 € par habitant » retiré (conversion non propriétaire).
4. **Étape 3, OTAN développé : appliqué.** 25,3 milliards / 5,4 jours conservés.
5. **Étape 4, exemple du multiplicateur : appliqué, y compris la coupe optionnelle.** 94 milliards « et non 61,9 » avec la règle moyenne de 0,66 ; l’exemple des 16 milliards est présenté comme un cas à multiplicateur plus élevé. `multiplier_operating_spending_y1` absent de `yardsticks.json` : la valeur 0,8 n’est pas affichée (« avec un multiplicateur plus élevé »). Paragraphe des multiplicateurs par type d’impôt remplacé par la phrase courte (Cour, « comparables »). Encadré : thèse en gras entre guillemets ; ligne de source « gouvernement, … » ; deuxième phrase raccourcie pour éviter la redite de la thèse.
6. **Étape 5, texte et « Estimez d’abord » : appliqué.** Premier paragraphe remplacé (422,2 milliards, 14,1 % du PIB, un euro sur quatre, chapitre 2) ; interaction courte supprimée (doublon du chapitre 2, étape 1, et de Q01). COR développé à sa première occurrence. Pour la longueur, la fin du paragraphe COR (« le déficit projeté viendrait d’abord de la baisse des ressources ») passe dans la réponse de l’encadré, avec sa pastille [[src:f07:S28]].
7. **Étape 5, encadré rééquilibré à droite : appliqué.** Thèse FMI ; 32 % de l’écart (« environ un tiers »), 5e sur 27 en SPA ; première mention de la zone euro au format « zone euro à 21 pays (ZE21, Bulgarie comprise) » ; OCDE développé dans la réponse. Retirés : 6,1 % / 14,8 % (chapitre 6), solde −5,1 / −0,2 (chapitre 2), « notre base, fichier 03 ». Visuel et pastilles mis à jour (ajout `pension_exp_per_capita_pps_2024_rank` et Eurostat `spr_exp_pens`). La recommandation du FMI est vérifiée dans `research/10`, l. 282 ; pas encore d’entrée FMI dans `sources.json` (D-data-pass) : pastille [[src:f20:f10]].
8. **Étape 6 : partiel.** Appliqué : suspension par la loi de financement de la sécurité sociale pour 2026 jusqu’en janvier 2028 [[prop:pension_suspension]] [[src:f03]] (vérifié dans `research/03`, §3) ; Nouveau Front populaire (2024) et La France insoumise (60 ans, 40 années, objectif du mandat) nommés ; encadré : thèse en gras, nouvelle attribution sans « fichier 11 » ni « fichier 03 » ; points/étiquettes NFP et LFI au visuel (sans montant : `claimed` est nul dans `proposals.json`). **Non appliqué (prérequis manquant)** : `return_60_general_cost_eur_bn.range.low` vaut encore 35 dans `figures.json`. Le chiffrage reste donc 35 à 58 milliards, 7,5 à 12,4 jours, 23 % à 38 % du déficit, 67 € à 111 € par mois, avec l’attribution actuelle (Montaigne en haut, Fipeco « à l’intérieur »). Étiquettes de Fipeco et de l’Institut Montaigne inchangées : le glossaire (l. 424) n’a pas encore reçu les libellés D-labels. Dès le passage à 43 : texte de la décision (43 à 58 ; 9,2 à 12,4 jours ; 28 % à 38 % ; 83 € à 111 € ; « environ 43 selon Fipeco, 58 selon l’Institut Montaigne »), barre 43–58 (consigne écrite dans le visuel).
9. **Étape 7 : appliqué, sauf la productivité.** Premier bloc : renvoi au chapitre 6 (21e et 27e sur 27) ; « en comptant en postes à temps plein » (texte et réponse) ; encadré : thèse en gras, source sans « fichier 08 ». Points du taux d’emploi retirés du visuel ; curseur conservé. `productivity_per_hour_pps_2025` et son rang sont absents : 114,6 et 8e sur 27 non affichés ; « elle a reculé depuis 2019 » reste sans chiffre.
10. **Étape 8 : appliqué, sauf les montants de la fraude fiscale.** « Juste, ou suffisant ? » ; « en comptant en postes à temps plein » ; « salaire minimum (SMIC) ». `tax_gap_cour_range_eur_bn`, `tax_audit_assessed_2024_eur_bn` et `tax_audit_collected_2024_eur_bn` sont absents : « 30 ou 130 », 20,1 et 11,4 non affichés. Étiquette de l’étude « Trop, c’est trop ! » inchangée : le glossaire n’en fixe pas. Pastilles source sans « fichier 07 / 08 » ; ligne de `tax_rich_package_eur_bn` : « synthèse de la plateforme ; composante succession sans chiffrage indépendant ».
11. **Étape 9 : appliqué.** « Juste, ou suffisant ? » ; immigration sans signes (« un gain de 1,02 % du PIB à un coût de 0,85 % du PIB ») ; AME « environ 7 heures, chapitre 2 » ; contribution à l’UE en langage B1 (accord des 27 pays) ; « Au total » en trois phrases, PLF développé, formule complète dans la première pastille `calc`. Pastilles source sans « fichier 07 / 11 / 16 ».
12. **Étape 10 : appliqué.** 89,6 milliards avec pastille ; titre d’encadré exact puis « *Dans les deux sens* » ; « (chapitre 4) » après 13,2 jours ; titre de la Cour en italique, au format du chapitre 4 ; OFCE remplacé par « les économistes qui attribuent le déficit aux baisses d’impôts (chapitre 4) » ; « Pour la Cour des comptes (chapitre 4) » ; phrase de la vieillesse supprimée (désormais dans l’encadré de l’étape 5) ; légende « coïncidence » ajoutée au visuel. En plus, pour la longueur et D-ownership : côté dépenses ramené à une ligne (7,6 points, « chapitre 1 », sans les 227 milliards ni `spending_gap_ea21_2025_eur_bn`) ; « (chapitre 3) » après le rang OCDE ; « (chapitre 2) » après SOCX ; phrase « Les deux chiffres sont exacts… » retirée ; SPA non redéveloppé.
13. **Étape 11 : appliqué.** 19,1 jours sur la carte de partage.
14. **Longueur : partiel.** 2 357 mots affichés, au-dessus de la cible de 2 200. Les remplacements demandés (étapes 1, 2, 5, 6, 9) ajoutent plus qu’ils ne retirent ; les coupes ci-dessus ont compensé environ 95 mots. Il manque environ 160 mots. Candidats à arbitrer, de façon symétrique entre gauche et droite : puce « Immigration » (étape 9) et puce « Taxe Zucman » (étape 8) renvoyées à leurs fiches, avec une ligne chacune ; liste « Pour aller plus loin » (41 mots) hors du compte ; troisième paragraphe de l’étape 6, une fois la borne basse corrigée.

Restent hors de ce chapitre : ajout des ids de la passe de données (productivité, fraude fiscale, `multiplier_operating_spending_y1`), borne basse à 43, entrée FMI dans `sources.json`, nouveaux libellés du glossaire (§1.13).

### Passe du 25 octobre 2026 (troisième) : audit contradictoire (lecteur de gauche, lecteur de droite, chiffres)

Règle suivie : aucun nombre sans pastille résolue dans `platform/data`. Les ids demandés par l’audit qui n’existent pas encore dans `figures.json` (fichier hors de mon périmètre) n’ont pas été créés : la phrase est écrite sans le nombre, avec une pastille `[[src:…]]` vers la source vérifiée, et l’ajout du chiffre est renvoyé aux points ouverts. `python3 -I validate.py` : PASS, 0 erreur, 0 alerte.

1. **Étape 5, démographie et « aucun plan ne peut ignorer » (gauche, élevée) : partiellement appliqué.** Phrase démographique sans source supprimée ; remplacée par la projection du COR (stable en % du PIB jusqu’en 2045, hausse ensuite, déficit d’abord dû à la baisse des ressources) [[src:f07:S28]], sans les valeurs 14,2 / 15,3 / 12,9 % (ids `pensions_cor_2045f_pct_gdp`, `pensions_cor_2070f_pct_gdp`, `pension_resources_2070f_pct_gdp` absents). Réponse normative remplacée par la formulation proposée, précisée « jusqu’en 2045 » (fichier 02 l. 542 : après 2045, la dépense augmente aussi).
2. **Étape 10, leviers de recettes absents de la règle (gauche, élevée) : appliqué.** Liste du texte élargie (baisses d’impôts et de cotisations depuis 2018, dépenses fiscales) ; famille « Grands postes » du visuel : `tax_cuts_2018_2023_eur_bn` (« coût en 2023, plafond brut »), `tax_expenditures_2025_eur_bn` (« pas une recette disponible telle quelle »), `contribution_relief_abolition_net_eur_bn` (avec les emplois). Les exonérations sociales (91,0) n’ont pas d’id : non ajoutées.
3. **Fraude fiscale absente (gauche, élevée) : partiellement appliqué (partie chapitre 7).** Puce « Fraude fiscale » ajoutée à l’étape 8 avec le même gabarit que la fraude sociale : absence d’estimation robuste selon la Cour [[src:f07:S10]] et rendement réaliste de 1 à 3 milliards (`antifraud_marginal_yield_eur_bn`, fiscal et social). Les montants 20,1 / 11,4 / « 30 ou 130 » ne sont pas affichés : ids `tax_audit_*` et `tax_gap_cour_range_eur_bn` absents. Chapitres 2 et 3 hors périmètre.
4. **Étape 10, réponses asymétriques (gauche, moyenne) : appliqué.** « déjà » supprimé ; côté dépenses : 8e sur 27 par habitant en SPA (« estimé », égalité statistique avec la Suède selon la note de l’id) et SOCX net public + privé proche des États-Unis ; côté recettes : 9e sur 27 en recettes fiscales par habitant en SPA (« estimé »). « n’est que » de la proposition non repris (adverbe orienté, symétrique de « déjà »).
5. **Économies annoncées par la droite absentes (gauche, moyenne) : appliqué.** Étape 6 : LR environ 42 milliards [[prop:lr_pensions]], Horizons environ 30 milliards [[prop:horizons_pensions_45y_65]], « annoncés, non estimés de façon indépendante ». Étape 9 : non-remplacement de 400 000 agents, 25 annoncés, 12,6 à 25,3 selon notre calcul [[prop:lr_non_replacement_400k]]. Note pour l’équipe mise à jour (les montants des partis peuvent venir de `proposals.json`, mention « annoncé »).
6. **« Test réel » seulement à gauche (gauche, moyenne) : appliqué (chapitre 7).** Étape 9 : mesure antifraude de 1,5 milliard du projet de budget 2026, jugée non crédible par le HCFP et disparue de la prévision 2026 [[prop:antifraud_plan]] (sans guillemets : la citation française exacte n’est pas vérifiée dans le fichier 07, l. 238). CDHR : ajout « environ 0,7 milliard est prévu pour 2026 » via [[prop:cdhr]] (`cdhr_2026f_eur_bn` absent ; la valeur 0,7 est dans `proposals.json`, estimation IPP). Chapitre 3 et quiz Q34 hors périmètre.
7. **Verbes différents selon le camp, Zucman (gauche, moyenne) : appliqué.** « Selon ses promoteurs … / Selon ses critiques … » ; promoteurs nommés dans le texte (proposition de loi n° 768, députées écologistes).
8. **Exonérations : seul le scénario extrême (gauche, moyenne) : partiellement appliqué.** Phrase ajoutée (effets forts près du SMIC, faibles ou nuls nettement au-dessus ; un recentrage coûterait beaucoup moins d’emplois) [[src:f20:f08]], sans le seuil « 2,5 SMIC » (paramètre absent de `yardsticks.json`) ni `plfss2027_art7_relief_eur_bn` (absent).
9. **Heures par habitant sans productivité horaire (gauche, faible) : partiellement appliqué.** Encadré de l’étape 7 : productivité horaire au-dessus de la moyenne de l’UE [[src:f20:f08]], sans 114,6 ni le rang 8/27 (`productivity_per_hour_pps_2025` absent). Réponse : effet de sélection et recul depuis 2019 conservés, sans le −0,8 % (pas d’id).
10. **« Ensemble plausible » de 10 à 25 milliards (droite, élevée) : partiellement appliqué (texte).** « Selon notre synthèse des chiffrages publiés (aucun organisme n’a chiffré cet ensemble) », phrase sur la composante succession sans chiffrage indépendant et « une estimation, pas une recette garantie ». La phrase proposée « la moitié haute » est remplacée par « une bonne part du haut de la fourchette » : la composante succession (3 à 10) ne fait pas à elle seule la moitié haute (fichier 07 §5). Le retrait de la CDHR du paquet et la note dans `figures.json` relèvent du propriétaire des données.
11. **Exemple de multiplicateur uniquement sur la dépense (droite, élevée) : partiellement appliqué.** Ajout : multiplicateurs plus faibles pour TVA, IR et CSG dans les modèles français [[src:f17:S6]] ; études historiques multi-pays en sens inverse (Guajardo, Leigh et Pescatori ; Alesina, Favero et Giavazzi) [[src:f17:S3]] [[src:f17:S4]] ; coûts « comparables » selon la Cour (p. 139) [[src:f17:S5]]. Repère 0,3-0,4 ajouté au visuel (classes `vat` et `income_tax_csg` de `simulator-levers.json`). Non repris : le montant net « [calc avec 0,4] » et les coefficients 0,43 / 1,29 et 0,28-0,46 / 0,96-1,50 (aucune pastille ne peut les porter). L’étiquette « austérité expansionniste » ne s’applique qu’à Alesina et coll. : Guajardo et coll. réfutent cette thèse (fichier 17).
12. **Remède selon la Cour et le FMI (droite, élevée) : appliqué (chapitre 7).** Réponse de l’étape 10 : position de la Cour [[src:f20:cour26]] en paraphrase (la citation française n’est vérifiée qu’en traduction anglaise dans le fichier 10, l. 139), avec en regard la position de l’OFCE [[src:f20:f10]] pour la symétrie. Le FMI n’est pas cité : pas de source FMI dans `sources.json`. Chapitre 4 hors périmètre.
13. **Étiquettes d’orientation asymétriques (droite, élevée) : partiellement appliqué.** Étape 8 : critiques nommés (commission des finances du Sénat, sept économistes dont Philippe Aghion, étude commandée par « Trop, c’est trop ! ») et promoteurs nommés. Étiquettes de l’Institut Montaigne et de Fipeco inchangées : elles suivent le glossaire §424, qui fait foi et relève de son propriétaire. Chapitre 3 hors périmètre.
14. **Solde des retraites sans convention (droite, moyenne) : partiellement appliqué.** Réponse de l’étape 5 : le quasi-équilibre dépend d’une convention (contribution d’équilibre de l’État employeur comptée en recettes) [[src:f20:f03]] ; le COR recommande de regarder la dépense en % du PIB (14,1 %). Les valeurs 49,3 milliards et −0,2 à −1,9 % du PIB ne sont pas affichées (ids absents).
15. **Masse salariale absente des grands postes ; asymétrie assiette / rendement (droite, moyenne) : appliqué.** Texte : « masse salariale et fonctionnement des administrations ». Étape 8 : « c’est une assiette, pas un rendement » ; visuel : barre grisée d’assiette 45-211 et barre de rendement 48 séparée, même gabarit que la fraude sociale. « Grands postes » : `annee_blanche_eur_bn` et `pension_indexation_plfss2027_eur_bn`.
16. **Métaphore du ménage à moitié (droite, faible) : appliqué** (étape 2). Chapitre 3 hors périmètre.
17. **Encadré de l’étape 6 sans auteur (droite, faible) : appliqué.** Argument attribué aux partis de gauche qui proposent le retour à 60 ans (fichier 11) ; réponse complétée par le coin fiscal (47,2 %, 3e de l’OCDE), sans « déjà » pour la même raison qu’au point 4.
18. **24,3 % contre 23,4 % (chiffres, élevée) : appliqué.** Texte et réponse « Estimez d’abord » : 23,4 % (COFOG 2024) en référence, 24,3 % présenté comme calcul propre du COR.
19. **Fourchette du retour à 60 ans (chiffres, moyenne) : partiellement appliqué.** Le texte n’attribue plus la borne basse à Fipeco et à l’Institut Montaigne : « selon les chiffrages publiés », haut de fourchette attribué à l’Institut Montaigne (58), Fipeco « à l’intérieur ». La décision sur la borne basse (option A : 43 ; option B : source primaire pour 35) revient au propriétaire de la recherche ; le texte, les calculs et le visuel suivront.
20. **16 milliards avec m = 0,8 non affiché (chiffres, moyenne) : appliqué.** Multiplicateur d’environ 0,8 affiché dans l’exemple ; la pastille `[[yard:example_cut_net_y1_eur_bn]]` porte m = 0,8 dans son libellé. Un id propre pour 0,8 n’existe pas (les classes de `simulator-levers.json` ne sont pas des cibles de pastille).
21. **`[[calc:somme des cibles]]` invérifiable ; noms de fonctions non documentés (chiffres, moyenne) : appliqué.** Tous les `[[calc:…]]` réécrits avec ids et opérateurs explicites (somme des sept cibles = 29,4 ; 6,26 jours ; 19,4 %), mention « (montants 2025 et PLF 2027, dont l’AME au PLF 2027 : 1,2 milliard) » ajoutée ; note pour l’équipe mise à jour. Remarque : le validateur ne reconnaît pas les suffixes `__low` / `__high` dans les `calc` ; pour les fourchettes, l’id de la fourchette est utilisé.
22. **Arrondis (chiffres, faible) : appliqué (chapitre 7).** 13,2 jours, 25,3 milliards, 8,1 jours. Autres chapitres hors périmètre.

**Longueur.** Les ajouts demandés représentent environ 450 mots. Coupes compensatoires : phrase du calendrier de la vieillesse (85 jours, 811 €, conservée dans le visuel), comparaison européenne de l’étape 5 (reprise en une pastille à l’étape 10), tableau de conversion de l’étape 6 (une phrase), 551 € par habitant (étape 7), emprunt mensuel du ménage (étape 2), descriptions de « Pour aller plus loin », reformulations. Texte affiché mesuré par script : environ 2 360 mots, 2 500 avec les titres d’étape (2 160 avant la passe). Au-dessus de la cible d’environ 2 200 : à arbitrer (candidats à la coupe : bullet « Immigration » renvoyée à sa fiche, encadré de l’étape 4 raccourci, titres des étapes 8 et 9).

### Passe du 25 octobre 2026 : données et longueur

- **Placeholders.** Le chapitre ne contenait aucune pastille `[[fig-a-creer:…]]` ni bloc de données en attente : rien à remplacer. Aucun des ids nouveaux de la passe de données (seconde passe) n’était nécessaire ici.
- **Pastilles.** `python3 -I validate.py` : aucune erreur ni alerte sur ce chapitre ; toutes les pastilles `[[fig:…]]`, `[[yard:…]]` et tous les ids des `[[calc:…]]` se résolvent. Chaque valeur affichée a été comparée à `figures.json` et `yardsticks.json` (format français) et chaque calcul refait : jours = x / 4,6962 ; part du déficit = x / 151,6 ; par habitant = x × 1 000 / 68,998 ; ménage = x × 1,92. Aucun écart.
- **Pastilles ajoutées** pour des nombres affichés qui n’en avaient pas : `[[yard:maastricht_deficit_limit_pct]]` (3 %), `[[yard:household_monthly_income_eur]]` (3 000 €, paramètre), `[[yard:example_cut_eur_bn]]` (30 milliards).
- **Nombres retirés plutôt que sourcés** (absents de `figures.json`, voir points ouverts) : « 3,5 % du PIB » (cible de l’OTAN, désormais « nouvelle cible de dépense de l’OTAN ») ; « 2 % sur les patrimoines de plus de 100 millions d’euros » (taxe Zucman, désormais « impôt minimum sur les très grands patrimoines ») ; « 72,6 milliards » des opérateurs (retiré du texte pour la longueur, conservé dans le visuel).
- **Longueur.** Texte affiché (encadrés `>` hors pastilles, hors visuels, notes et pastilles source) mesuré par script : 2 321 mots avant, 2 149 après, titres d’étape compris (2 229 et 2 057 sans les titres) ; la liste « Pour aller plus loin » est comptée. Coupes : répétitions (objectifs redits, phrases d’introduction), précisions secondaires (rang par habitant des dépenses de pension, niveau de vie relatif des retraités, calcul de la DG Trésor en nombre de personnes, convention intermédiaire de l’immigration dans le texte, financement des opérateurs), mentions de source allongées dans les encadrés. Ces détails sont renvoyés à la nouvelle liste « Pour aller plus loin ».
- **Encadré ajouté à l’étape 5.** Le point ouvert de la passe précédente est traité : « Le meilleur contre-argument » reprend le §4.4 du fichier 20 (salaire différé, pauvreté des personnes âgées, quasi-équilibre selon la convention du COR) ; le solde du système de retraite passe de l’étape 6 à cet encadré. La réponse ne cite que des chiffres déjà affichés. La contribution d’équilibre de l’État (49,3 milliards, fichier 20 §4.4) n’est pas dans `figures.json` : non utilisée.
- **Visuels** condensés en un paragraphe par étape ; ids et règles inchangés. Durée de lecture visée corrigée (2 à 3 minutes était incompatible avec environ 2 000 mots).
- **Titre.** « Les choix » est conforme au plan (fichier 20, §2.1 : « Ch. 7 Les choix »).

### Passe précédente (25 octobre 2026) : chiffres, neutralité, français

- Chiffres vérifiés contre `figures.json` et `yardsticks.json` v1.0.0 ; corrections : base COFOG 2024 du calendrier de la vieillesse (85 jours, 26 mars) distinguée du chiffre COR 2025 ; année 2023 et seuil de pauvreté précisés ; âge légal (réforme de 2023) reformulé ; fourchettes Zucman séparées par source (promoteurs 3,2 à 5,3 jours, critiques 0,4 à 1,3 jour) ; CDHR présentée comme premier acompte ; cabinets de conseil ajoutés à la liste des cibles ; « 7,6 points de PIB ».
- Neutralité : multiplicateur nul de 2024 daté et sourcé ; étiquettes d’orientation pour Fipeco et l’Institut Montaigne ; orientation de l’étude critique de la taxe Zucman nommée ; formulation factuelle pour la décision relative aux ressources propres ; contre-arguments symétriques à l’étape 10.
- Français : termes du glossaire (« multiplicateur budgétaire », « zone euro dans son ensemble », « âge légal de départ », sigles développés) ; espaces insécables laissées au filtre typographique (glossaire §2.1).

### Points ouverts

- **`yardsticks.json` (propriétaire des données)** : `gap_to_3pct_eur_bn.display_decimals` 0 → 1, pour aligner le validateur sur D-rounding (« 61,9 milliards »).
- **Ids encore absents de `figures.json`**, à créer avant tout affichage chiffré : `pensions_cor_2045f_pct_gdp` (14,2), `pensions_cor_2070f_pct_gdp` (15,3), `pension_resources_2025_pct_gdp` (13,9) et `pension_resources_2070f_pct_gdp` (12,9) (COR, juin 2026) ; variation de la productivité horaire de 2019 à 2025 (−0,8 %) ; `antifraud_2026_announced_eur_bn` (1,5, HCFP) ; pyramide des âges et taux d’emploi des 60-64 ans.
- **`zucman_critics_eur_bn`** : le champ `source` ne cite que l’étude Andrews et le CAE ; le texte nomme aussi le Sénat (2 à 3 milliards) et sept économistes dont P. Aghion (environ 5), tous deux dans le fichier 07 ; le fichier 10 (K14) attribue la fourchette 2-6 à F. Geerolf (octobre 2026). Harmoniser la source.
- **`cdhr_observed_2025_eur_bn`** : la note donne « 0,65-0,7 » milliard prévu pour 2026, alors que le fichier 07 a été corrigé en 0,7 : à mettre à jour dans `figures.json` (le chiffre n’est plus affiché ici).
- **Étiquette de Fipeco** : « site indépendant » n’est pas l’auto-description de Fipeco ; libellé conservé (D-labels), à revoir par le propriétaire du glossaire.
- **Validateur** : l’étiquette de Fipeco contient « Cour des comptes » ; sur une page où Fipeco serait cité avant la Cour, la Cour serait comptée sans étiquette. Sans effet ici (la Cour est étiquetée à l’étape 1).
- Les âges (60, 62, 64, 65 ans) et les durées (40 années, 45 annuités) restent sans pastille : ce sont des paramètres de politique, pas des statistiques. Les paramètres de la taxe Zucman et la cible de l’OTAN sont à ajouter comme paramètres si l’équipe veut les réafficher.
- Les fiches thématiques citées dans « Pour aller plus loin » doivent exister avec ces intitulés ; adapter les liens à l’architecture finale.
