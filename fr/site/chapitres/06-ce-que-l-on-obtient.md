# Chapitre 6. Qu’obtient-on en échange ?

*Script de récit défilant (scrollytelling) pour le site public. Version de travail du 30 octobre 2026 (après confrontation aux sources publiques).*

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
> Durée de lecture : environ 9 minutes.

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
> Dans le calendrier de la dépense publique, ces trois postes occupent environ 241 jours sur 365 [[calc:(cofog_social_protection_2024_pct_te + cofog_health_2024_pct_te + cofog_education_2024_pct_te) / 100 × days_in_year = 240,9]]. Ordre de grandeur, d’après notre calcul : parts de 2024, dépense de 2025.
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

> En 2025, 16,3 % des personnes vivant en France sont sous le seuil de risque de pauvreté, après impôts et prestations sociales [[fig:arop_2025_pct]]. C’est exactement le niveau de l’Union européenne dans son ensemble [[fig:eu27_arop_2025_pct|contexte]].
>
> La France a le 11e taux le plus élevé des 27 pays de l’UE [[fig:arop_2025_rank]].
>
> Le taux était de 13,6 % de la population en 2015 [[fig:arop_2015_pct]]. Eurostat signale des ruptures de série en 2020 et en 2022, dont l’effet n’est pas chiffré [[src:f10]].
>
> Pour Pierre Madec, de l’OFCE (Observatoire français des conjonctures économiques ; Sciences Po, sensibilité keynésienne), la hausse a aussi des causes économiques. Il cite l’inflation, la fin des aides exceptionnelles et des emplois peu payés.
>
> La mesure nationale de l’Insee (Institut national de la statistique et des études économiques) atteint 15,4 % de la population en 2024, comme en 2023 [[fig:poverty_national_2024_pct]]. C’est son plus haut niveau depuis 1996. Elle couvre la France métropolitaine, sans les sans-abri ni les personnes en institution [[src:f00:row47]].

**Visuel et animation**
- Graphique en points (dot plot) des 27 pays de l’UE, triés du taux le plus bas au plus élevé. Point de la France en couleur d’accent, ligne verticale pour l’UE-27.
- Axe : « en % de la population ». Titre : « Taux de risque de pauvreté après transferts sociaux, EU-SILC 2025 ».
- Animation : le point de la France glisse de 13,6 (2015) à 16,3 (2025). Marqueurs « rupture de série » en 2020 et 2022.
- La mesure Insee (15,4 %) s’affiche dans une carte séparée, avec la mention « Mesure nationale : ne pas comparer directement avec le taux européen » (glossaire, §1.10).
- Données pays : `data/eurostat_ilc_li02.csv` (fichier 20, §4.3).

