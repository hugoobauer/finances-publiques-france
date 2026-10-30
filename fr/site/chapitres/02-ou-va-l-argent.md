# Chapitre 2. Où va l’argent ?

<!--
NOTES POUR L’ÉQUIPE (non affichées sur le site)

Statut : brouillon pour relecture éditoriale, rédigé le 25 octobre 2026 ; passe « pastilles et coupes » le 25 octobre 2026 ; passe « finalisation » le 25 octobre 2026 ; confrontation aux sources publiques le 30 octobre 2026.
Périmètre : calendrier de la dépense publique, répartition de 1 000 €, fonctions COFOG,
protection sociale par risque, poids des retraites et de la santé.
Entrées : research/20-pedagogical-approach.md (§2.1, §3.1-3.3, §4.2-4.5), platform/data/figures.json,
platform/data/yardsticks.json, platform/data/quiz.json, fr/glossaire-et-conventions.md ;
nuances : research/01 (§4.1-4.2), research/02 (§3.2, §10.4), research/03, research/12.

Syntaxe des pastilles source :
- [[fig:id]]   = entrée de platform/data/figures.json
- [[yard:id]]  = étalon de platform/data/yardsticks.json
- [[quiz:id]]  = sondage ou question de platform/data/quiz.json
- [[calc:...]] = calcul de la plateforme (mention « illustratif »), formule sur des ids existants

Texte affiché = blocs de citation (« > ») et liste « Pour aller plus loin ». Tout le reste est de la spécification.
Conventions : % du PIB et % des dépenses publiques toujours étiquetés ; COFOG = 2024 (dernière année publiée,
les données 2025 sont attendues en décembre 2026 chez l’Insee) ; étalons = 2025.
Le calendrier est calculé sur 365 jours (calendrier 2025), comme les étalons ; certaines dates diffèrent
d’un jour de celles du fichier 20 §3.3 (voir platform/data/README.md §6).
-->

---

## Étape 0. Ouverture

**Texte affiché**

> # Où va l’argent ?
>
> En 2025, les administrations publiques (État, Sécurité sociale, collectivités locales) ont dépensé 1 714,1 milliards d’euros, soit 57,3 % du produit intérieur brut (PIB) [[fig:te_2025_eur_bn]] [[fig:te_2025_pct_gdp]]. Suivons l’argent, poste par poste, sur une année entière.
>
> Durée de lecture : environ 9 minutes.

**Visuel** : « 1 714,1 Md€ » au centre, qui se fragmente en 365 cases (une case = une journée). Données : `te_2025_eur_bn`, `days_in_year`.

---

## Étape 1. Estimez d’abord

**Texte affiché**

> Avant de regarder : selon vous, sur 100 € de dépense publique, combien vont aux retraites (fonction « vieillesse ») ?

**Interaction « Estimez d’abord »**
- Curseur de 0 à 60 €, pas de 0,50 € (quiz.json, Q01 et Q02). Après validation : votre estimation, la moyenne des visiteurs et la vraie valeur sur la même échelle.
<!-- estimez-réponse: cofog_old_age_2024_pct_te, cofog_health_2024_pct_te -->
- Vraie valeur : **23,40 €** (COFOG 2024) [[fig:cofog_old_age_2024_pct_te]] [[quiz:Q01]]. Mention : « 24,30 € avec le périmètre plus large du Conseil d’orientation des retraites (COR), en 2025 » [[fig:pensions_cor_2025_pct_te]].
- Deuxième question : « Et à la santé ? » Vraie valeur : **15,60 €** [[fig:cofog_health_2024_pct_te]] [[quiz:Q02]].

**Texte affiché après la réponse**

> Sur 100 € de dépense publique, 23,40 € vont à la vieillesse, surtout les retraites, et 15,60 € à la santé (données 2024) [[quiz:Q01]] [[quiz:Q02]]. À eux deux, près de 4 euros sur 10 [[calc:cofog_old_age_2024_pct_te + cofog_health_2024_pct_te = 39,0]].

---

## Étape 2. L’étalon du chapitre : une journée de dépense publique

**Texte affiché**

> Notre étalon pour comparer : **une journée de dépense publique**.
>
> 1 714,1 milliards divisés par 365 jours : **une journée coûte 4,70 milliards d’euros** [[yard:one_day_spending_eur_bn]]. Par habitant, cela fait **68 € par jour**, environ 24 800 € par an [[yard:te_per_capita_per_day_eur]] [[fig:te_per_capita_2025_eur]] [[fig:population_2025_m|contexte]].

**Visuel** : une case « 1 jour = 4,70 Md€ » se détache de la grille.

---

## Étape 3. Le calendrier de la dépense publique

**Texte affiché**

> Imaginons que la France paie ses dépenses dans l’ordre, poste par poste, à partir du 1er janvier. Combien de jours chaque poste occupe-t-il ?

**Visuel (composant « calendrier de la dépense publique »)**
- Ruban de 365 jours qui se remplit au défilement, une couleur par fonction, étiquette de date au front de remplissage (mobile : ruban vertical).
- Sous le ruban : « 1 jour = 4,70 Md€. Parts de 2024 (COFOG, dernières données publiées), appliquées à l’année 2025. Déficit : 2025. »
- Segments = yardsticks `calendar_days_*` (% des dépenses publiques × 365) ; dates = 1er janvier + plancher des jours cumulés.

### Étape 3a. Du 1er janvier au 31 mai : la protection sociale

> **Du 1er janvier au 31 mai**, tout l’argent va à la protection sociale (hors santé) : retraites, pensions de réversion, invalidité, famille, chômage, revenu de solidarité active (RSA), aides au logement. Cela fait **151 jours**, soit 41,5 % des dépenses publiques [[fig:cofog_social_protection_2024_pct_te]] [[yard:calendar_days_social_protection]].
>
> La vieillesse occupe à elle seule les jours **du 1er janvier au 26 mars** [[yard:calendar_days_old_age]].

### Étape 3b. Du 1er juin au 27 juillet : la santé

> **Du 1er juin au 27 juillet** : la santé (hôpitaux, soins de ville, médicaments). Cela fait **57 jours**, soit 15,6 % des dépenses publiques [[fig:cofog_health_2024_pct_te]] [[yard:calendar_days_health]].

### Étape 3c. Du 28 juillet au 4 septembre : les services publics généraux

> **Du 28 juillet au 4 septembre** : les services publics généraux (institutions, gestion des impôts, recherche fondamentale, aide extérieure, intérêts de la dette). Cela fait **39 jours**, soit 10,8 % des dépenses publiques [[fig:cofog_general_public_services_2024_pct_te]] [[yard:calendar_days_general_public_services]].
>
> Les intérêts de la dette en représentent environ un tiers : 3,5 % des dépenses publiques en 2024 [[fig:cofog_interest_2024_pct_te]] [[calc:cofog_interest_2024_pct_te / cofog_general_public_services_2024_pct_te = 0,32]].

### Étape 3d. Du 5 septembre au 12 novembre : économie, transports et école

> **Du 5 septembre au 10 octobre** : les affaires économiques, dont les transports et une partie des aides aux entreprises. Cela fait **36 jours**, soit 9,9 % des dépenses publiques [[fig:cofog_economic_affairs_2024_pct_te]] [[yard:calendar_days_economic_affairs]].
>
> **Du 11 octobre au 12 novembre** : l’enseignement, de la maternelle à l’université. Cela fait **32 jours**, soit 8,9 % des dépenses publiques [[fig:cofog_education_2024_pct_te]] [[yard:calendar_days_education]].

### Étape 3e. Du 13 novembre au 30 décembre : tout le reste

> Il reste sept semaines pour tout le reste :
> - la défense, du 13 au 24 novembre : 12 jours, 3,2 % des dépenses publiques [[fig:cofog_defense_2024_pct_te]] [[yard:calendar_days_defense]] ;
> - la police, la justice et les prisons, du 25 novembre au 5 décembre : 11 jours, 3,1 % des dépenses publiques [[fig:cofog_public_order_2024_pct_te]] [[yard:calendar_days_public_order]] ;
> - la culture, le sport et les cultes, du 6 au 14 décembre : 9 jours, 2,6 % des dépenses publiques [[fig:cofog_recreation_culture_2024_pct_te]] [[yard:calendar_days_recreation_culture]] ;
> - le logement et les équipements collectifs, du 15 au 24 décembre : 9 jours, 2,5 % des dépenses publiques [[fig:cofog_housing_amenities_2024_pct_te]] [[yard:calendar_days_housing_amenities]] ;
> - l’environnement, du 25 au 30 décembre : 7 jours, 1,8 % des dépenses publiques [[fig:cofog_environment_2024_pct_te]] [[yard:calendar_days_environment]].
>
> *Le 31 décembre vient des arrondis. Les dates sont arrondies au jour : une période peut compter un jour de plus ou de moins que la durée indiquée.*

