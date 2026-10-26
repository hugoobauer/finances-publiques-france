# Chapitre 6. Qu’obtient-on en échange ?

*Script de récit défilant (scrollytelling) pour le site public. Version de travail du 25 octobre 2026, à relire par l’équipe éditoriale.*

<!--
NOTES POUR L’ÉQUIPE (non affichées)
- Place dans le parcours : récit, chapitre 6 sur 7 (fichier 20, §2.1). Avant : chapitre 5 « La dette et ses intérêts ». Après : chapitre 7 « Les choix ».
- Chiffres : uniquement platform/data/figures.json et platform/data/yardsticks.json (état du 25 octobre 2026).
- Pastilles source :
  [[fig:id]]  = une valeur de figures.json ;
  [[yard:id]] = un étalon de yardsticks.json ;
  [[calc:...]] = un calcul de la plateforme (mention « illustratif »), formule donnée sur des identifiants de figures.json et yardsticks.json ;
  [[src:id]]  = une source de sources.json, pour une affirmation sans chiffre.
- Seul le contenu des blocs « Texte affiché » est visible. Les blocs « Visuel », « Devinez d’abord » et « Pastilles » sont des consignes de production.
- Composant « Devinez d’abord » : le libellé public est « Estimez d’abord » (glossaire, §1.13).
- Typographie : le filtre de rendu applique les espaces insécables, les apostrophes typographiques et le signe moins (glossaire, §2.1).
-->

---

## Étape 0. Ouverture

**Texte affiché**

> **Qu’obtient-on en échange ?**
>
> Vous savez combien la France dépense, qui paie et combien elle emprunte. Reste une question simple : qu’est-ce que cet argent permet d’obtenir ?
>
> Ce chapitre compare cinq résultats : pauvreté, santé, école, justice, emploi. Ils ne dépendent pas seulement de l’argent public, mais ils montrent où la dépense « rapporte » et où elle rapporte moins.
>
> Durée de lecture : environ 8 minutes.

**Visuel et animation**
- Plein écran : cinq pictogrammes (pauvreté, santé, école, justice, emploi) apparaissent l’un après l’autre, chacun avec un point d’interrogation.
- Aucun chiffre à cette étape.

**Pastilles** : aucune.

---

## Étape 1. Estimez d’abord : où la France fait-elle mieux que la moyenne ?

**Texte affiché**

> Avant de voir les chiffres, faites votre propre pronostic.
>
> Pour chacun des cinq domaines, la France fait-elle **mieux**, **à peu près pareil** ou **moins bien** que la moyenne des pays comparables ?
>
> Nous vous montrerons vos réponses à la fin du chapitre.

**Devinez d’abord** (libellé public : « Estimez d’abord »)
- Type : jeu de tri. Cinq cartes à glisser dans trois colonnes : « Mieux », « À peu près pareil », « Moins bien ».
- Cartes : « Pauvreté après impôts et prestations » ; « Espérance de vie » ; « Niveau en mathématiques des élèves de 15 ans » ; « Taux d’emploi » ; « Pauvreté des personnes âgées ».
- Réponses attendues (révélées à l’étape 8) :
  - pauvreté après transferts : à peu près pareil (UE-27, 2025) [[fig:arop_2025_pct]] [[fig:eu27_arop_2025_pct]] ;
  - espérance de vie : mieux (UE-27, 2024) [[fig:life_expectancy_2024_years]] [[fig:eu27_life_expectancy_2024_years]] ;
  - mathématiques : moins bien (OCDE, PISA 2025) [[fig:pisa_math_2025]] [[fig:oecd_pisa_math_2025]] ;
  - taux d’emploi : moins bien (UE-27, 2025) [[fig:employment_rate_2025_pct]] [[fig:eu27_employment_rate_2025_pct]] ;
  - pauvreté des personnes âgées : mieux (OCDE, 2022) [[fig:old_age_poverty_oecd_2022_pct]] [[fig:oecd_old_age_poverty_2022_pct]].
- La justice n’est pas dans le jeu : la base de données n’a pas encore d’indicateur chiffré pour ce domaine (voir étape 6).
- Enregistrer les réponses de façon anonyme pour afficher, à l’étape 8, la répartition des réponses des autres lecteurs.

**Pastilles** : aucune à cette étape (les chiffres arrivent à la révélation).

---

## Étape 2. Ce que l’on paie : les deux tiers de l’année

**Texte affiché**

> Rappel du chapitre 2, « Où va l’argent ? » : en 2024, trois postes absorbent les deux tiers des dépenses publiques.
>
> - La **protection sociale** (retraites, famille, chômage, minima sociaux) : 41,5 % des dépenses publiques [[fig:cofog_social_protection_2024_pct_te]], soit 23,6 % du produit intérieur brut (PIB) [[fig:cofog_social_protection_2024_pct_gdp]].
> - La **santé** : 15,6 % des dépenses publiques [[fig:cofog_health_2024_pct_te]], soit 8,9 % du PIB [[fig:cofog_health_2024_pct_gdp]].
> - L'**enseignement** : 8,9 % des dépenses publiques [[fig:cofog_education_2024_pct_te]], soit 5,1 % du PIB [[fig:cofog_education_2024_pct_gdp]].
>
> Dans le calendrier de la dépense publique, ces trois postes occupent environ 241 jours sur 365 [[calc:(cofog_social_protection_2024_pct_te + cofog_health_2024_pct_te + cofog_education_2024_pct_te) / 100 × days_in_year = 240,9]].
>
> Ramené à une personne, la dépense publique représente 68 € par habitant et par jour [[yard:te_per_capita_per_day_eur]]. Sur cette somme, environ 28 € vont à la protection sociale [[calc:te_per_capita_per_day_eur × cofog_social_protection_2024_pct_te / 100 = 28,2]], 11 € à la santé [[calc:te_per_capita_per_day_eur × cofog_health_2024_pct_te / 100 = 10,6]] et 6 € à l’enseignement [[calc:te_per_capita_per_day_eur × cofog_education_2024_pct_te / 100 = 6,1]].

**Visuel et animation**
- Ruban annuel du calendrier (composant du chapitre 2). Les trois blocs se colorent l’un après l’autre : protection sociale (151 jours), santé (57 jours), enseignement (32 jours), arrondis comme au chapitre 2. Les autres fonctions restent grises.
- Compteur « jours » qui monte jusqu’à 241.
- Puis bascule vers une pièce de 68 € qui se découpe en trois parts (28 €, 11 €, 6 €) et un reste gris (23 €, non affiché en texte).
- Note sous le graphique : « Parts 2024 (dernières données par fonction) appliquées à la dépense 2025 : ordre de grandeur. »

**Pastilles**
- 41,5 % [[fig:cofog_social_protection_2024_pct_te]] ; 23,6 % [[fig:cofog_social_protection_2024_pct_gdp]]
- 15,6 % [[fig:cofog_health_2024_pct_te]] ; 8,9 % du PIB [[fig:cofog_health_2024_pct_gdp]]
- 8,9 % des dépenses publiques [[fig:cofog_education_2024_pct_te]] ; 5,1 % [[fig:cofog_education_2024_pct_gdp]]
- 151 jours [[yard:calendar_days_social_protection]] ; 57 jours [[yard:calendar_days_health]] ; 32 jours [[yard:calendar_days_education]] (visuel seulement ; valeurs 151,5 / 56,9 / 32,5 arrondies à l’entier comme au chapitre 2)
- 241 jours [[calc:(cofog_social_protection_2024_pct_te + cofog_health_2024_pct_te + cofog_education_2024_pct_te) / 100 × days_in_year = 240,9]]
- 68 € [[yard:te_per_capita_per_day_eur]]
- 28 € / 11 € / 6 € [[calc:te_per_capita_per_day_eur × cofog_social_protection_2024_pct_te / 100 = 28,2]] [[calc:te_per_capita_per_day_eur × cofog_health_2024_pct_te / 100 = 10,6]] [[calc:te_per_capita_per_day_eur × cofog_education_2024_pct_te / 100 = 6,1]] (illustratif)