**Pastilles**
- 16,3 % [[fig:arop_2025_pct]] ; UE-27 16,3 % [[fig:eu27_arop_2025_pct]]
- 11e taux le plus élevé sur 27 [[fig:arop_2025_rank]] (rang 1 = taux le plus élevé)
- 13,6 % en 2015 [[fig:arop_2015_pct]] (mention « rupture de série » obligatoire, note de la figure) ; ruptures de série 2020 et 2022 [[src:f10]] (relevé de la plateforme dans les métadonnées Eurostat ilc_li02, 25 octobre 2026 ; ne pas les présenter comme l’explication de la hausse)
- OFCE : Pierre Madec, « Lutte contre la pauvreté : le décrochage français ? », blog de l’OFCE, 26 novembre 2025, https://www.ofce.fr/blog2024/fr/2025/20251125_PIM/ (consulté le 30 octobre 2026 par la confrontation aux sources publiques ; **entrée à ajouter à sources.json**, pas de pastille tant qu’elle n’existe pas)
- 15,4 % [[fig:poverty_national_2024_pct]] ; « plus haut depuis 1996 », France métropolitaine, stable par rapport à 2023, hors personnes en institution et sans domicile, ruptures de la série ERFS en 2010, 2012 et 2020 [[src:f00:row47]] (Insee, *Insee Première* n° 2117, 9 juillet 2026, https://www.insee.fr/fr/statistiques/9019316)

---

## Étape 4. Personnes âgées : un résultat net

**Texte affiché**

> Le tableau change pour les personnes âgées.
>
> En France, 6,1 % des 65 ans et plus vivent sous le seuil de pauvreté en 2022 [[fig:old_age_poverty_oecd_2022_pct]]. La source est l’Organisation de coopération et de développement économiques (OCDE). Ce seuil est fixé à la moitié du revenu médian. La moyenne des pays de l’OCDE est de 14,8 % des 65 ans et plus [[fig:oecd_old_age_poverty_2022_pct]].
>
> La mesure européenne place le seuil plus haut, aux trois cinquièmes du revenu médian. Avec elle, 11,6 % des 65 ans et plus sont sous le seuil de risque de pauvreté en 2025 [[fig:old_age_poverty_eu_2025_pct]]. C’est nettement moins que pour l’ensemble de la population (16,3 %) [[fig:arop_2025_pct]].
>
> Selon le Conseil d’orientation des retraites (COR), le niveau de vie moyen des retraités égale celui de l’ensemble de la population. Il en représente 100,2 % en 2023 [[fig:retirees_relative_living_standard_pct]]. Si l’on compte le loyer que les propriétaires n’ont pas à payer, les retraités passent au-dessus [[src:f03:cor26]].
>
> L’Institut Montaigne (libéral-centriste) y voit en partie la générosité du système, en partie la forte hausse du nombre de retraités [[src:f10]].
>
> Ce résultat a un coût : les retraites sont le premier poste de la dépense publique (chapitre 2).

**Visuel et animation**
- Deux barres horizontales côte à côte : France 6,1 % / moyenne OCDE 14,8 %. Axe : « en % des 65 ans et plus (seuil de 50 % du revenu médian), 2022 ».
- Puis deux barres France seule, seuil européen de 60 % : population totale 16,3 % / 65 ans et plus 11,6 %. Les deux graphiques gardent leur propre titre de seuil : ne pas mélanger les seuils de 50 % et 60 % sur un même axe.
- Jauge « niveau de vie des retraités / ensemble de la population » avec l’aiguille sur 100,2.

**Pastilles**
- 6,1 % [[fig:old_age_poverty_oecd_2022_pct]] ; 14,8 % [[fig:oecd_old_age_poverty_2022_pct]]
- 11,6 % [[fig:old_age_poverty_eu_2025_pct]] ; 16,3 % [[fig:arop_2025_pct]]
- 100,2 % [[fig:retirees_relative_living_standard_pct]] (hors loyers imputés) ; variante avec loyers imputés, retraités 6,5 % au-dessus de l’ensemble de la population (COR, *Rapport annuel* 2026, partie 3, chapitre 2, https://www.cor-retraites.fr/sites/default/files/2026-06/RA_Part3_Chap2.pdf ; fichier 03, l. 129) [[src:f03:cor26]] : **figure à créer** (`retirees_relative_living_standard_imputed_rent_pct`, 106,5) avant d’afficher le chiffre
- Institut Montaigne, *Budget base zéro : décider sous la contrainte*, novembre 2025 (« la générosité de notre système » ; hausse du nombre de retraités ; niveau de vie global des retraités au-dessus de celui de l’ensemble de la population), https://institutmontaigne.org/ressources/pdfs/publications/note-budget-base-zero-decider-sous-la-contrainte.pdf [[src:f10]] (fichier 10, [S44])

---

## Étape 5. Santé : de bons résultats, des tensions sur l’accès

**Devinez d’abord** (libellé public : « Estimez d’abord »)
- Question : « Combien d’années vit-on en moyenne en France, à la naissance ? » Curseur de 75 à 90 ans, pas de 0,5. Révélation avec la moyenne UE-27.
<!-- estimez-réponse: life_expectancy_2024_years -->

**Texte affiché**

> La santé est le 2e poste de la dépense publique : 8,9 % du PIB en 2024 [[fig:cofog_health_2024_pct_gdp]]. C’est 1,5 point de PIB de plus que la zone euro à 21 pays (ZE21, Bulgarie comprise) dans son ensemble [[fig:gap2024_health_pp]]. Ce calcul suit la classification des fonctions des administrations publiques (COFOG). L’écart est plus faible avec d’autres définitions [[src:f12]].
>
> Par habitant, à coût de la vie égal et dépense privée comprise, la France dépense moins que l’Allemagne, les Pays-Bas, la Belgique ou la Suède [[src:f12]]. C’est le coût total, pas la seule charge publique (étape 8).
>
> **Ce qui va bien.** L’espérance de vie à la naissance atteint 83,0 ans en 2024 [[fig:life_expectancy_2024_years]], contre 81,5 ans dans l’Union européenne à 27 pays (UE-27) [[fig:eu27_life_expectancy_2024_years]]. La France est 7e sur 27 [[fig:life_expectancy_2024_rank]].
>
> Six pays de l’UE font mieux [[calc:life_expectancy_2024_rank - 1 = 6]], dont l’Espagne, la Suède et l’Italie. Ces trois pays consacrent moins de dépense publique à la santé et à la protection sociale [[src:f10]].
>
> Autres points forts : la mortalité évitable par des soins et le reste à charge des ménages sont parmi les plus bas d’Europe [[src:f12]].
>
> **Ce qui va moins bien.** Le renoncement aux soins pour délais augmente depuis 2021, en partie à cause d’un changement de méthode. La France est dans le tiers le moins bien placé de l’UE. La survie après un cancer est dans la moyenne de l’OCDE, pas en tête [[src:f12]].
>
> **Où sont les marges ?** Les frais de gestion sont élevés, surtout parce que deux assurances se superposent : l’Assurance maladie et les complémentaires santé [[src:f12]]. La Fondation iFRAP (libérale) les juge bien plus bas aux Pays-Bas, tout en disant la comparaison imparfaite. Le chapitre 2 chiffre ce réservoir.

**Visuel et animation**
- Graphique 1 : barres de l’espérance de vie à la naissance, 2024, pays de l’UE-27 triés. France en couleur d’accent, ligne UE-27. Axe : « en années ».
- Graphique 2 : bandeau « Ce que l’on obtient » (composant partagé) avec trois pastilles qualitatives : « mortalité évitable par les soins : parmi les plus basses de l’UE », « reste à charge : parmi les plus faibles », « délais d’accès : en hausse depuis 2021 ». Pas de chiffre affiché tant que ces indicateurs ne sont pas dans `figures.json` (voir notes).

**Pastilles**
- 8,9 % du PIB [[fig:cofog_health_2024_pct_gdp]] ; +1,5 point [[fig:gap2024_health_pp]] (comparaison : zone euro ZE21, 2024) ; « plus faible avec d’autres définitions » et dépense par habitant en standard de pouvoir d’achat [[src:f12]]
- 83,0 ans [[fig:life_expectancy_2024_years]] ; 81,5 ans [[fig:eu27_life_expectancy_2024_years]] ; 7e sur 27 [[fig:life_expectancy_2024_rank]] ; six pays devant [[calc:life_expectancy_2024_rank - 1 = 6]] ; Espagne, Suède et Italie devant la France avec une dépense publique de santé et de protection sociale plus faible [[src:f10]] (fichier 10, §8.2 ; valeurs pays à ajouter à figures.json avant de les afficher, voir note 1)
- Fipeco (François Ecalle), *L’efficience des dépenses d’assurance maladie*, fiche encyclopédie, 30 janvier 2026, https://fipeco.fr/pdf/EfficienceD%C3%A9pensesSant%C3%A9.pdf : France 3e de l’OCDE pour la dépense de santé publique ou obligatoire (9,7 % du PIB en 2023, à égalité avec la Suède, derrière les États-Unis et l’Allemagne), 9e pour l’espérance de vie (2023), 10e pour la mortalité évitable (2022) ; « pourrait être nettement améliorée ». Chiffres non affichés : **figures à créer** (`health_public_compulsory_2023_pct_gdp`, `health_public_compulsory_2023_oecd_rank`, `life_expectancy_2023_oecd_rank`) et **entrée à ajouter à sources.json**.
- Fipeco, *Les montants laissés à la charge des ménages par l’assurance maladie*, 30 janvier 2024, https://fipeco.fr/pdf/Bouclier2024.pdf (« duplication des frais de gestion ») ; Fondation iFRAP (Iphigénie Betolaud), « 17 Md€ de coûts de gestion de la santé », 7 juin 2026, https://www.ifrap.org/emploi-et-politiques-sociales/17-mdeu-de-couts-de-gestion-de-la-sante (0,57 % du PIB contre 0,3 % aux Pays-Bas, Eurostat 2023 ; comparaison « imparfaite » selon l’auteure) : **entrées à ajouter à sources.json** ; montants réservés au chapitre 2.
- Mortalité évitable, reste à charge, délais (et rupture de série), survie après un cancer, frais de gestion [[src:f12]] (« les plus élevés de l’UE » retiré le 30 octobre 2026 : non confirmé par les textes publiés consultés)
- Renvoi au chapitre 2 (étape 8) pour le chiffrage des réservoirs (frais de gestion, soins de faible valeur) : aucun montant affiché ici.

---

## Étape 6. École et justice : sous la moyenne

**Devinez d’abord** (libellé public : « Estimez d’abord »)
- Question : « En mathématiques, les élèves français de 15 ans sont-ils au-dessus, dans ou en dessous de la moyenne de l’OCDE ? » Trois boutons. Révélation immédiate.
<!-- estimez-réponse: pisa_math_2025, oecd_pisa_math_2025 -->

**Texte affiché**

> **L’école.** Selon l’enquête 2025 du Programme international pour le suivi des acquis des élèves (PISA), les élèves de 15 ans obtiennent 458 points en mathématiques [[fig:pisa_math_2025]]. La moyenne de l’OCDE est de 463 points [[fig:oecd_pisa_math_2025]]. La France est 29e sur 38 pays de l’OCDE [[fig:pisa_math_2025_rank]]. Sa baisse depuis 2015 est l’une des plus fortes, même si la moyenne de l’OCDE a aussi baissé [[src:f13]].
>
> Parmi les pays riches, ceux qui dépensent le plus par élève n’ont pas toujours les meilleurs scores [[src:f13]]. Le Conseil d’analyse économique (CAE ; instance d’économistes placée auprès du Premier ministre) nuance. En 2021, la France dépensait un peu plus par élève que la moyenne de l’OCDE : moins en primaire, plus dans le secondaire.
>
> Le Canada, l’Estonie ou le Japon font mieux pour une dépense comparable ou plus faible. Mais le CAE juge efficaces les dépenses ciblées : petites classes en primaire, tutorat.
>
> Les enseignants sont moins payés que la moyenne de l’OCDE [[src:f04]]. Pour la Fondation iFRAP, l’école manque moins de moyens que d’organisation : elle propose notamment une part de salaire variable.
>
> **La justice.** En 2022, la France compte 11,3 juges professionnels pour 100 000 habitants [[fig:judges_per_100k_2022]], contre 17,6 en médiane au Conseil de l’Europe [[fig:cepej_median_judges_2022]]. Ce ratio exclut les nombreux juges non professionnels (tribunaux de commerce, prud’hommes). L’Union syndicale des magistrats (syndicat de magistrats) juge la situation « critique » en moyens humains et budgétaires [[src:f10]].
>
> La Cour des comptes (juridiction financière) notait en 2021 un budget en nette hausse depuis 2011, sans baisse des délais civils. Elle demandait de mieux répartir les effectifs.

**Visuel et animation**
- Graphique 1 : nuage de points « dépense par élève / score PISA 2025 », pays de l’OCDE, France en couleur d’accent, droite de tendance (fichier 20, §4.2, GF09 ; données `data/13_pisa2025_country_values.csv`). Les valeurs des autres pays sont dans le fichier de données ; le texte n’en cite aucune.
- Animation : la ligne « moyenne OCDE » (463) se dessine, puis le point France (458) apparaît sous la ligne.
- Graphique 2 (justice) : **débloqué pour le volet « juges », toujours bloqué pour le volet « délais »** (règle de publication du plan de site : les contre-preuves doivent être chiffrées de la même façon). Volet « juges » : petits multiples « juges professionnels pour 100 000 habitants » (fichier 20, §4.2, GF03), France 11,3 [[fig:judges_per_100k_2022]] contre une médiane de 17,6 [[fig:cepej_median_judges_2022]] ; valeurs lues sur le tableau de bord public de la CEPEJ (CEPEJ-STAT, profil France, données 2022, mise à jour du 25/10/2024), le rapport PDF restant inaccessible ; mention fixe sous le graphique : « hors juges non professionnels (tribunaux de commerce, conseils de prud’hommes) ». Pastilles ajoutées au texte affiché le 31 octobre 2026. Les valeurs des autres pays ne sont pas dans `figures.json` : à ajouter avant d’afficher les petits multiples, sinon montrer seulement France et médiane. Volet « délais » : la médiane européenne des délais civils en première instance n’est toujours pas confirmée (France : 333 jours, sans entrée dans `figures.json`) ; ne rien afficher tant qu’elle manque.

**Pastilles**
- 458 [[fig:pisa_math_2025]] ; 463 [[fig:oecd_pisa_math_2025]] ; 29e sur 38 [[fig:pisa_math_2025_rank]]
- Baisse depuis 2015, lien dépense-score [[src:f13]] ; salaire des enseignants [[src:f04]]
- CAE (Greneta, Landais), *Éducation : comment mieux orienter la dépense publique*, Note du CAE n° 84, mai 2025, https://cae-eco.fr/static/pdf/cae084-education-250514.pdf : dépense par élève 2021 (OCDE, *Regards sur l’éducation* 2024) 9 352 € contre 8 838 € pour l’OCDE ; primaire 11 % sous la moyenne, secondaire 13 % au-dessus ; enseignant du primaire à dix ans d’ancienneté payé 17 % de moins ; pays plus efficaces ; dépenses ciblées efficaces. Chiffres non affichés : **figures à créer** (`spending_per_pupil_2021_eur`, `oecd_spending_per_pupil_2021_eur`, `primary_spending_gap_2021_pct`, `secondary_spending_gap_2021_pct`) et **entrée à ajouter à sources.json**.
- Fondation iFRAP, *Société Civile* n° 227, octobre 2021, https://www.ifrap.org/education-et-culture/eduquer-mieux-en-reallouant-et-en-baissant-les-depenses (constat de la Cour des comptes de 2013 : l’Éducation nationale « ne souffre pas d’un manque de moyens » ; part variable de rémunération) : **entrée à ajouter à sources.json**.
- Justice : 11,3 juges professionnels pour 100 000 habitants [[fig:judges_per_100k_2022]] ; médiane du Conseil de l’Europe 17,6 [[fig:cepej_median_judges_2022]] (CEPEJ-STAT, données 2022, mise à jour du 25/10/2024 ; ratio hors juges non professionnels des tribunaux de commerce et des conseils de prud’hommes) ; jugement « critique » de l’Union syndicale des magistrats [[src:f10]] (la note de l’USM de 2024 donne 333 jours pour une affaire civile en première instance, contre 637 jours dans l’édition précédente : ne pas écrire que les procès sont « plus longs » sans médiane européenne confirmée) ; Union syndicale des magistrats, *Note sur le rapport CEPEJ 2024*, 18 octobre 2024 (données 2022, source syndicale), https://union-syndicale-magistrats.org/wp-content/uploads/2024/10/2024.10.18_note-USM-sur-rapport-CEPEJ-2024.pdf (fichier 10, [S38])
- Cour des comptes, note *Améliorer la gestion du service public de la justice*, 21 octobre 2021, lue seulement dans le résumé du Monde du Droit (25 octobre 2021), https://www.lemondedudroit.fr/judiciaire/324-organisation-judiciaire/78080-cour-des-comptes-ameliorer-la-gestion-du-service-public-de-la-justice.html (budget + 22 % de 2011 à 2021, délais civils en hausse) : **ouvrir la note primaire et ajouter l’entrée à sources.json** avant publication ; « nettement » remplace le chiffre en attendant.
- Budget de la justice par habitant (au-dessus de la médiane européenne, sous la moyenne) : retiré du texte affiché le 30 octobre 2026 (voir notes de relecture), à rétablir avec les chiffres CEPEJ primaires.

---

## Étape 7. Emploi : un point faible qui pèse sur les comptes

**Texte affiché**

> L’emploi n’est pas une dépense, mais il conditionne tout le reste. Plus de personnes en emploi, c’est plus de cotisations et d’impôts, et moins de prestations.
>
> En 2025, 69,3 % des personnes de 15 à 64 ans ont un emploi en France [[fig:employment_rate_2025_pct]], contre 71,0 % dans l’UE-27 [[fig:eu27_employment_rate_2025_pct]]. La France est 21e sur 27 [[fig:employment_rate_2025_rank]].
>
> Le taux d’emploi a pourtant progressé depuis 2014, comme la pauvreté, à l’inverse de la plupart des pays de l’UE. Pour l’OFCE, beaucoup d’emplois nouveaux étaient peu payés.
>
> Rapporté à toute la population, le nombre d’heures travaillées est le plus faible de l’UE : 666 par habitant et par an [[fig:hours_per_inhabitant_2025]], 27e sur 27 [[fig:hours_per_inhabitant_2025_rank]]. Cet indicateur compte toute la population, élèves et retraités compris : il dépend aussi de la démographie.
>
> Le chapitre 7 chiffre ce que rapporterait un taux d’emploi plus élevé. Le CAE prévient : la production augmenterait moins vite que l’emploi.
>
> Nuance : ceux qui ont un emploi travaillent un peu moins que la moyenne de l’UE, sans être les derniers [[src:f08]]. Rexecode (institut de conjoncture proche des organisations patronales) le note aussi. Le retard vient surtout du faible emploi des jeunes et des seniors [[src:f08]]. Ces comparaisons d’heures restent fragiles, prévient l’Insee.
>
> Par heure travaillée, la productivité française dépasse la moyenne de l’UE. En 2025, elle atteint l’indice 114,6 en standards de pouvoir d’achat (SPA), UE = 100 [[fig:productivity_per_hour_pps_2025]]. La France est 8e sur 27 [[fig:productivity_per_hour_pps_2025_rank]]. Une hypothèse : les moins qualifiés sont plus souvent sans emploi. D’après notre calcul, elle a reculé depuis 2019 [[src:f08]].

**Visuel et animation**
- Graphique en pente (slope chart) 2009 → 2025 : taux d’emploi France vs UE-27 (fichier 20, §4.13 ; `data/08_eurostat_lfsi_emp_a.csv`). Le texte ne cite que 2025. Ajout du 30 octobre 2026 : sous le graphique, une seconde ligne « taux de risque de pauvreté, France » sur la même période (Eurostat ilc_li02, ruptures 2020 et 2022 marquées), pour montrer que l’emploi et la pauvreté ont monté ensemble depuis 2014. Pas de valeur dans le texte tant que les figures de variation n’existent pas.

**Pastilles**
- 69,3 % [[fig:employment_rate_2025_pct]] ; 71,0 % [[fig:eu27_employment_rate_2025_pct]] ; 21e sur 27 [[fig:employment_rate_2025_rank]]
- 666 heures [[fig:hours_per_inhabitant_2025]] ; 27e sur 27 [[fig:hours_per_inhabitant_2025_rank]]
- Emploi et pauvreté 2014-2024 (+5,3 points d’emploi, +2,6 points de pauvreté, Eurostat ; emplois peu payés en micro-entreprise et en apprentissage) : OFCE, Pierre Madec, 26 novembre 2025, https://www.ofce.fr/blog2024/fr/2025/20251125_PIM/ (**entrée à ajouter à sources.json** ; chiffres non affichés, **figures à créer** `employment_rate_change_2014_2024_pp` et `arop_change_2014_2024_pp`, à vérifier dans Eurostat lfsi_emp_a et ilc_li02)
- CAE (Bozio, Ferreira, Landais, Lapeyre, Modena), *Objectif plein emploi : pourquoi et comment ?*, diapositives, 4 mars 2025, https://cae-eco.fr/static/pdf/pleinemploislides.pdf (« Elasticité du PIB aux heures travaillées ≤ 1 » ; productivité horaire « reste élevée », ralentissement relatif depuis les années 2000 face aux États-Unis) : **entrée à ajouter à sources.json** ; la réserve chiffrée relève du chapitre 7.
- Heures par personne en emploi : un peu sous la moyenne UE-27, pas les plus basses ; rôle de l’emploi des jeunes et des seniors [[src:f08]] ; Rexecode (Gancel, Redoulès), *La durée effective du travail et sa quantité en France et en Europe en 2024*, document de travail n° 98, décembre 2025, https://www.rexecode.fr/media/documents/document-de-travail/2025/la-duree-effective-du-travail-et-sa-quantite-en-france-et-en-europe-en-2024-document-de-travail-n.98-dec.-2025 (1 603 heures, ni la durée ni le taux d’emploi les plus bas) ; comparabilité : Insee et Destatis (Körner, Wolff), *La fragile comparabilité des durées de travail en France et en Allemagne*, *Insee Analyses* n° 26, juin 2016, https://www.insee.fr/fr/statistiques/fichier/version-html/2019603/IA26.pdf (**entrées à ajouter à sources.json**). Comparaison avec l’Allemagne et les Pays-Bas retirée le 30 octobre 2026 (non confirmée par les textes publiés consultés). Renvoi au chapitre 7 (étape 7) pour le levier emploi chiffré par la DG Trésor.
- 114,6 (SPA, UE-27 = 100) [[fig:productivity_per_hour_pps_2025]] ; 8e sur 27 [[fig:productivity_per_hour_pps_2025_rank]] (Eurostat nama_10_lp_ulc, 22 octobre 2026, source [[src:f08:es-lp]])
- Effet de sélection (présenté comme une hypothèse), recul depuis 2019 (calcul de la plateforme) [[src:f08]] (fichier 08, l. 261-268 : −0,8 % en volume sur 2019-2025, non affiché faute de figure ; aucun texte publié consulté ne donne ce recul ni l’effet de sélection)

---

## Étape 8. Le bilan : vos pronostics face aux résultats

**Texte affiché**

> Voici le bilan, comparé à vos pronostics de départ.
>
> **Mieux que la moyenne :** espérance de vie (UE-27, 2024), pauvreté des personnes âgées (OCDE, 2022), mortalité évitable par les soins, reste à charge des ménages.
>
> **Dans la moyenne :** pauvreté de l’ensemble de la population (UE-27, 2025), survie après un cancer (OCDE).
>
> **Moins bien que la moyenne :** mathématiques à 15 ans (OCDE, 2025), taux d’emploi et heures travaillées par habitant (UE-27, 2025), juges par habitant, renoncement aux soins pour délais.
>
> Notre règle : « dans la moyenne » veut dire un écart nul ou jugé non significatif par la source. Tout autre écart compte, même petit.
>
> Le groupe compte aussi, selon Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire). Dans l’OCDE, sa dépense de santé publique ou obligatoire est parmi les plus élevées. Son espérance de vie y est moins bien classée.
>
> Un résultat se lit à part : la redistribution. Avant prestations sociales (retraites comprises), 46,8 % de la population serait sous le seuil de risque de pauvreté en 2025 [[fig:arop_before_transfers_2025_pct]]. C’est l’un des taux les plus élevés de l’UE. Après prestations, la France revient dans la moyenne [[fig:arop_2025_pct|contexte]].
>
> Les prestations font donc baisser ce taux de 30,5 points [[fig:poverty_reduction_transfers_2025_pp]], la 3e baisse de l’UE [[fig:poverty_reduction_transfers_2025_rank]]. Les retraites en font la plus grande part, alors qu’elles remplacent en partie un revenu passé [[src:f10:S33]]. Hors retraites, sur la mesure de l’Insee, l’OFCE constate que les prestations sortent de la pauvreté moins de ménages pauvres qu’en 2017.
>
> Selon l’Insee, 56 % des personnes reçoivent plus qu’elles ne paient en 2023 (chapitre 3) [[fig:net_beneficiaries_2023_pct]]. Ce calcul compte l’école et l’hôpital, mais aussi la défense, la police et la justice, partagées à parts égales par convention. Les comptes étant en déficit, ce gain est en partie financé par l’emprunt [[src:f10]].
>
> Les meilleurs résultats se trouvent là où la France dépense le plus : retraites et santé. Mais d’autres pays font aussi bien ou mieux en dépensant moins [[src:f10]].
>
> Ailleurs, ils sont moyens ou faibles, même à l’école, où la dépense par élève dépasse un peu la moyenne. Ces rapprochements ne prouvent pas que la dépense soit la seule cause des résultats.

**Visuel et animation**
- Tableau de bord à trois colonnes (Mieux / Pareil / Moins bien). Les cartes de l’utilisateur (étape 1) se placent à gauche de chaque ligne, les bonnes réponses à droite ; une coche ou une croix s’affiche.
- Chaque ligne rappelle l’indicateur, l’année et le groupe de comparaison : UE-27 2025 (pauvreté, emploi), UE-27 2024 (espérance de vie), OCDE 2022 (pauvreté des 65 ans et plus), OCDE PISA 2025 (mathématiques).
- Afficher la répartition des réponses des autres lecteurs (« X % des lecteurs pensaient… » : valeur calculée en direct, jamais saisie à la main).

**Pastilles**
- Celles des étapes 3 à 7, reprises au survol de chaque ligne.
- Redistribution : avant et après prestations sociales [[src:f10]] ; 56 % [[fig:net_beneficiaries_2023_pct]] (Insee, *Insee Analyses* n° 118, 16 avril 2026, https://www.insee.fr/fr/statistiques/8974371 ; même valeur qu’au chapitre 3) ; services collectifs régaliens « répartis uniformément » ; environ 66 Md€ de déficit, environ 1 400 € par unité de consommation financés par la dette (non affichés : **figures à créer** `insee_broad_redistribution_deficit_2023_eur_bn` et `insee_broad_redistribution_debt_per_cu_2023_eur`).
- Règle des trois colonnes (ajout du 30 octobre 2026) : « dans la moyenne » = écart nul ou jugé non significatif par la source ; tout autre écart compte. Groupe et année affichés dans le texte. Classement OCDE de l’espérance de vie (9e, Fipeco, 2023) : non affiché, figure à créer (voir étape 5).
- OFCE (Madec, 26 novembre 2025) : effet des transferts hors retraites, mesure nationale, 7,7 points en 2013 contre 6,1 en 2023 ; part des ménages pauvres sortis de la pauvreté par les prestations, 37 % en 2017 contre 28 % en 2023. Non affichés : **figures à créer** (`ofce_transfers_poverty_effect_2013_pp`, `ofce_transfers_poverty_effect_2023_pp`, `ofce_poor_lifted_share_2017_pct`, `ofce_poor_lifted_share_2023_pct`), à ne pas mélanger avec la mesure Eurostat avant/après transferts.
- 46,8 % avant prestations, retraites comprises [[fig:arop_before_transfers_2025_pct]] (source [[src:f01:es-silc]], Eurostat ilc_li09) ; 30,5 points [[fig:poverty_reduction_transfers_2025_pp]] (statut « réserve » : surtout les retraites, en partie revenu différé) ; 3e sur 27 [[fig:poverty_reduction_transfers_2025_rank]] (source [[src:f10:S33]], calcul de la plateforme d’après Eurostat ilc_li09 et ilc_li02).

---

## Étape 9. Le meilleur contre-argument

**Texte affiché**

<!-- box-side: droite -->
> **Le meilleur contre-argument**
>
> **« Les résultats ne justifient plus le niveau de la dépense : l’argent est mal utilisé. »**
>
> Pour Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire), l’efficience de la dépense de santé « pourrait être nettement améliorée ». Le Fonds monétaire international (FMI ; organisation internationale) veut « rationaliser les dépenses inefficaces et réorienter les dépenses courantes et sociales vers les priorités » (traduit de l’anglais). Il demande aussi de protéger les plus vulnérables [[src:f06:imf_aiv2026]].
>
> Les chiffres de la pauvreté vont dans ce sens. Le taux après transferts est aujourd’hui exactement dans la moyenne européenne [[fig:arop_2025_pct|contexte]] [[fig:eu27_arop_2025_pct|contexte]]. Il était de 13,6 % de la population en 2015 [[fig:arop_2015_pct]]. La Belgique obtient une baisse comparable et arrive à un taux plus bas [[src:f10:S33]].
>
> Sans les retraites, les transferts ne font plus baisser le taux que de 10,2 points [[fig:poverty_reduction_excl_pensions_2025_pp]]. La France n’est alors que 6e de l’UE [[fig:poverty_reduction_excl_pensions_2025_rank]].
>
> *Sources : Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire),* L’efficience des dépenses d’assurance maladie, *30 janvier 2026 ; FMI (organisation internationale), déclaration de fin de mission au titre de l’article IV, 21 mai 2026 ; Eurostat (office statistique de l’Union européenne), statistiques de l’Union européenne sur le revenu et les conditions de vie (EU-SILC), 2025.*
>
> **Ce qu’on peut répondre**
>
> La redistribution fait un travail réel : retraites comprises, la baisse de la pauvreté est la 3e de l’UE [[fig:poverty_reduction_transfers_2025_rank]]. Ce rang tient surtout aux retraites.
>
> La hausse de la pauvreté a aussi d’autres causes selon l’OFCE (Sciences Po, sensibilité keynésienne) : inflation, fin des aides exceptionnelles, emplois peu payés.
>
> Certains services manquent de moyens, mais le diagnostic est discuté. La France a moins de juges par habitant que la plupart des pays européens [[src:f04]] [[src:f10]]. La Cour des comptes (juridiction financière) y voit aussi un problème de gestion.
>
> Sur un point, l’objection tient : hors retraites, l’effet des transferts français est bon, sans être exceptionnel [[src:f01:es-silc]].

