<!-- page
slug: sante-soins-inutiles
phrase: Traquons les soins inutiles
sujets: sante, deficit-dette
montant: low_value_care_eur_bn
levier: S6
debats: 6.7, 8.11
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/conception/04-sujets-et-objections.md (lignes `sante-soins-inutiles`, `sante-gestion`, page 14), fr/site/debats.md 6.7 et 8.11, research/12-health-hospital-outcomes-international.md (points 1, 4 et conclusion), platform/data/figures.json, simulator-levers.json (S6), sources.json (f12). Lecture du 31 octobre 2026.
- Données manquantes (aucun id dans platform/data, donc omis du texte affiché) :
  - Cour des comptes, avril 2026 : plus de 11 Md€ par an de dommages évitables ;
  - Fipeco (François Ecalle), 30 janvier 2024 : frais de gestion de 7,8 Md€ pour les complémentaires contre 6,7 Md€ pour l’Assurance maladie obligatoire (2022) ;
  - Fondation iFRAP (Iphigénie Betolaud), 7 juin 2026 : 16,9 Md€ de frais de gestion en 2024, 0,57 % du PIB contre 0,3 % aux Pays-Bas, économie possible de 7,6 Md€ ;
  - Drees : les complémentaires portent 52 % des frais de gestion de santé (17,6 Md€ en 2025) ;
  - frais de gestion en part du PIB pour l’UE-27 et le panel (0,36 % pour l’UE-27 dans le fichier 12), rang de la France sur les frais de gestion (1er sur 27) ;
  - rang de la France en dépense de santé en % du PIB (4e sur 27 en COFOG, seulement dans les notes de la fiche) ;
  - rang après la mesure : sans objet, aucune mesure précise ne permet de récupérer ces réservoirs.
- Choix faits : la page traite ensemble les soins de faible valeur (22 Md€) et l’écart de frais de gestion (6 Md€), deux « réservoirs, pas des économies garanties » ; les deux montants ne sont pas additionnés. Les chiffres de l’iFRAP et de Fipeco ne sont pas affichés faute d’identifiant ; leurs positions sont décrites sans nombre. Aucun texte ouvert ne conteste les montants ; la page l’écrit. Unité de complément : % du PIB, une seule fois, dans « Et ailleurs ? ».
- Vérification du 31 octobre 2026 : retiré le doublon % du PIB de « Combien » ; « Aucune source ouverte ne le donne » remplacé (l’iFRAP donne une estimation, imparfaite selon elle) ; définition du réservoir alignée sur le glossaire (« en entier ni à coup sûr ») ; « Aucun texte publié ne dit » ramené à « n’a été trouvé » (Débats 8.11) ; noms des auteurs et titres ajoutés dans « Qui dit quoi » ; « plus que ses voisins » remplacé par la moyenne de l’UE-27 (la France est 4e, pas 1re) ; « Les résultats sont bons » retiré (jugement) ; écart avec la zone euro donné dans les deux définitions (1,06 et 1,5 point), comme le prévoit le fichier 00 ; justification non sourcée « une réforme de la gestion peut modifier les soins prescrits » retirée.
-->

