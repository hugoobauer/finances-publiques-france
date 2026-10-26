# Chapitre 1. Combien ?

<!--
NOTES DE PRODUCTION (non affichées)
- Statut : finalisation (25 octobre 2026) : étiquettes d’orientation du glossaire §1.13, encadré conforme au §4.6, avertissements du validateur levés pour ce fichier. Prêt pour relecture éditoriale finale.
- Place dans le parcours : Récit, chapitre 1 sur 7. Titre « Combien ? », conforme au plan (fr/20-approche-pedagogique.md §2.1 ; research/20 §2.1) ; sous-titre affiché : « La taille de la dépense publique ». Fiche thématique associée : §4.1.
- Chiffres : uniquement platform/data/figures.json et yardsticks.json. Chaque nombre affiché porte sa pastille.
  [[fig:…]] = figures.json ; [[yard:…]] = yardsticks.json (étalons, puis paramètres) ; [[calc:…]] = calcul de la plateforme, formule sur des identifiants, mention « illustratif ».
- Le texte affiché est dans les blocs de citation (« > »). Tout le reste est de la spécification. Le filtre du site pose les espaces insécables et fines (glossaire §2.1).
- « Estimez d’abord » (glossaire §1.13). Niveau B1 (glossaire §4.2). Vouvoiement. « Nous » = l’équipe éditoriale.
-->

---

## Étape 1. Ouverture : « Estimez d’abord »

> **Combien ?**
> *La taille de la dépense publique*
>
> Durée de lecture : environ 7 minutes.
>
> Écoles, hôpitaux, retraites, routes, police, allocations : tout cela a un coût. Avant les chiffres, une question.
>
> **Estimez d’abord.** Pour 100 euros de richesse produite en France en 2025 (le produit intérieur brut, ou PIB), combien d’euros de dépenses publiques ?
>
> *[après la réponse]*
>
> Votre estimation : **{x} euros**. La réponse : **57,3 euros** : les dépenses publiques représentent 57,3 % du PIB en 2025 [[fig:te_2025_pct_gdp]], soit **1 714,1 milliards d’euros** en une année [[fig:te_2025_eur_bn]].

**Interaction** : curseur 0-100 €, pas de 1 €, grisé tant qu’il n’a pas été touché ; « Voir la réponse » actif après un déplacement. Retour neutre : « Vous étiez à {écart} points de la valeur. » Histogramme des estimations des autres lecteurs à partir de 200 réponses.

**Visuel** : pile de 100 pièces (PIB 2025), 57,3 se colorent au défilement ; axe « en % du PIB ». Fiche chiffre : « 1 714,1 Md€ | 57,3 % du PIB | 2025 | mesuré ».

**Pastilles source** : [[fig:te_2025_pct_gdp]] [[fig:te_2025_eur_bn]] → Eurostat, `gov_10a_main`, 21 octobre 2026 ; Insee, *Insee Première* n° 2106, 29 mai 2026.

---

## Étape 2. Ce que ce chiffre veut dire, et ce qu’il ne veut pas dire

> Attention : 57,3 % du PIB [[fig:te_2025_pct_gdp]] ne veut pas dire que les pouvoirs publics « prennent » 57,3 % de la richesse produite. Le chiffre compare deux grandeurs ; ce n’est pas une part du gâteau.
>
> Une grande partie de la dépense publique est un transfert. L’argent passe par les caisses publiques, puis revient aux ménages, qui le dépensent eux-mêmes (retraites, allocations, indemnités de chômage). Les prestations sociales versées en argent représentent à elles seules 19,4 % du PIB en 2025 [[fig:cash_social_benefits_2025_pct_gdp]]. Ces transferts doivent quand même être financés, par les impôts, les cotisations ou l’emprunt.
>
> **Qui dépense ?** Les « administrations publiques » : l’État, la Sécurité sociale, les collectivités locales et les organismes qui en dépendent. Les entreprises publiques (EDF, SNCF) n’en font pas partie.

**Visuel** : les pièces se séparent en deux flux, « transferts » (vers une silhouette de ménage, chiffré) et « services et investissements » (non chiffré : pas de figure dédiée). Icônes des quatre sous-secteurs, sans chiffres.

**Pastilles source** : [[fig:cash_social_benefits_2025_pct_gdp]] → Eurostat, `gov_10a_main`, 21 octobre 2026.

---

## Étape 3. Premier étalon : une journée de dépense publique

> 1 714,1 milliards d’euros [[fig:te_2025_eur_bn]], c’est difficile à se représenter. Divisons par 365 : **une journée de dépense publique coûte 4,70 milliards d’euros** en 2025 [[yard:one_day_spending_eur_bn]].
>
> Cet étalon sert dans tout le site. Une promesse de « 10 milliards d’euros » représente ainsi un peu plus de deux jours de dépense publique [[calc:10 / one_day_spending_eur_bn = 2,1]].

**Visuel** : calendrier 2025 en 365 cases ; une case affiche « 4,70 Md€ », puis toutes se remplissent jusqu’au 31 décembre. « 10 milliards » est un montant rond d’exemple, pas une proposition réelle.

**Pastilles source** : [[yard:one_day_spending_eur_bn]] → calcul de la plateforme (`te_2025_eur_bn / days_in_year`) d’après Eurostat, 21 octobre 2026.

---

## Étape 4. Deuxième étalon : par habitant

> Par habitant, la dépense publique atteint **environ 24 800 euros par an** en 2025 [[fig:te_per_capita_2025_eur]], soit **68 euros par jour** [[yard:te_per_capita_per_day_eur]], nourrissons et personnes âgées compris.
>
> C’est une moyenne : ce n’est ni ce que chacun reçoit, ni ce que chacun paie.