---

## Étape 3. Pauvreté : dans la moyenne européenne

**Devinez d’abord** (libellé public : « Estimez d’abord »)
- Question : « Selon vous, quelle part de la population vit sous le seuil de risque de pauvreté en France, après impôts et prestations sociales ? »
- Curseur de 0 à 40 %, pas de 1 point. Puis une seconde question : « Et dans l’ensemble de l’Union européenne ? »
- Révélation : barre de l’utilisateur, barre de la moyenne des réponses des lecteurs, puis valeur réelle.
<!-- estimez-réponse: arop_2025_pct, eu27_arop_2025_pct -->

**Texte affiché**

> En 2025, 16,3 % des personnes vivant en France sont sous le seuil de risque de pauvreté, après impôts et prestations sociales [[fig:arop_2025_pct]]. Eurostat parle de « taux de risque de pauvreté après transferts sociaux ». C’est exactement le niveau de l’Union européenne dans son ensemble [[fig:eu27_arop_2025_pct|contexte]].
>
> La France a le 11e taux le plus élevé des 27 pays de l’UE [[fig:arop_2025_rank]].
>
> Le taux était de 13,6 % de la population en 2015 [[fig:arop_2015_pct]]. L’enquête a changé de méthode en 2020 et en 2022 : une partie de la hausse peut venir de ces changements [[src:f10]].
>
> Mais la mesure nationale de l’Institut national de la statistique et des études économiques (Insee) est calculée autrement, et elle confirme la hausse. Elle atteint 15,4 % de la population sur les revenus de 2024 [[fig:poverty_national_2024_pct]], son plus haut niveau depuis 1996 [[src:f10]].

**Visuel et animation**
- Graphique en points (dot plot) des 27 pays de l’UE, triés du taux le plus bas au plus élevé. Point de la France en couleur d’accent, ligne verticale pour l’UE-27.
- Axe : « en % de la population ». Titre : « Taux de risque de pauvreté après transferts sociaux, EU-SILC 2025 ».
- Animation : le point de la France glisse de 13,6 (2015) à 16,3 (2025). Marqueurs « rupture de série » en 2020 et 2022.
- La mesure Insee (15,4 %) s’affiche dans une carte séparée, avec la mention « Mesure nationale : ne pas comparer directement avec le taux européen » (glossaire, §1.10).
- Données pays : `data/eurostat_ilc_li02.csv` (fichier 20, §4.3).

**Pastilles**
- 16,3 % [[fig:arop_2025_pct]] ; UE-27 16,3 % [[fig:eu27_arop_2025_pct]]
- 11e taux le plus élevé sur 27 [[fig:arop_2025_rank]] (rang 1 = taux le plus élevé)
- 13,6 % en 2015 [[fig:arop_2015_pct]] (mention « rupture de série » obligatoire, note de la figure) ; changements de méthode 2020 et 2022 [[src:f10]]
- 15,4 % [[fig:poverty_national_2024_pct]] ; « plus haut depuis 1996 » [[src:f10]]

---

## Étape 4. Personnes âgées : un résultat net

**Texte affiché**

> Le tableau change pour les personnes âgées.
>
> En France, 6,1 % des 65 ans et plus vivent sous le seuil de pauvreté en 2022 [[fig:old_age_poverty_oecd_2022_pct]]. La source est l’Organisation de coopération et de développement économiques (OCDE). Ce seuil est fixé à la moitié du revenu médian. La moyenne des pays de l’OCDE est de 14,8 % des 65 ans et plus [[fig:oecd_old_age_poverty_2022_pct]].
>
> La mesure européenne place le seuil plus haut, aux trois cinquièmes du revenu médian. Avec elle, 11,6 % des 65 ans et plus sont sous le seuil de risque de pauvreté en 2025 [[fig:old_age_poverty_eu_2025_pct]]. C’est nettement moins que pour l’ensemble de la population (16,3 %) [[fig:arop_2025_pct]].
>
> Selon le Conseil d’orientation des retraites (COR), le niveau de vie moyen des retraités égale celui de l’ensemble de la population. Il en représente 100,2 % en 2023 [[fig:retirees_relative_living_standard_pct]].
>
> Ce résultat a un coût : les retraites sont le premier poste de la dépense publique (chapitre 2).

**Visuel et animation**
- Deux barres horizontales côte à côte : France 6,1 % / moyenne OCDE 14,8 %. Axe : « en % des 65 ans et plus (seuil de 50 % du revenu médian), 2022 ».
- Puis deux barres France seule, seuil européen de 60 % : population totale 16,3 % / 65 ans et plus 11,6 %. Les deux graphiques gardent leur propre titre de seuil : ne pas mélanger les seuils de 50 % et 60 % sur un même axe.
- Jauge « niveau de vie des retraités / ensemble de la population » avec l’aiguille sur 100,2.

**Pastilles**
- 6,1 % [[fig:old_age_poverty_oecd_2022_pct]] ; 14,8 % [[fig:oecd_old_age_poverty_2022_pct]]
- 11,6 % [[fig:old_age_poverty_eu_2025_pct]] ; 16,3 % [[fig:arop_2025_pct]]
- 100,2 % [[fig:retirees_relative_living_standard_pct]]

---

## Étape 5. Santé : de bons résultats, des tensions sur l’accès

**Devinez d’abord** (libellé public : « Estimez d’abord »)
- Question : « Combien d’années vit-on en moyenne en France, à la naissance ? » Curseur de 75 à 90 ans, pas de 0,5. Révélation avec la moyenne UE-27.
<!-- estimez-réponse: life_expectancy_2024_years -->

**Texte affiché**

> La santé est le 2e poste de la dépense publique : 8,9 % du PIB en 2024 [[fig:cofog_health_2024_pct_gdp]]. C’est 1,5 point de PIB de plus que la zone euro à 21 pays (ZE21, Bulgarie comprise) dans son ensemble [[fig:gap2024_health_pp]]. Ce calcul suit la classification des fonctions des administrations publiques (COFOG). L’écart est plus faible avec d’autres définitions [[src:f12]].
>
> Par habitant et à coût de la vie égal, la France dépense moins pour sa santé que l’Allemagne, les Pays-Bas, la Belgique ou la Suède. Ce calcul compte la dépense publique et la dépense privée [[src:f12]].
>
> **Ce qui va bien.** L’espérance de vie à la naissance atteint 83,0 ans en 2024 [[fig:life_expectancy_2024_years]], contre 81,5 ans dans l’Union européenne à 27 pays (UE-27) [[fig:eu27_life_expectancy_2024_years]]. La France est 7e sur 27 [[fig:life_expectancy_2024_rank]].
>
> Six pays de l’UE font mieux [[calc:life_expectancy_2024_rank - 1 = 6]], dont l’Espagne, la Suède et l’Italie. Ces trois pays consacrent moins de dépense publique à la santé et à la protection sociale [[src:f10]].
>
> Autres points forts : la mortalité qui aurait pu être évitée par des soins est parmi les plus basses d’Europe. Le reste à charge des ménages (la part des soins qu’ils paient eux-mêmes) est parmi les plus faibles d’Europe [[src:f12]].
>
> **Ce qui va moins bien.** Le renoncement aux soins pour cause de délais augmente depuis 2021, en partie à cause d’un changement de méthode de l’enquête. La France est dans le tiers le moins bien placé de l’UE. La survie après un cancer est dans la moyenne de l’OCDE, pas en tête [[src:f12]].
>
> **Où sont les marges ?** Les frais de gestion sont les plus élevés de l’UE. C’est surtout parce que deux assurances se superposent : l’Assurance maladie et les complémentaires santé [[src:f12]]. Le chapitre 2 chiffre ce réservoir et celui des soins de faible valeur.

