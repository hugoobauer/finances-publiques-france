<!-- page
slug: taxer-riches
phrase: Il suffit de faire payer les plus riches
sujets: impots, retraites, deficit-dette
montant: tax_rich_package_eur_bn
levier: R1, R2, R3, R4, R5
debats: 3.7, 3.8, 3.9, 3.10, 3.11, 3.12, 3.13, 3.14, 2.8
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/site/debats.md 3.7 à 3.14 (positions, auteurs, liens) ; fr/conception/04-sujets-et-objections.md (lignes de la page) ; prototypes/retraites.html (#taxer-riches) ; figures.json (tax_rich_package_eur_bn, zucman_*, cdhr_*, isf_repeal_mechanical_loss_eur_bn, ipp_*, geerolf_*, oecd_tax_*), proposals.json (zucman_tax, cdhr), sources.json (f07:S4). Consultés le 31 octobre 2026.
- Données manquantes : (1) rendement de la taxe Zucman après imputation de l’impôt sur les sociétés (Sénat, « 2 à 3 »), lisible seulement dans proposals.json zucman_tax ; (2) rendements chiffrés de la suppression du PFU (3,2 à 9) et de la réforme des successions (9 à 20) : ids seulement dans proposals.json, non repris ici faute de chiffrage indépendant du dispositif exact ; (3) aucun rang « après la mesure » pour le taux de prélèvement dans figures.json : calculé ici par [[calc:]] à partir du PIB 2025 et du taux OCDE 2024 (années différentes, approximation) ; (4) Débats 2.8 (âge de départ, choix de société) : aucun chiffre repris ; le lien avec les retraites est dit en une phrase (« Les limites » : le même argent ne sert qu’une fois) ; (5) Terra Nova, ensemble de cinq mesures à 10 à 15 Md€ (Débats 3.14) : aucun id dans figures.json ni proposals.json, chiffre omis du texte affiché ; (6) départs de contribuables mesurés par le CAE (+0,04 à 0,09 point de taux de départ après 2013) : pas d’id, dit sans chiffre ; (7) CDHR : la valeur 0,4 est un premier acompte (décembre 2025, « moins de 0,4 ») ; la prévision 2026 (0,65 à 0,7) n’a pas d’id propre.
- Vérification (relecture contradictoire, 31 octobre 2026) : « 0,1 % des foyers » et non « de la population » ; taux IPP « en part du revenu économique » ; recettes fiscales totales OCDE au lieu de « taux de prélèvement » (glossaire, ligne tax-to-GDP) ; fourchette 2 à 6 attribuée à F. Geerolf (Débats 3.8) ; PPL n° 768 attribuée à ses autrices et à G. Zucman ; arguments contraires au Sénat et constat du CAE sur l’exil ajoutés pour l’équilibre.
- Choix faits : fourchette de la plateforme (10 à 25) en montant principal ; l’écart des estimations Zucman (2 à 6 contre 15 à 25) est donné dans « Qui dit quoi » ; unité de complément : points de taux de prélèvement. Sous-pages (Zucman, ISF-IFI, flat tax, successions, CDHR) à écrire ensuite.
-->

> # « Il suffit de faire payer les plus riches »
>
> **En bref.** Selon notre synthèse, de nouveaux impôts sur les plus aisés rapporteraient de 10 à 25 milliards d’euros par an, après réactions des contribuables [[fig:tax_rich_package_eur_bn]]. C’est de 6,6 % à 16,5 % du déficit [[calc:tax_rich_package_eur_bn / deficit_2025_eur_bn × 100 = 6,6 à 16,5]].
>
> ## Ce qui est vrai
>
> De tels impôts rapporteraient bien de l’argent. Et, au tout sommet, le taux d’impôt baisse. Selon l’IPP (Institut des politiques publiques ; institut de recherche académique), les foyers de milliardaires paient 26 % de leur revenu en impôts [[fig:ipp_effective_rate_billionaires_2016_pct]]. Les 0,1 % des foyers les plus aisés en paient 46 % [[fig:ipp_effective_rate_top01_2016_pct]] (données 2016).
>
> Ce revenu compte les bénéfices gardés dans les sociétés qui détiennent leurs entreprises (holdings). Ces bénéfices ne paient que l’impôt sur les sociétés.
>
> Cette mesure est discutée. François Geerolf, économiste à l’Observatoire français des conjonctures économiques (OFCE ; Sciences Po, sensibilité keynésienne), qui écrit à titre personnel, refait le calcul à base comparable. Il trouve 25,1 % pour les milliardaires [[fig:geerolf_rate_billionaires_homogeneous_pct]], contre 26,8 % au seuil des 10 % les plus aisés [[fig:geerolf_rate_top10_threshold_pct]]. Pour lui, l’écart existe, mais il est faible.
>
> ## Combien
>
> Notre synthèse, après réactions des contribuables, donne **de 10 à 25 milliards d’euros par an** [[fig:tax_rich_package_eur_bn]]. Elle additionne un impôt sur les très gros patrimoines, une taxation des revenus du capital et une réforme des successions. Nous n’avons trouvé aucun organisme qui chiffre cet ensemble exact.
>
> Le déficit de 2025, notifié à Eurostat, est de 151,6 milliards d’euros [[fig:deficit_2025_eur_bn]]. Le paquet couvrirait **de 6,6 % à 16,5 % du déficit** [[calc:tax_rich_package_eur_bn / deficit_2025_eur_bn × 100 = 6,6 à 16,5]].
>
> ## Les limites
>
> C’est une estimation, pas une recette garantie. Elle dépend des départs, de l’optimisation et du Conseil constitutionnel. Pour la taxe Zucman, le rapporteur du Sénat juge le texte « probablement inconstitutionnel » ; la rapporteure minoritaire avance des arguments contraires.
>
> Sur les départs, le Conseil d’analyse économique (CAE ; instance d’économistes placée auprès du Premier ministre) les juge faibles après la réforme fiscale de 2013.
>
> La contribution différentielle sur les hauts revenus (CDHR) montre le risque. Elle était annoncée à 2 milliards d’euros [[fig:cdhr_announced_eur_bn]]. Son premier acompte, en décembre 2025, a rapporté moins de 0,4 milliard [[fig:cdhr_observed_2025_eur_bn]]. Elle taxe le revenu, pas le patrimoine : elle ne prouve pas qu’une taxe sur le patrimoine échouerait.
>
> Les composantes ne s’additionnent pas toujours. Rétablir l’impôt de solidarité sur la fortune (ISF) recoupe la base de la taxe Zucman. La composante « successions » n’a pas de chiffrage indépendant.
>
> Comme toute hausse d’impôt, ces mesures freineraient un peu l’activité. Selon l’OFCE, cet effet est faible à court terme pour les impôts sur le capital [[src:f17:S8]].
>
> Le même argent ne sert qu’une fois. S’il finance les retraites, il ne réduit pas le déficit.
>
> Enfin, taxer davantage les plus aisés est une question de justice fiscale, donc de valeurs. Les chiffres disent seulement ce que cela rapporterait.
>
> ## Qui dit quoi
>
> Pour la taxe Zucman, les estimations divergent fortement.
>
> - **Proposition de loi n° 768 de députées écologistes, 7 janvier 2025** : de 15 à 25 milliards d’euros, soit environ 20 [[fig:zucman_proponents_eur_bn]]. Ce chiffre de Gabriel Zucman (économiste, directeur de l’Observatoire européen de la fiscalité) est statique, avant réactions des contribuables.
> - **François Geerolf, octobre 2026** : « les 20 milliards d’euros promis en valent plutôt 2 à 6 » [[fig:zucman_critics_eur_bn]].
> - **Patrick Andrews, étude commandée par le collectif de chefs d’entreprise « Trop, c’est trop ! », juin 2026** : environ 5,5 milliards d’euros [[fig:zucman_andrews_central_eur_bn]].
>
> Sur l’ensemble des impôts visant les plus aisés :
>
> - **Terra Nova (centre gauche), 20 septembre 2024** : cinq mesures rapporteraient une somme réelle, bien inférieure à l’effort nécessaire pour stabiliser la dette [[src:f07]].
> - **Fondation iFRAP (libérale), septembre 2025** : les milliards tirés des plus riches sont un « mirage », car ces foyers paient déjà des taux élevés [[src:f05]].
>
> Le CAE cite une perte de 3 à 4,5 milliards d’euros par an, due au remplacement de l’ISF par l’impôt sur la fortune immobilière [[fig:isf_repeal_mechanical_loss_eur_bn]]. C’est un effet mécanique, avant réactions des contribuables. Ce coût passé n’est pas le rendement d’un ISF rétabli.
>
> ## Et ailleurs ?
>
> Prenons les recettes fiscales totales, au sens de l’Organisation de coopération et de développement économiques (OCDE). La France est 2e des 36 pays dont le chiffre 2024 est publié [[fig:oecd_tax_to_gdp_2024_rank]]. Elles atteignent 43,5 % du produit intérieur brut (PIB) en 2024 [[fig:oecd_tax_to_gdp_2024_pct_gdp]]. La moyenne de l’OCDE est de 34,1 % [[fig:oecd_avg_tax_to_gdp_2024_pct_gdp]]. Le Danemark est premier, à 45,2 % [[fig:denmark_tax_to_gdp_2024_pct_gdp]].
>
> Avec le paquet, ce taux serait de 43,8 % à 44,3 % du PIB [[calc:oecd_tax_to_gdp_2024_pct_gdp + tax_rich_package_eur_bn / gdp_2025_eur_bn × 100 = 43,8 à 44,3]]. C’est un calcul approché, avec le PIB de 2025, si les autres pays ne changeaient rien. Même après cette mesure, la France resterait 2e sur 36 [[fig:oecd_tax_to_gdp_2024_rank]].