**Visuel** : une silhouette et un ticket de caisse quotidien « 68 € ». Pas de ventilation par poste (chapitre 2). Étiquette « illustratif ».

**Pastilles source** : [[fig:te_per_capita_2025_eur]] [[yard:te_per_capita_per_day_eur]] → calcul de la plateforme : dépenses publiques 2025 / population 2025 (Eurostat).

---

## Étape 5. Troisième étalon : la part payée à crédit

> En 2025, les recettes n’ont pas suffi. Le déficit public atteint **151,6 milliards d’euros**, soit 5,1 % du PIB [[fig:deficit_2025_eur_bn]] [[fig:deficit_2025_pct_gdp]].
>
> Autrement dit, **8,8 % des dépenses publiques** ont été financées par l’emprunt [[yard:share_te_borrowed_pct]] : environ **1 euro sur 11** [[yard:borrowed_one_euro_in]].
>
> En jours, le déficit représente **32,3 jours de dépense publique** [[yard:deficit_days]]. Si l’on payait les dépenses dans l’ordre du calendrier, tout serait financé à crédit **à partir du 29 novembre environ** [[yard:borrowing_starts_day]]. C’est une image : en réalité, l’emprunt finance une petite part des dépenses toute l’année.
>
> D’où vient ce déficit ? Le chapitre 4 présente les deux lectures.

**Visuel** : sur le calendrier de l’étape 3, les 32,3 dernières cases (du 30 novembre au 31 décembre, plus trois dixièmes de la case du 29 novembre) prennent la couleur « financé par l’emprunt ». Barre « en % des dépenses publiques totales » : 91,2 % recettes, 8,8 % emprunt. Note de pastille : le déficit n’est pas égal à la hausse de la dette (ajustements stock-flux).

**Pastilles source** : [[fig:deficit_2025_eur_bn]] [[fig:deficit_2025_pct_gdp]] → Eurostat, notification d’octobre 2026 ; Insee. [[yard:share_te_borrowed_pct]] [[yard:borrowed_one_euro_in]] [[yard:deficit_days]] [[yard:borrowing_starts_day]] → calculs de la plateforme.

---

## Étape 6. Quatrième étalon : si la France était un ménage

> Imaginons un ménage qui gagne **3 000 euros par mois** [[yard:household_monthly_income_eur]]. À la même échelle que les comptes publics de 2025, il dépenserait **3 291 euros par mois** [[yard:household_spending_month_eur]] et emprunterait donc **291 euros chaque mois** [[yard:household_borrowing_month_eur]].
>
> L’image a des limites dans les deux sens. Un État ne part pas à la retraite et ses recettes suivent la croissance. Il fixe lui-même ses impôts, et une partie de ses dépenses finance des investissements durables. Mais, comme un ménage, il paie des intérêts sur ce qu’il emprunte, à un prix fixé par les prêteurs (chapitre 5).

**Visuel** : relevé de compte mensuel (revenus 3 000 € ; dépenses 3 291 € ; ligne rouge « emprunt 291 € »). Encart repliable « Comment nous avons fait ce calcul » : revenus du ménage mis à l’échelle des recettes publiques totales 2025 ; même facteur pour les dépenses et le déficit. Étiquette « illustratif ».

**Pastilles source** : [[yard:household_monthly_income_eur]] (choix éditorial) [[yard:household_spending_month_eur]] [[yard:household_borrowing_month_eur]] [[fig:total_revenue_2025_eur_bn]] → calcul de la plateforme d’après Eurostat, 21 octobre 2026.

---

## Étape 7. La France en Europe : « Estimez d’abord »

<!-- estimez-réponse: te_pct_gdp_eu_rank_2025 -->

> **Estimez d’abord.** Parmi les 27 pays de l’Union européenne, à quel rang se place la France pour les dépenses publiques rapportées au PIB ?
>
> 1re · 2e · 5e · 10e
>
> *[après la réponse]*
>
> **2e sur 27** en 2025 [[fig:te_pct_gdp_eu_rank_2025]], derrière la Finlande : 57,5 % du PIB contre 57,3 % [[fig:finland_te_2025_pct_gdp]] [[fig:te_2025_pct_gdp]]. La France était 1re chaque année de 2014 à 2023 ; la Finlande est passée devant en 2024 [[fig:te_pct_gdp_eu_rank_2025|contexte]].
>
> *Comparaison : les 27 pays de l’Union européenne (UE-27), données 2025, Eurostat, 21 octobre 2026. Le premier rang est celui de la dépense la plus élevée.*

**Interaction** : choix multiple (question Q14 de `quiz.json`), puis le graphique se construit.

**Visuel** : barres horizontales des 27 pays, triées ; France surlignée, Finlande en couleur secondaire, ligne ZE21. Axe « en % du PIB », 2025. Mention : « Le PIB de l’Irlande est gonflé par les multinationales : son ratio n’est pas comparable. » Jeu `eu27_te_pct_gdp_2025` à ajouter avant mise en ligne (voir points à trancher) ; le texte ne cite aucun autre pays que la Finlande.

**Pastilles source** : [[fig:te_pct_gdp_eu_rank_2025]] [[fig:finland_te_2025_pct_gdp]] → calcul de la plateforme d’après Eurostat (`gov_10a_main`, 21 octobre 2026).

---

## Étape 8. L’écart avec la zone euro

