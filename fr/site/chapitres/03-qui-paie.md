# Chapitre 3. Qui paie ?

<!--
NOTE ÉDITORIALE (non affichée sur le site)

- Statut : brouillon pour relecture éditoriale et contradictoire. Rédigé le 25 octobre 2026 ; passe « chapitres » (intégration des nouvelles entrées et réduction) le même jour ; passe de finalisation le même jour.
- Place dans le récit : chapitre 3 sur 7 (fichier 20, §2.1). Précédent : ch. 2 « Où va l’argent ? ». Suivant : ch. 4 « Pourquoi le déficit ? ».
- Sources des chiffres : uniquement `platform/data/figures.json`, `yardsticks.json` et `quiz.json` (millésime du 25 octobre 2026, seconde passe de données). Aucun chiffre ajouté de mémoire.
- Pastilles : `[[fig:id]]` = figures.json ; `[[yard:id]]` = étalon ou paramètre de yardsticks.json ; `[[quiz:id]]` = idée reçue de quiz.json ; `[[calc:formule]]` = calcul de la plateforme (mention « illustratif »).
- Libellé de l’interaction : « Estimez d’abord » (glossaire, §1.13).
- Fiche thématique suivie : fichier 20, §4.7 ; nuances : fichiers 05, 14 (§7.1), 18 (§1).
- Volume du texte visible : 2 129 mots après la passe de finalisation du 25 octobre 2026 (2 065 avant, mesure de `validate.py`), mesuré par script (titre, blocs affichés, questions ; hors spécifications, pastilles, notes). Durée de lecture affichée : environ 9 minutes (2 129 / 240 mots par minute). Voir les notes de relecture.
-->

---

## Étape 0. Ouverture

**Texte affiché**

> ### Qui paie ?
>
> Chaque année, l’État, la Sécurité sociale et les collectivités locales prélèvent une partie de la richesse produite en France, le produit intérieur brut (PIB). Taxe sur la valeur ajoutée (TVA), contribution sociale généralisée (CSG), impôt sur le revenu, cotisations sociales : tout cela forme les **prélèvements obligatoires**.
>
> Avant de voir les chiffres, faites une estimation.
>
> Durée de lecture : environ 9 minutes.

**Interaction « Estimez d’abord »**

- Question : « Selon vous, quelle part de la richesse produite en France (le PIB) passe par les prélèvements obligatoires en 2025 ? »
- Curseur 0-100 % du PIB, pas de 1, départ à 50. Médiane des visiteurs affichée quand l’échantillon suffit (sinon « Pas encore assez de réponses »).
<!-- estimez-réponse: po_2025_pct_gdp (affichée à l’étape 1) -->

**Visuel** : 100 pièces (= 100 € de PIB), aucune colorée avant la réponse.

---

## Étape 1. La réponse : 43,6 % du PIB

**Texte affiché**

> En 2025, les prélèvements obligatoires représentent **43,6 % du PIB** [[fig:po_2025_pct_gdp]], soit **1 305 milliards d’euros** [[fig:po_2025_eur_bn]]. Sur 100 € de richesse produite, 43,6 € passent par les impôts ou les cotisations sociales [[fig:po_2025_pct_gdp]].
>
> Ce chiffre de l’Institut national de la statistique et des études économiques (Insee) compte les impôts et les cotisations sociales, **après déduction des crédits d’impôt**.

**Visuel** : les pièces se colorent jusqu’à 43,6 ; repère « Votre estimation : X % du PIB » et écart en points. Axe « en % du PIB ».

**Pastilles source** : [[fig:po_2025_pct_gdp]] [[fig:po_2025_eur_bn]] – Insee, *Insee Première* n° 2106, 29 mai 2026 ; série « Taux de prélèvements obligatoires rapportés au produit intérieur brut », 28 août 2026. Mention : mesuré.

---

## Étape 2. Ce que cela représente

**Texte affiché**

> **Par habitant**, cela fait environ **18 900 € par an** [[yard:po_per_capita_eur]]. C’est une moyenne : le total, y compris ce que paient les entreprises, divisé par le nombre d’habitants, enfants et retraités compris.
>
> **Dans le calendrier de la dépense publique**, ces prélèvements paient les dépenses du 1er janvier au **5 octobre environ** [[calc:po_2025_eur_bn / one_day_spending_eur_bn = 277,9]]. Les autres recettes publiques prennent le relais jusqu’au 29 novembre environ (chapitre 1) [[calc:total_revenue_2025_eur_bn / one_day_spending_eur_bn = 332,7]]. Ensuite, la dépense est payée **avec de l’argent emprunté** [[yard:deficit_days|contexte]].
>
> **Si la France était un ménage** qui gagne 3 000 € par mois [[yard:household_monthly_income_eur]], **2 506 €** viendraient des prélèvements obligatoires [[calc:po_2025_eur_bn × household_scale_eur_per_month_per_bn = 2 505,6]] (image illustrative, voir ses limites au chapitre 1).

**Visuel**

1. Silhouette « 1 habitant » : « 18 900 € par an ».
2. Ruban du calendrier (repris du chapitre 2) en trois couleurs : prélèvements (→ 5 octobre, 278 jours), autres recettes (→ 29 novembre), emprunt (32 derniers jours, bande rouge).
3. Budget du ménage : revenus 3 000 € (dont 2 506 € de prélèvements).

- Calculs : 1 305 / 4,696 = 277,9 jours (278e jour de 2025 = 5 octobre) ; 1 562,5 / 4,696 = 332,7 jours (29 novembre) ; 1 305 × 1,92 = 2 505,6 €.

**Pastilles source** : [[yard:po_per_capita_eur]] [[yard:one_day_spending_eur_bn]] [[fig:po_2025_eur_bn]] [[fig:total_revenue_2025_eur_bn]] [[yard:deficit_days]] [[yard:household_monthly_income_eur]] [[yard:household_scale_eur_per_month_per_bn]] – Calcul de la plateforme d’après Insee (*Insee Première* n° 2106, 29 mai 2026) et Eurostat (`gov_10a_main`, 21 octobre 2026). Mention : illustratif.

---

## Étape 3. Plus haut ou plus bas qu’avant ?

**Texte affiché**

> En 2017, les prélèvements obligatoires atteignaient **45,3 % du PIB**, le niveau le plus haut de la série [[fig:po_2017_pct_gdp]]. En 2024, ils étaient à **42,7 % du PIB** [[fig:po_2024_pct_gdp]], soit **2,6 points de PIB de moins** [[fig:po_change_2017_2024_pts]]. En 2025, ils remontent à 43,6 % du PIB [[fig:po_2025_pct_gdp]].
>
> Pourtant, **72 % des personnes interrogées** pensent que les impôts ont augmenté depuis 2017 [[quiz:M10]]. Ce n’est pas faux en euros. De 2017 à 2025, les prélèvements sont passés de 1 038,1 [[fig:po_2017_eur_bn]] à 1 305 milliards d’euros [[fig:po_2025_eur_bn]], soit **+25,7 %** [[fig:po_change_2017_2025_nominal_pct]]. Après inflation, la hausse n’est plus que de **+2,5 %** [[fig:po_change_2017_2025_real_pct]] : moins vite que l’économie, à peine plus vite que les prix.
>
> Côté dépenses, la même correction joue dans l’autre sens. Hors inflation, la dépense publique a augmenté chaque année en moyenne de 2005 à 2025, et encore en 2025.
>
> **En part de la richesse nationale, les prélèvements ont baissé ; en euros, ils ont augmenté.**
>
> Ces baisses n’ont pas profité à tous de la même façon. L’Institut des politiques publiques (IPP ; institut de recherche académique) a mesuré l’effet des mesures de 2017 à 2022 sur le niveau de vie.
>
> Le niveau de vie des 1 % les plus aisés augmente de **3,3 %** [[fig:ipp81_gain_top1_pct]]. Celui des 5 % les plus modestes augmente de **0,8 %** [[fig:ipp81_gain_bottom5_pct]]. Les chômeurs, eux, perdent **1,1 %** de leur niveau de vie [[fig:ipp81_gain_unemployed_pct]].
>
> Les deux affirmations sont vraies, selon ce que l’on mesure.

**Visuel**

- Courbe 2017 → 2025, « en % du PIB », points annotés 2017 (45,3), 2024 (42,7), 2025 (43,6).
- Interrupteur « en % du PIB / en milliards d’euros » : en euros, deux points seulement (2017 : 1 038,1 ; 2025 : 1 305), la série annuelle en euros n’étant pas dans figures.json.