### Étape 3f. À partir du 29 novembre : l’argent emprunté

> Dans notre calendrier, **à partir du 29 novembre environ, tout est payé avec de l’argent emprunté** [[yard:borrowing_starts_day]]. C’est le déficit de 2025 : 32,3 jours de dépense publique (chapitre 1) [[yard:deficit_days]].
>
> L’ordre du calendrier est une convention : l’emprunt ne finance pas spécialement la défense ou la culture, mais un peu chaque poste.

**Visuel** : bande rouge hachurée « Déficit 2025 » sur les 32,3 derniers jours (du 29 novembre, en cours de journée, au 31 décembre), par-dessus les fonctions.

---

## Étape 4. Sur 1 000 € de dépense publique

**Texte affiché**

> Autre façon de voir les mêmes chiffres : 1 000 € de dépense publique, découpés par poste (données 2024).

**Visuel** : une pile de dix billets de 100 € se répartit en bandes proportionnelles qui glissent vers un tableau. Valeurs = % des dépenses publiques × 10 (calcul de la plateforme, « illustratif »).

| Poste (COFOG 2024) | Sur 1 000 € | Pastille |
|---|---|---|
| Protection sociale (hors santé) | 415 € | [[fig:cofog_social_protection_2024_pct_te]] |
| dont vieillesse (retraites, personnes âgées) | 234 € | [[fig:cofog_old_age_2024_pct_te]] |
| dont RSA et prime d’activité | 22 € | [[fig:cofog_rsa_prime_activite_2024_pct_te]] |
| Santé | 156 € | [[fig:cofog_health_2024_pct_te]] |
| Services publics généraux | 108 € | [[fig:cofog_general_public_services_2024_pct_te]] |
| dont intérêts de la dette | 35 € | [[fig:cofog_interest_2024_pct_te]] |
| dont aide économique extérieure | 3 € | [[fig:cofog_foreign_econ_aid_2024_pct_te]] |
| Affaires économiques (dont transports) | 99 € | [[fig:cofog_economic_affairs_2024_pct_te]] |
| Enseignement | 89 € | [[fig:cofog_education_2024_pct_te]] |
| Défense | 32 € | [[fig:cofog_defense_2024_pct_te]] |
| Ordre et sécurité publics | 31 € | [[fig:cofog_public_order_2024_pct_te]] |
| Loisirs, culture et culte | 26 € | [[fig:cofog_recreation_culture_2024_pct_te]] |
| Logement et équipements collectifs | 25 € | [[fig:cofog_housing_amenities_2024_pct_te]] |
| Protection de l’environnement | 18 € | [[fig:cofog_environment_2024_pct_te]] |

Note sous le tableau : « Total : 999 € (arrondis). La vieillesse, dans cette nomenclature, comprend la prise en charge des personnes âgées mais pas les pensions de réversion. Calcul de la plateforme d’après Eurostat (gov_10a_exp, 21 octobre 2026). »

> Sur 1 000 €, **571 € vont à la protection sociale et à la santé** [[calc:(cofog_social_protection_2024_pct_te + cofog_health_2024_pct_te) × 10 = 571]]. Nous suivons la classification des fonctions des administrations publiques (COFOG), une nomenclature européenne commune à tous les pays.

---

## Étape 5. La protection sociale, risque par risque

**Texte affiché**

> Autre loupe : celle de la Drees (direction de la recherche, des études, de l’évaluation et des statistiques), le service statistique des ministères sociaux. Son périmètre compte la santé dans la protection sociale et inclut des organismes privés (mutuelles, régimes d’employeurs). En 2024, ces prestations représentaient **31,9 % du PIB** [[fig:sp_benefits_2024_pct_gdp]].
>
> **Deux risques reçoivent 82 % des prestations de protection sociale** [[calc:drees_old_age_survivors_2024_share_pct + drees_health_2024_share_pct = 82,1]] : la vieillesse et la survie (pensions de réversion), 45,8 %, et la santé (maladie, invalidité, accidents du travail), 36,3 % [[fig:drees_old_age_survivors_2024_share_pct]] [[fig:drees_health_2024_share_pct]]. La famille, l’emploi, le logement et la pauvreté se partagent les 17,9 % restants [[fig:drees_four_other_risks_2024_share_pct]].

**Visuel** : barres empilées à 100 %, accolades « 82 % » et « 18 % ». Axe : « en % des prestations de protection sociale (Drees) », ni % du PIB ni % des dépenses publiques. Infobulle « Pourquoi pas le même chiffre qu’à l’étape 3 ? » : « La Drees compte les prestations publiques et privées ; la COFOG ne compte que les administrations publiques et range la santé à part. »

---

## Étape 6. Où l’on veut couper, où se trouve l’argent

**Texte affiché**

> En septembre 2026, l’institut de sondage Elabe a demandé aux Français, pour *Les Echos*, quelles dépenses réduire en priorité. Les plus citées : la famille (34 % des personnes interrogées), les aides aux entreprises (33 %), le chômage (30 %) [[quiz:M6]]. Les moins citées : les retraites (7 % des personnes interrogées), la santé (6 %), l’éducation (5 %) [[quiz:M6]].
>
> Les réponses varient selon le vote : à gauche, les aides aux entreprises viennent en tête ; à droite, la famille [[quiz:M6]].
>
> La famille et le chômage pèsent ensemble **environ 7 % des dépenses publiques** (4,0 % et 2,9 %) [[fig:cofog_family_2024_pct_te]] [[fig:cofog_unemployment_2024_pct_te]] [[calc:cofog_family_2024_pct_te + cofog_unemployment_2024_pct_te = 6,9]]. La vieillesse, la santé et l’éducation en pèsent **environ 48 % des dépenses publiques** [[calc:cofog_old_age_2024_pct_te + cofog_health_2024_pct_te + cofog_education_2024_pct_te = 47,9]]. Les aides aux entreprises pèsent de 45 à 211 milliards d’euros selon la définition [[fig:business_aid_range_eur_bn]].
>
> Ce constat ne dit pas ce qu’il faudrait couper, qui est un choix politique. Il dit où se trouvent les grandes sommes.

**Visuel** : deux colonnes reliées, « % des personnes interrogées » (Elabe pour *Les Echos*, 1er-2 septembre 2026, 1 005 personnes) et « % des dépenses publiques » (COFOG 2024). Les aides aux entreprises, sans valeur COFOG unique, apparaissent en barre de fourchette (« jours de dépense publique », 45 à 211 Md€) avec renvoi à l’étape 9.

---

## Étape 7. Les retraites, premier poste

**Texte affiché**

> Premier poste : les retraites, **422,2 milliards d’euros en 2025, soit 14,1 % du PIB** (périmètre du Conseil d’orientation des retraites, COR) [[fig:pensions_cor_2025_eur_bn]] [[fig:pensions_cor_2025_pct_gdp]]. Avec nos étalons :
> - **90 jours de dépense publique** [[calc:pensions_cor_2025_eur_bn / one_day_spending_eur_bn = 89,9]] ;
> - **2,8 fois le déficit de 2025** [[calc:pensions_cor_2025_eur_bn / deficit_2025_eur_bn = 2,78]]. Ce n’est pas leur part dans ce déficit : financé surtout par des cotisations, le système est presque à l’équilibre [[fig:pension_balance_2025_eur_bn|contexte]] ;
> - pour un ménage gagnant 3 000 € par mois [[yard:household_monthly_income_eur]], **811 € par mois** [[yard:household_pensions_month_eur]] (image illustrative, voir ses limites au chapitre 1).
>
> Pourquoi 90 jours ici et 85 dans le calendrier [[calc:pensions_cor_2025_eur_bn / one_day_spending_eur_bn = 89,9]] [[yard:calendar_days_old_age]] ? Le COR compte les pensions de réversion. La fonction « vieillesse » de la COFOG ne les compte pas, mais inclut la prise en charge des personnes âgées.
>
> Ces parts dépendent aussi d’une convention, selon le Conseil d’analyse économique (CAE ; instance d’économistes placée auprès du Premier ministre). Compter autrement la cotisation de l’État employeur réduirait la dépense totale, pas le déficit.

**Visuel** : fiche de paie de 3 000 € ; dans la colonne « dépenses du mois », le bloc « retraites : 811 € » s’allume. Carte perception : « 47 % des Français pensent que le niveau de vie des retraités est inférieur à la moyenne » (institut de sondage Toluna-Harris Interactive pour l’Observatoire Hexagone (association favorable à une part de retraite par capitalisation), 21-24 février 2025, 1 101 personnes) [[quiz:M8]] ; mesuré en 2023 : 100,2 % en moyenne [[fig:retirees_relative_living_standard_pct]] ; mention : « une moyenne : le niveau de vie baisse souvent au départ à la retraite, et le COR prévoit un recul à long terme (chapitre 6) ».