> Dans la zone euro à 21 pays (ZE21, Bulgarie comprise), les dépenses publiques représentent 49,7 % du PIB en 2025 [[fig:ea21_te_2025_pct_gdp]]. L’écart avec la France est de **7,6 points de PIB** [[fig:spending_gap_ea21_2025_pp]], soit **environ 227 milliards d’euros par an** [[fig:spending_gap_ea21_2025_eur_bn]].
>
> Un point de PIB, c’est 1 % de la richesse produite en un an : environ 30 milliards d’euros en 2025 [[yard:one_point_gdp_eur_bn]].
>
> Avec nos étalons, cela représente :
> - **environ 48 jours** de dépense publique [[calc:spending_gap_ea21_2025_eur_bn / one_day_spending_eur_bn = 48,3]] ;
> - **environ 1,5 fois** le déficit de 2025 [[calc:spending_gap_ea21_2025_eur_bn / deficit_2025_eur_bn = 1,5]] ;
> - **environ 3 290 euros par habitant** et par an [[calc:spending_gap_ea21_2025_eur_bn × 1000 / population_2025_m = 3 290]].
>
> L’écart a culminé à 10,4 points en 2017 [[fig:spending_gap_ea21_2017_pp]]. Il s’est réduit depuis, surtout parce que la dépense a augmenté ailleurs dans la zone euro. Une raison comptable a aussi joué. Le crédit d’impôt pour la compétitivité et l’emploi (CICE) était compté en dépense ; il a été remplacé en 2019 par une baisse de cotisations.
>
> *Comparaison : ZE21, données 2025, Eurostat. Avec la zone euro à 20 pays de 2025 (ZE20) : 7,5 points, soit 225 milliards d’euros [[fig:spending_gap_ea20_2025_pp]] [[fig:spending_gap_ea20_2025_eur_bn]].*

**Visuel** : courbe de l’écart France moins ZE21, en points de PIB, 2005-2025 (série de `research/data/09_intl_fr_gap_timeseries.csv`, à ajouter aux données). Points étiquetés : 2005 (7,1 [[fig:spending_gap_ea21_2005_pp]]), 2017 (10,4, « pic »), 2024 (7,8 [[fig:spending_gap_ea21_2024_pp]]), 2025 (7,6). Annotations sans chiffre : crise financière (2008), Covid (2020), choc énergétique (2022), CICE (2017-2019). Puis la barre « 227 Md€ » devient trois cartes d’étalon, étiquette « illustratif ».

**Pastilles source** : [[fig:spending_gap_ea21_2025_pp]] [[fig:spending_gap_ea21_2025_eur_bn]] [[fig:ea21_te_2025_pct_gdp]] [[yard:one_point_gdp_eur_bn]] → calcul de la plateforme d’après Eurostat (`gov_10a_main`, `nama_10_gdp`). Réduction de l’écart depuis 2017 et CICE : research/09 (série de l’écart, §7.3) ; research/01 (note CICE ; Insee, compte des APU 2019).

---

## Étape 9. D’où vient l’écart ? « Estimez d’abord »

<!-- estimez-réponse: gap2024_sp_plus_health_pp -->

> **Estimez d’abord.** Qu’est-ce qui explique l’essentiel de l’écart de dépense entre la France et la zone euro ?
>
> Les dépenses de fonctionnement de l’État · La protection sociale et la santé · La défense · L’éducation
>
> *[après la réponse]*
>
> **La protection sociale et la santé.** Dans la dernière répartition par poste disponible (2024), l’écart avec la zone euro est de 7,8 points de PIB [[fig:spending_gap_ea21_2024_pp]]. La protection sociale et la santé en expliquent 5,1 points [[fig:gap2024_sp_plus_health_pp]], soit **environ les deux tiers** [[calc:gap2024_sp_plus_health_pp / spending_gap_ea21_2024_pp × 100 = 65,4]].
>
> La vieillesse (surtout les retraites) pèse à elle seule 2,5 points, **environ un tiers de l’écart** [[fig:gap2024_old_age_pp]] [[fig:gap2024_old_age_share]]. Le reste se répartit entre les autres fonctions (chapitre 2).

**Interaction** : choix multiple (Q25 de `quiz.json`, codée « droite » ; équilibrée par l’affirmation B de l’étape 10).

**Visuel** : barre empilée de 7,8 points (« en points de PIB, écart avec la ZE21, 2024 ») : vieillesse 2,5 ; reste de la protection sociale 1,1 ; santé 1,5 ; autres fonctions 2,7 (gris). En survol, la part « en % de l’écart total » (vieillesse 32 % ; protection sociale, vieillesse comprise, 46 % ; santé 19 %). Bandeau : « Données 2024. Ventilation 2025 attendue en décembre 2026 (Insee) et vers février 2027 (Eurostat). » Données : `gap2024_social_protection_pp`, `gap2024_health_pp`, `gap2024_social_protection_share`, `gap2024_health_share`.

**Pastilles source** : [[fig:spending_gap_ea21_2024_pp]] [[fig:gap2024_sp_plus_health_pp]] [[fig:gap2024_old_age_pp]] [[fig:gap2024_old_age_share]] → calcul de la plateforme d’après Eurostat (`gov_10a_exp`).

---

## Étape 10. Deux affirmations à l’épreuve des ordres de grandeur

