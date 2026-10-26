# 05 - Taxation: level and structure of compulsory levies, international comparison, distribution

*Research file for the public-finance education platform. Compiled 2026-10-25. All web sources accessed 2026-10-25 unless stated otherwise. Raw downloads are under `research/data/raw/taxation/`; cleaned and derived CSVs are under `research/data/`.*

---

## 1. Scope and definitions

| Term | Definition used here | Why it matters |
|---|---|---|
| *Prélèvements obligatoires* (PO, compulsory levies) | Insee national-accounts aggregate: taxes (ESA codes D2, D5, D91) + **actual** compulsory social contributions (D611 + D613), **minus** imputed social contributions (D612), **minus** taxes and contributions assessed but unlikely to be collected (D995), **minus all tax credits** (both the part used against tax due and the part paid out), including taxes paid to EU institutions. | This is the French headline: **43.6% of GDP in 2025**. It is the narrowest of the common measures. |
| OECD "tax-to-GDP ratio" | Taxes (OECD classification 1000-6000) including compulsory social security contributions paid to general government; non-wastable (payable) tax credits are handled differently from Insee; excludes non-tax compulsory payments (e.g., mandatory private pension contributions). | France = **43.5% in 2024** (OECD), vs. 42.7% for Insee PO in the same year. |
| Eurostat / DG TAXUD "total taxes incl. compulsory actual social contributions" | ESA 2010 aggregate used in *Taxation Trends in the EU*. | France = **43.5% in 2024**, same as OECD. |
| Eurostat `gov_10a_taxag` "Total receipts from taxes and social contributions **including imputed** social contributions" (D2_D5_D91_D61_M_D995) | Broadest: includes imputed contributions (notional employer contributions for civil-servant pensions paid directly by the State). | France = **45.3% in 2024**; it overstates the "burden" relative to the other measures by ~1.8 pt for France. |
| % of GDP vs % of total taxation | Every table below states which denominator it uses. "% of PO" or "% of total taxation" means a share of the levy total, not of GDP. | Structure comparisons (e.g., "France relies little on income tax") are usually expressed in % of total taxation; level comparisons in % of GDP. |
| *CSG* (*contribution sociale généralisée*, general social contribution) and *CRDS* (*contribution au remboursement de la dette sociale*, social-debt repayment contribution) | Flat-rate levies on almost all income (wages, pensions, capital income, benefits). Classified as **taxes on income (D51)** in ESA and as **personal income tax (1100)** by the OECD, **not** as social contributions. | This is why France's "personal income tax" looks average in OECD tables while its *impôt sur le revenu* (IR, progressive income tax) alone is small. |
| *Dépenses fiscales* (tax expenditures, "*niches fiscales*") | Derogations from a reference tax norm that reduce State tax revenue, listed in the *Voies et moyens* annex, tome II, of each budget bill. | Totals depend heavily on the chosen "norm" (see section 7). |

---

## 2. Key figures (summary table)