**Encadré** (même écran, jamais replié)

<!-- box-side: droite -->
> **Le meilleur contre-argument**
>
> **« Le système de retraite est en déficit, si l’on compte honnêtement ses ressources. »**
>
> Le quasi-équilibre publié chaque année compte comme une recette la contribution que l’État employeur verse pour équilibrer le régime de ses fonctionnaires. En 2025, elle atteignait 49,3 milliards d’euros [[fig:pension_state_balancing_contribution_2025_eur_bn]]. La Fondation iFRAP (libérale) la compare au taux de cotisation d’un employeur privé. Après déduction des dépenses de solidarité, elle voit dans l’écart une subvention d’équilibre, qui masque un déficit.
>
> Selon la convention, le déficit de 2025 va de 0,2 % à 1,9 % du PIB [[fig:pension_balance_convention_range_pct_gdp]]. Le bas suit la convention du COR ; le haut compte toutes les contributions d’équilibre comme des subventions.
>
> *Sources : Fondation iFRAP (libérale), article sur le régime de retraite des agents de l’État, 27 septembre 2022 ; Conseil d’orientation des retraites (COR ; instance d’études et de concertation sur les retraites), rapport annuel, juin 2026.* [[src:f03]] [[src:f03:cor26]]
>
> **Ce qu’on peut répondre**
>
> Le COR (instance d’études et de concertation sur les retraites) chiffre le déficit de 2025 à 5,1 milliards d’euros, le bas de la fourchette [[fig:pension_balance_2025_eur_bn]].
>
> En février 2025, la Cour des comptes (juridiction financière) a jugé que la comparaison avec le taux du privé n’isole pas une surcotisation [[src:f03]]. Les fonctionnaires cotisent sans leurs primes, et leur régime compte moins de cotisants par retraité. En septembre 2025, le CAE (instance d’économistes placée auprès du Premier ministre) conclut : pas de déficit caché, mais un coût salarial surévalué.
>
> Sur un point, l’objection tient : le solde dépend d’une convention. Mais le déficit public total, lui, ne change pas selon la convention.

---

## Étape 8. La santé, deuxième poste

**Texte affiché**

> En 2024, les administrations publiques ont consacré à la santé **261 milliards d’euros, soit 15,6 % des dépenses publiques et 8,9 % du PIB** [[fig:cofog_health_2024_eur_bn]] [[fig:cofog_health_2024_pct_te]] [[fig:cofog_health_2024_pct_gdp]].
>
> Pour un ménage gagnant 3 000 € par mois [[yard:household_monthly_income_eur]], l’Assurance maladie représenterait **510 € par mois** [[yard:household_health_month_eur]] (image illustrative, voir ses limites au chapitre 1). Ce calcul part des 265,4 milliards d’euros dépensés en 2025 pour l’objectif national de dépenses d’assurance maladie (Ondam) [[fig:ondam_2025_eur_bn]], un périmètre un peu différent.
>
> Deux pistes d’économies sont souvent citées. Ce sont des **réservoirs, pas des économies garanties**. Les frais de gestion dépassent d’environ 6 milliards d’euros la moyenne de l’Union européenne [[fig:health_admin_gap_eur_bn]]. Les soins inutiles ou de faible valeur atteindraient environ 22 milliards [[fig:low_value_care_eur_bn]] : c’est une extrapolation de la Cour des comptes, pas un montant contrôlé.

**Visuel** : sous le bloc « retraites : 811 € », le bloc « santé : 510 € » s’allume. Deux jauges en pointillé (6 Md€, 22 Md€), mention fixe « réservoir, pas rendement ».

---

## Étape 9. Les sommes citées par chaque camp, au même étalon

**Texte affiché**

> Chaque camp cite des sommes à mobiliser sans toucher aux grands postes. À gauche, surtout des recettes non perçues et des aides à conditionner ; à droite, surtout des dépenses. Même étalon pour tous : les jours de dépense publique.
>
> Une taille n’est pas un rendement : ce que chaque piste rapporterait vraiment, et les impôts nouveaux comme la taxe Zucman, sont au chapitre 7.
>
> Souvent citées à gauche :
> - **Les aides publiques aux entreprises** : de 45 milliards (sens européen) à 211 milliards d’euros (Sénat) en 2023, soit **de 10 à 45 jours** [[fig:business_aid_range_eur_bn]] [[calc:business_aid_range_eur_bn / one_day_spending_eur_bn = 9,6 ; 44,9]]. Précaution : le haut compte surtout des baisses d’impôts et de cotisations, et des prêts. La Fondation iFRAP n’y voit pas des aides. Des syndicats (CGT, Force ouvrière) le retiennent et demandent des conditions et une évaluation.
> - **Les « niches fiscales »** : 91,8 milliards d’euros d’impôts non prélevés en 2025, soit **environ 20 jours** [[fig:tax_expenditures_2025_eur_bn]] [[calc:tax_expenditures_2025_eur_bn / one_day_spending_eur_bn = 19,6]]. Précaution : des recettes non perçues, pas une recette disponible telle quelle ; elles recoupent en partie les aides aux entreprises (chapitre 3).
> - **Les « niches sociales »** (exonérations et baisses de cotisations) : 91,0 milliards d’euros en 2025, soit **environ 19 jours** [[fig:niches_sociales_2025_eur_bn]] [[calc:niches_sociales_2025_eur_bn / one_day_spending_eur_bn = 19,4]]. Précaution : des recettes non perçues, qui recoupent en grande partie les aides aux entreprises ; les montants ne s’additionnent pas.
> - **La fraude fiscale** : la Cour des comptes juge impossible de dire si elle est plus proche de 30 ou de 130 milliards d’euros par an [[fig:tax_gap_cour_range_eur_bn]]. Cela fait **de 6 à 28 jours** [[calc:tax_gap_cour_range_eur_bn / one_day_spending_eur_bn = 6,4 ; 27,7]]. Précaution : une perte estimée, pas un montant récupérable (chapitre 3).
> - **L’impôt sur la fortune** : sa transformation en impôt sur la fortune immobilière coûte de 3 à 4,5 milliards d’euros par an [[fig:isf_repeal_mechanical_loss_eur_bn]]. Cela fait **de 0,6 à 1 jour** [[calc:isf_repeal_mechanical_loss_eur_bn / one_day_spending_eur_bn = 0,64 ; 0,96]]. Précaution : une estimation citée par le CAE, effet mécanique seulement. La Fondation iFRAP prévoyait un gain d’investissement et d’emploi. Le CAE juge l’exil fiscal limité (chapitre 4).
>
> Souvent citées à droite :
> - **Le « train de vie de l’État »** (services publics généraux hors intérêts) : 7,3 % des dépenses publiques en 2024, soit **environ 27 jours** [[calc:cofog_general_public_services_2024_pct_te − cofog_interest_2024_pct_te = 7,3]] [[yard:calendar_days_gps_excl_interest]]. Précaution : ce poste inclut la recherche fondamentale et l’aide extérieure, mais pas le personnel administratif des hôpitaux et des écoles.
> - **La fraude sociale** : environ 14 milliards d’euros de pertes estimées par an (Haut Conseil du financement de la protection sociale), soit **environ 3 jours** [[fig:social_fraud_hcfips_dec2025_eur_bn]] [[calc:social_fraud_hcfips_dec2025_eur_bn / one_day_spending_eur_bn = 3,0]]. Précaution : une perte estimée sur un périmètre incomplet, dont une faible part est détectée. La Fondation iFRAP juge qu’on pourrait en récupérer davantage.
> - **La contribution à l’Union européenne** : de 6,4 à 9,5 milliards d’euros net en 2025, selon la méthode [[fig:eu_net_contribution_2025_operating_eur_bn]] [[fig:eu_net_contribution_2025_accounting_eur_bn]]. Cela fait **de 1,4 à 2 jours** [[calc:eu_net_contribution_2025_*_eur_bn / one_day_spending_eur_bn = 1,4 ; 2,0]]. Précaution : la réduire suppose de changer une règle européenne adoptée à l’unanimité des 27 pays. Le ministère de l’Économie juge la notion de solde net limitée (chapitre 7).
> - **L’aide au développement** : 4,9 milliards d’euros en 2024 (comptes nationaux), 12,9 milliards en 2025 selon l’Organisation de coopération et de développement économiques (OCDE) [[fig:cofog_foreign_econ_aid_2024_eur_bn]] [[fig:oda_2025_eur_bn]]. Soit **de 1 à près de 3 jours** [[calc:cofog_foreign_econ_aid_2024_eur_bn / one_day_spending_eur_bn = 1,0 ; oda_2025_eur_bn / one_day_spending_eur_bn = 2,7]]. Précaution : l’OCDE compte aussi des prêts et l’accueil de réfugiés et d’étudiants en France. Les crédits budgétaires, déjà en baisse, sont de 3,17 milliards en 2027 [[fig:oda_mission_plf2027_eur_bn]].
> - **L’aide médicale de l’État (AME) de droit commun** : 1,34 milliard d’euros en 2025 [[fig:ame_2025_eur_bn]], soit **0,3 jour** de dépense publique [[calc:ame_2025_eur_bn / one_day_spending_eur_bn = 0,29]] (environ 7 heures [[calc:ame_2025_eur_bn / one_day_spending_eur_bn × 24 = 6,8|contexte]]). Précaution : le rapport Évin-Stefanini (rapport remis au gouvernement, 2023) juge le dispositif utile et maîtrisé pour l’essentiel, malgré plus de bénéficiaires. Il propose de l’adapter, pas de le limiter aux soins urgents [[src:f16:S14]].