> On entend dans le débat deux affirmations opposées. Même gabarit pour les deux.
>
> **Affirmation A : « L’écart vient surtout du train de vie de l’État. »**
>
> Ce qui est exact : la rémunération des agents publics représente 12,4 % du PIB en France contre 10,0 % dans la zone euro en 2025 [[fig:compensation_employees_2025_pct_gdp]] [[fig:ea21_compensation_employees_2025_pct_gdp]]. L’écart est de 2,4 points de PIB [[calc:compensation_employees_2025_pct_gdp - ea21_compensation_employees_2025_pct_gdp = 2,4]], soit environ 72 milliards d’euros par an [[calc:(compensation_employees_2025_pct_gdp - ea21_compensation_employees_2025_pct_gdp) × one_point_gdp_eur_bn = 71,8]].
>
> C’est environ un tiers de l’écart total de dépense [[calc:(compensation_employees_2025_pct_gdp - ea21_compensation_employees_2025_pct_gdp) / spending_gap_ea21_2025_pp × 100 = 31,6]], à peu près autant que la vieillesse (étape 9). La Cour des comptes (juridiction financière) y voit un levier d’économies (chapitre 6).
>
> Ce qui ne tient pas : le mot « surtout ». Le reste de l’écart vient d’autres dépenses, d’abord sociales (étape 9). Cette masse salariale couvre aussi les collectivités locales et les hôpitaux, pas seulement l’État. Elle paie notamment des soignants et des enseignants. Ces derniers sont moins payés que la moyenne de l’Organisation de coopération et de développement économiques (OCDE) (chapitre 6).
>
> Enfin, en 2025, les salaires bruts rapportés au PIB sont sous la médiane de l’UE. L’écart tient surtout aux cotisations des employeurs publics, dont le financement des retraites des fonctionnaires. Le nombre d’agents, en part de l’emploi, dépasse la moyenne de l’OCDE, sans faire de la France un cas extrême.
>
> **Affirmation B : « La France ne dépense pas plus que ses voisins. »**
>
> Ce qui est exact : par habitant, en tenant compte des prix, la France n’est que 8e sur 27 [[fig:te_per_capita_pps_2025_rank]] (encadré ci-dessous).
>
> Ce qui ne tient pas : rapportée au PIB, sa dépense est la 2e de l’UE [[fig:te_pct_gdp_eu_rank_2025]]. Elle dépasse de 7,6 points de PIB celle de la zone euro [[fig:spending_gap_ea21_2025_pp]].
>
> Chacune contient une part de vrai ; aucune ne résume seule la situation.

**Visuel** : deux cartes côte à côte, même taille, même gabarit, aucune étiquette de parti ; ordre tiré au hasard à chaque chargement. Carte A : mini-barres « rémunération des salariés publics, en % du PIB, 2025 » (France 12,4 / ZE21 10,0), mention « écart : 2,4 points, environ 72 Md€ », et note « Les découpages par nature et par fonction se recoupent : on ne peut pas additionner leurs écarts. » Carte B : renvoi vers la bascule de l’étape 11.

**Pastilles source** : [[fig:compensation_employees_2025_pct_gdp]] [[fig:ea21_compensation_employees_2025_pct_gdp]] → Eurostat, `gov_10a_main`, 21 octobre 2026. [[yard:one_point_gdp_eur_bn]] [[fig:spending_gap_ea21_2025_pp]] → calculs de la plateforme (conversion en milliards et part de l’écart). Salaires bruts (D.11) sous la médiane de l’UE et poids des cotisations employeurs, dont cotisations imputées de retraite : research/04, §4 (K16, Eurostat `gov_10a_main`, calcul). Enseignants moins payés que la moyenne de l’OCDE : research/04, §6.1.2 (OCDE, *Regards sur l’éducation 2026*, tableau D3.1). Emploi public au-dessus de la moyenne de l’OCDE, sans être extrême : research/04, K18 (OCDE, *Government at a Glance 2025*). Cour des comptes, levier de la masse salariale : research/04, §8 (note de septembre 2026). Pas de nouveau chiffre affiché pour ces quatre points. [[fig:te_per_capita_pps_2025_rank]] → calcul de la plateforme d’après Eurostat (`nama_10_pc`, 22 octobre 2026).

---

## Étape 11. Encadré « Le meilleur contre-argument »

<!-- box-side: gauche -->
> **Le meilleur contre-argument**
>
> **« La France ne dépense pas beaucoup plus que ses voisins par habitant. Son ratio est élevé surtout parce que son PIB par habitant est plus faible que celui des pays comparables. »**
>
> Mesurons la dépense en standards de pouvoir d’achat (SPA), une unité qui corrige les écarts de prix entre pays. La dépense publique atteint alors **23 330 SPA par habitant** en France en 2025 [[fig:te_per_capita_pps_2025]]. La France se classe **8e sur 27**, pratiquement à égalité avec la Suède [[fig:te_per_capita_pps_2025_rank]] : sept pays dépensent davantage par habitant [[calc:te_per_capita_pps_2025_rank - 1 = 7]], dont l’Allemagne et les Pays-Bas.
>
> Des économistes de l’Observatoire français des conjonctures économiques (OFCE ; Sciences Po, sensibilité keynésienne) ajoutent un second argument. Selon eux, la hausse du ratio depuis 2008 tient surtout à la faible croissance du PIB, c’est-à-dire au dénominateur.
>
> *Sources : calcul de la plateforme d’après Eurostat (office statistique de l’Union européenne ; `nama_10_pc`, 22 octobre 2026) ; B. Ducoudré, M. Plane, R. Sampognaro, « Dépenses publiques : quels enjeux pour le prochain quinquennat ? », OFCE (Sciences Po, sensibilité keynésienne),* Policy Brief *n° 17, 19 avril 2017.*
>
> **Ce qu’on peut répondre**
>
> Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire) rappelle que le PIB est la base des impôts. Avec moins de revenu par habitant, financer la même dépense par habitant demande des prélèvements plus élevés.
>
> Quant au dénominateur, regardons la dépense hors inflation. Le Haut-commissariat à la Stratégie et au Plan (organisme d’expertise placé auprès du Premier ministre) l’a mesurée. De 2005 à 2025, elle a augmenté en moyenne de **1,4 % par an** [[fig:te_volume_growth_avg_2005_2025_pct]].
>
> Sur la même période, d’après Eurostat (office statistique de l’Union européenne), elle a gagné **+3,0 points de PIB** [[fig:te_change_2005_2025_pp]]. Les recettes ont gagné **+1,4 point de PIB** [[fig:total_revenue_change_2005_2025_pp]]. Les deux ratios ont pourtant le même dénominateur. La faible croissance compte donc, mais n’explique pas tout.
>
> Les deux chiffres sont donc vrais, mais répondent à deux questions différentes. Par habitant : quel volume de services et de prestations reçoit-on ? En % du PIB : quel effort faut-il pour les financer ?
>
> *Sources : F. Ecalle, « Le rapport des dépenses publiques au PIB : pertinence et comparabilité », Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire), 15 janvier 2025 ; Haut-commissariat à la Stratégie et au Plan (organisme d’expertise placé auprès du Premier ministre), « Focus Finances publiques », 17 juillet 2026 ; calcul de la plateforme d’après Eurostat (`gov_10a_main`, 21 octobre 2026).*