**Visuel et animation**
- Graphique 1 : barres de l’espérance de vie à la naissance, 2024, pays de l’UE-27 triés. France en couleur d’accent, ligne UE-27. Axe : « en années ».
- Graphique 2 : bandeau « Ce que l’on obtient » (composant partagé) avec trois pastilles qualitatives : « mortalité évitable par les soins : parmi les plus basses de l’UE », « reste à charge : parmi les plus faibles », « délais d’accès : en hausse depuis 2021 ». Pas de chiffre affiché tant que ces indicateurs ne sont pas dans `figures.json` (voir notes).

**Pastilles**
- 8,9 % du PIB [[fig:cofog_health_2024_pct_gdp]] ; +1,5 point [[fig:gap2024_health_pp]] (comparaison : zone euro ZE21, 2024) ; « plus faible avec d’autres définitions » et dépense par habitant en standard de pouvoir d’achat [[src:f12]]
- 83,0 ans [[fig:life_expectancy_2024_years]] ; 81,5 ans [[fig:eu27_life_expectancy_2024_years]] ; 7e sur 27 [[fig:life_expectancy_2024_rank]] ; six pays devant [[calc:life_expectancy_2024_rank - 1 = 6]] ; Espagne, Suède et Italie devant la France avec une dépense publique de santé et de protection sociale plus faible [[src:f10]] (fichier 10, §8.2 ; valeurs pays à ajouter à figures.json avant de les afficher, voir note 1)
- Mortalité évitable, reste à charge, délais (et rupture de série), survie après un cancer, frais de gestion « les plus élevés de l’UE » [[src:f12]]
- Renvoi au chapitre 2 (étape 8) pour le chiffrage des réservoirs (frais de gestion, soins de faible valeur) : aucun montant affiché ici.

---

## Étape 6. École et justice : sous la moyenne

**Devinez d’abord** (libellé public : « Estimez d’abord »)
- Question : « En mathématiques, les élèves français de 15 ans sont-ils au-dessus, dans ou en dessous de la moyenne de l’OCDE ? » Trois boutons. Révélation immédiate.
<!-- estimez-réponse: pisa_math_2025, oecd_pisa_math_2025 -->

**Texte affiché**

> **L’école.** Selon l’enquête 2025 du Programme international pour le suivi des acquis des élèves (PISA), les élèves de 15 ans obtiennent 458 points en mathématiques [[fig:pisa_math_2025]]. La moyenne de l’OCDE est de 463 points [[fig:oecd_pisa_math_2025]]. La France est 29e sur 38 pays de l’OCDE [[fig:pisa_math_2025_rank]]. Sa baisse depuis 2015 est l’une des plus fortes, même si la moyenne de l’OCDE a aussi baissé [[src:f13]].
>
> L’argent n’explique qu’une petite partie de ces écarts. Parmi les pays riches, ceux qui dépensent le plus par élève n’ont pas toujours les meilleurs scores [[src:f13]]. La France dépense à peu près autant par élève que la moyenne de l’OCDE, mais paie ses enseignants moins que cette moyenne [[src:f04]].
>
> **La justice.** Les comparaisons européennes montrent moins de juges par habitant en France que dans la plupart des pays européens. Les procès civils y sont aussi plus longs. Deux nuances : le budget de la justice par habitant est au-dessus de la médiane européenne, mais sous la moyenne. Et l’organisation des tribunaux diffère d’un pays à l’autre [[src:f04]] [[src:f10]].

**Visuel et animation**
- Graphique 1 : nuage de points « dépense par élève / score PISA 2025 », pays de l’OCDE, France en couleur d’accent, droite de tendance (fichier 20, §4.2, GF09 ; données `data/13_pisa2025_country_values.csv`). Les valeurs des autres pays sont dans le fichier de données ; le texte n’en cite aucune.
- Animation : la ligne « moyenne OCDE » (463) se dessine, puis le point France (458) apparaît sous la ligne.
- Graphique 2 (justice) : **bloqué avant publication** (règle de publication du plan de site : les contre-preuves des deux camps doivent être chiffrées de la même façon). Prévu : petits multiples « juges pour 100 000 habitants » (fichier 20, §4.2, GF03). `judges_per_100k_2022` (11,3) et `cepej_median_judges_2022` (17,6) ne sont toujours pas dans `figures.json` : la passe de données du 25 octobre 2026 n’a pas pu ouvrir la source primaire CEPEJ (coe.int refuse l’accès automatisé), et seule une source secondaire (Le Club des juristes) les confirme. À vérifier dans un navigateur. En attendant, afficher seulement le texte qualitatif ci-dessus.

**Pastilles**
- 458 [[fig:pisa_math_2025]] ; 463 [[fig:oecd_pisa_math_2025]] ; 29e sur 38 [[fig:pisa_math_2025_rank]]
- Baisse depuis 2015, lien dépense-score [[src:f13]] ; dépense par élève et salaire des enseignants [[src:f04]]
- Justice (juges, durée des procès, budget par habitant, limites de la comparaison) [[src:f04]] [[src:f10]]

---

## Étape 7. Emploi : un point faible qui pèse sur les comptes

**Texte affiché**

> L’emploi n’est pas une dépense, mais il conditionne tout le reste. Plus de personnes en emploi, c’est plus de cotisations et d’impôts, et moins de prestations.
>
> En 2025, 69,3 % des personnes de 15 à 64 ans ont un emploi en France [[fig:employment_rate_2025_pct]], contre 71,0 % dans l’UE-27 [[fig:eu27_employment_rate_2025_pct]]. La France est 21e sur 27 [[fig:employment_rate_2025_rank]].
>
> Rapporté à toute la population, le nombre d’heures travaillées est le plus faible de l’UE. Il est de 666 par habitant et par an [[fig:hours_per_inhabitant_2025]], au 27e rang sur 27 [[fig:hours_per_inhabitant_2025_rank]]. Cet indicateur divise les heures par toute la population, élèves, étudiants et retraités compris : il dépend donc aussi de la démographie.
>
> Le chapitre 7 chiffre ce que rapporterait un taux d’emploi plus élevé.
>
> Nuance : ceux qui ont un emploi travaillent plus d’heures qu’en Allemagne ou aux Pays-Bas (mais moins que la moyenne de l’UE). Le retard vient surtout du faible taux d’emploi des jeunes et des seniors [[src:f08]].
>
> Et par heure travaillée, la productivité française reste au-dessus de la moyenne de l’UE. En 2025, elle atteint l’indice 114,6 en standards de pouvoir d’achat (SPA), pour une moyenne de l’UE à 100 [[fig:productivity_per_hour_pps_2025]]. La France est 8e sur 27 [[fig:productivity_per_hour_pps_2025_rank]]. C’est en partie parce que les moins qualifiés sont plus souvent sans emploi. Elle a toutefois reculé depuis 2019 [[src:f08]].