> # « Traquons les soins inutiles »
>
> **En bref.** Une partie des soins coûte cher sans bénéfice clair pour le patient. La Cour des comptes (juridiction financière) l’estime à environ 22 milliards d’euros par an [[fig:low_value_care_eur_bn]], soit 14,5 % du déficit [[calc:low_value_care_eur_bn / deficit_2025_eur_bn * 100 = 14,5]]. C’est un réservoir, pas une économie garantie.
>
> ## Ce qui est vrai
>
> Des soins inutiles ou de faible valeur existent. La Cour des comptes les chiffre à 22 milliards d’euros par an [[fig:low_value_care_eur_bn]]. Elle le fait dans un rapport d’avril 2026 sur la qualité des soins à l’hôpital et en clinique.
>
> Les dépenses publiques de santé atteignent 261 milliards d’euros en 2024 [[fig:cofog_health_2024_eur_bn]], soit 15,6 % de la dépense publique [[fig:cofog_health_2024_pct_te]].
>
> Un second réservoir existe : les frais de gestion. Deux assurances se superposent, l’Assurance maladie et les complémentaires santé. Les frais de gestion dépassent d’environ 6 milliards d’euros par an la moyenne de l’Union européenne (UE) [[fig:health_admin_gap_eur_bn]].
>
> ## Combien
>
> Le premier réservoir vaut environ 22 milliards d’euros par an [[fig:low_value_care_eur_bn]]. Rapporté au déficit 2025 notifié à Eurostat, de 151,6 milliards d’euros [[fig:deficit_2025_eur_bn]], cela fait 14,5 % du déficit [[calc:low_value_care_eur_bn / deficit_2025_eur_bn * 100 = 14,5]].
>
> Le second réservoir vaut environ 6 milliards d’euros par an [[fig:health_admin_gap_eur_bn]], soit 4,0 % du déficit [[calc:health_admin_gap_eur_bn / deficit_2025_eur_bn * 100 = 4,0]].
>
> Ces deux montants sont des plafonds de ce que l’on pourrait viser. Ils ne disent pas ce qu’une réforme rapporterait.
>
> ## Les limites
>
> Les 22 milliards d’euros ne sont pas un montant contrôlé [[fig:low_value_care_eur_bn|contexte]]. Ils viennent d’une extrapolation à partir de ratios de l’Organisation de coopération et de développement économiques (OCDE). Aucune mesure précise ne permet de les récupérer en entier ni à coup sûr.
>
> Récupérer une partie de ce réservoir prendrait plusieurs années, avec un résultat incertain. Il s’agit de changer des pratiques médicales, pas de couper une ligne de budget. Le simulateur du site ne lui donne donc aucun rendement chiffré : il l’exclut des totaux.
>
> Pour les frais de gestion, l’économie dépend de la réforme choisie. La seule estimation publiée trouvée compare la France aux Pays-Bas ; son auteure la juge elle-même imparfaite. Enfin, les deux réservoirs viennent de méthodes différentes : la page ne les additionne pas.
>
> ## Qui dit quoi
>
> - **Cour des comptes (juridiction financière)**, avril 2026 : les soins inutiles ou de faible valeur coûtent 22 milliards d’euros par an [[fig:low_value_care_eur_bn]]. Elle le dit « sur la base d’extrapolations fondées sur des données de l’OCDE ».
> - **François Ecalle (Fipeco ; site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire)**, 30 janvier 2024. Selon lui, les complémentaires créent une « duplication des frais de gestion ».
> - **Iphigénie Betolaud (Fondation iFRAP, libérale)**, 7 juin 2026 : elle compare la France aux Pays-Bas et estime qu’une économie sur les frais de gestion est possible. Elle reconnaît elle-même que la comparaison est imparfaite.
>
> Nous n’avons trouvé aucun texte qui conteste ces montants. Une autre lecture est possible : ces dépenses seraient des coûts de qualité, et les réduire demanderait d’abord des investissements. Elle n’a pas été trouvée dans un texte publié.
>
> ## Et ailleurs ?
>
> La dépense publique de santé atteint 8,9 % du produit intérieur brut (PIB) en France [[fig:cofog_health_2024_pct_gdp]], contre 7,3 % dans l’Union européenne à 27 (UE-27) [[fig:eu_cofog_health_2024_pct_gdp_eu27]]. Avec la zone euro, l’écart va de 1,06 point de PIB [[fig:gap2024_health_sha_pp]] à 1,5 point [[fig:gap2024_health_pp]], selon la définition retenue.
>
> Pour l’espérance de vie, la France atteint 83,0 ans [[fig:life_expectancy_2024_years]], contre 81,5 ans dans l’UE-27 [[fig:eu27_life_expectancy_2024_years]]. Elle est 7e sur 27 [[fig:life_expectancy_2024_rank]].
>
> Nous n’avons trouvé aucune comparaison des soins inutiles entre pays dans les données de la plateforme.
