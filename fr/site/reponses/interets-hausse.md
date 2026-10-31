<!-- page
slug: interets-hausse
phrase: Les intérêts de la dette vont fortement grimper
sujets: interets, deficit-dette
montant: interest_rise_2025_2027_eur_bn
levier: G2
debats: 5.6, 5.7, 5.8
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/conception/04-sujets-et-objections.md (lignes 258 et 424), fr/site/debats.md points 5.6, 5.7, 5.8 (positions de la Cour des comptes du 25 juin 2026, de la mission Jaravel-Ragot-Tavernier-Valla de juillet 2026, de l’OFCE du 26 février 2026) ; platform/data/figures.json, yardsticks.json, sources.json, simulator-levers.json (G2 = « Choc de taux d’intérêt ») ; research/09-international-comparison-tables.md (lignes 184-186, 270-272) pour vérifier ce qui manque.
- Données manquantes :
  - Intérêts en % du PIB, UE-27, zone euro, OCDE et panel (DE, IT, ES, NL, BE, SE, DK) : le tableau existe dans research/09 (COFOG GF0107, 2024 : France 2,0 ; UE-27 1,9 ; ZE21 1,9 ; rang 9 sur 27) mais figures.json n’a aucun identifiant correspondant (seul cofog_interest_2024_pct_te, France). La section « Et ailleurs ? » utilise donc la dette (debt_eu_rank_2025, ea21_debt_2025_pct_gdp). À verser : intérêts 2024 UE-27, ZE21, rang, panel.
  - Rang de la France après la mesure : sans objet (la hausse des intérêts n’est pas une mesure).
  - Prévision de la Cour des comptes pour 2026 (environ 77 Md€, cité dans debats.md 5.6) : sans identifiant, donc remplacée par « un peu moins » ; à verser si l’on veut l’afficher.
  - Hausse de plus de 9 % en 2025 (Cour des comptes) : sans identifiant, omise.
  - Économies nécessaires pour stabiliser la dette selon Terra Nova (environ 100 Md€) et l’Institut Montaigne (140 Md€ d’ici 2029) : sans identifiant, non affichées.
- Choix faits :
  - Périmètre retenu : administrations publiques (65,7 Md€ en 2025, base de l’étalon de 25,3). La charge de la dette de l’État (51,6) est expliquée en une phrase, avec l’écart de 14,1.
  - Montant en Md€ par an et part du déficit de référence (151,6 Md€). Unité de complément : euros par mois et par ménage non utilisée ; pourcentage des recettes utilisé une fois (4,2 %).
  - Qui dit quoi : trois lectures (Cour des comptes, mission de l’IGF, OFCE). Aucun montant de la Cour ou de la mission n’est écrit sans identifiant ; leurs positions sont citées sans chiffre.
  - Le levier G2 (choc de taux) n’est pas décrit dans le texte : le site génère le bouton. Les chocs de 100 points de base (3,4 puis 8,1 Md€) viennent de HCFP-2026-5 §116 ; ce sont des estimations du gouvernement, attribuées comme telles, années 2027 et 2028.
  - Qui dit quoi complété (vérification) : écart de 89,6 Md€ au solde stabilisant la dette en 2025 (Cour, debt_stabilizing_gap_2025_eur_bn) et ajustement d’environ 125 Md€ d’ici 2032 (mission IGF, igf_adjustment_2032_eur_bn), pour appuyer « ce n’est pas l’effort nécessaire » (débat 5.8). Terra Nova (environ 100 Md€) et l’Institut Montaigne (140 Md€ d’ici 2029), cités au point 5.8, n’ont pas d’identifiant : non affichés.
  - Titre : la phrase de 04-sujets-et-objections.md (« … grimper de 25 milliards en deux ans ») a été remplacée par « … vont fortement grimper », car le validateur refuse un chiffre sans pastille dans le titre. À trancher : remettre le montant avec pastille si le format le permet, ou aligner la ligne de 04.
  - Aucun texte d’économiste ou d’institut sur ces montants n’a été ouvert (débat 5.6) ; la page le dit au lieu d’affirmer que personne ne conteste l’ordre de grandeur.
-->

