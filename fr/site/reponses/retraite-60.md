<!-- page
slug: retraite-60
phrase: Revenons à la retraite à 60 ans
sujets: retraites
montant: return_60_general_cost_eur_bn
levier: S1
debats: 2.6, 2.7, 2.8
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/conception/04-sujets-et-objections.md (ligne retraite-60), fr/site/debats.md points 2.6 à 2.8, platform/data/figures.json, proposals.json, sources.json (f07:S14, f11:S4b, f11:S13), fr/site/chapitres/07-les-choix.md (étape 6).
- Données manquantes :
  - Fipeco, 25 juin 2024 : 17 milliards d’euros d’ici 2030 (abandon de la réforme de 2023) et jusqu’à 26 milliards à terme (60 ans) : pas d’identifiant propre, seule la somme (43) existe ; non affichés.
  - Part de l’âge légal actuel (64 ans) et calendrier de la suspension (loi de financement de la sécurité sociale pour 2026) : pas d’identifiant de chiffre ; `pension_suspension` existe dans proposals.json mais n’a pas été relu ici ; non affichés.
  - Âge légal ou effectif de départ dans le panel (DE, IT, ES, NL, BE, SE, DK) et dans l’OCDE : aucun identifiant ; non affichés.
  - Panel pour les dépenses de vieillesse (DE 9,9, IT 13,9, ES 10,4, NL 6,1, BE 10,2, SE 10,9, DK 7,2) : seulement dans les notes de `eu_cofog_old_age_2024_pct_gdp_eu27`, sans identifiant par pays ; non affichés.
  - Rang de la France après le retour à 60 ans : aucun identifiant `rank_after_*` pour cette mesure (seuls existent les rangs après une baisse de 0,5 et de 1 point, qui ne s’appliquent pas).
  - Fondation iFRAP, juin 2026, « Les six angles morts du rapport du COR » : pas d’identifiant source ; position citée sans pastille (aucun chiffre).
  - Union syndicale Solidaires : pas d’étiquette au glossaire §1.13, donc position non reprise (voir debats.md 2.8). Conséquence : la seule lecture favorable affichée est celle de La France insoumise (parti) ; aucun organisme étiqueté favorable à la mesure n’a été trouvé.
  - Fondation iFRAP : la pastille [[src:f03:cor26]] renvoie au rapport du COR qu’elle commente, pas à son article.
- Vérification (31 octobre 2026) : retiré de « Ce qui est vrai » le niveau de vie des retraités (100,2 %, année 2023 non dite, et ce n’est pas une concession à la phrase) et « pèse lourd » ; Fipeco : « jusqu’à » (le 26 est un maximum) ; fourchette LFI 2022 attribuée à l’Institut Montaigne ; supprimé « Ces chiffres de partis sont annoncés » (aucun chiffre de parti affiché) ; « aucun chiffrage officiel » adouci (debats.md 2.6 : la collecte n’a pas pu l’exclure).
- Choix faits : fourchette 43 à 58 (figures.json) ; versions partielles (26 à 35) et LFI 2022 (36 à 112,8) en fourchettes à part ; % du PIB en complément, une fois. Les 9 milliards d’euros de La France insoumise (retour à 62 ans, octobre 2026) n’ont pas d’identifiant : non affichés.
-->