**Visuel** : deux colonnes de cinq cibles chacune, sur le même ruban, à la même échelle, même gabarit et couleur neutre (aucune couleur de camp) ; barres de fourchette quand il y a deux définitions ou une incertitude ; chaque ligne porte sa précaution au même format. Les niches et les aides aux entreprises portent la mention « périmètres qui se recoupent ». Données : `business_aid_range_eur_bn`, `tax_expenditures_2025_eur_bn`, `niches_sociales_2025_eur_bn`, `tax_gap_cour_range_eur_bn`, `isf_repeal_mechanical_loss_eur_bn`, `calendar_days_gps_excl_interest`, `social_fraud_hcfips_dec2025_eur_bn`, `eu_net_contribution_2025_*`, `cofog_foreign_econ_aid_2024_eur_bn`, `oda_2025_eur_bn`, `ame_2025_eur_bn`.

**Pastilles source** : Cour des comptes, *La lutte contre la fraude fiscale*, 16 décembre 2025 [[fig:tax_gap_cour_range_eur_bn]] (mention : pas une estimation, seulement l’étendue de l’incertitude) ; Cour des comptes, *Analyse de l’exécution budgétaire 2025 – Dépenses fiscales*, avril 2026 [[fig:tax_expenditures_2025_eur_bn]] ; annexe 4 du projet de loi de financement de la sécurité sociale pour 2027 [[fig:niches_sociales_2025_eur_bn]] ; Conseil d’analyse économique, *Focus* n° 118, juillet 2025 [[fig:isf_repeal_mechanical_loss_eur_bn]] ; Haut Conseil du financement de la protection sociale, note adoptée le 4 décembre 2025 [[fig:social_fraud_hcfips_dec2025_eur_bn]] ; C. Évin et P. Stefanini, *Rapport sur l’aide médicale de l’État*, décembre 2023 [[src:f16:S14]].

---

## Étape 10. Et ailleurs en Europe ?

**Texte affiché**

> Environ deux tiers de l’écart (chapitre 1) avec la zone euro à 21 pays (ZE21, Bulgarie comprise) viennent des dépenses sociales et de santé [[fig:gap2024_sp_plus_health_pp|contexte]].
>
> En 2024, les prestations de protection sociale atteignaient 32,0 % du PIB en France, contre 27,4 % du PIB dans l’Union européenne à 27 [[fig:sp_benefits_esspros_2024_pct_gdp]] [[fig:eu27_sp_benefits_2024_pct_gdp]]. Elle est parmi les trois premiers pays [[fig:sp_benefits_eu_rank_2024|contexte]]. Mais par habitant, en tenant compte du coût de la vie, elle est **7e sur 27** (2024) [[fig:sp_benefits_per_capita_pps_2024_rank]].

**Visuel** : barre « écart avec la ZE21, 2024 : 7,8 points de PIB » décomposée (protection sociale dont vieillesse, santé, autres), axe « en points de PIB ». Bascule « en % du PIB » ↔ « par habitant, en SPA ». Rang 2024 en % du PIB : 0,05 point d’avance sur l’Autriche, donc toujours « parmi les trois premiers », jamais « 2e ».

**Encadré** (même écran, jamais replié)

<!-- box-side: gauche -->
> **Le meilleur contre-argument**
>
> **« Public et privé additionnés, les écarts entre pays se resserrent fortement : la France passe surtout davantage par le public. »**
>
> L’argument s’appuie sur la dépense sociale nette, une mesure de l’OCDE mise au point par Willem Adema (économiste à l’OCDE) et Maxime Ladaique. On additionne la dépense sociale publique et privée, après impôts.
>
> Pour 2021, selon l’OCDE, on obtient 32 % du PIB en France et 33 % aux États-Unis [[fig:socx_net_total_2021_pct_gdp]] [[fig:us_socx_net_total_2021_pct_gdp]]. Baisser la dépense publique déplacerait donc une partie du coût et des risques vers les ménages, sans forcément baisser le coût total.
>
> *Sources : Willem Adema (économiste à l’OCDE) et Maxime Ladaique, document de travail de l’OCDE n° 92, novembre 2009 ; base de données de l’OCDE sur les dépenses sociales (SOCX), consultée le 25 octobre 2026.* [[src:f10]]
>
> **Ce qu’on peut répondre**
>
> Sur un point, l’objection tient : public et privé additionnés, l’écart avec les États-Unis disparaît. Mais Adema et Ladaique classaient déjà la France parmi les pays qui dépensent le plus en net. En 2021, elle est 2e sur 38 pays, loin de la moyenne des pays membres (22,0 % du PIB) [[fig:socx_net_total_2021_rank]] [[fig:oecd_mean_socx_net_total_2021_pct_gdp]].
>
> Et la part publique est financée par les prélèvements ou par l’emprunt : c’est elle qui pèse sur le déficit et la dette.
>
> *Cette mesure et celle d’Eurostat, plus haut, diffèrent : l’égalité des deux chiffres est une coïncidence.*

---

## Étape 11. Transition

**Texte affiché**

> Résumons. Sur 1 000 € de dépense publique, 571 € vont à la protection sociale et à la santé [[calc:(cofog_social_protection_2024_pct_te + cofog_health_2024_pct_te) × 10 = 571]].
>
> Qui paie ces 1 714,1 milliards [[fig:te_2025_eur_bn]] ? Pour l’essentiel, les impôts et les cotisations ; pour le reste, l’emprunt. Et chacun ne contribue pas de la même façon.
>
> **→ Chapitre 3 : Qui paie ?**

**Visuel** : le ruban se replie en une barre qui devient la barre « recettes » du chapitre suivant.

**Boutons** : « Chapitre 3 : Qui paie ? » (principal) ; « Testez une mesure dans le vérificateur de promesses » ; lien discret « Équilibrez vous-même le budget ».

---

## Pour aller plus loin

- **Chaque fonction COFOG** : ce que recouvre chaque poste du calendrier, et son évolution.
- **Protection sociale par risque** : les six risques de la Drees, en milliards d’euros, et le passage de la Drees à la COFOG.
- **Retraites** : le niveau de vie des retraités, et le solde du système selon les conventions.
- **Santé** : Ondam et dépense COFOG, frais de gestion, soins de faible valeur.
- **Aides publiques aux entreprises** : les définitions, de l’aide d’État européenne à la commission d’enquête du Sénat.
- **Cibles souvent citées d'« économies faciles »** et **Immigration et finances publiques (y compris l’AME)** : chaque cible, avec ses arguments pour et contre.
- **Comparer avec l’Europe** : choisissez l’indicateur (% du PIB, par habitant en SPA, public ou public et privé).
- **Méthode** : COFOG, comptes de la Drees et comptes de la santé, et pourquoi leurs chiffres diffèrent.

---

<!--
CALCULS ET DATES (vérifiés le 25 octobre 2026, passe « pastilles et coupes »)

Dates du calendrier (365 jours, 1er janvier + plancher des jours cumulés, yardsticks calendar_days_*) :
protection sociale 151,475 → 31 mai ; vieillesse 85,41 → 26 mars ; santé 56,94 (cumul 208,4) → 27 juil. ;
services généraux 39,42 (247,8) → 4 sept. ; affaires économiques 36,135 (284,0) → 10 oct. ; enseignement 32,485 (316,5) → 12 nov. ;
défense 11,68 (328,1) → 24 nov. ; ordre public 11,315 (339,5) → 5 déc. ; culture 9,49 (348,9) → 14 déc. ;
logement 9,125 (358,1) → 24 déc. ; environnement 6,57 (364,6) → 30 déc. Emprunt : borrowing_starts_day 332,7 → 29 nov.
Affichage des jours (arrondi) : 151, 85, 57, 39, 36, 32, 12, 11, 9, 9, 7 ; train de vie 26,645 → « environ 27 ».

