<!-- page
slug: revenir-a-3-pct
phrase: Revenons à 3 % de déficit tout de suite
sujets: deficit-dette, interets
montant: gross_measures_goal_b_eur_bn
levier: 
debats: 7.1, 7.2, 7.7
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/conception/04-sujets-et-objections.md (ligne revenir-a-3-pct, rang 11) ; fr/site/debats.md points 7.1, 7.2, 7.6, 7.7 (OFCE, HCFP, mission IGF, Cour des comptes, FMI, Fondation iFRAP, Fipeco, Institut Avant-Garde) ; figures.json, yardsticks.json, sources.json (consultés le 31 octobre 2026).
- Données manquantes :
  - Déficit des autres pays (UE-27, zone euro, OCDE, panel DE, IT, ES, NL, BE, SE, DK) : aucun identifiant dans figures.json. La comparaison de déficit est donc omise ; seule la comparaison de dette (zone euro, rang UE) est affichée.
  - Rang de la France après la mesure (déficit) : aucun identifiant ; omis.
  - FMI : effort recommandé d’environ 0,8 % du PIB par an de 2027 à 2029 (debats 7.7) : pas d’identifiant ; chiffre omis, position décrite sans nombre.
  - OFCE : ajustement de 2,8 % du PIB jusqu’en 2029 (debats 7.7) et multiplicateurs de 0,7 à 0,8 (debats 7.2) : pas d’identifiant ; omis (la plage figure seulement dans la pastille de multiplier_operating_spending_y1).
  - Institut Avant-Garde : fourchette de multiplicateur de 0,75 à 1 : pas d’identifiant ; omis.
  - HCFP : 0,5 point de croissance perdu pour 0,8 point de PIB d’effort : pas d’identifiant ; omis.
  - Sources sans identifiant dans sources.json (phrases laissées sans pastille [[src:]]) : OFCE, « Quelles trajectoires pour les finances publiques de la France ? », 11 juillet 2025 (f17:S8 est le Policy Brief n° 154 de février 2026, il ne couvre pas la trajectoire de 2025) ; Fondation iFRAP, « Croissance à 0,7 % en 2026 : la boule de neige de la dette est en route », juillet 2026. À verser dans sources.json.
- Choix faits :
  - Fourchette de 61,9 à 94 Md€ : 61,9 est l’écart statique (base 2025) ; 94 est le montant brut avec effet sur l’activité (multiplicateur 0,6, première année). Les deux sont des calculs de la plateforme, « illustratifs ». Part du déficit calculée sur le déficit 2025 notifié (151,6).
  - 125 Md€ (mission IGF) : ajustement cumulé d’ici 2032, par rapport à une politique inchangée, calculé avec un multiplicateur nul (debats 7.6) ; objectif différent (stabiliser la dette) ; cité comme tel, jamais additionné ni comparé à un montant annuel.
  - 2031 (mission IGF, debats 7.2) : année où le déficit passerait sous 3 % sans l’hypothèse d’un multiplicateur nul ; même rapport que f11:S29.
  - Pas de levier affiché dans l’en-tête : l’objectif B est un objectif du simulateur, pas une mesure ; le champ levier reste vide.
  - Titre : « 3 % » sans dénominateur ni pastille, car c’est la phrase entendue (même cas que tva-energie.md).
- Vérification (31 octobre 2026) : En bref ramené à deux phrases ; HCFP et IGF avec leur étiquette du §1.13 ; 125 Md€ situé « d’ici 2032 » et rattaché à son hypothèse de multiplicateur nul (la mission juge cette hypothèse « très favorable ») ; pastille f17:S8 retirée de la phrase sur la trajectoire OFCE de juillet 2025 ; « Ce qui est vrai » complété par l’argument d’un effort rapide ; phrase finale de « Qui dit quoi » limitée aux textes cités.
-->