**Visuel et animation**
- Graphique en pente (slope chart) 2009 → 2025 : taux d’emploi France vs UE-27 (fichier 20, §4.13 ; `data/08_eurostat_lfsi_emp_a.csv`). Le texte ne cite que 2025.

**Pastilles**
- 69,3 % [[fig:employment_rate_2025_pct]] ; 71,0 % [[fig:eu27_employment_rate_2025_pct]] ; 21e sur 27 [[fig:employment_rate_2025_rank]]
- 666 heures [[fig:hours_per_inhabitant_2025]] ; 27e sur 27 [[fig:hours_per_inhabitant_2025_rank]]
- Heures par personne en emploi : plus élevées qu’en Allemagne et aux Pays-Bas, plus basses que la moyenne UE-27 ; rôle de l’emploi des jeunes et des seniors [[src:f08]] ; renvoi au chapitre 7 (étape 7) pour le levier emploi chiffré par la DG Trésor
- 114,6 (SPA, UE-27 = 100) [[fig:productivity_per_hour_pps_2025]] ; 8e sur 27 [[fig:productivity_per_hour_pps_2025_rank]] (Eurostat nama_10_lp_ulc, 22 octobre 2026, source [[src:f08:es-lp]])
- Effet de sélection, recul depuis 2019 [[src:f08]] (fichier 08, l. 261-268 : −0,8 % en volume sur 2019-2025, non affiché faute de figure)

---

## Étape 8. Le bilan : vos pronostics face aux résultats

**Texte affiché**

> Voici le bilan, comparé à vos pronostics de départ.
>
> **Mieux que la moyenne :** espérance de vie, pauvreté des personnes âgées, mortalité évitable par les soins, reste à charge des ménages.
>
> **Dans la moyenne :** pauvreté de l’ensemble de la population, survie après un cancer.
>
> **Moins bien que la moyenne :** mathématiques à 15 ans, taux d’emploi, heures travaillées par habitant, juges par habitant, renoncement aux soins pour délais.
>
> Un résultat se lit à part : la redistribution. Avant prestations sociales (retraites comprises), 46,8 % de la population serait sous le seuil de risque de pauvreté en 2025 [[fig:arop_before_transfers_2025_pct]]. C’est l’un des taux les plus élevés de l’UE. Après prestations, la France revient dans la moyenne [[fig:arop_2025_pct|contexte]].
>
> Les prestations font donc baisser ce taux de 30,5 points [[fig:poverty_reduction_transfers_2025_pp]], la 3e baisse de l’UE [[fig:poverty_reduction_transfers_2025_rank]]. Les retraites en font la plus grande part. Or elles remplacent en partie un revenu d’activité passé, ce qui grossit cet effet [[src:f10:S33]].
>
> Selon l’Insee, 56 % des personnes reçoivent plus qu’elles ne paient en 2023 (chapitre 3) [[fig:net_beneficiaries_2023_pct]]. Ce calcul compte aussi les services publics comme l’école et l’hôpital.
>
> Les meilleurs résultats se trouvent là où la France dépense le plus : retraites et santé. Mais d’autres pays obtiennent des résultats proches ou meilleurs en dépensant moins [[src:f10]].
>
> Ailleurs, ils sont moyens ou faibles, y compris là où la dépense est proche de la moyenne, comme à l’école. Ces rapprochements ne prouvent pas que la dépense soit la seule cause des résultats, dans un sens ou dans l’autre.

**Visuel et animation**
- Tableau de bord à trois colonnes (Mieux / Pareil / Moins bien). Les cartes de l’utilisateur (étape 1) se placent à gauche de chaque ligne, les bonnes réponses à droite ; une coche ou une croix s’affiche.
- Chaque ligne rappelle l’indicateur, l’année et le groupe de comparaison : UE-27 2025 (pauvreté, emploi), UE-27 2024 (espérance de vie), OCDE 2022 (pauvreté des 65 ans et plus), OCDE PISA 2025 (mathématiques).
- Afficher la répartition des réponses des autres lecteurs (« X % des lecteurs pensaient… » : valeur calculée en direct, jamais saisie à la main).

**Pastilles**
- Celles des étapes 3 à 7, reprises au survol de chaque ligne.
- Redistribution : avant et après prestations sociales [[src:f10]] ; 56 % [[fig:net_beneficiaries_2023_pct]] (Insee, *Insee Analyses* n° 118, 16 avril 2026 ; même valeur qu’au chapitre 3).
- 46,8 % avant prestations, retraites comprises [[fig:arop_before_transfers_2025_pct]] (source [[src:f01:es-silc]], Eurostat ilc_li09) ; 30,5 points [[fig:poverty_reduction_transfers_2025_pp]] (statut « réserve » : surtout les retraites, en partie revenu différé) ; 3e sur 27 [[fig:poverty_reduction_transfers_2025_rank]] (source [[src:f10:S33]], calcul de la plateforme d’après Eurostat ilc_li09 et ilc_li02).

---

## Étape 9. Le meilleur contre-argument

**Texte affiché**

<!-- box-side: droite -->
> **Le meilleur contre-argument**
>
> **« Les résultats ne justifient plus le niveau de la dépense : l’argent est mal utilisé. »**
>
> Pour le Fonds monétaire international (FMI ; organisation internationale), la France doit « rationaliser les dépenses inefficaces » (traduit de l’anglais) [[src:f06:imf_aiv2026]]. La Cour des comptes (juridiction financière) regrette l’absence d’effort global d’économies en 2025 [[src:f20:cour26]].
>
> Les chiffres de la pauvreté vont dans ce sens. Le taux après transferts est aujourd’hui exactement dans la moyenne européenne [[fig:arop_2025_pct|contexte]] [[fig:eu27_arop_2025_pct|contexte]]. Il était de 13,6 % de la population en 2015 [[fig:arop_2015_pct]]. La Belgique obtient une baisse comparable et arrive à un taux plus bas [[src:f10:S33]].
>
> Sans les retraites, les transferts ne font plus baisser le taux que de 10,2 points [[fig:poverty_reduction_excl_pensions_2025_pp]]. La France n’est alors que 6e de l’UE [[fig:poverty_reduction_excl_pensions_2025_rank]]. Et les comptes publics étant en déficit, l’Insee (institut public de statistique) note que l’ensemble est en partie financé par l’emprunt [[src:f10]].
>
> *Sources : FMI (organisation internationale), déclaration de fin de mission au titre de l’article IV, 21 mai 2026 ; Cour des comptes (juridiction financière),* *La situation et les perspectives des finances publiques*, *25 juin 2026 ; Eurostat (office statistique de l’Union européenne), statistiques de l’Union européenne sur le revenu et les conditions de vie (EU-SILC), 2025.*
>
> **Ce qu’on peut répondre**
>
> La redistribution fait un travail réel. Retraites comprises, la baisse du taux de pauvreté est la 3e de l’UE (étape 8) [[fig:poverty_reduction_transfers_2025_rank]]. Une partie de la hausse depuis 2015 peut aussi tenir aux changements de méthode de l’enquête [[src:f10]].
>
> Certains services manquent de moyens plutôt que d’efficacité. La France a moins de juges par habitant que la plupart des pays européens. Elle paie ses enseignants moins que la moyenne des pays de l’OCDE [[src:f04]] [[src:f10]]. Les résultats dépendent aussi d’autres facteurs que le budget : inégalités sociales, démographie, modes de vie [[src:f04]].
>
> Sur un point, l’objection tient : hors retraites, l’effet des transferts français est bon, sans être exceptionnel [[src:f01:es-silc]].

