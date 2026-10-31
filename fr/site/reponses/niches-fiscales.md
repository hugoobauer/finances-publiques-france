<!-- page
slug: niches-fiscales
phrase: Supprimons les niches fiscales
sujets: impots, aides-entreprises
montant: tax_expenditures_2025_eur_bn
levier: R9
debats: 3.15, 8.3
-->

<!--
NOTES POUR L’ÉQUIPE
- Sources lues : fr/conception/05-pages-de-reponse.md ; 04-sujets-et-objections.md (rang 13, ligne niches-fiscales ; rang 5 des aides aux entreprises) ; fr/site/debats.md points 3.15, 3.16, 8.3 ; figures.json (tax_expenditures_2025_eur_bn, tax_expenditures_2025_pct_gdp, tax_expenditures_count, niches_sociales_2025_eur_bn, oecd_tax_to_gdp_2024_*, gdp_2025_eur_bn, deficit_2025_eur_bn) ; proposals.json (tax_expenditures_trim_lfi, dutreil_reform_eelv) ; simulator-levers.json (R9) ; glossaire §1.13, §1.14 (étiquettes), entrée « réservoir ».
- Données manquantes (sans identifiant dans figures.json, donc omises du texte affiché) : coût du crédit d’impôt recherche (7,1 Md€), du crédit d’impôt emploi à domicile (7,1 Md€) et du pacte Dutreil (3,8 Md€), lisibles seulement dans les notes de tax_expenditures_trim_lfi ; estimation de la Fondation iFRAP (environ 52 Md€ de niches, 8,3 Md€ gardés comme aide) ; chiffres de Fipeco (coût chiffré pour 387 niches sur 474, environ 10 Md€ de baisse due au changement de méthode sur la TVA, 95,0 Md€ en 2023 avec l’ancienne méthode) ; part des niches dans les 211 Md€ du Sénat (88 Md€, CGT) ; comparaison internationale du coût des niches (aucune dans figures.json) ; rang après la mesure pour le total de 91,8 Md€ (il dépasserait le Danemark : non affiché, car la suppression totale n’est pas un scénario sérieux).
- Choix faits : pas de fourchette de 22 à 91,8 Md€ (vérification du 31 octobre 2026) : les 22 Md€ de La France insoumise portent sur les niches fiscales ET sociales (measure_fr de tax_expenditures_trim_lfi), alors que 91,8 Md€ ne compte que les niches fiscales ; le total est présenté comme un plafond théorique, un réservoir, pas un rendement (glossaire). Les 22 Md€ sont « annoncés » pour 2027 (claimed.year) ; leur part est rapportée au déficit 2025 de référence, comme le veut la spécification. Le calcul OCDE de « Et ailleurs ? » mêle un taux 2024, le PIB 2025 et une annonce pour 2027 : ordre de grandeur seulement. Le calcul littéral « 22 » remplace l’identifiant de la proposition, que [[calc:]] ne sait pas lire (claimed.central seulement). Seul rendement chiffré d’une niche : Dutreil (1,3 Md€, calcul statique de l’équipe, EELV). Les niches sociales (91,0 Md€) sont citées comme périmètre voisin, non additionné. « Et ailleurs ? » : taux de prélèvement OCDE, avec rang après la mesure calculé si les 22 Md€ étaient encaissés en entier (le Danemark, à 45,2 %, reste au-dessus).
-->