**Visuel et animation**
- Encadré fixe, jamais replié (glossaire, §4.6), sur le même écran que le bilan de l’étape 8.
- Mini-graphique « avant / après transferts » par pays (dot plot double, fichier 20, §4.14 ; `data/debates/computed_poverty_reduction_by_transfers.csv`). Seules les valeurs françaises sont dans `figures.json` (46,8 % ; 30,5 et 10,2 points ; 3e et 6e rangs) ; les valeurs des autres pays restent au survol, sans être citées dans le texte.

**Pastilles**
- « exactement dans la moyenne européenne » [[fig:arop_2025_pct|contexte]] [[fig:eu27_arop_2025_pct|contexte]] (16,3 % chacun, affiché à l’étape 3) ; 13,6 % en 2015 [[fig:arop_2015_pct]] (mention « rupture de série »)
- Belgique (baisse de 30,7 points, taux plus bas) [[src:f10:S33]] ; « financé par l’emprunt » déplacé à l’étape 8 le 30 octobre 2026 (la remarque de l’Insee porte sur l’ensemble des services publics et des transferts, pas sur l’efficience)
- 10,2 points [[fig:poverty_reduction_excl_pensions_2025_pp]] (statut « réserve » : retraites comptées comme revenu ; moyenne UE-27 8,1, non affichée) ; 6e sur 27 [[fig:poverty_reduction_excl_pensions_2025_rank]] [[src:f01:es-silc]]
- Fipeco, *L’efficience des dépenses d’assurance maladie*, 30 janvier 2026, https://fipeco.fr/pdf/EfficienceD%C3%A9pensesSant%C3%A9.pdf (« pourrait être nettement améliorée » ; « certainement pas le seul déterminant ») : **entrée à ajouter à sources.json**
- FMI, déclaration de fin de mission au titre de l’article IV, 21 mai 2026, https://www.imf.org/en/news/articles/2026/05/21/mcs-052126-france-staff-concluding-statement-of-the-2026-article-iv-mission (citation complète traduite de l’anglais : « rationalize inefficient spending and reallocate current and social spending toward priority areas » ; « preserve equity and protect the most vulnerable if measures are well targeted and carefully sequenced ») [[src:f06:imf_aiv2026]]
- Réponse : 3e baisse de l’UE retraites comprises [[fig:poverty_reduction_transfers_2025_rank]] ; causes de la hausse (OFCE, Madec, 26 novembre 2025, voir étape 3) ; juges [[src:f04]] [[src:f10]] ; Cour des comptes 2021 (justice, voir étape 6) ; CAE note n° 84 (voir étape 6) ; Fipeco ; « l’objection tient » hors retraites [[src:f01:es-silc]]. Le « changement de méthode » ne sert plus de réponse (30 octobre 2026).