**Visuel et animation**
- Encadré fixe, jamais replié (glossaire, §4.6), sur le même écran que le bilan de l’étape 8.
- Mini-graphique « avant / après transferts » par pays (dot plot double, fichier 20, §4.14 ; `data/debates/computed_poverty_reduction_by_transfers.csv`). Seules les valeurs françaises sont dans `figures.json` (46,8 % ; 30,5 et 10,2 points ; 3e et 6e rangs) ; les valeurs des autres pays restent au survol, sans être citées dans le texte.

**Pastilles**
- « exactement dans la moyenne européenne » [[fig:arop_2025_pct|contexte]] [[fig:eu27_arop_2025_pct|contexte]] (16,3 % chacun, affiché à l’étape 3) ; 13,6 % en 2015 [[fig:arop_2015_pct]] (mention « rupture de série »)
- Belgique (baisse de 30,7 points, taux plus bas) [[src:f10:S33]] ; « l’ensemble est en partie financé par l’emprunt » [[src:f10]]
- 10,2 points [[fig:poverty_reduction_excl_pensions_2025_pp]] (statut « réserve » : retraites comptées comme revenu ; moyenne UE-27 8,1, non affichée) ; 6e sur 27 [[fig:poverty_reduction_excl_pensions_2025_rank]] [[src:f01:es-silc]]
- FMI, déclaration de fin de mission au titre de l’article IV, 21 mai 2026 (citation traduite de l’anglais) [[src:f06:imf_aiv2026]] ; Cour des comptes, *La situation et les perspectives des finances publiques*, 25 juin 2026 [[src:f20:cour26]]
- Réponse : 3e baisse de l’UE retraites comprises [[fig:poverty_reduction_transfers_2025_rank]] ; changements de méthode [[src:f10]] ; juges et salaires des enseignants [[src:f04]] [[src:f10]] ; facteurs hors budget [[src:f04]] ; « l’objection tient » hors retraites [[src:f01:es-silc]]

---

## Étape 10. Deux lectures du même bilan

**Texte affiché**

> Le même bilan nourrit donc deux lectures. Pour l’Union syndicale des magistrats (syndicat de magistrats), notamment, il manque des moyens. Couper partout aggraverait les difficultés de la justice, de l’école et de l’accès aux soins [[src:f10]] [[src:f04]] [[src:f12]].
>
> Pour la Cour des comptes, le FMI, l’Institut Montaigne (libéral-centriste) et la Fondation iFRAP (libérale), l’argent est mal utilisé [[src:f10]].
>
> Selon les domaines, les données donnent raison à l’une ou à l’autre. Le débat ne se résume donc pas à « dépenser plus ou moins » : il porte aussi sur **où** dépenser.

**Visuel et animation**
- Bloc de texte simple, sur le même écran que l’encadré de l’étape 9. Les deux lectures ont la même typographie et la même couleur neutre (règle de symétrie, fichier 20, P7).
- Sous le texte, liens vers les fiches thématiques (fonction publique et résultats ; santé ; éducation).

**Pastilles**
- Union syndicale des magistrats, justice, salaires des enseignants [[src:f10]] [[src:f04]] ; accès aux soins [[src:f12]] (CEPEJ, cycle 2024, données 2022, transcrite par l’USM, fichier 10, §8.1)
- Cour des comptes, FMI, Institut Montaigne (*Budget base zéro*, novembre 2025), Fondation iFRAP (*Revue* n° 270, septembre 2025) [[src:f10]] (fichier 10, §4.1 et §5.4)
- Étiquettes d’orientation : glossaire §1.13 après la décision D-labels (Institut Montaigne « libéral-centriste », financement dans la pastille source).

---

## Étape 11. Transition

**Texte affiché**

> Vous savez maintenant combien la France dépense, comment elle se finance et ce qu’elle obtient en échange.
>
> Reste la question la plus difficile : que faire ? Le vieillissement, l’emploi et la hausse des intérêts imposent des choix. Le chapitre 7, « Les choix », en présente l’ampleur.
>
> Vous pouvez aussi comparer vous-même la France à ses voisins, indicateur par indicateur.
>
> **Pour aller plus loin**
>
> - Fiche « Santé » : volumes et prix des soins, mortalité évitable, reste à charge, survie après un cancer.
> - Fiche « Fonction publique et résultats » : juges par habitant, salaires des enseignants, scores PISA en lecture et en sciences.
> - Fiche « Retraites » : niveau de vie des retraités et coût du système.
> - Fiche « Taux d’emploi, heures travaillées et productivité » : emploi des jeunes et des seniors, scénarios du Trésor.
> - Fiche « Protection sociale par risque » : pauvreté avant et après transferts, effet des retraites.
>
> **→ Chapitre 7 : Les choix**

**Visuel et animation**
- Deux boutons :
  - « Chapitre 7 : Les choix » (principal) ;
  - « Ouvrir le comparateur de pays » (secondaire), préréglé sur l’indicateur « taux de risque de pauvreté », UE-27, 2025.
- « Pour aller plus loin » : liens vers les fiches thématiques (fichier 20, §4.5, §4.6, §4.4, §4.13, §4.3), sans chiffre dans la liste.
- Rappel du score du jeu de tri de l’étape 1, avec un bouton de partage (« J’ai trouvé 3 résultats sur 5. Et vous ? »).

**Pastilles** : aucune.

---

<!--
NOTES POUR L’ÉQUIPE (non affichées), suite

1. Indicateurs absents de figures.json, à ajouter avant publication (valeurs dans les fichiers de recherche cités ; ne pas les saisir dans le texte avant leur intégration et leur validation par validate.py) :
   - Justice : juges professionnels pour 100 000 habitants et médiane européenne ; durée des procédures civiles en première instance (fichier 04, §6.4 ; fichier 10, §8.1 ; fichier 20, §4.2 GF03). Attention : les fichiers 04/20 et 10 citent des valeurs et médianes CEPEJ légèrement différentes ; arbitrer dans le fichier 00 d’abord.
   - Pauvreté : ~~taux avant transferts, réduction par les transferts avec et sans retraites, rang UE~~ (ajoutés le 25 octobre 2026 et affichés aux étapes 8 et 9) ; pauvreté des enfants (fichier 20, §4.3).
   - Santé : mortalité évitable par les soins et rang UE, reste à charge, part des frais de gestion dans la dépense de santé, survie au cancer, besoins non satisfaits pour délai (fichier 12, §0 et §5-6).
   - Éducation : évolution PISA depuis 2015, scores en lecture et en sciences, salaire des enseignants (fichier 13, §0 ; fichier 04, §6.1).
   - Ajouts demandés par l’audit du 25 octobre 2026 : `eu27_arop_2015_pct` (Eurostat ilc_li02, avec note de rupture de série ; fichier 10, §9.2) pour rétablir à l’étape 9 la comparaison « 13,6 % contre … pour l’UE en 2015 » ; espérance de vie 2024 de l’Espagne, de la Suède et de l’Italie (Eurostat demo_mlexpec, https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_mlexpec ; fichier 10, §8.2) pour l’étape 5 ; ~~`productivity_per_hour_pps_2025` et son rang~~ (ajoutés le 25 octobre 2026, affichés à l’étape 7).
   Une fois ajoutés, remplacer les formulations qualitatives des étapes 5 et 6 par les chiffres avec leurs pastilles [[fig:...]].
