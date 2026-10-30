# Chapitre 1. Combien ?

<!--
NOTES DE PRODUCTION (non affichées)
- Statut : confrontation aux sources publiques (30 octobre 2026), voir les notes de relecture ; finalisation (25 octobre 2026) : étiquettes d’orientation du glossaire §1.13, encadré conforme au §4.6, avertissements du validateur levés pour ce fichier. Prêt pour relecture éditoriale finale.
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
> Durée de lecture : environ 9 minutes.
>
> Écoles, hôpitaux, retraites, routes, police, allocations : tout cela a un coût.
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

> Attention : 57,3 % du PIB [[fig:te_2025_pct_gdp]] ne veut pas dire que les pouvoirs publics « prennent » ou consomment 57,3 % de la richesse produite. Le chiffre compare deux grandeurs ; ce n’est pas une part du gâteau.
>
> Une grande partie de la dépense publique est un transfert : l’argent est versé aux ménages, qui le dépensent eux-mêmes (retraites, allocations, indemnités de chômage). Les prestations sociales versées en argent représentent à elles seules 19,4 % du PIB en 2025 [[fig:cash_social_benefits_2025_pct_gdp]]. Ce chiffre ne compte ni les soins remboursés ni les services publics.
>
> Ces transferts sont financés par les impôts, les cotisations ou l’emprunt, souvent payés par d’autres personnes que celles qui les reçoivent.
>
> **Qui dépense ?** Les « administrations publiques » : l’État, la Sécurité sociale, les collectivités locales et les organismes qui en dépendent. Les entreprises publiques (EDF, SNCF) n’en font pas partie.

**Visuel** : les pièces se séparent en deux flux, « transferts » (vers une silhouette de ménage, chiffré) et « services et investissements » (non chiffré : pas de figure dédiée). Icônes des quatre sous-secteurs, sans chiffres.

**Pastilles source** : [[fig:cash_social_benefits_2025_pct_gdp]] → Eurostat, `gov_10a_main`, 21 octobre 2026.

---

## Étape 3. Premier étalon : une journée de dépense publique

> 1 714,1 milliards d’euros [[fig:te_2025_eur_bn]], c’est difficile à se représenter. Divisons par 365 : **une journée de dépense publique coûte 4,70 milliards d’euros** en 2025 [[yard:one_day_spending_eur_bn]].
>
> Une promesse de « 10 milliards d’euros » représente ainsi un peu plus de deux jours de dépense publique [[calc:10 / one_day_spending_eur_bn = 2,1]].

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

> En 2025, les dépenses ont dépassé les recettes. Le déficit public atteint **151,6 milliards d’euros**, soit 5,1 % du PIB [[fig:deficit_2025_eur_bn]] [[fig:deficit_2025_pct_gdp]].
>
> Autrement dit, **8,8 % des dépenses publiques** ont été financées par l’emprunt [[yard:share_te_borrowed_pct]] : environ **1 euro sur 11** [[yard:borrowed_one_euro_in]].
>
> En jours, le déficit représente **32,3 jours de dépense publique** [[yard:deficit_days]]. Si l’on payait les dépenses dans l’ordre du calendrier, tout serait financé à crédit **à partir du 29 novembre environ** [[yard:borrowing_starts_day]]. C’est une image : en réalité, l’emprunt finance une petite part des dépenses toute l’année.
>
> Faut-il s’en inquiéter ? Les économistes divergent, sauf sur le court terme. François Ecalle, de Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire), juge nécessaire de stabiliser la dette par rapport au PIB.
>
> François Geerolf, économiste à l’Observatoire français des conjonctures économiques (OFCE ; Sciences Po, sensibilité keynésienne), qui écrit à titre personnel, juge cet effort inutile. Selon lui, la dette se stabilisera « naturellement ».
>
> D’où vient ce déficit ? Côté recettes, la France est aussi l’un des pays qui prélèvent le plus : 2e de l’Organisation de coopération et de développement économiques (OCDE) en 2024 [[fig:oecd_tax_to_gdp_2024_rank]]. Le chapitre 4 présente les deux lectures, dépenses et recettes.

**Visuel** : sur le calendrier de l’étape 3, les 32,3 dernières cases (du 30 novembre au 31 décembre, plus trois dixièmes de la case du 29 novembre) prennent la couleur « financé par l’emprunt ». Barre « en % des dépenses publiques totales » : 91,2 % recettes, 8,8 % emprunt. Note de pastille : le déficit n’est pas égal à la hausse de la dette (ajustements stock-flux).