---

## Étape 10. Trois lectures du même bilan

**Texte affiché**

> Pour les uns, des services manquent de moyens. L’Union syndicale des magistrats (syndicat de magistrats) le dit pour la justice [[src:f10]]. L’OFCE (Sciences Po, sensibilité keynésienne) note que les prestations sortent moins de ménages de la pauvreté qu’avant.
>
> Pour d’autres, l’argent est mal utilisé : Fipeco pour la santé, la Fondation iFRAP (libérale) pour l’école et les frais de gestion. Le FMI (organisation internationale) veut réorienter la dépense vers les priorités [[src:f06:imf_aiv2026]].
>
> Pour d’autres encore, la première question est le niveau de la dépense. L’Institut Montaigne (libéral-centriste) veut d’abord décider ce que l’État doit faire [[src:f10]]. La Cour des comptes (juridiction financière) constate que, faute d’économies, la dépense hors intérêts croît un peu plus vite que l’économie [[src:f20:cour26]].
>
> Selon les domaines, les données donnent raison à l’une ou à l’autre. Le débat porte à la fois sur **combien** et sur **où** dépenser.

**Visuel et animation**
- Bloc de texte simple, sur le même écran que l’encadré de l’étape 9. Les trois lectures ont la même typographie et la même couleur neutre (règle de symétrie, fichier 20, P7).
- Sous le texte, liens vers les fiches thématiques (fonction publique et résultats ; santé ; éducation).