2. Année et groupe de chaque comparaison internationale : pauvreté UE-27, EU-SILC 2025 ; espérance de vie UE-27, 2024 ; pauvreté des 65 ans et plus OCDE, 2022 (seuil 50 %) ; PISA OCDE, 2025 ; emploi et heures UE-27, 2025 ; santé zone euro ZE21, COFOG 2024.
3. Calculs « illustratif » (étape 2) : formules du convertisseur d’yardsticks.json (`conversions`). Les montants de 2024 ou de 2022 rapportés à la dépense 2025 sont des ordres de grandeur.
4. Étapes 9 et 10 : vérifier avec l’équipe juridique l’attribution de chaque lecture à ses défenseurs (Union syndicale des magistrats ; Cour des comptes, FMI, Institut Montaigne, Fondation iFRAP) et les citations exactes (fichier 10, §4.1, §5.4, §8.1, §8.2 ; fichier 04, §8). Les syndicats d’enseignants ne sont plus cités : aucune prise de position de leur part n’a été retrouvée dans la base.
-->

---

## Notes de relecture

**Passe de finalisation du 25 octobre 2026 (pass : finalisation)**
1. *Chiffres de la passe de données (D-data-pass)* : **appliqué**. Étape 7 : productivité horaire 114,6 en SPA (UE = 100) [[fig:productivity_per_hour_pps_2025]], 8e sur 27 [[fig:productivity_per_hour_pps_2025_rank]]. Étape 8 : 46,8 % avant prestations, retraites comprises [[fig:arop_before_transfers_2025_pct]] ; baisse de 30,5 points [[fig:poverty_reduction_transfers_2025_pp]], 3e de l’UE [[fig:poverty_reduction_transfers_2025_rank]], avec la réserve de la figure (retraites en partie revenu différé). Étape 9 : 10,2 points hors retraites [[fig:poverty_reduction_excl_pensions_2025_pp]], 6e de l’UE [[fig:poverty_reduction_excl_pensions_2025_rank]]. Pastille FMI remplacée par [[src:f06:imf_aiv2026]] (l’entrée contient l’URL de la déclaration du 21 mai 2026), pastille Cour par [[src:f20:cour26]], Belgique par [[src:f10:S33]]. Retour à 60 ans : non affiché dans ce chapitre, rien à changer.
2. *Justice (étape 6)* : **non appliqué**. `judges_per_100k_2022` et `cepej_median_judges_2022` n’ont pas été ajoutés (source primaire CEPEJ inaccessible). Le texte reste qualitatif et le graphique justice reste bloqué. **Règle de publication** : l’étape 6 ne doit pas être mise en ligne tant que ces deux chiffres manquent, puisque la réponse de l’étape 9 s’appuie sur les juges par habitant sans chiffre. Les étapes 8 et 9 sont désormais chiffrées des deux côtés.
3. *Étiquettes (D-labels) et encadré (§4.6)* : **appliqué**. Première mention du FMI : « Fonds monétaire international (FMI ; organisation internationale) » ; « Cour des comptes (juridiction financière) » ; Insee et Eurostat étiquetés dans l’encadré ; titre exact, thèse en gras entre guillemets, auteurs avant les faits, ligne *Sources :* en italique avec étiquettes et titre de la Cour en italique, `box-side: droite`. La réponse répond seulement à la thèse et dit où l’objection tient (effet hors retraites). « (notre traduction) » devient « (traduit de l’anglais) ».
4. *Doublons et listes d’« économies faciles » (D-ownership)* : rien dans ce chapitre (ni AME, ni 980 000 emplois, ni paquet de 10 à 25 milliards).
5. *Contrôles du validateur* : **appliqué**. Sigles développés à la première occurrence (PIB, COFOG, UE-27, PISA, EU-SILC) ; calcul de l’étape 2 découpé en trois formules évaluables ; 16,3 % de l’UE en pastille « contexte » pour éviter deux identifiants sur le même nombre ; « de 15 à 64 ans » ; dénominateurs « de la population » ; seuils 50 % et 60 % écrits « la moitié » et « les trois cinquièmes » du revenu médian (aucune figure pour ces paramètres) ; « 666 par habitant et par an » (le validateur ne relie pas un nombre suivi de « heures » à sa pastille) ; réponses déclarées dans les trois blocs « Estimez d’abord » ; phrases et paragraphes trop longs coupés. Durée de lecture portée à 8 minutes (1 903 mots / 240 = 7,9).
6. *Résultat* : `python3 -I validate.py --strict` : 0 erreur et 0 avertissement propres à ce fichier ; 1 903 mots visibles. Restent trois avertissements transversaux qui citent ce chapitre sans venir de lui : arrondi « 15,60 » de `cofog_health_2024_pct_te` au chapitre 2, et étiquettes de la Cour des comptes, du FMI et de l’Institut Montaigne absentes ou différentes dans d’autres chapitres (2 et 7 au moment de cette passe).