**Pastilles source** : [[fig:po_2017_pct_gdp]] [[fig:po_2024_pct_gdp]] [[fig:po_change_2017_2024_pts]] – Insee, série des taux de prélèvements obligatoires 1959-2025, 28 août 2026. Mention : mesuré. [[fig:po_2017_eur_bn]] [[fig:po_change_2017_2025_nominal_pct]] – Insee, tableau 3.216, 28 août 2026. Mention : mesuré. [[fig:po_change_2017_2025_real_pct]] – calcul du fichier 14 (§7.1) d’après Insee et Eurostat (`prc_hicp_aind`), déflaté par l’IPCH. Mention : estimé. [[quiz:M10]] – sondage Elabe pour BFMTV, 4-5 novembre 2025. Dépenses hors inflation : Cour des comptes, synthèse du rapport *La situation et les perspectives des finances publiques*, 25 juin 2026 (https://www.ccomptes.fr/sites/default/files/2026-06/20260625-synthese-RSPFP-2026.pdf) ; Haut-commissariat à la Stratégie et au Plan, *Focus Finances publiques*, 17 juillet 2026 (https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-07-17%20-%20Focus%20Finances%20publiques/HCSP-2026-FRANCE%202035-2050_Focus-Finances%20publiques_0.pdf). Mention : mesuré. Taux de croissance en volume à afficher dès que `te_volume_growth_2025_pct` et `te_volume_growth_avg_2005_2025_pct` existeront dans figures.json. Effets par niveau de vie : IPP, *Note IPP* n° 81, mars 2022 (https://www.ipp.eu/en/publication/redistributive-effects-of-the-socio-fiscal-measures-implemented-during-the-2017-2022-five-year-term-aimed-at-households/), via [[src:f08]] ; [[fig:ipp81_gain_top1_pct]] [[fig:ipp81_gain_bottom5_pct]] [[fig:ipp81_gain_unemployed_pct]] – microsimulation des seules mesures « ménages » décidées pendant le quinquennat (variation du revenu disponible). Mention : estimé. Financement : « Financé surtout par des contrats de recherche ; pas de subvention publique pérenne directe (site de l’IPP). » (https://www.ipp.eu/decouvrir-lipp/budget-et-financements/).

---

## Étape 4. Et par rapport aux autres pays ?

**Texte affiché**

> Pour comparer les pays, il faut la même règle de calcul pour tous : celle de l’Organisation de coopération et de développement économiques (OCDE).
>
> Selon cette mesure, les recettes fiscales totales, cotisations sociales comprises, représentent **43,5 % du PIB** en France en 2024 [[fig:oecd_tax_to_gdp_2024_pct_gdp]]. La France est **2e sur les 36 pays de l’OCDE** ayant publié leurs données 2024 [[fig:oecd_tax_to_gdp_2024_rank]], derrière le Danemark (**45,2 % du PIB**) [[fig:denmark_tax_to_gdp_2024_pct_gdp]]. La moyenne de l’OCDE est de **34,1 % du PIB** [[fig:oecd_avg_tax_to_gdp_2024_pct_gdp]].
>
> Rapporté au nombre d’habitants plutôt qu’au PIB, l’écart se réduit. En recettes fiscales par habitant, mesurées en standards de pouvoir d’achat (estimation), la France est **9e sur 27** dans l’Union européenne en 2024 [[fig:tax_revenue_per_capita_pps_2024_rank]].
>
> **Pourquoi 43,5 % du PIB et pas 42,7 %, le taux de l’Insee pour 2024 [[fig:po_2024_pct_gdp]] ?** Surtout à cause des crédits d’impôt versés même à ceux qui ne paient pas d’impôt (crédits d’impôt remboursables : **19,6 milliards d’euros** en 2024 [[fig:refundable_tax_credits_2024_eur_bn]]). L’OCDE et Eurostat les comptent comme une dépense publique, et non comme une baisse d’impôt.
>
> Sur la définition européenne, proche de celle de l’OCDE, la Cour des comptes (juridiction financière) estime 2025 à **44,2 à 44,3 % du PIB** [[fig:po_2025_esa_concept_pct_gdp]].

**Visuel**

- Barres horizontales des pays de l’OCDE en 2024, « en % du PIB (définition OCDE) » ; France, Danemark et moyenne OCDE mis en évidence. Légende toujours visible : « Année : 2024. Groupe : les 36 pays de l’OCDE ayant publié 2024. Mesure : recettes fiscales totales, cotisations sociales comprises (OCDE). »
- Valeurs des autres pays : série graphique à intégrer comme fichier de données (`research/data/oecd_revenue_statistics_2025_pct_gdp.csv`), pas comme figures isolées. Le 42,7 % de l’Insee n’apparaît jamais sur le graphique.
- Ouvre le comparateur de pays avec l’indicateur déjà choisi.

**Pastilles source** : [[fig:oecd_tax_to_gdp_2024_pct_gdp]] [[fig:oecd_tax_to_gdp_2024_rank]] [[fig:denmark_tax_to_gdp_2024_pct_gdp]] [[fig:oecd_avg_tax_to_gdp_2024_pct_gdp]] – OCDE, *Statistiques des recettes publiques 2025*, décembre 2025. Mention : mesuré. [[fig:refundable_tax_credits_2024_eur_bn]] – Insee, tableau 3.217, d’après le fichier 18, §1.3. Mention : mesuré. [[fig:po_2025_esa_concept_pct_gdp]] – Cour des comptes, *La situation et les perspectives des finances publiques*, 25 juin 2026. Mention : estimé. [[fig:tax_revenue_per_capita_pps_2024_rank]] – calcul du fichier 05 (§5.1C) d’après Eurostat (`gov_10a_taxag`, `nama_10_pc`), en standards de pouvoir d’achat. Mention : estimé.

---

## Étape 5. Encadré « Le meilleur contre-argument » (le niveau)

**Texte affiché**

<!-- box-side: droite -->
> **Le meilleur contre-argument**
>
> **« À ce niveau, les prélèvements freinent l’emploi et l’activité : l’effort doit venir de la dépense. »**
>
> La France prélève déjà plus que presque tous les pays de l’OCDE (étape 4). Le travail y est particulièrement taxé. Pour un célibataire au salaire moyen, impôts et cotisations prennent **près de la moitié du coût du travail** [[fig:oecd_tax_wedge_single_2025_pct]]. C’est le 3e niveau sur 38 pays de l’OCDE [[fig:oecd_tax_wedge_single_2025_rank]].
>
> Pour l’Institut Montaigne (libéral-centriste), l’ajustement doit donc venir surtout de la dépense. Le faire par les seules recettes demanderait des hausses d’impôts sans précédent.
>
> *Sources : Institut Montaigne (libéral-centriste), *Budget base zéro*, novembre 2025 ; OCDE (organisation internationale), *Les impôts sur les salaires 2026*, avril 2026.* [[src:f10]]
>
> **Ce qu’on peut répondre**
>
> Un taux élevé ne veut pas dire que les Français perdent cet argent. Une grande partie leur revient en retraites, en soins remboursés et en services publics. L’Insee (institut public de statistique) compte une majorité de bénéficiaires nets (étape 8).
>
> La France finance aussi par des cotisations publiques ce que d’autres pays financent par des assurances privées obligatoires. Celles-ci ne comptent pas comme des impôts (chapitre 2). Ces cotisations ouvrent aussi des droits : retraite, chômage, santé. Sur un point, l’objection tient : le travail reste parmi les plus taxés.

**Visuel** : encadré fixe, sur le même écran que l’étape 4, jamais replié (glossaire, §4.6).

**Pastilles source** : Institut Montaigne, *Budget base zéro*, novembre 2025, via [[src:f10]] (fichier 10, §4.1 et §5.4, réf. S44) ; étiquette d’orientation du glossaire, §1.13. Financement : « Financé par des contributions privées de plus de 200 entreprises, chacune à moins de 1,2 % du budget (site de l’Institut Montaigne). » (https://www.institutmontaigne.org/qui-sommes-nous). Mention : position d’un institut. [[fig:oecd_tax_wedge_single_2025_pct]] [[fig:oecd_tax_wedge_single_2025_rank]] – OCDE, *Les impôts sur les salaires 2026*, avril 2026 (dénominateur : coût total du travail, pas le PIB ; valeur 47,2 %, affichée « près de la moitié » pour ne pas la confondre avec les 47,2 % de foyers imposables de l’étape 7). Mention : mesuré. Réponse : Insee, « Revenus des ménages élargis à l’ensemble de l’économie en 2023 », *Insee Analyses* n° 118, 16 avril 2026 (bénéficiaires nets, étape 8) ; méthode des *Statistiques des recettes publiques* de l’OCDE (chapitre 2, encadré SOCX).

---

## Étape 6. De quoi sont faits ces 1 305 milliards ?

**Texte affiché**

> Les prélèvements obligatoires ne se résument pas à l’impôt sur le revenu. En 2025 :
>
> - les **cotisations sociales**, payées sur les salaires, rapportent **446,3 milliards d’euros** [[fig:social_contributions_2025_eur_bn]] ; elles financent surtout les retraites et l’assurance maladie ;
> - la **TVA**, payée par tous les consommateurs, **208,8 milliards** [[fig:vat_2025_eur_bn]] ;
> - la **CSG et la contribution au remboursement de la dette sociale (CRDS)**, prélevées sur presque tous les revenus, **165,9 milliards** [[fig:csg_crds_2025_eur_bn]] ;
> - l'**impôt sur le revenu**, celui de la déclaration annuelle, **94,3 milliards** [[fig:ir_net_2025_eur_bn]] ;
> - l'**impôt sur les sociétés**, **59,3 milliards** [[fig:corporate_tax_net_2025_eur_bn]].
>
> Le reste vient des impôts locaux et d’autres taxes.

**Visuel**

- Barre empilée de 1 305 Md€ : cotisations sociales, TVA, CSG + CRDS, impôt sur le revenu, impôt sur les sociétés, « autres » (impôts locaux et autres taxes : segment sans valeur affichée tant que le reste n’est pas calculé sur le même concept que les prélèvements obligatoires). Au toucher : montant et part des prélèvements obligatoires.
- Second temps : Sankey « recette → État, Sécurité sociale, collectivités », avec la note : « Les recettes sont en partie affectées par la loi : rapporter un impôt à une dépense précise est une convention (Fipeco). »

**Pastilles source** : [[fig:po_2025_eur_bn]] – Insee, *Insee Première* n° 2106, 29 mai 2026. [[fig:social_contributions_2025_eur_bn]] [[fig:vat_2025_eur_bn]] [[fig:csg_crds_2025_eur_bn]] [[fig:ir_net_2025_eur_bn]] [[fig:corporate_tax_net_2025_eur_bn]] – Insee, comptes nationaux annuels base 2020, tableau 3.217, 28 août 2026 (impôts nets des crédits d’impôt). Mention : mesuré.

---

## Étape 7. Qui paie l’impôt sur le revenu ?

**Texte affiché (avant la réponse)**

> Combien de foyers paient vraiment l’impôt sur le revenu ?

**Interaction « Estimez d’abord »**

- Question : « Selon vous, quelle part des foyers fiscaux paie un impôt sur le revenu (après réductions et crédits d’impôt) ? »
- Curseur 0-100 %, pas de 1, départ à 50.
<!-- estimez-réponse: ir_households_paying_pct -->

**Texte affiché (après la réponse)**

> Pour les revenus de 2024, **47,2 % des foyers fiscaux** paient un impôt sur le revenu [[fig:ir_households_paying_pct]]. Un peu plus de la moitié, 52,8 % des foyers fiscaux, n’en paie donc pas [[calc:100 − ir_households_paying_pct = 52,8]].
>
> Mais ne pas payer l’impôt sur le revenu ne veut pas dire ne payer aucun impôt. **Tout le monde paie la TVA** sur ses achats. **Presque tous les revenus supportent la CSG** : salaires, pensions, allocations chômage, revenus du capital, avec des taux réduits ou des exonérations pour les plus modestes.

**Visuel** : 100 maisons, 47 colorées (« paient un impôt sur le revenu net ») ; puis toutes reçoivent les étiquettes « TVA » et « CSG ». Repère : réponse de l’utilisateur contre 47,2 %.

**Pastilles source** : [[fig:ir_households_paying_pct]] – DGFiP, *Statistiques* n° 41, novembre 2025. Mention : mesuré. Note : « Un foyer fiscal n’est pas un ménage : un couple marié compte pour un foyer, deux colocataires pour deux. »

---

## Étape 8. Qui paie l’ensemble des prélèvements ?

**Interaction « Estimez d’abord »**

- Question : « Selon vous, quelle part de l’ensemble des prélèvements est payée par les 10 % les plus aisés ? »
- Curseur 0-100 %, pas de 1, départ à 50.
<!-- estimez-réponse: top10_share_levies_2023_pct -->

**Texte affiché (après la réponse)**

> En 2023, les 10 % les plus aisés de la population paient **33,3 % de l’ensemble des prélèvements** [[fig:top10_share_levies_2023_pct]], pas seulement de l’impôt sur le revenu.
>
> En bas de l’échelle, c’est différent, à cause du poids de la TVA et des autres taxes indirectes. En 2022, les prélèvements représentaient **64 % du revenu avant transferts** des 10 % les plus modestes [[fig:levies_share_income_d1_2022_pct]], contre **48 %** pour les 10 % les plus aisés [[fig:levies_share_income_d10_2022_pct]].
>
> Ce ratio se lit avec prudence. Il rapporte des taxes payées sur une consommation financée en partie par les prestations sociales. Or le revenu est mesuré avant la plupart de ces prestations : il est donc très faible pour les plus modestes.
>
> Le système réduit surtout les inégalités par ce qu’il **verse** : prestations sociales, retraites, services publics gratuits. En comptant ces services, **56 % des personnes reçoivent plus qu’elles ne paient** en 2023 [[fig:net_beneficiaries_2023_pct]].

**Visuel**

- Barres par dixième de la population : prélèvements payés / prestations et services reçus. Les séries par dixième sont des données de graphique (fichier de données à créer depuis l'*Insee Analyses* n° 118) ; en attendant, n’afficher que « 10 % les plus aisés : 33,3 % », le couple « 64 % / 48 % du revenu avant transferts (2022) » et le compteur « 56 % de bénéficiaires nets ».

**Pastilles source** : [[fig:top10_share_levies_2023_pct]] [[fig:net_beneficiaries_2023_pct]] – Insee, « Revenus des ménages élargis à l’ensemble de l’économie en 2023 », *Insee Analyses* n° 118, 16 avril 2026. Mention : estimé. [[fig:levies_share_income_d1_2022_pct]] [[fig:levies_share_income_d10_2022_pct]] – Insee, *Insee Première* n° 2022, novembre 2024 (données 2022 ; l’édition 2023 ne reprend pas ce ratio ; revenu avant transferts augmenté des pensions et allocations chômage). Mention : estimé.

---

## Étape 9. Encadré « Le meilleur contre-argument » (qui paie)

**Texte affiché**

<!-- box-side: gauche -->
> **Le meilleur contre-argument**
>
> **« Les chiffres par dixième masquent le tout sommet : les milliardaires paient moins d’impôts, en part de leur revenu, que les autres foyers très aisés. »**
>
> L’IPP (institut de recherche académique) a relié les déclarations des personnes aux comptes de leurs sociétés. Les foyers de milliardaires paieraient environ **26 %** de leur revenu en impôts [[fig:ipp_effective_rate_billionaires_2016_pct]]. Les 0,1 % les plus aisés en paieraient environ **46 %** [[fig:ipp_effective_rate_top01_2016_pct]].
>
> La raison : une grande partie des revenus des milliardaires reste dans les sociétés qui détiennent leurs entreprises (holdings). Ces revenus ne paient alors que l’impôt sur les sociétés.
>
> *Source : IPP (institut de recherche académique), L. Bach, A. Bozio, A. Guillouzouic et C. Malgouyres, « Quels impôts les milliardaires paient-ils ? », *Note IPP* n° 92, juin 2023, mise à jour en mai 2025 (données 2016).*
>
> **Ce qu’on peut répondre**
>
> La méthode est discutée. Le gouvernement juge « non consensuel » de compter comme un revenu les bénéfices non distribués.
>
> François Geerolf a publié une note critique en octobre 2026. Il est économiste à l’Observatoire français des conjonctures économiques (OFCE ; Sciences Po, sensibilité keynésienne) et écrit à titre personnel. Sur une base de revenu homogène, il trouve **25,1 %** pour les milliardaires [[fig:geerolf_rate_billionaires_homogeneous_pct]], contre **26,8 %** au seuil des 10 % les plus aisés [[fig:geerolf_rate_top10_threshold_pct]].
>
> Selon lui, l’écart devient faible. À notre connaissance, les auteurs de l’étude n’ont pas encore répondu publiquement.
>
> Une partie de l’écart tient aussi au calendrier : les bénéfices gardés dans la holding seront imposés s’ils sont distribués. Depuis 2025, un impôt minimum vise aussi ces très hauts revenus : la contribution différentielle sur les hauts revenus (CDHR). Son rendement est discuté au chapitre 7.

<!-- coïncidence : les 26 % de l’IPP (taux d’imposition des milliardaires, données 2016) et les +25,7 % de l’étape 3 (hausse des prélèvements en euros de 2017 à 2025) sont deux chiffres sans rapport. -->

**Visuel** : encadré fixe, sur le même écran que l’étape 8, jamais replié.

**Pastilles source** : [[fig:ipp_effective_rate_billionaires_2016_pct]] [[fig:ipp_effective_rate_top01_2016_pct]] – IPP, Note n° 92 (données 2016). Mention : estimé. [[fig:geerolf_rate_billionaires_homogeneous_pct]] [[fig:geerolf_rate_top10_threshold_pct]] – F. Geerolf, *Les mensonges de la taxe Zucman : un vrai sujet, un faux diagnostic, un mauvais remède*, octobre 2026 (https://fgeerolf.com/mensonges-taxe-zucman.pdf). Mention : estimé. Ni la note de l’IPP ni celle de F. Geerolf ne sont publiées dans une revue à comité de lecture. Réponse du gouvernement à la question écrite n° 1212 (fichier 07, réf. S50). Financement : IPP, « Financé surtout par des contrats de recherche ; pas de subvention publique pérenne directe (site de l’IPP). » (https://www.ipp.eu/decouvrir-lipp/budget-et-financements/) ; OFCE, « Financé par une subvention publique versée par l’État à la Fondation nationale des sciences politiques (site de l’OFCE). » (https://www.ofce.fr/ofce/statuts.html). CDHR : rendement annoncé et observé au chapitre 7, étape 8 (propriétaire des rendements).

---

## Étape 10. Deux idées reçues, le même traitement

**Texte affiché**

> **« Il suffit de faire payer les plus riches. »** Ce qui est plausible : de nouvelles taxes sur les très hauts revenus et patrimoines pourraient rapporter **de 10 à 25 milliards d’euros par an** [[fig:tax_rich_package_eur_bn]]. Ce montant tient compte des réactions des contribuables.
>
> C’est notre propre synthèse des chiffrages publiés : aucun organisme n’a chiffré cet ensemble. Une part notable repose sur une réforme des droits de succession qu’aucune estimation indépendante n’a chiffrée.
>
> C’est **de 2,1 à 5,3 jours de dépense publique** et **de 6,6 % à 16,5 % du déficit** de 2025 [[calc:tax_rich_package_eur_bn / one_day_spending_eur_bn = 2,1 à 5,3 ; tax_rich_package_eur_bn / deficit_2025_eur_bn × 100 = 6,6 à 16,5]]. Ce sont des ordres de grandeur. Ce qui ne tient pas : « il suffit ». C’est une estimation, pas une recette garantie, et elle ne comble pas le déficit.
>
> **« Une minorité paie pour tout le monde. »** Ce qui est exact : moins de la moitié des foyers paie l’impôt sur le revenu [[fig:ir_households_paying_pct]]. Les 10 % les plus aisés paient un tiers de l’ensemble des prélèvements [[fig:top10_share_levies_2023_pct]], bien plus que leur poids dans la population.
>
> Ce qui ne tient pas : « pour tout le monde ». Tout le monde paie la TVA, et presque tous les revenus supportent la CSG. Les deux tiers des prélèvements viennent des 90 % restants [[calc:100 − top10_share_levies_2023_pct = 66,7]].
>
> La question « qui *devrait* payer plus ? » est une question de justice. Ce site ne la tranche pas. Il donne les ordres de grandeur.

**Visuel** : deux cartes de même gabarit, taille et couleur neutre, dans un ordre tiré au hasard à chaque visite. Gauche : fourchette 10–25 Md€ convertie en jours (2,1–5,3) et en % du déficit (6,6–16,5 %). Droite : pictogramme de l’étape 7 (47,2 %) + 33,3 %.

**Pastilles source** : [[fig:tax_rich_package_eur_bn]] – synthèse de la plateforme (fichier 07, §5 ; composante « succession » sans chiffrage indépendant). Mention : estimé (montants visés pour 2027 rapportés aux dénominateurs de 2025 : ordre de grandeur). [[yard:one_day_spending_eur_bn]] [[fig:deficit_2025_eur_bn]] – calcul de la plateforme. Mention : illustratif. [[fig:ir_households_paying_pct]] – DGFiP, *Statistiques* n° 41, novembre 2025. [[fig:top10_share_levies_2023_pct]] – Insee, *Insee Analyses* n° 118, 16 avril 2026.

---

## Étape 11. Les « niches fiscales » : des impôts qu’on ne prélève pas

**Texte affiché**

> L’État renonce aussi à certaines recettes, par des réductions, des crédits ou des exonérations d’impôt : ce sont les **dépenses fiscales**, souvent appelées « niches fiscales ».
>
> En 2025, il y en a **474** [[fig:tax_expenditures_count]]. Elles coûtent **91,8 milliards d’euros**, soit **3,1 % du PIB** [[fig:tax_expenditures_2025_eur_bn]] [[fig:tax_expenditures_2025_pct_gdp]] : **environ 20 jours de dépense publique**, ou **1 331 € par habitant** [[calc:tax_expenditures_2025_eur_bn / one_day_spending_eur_bn = 19,6 ; tax_expenditures_2025_eur_bn × 1000 / population_2025_m = 1 331]].
>
> **Attention : ce coût n’est pas une recette disponible telle quelle.** Chaque niche a ses bénéficiaires et un objectif. Mais la Cour des comptes relève que le coût réel n’est connu que pour une partie de ces dispositifs. Ils sont peu évalués : leur utilité n’est pas toujours démontrée.
>
> Exemple côté cotisations : la baisse des cotisations patronales sur les bas salaires. Selon le rapport Bozio-Wasmer (rapport remis au gouvernement, 2024), elle a des effets forts sur l’emploi près du salaire minimum interprofessionnel de croissance (SMIC).
>
> Ces effets sont faibles ou nuls au-delà d’environ 2,5 SMIC [[fig:bozio_wasmer_threshold_smic]]. Un recentrage coûterait donc beaucoup moins d’emplois qu’une suppression totale, dont le rendement et le coût en emplois sont au chapitre 7.
>
> **Et la fraude fiscale ?** Selon la Cour des comptes, aucune estimation robuste de son montant n’existe. Personne ne peut dire si elle est plus proche de 30 ou de 130 milliards d’euros par an [[fig:tax_gap_cour_range_eur_bn]]. En 2024, le contrôle fiscal a notifié 20,1 milliards d’euros [[fig:tax_audit_assessed_2024_eur_bn]] et en a encaissé 11,4 [[fig:tax_audit_collected_2024_eur_bn]].
>
> Ce qui est encaissé est déjà compté dans les recettes. Ce qu’un nouveau plan contre la fraude rapporterait en plus est discuté au chapitre 7.

**Visuel** : sur le ruban du calendrier, un bloc de 20 jours « dépenses fiscales » en pointillés au-dessus du ruban (ce que l’État aurait pu prélever), pas dedans. Lien vers la fiche « Aides publiques aux entreprises ».

- Calculs : 91,83 / 4,696 = 19,6 jours ; 91,83 × 1 000 / 68,998 = 1 331 €.

**Pastilles source** : [[fig:tax_expenditures_2025_eur_bn]] [[fig:tax_expenditures_count]] [[fig:tax_expenditures_2025_pct_gdp]] – Cour des comptes, *Analyse de l’exécution budgétaire 2025 – Dépenses fiscales*, avril 2026. Mention : estimé. [[fig:bozio_wasmer_threshold_smic]] – A. Bozio et É. Wasmer, *Les politiques d’exonérations de cotisations sociales : une inflexion nécessaire*, octobre 2024 (https://vie-publique.fr/files/rapport/pdf/295596.pdf ; seuil de 2,5 SMIC : ancien seuil du CICE et point de sortie du scénario central du rapport ; un paramètre, pas une statistique mesurée). Mention : estimé. Suppression totale des allègements (48 milliards nets, environ 980 000 emplois) : chapitre 7, étape 8, propriétaire des rendements. [[fig:tax_gap_cour_range_eur_bn]] [[fig:tax_audit_assessed_2024_eur_bn]] [[fig:tax_audit_collected_2024_eur_bn]] – Cour des comptes, *La lutte contre la fraude fiscale*, 16 décembre 2025 (https://www.ccomptes.fr/sites/default/files/2025-12/20251216-Lutte-contre-la-fraude-fiscale.pdf). Mentions : fourchette de 30 à 130 milliards = ce n’est pas une estimation, seulement l’ampleur de l’incertitude (sur 1 268 milliards de prélèvements obligatoires en 2024) ; montants notifiés et encaissés = mesuré. Rendement d’un nouveau plan antifraude : chapitre 7, étape 8.

---

## Étape 12. Aperçu : « Le reçu de vos impôts »

**Texte affiché**

> Prenons une personne « moyenne », qui représente environ 18 900 € de prélèvements par an [[yard:po_per_capita_eur]]. Si on répartit cette somme comme les dépenses publiques de 2024, on obtient ce reçu.

**Reçu affiché (illustratif)**

> | Poste | Montant |
> |---|---|
> | Protection sociale (retraites, famille, chômage, aides au logement, revenu de solidarité active) | environ 7 850 € [[calc:po_per_capita_eur × cofog_social_protection_2024_pct_te / 100 = 7 849]] |
> | dont vieillesse (surtout retraites) | environ 4 430 € [[calc:po_per_capita_eur × cofog_old_age_2024_pct_te / 100 = 4 426]] |
> | Santé | environ 2 950 € [[calc:po_per_capita_eur × cofog_health_2024_pct_te / 100 = 2 951]] |
> | Éducation | environ 1 680 € [[calc:po_per_capita_eur × cofog_education_2024_pct_te / 100 = 1 683]] |
> | Défense | environ 610 € [[calc:po_per_capita_eur × cofog_defense_2024_pct_te / 100 = 605]] |
> | Autres fonctions (services généraux et intérêts de la dette, économie et transports, sécurité, culture, logement et équipements collectifs, environnement) | le reste |
> | **En plus : 8,8 % des dépenses publiques financées par l’emprunt (2025)** [[fig:share_te_borrowed_2025_pct]] | |

> Ce reçu est une convention : les cotisations et la CSG vont d’abord à la Sécurité sociale, l’impôt sur le revenu d’abord à l’État. Un second reçu montrera ce que vous recevez (prestations, soins, école, routes).
>
> **Calculez votre propre reçu** à partir de votre impôt sur le revenu et, si vous le souhaitez, de votre salaire.

**Visuel** : ticket de caisse imprimé ligne par ligne, dernière ligne (« emprunt ») en rouge ; bouton « Calculer mon reçu » → outil « Le reçu de vos impôts ».

- Calculs (18 913,6 € × part des dépenses publiques totales) : 41,5 % → 7 849 € ; 23,4 % → 4 426 € ; 15,6 % → 2 951 € ; 8,9 % → 1 683 € ; 3,2 % → 605 €. Arrondis à la dizaine. Parts 2024 (COFOG, dernière année publiée) appliquées à des prélèvements 2025 : le préciser dans la pastille.

**Pastilles source** : [[yard:po_per_capita_eur]] [[fig:cofog_social_protection_2024_pct_te]] [[fig:cofog_old_age_2024_pct_te]] [[fig:cofog_health_2024_pct_te]] [[fig:cofog_education_2024_pct_te]] [[fig:cofog_defense_2024_pct_te]] [[fig:share_te_borrowed_2025_pct]] – Calcul de la plateforme d’après Eurostat (COFOG 2024, `gov_10a_exp`) et Insee (2025). Mention : illustratif. Note : « Le site du ministère, “À quoi servent mes impôts ?”, propose un calcul proche avec des conventions un peu différentes. »

---

## Étape 13. Transition vers le chapitre 4

**Texte affiché**

> Les prélèvements ont baissé en part du PIB depuis 2017. Le déficit, lui, reste élevé. Les baisses d’impôts ont-elles creusé le déficit ? Ou les dépenses ont-elles trop augmenté ?
>
> Selon la Cour des comptes, les baisses d’impôts et de cotisations décidées de 2018 à 2023 ont un coût important. Elles n’ont pas été compensées par des économies de dépense. Dans l’autre sens, les dépenses publiques ont augmenté depuis 2019. Combien pèse chaque côté, et lequel explique le déficit ? Estimez-le au chapitre suivant.
>
> **→ Chapitre 4 : Pourquoi le déficit ?**
>
> *Ou bien : calculez votre reçu, ou essayez d’équilibrer vous-même le budget.*

**Visuel** : le ruban se replie. Trois boutons : « Chapitre 4 » (principal), « Le reçu de vos impôts », « Équilibrez vous-même le budget ».

**Pastilles source** : Citation de la Cour des comptes (baisses « non compensées par des économies en dépenses ») : *La situation et les perspectives des finances publiques*, 15 juillet 2024, p. 35-36.

---

## Pour aller plus loin

**Texte affiché**

> - **Fiscalité : niveau, structure, qui paie** (fiche thématique) : les cotisations patronales et les comparaisons par habitant.
> - **Aides publiques aux entreprises** : les « niches sociales » (**91,0 milliards d’euros** en 2025 [[fig:niches_sociales_2025_eur_bn]]) et les allègements de cotisations. Leurs périmètres ne s’additionnent pas.
> - **Les baisses d’impôts depuis 2017** : le détail des mesures et les lectures opposées.
> - **Page de méthode : trois passerelles de mesure** : du taux de l’Insee à celui de l’OCDE, poste par poste.
> - **Propositions des partis** : chaque mesure fiscale chiffrée au même étalon.

**Pastilles source** : [[fig:niches_sociales_2025_eur_bn]] – annexe 4 au PLFSS 2027, octobre 2026. Mention : estimé.

---

<!--
ANNEXE A (non affichée) – État des données (mise à jour du 25 octobre 2026, passe « chapitres »)

Toutes les entrées proposées par l’ancienne annexe A existent désormais dans figures.json, sauf :
- A2 (part de l’IR payée par les 10 % les plus aisés) : la DGFiP écrit seulement « près des trois quarts » ; pas de valeur stockable. La phrase a été retirée de l’étape 7 (l’étape 8 porte le chiffre des 10 % les plus aisés).
- A3 (séries par dixième) et A6 (valeurs OCDE de chaque pays) : séries de graphique, à livrer comme fichiers de données, pas comme figures isolées.
- `contribution_relief_general_eur_bn` (75 Md€, 2023, statut « caveat ») n’est plus cité dans le texte visible (déplacé vers la fiche « Aides publiques aux entreprises »).
- `tax_revenue_per_capita_pps_2024` (17 800 SPA) : non cité, seul le rang l’est.

ANNEXE B (non affichée) – Points de relecture

1. Étape 2 : calendrier en trois couleurs (5 octobre / 29 novembre) calculé sur 365 jours ; vérifier avec le rendu du chapitre 2 (même ruban, même convention).
2. Étape 10 : vérifier à l’audit de symétrie que les deux cartes ont la même longueur et le même verbe d’attribution.
3. Étape 11 : le total retenu est celui de la Cour des comptes (91,83 Md€), comme le recommande la fiche 4.12.
4. Étape 12 : colonne du tableau « 1 000 € » (fichier 01, §4.2) pour l’outil complet encore à arrêter.
5. Pour aller plus loin : titres des fiches repris du fichier 20 (§4.7, 4.10, 4.11, 4.12, 4.17) ; les liens seront posés quand les URL existeront.
-->

---

## Notes de relecture

### Passe de finalisation du 25 octobre 2026

*Volume du texte visible (mesure de `validate.py`) : 2 065 mots avant, 2 129 après (cible : 1 500 à 2 200). Durée de lecture affichée : environ 9 minutes, inchangée. `python3 -I validate.py --strict` : 0 erreur et 0 avertissement localisés dans ce chapitre. Restent deux avertissements inter-pages (« 25 Md€ » et « 47,2 % ») dont la cause est au chapitre 7 (voir point 9). Aucun chiffre sans pastille qui résout.*

1. **Nouvelles données (D-data-pass) : appliqué.** Étape 3 : effets de la *Note IPP* n° 81 chiffrés : 3,3 % pour les 1 % les plus aisés, 0,8 % pour les 5 % les plus modestes, perte de 1,1 % pour les chômeurs (`ipp81_gain_top1_pct`, `ipp81_gain_bottom5_pct`, `ipp81_gain_unemployed_pct`). Étape 11 : seuil « environ 2,5 SMIC » (`bozio_wasmer_threshold_smic`, paramètre « caveat »). Fraude fiscale : fourchette de 30 à 130 milliards, présentée comme l’ampleur de l’incertitude et non comme une estimation (`tax_gap_cour_range_eur_bn`). Contrôle fiscal 2024 : 20,1 milliards notifiés et 11,4 encaissés (`tax_audit_assessed_2024_eur_bn`, `tax_audit_collected_2024_eur_bn`). La citation de la Cour est paraphrasée sans guillemets, car la formulation française exacte n’est pas vérifiée (fichier 07, l. 230, en anglais). `tax_rich_package_eur_bn` : la fourchette de 10 à 25 milliards est inchangée après le retrait de la CDHR. La pastille porte déjà la note « synthèse de la plateforme ; composante succession sans chiffrage indépendant ». Le chapitre n’affiche pas le retour à 60 ans.
2. **Étiquettes (§1.13) : appliqué.** IPP (« IPP ; institut de recherche académique », étape 3 ; repris dans l’encadré de l’étape 9 et dans sa ligne de source). Cour des comptes (juridiction financière), première mention à l’étape 4. Institut Montaigne (libéral-centriste), dans le texte et dans la source de l’encadré de l’étape 5. OCDE (organisation internationale), dans la ligne de source du même encadré. Insee (institut public de statistique), dans la réponse. François Geerolf : forme complète du glossaire. Rapport Bozio-Wasmer (rapport remis au gouvernement, 2024). Financements vérifiés ajoutés aux pastilles, pas au texte : Institut Montaigne (étape 5), IPP (étapes 3 et 9), OFCE (étape 9).
3. **Encadrés (§4.6) : appliqué.** Étape 9 : thèse en gras entre guillemets ajoutée : « Les chiffres par dixième masquent le tout sommet : les milliardaires paient moins d’impôts, en part de leur revenu, que les autres foyers très aisés. » Puis l’auteur avec son étiquette et la ligne de source en italique. La citation longue devient un texte attribué en phrases courtes. Réponse : « les auteurs de l’étude » (sans organisme non étiqueté). Le paragraphe sur les rendements de la CDHR est réduit à une ligne qui renvoie au chapitre 7. Étape 5 : paragraphes séparés et thèse inchangée. La réponse ajoute « Sur un point, l’objection tient : le travail reste parmi les plus taxés » (§4.6, objection qui résiste). Le coin socio-fiscal est affiché « près de la moitié du coût du travail » et non « 47,2 % », pour éviter la confusion avec les 47,2 % de foyers imposables de l’étape 7 (valeur exacte dans la pastille).
4. **Doublons de propriété : appliqué.** L’ensemble « taxer les plus riches » (10 à 25 milliards ; 2,1 à 5,3 jours ; 6,6 % à 16,5 % du déficit) reste à l’étape 10, propriétaire. CDHR (annoncé et observé) : une ligne avec renvoi au chapitre 7, propriétaire des rendements. Les pastilles `cdhr_*` sont retirées, ainsi que la barre « CDHR » du visuel. Pour les 980 000 emplois, le chapitre 7 (étape 8) est retenu : c’est le coût du rendement de 48 milliards, et ce chapitre est propriétaire des rendements et des verdicts. Ce chapitre n’affiche plus ni les 48 milliards ni les 980 000 emplois. Il garde la nuance Bozio-Wasmer (seuil de 2,5 SMIC) et renvoie au chapitre 7. Le rendement d’un plan antifraude (1 à 3 milliards) passe aussi au chapitre 7. Ce chapitre garde la taille de la fraude fiscale et les montants du contrôle. Le chapitre 2 (étape 9) y renvoie déjà.
5. **Sigles : appliqué.** PIB développé à l’étape 0. Insee à l’étape 1. SMIC sous sa forme canonique (« salaire minimum interprofessionnel de croissance »). RSA écrit en toutes lettres dans le reçu.
6. **Pastilles et dénominateurs : appliqué.** « 43,6 € » sur 100 € avec sa pastille (même arrondi que 43,6 % du PIB). `deficit_days` marqué `|contexte` (32,3 jours appartient au chapitre 1). Ajout de « 43,5 % du PIB », « 52,8 % des foyers fiscaux » et « les 10 % les plus aisés de la population ». Les gains de l’IPP sont écrits en hausse du niveau de vie. Le chiffre de 10,0 % du PIB pour les cotisations patronales est retiré de « Pour aller plus loin » (collision avec un autre 10,0 % au chapitre 1).
7. **« Estimez d’abord » : appliqué.** Identifiants de réponse déclarés (`po_2025_pct_gdp`, `ir_households_paying_pct`, `top10_share_levies_2023_pct`).
8. **Lisibilité : appliqué.** Toutes les phrases affichées font 25 mots au plus, et tous les paragraphes 60 mots au plus. Note « coïncidence » non affichée : les 26 % de l’IPP et les 25,7 % de l’étape 3 n’ont aucun rapport.
9. **Hors de ce fichier (chapitre 7) :** « 25 Md€ » est la borne haute de `tax_rich_package_eur_bn` et de `zucman_proponents_eur_bn`, au chapitre 7, l. 192-193. Ce chapitre ne peut pas lever l’avertissement. « 47,2 % » apparaît ici pour `ir_households_paying_pct` (réponse de l’étape 7) et au chapitre 7, l. 149, pour `oecd_tax_wedge_single_2025_pct`. Le chapitre 7 peut écrire « près de la moitié du coût du travail », comme ici. L’ensemble « taxer les plus riches » du chapitre 7 (l. 193) doit devenir une ligne avec renvoi au chapitre 3. Le chapitre 7 doit aussi garder les 980 000 emplois et le rendement de la CDHR, vers lesquels ce chapitre renvoie.

### Passe transversale (plan de site) du 25 octobre 2026 : corrections transversales

*Volume du texte visible, mesuré par script (titre, blocs affichés `>`, questions des interactions ; hors pastilles, spécifications, commentaires et notes) : 2 204 mots avant, 2 148 après (cible : 1 500 à 2 200). Durée de lecture affichée : environ 9 minutes (240 mots par minute). Validateur `python3 -I validate.py` : 0 erreur, 0 avertissement. Aucun chiffre ajouté sans pastille qui résout.*

1. **Titres d’étape « ## Étape N. Titre » : appliqué** (14 titres).
2. **Étape 0 : appliqué.** TVA et CSG développées à la première occurrence ; ligne « Durée de lecture : environ 9 minutes. » ajoutée.
3. **Étape 2 (calendrier gardé, ménage réduit) : appliqué.** Résultats ajoutés aux pastilles de calcul (277,9 ; 332,7 ; 2 505,6) ; « 29 novembre environ (chapitre 1) » ; ménage réduit à une ligne avec renvoi « (image illustrative, voir ses limites au chapitre 1) » ; encadré « Les limites de la métaphore » supprimé (propriété des chapitres 1 et 5) ; visuel 3 réduit aux revenus ; `household_spending_month_eur` et `household_borrowing_month_eur` retirés des pastilles.
4. **Étape 3 : partiellement appliqué.** « 72 % des personnes interrogées » ; paragraphe IPP déplacé depuis l’étape 13, avec étiquette « institut de recherche académique » et pastille `[[src:f08]]` ; *Note IPP* n° 81 ajoutée aux pastilles. Montants +3,3 % / +0,8 % / perte de 1,1 % non affichés : `ipp81_gain_top1_pct`, `ipp81_gain_bottom5_pct`, `ipp81_gain_unemployed_pct` n’existent pas encore dans figures.json (texte qualitatif conservé).
5. **Étape 4 : appliqué.** OCDE développée ; crédits d’impôt remboursables expliqués en français simple. L’étape reste propriétaire de la comparaison OCDE (43,5 % ; 2e sur 36 ; 34,1 %).
6. **Étape 5 (encadré rééquilibré vers une lecture libérale) : appliqué.** Thèse « À ce niveau, les prélèvements freinent l’emploi et l’activité : l’effort doit venir de la dépense » (Institut Montaigne, étiquette « libéral-centriste » proposée par la décision D-labels, et coin socio-fiscal de l’OCDE, 47,2 % du coût du travail, 3e sur 38) ; réponse Insee (bénéficiaires nets), cotisations publiques contre assurances privées (renvoi au chapitre 2), droits ouverts. `last_surplus_year` et le rappel de `po_2025_pct_gdp` retirés (1974 appartient au chapitre 4). Pastilles réécrites ([[src:f10]], fichier 10, §4.1 et §5.4, réf. S44 ; OCDE ; *Insee Analyses* n° 118). À vérifier : l’étiquette du glossaire §1.13 porte encore « financé par des entreprises, libéral-centriste » ; ce chapitre suit l’étiquette décidée.
7. **Étape 6 : appliqué.** CRDS développée (la TVA, déjà développée à l’étape 0, reste en sigle).
8. **Étape 7 : appliqué.** `= 52,8` ajouté à la pastille de calcul.
9. **Étape 9 (encadré gauche gardé) : appliqué.** Citation en phrases courtes, sans « taux d’imposition effectif » ni « sociétés holdings » ; *Note IPP* n° 92 en italique et étiquette IPP dans la ligne de source ; Geerolf : OFCE développé avec son étiquette et « qui écrit à titre personnel » ; CDHR développée. La citation reprend le texte exact demandé (chiffres en gras, citation non graissée) ; le statut « revue à comité de lecture » reste mentionné pour les deux notes, dans la pastille.
10. **Étape 10 : appliqué.** Arrondi canonique partagé avec le chapitre 7, étape 8 : « de 2,1 à 5,3 jours » et « de 6,6 % à 16,5 % du déficit », résultats dans la pastille de calcul ; `= 66,7` ajouté à la seconde carte.
11. **Étape 11 : partiellement appliqué.** Résultats `= 19,6 ; 1 331` ajoutés ; « en comptant en postes à temps plein » ; SMIC développé. Non appliqués faute de données : fourchette « plutôt 30 ou 130 milliards », 20,1 milliards notifiés et 11,4 encaissés (`tax_gap_cour_range_eur_bn`, `tax_audit_assessed_2024_eur_bn`, `tax_audit_collected_2024_eur_bn` absents) ; seuil « environ 2,5 SMIC » (paramètre Bozio-Wasmer absent de yardsticks.json). Le texte qualitatif reste en place.
12. **Étape 12 : appliqué.** Résultats ajoutés aux cinq pastilles du reçu (7 849 ; 4 426 ; 2 951 ; 1 683 ; 605).
13. **Étape 13 : appliqué.** Les 62 milliards, 13 jours et 41 % (réponse notée du chapitre 4) sont retirés, ainsi que Rexecode, les hausses de 2010-2014 et la dérive des dépenses (propriété du chapitre 4, étapes 4, 5 et 7) ; nouveau paragraphe qui renvoie l’estimation au chapitre suivant. Bloc de 13 jours et ligne de calculs retirés du visuel ; pastilles réduites à la citation de la Cour (RSPFP, 15 juillet 2024, p. 35-36).
14. **Validation et volume : appliqué.** `python3 -I validate.py` : PASS ; 2 148 mots visibles ; durée affichée 9 minutes ; commentaire « Volume du texte visible » mis à jour.

**Données manquantes (rien inventé)** : `ipp81_gain_top1_pct`, `ipp81_gain_bottom5_pct`, `ipp81_gain_unemployed_pct`, `tax_gap_cour_range_eur_bn`, `tax_audit_assessed_2024_eur_bn`, `tax_audit_collected_2024_eur_bn`, paramètre du seuil Bozio-Wasmer (2,5 SMIC).

### Audit de symétrie gauche/droite du 25 octobre 2026

*Volume du texte visible : 1 995 mots avant, 2 207 après (cible : 1 500 à 2 200 mots, environ). Validateur `python3 -I validate.py` : 0 erreur, 0 avertissement. Ce passage ne modifie que ce fichier ; les entrées de figures.json demandées par l’audit n’existent pas encore et n’ont pas été créées ici. Aucun chiffre n’a été ajouté sans pastille qui résout : là où l’entrée manque, le texte reste qualitatif et la pastille source annonce l’identifiant attendu.*

1. **Fraude fiscale absente (lecture « gauche », sévérité haute) : partiellement appliqué.** Étape 11 : paragraphe « Et la fraude fiscale ? » (Cour des comptes, 16 décembre 2025 : aucune estimation robuste ; rendement réaliste d’un nouveau plan, fiscal et social, de 1 à 3 milliards `[[fig:antifraud_marginal_yield_eur_bn]]`, avec la mention « estimation, pas une recette garantie »). Non affichés faute d’entrée : « plutôt 30 ou 130 milliards », 20,1 milliards notifiés et 11,4 milliards encaissés en 2024 (`tax_gap_cour_range_eur_bn`, `tax_audit_assessed_2024_eur_bn`, `tax_audit_collected_2024_eur_bn` à créer, fichier 07, §3.7, réf. S10). Chapitre 7 : hors périmètre de ce fichier.
2. **Baisses d’impôts sur le capital 2017-2018 et leur répartition (gauche, haute) : partiellement appliqué.** Étape 13 : effets par niveau de vie de la Note IPP n° 81 en texte qualitatif (1 % les plus aisés davantage gagnants que les 5 % les plus modestes ; chômeurs perdants). Les montants (+3,3 %, +0,8 %, −1,1 %) attendent `ipp81_gain_top1_pct`, `ipp81_gain_bottom5_pct`, `ipp81_gain_unemployed_pct`. La phrase ISF/IFI et prélèvement forfaitaire unique relève du chapitre 4 (hors périmètre).
3. **Exonérations : le pire scénario comme seul exemple (gauche, moyenne) : partiellement appliqué.** Étape 11 : phrase des mêmes auteurs ajoutée (effets forts près du SMIC, faibles ou nuls plus haut ; un recentrage coûterait beaucoup moins d’emplois). Le seuil « environ 2,5 SMIC » n’est pas affiché tant que l’entrée (Bozio-Wasmer 2024, p. 67-68) n’existe pas ; `plfss2027_art7_relief_eur_bn` (3,7) non créé, donc non cité.
4. **« Financée par l’emprunt » asymétrique (gauche, moyenne) : appliqué pour ce chapitre.** Étape 8 : phrase supprimée (le reçu de l’étape 12 montre déjà la part empruntée de toute la dépense). Étape 13 : citation de la Cour ajoutée, les baisses « non compensées par des économies en dépenses » « ont creusé le déficit de l’État et accru sa dette » (RSPFP, juillet 2024, p. 35-36, fichier 08, §3). Quiz Q18, chapitres 4 et 6 : hors périmètre.
5. **Critique de Geerolf reprise à notre compte (gauche, basse) : appliqué.** « selon lui, l’écart devient faible » ; ajout « À notre connaissance, les auteurs de l’IPP n’ont pas encore répondu publiquement à cette note » (aucune réponse trouvée dans les fichiers 05 et 10). Paragraphe CDHR réduit à une phrase ; aucune prévision 2026 de la CDHR n’existe dans figures.json, donc seuls l’observé et l’annoncé restent.
6. **« Beaucoup » contre « d’autres » ; rang par habitant relégué (gauche, basse) : appliqué.** « Certains économistes » ; le rang 9e sur 27 (SPA, mention « estimation ») passe dans le texte de l’étape 4 et quitte « Pour aller plus loin ».
7. **Ensemble « taxer les riches » présenté comme « exact » (droite, haute) : appliqué pour le texte, partiellement pour les données.** Étape 10 : « Ce qui est plausible : selon notre propre synthèse des chiffrages publiés (aucun organisme n’a chiffré cet ensemble) … pourraient rapporter … une estimation, pas une recette garantie ». Phrase sur la succession ajoutée sous la forme « Une part notable de cette fourchette » et non « La moitié haute » : dans le fichier 07, §5, la composante succession (3 à 10 milliards) ne représente qu’environ la moitié de l’écart entre les deux bornes, la composante patrimoine en porte autant. Pastille source réécrite (« synthèse de la plateforme ; composante succession sans chiffrage indépendant »). Retrait de la CDHR (déjà en vigueur) de la fourchette et note de l’entrée : à faire dans figures.json et le fichier 07 (hors périmètre) ; la fourchette arrondie reste de 10 à 25 milliards selon l’audit.
8. **Étiquettes asymétriques (droite, haute) : appliqué pour ce chapitre.** Étape 9 : « non publiée dans une revue à comité de lecture » retiré du texte ; la pastille indique désormais que ni la note de l’IPP ni celle de F. Geerolf ne sont publiées dans une revue à comité de lecture. Rexecode reste « proche des organisations patronales » (étiquette d’orientation, pas de financement). Glossaire et chapitres 4 et 7 : hors périmètre.
9. **Correction « hors inflation » appliquée aux seules recettes (droite, moyenne) : partiellement appliqué.** Étape 3 : « Côté dépenses, la même correction joue dans l’autre sens : hors inflation, la dépense publique a augmenté en moyenne chaque année de 2005 à 2025, et encore en 2025 », sources en pastille (synthèse RSPFP de la Cour, 25 juin 2026 ; HCSP, *Focus Finances publiques*, 17 juillet 2026). Le taux de 1,4 % attend `te_volume_growth_2025_pct` et `te_volume_growth_avg_2005_2025_pct`.
10. **Conversion en jours réservée aux baisses d’impôts (droite, moyenne) : appliqué.** Étape 13 : hausses d’impôts de 2010 à 2014 (3,8 points de PIB `[[fig:tax_hikes_2010_2014_pts]]`) et hausse des dépenses de 2019 à 2025 (2,0 points de PIB, 12,7 jours `[[fig:te_change_2019_2025_pp]]` `[[yard:te_change_2019_2025_days]]`), avec le rappel que la réponse dépend de l’année de départ. Chapitre 4 : hors périmètre.
11. **Limites de la métaphore à moitié (droite, basse) : appliqué** à l’étape 2 (« Mais, comme un ménage, il paie des intérêts… »). Chapitre 7 : hors périmètre.
12. **Ratio 64 % / 48 % sans contexte ; concentration de l’IR retirée (droite, basse) : partiellement appliqué.** Étape 8 : phrase de lecture ajoutée. Vérification dans l'*Insee Première* n° 2022 : l’Insee écrit seulement « du fait notamment du poids de la fiscalité indirecte » ; il ne dit pas que la consommation des plus modestes est financée par les prestations. La phrase n’est donc pas attribuée à l’Insee et décrit la construction du ratio (taxes sur une consommation financée en partie par les prestations, rapportées à un revenu mesuré avant la plupart de ces prestations ; seules pensions et allocations chômage y sont incluses). « Près des trois quarts » de l’IR payés par les 10 % les plus aisés : non rétabli, `ir_top10_share_pct` n’existe pas (voir annexe A, A2).
13. **Formules du reçu sans « / 100 » (chiffres, basse) : appliqué** aux cinq lignes de l’étape 12 ; valeurs affichées inchangées.
14. **Deux nombres sans pastille (chiffres, basse) : appliqué.** « les quelque 75 foyers » devient « les foyers de milliardaires » ; « les deux tiers … 90 % restants » reçoit `[[calc:100 − top10_share_levies_2023_pct]]`.

**Réduction pour tenir le volume** : phrase « Nous ne plaçons donc jamais… » (étape 4), rappel de l’affectation des recettes (étape 6, déjà à l’étape 12), introduction de l’étape 10, fin de la note du reçu, formulations raccourcies à l’étape 13.

**Entrées à créer dans figures.json (propriétaire des données)** : `tax_gap_cour_range_eur_bn`, `tax_audit_assessed_2024_eur_bn`, `tax_audit_collected_2024_eur_bn`, `ipp81_gain_top1_pct`, `ipp81_gain_bottom5_pct`, `ipp81_gain_unemployed_pct`, seuil Bozio-Wasmer de 2,5 SMIC, `te_volume_growth_2025_pct`, `te_volume_growth_avg_2005_2025_pct`, `ir_top10_share_pct` ; et correction de `tax_rich_package_eur_bn` (retrait de la CDHR, note). Les chiffres correspondants seront ajoutés au texte quand ces entrées résoudront.

### Passe « chapitres » du 25 octobre 2026 (intégration des données et réduction)

*Volume du texte visible, mesuré par script (titre, blocs affichés `>`, questions des interactions ; hors pastilles, spécifications, commentaires et notes) : 2 091 mots avant, 1 992 après. Cible : 1 500 à 2 200 mots.*

**Données intégrées (ancienne annexe A ; ce chapitre ne contenait aucune pastille provisoire ni bloc d’attente de données)**

1. Étape 3 : `po_2017_eur_bn` (1 038,1), `po_change_2017_2025_nominal_pct` (+25,7 %), `po_change_2017_2025_real_pct` (+2,5 %) et le sondage Elabe par la pastille `[[quiz:M10]]` (72 %). L’interrupteur « % du PIB / euros » n’est plus bloqué (deux points 2017 et 2025).
2. Étape 4 : passerelle obligatoire de la fiche 4.7 avec `refundable_tax_credits_2024_eur_bn` (19,6 Md€) ; la mention de l'« estimation plus ancienne du PIB » est retirée (cause secondaire, renvoyée à la page de méthode).
3. Étape 5 : réponse au contre-argument chiffrée avec le coin socio-fiscal (`oecd_tax_wedge_single_2025_pct` 47,2 %, rang 3 sur 38), dénominateur « coût du travail » explicite.
4. Étape 6 : les cinq montants de l’annexe A1 ; la mise en production de la barre empilée n’est plus bloquée.
5. Étape 8 : `levies_share_income_d1_2022_pct` (64 %) et `levies_share_income_d10_2022_pct` (48 %), année 2022 et dénominateur « revenu avant transferts » précisés.
6. Étape 9 : taux IPP (26 % / 46 %) dans l’encadré, taux Geerolf (25,1 % / 26,8 %) dans la réponse ; même statut « estimé » pour les deux camps.
7. Pour aller plus loin : `employer_ssc_2024_pct_gdp` (10,0 % du PIB), `tax_revenue_per_capita_pps_2024_rank` (9e sur 27).

**Non résolu ou réécrit faute de donnée**

8. Étape 7 : « près des trois quarts » (DGFiP) n’a pas de valeur dans figures.json ; la phrase est supprimée plutôt que laissée sans pastille.
9. Étapes 4 et 8 : séries de graphique (OCDE par pays, dixièmes Insee) toujours à livrer comme fichiers de données.

**Réduction**

10. Coupés ou condensés : spécifications des visuels, phrases de transition redondantes (étapes 1, 2, 3, 12, 13), seconde cause de l’écart Insee/OCDE, rappel « niches sociales » et allègements généraux de l’étape 11 (déplacés vers « Pour aller plus loin »), phrase sur la concentration de l’IR.
11. Conservés : ouverture « Estimez d’abord », étalons (habitant, calendrier, ménage, jours de dépense), comparaison internationale avec année et groupe, deux encadrés « Le meilleur contre-argument », transition vers le chapitre 4.

**Vérification des pastilles**

12. Chaque pastille `[[fig:]]`, `[[yard:]]` et `[[quiz:]]` résout dans les fichiers de données (`python3 -I validate.py` : aucune erreur pour ce chapitre) ; chaque valeur affichée a été comparée par script à la valeur stockée, au format français (virgule décimale, arrondi du glossaire §2.2). Écarts d’arrondi assumés : 18 913,6 → « environ 18 900 € » ; 91,83 → 91,8 ; 3,07 → 3,1 ; 0,4 affiché « moins de 0,4 » (note de l’entrée).

### Relecture du 25 octobre 2026 (chiffres, neutralité, français)

*Tous les calculs ont été refaits (5 octobre et 29 novembre, 2 506 €, 2,1 à 5,3 jours, 6,6 à 16,5 %, 19,6 jours, 1 331 €, 13,2 jours, 40,9 %, lignes du reçu).*

**Chiffres**

1. Étape 2 (visuel) : bande « emprunt » corrigée de 30 à 32 jours (`deficit_days` = 32,3).
2. Étape 2 : « environ 2 506 € » devient « 2 506 € » ; pastilles ajoutées (revenu de référence, facteur d’échelle, `po_2025_eur_bn`).
3. Étape 4 : le 44,2-44,3 % est le concept européen estimé par la Cour, pas une « mesure internationale » ; libellé corrigé, conditionnel ajouté.
4. Étape 6 : source de `po_2025_eur_bn` corrigée (*Insee Première* n° 2106).
5. Étape 9 : « moins de 0,4 milliard » pour le seul acompte de décembre 2025 ; « environ 2 milliards » annoncés.
6. Étape 10 : mention « ordre de grandeur » (montants 2027 sur dénominateurs 2025).
7. Étape 12 : pastille de calcul sur chaque ligne du reçu ; dénominateur explicite de la ligne « emprunt ».
8. Étape 13 : le chiffre de la Cour est une évaluation pour 2023.
9. Étape 11 (visuel) : 91,83 arrondi à 91,8 partout.

**Neutralité**

10. Étape 13 : le visuel ne « couvre » plus la bande du déficit ; comparaison de taille, lecture opposée (Rexecode), rappel des dépenses.
11. Étape 10 : même gabarit « Ce qui est exact » / « Ce qui ne tient pas » pour les deux idées reçues.
12. Étape 9 : présentation factuelle de la critique de Geerolf, objection du gouvernement, effet de calendrier, deux lectures du rendement de la CDHR.
13. Étape 5 : la réponse ajoute le point le plus fort de l’autre camp (poids sur le travail) et sa propre réponse.
14. Étapes 8, 11, 12 : formulations chargées retirées (« payés par les contribuables de demain ») ou rééquilibrées.

**Français et glossaire**

15. Étape 0 : énumération « Impôts, cotisations, CSG, TVA » remplacée. Étape 2 : « une entreprise n’est pas un habitant » reformulé. Étape 4 : « recettes fiscales totales, cotisations sociales comprises ». Étape 5 : « excédent des comptes publics ». Étape 7 : CSG « avec des taux réduits ou des exonérations pour les plus modestes ». Étape 12 : « aides au logement » / « logement et équipements collectifs ».
16. Typographie : espaces insécables, virgule décimale et apostrophes en saisie ordinaire (glossaire, §2 : filtre au rendu).

**Reste à faire**

- Livrer les fichiers de données des séries de graphique (OCDE par pays, dixièmes Insee).
- Poser les liens de « Pour aller plus loin » quand les fiches thématiques auront leurs URL.