**Visuel** : sur le même écran que les étapes 7 à 10, jamais replié (glossaire §4.6). Le graphique de l’étape 7 reçoit une bascule « en % du PIB » ↔ « en SPA par habitant » ; la barre de la France glisse de la 2e à la 8e place (600 ms, sans animation si « réduire les animations »). Suède marquée « pratiquement à égalité ». Pas de rang 2024 en SPA sans mention (8e ou 9e selon la méthode). Valeurs SPA des 26 autres pays à ajouter avant mise en ligne. La liste complète des sept pays (research/01) peut figurer dans le graphique, pas dans le texte.

**Pastilles source** : [[fig:te_per_capita_pps_2025]] [[fig:te_per_capita_pps_2025_rank]] → calcul de la plateforme : dépense / PIB × PIB par habitant en SPA, Eurostat (`nama_10_pc`, 22 octobre 2026). OFCE, *Policy Brief* n° 17 (2017), pastille de financement : « Financé par une subvention publique versée par l’État à la Fondation nationale des sciences politiques (site de l’OFCE). » (https://www.ofce.fr/ofce/statuts.html, glossaire §1.13) ; Fipeco (15 janvier 2025), pas de pastille de financement (non détaillé sur son site). Réponse sur le dénominateur : [[fig:te_volume_growth_avg_2005_2025_pct]] (Haut-commissariat à la Stratégie et au Plan, « Focus Finances publiques », 17 juillet 2026, croissance en volume de la dépense 2005-2025) ; [[fig:te_change_2005_2025_pp]] [[fig:total_revenue_change_2005_2025_pp]] (Eurostat `gov_10a_main`, 21 octobre 2026 ; research/10 §4.2).

---

## Étape 12. Une autre objection : public ou privé ?

> Une autre objection revient souvent : en France, retraites et santé passent surtout par des caisses publiques, ailleurs davantage par des assurances privées. Le chapitre 2 en mesure la portée.

---

## Étape 13. Pourquoi vous verrez parfois un autre chiffre

> Pendant la campagne, vous lirez parfois 56,6 % du PIB pour 2025, et non 57,3 % du PIB [[fig:te_excl_tax_credits_2025_pct_gdp]] [[fig:te_2025_pct_gdp]]. Ce n’est pas une erreur. Le gouvernement, le Haut Conseil des finances publiques (HCFP) et la Cour des comptes retirent certains crédits d’impôt. La comptabilité nationale, elle, les compte comme des dépenses.
>
> Sur cette base, le projet de loi de finances pour 2027 prévoit 57,1 % du PIB en 2026, puis 56,9 % en 2027 [[fig:te_excl_tax_credits_2026f_pct_gdp]] [[fig:te_excl_tax_credits_2027f_pct_gdp]].
>
> Sur ce site, nous utilisons 57,3 % du PIB [[fig:te_2025_pct_gdp]], la mesure d’Eurostat, harmonisée pour comparer les pays européens.

**Visuel** : fiche chiffre double (« 57,3 % du PIB | Eurostat / Insee | mesuré » et « 56,6 % du PIB | hors crédits d’impôt | gouvernement, HCFP, Cour des comptes | mesuré »), puis courbe 2025-2027, points 2026 et 2027 « prév. » en pointillés.

**Pastilles source** : [[fig:te_excl_tax_credits_2025_pct_gdp]] [[fig:te_excl_tax_credits_2026f_pct_gdp]] [[fig:te_excl_tax_credits_2027f_pct_gdp]] → HCFP, *Avis n° HCFP-2026-5*, 25 septembre 2026 (publié le 1er octobre 2026) ; *Projet de loi de finances pour 2027*.

---

## Étape 14. À retenir, et la suite

> **À retenir**
> - 1 714,1 milliards d’euros de dépenses publiques en 2025, soit 57,3 % du PIB [[fig:te_2025_eur_bn]] [[fig:te_2025_pct_gdp]].
> - Une journée de dépense publique : 4,70 milliards d’euros [[yard:one_day_spending_eur_bn]] ; par habitant, 68 euros par jour [[yard:te_per_capita_per_day_eur]].
> - Environ un euro sur onze est emprunté ; le déficit équivaut à 32,3 jours de dépense [[yard:borrowed_one_euro_in]] [[yard:deficit_days]].
> - 2e de l’UE en % du PIB, mais 8e par habitant en pouvoir d’achat [[fig:te_pct_gdp_eu_rank_2025]] [[fig:te_per_capita_pps_2025_rank]].
> - Environ les deux tiers de l’écart avec la zone euro viennent de la protection sociale et de la santé (2024) [[calc:gap2024_sp_plus_health_pp / spending_gap_ea21_2024_pp × 100 = 65,4]].
>
> **Pour aller plus loin**
> - Fiche « Vue d’ensemble des dépenses » : l’évolution de l’écart avec la zone euro depuis 2005, année par année.
> - Espace confiance, page Méthode : comptabilité nationale et comptabilité budgétaire, crédits d’impôt, SPA.
> - Page Débats : tous les contre-arguments sur la taille de la dépense, avec auteurs et orientations.
> - Outil « Comparer avec l’Europe » : choisissez un autre pays ou un autre indicateur.
>
> **La suite.** Savoir combien on dépense ne dit pas à quoi sert l’argent. Le chapitre 2, « Où va l’argent ? », répartit ces 1 714,1 milliards [[fig:te_2025_eur_bn]] jour par jour sur le calendrier de l’année.

**Visuel** : carte récapitulative partageable (quatre étalons en icônes : jour, habitant, déficit, ménage ; chaque chiffre garde sa pastille sur le web). Boutons « Chapitre 2 : Où va l’argent ? » (principal) et « Comparer avec l’Europe » (secondaire, préréglé « dépenses publiques, % du PIB, 2025, UE-27 »). Le calendrier de l’étape 5 sert de transition vers celui du chapitre 2. Liens « Pour aller plus loin » : fiche §4.1, Méthode (§4.17), Débats, comparateur (fr/20-approche-pedagogique.md §2.1).

**Pastilles source** : reprises des étapes 1, 3, 5, 7, 9 et 11.

---

<!--
LISTE DES IDENTIFIANTS UTILISÉS (contrôle)
figures.json : te_2025_eur_bn, te_2025_pct_gdp, cash_social_benefits_2025_pct_gdp, te_per_capita_2025_eur, deficit_2025_eur_bn, deficit_2025_pct_gdp, total_revenue_2025_eur_bn, te_pct_gdp_eu_rank_2025, finland_te_2025_pct_gdp, ea21_te_2025_pct_gdp, spending_gap_ea21_2025_pp, spending_gap_ea21_2025_eur_bn, spending_gap_ea20_2025_pp, spending_gap_ea20_2025_eur_bn, spending_gap_ea21_2005_pp, spending_gap_ea21_2017_pp, spending_gap_ea21_2024_pp, gap2024_sp_plus_health_pp, gap2024_social_protection_pp, gap2024_old_age_pp, gap2024_old_age_share, gap2024_health_pp, gap2024_social_protection_share, gap2024_health_share, compensation_employees_2025_pct_gdp, ea21_compensation_employees_2025_pct_gdp, te_per_capita_pps_2025, te_per_capita_pps_2025_rank, te_excl_tax_credits_2025_pct_gdp, te_excl_tax_credits_2026f_pct_gdp, te_excl_tax_credits_2027f_pct_gdp, population_2025_m.
yardsticks.json : one_day_spending_eur_bn, one_point_gdp_eur_bn, te_per_capita_per_day_eur, share_te_borrowed_pct, borrowed_one_euro_in, deficit_days, borrowing_starts_day, household_spending_month_eur, household_borrowing_month_eur ; paramètres household_monthly_income_eur, days_in_year.

POINTS À TRANCHER AVANT PUBLICATION
1. Jeux de données à ajouter (propriétaire : données) : valeurs 2025 des 27 pays en % du PIB et en SPA par habitant (étapes 7 et 11) ; série 2005-2025 de l’écart avec la ZE21 (étape 8).
2. finland_te_2025_pct_gdp porte l’année « 2024-2025 » alors que 57,5 % est la valeur 2025 : corriger le champ year dans figures.json.
3. Q25 de quiz.json : l’option « L’administration et le train de vie » doit devenir « Les dépenses de fonctionnement de l’État » (glossaire). Toujours non fait au 25 octobre 2026.
4. Les trois conversions de l’étape 8 et les « deux tiers » de l’étape 9 sont des [[calc:]] : si l’on préfère des étalons versionnés, créer dans yardsticks.json spending_gap_ea21_days, spending_gap_ea21_deficit_ratio, spending_gap_ea21_per_capita_eur et gap2024_sp_plus_health_share.
5. LISEZMOI-site.md (§5.1, point 2, et tableau des chapitres : 5 548 mots) est à mettre à jour par son propriétaire : titre tranché, nouvelle longueur.
6. Étape 11, réponse sur le dénominateur (propriétaire : données) : créer te_volume_growth_avg_2005_2025_pct (HCSP, 1,4 % par an), te_change_2005_2025_pp et total_revenue_change_2005_2025_pp (research/10 §4.2), puis remplacer la formulation qualitative par les chiffres avec pastilles. Facultatif : une figure D.11 (salaires bruts, % du PIB, France et médiane UE) pour chiffrer l’étape 10.
-->

---

## Notes de relecture

### Passe du 25 octobre 2026 : ids de données créés

- Étape 11, réponse sur le dénominateur : **appliqué**. Chiffres affichés avec pastilles : 1,4 % par an en volume (`te_volume_growth_avg_2005_2025_pct`, HCSP, 17 juillet 2026) ; +3,0 points de PIB pour la dépense contre +1,4 point pour les recettes (`te_change_2005_2025_pp`, `total_revenue_change_2005_2025_pp`, Eurostat). Point à trancher 6 clos. Les mentions « partiellement appliqué » ci-dessous sont dépassées.

**Passe de finalisation du 25 octobre 2026 (étiquettes, encadré, propriété, contrôles)**
- 1. Nouvelles données (D-data-pass) : **sans objet** ; aucune des 19 figures ajoutées n’est affectée au chapitre 1, et le chapitre ne montre pas le retour à 60 ans. Point à trancher 6 inchangé : `te_volume_growth_avg_2005_2025_pct`, `te_change_2005_2025_pp` et `total_revenue_change_2005_2025_pp` n’existent toujours pas ; la réponse sur le dénominateur reste qualitative.
- 2. Étiquettes (§1.13), copiées mot pour mot : Cour des comptes (juridiction financière) à sa première mention (étape 10) ; Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire), ancienne variante « tenu par » retirée ; OFCE (Observatoire français des conjonctures économiques ; Sciences Po, sensibilité keynésienne) dans le texte et dans la ligne de source ; dans l’encadré et sa réponse, Haut-commissariat à la Stratégie et au Plan (organisme d’expertise placé auprès du Premier ministre) et Eurostat (office statistique de l’Union européenne). Sigle HCSP retiré de la ligne de source affichée et de la pastille (§2.7). Pastille de financement de l’OFCE ajoutée dans la ligne « Pastilles source » (vérifiée par le propriétaire du glossaire sur ofce.fr) ; aucune pour Fipeco.
- 3. Encadré (§4.6) : titre exact conservé ; thèse en gras entre guillemets ; auteur nommé avec son étiquette ; lignes « *Sources :* » en italique reprenant les étiquettes ; `box-side: gauche` conservé ; « Ce qu’on peut répondre » ne répond qu’à la thèse (revenu par habitant et dénominateur).
- 4. Doublons de propriété et listes d’« économies faciles » : **sans objet** ; le chapitre 1 reste propriétaire du bloc du déficit, de l’image du ménage et de l’écart avec la zone euro ; aucune mention des 980 000 emplois, du paquet de 10 à 25 milliards ni des économies faciles.
- 5. Validateur : réponses déclarées pour les « Estimez d’abord » des étapes 7 et 9 (`<!-- estimez-réponse: … -->`) ; pastilles ajoutées aux nombres nus (57,3 euros et 57,3 % aux étapes 1, 2 et 13 ; 1 714,1 milliards aux étapes 3 et 14) ; rang historique de l’étape 7 marqué `|contexte` ; « une fois et demie » affiché « 1,5 fois » ; « deux tiers » du récapitulatif chipé par le `[[calc:]]` de l’étape 9 ; dénominateur « du PIB » ajouté à l’étape 13 ; première mention de la zone euro sous la forme « zone euro à 21 pays (ZE21, Bulgarie comprise) » (étape 8) ; phrases de plus de 25 mots coupées (étapes 2, 6, 8, 10, 11, 13) ; paragraphes de l’étape 10 et de la réponse de l’étape 11 scindés (60 mots au plus) ; ligne de légende UE-27 réécrite sans nombre nu.
- 6. Contrôles : `python3 -I validate.py --strict` : 0 erreur et 0 avertissement propres à ce fichier. Restent deux avertissements inter-chapitres de coïncidence de valeurs, à traiter par les autres propriétaires ou par le validateur : « 10,0 % » (rémunération des salariés publics de la ZE21, ici ; cotisations employeurs, chapitre 3) et « 30 milliards » (point de PIB, ici ; exemple de coupe, chapitre 7). Texte affiché : 1 762 mots, « environ 7 minutes » inchangé.

