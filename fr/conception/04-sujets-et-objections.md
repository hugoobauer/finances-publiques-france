# Conception du site, étape 4 : sujets et réponses « Oui, mais… »

*Document de travail, 31 octobre 2026. Il établit l'inventaire des pages de sujet et des pages de réponse définies dans `01-parcours-et-architecture.md` (§4, §7, §8). Il s'appuie sur les fichiers de recherche 07, 08, 11 et 16, sur `platform/data/` (`figures.json`, `proposals.json`, `simulator-levers.json`, `yardsticks.json`), sur `fr/site/debats.md` et sur le prototype « retraites ». Il ne contient aucun chiffre nouveau : quand un identifiant manque, la case dit « à chiffrer ».*

## 1. Comment lire ce document

**Ce qu'il fournit.** Pour 12 sujets (les 10 prévus et 2 ajoutés, voir §7) : le fait en tête, l'unité principale, la comparaison « Et ailleurs ? » disponible ou manquante, puis 6 à 8 cartes « Oui, mais… » avec leur montant, les identifiants de chiffres, les points « Débats » qui nourrissent la réponse et les lacunes. Il se termine par les réponses qui servent plusieurs sujets (§4), les 15 premières pages de réponse à rédiger (§5), les chiffres à verser dans les données (§6) et les points à trancher (§7).

**Règles appliquées.**

