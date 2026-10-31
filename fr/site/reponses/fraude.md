<!-- page
slug: fraude
phrase: Luttons d’abord contre la fraude sociale
sujets: chomage-minima, impots, deficit-dette
montant: antifraud_marginal_yield_eur_bn
levier: R12
debats: 8.4, 8.5, 8.6
- 31 octobre 2026 : répartition de juillet 2024 (cotisations, prestations) retirée du texte affiché, comme au point 8.5 de la page « Débats ».
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/conception/04-sujets-et-objections.md (ligne `fraude`), fr/site/debats.md 8.4 à 8.6, platform/data/figures.json, proposals.json, simulator-levers.json (R12), sources.json (f07:S3, f07:S10, f11:S28), fr/site/chapitres/02 et 03 (cadrage des pertes estimées). Lecture du 31 octobre 2026.
- Données manquantes (aucun id dans platform/data, donc omis du texte affiché) :
  - Fondation iFRAP, 15 janvier 2026 (mise à jour 9 avril 2026) : 17,5 Md€ avec erreurs de paiement, 2,06 Md€ détectés, environ 1,2 Md€ recouvrés ou évités, 3 à 4 Md€ récupérables ;
  - rapport n° 3072 de l’Assemblée nationale (rapporteur M. Feld, 21 juillet 2026) : écart fiscal de 80 à 100 Md€ avancé par les syndicats de la DGFiP ; dix agents de contrôle pour environ 100 M€ par an de droits rappelés ;
  - Cour des comptes, 16 décembre 2025 : 1 268 Md€ de prélèvements obligatoires ; résultats du contrôle de 16,1 à 17,4 Md€ entre 2015 et 2024 ; 12,2 Md€ recouvrés en 2015 ;
  - estimation de 3,5 Md€ du Rassemblement national jugée « pas crédible » (presse, via le HCFP) ;
  - comparaisons internationales de la fraude (UE-27, zone euro, OCDE, panel) et rang après la mesure : aucun id dans figures.json.
- Choix faits : la page sépare trois choses (pertes estimées sociales, fourchette d’incertitude fiscale, rendement réaliste d’un nouveau plan). Les 14 et 30 à 130 ne sont jamais additionnés ni présentés comme un montant récupérable. Fourchette retenue : 1 à 3 Md€ (synthèse de la plateforme, aucun texte ouvert ne la donne). Les trois montants annoncés par des partis (LFI, RN, LR) ne sont pas repris, pour tenir la page courte. Unité de complément : aucune. Vérification (31 octobre 2026) : les 7,25 et 5,73 sont la répartition de l’estimation de juillet 2024 (12,98), pas des 14 de décembre 2025 ; ajout de `social_fraud_hcfips_2024_eur_bn`. Étiquette HCFiPS rétablie mot pour mot (glossaire §1.13). « Non crédible » (HCFP) n’est pas employé : le HCFP écrit « optimiste voire hypothétique ».
-->

