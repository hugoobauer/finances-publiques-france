<!-- page
slug: age-65
phrase: Il faut reculer l’âge de départ à 65 ans
sujets: retraites
levier: S1
debats: 2.3, 2.5, 2.7, 2.8, 7.1
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : research/03-pensions.md (§3.2, §4.1, §4.2, §7.3, §7.4, §9, 25 octobre 2026) ; research/17-fiscal-multipliers-for-simulator.md (tableau des modèles d’âge, source S10) ; research/11-2027-candidate-programs-costing.md §4.3 et §4.4 ; fr/site/debats.md points 2.3, 2.5, 2.7, 2.8, 7.1 ; fr/conception/04-sujets-et-objections.md (ligne 3 de la section Retraites, rang 8) ; platform/data/simulator-levers.json (levier S1, positions 62, 63, 64, 65) ; proposals.json (horizons_pensions_45y_65, lr_pensions) ; sources.json (f03:cor26, f11:S8, f11:S13, f17:S1, f17:S10).
- Données manquantes (aucun identifiant dans figures.json, donc omises du texte affiché) :
  - le rendement de la position 65 du levier S1 : de 9 à 19 Md€ par an à terme (10 à 20 ans), soit de 5,9 à 12,5 % du déficit ; sans identifiant, il n’est pas affiché ;
  - l’effet d’un an de recul de l’âge selon les modèles du COR (DG Trésor, OFCE, I-MIP) : de +0,3 à +0,65 point de PIB sur le solde primaire des administrations publiques à 20 ans, et de 200 000 à 240 000 emplois ;
  - l’effet d’un an de moins (64 à 63) chiffré par la Cour des comptes : 5,8 Md€ pour le système de retraites, 13 Md€ pour l’ensemble des administrations publiques en 2035 ;
  - la comparaison des modèles de la Cour des comptes (février 2025, tableau 4) : PIB de −0,1 % (OFCE) à +1,1 % pour deux ans d’âge, et report d’environ 20 % des économies brutes sur d’autres prestations (Drees/Dares, réforme de 2010) : dits en mots avec [[src:f17:S10]], sans chiffre ;
  - l’âge effectif de sortie (hommes : 61,9 ans en France, 64,7 en moyenne OCDE, OCDE 2024) et l’âge normal futur (65 ans en France, 67 en Allemagne) : base d’un « Et ailleurs ? » sur l’âge, absents de figures.json ;
  - un rang de la France « après la mesure » : aucun identifiant rank_after_* pour le recul de l’âge (rank_after_old_age_cut_0_5pt simule une baisse de la dépense de 0,5 point, sans lien établi avec un an d’âge) ; ligne retirée à la vérification ;
  - la source de la lecture de la Fondation iFRAP (« Les six angles morts du rapport du COR », juin 2026) n’a pas d’entrée dans sources.json ; la pastille [[src:f03:cor26]] renvoie aux simulations du COR qu’elle commente ;
  - la part de l’horizon 2032 dans les 42 Md€ de LR (environ 9 Md€ pour la mesure d’âge) : seulement dans le texte de lr_pensions.
- Choix faits : pas de montant dans « En bref » ni de part du déficit pour la mesure elle-même, faute d’identifiant ; la part du déficit du chiffre d’Horizons (30 / 151,6, soit 19,8 %) n’est pas affichée, car [[calc:]] n’accepte pas d’identifiant de proposals.json (erreur du validateur) ; le chiffre d’Horizons est de plus d’un périmètre plus large. Le chiffre de LR (42 Md€) reste cumulé sur cinq ans, hors de l’échelle annuelle (écart à confirmer avec les 40 Md€ de Franceinfo, débats 2.7). Solidaires n’est pas nommée (pas d’étiquette au glossaire, règle 7) : sa lecture (manque de recettes plutôt qu’excès de dépense, débats 2.3 et 2.5) est rapportée de façon neutre (« D’autres jugent », règle 8) avec renvoi à la page Débats.
- Vérification (31 octobre 2026) : « solde de l’État » remplacé par « ensemble des administrations publiques » (les modèles du COR mesurent le solde primaire des administrations publiques) ; « le confirment » retiré (verdict) ; COR étiqueté à la première mention ; projections dites comme telles ; « l’effet plein demande de dix à vingt ans » remplacé (dix et vingt ans sont les horizons des simulations, pas la durée de montée en charge) ; phrase sur la croissance sourcée à la Cour des comptes (f17:S10 : les modèles divergent à dix ans, jusqu’au signe), alors que debats 2.8 la notait non vérifiée ; reports sur d’autres prestations sourcés (f17:S10) ; ajout de la remarque du COR sur le temps libre (research/03 §9.3) ; LR daté d’octobre 2026 (plan du 12 octobre, f11:S8) et non de septembre, décote entre 63 et 65 ans précisée ; « il ne recommande pas d’âge » (COR) retiré, non vérifié ; ajout de la Cour des comptes et d’une lecture opposée sans nom ; années ajoutées dans « Et ailleurs ? » ; ligne du rang après baisse de 0,5 point retirée (ne mesure pas cette mesure).
-->