**Passe transversale du 25 octobre 2026 (plan de site ; corrections transversales)**
- Propriété conservée : bloc du déficit 2025 (étape 5, intact), image du ménage complète et texte canonique des limites (étape 6), écart international et ventilation 2024 (étapes 8 et 9). Les autres chapitres renvoient au chapitre 1.
- 1. Durée de lecture (étape 1) : **appliqué** (« environ 7 minutes » ; 1 670 mots affichés / 240, script de comptage). « Niveau : B1 » non affiché.
- 2. Arrondi « 57,3 % de la richesse produite » (étape 2) : **appliqué**.
- 3. Bloc du déficit (étape 5) : **appliqué** (conservé sans coupe).
- 4. Limites de l’image du ménage (étape 6) : **appliqué** (texte canonique, symétrique : impôts fixés par l’État ; prix des intérêts fixé par les prêteurs).
- 5. Étape 8 : **appliqué** (définition du point de PIB, environ 30 milliards, pastille `[[yard:one_point_gdp_eur_bn]]` = 29,9, ajoutée aussi aux pastilles source ; CICE développé ; « ZE21, Bulgarie comprise »).
- 6. Étape 9, « répartition par poste » remplace « ventilation par fonction » (jargon) : **appliqué**.
- 7. Étape 10, OCDE développé à la première occurrence : **appliqué**.
- 8. Étape 11, encadré (contre-argument de gauche/keynésien maintenu) : **appliqué** (« pratiquement à égalité » dans le texte et le visuel ; OFCE développé ; *Policy Brief* distingué en romain dans la ligne de source en italique, glossaire §2.5). « Ce qu’on peut répondre » inchangé.
- 9. Étape 12, objection SOCX déplacée au chapitre 2, étape 10 : **appliqué** (une ligne de renvoi ; visuel et pastilles supprimés ; quatre identifiants SOCX retirés de la liste de contrôle et du point à trancher 1).
- 10. Étape 13, dénominateur « du PIB » ajouté : **appliqué**.
- 11. Étape 14 : **sans changement** (forme canonique déjà en place).
- 12. Contrôles : `python3 -I validate.py` : 0 erreur, 0 avertissement. Texte affiché : 1 665 mots avant la ligne de durée, environ 1 670 après (cible 1 500-2 200). Aucun chiffre hors données ajouté ; aucun point rejeté.