**Passe transversale (plan de site) du 25 octobre 2026 (pass : corrections transversales)**
1. *Titres d’étapes, note d’équipe, durée de lecture* : **appliqué**. Douze titres « ## Étape N. Titre » ; note « Avant : chapitre 5 « La dette et ses intérêts » » ; « Durée de lecture : environ 7 minutes. » ajouté à l’étape 0 (1 714 mots visibles / 240 mots par minute = 7,1). Ajouts liés aux décisions D-titles : ligne « **→ Chapitre 7 : Les choix** » en fin d’étape 11, renvois « le chapitre 2, « Où va l’argent ? » » et « le chapitre 7, « Les choix » » dans le texte courant.
2. *Étape 4 (propriétaire des résultats retraités)* : **appliqué**. OCDE développé à la première occurrence ; phrase ménage 811 € remplacée par le renvoi « (chapitre 2) » ; icône ménage et pastille 811 € retirées.
3. *Étape 5* : **appliqué**. Phrase 510 € supprimée ; « Où sont les marges ? » réécrit (renvoi au chapitre 2, sans 6 ni 22 milliards, sans « gisement ») ; Graphique 3 et étalon ménage retirés ; pastilles `household_health_month_eur`, `health_admin_gap_eur_bn`, `low_value_care_eur_bn` et leurs calculs retirées. Ajout D-vocabulary : première mention « zone euro à 21 pays (ZE21, Bulgarie comprise) ».
4. *Étape 6* : **partiel**. PISA développé ; paragraphe 44 % et Graphique 2 retirés (le graphique justice devient Graphique 2). **Rejeté pour l’instant (données absentes)** : `judges_per_100k_2022` et `cepej_median_judges_2022` n’existent pas dans figures.json ; formulation qualitative maintenue, graphique justice toujours bloqué (règle de publication).
5. *Étape 7* : **partiel**. Paragraphes Trésor (38 milliards, 8,1 jours, 25 %, 551 €) et « Ce gain ne serait ni immédiat ni gratuit » remplacés par le renvoi au chapitre 7 ; puces convertisseur et 84 Md€ et pastilles correspondantes retirées ; « Nuance » conservée. **Rejeté pour l’instant** : `productivity_per_hour_pps_2025` et son rang absents de figures.json ; pas de 114,6 ni de 8e sur 27.
6. *Étape 8* : **partiel**. Paragraphe redistribution inséré (56 %, `net_beneficiaries_2023_pct`). Ajustement : l’Insee est développé dès l’étape 3 (première occurrence de la page), d’où « Selon l’Insee » à l’étape 8. **Rejeté pour l’instant** : phrase 30,5 points / 3e rang (`poverty_reduction_transfers_2025_pp` et rang absents).
7. *Étape 9, encadré rééquilibré à droite (FMI, Cour des comptes)* : **partiel**. Encadré remplacé, titre sans guillemets, thèse en gras, ligne source en italique ; paragraphe « formulé par la rédaction » supprimé ; pastilles refaites. Ajustement typographique : le titre du rapport de la Cour est en romain dans la ligne source en italique (italique dans l’italique impossible en Markdown). **Rejeté pour l’instant** : 10,2 points / 6e rang (`poverty_reduction_excl_pensions_2025_pp` et rang absents). La pastille FMI reste [[src:f10]] tant que l’entrée FMI Article IV 2026 n’est pas dans sources.json.
8. *Étape 10, synthèse courte* : **appliqué**. Doublons 12,4 % / 10,0 % (chapitre 1, étape 10) et rang PISA retirés ; étiquette Institut Montaigne « libéral-centriste » (D-labels ; le glossaire §1.13 porte encore « financé par des entreprises, libéral-centriste » à la date de cette passe) ; visuel deux colonnes remplacé par un bloc simple.
9. *Contrôles* : **appliqué**. Doublons retirés : 811 €, 510 €, 6 / 22 milliards, 44 %, Trésor 38 milliards. Phrases de plus de 25 mots coupées (étapes 2 à 10), sauf quatre qui ne dépassent qu’à cause des sigles développés ou du gras. `python3 -I validate.py` : PASS (0 erreur, 0 avertissement). Texte visible mesuré par script (lignes « > » hors commentaires et pastilles) : 1 895 mots avant, 1 714 après.

**Audit de neutralité et de cohérence du 25 octobre 2026 (lecteurs de gauche, de droite, chiffres)**
1. *« Financée par l’emprunt » répété (lecteur de gauche)* : **appliqué** pour ce chapitre. L’étape 9 garde le point une seule fois, en formulation neutre : « les comptes publics étant en déficit, l’Insee note que l’ensemble est en partie financé par l’emprunt ». Les corrections symétriques des chapitres 3 et 4 et de la question Q18 du quiz relèvent d’autres fichiers.
2. *Attributions des étapes 9 et 10 (lecteur de gauche)* : **partiellement appliqué**. Étape 10 : chaque lecture indique sa base de données (CEPEJ et OCDE ; Eurostat et OCDE) et ses défenseurs avec étiquette (Cour des comptes, juridiction financière ; FMI, organisation internationale ; Institut Montaigne, financé par des entreprises, libéral-centriste ; Fondation iFRAP, libérale ; Union syndicale des magistrats, syndicat de magistrats). Les syndicats d’enseignants sont retirés, faute de source dans la base. Étape 9 : les sources factuelles sont nommées avec leur nature (Insee, Eurostat), mais aucun défenseur nommé n’existe dans le fichier 10, §9. L’encadré dit donc que l’argument est formulé par la rédaction. À compléter quand un auteur sourcé sera trouvé (glossaire, §4.6).
3. *Productivité horaire (lecteur de gauche)* : **partiellement appliqué**. L’étape 7 dit maintenant que l’indicateur par habitant dépend de la démographie et que la productivité horaire est au-dessus de la moyenne de l’UE (effet de sélection, recul depuis 2019) [[src:f08]], sans chiffre. 114,6 et 8e sur 27 ne sont pas affichés : la figure `productivity_per_hour_pps_2025` n’existe pas dans figures.json, et ce fichier n’est pas le nôtre (demande en note 1). L’encadré du chapitre 7 relève d’un autre fichier.
4. *« Les meilleurs résultats là où la France dépense le plus » (lecteur de droite)* : **appliqué**, mais sans valeurs pour les autres pays. Étape 5 : « Six pays de l’UE font mieux » avec `[[calc:life_expectancy_2024_rank - 1 = 6]]`, en nommant l’Espagne, la Suède et l’Italie d’après le fichier 10, §8.2. Leur espérance de vie n’est pas affichée (figures à créer, note 1). Le fichier 10 parle de dépense publique « de santé et de protection sociale » sans base : « une part plus faible de leur PIB » n’a donc pas été repris. Étape 8 : phrase remplacée comme proposé.
5. *Deuxième lecture trop générique (lecteur de droite)* : **appliqué**. La phrase reprend trois indicateurs concrets avec leurs pastilles : frais de gestion en santé, PISA 29e sur 38, rémunération des agents publics à 12,4 % contre 10,0 % du PIB (zone euro dans son ensemble, terme du glossaire). « Masse salariale » est remplacé par la formule du glossaire et du chapitre 1 (« rémunération des agents publics »). Les citations du FMI et de la Cour sont conservées.
6. *« Au plus 6 milliards » (lecteur de droite)* : **appliqué**. « Environ 6 milliards », comme dans la note de la figure et au chapitre 2. Une seule réserve par montant : « un gisement, pas un rendement » (6 Md€), « une extrapolation, pas une économie disponible » (22 Md€). « Réforme profonde » est retiré. La symétrie avec les estimations de recettes (`tax_rich_package`) relève des chapitres 3 et 7.
7. *Pastilles hors du texte affiché (chiffres)* : **appliqué**. Chaque nombre des blocs « Texte affiché » des étapes 2 à 10 porte sa pastille juste après lui, avec les mêmes identifiants et formules. Les affirmations sans chiffre portent une pastille `[[src:]]`. Les listes « Pastilles » restent en consignes de production, comme au chapitre 5.
8. *Comparaison 2015 sans donnée (chiffres)* : **appliqué** (solution d’attente). « Nettement sous la moyenne il y a dix ans » devient « de 13,6 % en 2015 [[fig:arop_2015_pct]] ». La comparaison avec l’UE est retirée jusqu’à l’ajout de `eu27_arop_2015_pct` (note 1).
9. *Arrondis entre chapitres (chiffres)* : **appliqué** pour ce chapitre. Visuel de l’étape 2 aligné sur le chapitre 2 : 151, 57 et 32 jours (au lieu de 151,5 ; 56,9 ; 32,5). « Au plus 6 milliards » est corrigé (point 6). « 8,1 jours » est conservé : c’est la valeur que l’audit demande d’utiliser partout. Les autres arrondis cités (chapitres 2, 3 et 7) relèvent d’autres fichiers.

Contrôles : `python3 -I validate.py` après modification : PASS (0 erreur, 0 avertissement). Le script compte 1 964 mots de texte visible (blocs « > », pastilles exclues), dans la fourchette de 1 500 à 2 200 mots. Aucun nombre n’a été ajouté sans pastille : le seul nouveau nombre est le « six » de l’étape 5 (pastille `calc`) ; 12,4 % et 10,0 % étaient déjà des figures.