**Pastilles**
- Union syndicale des magistrats, justice seulement [[src:f10]] (CEPEJ, cycle 2024, données 2022, transcrite par l’USM, fichier 10, §8.1). Aucun autre texte publié sur le manque de moyens de la santé ou de l’école n’a été ouvert par la confrontation du 30 octobre 2026 : ne pas étendre la position de l’USM à ces domaines.
- OFCE (Madec, 26 novembre 2025, voir étape 8) : **entrée à ajouter à sources.json**
- Lecture « mal utilisé » : Fipeco (santé, 30 janvier 2026), Fondation iFRAP (école, octobre 2021 ; frais de gestion, 7 juin 2026), FMI [[src:f06:imf_aiv2026]] (URL aux étapes 5, 6 et 9)
- Lecture « niveau » : Institut Montaigne, *Budget base zéro*, novembre 2025 (les revues de dépenses ne sont que « le dernier maillon d’une recherche d’économies ») [[src:f10]] ; Cour des comptes, *La situation et les perspectives des finances publiques*, 25 juin 2026, page de présentation https://www.ccomptes.fr/fr/publications/la-situation-et-les-perspectives-des-finances-publiques-17 (dépense primaire « à un rythme légèrement supérieur à la croissance économique », « faute d’économies ») [[src:f20:cour26]]
- Étiquettes d’orientation : glossaire §1.13 après la décision D-labels (Institut Montaigne « libéral-centriste », financement dans la pastille source).