1. **Déficit de référence : 151,6 Md€** (déficit 2025 notifié à Eurostat, `deficit_2025_eur_bn`). Part du déficit = montant ÷ 151,6, arrondie à 0,1 point. Les chiffres de 2026 et 2027 restent dans le simulateur.
2. **Ordre des cartes (décision du 31 octobre 2026) :** par montant décroissant, puis les cartes sans montant par ordre alphabétique. Précisions retenues pour que l'ordre soit vérifiable : (a) pour une fourchette, on trie sur le **milieu** de la fourchette affichée (révisé le 31 octobre 2026 : la borne haute faisait remonter les fourchettes très larges) ; (b) à égalité, ordre alphabétique de la phrase (sans accents, ponctuation ni guillemets) ; (c) le montant est celui de l'effet annuel de la mesure que la phrase réclame ; une phrase qui ne réclame aucune mesure (un constat, une comparaison, un solde) n'a pas de montant, sauf quand le constat a lui-même une valeur en euros (hausse des intérêts, hausse de la dépense depuis 2019). Les tableaux ci-dessous sont déjà dans cet ordre.
3. **Nature du montant**, toujours écrite : *rendement* (recette ou économie), *coût*, *réservoir* (« réservoir, pas économie garantie » : jamais additionné à un rendement), *annoncé* (chiffre d'un parti, non vérifié), *estimé*, *constat*, *illustratif* (calcul de la plateforme). Les montants « cumulés sur cinq ans » (plans LR, par exemple) ne sont **pas** comparés au déficit annuel : la case le dit.
4. **Aucune étiquette de camp.** Aucune carte ni aucune phrase ne rattache une idée à un camp (décision du 31 octobre 2026). Les phrases sont écrites comme on les entend. La diversité des sensibilités dont viennent les cartes d'un même sujet a été vérifiée à part et n'est consignée nulle part. Les organismes cités gardent l'étiquette du glossaire §1.13, à poser à leur première mention sur chaque page rédigée : Institut Montaigne (libéral-centriste) ; Fondation iFRAP (libérale) ; Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire) ; Rexecode (institut de conjoncture proche des organisations patronales) ; IPP (institut de recherche académique) ; Cour des comptes (juridiction financière). Les partis sont nommés sans étiquette, leurs chiffres sont « annoncés ».
5. **Identifiants.** Les noms entre accents graves sont des identifiants de `figures.json`, sauf mention : `proposals` (`proposals.json`), levier `S1`, `R9`, etc. (`simulator-levers.json`), étalon (`yardsticks.json`). « Débats 2.6 » renvoie au point 2.6 de `fr/site/debats.md`. Le nom entre parenthèses de chaque carte est l'identifiant provisoire (slug) de la page de réponse.
6. **Rang après la mesure** (fichier 01, §6) : il est annoncé « calculable » seulement quand la série par pays existe déjà dans la base ou dans les fichiers de recherche.

## 2. Vue d'ensemble

| # | Sujet | Unité principale | Cartes (avec montant) | « Et ailleurs ? » | Principale lacune |
|---|---|---|---|---|---|
| 1 | [Retraites](#sujet-1) | Part de la dépense | 8 (5) | Oui, en partie (UE par habitant, pauvreté des aînés) ; monde à chiffrer | âge effectif et taux de remplacement |
| 2 | [Santé](#sujet-2) | Part de la dépense | 8 (5) | Écart ZE21 et espérance de vie ; reste dans le fichier 12 sans identifiant | versement des chiffres du fichier 12 |
| 3 | [École et enseignement](#sujet-3) | Part de la dépense | 7 (1) | PISA seulement ; dépense par élève à chiffrer | aucune mesure chiffrée (sauf salaires) |
| 4 | [Chômage et minima sociaux](#sujet-4) | Part de la dépense | 8 (6) | Emploi et pauvreté ; indemnisation à chiffrer | indemnisation UE, 1re, à verser |
| 5 | [Fonction publique](#sujet-5) | Part de la dépense | 7 (5) | Oui (zone euro, OCDE) ; PPS et périmètre égal à chiffrer | comparaison à périmètre égal |
| 6 | [Impôts et cotisations](#sujet-6) | Part du PIB (à trancher) | 8 (5) | Oui, la meilleure (OCDE, monde) ; rang après mesure calculable | structure fiscale comparée |
| 7 | [Déficit et dette](#sujet-7) | Jours de dépense | 8 (5) | Dette oui ; déficit et monde à chiffrer | rang du déficit, hors Europe |
| 8 | [Intérêts de la dette](#sujet-8) | Part de la dépense | 7 (2) | Taux et notation ; charge d'intérêts comparée à chiffrer | deux cartes sans source |
| 9 | [Aides aux entreprises](#sujet-9) | Part de la dépense | 8 (6) | Non | aucun comparateur |
| 10 | [Immigration](#sujet-10) | Part du PIB | 6 (2) | Rang OCDE ; rangs UE et panel à chiffrer | données 2006-2018 |
| 11 | [Prix, énergie et pouvoir d'achat](#sujet-11) | Part du déficit (à trancher) | 7 (7) | Non | aucun chiffre du sujet dans figures.json |
| 12 | [Train de vie de l'État et « économies faciles »](#sujet-12) | Part du déficit | 7 (6) | Aide au développement et contribution UE | audiovisuel et associations à comparer |

**Lecture.** 89 cartes au total. Les sujets 1, 6, 7 et 12 sont prêts pour la rédaction ; les sujets 3, 8, 9, 10 et 11 demandent d'abord des chiffres ou des sources (§6).

## 3. Fiches de sujet

<a id="sujet-1"></a>
### Sujet 1 : Retraites (`retraites`)

**Le fait en tête.** Les retraites sont le premier poste de la dépense publique : 422,2 Md€ en 2025, soit 24,3 € sur 100 € de dépense (14,1 % du PIB).  
*Identifiants :* `pensions_cor_2025_eur_bn`, `pensions_cor_2025_pct_te`, `pensions_cor_2025_pct_gdp`.

**Unité principale.** Part de la dépense publique (« près d'un euro sur quatre »). Calendrier : environ 90 jours avec le périmètre du COR (422,2 ÷ 4,70), 85,4 jours avec la COFOG (`calendar_days_old_age`) ; **choisir une seule convention** (point 7.3).

**« Et ailleurs ? » disponible.** Dépense de pensions par habitant en SPA : 5 940, 5e sur 27 (`pension_exp_per_capita_pps_2024`, `pension_exp_per_capita_pps_2024_rank`). Part de l'écart de dépense avec la ZE21 due à la vieillesse : 2,5 points sur 7,8, soit 32 % (`gap2024_old_age_pp`, `gap2024_old_age_share`). Pauvreté des 65 ans et plus, OCDE, seuil de 50 % : 6,1 % contre 14,8 % en moyenne OCDE (`old_age_poverty_oecd_2022_pct`, `oecd_old_age_poverty_2022_pct`). Dépense sociale nette totale : 2e de l'OCDE (`socx_net_total_2021_rank`).

**« Et ailleurs ? » manquant.** La dépense de vieillesse en % du PIB avec moyenne UE et rang (valeurs dans le fichier 09, sans identifiant) : à chiffrer. Âge effectif de départ, taux de remplacement et dépense de retraite des pays de l'OCDE et du reste du monde (OCDE, *Pensions at a Glance* ; OIT) : à chiffrer, aucune donnée dans la base. Rang après la mesure : calculable pour la dépense en % du PIB dès que la série COFOG 10.2 est versée ; le retour à 60 ans ajouterait 1,4 à 1,9 point de PIB (`return_60_general_cost_pct_gdp`).

**Pour aller plus loin.** chapitre 2 (où va l'argent), chapitre 7 (les choix).

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Revenons à la retraite à 60 ans » (`retraite-60`) | 43 à 58 Md€ (28,4 à 38,3 % du déficit) ; coût | `return_60_general_cost_eur_bn`, `return_60_general_cost_pct_gdp` (1,4 à 1,9 point), `return_60_partial_cost_eur_bn` (versions partielles : 26 à 35) ; proposals : `retirement_60_general_nfp`, `retirement_60_partial_rn_2024`, `lfi_retirement_60_40` | 2.6, 2.7, 2.8 | 43 et 58 viennent de deux périmètres (Fipeco, Institut Montaigne) ; aucun chiffrage indépendant des programmes 2027 ; fourchette large pour la version LFI (36 à 112,8) à expliquer |
| 2 | « Faisons payer les plus riches, pas les retraités » (`taxer-riches`) | 10 à 25 Md€ (6,6 à 16,5 % du déficit) ; rendement après réactions des contribuables, calcul de la plateforme | `tax_rich_package_eur_bn` | 2.8, 3.8, 3.9, 3.14 | synthèse propre à la plateforme (illustratif) ; risque juridique de la taxe Zucman ; voir aussi la page « taxer les plus riches » (sujet Impôts) |
| 3 | « Il faut reculer l'âge de départ à 65 ans » (`age-65`) | 9 à 19 Md€ (5,9 à 12,5 % du déficit) ; rendement à terme (10 à 20 ans) | levier `S1`, position 65 (+0,3 à +0,65 point de PIB) ; annoncé : `horizons_pensions_45y_65` (30 par an à effet plein), `lr_pensions` (42 cumulés sur 5 ans, non comparables) | 2.3, 2.5, 2.7, 2.8, 7.1 | valeur du levier S1 sans identifiant `figures.json` : à verser ; les modèles ne s'accordent pas sur l'effet d'un recul de l'âge sur la croissance (Débats 2.8) |
| 4 | « Abrogeons la réforme de 2023 (retour à 62 ans) » (`abrogation-2023`) | 6 à 17 Md€ (4,0 à 11,2 % du déficit) ; coût : 6 à 9 en 2027 (annoncé LFI : 9), 10 à 17 à effet plein | `repeal_2023_reform_lfi`, `rn_back_to_62`, `rn_2026_pension_plan_cost_eur_bn` (annoncé RN : 9), `pension_suspension` (suspension en vigueur : 1,9 en 2027), levier `S1` position 62 | 2.6, 2.7 | les deux horizons (2027 et effet plein) ne se mélangent pas dans une barre : une barre par horizon ; chiffre RN jugé trop bas par l'Institut Montaigne (Débats 2.7) |
| 5 | « Les retraités ont un niveau de vie élevé, ils peuvent contribuer » (`retraites-contribution`) | 4,1 à 5,7 Md€ (2,7 à 3,8 % du déficit) ; rendement : 4,1 (sous-indexation PLFSS 2027), 4,4 à 5,7 (année blanche, périmètre plus large) | `pension_indexation_plfss2027_eur_bn`, `annee_blanche_eur_bn` ; levier `R10` (plafonner l'abattement de 10 % : 1,4) | 2.9, 6.5 | niveau de vie : 100,2 % de la moyenne (`retirees_relative_living_standard_pct`), plus haut avec les loyers imputés ; l'année blanche gèle aussi prestations et barème (IPP : régressive) |
| 6 | « C'est un choix de société, et la dépense reste stable » (`retraites-choix-de-societe`) | sans montant de mesure | `pensions_cor_2045f_pct_gdp` (14,2 %), `pensions_cor_2070f_pct_gdp` (15,3 %), `pension_resources_2025_pct_gdp`, `pension_resources_2070f_pct_gdp` | 2.3, 2.5, 2.8 | projections du COR, scénario de référence ; le coût du choix en prélèvements n'a pas d'identifiant : à chiffrer |
| 7 | « Le régime des fonctionnaires cache un déficit » (`retraites-fonctionnaires`) | sans montant de mesure ; contribution d'équilibre de l'État : 49,3 Md€ | `pension_state_balancing_contribution_2025_eur_bn` | 2.4 | convention de comptage, pas une économie (le CAE parle d'une dépense surévaluée) ; ne pas convertir en part du déficit |
| 8 | « Le système de retraite est presque à l'équilibre » (`retraites-equilibre`) | sans montant de mesure ; solde du système : −5,1 Md€, soit −0,2 % du PIB | `pension_balance_2025_eur_bn`, `pension_balance_2025_pct_gdp`, `pension_balance_convention_range_pct_gdp` (déficit de 0,2 à 1,9 % du PIB selon la convention) | 2.4, 2.5 | le chiffre dépend de la convention sur la contribution de l'État employeur (49,3 Md€) ; ne pas convertir le solde en « part du déficit » |

**Lacunes du sujet.** Aucun chiffrage indépendant des programmes retraites 2027 ; effet de l'âge sur l'emploi des seniors et sur la croissance ; capitalisation (aucune donnée) ; comparaison hors Europe.

<a id="sujet-2"></a>
### Sujet 2 : Santé (`sante`)

**Le fait en tête.** La santé pèse 261 Md€ en 2024 : 15,6 € sur 100 € de dépense publique (8,9 % du PIB).  
*Identifiants :* `cofog_health_2024_eur_bn`, `cofog_health_2024_pct_te`, `cofog_health_2024_pct_gdp` ; Ondam exécuté 2025 : `ondam_2025_eur_bn`.

**Unité principale.** Part de la dépense publique. Calendrier : 56,9 jours (`calendar_days_health`).

**« Et ailleurs ? » disponible.** Écart de dépense de santé avec la ZE21 : 1,5 point de PIB en COFOG, 1,06 en SHA (`gap2024_health_pp`, `gap2024_health_sha_pp`), soit 19 % de l'écart total (`gap2024_health_share`). Résultat : espérance de vie 83,0 ans contre 81,5 dans l'UE-27, 7e (`life_expectancy_2024_years`, `eu27_life_expectancy_2024_years`, `life_expectancy_2024_rank`).

**« Et ailleurs ? » manquant.** Santé en % du PIB avec rang UE et OCDE, dépense par habitant en SPA (8e sur 27), mortalité évitable et traitable (3e sur 27), restes à charge, délais d'accès, indicateur APL de l'accès au médecin : toutes les valeurs sont dans le fichier 12 mais sans identifiant : à chiffrer (verser en priorité). OCDE et reste du monde : *Health at a Glance* (fichier 12) ; hors OCDE : à chiffrer.

**Pour aller plus loin.** chapitre 2, chapitre 6 (ce que l'on obtient).

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Traquons les soins inutiles » (`sante-soins-inutiles`) | 22 Md€ (14,5 % du déficit) ; réservoir, pas économie garantie | `low_value_care_eur_bn` | 6.7, 8.11 | extrapolation de la Cour des comptes à partir de ratios de l'OCDE, non auditée ; aucune mesure précise ne permet de récupérer ce réservoir |
| 2 | « Il y a trop d'administration : deux assurances se superposent » (`sante-gestion`) | 6 Md€ (4,0 % du déficit) ; réservoir, pas économie garantie | `health_admin_gap_eur_bn` | 6.7, 8.11 | effet d'un regroupement des assurances (Assurance maladie et complémentaires) : à chiffrer, aucune source ouverte ; la moitié environ des frais vient des complémentaires |
| 3 | « Les hôpitaux manquent de moyens : augmentons l'Ondam » (`sante-ondam`) | 2,7 Md€ (1,8 % du déficit) ; coût d'un point d'Ondam en plus, calcul de la plateforme | levier `S5` (0,27 par 0,1 point), base `ondam_2026_eur_bn` | 6.6, 6.11 | aucune mesure de parti chiffrée dans la base ; résultat attendu d'un point de plus non documenté ; salaires hospitaliers (infirmières à 0,97 fois le salaire moyen, fichier 12) sans identifiant |
| 4 | « Coupons l'aide médicale de l'État (AME) » (`ame`) | 1,34 Md€ (0,9 % du déficit) ; plafond, si supprimée entièrement | `ame_2025_eur_bn`, `ame_beneficiaries_2025` ; proposals : `rn_ame_to_amu` (1,3 annoncé) | 8.7 | page partagée avec le sujet Immigration ; rapport Évin-Stefanini : dispositif jugé utile et maîtrisé |
| 5 | « Il faut des jours de carence et plus de contrôles sur les arrêts maladie » (`arrets-maladie`) | 0,17 Md€ (0,1 % du déficit) ; estimé pour deux jours de carence dans la fonction publique ; LR annonce 4 cumulés sur 5 ans (non comparable) | `horizons_waiting_days` ; `lr_sick_leave` | aucun point : à ouvrir | aucun chiffrage indépendant du plan LR ; montant total des indemnités journalières : à chiffrer |
| 6 | « Faisons payer davantage les patients » (`sante-reste-a-charge`) | sans montant de mesure | aucun | aucun point : à ouvrir | franchises, tickets modérateurs, déremboursements : à chiffrer, rien dans la base ; restes à charge parmi les plus bas de l'UE (fichier 12, sans identifiant) |
| 7 | « Il y a des déserts médicaux, l'accès se dégrade » (`sante-acces`) | sans montant de mesure | aucun (APL : 29 % de la population en 2024, fichier 12) | 6.6 | indicateur APL, délais d'attente et soins non satisfaits sans identifiant : à chiffrer ; le saut des soins non satisfaits en 2020 est en partie une rupture de série (ne pas écrire « multiplié par trois ») |
| 8 | « On dépense beaucoup pour des résultats moyens » (`sante-resultats`) | sans montant de mesure | `gap2024_health_pp`, `gap2024_health_sha_pp`, `life_expectancy_2024_years` | 6.1, 6.6, 6.11 | mortalité traitable, survie au cancer, délais : valeurs au fichier 12, sans identifiant ; le lien dépense-résultat n'est pas causal |

**Lacunes du sujet.** Verser les valeurs du fichier 12 (santé en % du PIB, par habitant en SPA, mortalité traitable, restes à charge, APL) ; aucune mesure de parti sur le reste à charge ; pas de point « Débats » sur les arrêts maladie.

<a id="sujet-3"></a>
### Sujet 3 : École et enseignement (`ecole`)

**Le fait en tête.** L'enseignement coûte 148,6 Md€ en 2024 : 8,9 € sur 100 € de dépense publique (5,1 % du PIB).  
*Identifiants :* `cofog_education_2024_eur_bn`, `cofog_education_2024_pct_te`, `cofog_education_2024_pct_gdp`.

**Unité principale.** Part de la dépense publique. Calendrier : 32,5 jours (`calendar_days_education`).

**« Et ailleurs ? » disponible.** Résultat : PISA 2025 en mathématiques, 458 contre 463 en moyenne OCDE, 29e de l'OCDE (`pisa_math_2025`, `oecd_pisa_math_2025`, `pisa_math_2025_rank`). Rapport des intérêts à l'enseignement : `interest_vs_education_pct` (44,2 %).

**« Et ailleurs ? » manquant.** Dépense d'enseignement en % du PIB (UE 4,7, 11e : fichier 09), dépense par élève (14 932 USD PPA contre 14 436 en moyenne OCDE, 16e sur 35 : fichier 13), PISA lecture et sciences, évolution depuis 2015 (−35 points en mathématiques), TIMSS et PIRLS : tout est dans les fichiers 09 et 13 sans identifiant : à chiffrer. Reste du monde : PISA couvre aussi des pays hors OCDE, non versés. Rang après la mesure : sans objet tant qu'aucune mesure n'est chiffrée.

**Pour aller plus loin.** chapitre 6, étape 6.

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Les enseignants sont mal payés, revalorisons-les » (`salaires-enseignants`) | 2,1 à 2,4 Md€ (1,4 à 1,6 % du déficit) ; coût de +1 % du point d'indice pour les trois versants (part de l'école : à chiffrer) | `index_point_plus1` | 6.8, 1.8 | écart de 17 % avec les pairs de l'OCDE pour un enseignant du primaire à dix ans d'ancienneté (CAE, sans identifiant) ; coût d'un rattrapage ciblé enseignants : à chiffrer |
| 2 | « Il faut plus de moyens pour l'école » (`ecole-moyens`) | sans montant de mesure | aucun | 6.8, 6.11 | aucune mesure chiffrée dans la base (taille des classes, dédoublements, tutorat) : à chiffrer ; c'est le plus gros trou du sujet |
| 3 | « Le niveau baisse » (`ecole-niveau`) | sans montant de mesure | `pisa_math_2025`, `oecd_pisa_math_2025`, `pisa_math_2025_rank` | 6.1, 6.8 | évolution depuis 2015, TIMSS, PIRLS : fichier 13, sans identifiant |
| 4 | « Le problème, c'est l'organisation, pas les moyens » (`ecole-organisation`) | sans montant de mesure | aucun | 6.8, 6.11 | écart public-privé de 29,4 Md€ en 2019 (Fondation iFRAP) sans identifiant ; le CAE juge efficaces les dépenses ciblées |
| 5 | « Les universités manquent d'argent » (`universites`) | sans montant de mesure | `operators_public_funding_eur_bn` (opérateurs en général) | aucun point : à ouvrir | subventions aux universités (12,9 Md€ au PLF 2027, fichier 16) sans identifiant : à chiffrer ; aucune comparaison internationale |
| 6 | « On dépense autant que les autres pour de moins bons résultats » (`ecole-efficacite`) | sans montant de mesure | `pisa_math_2025`, `oecd_pisa_math_2025` | 6.8, 6.11 | dépense par élève et lien dépense-score (la dépense explique environ 6 % des écarts de score) : fichier 13, sans identifiant |
| 7 | « On supprime des postes d'enseignants » (`ecole-postes`) | sans montant de mesure | aucun (PLF 2027 : −1 588 enseignants, fichier 13 §5) | aucun point : à ouvrir | schéma d'emplois du PLF 2027 sans identifiant ; lien avec la démographie scolaire non documenté |

**Lacunes du sujet.** Sujet le moins chiffré : une seule carte a un montant. À combler avant rédaction : coût de mesures ciblées (dédoublements, salaires), comparaison UE de la dépense par élève, page « Débats » sur l'école (un seul point aujourd'hui, 6.8).

<a id="sujet-4"></a>
### Sujet 4 : Chômage et minima sociaux (`chomage-minima`)

**Le fait en tête.** L'indemnisation du chômage pèse 2,9 € sur 100 € de dépense publique en 2024 ; le RSA et la prime d'activité 2,2 € ; la famille 4,0 €.  
*Identifiants :* `cofog_unemployment_2024_pct_te`, `cofog_rsa_prime_activite_2024_pct_te`, `cofog_family_2024_pct_te`.

**Unité principale.** Part de la dépense publique.

**« Et ailleurs ? » disponible.** Taux d'emploi des 15-64 ans : 69,3 % contre 71,0 % dans l'UE-27, 21e sur 27 (`employment_rate_2025_pct`, `eu27_employment_rate_2025_pct`, `employment_rate_2025_rank`). Heures travaillées par habitant : 666, dernier de l'UE (`hours_per_inhabitant_2025`, `hours_per_inhabitant_2025_rank`). Pauvreté après transferts : 16,3 %, comme l'UE-27, 11e (`arop_2025_pct`, `eu27_arop_2025_pct`, `arop_2025_rank`) ; baisse due aux transferts hors retraites : 10,2 points, 6e (`poverty_reduction_excl_pensions_2025_pp`, `poverty_reduction_excl_pensions_2025_rank`).

**« Et ailleurs ? » manquant.** Dépense d'indemnisation du chômage en % du PIB : la France est 1re de l'UE (fichier 02, §5.2), mais la valeur n'a pas d'identifiant : à chiffrer (verser en priorité, c'est la comparaison que le sujet appelle). Durée et taux de remplacement de l'indemnisation (OCDE) et reste du monde (OIT) : à chiffrer, aucune donnée. Exemple de « rang après la mesure » déjà décrit au fichier 01 (§6) : il suppose cette série.

**Pour aller plus loin.** chapitre 2, chapitre 6.

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Si l'on travaillait autant qu'en Allemagne, les comptes seraient rétablis » (`travailler-plus`) | 38 à 84 Md€ (25,1 à 55,4 % du déficit) ; recettes en plus ; scénario illustratif (38 en équivalents temps plein, 84 en effectifs) | `employment_germany_levies_eur_bn`, `employment_germany_levies_headcount_eur_bn` ; levier `G1` | 6.10 | note de la DG Trésor, « purement illustratif » ; ne dit pas comment créer ces emplois |
| 2 | « Garantissons un revenu aux jeunes » (`garantie-jeunes`) | 9,5 à 12,3 Md€ (6,3 à 8,1 % du déficit) ; coût (9,5 annoncé LFI, 12,3 estimé) | `youth_guarantee_lfi` | aucun point : à ouvrir | aucune comparaison internationale ; effet sur l'emploi des jeunes non documenté |
| 3 | « Les aides sociales coûtent trop cher, baissons-les de 10 % » (`aides-sociales-10pct`) | 9,98 Md€ (6,6 % du déficit) ; rendement illustratif : 10 % de 65,8 (famille) + 34,0 (pauvreté-exclusion), curseur du simulateur, pas une proposition de parti | `drees_family_benefits_2024_eur_bn`, `drees_poverty_exclusion_benefits_2024_eur_bn` ; levier `S8` | 8.1, 6.3 | la famille est en tête des dépenses que les Français citent comme à réduire (34 %, Débats 8.1) : prévoir un sujet « Famille » (point 7.1) ; effets sur la pauvreté non chiffrés |
| 4 | « Alignons l'assurance chômage sur les standards européens » (`assurance-chomage`) | 5 Md€ (3,3 % du déficit) ; annoncé (Renaissance, annuel) ; LR annonce 30 cumulés sur 5 ans avec le plafond des aides à 70 % du SMIC (non comparable) | `re_unemployment`, `lr_unemployment` | aucun point : à ouvrir | aucun chiffrage indépendant ; la comparaison européenne de l'indemnisation est la donnée manquante |
| 5 | « Abrogeons les réformes de l'assurance chômage » (`assurance-chomage-abrogation`) | 3 Md€ (2,0 % du déficit) ; coût annoncé (LFI) | `unemployment_repeal_lfi` | aucun point : à ouvrir | aucun chiffrage indépendant |
| 6 | « Luttons d'abord contre la fraude sociale » (`fraude`) | 1 à 3 Md€ (0,7 à 2,0 % du déficit) ; rendement réaliste d'un nouveau plan antifraude (fiscal et social) ; pertes estimées : 14 | `antifraud_marginal_yield_eur_bn`, `social_fraud_hcfips_dec2025_eur_bn` (14), `social_fraud_contributions_eur_bn`, `social_fraud_benefits_eur_bn` | 8.4, 8.5, 8.6 | les pertes ne sont pas un montant récupérable ; la mesure antifraude du budget 2026 a été jugée non crédible par le HCFP ; page partagée avec Impôts (fraude fiscale) |
| 7 | « La pauvreté augmente malgré les aides » (`pauvrete-hausse`) | sans montant de mesure | `arop_2015_pct`, `arop_2025_pct`, `poverty_national_2024_pct` | 6.2, 6.3 | ruptures de série Eurostat en 2020 et 2022, effet non chiffré |
| 8 | « Le chômage ne coûte pas si cher » (`chomage-poids`) | sans montant de mesure | `cofog_unemployment_2024_pct_te` | 8.1, 6.10 | montant de l'indemnisation en Md€ (45,6 en 2024, fichier 02) sans identifiant : à chiffrer |

**Lacunes du sujet.** Comparaison UE de l'indemnisation (fichier 02) à verser ; aucun point « Débats » sur l'assurance chômage ni la garantie jeunes ; pas de donnée OCDE sur la durée d'indemnisation.

<a id="sujet-5"></a>
### Sujet 5 : Fonction publique (`fonction-publique`)

**Le fait en tête.** La masse salariale publique brute représente 362,1 Md€ en 2024, soit 21,7 € sur 100 € de dépense publique ; la rémunération des agents publics pèse 12,4 % du PIB, contre 10,0 % dans la zone euro.  
*Identifiants :* `wage_bill_gross_2024_eur_bn`, `wage_bill_gross_2024_pct_te`, `compensation_employees_2025_pct_gdp`, `ea21_compensation_employees_2025_pct_gdp`.

**Unité principale.** Part de la dépense publique (21,7 %).

**« Et ailleurs ? » disponible.** Rémunération des agents publics en % du PIB : 12,4 contre 10,0 (ZE21) (`compensation_employees_2025_pct_gdp`, `ea21_compensation_employees_2025_pct_gdp`). Part de la fonction publique dans l'emploi : 19,8 % (DGAFP) et 20,7 % en définition OCDE (`civil_service_share_employment_2024_pct`, `gg_employment_share_oecd_pct`).

**« Et ailleurs ? » manquant.** Moyenne OCDE de l'emploi public (18,4 %, 8e sur 30) et comparaison par habitant en SPA (indice 117, 8e sur 27 ; coûts de production 108, 10e sur 27) : fichier 13, sans identifiant : à chiffrer. Comparaison à périmètre égal (emploi public, éducation et santé quel que soit l'employeur : France 5e sur 27) : fichier 13, à chiffrer ; elle change la conclusion et doit figurer sur la page. Rang après la mesure : calculable en emploi public dès qu'on chiffre le poids d'un millier de postes.

**Pour aller plus loin.** chapitre 1 (comparaison), chapitre 6.

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Augmentons les salaires des fonctionnaires de 10 % » (`point-indice-plus-10`) | 20 à 24 Md€ (13,2 à 15,8 % du déficit) ; coût (17 annoncé) | `index_point_plus10_lfi` | 1.8 | coût par versant à chiffrer ; page partagée avec École et Santé (enseignants, hospitaliers) |
| 2 | « La masse salariale publique doit contribuer à l'effort » (`masse-salariale-effort`) | 17,4 à 20 Md€ (11,5 à 13,2 % du déficit) ; rendement à l'horizon 2032 (part proportionnelle ; minimum) | `cour_wage_bill_share_2032_eur_bn`, `cour_wage_bill_minimum_2032_eur_bn` | 8.12, 1.8 | note structurelle de la Cour des comptes (septembre 2026) ; la Cour ne dit pas comment (postes, point d'indice, durée du travail) |
| 3 | « Ne remplaçons pas tous les départs en retraite » (`non-remplacement`) | 2,5 à 25,3 Md€ (1,6 à 16,7 % du déficit) ; rendement à l'horizon 2032 selon les variantes annoncées (RN, Renaissance, Horizons, LR), calcul de la plateforme (illustratif) | `lr_non_replacement_400k` (12,6 à 25,3 ; annoncé 25), `horizons_replace_2_of_3` (7,9 à 15,8), `re_100k_posts` (3,2 à 6,3 ; annoncé 7), `rn_posts_not_filled` (2,5 à 12,7) | 8.12, 7.3, 1.8 | calcul brut (coût moyen de 63 000 € par poste), la moitié si elle revient aux agents ; effets sur les services (école, hôpital exclus par certains plans) ; multiplicateur des dépenses de fonctionnement 0,5 à 1,1 (`multiplier_operating_spending_y1`) |
| 4 | « Gelons le point d'indice » (`point-indice-gel`) | 2,1 à 2,4 Md€ (1,4 à 1,6 % du déficit) ; rendement par point de point d'indice, trois versants | `index_point_plus1`, levier `S3` | 1.8 | effet sur l'attractivité et les recrutements non chiffré |
| 5 | « Il faut des jours de carence dans la fonction publique » (`arrets-maladie`) | 0,17 Md€ (0,1 % du déficit) ; estimé pour deux jours (Horizons) | `horizons_waiting_days` | aucun point : à ouvrir | page partagée avec Santé |
| 6 | « La France a trop de fonctionnaires » (`trop-de-fonctionnaires`) | sans montant de mesure | `civil_service_share_employment_2024_pct`, `gg_employment_share_oecd_pct`, `compensation_employees_2025_pct_gdp` | 1.8, 1.9, 6.10 | à périmètre égal (privé non lucratif, par exemple en Allemagne), l'écart se réduit nettement (fichier 13) : à chiffrer ; pas d'effet mécanique sur le déficit |
| 7 | « Les fonctionnaires sont mal payés, les services manquent de bras » (`services-manquent-de-moyens`) | sans montant de mesure | `compensation_employees_2025_pct_gdp` | 6.11, 6.9 | salaires relatifs par métier (infirmières, enseignants) sans identifiant ; justice : juges pour 100 000 habitants (`judges_per_100k_2022`, `cepej_median_judges_2022`) |

**Lacunes du sujet.** Effectifs par versant et évolution (fichier 04, non versés comme chiffres de sujet) ; coût moyen par agent (levier S4 non chiffré : « v2 »).

<a id="sujet-6"></a>
### Sujet 6 : Impôts et cotisations (`impots`)

**Le fait en tête.** Les prélèvements obligatoires représentent 1 305 Md€ en 2025, soit 43,6 % du PIB ; l'OCDE place la France 2e sur 36 en 2024.  
*Identifiants :* `po_2025_eur_bn`, `po_2025_pct_gdp`, `oecd_tax_to_gdp_2024_pct_gdp`, `oecd_tax_to_gdp_2024_rank`.

**Unité principale.** À trancher : la « part de la dépense publique » ne convient pas aux recettes. Proposition : part du PIB, avec la phrase-repère du fichier 01 (§5) ; les jours de dépense (1 305 ÷ 4,70, environ 278 jours) restent dans la pastille.

**« Et ailleurs ? » disponible.** Taux de prélèvement OCDE 2024 : 43,5 % contre 34,1 % en moyenne OCDE, 2e sur 36 derrière le Danemark à 45,2 % (`oecd_tax_to_gdp_2024_pct_gdp`, `oecd_avg_tax_to_gdp_2024_pct_gdp`, `denmark_tax_to_gdp_2024_pct_gdp`). Coin socio-fiscal du célibataire au salaire moyen : 47,2 %, 3e (`oecd_tax_wedge_single_2025_pct`, `oecd_tax_wedge_single_2025_rank`). Recettes par habitant en SPA : 9e de l'UE (`tax_revenue_per_capita_pps_2024_rank`). Meilleure couverture du composant « Et ailleurs ? » : l'OCDE couvre le reste du monde.

**« Et ailleurs ? » manquant.** Structure des prélèvements (impôts sur le capital, sur le patrimoine, sur la production) comparée à l'OCDE : fichier 07 §6.2 et fichier 05, sans identifiant : à chiffrer. **Rang après la mesure, déjà calculable :** un paquet de 10 à 25 Md€ ajouterait 0,3 à 0,8 point de PIB (÷ `gdp_2025_eur_bn`) ; sur la mesure OCDE (43,5 %) la France resterait 2e, derrière le Danemark à 45,2 % (calcul illustratif à faire valider).

**Pour aller plus loin.** chapitre 3 (qui paie), chapitre 4.

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Les baisses d'impôts depuis 2017 ont creusé le déficit » (`baisses-impots-2017`) | 62 Md€ (40,9 % du déficit) ; coût des mesures décidées de 2018 à 2023 (en 2023), pas leur effet total | `tax_cuts_2018_2023_eur_bn`, `tax_cuts_2018_2023_pts` (2,2 points), `po_change_2017_2024_pts` | 3.3, 3.4, 4.1 à 4.12 | le point de départ change la conclusion (2017 est un sommet : 45,3 % du PIB) ; Rexecode compte 36,7 de prélèvements nouveaux de 2024 à 2026 (`rexecode_levies_2024_2026_eur_bn`) ; page partagée avec Déficit |
| 2 | « Supprimons les niches fiscales » (`niches-fiscales`) | 22 à 91,8 Md€ (14,5 à 60,6 % du déficit) ; réservoir, pas rendement : 22 annoncé par LFI pour les niches « injustes », 91,8 coût total | `tax_expenditures_2025_eur_bn`, `tax_expenditures_count`, `niches_sociales_2025_eur_bn` ; `tax_expenditures_trim_lfi` ; levier `R9` | 3.15, 8.3 | chaque niche a un objectif et des bénéficiaires ; coût connu pour une partie seulement ; niches fiscales et sociales se recoupent avec les aides aux entreprises : ne pas additionner |
| 3 | « Il suffit de faire payer les plus riches » (`taxer-riches`) | 10 à 25 Md€ (6,6 à 16,5 % du déficit) ; rendement après réactions des contribuables, calcul de la plateforme | `tax_rich_package_eur_bn` ; `zucman_proponents_eur_bn` (15 à 25), `zucman_critics_eur_bn` (2 à 6), `cdhr_observed_2025_eur_bn` (0,4 contre 2 annoncé), `isf_repeal_mechanical_loss_eur_bn` (3 à 4,5) | 3.7 à 3.14 | page pivot avec sous-pages (Zucman, ISF-IFI, flat tax, successions, CDHR) ; risque juridique ; successions : estimation 9 à 19 à revérifier (Débats 3.12) |
| 4 | « Les impôts freinent l'activité, baissons-les (impôts de production) » (`baisse-impots-production`) | 17,1 Md€ (11,3 % du déficit) ; coût annoncé (RN : supprimer CFE, CVAE et C3S) | `abolish_local_business_taxes_rn` ; `lr_tax_cuts` (51 cumulés sur 5 ans) | 3.2, 4.12 | aucun chiffrage indépendant ; effet sur la croissance et l'emploi à chiffrer ; page partagée avec Aides aux entreprises |
| 5 | « Augmentons la TVA » (`tva-plus-1-point`) | 8,2 Md€ (5,4 % du déficit) ; rendement net d'un point, tous taux (13 brut) | `vat_1pt_net_eur_bn`, levier `R7` | 7.4 | impôt régressif (Insee) ; multiplicateur de la TVA : modèles divergents ; page partagée avec Déficit et Prix |
| 6 | « Le travail est trop taxé » (`travail-trop-taxe`) | sans montant de mesure | `oecd_tax_wedge_single_2025_pct`, `oecd_tax_wedge_single_2025_rank`, `employer_ssc_2024_pct_gdp` | 3.1, 3.2 | cotisations employeur comparées à l'UE : à chiffrer ; le coin socio-fiscal finance des prestations (retraites, santé) |
| 7 | « Les milliardaires paient moins d'impôts que les autres » (`milliardaires-taux-effectif`) | sans montant de mesure | `ipp_effective_rate_top01_2016_pct` (46), `ipp_effective_rate_billionaires_2016_pct` (26), `geerolf_rate_billionaires_homogeneous_pct`, `geerolf_rate_top10_threshold_pct` | 3.7 | méthode contestée (bénéfices non distribués) ; données 2016 ; sous-page de « taxer les plus riches » |
| 8 | « Une minorité paie pour tout le monde » (`minorite-paie`) | sans montant de mesure | `ir_households_paying_pct` (47,2 %), `top10_share_levies_2023_pct` (33,3 %), `levies_share_income_d1_2022_pct`, `levies_share_income_d10_2022_pct` | 3.5, 3.6, 6.4 | la part dépend de ce que l'on compte (avec ou sans TVA) ; 47,2 apparaît aussi comme coin socio-fiscal : exemption de lint déjà en place |

**Lacunes du sujet.** Structure fiscale comparée à l'OCDE (fichier 05) à verser ; successions : estimation à revérifier ; pas de chiffrage indépendant des baisses d'impôts annoncées.

<a id="sujet-7"></a>
### Sujet 7 : Déficit et dette (`deficit-dette`)

**Le fait en tête.** En 2025, les administrations publiques ont dépensé 151,6 Md€ de plus qu'elles n'ont encaissé : 8,8 % de la dépense, soit environ 32 jours de dépense publique, financés par l'emprunt.  
*Identifiants :* `deficit_2025_eur_bn`, `deficit_2025_pct_gdp`, `share_te_borrowed_2025_pct` ; étalons `deficit_days`, `borrowing_starts_day` ; dette fin 2025 : `debt_2025_eur_bn`, `debt_2025_pct_gdp`.

**Unité principale.** Jours de dépense publique (calendrier, « à partir du 29 novembre ») ; page de réponse : part du déficit.

**« Et ailleurs ? » disponible.** Dette : 115,7 % du PIB contre 87,3 % dans la ZE21, soit 28,4 points d'écart (2,0 points sous la ZE21 en 2005) ; 3e de l'UE (`debt_2025_pct_gdp`, `ea21_debt_2025_pct_gdp`, `debt_gap_ea21_2025_pp`, `debt_gap_ea21_2005_pp`, `debt_eu_rank_2025`). Dernier excédent : 1974 (`last_surplus_year`). Dette nette : `net_debt_2025_pct_gdp`.

**« Et ailleurs ? » manquant.** Rang du déficit 2025 (4e plus grand déficit de l'UE, fichier 09) et déficit moyen UE et ZE : à chiffrer. Dette et déficit hors Europe (FMI, OCDE) : à chiffrer, aucune donnée. Rang après la mesure : pour « revenir à 3 % », calculable avec la série Eurostat des déficits.

**Pour aller plus loin.** chapitre 4 (pourquoi le déficit), chapitre 5 (dette et intérêts).

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Stabilisons d'abord la dette » (`stabiliser-la-dette`) | 89,6 à 125 Md€ (59,1 à 82,5 % du déficit) ; effort à atteindre : 89,6 en 2025 (Cour des comptes) ; environ 125 d'ici 2032 (mission hébergée par l'IGF) | `debt_stabilizing_gap_2025_eur_bn`, `debt_stabilizing_gap_2025_pts`, `igf_adjustment_2032_eur_bn` ; étalon `gross_measures_goal_a_eur_bn` (avec bouclage) | 5.14, 5.15, 7.6 | un niveau, pas un montant à retrouver chaque année ; hypothèses de croissance ; l'IGF suppose un multiplicateur nul, jugé « très favorable » |
| 2 | « Revenons à 3 % de déficit tout de suite » (`revenir-a-3-pct`) | 61,9 à 94 Md€ (40,8 à 62,0 % du déficit) ; effort : 61,9 en statique, 94,0 avec effet sur l'activité (multiplicateur 0,6) | étalons `gap_to_3pct_eur_bn`, `gross_measures_goal_b_eur_bn` ; `multiplier_mixed_y1` | 7.1, 7.2, 7.7 | calcul de la plateforme (illustratif) sur la base 2025 ; étaler ou concentrer l'effort : désaccord (Débats 7.7) |
| 3 | « C'est la faute des baisses d'impôts » (`baisses-impots-2017`) | 62 Md€ (40,9 % du déficit) ; coût des mesures décidées de 2018 à 2023, pas leur effet total | `tax_cuts_2018_2023_eur_bn` | 4.1 à 4.12 | même page que dans Impôts ; contre-lecture : la dépense (Débats 4.7) |
| 4 | « C'est la faute de la dépense, qui ne baisse pas » (`depenses-cliquet`) | 59,8 Md€ (39,4 % du déficit) ; constat : +2,0 points de PIB de 2019 à 2025, soit 12,7 jours ; conversion en euros à ajouter (2,0 × `one_point_gdp_eur_bn`) | `te_change_2019_2025_pp`, `total_revenue_change_2019_2025_pp`, `balance_change_2019_2025_pp` ; étalon `te_change_2019_2025_days` | 4.2, 4.7, 4.8, 4.9 | la période choisie change la conclusion (2017 ou 2019 : Débats 4.9) ; croissance faible et dépense en part de PIB (4.8) |
| 5 | « Il faudra dépenser plus pour la défense et le climat » (`besoins-defense-climat`) | 25 à 44 Md€ (16,5 à 29,0 % du déficit) ; coût : 25 à 34 par an pour le climat d'ici 2030 ; 44 par an pour la cible OTAN de 3,5 % en 2035 | `climate_public_need_eur_bn`, `nato_35_gap_eur_bn`, `lpm_2025_eur_bn`, `lpm_2027_eur_bn` | aucun point : à ouvrir | fichier 08 §8, aucune carte ni page de réponse encore ; sujet candidat (point 7.1) |
| 6 | « Les économies freinent la croissance : elles ne rapportent pas » (`multiplicateur`) | sans montant de mesure | `multiplier_mixed_y1` (0,6), `deficit_semi_elasticity`, étalons `macro_feedback_factor_mixed`, `example_cut_net_y1_eur_bn` (30 de baisse, 16,3 de gain net) | 7.1 à 7.8 | page transversale à lier depuis toutes les pages de réponse « combien ça rapporte » ; multiplicateur nul : hypothèse extrême (Débats 7.6) |
| 7 | « Tant que les taux sont bas, la dette ne coûte rien » (`taux-croissance-r-g`) | sans montant de mesure | `apparent_interest_rate_2025_pct`, `nominal_gdp_growth_2025_pct`, `r_minus_g_2025_pp`, `debt_stabilizing_primary_balance_2025_pct_gdp` | 5.12, 5.13 | r et g égaux en 2025 (écart estimé 0,1 point) ; page partagée avec Intérêts |
| 8 | « Un État, c'est comme un ménage : il faut rembourser sa dette » (`etat-comme-menage`) | sans montant de mesure | étalons `household_debt_eur`, `household_spending_month_eur`, `household_borrowing_month_eur`, `household_interest_month_eur` | 5.4, 5.1 | limites de la métaphore à toujours rappeler (un État ne part pas à la retraite, renouvelle sa dette, possède des biens) |

**Lacunes du sujet.** Déficit comparé (rang, moyennes) à verser ; aucune donnée hors Europe ; sujet « défense et climat » sans page Débats.

<a id="sujet-8"></a>
### Sujet 8 : Intérêts de la dette (`interets`)

**Le fait en tête.** Les administrations publiques ont payé 65,7 Md€ d'intérêts en 2025 (3,8 % de la dépense, 2,2 % du PIB) ; le gouvernement en prévoit environ 91 Md€ en 2027.  
*Identifiants :* `interest_2025_eur_bn`, `interest_2025_pct_te`, `interest_2025_pct_gdp`, `interest_2026f_eur_bn`, `interest_2027f_eur_bn` ; étalon `interest_rise_2025_2027_eur_bn` (25,3).

**Unité principale.** Part de la dépense publique (3,8 %) ; jours de dépense : 14 en 2025.

**« Et ailleurs ? » disponible.** Taux de l'OAT à 10 ans : 4,44 % en moyenne en septembre 2026, 5,126 % le 22 octobre ; écart avec le Bund : 97 pb en septembre, 169 pb le 22 octobre, contre un maximum mensuel de 154 pb en novembre 2011 (`oat10y_sep2026_pct`, `oat10y_22oct2026_pct`, `oat_bund_spread_sep2026_bp`, `oat_bund_spread_22oct2026_bp`, `oat_bund_spread_peak_nov2011_bp`). Notation : Aa3 (Moody's, perspective négative), A+ (S&P, Fitch) (`rating_moodys_oct2026_notches`, `rating_sp_oct2026_notches`, `rating_fitch_oct2026_notches`). Durée de vie moyenne de la dette de l'État : 8,4 ans (`avg_maturity_state_debt_2026_years`).

**« Et ailleurs ? » manquant.** Charge d'intérêts en % du PIB comparée à l'UE (2,0 % contre 1,9 %, 9e : fichier 09) : à chiffrer. Taux et écarts des autres pays (Italie, Espagne, Allemagne) et hors zone euro : à chiffrer, aucune donnée. **Le composant « rang après la mesure » ne s'applique pas** (on ne décide pas du montant des intérêts) ; le remplacer par la sensibilité aux taux : `interest_shock_100bp_y1_eur_bn` (3,4), `interest_shock_100bp_y2_eur_bn` (8,1).

**Pour aller plus loin.** chapitre 5 (dette et intérêts).

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Les intérêts vont grimper de 25 milliards en deux ans » (`interets-hausse`) | 25,3 Md€ (16,7 % du déficit) ; constat : hausse de 2025 à 2027, étalon commun à tous les camps | `interest_rise_2025_2027_eur_bn`, `interest_2026f_eur_bn`, `interest_2027f_eur_bn` ; `state_debt_charge_2025_eur_bn`, `state_debt_charge_2027_eur_bn` (périmètre de l'État) | 5.6, 5.7, 5.8 | deux périmètres (administrations publiques, 65,7 ; charge de la dette de l'État, 51,6) : écart de 14,1 (étalon `interest_concepts_gap_2025_eur_bn`) à expliquer ; la Cour prévoyait un peu moins pour 2026 |
| 2 | « Si les taux montent, on va être étranglés » (`taux-hausse`) | 3,4 à 8,1 Md€ (2,2 à 5,3 % du déficit) ; coût de +100 pb sur toutes les maturités : année 1 puis année 2 | `interest_shock_100bp_y1_eur_bn`, `interest_shock_100bp_y2_eur_bn`, `avg_maturity_state_debt_2026_years`, levier `G2` | 5.5, 5.9, 5.10 | l'effet continue de croître après l'année 2 ; lien entre instabilité politique et taux : phrase forte supprimée (Débats 5.10) |
| 3 | « Annulons ou renégocions la dette » (`annulation-dette`) | sans montant de mesure | aucun | aucun point : à ouvrir | aucune source ouverte dans la base ; carte à documenter (positions publiées, droit, effets) avant toute rédaction ; sinon la retirer |
| 4 | « La BCE n'a qu'à racheter la dette » (`bce-rachat-dette`) | sans montant de mesure | aucun | aucun point : à ouvrir | aucune source ouverte dans la base ; carte à documenter (BCE, Banque de France) avant rédaction ; sinon la retirer |
| 5 | « La dette ne coûte rien tant que r est inférieur à g » (`taux-croissance-r-g`) | sans montant de mesure | `apparent_interest_rate_2025_pct`, `nominal_gdp_growth_2025_pct`, `r_minus_g_2025_pp` | 5.12, 5.13 | même page que dans Déficit et dette ; thèse d'Olivier Blanchard (2019) et réserves de la DG Trésor |
| 6 | « La note de la France va encore se dégrader » (`notation`) | sans montant de mesure | `rating_moodys_oct2026_notches`, `rating_sp_oct2026_notches`, `rating_fitch_oct2026_notches` | 5.11 | notations 2023-2024 confirmées seulement par la presse : à vérifier sur les communiqués des agences avant affichage (STATUS §4.1) |
| 7 | « On paie des intérêts à des étrangers » (`dette-non-residents`) | sans montant de mesure | `nonresident_share_state_debt_2026q2_pct` (59,7 %), `nonresident_share_gg_securities_2026q2_pct` | aucun point : à ouvrir | part détenue par les non-résidents (fin T2 2026) ; répartition des intérêts par détenteur : à chiffrer (même lacune que la critique G2 du chapitre 4) |

**Lacunes du sujet.** Deux cartes sans aucune source (annulation, BCE) ; répartition des intérêts par détenteur ; comparaison internationale des charges d'intérêts.

<a id="sujet-9"></a>
### Sujet 9 : Aides aux entreprises (`aides-entreprises`)

**Le fait en tête.** Les aides publiques aux entreprises représentent de 45 à 211 Md€ en 2023 selon ce que l'on compte : il n'existe pas de définition légale.  
*Identifiants :* `business_aid_range_eur_bn`, `business_aid_hcsp_perimeter1_eur_bn` (82), `contribution_relief_general_eur_bn` (75).

**Unité principale.** Part de la dépense publique : de 2,6 % à 12,3 % (45 et 211 ÷ `te_2025_eur_bn`, calcul à ajouter aux étalons) ; les jours (10 à 45, Débats 3.16) restent dans la pastille.

**« Et ailleurs ? » disponible.** Affaires économiques (COFOG, y compris transports) : 9,9 % de la dépense publique en 2024 (`cofog_economic_affairs_2024_pct_te`). Cotisations sociales des employeurs : 10,0 % du PIB en 2024 (`employer_ssc_2024_pct_gdp`), sans comparateur.

**« Et ailleurs ? » manquant.** Aides d'État comparées à l'UE (tableau de bord des aides d'État de la Commission) et allègements de cotisations comparés : à chiffrer, aucune donnée ; COFOG 04 en % du PIB avec rang (5,7 %, 12e : fichier 09) : à chiffrer. Reste du monde : à chiffrer. Rang après la mesure : sans objet tant que le comparateur manque ; sujet à combler en priorité pour « Et ailleurs ? ».

**Pour aller plus loin.** chapitre 3, chapitre 7.

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Supprimons les cadeaux aux entreprises » (`aides-entreprises-supprimer`) | 45 à 211 Md€ (29,7 à 139,2 % du déficit) ; réservoir, pas rendement : de l'aide d'État au sens européen à la commission d'enquête du Sénat | `business_aid_range_eur_bn`, `business_aid_hcsp_perimeter1_eur_bn` | 3.16, 8.2 | aucune définition légale ; le haut de la fourchette compte surtout des baisses d'impôts et de cotisations et des prêts ; la part du déficit dépasse 100 % : rappeler que ce n'est pas une recette |
| 2 | « Supprimons les allègements de cotisations » (`allegements-cotisations`) | 48 à 75 Md€ (31,7 à 49,5 % du déficit) ; rendement : 75 brut, 48 net des effets sur l'emploi | `contribution_relief_general_eur_bn`, `contribution_relief_abolition_net_eur_bn`, `contribution_relief_abolition_jobs_fte` (−980 000 emplois) ; levier `R11` | 3.17, 8.3 | rapport Bozio-Wasmer : arrêter les baisses vers 2,5 SMIC à budget constant ; d'autres chiffrages d'emplois existent (ministre : 15 000 à 40 000, Débats 3.17) |
| 3 | « Réduisons les aides ciblées de 30 % » (`aides-ciblees-30pct`) | 24,6 Md€ (16,2 % du déficit) ; rendement maximal illustratif : 30 % de 82, curseur du simulateur | `business_aid_hcsp_perimeter1_eur_bn` ; levier `S7` | 3.16, 8.2 | aides ciblées peu évaluées ; effets sur l'investissement non chiffrés |
| 4 | « Baissons les impôts de production » (`baisse-impots-production`) | 17,1 Md€ (11,3 % du déficit) ; coût annoncé (RN : CFE, CVAE, C3S) | `abolish_local_business_taxes_rn` | 3.2, 4.12 | même page que dans Impôts ; aucun chiffrage indépendant |
| 5 | « Supprimons les niches des entreprises (CIR, Dutreil) » (`niches-fiscales`) | 1,3 à 22 Md€ (0,9 à 14,5 % du déficit) ; rendement : 1,3 estimé pour Dutreil de 75 % à 50 % ; 22 annoncé (LFI) pour l'ensemble des niches « injustes » | `dutreil_reform_eelv`, `tax_expenditures_trim_lfi`, `tax_expenditures_2025_eur_bn` | 3.15, 8.3 | même page que dans Impôts ; ne pas additionner avec les aides aux entreprises |
| 6 | « Taxons les superprofits et les grandes entreprises » (`superprofits`) | 5 à 8 Md€ (3,3 à 5,3 % du déficit) ; rendement : 8,0 observé en 2025 (surtaxe ponctuelle d'impôt sur les sociétés), 5 annoncé (LFI) | `cit_surtax_large_firms`, `windfall_tax_lfi`, `multinationals_tax_lfi`, `progressive_cit_lfi`, `cvae_restore_lfi` | aucun point : à ouvrir | aucun chiffrage indépendant des annonces ; surtaxe 2025 ponctuelle ; effet sur l'investissement non chiffré |
| 7 | « Il faut des contreparties et une évaluation des aides » (`aides-contreparties`) | sans montant de mesure | `business_aid_hcsp_perimeter1_eur_bn` | 3.16, 8.2 | état des évaluations (HCSP, Sénat) : à documenter ; aucun chiffre de mesure |
| 8 | « Les aides créent des emplois, n'y touchons pas » (`aides-emplois`) | sans montant de mesure | `contribution_relief_abolition_jobs_fte`, `bozio_wasmer_threshold_smic` | 3.17, 8.2 | l'effet des aides est contesté (fichier 08 §4.3), sans identifiant : à chiffrer |

**Lacunes du sujet.** Aucun comparateur international (aides d'État, allègements) ; peu d'évaluations chiffrées ; aucune carte n'a de rang après la mesure.

<a id="sujet-10"></a>
### Sujet 10 : Immigration (`immigration`)

**Le fait en tête.** Selon l'OCDE (moyenne 2006-2018), le solde budgétaire des personnes nées à l'étranger va d'un gain de 1,02 % du PIB par an à un coût de 0,85 %, selon la convention retenue.  
*Identifiants :* `immig_net_contrib_individual_pct_gdp` (+1,02), `immig_net_contrib_congestible_pct_gdp` (+0,25), `immig_net_contrib_all_public_goods_pct_gdp` (−0,85).

**Unité principale.** Part du PIB (la source l'exprime ainsi), avec la conversion en Md€ affichée comme illustration (1 point de PIB = `one_point_gdp_eur_bn`) ; part du déficit sur les pages de réponse.

**« Et ailleurs ? » disponible.** Rang de la France à l'OCDE pour la contribution nette (convention « tous biens publics ») : 21e sur 25 (`immig_net_contrib_rank`). La même étude couvre des pays hors Europe (OCDE).

**« Et ailleurs ? » manquant.** Rangs dans l'UE (16e sur 19) et dans le panel (7e sur 8), solde des natifs, gain d'un alignement de l'emploi des immigrés (+0,22 % du PIB) et part de la population née à l'étranger : fichier 15, sans identifiant : à chiffrer. Données antérieures à 2022 (moyenne 2006-2018) : le dire. Rang après la mesure : sans objet.

**Pour aller plus loin.** chapitre 7, étape sur les « économies faciles ».

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Faisons des économies sur l'immigration » (`immigration-economies`) | 15,1 Md€ (10,0 % du déficit) ; annoncé (RN, contre-budget 2027) ; 29,0 en 2031 ; LR annonce 10 cumulés sur 5 ans | `rn_immigration_2027`, `rn_immigration_2026` (11,9), `rn_immigration_2024` (8), `lr_immigration` | 8.7 | fragilité juridique (priorité nationale, référendum) ; aucun chiffrage indépendant ; 8 est la lecture de l'Institut Montaigne de l'annonce RN de 2024 ; fichier 15 : dépenses brutes de politique migratoire à ne pas confondre avec le solde net |
| 2 | « Supprimons l'aide médicale de l'État (AME) » (`ame`) | 1,34 Md€ (0,9 % du déficit) ; plafond, si supprimée entièrement | `ame_2025_eur_bn`, `ame_2025_pct_te`, `ame_beneficiaries_2025`, `ame_action_plf2027_eur_bn` ; `rn_ame_to_amu` (1,3 annoncé) | 8.7 | 0,3 jour de dépense ; rapport Évin-Stefanini : dispositif jugé utile et maîtrisé ; page partagée avec Santé et Train de vie |
| 3 | « Faisons travailler les immigrés » (`immigration-emploi`) | sans montant de mesure | aucun (fichier 15 : +0,22 % du PIB, soit environ 7 Md€, illustratif) | 6.10 | valeur sans identifiant : à chiffrer ; moyenne 2006-2018 |
| 4 | « La France accueille plus que ses voisins » (`immigration-comparaison`) | sans montant de mesure | aucun (fichier 15, série Eurostat des personnes nées à l'étranger) | aucun point : à ouvrir | part de la population née à l'étranger : à chiffrer ; rupture de série Insee en 2024 |
| 5 | « L'immigration rapporte plus qu'elle ne coûte » (`immigration-solde`) | sans montant de mesure | `immig_net_contrib_individual_pct_gdp`, `immig_net_contrib_congestible_pct_gdp`, `immig_net_contrib_all_public_goods_pct_gdp`, `immig_net_contrib_rank` | 8.7 | le résultat dépend de la façon de répartir la défense et les intérêts ; études statiques et études dynamiques divergent (fichier 15) ; enfants nés en France de parents immigrés : choix de comptage |
| 6 | « Réservons les prestations aux Français (« priorité nationale ») » (`priorite-nationale`) | sans montant de mesure | inclus dans `rn_immigration_2027` (composante non isolée) | 8.7 | part de la priorité nationale dans les 15,1 annoncés : à chiffrer ; risque constitutionnel |

**Lacunes du sujet.** Sujet le plus exposé au risque de lecture « partisane » : chaque carte reste un fait chiffré avec sa convention ; les données OCDE datent de 2006-2018 ; aucune donnée post-2022.

<a id="sujet-11"></a>
### Sujet 11 : Prix, énergie et pouvoir d'achat (`prix-pouvoir-achat`)

**Le fait en tête.** Les boucliers tarifaires de 2021 à 2024 ont coûté environ 72 Md€ bruts, 36 Md€ nets, sur quatre ans, et la Cour des comptes les juge peu ciblés.  
*Identifiants :* aucun dans `figures.json` ; données dans `proposals.json` : `energy_shields_2021_2024` (9 à 18 par an). Identifiants à créer..

**Unité principale.** Part du déficit annuel (la mesure est annuelle) ; page de sujet : à trancher, l'unité « part de la dépense publique » n'est pas naturelle ici.

**« Et ailleurs ? » disponible.** Aucune.

**« Et ailleurs ? » manquant.** Prix des carburants et de l'énergie, taux de TVA sur l'énergie, loyers : comparaison avec l'UE et le reste du monde entièrement à chiffrer (Eurostat, AIE). **Sujet nouveau**, absent de la liste du fichier 01 : il répond pourtant à la demande de départ (gel des prix des carburants ou des loyers).

**Pour aller plus loin.** chapitre 7 ; fichier 11 §6.

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Bloquons le prix du carburant à 1,70 € le litre » (`gel-prix-carburant`) | 12 à 26,5 Md€ (7,9 à 17,5 % du déficit) ; coût, estimation de la plateforme selon le prix du pétrole (4,6 par 0,10 € au-dessus de 1,70) | `fuel_freeze_lfi` | aucun point : à ouvrir | coût ouvert, fixé par le marché ; aucun chiffrage indépendant publié ; le HCFP cite les prix de l'énergie parmi les incertitudes |
| 2 | « Augmentons les salaires nets, baissons les prélèvements sur les salaires » (`baisse-prelevements-salaires`) | 15 Md€ (9,9 % du déficit) ; coût annoncé (PS-Place publique) | `ps_wage_levy_cut` | aucun point : à ouvrir | aucun chiffrage indépendant ; financement par les successions annoncé à 15 (`inheritance_package_ps`) |
| 3 | « Refaisons un bouclier tarifaire ou une remise sur le carburant » (`bouclier-remise`) | 7,5 à 18 Md€ (4,9 à 11,9 % du déficit) ; coût par an : 9 à 18 pour les boucliers 2021-2024 ; 7,5 pour la remise carburant 2022 (réalisés) | `energy_shields_2021_2024`, `fuel_rebate_2022` | aucun point : à ouvrir | mesures peu ciblées selon la Cour des comptes ; 4,5 de contributions sur les superprofits en 2021-2024 (fichier 11) |
| 4 | « Baissons la TVA sur l'énergie à 5,5 % » (`tva-energie`) | 11 à 12,2 Md€ (7,3 à 8,0 % du déficit) ; coût : 11 estimé (borne basse, Institut Montaigne), 12,2 annoncé (RN) | `energy_vat_rn` | aucun point : à ouvrir | la valeur de 17,4 d'un simulateur citoyen n'est pas retenue ; conflit possible avec le droit européen |
| 5 | « Mettons la TVA à 0 % sur 100 produits essentiels » (`tva-zero-essentiels`) | 3,5 Md€ (2,3 % du déficit) ; coût annoncé (RN) | `vat_100_products_rn` | aucun point : à ouvrir | aucun chiffrage indépendant ; liste des produits non précisée |
| 6 | « Portons le SMIC à 1 600 ou 1 700 € net » (`smic`) | 1,5 à 4 Md€ (1,0 à 2,6 % du déficit) ; coût pour les finances publiques seules | `smic_1700_lfi` (3,5 à 4), `smic_1600_nfp` (3,5), `smic_1600_ps` (1,8 à 2,2), `smic_2000_gross_eelv` (1,5 à 2) | aucun point : à ouvrir | coût pour les entreprises et effet sur l'emploi non chiffrés ; partiel : estimations de la plateforme à partir de l'Institut Montaigne 2024 |
| 7 | « Gelons ou encadrons les loyers » (`loyers`) | 0,2 Md€ (0,1 % du déficit) ; coût pour le budget ; le coût est ailleurs (offre, qualité, mobilité) | `rent_control` | aucun point : à ouvrir | étude IPP (note 125) : environ 0,6 transféré aux locataires ; littérature internationale sur les gels stricts : pertes d'offre |

**Lacunes du sujet.** Aucun chiffre du sujet dans `figures.json` ; aucun point « Débats » ; aucun comparateur. À traiter comme un sujet à part entière avant la rédaction.

<a id="sujet-12"></a>
### Sujet 12 : Train de vie de l'État et « économies faciles » (`train-de-vie`)

**Le fait en tête.** Les cibles les plus citées (contribution à l'UE, aide au développement, mission Pouvoirs publics, audiovisuel public, associations, AME, conseil) pèsent environ 29 Md€, même supprimées entièrement.  
*Identifiants :* somme déjà employée au chapitre 7 : `eu_net_contribution_2025_accounting_eur_bn` + `oda_mission_plf2027_eur_bn` + `pouvoirs_publics_mission_eur_bn` + `public_broadcasting_plf2027_eur_bn` + `state_payments_associations_2025_eur_bn` + `ame_action_plf2027_eur_bn` + `strategy_consulting_2025_eur_bn` = 29,4 (19,4 % du déficit).

**Unité principale.** Part du déficit (29,4 Md€ : 19,4 %).

**« Et ailleurs ? » disponible.** Aide au développement : 0,42 % du RNB, 11e du CAD (`oda_2025_pct_gni`, `oda_2025_rank`). Contribution nette à l'UE, en % du RNB : 4e (`eu_net_contribution_rank_pct_gni_2025`). Services publics généraux hors intérêts : 26,6 jours (`calendar_days_gps_excl_interest`).

**« Et ailleurs ? » manquant.** Audiovisuel public (COFOG 08.3, 0,26 % du PIB, 5e sur 27, contre 0,20 % dans l'UE : fichier 16) et subventions aux associations : à chiffrer. Reste du monde : l'aide au développement (CAD) est la seule comparaison disponible. Rang après la mesure : pour l'aide au développement, calculable avec la série CAD.

**Pour aller plus loin.** chapitre 7 (étape 10) ; fichier 16.

**Cartes « Oui, mais… »** (classées par montant, règle affichée sur la page).

| # | « Phrase entendue » (page de réponse) | Montant annuel et part du déficit 2025 | Identifiants | Débats | Lacunes et réserves |
|---|---|---|---|---|---|
| 1 | « Arrêtons de payer pour l'étranger : coupons l'aide au développement » (`aide-au-developpement`) | 3,17 à 12,9 Md€ (2,1 à 8,5 % du déficit) ; plafond : 3,17 de crédits budgétaires (PLF 2027), 12,9 au sens de l'OCDE (prêts, accueil de réfugiés et d'étudiants compris) | `oda_mission_plf2027_eur_bn`, `oda_2025_eur_bn`, `oda_2025_pct_gni`, `oda_2025_rank`, `cofog_foreign_econ_aid_2024_eur_bn` (4,9) | 8.9 | le PLF 2027 réduit déjà les crédits de 0,40 ; trois chiffres différents selon la définition |
| 2 | « Coupons dans les subventions aux associations » (`associations`) | 1,6 à 10,5 Md€ (1,1 à 6,9 % du déficit) ; plafond théorique : 10,5 de versements de l'État ; 1,6 pour une baisse de 10 % (Fondation iFRAP, annoncé, y compris collectivités) | `state_payments_associations_2025_eur_bn`, `ifrap_associations_10pct`, `lr_associations` (3 cumulés sur 5 ans) | 8.13 | la plupart des versements financent des politiques (sport, social, culture) ; aucun point « Débats » dédié |
| 3 | « Sortons de l'Union européenne ou plafonnons notre contribution » (`contribution-ue`) | 1,4 à 9,5 Md€ (0,9 à 6,3 % du déficit) ; contribution nette de 6,4 à 9,5 ; gain d'un plafond à 5 Md€ : 1,4 à 4,5 (11,1 annoncé par le RN) | `eu_net_contribution_2025_accounting_eur_bn`, `eu_net_contribution_2025_operating_eur_bn`, `eu_gross_levy_2025_eur_bn`, `eu_gross_levy_2027f_eur_bn`, `eu_spending_in_france_2025_eur_bn` (16,4) ; `rn_eu_cap` | 8.8 | plafond impossible sans accord à l'unanimité ; le prélèvement brut (30,9 en 2027) finance des aides qui reviennent en France ; « sortir de l'UE » n'est pas chiffré (hors périmètre) |
| 4 | « Supprimons les agences et les opérateurs inutiles » (`agences-operateurs`) | 0,54 à 7,5 Md€ (0,4 à 4,9 % du déficit) ; rendement : 0,54 (Sénat) ; 2,5 à 7,5 annoncés (gouvernement 2025, RN 3,4, LR 7,5) | `agencies_senate_saving_eur_bn`, `operators_public_funding_eur_bn` (72,6 de financements, réservoir non pertinent) ; `agencies_reform`, `rn_agencies`, `lr_agencies` | 8.12 | les 72,6 financent surtout universités, recherche, emploi, logement, pas des frais de structure ; ne pas afficher 72,6 comme gain |
| 5 | « Privatisons l'audiovisuel public » (`audiovisuel-public`) | 1,6 à 3,82 Md€ (1,1 à 2,5 % du déficit) ; plafond : 3,82 d'avances (PLF 2027) ; 1,6 annoncé par le RN | `public_broadcasting_plf2027_eur_bn` ; `rn_broadcasting_privatization` | aucun point : à ouvrir | faisabilité jugée incertaine (Institut Montaigne) ; comparaison internationale à chiffrer |
| 6 | « Réduisons le train de vie des ministères : cabinets, conseil, Pouvoirs publics » (`train-de-vie-ministeres`) | 0,06 à 1,16 Md€ (moins de 0,1 à 0,8 % du déficit) ; plafond : 1,16 pour la mission Pouvoirs publics ; 0,155 pour les cabinets ministériels ; 0,06 pour le conseil en stratégie | `pouvoirs_publics_mission_eur_bn`, `ministerial_cabinets_gross_pay_eur_bn`, `strategy_consulting_2025_eur_bn` | 8.10 | ensemble inférieur à 1 % du déficit ; le conseil est déjà largement réduit ; aucun point « Débats » sur les cabinets |
| 7 | « L'État vit au-dessus de ses moyens, son fonctionnement coûte trop cher » (`fonctionnement-etat`) | sans montant de mesure | `cofog_general_public_services_2024_pct_te`, `cofog_interest_2024_pct_te` ; étalon `calendar_days_gps_excl_interest` | 8.10 | le poste « services publics généraux » inclut recherche fondamentale et aide extérieure, pas le personnel administratif des hôpitaux et des écoles |

**Lacunes du sujet.** Sujet transversal aux deux pages-clés du prototype (« train de vie » et « AME ») ; aucun point « Débats » propre pour associations, audiovisuel et cabinets.

## 4. Réponses qui servent plusieurs sujets

Une page de réponse a une seule adresse (la page « principale »). Les autres sujets la montrent comme une carte, avec le même montant et le même texte d'une ligne ; la page de réponse renvoie vers tous les sujets qui la citent.

| Page de réponse (slug) | Sujets qui la montrent | Page principale | Montant commun | Remarque |
|---|---|---|---|---|
| `taxer-riches` (pivot avec sous-pages Zucman, ISF-IFI, flat tax, successions, CDHR, milliardaires) | Retraites, Impôts (aussi liée à Déficit et dette) | Impôts | 10 à 25 Md€ (`tax_rich_package_eur_bn`) | carte la plus citée du site ; première page à écrire |
| `fraude` (fiscale et sociale) | Chômage et minima, Impôts (fraude fiscale 30 à 130), Déficit et dette | Chômage et minima | 1 à 3 Md€ (`antifraud_marginal_yield_eur_bn`) | séparer pertes estimées (14 et 30 à 130) et rendement réaliste |
| `baisses-impots-2017` | Impôts, Déficit et dette | Impôts | 62 Md€ (`tax_cuts_2018_2023_eur_bn`) | la contre-lecture sur la dépense (`depenses-cliquet`) doit être visible sur la même page |
| `niches-fiscales` | Impôts, Aides aux entreprises | Impôts | 22 à 91,8 Md€ (réservoir) | ne pas additionner avec `aides-entreprises-supprimer` |
| `baisse-impots-production` | Impôts, Aides aux entreprises | Impôts | 17,1 Md€ annoncé | aucun chiffrage indépendant |
| `tva-plus-1-point` | Impôts, Déficit et dette, Prix | Impôts | 8,2 Md€ net par point | régressive |
| `ame` | Immigration, Santé, Train de vie | Immigration | 1,34 Md€ (`ame_2025_eur_bn`) | déjà prototypée |
| `non-remplacement` | Fonction publique, Train de vie (agences), Déficit et dette | Fonction publique | 2,5 à 25,3 Md€ (illustratif) | variantes de quatre programmes sur une même barre |
| `point-indice-plus-10` et `point-indice-gel` | Fonction publique, École, Santé | Fonction publique | 2,1 à 2,4 par point ; 20 à 24 pour +10 % | part École et part Santé à chiffrer |
| `arrets-maladie` | Santé, Fonction publique | Santé | 0,17 Md€ (carence dans la fonction publique) | plan LR en cumul sur 5 ans, non comparable |
| `travailler-plus` | Chômage et minima, Immigration, Retraites (âge) | Chômage et minima | 38 à 84 Md€ (illustratif) | lien avec `age-65` et `immigration-emploi` |
| `taux-croissance-r-g` | Déficit et dette, Intérêts | Déficit et dette | r − g = 0,1 point (`r_minus_g_2025_pp`) | thèse de Blanchard et réserves |
| `multiplicateur` | Toutes les pages « combien ça rapporte » | Déficit et dette | 0,6 (`multiplier_mixed_y1`) ; 30 de baisse donnent 16,3 de gain net | page transversale ; bloc réutilisable, pas seulement une carte |
| `revenir-a-3-pct` et `stabiliser-la-dette` | Déficit et dette, Intérêts | Déficit et dette | 61,9 à 94 ; 89,6 à 125 Md€ | deux objectifs à ne pas confondre |
| `etat-comme-menage` | Déficit et dette, Intérêts | Déficit et dette | étalons du ménage | limites de la métaphore à chaque fois |
| `aides-entreprises-supprimer` et `allegements-cotisations` | Aides aux entreprises, Impôts (« le travail est trop taxé ») | Aides aux entreprises | 45 à 211 ; 48 à 75 Md€ | `aides-emplois` tempère `allegements-cotisations` |
| `smic` | Prix et pouvoir d'achat, Chômage et minima | Prix | 1,8 à 4 Md€ | coût public seul |
| `age-65` et `abrogation-2023` | Retraites, Fonction publique (régime des agents de l'État) | Retraites | 9 à 19 ; 6 à 17 Md€ | horizons différents |
| `retraites-fonctionnaires` | Retraites, Fonction publique | Retraites | 49,3 Md€ (contribution d'équilibre, pas une économie) | convention de comptage |
| `besoins-defense-climat` | Déficit et dette (sujet candidat « Défense et climat », §7) | Déficit et dette | 25 à 44 Md€ | aucun point Débats |

## 5. Les 15 premières pages de réponse à écrire

**Critères, dans cet ordre :** (1) la promesse est l'une de celles qui ont motivé le projet ou l'une des plus entendues ; (2) les chiffres sont prêts (identifiants dans `figures.json`, point « Débats » rédigé) ; (3) la page sert plusieurs sujets (§4) ; (4) un levier du simulateur existe pour le bouton « Ajouter à mon budget » ; (5) l'ensemble reste équilibré : il couvre aussi bien des promesses de recettes que d'économies, sans qu'aucune sensibilité n'y domine (vérifié à part, non consigné).

| Rang | Page (slug) | Montant | Sujets servis | Prêt ? | Levier |
|---|---|---|---|---|---|
| 1 | « Il suffit de faire payer les plus riches » (`taxer-riches`) | 10 à 25 Md€ | Impôts, Retraites, Déficit | oui | R1 à R5 |
| 2 | « Revenons à la retraite à 60 ans » (`retraite-60`) | 43 à 58 Md€ | Retraites | oui | S1 |
| 3 | « Luttons contre la fraude » (`fraude`) | 1 à 3 Md€ réalistes | Chômage et minima, Impôts, Déficit | oui | R12 |
| 4 | « Réduisons le train de vie de l'État » (`train-de-vie-ministeres`, avec le total de 29,4 Md€) | 29,4 Md€ plafond | Train de vie, Déficit | oui, prototypée | S12 à S19 |
| 5 | « Supprimons les cadeaux aux entreprises » (`aides-entreprises-supprimer`) | 45 à 211 Md€ | Aides aux entreprises, Impôts | oui | S7, R11 |
| 6 | « Les baisses d'impôts depuis 2017 ont creusé le déficit » (`baisses-impots-2017`) | 62 Md€ | Impôts, Déficit | oui | aucun (constat) |
| 7 | « Ne remplaçons pas tous les départs en retraite » (`non-remplacement`) | 2,5 à 25,3 Md€ | Fonction publique, Train de vie | oui (illustratif) | S4 (non chiffré) |
| 8 | « Il faut reculer l'âge à 65 ans » (`age-65`) | 9 à 19 Md€ à terme | Retraites | à moitié : levier sans identifiant | S1 |
| 9 | « Coupons l'AME » (`ame`) | 1,34 Md€ | Immigration, Santé, Train de vie | oui, prototypée | S19 |
| 10 | « Bloquons le prix du carburant » et « Baissons la TVA sur l'énergie » (`gel-prix-carburant`, `tva-energie`) | 12 à 26,5 ; 11 à 12,2 Md€ | Prix | à moitié : pas d'identifiant ni de Débats | S9 |
| 11 | « Revenons à 3 % tout de suite » (`revenir-a-3-pct`) | 61,9 à 94 Md€ | Déficit, Intérêts | oui | objectif B du simulateur |
| 12 | « Les intérêts vont grimper de 25 milliards » (`interets-hausse`) | 25,3 Md€ (constat) | Intérêts, Déficit | oui | G2 |
| 13 | « Supprimons les niches fiscales » (`niches-fiscales`) | 22 à 91,8 Md€ (réservoir) | Impôts, Aides aux entreprises | oui | R9 |
| 14 | « Traquons les soins inutiles » (`sante-soins-inutiles`, avec `sante-gestion`) | 22 et 6 Md€ (réservoirs) | Santé | oui, comparaison à verser | S6 |
| 15 | « Le système de retraite est presque à l'équilibre » (`retraites-equilibre`) | −5,1 Md€ ; jusqu'à 1,9 % du PIB | Retraites | oui, prototypée | aucun (constat) |

**Ensuite (16 à 25, non classées) :** `travailler-plus`, `tva-plus-1-point`, `contribution-ue`, `aide-au-developpement`, `associations`, `agences-operateurs`, `allegements-cotisations`, `stabiliser-la-dette`, `taux-hausse`, `multiplicateur` (à écrire tôt, car toutes les pages s'y réfèrent).

**Remarque sur le rang 8 et le rang 10.** Ces deux pages passent avant d'autres parce qu'elles complètent des paires (60 ans et 65 ans ; carburant et TVA) ; leurs données incomplètes les retarderaient si l'on suivait le seul critère n° 2.

## 6. Chiffres à verser dans `figures.json` (par priorité)

Chaque ligne manque aujourd'hui d'identifiant et bloque une comparaison ou une carte. La source est déjà nommée dans le fichier de recherche indiqué ; la procédure est celle de `STATUS.md` §4.2 (fichier 00, puis `figures.json`, puis `validate.py`).

| Priorité | Chiffre à créer | Fichier | Débloque |
|---|---|---|---|
| 1 | Indemnisation du chômage en % du PIB, UE-27 et rang (SESPROS) | 02 §5.2 | sujet 4, comparaison phare |
| 1 | COFOG par fonction en % du PIB avec moyenne UE, rang et panel (vieillesse, santé, enseignement, affaires économiques, intérêts, culture) | 09 §3 | sujets 1, 2, 3, 8, 9, 12 |
| 1 | Santé : par habitant en SPA, mortalité traitable, restes à charge, indicateur APL | 12 §0 | sujet 2 |
| 1 | Chiffres du levier `S1` (âge de départ, positions 62, 63, 65) comme identifiants | 07, 03 | cartes `age-65`, `abrogation-2023` |
| 2 | Aides aux entreprises et allègements de cotisations comparés à l'UE (aides d'État) | 08 §4 | sujet 9 (aucun comparateur aujourd'hui) |
| 2 | Emploi public à périmètre égal (O+P+Q) et par habitant en SPA | 13 §2.4, §3 | sujet 5 |
| 2 | Dépense par élève, TIMSS, PIRLS, évolution PISA depuis 2015 | 13 §4 | sujet 3 |
| 2 | Boucliers tarifaires (72 bruts, 36 nets), remise carburant, prix de l'énergie comparés | 11 §6, 07 §3.5 | sujet 11 (aucun chiffre aujourd'hui) |
| 2 | Rang du déficit 2025 dans l'UE, déficit moyen UE et ZE | 09 §2 | sujet 7 |
| 3 | Part des personnes nées à l'étranger, rangs UE et panel, gain d'emploi de 0,22 % du PIB | 15 | sujet 10 |
| 3 | Charge d'intérêts comparée, taux des autres pays | 09, 18 | sujet 8 |
| 3 | Schéma d'emplois du PLF 2027 (enseignants), subventions aux universités | 13 §5, 16 | sujets 3 et 12 |
| 3 | Dette et déficit hors Europe (FMI, OCDE), prestations de retraite et durée d'indemnisation (OCDE, OIT) | aucun | « reste du monde » partout où il manque |

**Cartes sans aucune source dans la base** (à documenter avant rédaction, sinon à retirer) : `annulation-dette`, `bce-rachat-dette`. **Cartes sans point « Débats »** : les sept du sujet Prix, `arrets-maladie`, `sante-reste-a-charge`, `assurance-chomage`, `assurance-chomage-abrogation`, `garantie-jeunes`, `superprofits`, `audiovisuel-public`, `besoins-defense-climat`, `ecole-postes`, `universites`, `immigration-comparaison`, `dette-non-residents` : leur bloc « Qui dit quoi » est à constituer à partir de textes publiés ouverts (méthode de `debats.md`).

## 7. Ajustements proposés et points à trancher

### 7.1 Ajustements à la liste des sujets

1. **Deux sujets ajoutés.** « Prix, énergie et pouvoir d'achat » (gel des carburants et des loyers, TVA sur l'énergie, SMIC : promesses citées dès la demande de départ, absentes de la liste du fichier 01) et « Train de vie de l'État et économies faciles » (déjà prototypé par les cartes « train de vie » et « AME », et traité au chapitre 7). Cela fait 12 sujets.
2. **Candidats pour une version 2**, classés par intérêt : **Famille** (en tête des dépenses que les sondés citeraient pour des économies, 34 % ; `cofog_family_2024_pct_te`, `drees_family_benefits_2024_eur_bn` ; aujourd'hui une seule carte, dans Chômage et minima) ; **Défense et climat** (besoins nouveaux, 25 à 44 Md€) ; **Collectivités locales** (annonces RN 8,2 et LR 10 cumulés ; fichier 08 §5) ; **Logement** ; **Justice** (blocage du chapitre 6 jusqu'à la mise à jour CEPEJ de décembre 2026).
3. **« Aides aux entreprises » et « Impôts »** partagent trois pages (niches, impôts de production, allègements) ; si le partage gêne la navigation, fusionner les deux sujets en « Recettes et aides » au lieu de dupliquer les cartes.

### 7.2 Points à trancher

1. **Tri des fourchettes :** borne haute (retenue ici) ou milieu de la fourchette ? La borne haute place en tête les cartes dont la fourchette est la plus large (`aides-entreprises-supprimer`) ; le milieu serait plus stable mais demande un choix de « centre » pour les estimations qui n'en ont pas.
2. **Cartes dont le montant est un constat** (hausse des intérêts, hausse de la dépense depuis 2019) : les classer avec les mesures, comme ici, ou les mettre avec les cartes sans montant ?
3. **Unité des pages de sujet qui ne portent pas sur une dépense** (Impôts, Prix, Immigration) : la « part de la dépense publique » du fichier 01 (§5) ne convient pas ; proposition dans chaque fiche. Pour Retraites : une seule convention pour le calendrier (COR ou COFOG).
4. **Montants cumulés sur cinq ans** (plans LR, `lr_pensions`, `lr_unemployment`) : ne les comparer au déficit annuel qu'une fois ramenés à une année, avec la règle de montée en charge de `proposals.json` ; d'ici là, la carte n'affiche pas de part du déficit pour eux.
5. **Cartes aux données 2006-2018 ou 2016** (immigration, milliardaires) : afficher la date sur la carte elle-même, pas seulement sur la page.
6. **Cartes « à retirer si non documentées »** (`annulation-dette`, `bce-rachat-dette`) : décision à prendre après une recherche de sources publiées ; sans source, elles disparaissent plutôt que de recevoir une réponse non sourcée.
7. **Carte « on dépense plus pour de moins bons résultats »** (École, Santé) : le lien dépense-résultat n'étant pas causal (Débats 6.11), la réponse doit montrer les trois lectures du bilan, pas en choisir une.

*Aucun fichier de données n'a été modifié. Prochaine étape suggérée : verser les chiffres de priorité 1 du §6, puis rédiger les pages 1 à 5 du §5, puis maquetter la page de sujet « Retraites » avec les huit cartes ci-dessus.*
