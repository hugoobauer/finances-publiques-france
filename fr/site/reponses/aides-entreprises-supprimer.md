<!-- page
slug: aides-entreprises-supprimer
phrase: Supprimons les cadeaux aux entreprises
sujets: aides-entreprises, impots
montant: business_aid_range_eur_bn
levier: S7, R11
debats: 3.16, 8.2
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/conception/05-pages-de-reponse.md ; 04-sujets-et-objections.md (rang 5, lignes aides-entreprises-supprimer) ; fr/site/debats.md points 3.16, 8.2, 8.3 ; research/08-revenue-cuts-since-2017-and-structural.md §4 et contre-arguments (tableau des périmètres : Sénat 211 et 108, HCSP 82 et 187, France Stratégie, Clersé) ; figures.json, simulator-levers.json (S7, R11), glossaire §1.12-§1.14.
- Données manquantes (sans identifiant dans figures.json, donc omises du texte affiché) : composition des 211 Md€ du Sénat (7 de subventions, 41 de prêts et garanties Bpifrance, 88 de dépenses fiscales, 75 de cotisations) sauf les 75 (contribution_relief_general_eur_bn) ; périmètre 2 du Haut-commissariat à la Stratégie et au Plan (187 Md€) ; périmètre étroit du Sénat (108 Md€) ; estimation de la Fondation iFRAP (environ 18,5 Md€ ; 3,2 Md€ de baisses de cotisations gardées) ; fourchette de Force ouvrière (15 à 270 Md€) ; 203,2 Md€ du Clersé ; moyenne OCDE du coin socio-fiscal (35,1, seulement dans les notes de oecd_tax_wedge_single_2025_pct) ; aucune comparaison internationale du total des aides aux entreprises.
- Choix faits : le total n’est pas un rendement ; seuls deux chiffres de rendement existent (75 brut et 48 net pour les allègements généraux). Le levier S7 (périmètre 1, 82 Md€) et le levier R11 (allègements généraux) se recoupent peu mais ne s’additionnent pas avec la fourchette. « Et ailleurs ? » : pas de rang après mesure disponible ; on donne le coin socio-fiscal et son rang, sans commentaire. HCSP écrit en toutes lettres (glossaire §1.14), avec son étiquette §1.13. CGT et Force ouvrière sans étiquette (glossaire §1.13, règle 7 ; même choix qu’au chapitre 2). Sénat : rapporteur et appartenance nommés comme dans research/08 §4.1 (PCF, LR). Les 211 Md€ ne sont pas « surtout » des allègements : la plus grosse part est fiscale (88) ; le texte dit donc « baisses d’impôts et de cotisations, et prêts » (Débats 3.16), sans chiffre de composition.
- Vérification adverse (31 octobre 2026) : année 2023 ajoutée à la fourchette ; « la plus grande part » corrigé ; Force ouvrière ajoutée ; étiquette du Haut-commissariat ajoutée ; réserve Mésange (long terme) ajoutée sans chiffre (−0,1 point de PIB sans identifiant) ; recommandation Bozio-Wasmer de recentrer ajoutée ; constat commun Sénat / Haut-commissariat sur l’absence d’évaluation systématique (nombre de dispositifs, 2 200 ou 2 267, sans identifiant, omis).
-->