---

## Étape 11. Transition

**Texte affiché**

> Vous savez maintenant combien la France dépense, comment elle se finance et ce qu’elle obtient en échange.
>
> Reste la question la plus difficile : que faire ? Le vieillissement, l’emploi et la hausse des intérêts imposent des choix. Le chapitre 7, « Les choix », en présente l’ampleur.
>
> **Pour aller plus loin**
>
> - Fiche « Santé » : mortalité évitable, reste à charge, cancer.
> - Fiche « Fonction publique et résultats » : juges, enseignants, PISA.
> - Fiche « Retraites » : niveau de vie des retraités.
> - Fiche « Taux d’emploi, heures travaillées et productivité ».
> - Fiche « Protection sociale par risque » : effet des retraites.
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
   - Justice : ~~juges professionnels pour 100 000 habitants et médiane européenne~~ (`judges_per_100k_2022` et `cepej_median_judges_2022`, CEPEJ-STAT, ajoutés le 31 octobre 2026 et affichés à l’étape 6) ; reste la durée des procédures civiles en première instance et sa médiane européenne, non confirmée (fichier 04, §6.4 ; fichier 10, §8.1 ; fichier 20, §4.2 GF03). Attention : les fichiers 04/20 et 10 citent des valeurs et médianes CEPEJ légèrement différentes ; arbitrer dans le fichier 00 d’abord.
   - Pauvreté : ~~taux avant transferts, réduction par les transferts avec et sans retraites, rang UE~~ (ajoutés le 25 octobre 2026 et affichés aux étapes 8 et 9) ; pauvreté des enfants (fichier 20, §4.3).
   - Santé : mortalité évitable par les soins et rang UE, reste à charge, part des frais de gestion dans la dépense de santé, survie au cancer, besoins non satisfaits pour délai (fichier 12, §0 et §5-6).
   - Éducation : évolution PISA depuis 2015, scores en lecture et en sciences, salaire des enseignants (fichier 13, §0 ; fichier 04, §6.1).
   - Ajouts demandés par l’audit du 25 octobre 2026 : `eu27_arop_2015_pct` (Eurostat ilc_li02, avec note de rupture de série ; fichier 10, §9.2) pour rétablir à l’étape 9 la comparaison « 13,6 % contre … pour l’UE en 2015 » ; espérance de vie 2024 de l’Espagne, de la Suède et de l’Italie (Eurostat demo_mlexpec, https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_mlexpec ; fichier 10, §8.2) pour l’étape 5 ; ~~`productivity_per_hour_pps_2025` et son rang~~ (ajoutés le 25 octobre 2026, affichés à l’étape 7).
   - Ajouts demandés par la confrontation aux sources publiques du 30 octobre 2026 (voir notes de relecture et listes « Pastilles ») : niveau de vie des retraités avec loyers imputés (COR) ; dépense de santé publique ou obligatoire et rangs OCDE (Fipeco) ; dépense par élève 2021 et écarts primaire / secondaire (CAE n° 84) ; variations 2014-2024 du taux d’emploi et du taux de pauvreté, effet des transferts sur la mesure nationale (OFCE, Madec) ; déficit et dette par unité de consommation de la redistribution élargie (Insee Analyses n° 118) ; frais de gestion AMO + AMC (iFRAP, avec sa réserve) pour le chapitre 2.
   - Sources à ajouter à sources.json (aucune pastille possible avant) : OFCE (Madec, 26 novembre 2025) ; CAE n° 84 (mai 2025) ; CAE *Objectif plein emploi* (4 mars 2025) ; Fipeco *L’efficience des dépenses d’assurance maladie* (30 janvier 2026) et *Les montants laissés à la charge des ménages* (30 janvier 2024) ; Fondation iFRAP (7 juin 2026 ; *Société Civile* n° 227, octobre 2021) ; Rexecode DT n° 98 (décembre 2025) ; Insee Analyses n° 26 (juin 2016) ; Cour des comptes, note justice (21 octobre 2021, note primaire à ouvrir). URL dans les listes « Pastilles » des étapes concernées.
   Une fois ajoutés, remplacer les formulations qualitatives des étapes 5 à 8 par les chiffres avec leurs pastilles [[fig:...]].