> # « Revenons à 3 % de déficit tout de suite »
>
> **En bref.** Ramener le déficit public à 3 % du PIB (produit intérieur brut) [[yard:maastricht_deficit_limit_pct]] demande 61,9 milliards d’euros [[yard:gap_to_3pct_eur_bn]], soit 40,8 % du déficit de 2025 [[calc:gap_to_3pct_eur_bn / deficit_2025_eur_bn * 100 = 40,8]]. Avec l’effet des mesures sur l’activité, il en faut environ 94 milliards [[yard:gross_measures_goal_b_eur_bn]], soit 62,0 % du déficit [[calc:gross_measures_goal_b_eur_bn / deficit_2025_eur_bn * 100 = 62,0]].
>
> ## Ce qui est vrai
>
> La limite de 3 % du PIB est la valeur de référence du traité de Maastricht [[yard:maastricht_deficit_limit_pct]]. En 2025, le déficit public atteignait 5,1 % du PIB [[fig:deficit_2025_pct_gdp]], soit 151,6 milliards d’euros [[fig:deficit_2025_eur_bn]]. L’écart est donc réel.
>
> Plusieurs institutions recommandent aussi de concentrer l’effort sur les premières années (voir « Qui dit quoi »).
>
> ## Combien
>
> La plateforme calcule deux montants annuels, pour la première année.
>
> - **61,9 milliards** : l’écart entre le déficit de 2025 et la limite de 3 % du PIB [[yard:gap_to_3pct_eur_bn]]. C’est le montant si les mesures ne freinent pas l’économie.
> - **94 milliards** : les mesures brutes nécessaires, avec un multiplicateur budgétaire de 0,6 [[fig:multiplier_mixed_y1]]. Chaque euro de mesures réduit alors le déficit d’environ 0,66 euro [[yard:macro_feedback_factor_mixed]].
>
> Cela représente de 40,8 à 62,0 % du déficit de 2025 [[calc:gap_to_3pct_eur_bn / deficit_2025_eur_bn * 100 = 40,8 ; gross_measures_goal_b_eur_bn / deficit_2025_eur_bn * 100 = 62,0]]. Ce sont des calculs de la plateforme, donc illustratifs.
>
> ## Les limites
>
> Le multiplicateur n’est pas publié tel quel. La plateforme le déduit d’un avis du Haut Conseil des finances publiques (HCFP ; organisme indépendant placé auprès de la Cour des comptes). Il vaut pour des mesures mixtes. Il est plus élevé pour les baisses de dépenses de fonctionnement [[fig:multiplier_operating_spending_y1|contexte]]. Avec un multiplicateur plus élevé, il faudrait davantage de mesures.
>
> Appliquer une règle d’un an à un effort sur plusieurs années est une simplification. Ces 94 milliards [[yard:gross_measures_goal_b_eur_bn]] ne s’additionnent pas avec l’effort pour stabiliser la dette, qui est un autre objectif. Pour celui-ci, la Cour des comptes (juridiction financière) chiffre l’écart à 89,6 milliards d’euros en 2025 [[fig:debt_stabilizing_gap_2025_eur_bn]].
>
> ## Qui dit quoi
>
> - **OFCE (Observatoire français des conjonctures économiques ; Sciences Po, sensibilité keynésienne)** : en février 2026, il juge que les économies du budget 2026 freinent la croissance [[src:f17:S8]]. En juillet 2025, il a décrit une trajectoire plus progressive, avec un effort réparti jusqu’en 2029.
> - **Mission sur la transparence des finances publiques**, accueillie par l’Inspection générale des finances (IGF ; corps d’inspection du ministère de l’Économie), juillet 2026. Stabiliser la dette demande environ 125 milliards d’euros d’ici 2032 [[fig:igf_adjustment_2032_eur_bn]], si l’effort ne freine pas la croissance, une hypothèse « très favorable ». Sinon, le déficit passerait sous 3 % du PIB [[yard:maastricht_deficit_limit_pct]] en 2031. Elle conseille un effort concentré au début [[src:f11:S29]].
> - **FMI (Fonds monétaire international ; organisation internationale)** : en mai 2026, il recommande de concentrer l’effort au début et juge le rythme actuel insuffisant [[src:f06:imf_aiv2026]].
> - **Fondation iFRAP (libérale)** : en juillet 2026, elle juge un effort massif dès le départ plus efficace qu’un ajustement brutal imposé par les marchés.
> - **Cour des comptes (juridiction financière)** : en juin 2026, elle écrit qu’il vaut mieux concentrer l’effort quand les taux d’intérêt sont sous tension. Quand les multiplicateurs sont élevés, l’étaler limite la perte d’activité [[src:f11:S28]].
>
> Dans les textes cités, aucune source ne propose de revenir à 3 % du PIB [[yard:maastricht_deficit_limit_pct]] en une seule année : elles divergent sur le rythme.
>
> ## Et ailleurs ?
>
> Nous n’avons pas de chiffre de déficit comparable pour les autres pays de l’Union européenne (UE) ou de la zone euro. Nous n’en affichons donc pas.
>
> Sur la dette, la France est au 3e rang sur 27 dans l’UE [[fig:debt_eu_rank_2025]]. Fin 2025, son taux d’endettement est de 115,7 % du PIB, contre 87,3 % dans la zone euro [[fig:debt_2025_pct_gdp]] [[fig:ea21_debt_2025_pct_gdp]].