> # « Supprimons les cadeaux aux entreprises »
>
> **En bref.** Selon la définition retenue, les aides publiques aux entreprises vont de 45 à 211 milliards d’euros en 2023 [[fig:business_aid_range_eur_bn]]. C’est de 29,7 à 139,2 % du déficit 2025 [[calc:business_aid_range_eur_bn / deficit_2025_eur_bn * 100 = 29,7 ; 139,2]]. Ce total est une assiette, pas une recette.
>
> ## Ce qui est vrai
>
> Les montants sont élevés, et il n’existe pas de définition officielle unique des aides. Les allègements généraux de cotisations patronales coûtent à eux seuls environ 75 milliards d’euros en 2023 [[fig:contribution_relief_general_eur_bn]].
>
> Le Sénat et le Haut-commissariat à la Stratégie et au Plan font le même constat : ces dispositifs ne sont pas évalués de façon systématique. Des syndicats demandent aussi des conditions et des contreparties.
>
> ## Combien
>
> Le montant dépend du périmètre. Le bas, 45 milliards d’euros [[fig:business_aid_range_eur_bn]], correspond aux aides d’État au sens du droit européen. Le haut, 211 milliards d’euros, vient de la commission d’enquête du Sénat [[fig:business_aid_range_eur_bn]]. Entre les deux, le Haut-commissariat retient 82 milliards d’euros pour les aides directes et ciblées [[fig:business_aid_hcsp_perimeter1_eur_bn]].
>
> Rapporté au déficit 2025 notifié à Eurostat, de 151,6 milliards d’euros [[fig:deficit_2025_eur_bn]], le total représente de 29,7 à 139,2 % du déficit [[calc:business_aid_range_eur_bn / deficit_2025_eur_bn * 100 = 29,7 ; 139,2]]. Le haut de la fourchette dépasse le déficit entier : c’est une assiette, pas une économie disponible.
>
> ## Les limites
>
> Pourquoi les périmètres diffèrent : deux choix de classement pèsent presque tout. Les allègements généraux de cotisations comptent-ils comme une aide ? Les prêts et garanties de Bpifrance comptent-ils pour leur valeur nominale ? Le haut de la fourchette compte surtout des baisses d’impôts et de cotisations, et des prêts.
>
> Les périmètres recoupent aussi les niches fiscales, qui coûtent 91,8 milliards d’euros en 2025 [[fig:tax_expenditures_2025_eur_bn]] : il ne faut pas additionner les deux.
>
> Supprimer une aide ne rapporte pas son montant. Pour les allègements généraux, le rapport Bozio-Wasmer (2024) chiffre un gain net de 48 milliards d’euros, après environ 980 000 emplois détruits [[fig:contribution_relief_abolition_net_eur_bn]] [[fig:contribution_relief_abolition_jobs_fte]]. C’est nettement moins que les 75 milliards d’euros d’allègements [[fig:contribution_relief_general_eur_bn]].
>
> Ce gain est un calcul statique. À long terme, dans le modèle Mésange de la Direction générale du Trésor, ce gain disparaît presque. Le rapport recommande de recentrer ces allègements plutôt que de les supprimer.
>
> ## Qui dit quoi
>
> - **Sénat, commission d’enquête (rapporteur F. Gay, PCF)**, juillet 2025 : 211 milliards d’euros en 2023, « au moins », avec un large périmètre [[fig:business_aid_range_eur_bn]]. Son président, O. Rietmann (LR), juge que les allègements généraux compensent un coût du travail élevé et ne sont pas des aides.
> - **CGT**, 28 août 2025 : ce syndicat reprend les 211 milliards d’euros du Sénat [[fig:business_aid_range_eur_bn]] et dénonce des aides versées « sans conditions ni contreparties ».
> - **Force ouvrière**, avril 2026 : ce syndicat soutient le large périmètre du Sénat et demande une meilleure évaluation.
> - **Fondation iFRAP (libérale)**, 25 juillet 2025 : le chiffre du Sénat est trop élevé. Les baisses générales de cotisations et la plupart des niches ne sont pas des aides ciblées.
> - **Haut-commissariat à la Stratégie et au Plan (organisme d’expertise placé auprès du Premier ministre)**, juillet 2026 : 82 milliards d’euros pour les aides directes et ciblées [[fig:business_aid_hcsp_perimeter1_eur_bn]]. Il cherche à fixer des définitions stables, pas à refaire un chiffrage.
>
> ## Et ailleurs ?
>
> Nous n’avons trouvé aucune comparaison internationale du total des aides aux entreprises : les définitions varient d’un pays à l’autre. Seules les aides d’État au sens européen suivent une règle commune ; elles forment ici le bas de la fourchette.
>
> Sur le coût du travail, le coin socio-fiscal d’un célibataire au salaire moyen est de 47,2 % du coût du travail en France en 2025 [[fig:oecd_tax_wedge_single_2025_pct]]. La France est 3e de l’Organisation de coopération et de développement économiques (OCDE) [[fig:oecd_tax_wedge_single_2025_rank]].