2. Année et groupe de chaque comparaison internationale : pauvreté UE-27, EU-SILC 2025 ; espérance de vie UE-27, 2024 ; pauvreté des 65 ans et plus OCDE, 2022 (seuil 50 %) ; PISA OCDE, 2025 ; emploi et heures UE-27, 2025 ; santé zone euro ZE21, COFOG 2024.
3. Calculs « illustratif » (étape 2) : formules du convertisseur d’yardsticks.json (`conversions`). Les montants de 2024 ou de 2022 rapportés à la dépense 2025 sont des ordres de grandeur.
4. Étapes 9 et 10 : vérifier avec l’équipe juridique l’attribution de chaque lecture à ses défenseurs (Union syndicale des magistrats ; Cour des comptes, FMI, Institut Montaigne, Fondation iFRAP) et les citations exactes (fichier 10, §4.1, §5.4, §8.1, §8.2 ; fichier 04, §8). Les syndicats d’enseignants ne sont plus cités : aucune prise de position de leur part n’a été retrouvée dans la base.
-->

---

## Notes de relecture

**Passe du 31 octobre 2026 : chiffres CEPEJ de la justice et pas d’étiquette de camp sur les idées**

- Étape 6, justice : pastilles [[fig:judges_per_100k_2022]] (11,3 juges professionnels pour 100 000 habitants, 2022) et [[fig:cepej_median_judges_2022]] (médiane du Conseil de l’Europe, 17,6) ajoutées, lues sur CEPEJ-STAT (mise à jour du 25/10/2024). Mise en garde ajoutée : le ratio exclut les nombreux juges non professionnels (tribunaux de commerce, prud’hommes). La phrase « Ces données de 2022 viennent surtout de l’Union syndicale des magistrats » est retirée (les juges viennent désormais de la CEPEJ) ; l’Union syndicale des magistrats reste citée pour la durée des procès civils et le jugement « critique » [[src:f10]]. Lecture de la Cour des comptes (2021) inchangée. Étape 9 inchangée (formulation qualitative compatible avec les nouveaux chiffres).
- Graphique 2 : volet « juges » débloqué (France et médiane ; valeurs des autres pays à ajouter à `figures.json` avant les petits multiples) ; volet « délais civils » toujours bloqué (médiane européenne non confirmée, aucune entrée dans `figures.json`). Notes de l’étape 6 et de l’étape 11 mises à jour.
- Décision du 31 octobre 2026 (glossaire §1.13, règle 8) : aucun libellé de camp dans le texte affiché de ce chapitre ; dans les notes, « les contre-preuves des deux camps » → « les contre-preuves » et « aucun texte publié de gauche » → « aucun autre texte publié sur le manque de moyens ».
- Longueur : « Le même bilan nourrit donc plusieurs lectures. » (étape 10) retiré, redondant avec le titre de l’étape, pour rester sous 2 200 mots. Contrôle : `validate.py --strict` PASS ; 2 198 mots visibles (2 192 avant).

**Confrontation aux sources publiques (2026-10-30)**

*Décision : pas de relecteurs humains ; le texte est confronté aux positions publiées d’économistes et d’institutions de sensibilités différentes. Seuls les textes effectivement ouverts par la confrontation (URL et date dans les listes « Pastilles ») sont cités. Aucun chiffre nouveau n’est affiché : faute d’identifiant dans `platform/data`, les apports chiffrés sont écrits en qualitatif et listés en note 1 (figures et sources à créer).*

*Points corrigés (verdicts « partly_supported » et « not_supported »)*
1. *01 et 18, classement en trois colonnes* : **appliqué**. Étape 8 : groupe et année écrits à côté de chaque indicateur ; règle affichée (« dans la moyenne » = écart nul ou jugé non significatif par la source ; tout autre écart compte) ; effet du groupe signalé avec l’exemple OCDE de Fipeco (espérance de vie moins bien classée que dans l’UE-27).
2. *02 et 03, calendrier et 68 € par jour* : **appliqué**. Étape 2 : « ordre de grandeur, d’après notre calcul : parts de 2024, dépense de 2025 » dans le texte affiché ; pastilles `calc` (illustratif) inchangées. Aucun texte publié ne donne ni ne conteste ces calculs (Insee Analyses n° 118 rappelle seulement que les montants par personne dépendent de conventions).
3. *04, « exactement dans la moyenne »* : **conservé** (16,3 % contre 16,3 %), avec le 11e taux le plus élevé juste après, qui montre que seize pays font mieux. La sensibilité au seuil et au groupe passe par la règle de l’étape 8.
4. *07, seuils de 50 % et 60 %* : **conservé** (séparation des seuils déjà faite) ; direction confirmée par le COR (*Rapport annuel* 2026, partie 3, chapitre 2).
5. *10, espérance de vie* : **appliqué**. Lecture de Fipeco (rang OCDE moins bon que le rang de dépense) ajoutée à l’étape 8 ; « pourrait être nettement améliorée » dans l’encadré. Valeurs de l’Espagne, de la Suède et de l’Italie toujours non affichées (note 1).
6. *11, frais de gestion* : **appliqué**. « Les plus élevés de l’UE » retiré (non confirmé : iFRAP ne compare qu’aux Pays-Bas). Explication par la superposition des deux assurances conservée ; iFRAP et sa propre réserve ajoutés. Aucun montant ici (chapitre 2 propriétaire) ; recommandation pour le chapitre 2 : présenter l’économie de 7,6 Md€ de l’iFRAP comme un plafond, avec sa réserve.
7. *13, dépense par élève* : **appliqué**. « À peu près autant » remplacé par la lecture du CAE (un peu plus que la moyenne de l’OCDE en 2021, moins en primaire, plus dans le secondaire), sans chiffre faute de figure.
8. *15, 16 et 17, emploi, heures, productivité* : **appliqué**. Comparaison « plus d’heures qu’en Allemagne ou aux Pays-Bas » retirée (non confirmée) ; Rexecode cité pour « pas la durée la plus courte » ; fragilité des comparaisons d’heures (Insee et Destatis, 2016) ; effet de sélection présenté comme une hypothèse et recul depuis 2019 comme notre calcul ; réserve du CAE (la production augmente moins vite que l’emploi) ajoutée, son chiffrage reste au chapitre 7.
9. *22, attributions de l’encadré* : **appliqué**. Citation du FMI complétée (« réorienter les dépenses courantes et sociales vers les priorités » ; protéger les plus vulnérables). La Cour des comptes sort de l’encadré : la page ouverte dit « faute d’économies », pas « argent mal utilisé ». Elle est citée à l’étape 10 dans la lecture « niveau de la dépense ». La thèse « mal utilisé » est portée par Fipeco (santé) et le FMI.
10. *06, mesure Insee* : **appliqué**. France métropolitaine, stable par rapport à 2023, hors sans-abri et personnes en institution ; pastille vers l’*Insee Première* n° 2117 ([[src:f00:row47]]). « Elle confirme la hausse » retiré.
11. *12 et 21* (« soutenu » et « présenté équitablement ») : nuance du CAE ajoutée (les dépenses ciblées sont efficaces) à l’étape 6 ; « ces rapprochements ne prouvent pas » conservé à l’étape 8.