**Passe « chapitres » du 25 octobre 2026 (après la seconde passe de données)**
- Espaces réservés : aucun `[[fig-a-creer:…]]` ni bloc de données en attente dans ce chapitre ; rien à remplacer. `python3 -I validate.py` ne signale ni erreur ni avertissement pour ce fichier.
- Pastilles : les 42 identifiants distincts `[[fig:]]` et `[[yard:]]` sont résolus ; chaque valeur affichée a été recomparée au fichier de données (format français, arrondi) ; les sept pastilles `[[calc:]]` refaites (240,9 jours ; 28,2 / 10,6 / 6,1 € ; 1,28 et 4,68 jours ; 8,09 jours ; 25,1 % ; 551 €), ainsi que l’étalon 44,2 %. Aucun écart.
- Aucune des nouvelles figures de la passe de données ne couvre les indicateurs listés en note 1 (justice, mortalité évitable, reste à charge, PISA lecture et sciences, pauvreté avant transferts) : les formulations qualitatives sourcées restent en place.
- Réduction : texte visible (blocs « Texte affiché », hors pastilles et consignes) mesuré par script à 1 801 mots avant, 1 689 après (liste « Pour aller plus loin » comprise). Coupes : rappel des 8,9 % et 32,5 jours de l’enseignement à l’étape 6 (déjà à l’étape 2, pastilles retirées en conséquence) ; scores PISA en lecture et sciences, détail des sources et des données cancer 2010-2014 (renvoyés aux fiches) ; « 16 pays plus bas, 10 plus élevés » à l’étape 3 (chiffres sans pastille) ; resserrement des étapes 0, 3, 5, 7, 8, 9 et 10 sans perte d’idée ni de nuance.
- Ajout d’une liste « Pour aller plus loin » à l’étape 11 (fiches Santé, Fonction publique et résultats, Retraites, Emploi, Protection sociale par risque), sans chiffre.
- Inchangés : ouverture « Estimez d’abord », étalons (calendrier, ménage, € par habitant et par jour), comparaisons internationales avec année et groupe, encadré « Le meilleur contre-argument », transition vers le chapitre 7.

**Relecture précédente**

*Relecture du 25 octobre 2026 (chiffres, neutralité, qualité du français). Tous les chiffres ont été vérifiés contre `platform/data/figures.json` et `yardsticks.json` (valeur, unité, % du PIB ou % des dépenses publiques, année) ; tous les calculs « illustratif » ont été refaits et sont justes (240,9 jours ; 28,2 / 10,6 / 6,1 € ; 1,28 et 4,68 jours ; 8,09 jours ; 25,1 % ; 551 € ; 44,2 %). Aucun chiffre nouveau n’a été ajouté.*

**Chiffres et exactitude**
- Étape 3 : rang de pauvreté reformulé (« 11e taux le plus élevé », rang 1 = taux le plus élevé) ; « une partie de la hausse vient » ramené à « peut venir » (fichier 10, §9.2 : l’effet des ruptures de série n’est pas chiffré) ; terme du glossaire « après transferts sociaux » ajouté.
- Étape 4 : seuils (50 % OCDE, 60 % UE) précisés dans le texte, pas seulement dans le graphique ; « taux de risque de pauvreté » pour la mesure européenne.
- Étape 5 : « moyenne de la zone euro » remplacé par « la zone euro dans son ensemble » (agrégat pondéré, glossaire) ; EA21 → ZE21 ; « soins peu utiles » aligné sur l’intitulé de la figure (« inutiles ou de faible valeur ») ; ajout de la rupture de série sur le renoncement aux soins (fichier 12, §0.7) et de l’ancienneté des données sur le cancer (CONCORD-3, 2010-2014).
- Étape 6 : « intérêts de la dette » → « intérêts de la dette publique » ; « dépense d’enseignement » → « dépense publique d’enseignement ».
- Étape 7 : « prélèvements » → « prélèvements obligatoires » et base 2022 indiquée ; la nuance sur les heures omettait que les heures par personne en emploi sont sous la moyenne de l’UE (fichier 08, §16) : corrigé.
- Étape 8 : « accès aux soins » et « moyens de la justice » remplacés par les indicateurs réellement disponibles (renoncement pour délais, juges par habitant).
- Étape 9 : erreur de concept corrigée : le taux « avant transferts » d’Eurostat est calculé avant prestations sociales (retraites comprises), pas avant impôts ; année 2023 ajoutée pour les 56 %.
- Étape 10 : la citation « rationaliser » est du FMI, pas de la Cour des comptes ; attribution corrigée et mention « traduit de l’anglais » dans la pastille.

**Neutralité**
- Étape 5 : ajout du meilleur argument des défenseurs du système de santé (dépense par habitant en pouvoir d’achat inférieure à celle de l’Allemagne, des Pays-Bas, de la Belgique et de la Suède ; fichier 12, §0.1 et §0.8).
- Étapes 5 et 7 : symétrie de l'« argent facile » : les 6 milliards (frais de gestion), les 22 milliards (soins de faible valeur) et les 38 milliards (emploi) sont désormais tous présentés comme des plafonds ou des scénarios, avec leurs conditions (réforme profonde, extrapolation non vérifiée, délais et réformes débattues, coût futur des pensions).
- Étape 4 : le coût des retraites est présenté comme la contrepartie du bon résultat, et non comme une remarque à part.
- Étape 6 : « un des rares domaines où plusieurs sources concluent à un manque de moyens » (affirmation non étayée) remplacé par un constat sourcé, avec deux nuances (budget par habitant au-dessus de la médiane européenne ; organisations judiciaires différentes).
- Étape 7 : titre « le point faible qui pèse le plus » (superlatif non démontré) → « un point faible qui pèse ».
- Étape 8 : ajout d’indicateurs favorables (reste à charge) et neutres (cancer) déjà cités à l’étape 5 ; avertissement sur la causalité ajouté.
- Étape 9 : la réponse au contre-argument cite aussi l’exemple belge (fichier 10, §9.3) et rappelle la rupture de série, pour ne pas surestimer la dégradation.
- Étape 10 : la conclusion « le débat porte moins sur dépenser plus ou moins que sur où dépenser » prenait parti contre ceux qui jugent le niveau de dépense décisif ; reformulée en « ne se résume pas à… il porte aussi sur ».

**Français et typographie**
- « habitants de la France » → « personnes vivant en France » ; « sont pauvres » → « vivent sous le seuil de pauvreté » ; « l’école » → « l’enseignement » (le poste COFOG inclut le supérieur).
- Étalon ménage aligné sur la formulation du chapitre 2 (« Si la France était un ménage gagnant 3 000 € par mois… »).
- « Les ménages paient eux-mêmes une petite part » → « reste à charge des ménages », terme du glossaire.
- « Les résultats contre le cancer » → « La survie après un cancer ».
- Espaces insécables, apostrophes typographiques et signe moins : laissés au filtre de rendu (glossaire, §2.1) ; guillemets « » et virgule décimale vérifiés dans tout le texte.

**À trancher par l’équipe**
- Étape 10 : ~~attributions asymétriques~~ traité par l’audit du 25 octobre 2026 (point 2) ; reste la vérification juridique (note 4).
- Étape 11 : le message de partage « J’ai trouvé 3 résultats sur 5 » doit être généré à partir du score réel.