**Troisième passe du 25 octobre 2026 (audit contradictoire : lecteurs de gauche et de droite, cohérence des chiffres)**
- Étape 10, affirmation A (non sequitur, taille de l’écart masquée ; lecture « droite ») : **partiellement appliqué**. Repris : l’écart de 2,4 points est chiffré en milliards (environ 72 Md€, `[[calc:]]` avec `one_point_gdp_eur_bn`) et en part de l’écart total (environ un tiers, comparable à la vieillesse) ; la réfutation porte désormais sur « surtout » ; l’avis de la Cour des comptes (levier d’économies) est mentionné ; enseignants moins payés que la moyenne de l’OCDE (renvoi au chapitre 6). Écarté : la conclusion « l’écart tient surtout au nombre d’agents, pas à leur rémunération », contredite par research/04 (K16, §4, §8 point 2 : salaires bruts D.11 sous la médiane de l’UE en 2025 ; l’écart de D.1 vient surtout des cotisations employeurs, dont les cotisations imputées de retraite ; emploi public au-dessus de la moyenne de l’OCDE mais pas extrême, K18). Le texte énonce ces deux faits sans trancher. Formulation en phrases de deux chiffres au plus (glossaire §4).
- Étape 11, réponse à l’argument du dénominateur (OFCE ; lecture « droite ») : **partiellement appliqué**. Une réponse est ajoutée dans « Ce qu’on peut répondre » (croissance de la dépense hors inflation sur 2005-2025, HCSP ; hausse du ratio de dépense nettement supérieure à celle des recettes, même dénominateur, Eurostat). Les chiffres proposés (1,4 % par an ; +3,0 contre +1,4 points) ne sont pas affichés : `te_volume_growth_avg_2005_2025_pct` et `te_change_2005_2025_pp` n’existent pas dans platform/data au moment de la passe, et ce chapitre ne peut pas modifier les données (point à trancher 6). L’argument libéral « les prélèvements pèsent sur la croissance » n’est pas ajouté : aucune source attribuée dans la base de recherche.
- Arrondis entre chapitres (32,3 jours ; 1 714,1 milliards) : **sans objet pour ce fichier** ; le chapitre 1 utilise déjà l’arrondi unique. Les corrections portent sur les chapitres 2, 3, 6 et 7.
- Même nombre, deux identifiants (24 800 €) : **sans objet pour ce fichier** ; le chapitre 1 utilise déjà `[[fig:te_per_capita_2025_eur]]`, la correction porte sur le chapitre 2.
- Étape 12, unités manquantes : **appliqué** (« 33,2 % du PIB », « 22,0 % du PIB »).
- Pastilles `[[calc:]]` sans résultat : **sans objet pour ce fichier** ; toutes les pastilles `[[calc:]]` du chapitre 1, y compris les deux nouvelles (71,8 ; 31,6), portent leur résultat.
- Contrôles : `python3 -I validate.py` : 0 erreur, 0 avertissement. Texte affiché (blocs « > », hors pastilles et code) : environ 1 760 mots, dans la cible de 1 500 à 2 200.