*Contre-arguments ajoutés (verdict « missing_counterargument »)*
12. *05 et 23, hausse de la pauvreté* : explication causale de l’OFCE (Pierre Madec, 26 novembre 2025 : inflation, fin des aides exceptionnelles, emplois peu payés) à l’étape 3 et dans la réponse de l’étape 9. Les ruptures de série 2020 et 2022 sont présentées comme un relevé des métadonnées Eurostat (fichier 10), non chiffré, et ne servent plus de réponse dans l’encadré.
13. *08, niveau de vie des retraités* : variante du COR avec loyers imputés (retraités au-dessus de l’ensemble de la population) et lecture de l’Institut Montaigne (générosité du système, mais aussi forte hausse du nombre de retraités), à l’étape 4. Chiffre de 6,5 % non affiché (figure à créer).
14. *19, effet des transferts* : constat de l’OFCE (mesure nationale, hors retraites : moins de ménages pauvres sortis de la pauvreté qu’en 2017) à l’étape 8, sans mélange avec la mesure Eurostat ; chiffres non affichés (figures à créer).
15. *09, deux mesures de la dépense de santé* : mesure publique ou obligatoire (Fipeco, OCDE) à l’étape 8 ; à l’étape 5, la mesure par habitant est présentée comme « le coût total, pas la seule charge publique ».
16. *14, justice* : constat de la Cour des comptes (2021 : budget en nette hausse depuis 2011, délais civils non réduits, meilleure répartition des effectifs) ajouté à côté des données de l’Union syndicale des magistrats, présentées comme « données de 2022 » d’un syndicat. Graphique justice toujours bloqué. **Réserve** : la note de la Cour n’a été lue que dans un résumé de presse (Le Monde du Droit) ; ouvrir la note primaire avant publication.

*Critiques de gauche*
- **Appliquées (8)** : (1) cause de la hausse de la pauvreté (OFCE) et ruptures de série présentées comme un relevé de métadonnées ; (2) position de l’Union syndicale des magistrats limitée à la justice, lecture de l’OFCE sur l’effet des transferts ajoutée à l’étape 10, « couper partout » retiré ; (3) citation complète du FMI, Cour des comptes limitée à « faute d’économies » et séparée de la lecture « mal utilisé » ; (4) emploi et pauvreté en hausse ensemble depuis 2014, emplois peu payés (OFCE), et consigne de visuel ajoutée ; (6) dépense par élève par niveau et dépenses ciblées efficaces (CAE, étiqueté comme organisme public) ; (8) glose des 56 % corrigée (défense, police, justice, répartition par convention) et remarque sur l’emprunt déplacée de l’encadré vers l’étape 8 ; (9) limites de la mesure Insee ; (10) fragilité des comparaisons d’heures, recul depuis 2019 et effet de sélection requalifiés.
- **Appliquée en partie (2)** : (5) groupe, année et règle de classement affichés ; la mention de l’Observatoire des inégalités (2022) est **rejetée** : l’organisme n’a pas d’étiquette au glossaire §1.13 (règle 7), et son édition de 2022 repose sur des données plus anciennes et un autre seuil ; le recul relatif est déjà porté par l’OFCE. (7) justice : le paragraphe qualitatif est rééquilibré (données syndicales et constat de la Cour), le budget par habitant « au-dessus de la médiane, sous la moyenne » est retiré du texte affiché en attendant les chiffres CEPEJ primaires ; les chiffres de l’Union syndicale des magistrats (37,3 agents non juges pour 100 000 habitants ; 72,50 € par habitant contre 140,73 € en Allemagne) ne sont pas affichés : aucune figure, source secondaire et intéressée.
- Phrase demandée « aucune source de gauche publiée n’a été trouvée sur la santé et l’école » : écrite dans la pastille de l’étape 10, pas dans le texte affiché (règle §4.6 : aucune référence interne affichée).

*Critiques de droite*
- **Appliquées (9)** : (1) thèse séparée en efficience (Fipeco, iFRAP, FMI) et niveau de la dépense (Institut Montaigne, Cour des comptes) ; conclusion « combien et où » au lieu de « aussi où » ; (2) « couper partout » retiré, deux lectures formulées sans caricature, seconde moitié de la citation du FMI reproduite ; (3) justice : constat de la Cour à côté des données syndicales, source et année des données indiquées ; (4) variante du COR avec loyers imputés et lecture de l’Institut Montaigne ; (5) deux mesures de la dépense de santé, chacune avec la question à laquelle elle répond ; (6) rang OCDE et lecture de Fipeco sur l’efficience ; (8) école : « un peu au-dessus de la moyenne de l’OCDE », pays plus efficaces, lecture de l’iFRAP (organisation et part variable de la paie) ; (9) changement de méthode retiré de la réponse de l’encadré, limites de la mesure Insee ajoutées ; (10) Allemagne et Pays-Bas retirés, Rexecode cité, effet de sélection en hypothèse, réserve du CAE.
- **Appliquées en partie (3)** : (7) frais de gestion : superposition des assurances et comparaison néerlandaise de l’iFRAP ajoutées, mais le montant de 17 Md€ n’est pas affiché : aucune figure, et le chapitre 2 est propriétaire des montants de santé (décision D-ownership) ; (11) les deux mesures de l’effet des transferts sont dans le même encadré et la réserve suit le 3e rang (« ce rang tient surtout aux retraites ») ; le 3e rang reste la première réponse, car c’est le constat que conteste l’encadré, désormais accompagné de sa réserve ; (12) règle des colonnes affichée et réserve du calendrier dans le texte. **Rejeté** : la suppression du calendrier de 241 jours. C’est un étalon de la plateforme (glossaire §1.13), affiché comme calcul illustratif avec sa formule ; il ne prétend pas être une position publiée.
- **Rejetée** : la nuance « plusieurs pays du Benelux et du Nord sont plus bas » (critique 9, fin). Le 11e taux le plus élevé, affiché juste après, dit déjà que seize pays font mieux ; les valeurs pays restent dans le graphique, sans chiffre dans le texte.

*Contrôles* : `python3 -I platform/data/validate.py --strict` : 0 erreur et 0 avertissement propres à ce fichier ; 2 192 mots visibles (plafond 2 200), durée de lecture portée à 9 minutes. Coupes faites pour rester sous le plafond : définition Eurostat répétée (étape 3), détail de la liste « Pour aller plus loin » et phrase sur le comparateur (étape 11, le bouton reste), resserrement des étapes 5 à 9 ; la mention de Fipeco dans la réponse de l’encadré (« pas le seul déterminant ») est retirée, l’idée restant à l’étape 8. Reste un avertissement transversal qui ne vient pas de ce fichier : étiquette de la Cour des comptes absente au chapitre 1.

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