| # | Indicator | Value | Unit | Data year | Source (publication date) |
|---|---|---|---|---|---|
| 1 | *Taux de prélèvements obligatoires* (Insee, net of tax credits, incl. EU) | **43.6** | % of GDP | 2025 (provisional) | Insee, IP n°2106 (May 2026) and series 2381412 (28 Aug 2026) [1][2] |
| 2 | Same, 2024 (revised; was 42.8 in March 2026) | 42.7 | % of GDP | 2024 (semi-final) | Insee [2] |
| 3 | PO amount | **1,305.1** | EUR bn | 2025 | Insee table 3.216/3.217 (28 Aug 2026) [3] |
| 4 | Implied nominal GDP (PO / PO rate) | 2,991 | EUR bn | 2025 | computed from [3] |
| 5 | Public expenditure (ESA, total expenditure TE) | **1,714.1 = 57.3** (Eurostat, Oct 2026; canonical, file 00 row 1); Insee May 2026: 1,714.2 | EUR bn / % of GDP | 2025 | Eurostat `gov_10a_main` (21 Oct 2026); Insee IP n°2106 [1] (confirms user figure) (aligned 2026-10-25 with file 00: was 1,714.2 only) |
| 6 | Public deficit | 151.6 = 5.1 (Oct 2026 EDP notification; 152.5 in Insee IP 2106, May 2026) | EUR bn / % of GDP | 2025 | Eurostat gov_10dd_edpt1 (21 Oct 2026); Insee IP n°2106 [1] |
| 7 | PLF 2027 forecast of PO rate | 43.9 (2026), **44.2 (2027)** | % of GDP | forecast | PLF 2027, *article liminaire* (filed 1 Oct 2026) [4] |
| 8 | PO peak since 1959 (Insee) | 45.3 (2017); 45.0 (2022) | % of GDP | 2017 / 2022 | Insee series [2] |
| 9 | OECD tax-to-GDP (total tax revenue incl. SSC), France | **43.5**, rank **2nd of 36** OECD countries reporting 2024 (Denmark 45.2) | % of GDP | 2024 | OECD Revenue Statistics 2025 (Dec 2025) [5][6] (corrected 2026-10-25 to match file 00 row 30: was "2nd/38"; the OECD country note's "2nd of 38" fills Australia and Japan with 2023 data, see note under table 5.1A) |
| 10 | OECD average | 34.1 (mean); median 35.2 (our calc.) | % of GDP | 2024 | [5][6] |
| 11 | EU-27 tax-to-GDP (DG TAXUD measure) | 39.4; France 43.5, rank 2nd | % of GDP | 2024 | EC DG TAXUD, Taxation Trends data (31 Mar 2026) [7] |
| 12 | Tax revenue per capita (incl. imputed SSC) in PPS | France 17,800 vs EU-27 aggregate 16,157; France ranks **9th of 27** | PPS per inhabitant | 2024 | our calc. from Eurostat `gov_10a_taxag` × `nama_10_pc` [8][9] |
| 13 | Social contributions (actual, effective) | 446.3 = 14.9 | EUR bn / % of GDP | 2025 | Insee 3.217 [3] |
| 14 | Employer social contributions (actual) | 10.0 (OECD/Eurostat); rank 2nd OECD, 1st in panel | % of GDP | 2024 | Eurostat `gov_10a_taxag` D611 [8]; OECD [6] |
| 15 | CSG + CRDS | 165.9 = 5.5 | EUR bn / % of GDP | 2025 | Insee 3.217 [3] |
| 16 | *Impôt sur le revenu* (IR) net of credits (national accounts) | 94.3 = 3.2 | EUR bn / % of GDP | 2025 | Insee 3.217 [3] (computed: 103.6 - 7.2 - 2.1) |
| 17 | VAT (*TVA*) | 208.8 = 7.0 | EUR bn / % of GDP | 2025 | Insee 3.217 [3] |
| 18 | Corporate income tax (*IS*) net of credits | 59.3 = 2.0 (+7.5 bn exceptional surtax) | EUR bn / % of GDP | 2025 | Insee 3.217 [3] |
| 19 | Property taxes (OECD 4000) | 3.4, rank 2nd/37; OECD mean 1.6 | % of GDP | 2024 | OECD [6] |
| 20 | Inheritance and gift taxes (*DMTG*) | 21.1 = 0.70 (OECD 4300: 0.7, rank **1st**) | EUR bn / % of GDP | 2025 / 2024 | Insee [3]; OECD [6] |
| 21 | Tax wedge, single worker at average wage | **47.2** (OECD avg 35.1), rank 3rd/38 | % of labor cost | 2025 | OECD Taxing Wages 2026 (Apr 2026) [10] |
| 22 | Implicit tax rate on labor | 38.8 (EU-27 37.1), rank 6th | % | 2024 | DG TAXUD [7] |
| 23 | Income-tax households paying net IR | 19.6 m of 41.5 m = **47.2%** (so 52.8% pay none) | % of *foyers fiscaux* | income 2024 (tax 2025) | DGFiP Statistiques n°41 (Nov 2025) [11] |
| 24 | Share of IR paid by top 10% of *foyers* (by RFR per share) | "nearly three quarters" | % of IR | income 2024 | DGFiP n°41 [11] |
| 25 | Share of **all** levies paid by top 10% of individuals (Insee distributed accounts) | 393.8 of 1,241.1 bn = **31.7%** (2022); **422.8 of 1,270.9 bn = 33.3% (2023)** | % of all levies | 2022 / **2023** | Insee IP n°2022 (Nov 2024) [12]; *superseded by* Insee Analyses n°118 (16 Apr 2026) [25] (corrected after verification: the file stated that no 2023 edition existed; 2023 is now the latest year, with a revised method that also attributes undistributed corporate profits) |
| 26 | Net beneficiaries of "broadened redistribution" (incl. public services) | 57% (2022); **56% (2023)** of individuals | % of population | 2022 / **2023** | Insee IP n°2022 [12]; Insee Analyses n°118 [25] |
| 27 | Effective total tax rate, top 0.0002% ("billionaires", ~75 households) | 26% (vs 46% for top 0.1%); personal taxes ~2% of economic income for top 0.001% | % of economic income | 2016 | IPP Note n°92 (June 2023, updated 2025) [13] |
| 28 | Tax expenditures (*dépenses fiscales*) | 91.83 (2025, PLF 2026); 89.40 (2024, final); 474 measures | EUR bn | 2025 / 2024 | Cour des comptes, NEB 2025 (Apr 2026) [14] |
| 29 | Tax expenditures in PLF 2027 (unweighted sum of itemized costs, our calc.; not an official total) | 91.7 (2025 realized), 92.0 (2026), 83.9 (2027) over 459 items | EUR bn | 2025-2027 | PLF 2027 VM tome II annex 1 [15] (verified 2026-10-25: spreadsheet re-downloaded through the browser and re-summed; 91,664 / 92,019 / 83,919 MEUR). **For the website, use the Cour des comptes' 91.83 bn (2025) in row 28**; the 2027 sum is depressed by 83 "nc" (not costed) items. |
| 30 | Social-contribution exemptions (*niches sociales*), ROBSS scope (*régimes obligatoires de base de sécurité sociale*, mandatory basic social-security schemes) | Total incl. base exemptions and DFS: **93.2 (2024), 91.0 (2025), 84.4 (2026f)**; general reductions *allègements généraux* (base schemes) 65.0 (2025) → 57.4 (2026f) → 52.0 (2027f) | EUR bn | 2024-2027 | PLFSS 2027 annex 4 (Oct 2026) [27] (updated 2026-10-25: was 90.8 for 2024 and 64.9 for the general reductions, from PLFSS 2026 annex 4 [16]; the 2026 drop is partly a scope shift to Unédic and Agirc-Arrco, see 7.2) |
| 31 | "Public aid to companies" | 211 (Senate, 2023); 157 (Clersé study published 2022; corrected after verification: was "Clersé, 2019"; the data year is not stated in the cited source); 108 (Senate "strict"); 112 (HCP, excl. contributions) | EUR bn | various | Senate commission (July 2025) via Public Sénat [17] |

> Starting figures supplied by the user: **43.6% PO 2025 - confirmed** (Insee, May and Aug 2026). **Public expenditure 1,714 bn / 57.3% - confirmed** (Insee IP 2106). Note that the PLF 2027 uses a different convention (expenditure **excluding tax credits**): 1,694 bn = 56.6% of GDP for 2025 [4]. The Drees 31.9% figure belongs to the social-protection file and was not re-verified here.

---

## 3. Level of compulsory levies

### 3.1 France 1959-2025 (Insee, % of GDP, net of tax credits, incl. EU levies)

| Year | PO rate | Year | PO rate | Year | PO rate |
|---|---|---|---|---|---|
| 1960 | 30.3 | 2000 | 43.4 | 2017 | **45.3** (series peak) |
| 1970 | 34.0 | 2005 | 42.7 | 2019 | 44.0 |
| 1975 | 35.6 | 2009 | 41.2 | 2020 | 44.3 |
| 1980 | 39.9 | 2010 | 41.4 | 2022 | 45.0 |
| 1985 | 42.3 | 2012 | 43.9 | 2023 | 43.2 |
| 1990 | 41.2 | 2013 | 44.8 | 2024 | 42.7 |
| 1995 | 42.3 | 2015 | 44.5 | **2025** | **43.6** |

*Source for every row: Insee, "Taux de prélèvements obligatoires rapportés au produit intérieur brut", series 1959-2025, updated 28 Aug 2026 [2]; CSV: `data/insee_taux_prelevements_obligatoires_1959_2025.csv`.*

Key readings:
- The bulk of the rise happened **1960-1985** (+12 pt); since 1985 the rate has oscillated in a ~41-45% band. The PO rate in 2025 (43.6) is about 1 pt below its 2013-2016 level (44.5-44.8) and close to 2012 (43.9) (corrected after verification: was "about where it was in 2013-2016").
- 2025 increase (+0.9 pt): Insee attributes it to spontaneous growth of IR (strong 2025 *régularisations* after high 2024 real incomes), DMTO (*droits de mutation à titre onéreux*, real-estate transfer duties) rebounding, and **23.0 bn of new measures**, including 8.0 bn of temporary surtaxes (exceptional contribution on large companies' profits, maritime freight) [1].
- PLF 2027 (filed 1 Oct 2026) forecasts **43.9% in 2026 and 44.2% in 2027** - i.e., a new all-time high would be approached only if the 2017 peak (45.3) is exceeded, which is not forecast. The 2023-2027 programming law (LPFP) had planned 44.4% for 2027 [4]. Fiscal consolidation planned in PLF 2027 is described as "equitably split" between spending and revenue (*mise en cohérence de dépenses fiscales*, "fight against rents") [4].
- HCFP (*Haut Conseil des finances publiques*, the fiscal council), opinion n°HCFP-2026-5 of 25 Sep 2026 [26]: it judges the government's **2027 GDP growth assumption (1.0%) "optimistic"**, but finds the forecast of **spontaneous PO growth realistic** (+2.3%, elasticity 0.8). Total PO growth would be +3.6% (+48 bn), including about +17 bn of net new measures, which the HCFP says it could not assess in detail; PO would reach 1,338.5 bn (43.9% of GDP) in 2026 and 1,386.3 bn (44.2%) in 2027 [26]. (Corrected after verification: the file said the HCFP called "the government's 2027 forecasts" optimistic, citing only press coverage. The word applies to the growth forecast, not to the revenue forecasts.)

### 3.2 Levies by beneficiary (2025, Insee table 3.216)

| Beneficiary | EUR bn | % of GDP | % of total PO |
|---|---|---|---|
| Central government (*APUC*) | 378.8 | 12.7 | 29.0 |
|   of which State (*État*) | 357.7 | 12.0 | 27.4 |
|   of which other central bodies (*ODAC*) | 21.1 | 0.7 | 1.6 |
| Local government (*APUL*) | 190.2 | 6.4 | 14.6 |
| Social security (*ASSO*) | **733.2** | **24.5** | **56.2** |
|   of which taxes (CSG, VAT shares, etc.) | 299.1 | 10.0 | 22.9 |
|   of which social contributions | 434.1 | 14.5 | 33.3 |
| EU institutions | 2.9 | 0.1 | 0.2 |
| **Total** | **1,305.1** | **43.6** | **100** |

*Source for every row: Insee, Comptes nationaux base 2020, table 3.216 (28 Aug 2026) [3]; CSV `data/derived_insee_PO_by_subsector_2023_2025.csv`. Taxes are recorded after tax-revenue transfers between sub-sectors (e.g., VAT shares allocated to social security and local authorities).*

**Pedagogical point:** more than half of all compulsory levies (56%) go to social security funds (pensions, health, family, unemployment via Unédic), not to the State budget. The State keeps ~27%. Debates about the State (State deficit 128.1 bn in 2025 **in national accounts**, Insee IP 2106; corrected after verification: was "the State's budget (deficit 128 bn)", but this is the ESA *solde de l'État*, not the budget-accounting deficit) cover only a minority of the levy flow.

---

## 4. Structure of levies (France, 2025, Insee national accounts)

All amounts in EUR bn; % of GDP uses GDP = 2,991 bn (implied by Insee); % of PO uses PO = 1,305.1 bn. Source for every row: Insee table 3.217 "Principaux impôts par catégorie", base 2020, 28 Aug 2026 [3]; derived CSV `data/derived_insee_main_taxes_2025_pct.csv`.

| Levy | 2005 | 2024 | **2025** | % of GDP 2025 | % of PO 2025 | Main beneficiary |
|---|---|---|---|---|---|---|
| Actual social contributions (employer + employee + self-employed) | 279.5 | 432.4 | **446.3** | 14.9 | 34.2 | Social security |
| VAT (*TVA*) | 126.7 | 207.8 | **208.8** | 7.0 | 16.0 | State, social security, local (shares) |
| CSG | 71.5 | 153.1 | **156.6** | 5.2 | 12.0 | Social security |
| CRDS | 5.2 | 9.1 | 9.3 | 0.3 | 0.7 | CADES |
| *Prélèvement de solidarité* and other social levies on capital income | 2.2 | 14.6 | 14.4 | 0.5 | 1.1 | Social security / State |
| IR (*impôt sur le revenu*) before credits | 52.5 | 96.0 | 103.6 | 3.5 | 7.9 | State |
|   minus IR credits (used + paid out) | -3.1 | -8.9 | -9.3 | -0.3 | -0.7 | |
|   **IR net** | 49.4 | 87.1 | **94.3** | 3.2 | 7.2 | |
| Corporate tax (*IS*) before credits | 42.9 | 68.0 | 69.5 | 2.3 | 5.3 | State |
|   minus IS credits (incl. CIR) | -0.9 | -10.7 | -10.1 | -0.3 | -0.8 | |
|   exceptional contribution on large companies' profits | - | - | 7.5 | 0.25 | 0.6 | State (temporary) |
| Energy excise (*TICPE*, now *accise sur les énergies*) | 24.6 | 30.2 | 30.5 | 1.0 | 2.3 | State, regions |
| Electricity / gas excises | 3.3 | 8.0 | 11.7 | 0.4 | 0.9 | State |
| Tobacco excise | 9.3 | 13.7 | 13.6 | 0.45 | 1.0 | Social security |
| Wage-bill/payroll taxes (D291: *taxe sur les salaires*, *versement mobilité*, training levies, *forfait social*...) | 21.8 | 58.1 | 60.1 | 2.0 | 4.6 | Various |
| Other production taxes (D292) | 52.4 | 71.8 | 72.7 | 2.4 | 5.6 | Mostly local |
|   *Taxe foncière* (property tax) | 19.4 | 42.9 | 44.2 | 1.5 | 3.4 | Local |
|     paid by households | 10.8 | 26.2 | 27.0 | 0.9 | 2.1 | |
|   *CFE* (business property tax) | n/a | 7.7 | 8.1 | 0.3 | 0.6 | Local |
|   *CVAE* (business value-added tax, being phased out) | n/a | 3.9 | **3.7** (15.2 in 2019) | 0.13 | 0.3 | Local |
|   *C3S* (company social solidarity levy on turnover) | 4.3 | 5.2 | 5.3 | 0.18 | 0.4 | Social security |
| Registration duties (all) | 9.6 | 17.2 | 20.2 | 0.7 | 1.5 | |
|   of which *DMTO* (real-estate transfer duties, local) | 8.6 | 14.7 | 17.7 | 0.6 | 1.4 | *Départements*, communes |
| Inheritance + gift duties (*DMTG*) | 8.9 | 20.8 | **21.1** | 0.70 | 1.6 | State |
|   successions / donations | 7.5 / 1.4 | 15.9 / 4.9 | 16.1 / 5.0 | | | |
| *IFI* (real-estate wealth tax; ex-ISF) | 3.0 (ISF) | 2.7 | **2.7** (ISF 2017: 5.1) | 0.09 | 0.2 | State |
| *Taxe d'habitation* (residual, second homes) | 11.3 | 3.2 | 2.9 | 0.10 | 0.2 | Local |
| *Contribution différentielle sur les hauts revenus* (CDHR, new 20% minimum tax) | - | - | 0.37 | 0.01 | 0.03 | State |
| Imputed social contributions (excluded from PO) | 31.2 | 51.2 | 52.4 | 1.75 | (excluded) | |
| **Total PO** | **752.4** | **1,254.0** | **1,305.1** | **43.6** | **100** | |

Readings:
1. **Labor is the main base.** Social contributions + CSG on earned income + payroll taxes dominate. DG TAXUD classifies 51.5% of French total taxation as "taxes on labor" in 2024 (EU-27: 51.5%), 24.7% as consumption (EU-27: 26.8%), 23.7% as capital (EU-27: 21.6%) [7].
2. **CSG (156.6 bn) is 1.7 times the net IR (94.3 bn).** The French "income tax" in the international sense is mostly a flat tax (CSG), which is why France's progressive income tax looks small.
3. **The "taxes on the rich" are small items in EUR terms:** IFI 2.7 bn, CEHR ~2 bn (DGFiP, 2024 income) [11], CDHR 0.37 bn booked in 2025 (first installment only; final yield not yet known) [3]. For scale, the 2025 Maastricht deficit is **151.6 bn** (October 2026 EDP notification, canonical; 152.5 bn in the May 2026 vintage): IFI = 1.8% of the deficit; restoring ISF at its 2017 yield (5.1 bn in national accounts) would add ~2.4 bn gross, i.e., ~1.6% of the deficit, before behavioral responses. (Calculation ours from [1][3]; corrected 2026-10-25 to align with file 00 row 31: was "152.5 bn" and "~1.5%".)
4. **Production taxes** (D29, 4.4% of GDP in 2024) are ~1.8x the EU-27 aggregate (2.4%) [8] even after the CVAE cuts (15.2 bn in 2019 to 3.7 bn in 2025). France ranks 2nd in the EU-27; Sweden is 1st (10.1%) because its general payroll tax is classified in D29 (added after verification).

---

## 5. International comparison

Groups: OECD-38; EU-27; euro area EA-20 (the 2024 membership; Bulgaria joined on 1 Jan 2026, so Eurostat now also publishes EA-21); panel = France, Germany, Italy, Spain, Netherlands, Belgium, Sweden, Denmark. "Mean" = unweighted country mean (our calc.); "aggregate" = GDP-weighted figure published by Eurostat/OECD. Rank 1 = highest.

### 5.1 Tax-to-GDP level

**A. OECD Revenue Statistics 2025 (taxes + SSC, % of GDP)** - source for all rows: OECD SDMX `DSD_REV_COMP_OECD@DF_RSOECD`, downloaded 2026-10-25 [6]; CSV `data/oecd_revenue_statistics_2025_pct_gdp.csv`. 2024 is provisional; Australia and Japan lack 2024 data (n = 36).

| Year | France | OECD avg (published) | OECD median (our calc.) | FR rank / n | Panel mean | Panel median | FR panel rank | FR minus OECD avg |
|---|---|---|---|---|---|---|---|---|
| 2004 | 42.8 | 32.2 | 32.2 | 4 / 38 | 40.1 | 41.0 | 4 / 8 | +10.6 |
| 2014 | 45.4 | 32.9 | - | 2 | - | - | - | +12.5 |
| 2017 | 46.2 | 33.3 | - | **1** | - | - | - | +12.9 |
| 2023 | 43.9 | 33.7 | 35.0 | 2 / 38 | 40.7 | 41.6 | 2 / 8 | +10.1 |
| **2024** | **43.5** | **34.1** | **35.2** | **2 / 36** | **41.1** | **42.0** | **2 / 8** | **+9.4** |

2024 panel values: DK 45.2, **FR 43.5**, IT 42.8, BE 42.6, SE 41.4, NL 38.5, DE 38.0, ES 36.7 [6]. France was ranked 1st in 2017, 2018 and 2022 and 2nd in 2011-2015, 2019-2021, 2023-2024 (our calc. from [6]).

*Note (added after verification): the "OECD avg (published)" column is the OECD's own average (34.06 in 2024). The unweighted mean of the 36 countries reporting 2024 is 34.17, which is the 34.2 shown in table 5.2. The OECD country note ranks France "2nd among the 38 OECD countries" by using 2023 data for Australia and Japan; on 2024 data alone, France is 2nd of 36. In 2016 France ranked 3rd.*

**20-year gap evolution:** France's gap over the OECD average was ~10-11 pt in 2000-2010 (low point 10.1 in 2007), widened to ~12-13 pt in 2012-2018 (the 2011-2013 tax increases), and has narrowed to **9.4 pt in 2024**, the smallest since at least 2000, because the OECD average rose (32.9 to 34.1) while France fell back from its 2017 peak.

**B. Eurostat ESA aggregates (% of GDP)** - source: Eurostat `gov_10a_taxag`, updated 21 Oct 2026 [8]; CSV `data/eurostat_gov_10a_taxag_PC_GDP.csv`; verification recomputation `data/05_verify_recomputed_stats.csv`. Eurostat has 2025 data for **20 EU member states**. 2025 data are **not yet available for France, Germany, Netherlands, Finland, Poland, Cyprus and Malta** (corrected after verification: the file said 22 countries and listed only four missing). 2024 is the latest common year.

| Indicator (2024) | France | EU-27 aggregate | EU-27 mean | EU-27 median | FR rank EU-27 | EA-20 mean / median | FR rank EA-20 | Panel mean / median | FR rank panel |
|---|---|---|---|---|---|---|---|---|---|
| Taxes + actual SSC, **compulsory and voluntary** (excl. imputed; code D2_D5_D91_D61_M_D612_M_D614_M_D995) (corrected after verification: this row was labeled "actual compulsory SSC") | 43.5 | 39.3 | 37.0 | 36.8 | 2 / 27 | 37.3 / 38.2 | **1 / 20** | 41.4 / 41.9 | 2 / 8 |
| Taxes + **compulsory** actual SSC only (code D2_D5_D91_D61_M_D611V_D612_M_M_D613V_D614_M_D995; the DG TAXUD concept) (row added after verification) | 43.5 | 39.2 | 36.9 | 36.7 | 2 / 27 | 37.3 / 38.1 | **1 / 20** | 41.1 / 41.5 | 2 / 8 |
| Taxes + all SSC **incl. imputed** | 45.3 | 40.2 | 37.7 | 37.6 | 2 / 27 | 38.1 / 38.4 | **1 / 20** | 42.2 / 42.0 | 2 / 8 |

Eurostat gap series (incl. imputed): France minus EU-27 aggregate = +3.5 pt (1995), +4.9 (2004), +6.6 (2014), +7.5 (2017, max), **+5.1 (2024)** (our calc. from [8]). CSV `data/eurostat_gov_10a_taxag_PC_GDP.csv`.

**C. Per capita in purchasing-power standards (PPS)** - our calc.: tax ratio (incl. imputed SSC) × GDP per capita in PPS (Eurostat `nama_10_pc`, unit CP_PPS_EU27_2020_HAB) [8][9]; CSV `data/derived_tax_per_capita_pps.csv`.

| Year | France | EU-27 aggregate | EU-27 mean / median | FR rank EU-27 | EA-20 mean / median | FR rank EA-20 | Panel mean / median | FR rank panel |
|---|---|---|---|---|---|---|---|---|
| 2004 | 10,528 | 8,395 | 7,668 / 6,720 | 8 | 8,130 / 7,335 | 6 | 10,754 / 10,598 | 5 |
| 2024 | 17,800 | 16,157 | 15,759 / 13,577 | **9** | 16,548 / 14,757 | 7 | 18,931 / 18,971 | **6** |

2024 panel (PPS per head): DK 23,562; BE 21,039; NL 20,941; DE 19,226; SE 18,715; **FR 17,800**; IT 16,590; ES 13,577.

> **Important nuance for the platform:** France is 2nd in the EU in levies **as a share of GDP**, but only **9th in levies per inhabitant in PPS**, below Germany, the Netherlands, Belgium, Denmark, Sweden. High ratios partly reflect lower GDP per capita, not only higher tax amounts per person. This cuts both ways: it means France does not collect "more euros per citizen" than its northern neighbors, but it also means the levy weighs more relative to what the economy produces.

### 5.2 Tax structure vs. OECD and panel (% of GDP, 2024)

Source for all rows: OECD Revenue Statistics 2025 SDMX [6]; ranks among 36-37 reporting OECD countries (our calc.).

| Category (OECD code) | France | OECD mean | OECD median | FR rank OECD | Panel mean | Panel median | FR rank panel | 2004 France |
|---|---|---|---|---|---|---|---|---|
| Total (all) | 43.5 | 34.2 | 35.2 | 2 | 41.1 | 42.0 | 2 | 42.8 |
| Taxes on income & profits (1000) | 11.5 | 12.2 | 11.5 | 19 | 15.9 | 14.6 | **8 (last)** | 10.0 |
|   Personal income tax incl. CSG/CRDS (1100) | 9.3 | 8.3 | 8.3 | 16 | 12.3 | 10.7 | 7 | 7.4 |
|   Corporate income tax (1200) | 2.3 | 3.6 | 3.5 | 31 | 3.4 | 3.4 | 7 | 2.6 |
| Social security contributions (2000) | 14.7 | 9.1 | 10.3 | 6 | 11.1 | 12.6 | 2 | 15.8 |
|   employees (2100) | 3.6 | 3.3 | 3.1 | 12 | 3.1 | 3.0 | 4 | 3.9 |
|   employers (2200) | **10.0** | 5.1 | 5.1 | **2** | 6.8 | 7.4 | **1** | 10.7 |
| Payroll taxes (3000) | 2.0 | 0.4 | 0.0 | 3 | 0.9 | 0.0 | 2 | 1.2 |
| Property taxes (4000) | **3.4** | 1.6 | 1.3 | **2** | 1.9 | 1.8 | **1** | 3.2 |
|   recurrent on immovable property (4100) | 1.9 | 0.9 | 0.6 | 6 | 1.0 | 0.9 | 1 | 2.0 |
|   estate, inheritance, gift (4300) | **0.7** | 0.2 | 0.0 | **1** | 0.3 | 0.3 | 1 | 0.5 |
| Goods & services (5000) | 11.1 | 10.4 | 11.0 | 18 | 10.8 | 11.1 | 5 | 11.1 |
|   general consumption taxes, mainly VAT (5110) | 7.4 | 7.1 | 7.2 | 17 | 7.3 | 7.0 | 3 | 7.3 |
|   specific consumption taxes, excises (5120) | 3.4 | 2.5 | 2.5 | 7 | 2.8 | 2.7 | 2 | 3.5 |

Structure in % of total tax revenue, 2023 (OECD country note): SSC 33.2% (OECD 25.5%), personal income tax 21.5% (OECD 23.7%), VAT 16.6% (OECD 20.5%), property 7.9% (OECD 5.1%), corporate 5.4% (OECD 11.9%) [5].

*Ranks are among countries that report each category: n = 36 for total, 1100, 1200, 2000, 4100, 4300 and 5110; 37 for 1000, 3000, 4000, 5000 and 5120; 32 for 2200; 31 for 2100 (verification note).*

**Where France's excess over the OECD comes from (2024, % of GDP, FR minus OECD unweighted mean):** SSC +5.5 (of which employers +4.9), property +1.7, payroll +1.5, excises +0.8, PIT/CSG +1.0, VAT +0.3, other (6000) +0.6; offset by CIT -1.4 and smaller negative items (our calc. from [6]; items do not sum exactly to the 9.3-pt total gap because of minor categories and different country coverage). **In other words, social contributions, payroll and property taxes together (+8.8 pt, about 95% of the gap) account for almost the entire gap.** (Corrected after verification of rounding: was SSC +5.6, property +1.8, payroll +1.6, excises +0.9, CIT -1.3, subtotal +9.0. Exact values: +5.54, +1.75, +1.54, +0.82, -1.36, subtotal +8.83.) France does **not** stand out on taxes on corporate profits (31st of 36) or on the overall income-tax block (19th; last in the panel).

### 5.3 EU Taxation Trends (DG TAXUD, data released 30-31 Mar 2026)

Source for all rows: EC DG TAXUD, "Data on Taxation Trends" xlsx files (main aggregates, labour, capital, consumption, property, ITR) [7]; CSV `data/ec_taxation_trends_2026_selected.csv`.

| Indicator, 2024 | France | EU-27 | FR rank EU-27 | FR change 2014-2024 (pp) |
|---|---|---|---|---|
| Total taxes incl. compulsory actual SSC, % GDP | 43.5 | 39.4 | 2 | -2.1 |
| Taxes excl. SSC, % GDP | 28.8 | 26.45 (rounds to 26.4 or 26.5) | 7 | 0.0 |
| Taxes on labor, % GDP | 22.4 | 20.3 | 5 | -1.7 |
|   paid by employers, % GDP | **12.0** | 8.0 | **1** | -1.4 |
|   paid by employees, % GDP | 8.7 | 10.0 | 15 | -0.3 |
| Taxes on consumption, % GDP | 10.8 | 10.6 | 19 | -0.4 |
| Taxes on capital, % GDP | 10.3 | 8.5 | 4 | 0.0 |
|   on corporate income, % GDP | 2.9 | 3.3 | 19 | +0.2 |
|   on household capital income, % GDP | 1.9 | 1.1 | **1** | +0.4 |
|   on the stock of capital (wealth, property), % GDP | 3.7 | 2.1 | 2 | -0.4 |
| Property taxes, % GDP | 3.4 | 1.8 | **1** | -1.1 |
| Recurrent immovable property taxes, % GDP | 2.0 | 0.9 | **1** | -1.2 |
| Inheritance and gift taxes, % GDP | 0.71 | 0.26 | **1** | +0.2 |
| **Implicit tax rate (ITR) on labor**, % | **38.8** | 37.1 | 6 | **-2.6** |
| ITR on consumption, % | 16.4 | 16.5 | 21 | -0.8 |
| ITR on capital | not retrieved (separate release, metadata June 2026) | | | |

Readings: France's labor-tax intensity falls mainly on **employers**; the employee side is below the EU average. The ITR on labor fell 2.6 pt over 2014-2024 (CICE then *allègements généraux*), a larger drop than the EU-27 (-1.1).

### 5.4 Tax wedge on labor (OECD Taxing Wages 2026, published April 2026)

Source for all rows: OECD SDMX `DSD_TAX_WAGES_COMP@DF_TW_COMP`, measure AV_TW (% of labor cost), single worker without children [10]; CSV `data/oecd_taxing_wages_2026_tax_wedge_single.csv`. "EU-22" = EU members of the OECD.

| Wage level (single, no child) | Year | France | OECD mean / median | FR rank /38 | EU-22 mean / median | FR rank EU-22 | Panel (DE, IT, ES, NL, BE, SE, DK) | FR rank panel |
|---|---|---|---|---|---|---|---|---|
| 67% of average wage | 2005 | 46.5 | 32.3 / 35.4 | 4 | 39.4 / 41.8 | 4 | 47.3, 42.5, 35.7, 41.7, 49.4, 46.6, 35.8 | 4 |
| 67% of average wage | 2025 | **41.2** | 31.3 / 33.3 | 5 | 37.3 / 37.5 | 5 | 45.5, 38.5, 37.9, 27.5, 45.7, 38.8, 33.2 | 3 |
| 100% of average wage | 2005 | 50.5 | 35.4 / 38.5 | 4 | 43.1 / 43.4 | 4 | 52.1, 45.9, 39.0, 38.9, 55.5, 48.1, 38.7 | 3 |
| 100% of average wage | 2025 | **47.2** | 35.1 / 37.9 | **3** | 41.7 / 41.2 | 3 | 49.3, 45.8, 41.4, 35.9, 52.5, 41.1, 35.8 | 3 |
| 167% of average wage | 2005 | 53.3 | 39.7 / 41.6 | 5 | 47.5 / 47.7 | 5 | 54.9, 50.7, 42.4, 42.4, 60.9, 54.7, 47.7 | 4 |
| 167% of average wage | 2025 | **54.1** | 39.4 / 42.1 | 3 | 46.1 / 45.1 | 3 | 50.0, 54.3, 46.2, 42.2, 58.6, 48.8, 41.8 | 3 |

Country note: France's average-wage wedge was 50.4% in 2000 and 47.2% in 2025 (-3.3 pt; OECD -1.0 pt). For a one-earner couple with two children at the average wage, France is **2nd** in the OECD at 39.1% (OECD 26.2%) [10]. Income tax and employer SSC make up 82% of France's wedge [10].

**Reading:** two decades of targeted employer-contribution cuts lowered the wedge at low wages (-5.3 pt at 67% AW) while it **rose** at 167% AW (+0.8 pt). The French labor-tax system has become markedly more progressive across the wage distribution; the cost is a "low-wage trap" debate (very steep marginal rates as wages rise from 1 to 1.6-3 times the minimum wage because exemptions phase out) - see section 7.2.

---

## 6. Distribution: who pays?

### 6.1 Income tax (*IR*) concentration - DGFiP, income 2024 taxed in 2025

Source for all rows: DGFiP Statistiques n°41, "L'impôt sur le revenu 2024 a été plus dynamique que les revenus", November 2025 [11] (the impots.gouv.fr site was in maintenance on 2026-10-25; the PDF was retrieved from the Internet Archive copy of the official URL).

| Indicator | Value |
|---|---|
| Net IR assessed (after reductions and credits) | 92 bn EUR (+9.9%) |
| Tax households (*foyers fiscaux*) | 41.5 million |
| Households paying net IR | 19.6 million = **47.2%** |
| Households not paying net IR | ~21.9 million = **52.8%** |
| Top decile (by RFR per tax share): average IR | 16,395 EUR; 15.6% of its RFR; 14.2% of declared income |
| Top decile share of IR | "**nearly three quarters**" (*près des trois quarts*) |
| Bottom decile | net average **refund** of 31 EUR (refundable credits) |
| Flat-rate IR on capital income (PFU part) | 10 bn, of which 92% paid by top decile and 54.7% by top 0.1% |
| CEHR (3-4% surtax on income >250k/500k) | ~2 bn, all top decile |
| Reductions/credits (*RICI*) | 20 bn; 30.9% of households benefit; top decile average 2,538 EUR vs 49 EUR bottom decile |

Caveats to state on the platform: (i) "*foyer fiscal*" ≠ household or individual; (ii) non-taxpayers of IR still pay CSG on all their income (CSG ≈ 1.7× IR), VAT and other levies; (iii) the share of non-payers moved from ~55% to ~53% in one year because the 2025 scale was indexed by only 1.8% while incomes rose 4.9% (bracket creep) [11].

The PLF 2027 *Voies et moyens* tome II, annex 5, gives decile breakdowns (deciles of *foyers fiscaux* ranked by RFR, *revenu fiscal de référence*, reference taxable income) for the 8 largest IR tax expenditures. Examples for income 2024 (budget impact 2025): the top decile (RFR above EUR 121,526) receives **1.30 bn of the 6.50 bn** "home-employee" tax credit (*crédit d'impôt emploi d'un salarié à domicile*; 6.50 bn excludes the 0.38 bn *avance immédiate*, the final cost is 6.88 bn), and the top decile (RFR above EUR 59,112) receives **1.54 bn of the 5.35 bn** 10% pension allowance (*abattement de 10 % sur les pensions*) [15]. (Verified 2026-10-25 in the annex 5 xlsx, sheets "110246" and "120401", re-downloaded through the browser; saved as `data/raw/taxation/plf2027_browser/PLF2027_VM_T2_annexes2_5.csv.txt`. Was flagged as unverified.)

### 6.2 All levies, all transfers: Insee distributed national accounts (2022 data)

Source for all rows: Insee Première n°2022, "Transferts monétaires et services publics augmentent de 16 % le niveau de vie au milieu de l'échelle", November 2024 [12]. People ranked by decile of usual living standard; amounts EUR bn, 2022.

| Decile | D1 | D2 | D3 | D4 | D5 | D6 | D7 | D8 | D9 | D10 | Total |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Broadened primary income | 32.1 | 59.8 | 89.3 | 123.7 | 152.8 | 180.9 | 217.9 | 267.6 | 345.3 | 758.1 | 2,227.4 |
| All levies paid | 30.3 | 41.4 | 55.7 | 72.4 | 87.2 | 102.2 | 122.5 | 147.3 | 188.3 | **393.8** | **1,241.1** |
|   on products & production | 19.2 | 24.0 | 28.0 | 31.3 | 34.3 | 37.3 | 40.7 | 43.5 | 47.7 | 61.9 | 368.0 |
|   on income & wealth | 5.9 | 4.5 | 7.8 | 11.7 | 14.6 | 18.3 | 24.7 | 31.8 | 48.9 | 186.1 | 354.3 |
|   social contributions | 5.2 | 12.9 | 20.0 | 29.4 | 38.2 | 46.6 | 57.1 | 72.0 | 91.7 | 145.7 | 518.8 |
| Net transfer (received - paid) | +95.8 | +98.4 | +78.0 | +59.4 | +33.9 | +18.8 | -2.2 | -35.7 | -70.5 | **-275.8** | 0 |
| % of individuals net beneficiaries | 99 | 98 | 92 | 78 | 58 | 46 | 37 | 27 | 23 | 17 | **57** |

> **Update (added after verification): a newer edition supersedes this table.** Insee Analyses n°118, *Revenus des ménages élargis à l'ensemble de l'économie en 2023*, published 16 Apr 2026 [25], gives 2023 data on a revised basis. The revision reattributes 123 bn of undistributed corporate profits to shareholder households, so the levels are not strictly comparable with 2022. In 2023: levies on households total **1,270.9 bn**, of which the top 10% pay **422.8 bn = 33.3%** and the top 20% pay 48.3% (our calc.). The bottom half pays 285 bn and the top half 986 bn. **56%** of people are net beneficiaries (99% in D1 vs 18% in D10). The D10/D1 ratio of broadened income is **26 before transfers and 3.5 after**. Insee's Gini decomposition shows that **levies on production and consumption increase inequality by 3.9 Gini points**, while income and wealth taxes reduce it by 2.8 points; individualizable in-kind transfers explain 51% of the reduction [25]. Insee does not publish an updated "48% vs 64%" levy-to-income comparison in this edition, so that figure remains a 2022 result. The platform should cite the 2023 figures.

Key Insee findings (2022 edition): top 10% pay **31.7%** of all levies (our calc.: 393.8/1,241.1) and the top 20% pay 46.9%; the bottom half of the distribution pays 287 bn vs 954 bn for the top half. The ratio D10/D1 of broadened income is 23.6 before transfers and **3.8 after** (divided by 6.3). **But:** "because of the weight of indirect taxation", levies represent **48%** of pre-transfer income (augmented with pensions and unemployment benefits) for the richest 10% and **64%** for the poorest 10% [12]. The system is progressive overall because of **transfers and public services**, not because levies as a whole are progressive at the bottom.

### 6.3 The very top: effective tax rates (IPP)

Source: IPP Note n°92, L. Bach, A. Bozio, A. Guillouzouic, C. Malgouyres, "Quels impôts les milliardaires paient-ils ?", June 2023 (updated version posted May 2025) [13]. Data: 2016, linking personal tax returns with corporate tax returns ("economic income" includes retained earnings of controlled companies).

| Group | Effective total tax rate (all direct taxes incl. CIT attributed to owners, % of economic income) |
|---|---|
| Top 0.1% (~37,800 tax households) | **~46%** (peak) |
| Top 0.0002% (~75-80 households, "billionaires") | **~26%** |
| Personal taxes only (IR, social levies, ISF) in top 0.001% (~378 households) | **~2%** of economic income |
| IPP simulation: applying the personal income-tax scale to all economic income of the top 0.0002% | 26% → **59%** |

Contested points: F. Geerolf (OFCE-affiliated economist; critique not peer-reviewed) argues that on a homogeneous base the billionaires' rate is 25.1% vs 26.8% at the top-10% threshold, so the "regressivity" largely disappears [19]. The IPP result is mostly about **retained corporate earnings** being taxed only at the CIT rate - a timing/deferral issue as much as a rate issue. The 2025 CDHR (minimum 20% tax on income >250k/500k) and the PLF 2027 article ending the step-up of deferred capital gains on *apport-cession* at death respond to this diagnosis [4].

### 6.4 Outcome: inequality before/after transfers (Eurostat EU-SILC, survey 2025)

Source: Eurostat `ilc_di12`, `ilc_di12b`, `ilc_di12c`, updated 20 Oct 2026 [20]; CSVs `data/eurostat_ilc_di12*_gini.csv`.

| Gini coefficient (0-100), survey 2025 | France | EU-27 aggregate | EU-27 median | FR rank EU-27 (1 = most unequal) | Panel (DE, IT, ES, NL, BE, SE, DK) |
|---|---|---|---|---|---|
| Before all social transfers (pensions counted as transfers) | **53.7** | 47.8 | 46.7 | **1** | 49.2, 48.0, 44.6, 46.2, 45.5, 46.7, 46.8 |
| Before social transfers other than pensions | 37.4 | 34.1 | 34.1 | 4 | 36.0, 35.1, 34.1, 31.7, 30.9, 34.9, 35.4 |
| Disposable income (after transfers and direct taxes) | **30.4** | 29.2 | 29.2 | 11 | 30.1, 31.0, 30.8, 25.9, 23.4, 28.6, 28.2 |

Reading: France's tax-and-transfer system produces one of the largest reductions in measured inequality in the EU (-23 Gini points from pre-transfer to disposable income), but France starts from the most unequal pre-transfer distribution (largely mechanical: public pensions are a big share of income) and ends slightly above the EU average. EU-SILC disposable income excludes indirect taxes and in-kind public services (unlike Insee's broadened accounts).

---

## 7. Tax expenditures, social-contribution exemptions and "aid to business"

### 7.1 Tax expenditures (*dépenses fiscales*)

| Vintage / source | Year covered | Amount (EUR bn) | Notes |
|---|---|---|---|
| PLF 2024 initial | 2024 | 78.4-78.7 | Cour des comptes reports both 78.41 and 78.74 [14] |
| PLF 2025 | 2024 | 83.3 | revision [14] |
| **PLF 2026, final** | **2024** | **89.40** | +10.7 bn vs first estimate (+13.5%), "unprecedented" [14] |
| PLF 2025 initial | 2025 | 85.1 | [14] |
| **PLF 2026 revised** | **2025** | **91.83** = 3.07% of GDP, 25.8% of net State tax revenue, ~7% of PO; 474 measures | Cour des comptes NEB 2025, April 2026 [14] |
| PLF 2026, under the **former VAT convention** | 2025 | 105.61 | **Since the PLF 2024**, VAT tax expenditures are costed only on the State's net share of VAT, after transfers to social security and local authorities. For 2025 this gives 11.00 bn instead of 24.78 bn under the old convention [14]. (Corrected after verification: the file said "the PLF 2026 re-classified ~14 bn"; the Cour des comptes dates the change to the PLF 2024. The PLF 2025 initial figure was 85.09 bn under the new convention vs 99.40 bn under the old one.) |
| PLF 2027 annex 1, sum of 459 items (our calc.) | 2025 / 2026 / 2027 | **91.7 / 92.0 / 83.9** (91,664 / 92,019 / 83,919 MEUR) | Unweighted sum of the itemized costs; "nc" (not costed: 56 / 62 / 83 items) and "ε" (under 0.5 MEUR) count as zero, so this is **not an official total** and the 2027 figure is biased down (e.g., the electric-vehicle exemption 940102, 3.4 bn in 2026, is "nc" in 2027) [15]. **Verified 2026-10-25:** the xls (800,768 bytes, `application/vnd.ms-excel`) was fetched from fid-download/84340 inside a browser session on budget.gouv.fr and its "Chiffrages" sheet exported to `data/raw/taxation/plf2027_browser/PLF2027_VM_T2_annexe1_Chiffrages.csv`; the re-summed totals match the earlier figures and `data/plf2027_vm_tome2_tax_expenditures_summary.csv` exactly. (Earlier note: the copies under `raw/taxation/plf2027/` are 212-byte bot-protection stubs.) |

Breakdown (PLF 2027 annex 1, 2026 forecast, our sums, verified 2026-10-25 in the same file): IR 44.3 bn (171 items); IR+IS 14.1; VAT 11.2 (11.15); energy excise 8.5; IS 3.6; registration duties 4.3; other levies (*autres droits*) 4.7; local taxes 1.1; other direct taxes 0.2 [15]. Largest single items 2026: research tax credit *CIR* 7.1 bn (7,067 MEUR); home-employee tax credit 7.1 (7,107); 10% pension allowance 5.6 (5,598; PLF 2027 article 3 proposes to reduce it, with a stated yield of **1,100 MEUR in 2027** per annex 2 "*Bilan mesures 2026-2027*"; the annex 1 forecast falls to 4,715); *pacte Dutreil* (business transmission exemption) 3.8; employee savings exemption 3.1 [15]. Annex 2 also shows that tax-expenditure cuts proposed or voted for 2027 total 2.14 bn, against 0.43 bn of new or enlarged ones (net saving 1.72 bn) [15]. Cour des comptes: 15 measures = 46.7 bn (>50% of total); tax expenditures erase 52.4% of energy-excise yield, **46.4% of IR yield** and 20.7% of inheritance-duty yield; reliability is weak (actual cost known for only 55%) [14].

CSV: `data/plf2027_vm_tome2_tax_expenditures_summary.csv`.

### 7.2 Social-contribution exemptions (*niches sociales*)

**Latest vintage (added 2026-10-25): PLFSS 2027 annex 4 (Oct 2026) [27]**, ROBSS scope, EUR bn:

| Item | 2024 | 2025 | 2026 (p) | 2027 (p) |
|---|---|---|---|---|
| Total cost: exemptions + base exemptions (*exemptions d'assiette*) + DFS (*déduction forfaitaire spécifique*, flat-rate deduction for professional expenses) | **93.2** | **91.0** (of which base exemptions 15.3, DFS 1.1) | 84.4 | - |
| Exemptions of contributions (general + targeted), table 6 | - | 74.5 | 66.7 | 61.0 |
|   *allègements généraux*, base regimes | - | 65.0 | 57.4 (RGDU 54.3 + residual proportional cuts 3.1) | 52.0 |
|   compensated targeted exemptions | - | 6.9 | 9.1 | 8.7 |
|   non-compensated | - | 2.7 | 0.3 | 0.3 |
| Net base exemptions (table 9) | - | - | 16.3 | - |

Readings: (i) the 2024 total was revised from 90.8 (PLFSS 2026 annex 4) to 93.2; (ii) the 2026 fall in the ROBSS-scope figure is largely a **scope shift**: the single RGDU now also covers unemployment-insurance (Unédic) and Agirc-Arrco contributions, which are then compensated by the base schemes, so the cost does not disappear from public finances; (iii) the 2027 figure includes PLFSS 2027 article 7 (-2.8 bn on the ROBSS scope, -3.7 bn on the full scope incl. Unédic and Agirc-Arrco) [27][28]. Niches sociales were 13.7% of base-scheme revenue in 2025, under the 14% ceiling set by the 2023-2027 programming law [27].

*Previous vintage, kept for reference:* PLFSS 2026, annex 4 (Oct 2025) [16].

| Item | 2024 | 2025 (p) | 2026 (p) |
|---|---|---|---|
| Total exemptions + base exemptions + DFS, ROBSS scope | **90.8** | 88.5 | - |
| Exemptions of contributions (general + targeted), ROBSS | 74.7 | 71.8 | 71.5 |
|   *allègements généraux* (general low-wage reductions), base regimes | 64.9 | 62.2 | 61.8 |
|   compensated targeted exemptions | 7.0 | 6.8 | 6.9 |
|   non-compensated | 2.8 | 2.8 | 2.8 |
| General reductions incl. special regimes, all scopes | **>75** (39.4 general reduction + 36.0 proportional cuts of 1.8 and 6 pts) | | |
| Base exemptions (*exemptions d'assiette*: profit-sharing, meal vouchers, etc.) | 14.7 | 15.5 (net) | |

Context: these reductions are compensated to social security mainly by **VAT shares** (PLF 2027 sets the VAT fraction for social security at 26.62% for 2027) [4]. From 2026 the three schemes are merged into a single *réduction générale dégressive unique* (RGDU, single tapering general reduction). Its scale has been frozen at the value of the minimum wage (SMIC) of 1 Jan 2026 since the SMIC increase of 1 June 2026, saving about 2.8 bn on base-scheme balances in 2026 and a further 2.8 bn in 2027 [27]. PLFSS 2027 (bill n°3211, filed 1 Oct 2026), **article 7** "*Rationaliser l'assiette des allègements généraux*", proposes to include wage supplements (profit-sharing *intéressement*, *participation*, employer top-ups to savings plans) in the pay used to compute the RGDU rate; the exposé des motifs states that this "will correct the amount of general reductions by **3.7 bn**" (3.7 bn full scope; 2.8 bn on the ROBSS scope per annex 4) [27][28]. (Verified 2026-10-25 in the bill text and annex 4; was "a June 2026 decree froze them" and "reported yield 3.7 bn; press source, not verified in the bill text". The freeze is confirmed; its legal vehicle was not checked. Parliamentary votes on article 7 after 25 Oct 2026 were not tracked.)

### 7.3 "Public aid to companies": why estimates range from ~110 to ~210 bn

Source: Public Sénat, "211 milliards d'euros d'aides publiques aux entreprises : sur quoi repose le calcul…", 15 Sep 2025 [17], summarizing the Senate inquiry report (July 2025).

| Estimate | Year | Total (EUR bn) | Main components |
|---|---|---|---|
| Senate inquiry (Rapporteur F. Gay, chair O. Rietmann) | 2023 | **211** ("at least") | State subsidies 7 + Bpifrance loans/guarantees 41 + tax expenditures incl. reclassified 88 + contribution reductions 75 |
| Senate "strict" scope | 2023 | 108 | excludes Bpifrance, reclassified TE, VAT TE |
| Clersé (Univ. Lille, for CGT/IRES; the commissioning is not stated in [17]) | study published 2022 (corrected after verification: was "2019"; the data year is not stated in [17]) | 157 (205 with reclassified TE) | |
| France Stratégie | study published 2020 (corrected after verification: was "~2019") | 179 (223 with reclassified TE) | |
| Haut-commissariat au Plan | July 2025 | 112 | excludes contribution reductions |
| Minister E. Lombard (statement) | 2025 | ~150 | 40 TE + 30 budget + 80 contributions |

**Divergences explained:** no official definition; whether general contribution cuts are "aid" (they apply to all employers, including associations and public firms, and compensate a high statutory rate) or a feature of the tax schedule; whether loans/guarantees count at face value or at subsidy-equivalent cost; whether reduced VAT rates (paid by consumers) count; whether reclassified ("*déclassées*") measures are included. **Recommendation for the platform:** present a range and the components, never a single number.

---

## 8. Divergences between sources (summary)

| Topic | Values | Explanation |
|---|---|---|
| France 2024 levy ratio | Insee PO 42.7; OECD 43.5; DG TAXUD 43.5; Eurostat incl. imputed 45.3 | Insee nets **all** tax credits (19.6 bn in 2024) and excludes imputed contributions (51.2 bn); OECD/DG TAXUD treat payable credits differently; Eurostat's broad aggregate includes imputed contributions. |
| France 2023 | Insee 43.2; OECD 43.9 | Same reasons. |
| 2025 public spending | Insee 57.3% (1,714 bn); PLF 2027 56.6% (1,694 bn) | PLF figure excludes tax credits (*hors CI*) and uses budget conventions. |
| 2025 GDP | 2,991 bn (implied by Insee Aug 2026 PO table and by Eurostat Oct 2026: 1,714.1 bn = 57.3%); 2,995 bn (Cour des comptes NEB, April 2026, footnote 2: "*Le PIB de la France s'élève à 2 995 Md€ en 2025, selon l'Insee*") | Vintage revisions: the Cour used an Insee estimate published before the May 2026 accounts (the exact vintage is not stated by the Cour). The Cour's 3.07% of GDP is unchanged on 2,991 bn (91.83 / 2,991 = 3.07%). (Verified 2026-10-25 in the NEB PDF; was flagged "not re-checked".) |
| 2024 PO rate | 42.8 (Insee March 2026) → 42.7 (Insee May/Aug 2026) | Revision. |
| 2019 PO rate | 43.9 (Insee IP 2106 table) vs 44.0 (Insee series) | Rounding of 43.958. |
| Tax-expenditure total | 85.1 / 91.8 / 105.6 bn for 2025 | Vintage (PLF 2025 vs 2026) and VAT convention change. |
| Share of IR paid by top 10% | "nearly 3/4" (DGFiP 2024 income); press often says 70% | Different years, IR before/after credits, ranking by RFR per share. |
| Top 10% share of all levies | 31.7% (Insee 2022); 33.3% (Insee 2023, IA 118, revised method) | Includes VAT and contributions, so not comparable with IR-only figures. The 2023 method also attributes undistributed corporate profits to households (added after verification). |
| Euro area composition | EA-20 (2024 stats) vs EA-21 (since 2026) | Bulgaria joined 1 Jan 2026. |
| OECD 2022 vs 2023 drop | OECD: 45.9 → 43.9 (-2.0); Insee: 45.0 → 43.2 (-1.8) | Different treatment of credits and of energy-crisis measures; not fully reconciled (gap). |
| "Aid to companies" | 108-211 bn | Scope (section 7.3). |

---

## 9. Economists' disagreements and the strongest counter-arguments to the platform's thesis (steelman)

The platform's thesis: proposals that promise to restore public finances or purchasing power by taxing "the rich" (ISF return, *taxe Zucman*) without addressing spending misjudge orders of magnitude. The strongest objections, with sources:

1. **"High levies mostly fund transfers that come back to households."** Insee's distributed accounts show that, of 1,241 bn of levies in 2022, 568 bn returned as cash benefits (357 bn pensions) and 673 bn as in-kind transfers and collective services; **57% of people are net beneficiaries** [12]. In 2023: 1,271 bn of levies vs 1,337 bn of transfers received (398 bn of pensions), and **56%** net beneficiaries [25]. A high PO rate partly reflects the choice to socialize pensions and health insurance; in countries with mandatory private pensions or insurance (Netherlands, Denmark, Switzerland), equivalent payments are "non-tax compulsory payments" outside the tax-to-GDP ratio (OECD methodology; country-level NTCP figures not retrieved here - gap). Also, France's ratio is 2nd in % of GDP but only **9th per capita in PPS** in the EU (section 5.1C).
   *Implication for the platform:* compare "net" burdens and spending mixes, not only gross ratios.

2. **"France could tax more - specifically capital income, inheritance and the very top - without the feared exodus."**
   - CAE Focus n°118 (July 2025; Bach, Bozio, Grimprel, Guillouzouic, Landais, Malgouyres): only **0.2% of the top 1%** of capital-income earners emigrate each year (half the rate of the general population, 0.38%); a +1 pt increase in the effective tax rate raises long-run expatriation of high-wealth households by **0.02-0.23%**; macro effects on payroll are tiny; **tax optimization reduces yields far more than exile** [22]. *Caveat added after verification (fairness):* this last point is not a French estimate. The CAE draws it from Scandinavian evidence (Jakobsen et al. 2024): for each euro of mechanical yield from higher wealth taxation, about 54 cents disappear through intensive-margin responses (optimization, avoidance, saving) vs 20 cents through emigration. Total behavioral responses cut wealth or capital-income tax revenue by **about 74%** relative to the mechanical effect. This evidence cuts **both ways**: exile is not the main problem, but **realized yields of wealth taxes can be a fraction of static estimates**. The CAE adds that these distortions are not clearly larger than those of other taxes on top incomes [22].
   - IPP Note 92: billionaires' effective rate (26%) below the top 0.1% (46%), due to retained earnings in holding companies [13].
   - CAE Note n°69 "*Repenser l'héritage*" (Dec 2021; Dherbécourt, Fack, Landais, Stantcheva): inheritance is increasingly important; the main exemptions (life insurance, *pacte Dutreil*, bare-ownership gifts) hollow out the tax base [23]. *Verified in the CAE PDF (https://www.cae-eco.fr/staticfiles/pdf/cae-note069.pdf) after verification:* the economic flow of transmissions exceeds 15% of GDP (~300 bn/year). "About 40% of transmitted wealth escapes the inheritance flow seen in tax sources": in the 1994-2006 DMTG surveys, wealth declared to the tax administration was 35-40% below the economic flow. This is a measurement gap, not purely legal exemptions. Base-broadening scenarios raise **~9 bn** (broad base, current scale) to **~19 bn** (broader base, same effective rates) of additional duties. One scenario leaving 99% of heirs better off or unaffected yields "more than 10 bn" in steady state. The CAE costed the *pacte Dutreil* at 2-3 bn in 2018-2019. (Corrected after verification: the file gave "reform yield 12-19 bn" from press summaries.) Cour des comptes: the *pacte Dutreil* alone costs ~4 bn/year (was costed at 0.8 bn before revision) [14].
   - Tax expenditures erase **46% of IR yield** [14]: base-broadening without rate increases could raise revenue (PLF 2027 itself relies on "*mise en cohérence des dépenses fiscales*").
   *Implication:* the platform must not claim that taxing capital/inheritance "cannot raise anything"; the honest claim is about **orders of magnitude relative to a 151.6 bn deficit (2025, October 2026 EDP notification) and 1,714 bn of spending** (corrected 2026-10-25 to align with file 00 row 31: was "152.5 bn deficit").

3. **"Orders of magnitude for the Zucman tax are disputed."** Proponents' estimate **about 20 bn/year (range 15-25)** for a 2% minimum tax on fortunes above EUR 100 m (canonical wording, file 00 row 45). Critics: **about 2-6 bn** after corporate-tax imputation and behavioral or legal effects (file 00 row 45). F. Geerolf (Oct 2026; OFCE-affiliated, not peer-reviewed) [19] writes that costings which impute corporate tax or correct the data bring the promised 20 bn down to **2 to 6 bn**. The study commissioned by the business collective *Trop, c'est trop !* (P. Andrews, doctoral student, Paris-Panthéon-Assas; June 2026; advocacy-funded, pro-business orientation) [29] finds a static yield of **24 bn** with no corporate-tax imputation, **5.5 bn** in its central scenario (82% of the corporate tax paid by controlled companies imputed) and **1.25 bn** with full imputation; it adds that behavioral responses erode the base by 14-34% in the medium term and that output losses would make the net fiscal balance negative (down to -22.75 bn a year), a macro claim that rests on its own model. It also documents the base concentration Geerolf cites: **45% of the base is held by three families** [29]. (Corrected 2026-10-25 after reading the primary study: the file said "critics' estimates 1.5-5 bn", sourced from Wikipedia [24] and flagged as unverified. The study's static range is 1.25-5.5 bn, central 5.5 bn.) No official (DGFiP/Trésor) costing was found (gap). Scale: 20 bn = about 13% of the 2025 deficit (151.6 bn); the 15-25 bn range = about 10-16%; the critics' 2-6 bn = about 1-4%.

4. **Laffer / elasticity debate.** France is near the top of the OECD on the labor tax wedge (3rd) and on employer contributions (2nd); economists who stress behavioral responses argue that further rate increases on labor and mobile capital have low or negative marginal yields. Evidence: the 2025 IR boom partly came from bracket creep and **timing shifts** - capital income jumped +32% in 2024, which DGFiP links in part to anticipation of the CDHR [11] - showing high short-run elasticity of top capital incomes to announced taxes. Conversely the CAE/IPP evidence above finds low *migration* elasticities. The disagreement is mostly about *which* margin (migration vs. income shifting/realization timing vs. investment) dominates. (Academic elasticity-of-taxable-income estimates for France were not systematically retrieved here - gap.)

5. **"Tax competitiveness" vs. "the tax structure is the problem, not the level."** France's corporate tax yield is low (2.3% GDP, 31st OECD) but production taxes (4.4% GDP vs EU 2.4%) and employer contributions are high [6][8]; many economists (e.g., CAE, Trésor) argue that shifting from production/labor taxes to consumption, property or inheritance would be more growth-friendly at constant level. The OECD notes France's tax mix relies less than average on VAT (16.6% of revenue vs 20.5%) [5].

6. **Regressivity at the bottom.** Insee: levies = 64% of pre-transfer income for D1 vs 48% for D10, due to indirect taxes (2022) [12]. The 2023 edition confirms the mechanism: levies on production and consumption add 3.9 Gini points of inequality [25]. Critics of "fair share" rhetoric and critics of VAT increases both use this.

7. **The "52.8% don't pay income tax" talking point is misleading if used alone**: everyone pays CSG (1.7× IR), VAT and excises; IR is only ~7% of total levies [3][11].

---

## 10. Open questions and gaps

- **PLF 2027 *Voies et moyens* tome II official total** of tax expenditures for 2026-2027: still not retrieved (the tome II PDF was not located; the annex spreadsheets give items only). The annex 1 sum of items is now verified (section 7.1). A secondary source cites "~89 bn" for 2027 - ⚠ unverified and inconsistent with the 83.9 bn sum of costed items. **Recommendation: drop the "~89 bn" from the site**; use the Cour's 91.83 bn (2025) as the headline.
- ~~**HCFP opinion on PLF/PLFSS 2027**: not retrieved~~. Retrieved after verification: Avis HCFP-2026-5 of 25 Sep 2026 [26] (see 3.1).
- ~~**PLFSS 2027 annex 4** (exemptions 2026-2027): not retrieved~~. Retrieved 2026-10-25 from securite-sociale.fr [27]; section 7.2 updated.
- **DGFiP shares of IR for top 1% / top 0.1%** (income 2024): table 4 of DGFiP n°41 was not extractable from the PDF text; the "481 households with RFR >9 m EUR paying ~1.94 bn" figure seen in press could not be verified (impots.gouv.fr in maintenance). ⚠ unverified. Recommendation: drop from site unless DGFiP n°41 table 4 is retrieved.
- ~~**Insee distributed accounts for 2023 or 2024**: none found~~. Corrected after verification: the 2023 accounts were published in Insee Analyses n°118 (16 Apr 2026) [25]; no 2024 edition was found.
- **OECD non-tax compulsory payments** (to adjust tax-to-GDP for NL/DK/CH private mandatory pensions) and **OECD net social expenditure**: not retrieved in this file (see social-protection file).
- **ITR on capital** (DG TAXUD) not retrieved.
- ~~**France Stratégie capital-tax evaluation committee (final report, Oct 2023)**: from memory, unverified~~. **Verified 2026-10-25** in the committee's opinion (*Avis du comité*, fourth and final report, October 2023) [30]: dividends declared by households rose to **about 23 bn a year in 2018-2020, vs 14 bn in 2013-2017**; the research teams established a **causal effect of the PFU** (*prélèvement forfaitaire unique*, 30% flat tax on capital income) on dividend payouts to households but **could not estimate its macroeconomic size**, and the effect is smaller than the one measured for the 2013 move to the progressive scale; the committee writes that the PFU "would have been self-financing in the first years"; and the research "**did not detect any impact of the PFU on investment or wages**" in the most exposed firms, where higher dividends were financed by lower net saving. It also notes that 1% of tax households (400,000) receive 96% of declared dividends (2021). (Corrected wording: was "a sharp increase in dividends ... and no clearly identifiable effect on productive investment", from memory.)
- ~~**CAE Note 69 figures** only verified via secondary summaries~~. Checked in the primary PDF after verification (see section 9, point 2). The "12-19 bn" figure was corrected to "~9 to ~19 bn".
- **Eurostat 2025 tax ratios for France** not yet published in `gov_10a_taxag` (as of 21 Oct 2026 update).
- **Academic elasticity of taxable income estimates for France** not compiled.

---

## 11. Data files produced

| File | Content | Source |
|---|---|---|
| `data/insee_taux_prelevements_obligatoires_1959_2025.csv` | PO rate 1959-2025 | Insee [2] |
| `data/insee_t_3216_T_3216.csv`, `data/derived_insee_PO_by_subsector_2023_2025.csv` | PO by sub-sector, EUR bn and % GDP | Insee [3] |
| `data/insee_t_3217_T_3217.csv`, `data/derived_insee_main_taxes_2025_pct.csv` | Main taxes 1995-2025, EUR bn; 2025 % GDP / % PO | Insee [3] |
| `data/eurostat_gov_10a_taxag_PC_GDP.csv`, `..._MIO_EUR.csv`, `..._total_pcgdp.csv` | ESA tax aggregates by country 1995-2025 | Eurostat [8] |
| `data/eurostat_nama_10_pc_gdp_pps_per_capita.csv`, `data/derived_tax_per_capita_pps.csv` | GDP per capita PPS; tax per capita PPS | Eurostat [9] |
| `data/oecd_revenue_statistics_2025_pct_gdp.csv` | OECD tax/GDP by category 2000-2024 | OECD [6] |
| `data/oecd_taxing_wages_2026_tax_wedge_single.csv` | Tax wedges 2000-2025 | OECD [10] |
| `data/ec_taxation_trends_2026_selected.csv` | DG TAXUD taxation trends tables | EC [7] |
| `data/plf2027_vm_tome2_tax_expenditures_summary.csv` | Tax expenditures by tax, PLF 2027 | PLF 2027 [15] |
| `data/eurostat_ilc_di12_gini.csv`, `..._di12b_gini.csv`, `..._di12c_gini.csv` | Gini before/after transfers | Eurostat [20] |
| Scripts: `research/scripts/jsonstat2csv.py`, `research/scripts/taxstats.py` | JSON-stat parser; group stats (mean/median/rank) | - |

---

## 12. Sources (all accessed 2026-10-25)

1. Insee, *Le compte des administrations publiques en 2025*, Insee Première n°2106, May 2026. https://www.insee.fr/fr/statistiques/8997691 (PDF: https://www.insee.fr/fr/statistiques/fichier/8997691/ip2106.pdf)
2. Insee, *Taux de prélèvements obligatoires rapportés au produit intérieur brut* (series 1959-2025), updated 28 Aug 2026. https://www.insee.fr/fr/statistiques/2381412 (xlsx: https://www.insee.fr/fr/statistiques/fichier/2381412/econ-fin-pub-prelev-oblig.xlsx)
3. Insee, *Dépenses et recettes des administrations publiques en 2025*, Comptes nationaux annuels base 2020, tables 3.216 and 3.217, 28 Aug 2026. https://www.insee.fr/fr/statistiques/8988845 (https://www.insee.fr/fr/statistiques/fichier/8988845/t_3216_fr.xlsx ; https://www.insee.fr/fr/statistiques/fichier/8988845/t_3217_fr.xlsx)
4. Government of France, *Projet de loi de finances pour 2027* (n°3210), filed at the Assemblée nationale 1 Oct 2026, *article liminaire* and *exposé des motifs*. https://www.assemblee-nationale.fr/dyn/opendata/PRJLANR5L17B3210.html
5. OECD, *Revenue Statistics 2025 - France country note*, December 2025. https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/revenue-statistics-2025-country-notes_3708be73/france_77750c88/c55b0aeb-en.pdf ; report: https://www.oecd.org/en/publications/2025/12/revenue-statistics-2025_07ca0a8e.html
6. OECD Data Explorer, Revenue Statistics - OECD countries: comparative tables (SDMX `OECD.CTP.TPS,DSD_REV_COMP_OECD@DF_RSOECD`), queried 2026-10-25. https://sdmx.oecd.org/public/rest/data/OECD.CTP.TPS,DSD_REV_COMP_OECD@DF_RSOECD,/.TAX_REV.S13._T+T_1000+T_1100+T_1200+T_2000+T_2100+T_2200+T_3000+T_4000+T_4100+T_4300+T_5000+T_5110+T_5120+T_5200+T_6000._T.PT_B1GQ.A?startPeriod=2000&format=csvfile
7. European Commission, DG TAXUD, *Data on Taxation Trends* (data release 30-31 Mar 2026; news "Tax revenue rebounds in 2024 after decade low in 2023", 31 Mar 2026). https://taxation-customs.ec.europa.eu/taxation/economic-analysis/data-taxation-trends_en ; https://taxation-customs.ec.europa.eu/news/tax-revenue-rebounds-2024-after-decade-low-2023-2026-03-31_en ; ITR file: https://ec.europa.eu/taxation_customs/document/download/73ab0a07-7577-415d-87ab-8d18208f7fd5_en
8. Eurostat, *Main national accounts tax aggregates* (`gov_10a_taxag`), updated 21 Oct 2026. https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_taxag?format=JSON&unit=PC_GDP&sector=S13_S212
9. Eurostat, *Main GDP aggregates per capita* (`nama_10_pc`, CP_PPS_EU27_2020_HAB), updated 22 Oct 2026. https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_pc?format=JSON&unit=CP_PPS_EU27_2020_HAB&na_item=B1GQ
10. OECD, *Taxing Wages 2026 - France country note*, April 2026, and SDMX `DSD_TAX_WAGES_COMP@DF_TW_COMP`. https://www.oecd.org/content/dam/oecd/en/publications/reports/2026/04/taxing-wages-2026-country-notes_491a0e97/france_e4ab8466/7d4e9727-en.pdf ; https://www.oecd.org/en/publications/2026/04/taxing-wages-2026_d1f39986.html
11. DGFiP, *DGFiP Statistiques n°41 - L'impôt sur le revenu 2024 a été plus dynamique que les revenus*, November 2025 (T. Pequignot, K. Bamuadila Nguanu, O. Arnal). https://www.impots.gouv.fr/sites/default/files/media/9_statistiques/0_etudes_et_stats/0_publications/dgfip_statistiques/2025/num41_11/dgfip_stat_41.pdf (retrieved via Internet Archive copy because impots.gouv.fr was in maintenance)
12. Insee, *Comptes nationaux par catégories de ménages en 2022 - Transferts monétaires et services publics augmentent de 16 % le niveau de vie au milieu de l'échelle*, Insee Première n°2022, November 2024. https://www.insee.fr/fr/statistiques/8275760 (PDF: https://www.insee.fr/fr/statistiques/fichier/8275760/ip2022.pdf); earlier: Insee Analyses n°88 (Sept 2023) https://www.insee.fr/fr/statistiques/7669723
13. IPP (Institut des politiques publiques), L. Bach, A. Bozio, A. Guillouzouic, C. Malgouyres, *Quels impôts les milliardaires paient-ils ?*, Note IPP n°92, June 2023 (updated version May 2025). https://www.ipp.eu/wp-content/uploads/2025/05/92_Note_IPP_Billionaires-version-actualisee.pdf ; https://www.ipp.eu/actualites/quels-impots-les-milliardaires-paient-ils/
14. Cour des comptes, *Analyse de l'exécution budgétaire 2025 - Dépenses fiscales* (NEB), April 2026. https://www.ccomptes.fr/sites/default/files/2026-04/NEB-2026-Depenses-fiscales.pdf
15. Direction du Budget, *PLF 2027 - Évaluation des voies et moyens, tome II*: Annex 1 *Dépenses fiscales* (xls) and Annex 5 *Ventilation par décile - IR* (xlsx), October 2026. https://www.budget.gouv.fr/documentation/documents-budgetaires/exercice-2027/projet-loi-finances-les/les-documents-annexes-au-plf (files: https://www.budget.gouv.fr/documentation/fid-download/84340 ; https://www.budget.gouv.fr/documentation/fid-download/84352 ; Annex 2 *Évolution des dépenses fiscales*: https://www.budget.gouv.fr/documentation/fid-download/84343 ; retrieved through a browser session on 2026-10-25 (direct scripted requests return a 212-byte bot-protection page); sheet exports saved under `data/raw/taxation/plf2027_browser/`)
16. Sécurité sociale, *PLFSS 2026 - Annexe 4: Présentation des mesures d'exonérations de cotisations et contributions…*, 14 Oct 2025. https://www.securite-sociale.fr/files/live/sites/SSFR/files/medias/PLFSS/2026/PLFSS2026-Annexe4-20251014-183718-59-11_avec%20couverture.pdf
17. Public Sénat, *211 milliards d'euros d'aides publiques aux entreprises : sur quoi repose le calcul de la commission d'enquête du Sénat ?*, 15 Sep 2025 (summarizing Senate inquiry report, July 2025). https://www.publicsenat.fr/actualites/economie/211-milliards-deuros-daides-publiques-aux-entreprises-sur-quoi-repose-le-calcul-de-la-commission-denquete-du-senat
18. Public Sénat, *Budget 2027 : le Haut Conseil des finances publiques pointe des prévisions « optimistes » du gouvernement*, Oct 2026 (secondary; superseded by the primary opinion [26]). https://www.publicsenat.fr/actualites/economie/budget-2027-le-haut-conseil-des-finances-publiques-pointe-des-previsions-optimistes-du-gouvernement
19. F. Geerolf, *Les mensonges de la taxe Zucman : un vrai sujet, un faux diagnostic, un mauvais remède*, October 2026 (critique note, not peer-reviewed). https://fgeerolf.com/mensonges-taxe-zucman.pdf
20. Eurostat, EU-SILC Gini coefficients `ilc_di12`, `ilc_di12b`, `ilc_di12c`, updated 20 Oct 2026. https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ilc_di12?format=JSON
21. Legifiscal, *PLFSS 2027 : présentation* (secondary; its reported 3.7 bn yield is now confirmed by the primary bill [28] and annex 4 [27]). https://www.legifiscal.fr/actualites-fiscales/4657-presentation-plfss-2027.html
22. CAE (Conseil d'analyse économique), L. Bach, A. Bozio, N. Grimprel, A. Guillouzouic, C. Landais, C. Malgouyres, *Fiscalité du capital : quels sont les effets de l'exil fiscal sur l'économie ?*, Focus n°118, July 2025 (v2 Sept 2025). https://cae-eco.fr/static/pdf/Focus_118_emigration_fiscale_250725_v2.pdf
23. CAE, C. Dherbécourt, G. Fack, C. Landais, S. Stantcheva, *Repenser l'héritage*, Note du CAE n°69, December 2021 (figures via Legifiscal summary). https://www.legifiscal.fr/actualites-fiscales/3019-cae-conseil-analyse-economique-heritage-nouvelle-proposition.html
24. Wikipedia (fr), *Taxe Zucman* (aggregator of yield estimates; used only to locate the range, flagged as non-authoritative; no longer relied on for any figure since 2026-10-25, see [29]). https://fr.wikipedia.org/wiki/Taxe_Zucman
25. Insee, *Revenus des ménages élargis à l'ensemble de l'économie en 2023*, Insee Analyses n°118, 16 Apr 2026 (distributed national accounts 2023, semi-final, base 2020). https://www.insee.fr/fr/statistiques/8974371 (data: https://www.insee.fr/fr/statistiques/fichier/8974371/IA118.xlsx, figures 2a-2b) - added after verification.
26. Haut Conseil des finances publiques, *Avis n°HCFP-2026-5 relatif aux projets de lois de finances et de financement de la sécurité sociale pour l'année 2027*, 25 Sep 2026. https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf ; listing: https://www.hcfp.fr/liste-avis/avis-ndeg2026-5-lois-de-finances-2027 - added after verification.
27. Sécurité sociale, *PLFSS 2027 - Annexe 4: Présentation des mesures de réduction et d'exonération de cotisations et contributions ainsi que de leur compensation*, October 2026 (introduction; table 6; section 1.3.1; table 9). https://www.securite-sociale.fr/files/live/sites/SSFR/files/medias/PLFSS/2027/PLFSS2027-Annexe4-VDEF.pdf (listing: https://www.securite-sociale.fr/la-secu-en-detail/loi-de-financement/annee-en-cours); local copy `data/raw/taxation/plfss2027/PLFSS2027-Annexe4-VDEF.pdf` - added 2026-10-25.
28. Government of France, *Projet de loi de financement de la sécurité sociale pour 2027* (n°3211), filed at the Assemblée nationale 1 Oct 2026, article 7 and its *exposé des motifs*; article 16 *exposé des motifs* (3.7 bn). https://www.assemblee-nationale.fr/dyn/opendata/PRJLANR5L17B3211.html ; local copy `data/raw/taxation/plfss2027/PRJLANR5L17B3211.html` - added 2026-10-25.
29. *Trop, c'est trop !* (business collective; advocacy-commissioned study), P. Andrews with N. Janson, A. Levy, O. Redoulès, E. Tison, *La taxe Zucman : diagnostic fiscal, rendement effectif et effets macroéconomiques*, June 2026. https://www.institut-entreprise.fr/wp-content/uploads/2026/06/TCT_Taxe-Zucman-2026.pdf ; local copy `data/raw/taxation/zucman/TCT_Taxe-Zucman-2026.pdf` - added 2026-10-25 (replaces Wikipedia [24] for the critics' figures).
30. France Stratégie, *Comité d'évaluation des réformes de la fiscalité du capital - Quatrième rapport* (final report), *Avis du comité*, October 2023. https://www.strategie-plan.gouv.fr/files/files/Publications/Rapport/fs-2023-rapport-isf-quatrieme_rapport_complet_17octobre_avis_0.pdf ; full report: https://www.strategie-plan.gouv.fr/files/files/Publications/Rapport/fs-2023-rapport-isf-quatrieme_rapport_complet_17octobre_2.pdf ; local copy `data/raw/taxation/fstrat/fs-2023-rapport-isf-quatrieme_avis.pdf` - added 2026-10-25.

---

## Verification log (2026-10-25)

### First pass

An adversarial fact-check re-downloaded every core source independently into `research/data/raw/05_verify/` and recomputed group statistics from the raw data. Recomputed statistics are in `research/data/05_verify_recomputed_stats.csv`. Scripts were kept in the session scratchpad, not in the data directory.

### Confirmed (value, unit, year and source match)

| Claim | Check performed | Result |
|---|---|---|
| PO rate 2025 43.6% GDP; 2024 42.7; 2023 43.2; 2022 45.0; 2017 peak 45.3; 1960 30.3; 1980 39.9; all values in table 3.1 | Re-downloaded `econ-fin-pub-prelev-oblig.xlsx` (Insee, 2381412) | Confirmed (43.632; 42.723; 43.154; 45.044; 45.300) |
| PO 1,305.1 bn; implied GDP 2,991 bn; by beneficiary (APUC 378.8, State 357.7, ODAC 21.1, APUL 190.2, ASSO 733.2 = 24.5% GDP, of which taxes 299.1 / contributions 434.1, EU 2.9) | Re-downloaded `t_3216_fr.xlsx` | Confirmed |
| Table 4 (3.217): VAT 208.8; actual SSC 446.3; CSG 156.6; CRDS 9.3; IR gross 103.6 / credits -9.3 / net 94.3; IS 69.5 / credits -10.1; exceptional surtax 7.5; DMTG 21.1 (16.1/5.0); IFI 2.7 (ISF 2017 5.07); CVAE 3.7 (15.2 in 2019); CDHR 0.37; imputed 52.4; tax credits 19.6 bn (2024); 2005 column | Re-downloaded `t_3217_fr.xlsx` | Confirmed |
| Spending 1,714.2 bn = 57.3%; deficit 152.5 bn = 5.1%; +0.9 pt PO; 23.0 bn new measures incl. 8.0 bn temporary surtaxes | Insee IP 2106 PDF (May 2026) | Confirmed |
| PLF 2027 article liminaire: PO 43.6/43.9/44.2 (LPFP 2027: 44.4); spending excl. tax credits 56.6/57.1/56.9 (1,694 bn in 2025); filed 1 Oct 2026; VAT fraction 26.62%; "equitably split" effort | Assemblée nationale text n°3210 | Confirmed |
| OECD tax-to-GDP France 43.5 (2024), 2nd; OECD avg 34.1; median 35.2; gap +9.4; +10.7 (2000); +12.9 (2017 max); 2004/2014/2023 rows; panel values; all rows of table 5.2 except the gap decomposition | SDMX re-download plus OECD country note PDF | Confirmed |
| OECD structure 2023 (SSC 33.2 vs 25.5; PIT 21.5 vs 23.7; VAT 16.6 vs 20.5; property 7.9 vs 5.1; CIT 5.4 vs 11.9) | OECD country note | Confirmed |
| Tax wedge table 5.4 (all 6 rows: values, OECD and EU-22 means/medians, ranks, panel); 47.2 vs 35.1 (3rd); 50.4 in 2000; couple with 2 children 39.1 (2nd); 82% share | SDMX re-download plus Taxing Wages 2026 country note | Confirmed |
| DG TAXUD table 5.3 (all rows incl. ITR labor 38.8 vs 37.1, rank 6, -2.6; ITR consumption 16.4); structure 51.5 / 24.7 / 23.7% | Re-downloaded main aggregates, labor, capital, property, consumption and ITR xlsx (Mar 2026) | Confirmed |
| Eurostat incl. imputed 45.3; EU aggregate 40.2; gap series +3.5/+4.9/+6.6/+7.5/+5.1; D29 4.4 vs 2.4; D611 10.0; PPS table (17,800; 16,157; rank 9/27; panel 6/8; 2004 row) | `gov_10a_taxag` (21 Oct 2026) and `nama_10_pc` (22 Oct 2026) re-download | Confirmed |
| Gini 53.7 / 37.4 / 30.4; EU 47.8 / 34.1 / 29.2; ranks 1 / 4 / 11; panel values | `ilc_di12`, `ilc_di12b`, `ilc_di12c` (20 Oct 2026) | Confirmed (age = TOTAL) |
| Insee IP 2022 table (2022): 393.8 / 1,241.1; 57%; 48% vs 64%; 23.6 to 3.8; 287 vs 954 bn | IP 2022 PDF | Confirmed, but superseded (see corrections) |
| DGFiP n°41: 92 bn (+9.9%); 41.5 m households; 19.6 m = 47.2%; top decile 16,395 EUR, 15.6% / 14.2%, "près des trois quarts"; off-scale tax 10 bn (92% top decile, 54.7% top 0.1%); CEHR ~2 bn; RICI 20 bn, 30.9%, 2,538 vs 49 EUR; -31 EUR D1; capital income +32.1% linked partly to CDHR anticipation | Saved PDF (the official URL now returns a "site en maintenance" page) | Confirmed |
| IPP Note 92: 46% (top 0.1%) vs 26% (top 0.0002%, 75 households); ~2% for 378 households; 26% to 59% simulation; 2016 data | IPP PDF | Confirmed |
| CAE Focus 118: 0.2% vs 0.38%; 0.02-0.23% | CAE PDF | Confirmed (with an added caveat, see below) |
| Cour des comptes NEB: 91.83 bn; 3.07% GDP; 25.76% of net tax revenue; 474 measures; 89.40 final 2024; 78.41/78.74 and 83.29; 85.09; 105.61; 15 measures = 46.7 bn; 52.4% / 46.4% / 20.7%; 55% reliability; Dutreil 0.8 to 4 bn | NEB PDF (April 2026) | Confirmed |
| PLFSS 2026 annex 4: 90.8 / 88.5; 74.7 / 71.8 / 71.5; 64.9 / 62.2 / 61.8; 14.7; >75 bn (39.4 + 36) | Annex PDF | Confirmed |
| Senate inquiry figures: 211 (7 + 41 + 88 + 75), 108, 112 (HCP, July), Lombard ~150 (40 + 30 + 80); Public Sénat article dated 15 Sep 2025 | Public Sénat page | Confirmed |
| Geerolf: 25.1% vs 26.8% | Geerolf PDF (dated Oct 2026) | Confirmed; date added |

### Corrected (visible in the text above)

1. **Distributed national accounts superseded.** Insee Analyses n°118 (16 Apr 2026) gives 2023 data: top 10% pay 33.3% of levies (422.8 / 1,270.9 bn), 56% are net beneficiaries, and the D10/D1 ratio goes from 26 to 3.5. The file said no 2023 edition existed.
2. **HCFP characterization.** "Optimistic" applies to the 2027 growth assumption. The HCFP calls the spontaneous PO forecast "realistic". The primary opinion (25 Sep 2026) is now cited.
3. **Eurostat row label.** The "Taxes + actual compulsory SSC" row actually matched the aggregate that includes voluntary contributions. A compulsory-only row was added (EU aggregate 39.2, mean 36.9, median 36.7; panel mean/median 41.1 / 41.5 instead of 41.4 / 41.9).
4. **Eurostat 2025 coverage.** 20 EU states have 2025 data, not 22. Seven are missing (DE, FR, CY, MT, NL, PL, FI), not four.
5. **OECD gap decomposition rounding.** SSC +5.5 (was 5.6); property +1.7 (1.8); payroll +1.5 (1.6); excises +0.8 (0.9); CIT -1.4 (-1.3); subtotal +8.8 (was +9.0).
6. **VAT convention for tax expenditures.** The change dates from the PLF 2024, not the PLF 2026.
7. **State deficit.** The 128.1 bn is the State's deficit in national accounts (ESA), not the "State budget" (budget-accounting) deficit.
8. **PO 2025 vs 2013-2016.** 43.6 is about 1 pt below the 2013-2016 level, not "about where it was".
9. **Clersé / France Stratégie dates.** Public Sénat dates the studies to 2022 and 2020, not 2019 / ~2019.
10. **CAE Note 69.** Verified in the primary PDF. The yield range is ~9 to ~19 bn (not 12-19). The "~40%" is a gap between declared and economic inheritance flows (1994-2006 surveys), not only legal exemptions.
11. **D29 ranking context.** France is 2nd in the EU; Sweden is 1st (10.1%, because its payroll tax is classified in D29). "~2x" was changed to "~1.8x".

### Fairness and steelman additions

- CAE Focus 118: added the Scandinavian evidence it relies on. Behavioral responses erase about 74% of the mechanical yield of wealth taxes (54 cents intensive margin vs 20 cents exile). This supports the platform's caution about static yield estimates as much as it rebuts the "exodus" argument.
- Zucman tax: added Geerolf's (Oct 2026) 2-6 bn range and his base-concentration argument. The "Trop c'est trop" 1.5-5 bn range is still sourced only via Wikipedia and is marked unverified.
- Think-tank and advocacy orientation flags were already present (Geerolf not peer-reviewed; Clersé for CGT/IRES; "Trop c'est trop" business collective). The CGT/IRES commissioning of the Clersé study is not stated in the cited source.

### Left unverified (⚠) (status as of the first pass; superseded by the 2026-10-25 second pass below)

- PLF 2027 tax-expenditure sums (91.7 / 92.0 / 83.9 bn, 459 items), the breakdown by tax, the largest items, and the annex 5 decile figures. The local "raw" files are bot-protection stubs. The real spreadsheet is downloadable through a browser but could not be parsed in this session.
- PLFSS 2027 reported 3.7 bn yield (press only), and PLFSS 2027 annex 4 (not located).
- "Trop c'est trop" 1.5-5 bn Zucman estimate (Wikipedia only).
- Cour des comptes GDP 2,995 bn (March 2026 vintage), not re-checked.
- France Stratégie capital-tax committee findings (already flagged as from memory).
- OECD publication landing pages (oecd.org/en/publications/...) return HTTP 403 to scripted requests. This is likely bot protection, not a dead link; the PDF country notes and the SDMX endpoints work.
- impots.gouv.fr was in maintenance; the DGFiP n°41 URL could not be re-tested live.

### Superseding publications checked

- OECD Revenue Statistics 2025 (Dec 2025) is still the latest edition; the 2026 edition is expected in Dec 2026.
- OECD Taxing Wages 2026 (Apr 2026) is the latest.
- DG TAXUD Taxation Trends data (Mar 2026) are the latest.
- Insee PO series (Aug 2026) and IP 2106 (May 2026) are the latest.
- The Insee distributed accounts were superseded by IA 118 (Apr 2026), and the text has been updated.
- The HCFP opinion 2026-5 is now cited.

### Second pass (2026-10-25): open ⚠ items and alignment with file 00

**Alignment with `00-reference-figures.md`** (README §8 has no row specific to this file; the "also keep in mind" note on the 152.5 bn deficit applies):
- Deficit 2025: §4 reading 3 and §9 points 2-3 now use the canonical **151.6 bn** (October 2026 EDP notification) instead of 152.5 bn (May 2026 vintage). Recomputed shares: IFI 1.8% (unchanged), ISF restoration ~1.6% (was ~1.5%), Zucman 15-25 bn = ~10-16% (unchanged).
- Total expenditure 2025: summary row 5 now shows Eurostat's 1,714.1 bn = 57.3% (file 00 row 1) beside Insee's 1,714.2 bn.
- OECD rank: summary row 9 now reads "2nd of 36 (2024 data)" as in file 00 row 30 (was "2nd/38").
- Zucman tax: wording aligned with file 00 row 45 (proponents about 20 bn, range 15-25; critics about 2-6 bn).
- Ifop 86% poll, PISA 2025 and the PLF 2027 staffing plan: none of these appears in this file (checked by search), so no flag needed to be removed.

**Confirmed (⚠ removed):**

| Item | Check performed | Result |
|---|---|---|
| PLF 2027 tax-expenditure sums 91.7 / 92.0 / 83.9 bn, 459 items; breakdown by tax; largest items | Annex 1 xls (fid-download/84340, 800,768 bytes) fetched through the browser on budget.gouv.fr; "Chiffrages" sheet exported to `data/raw/taxation/plf2027_browser/PLF2027_VM_T2_annexe1_Chiffrages.csv` and re-summed | Confirmed exactly (91,664 / 92,019 / 83,919 MEUR; 459 distinct items; "nc" = 56 / 62 / 83 items). Still a sum of items, not an official total. |
| 10% pension allowance cut "1.1 bn in 2027" | Annex 2 xlsx (fid-download/84343), sheet "*Bilan mesures 2026-2027*" | Confirmed: "Réduction proposée, PLF 2027, art. 3", 1,100 MEUR in 2027. |
| Annex 5 decile figures (1.30 of 6.50 bn; 1.54 of 5.35 bn; income 2024) | Annex 5 xlsx (fid-download/84352), sheets 110246 and 120401 | Confirmed (1,301 of 6,500; 1,541 of 5,347 MEUR). Added: 6.50 bn excludes the *avance immédiate* (final 6.88 bn). |
| PLFSS 2027 3.7 bn yield | PLFSS 2027 bill n°3211 (Assemblée open data), article 7 exposé des motifs; annex 4 table 6 note | Confirmed: 3.7 bn full scope, 2.8 bn ROBSS scope. The freeze of the scale is confirmed (annex 4); "June 2026 decree" was reworded. |
| PLFSS 2027 annex 4 | Located on securite-sociale.fr (`PLFSS2027-Annexe4-VDEF.pdf`, 2.5 MB) | Retrieved; section 7.2 and summary row 30 updated (2024 total revised 90.8 → 93.2 bn). |
| Cour des comptes GDP 2,995 bn | NEB PDF, footnote 2 | Confirmed as printed by the Cour ("selon l'Insee"); the vintage is not stated. |
| France Stratégie capital-tax committee (from memory) | Committee opinion, fourth and final report (Oct 2023), PDF on strategie-plan.gouv.fr | Confirmed in substance and now sourced [30]; wording made precise (causal PFU effect on dividends, size not estimable; no detected effect on investment or wages). |

**Corrected:**
1. "Trop c'est trop" Zucman estimate: was "1.5-5 bn" (Wikipedia). Now taken from the primary study (June 2026) [29]: static 24 bn (no imputation), **5.5 bn central**, 1.25 bn with full imputation; 45% of the base held by three families confirmed.
2. Niches sociales: the headline moved to the PLFSS 2027 annex 4 vintage (93.2 bn in 2024, 91.0 bn in 2025, 84.4 bn in 2026f), and the 2026 fall is labeled as partly a scope shift.

**Still unverified (⚠ kept):**
- "~89 bn" tax-expenditure total for 2027 (secondary source): not found in any primary document and inconsistent with the 83.9 bn sum of costed items. Recommendation: **drop from site**.
- Official PLF 2027 tome II total of tax expenditures: the tome II PDF was not located. Recommendation: **replace by** the Cour's 91.83 bn (2025) as the headline, with the annex 1 sums as a labeled "sum of items".
- DGFiP top 1% / top 0.1% shares of IR and the "481 households above 9 m EUR" press figure (gap, not displayed): not re-checked in this pass. Recommendation: **drop from site** unless DGFiP n°41 table 4 is retrieved.

**Downloads saved this pass:** `data/raw/taxation/plf2027_browser/` (annex 1 "Chiffrages" CSV export; annexes 2 and 5 sheet exports), `data/raw/taxation/plfss2027/` (bill n°3211 HTML and text; annex 4 PDF and text), `data/raw/taxation/zucman/` (*Trop, c'est trop !* study PDF and text), `data/raw/taxation/fstrat/` (France Stratégie committee opinion PDF and text).
