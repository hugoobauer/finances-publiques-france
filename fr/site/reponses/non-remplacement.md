<!-- page
slug: non-remplacement
phrase: Ne remplaçons pas tous les départs en retraite
sujets: fonction-publique, train-de-vie, deficit-dette
montant: lr_non_replacement_400k
levier: S4
debats: 8.12, 7.3, 1.8
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/conception/04-sujets-et-objections.md (ligne rang 7), fr/site/debats.md points 8.12, 7.3 et 1.8 ; research/11-2027-candidate-programs-costing.md (variantes, règle de retour de 50 % de la RGPP, réalisé 2009 [f11:S36], notes de 25 octobre 2026) ; platform/data/proposals.json (lr_non_replacement_400k, horizons_replace_2_of_3, re_100k_posts, rn_posts_not_filled) ; figures.json.
- Données manquantes : (1) coût moyen par poste de 63 000 € et nombre total d’agents publics (5,9 millions) : dans research/11 seulement, sans identifiant ; (2) nombre de postes de chaque variante (400 000, 250 000, 100 000, 201 000) : dans le texte des mesures de proposals.json mais pas comme valeur chiffrée ; (3) part du gain rendue aux agents (50 % en règle, environ 80 % réalisé en 2009 [f11:S36]) ; (4) fourchette de multiplicateur 0,7 à 0,8 de l’OFCE et « proche de 1 » du HCFP (debats 7.3) : affichées sans chiffre, avec [[src:f17:S8]] et [[src:f17:S1]] ; (5) moyenne OCDE de l’emploi public et rang UE-27 de la rémunération des agents publics ; (6) rang de la France après la mesure : aucun identifiant rank_after_* pour les effectifs ; (7) estimation de l’iFRAP de 250 000 postes (environ 15 Md€) et écart de personnel de 2,98 points de PIB en 2019 (debats 1.8) ; la Fondation iFRAP (libérale, 2 février 2022) et l’OFCE (Policy Brief n° 17, 2017) sur le nombre d’agents n’ont pas d’identifiant dans sources.json, d’où leur absence de « Qui dit quoi » ; (8) coût ponctuel des indemnités de départ volontaire du plan de Renaissance : non chiffré.
- Vérification du 31 octobre 2026 : « calcul brut » retiré (les bas de fourchette sont nets du retour aux agents) ; « 25 milliards par an » des Républicains remplacé par le montant annoncé sans horizon (recherche 11, §5.3 : l’horizon est ambigu, la lecture annuelle est celle de la plateforme) ; départs volontaires de Renaissance ajoutés aux limites ; « l’école ou l’hôpital » retiré (non sourcé) ; le 0,8 n’est plus attribué à l’OFCE (sa fourchette publiée est de 0,7 à 0,8) ; HCFP ajouté comme seconde lecture sur le multiplicateur ; pensions déplacées dans « Les limites » ; « Par agent » corrigé (ce sont des parts de l’emploi total).
- Choix faits : fourchette de 2,5 à 25,3 Md€ = plus bas et plus haut des quatre variantes (calcul de la plateforme, illustratif) ; les bornes basses supposent qu’une partie du gain revient aux agents. Part du déficit calculée sur 151,6 Md€. Pas de chiffrage des agences (0,54 Md€ du Sénat) dans le corps du texte : autre mesure. Les mesures sont nommées par programme, sans étiquette de camp.
-->