> # « Les intérêts de la dette vont fortement grimper »
>
> **En bref.** Selon les prévisions du gouvernement, la charge d’intérêts des administrations publiques augmenterait de 25,3 milliards d’euros entre 2025 et 2027 [[yard:interest_rise_2025_2027_eur_bn]]. Cela représente 16,7 % du déficit de 2025 [[calc:interest_rise_2025_2027_eur_bn / deficit_2025_eur_bn * 100 = 16,7]].
>
> ## Ce qui est vrai
>
> La hausse figure dans les prévisions officielles du gouvernement. En 2025, la France a payé 65,7 milliards d’euros d’intérêts [[fig:interest_2025_eur_bn]], soit 2,2 % du produit intérieur brut (PIB) [[fig:interest_2025_pct_gdp]].
>
> Le gouvernement prévoit 79,2 milliards d’euros en 2026 [[fig:interest_2026f_eur_bn]], puis environ 91 milliards d’euros en 2027 [[fig:interest_2027f_eur_bn]]. La différence entre 2027 et 2025 donne 25,3 milliards d’euros [[yard:interest_rise_2025_2027_eur_bn]].
>
> En 2025, ces intérêts représentaient 4,2 % des recettes publiques [[yard:interest_to_revenue_pct]].
>
> ## Combien
>
> En 2027, les administrations publiques paieraient 25,3 milliards d’euros d’intérêts de plus qu’en 2025, sur l’année [[yard:interest_rise_2025_2027_eur_bn]]. C’est l’écart entre deux années, pas un total cumulé sur deux ans.
>
> Le déficit public de 2025, notifié à Eurostat, est de 151,6 milliards d’euros [[fig:deficit_2025_eur_bn]]. La hausse en représente donc 16,7 % [[calc:interest_rise_2025_2027_eur_bn / deficit_2025_eur_bn * 100 = 16,7]].
>
> Cette page utilise une seule mesure, celle des administrations publiques : État, collectivités locales et administrations de sécurité sociale.
>
> ## Les limites
>
> Les montants de 2026 et 2027 sont des prévisions du gouvernement. Ils dépendent des taux auxquels les administrations publiques empruntent. Selon le gouvernement, une hausse de 1 point de tous les taux coûterait 3,4 milliards d’euros la première année, en 2027 [[fig:interest_shock_100bp_y1_eur_bn]]. Elle coûterait 8,1 milliards d’euros la deuxième année, en 2028 [[fig:interest_shock_100bp_y2_eur_bn]].
>
> Le périmètre compte aussi. Dans le budget de l’État seul, la charge de la dette était de 51,6 milliards d’euros en 2025 [[fig:state_debt_charge_2025_eur_bn]]. L’écart avec les 65,7 milliards d’euros est de 14,1 milliards d’euros [[yard:interest_concepts_gap_2025_eur_bn]]. Il vient des autres administrations et de la façon de compter.
>
> Enfin, la hausse de 25,3 milliards d’euros [[yard:interest_rise_2025_2027_eur_bn]] est un repère de taille. Ce n’est pas l’effort nécessaire pour stabiliser la dette.
>
> ## Qui dit quoi
>
> - **Cour des comptes (juridiction financière)**, 25 juin 2026. La hausse des intérêts de 2026 efface la plus grande partie de l’effort de réduction du déficit prévu cette année-là. Pour 2026, la Cour prévoyait un peu moins d’intérêts que le gouvernement [[src:f11:S28]]. En 2025, le déficit dépassait de 89,6 milliards d’euros celui qui aurait stabilisé la dette [[fig:debt_stabilizing_gap_2025_eur_bn]].
> - **Mission sur la transparence des finances publiques (Jaravel, Ragot, Tavernier, Valla)**, juillet 2026. Elle est hébergée par l’Inspection générale des finances (IGF ; corps d’inspection du ministère de l’Économie). À politique inchangée, la charge d’intérêts monte fortement jusqu’en 2030 [[src:f11:S29]]. Pour stabiliser durablement la dette, la mission chiffre l’ajustement à environ 125 milliards d’euros d’ici 2032 [[fig:igf_adjustment_2032_eur_bn]].
> - **OFCE (Observatoire français des conjonctures économiques ; Sciences Po, sensibilité keynésienne)**, 26 février 2026 : les intérêts ont un multiplicateur nul ou très faible. Les payer soutient très peu l’activité [[src:f17:S8]].
>
> Nous n’avons pas trouvé de texte d’économiste ou d’institut qui discute ces montants.
>
> ## Et ailleurs ?
>
> Nous n’avons pas de chiffre vérifié sur les intérêts des autres pays. Voici ce que nous avons sur la dette et sur les taux, dont dépendent les intérêts.
>
> Fin 2025, la dette française atteignait 115,7 % du PIB [[fig:debt_2025_pct_gdp]], contre 87,3 % pour la zone euro à 21 pays [[fig:ea21_debt_2025_pct_gdp]]. Dans l’Union européenne, la France avait le 3e taux d’endettement le plus élevé sur 27 [[fig:debt_eu_rank_2025]].
>
> En septembre 2026, l’écart de taux à 10 ans avec l’Allemagne était de 97 points de base [[fig:oat_bund_spread_sep2026_bp]]. Un point de base vaut un centième de point de pourcentage.