**Pastilles source** : [[fig:deficit_2025_eur_bn]] [[fig:deficit_2025_pct_gdp]] → Eurostat, notification d’octobre 2026 ; Insee. [[yard:share_te_borrowed_pct]] [[yard:borrowed_one_euro_in]] [[yard:deficit_days]] [[yard:borrowing_starts_day]] → calculs de la plateforme. [[fig:oecd_tax_to_gdp_2024_rank]] → OCDE, *Revenue Statistics 2025*, décembre 2025. Débat sur la dette, pastille texte : « F. Ecalle et F. Geerolf, “La dette publique est-elle vraiment alarmante ?”, *Le Monde*, 12 janvier 2025 » (https://fgeerolf.com/ofce/lemonde-20250112-1.pdf, consulté le 30 octobre 2026). Ecalle : « il me semble nécessaire de contrôler la dette ou, au moins, de parvenir à stabiliser son niveau en pourcentage du produit intérieur brut » ; Geerolf : « un tel effort est inutile car la dette va se stabiliser naturellement » ; tous deux : pas de problème à court terme.

---

## Étape 6. Quatrième étalon : si la France était un ménage

> Imaginons un ménage qui gagne **3 000 euros par mois** [[yard:household_monthly_income_eur]]. À la même échelle que les comptes publics de 2025, il dépenserait **3 291 euros par mois** [[yard:household_spending_month_eur]] et emprunterait donc **291 euros chaque mois** [[yard:household_borrowing_month_eur]].
>
> L’image a des limites dans les deux sens. Un État ne part pas à la retraite et ses recettes suivent la croissance. Il fixe lui-même ses impôts, et une partie de ses dépenses finance des investissements durables.
>
> Mais son emprunt n’est pas illimité. Comme un ménage, il paie des intérêts, à un prix fixé par les prêteurs. Le rôle de la Banque centrale européenne dans ce prix est débattu (chapitre 5).

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
> **2e sur 27** en 2025 [[fig:te_pct_gdp_eu_rank_2025]], derrière la Finlande : 57,5 % du PIB contre 57,3 % [[fig:finland_te_2025_pct_gdp]] [[fig:te_2025_pct_gdp]]. L’écart n’est que de 0,2 point [[calc:finland_te_2025_pct_gdp - te_2025_pct_gdp = 0,2]] : selon la date des données et la méthode, les deux pays échangent parfois leur place. La France était 1re chaque année de 2014 à 2023 [[fig:te_pct_gdp_eu_rank_2025|contexte]].
>
> Ce classement compare des tailles. Il ne dit pas si les services rendus, ou leur coût total pour les ménages, sont plus élevés qu’ailleurs.
>
> *Comparaison : les 27 pays de l’Union européenne (UE-27), données 2025, Eurostat, 21 octobre 2026. Le premier rang est celui de la dépense la plus élevée.*

**Interaction** : choix multiple (question Q14 de `quiz.json`), puis le graphique se construit.

**Visuel** : barres horizontales des 27 pays, triées ; France surlignée, Finlande en couleur secondaire, ligne ZE21. Axe « en % du PIB », 2025. Mention : « Le PIB de l’Irlande est gonflé par les multinationales : son ratio n’est pas comparable. » Jeu `eu27_te_pct_gdp_2025` à ajouter avant mise en ligne (voir points à trancher) ; le texte ne cite aucun autre pays que la Finlande.

**Pastilles source** : [[fig:te_pct_gdp_eu_rank_2025]] [[fig:finland_te_2025_pct_gdp]] → calcul de la plateforme d’après Eurostat (`gov_10a_main`, 21 octobre 2026). Places échangées selon la méthode : F. Ecalle, Fipeco, « Le rapport des dépenses publiques au PIB : pertinence et comparabilité », 15 janvier 2025 (https://fipeco.fr/pdf/D%C3%A9pensesPIB2025.pdf, consulté le 30 octobre 2026) : en neutralisant certains doubles comptes, « la France et la Finlande échangent la première et la deuxième place » (données 2023). Selon la revue du 30 octobre 2026, le FMI (Article IV, 21 mai 2026) place la France 1re de la zone euro pour 2025 ; page non ouverte par ce chapitre (accès refusé), donc non citée.

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
> Ces images comparent des tailles : ce n’est pas un objectif d’économies. Pour les économistes de l’OFCE, le poids de la dépense relève « avant tout » d’un « choix de société ». Pour Fipeco, la bonne question est de savoir si chaque dépense vaut plus que les prélèvements qui la financent.
>
> L’écart a culminé à 10,4 points en 2017 [[fig:spending_gap_ea21_2017_pp]]. Jusqu’en 2019, il a baissé surtout parce que la dépense française a reculé. Depuis, la dépense a augmenté partout, mais plus vite dans l’ensemble de la zone euro qu’en France.
>
> Une raison comptable a pu jouer. Le crédit d’impôt pour la compétitivité et l’emploi (CICE), compté en dépense, a laissé place en 2019 à une baisse de cotisations. Son effet exact est difficile à isoler.
>
> *Comparaison : ZE21, données 2025, Eurostat. La ZE21 comprend la France : sans elle, la moyenne serait plus basse et l’écart plus grand. Avec la zone euro à 20 pays de 2025 (ZE20) : 7,5 points, soit 225 milliards d’euros [[fig:spending_gap_ea20_2025_pp]] [[fig:spending_gap_ea20_2025_eur_bn]].*

**Visuel** : courbe de l’écart France moins ZE21, en points de PIB, 2005-2025 (série de `research/data/09_intl_fr_gap_timeseries.csv`, à ajouter aux données). Points étiquetés : 2005 (7,1 [[fig:spending_gap_ea21_2005_pp]]), 2017 (10,4, « pic »), 2024 (7,8 [[fig:spending_gap_ea21_2024_pp]]), 2025 (7,6). Annotations sans chiffre : crise financière (2008), Covid (2020), choc énergétique (2022), CICE (2017-2019). Puis la barre « 227 Md€ » devient trois cartes d’étalon, étiquette « illustratif ».

**Pastilles source** : [[fig:spending_gap_ea21_2025_pp]] [[fig:spending_gap_ea21_2025_eur_bn]] [[fig:ea21_te_2025_pct_gdp]] [[yard:one_point_gdp_eur_bn]] → calcul de la plateforme d’après Eurostat (`gov_10a_main`, `nama_10_gdp`). Réduction de l’écart depuis 2017 : research/data/09_intl_fr_gap_timeseries.csv (Eurostat, 21 octobre 2026 : France 57,7 % en 2017, 55,3 % en 2019, 57,3 % en 2025 ; ZE21 47,3 %, 46,9 %, 49,7 %), pas de chiffre affiché. CICE : F. Ecalle, Fipeco, « Les principales réformes fiscales du quinquennat », 27 janvier 2022 (remplacement par une baisse de cotisations au 1er janvier 2019) ; Insee, « Les comptes des administrations publiques en 2019 », 25 mars 2020 (dépense « quasiment stable » en 2019 : effet non visible sur la seule année 2019, d’où « difficile à isoler »). « Choix de société » : B. Ducoudré, M. Plane, R. Sampognaro, OFCE, *Policy Brief* n° 17, 19 avril 2017, conclusion (https://www.ofce.fr/pdf/pbrief/2017/pbrief17.pdf, consulté le 30 octobre 2026). « La question pertinente […] est de savoir si ces dépenses ont une utilité supérieure au coût des prélèvements obligatoires nécessaires pour les financer » : F. Ecalle, Fipeco, 15 janvier 2025 (même URL qu’à l’étape 7). ZE21 comprenant la France : constat de définition, sans chiffre (variante hors France publiée par la Banque de France, *Bulletin* n° 259, 25 juillet 2025, non ouverte par ce chapitre : accès refusé).

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
>
> Ce résultat se lit de deux façons : un choix de financement public plutôt que privé, ou un poids à couvrir par des prélèvements (étape 12).

**Interaction** : choix multiple (Q25 de `quiz.json`, codée « droite » ; équilibrée par l’affirmation B de l’étape 10).

**Visuel** : barre empilée de 7,8 points (« en points de PIB, écart avec la ZE21, 2024 ») : vieillesse 2,5 ; reste de la protection sociale 1,1 ; santé 1,5 ; autres fonctions 2,7 (gris). En survol, la part « en % de l’écart total » (vieillesse 32 % ; protection sociale, vieillesse comprise, 46 % ; santé 19 %). Bandeau : « Données 2024. Ventilation 2025 attendue en décembre 2026 (Insee) et vers février 2027 (Eurostat). » Données : `gap2024_social_protection_pp`, `gap2024_health_pp`, `gap2024_social_protection_share`, `gap2024_health_share`.

**Pastilles source** : [[fig:spending_gap_ea21_2024_pp]] [[fig:gap2024_sp_plus_health_pp]] [[fig:gap2024_old_age_pp]] [[fig:gap2024_old_age_share]] → calcul de la plateforme d’après Eurostat (`gov_10a_exp`).

---

## Étape 10. Deux affirmations à l’épreuve des ordres de grandeur

> On entend dans le débat deux affirmations opposées. Même gabarit pour les deux.
>
> **Affirmation A : « L’écart vient surtout des salaires et des effectifs publics. »**
>
> Ce qui est exact : la rémunération des agents publics représente 12,4 % du PIB en France contre 10,0 % dans la zone euro en 2025 [[fig:compensation_employees_2025_pct_gdp]] [[fig:ea21_compensation_employees_2025_pct_gdp]]. L’écart est de 2,4 points de PIB [[calc:compensation_employees_2025_pct_gdp - ea21_compensation_employees_2025_pct_gdp = 2,4]], soit environ 72 milliards d’euros par an [[calc:(compensation_employees_2025_pct_gdp - ea21_compensation_employees_2025_pct_gdp) × one_point_gdp_eur_bn = 71,8]].
>
> C’est environ un tiers de l’écart total de dépense [[calc:(compensation_employees_2025_pct_gdp - ea21_compensation_employees_2025_pct_gdp) / spending_gap_ea21_2025_pp × 100 = 31,6]], à peu près autant que la vieillesse (étape 9). La Cour des comptes (juridiction financière) y voit un levier d’économies (chapitre 6). La Fondation iFRAP (libérale) propose de réduire l’emploi public pour combler une partie de l’écart avec le reste de la zone euro.
>
> Ce qui ne tient pas : le mot « surtout ». Le reste de l’écart vient d’autres dépenses, d’abord sociales (étape 9). Cette masse salariale couvre aussi les collectivités locales et les hôpitaux, pas seulement l’État. Elle paie notamment des soignants et des enseignants. Ces derniers sont moins payés que la moyenne de l’OCDE (chapitre 6).
>
> Enfin, en 2025, les salaires bruts rapportés au PIB sont sous la médiane de l’UE. L’écart tient surtout aux cotisations des employeurs publics, dont le financement des retraites des fonctionnaires.
>
> Pour le nombre d’agents, tout dépend du périmètre. Face au reste de la zone euro, la Fondation iFRAP en trouve nettement plus en France (2019). Face à l’OCDE, la France est un peu au-dessus de la moyenne selon l’OCDE (2023), un peu en dessous selon l’OFCE (2017).
>
> **Affirmation B : « La France ne dépense pas plus que ses voisins. »**
>
> Ce qui est exact : par habitant, en tenant compte des prix, la France n’est que 8e sur 27 [[fig:te_per_capita_pps_2025_rank]] (encadré ci-dessous). Et une partie de l’écart tient à des retraites et des soins payés ici par des caisses publiques, ailleurs par le privé (étape 12).
>
> Ce qui ne tient pas : rapportée au PIB, sa dépense est la 2e de l’UE [[fig:te_pct_gdp_eu_rank_2025]]. Elle dépasse de 7,6 points de PIB celle de la zone euro [[fig:spending_gap_ea21_2025_pp]]. Or le PIB mesure la base des prélèvements obligatoires qui paient ces dépenses (étape 12).
>
> Chacune contient une part de vrai ; aucune ne résume seule la situation.

**Visuel** : deux cartes côte à côte, même taille, même gabarit, aucune étiquette de parti ; ordre tiré au hasard à chaque chargement. Carte A : mini-barres « rémunération des salariés publics, en % du PIB, 2025 » (France 12,4 / ZE21 10,0), mention « écart : 2,4 points, environ 72 Md€ », et note « Les découpages par nature et par fonction se recoupent : on ne peut pas additionner leurs écarts. » Carte B : renvoi vers la bascule de l’étape 11.

**Pastilles source** : [[fig:compensation_employees_2025_pct_gdp]] [[fig:ea21_compensation_employees_2025_pct_gdp]] → Eurostat, `gov_10a_main`, 21 octobre 2026. [[yard:one_point_gdp_eur_bn]] [[fig:spending_gap_ea21_2025_pp]] → calculs de la plateforme (conversion en milliards et part de l’écart). Salaires bruts (D.11) sous la médiane de l’UE et poids des cotisations employeurs, dont cotisations imputées de retraite : research/04, §4 (K16, Eurostat `gov_10a_main`, calcul). Enseignants moins payés que la moyenne de l’OCDE : research/04, §6.1.2 (OCDE, *Regards sur l’éducation 2026*, tableau D3.1). Emploi public un peu au-dessus de la moyenne de l’OCDE : research/04, K18 (OCDE, *Government at a Glance 2025*, fig. 13.1, données 2023 : France 20,7 % de l’emploi total, moyenne OCDE 18,4 %). Un peu en dessous : B. Ducoudré, M. Plane, R. Sampognaro, OFCE, *Policy Brief* n° 17, 19 avril 2017, résumé (« 20 % de l’emploi total, soit un niveau légèrement inférieur à celui de la moyenne de l’OCDE », tous contrats). Fondation iFRAP : S. Gorreri, S.-F. Servière, « Effectifs publics : 1 million d’agents par rapport à la zone euro », 2 février 2022 (https://www.ifrap.org/fonction-publique-et-administration/effectifs-publics-1-million-dagents-par-rapport-la-zone-euro, consulté le 30 octobre 2026) : comparaison avec le reste de la zone euro (18 pays), données 2019, écart de dépenses de personnel de 2,98 points de PIB, ou 1,75 point pour les rémunérations du secteur non marchand ; propose des « correctifs de baisse de l’emploi public » pour « entre 10 % et 15 % de ces écarts ». Aucun de ces chiffres n’est affiché (pas d’identifiant dans platform/data). Cour des comptes, levier de la masse salariale : research/04, §8 (note de septembre 2026). Pas de nouveau chiffre affiché pour ces quatre points. [[fig:te_per_capita_pps_2025_rank]] → calcul de la plateforme d’après Eurostat (`nama_10_pc`, 22 octobre 2026).

---

## Étape 11. Encadré « Le meilleur contre-argument »

<!-- box-side: gauche -->
> **Le meilleur contre-argument**
>
> **« Le ratio au PIB exagère l’écart. Par habitant, la France ne dépense pas plus que plusieurs voisins. Et la hausse du ratio depuis 2008 tient surtout à la faible croissance. »**
>
> Le premier argument repose sur un calcul de la plateforme. Mesurons la dépense en standards de pouvoir d’achat (SPA), une unité qui corrige les écarts de prix entre pays. La dépense publique atteint alors **23 330 SPA par habitant** en France en 2025 [[fig:te_per_capita_pps_2025]].
>
> La France se classe **8e sur 27**, pratiquement à égalité avec la Suède [[fig:te_per_capita_pps_2025_rank]] : sept pays dépensent davantage par habitant [[calc:te_per_capita_pps_2025_rank - 1 = 7]], dont l’Allemagne et les Pays-Bas.
>
> Le second argument vient d’économistes de l’OFCE, dans une note d’avril 2017. Selon eux, la dépense a beaucoup ralenti après la crise de 2008. Si son poids dans le PIB a augmenté, c’est « avant tout » parce que la croissance s’est affaissée. Pour eux, ce poids reflète d’abord le modèle social et fiscal du pays.
>
> *Sources : calcul de la plateforme d’après Eurostat (office statistique de l’Union européenne ; `nama_10_pc`, 22 octobre 2026) ; B. Ducoudré, M. Plane, R. Sampognaro, « Dépenses publiques : quels enjeux pour le prochain quinquennat ? », OFCE (Sciences Po, sensibilité keynésienne),* Policy Brief *n° 17, 19 avril 2017.*
>
> **Ce qu’on peut répondre**
>
> Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire) rappelle que le PIB est la base des impôts. Avec moins de revenu par habitant, financer la même dépense par habitant demande des prélèvements plus élevés.
>
> Quant au dénominateur, de 2005 à 2025, la dépense a gagné **+3,0 points de PIB** [[fig:te_change_2005_2025_pp]], d’après Eurostat. Les recettes ont gagné **+1,4 point de PIB** [[fig:total_revenue_change_2005_2025_pp]]. Les deux ratios ont pourtant le même dénominateur. La faible croissance compte donc, mais n’explique pas toute la hausse de la dépense.
>
> Cette période commence avant la crise de 2008, alors que la note de l’OFCE porte sur les années suivantes.
>
> Les deux chiffres répondent donc à deux questions différentes. Par habitant : quel volume de services et de prestations reçoit-on ? En % du PIB : quel effort faut-il pour les financer ?
>
> *Sources : F. Ecalle, « Le rapport des dépenses publiques au PIB : pertinence et comparabilité », Fipeco (site indépendant, ancien magistrat de la Cour des comptes, orthodoxie budgétaire), 15 janvier 2025 ; calcul de la plateforme d’après Eurostat (`gov_10a_main`, 21 octobre 2026).*

**Visuel** : sur le même écran que les étapes 7 à 10, jamais replié (glossaire §4.6). Le graphique de l’étape 7 reçoit une bascule « en % du PIB » ↔ « en SPA par habitant » ; la barre de la France glisse de la 2e à la 8e place (600 ms, sans animation si « réduire les animations »). Suède marquée « pratiquement à égalité ». Pas de rang 2024 en SPA sans mention (8e ou 9e selon la méthode). Valeurs SPA des 26 autres pays à ajouter avant mise en ligne. La liste complète des sept pays (research/01) peut figurer dans le graphique, pas dans le texte.

**Pastilles source** : [[fig:te_per_capita_pps_2025]] [[fig:te_per_capita_pps_2025_rank]] → calcul de la plateforme : dépense / PIB × PIB par habitant en SPA, Eurostat (`nama_10_pc`, 22 octobre 2026). OFCE, *Policy Brief* n° 17 (2017), pastille de financement : « Financé par une subvention publique versée par l’État à la Fondation nationale des sciences politiques (site de l’OFCE). » (https://www.ofce.fr/ofce/statuts.html, glossaire §1.13) ; Fipeco (15 janvier 2025), pas de pastille de financement (non détaillé sur son site). OFCE, passages repris (https://www.ofce.fr/pdf/pbrief/2017/pbrief17.pdf, consulté le 30 octobre 2026) : « Le poids important de la dépense publique française s’explique d’abord par son modèle social et fiscal » ; rythme de croissance de la dépense « divisé par deux par rapport à la période avant-crise » ; « Si le poids de la dépense publique s’est accru de près de 5 points de PIB depuis 2008, cela s’explique avant tout par l’affaissement de la croissance depuis la crise ». La note ne fait aucune comparaison par habitant : l’argument par habitant n’est pas attribué à l’OFCE. Réponse sur le dénominateur : [[fig:te_volume_growth_avg_2005_2025_pct]] retiré du texte affiché le 30 octobre 2026 (le même tableau du Haut-commissariat à la Stratégie et au Plan donne aussi 1,4 % par an pour les recettes : ce chiffre seul ne montre pas que la dépense a dépassé les recettes) ; [[fig:te_change_2005_2025_pp]] [[fig:total_revenue_change_2005_2025_pp]] (Eurostat `gov_10a_main`, 21 octobre 2026 ; research/10 §4.2).

---

## Étape 12. Une autre objection : public ou privé ?

> En France, retraites et santé passent surtout par des caisses publiques ; ailleurs, davantage par des assurances privées. Pour les économistes de l’OFCE (2017), il faut donc comparer à service égal.
>
> Leur exemple : aux États-Unis, la dépense publique de retraite et de santé est bien plus faible qu’en France. Mais, dépenses privées comprises, la dépense totale y est plus élevée.
>
> Fipeco répond que la différence reste importante. Une dépense publique est payée par des prélèvements obligatoires, que les ménages n’ont pas le choix de payer ou non. Le chapitre 2 mesure le poids de chaque argument.

**Pastilles source** : pastilles texte, sans chiffre affiché. OFCE : B. Ducoudré, M. Plane, R. Sampognaro, *Policy Brief* n° 17, 19 avril 2017, résumé : « les dépenses publiques de retraite et santé sont aux États-Unis 8 points de PIB inférieures à celles de la France, mais les dépenses totales de retraite et santé, incluant les dépenses privées, sont 2 points de PIB supérieures » (https://www.ofce.fr/pdf/pbrief/2017/pbrief17.pdf, consulté le 30 octobre 2026). Fipeco : F. Ecalle, 15 janvier 2025 : « La comparaison des seules dépenses publiques est néanmoins pertinente car il s’agit des dépenses financées par des PO, pour lesquels les ménages ont, par définition, un choix très limité » ; services publics financés par des prélèvements « que ceux-ci n’ont pas le choix de payer ou non » (https://fipeco.fr/pdf/D%C3%A9pensesPIB2025.pdf, consulté le 30 octobre 2026).

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
> - 2e de l’UE en % du PIB, au coude-à-coude avec la Finlande, mais 8e par habitant en pouvoir d’achat [[fig:te_pct_gdp_eu_rank_2025]] [[fig:te_per_capita_pps_2025_rank]]. Le choix de la mesure est lui-même débattu.
> - Environ les deux tiers de l’écart avec la zone euro viennent de la protection sociale et de la santé (2024) [[calc:gap2024_sp_plus_health_pp / spending_gap_ea21_2024_pp × 100 = 65,4]].
>
> **Pour aller plus loin**
> - Fiche « Vue d’ensemble des dépenses » : l’évolution de l’écart avec la zone euro depuis 2005, année par année.
> - Espace confiance, page Méthode : comptabilité nationale et comptabilité budgétaire, crédits d’impôt, SPA.
> - Page Débats : tous les contre-arguments sur la taille de la dépense, avec auteurs et orientations.
>
> **La suite.** Savoir combien on dépense ne dit pas à quoi sert l’argent. Le chapitre 2, « Où va l’argent ? », répartit ces 1 714,1 milliards [[fig:te_2025_eur_bn]] jour par jour sur le calendrier de l’année.

**Visuel** : carte récapitulative partageable (quatre étalons en icônes : jour, habitant, déficit, ménage ; chaque chiffre garde sa pastille sur le web). Boutons « Chapitre 2 : Où va l’argent ? » (principal) et « Comparer avec l’Europe » (secondaire, préréglé « dépenses publiques, % du PIB, 2025, UE-27 »). Le calendrier de l’étape 5 sert de transition vers celui du chapitre 2. Liens « Pour aller plus loin » : fiche §4.1, Méthode (§4.17), Débats, comparateur (fr/20-approche-pedagogique.md §2.1).

**Pastilles source** : reprises des étapes 1, 3, 5, 7, 9 et 11.

---

<!--
LISTE DES IDENTIFIANTS UTILISÉS (contrôle)
figures.json : te_2025_eur_bn, te_2025_pct_gdp, cash_social_benefits_2025_pct_gdp, te_per_capita_2025_eur, deficit_2025_eur_bn, deficit_2025_pct_gdp, total_revenue_2025_eur_bn, te_pct_gdp_eu_rank_2025, finland_te_2025_pct_gdp, ea21_te_2025_pct_gdp, spending_gap_ea21_2025_pp, spending_gap_ea21_2025_eur_bn, spending_gap_ea20_2025_pp, spending_gap_ea20_2025_eur_bn, spending_gap_ea21_2005_pp, spending_gap_ea21_2017_pp, spending_gap_ea21_2024_pp, gap2024_sp_plus_health_pp, gap2024_social_protection_pp, gap2024_old_age_pp, gap2024_old_age_share, gap2024_health_pp, gap2024_social_protection_share, gap2024_health_share, compensation_employees_2025_pct_gdp, ea21_compensation_employees_2025_pct_gdp, te_per_capita_pps_2025, te_per_capita_pps_2025_rank, te_excl_tax_credits_2025_pct_gdp, te_excl_tax_credits_2026f_pct_gdp, te_excl_tax_credits_2027f_pct_gdp, population_2025_m, oecd_tax_to_gdp_2024_rank, te_change_2005_2025_pp, total_revenue_change_2005_2025_pp (te_volume_growth_avg_2005_2025_pct : pastille seulement, retiré du texte affiché le 30 octobre 2026).
yardsticks.json : one_day_spending_eur_bn, one_point_gdp_eur_bn, te_per_capita_per_day_eur, share_te_borrowed_pct, borrowed_one_euro_in, deficit_days, borrowing_starts_day, household_spending_month_eur, household_borrowing_month_eur ; paramètres household_monthly_income_eur, days_in_year.

POINTS À TRANCHER AVANT PUBLICATION
1. Jeux de données à ajouter (propriétaire : données) : valeurs 2025 des 27 pays en % du PIB et en SPA par habitant (étapes 7 et 11) ; série 2005-2025 de l’écart avec la ZE21 (étape 8).
2. finland_te_2025_pct_gdp porte l’année « 2024-2025 » alors que 57,5 % est la valeur 2025 : corriger le champ year dans figures.json.
3. Q25 de quiz.json : l’option « L’administration et le train de vie » doit devenir « Les dépenses de fonctionnement de l’État » (glossaire). Toujours non fait au 25 octobre 2026.
4. Les trois conversions de l’étape 8 et les « deux tiers » de l’étape 9 sont des [[calc:]] : si l’on préfère des étalons versionnés, créer dans yardsticks.json spending_gap_ea21_days, spending_gap_ea21_deficit_ratio, spending_gap_ea21_per_capita_eur et gap2024_sp_plus_health_share.
5. LISEZMOI-site.md (§5.1, point 2, et tableau des chapitres : 5 548 mots) est à mettre à jour par son propriétaire : titre tranché, nouvelle longueur.
7. Chiffres demandés par la confrontation aux sources publiques du 30 octobre 2026 (propriétaire : données ; non affichés faute d’identifiant) : voir la note de relecture du 30 octobre 2026, liste « Chiffres manquants ».
6. Étape 11, réponse sur le dénominateur (propriétaire : données) : créer te_volume_growth_avg_2005_2025_pct (HCSP, 1,4 % par an), te_change_2005_2025_pp et total_revenue_change_2005_2025_pp (research/10 §4.2), puis remplacer la formulation qualitative par les chiffres avec pastilles. Facultatif : une figure D.11 (salaires bruts, % du PIB, France et médiane UE) pour chiffrer l’étape 10.
-->

---

## Notes de relecture

### Confrontation aux sources publiques (2026-10-30)

Textes rouverts par cette passe (PDF ou page téléchargés le 30 octobre 2026, passages cités vérifiés mot pour mot) : OFCE, *Policy Brief* n° 17, 19 avril 2017 ; F. Ecalle, Fipeco, « Le rapport des dépenses publiques au PIB : pertinence et comparabilité », 15 janvier 2025 ; F. Ecalle et F. Geerolf, *Le Monde*, 12 janvier 2025 (copie https://fgeerolf.com/ofce/lemonde-20250112-1.pdf) ; Fondation iFRAP, « Effectifs publics : 1 million d’agents par rapport à la zone euro », 2 février 2022. Pages refusées (non citées) : Banque de France, *Bulletin* n° 259 ; FMI, déclaration de fin de mission Article IV du 21 mai 2026. Institut Montaigne, Rexecode et Observatoire des inégalités : non rouverts, donc non cités dans le texte.

**Points de la revue (verdicts partly_supported, not_supported, missing_counterargument)**
- 01-combien-02 (transferts) : **corrigé**. Étape 2 : « passe par les caisses publiques, puis revient aux ménages » (image circulaire) remplacé par « est versé aux ménages » ; périmètre du 19,4 % précisé (argent versé seulement, ni soins remboursés ni services) ; financement « souvent payé par d’autres personnes que celles qui les reçoivent » (Fipeco). Ajout « ou consomment » (point 01 : 57 % n’est pas ce que l’État consomme).
- 01-combien-03 (journée de dépense) : **sans changement** ; déjà présenté comme un étalon de la plateforme. La sensibilité à la définition (HCFP hors crédits d’impôt) reste expliquée à l’étape 13.
- 01-combien-04 (par habitant) : **corrigé** par le récapitulatif (« Le choix de la mesure est lui-même débattu ») et par l’encadré (Fipeco, prudence sur les comparaisons par habitant). L’étape 4 reste descriptive, avec sa mise en garde « moyenne ».
- 01-combien-05 (déficit) : **corrigé**. « Les recettes n’ont pas suffi » devient « les dépenses ont dépassé les recettes » ; ajout du débat Ecalle / Geerolf (accord sur le court terme ; stabiliser la dette contre effort « inutile », la dette se stabilisant « naturellement »), *Le Monde*, 12 janvier 2025. La phrase d’introduction du journaliste (« réduction des dépenses sociales » inévitable) n’est pas attribuée à Ecalle : ce n’est pas sa citation.
- 01-combien-06 (ménage à 3 000 €) : **sans changement** ; illustration éditoriale déjà étiquetée « illustratif » et « choix éditorial ». Ajout dans les limites : « son emprunt n’est pas illimité » ; rôle de la Banque centrale européenne « débattu » (chapitre 5).
- 01-combien-08 (rang UE) : **corrigé**. Étape 7 : « L’écart n’est que de 0,2 point » (`[[calc:]]`) et « selon la date des données et la méthode, les deux pays échangent parfois leur place » (Fipeco : doubles comptes neutralisés, données 2023). Phrase « la Finlande est passée devant en 2024 » retirée (redondante). Récapitulatif : « au coude-à-coude avec la Finlande ».
- 01-combien-10 (missing_counterargument) : **contre-argument ajouté** à l’étape 8 : « ce n’est pas un objectif d’économies » ; OFCE (« avant tout » un « choix de société », conclusion du *Policy Brief* n° 17) et, en face, Fipeco (une dépense doit valoir plus que les prélèvements qui la financent). L’effet récessif chiffré (−0,9 % du PIB) n’est pas ajouté : pas d’identifiant de données.
- 01-combien-11 (réduction de l’écart, CICE) : **corrigé**. Deux temps distingués (série Eurostat du 21 octobre 2026, research/data/09) : de 2017 à 2019, recul de la dépense française ; depuis 2019, hausse plus rapide dans la zone euro. CICE : « a pu jouer », « effet exact difficile à isoler » (Insee 2019 : dépense quasi stable cette année-là).
- 01-combien-13 et 14 (masse salariale, emploi public) : **corrigé**. Affirmation A reformulée (« salaires et effectifs publics ») ; proposition de la Fondation iFRAP (libérale) ajoutée ; nombre d’agents selon le périmètre : nettement plus que le reste de la zone euro (iFRAP, 2019), un peu au-dessus de la moyenne de l’OCDE (OCDE, 2023), un peu en dessous (OFCE, 2017).
- 01-combien-17 (encadré) : **corrigé**. Thèse scindée en deux arguments ; l’argument par habitant est présenté comme « un calcul de la plateforme » ; l’OFCE n’est crédité que de ce qu’il a publié (ralentissement de la dépense, hausse du ratio « avant tout » due à la croissance, poids expliqué d’abord par le modèle social et fiscal), avec la date (avril 2017).
- 01-combien-18 (23 330 SPA, 8e) : **corrigé** dans la présentation : calcul de la plateforme dit dans le texte, non attribué à une source publiée. Valeurs inchangées (non contredites).
- 01-combien-20 (1,4 % par an) : **corrigé**. Chiffre du Haut-commissariat à la Stratégie et au Plan retiré du texte affiché : le même tableau donne 1,4 % par an pour les recettes. Reste la comparaison Eurostat +3,0 / +1,4 points, avec la mention que la période commence avant 2008.

**Critiques de gauche (9)**
- G1 (étape 12 réduite à un renvoi) : **appliqué**. Étape 12 : position de l’OFCE (comparer à service égal ; exemple des États-Unis, sans chiffre) puis réponse de Fipeco (prélèvements obligatoires, choix très limité des ménages).
- G2 (affirmation B réfutée dans sa version faible) : **appliqué**. « Ce qui est exact » inclut l’argument public / privé ; « Ce qui ne tient pas » y répond (le PIB mesure la base des prélèvements, étape 12).
- G3 (encadré attribuant à l’OFCE une thèse par habitant) : **appliqué**, sauf un point **rejeté** : retirer « sensibilité keynésienne ». Raison : étiquette imposée mot pour mot par le glossaire §1.13 (décision D-labels) pour toute mention de l’OFCE, pas un choix propre à cet encadré.
- G4 (fenêtre 2005-2025, chiffre de 1,4 %) : **appliqué** (chiffre retiré ; fenêtre signalée ; ralentissement après 2008 dit dans la thèse). Fenêtre 2008-2025 non affichée : chiffre manquant.
- G5 (conversions de l’écart lues comme des économies) : **appliqué** (étape 8).
- G6 (composition de l’écart sans interprétation) : **appliqué** (une phrase à l’étape 9, renvoi à l’étape 12).
- G7 (rang sans mise en garde) : **appliqué** (étape 7, phrase complète ; récapitulatif, forme courte). L’Observatoire des inégalités n’est pas cité : texte non rouvert et pas d’étiquette dans le glossaire §1.13 ; le raisonnement est repris sans attribution.
- G8 (emploi public et OCDE sans année ni périmètre) : **appliqué** (années et périmètres, OCDE 2023 et OFCE 2017).
- G9 (déficit présenté sous un seul angle) : **appliqué** (débat Ecalle / Geerolf ; Banque centrale européenne dans les limites du ménage).

**Critiques de droite (10)**
- D1 (« les recettes n’ont pas suffi ») : **appliqué** (formulation neutre ; contexte des prélèvements : 2e de l’OCDE pour le taux de prélèvement en 2024, `oecd_tax_to_gdp_2024_rank`). L’écart de prélèvements avec la zone euro (Rexecode, iFRAP) n’est pas affiché : textes non rouverts, pas d’identifiant.
- D2 (objection public / privé sans réponse) : **appliqué** (réponse de Fipeco à l’étape 12 et dans l’affirmation B).
- D3 (rang par habitant mis à égalité) : **appliqué en partie** (récapitulatif et affirmation B). **Rejeté** : retirer le rang par habitant du récapitulatif. Raison : les deux rangs sont des faits vérifiés, la critique de gauche demande de garder l’argument, et la mention « le choix de la mesure est débattu » suffit.
- D4 (0,2 point, France 1re selon d’autres sources) : **appliqué en partie** (écart de 0,2 point, places échangées selon la méthode). **Rejeté** : « d’autres sources placent la France 1re ». Raison : la page du FMI n’a pas pu être ouverte ; le texte de Fipeco ouvert dit l’inverse pour la méthode corrigée (la France passe 2e derrière la Finlande, données 2023). Le rang 1er de 2014 à 2023 reste affiché.
- D5 (affirmation A, « surtout », comparateurs) : **appliqué en partie** (slogan précisé, proposition iFRAP, comparateurs explicités). **Rejeté** : retirer « surtout » de A, et déclarer aussi « ce qui ne tient pas » pour la vieillesse. Raisons : le gabarit teste une affirmation entendue dans le débat, dont « surtout » est le cœur ; la version précise de l’iFRAP figure désormais dans « Ce qui est exact ». La vieillesse n’est pas une affirmation du débat ; la page dit déjà que les deux pèsent environ un tiers.
- D6 (ZE21 comprenant la France) : **appliqué** (phrase sans chiffre dans la note de comparaison). Écart hors France : chiffre manquant.
- D7 (contexte du déficit, limites du ménage) : **appliqué** (débat Ecalle / Geerolf ; « son emprunt n’est pas illimité »). « Déficit le plus élevé de la zone euro » (Institut Montaigne) non ajouté : texte non rouvert, pas d’identifiant.
- D8 (transferts « circulaires », 19,4 %) : **appliqué** (voir point 02). Part de la protection sociale dans la dépense totale : chiffre manquant.
- D9 (réponse de l’encadré trop mince) : **appliqué** (chiffre de 1,4 % retiré, fenêtre signalée). Second texte libéral sur le dénominateur non ajouté : aucun texte ouvert ne traite ce point.
- D10 (CICE et réduction de l’écart) : **appliqué** (voir point 11).

**Chiffres manquants (à créer dans platform/data avant de les afficher)**
1. Écart de prélèvements obligatoires France / zone euro, en points de PIB (Eurostat ; Rexecode, *Document de travail* n° 97 ; Fondation iFRAP, 14 janvier 2025), pour l’étape 5.
2. Rang de la France pour le déficit 2025 dans la zone euro (Eurostat, notification d’octobre 2026), pour l’étape 5.
3. Écart de dépense avec la zone euro hors France, 2025 (Eurostat ; ou Banque de France, *Bulletin* n° 259 : 9,3 points en 2023), pour l’étape 8.
4. Variation de la dépense et des recettes en points de PIB depuis 2008 (ou 2010) jusqu’en 2025 (Eurostat `gov_10a_main`), pour l’encadré.
5. Croissance annuelle moyenne des recettes en volume, 2005-2025 (Haut-commissariat à la Stratégie et au Plan, 1,4 % par an), si le chiffre de la dépense en volume revient dans le texte.
6. Part de la protection sociale dans la dépense publique totale (Eurostat COFOG ; Institut Montaigne : 56 euros sur 100), et part « services et investissements », pour l’étape 2 et son visuel.
7. Écarts iFRAP de dépenses de personnel avec le reste de la zone euro (2,98 et 1,75 points de PIB, 2019), si on veut les afficher à l’étape 10.

**Longueur et contrôles** : texte affiché 1 770 → 2 164 mots (cible 1 500-2 200) ; durée de lecture « environ 9 minutes ». Coupes pour compenser : phrases d’amorce (étapes 1, 3, 12), ligne « Outil Comparer avec l’Europe » de « Pour aller plus loin », reformulations. `python3 -I validate.py --strict` : 0 erreur pour ce fichier. Un avertissement demeure : « first mention of Cour des comptes » (étape 5). Faux positif du validateur : le nom figure dans l’étiquette de Fipeco (« ancien magistrat de la Cour des comptes ») ; la Cour elle-même est citée avec son étiquette à l’étape 10. À corriger dans validate.py (propriétaire : données), pas dans ce chapitre.

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