[[calc:]] : 4 sur 10 = 23,4 + 15,6 = 39,0 ; intérêts / services généraux = 3,5 / 10,8 = 32 % (« environ un tiers ») ;
571 € = (41,5 + 15,6) × 10 ; famille + chômage = 4,0 + 2,9 = 6,9 (« environ 7 % ») ; 48 % = 23,4 + 15,6 + 8,9 = 47,9 ;
90 jours = 422,2 / 4,6962 = 89,9 ; (6 119 €/hab retiré le 30 octobre 2026) ; 2,8 fois = 422,2 / 151,6 = 2,78 ;
train de vie = 10,8 − 3,5 = 7,3 % ; aides aux entreprises 45 / 4,6962 = 9,6 et 211 / 4,6962 = 44,9 jours ;
fraude sociale 14 / 4,6962 = 2,98 → « environ 3 jours » (part des cotisations retirée le 30 octobre 2026) ;
niches fiscales 91,83 / 4,6962 = 19,6 (« environ 20 », même arrondi que le chapitre 3) ; niches sociales 91,0 / 4,6962 = 19,4 (« environ 19 ») ;
fraude fiscale 30 / 4,6962 = 6,4 et 130 / 4,6962 = 27,7 (« de 6 à 28 jours ») ; ISF-IFI 3 / 4,6962 = 0,64 et 4,5 / 4,6962 = 0,96 (« de 0,6 à 1 jour ») ;
retraites, convention du solde : 49,3 Md€ (COR, tableau 2.2) ; fourchette 0,2-1,9 % du PIB (`pension_balance_convention_range_pct_gdp`) ;
UE 6,4 / 4,6962 = 1,4 et 9,5 / 4,6962 = 2,0 jours ; aide extérieure 4,9 / 4,6962 = 1,0 et APD 12,9 / 4,6962 = 2,7 jours ;
AME 1,34 / 4,6962 = 0,29 jour (« 0,3 jour ») et × 24 = 6,8 heures ; table 1 000 € : somme 999 €.
-->

## Notes de relecture

<!-- Non affiché sur le site. -->

**Confrontation aux sources publiques (2026-10-30)**
Décision : pas de relecteurs humains ; le texte est confronté aux positions publiées d’économistes et d’institutions de plusieurs orientations. Seuls les textes ouverts par la passe de collecte sont cités (URL et date ci-dessous). Aucun fichier de données modifié (ce fichier ne possède que le chapitre) ; seuls des ids existants de platform/data sont utilisés.