> # « Revenons à la retraite à 60 ans »
>
> **En bref.** Un retour général à 60 ans coûterait de 43 à 58 milliards d’euros par an selon les deux chiffrages publiés en 2024 [[fig:return_60_general_cost_eur_bn]]. Cela représente de 28,4 à 38,3 % du déficit de 2025 [[calc:return_60_general_cost_eur_bn / deficit_2025_eur_bn * 100 = 28,4 à 38,3]].
>
> ## Ce qui est vrai
>
> L’âge de départ n’est pas qu’une question de chiffres : c’est aussi un choix de société. Le coût d’un départ plus tôt peut être financé de plusieurs façons, par exemple par des cotisations plus élevées.
>
> Le Conseil d’orientation des retraites (COR ; instance d’études et de concertation sur les retraites) publie les comptes du système. En 2025, le système affiche un déficit de 5,1 milliards d’euros [[fig:pension_balance_2025_eur_bn]]. Ses dépenses sont de 422,2 milliards d’euros, soit 14,1 % du produit intérieur brut (PIB) [[fig:pensions_cor_2025_eur_bn]] [[fig:pensions_cor_2025_pct_gdp]]. Le déficit actuel est donc petit à côté des dépenses.
>
> ## Combien
>
> Les chiffrages publiés vont de 43 à 58 milliards d’euros par an, sur des périmètres différents [[fig:return_60_general_cost_eur_bn]]. Rapporté au déficit de 2025, notifié à Eurostat (151,6 milliards d’euros [[fig:deficit_2025_eur_bn]]), cela fait de 28,4 à 38,3 % du déficit [[calc:return_60_general_cost_eur_bn / deficit_2025_eur_bn * 100 = 28,4 à 38,3]].
>
> En complément, c’est de 1,4 à 1,9 point de PIB [[fig:return_60_general_cost_pct_gdp]].
>
> Les versions partielles coûtent moins : de 26 à 35 milliards d’euros par an pour un retour à 60 ans limité aux carrières longues [[fig:return_60_partial_cost_eur_bn]].
>
> ## Les limites
>
> Les deux bornes, 43 et 58 milliards d’euros [[fig:return_60_general_cost_eur_bn]], ne mesurent pas la même chose. La première vient de Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire). Elle additionne deux estimations à des horizons différents, dont l’une est un maximum. La seconde, de l’Institut Montaigne (libéral-centriste), couvre tout le programme de retraite du Nouveau Front populaire.
>
> Le coût monte en charge sur plusieurs années, et les modèles ne s’accordent pas sur l’effet sur la croissance. Nous n’avons trouvé aucun chiffrage officiel récent, ni aucun chiffrage indépendant des programmes de 2027.
>
> La France insoumise proposait en 2022 la retraite à 60 ans avec 40 annuités [[prop:lfi_retirement_60_40|contexte]]. L’Institut Montaigne la chiffrait de 36 à 112,8 milliards d’euros selon le périmètre [[prop:lfi_retirement_60_40]]. Ce n’est pas un chiffrage de 2027.
>
> ## Qui dit quoi
>
> - **Fipeco**, 25 juin 2024 : abandonner la réforme de 2023, puis revenir à 60 ans, coûterait jusqu’à environ 43 milliards d’euros par an à terme [[fig:return_60_general_cost_eur_bn]]. Le texte argumente contre ces deux mesures.
> - **Institut Montaigne (libéral-centriste)**, 3 juillet 2024 : le programme de retraite du Nouveau Front populaire coûterait 58 milliards d’euros par an d’ici 2027 [[prop:retirement_60_general_nfp]] [[src:f07:S14]]. Il ne donne pas de chiffre pour le seul âge. Pour le programme du Rassemblement national de 2024 (60 ans après 40 annuités), il retient 34,7 milliards d’euros par an [[prop:retirement_60_partial_rn_2024]].
> - **Fondation iFRAP (libérale)**, juin 2026 : dans les simulations du COR, seule une hausse de l’âge de départ améliore le PIB, l’emploi et le solde public [[src:f03:cor26]]. Selon elle, les hausses de cotisations freinent l’activité.
> - **La France insoumise**, octobre 2026 : la retraite à 60 ans est promise plus tard dans le mandat, sans coût indiqué [[src:f11:S4b]].
>
> Les chiffrages de Fipeco et de l’Institut Montaigne datent de 2024 et portent sur des programmes de 2024.
>
> D’autres jugent qu’un départ à 60 ans peut se financer par de nouvelles recettes, par exemple la fin d’exonérations de cotisations. La page « Débats » donne leurs sources.
>
> ## Et ailleurs ?
>
> La France consacre 13,4 % du PIB aux dépenses de vieillesse en 2024 [[fig:cofog_old_age_2024_pct_gdp]], contre 10,6 % pour l’Union européenne à 27 (UE-27) [[fig:eu_cofog_old_age_2024_pct_gdp_eu27]]. Elle se place 4e sur 27 [[fig:eu_cofog_old_age_2024_rank]].
>
> Ces dépenses sont mesurées selon la classification des fonctions des administrations publiques (COFOG). Elles ne disent pas à quel âge on part dans chaque pays.