> # « Luttons d’abord contre la fraude sociale »
>
> **En bref.** La fraude sociale existe et se chiffre en milliards d’euros. Mais ses pertes estimées ne sont pas un montant à récupérer. Un nouveau plan antifraude rapporterait, de façon réaliste, de 1 à 3 milliards d’euros par an [[fig:antifraud_marginal_yield_eur_bn]]. C’est de 0,7 à 2,0 % du déficit [[calc:antifraud_marginal_yield_eur_bn / deficit_2025_eur_bn * 100 = 0,7 ; 2,0]].
>
> ## Ce qui est vrai
>
> La fraude sociale est réelle. Le Haut Conseil du financement de la protection sociale (HCFiPS) est une instance de concertation sur le financement de la protection sociale. En décembre 2025, il l’estime à environ 14 milliards d’euros de pertes par an [[fig:social_fraud_hcfips_dec2025_eur_bn]]. C’est 9,2 % du déficit de référence [[calc:social_fraud_hcfips_dec2025_eur_bn / deficit_2025_eur_bn * 100 = 9,2]].
>
> Son estimation précédente, de juillet 2024, était de 12,98 milliards d’euros [[fig:social_fraud_hcfips_2024_eur_bn]].
>
> La fraude fiscale existe aussi. Mais la Cour des comptes (juridiction financière) juge qu’on ne peut pas la chiffrer. Personne ne peut dire si elle est plus proche de 30 ou de 130 milliards d’euros par an [[fig:tax_gap_cour_range_eur_bn]].
>
> ## Combien
>
> Deux choses sont à distinguer. Les pertes estimées disent l’ampleur de la fraude. Le rendement d’un nouveau plan dit ce qui rentrerait en plus dans les caisses publiques. Le second est bien plus petit que le premier.
>
> Le rendement réaliste d’un nouveau plan, fiscal et social, va de 1 à 3 milliards d’euros par an [[fig:antifraud_marginal_yield_eur_bn]]. Rapporté au déficit 2025 notifié à Eurostat, de 151,6 milliards d’euros [[fig:deficit_2025_eur_bn]], cela représente de 0,7 à 2,0 % du déficit [[calc:antifraud_marginal_yield_eur_bn / deficit_2025_eur_bn * 100 = 0,7 ; 2,0]].
>
> Cette fourchette est une synthèse de la plateforme : aucun texte public ne donne ce chiffre.
>
> ## Les limites
>
> Les pertes estimées ne sont pas un montant récupérable. Le HCFiPS mesure ce qui échappe aux caisses, sur un périmètre incomplet. Une grande part de la fraude n’est jamais détectée.
>
> En 2024, le contrôle fiscal a notifié 20,1 milliards d’euros [[fig:tax_audit_assessed_2024_eur_bn]] et encaissé 11,4 milliards d’euros [[fig:tax_audit_collected_2024_eur_bn]]. Ces sommes encaissées sont déjà dans les recettes : un nouveau plan ne compte que ce qui s’y ajoute.
>
> Les rendements annoncés sont incertains. Le projet de budget 2026 affichait 1,5 milliard d’euros pour une mesure antifraude [[fig:antifraud_2026_announced_eur_bn]]. Cette mesure a ensuite disparu de la prévision. Le projet de budget 2027 en attend 1,0 milliard d’euros [[prop:antifraud_plan]].
>
> Enfin, la fraude sociale [[fig:social_fraud_hcfips_dec2025_eur_bn|contexte]] et la fraude fiscale [[fig:tax_gap_cour_range_eur_bn|contexte]] ne s’additionnent pas en un montant à récupérer. Ce sont des pertes estimées, pas des économies.
>
> ## Qui dit quoi
>
> - **Cour des comptes (juridiction financière), 16 décembre 2025** : aucune estimation robuste de la fraude fiscale n’existe [[fig:tax_gap_cour_range_eur_bn|contexte]]. Les vieilles estimations « créent l’espérance d’une manne potentielle » [[src:f07:S10]].
> - **Haut Conseil des finances publiques (HCFP ; organisme indépendant placé auprès de la Cour des comptes), 25 septembre 2026** : la mesure de 2026 a disparu [[fig:antifraud_2026_announced_eur_bn|contexte]]. Son rendement était « optimiste voire hypothétique » [[src:f07:S3]].
> - **Fondation iFRAP (libérale), 15 janvier 2026** : elle retient une estimation étroite proche de celle du HCFiPS, plus élevée avec les erreurs de paiement. Elle juge qu’on pourrait récupérer davantage qu’aujourd’hui.
> - **Commission des finances de l’Assemblée nationale (rapport d’information, rapporteur M. Feld), 21 juillet 2026** : elle juge le contrôle fiscal très rentable. Elle juge que la baisse de ses moyens a été une erreur budgétaire.
>
> ## Et ailleurs ?
>
> Nous n’avons trouvé aucune comparaison internationale de la fraude dans les données de la plateforme. Pour la France, la Cour des comptes constate déjà qu’il n’existe pas d’estimation robuste.