> # « Il faut reculer l’âge de départ à 65 ans »
>
> **En bref.** Reculer l’âge légal de départ améliore le solde des retraites et celui de l’ensemble des administrations publiques. Tous les modèles réunis par le Conseil d’orientation des retraites (COR ; instance d’études et de concertation sur les retraites) le montrent [[src:f03:cor26]]. Le gain d’un recul à 65 ans n’a pas encore de chiffre vérifié sur ce site.
>
> ## Ce qui est vrai
>
> La retraite est le premier poste de la dépense publique : 422,2 milliards d’euros en 2025, soit 14,1 % du produit intérieur brut (PIB) [[fig:pensions_cor_2025_eur_bn]] [[fig:pensions_cor_2025_pct_gdp]].
>
> Selon le scénario de référence du COR, la dépense reste proche de ce niveau en 2045 (14,2 % du PIB) [[fig:pensions_cor_2045f_pct_gdp]]. Elle monte ensuite à 15,3 % en 2070 [[fig:pensions_cor_2070f_pct_gdp]]. Les ressources, elles, passent de 13,9 % du PIB en 2025 à 12,9 % en 2070 [[fig:pension_resources_2025_pct_gdp]] [[fig:pension_resources_2070f_pct_gdp]]. Ce sont des projections.
>
> Travailler plus longtemps réduit les pensions versées et augmente les cotisations. Dans les simulations du COR, l’effet sur le solde public est donc positif dans tous les modèles. Sa taille varie selon le modèle [[src:f03:cor26]].
>
> ## Combien
>
> Le simulateur de ce site propose ce recul d’un an. Son rendement à terme n’a pas encore de chiffre vérifié : nous n’affichons ni son montant ni sa part du déficit.
>
> Les partis annoncent leurs propres chiffres. Horizons annonce environ 30 milliards d’euros par an à effet plein pour son plan [[prop:horizons_pensions_45y_65]]. Ce chiffre couvre plus que l’âge seul. Pour repère, le déficit public de 2025 est de 151,6 milliards d’euros [[fig:deficit_2025_eur_bn]].
>
> Dans l’autre sens, un retour général à 60 ans coûterait de 43 à 58 milliards d’euros par an [[fig:return_60_general_cost_eur_bn]]. Ces deux chiffrages de 2024 portent sur des périmètres différents.
>
> ## Les limites
>
> Le gain arrive lentement, car la mesure touche les générations une à une. La loi de financement de la sécurité sociale pour 2026 suspend la hausse vers 64 ans jusqu’en janvier 2028 [[src:f03:cor26]].
>
> Le résultat dépend aussi de l’emploi des seniors. S’ils ne trouvent pas de travail, une partie des économies se reporte sur le chômage, l’invalidité ou les minima sociaux [[src:f17:S10]]. À dix ans, les modèles ne s’accordent pas sur l’effet sur la croissance : il va d’un léger recul à une nette hausse [[src:f17:S10]].
>
> Le COR rappelle aussi qu’un âge plus élevé augmente la production, mais réduit le temps libre. Le bilan dépend des préférences de chacun [[src:f03:cor26]].
>
> Enfin, une économie réduit le déficit de moins que son montant : elle freine un peu l’activité, donc les recettes. Les sources que nous avons lues décrivent toutes cet effet, d’une taille variable [[src:f17:S1]].
>
> ## Qui dit quoi
>
> - **Fondation iFRAP (libérale)**, juin 2026 : dans les simulations du COR, seule une hausse de l’âge de départ améliore le PIB, l’emploi et le solde public [[src:f03:cor26]]. Selon elle, les hausses de cotisations et les baisses de pensions freinent l’activité.
> - **Cour des comptes (juridiction financière)**, février 2025 : elle se fie plus aux études sur la réforme de 2010 qu’aux modèles de court terme. Ceux-ci prévoient plus de chômage [[src:f17:S10]].
> - **Horizons**, parti d’Édouard Philippe, septembre 2026 : 65 ans et 45 annuités d’ici dix ans [[prop:horizons_pensions_45y_65|contexte]]. Le parti chiffre son plan à environ 30 milliards d’euros par an [[prop:horizons_pensions_45y_65]]. Chiffre annoncé ; source : Franceinfo [[src:f11:S13]].
> - **Les Républicains**, octobre 2026 : une décote entre 63 et 65 ans et le taux plein à 65 ans [[prop:lr_pensions|contexte]]. Le parti annonce environ 42 milliards d’euros d’économies au total sur cinq ans [[prop:lr_pensions]] [[src:f11:S8]]. Chiffre annoncé, non comparable aux chiffres par an.
>
> D’autres jugent que la dépense de retraites est stable et que le problème vient d’un manque de recettes. La page « Débats » donne leurs sources. Nous n’avons trouvé aucune contre-estimation publiée des deux chiffres de partis.
>
> ## Et ailleurs ?
>
> En 2024, la France consacre aux dépenses de vieillesse 13,4 % du PIB [[fig:cofog_old_age_2024_pct_gdp]]. La moyenne de l’Union européenne à 27 (UE-27) est de 10,6 % [[fig:eu_cofog_old_age_2024_pct_gdp_eu27]]. La France est 4e sur 27 [[fig:eu_cofog_old_age_2024_rank]].
>
> Par habitant, en standards de pouvoir d’achat (SPA), la France a la 5e dépense de retraite la plus élevée sur 27 en 2024 [[fig:pension_exp_per_capita_pps_2024_rank]]. Ces chiffres ne disent pas à quel âge on part dans chaque pays.
>
> En 2022, 6,1 % des 65 ans et plus sont pauvres en France [[fig:old_age_poverty_oecd_2022_pct]], selon l’Organisation de coopération et de développement économiques (OCDE). La moyenne de l’OCDE est de 14,8 % des 65 ans et plus [[fig:oecd_old_age_poverty_2022_pct]].