> # « Supprimons les niches fiscales »
>
> **En bref.** En 2025, les niches fiscales coûtent 91,8 milliards d’euros à l’État [[fig:tax_expenditures_2025_eur_bn]]. C’est un réservoir, pas un rendement. Le programme de La France insoumise annonce 22 milliards d’euros [[prop:tax_expenditures_trim_lfi]], soit 14,5 % du déficit [[calc:22 / deficit_2025_eur_bn * 100 = 14,5]].
>
> ## Ce qui est vrai
>
> Les niches fiscales, que l’on appelle aussi dépenses fiscales, sont très nombreuses : on en compte 474 en 2025 [[fig:tax_expenditures_count]]. Ce sont des recettes que l’État ne perçoit pas.
>
> Leur coût total est élevé : 3,1 % du produit intérieur brut (PIB) [[fig:tax_expenditures_2025_pct_gdp]]. Le FMI (Fonds monétaire international ; organisation internationale) recommande que toute recette nouvelle vise les niches inefficaces.
>
> ## Combien
>
> Le total est de 91,8 milliards d’euros en 2025 [[fig:tax_expenditures_2025_eur_bn]]. Rapporté au déficit de 2025 notifié à Eurostat, 151,6 milliards d’euros [[fig:deficit_2025_eur_bn]], il représenterait 60,6 % du déficit [[calc:tax_expenditures_2025_eur_bn / deficit_2025_eur_bn * 100 = 60,6]]. Ce n’est qu’un plafond théorique.
>
> Le programme de La France insoumise (LFI) annonce 22 milliards d’euros, en réduisant les niches fiscales et sociales jugées « injustes » [[prop:tax_expenditures_trim_lfi]]. Cela ferait 14,5 % du déficit [[calc:22 / deficit_2025_eur_bn * 100 = 14,5]]. Nous n’avons trouvé aucune estimation indépendante de ce chiffre.
>
> ## Les limites
>
> Un coût n’est pas un rendement. Chaque niche a un objectif et des bénéficiaires, et la supprimer change leur comportement. Le coût n’est connu que pour une partie des niches, et elles sont peu évaluées. Comme toute hausse d’impôt, une suppression freinerait aussi un peu l’activité [[src:f17:S6]].
>
> Un exemple chiffré : Les Écologistes proposent de réduire l’exonération du pacte Dutreil, qui allège l’impôt lors de la transmission d’une entreprise. D’après notre calcul, cela rapporterait environ 1,3 milliard d’euros par an [[prop:dutreil_reform_eelv]]. C’est un calcul statique, sans réaction des contribuables.
>
> Les niches fiscales recoupent aussi d’autres mesures. Les niches sociales, surtout des exonérations de cotisations, coûtent 91,0 milliards d’euros en 2025 [[fig:niches_sociales_2025_eur_bn]]. Une partie de ces deux totaux figure aussi dans les aides aux entreprises : ces montants ne s’additionnent pas.
>
> ## Qui dit quoi
>
> - **Fondation iFRAP (libérale)**, 25 juillet 2025 : la plupart des niches ne sont pas des aides ciblées aux entreprises. Elles « suivent le niveau global des prélèvements » et reflètent en partie le niveau d’imposition.
> - **CGT**, 28 août 2025 : ce syndicat compte une part des niches parmi les aides aux entreprises. Elle dénonce des aides accordées « sans conditions ni contreparties ».
> - **Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire)**, 4 décembre 2024 : le coût n’est chiffré que pour une partie des niches. Un changement de méthode sur la taxe sur la valeur ajoutée (TVA) a réduit le total.
> - **FMI**, 21 mai 2026 : toute recette nouvelle doit viser les niches et les dépenses fiscales inefficaces.
> - **La France insoumise**, programme 2027 : annonce 22 milliards d’euros en réduisant les niches fiscales et sociales « injustes » [[prop:tax_expenditures_trim_lfi]].
>
> ## Et ailleurs ?
>
> Nous n’avons trouvé aucune comparaison internationale du coût des niches. Sur l’ensemble des prélèvements, la France est 2e en 2024 [[fig:oecd_tax_to_gdp_2024_rank]], parmi les 36 pays de l’Organisation de coopération et de développement économiques (OCDE) classés. Son taux est de 43,5 % du PIB [[fig:oecd_tax_to_gdp_2024_pct_gdp]], contre une moyenne de 34,1 % [[fig:oecd_avg_tax_to_gdp_2024_pct_gdp]]. Le Danemark est premier, à 45,2 % [[fig:denmark_tax_to_gdp_2024_pct_gdp]].
>
> Si les 22 milliards d’euros étaient encaissés en entier, ce taux passerait à 44,2 % du PIB [[calc:oecd_tax_to_gdp_2024_pct_gdp + 22 / gdp_2025_eur_bn * 100 = 44,2]]. Même après cette mesure, la France resterait 2e sur 36 [[fig:oecd_tax_to_gdp_2024_rank]].