*Points vérifiés (verdicts) et corrections*
1. 02-01 (part des retraites, COFOG 23,40 € / COR 24,30 €), partiellement étayé : COR, *Rapport annuel 2026, synthèse*, juin 2026 (https://www.cor-retraites.fr/sites/default/files/2026-06/Synth%C3%A8se_RA_2026_0.pdf) confirme 422 Md€, 14,1 % du PIB, 24,3 % de la dépense publique. **Corrigé** (étape 7) : phrase ajoutée, sans chiffre, sur la dépendance de toutes les parts à une convention (H. Paris, CAE, *Focus* n° 121, septembre 2025, https://cae-eco.fr/static/pdf/Focus_121_pension_250919.pdf : autre comptabilisation des cotisations de l’État employeur = dépense et recettes plus basses, solde inchangé). Le chiffre de 28,9 Md€ n’est pas affiché : aucun id. L’exclusion des pensions de réversion de la fonction « vieillesse » COFOG (sous-fonction « survie » distincte) n’a pas été contredite ; gardée.
2. 02-02, 02-03, 02-05 (étalon d’une journée, calendrier, date du 29 novembre), partiellement étayés faute de source contraire : outils pédagogiques de la plateforme, déjà présentés comme une convention (étape 3f). Aucun changement.
3. 02-04 (intérêts ≈ un tiers des services généraux) et 02-13 (COFOG santé / Ondam) : non contredits ; aucun changement. À recouper avec les tableaux Insee/PLFSS par le propriétaire des données.
4. 02-06 (Drees 31,9 % du PIB, 82 %) : non contredit ; la Cour des comptes (février 2025, https://www.vie-publique.fr/files/rapport/pdf/297428.pdf) confirme que des présentations comptables différentes ne se rapprochent pas. Aucun changement.
5. 02-07 (sondage Elabe) : étayé (Elabe pour *Les Echos*, 3 septembre 2026, https://elabe.fr/fichier-pdf/13231-20260903_elabe_les-echos_les-francais-et-la-dette-publique/). Voir critique gauche n° 8.
6. 02-08, 02-10, 02-11 (retraites, encadré iFRAP) : étayés ; voir critiques gauche n° 3 et 4, droite n° 1.
7. 02-09 (811 € par mois) : illustration de la plateforme, mention « image illustrative » gardée. Aucun changement.
8. 02-12 (carte perception, 100,2 %) : **corrigé** (visuel) : « en moyenne » et mention « le niveau de vie baisse souvent au départ à la retraite, et le COR prévoit un recul à long terme (chapitre 6) » (Drees, *Études et Résultats* n° 1369, 26 mars 2026, https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/etudes-et-resultats/260326-niveau-de-vie-des-retraites ; COR 2026). Le sondage Toluna-Harris Interactive n’a pas pu être rouvert par la collecte : à revérifier par le propriétaire de quiz.json (M8).
9. 02-14 (réservoirs santé) : étayé par la Cour des comptes (avril 2026). Aucun changement.
10. 02-15 (aides aux entreprises), débat présenté de façon équilibrée mais bas de fourchette à documenter : le plancher de 45 Md€ est la définition des aides d’État au sens européen (figures.json, `business_aid_range_eur_bn`, research/08 §4) ; **affiché** dans le texte. Voir critiques gauche n° 1 et droite n° 2.
11. 02-16, 02-17 (niches fiscales et sociales) : recoupement confirmé (Sénat via CGT ; Fondation iFRAP). **Corrigé** : mention « recettes non perçues » sur les deux lignes.
12. 02-18 (fraude fiscale) : étayé par la Cour des comptes (16 décembre 2025, https://www.ccomptes.fr/sites/default/files/2025-12/20251216-Lutte-contre-la-fraude-fiscale.pdf). Aucun changement.
13. 02-19 (ISF) : **corrigé** : « une estimation citée par le CAE, effet mécanique seulement » au lieu de « un chiffrage du CAE » (CAE *Focus* n° 118, juillet 2025, https://cae-eco.fr/static/pdf/Focus_118_emigration_fiscale_250725_v2.pdf) ; contre-argument libéral ajouté (Fondation iFRAP, 15 février 2018, https://www.ifrap.org/budget-et-fiscalite/la-suppresion-totale-de-lisf-aurait-ete-la-meilleure-solution : gain d’investissement et d’emploi prévu, présenté comme une prévision) et constat du CAE sur l’exil fiscal limité.
14. 02-20 (« train de vie de l’État ») : calcul de la plateforme ; aucune source contraire. Aucun changement.
15. 02-21 (fraude sociale) : **corrigé** : « une perte estimée sur un périmètre incomplet, dont une faible part est détectée. La Fondation iFRAP juge qu’on pourrait en récupérer davantage » (Fondation iFRAP, 15 janvier 2026, mise à jour 9 avril 2026, https://www.ifrap.org/emploi-et-politiques-sociales/la-fraude-sociale-en-2024-175-mdeu-estimes-seulement-12-mdeu-recouvre-ou-evite). « Plus de la moitié porte sur les cotisations » **retiré** : non confirmé par un texte ouvert (note HCFiPS illisible), et place nécessaire.
16. 02-22 (contribution à l’UE) : **corrigé** : « Le ministère de l’Économie juge la notion de solde net limitée » (Banque des Territoires, 15 octobre 2026, https://www.banquedesterritoires.fr/budget-2027-la-facture-europeenne-continue-de-gonfler, citant Bercy : la notion « rencontre plusieurs limites »). Règle d’unanimité gardée (décision sur les ressources propres), à confirmer par une source ouverte.
17. 02-23 (AME, aide au développement) : **corrigé** ; voir critiques droite n° 6 et 8.
18. 02-24 (SOCX, Adema) : **corrigé** ; voir critiques gauche n° 7 et droite n° 5.

*Critiques de gauche*
1. Aides aux entreprises réduites à « supprimer » (élevée) : **appliqué**. « Les supprimer aurait un coût en emplois » retiré ; ajouté : « Des syndicats (CGT, Force ouvrière) le retiennent [le périmètre large] et demandent des conditions et une évaluation » (CGT, *Mémo éco* n° 150, 28 août 2025 ; FO, note à la Commission de concertation, avril 2026, URL dans la passe de collecte). Bornes « sens européen » / « Sénat » affichées. **Non appliqué** : 203 Md€ (Clersé), 15-270 Md€ (FO) et ventilation 41/88/75/7 Md€, faute d’ids. Le coût en emplois des allègements reste au chapitre 3.
2. Libellé « économies faciles » (moyenne) : **appliqué**. Titre de l’étape : « Les sommes citées par chaque camp, au même étalon » ; phrase d’ouverture : « À gauche, surtout des recettes non perçues et des aides à conditionner ; à droite, surtout des dépenses. » Le terme du glossaire reste dans « Pour aller plus loin » (nom de la fiche).
3. Fourchette 0,2-1,9 % appelée « déficit » (moyenne) : **appliqué, formulation commune**. « Le bas suit la convention du COR ; le haut compte toutes les contributions d’équilibre comme des subventions. » Constat du CAE (*Focus* n° 121) ajouté dans la réponse.
4. « 2,8 fois le déficit » sans le solde (moyenne) : **appliqué**. « Ce n’est pas leur part dans ce déficit : financé surtout par des cotisations, le système est presque à l’équilibre », avec pastille `pension_balance_2025_eur_bn` (contexte).
5. Dénominateur conventionnel (moyenne) : **appliqué sans chiffre** (voir point 1) ; 28,9 Md€ : aucun id.
6. Carte perception (moyenne) : **appliqué** (point 8), sans les chiffres −9 % et 90,3 % (aucun id ; résultat détenu par le chapitre 6).
7. Encadré SOCX plus fort que la source (moyenne) : **appliqué**. Thèse : « Public et privé additionnés, les écarts entre pays se resserrent fortement : la France passe surtout davantage par le public. » ; « coût et des risques » ; réponse : « Adema et Ladaique classaient déjà la France parmi les pays qui dépensent le plus en net » (W. Adema et M. Ladaique, OCDE, document de travail n° 92, 13 novembre 2009, https://econpapers.repec.org/RePEc:oec:elsaab:92-en).
8. Sondage sans clivage partisan (faible) : **appliqué sans chiffre** : « à gauche, les aides aux entreprises viennent en tête ; à droite, la famille ». Les pourcentages par électorat (47 %, 50 %…) ne sont pas dans quiz.json : à ajouter à M6 si on veut les afficher.
9. Solde net UE (faible) : **appliqué** (point 16), sans la citation de la députée (propos politique, pas une étude).
10. Baisse du budget d’aide au développement (faible) : **appliqué** avec un id existant : « Les crédits budgétaires, déjà en baisse, sont de 3,17 milliards en 2027 » (`oda_mission_plf2027_eur_bn`). Le 4,3 Md€ 2025 « en baisse d’un tiers » (B. Cabrillac, Ferdi, entretien pour l’Institut Montaigne, 18 mars 2025) n’a pas d’id.
11. Attribution ISF et guillemets « déficit caché » (faible) : **appliqué** (point 13 ; guillemets retirés, la Cour « a jugé que la comparaison avec le taux du privé n’isole pas une surcotisation »).

*Critiques de droite*
1. Réponse qui étire la Cour des comptes (élevée) : **appliqué**. Méthode iFRAP décrite (comparaison au taux d’un employeur privé, après déduction des dépenses de solidarité) ; motifs de la Cour donnés (assiette sans les primes, moins de cotisants par retraité) ; guillemets retirés. **Non appliqué** : 26,3 Md€ (2021) et déficit de 6,6 Md€ de la Cour (millésime antérieur au 5,1 Md€ du COR 2026) : aucun id, et le chiffre de 2021 n’est pas comparable aux 49,3 Md€ de 2025.
2. Plancher de 45 Md€ au-dessus de l’estimation stricte (élevée) : **partiellement appliqué**. Source du plancher documentée (aides d’État au sens européen) ; critère de désaccord affiché (« La Fondation iFRAP n’y voit pas des aides ») ; fourchette inchangée : l’estimation de 18,5 Md€ (Fondation iFRAP, 25 juillet 2025, mise à jour 17 septembre 2025, https://www.ifrap.org/budget-et-fiscalite/aides-aux-entreprises-211-milliards-deuros-par-ou-185-milliards) et le bas de 15 Md€ cité par FO n’ont pas d’id.
3. Fraude sociale (moyenne) : **appliqué sans chiffre** (point 15). 17,5 Md€, 2,06 Md€ détectés, 1,2 Md€ recouvrés, 3-4 Md€ récupérables : aucun id. La précaution n’est plus formulée comme celle de la fraude fiscale.
4. ISF (moyenne) : **appliqué** (point 13).
5. Attribution SOCX à Adema (moyenne) : **appliqué en partie**. Les chiffres 2021 viennent de la base SOCX de l’OCDE (figures.json, DF_NET_GDP), pas d’un calcul de la plateforme : la critique est **rejetée sur ce point**. Texte : « une mesure de l’OCDE mise au point par Willem Adema (économiste à l’OCDE) et Maxime Ladaique » ; « Pour 2021, selon l’OCDE » ; ligne de source complétée (document de travail n° 92, 2009).
6. AME (moyenne) : **appliqué**. « juge le dispositif utile et maîtrisé pour l’essentiel, malgré plus de bénéficiaires. Il propose de l’adapter, pas de le limiter aux soins urgents » (rapport Évin-Stefanini, 4 décembre 2023, https://www.vie-publique.fr/files/rapport/pdf/292122.pdf). La phrase exacte sur les soins urgents reste à isoler dans le rapport.
7. Niches en jours de dépense (faible) : **appliqué en partie** : « des recettes non perçues » sur les deux lignes. La phrase iFRAP sur les niches qui suivent le niveau des impôts n’est pas ajoutée (place ; le désaccord de définition est déjà dit sur la ligne des aides).
8. Aide au développement (faible) : **appliqué** (critique gauche n° 10).

*Coupes pour rester sous 2 200 mots* (texte affiché : 2 142 → 2 186 mots, validate.py) : phrase sur la moyenne des visiteurs (étape 1) ; « Pris seul… » (étape 0) ; « Faites défiler… » (étape 3) ; « Plus de la moitié de l’année… » (étape 3b) ; « Le chapitre 5 y revient en détail » (étape 3c) ; redite enseignement / intérêts / défense sous le tableau (étape 4) ; « Une grande partie n’est pas de la dépense au sens strict » (étape 6) ; puce « 6 100 € par habitant » et renvoi « Ce que les retraites permettent d’obtenir » (étape 7) ; renvoi « Les résultats en santé » (étape 8) ; phrase finale « Une fourchette large… » (étape 9) ; écart santé 1,06 / 1,5 point (étape 10 ; détenu par le chapitre 1) ; « pays réputé à faible dépense publique » (encadré SOCX) ; rappel du calendrier (étape 11) ; « Pour les défenseurs du système… » (réponse de l’étape 7, remplacée par les motifs de la Cour et du CAE).

*Points ouverts pour d’autres propriétaires*
- Glossaire (§1.13, règle 7) : CGT, Force ouvrière et Ferdi n’ont pas d’étiquette ; le texte écrit « Des syndicats (CGT, Force ouvrière) ». Sénat : nommer le rapporteur de la commission d’enquête (§1.12) une fois vérifié.
- Données (ids manquants) : estimations des aides aux entreprises 18,5 Md€ (iFRAP), 203,2 Md€ (Clersé), 15-270 Md€ (FO) et ventilation Sénat 41/88/75/7 Md€ ; fraude sociale 17,5 Md€ / 2,06 / 1,2 / 3-4 Md€ (iFRAP) ; CAE *Focus* n° 121, 28,9 Md€ ; Drees −9 % de niveau de vie médian au départ ; COR 90,3 % en 2070 ; iFRAP 26,3 Md€ (2021) ; Cour des comptes 6,6 Md€ (2025) ; crédits du programme d’aide au développement 4,3 Md€ (2025) ; clivage partisan du sondage Elabe (M6) ; source `[[src:]]` pour le CAE *Focus* n° 121.
- Vérification : `python3 -I platform/data/validate.py --strict` : 0 erreur et 0 avertissement pour ce chapitre (2 186 mots affichés ; « environ 9 minutes » inchangé). Les erreurs restantes du validateur portent sur d’autres chapitres.

**Passe « finalisation » (25 octobre 2026, plan de site : D-data-pass, D-labels, D-boxes, D-ownership, D-rounding, D-vocabulary, D-reading-time)**
1. Chiffres nouveaux (D-data-pass), étape 7 : **appliqué**. Encadré iFRAP : contribution d’équilibre de l’État 49,3 milliards (`pension_state_balancing_contribution_2025_eur_bn`) et fourchette du solde selon la convention, de 0,2 % à 1,9 % du PIB (`pension_balance_convention_range_pct_gdp`). Le titre de l’article iFRAP (« 26 milliards… », données 2021, sans pastille) est remplacé dans la ligne de source par sa description. Retour à 60 ans : non affiché dans ce chapitre (aucun changement).
2. Étiquettes (glossaire §1.13) : **appliqué**. Fondation iFRAP (libérale), COR (instance d’études et de concertation sur les retraites) dans l’encadré et la réponse, Cour des comptes (juridiction financière) à la première mention, Willem Adema (économiste à l’OCDE), Observatoire Hexagone (association favorable à une part de retraite par capitalisation) dans la carte perception, « institut de sondage » pour Elabe et Toluna-Harris Interactive, rapport Évin-Stefanini (rapport remis au gouvernement).
3. Encadrés (§4.6) : **appliqué**. Les deux encadrés ont le titre exact, la thèse en gras entre guillemets, l’auteur avec son étiquette, une ligne de source en italique qui reprend l’étiquette, l’étiquette `box-side` (droite à l’étape 7, gauche à l’étape 10). Les réponses ne répondent qu’à l’encadré (retrait de « 14,1 % du PIB » à l’étape 7) et disent ce qui tient dans l’objection.
4. Doublons (D-ownership) : **appliqué**. Les 980 000 emplois sont gardés au chapitre 3 (étape 11, rapport Bozio-Wasmer, le plus pertinent) ; ici, renvoi « (chapitre 3) » sans chiffre ni pastille `contribution_relief_abolition_jobs_fte`. Étape 6 : la conversion en jours des aides aux entreprises est retirée (gardée à l’étape 9). Étape 9 garde les tailles en jours ; rendements et verdicts renvoyés au chapitre 7 (taxe Zucman comprise), paquet « plus aisés » non repris (chapitre 3). Fraude sociale alignée sur le chiffre de décembre 2025 (environ 14 milliards), comme le chapitre 7.
5. Équilibre des cibles d’« économies faciles », étape 9 : **appliqué**. Avant : 1 cible à gauche, 5 à droite. Après : 5 et 5, même gabarit (montant, jours, précaution, renvoi). Gauche : aides aux entreprises, niches fiscales, niches sociales, fraude fiscale (`tax_gap_cour_range_eur_bn`, étendue de l’incertitude selon la Cour, pas une estimation), impôt sur la fortune (`isf_repeal_mechanical_loss_eur_bn`). Droite : train de vie de l’État, fraude sociale, contribution à l’UE, aide au développement, AME. Précautions ajoutées là où il n’y en avait pas (UE, aide au développement, AME). Rachats d’actions et « superprofits » non repris : aucun id dans platform/data.
6. Validateur : **appliqué**. Sigles développés (PIB, Drees, COFOG, SOCX, OCDE) ; dénominateurs (étapes 3e, 6, 10) ; pastilles de contexte (`population_2025_m`, `gap2024_sp_plus_health_pp`, `sp_benefits_eu_rank_2024`, `social_fraud_contributions_eur_bn`, calcul des heures d’AME) ; pastilles ajoutées (sondage Elabe, 90 et 85 jours, 571 €, 1 714,1 milliards) ; pastilles Q01/Q02 à l’étape 1 au lieu des ids COFOG (arrondi « 15,60 € » propre au quiz) ; bloc « Estimez d’abord » déclaré par `<!-- estimez-réponse -->` ; note « coïncidence » affichée sous l’encadré SOCX (32 % SOCX et 32,0 % Eurostat), SOCX affiché « 32 % » et « 33 % » pour ne pas doubler le « 32,0 % » d’un autre id ; phrases de plus de 25 mots et paragraphes de plus de 60 mots coupés.
7. Durée de lecture : **appliqué**. 2 142 mots affichés (validate.py), soit 8,9 minutes : « environ 9 minutes ».
8. Vérification : `python3 -I validate.py --strict` : 0 erreur et 0 avertissement pour ce chapitre.
Points ouverts : chapitre 7 (étape 8) cite encore la fraude fiscale sans `tax_gap_cour_range_eur_bn` et garde les 980 000 emplois en double avec le chapitre 3 (hors périmètre de ce fichier).

**Passe transversale (plan de site) : corrections transversales (25 octobre 2026)**
Décisions suivies : D-ownership, D-rounding, D-titles-and-transitions, D-boxes, D-vocabulary. Ce chapitre est propriétaire : part des retraites dans la dépense (question Q01/Q02, étape 1) ; dépense de retraite 422,2 milliards / 14,1 % du PIB / 90 jours / 811 € et débat sur la convention du solde (étape 7) ; réservoirs santé (environ 6 et 22 milliards) et 510 € (étape 8) ; taille en jours des cibles d’« économies faciles » côté dépenses (étape 9) ; objection SOCX (encadré de l’étape 10).
1. Titres d’étapes au format « Étape N. Titre » (18 titres, point au lieu du point médian) : **appliqué**.
2. Durée de lecture recalculée : **appliqué**. 1 950 mots affichés après corrections (script, nombres groupés comptés pour un mot), soit 8,1 minutes à 240 mots par minute : « environ 8 minutes » inchangé.
3. Étape 1 propriétaire de la question Q01/Q02 : **appliqué** (aucun changement).
4. Encart ménage de l’étape 2 (3 291 €) supprimé, image du ménage détenue par le chapitre 1 : **appliqué**. Ajout hors liste : « (3 291 €) » retiré aussi du visuel de l’étape 7.
5. RSA développé à sa première occurrence (étape 3a) : **appliqué**.
6. Étape 3c, fuite de la réponse notée du chapitre 5 (« 14 jours ») : **appliqué**. Supprimés : « environ 13 jours », `calendar_days_interest_cofog`, la phrase D.41 avec `interest_2025_pct_te` et son calcul 13,9, la phrase sur les deux concepts ; lignes correspondantes retirées du commentaire CALCULS.
7. Étape 3f, bloc déficit détenu par le chapitre 1 : **appliqué**. Retirés : 151,6 milliards, 5,1 % du PIB, 1 euro sur 11, 8,8 % et leurs pastilles ; 32,3 jours gardé avec « (chapitre 1) ».
8. Image du billet de 1 000 € (qui n’existe pas) : **appliqué** (texte et visuel : pile de dix billets de 100 €).
9. Dénominateur de « 82 % » (des prestations de protection sociale) : **appliqué**.
10. Dénominateur des pourcentages Elabe (des personnes interrogées) : **appliqué**.
11. Étape 7 : **appliqué**. « 422,2 milliards » ; ligne ménage avec `household_monthly_income_eur` et la mention « image illustrative, voir ses limites au chapitre 1 » ; pauvreté des personnes âgées (6,1 % / 14,8 %) remplacée par un renvoi au chapitre 6. Ajout hors liste : « (chapitre 6) » après le 100,2 % de la carte perception (résultat détenu par le chapitre 6).
12. Encadré de l’étape 7 rééquilibré vers la lecture libérale (Fondation iFRAP, « déficit caché » ; réponse COR et Cour des comptes) : **partiel**. Encadré et réponse appliqués mot pour mot, titre affiché « Le meilleur contre-argument », source en italique avec le titre et la date de l’article iFRAP (research/03 §5, note ifrap22). Phrase à données (49,3 milliards ; 0,2 à 1,9 % du PIB) **non ajoutée** : `pension_state_balancing_contribution_2025_eur_bn` et `pension_balance_convention_range_pct_gdp` n’existent pas encore dans figures.json. À ajouter dès que validate.py les résout. Point à trancher : le titre de l’article iFRAP contient « 26 milliards » (données 2021) sans pastille ; à retirer de la ligne source si la règle « aucun chiffre sans pastille » s’applique aussi aux titres.
13. Étape 8 : **appliqué**. « l’Assurance maladie » ; `household_monthly_income_eur` et mention « image illustrative » ; formulation Ondam (« montant effectivement dépensé ») ; espérance de vie remplacée par un renvoi au chapitre 6 ; réservoirs réécrits en phrases courtes.
14. Étape 9 : **appliqué**. AME « 0,3 jour (environ 7 heures) » avec le calcul 0,29 ; renvoi « niches fiscales et fraude fiscale » vers le chapitre 3.
15. Étape 10, écart international détenu par le chapitre 1 : **appliqué**. Paragraphe et puces remplacés par un renvoi (deux tiers, `gap2024_sp_plus_health_pp`) et l’écart santé 1,06 / 1,5 ; « zone euro à 21 pays (ZE21, Bulgarie comprise) » ; « SHA » retiré. Le visuel ne contenait pas « (SHA) » ; barre décomposée gardée.
16. Encadré SOCX : **appliqué**. Ligne Willem Adema (OCDE développée à la première occurrence), titre affiché « Le meilleur contre-argument », source en italique « base SOCX » avec `[[src:f10]]`. Réponse inchangée.
17. Bouton « Chapitre 3 : Qui paie ? » : **appliqué**. Ajout de la ligne de transition affichée « → Chapitre 3 : Qui paie ? » (décision D-titles-and-transitions).
18. « comptes de la santé (SHA) » → « comptes de la santé » dans « Pour aller plus loin » : **appliqué**.
19. Vérifications : **appliqué**. `python3 -I validate.py` : PASS (0 erreur, 0 avertissement). Texte affiché : 1 950 mots (objectif 1 500-2 200). Libellés d’encadré « Encadré (même écran, jamais replié) » ; le titre affiché est dans le bloc.
Rejeté : aucun. Chiffres absents des données (non utilisés) : `pension_state_balancing_contribution_2025_eur_bn` (49,3), `pension_balance_convention_range_pct_gdp` (0,2-1,9).

**Passe « audit gauche / droite / chiffres » (25 octobre 2026)**
1. Fraude fiscale promise au chapitre 3 mais absente (gauche, élevée) : **appliqué, variante de repli**. Les chiffres `tax_audit_*` et `tax_gap_cour_range_eur_bn` n’existent pas dans figures.json et le chapitre 3 n’a pas de passage sur la fraude fiscale : la promesse est retirée de l’étape 9 (« Les « niches fiscales », côté recettes, sont au chapitre 3 », traitées au chapitre 3 étape 11). À rétablir dès que les chiffres et le passage du chapitre 3 existent.
2. Aides aux entreprises écartées de la comparaison du sondage, étape 6 (gauche, moyenne) : **appliqué**. Phrase ajoutée avec `business_aid_range_eur_bn` et le calcul en jours (9,6 ; 44,9) ; visuel : barre de fourchette au lieu d’un simple renvoi.
3. Dernier mot laissé au « déficit caché », étape 7 (gauche, faible) : **appliqué**. Ajout : « lecture que la Cour des comptes a écartée en février 2025 ».
4. Convention du solde des retraites sans chiffre, étape 7 (droite, moyenne) : **partiellement appliqué**. La réponse nomme déjà la contribution d’équilibre de l’État employeur ; la pastille de 49,3 Md€ n’est pas ajoutée car `pension_state_balancing_contribution_2025_eur_bn` n’existe pas encore dans figures.json (règle : aucun chiffre sans pastille). À ajouter avec `pension_balance_convention_range_pct_gdp` une fois créés (research/03 §5, COR juin 2026, tableau 2.2). Volet chapitre 7 hors périmètre de ce fichier.
5. Coût en emplois des allègements généraux absent de la précaution, étape 9 (droite, faible) : **appliqué**, avec `[[fig:contribution_relief_abolition_jobs_fte]]`.
6. Durées et dates du calendrier qui ne concordent pas au jour près, étape 3e (chiffres, faible) : **appliqué**. Phrase d’explication ajoutée après « Le 31 décembre vient des arrondis ».
7. « En comptabilité nationale » laissait croire que la COFOG n’en relève pas, étape 3c (chiffres, faible) : **appliqué**. Nouvelle formulation D.41 2025, « soit 14 jours » avec calcul (13,9), et une phrase qui précise que les deux chiffres diffèrent par l’année et le concept.
8. Arrondis différents d’un chapitre à l’autre (chiffres, faible) : **partiellement appliqué**. Dans ce chapitre : « 32,3 jours » (étape 3f) et « 1 714,1 milliards » (étapes 0, 2, 11 et visuel) ; « 151 jours » et « environ 6 milliards » étaient déjà conformes. Corrections des chapitres 3, 6 et 7 hors périmètre de ce fichier.
9. Même « 24 800 € » rattaché à deux ids (chiffres, faible) : **appliqué**. `[[yard:te_per_capita_eur]]` remplacé par `[[fig:te_per_capita_2025_eur]]`, comme au chapitre 1.
10. Unité « % du PIB » manquante au chapitre 1 (chiffres, faible) : **rejeté pour ce fichier**. Le constat porte sur le chapitre 1 ; dans ce chapitre, les deux valeurs SOCX (étape 10) sont déjà étiquetées « % du PIB ».
11. Pastilles `[[calc:]]` sans résultat (chiffres, faible) : **appliqué**. Résultat ajouté à chaque calcul (39,0 ; 0,32 ; 13,9 ; 571 ; 82,1 ; 6,9 ; 47,9 ; 9,6-44,9 ; 89,9 ; 6 119 ; 2,78 ; 7,3 ; 2,8 ; 1,4-2,0 ; 1,0-2,7 ; 6,8), au format des chapitres 1, 4 et 5.

**Passe « pastilles et coupes » (25 octobre 2026, après la passe données « Data pass for the chapters, second pass » de platform/data/REVIEW.md)**
- Pastilles : les 22 `[[fig-a-creer:…]]` remplacées par `[[fig:…]]` (13 ids : 9 COFOG `*_2024_pct_te`, 3 parts Drees, `gap2024_health_sha_pp`). Aucun bloc d’attente de données dans ce chapitre. Aucune valeur déclarée invérifiable par la passe données ne concernait ce chapitre.
- Nouveaux étalons branchés : `calendar_days_general_public_services`, `calendar_days_interest_cofog`, `calendar_days_economic_affairs`, `calendar_days_public_order`, `calendar_days_recreation_culture`, `calendar_days_housing_amenities`, `calendar_days_environment`, `calendar_days_gps_excl_interest`. Leurs durées en jours (39, 36, 11, 9, 9, 7, 27) sont désormais affichées. Le `[[calc:]]` des intérêts (× 365) et celui du train de vie (× 365) sont remplacés par ces étalons.
- Vérification : chaque pastille résout dans figures.json / yardsticks.json (paramètre `household_monthly_income_eur` compris), et chaque valeur affichée correspond, au format français, à la valeur des fichiers (10,8 % ; 3,5 % ; 9,9 % ; 3,1 % ; 2,6 % ; 2,5 % ; 1,8 % ; 4,0 + 2,9 ; 45,8 % ; 36,3 % ; 17,9 % ; +1,06 point). `python3 -I validate.py` : 0 erreur pour ce chapitre.
- Nouvelle formulation (étape 10) : « de 1 à 1,5 point de PIB selon la nomenclature » remplacé par les deux valeurs exactes (+1,5 COFOG ; +1,06 SHA), toutes deux en pastille.
- Coupes (texte affiché, mesuré par script : 2 281 → 1 911 mots ; objectif 1 500-2 200) : redites de l’ouverture et de l’étalon ; « 1,16 Md€ par jour » des retraites (redondant avec 90 jours) ; montants Drees famille (65,8 Md€) et pauvreté (34,0 Md€), renvoyés à la fiche Protection sociale par risque ; niveau de vie des retraités (100,2 %) déplacé dans la carte perception ; part de l’écart en % (46 %, 19 %) et rang par habitant des pensions (5e) retirés du texte, gardés dans le comparateur ; spécifications visuelles resserrées. Ajout d’une liste « Pour aller plus loin » vers les fiches thématiques (fichier 20 §4.2-4.5, §4.12, §4.15-4.17).
- Durée de lecture : « environ 2 minutes » remplacé par « environ 8 minutes » (environ 1 900 mots affichés, environ 240 mots par minute). À arbitrer avec le fichier 20 §2.1, qui prévoit environ 12 minutes pour les 7 chapitres.
- Conservé : ouverture « Estimez d’abord », étalons (jour de dépense, ménage), comparaison internationale datée avec groupe (ZE21, UE27, OCDE), deux encadrés « Le meilleur contre-argument », transition.

**Relecture précédente (25 octobre 2026, chiffres, neutralité, français), résumé**
- Chiffres : calculs refaits (dates, 571 €, 48 %, 90 jours, 6 100 €, 2,8 fois, heures d’AME) ; Ondam distingué de la dépense COFOG de santé ; périmètre Drees corrigé (Agirc-Arrco dans les deux nomenclatures ; la différence vient des organismes privés et du rangement de la santé) ; écart 90 jours (COR) / 85 jours (COFOG) expliqué ; contre-argument SOCX distingué du 32,0 % Eurostat.
- Neutralité : étape 9 rééquilibrée (cibles de droite listées par le fichier 20, même précaution sur chaque ligne, précaution sur le haut de la fourchette des aides aux entreprises) ; contre-argument retraites renforcé (Cour des comptes, février 2025) et « déficit caché » attribué à la Fondation iFRAP ; orientation du commanditaire du sondage M8 reprise de quiz.json ; jugements supprimés (« C’est beaucoup », « n’est que 7e »).
- Français : signes moins retirés du texte courant (glossaire §2.2) ; typographie laissée au filtre de rendu (glossaire §2.1).