**Deuxième passe du 25 octobre 2026 (pastilles, longueur, titre)**
- Espaces réservés : aucun `[[fig-a-creer:…]]` ni bloc `EN ATTENTE DE DONNÉES` dans ce chapitre (rien à remplacer ; aucune donnée déclarée invérifiable par l’étape données ne concernait le chapitre 1). `validate.py` : 0 erreur pour ce fichier.
- Pastilles et valeurs : chaque pastille recoupée avec figures.json et yardsticks.json (format français, arrondi). Corrections :
  - étape 8 : les trois conversions (48 jours, une fois et demie le déficit, 3 290 € par habitant) portaient des pastilles d’entrées dont la valeur n’est pas le nombre affiché (4,70 ; 151,6 ; 68,998) : remplacées par des `[[calc:]]` avec leur formule et leur résultat (48,3 ; 1,5 ; 3 290) ;
  - étapes 3, 9, 10, 11 : pastilles `[[calc:]]` ajoutées aux nombres qui n’en avaient pas (2,1 jours pour 10 milliards ; 65,4 % = deux tiers ; 2,4 points ; sept pays) ;
  - étape 6 : 3 000 € reçoit sa pastille `[[yard:household_monthly_income_eur]]` (paramètre, choix éditorial) ;
  - « 1 714 milliards » → « 1 714,1 milliards » partout, pour un arrondi unique (glossaire, règle « même chiffre, même arrondi »).
- Longueur du texte affiché (blocs « > », hors pastilles, didascalies et code ; script de comptage) : 1 869 mots avant, 1 555 après (fichier complet : 5 548 mots avant, environ 4 040 après). Coupes : répétitions (étape 4, étape 5, recap), liste des sept pays (renvoyée au graphique), série 2005-2024 de l’écart (renvoyée au graphique et à la fiche §4.1), détails de l’étape 13. Ajout d’une liste « Pour aller plus loin » (fiche §4.1, Méthode, Débats, comparateur). Spécifications visuelles condensées.
- Titre : « Chapitre 1. Combien ? », conforme au plan (fr/20-approche-pedagogique.md §2.1, qui a retenu « Combien ? » le 25 octobre 2026) ; « La taille de la dépense publique » devient le sous-titre. Point 3 de l’ancienne liste clos.

**Première relecture du 25 octobre 2026 (chiffres, neutralité, français)** : tous les nombres recoupés avec les fichiers de données et les calculs dérivés refaits ; arrondi unique de `deficit_days` (32,3) ; calendrier corrigé à 32 cases plus trois dixièmes ; phrase sur le financement des transferts (étape 2) ; image du calendrier nuancée (étape 5) ; limites du ménage symétriques (étape 6) ; raisons de la baisse de l’écart depuis 2017 sans chiffre (étape 8) ; « train de vie de l’État » retiré de l’option de quiz ; gabarit identique pour les deux affirmations (étape 10) ; deux lectures explicites à l’étape 12 ; typographie vérifiée.