> # « Ne remplaçons pas tous les départs en retraite »
>
> **En bref.** Quatre programmes proposent de ne pas remplacer une partie des agents publics qui partent. Selon le calcul de la plateforme (illustratif), la mesure rapporterait de 2,5 à 25,3 milliards d’euros par an [[prop:rn_posts_not_filled]] [[prop:lr_non_replacement_400k]]. C’est de 1,6 à 16,7 % du déficit public [[calc:2,5 / deficit_2025_eur_bn * 100 = 1,6]] [[calc:25,3 / deficit_2025_eur_bn * 100 = 16,7]].
>
> ## Ce qui est vrai
>
> La masse salariale publique brute atteint 362,1 milliards d’euros en 2024 [[fig:wage_bill_gross_2024_eur_bn]]. C’est 21,7 % de la dépense publique [[fig:wage_bill_gross_2024_pct_te]]. Un poste non remplacé réduit donc bien une dépense, année après année.
>
> Un départ à la retraite n’est pas un licenciement : ne pas remplacer l’agent n’entraîne pas d’indemnité de départ.
>
> ## Combien
>
> Les quatre programmes visent des nombres de postes très différents. Le montant le plus haut est celui des Républicains, le plus bas celui du Rassemblement national.
>
> - Les Républicains : de 12,6 à 25,3 milliards d’euros par an à l’horizon 2032 [[prop:lr_non_replacement_400k]].
> - Horizons : de 7,9 à 15,8 milliards [[prop:horizons_replace_2_of_3]].
> - Renaissance : de 3,2 à 6,3 milliards [[prop:re_100k_posts]].
> - Rassemblement national : de 2,5 à 12,7 milliards [[prop:rn_posts_not_filled]].
>
> Rapportée au déficit de 2025, notifié à Eurostat (151,6 milliards d’euros [[fig:deficit_2025_eur_bn]]), la fourchette représente de 1,6 à 16,7 % du déficit [[calc:2,5 / deficit_2025_eur_bn * 100 = 1,6]] [[calc:25,3 / deficit_2025_eur_bn * 100 = 16,7]]. Ce sont des variantes de la même mesure : elles ne s’additionnent pas.
>
> ## Les limites
>
> Le haut de chaque fourchette suppose que tout le gain reste dans le budget. Le bas suppose qu’une partie revient aux agents restants, en primes ou en salaires. C’était la règle de la révision générale des politiques publiques (RGPP), à partir de 2008 [[src:f11:S36]].
>
> Pour le Rassemblement national, le bas retient la part rendue réellement en 2009, plus forte que la règle [[prop:rn_posts_not_filled|contexte]] [[src:f11:S36]].
>
> Le montant n’est atteint qu’à pleine montée en charge, vers 2032 pour la plupart des plans. Il faut aussi choisir où supprimer : un plan qui épargne des ministères concentre les baisses sur les autres.
>
> Le plan de Renaissance passe aussi par des départs volontaires. Ceux-là coûtent des indemnités ponctuelles, non déduites ici [[prop:re_100k_posts|contexte]].
>
> La mesure ne réduit pas les pensions : les agents partis touchent leur retraite. Enfin, une baisse de la dépense réduit l’activité. La plateforme retient un multiplicateur de 0,8 la première année [[fig:multiplier_operating_spending_y1]] : le déficit baisse donc moins que la dépense.
>
> ## Qui dit quoi
>
> - **Les Républicains** annoncent 25 milliards d’euros d’économies [[prop:lr_non_replacement_400k]] (Public Sénat, 12 octobre 2026) [[src:f11:S8]]. L’article ne donne ni l’horizon, ni les indemnités, ni un calcul net. La plateforme lit ce montant comme un niveau annuel en fin de mandat.
> - **Renaissance** annonce 7 milliards d’euros par an sur les postes de l’État, hors Éducation, Armées, Justice et Intérieur [[prop:re_100k_posts]] (presse, 3 juillet 2026) [[src:f11:S39]].
> - **Horizons** et le **Rassemblement national** n’ont pas chiffré cette mesure. Les montants ci-dessus sont ceux de la plateforme [[prop:horizons_replace_2_of_3|contexte]] [[prop:rn_posts_not_filled|contexte]].
> - **La Cour des comptes (juridiction financière)** demande au minimum environ 20 milliards d’euros d’économies sur la masse salariale d’ici 2032 [[fig:cour_wage_bill_minimum_2032_eur_bn]]. Elle ne se limite pas au non-remplacement.
> - **L’Observatoire français des conjonctures économiques (OFCE ; Sciences Po, sensibilité keynésienne)** juge que l’effet sur l’activité varie selon la mesure. Pour les économies structurelles, sa fourchette inclut la valeur de 0,8 retenue par la plateforme [[fig:multiplier_operating_spending_y1]] [[src:f17:S8]].
> - **Le Haut Conseil des finances publiques (HCFP ; organisme indépendant placé auprès de la Cour des comptes)** va plus loin. Pour lui, l’effet des baisses de demande publique est plus fort [[src:f17:S1]].
>
> ## Et ailleurs ?
>
> En 2025, la rémunération des agents publics, cotisations des employeurs comprises, représente 12,4 % du produit intérieur brut (PIB) en France [[fig:compensation_employees_2025_pct_gdp]]. Elle en représente 10,0 % dans la zone euro [[fig:ea21_compensation_employees_2025_pct_gdp]]. L’écart est de 2,4 points [[calc:compensation_employees_2025_pct_gdp - ea21_compensation_employees_2025_pct_gdp = 2,4]].
>
> Pour le nombre d’agents, tout dépend du périmètre. La fonction publique française pèse 19,8 % de l’emploi total en 2024 [[fig:civil_service_share_employment_2024_pct]]. Avec la définition de l’Organisation de coopération et de développement économiques (OCDE), l’emploi public pèse 20,7 % en 2023 [[fig:gg_employment_share_oecd_pct]].
