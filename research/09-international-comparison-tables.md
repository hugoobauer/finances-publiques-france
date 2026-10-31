# 09 - Harmonized international comparison tables (Eurostat / OECD)

*Reference backbone for all other research files. Computed on 2026-10-25 from Eurostat and OECD SDMX APIs. Every number in this file can be regenerated with the script below.*

- **Script:** `research/data/scripts/build_international_comparison.py` (pure Python standard library; run `python3 -I build_international_comparison.py --refresh` to re-download)
- **Raw extracts (untouched API output):** `research/data/raw/09_intl/eurostat/*.csv` and `research/data/raw/09_intl/oecd/*.csv`
- **Computed outputs (CSV):**
  - `research/data/09_intl_comparison_stats.csv`: one row per indicator x year (2005, 2015, latest, latest-1) with France value, aggregates, means, medians, ranks, gaps, panel country values and the EU top 3
  - `research/data/09_intl_long_eurostat.csv`: every series in long format (indicator, geo, year, value, flag)
  - `research/data/09_intl_fr_gap_timeseries.csv`: France vs EA21 vs EU-27 gap, 1995-latest, for the headline indicators
  - `research/data/09_intl_country_values_latest.csv`: latest value of 16 headline indicators for all 27 Member States plus the aggregates
  - `research/data/09_intl_oecd_stats.csv`: OECD-38 tax revenue (Revenue Statistics) and general government accounts (OECD National Accounts at a Glance)
  - `research/data/09_intl_oecd_socx_gross_net.csv`: OECD SOCX, public gross vs. private vs. net total social expenditure
  - `research/data/09_intl_download_log.csv` (exact URL and extraction time of each file) and `research/data/09_intl_eurostat_last_updates.csv` (Eurostat "last update" stamp of each dataset)

---

## 1. Scope and definitions

### 1.1 Sources and dataset codes

| Dataset code | Content | Eurostat last update (from API) | Latest year for France | Used for |
|---|---|---|---|---|
| `gov_10a_main` | Government revenue, expenditure and main aggregates (ESA 2010), sector S13 | 21 Oct 2026 | 2025 | TE, TR, D.1, D.62, D.632, P.2, P.51g, D.41, D.61 |
| `gov_10dd_edpt1` | Government deficit/surplus and debt (EDP notification tables) | 21 Oct 2026 (autumn 2026 EDP notification) | 2025 | Deficit (B.9), Maastricht debt (GD) |
| `gov_10a_exp` | General government expenditure by function (COFOG) | 21 Oct 2026 (France 2023-2024 flagged "p" = provisional) | **2024** | COFOG divisions and groups, % GDP and % of total expenditure |
| `gov_10a_taxag` | Main national accounts tax aggregates, sector S13 + S212 (EU institutions) | 21 Oct 2026 | **2024** | Total taxes + net social contributions |
| `spr_exp_type` | ESSPROS: expenditure on social protection by type (replaces the discontinued `spr_exp_sum`, which the API now reports as "not available for dissemination") | 7 Oct 2026 | 2024 (p) | Social protection expenditure, % GDP and PPS per inhabitant |
| `spr_exp_func` | ESSPROS: social benefits by function, **including 2025 early estimates (flag "e")** | 23 Oct 2026 | 2025 (e) | Total, old-age, sickness benefits |
| `nama_10_pc` | Main GDP aggregates per capita | 22 Oct 2026 | 2025 (p) | GDP per capita in PPS (EU27_2020 = basis) |
| `demo_mlexpec`, `ilc_li02`, `ilc_li10`, `ilc_di12` | Life expectancy; EU-SILC poverty before/after transfers; Gini | 25 Sep / 20 Oct 2026 | 2024 / 2025 (SILC survey year) | Outcome indicators |
| OECD `DSD_REV_COMP_OECD@DF_RSOECD` v2.0 | *Revenue Statistics 2025* (published Dec 2025; 2024 data provisional, 36 of 38 countries) | n/a | 2024 | Total tax revenue % GDP, OECD-38 |
| OECD `DSD_NAAG_VI@DF_NAAG_VI` v1.0 | *National Accounts at a Glance*, Chapter 6 General government | n/a | 2025 (28 countries) / 2024 (37 countries) | GG expenditure, revenue, compensation of employees, OECD-38 |
| OECD `DSD_SOCX_AGG@DF_PUB_PRV` and `@DF_NET_GDP` | SOCX social expenditure: public, private, net | n/a | 2022 (complete); 2023-2024 partial for public gross (added after verification) / 2021 (net) | Steelman: gross vs. net social spending |

### 1.2 Definitions and conventions

- **General government (S13)** = central government (State and *organismes divers d'administration centrale*, ODAC) + local government (*administrations publiques locales*, APUL) + social security funds (*administrations de sécurité sociale*, ASSO), consolidated, ESA 2010. This is the same perimeter Insee uses for *dépense publique* (public expenditure).
- **TE (total expenditure)** and **TR (total revenue)** are ESA 2010 concepts (Eurostat). For France, TE 2025 = EUR 1,714.1 bn = 57.3% of GDP, and TR 2025 = EUR 1,562.5 bn = 52.2% of GDP. GDP 2025 = EUR 2,991.1 bn (`gov_10dd_edpt1`, B1GQ). **Rule of thumb: 1 percentage point (pp) of French GDP is about EUR 30 bn in 2025.**
- **"% of GDP" vs "% of total expenditure"**: unless labeled "% of total GG expenditure", every figure is **% of GDP**. COFOG shares of total expenditure come from unit `PC_TOT` of `gov_10a_exp`.
- **Aggregates vs. means.** The Eurostat aggregates (`EU27_2020`, `EA21`, `EA20`) are **GDP-weighted**: they are ratios of summed euro amounts, so Germany, France and Italy dominate them. The **means and medians** are **unweighted** across Member States, so Malta counts as much as Germany. France minus the aggregate measures distance to "the average euro of EU GDP". France minus the mean or median measures distance to "the typical country". Both are reported.
- **Euro area.** Bulgaria joined on 1 January 2026, so the current composition is **EA21**. Eurostat's own 2025 headline in the 21 Oct 2026 news release still uses **EA20** (the composition in force in 2025). Both aggregates are shown. Member-state means, medians and ranks use the 21 current members for every year (fixed composition, so 2005 and 2015 statistics include countries that had not yet adopted the euro).
- **Panel** = DE, IT, ES, NL, BE, SE, DK. Panel mean and median **exclude France**; France's panel rank is out of 8 (panel + France).
- **Rank:** 1 = highest value. For the deficit (B.9), the rank is computed on the size of the deficit (1 = largest deficit).
- **Years:** "2005", "2015" and "latest" (2025 for `gov_10a_main`, `gov_10dd_edpt1`, `nama_10_pc` and ESSPROS early estimates; 2024 for COFOG, tax aggregates and full ESSPROS). The latest year minus 1 is also in the CSV.
- **PPS per inhabitant:** Eurostat Purchasing Power Standard (EU27_2020 = 1). For total expenditure and COFOG functions, per capita PPS is **derived** as (% of GDP / 100) x GDP per capita in PPS (`nama_10_pc`, `CP_PPS_EU27_2020_HAB`). This applies the **GDP-wide PPP**, not a government-specific PPP. ESSPROS PPS figures (`spr_exp_type`, `spr_exp_func`) are published directly by Eurostat.
- **Flags:** p = provisional, e = estimated (Eurostat flags carried through in `09_intl_long_eurostat.csv`).

---

## 2. Key figures (France, latest year)

| # | Indicator | France | Unit | Data year | Comparator | Source (dataset, publication / update date) |
|---|---|---|---|---|---|---|
| 1 | Total general government expenditure | **57.3** (EUR 1,714.1 bn) | % of GDP | 2025 | EA20 49.8; EA21 49.7; EU-27 49.4; France ranked **2nd of 27, behind Finland (57.5)** | Eurostat `gov_10a_main`, update 21 Oct 2026 [E1] |
| 2 | Total general government revenue | **52.2** (EUR 1,562.5 bn) | % of GDP | 2025 | EA21 46.7; EU-27 46.3; 2nd of 26 reporting (Denmark not yet disseminated), behind FI 53.7 | [E1] |
| 3 | Deficit (EDP B.9) | **-5.1** | % of GDP | 2025 | EA20 -3.0; EU-27 -3.1; 4th-largest deficit (RO -7.8, PL -7.2, BE -5.2) | Eurostat `gov_10dd_edpt1`; Euro indicators news release 21 Oct 2026 [E2][E3] |
| 4 | Maastricht gross debt | **115.7** | % of GDP | 2025 | EA20 87.7; EU-27 81.5; 3rd (EL 145.4, IT 136.7) | [E2][E3] |
| 5 | Total taxes + net social contributions (S13+S212) | **45.3** (as published; **45.0** at current 2024 GDP) | % of GDP | 2024 | EU-27 40.2; EA21 40.6; 2nd behind DK 45.5 in the published table. *Vintage note (2026-10-25): the published % of GDP uses a pre-May-2026 GDP for France and Denmark. EUR amounts / current GDP (`nama_10_gdp`, 22 Oct 2026) give BE 45.2, FR 45.0, DK 44.7, so France is 2nd behind **Belgium**.* | Eurostat `gov_10a_taxag` [E4]; `data/raw/09_pass3/taxag_all_2024.json` |
| 6 | Same, excluding imputed (D.612) and voluntary household (D.614) contributions (closest Eurostat concept to Insee's *prélèvements obligatoires*) | **43.5** (as published; **43.3** at current 2024 GDP) | % of GDP | 2024 | EU-27 39.3; EA21 39.6; 2nd of 27 behind DK on both GDP vintages (at current GDP: DK 44.6, FR 43.3). **Not equal to Insee PO:** Insee's 2024 PO rate is **42.7%** (net of tax credits), 0.8 pp lower than the published 43.5% and 0.6 pp lower at current GDP; about 0.7 pp of that is tax credits (bridge in section 6, verified 2026-10-25) | [E4]; Insee [I1] |
| 7 | OECD total tax revenue | **43.5** | % of GDP | 2024 | OECD average 34.1; 2nd of 36 reporting, behind DK 45.2 | OECD *Revenue Statistics 2025* (Dec 2025) [O1] |
| 8 | COFOG 10 Social protection | **23.6** (corrected 2026-10-25: was 23.7, the COFOG table's own ratio on a pre-May-2026 GDP) | % of GDP | 2024 | EA21 aggregate 20.0; EU-27 aggregate 19.5; 2nd of 27 behind FI 26.4 (all at current GDP) | Eurostat `gov_10a_exp` EUR amounts / `nama_10_gdp` (21-22 Oct 2026) [E5]; file 00 row 11 |
| 9 | COFOG 10 Social protection | **41.5** | % of total GG expenditure | 2024 | EA21 40.7; EU-27 40.0; 4th | [E5] |
| 10 | COFOG 10.2 Old age | **13.4** | % of GDP | 2024 | EA21 10.8; EU-27 10.6; 4th (FI 15.5, AT 14.3, IT 13.9) | [E5] |
| 11 | COFOG 07 Health | **8.9** | % of GDP | 2024 | EA21 7.4; EU-27 7.3; 4th | [E5] |
| 12 | COFOG 09 Education | **5.1** | % of GDP | 2024 | EA21 4.6; EU-27 4.7; 11th (near the median, 5.0) | [E5] |
| 13 | COFOG 02 Defense | **1.8** (1.85; corrected 2026-10-25: was 1.9, the COFOG table's own ratio on a pre-May-2026 GDP) | % of GDP | 2024 | EA21 aggregate 1.4; EU-27 aggregate 1.5; **8th of 27** at current GDP (EE 3.7, PL 2.9, LV 2.7, LT 2.6, EL 2.2, HU 2.0, SE 1.95); was 7th (tied with SE at 1.9) in the published table | Eurostat `gov_10a_exp` EUR amounts / `nama_10_gdp` [E5]; file 00 row 15 |
| 14 | COFOG 01.7 Public debt transactions (interest) | **2.0** | % of GDP | 2024 | EA21 1.9; EU-27 1.9; 9th | [E5] |
| 15 | Compensation of government employees (D.1) | **12.4** | % of GDP | 2025 | EA21 10.0; EU-27 10.3; 6th (DK 14.2) | [E1] |
| 16 | Social protection benefits (ESSPROS) | **31.96** (p) | % of GDP | 2024 | EU-27 27.41; 2nd behind FI 32.5 | Eurostat `spr_exp_type` / `spr_exp_func` [E6] |
| 17 | Social protection benefits (ESSPROS early estimate) | **32.12** (e) | % of GDP | 2025 | EU-27 27.49; 3rd (AT 32.4, FI 32.2) | Eurostat `spr_exp_func`, update 23 Oct 2026 [E6] |
| 18 | Total social protection expenditure (ESSPROS, incl. administration) | **34.37** (p) | % of GDP | 2024 | EU-27 28.55; **1st** | [E6] |
| 19 | Total social protection expenditure (ESSPROS) | **13,557** | PPS per inhabitant | 2024 | EU-27 11,431; **6th** (top 3: LU 19,788, AT 14,934, DE 14,838) | [E6] |
| 20 | Total GG expenditure per inhabitant (derived) | **23,330** | PPS per inhabitant | 2025 | EU-27 20,636; EA21 21,424; panel mean 23,036; **8th** of 27, **5th of 8** in panel | [E1] x [E7] |
| 21 | GDP per inhabitant | **40,716** (p) | PPS | 2025 | EU-27 41,774; 12th of 27 | Eurostat `nama_10_pc` [E7] |

**Reconciling the user's starting figures:**
- *Public expenditure 2025 = EUR 1,714 bn = 57.3% of GDP (Insee)*: **confirmed exactly** by Eurostat `gov_10a_main` (EUR 1,714,111.7 m; 57.3%) and by OECD NAAG (57.31%). This is the same ESA 2010 transmission. **New element:** France is no longer the EU's highest-spending country in 2025. Finland (57.5%) has passed it, as it already had in 2024 (FI 57.9 vs FR 57.0).
- *Social protection benefits 2024 = 31.9% of GDP (Drees)*: **consistent** with Eurostat ESSPROS 31.96% (provisional). The Drees *Comptes de la protection sociale* (social protection accounts) are France's ESSPROS transmission. The 2025 early estimate is 32.12%.
- *Compulsory levies 2025 = 43.6% of GDP (Insee)*: **confirmed in the Insee source** (*Le compte des administrations publiques en 2025*, Insee Première, 29 May 2026: PO 43.6% in 2025, **42.7% in 2024**, "net of tax credits") [I1]. It is **not directly verifiable in Eurostat yet**, because `gov_10a_taxag` stops at 2024. The closest Eurostat concept gives 43.5% in 2024 (row 6), and OECD gives 43.5% in 2024. Eurostat's broad measure (incl. imputed contributions) gives 45.3% in 2024. **Caution (added after verification):** the 2024 Eurostat/OECD 43.5% must not be read as "the same as Insee's 43.6%". Those are different years, and the like-for-like Insee 2024 value is 42.7%, 0.8 pp below the international measures. See section 6 for why the measures differ.

---

## 3. Detailed comparison tables (EU-27, euro area, panel)

How to read these tables: "EA agg." shows EA21 / EA20 (GDP-weighted). "MS mean / median" is the unweighted mean and median across Member States. Ranks: 1 = highest (for the deficit, 1 = largest deficit). "n/a" for the 2005 COFOG and ESSPROS aggregates means Eurostat does not publish an EU-27/EA aggregate for that year (COFOG Slovakia 2005 and ESSPROS Croatia 2005 are also missing). In that case the means and medians cover 26 countries. The "Src" column gives the Eurostat dataset code. Full URLs are in section 10. All values are taken from `09_intl_comparison_stats.csv`.

### 3.1 Tables by block

#### Headline aggregates

| Indicator | Unit | Year | France | EU-27 agg. | EA agg. (EA21 / EA20) | EU-27 MS mean / median | FR rank EU-27 | EA21 MS mean / median | FR rank EA21 | Panel mean / median | FR rank panel (of 8) | FR - EA agg. (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Total general government expenditure | % of GDP | 2005 | **54.3** | 47.2 | 47.2 / 47.2 | 43.8 / 44.1 | 1/27 | 43.3 / 43.5 | 1/21 | 47.3 / 47.1 | 1/8 | 7.1 | [gov_10a_main] |
| Total general government expenditure | % of GDP | 2015 | **57.6** | 48.3 | 48.6 / 48.6 | 45.4 / 44.4 | 1/27 | 45.3 / 44.4 | 1/21 | 48.9 / 50.3 | 1/8 | 9.0 | [gov_10a_main] |
| Total general government expenditure | % of GDP | 2025 | **57.3** | 49.4 | 49.7 / 49.8 | 46.4 / 47.3 | 2/27 | 46.3 / 47.3 | 2/21 | 48.9 / 49.3 | 1/8 | 7.6 | [gov_10a_main] |
| Total general government revenue | % of GDP | 2005 | **50.8** | 44.8 | 44.6 / 44.6 | 42.2 / 40.7 | 4/27 | 41.7 / 40.7 | 2/21 | 47.0 / 43.5 | 3/8 | 6.2 | [gov_10a_main] |
| Total general government revenue | % of GDP | 2015 | **53.7** | 46.4 | 46.6 / 46.6 | 43.5 / 43.4 | 1/27 | 43.2 / 43.4 | 1/21 | 47.1 / 47.9 | 1/8 | 7.1 | [gov_10a_main] |
| Total general government revenue | % of GDP | 2025 | **52.2** | 46.3 | 46.7 / 46.8 | 43.8 / 43.6 | 2/26 | 44.1 / 43.6 | 2/21 | 46.5 / 47.5 | 1/7 | 5.5 | [gov_10a_main] |
| Net lending(+)/borrowing(-) (EDP deficit) | % of GDP | 2005 | **-3.5** | -2.4 | -2.6 / -2.7 | -1.6 / -2.1 | 6/27 | -1.6 / -2.1 | 4/21 | -0.3 / -0.5 | 2/8 | -0.9 | [gov_10dd_edpt1] |
| Net lending(+)/borrowing(-) (EDP deficit) | % of GDP | 2015 | **-3.9** | -1.9 | -2.0 / -2.0 | -1.9 / -1.9 | 4/27 | -2.1 / -2.0 | 4/21 | -1.8 / -1.8 | 2/8 | -1.9 | [gov_10dd_edpt1] |
| Net lending(+)/borrowing(-) (EDP deficit) | % of GDP | 2025 | **-5.1** | -3.1 | -3.0 / -3.0 | -2.4 / -2.5 | 4/27 | -2.1 / -2.5 | 2/21 | -2.0 / -2.4 | 2/8 | -2.1 | [gov_10dd_edpt1] |
| Gross debt (Maastricht) | % of GDP | 2005 | **68.2** | 67.2 | 70.2 / 70.3 | 47.9 / 42.4 | 7/27 | 50.2 / 42.4 | 7/21 | 64.1 / 49.6 | 3/8 | -2.0 | [gov_10dd_edpt1] |
| Gross debt (Maastricht) | % of GDP | 2015 | **97.0** | 85.0 | 90.7 / 91.0 | 71.5 / 68.8 | 7/27 | 78.0 / 74.1 | 7/21 | 81.1 / 71.0 | 4/8 | 6.3 | [gov_10dd_edpt1] |
| Gross debt (Maastricht) | % of GDP | 2025 | **115.7** | 81.5 | 87.3 / 87.7 | 64.9 / 58.9 | 3/27 | 69.2 / 60.5 | 3/21 | 73.6 / 62.8 | 2/8 | 28.4 | [gov_10dd_edpt1] |
| Total taxes and net social contributions (S13+S212, after D.995) | % of GDP | 2005 | **44.7** | 39.7 | 39.6 / 39.6 | 36.6 / 36.1 | 4/27 | 36.1 / 36.1 | 2/21 | 41.8 / 39.0 | 4/8 | 5.1 | [gov_10a_taxag] |
| Total taxes and net social contributions (S13+S212, after D.995) | % of GDP | 2015 | **47.7** | 40.8 | 41.2 / 41.2 | 37.0 / 37.0 | 1/27 | 36.9 / 37.0 | 1/21 | 42.0 / 43.2 | 1/8 | 6.5 | [gov_10a_taxag] |
| Total taxes and net social contributions (S13+S212, after D.995) | % of GDP | 2024 | **45.3** | 40.2 | 40.6 / 40.6 | 37.7 / 37.6 | 2/27 | 37.8 / 38.0 | 1/21 | 41.8 / 41.8 | 2/8 | 4.7 | [gov_10a_taxag] |
| Taxes and actual compulsory social contributions (excl. imputed D.612 and households' voluntary D.614; closest to Insee 'prelevements obligatoires') | % of GDP | 2005 | **42.9** | 38.7 | 38.4 / 38.5 | 35.8 / 35.3 | 4/27 | 35.1 / 35.3 | 2/21 | 41.0 / 38.8 | 4/8 | 4.5 | [gov_10a_taxag] |
| Taxes and actual compulsory social contributions (excl. imputed D.612 and households' voluntary D.614; closest to Insee 'prelevements obligatoires') | % of GDP | 2015 | **45.7** | 39.8 | 40.1 / 40.1 | 36.2 / 35.4 | 2/27 | 35.9 / 35.4 | 1/21 | 41.2 / 43.0 | 2/8 | 5.6 | [gov_10a_taxag] |
| Taxes and actual compulsory social contributions (excl. imputed D.612 and households' voluntary D.614; closest to Insee 'prelevements obligatoires') | % of GDP | 2024 | **43.5** | 39.3 | 39.6 / 39.7 | 37.0 / 36.8 | 2/27 | 37.0 / 38.0 | 1/21 | 41.0 / 41.6 | 2/8 | 3.9 | [gov_10a_taxag] |
| Taxes only (D.2+D.5+D.91, S13+S212) | % of GDP | 2005 | **27.3** | 25.7 | 24.7 / 24.7 | 25.3 / 24.2 | 6/27 | 24.2 / 24.2 | 4/21 | 30.9 / 26.9 | 4/8 | 2.6 | [gov_10a_taxag] |
| Taxes only (D.2+D.5+D.91, S13+S212) | % of GDP | 2015 | **29.2** | 26.8 | 26.2 / 26.2 | 25.5 / 24.6 | 6/27 | 24.6 / 24.6 | 4/21 | 31.2 / 30.0 | 5/8 | 3.0 | [gov_10a_taxag] |
| Taxes only (D.2+D.5+D.91, S13+S212) | % of GDP | 2024 | **28.9** | 26.3 | 26.0 / 26.0 | 25.8 / 24.5 | 7/27 | 25.2 / 24.5 | 5/21 | 31.0 / 29.8 | 5/8 | 2.9 | [gov_10a_taxag] |
| Net social contributions (D.61, S13+S212) | % of GDP | 2005 | **17.6** | 14.1 | 14.9 / 14.9 | 11.3 / 11.9 | 1/27 | 11.9 / 11.9 | 1/21 | 10.9 / 12.6 | 1/8 | 2.7 | [gov_10a_taxag] |
| Net social contributions (D.61, S13+S212) | % of GDP | 2015 | **18.7** | 14.1 | 15.1 / 15.1 | 11.6 / 12.1 | 1/27 | 12.3 / 12.1 | 1/21 | 11.0 / 13.2 | 1/8 | 3.6 | [gov_10a_taxag] |
| Net social contributions (D.61, S13+S212) | % of GDP | 2024 | **16.5** | 13.9 | 14.6 / 14.6 | 11.9 / 12.6 | 3/27 | 12.5 / 12.6 | 3/21 | 10.8 / 12.6 | 2/8 | 1.9 | [gov_10a_taxag] |

#### Economic classification (ESA 2010, gov_10a_main)

| Indicator | Unit | Year | France | EU-27 agg. | EA agg. (EA21 / EA20) | EU-27 MS mean / median | FR rank EU-27 | EA21 MS mean / median | FR rank EA21 | Panel mean / median | FR rank panel (of 8) | FR - EA agg. (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Compensation of employees (D.1, payable) | % of GDP | 2005 | **13.0** | 10.6 | 10.4 / 10.4 | 11.1 / 10.9 | 6/27 | 10.9 / 10.6 | 5/21 | 11.1 / 10.6 | 2/8 | 2.6 | [gov_10a_main] |
| Compensation of employees (D.1, payable) | % of GDP | 2015 | **13.0** | 10.3 | 10.2 / 10.2 | 10.7 / 10.6 | 3/27 | 10.6 / 10.8 | 2/21 | 11.2 / 11.0 | 2/8 | 2.8 | [gov_10a_main] |
| Compensation of employees (D.1, payable) | % of GDP | 2025 | **12.4** | 10.3 | 10.0 / 10.0 | 11.2 / 11.5 | 6/27 | 11.1 / 11.5 | 5/21 | 10.9 / 10.7 | 3/8 | 2.4 | [gov_10a_main] |
| Social benefits other than in kind (D.62) | % of GDP | 2005 | **17.5** | 15.6 | 15.7 / 15.7 | 13.4 / 13.9 | 3/27 | 13.3 / 13.3 | 3/21 | 14.6 / 15.1 | 2/8 | 1.8 | [gov_10a_main] |
| Social benefits other than in kind (D.62) | % of GDP | 2015 | **19.7** | 16.5 | 16.9 / 16.9 | 14.7 / 14.3 | 3/27 | 15.0 / 15.2 | 3/21 | 15.7 / 15.7 | 2/8 | 2.8 | [gov_10a_main] |
| Social benefits other than in kind (D.62) | % of GDP | 2025 | **19.4** | 16.4 | 16.8 / 16.9 | 14.4 / 14.1 | 3/27 | 14.8 / 15.9 | 3/21 | 15.4 / 16.5 | 2/8 | 2.6 | [gov_10a_main] |
| Social transfers in kind via market producers (D.632) | % of GDP | 2005 | **5.6** | 4.6 | 4.9 / 4.9 | 2.7 / 2.2 | 4/27 | 2.9 / 2.2 | 4/21 | 4.4 / 2.7 | 4/8 | 0.7 | [gov_10a_main] |
| Social transfers in kind via market producers (D.632) | % of GDP | 2015 | **6.2** | 5.2 | 5.6 / 5.6 | 3.0 / 2.4 | 4/27 | 3.3 / 2.6 | 4/21 | 5.2 / 3.6 | 4/8 | 0.6 | [gov_10a_main] |
| Social transfers in kind via market producers (D.632) | % of GDP | 2025 | **6.4** | 5.4 | 6.0 / 6.0 | 3.4 / 2.8 | 4/27 | 3.8 / 2.8 | 4/21 | 5.4 / 3.5 | 4/8 | 0.4 | [gov_10a_main] |
| Intermediate consumption (P.2) | % of GDP | 2005 | **5.1** | 5.3 | 5.1 / 5.1 | 6.0 / 6.0 | 19/27 | 5.7 / 5.3 | 13/21 | 5.8 / 5.3 | 5/8 | 0.0 | [gov_10a_main] |
| Intermediate consumption (P.2) | % of GDP | 2015 | **5.3** | 5.7 | 5.5 / 5.5 | 6.0 / 5.8 | 19/27 | 5.7 / 5.5 | 13/21 | 6.3 / 5.6 | 6/8 | -0.2 | [gov_10a_main] |
| Intermediate consumption (P.2) | % of GDP | 2025 | **5.5** | 6.1 | 5.9 / 5.9 | 6.3 / 5.8 | 19/27 | 6.0 / 5.7 | 13/21 | 6.5 / 6.4 | 7/8 | -0.4 | [gov_10a_main] |
| Gross fixed capital formation (P.51g) | % of GDP | 2005 | **4.4** | 3.4 | 3.4 / 3.4 | 3.8 / 3.7 | 7/27 | 3.8 / 3.7 | 6/21 | 3.1 / 3.1 | 1/8 | 1.0 | [gov_10a_main] |
| Gross fixed capital formation (P.51g) | % of GDP | 2015 | **3.9** | 3.2 | 3.0 / 2.9 | 4.0 / 3.8 | 12/27 | 3.7 / 3.8 | 7/21 | 3.1 / 2.6 | 2/8 | 0.9 | [gov_10a_main] |
| Gross fixed capital formation (P.51g) | % of GDP | 2025 | **4.4** | 3.9 | 3.7 / 3.7 | 4.4 / 4.4 | 14/27 | 4.3 / 4.4 | 10/21 | 3.7 / 3.5 | 2/8 | 0.7 | [gov_10a_main] |
| Interest payable (D.41, ESA) | % of GDP | 2005 | **2.7** | 2.8 | 2.9 / 2.9 | 2.2 / 1.8 | 8/27 | 2.2 / 1.8 | 7/21 | 2.8 / 2.3 | 3/8 | -0.2 | [gov_10a_main] |
| Interest payable (D.41, ESA) | % of GDP | 2015 | **2.0** | 2.2 | 2.3 / 2.3 | 2.1 / 1.8 | 13/27 | 2.3 / 2.3 | 12/21 | 2.1 / 1.4 | 4/8 | -0.3 | [gov_10a_main] |
| Interest payable (D.41, ESA) | % of GDP | 2025 | **2.2** | 1.9 | 1.9 / 1.9 | 1.6 / 1.3 | 8/27 | 1.5 / 1.3 | 5/21 | 1.7 / 1.1 | 4/8 | 0.3 | [gov_10a_main] |
| Net social contributions received (D.61) | % of GDP | 2005 | **17.6** | 14.1 | 14.9 / 14.9 | 11.3 / 11.9 | 1/27 | 11.9 / 11.9 | 1/21 | 10.9 / 12.6 | 1/8 | 2.7 | [gov_10a_main] |
| Net social contributions received (D.61) | % of GDP | 2015 | **18.7** | 14.1 | 15.1 / 15.1 | 11.6 / 12.1 | 1/27 | 12.3 / 12.1 | 1/21 | 10.9 / 13.2 | 1/8 | 3.6 | [gov_10a_main] |
| Net social contributions received (D.61) | % of GDP | 2025 | **16.7** | 14.3 | 15.1 / 15.1 | 12.1 / 12.6 | 3/27 | 12.8 / 12.8 | 3/21 | 11.0 / 13.2 | 2/8 | 1.6 | [gov_10a_main] |

#### COFOG divisions (% of GDP)

| Indicator | Unit | Year | France | EU-27 agg. | EA agg. (EA21 / EA20) | EU-27 MS mean / median | FR rank EU-27 | EA21 MS mean / median | FR rank EA21 | Panel mean / median | FR rank panel (of 8) | FR - EA agg. (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COFOG GF01 General public services | % of GDP | 2005 | **7.4** | n/a | n/a / n/a | 6.3 / 6.2 | 7/26 | 6.4 / 6.2 | 6/20 | 7.0 / 6.3 | 3/8 | n/a | [gov_10a_exp] |
| COFOG GF01 General public services | % of GDP | 2015 | **6.6** | 6.5 | 6.6 / 6.6 | 6.3 / 6.2 | 11/27 | 6.4 / 6.5 | 9/21 | 6.6 / 6.5 | 4/8 | 0.0 | [gov_10a_exp] |
| COFOG GF01 General public services | % of GDP | 2024 | **6.2** (p) | 6.0 | 6.1 / 6.1 | 5.6 / 5.5 | 7/27 | 5.4 / 5.5 | 6/21 | 6.0 / 5.8 | 4/8 | 0.1 | [gov_10a_exp] |
| COFOG GF02 Defense | % of GDP | 2005 | **1.8** | n/a | n/a / n/a | 1.4 / 1.3 | 4/26 | 1.3 / 1.3 | 3/20 | 1.2 / 1.2 | 1/8 | n/a | [gov_10a_exp] |
| COFOG GF02 Defense | % of GDP | 2015 | **1.7** | 1.2 | 1.2 / 1.2 | 1.1 / 1.1 | 3/27 | 1.1 / 1.1 | 3/21 | 1.0 / 1.1 | 1/8 | 0.5 | [gov_10a_exp] |
| COFOG GF02 Defense | % of GDP | 2024 | **1.9** (p) [**1.8** (1.85) at current GDP, 8th of 27: canonical, see section 2 row 13] | 1.5 | 1.4 / 1.4 | 1.6 / 1.5 | 7/27 | 1.5 / 1.4 | 5/21 | 1.5 / 1.4 | 1/8 | 0.5 | [gov_10a_exp] |
| COFOG GF03 Public order and safety | % of GDP | 2005 | **1.5** | n/a | n/a / n/a | 1.8 / 1.8 | 19/26 | 1.8 / 1.7 | 15/20 | 1.6 / 1.7 | 6/8 | n/a | [gov_10a_exp] |
| COFOG GF03 Public order and safety | % of GDP | 2015 | **1.6** | 1.7 | 1.7 / 1.7 | 1.8 / 1.7 | 17/27 | 1.7 / 1.7 | 13/21 | 1.6 / 1.7 | 5/8 | -0.1 | [gov_10a_exp] |
| COFOG GF03 Public order and safety | % of GDP | 2024 | **1.8** (p) | 1.7 | 1.7 / 1.7 | 1.8 / 1.7 | 9/27 | 1.8 / 1.7 | 7/21 | 1.6 / 1.7 | 2/8 | 0.1 | [gov_10a_exp] |
| COFOG GF04 Economic affairs | % of GDP | 2005 | **5.2** | n/a | n/a / n/a | 5.1 / 4.8 | 10/26 | 5.1 / 4.8 | 7/20 | 4.8 / 4.4 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF04 Economic affairs | % of GDP | 2015 | **6.2** | 5.1 | 5.1 / 5.0 | 5.5 / 5.0 | 9/27 | 5.4 / 5.0 | 7/21 | 4.8 / 4.5 | 2/8 | 1.1 | [gov_10a_exp] |
| COFOG GF04 Economic affairs | % of GDP | 2024 | **5.7** (p) | 5.3 | 5.2 / 5.2 | 5.3 / 5.5 | 12/27 | 5.2 / 5.5 | 9/21 | 4.9 / 5.1 | 2/8 | 0.5 | [gov_10a_exp] |
| COFOG GF05 Environmental protection | % of GDP | 2005 | **0.8** | n/a | n/a / n/a | 0.7 / 0.7 | 7/26 | 0.8 / 0.8 | 6/20 | 0.8 / 0.8 | 3/8 | n/a | [gov_10a_exp] |
| COFOG GF05 Environmental protection | % of GDP | 2015 | **0.9** | 0.8 | 0.8 / 0.8 | 0.8 / 0.8 | 10/27 | 0.8 / 0.8 | 7/21 | 0.8 / 0.9 | 3/8 | 0.1 | [gov_10a_exp] |
| COFOG GF05 Environmental protection | % of GDP | 2024 | **1.0** (p) | 0.8 | 0.9 / 0.9 | 0.8 / 0.7 | 6/27 | 0.8 / 0.7 | 6/21 | 0.9 / 0.9 | 3/8 | 0.1 | [gov_10a_exp] |
| COFOG GF06 Housing and community amenities | % of GDP | 2005 | **1.1** | n/a | n/a / n/a | 0.8 / 0.7 | 7/26 | 0.8 / 0.7 | 4/20 | 0.6 / 0.6 | 1/8 | n/a | [gov_10a_exp] |
| COFOG GF06 Housing and community amenities | % of GDP | 2015 | **1.2** | 0.6 | 0.6 / 0.6 | 0.7 / 0.5 | 5/27 | 0.7 / 0.5 | 4/21 | 0.4 / 0.5 | 1/8 | 0.6 | [gov_10a_exp] |
| COFOG GF06 Housing and community amenities | % of GDP | 2024 | **1.4** (p) | 0.7 | 0.7 / 0.7 | 0.8 / 0.6 | 4/27 | 0.7 / 0.6 | 3/21 | 0.6 / 0.5 | 1/8 | 0.7 | [gov_10a_exp] |
| COFOG GF07 Health | % of GDP | 2005 | **7.8** | n/a | n/a / n/a | 5.9 / 6.2 | 1/26 | 5.9 / 6.2 | 1/20 | 6.4 / 6.6 | 1/8 | n/a | [gov_10a_exp] |
| COFOG GF07 Health | % of GDP | 2015 | **8.2** | 7.0 | 7.1 / 7.1 | 6.1 / 6.1 | 3/27 | 6.0 / 6.1 | 2/21 | 7.3 / 7.0 | 2/8 | 1.1 | [gov_10a_exp] |
| COFOG GF07 Health | % of GDP | 2024 | **8.9** (p) | 7.3 | 7.4 / 7.4 | 6.8 / 6.6 | 4/27 | 6.8 / 6.6 | 3/21 | 7.4 / 7.4 | 1/8 | 1.5 | [gov_10a_exp] |
| COFOG GF08 Recreation, culture and religion | % of GDP | 2005 | **1.5** | n/a | n/a / n/a | 1.2 / 1.3 | 5/26 | 1.2 / 1.2 | 3/20 | 1.3 / 1.4 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF08 Recreation, culture and religion | % of GDP | 2015 | **1.5** | 1.1 | 1.1 / 1.1 | 1.3 / 1.2 | 7/27 | 1.2 / 1.2 | 5/21 | 1.2 / 1.2 | 2/8 | 0.4 | [gov_10a_exp] |
| COFOG GF08 Recreation, culture and religion | % of GDP | 2024 | **1.5** (p) | 1.2 | 1.1 / 1.1 | 1.3 / 1.3 | 5/27 | 1.2 / 1.2 | 4/21 | 1.2 / 1.2 | 1/8 | 0.4 | [gov_10a_exp] |
| COFOG GF09 Education | % of GDP | 2005 | **5.5** | n/a | n/a / n/a | 5.3 / 5.5 | 12/26 | 5.2 / 5.5 | 8/20 | 5.3 / 5.1 | 4/8 | n/a | [gov_10a_exp] |
| COFOG GF09 Education | % of GDP | 2015 | **5.3** | 4.7 | 4.6 / 4.6 | 5.0 / 5.1 | 9/27 | 4.9 / 5.0 | 7/21 | 5.4 / 5.2 | 4/8 | 0.7 | [gov_10a_exp] |
| COFOG GF09 Education | % of GDP | 2024 | **5.1** (p) | 4.7 | 4.6 / 4.6 | 5.0 / 5.0 | 11/27 | 5.0 / 5.0 | 8/21 | 5.3 / 5.1 | 4/8 | 0.5 | [gov_10a_exp] |
| COFOG GF10 Social protection | % of GDP | 2005 | **21.7** | n/a | n/a / n/a | 15.5 / 15.4 | 3/26 | 15.1 / 15.2 | 1/20 | 18.3 / 17.1 | 3/8 | n/a | [gov_10a_exp] |
| COFOG GF10 Social protection | % of GDP | 2015 | **24.3** | 19.6 | 19.9 / 19.9 | 16.8 / 17.0 | 2/27 | 17.0 / 17.2 | 2/21 | 19.7 / 19.5 | 1/8 | 4.4 | [gov_10a_exp] |
| COFOG GF10 Social protection | % of GDP | 2024 | **23.7** (p) [**23.6** at current GDP: canonical, see section 2 row 8] | 19.5 | 20.0 / 20.0 | 17.0 / 17.1 | 2/27 | 17.2 / 17.1 | 2/21 | 19.4 / 19.6 | 1/8 | 3.7 | [gov_10a_exp] |

#### COFOG groups (% of GDP)

| Indicator | Unit | Year | France | EU-27 agg. | EA agg. (EA21 / EA20) | EU-27 MS mean / median | FR rank EU-27 | EA21 MS mean / median | FR rank EA21 | Panel mean / median | FR rank panel (of 8) | FR - EA agg. (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COFOG GF0107 Public debt transactions (interest) | % of GDP | 2005 | **2.8** | n/a | n/a / n/a | 2.3 / 1.9 | 9/26 | 2.4 / 2.1 | 8/20 | 2.9 / 2.3 | 4/8 | n/a | [gov_10a_exp] |
| COFOG GF0107 Public debt transactions (interest) | % of GDP | 2015 | **2.2** | 2.4 | 2.5 / 2.5 | 2.2 / 1.8 | 13/27 | 2.4 / 2.3 | 12/21 | 2.3 / 1.5 | 4/8 | -0.3 | [gov_10a_exp] |
| COFOG GF0107 Public debt transactions (interest) | % of GDP | 2024 | **2.0** (p) | 1.9 | 1.9 / 1.9 | 1.7 / 1.4 | 9/27 | 1.6 / 1.3 | 6/21 | 1.7 / 1.1 | 4/8 | 0.1 | [gov_10a_exp] |
| COFOG GF1001 Sickness and disability | % of GDP | 2005 | **2.5** | n/a | n/a / n/a | 2.5 / 2.2 | 10/26 | 2.3 / 2.0 | 5/20 | 3.5 / 2.5 | 4/8 | n/a | [gov_10a_exp] |
| COFOG GF1001 Sickness and disability | % of GDP | 2015 | **2.7** | 2.7 | 2.6 / 2.6 | 2.4 / 2.2 | 10/27 | 2.2 / 2.1 | 7/21 | 3.4 / 3.2 | 6/8 | 0.1 | [gov_10a_exp] |
| COFOG GF1001 Sickness and disability | % of GDP | 2024 | **2.9** (p) | 2.8 | 2.8 / 2.8 | 2.4 / 2.2 | 10/27 | 2.4 / 2.6 | 8/21 | 3.5 / 3.5 | 6/8 | 0.1 | [gov_10a_exp] |
| COFOG GF1002 Old age | % of GDP | 2005 | **11.4** | n/a | n/a / n/a | 7.9 / 7.3 | 3/26 | 7.9 / 7.5 | 3/20 | 8.0 / 7.1 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF1002 Old age | % of GDP | 2015 | **13.5** | 10.5 | 10.7 / 10.7 | 9.2 / 8.8 | 3/27 | 9.5 / 8.9 | 3/21 | 9.4 / 9.1 | 2/8 | 2.8 | [gov_10a_exp] |
| COFOG GF1002 Old age | % of GDP | 2024 | **13.4** (p) | 10.6 | 10.8 / 10.9 | 9.5 / 9.8 | 4/27 | 9.7 / 9.9 | 4/21 | 9.8 / 10.2 | 2/8 | 2.6 | [gov_10a_exp] |
| COFOG GF1003 Survivors | % of GDP | 2005 | **1.5** | n/a | n/a / n/a | 1.0 / 1.1 | 9/26 | 1.1 / 1.2 | 8/20 | 1.3 / 1.9 | 5/8 | n/a | [gov_10a_exp] |
| COFOG GF1003 Survivors | % of GDP | 2015 | **1.6** | 1.6 | 1.7 / 1.7 | 1.1 / 1.1 | 8/27 | 1.2 / 1.4 | 7/21 | 1.3 / 1.8 | 5/8 | -0.1 | [gov_10a_exp] |
| COFOG GF1003 Survivors | % of GDP | 2024 | **1.4** (p) | 1.4 | 1.6 / 1.6 | 1.0 / 0.9 | 7/27 | 1.1 / 1.2 | 6/21 | 1.1 / 1.4 | 4/8 | -0.2 | [gov_10a_exp] |
| COFOG GF1004 Family and children | % of GDP | 2005 | **2.4** | n/a | n/a / n/a | 1.8 / 1.5 | 6/26 | 1.6 / 1.5 | 4/20 | 2.0 / 1.4 | 3/8 | n/a | [gov_10a_exp] |
| COFOG GF1004 Family and children | % of GDP | 2015 | **2.5** | 1.8 | 1.7 / 1.7 | 1.9 / 2.0 | 5/27 | 1.9 / 2.0 | 4/21 | 2.1 / 1.9 | 2/8 | 0.8 | [gov_10a_exp] |
| COFOG GF1004 Family and children | % of GDP | 2024 | **2.3** (p) | 2.0 | 1.9 / 1.9 | 2.1 / 1.8 | 8/27 | 2.0 / 1.8 | 6/21 | 2.2 / 2.2 | 3/8 | 0.4 | [gov_10a_exp] |
| COFOG GF1005 Unemployment | % of GDP | 2005 | **1.9** | n/a | n/a / n/a | 1.2 / 0.8 | 6/26 | 1.1 / 0.8 | 4/20 | 2.1 / 2.0 | 5/8 | n/a | [gov_10a_exp] |
| COFOG GF1005 Unemployment | % of GDP | 2015 | **1.9** | 1.5 | 1.6 / 1.6 | 1.1 / 0.9 | 5/27 | 1.1 / 1.0 | 4/21 | 1.8 / 1.6 | 4/8 | 0.3 | [gov_10a_exp] |
| COFOG GF1005 Unemployment | % of GDP | 2024 | **1.7** (p) | 1.2 | 1.3 / 1.3 | 0.8 / 0.7 | 1/27 | 0.8 / 0.7 | 1/21 | 1.2 / 1.1 | 1/8 | 0.4 | [gov_10a_exp] |
| COFOG GF1006 Housing (social) | % of GDP | 2005 | **1.0** | n/a | n/a / n/a | 0.3 / 0.1 | 1/26 | 0.2 / 0.1 | 1/20 | 0.3 / 0.3 | 1/8 | n/a | [gov_10a_exp] |
| COFOG GF1006 Housing (social) | % of GDP | 2015 | **0.9** | 0.3 | 0.4 / 0.4 | 0.2 / 0.1 | 1/27 | 0.2 / 0.1 | 1/21 | 0.3 / 0.3 | 1/8 | 0.5 | [gov_10a_exp] |
| COFOG GF1006 Housing (social) | % of GDP | 2024 | **0.7** (p) | 0.3 | 0.4 / 0.4 | 0.2 / 0.1 | 2/27 | 0.2 / 0.1 | 2/21 | 0.3 / 0.3 | 1/8 | 0.3 | [gov_10a_exp] |
| COFOG GF1007 Social exclusion n.e.c. | % of GDP | 2005 | **0.8** | n/a | n/a / n/a | 0.6 / 0.4 | 6/26 | 0.5 / 0.3 | 3/20 | 0.8 / 0.8 | 4/8 | n/a | [gov_10a_exp] |
| COFOG GF1007 Social exclusion n.e.c. | % of GDP | 2015 | **1.0** | 0.8 | 0.8 / 0.8 | 0.7 / 0.5 | 5/27 | 0.6 / 0.5 | 3/21 | 1.2 / 1.0 | 4/8 | 0.2 | [gov_10a_exp] |
| COFOG GF1007 Social exclusion n.e.c. | % of GDP | 2024 | **1.2** (p) | 0.9 | 0.9 / 0.9 | 0.7 / 0.5 | 3/27 | 0.7 / 0.5 | 3/21 | 1.1 / 0.8 | 2/8 | 0.3 | [gov_10a_exp] |
| COFOG GF0701 Health: medical products | % of GDP | 2005 | **1.3** | n/a | n/a / n/a | 1.0 / 0.9 | 6/26 | 1.0 / 1.0 | 5/20 | 1.0 / 0.9 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF0701 Health: medical products | % of GDP | 2015 | **1.5** | 1.2 | 1.2 / 1.2 | 0.9 / 0.8 | 3/27 | 0.9 / 0.8 | 3/21 | 0.9 / 0.8 | 2/8 | 0.3 | [gov_10a_exp] |
| COFOG GF0701 Health: medical products | % of GDP | 2024 | **1.5** (p) | 1.1 | 1.2 / 1.2 | 0.9 / 0.8 | 3/27 | 1.0 / 0.9 | 3/21 | 0.9 / 0.8 | 2/8 | 0.3 | [gov_10a_exp] |
| COFOG GF0702 Health: outpatient services | % of GDP | 2005 | **2.7** | n/a | n/a / n/a | 1.5 / 1.4 | 3/26 | 1.5 / 1.4 | 2/20 | 2.0 / 2.0 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF0702 Health: outpatient services | % of GDP | 2015 | **2.9** | 2.2 | 2.3 / 2.3 | 1.6 / 1.5 | 3/27 | 1.6 / 1.5 | 2/21 | 2.3 / 2.3 | 2/8 | 0.6 | [gov_10a_exp] |
| COFOG GF0702 Health: outpatient services | % of GDP | 2024 | **3.1** (p) | 2.3 | 2.4 / 2.4 | 1.8 / 1.7 | 3/27 | 1.8 / 1.7 | 2/21 | 2.4 / 2.3 | 2/8 | 0.7 | [gov_10a_exp] |
| COFOG GF0703 Health: hospital services | % of GDP | 2005 | **3.4** | n/a | n/a / n/a | 3.0 / 2.8 | 6/26 | 3.0 / 2.9 | 5/20 | 3.0 / 2.6 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF0703 Health: hospital services | % of GDP | 2015 | **3.4** | 3.1 | 3.1 / 3.1 | 3.1 / 3.0 | 9/27 | 3.1 / 3.1 | 8/21 | 3.5 / 2.9 | 4/8 | 0.3 | [gov_10a_exp] |
| COFOG GF0703 Health: hospital services | % of GDP | 2024 | **3.7** (p) | 3.3 | 3.2 / 3.2 | 3.5 / 3.4 | 9/27 | 3.5 / 3.4 | 6/21 | 3.4 / 2.9 | 3/8 | 0.5 | [gov_10a_exp] |
| COFOG GF0704 Health: public health services | % of GDP | 2005 | **0.2** | n/a | n/a / n/a | 0.2 / 0.1 | 6/26 | 0.1 / 0.1 | 4/20 | 0.1 / 0.1 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF0704 Health: public health services | % of GDP | 2015 | **0.2** | 0.2 | 0.1 / 0.1 | 0.2 / 0.1 | 5/27 | 0.1 / 0.1 | 4/21 | 0.2 / 0.1 | 2/8 | 0.1 | [gov_10a_exp] |
| COFOG GF0704 Health: public health services | % of GDP | 2024 | **0.3** (p) | 0.2 | 0.2 / 0.2 | 0.2 / 0.1 | 5/27 | 0.2 / 0.1 | 4/21 | 0.2 / 0.2 | 1/8 | 0.1 | [gov_10a_exp] |
| COFOG GF0705 Health: R&D | % of GDP | 2005 | **0.2** | n/a | n/a / n/a | 0.1 / 0.1 | 3/25 | 0.1 / 0.1 | 3/19 | 0.2 / 0.2 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF0705 Health: R&D | % of GDP | 2015 | **0.2** | 0.1 | 0.2 / 0.2 | 0.1 / 0.1 | 3/26 | 0.1 / 0.1 | 3/20 | 0.2 / 0.2 | 2/8 | 0.0 | [gov_10a_exp] |
| COFOG GF0705 Health: R&D | % of GDP | 2024 | **0.2** (p) | 0.2 | 0.2 / 0.2 | 0.1 / 0.1 | 4/26 | 0.1 / 0.1 | 4/20 | 0.2 / 0.2 | 3/8 | 0.0 | [gov_10a_exp] |
| COFOG GF0706 Health n.e.c. | % of GDP | 2005 | **0.1** | n/a | n/a / n/a | 0.2 / 0.2 | 15/26 | 0.2 / 0.1 | 11/20 | 0.2 / 0.1 | 3/8 | n/a | [gov_10a_exp] |
| COFOG GF0706 Health n.e.c. | % of GDP | 2015 | **0.0** | 0.2 | 0.2 / 0.2 | 0.2 / 0.2 | 23/27 | 0.2 / 0.2 | 17/21 | 0.2 / 0.2 | 7/8 | -0.2 | [gov_10a_exp] |
| COFOG GF0706 Health n.e.c. | % of GDP | 2024 | **0.1** (p) | 0.2 | 0.2 / 0.2 | 0.2 / 0.2 | 17/27 | 0.2 / 0.2 | 12/21 | 0.2 / 0.2 | 6/8 | -0.1 | [gov_10a_exp] |
| COFOG GF0901 Education: pre-primary and primary | % of GDP | 2005 | **1.4** | n/a | n/a / n/a | 1.7 / 1.6 | 17/26 | 1.6 / 1.5 | 13/20 | 2.1 / 1.6 | 7/8 | n/a | [gov_10a_exp] |
| COFOG GF0901 Education: pre-primary and primary | % of GDP | 2015 | **1.4** | 1.6 | 1.4 / 1.4 | 1.6 / 1.4 | 14/27 | 1.5 / 1.4 | 11/21 | 2.2 / 1.6 | 6/8 | 0.0 | [gov_10a_exp] |
| COFOG GF0901 Education: pre-primary and primary | % of GDP | 2024 | **1.4** (p) | 1.6 | 1.5 / 1.5 | 1.8 / 1.5 | 18/27 | 1.6 / 1.5 | 15/21 | 2.2 / 1.6 | 7/8 | -0.1 | [gov_10a_exp] |
| COFOG GF0902 Education: secondary | % of GDP | 2005 | **2.5** | n/a | n/a / n/a | 1.9 / 1.9 | 2/26 | 2.0 / 2.0 | 2/20 | 1.8 / 1.8 | 1/8 | n/a | [gov_10a_exp] |
| COFOG GF0902 Education: secondary | % of GDP | 2015 | **2.4** | 1.8 | 1.8 / 1.8 | 1.7 / 1.8 | 3/27 | 1.8 / 1.8 | 3/21 | 1.8 / 1.8 | 2/8 | 0.6 | [gov_10a_exp] |
| COFOG GF0902 Education: secondary | % of GDP | 2024 | **2.2** (p) | 1.7 | 1.8 / 1.8 | 1.7 / 1.7 | 4/27 | 1.8 / 1.8 | 4/21 | 1.7 / 1.6 | 2/8 | 0.4 | [gov_10a_exp] |
| COFOG GF0904 Education: tertiary | % of GDP | 2005 | **0.5** | n/a | n/a / n/a | 1.0 / 0.8 | 24/26 | 0.9 / 0.8 | 18/20 | 0.9 / 0.8 | 7/8 | n/a | [gov_10a_exp] |
| COFOG GF0904 Education: tertiary | % of GDP | 2015 | **0.5** | 0.8 | 0.7 / 0.7 | 1.0 / 0.9 | 25/27 | 0.9 / 0.9 | 19/21 | 1.0 / 0.9 | 7/8 | -0.2 | [gov_10a_exp] |
| COFOG GF0904 Education: tertiary | % of GDP | 2024 | **0.4** (p) | 0.8 | 0.7 / 0.7 | 0.9 / 0.8 | 25/27 | 0.9 / 0.8 | 19/21 | 1.0 / 1.0 | 7/8 | -0.3 | [gov_10a_exp] |

#### COFOG as % of total general government expenditure

| Indicator | Unit | Year | France | EU-27 agg. | EA agg. (EA21 / EA20) | EU-27 MS mean / median | FR rank EU-27 | EA21 MS mean / median | FR rank EA21 | Panel mean / median | FR rank panel (of 8) | FR - EA agg. (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| COFOG GF01 General public services | % of total GG expenditure | 2005 | **13.7** | n/a | n/a / n/a | 14.3 / 13.3 | 12/26 | 14.5 / 13.8 | 11/20 | 14.8 / 13.4 | 4/8 | n/a | [gov_10a_exp] |
| COFOG GF01 General public services | % of total GG expenditure | 2015 | **11.5** | 13.4 | 13.5 / 13.6 | 13.8 / 13.1 | 22/27 | 14.1 / 13.6 | 18/21 | 13.5 / 13.1 | 6/8 | -2.0 | [gov_10a_exp] |
| COFOG GF01 General public services | % of total GG expenditure | 2024 | **10.8** (p) | 12.4 | 12.4 / 12.5 | 12.0 / 11.5 | 19/27 | 11.7 / 11.5 | 14/21 | 12.4 / 12.8 | 7/8 | -1.6 | [gov_10a_exp] |
| COFOG GF02 Defense | % of total GG expenditure | 2005 | **3.3** | n/a | n/a / n/a | 3.2 / 2.8 | 9/26 | 3.0 / 2.8 | 6/20 | 2.6 / 2.7 | 1/8 | n/a | [gov_10a_exp] |
| COFOG GF02 Defense | % of total GG expenditure | 2015 | **3.0** | 2.4 | 2.4 / 2.4 | 2.4 / 2.4 | 7/27 | 2.4 / 2.4 | 6/21 | 2.1 / 2.2 | 1/8 | 0.6 | [gov_10a_exp] |
| COFOG GF02 Defense | % of total GG expenditure | 2024 | **3.2** (p) | 3.0 | 2.8 / 2.8 | 3.5 / 3.1 | 13/27 | 3.3 / 2.9 | 8/21 | 3.0 / 2.7 | 4/8 | 0.4 | [gov_10a_exp] |
| COFOG GF03 Public order and safety | % of total GG expenditure | 2005 | **2.8** | n/a | n/a / n/a | 4.1 / 4.0 | 21/26 | 4.2 / 4.0 | 17/20 | 3.4 / 3.3 | 6/8 | n/a | [gov_10a_exp] |
| COFOG GF03 Public order and safety | % of total GG expenditure | 2015 | **2.8** | 3.5 | 3.4 / 3.4 | 3.9 / 3.8 | 22/27 | 3.9 / 3.8 | 18/21 | 3.3 / 3.4 | 6/8 | -0.6 | [gov_10a_exp] |
| COFOG GF03 Public order and safety | % of total GG expenditure | 2024 | **3.1** (p) | 3.5 | 3.5 / 3.4 | 4.0 / 3.9 | 23/27 | 4.0 / 3.9 | 18/21 | 3.4 / 3.3 | 7/8 | -0.4 | [gov_10a_exp] |
| COFOG GF04 Economic affairs | % of total GG expenditure | 2005 | **9.5** | n/a | n/a / n/a | 11.7 / 11.2 | 19/26 | 11.8 / 11.6 | 16/20 | 10.3 / 9.5 | 4/8 | n/a | [gov_10a_exp] |
| COFOG GF04 Economic affairs | % of total GG expenditure | 2015 | **10.8** | 10.5 | 10.4 / 10.4 | 12.2 / 11.9 | 17/27 | 11.9 / 11.6 | 13/21 | 9.7 / 9.7 | 2/8 | 0.4 | [gov_10a_exp] |
| COFOG GF04 Economic affairs | % of total GG expenditure | 2024 | **9.9** (p) | 10.8 | 10.6 / 10.6 | 11.6 / 11.5 | 19/27 | 11.5 / 11.2 | 15/21 | 10.0 / 10.1 | 5/8 | -0.7 | [gov_10a_exp] |
| COFOG GF05 Environmental protection | % of total GG expenditure | 2005 | **1.5** | n/a | n/a / n/a | 1.8 / 1.6 | 16/26 | 1.9 / 1.8 | 15/20 | 1.8 / 1.6 | 5/8 | n/a | [gov_10a_exp] |
| COFOG GF05 Environmental protection | % of total GG expenditure | 2015 | **1.6** | 1.6 | 1.7 / 1.7 | 1.9 / 1.8 | 19/27 | 1.9 / 1.8 | 16/21 | 1.7 / 1.9 | 5/8 | -0.1 | [gov_10a_exp] |
| COFOG GF05 Environmental protection | % of total GG expenditure | 2024 | **1.8** (p) | 1.7 | 1.7 / 1.7 | 1.7 / 1.6 | 11/27 | 1.8 / 1.6 | 9/21 | 1.8 / 1.8 | 4/8 | 0.1 | [gov_10a_exp] |
| COFOG GF06 Housing and community amenities | % of total GG expenditure | 2005 | **2.1** | n/a | n/a / n/a | 1.9 / 1.6 | 9/26 | 1.8 / 1.4 | 6/20 | 1.3 / 1.2 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF06 Housing and community amenities | % of total GG expenditure | 2015 | **2.1** | 1.3 | 1.2 / 1.2 | 1.7 / 1.2 | 6/27 | 1.6 / 1.2 | 5/21 | 0.9 / 0.9 | 1/8 | 0.9 | [gov_10a_exp] |
| COFOG GF06 Housing and community amenities | % of total GG expenditure | 2024 | **2.5** (p) | 1.5 | 1.5 / 1.5 | 1.7 / 1.4 | 6/27 | 1.7 / 1.4 | 5/21 | 1.1 / 1.1 | 1/8 | 1.0 | [gov_10a_exp] |
| COFOG GF07 Health | % of total GG expenditure | 2005 | **14.4** | n/a | n/a / n/a | 13.3 / 13.7 | 8/26 | 13.6 / 13.8 | 6/20 | 13.6 / 13.7 | 3/8 | n/a | [gov_10a_exp] |
| COFOG GF07 Health | % of total GG expenditure | 2015 | **14.3** | 14.6 | 14.7 / 14.7 | 13.4 / 13.9 | 8/27 | 13.4 / 13.9 | 6/21 | 15.1 / 14.5 | 5/8 | -0.4 | [gov_10a_exp] |
| COFOG GF07 Health | % of total GG expenditure | 2024 | **15.6** (p) | 15.0 | 15.1 / 15.1 | 15.0 / 14.6 | 10/27 | 15.1 / 14.6 | 8/21 | 15.2 / 14.8 | 3/8 | 0.5 | [gov_10a_exp] |
| COFOG GF08 Recreation, culture and religion | % of total GG expenditure | 2005 | **2.7** | n/a | n/a / n/a | 2.8 / 2.6 | 11/26 | 2.8 / 2.6 | 8/20 | 2.7 / 2.7 | 4/8 | n/a | [gov_10a_exp] |
| COFOG GF08 Recreation, culture and religion | % of total GG expenditure | 2015 | **2.6** | 2.4 | 2.3 / 2.3 | 2.8 / 2.7 | 17/27 | 2.7 / 2.6 | 11/21 | 2.5 / 2.6 | 4/8 | 0.3 | [gov_10a_exp] |
| COFOG GF08 Recreation, culture and religion | % of total GG expenditure | 2024 | **2.6** (p) | 2.4 | 2.3 / 2.3 | 2.7 / 2.7 | 15/27 | 2.6 / 2.6 | 10/21 | 2.5 / 2.6 | 4/8 | 0.3 | [gov_10a_exp] |
| COFOG GF09 Education | % of total GG expenditure | 2005 | **10.1** | n/a | n/a / n/a | 12.2 / 12.0 | 22/26 | 12.2 / 11.8 | 16/20 | 11.1 / 11.0 | 6/8 | n/a | [gov_10a_exp] |
| COFOG GF09 Education | % of total GG expenditure | 2015 | **9.1** | 9.8 | 9.4 / 9.4 | 11.1 / 11.1 | 24/27 | 11.0 / 11.1 | 19/21 | 11.0 / 11.5 | 7/8 | -0.3 | [gov_10a_exp] |
| COFOG GF09 Education | % of total GG expenditure | 2024 | **8.9** (p) | 9.7 | 9.4 / 9.4 | 11.1 / 10.8 | 25/27 | 11.0 / 10.8 | 19/21 | 10.8 / 11.5 | 7/8 | -0.5 | [gov_10a_exp] |
| COFOG GF10 Social protection | % of total GG expenditure | 2005 | **39.9** | n/a | n/a / n/a | 34.7 / 33.4 | 5/26 | 34.2 / 33.0 | 3/20 | 38.4 / 36.4 | 4/8 | n/a | [gov_10a_exp] |
| COFOG GF10 Social protection | % of total GG expenditure | 2015 | **42.2** | 40.6 | 40.9 / 41.0 | 36.8 / 37.2 | 4/27 | 37.1 / 37.2 | 3/21 | 40.2 / 41.3 | 2/8 | 1.3 | [gov_10a_exp] |
| COFOG GF10 Social protection | % of total GG expenditure | 2024 | **41.5** (p) | 40.0 | 40.7 / 40.7 | 36.6 / 37.2 | 4/27 | 37.3 / 37.3 | 4/21 | 39.9 / 41.0 | 2/8 | 0.8 | [gov_10a_exp] |
| COFOG GF0107 Public debt transactions (interest) | % of total GG expenditure | 2005 | **5.2** | n/a | n/a / n/a | 5.1 / 4.5 | 12/26 | 5.2 / 5.0 | 10/20 | 6.1 / 5.4 | 5/8 | n/a | [gov_10a_exp] |
| COFOG GF0107 Public debt transactions (interest) | % of total GG expenditure | 2015 | **3.9** | 4.9 | 5.1 / 5.1 | 4.9 / 4.3 | 17/27 | 5.3 / 5.0 | 14/21 | 4.6 / 3.4 | 4/8 | -1.2 | [gov_10a_exp] |
| COFOG GF0107 Public debt transactions (interest) | % of total GG expenditure | 2024 | **3.5** (p) | 3.9 | 3.9 / 3.9 | 3.7 / 3.2 | 10/27 | 3.4 / 3.0 | 7/21 | 3.6 / 2.3 | 4/8 | -0.4 | [gov_10a_exp] |
| COFOG GF1002 Old age | % of total GG expenditure | 2005 | **21.0** | n/a | n/a / n/a | 17.8 / 16.9 | 8/26 | 18.0 / 16.9 | 6/20 | 17.0 / 15.7 | 2/8 | n/a | [gov_10a_exp] |
| COFOG GF1002 Old age | % of total GG expenditure | 2015 | **23.5** | 21.7 | 22.1 / 22.1 | 20.1 / 20.4 | 7/27 | 20.5 / 20.4 | 6/21 | 19.3 / 20.4 | 2/8 | 1.4 | [gov_10a_exp] |
| COFOG GF1002 Old age | % of total GG expenditure | 2024 | **23.4** (p) | 21.8 | 22.1 / 22.1 | 20.5 / 20.2 | 7/27 | 20.8 / 20.2 | 7/21 | 20.0 / 20.0 | 2/8 | 1.3 | [gov_10a_exp] |

#### Social protection (ESSPROS)

| Indicator | Unit | Year | France | EU-27 agg. | EA agg. (EA21 / EA20) | EU-27 MS mean / median | FR rank EU-27 | EA21 MS mean / median | FR rank EA21 | Panel mean / median | FR rank panel (of 8) | FR - EA agg. (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Social protection expenditure, total (ESSPROS, incl. admin) | % of GDP | 2005 | **31.2** | n/a | n/a / n/a | 21.2 / 21.1 | 1/26 | 21.1 / 21.3 | 1/20 | 26.4 / 26.9 | 1/8 | n/a | [spr_exp_type] |
| Social protection expenditure, total (ESSPROS, incl. admin) | % of GDP | 2015 | **34.0** | 28.3 | 29.0 / 29.0 | 23.1 / 21.4 | 1/27 | 23.3 / 24.0 | 1/21 | 29.3 / 29.2 | 1/8 | 5.0 | [spr_exp_type] |
| Social protection expenditure, total (ESSPROS, incl. admin) | % of GDP | 2024 | **34.4** (p) | 28.6 | 29.4 / 29.4 | 23.7 / 23.2 | 1/27 | 23.9 / 23.2 | 1/21 | 28.8 / 29.1 | 1/8 | 5.0 | [spr_exp_type] |
| Social protection benefits (ESSPROS) | % of GDP | 2005 | **29.2** | n/a | n/a / n/a | 20.5 / 20.6 | 1/26 | 20.3 / 20.8 | 1/20 | 25.4 / 25.7 | 1/8 | n/a | [spr_exp_type] |
| Social protection benefits (ESSPROS) | % of GDP | 2015 | **32.1** | 27.2 | 27.7 / 27.8 | 22.4 / 21.0 | 2/27 | 22.6 / 23.6 | 1/21 | 28.1 / 28.4 | 2/8 | 4.4 | [spr_exp_type] |
| Social protection benefits (ESSPROS) | % of GDP | 2024 | **32.0** (p) | 27.4 | 28.1 / 28.2 | 23.0 / 22.9 | 2/27 | 23.2 / 22.9 | 2/21 | 27.7 / 27.9 | 1/8 | 3.9 | [spr_exp_type] |
| Social protection benefits, all functions (ESSPROS, incl. 2025 early estimates) | % of GDP | 2005 | **29.2** | n/a | n/a / n/a | 20.5 / 20.6 | 1/26 | 20.3 / 20.8 | 1/20 | 25.4 / 25.7 | 1/8 | n/a | [spr_exp_func] |
| Social protection benefits, all functions (ESSPROS, incl. 2025 early estimates) | % of GDP | 2015 | **32.1** | 27.2 | 27.7 / 27.8 | 22.4 / 21.0 | 2/27 | 22.6 / 23.6 | 1/21 | 28.1 / 28.4 | 2/8 | 4.4 | [spr_exp_func] |
| Social protection benefits, all functions (ESSPROS, incl. 2025 early estimates) | % of GDP | 2025 | **32.1** (e) | 27.5 | 28.3 / 28.3 | 23.1 / 23.1 | 3/27 | 23.4 / 23.1 | 3/21 | 27.8 / 27.9 | 1/8 | 3.9 | [spr_exp_func] |
| Social benefits: old age function (ESSPROS, incl. 2025 early estimates) | % of GDP | 2005 | **10.9** | n/a | n/a / n/a | 8.0 / 8.0 | 3/26 | 7.8 / 7.8 | 3/20 | 9.6 / 10.2 | 2/8 | n/a | [spr_exp_func] |
| Social benefits: old age function (ESSPROS, incl. 2025 early estimates) | % of GDP | 2015 | **13.0** | 11.1 | 11.2 / 11.3 | 9.6 / 9.6 | 3/27 | 9.5 / 9.6 | 3/21 | 11.3 / 10.8 | 2/8 | 1.7 | [spr_exp_func] |
| Social benefits: old age function (ESSPROS, incl. 2025 early estimates) | % of GDP | 2025 | **13.2** (e) | 11.4 | 11.6 / 11.6 | 9.8 / 9.9 | 4/27 | 9.8 / 9.9 | 4/21 | 11.6 / 10.9 | 2/8 | 1.6 | [spr_exp_func] |
| Social benefits: sickness/health care function (ESSPROS, incl. 2025 early estimates) | % of GDP | 2005 | **8.5** | n/a | n/a / n/a | 5.8 / 6.0 | 1/26 | 5.9 / 6.2 | 1/20 | 6.9 / 7.2 | 1/8 | n/a | [spr_exp_func] |
| Social benefits: sickness/health care function (ESSPROS, incl. 2025 early estimates) | % of GDP | 2015 | **8.9** | 7.7 | 8.0 / 8.0 | 6.1 / 5.8 | 3/27 | 6.2 / 6.0 | 3/21 | 7.6 / 7.4 | 3/8 | 1.0 | [spr_exp_func] |
| Social benefits: sickness/health care function (ESSPROS, incl. 2025 early estimates) | % of GDP | 2025 | **9.7** (e) | 8.2 | 8.6 / 8.6 | 6.8 / 6.7 | 3/27 | 7.0 / 6.7 | 3/21 | 7.9 / 7.5 | 3/8 | 1.1 | [spr_exp_func] |
| Social protection expenditure, total (ESSPROS) | PPS per inhabitant | 2005 | **7,912** | n/a | n/a / n/a | 4,839 / 4,288 | 5/26 | 5,010 / 4,438 | 4/20 | 7,025 / 7,589 | 3/8 | n/a | [spr_exp_type] |
| Social protection expenditure, total (ESSPROS) | PPS per inhabitant | 2015 | **10,169** | 7,860 | n/a / 8,554 | 6,497 / 5,270 | 6/27 | 6,628 / 5,316 | 5/21 | 9,296 / 9,813 | 4/8 | 1,615 | [spr_exp_type] |
| Social protection expenditure, total (ESSPROS) | PPS per inhabitant | 2024 | **13,557** (p) | 11,431 | n/a / 12,201 | 9,484 / 8,054 | 6/27 | 9,711 / 8,315 | 5/21 | 12,644 / 13,330 | 4/8 | 1,357 | [spr_exp_type] |
| Social protection benefits, all functions (ESSPROS) | PPS per inhabitant | 2005 | **7,399** | n/a | n/a / n/a | 4,667 / 4,125 | 6/26 | 4,817 / 4,336 | 4/20 | 6,743 / 7,292 | 4/8 | n/a | [spr_exp_func] |
| Social protection benefits, all functions (ESSPROS) | PPS per inhabitant | 2015 | **9,608** | 7,538 | n/a / 8,187 | 6,291 / 5,112 | 6/27 | 6,412 / 5,180 | 4/21 | 8,911 / 9,578 | 4/8 | 1,421 | [spr_exp_func] |
| Social protection benefits, all functions (ESSPROS) | PPS per inhabitant | 2025 | **13,083** (e) | 11,477 | 12,100 / 12,187 | 9,646 / 8,721 | 7/27 | 9,881 / 8,830 | 6/21 | 12,707 / 13,193 | 5/8 | 983.4 | [spr_exp_func] |
| Social benefits: old age function (ESSPROS) | PPS per inhabitant | 2005 | **2,755** | n/a | n/a / n/a | 1,745 / 1,550 | 7/26 | 1,790 / 1,715 | 5/20 | 2,540 / 2,815 | 5/8 | n/a | [spr_exp_func] |
| Social benefits: old age function (ESSPROS) | PPS per inhabitant | 2015 | **3,881** | 3,086 | n/a / 3,319 | 2,592 / 2,170 | 5/27 | 2,608 / 2,350 | 3/21 | 3,558 / 3,558 | 3/8 | 561.8 | [spr_exp_func] |
| Social benefits: old age function (ESSPROS) | PPS per inhabitant | 2025 | **5,370** (e) | 4,764 | 4,962 / 4,996 | 4,030 / 3,490 | 9/27 | 4,062 / 3,490 | 7/21 | 5,268 / 5,406 | 6/8 | 407.8 | [spr_exp_func] |
| Social benefits: sickness/health care function (ESSPROS) | PPS per inhabitant | 2005 | **2,150** | n/a | n/a / n/a | 1,311 / 1,282 | 3/26 | 1,385 / 1,381 | 3/20 | 1,823 / 1,938 | 2/8 | n/a | [spr_exp_func] |
| Social benefits: sickness/health care function (ESSPROS) | PPS per inhabitant | 2015 | **2,678** | 2,137 | n/a / 2,357 | 1,715 / 1,502 | 4/27 | 1,785 / 1,610 | 4/21 | 2,442 / 2,495 | 3/8 | 320.8 | [spr_exp_func] |
| Social benefits: sickness/health care function (ESSPROS) | PPS per inhabitant | 2025 | **3,929** (e) | 3,445 | 3,680 / 3,709 | 2,877 / 2,662 | 6/27 | 3,009 / 2,774 | 6/21 | 3,670 / 3,303 | 3/8 | 249.1 | [spr_exp_func] |

#### Per capita in PPS

| Indicator | Unit | Year | France | EU-27 agg. | EA agg. (EA21 / EA20) | EU-27 MS mean / median | FR rank EU-27 | EA21 MS mean / median | FR rank EA21 | Panel mean / median | FR rank panel (of 8) | FR - EA agg. (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Total GG expenditure per capita (TE % GDP x GDP per capita PPS) | PPS per inhabitant (derived) | 2005 | **13,582** | 10,434 | 11,474 / 11,649 | 9,614 / 9,058 | 6/27 | 9,922 / 9,438 | 4/21 | 12,775 / 13,430 | 4/8 | 2,108 | [gov_10a_main x nama_10_pc] |
| Total GG expenditure per capita (TE % GDP x GDP per capita PPS) | PPS per inhabitant (derived) | 2015 | **17,001** | 13,432 | 14,303 / 14,460 | 12,644 / 10,530 | 6/27 | 12,900 / 11,078 | 4/21 | 15,919 / 16,561 | 4/8 | 2,698 | [gov_10a_main x nama_10_pc] |
| Total GG expenditure per capita (TE % GDP x GDP per capita PPS) | PPS per inhabitant (derived) | 2025 | **23,330** | 20,636 | 21,424 / 21,601 | 19,863 / 17,234 | 8/27 | 20,228 / 17,287 | 7/21 | 23,036 / 24,360 | 5/8 | 1,906 | [gov_10a_main x nama_10_pc] |
| Government final consumption expenditure per capita | PPS per inhabitant | 2005 | **5,820** | 4,503 | 4,905 / 4,981 | 4,234 / 3,894 | 6/27 | 4,301 / 3,902 | 4/21 | 5,799 / 6,004 | 5/8 | 915.2 | [nama_10_pc] |
| Government final consumption expenditure per capita | PPS per inhabitant | 2015 | **7,104** | 5,799 | 6,117 / 6,190 | 5,478 / 4,655 | 8/27 | 5,509 / 4,669 | 6/21 | 7,422 / 7,842 | 5/8 | 987.7 | [nama_10_pc] |
| Government final consumption expenditure per capita | PPS per inhabitant | 2025 | **9,796** (p) | 8,998 | 9,261 / 9,320 | 8,928 / 7,703 | 10/27 | 9,014 / 7,854 | 8/21 | 10,817 / 11,455 | 6/8 | 534.7 | [nama_10_pc] |
| GDP per capita | PPS (EU27_2020) per inhabitant | 2005 | **25,013** | 22,106 | 24,309 / 24,681 | 21,453 / 20,481 | 10/27 | 22,467 / 22,627 | 8/21 | 26,906 / 27,177 | 6/8 | 703.8 | [nama_10_pc] |
| GDP per capita | PPS (EU27_2020) per inhabitant | 2015 | **29,516** | 27,810 | 29,430 / 29,753 | 27,993 / 24,604 | 10/27 | 28,889 / 25,351 | 8/21 | 32,476 / 35,062 | 6/8 | 86.4 | [nama_10_pc] |
| GDP per capita | PPS (EU27_2020) per inhabitant | 2025 | **40,716** (p) | 41,774 | 43,107 / 43,375 | 43,569 / 38,557 | 12/27 | 44,728 / 40,075 | 10/21 | 47,128 / 47,598 | 6/8 | -2,391 | [nama_10_pc] |
| COFOG GF01 per capita (derived) | PPS per inhabitant (derived) | 2005 | **1,851** | n/a | n/a / n/a | 1,416 / 1,295 | 9/26 | 1,498 / 1,482 | 8/20 | 1,881 / 1,851 | 5/8 | n/a | [gov_10a_exp x nama_10_pc] |
| COFOG GF01 per capita (derived) | PPS per inhabitant (derived) | 2015 | **1,948** | 1,808 | 1,942 / 1,964 | 1,722 / 1,759 | 11/27 | 1,781 / 1,848 | 9/21 | 2,118 / 2,039 | 6/8 | 5.7 | [gov_10a_exp x nama_10_pc] |
| COFOG GF01 per capita (derived) | PPS per inhabitant (derived) | 2024 | **2,436** (p) | 2,412 | 2,540 / 2,557 | 2,261 / 2,179 | 9/27 | 2,262 / 2,179 | 7/21 | 2,714 / 2,952 | 5/8 | -104.1 | [gov_10a_exp x nama_10_pc] |
| COFOG GF02 per capita (derived) | PPS per inhabitant (derived) | 2005 | **450.2** | n/a | n/a / n/a | 265.1 / 245.4 | 2/26 | 264.6 / 245.4 | 2/20 | 327.5 / 320.9 | 1/8 | n/a | [gov_10a_exp x nama_10_pc] |
| COFOG GF02 per capita (derived) | PPS per inhabitant (derived) | 2015 | **501.8** | 333.7 | 353.2 / 357.0 | 280.5 / 253.5 | 1/27 | 284.6 / 253.5 | 1/21 | 338.2 / 322.0 | 1/8 | 148.6 | [gov_10a_exp x nama_10_pc] |
| COFOG GF02 per capita (derived) | PPS per inhabitant (derived) | 2024 | **746.6** (p) | 602.9 | 583.0 / 586.9 | 599.8 / 609.0 | 8/27 | 567.9 / 605.1 | 5/21 | 676.4 / 658.1 | 4/8 | 163.6 | [gov_10a_exp x nama_10_pc] |
| COFOG GF07 per capita (derived) | PPS per inhabitant (derived) | 2005 | **1,951** | n/a | n/a / n/a | 1,319 / 1,290 | 5/26 | 1,378 / 1,325 | 4/20 | 1,728 / 1,718 | 2/8 | n/a | [gov_10a_exp x nama_10_pc] |
| COFOG GF07 per capita (derived) | PPS per inhabitant (derived) | 2015 | **2,420** | 1,947 | 2,090 / 2,112 | 1,739 / 1,510 | 9/27 | 1,761 / 1,510 | 7/21 | 2,405 / 2,460 | 6/8 | 330.8 | [gov_10a_exp x nama_10_pc] |
| COFOG GF07 per capita (derived) | PPS per inhabitant (derived) | 2024 | **3,497** (p) | 2,934 | 3,082 / 3,102 | 2,839 / 2,589 | 8/27 | 2,896 / 2,589 | 7/21 | 3,393 / 3,573 | 5/8 | 415.5 | [gov_10a_exp x nama_10_pc] |
| COFOG GF09 per capita (derived) | PPS per inhabitant (derived) | 2005 | **1,376** | n/a | n/a / n/a | 1,154 / 1,106 | 7/26 | 1,177 / 1,170 | 5/20 | 1,441 / 1,549 | 5/8 | n/a | [gov_10a_exp x nama_10_pc] |
| COFOG GF09 per capita (derived) | PPS per inhabitant (derived) | 2015 | **1,564** | 1,307 | 1,354 / 1,369 | 1,403 / 1,241 | 9/27 | 1,398 / 1,262 | 7/21 | 1,795 / 1,905 | 5/8 | 210.6 | [gov_10a_exp x nama_10_pc] |
| COFOG GF09 per capita (derived) | PPS per inhabitant (derived) | 2024 | **2,004** (p) | 1,889 | 1,916 / 1,928 | 2,075 / 1,988 | 12/27 | 2,085 / 1,990 | 10/21 | 2,421 / 2,711 | 6/8 | 88.3 | [gov_10a_exp x nama_10_pc] |
| COFOG GF10 per capita (derived) | PPS per inhabitant (derived) | 2005 | **5,428** | n/a | n/a / n/a | 3,568 / 3,012 | 6/26 | 3,648 / 3,273 | 4/20 | 4,951 / 4,827 | 4/8 | n/a | [gov_10a_exp x nama_10_pc] |
| COFOG GF10 per capita (derived) | PPS per inhabitant (derived) | 2015 | **7,172** | 5,451 | 5,856 / 5,921 | 4,829 / 3,951 | 6/27 | 4,958 / 4,146 | 4/21 | 6,403 / 6,460 | 3/8 | 1,316 | [gov_10a_exp x nama_10_pc] |
| COFOG GF10 per capita (derived) | PPS per inhabitant (derived) | 2024 | **9,313** (p) | 7,838 | 8,329 / 8,385 | 7,098 / 5,758 | 7/27 | 7,357 / 6,182 | 6/21 | 8,821 / 8,823 | 4/8 | 983.8 | [gov_10a_exp x nama_10_pc] |
| COFOG GF1002 per capita (derived) | PPS per inhabitant (derived) | 2005 | **2,851** | n/a | n/a / n/a | 1,774 / 1,466 | 5/26 | 1,890 / 1,608 | 4/20 | 2,146 / 1,930 | 3/8 | n/a | [gov_10a_exp x nama_10_pc] |
| COFOG GF1002 per capita (derived) | PPS per inhabitant (derived) | 2015 | **3,985** | 2,920 | 3,149 / 3,184 | 2,559 / 2,307 | 4/27 | 2,676 / 2,345 | 4/21 | 3,011 / 2,948 | 1/8 | 835.7 | [gov_10a_exp x nama_10_pc] |
| COFOG GF1002 per capita (derived) | PPS per inhabitant (derived) | 2024 | **5,265** (p) | 4,260 | 4,498 / 4,570 | 3,881 / 3,293 | 5/27 | 4,036 / 3,293 | 5/21 | 4,357 / 4,654 | 2/8 | 767.8 | [gov_10a_exp x nama_10_pc] |

#### Outcomes

| Indicator | Unit | Year | France | EU-27 agg. | EA agg. (EA21 / EA20) | EU-27 MS mean / median | FR rank EU-27 | EA21 MS mean / median | FR rank EA21 | Panel mean / median | FR rank panel (of 8) | FR - EA agg. (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Life expectancy at birth | years | 2005 | **80.3** | 78.4 | n/a / n/a | 77.1 / 78.7 | 3/27 | 77.5 / 79.1 | 2/21 | 79.8 / 79.6 | 3/8 | n/a | [demo_mlexpec] |
| Life expectancy at birth | years | 2015 | **82.1** | 80.5 | 81.2 / 81.3 | 79.5 / 80.8 | 4/27 | 79.9 / 81.2 | 3/21 | 81.6 / 81.5 | 4/8 | 0.9 | [demo_mlexpec] |
| Life expectancy at birth | years | 2024 | **83.0** (p) | 81.5 | 82.2 / 82.4 | 80.9 / 82.0 | 7/27 | 81.2 / 82.1 | 6/21 | 82.7 / 82.4 | 4/8 | 0.8 | [demo_mlexpec] |
| At-risk-of-poverty rate after social transfers (60% median) | % of population | 2005 | **13.0** | n/a | n/a / n/a | 15.3 / 14.0 | 16/24 | 15.8 / 14.8 | 14/19 | 14.0 / 12.2 | 4/8 | n/a | [ilc_li02] |
| At-risk-of-poverty rate after social transfers (60% median) | % of population | 2015 | **13.6** | 17.4 | 17.4 / n/a | 17.1 / 16.3 | 22/27 | 17.4 / 16.6 | 18/21 | 16.2 / 16.3 | 6/8 | -3.8 | [ilc_li02] |
| At-risk-of-poverty rate after social transfers (60% median) | % of population | 2025 | **16.3** | 16.3 | 16.9 / n/a | 16.0 / 15.6 | 11/27 | 16.7 / 16.1 | 10/21 | 15.1 / 15.6 | 3/8 | -0.6 | [ilc_li02] |
| At-risk-of-poverty rate before social transfers (pensions counted as income) | % of population | 2005 | **26.0** | n/a | n/a / n/a | 25.4 / 25.6 | 9/24 | 24.8 / 24.5 | 5/19 | 25.7 / 24.5 | 4/8 | n/a | [ilc_li10] |
| At-risk-of-poverty rate before social transfers (pensions counted as income) | % of population | 2015 | **23.9** | 25.6 | n/a / n/a | 26.2 / 25.8 | 22/27 | 26.5 / 26.4 | 18/21 | 26.5 / 25.8 | 7/8 | n/a | [ilc_li10] |
| At-risk-of-poverty rate before social transfers (pensions counted as income) | % of population | 2025 | **26.5** | 24.4 | 25.1 / n/a | 24.1 / 24.4 | 7/27 | 24.8 / 24.4 | 7/21 | 24.4 / 24.5 | 2/8 | 1.4 | [ilc_li10] |
| Poverty reduction by social transfers excl. pensions (before - after) | percentage points | 2005 | **13.0** | n/a | n/a / n/a | 10.1 / 10.4 | 7/24 | 8.9 / 8.6 | 4/19 | 11.6 / 11.0 | 4/8 | n/a | [ilc_li10 - ilc_li02] |
| Poverty reduction by social transfers excl. pensions (before - after) | percentage points | 2015 | **10.3** | 8.2 | n/a / n/a | 9.1 / 8.4 | 12/27 | 9.2 / 8.4 | 9/21 | 10.2 / 10.7 | 5/8 | n/a | [ilc_li10 - ilc_li02] |
| Poverty reduction by social transfers excl. pensions (before - after) | percentage points | 2025 | **10.2** | 8.1 | 8.2 / n/a | 8.1 / 8.2 | 6/27 | 8.2 / 8.2 | 5/21 | 9.2 / 8.3 | 3/8 | 2.0 | [ilc_li10 - ilc_li02] |
| Gini coefficient of equivalised disposable income | index 0-100 | 2015 | **29.2** | 30.8 | n/a / 30.7 | 30.3 / 29.7 | 15/27 | 30.6 / 30.1 | 13/21 | 29.2 / 27.4 | 4/8 | -1.5 | [ilc_di12] |
| Gini coefficient of equivalised disposable income | index 0-100 | 2025 | **30.4** | 29.2 | 29.9 / 29.8 | 29.1 / 29.2 | 11/27 | 29.6 / 30.4 | 11/21 | 28.3 / 28.6 | 3/8 | 0.5 | [ilc_di12] |

#### Panel country values

| Indicator (year) | FR | DE | IT | ES | NL | BE | SE | DK | top 3 EU-27 |
|---|---|---|---|---|---|---|---|---|---|
| Total general government expenditure (2025) | **57.3** | 50.1 | 51.1 | 45.3 | 45.2 | 54.4 | 49.3 | 47.2 | FI 57.5; FR 57.3; AT 54.6 |
| Total general government revenue (2025) | **52.2** | 47.2 | 48.0 | 42.9 | 43.6 | 49.2 | 47.8 | n/a | FI 53.7; FR 52.2; AT 50.4 |
| Net lending(+)/borrowing(-) (EDP deficit) (2025) | **-5.1** | -2.9 | -3.1 | -2.4 | -1.6 | -5.2 | -1.6 | 2.9 | RO -7.8; PL -7.2; BE -5.2 |
| Gross debt (Maastricht) (2025) | **115.7** | 62.8 | 136.7 | 100.5 | 44.7 | 108.1 | 35.1 | 27.2 | EL 145.4; IT 136.7; FR 115.7 |
| Total taxes and net social contributions (S13+S212, after D.995) (2024) | **45.3** | 40.9 | 42.3 | 37.2 | 39.4 | 45.2 | 41.8 | 45.5 | DK 45.5; FR 45.3; BE 45.2 |
| COFOG GF10 Social protection (2024) | **23.7** (23.6 at current GDP) | 20.4 | 21.3 | 18.7 | 16.6 | 20.4 | 19.0 | 19.6 | FI 26.5; FR 23.7; AT 22.8 |
| COFOG GF1002 Old age (2024) | **13.4** | 9.9 | 13.9 | 10.4 | 6.1 | 10.2 | 10.9 | 7.2 | FI 15.5; AT 14.3; IT 13.9 |
| COFOG GF07 Health (2024) | **8.9** | 7.6 | 6.6 | 6.5 | 7.3 | 8.0 | 7.4 | 8.3 | AT 9.5; HR 9.0; CZ 9.0 |
| COFOG GF09 Education (2024) | **5.1** | 4.5 | 4.0 | 4.1 | 5.1 | 6.3 | 7.2 | 5.6 | SE 7.2; BE 6.3; EE 6.3 |
| COFOG GF02 Defense (2024) | **1.9** (1.8 at current GDP) | 1.4 | 1.3 | 0.9 | 1.6 | 1.3 | 1.9 | 1.8 | EE 3.7; PL 2.9; LV 2.7 |
| COFOG GF0107 Public debt transactions (interest) (2024) | **2.0** | 1.1 | 4.0 | 2.5 | 0.7 | 2.3 | 0.8 | 0.8 | HU 5.0; IT 4.0; EL 3.6 |
| Compensation of employees (D.1, payable) (2025) | **12.4** | 8.5 | 9.0 | 10.7 | 8.9 | 12.6 | 12.3 | 14.2 | DK 14.2; HR 13.5; FI 13.5 |
| Social protection benefits (ESSPROS) (2024) | **32.0** | 30.0 | 28.4 | 25.2 | 26.4 | 28.7 | 27.3 | 27.9 | FI 32.5; FR 32.0; AT 31.9 |
| Total GG expenditure per capita (TE % GDP x GDP per capita PPS) (2025) | **23,330** | 24,360 | 20,478 | 17,287 | 24,929 | 25,893 | 22,847 | 25,460 | LU 49501.3; AT 26971.3; BE 25893.0 |

Source for the panel table: Eurostat `gov_10a_main`, `gov_10dd_edpt1` (2025), `gov_10a_taxag`, `gov_10a_exp`, `spr_exp_type` (2024), `nama_10_pc` (2025). Per capita PPS is derived (see 1.2). COFOG and tax-aggregate rows in this panel table are the published % of GDP (2024 France values on a pre-May-2026 GDP); the canonical France values at current GDP are 23.6 (GF10) and 1.8 (GF02) (note added 2026-10-25). Denmark's 2025 revenue is not yet disseminated in `gov_10a_main` (the deficit is: +2.9%).

### 3.2 Where does France's spending gap come from? (COFOG decomposition, 2024)

France spends **7.8 pp of GDP** more than the GDP-weighted euro area (EA21) in 2024: 57.0% vs 49.2% on `gov_10a_main` (canonical), and 7.84 pp on the COFOG total once COFOG euro amounts are divided by current GDP. At 2024 GDP (EUR 2,935.2 bn), that is about **EUR 229 bn**. *(Reconciled 2026-10-25: the earlier version used the COFOG table's own % of GDP, 57.3 vs 49.1 = 8.2 pp. France's COFOG % of GDP for 2024 still uses a pre-May-2026 GDP: its euro level, EUR 1,671.8 bn, is the same as `gov_10a_main` and equals 57.0% of current GDP. Recomputed in `data/00_reconcile_cofog_gap_2024_EA20_EA21.csv`.)* Decomposition by function (France minus EA21 aggregate, % of GDP; Eurostat `gov_10a_exp` EUR amounts / `nama_10_gdp`):

| COFOG division | France 2024 | EA21 agg. | Gap (pp of GDP) | Approx. EUR bn | Share of total gap | France minus panel mean (pp) | Source |
|---|---|---|---|---|---|---|---|
| 10 Social protection | 23.6 | 20.0 | **+3.6** | ~106 | ~46% | +4.3 | [E5] |
| of which 10.2 Old age | 13.4 | 10.8 | **+2.5** | ~74 | ~32% | +3.6 | [E5] |
| 07 Health | 8.9 | 7.4 | **+1.5** | ~43 | ~19% | +1.6 | [E5] |
| 06 Housing and community amenities | 1.4 | 0.7 | +0.7 | ~21 | ~9% | +0.9 | [E5] |
| 02 Defense | 1.8 | 1.4 | +0.5 | ~14 | ~6% | +0.4 | [E5] |
| 09 Education | 5.1 | 4.6 | +0.5 | ~13 | ~6% | -0.2 | [E5] |
| 04 Economic affairs | 5.7 | 5.2 | +0.4 | ~13 | ~6% | +0.8 | [E5] |
| 08 Recreation, culture, religion | 1.5 | 1.1 | +0.3 | ~10 | ~4% | +0.3 | [E5] |
| 05 Environmental protection | 1.0 | 0.9 | +0.2 | ~5 | ~2% | +0.2 | [E5] |
| 01 General public services (incl. interest 01.7) | 6.2 | 6.1 | +0.1 | ~2 | ~1% | +0.1 | [E5] |
| 03 Public order and safety | 1.8 | 1.7 | +0.1 | ~2 | ~1% | +0.2 | [E5] |
| **Total** | **57.0** | **49.1** | **+7.8** | **~230** | 100% | +8.4 | [E5] |

**Key takeaway:** about **two-thirds of France's spending gap with the euro area is social protection plus health** (5.1 of 7.8 pp, 65%). Pensions alone (old age, 2.5 pp) account for about a third (32%). These shares match file 01 (EA20: 46% / 19% / 32%). Interest (01.7) and general public services, often cited in public debate as "bureaucracy", account for almost none of the gap **as measured by COFOG**. Caveat: COFOG classifies administrative staff within each function, so "administration" in a broad sense is spread across divisions. Note also that France's compensation of employees (D.1, an economic, not functional, classification) is 2.4 pp above the euro area (section 3.1).

### 3.3 Evolution of France's gap over ~20 years (France minus EA21 aggregate, pp of GDP)

| Indicator | 1995 | 2005 | 2015 | 2017 | 2019 | 2024 | 2025 | Source |
|---|---|---|---|---|---|---|---|---|
| Total expenditure (TE) gap vs EA21 agg. | +2.9 | +7.1 | +9.0 | +10.4 | +8.4 | +7.8 | **+7.6** | `09_intl_fr_gap_timeseries.csv` from [E1] |
| TE gap vs EU-27 MS unweighted mean | +8.4 | +10.5 | +12.2 | +14.8 | +12.2 | +11.3 | **+10.9** | [E1] |
| Total revenue (TR) gap vs EA21 agg. | +5.0 | +6.2 | +7.1 | +8.0 | +6.6 | +5.1 | **+5.5** | [E1] |
| Taxes + social contributions gap vs EA21 agg. | +3.7 | +5.1 | +6.5 | +7.2 | +6.0 | **+4.7** | n/a | [E4] |
| Debt gap vs EA21 agg. | n/a (EA21 not available) | -2.0 | +6.3 | +11.7 | +15.0 | +26.5 | **+28.4** | [E2] |

Reading: the **expenditure gap widened from about 3 pp (1995) to a peak of about 10 pp (2017)**. It has narrowed to about 7.6 pp since then, mainly because the euro area's spending ratio rose (EA21 TE: 47.3% in 2017 vs 49.7% in 2025), while France's moved from 57.7% to 57.3%. The **revenue gap narrowed more** (8.0 pp in 2017 to 5.5 pp in 2025). The **debt gap exploded**: France was below the euro-area debt ratio in 2005 (68.2% vs 70.2%) and is now 28 pp above it.

### 3.4 OECD comparisons (OECD-38)

| Indicator | Year | France | OECD mean (computed, unweighted) | OECD median | n | France rank | OECD published average | Top 5 | Source |
|---|---|---|---|---|---|---|---|---|---|
| Total tax revenue (incl. social security contributions) | 2005 | 43.1 | 32.6 | 32.7 | 38 | 4 | 32.6 | DNK 47.9; SWE 47.4; BEL 43.4; FRA 43.1; NOR 42.6 | [O1] |
| Total tax revenue | 2015 | 45.4 | 32.9 | 32.9 | 38 | 2 | 32.9 | DNK 46.5; FRA 45.4; BEL 44.2; FIN 43.8; AUT 43.7 | [O1] |
| Total tax revenue | 2022 | 45.9 | 34.0 | 34.7 | 38 | **1** | 34.0 | FRA 45.9; FIN 43.4; NOR 43.3; AUT 43.0; SWE 42.9 | [O1] |
| Total tax revenue | 2023 | 43.9 | 33.7 | 35.0 | 38 | 2 | 33.7 | DNK 44.0; FRA 43.9; FIN 42.8; AUT 42.6; BEL 41.9 | [O1] |
| Total tax revenue | **2024** (provisional) | **43.5** | 34.2 (36 countries) | 35.2 | 36 (AUS, JPN missing) | **2** | **34.1** | DNK 45.2; FRA 43.5; AUT 43.4; ITA 42.8; BEL 42.6 | [O1] |
| GG total expenditure | 2005 | 54.3 | 41.1 | 42.2 | 36 | 1 | n/a | FRA 54.3; SWE 52.3; BEL 51.9; AUT 51.7; DNK 51.1 | [O2] |
| GG total expenditure | 2015 | 57.6 | 42.3 | 41.7 | 37 | 1 | n/a | FRA 57.6; FIN 55.7; GRC 54.8; DNK 54.4; BEL 53.9 | [O2] |
| GG total expenditure | 2023 | 56.8 | 43.5 | 44.5 | 37 | 1 | n/a | FRA 56.8; FIN 56.1; ITA 53.6; BEL 52.7; AUT 52.1 | [O2] |
| GG total expenditure | **2024** | **57.0** | 43.9 | 45.3 | 37 (TUR missing) | **2** | n/a | FIN 57.9; FRA 57.0; AUT 54.6; BEL 54.1; ITA 50.3 | [O2] |
| GG total expenditure | 2025 (partial) | 57.3 | 46.4 | 47.3 | 28 (non-European members mostly missing) | 2 | n/a | FIN 57.5; FRA 57.3; AUT 54.6; BEL 54.4; ITA 51.1 | [O2] |
| GG compensation of employees | 2024 | 12.4 | 10.4 | 10.9 | 36 | 9 | n/a | ISL 14.2; DNK 14.0; FIN 13.4; NOR 13.0; LVA 12.9 | [O2] |

Notes: the OECD "average" in *Revenue Statistics* is unweighted. The 2024 figure (34.1%) was estimated by OECD by applying the average change of reporting countries to the 2023 average, so it is not a fully recomputed mean. Our recomputed mean for the 36 reporting countries is 34.2%. OECD NAAG uses the same ESA 2010 data as Eurostat for European members; for non-EU members it uses SNA 2008 national definitions, so cross-OECD expenditure comparisons are less harmonized than intra-EU ones. The 2025 OECD sample (28) is biased towards European countries and should not be used for averages.

---

## 4. International comparison: synthesis

1. **Size of government.** France has had the EU's and OECD's highest public expenditure ratio for most of the past 20 years: on the October 2026 Eurostat vintage it was 1st in 2005 and in every year from 2014 to 2023. **In 2024 and 2025 it ranks 2nd behind Finland.** (On SOCX *public social* expenditure, a different indicator, it was 2nd behind Finland in 2023: see section 7.1.) The France-euro area gap is +7.6 pp of GDP in 2025, about **EUR 227 bn** at 2025 GDP. Against the typical (median) EU country the gap is +10 pp (57.3 vs 47.3).
2. **Taxes.** France ranks 1st or 2nd in both the EU (Eurostat) and the OECD (2nd of 36 in 2024, behind Denmark). The tax gap with the euro area (+4.7 pp, 2024) is **smaller than the expenditure gap** (+7.8 pp in 2024). (Corrected after verification: was "The difference is the structural deficit, financed by debt". "Structural deficit" is a technical, cyclically adjusted concept that was not computed here.) The roughly 3 pp difference corresponds mainly to France's **larger headline deficit** (EDP deficit gap vs EA21: 5.8 - 3.0 = 2.8 pp in 2024), plus a small difference in non-tax revenue (total revenue gap 5.1 pp vs tax gap 4.7 pp).
3. **Composition.** The gap is concentrated in **social protection (especially pensions) and health**. Education is near the EU median as % of GDP and **below the panel and EU-27 mean in PPS per inhabitant** (2,004 PPS vs EU mean 2,075 and panel mean 2,421, 2024). Tertiary education (GF0904) is **0.4% of GDP, 25th of 27**: COFOG records much French higher education spending under other headings (e.g. research), so treat this with caution. Defense is above the EU mean but below the Baltic/Polish frontline states. Interest is close to the euro-area aggregate in 2024 (2.0 vs 1.9), although rising (ESA D.41: 2.2% in 2025).
4. **Per inhabitant in PPS the picture changes.** Because French GDP per capita (PPS) is **below the EU-27 average in 2025 (40,716 vs 41,774) and below every panel country except Italy and Spain**, France's high ratios partly reflect a smaller denominator. In PPS per inhabitant, total public expenditure ranks **8th in the EU** and **5th of 8 in the panel** (below BE, NL, DK, DE). It is only 1.3% above the panel mean. ESSPROS social protection per inhabitant ranks 6th. The French specificity is a **high share of national income channeled through the state, not an unusually high volume of public services per person** compared with richer northern neighbors.
5. **Social contributions vs taxes.** France's lead in compulsory levies comes from **social contributions** (D.61: 16.5% of GDP in 2024, 3rd behind DE and SI; 1st in 2005 and 2015). Its taxes excluding contributions (28.9%) rank only 7th in the EU, far below Denmark (45.2%), whose welfare state is tax-financed. This matters for the platform: "taxing the rich" acts on the D.5/D.91 part, not on the contribution-financed core of the welfare state.

---

## 5. Outcome indicators (what is obtained for the spending)

| Outcome | France | Year | EU-27 agg. | EU-27 MS mean | FR rank EU-27 (1 = highest) | Panel mean | FR rank panel | Source |
|---|---|---|---|---|---|---|---|---|
| Life expectancy at birth (years) | 83.0 (p) | 2024 | 81.5 | 80.9 | 7/27 | 82.7 | 4/8 | Eurostat `demo_mlexpec` [E8] |
| At-risk-of-poverty rate after social transfers (60% of median, %) | 16.3 | 2025 (SILC survey year; incomes of 2024) | 16.3 | 16.0 | 11/27 (17th-lowest) | 15.1 | 3/8 | Eurostat `ilc_li02` [E9] |
| At-risk-of-poverty rate before social transfers (pensions counted as income, %) | 26.5 | 2025 | 24.4 | 24.1 | 7/27 | 24.4 | 2/8 | Eurostat `ilc_li10` [E10] |
| Poverty reduction by non-pension transfers (pp) | 10.2 | 2025 | 8.1 | 8.1 | 6/27 | 9.2 | 3/8 | derived [E9]-[E10] |
| Gini coefficient of disposable income (0-100) | 30.4 | 2025 | 29.2 | 29.1 | 11/27 | 28.3 | 3/8 | Eurostat `ilc_di12` [E11] |
| Poverty rate after transfers, 2015 (for trend) | 13.6 | 2015 | 17.4 | 17.1 | 22/27 | 16.2 | 6/8 | [E9] |

Reading: France's transfers reduce poverty more than the EU average (10.2 pp vs 8.1), and life expectancy is in the top third. However, **France's relative position on poverty and inequality has deteriorated since 2015**: its poverty rate rose from 13.6% to 16.3% (rank moved from 22nd to 11th highest), and the Gini rose from 29.2 to 30.4. The 2025 SILC value should be checked against Insee's own poverty release (ERFS/SRCV), because EU-SILC break-in-series notes apply. Sector-specific outcomes (PISA, health system efficiency, pension adequacy) are covered in the thematic files.

---

## 6. Divergences between sources

| Topic | Values | Why they differ |
|---|---|---|
| **Compulsory levies, France 2024** | Eurostat broad (D.2+D.5+D.91+D.61-D.995, S13+S212): **45.3%**. Eurostat excluding imputed (D.612) and voluntary household (D.614) contributions: **43.5%**. OECD *Revenue Statistics*: **43.5%**. Insee *prélèvements obligatoires*: 43.6% for **2025** and **42.7% for 2024** (Insee Première, 29 May 2026 [I1]; corrected after verification: was "the 2024 Insee value was not re-checked here") | The Eurostat broad aggregate includes **imputed social contributions** (D.612, the notional employer contribution for civil-servant pensions, a large item in France), which Insee and OECD exclude. Insee states that its PO rate is **net of tax credits** (*nets des crédits d'impôt*), whereas national accounts record refundable tax credits as expenditure. **Bridge (verified 2026-10-25; was "plausibly explains most of the 0.8 pp gap", flagged unverified):** (1) Insee's PO series note says its rate is "*hors cotisations sociales imputées et crédit d'impôts*" (excluding imputed social contributions and tax credits) and includes the share collected for the EU (0.1 pt), so the like-for-like Eurostat measure is the S13+S212 aggregate excluding D.612/D.614: EUR 1,270.2 bn in 2024 (`gov_10a_taxag`, 21 Oct 2026). (2) Part of the 0.8 pp is a **GDP vintage effect**: that amount divided by current 2024 GDP (EUR 2,935.2 bn) is **43.28%**, not the published 43.5%. (3) **Tax credits** recorded as expenditure: total expenditure 2024 (EUR 1,672.7 bn) minus expenditure excluding tax credits (about EUR 1,653 bn, derived from HCFP-2026-5: EUR 1,742 bn in 2026 after growth of +2.8% in 2026 and +2.5% in 2025, §80-81 and Table 15) is about **EUR 19-20 bn = 0.66 pp** of GDP (2025 cross-check: 57.3% vs 56.6% excl. tax credits, also about 0.7 pp). (4) 43.28 - 0.66 = 42.62% vs Insee 42.72%: a **residual of about 0.1 pp** remains unexplained (rounding of the derived tax-credit amount, D.614 treatment or other small items; Insee does not publish an item-by-item bridge). In words: of the apparent 0.8 pp gap, about 0.2 pp is GDP vintage and about 0.7 pp is tax credits, offset by about 0.1 pp of unexplained residual. Sources: Insee PO series https://www.insee.fr/fr/statistiques/2381412 (note to the table); HCFP https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf; Eurostat https://ec.europa.eu/eurostat/databrowser/view/gov_10a_taxag/default/table. (Corrected after verification: was "Insee's PO also excludes certain taxes and adjusts for uncollectable amounts". Uncollectable amounts, D.995, are already deducted in the Eurostat measures, so this is not a source of difference.) OECD excludes D.612 and voluntary contributions. **Recommendation:** for international ranking use OECD 43.5% or Eurostat-excl-imputed 43.5%; never mix the 45.3% broad Eurostat figure with Insee's PO. |
| **Total expenditure France 2024: 57.0% vs 57.3%** | `gov_10a_main` 2024: **57.0%**; `gov_10a_exp` COFOG total 2024: **57.3% (p)** | **Vintage difference.** The COFOG breakdown for 2024 still reflects France's earlier transmission (provisional flag "p"); the main aggregates were revised in the spring/autumn 2026 transmission. The full 2025 COFOG breakdown and revised 2024 values are expected with Eurostat's early-2027 COFOG release. Use `gov_10a_main` for totals and COFOG for **structure** only. |
| **Total expenditure: Eurostat vs OECD** | Eurostat 2025: 57.3; OECD NAAG 2025: 57.31; 2024: 57.0 vs 56.99 | Same ESA 2010 data; rounding only. |
| **Social protection: COFOG GF10 (23.6% at current GDP; 23.7% in the published COFOG table) vs ESSPROS benefits (31.96%) vs ESSPROS total (34.37%), 2024** | | **Scope.** COFOG 10 excludes health care (in COFOG 07) and covers only general government. ESSPROS includes sickness/health care benefits, benefits paid by **non-government** schemes (e.g. supplementary pension schemes run by social partners where classified outside S13, employer-provided benefits, *mutuelles*), and in the "total" also administration costs. Drees's 31.9% corresponds to ESSPROS benefits. |
| **Interest: COFOG 01.7 (2.0%) vs ESA D.41 (2.0% in 2024; 2.2% in 2025)** | | Close in 2024. D.41 is the economic-classification measure (accrued interest, after FISIM). Budget-accounting interest (*charge de la dette* in the State budget, incl. inflation indexation of OATi) differs and is higher in high-inflation years. |
| **Euro area aggregate: EA20 vs EA21** | 2025 TE: EA20 49.8 vs EA21 49.7; debt: EA20 87.7 vs EA21 87.3 | Bulgaria's inclusion (low debt, low spending) lowers the EA21 ratios marginally. Eurostat's news release of 21 Oct 2026 uses EA20 for 2025 data. |
| **Social protection per capita in PPS, ESSPROS "total expenditure" vs "benefits"** | 13,557 vs 12,606 PPS (2024) | The total includes administration and other expenditure. |
| **EU-SILC year convention** | "2025" poverty rate = SILC survey 2025 = incomes of 2024 for France | Comparisons with Insee's *taux de pauvreté* (which dates by income year) must shift by one year. |

---

## 7. Economists' disagreements and the strongest counter-arguments to the platform's thesis (steelman)

The platform's thesis is that proposals promising to restore public finances or purchasing power without addressing the structure of spending misjudge orders of magnitude. The data above broadly support **that France's distinctive feature is spending, concentrated in pensions and health**. Below are the strongest objections, with the data to assess each.

### 7.1 "Gross public spending overstates the difference: net, total social spending is not exceptional" (strong)

OECD SOCX lets us move from **gross public** social spending to **net total** social spending (public + mandatory and voluntary private, after taxes on benefits and adding tax breaks for social purposes):

| Measure (OECD SOCX) | Year | France | France rank OECD-38 | OECD mean | DE | IT | NL | SE | DK | USA | GBR | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Public gross social expenditure, % GDP | 2022 | 31.4 | **1** | 20.5 | 27.7 | 28.2 | 17.7 | 25.3 | 25.5 | 19.0 | 22.7 | OECD SOCX `DF_PUB_PRV` [O3] |
| Private (mandatory + voluntary) social expenditure, % GDP | 2021 | 3.6 | 9 | 3.0 | 3.6 | 2.1 | 11.4 | 2.8 | 3.4 | **12.8** | 4.1 | [O3] |
| **Net total** social expenditure, % GDP | 2019 | 30.1 | **1** | 20.3 | 26.3 | 24.3 | 24.9 | 23.6 | 25.0 | 29.2 | 24.1 | OECD SOCX `DF_NET_GDP` [O4] |
| **Net total** social expenditure, % GDP | 2021 | 32.0 (raw 31.95) | **2** (USA 33.2) | 22.0 | 28.5 | 26.4 | 27.0 | 23.9 | 24.4 | **33.2** | 26.0 | [O4] |
| Public gross social expenditure, % GDP (same year as net, added after verification) | 2021 | 32.7 | **1** | 22.1 | 28.9 | 29.8 | 19.8 | 26.3 | 28.1 | 21.6 | 24.4 | [O3] |
| Public gross social expenditure, % GDP (added after verification: newer SOCX data) | 2023 (33 of 38 countries) | 30.6 | **2** (FIN 30.9) | 20.9 | 27.3 | 27.5 | 18.4 | 25.8 | 26.3 | 19.0 | 23.0 | [O3] |
| Public gross social expenditure, % GDP (added after verification; partly estimates) | 2024 (24 of 38 countries) | 30.6 | **3** (AUT 31.6, FIN 31.4) | n/a (incomplete) | 27.9 | 27.6 | 18.9 | 26.1 | 26.4 | 19.8 | n/a | [O3] |

Reading: once **private** provision (Dutch occupational pensions, US employer health insurance) and **taxation of benefits** (heavy in Denmark and Sweden) are counted, the France-Netherlands gap shrinks from about **12.9 pp** (gross public, 2021) to about 4.9 pp (net total, 2021). (Corrected after verification: was "13.7 pp (gross public 2022) to 4.9 pp (net total 2021)", which compared two different years.) The **United States spends more than France** in net total terms in 2021. **Update (after verification):** SOCX now has public gross data for 2023 (33 countries) and 2024 (24 countries, partly estimates). France is no longer 1st: it is **2nd in 2023 behind Finland** and **3rd in 2024 behind Austria and Finland** among reporting countries. The steelman: **France has socialized what other countries finance privately**, so cutting public spending could shift costs onto households (insurance premiums, private pension savings) rather than eliminate them. **Response for the platform:** the fiscal problem (deficit, debt) concerns the *public* share. Whether to move costs to private funding is a political choice with distributive effects, not a free saving. The two framings should be presented together.

### 7.2 "France's ratios are high because its GDP per head is low, not because the state is lavish" (strong)

Per inhabitant in PPS, France's total public expenditure (23,330 PPS, 2025) is **8th in the EU-27** and **below BE, NL, DK and DE** (section 3.1). The thesis ("France spends more than everyone") holds **in % of GDP**, much less **in volume per inhabitant**. The platform should always show both measures.

### 7.3 "The deficit deterioration since 2017 is revenue-driven, not spending-driven" (strong, and much debated in France)

From Eurostat: between **2017 and 2024**, France's expenditure ratio fell by **0.7 pp** (57.7 to 57.0), while its revenue ratio fell by **3.1 pp** (54.3 to 51.2), and the deficit widened from 3.4% to 5.8%. *(Concept note, 2026-10-25: this is ESA **total revenue** (TR), not *prélèvements obligatoires*. Insee's PO ratio fell 2.6 pts (45.3 → 42.7, May 2026 vintage; OFCE's −2.5 uses the earlier vintage), and the Cour des comptes values the **discretionary** cuts of 2018-2023 at EUR 62 bn = 2.2 pts. Part of the TR and TE falls reflects the 2019 conversion of the CICE, recorded as spending in ESA, into contribution cuts (about 1 pt of GDP, per the Insee blog cited in file 01).)* On this arithmetic, **the revenue decline accounts for the entire deterioration**. Economists at OFCE (*Observatoire français des conjonctures économiques*, Sciences Po, generally Keynesian / center-left orientation) and IPP (*Institut des politiques publiques*, academic, PSE/CREST), together with the Cour des comptes's analyses of tax cuts (*baisses de prélèvements obligatoires*: housing tax, CVAE, corporate income tax, social contributions), stress the cost of the tax and contribution cuts since 2018. The sourced figure is the Cour des comptes's: the 2018-2023 cuts (corporate income tax, CVAE, abolition of the *taxe d'habitation* (housing tax), social-contribution relief, etc.) had an impact "*estimé à 62 Md€ en 2023, soit 2,2 pts de PIB*" (estimated at EUR 62 bn in 2023, i.e. 2.2 points of GDP), cumulative and valued in 2023 (Cour des comptes, *La situation et les perspectives des finances publiques*, July 2024, chapter I.II.C, p. 35, https://www.ccomptes.fr/sites/default/files/2024-09/20240715-RSPFP-2024.pdf; file 00 row 28). *(Corrected 2026-10-25: was "several tens of billions of euros per year", flagged unverified, with no source.)* The Cour adds that the PO rate in 2022 (45.0%) was still close to 2017 (45.3%) because of strong spontaneous revenue growth in 2021-2022, which "masked" the cuts until 2023. **Counter-counter-argument:** (i) the 2017 revenue peak was inflated: the CICE tax credit was recorded as expenditure (subsidies) in national accounts, then converted into lower employer contributions in 2019, which lowered revenue (actual contributions received fell 4.4% in 2019 "under the effect of the CICE transformation") and, once the residual CICE claims had been paid, lowered expenditure too. The switch also cost about 0.9 pp of GDP one-off in 2019, when the 2018 CICE claims and the new contribution cuts overlapped (corrected after verification: was "from memory, should be confirmed with Insee". Now **confirmed** by Insee, *Les comptes de la Nation / compte des APU 2019*, March and May 2020, https://www.insee.fr/fr/statistiques/4470888 and https://www.insee.fr/fr/statistiques/fichier/4498247/ip1801.pdf). Part of the 2017-2024 revenue fall is therefore a **reclassification from the expenditure side to the revenue side**, not a net tax cut; (ii) the 2023-2024 revenue shortfalls were partly cyclical/compositional "spontaneous" elasticity effects, documented by the HCFP and Cour des comptes; (iii) a 7.6 pp spending gap with the euro area remains, whatever caused the recent deterioration. **The platform should acknowledge that "spending is the structural difference" and "revenue cuts drove the recent deficit" are both true.**

### 7.4 "High spending buys outcomes: lower poverty, high life expectancy, low elderly poverty" (medium)

France's transfers cut poverty by 10.2 pp (EU mean 8.1), life expectancy is 7th in the EU, and pension spending finances a low old-age poverty rate (see pensions file). However, France's poverty and inequality rankings have worsened since 2015 despite stable spending, and per-PPS spending is close to that of the panel, which obtains similar or better outcomes (NL, DK, SE: lower poverty, similar life expectancy). The efficiency argument therefore cuts both ways.

### 7.5 "Interest is not the problem" (supported by data, but trending)

COFOG interest (2.0% of GDP, 2024) is close to the euro-area aggregate, and well below Italy (4.0%). But the debt gap is now 28 pp, and D.41 rose to 2.2% in 2025. With the debt ratio rising, interest is the fastest-rising item (see the debt file).

### 7.6 "Tax-to-GDP is already maximal, so the tax route is exhausted" (contested, the reverse steelman)

Denmark (45.2% OECD 2024) and earlier France (45.9% in 2022) show that higher ratios are possible. Defenders of wealth taxes point out that France's taxes *excluding* social contributions are only 7th in the EU (28.9% of GDP vs DK 45.2). Their argument is that the issue is the **mix and progressivity**, not the level. The orders of magnitude remain: closing a 5.1% deficit means about EUR 150 bn (2025 GDP). Yields of individual wealth-tax proposals should be compared with this figure (see the taxation/Zucman file).

---

## 8. Open questions and gaps

- **COFOG 2025** not yet published (expected early 2027). The 2024 French COFOG structure (57.3% total) is on an older vintage than the main aggregates (57.0%).
- **`gov_10a_taxag` 2025** not yet available, so the Insee 43.6% PO figure for 2025 could not be cross-checked against Eurostat. **OECD *Revenue Statistics 2026*** (2025 data) is expected in December 2026.
- **Denmark 2024-2025 total revenue** is missing in `gov_10a_main` (not yet disseminated), so Denmark is excluded from the 2024-2025 revenue ranks. This does not change France's 2nd place: DK TE 47.2 + surplus 2.9 implies TR of about 50.1%, below France's 52.2%.
- **PPS per capita for government spending** uses the GDP PPP. Eurostat's specific PPPs for "collective" and "individual" government consumption would give different volumes (France's PLI for government services was not tested).
- **SOCX** complete data stop at 2022 (gross) and 2021 (net), so the net comparison predates the latest years. Partial public gross data exist for 2023 (33 countries) and 2024 (24 countries), and in those years France ranks 2nd and 3rd (section 7.1, updated after verification).
- **CICE accounting treatment** (section 7.3): confirmed after verification with Insee (2019 APU account, 2020 releases).
- **Insee 2024 PO value**: 42.7% (Insee Première, 29 May 2026), checked after verification. The 0.8 pp gap with Eurostat/OECD (43.5%) is now bridged in section 6 (about 0.2 pp GDP vintage, about 0.7 pp tax credits, about 0.1 pp unexplained residual; verified 2026-10-25). Insee publishes no official item-by-item bridge.
- **Outcome indicators** are limited to cross-cutting outcomes. PISA, health-system efficiency (amenable mortality, OECD *Health at a Glance*) and pension adequacy (*Pension Adequacy Report*) belong to the thematic files.

---

## 9. Reproducibility notes

- Extraction: 2026-10-25, from the Eurostat SDMX 2.1 dissemination API (`format=SDMX-CSV`, `startPeriod=1995`) and the OECD SDMX REST API (`Accept: application/vnd.sdmx.data+csv`). Exact URLs are in `research/data/09_intl_download_log.csv`.
- For EU-SILC datasets the `EA20` code does not exist (HTTP 400). The script automatically retries without it.
- The ESSPROS dataset `spr_exp_sum` (used in older literature) is no longer disseminated. Use `spr_exp_type` (totals) and `spr_exp_func` (by function, with early estimates).
- Ranks use competition ranking (ties share the best rank). Missing countries per year are listed in the `missing_EU27` column of the stats CSV.

---

## 10. Sources (all accessed 2026-10-25)

| Ref | Institution | Title / dataset | Publication / update date | URL |
|---|---|---|---|---|
| E1 | Eurostat | Government revenue, expenditure and main aggregates (`gov_10a_main`) | updated 21 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table ; API: https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/gov_10a_main/A.PC_GDP.S13.TE.FR?format=SDMX-CSV |
| E2 | Eurostat | Government deficit/surplus, debt and associated data (`gov_10dd_edpt1`) | updated 21 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table |
| E3 | Eurostat | Euro indicators news release "Euro area government deficit at 3.0% and EU at 3.1% of GDP" (2nd EDP notification 2026) | 21 Oct 2026 | https://ec.europa.eu/eurostat/en/web/products-euro-indicators/w/2-21102026-ap |
| E4 | Eurostat | Main national accounts tax aggregates (`gov_10a_taxag`) | updated 21 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/gov_10a_taxag/default/table |
| E5 | Eurostat | General government expenditure by function (COFOG) (`gov_10a_exp`) | updated 21 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table |
| E6 | Eurostat | ESSPROS: Expenditure on social protection by type (`spr_exp_type`); Expenditure on social benefits by function (`spr_exp_func`) | 7 Oct 2026; 23 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/spr_exp_type/default/table ; https://ec.europa.eu/eurostat/databrowser/view/spr_exp_func/default/table |
| E7 | Eurostat | Main GDP aggregates per capita (`nama_10_pc`) | updated 22 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/nama_10_pc/default/table |
| E8 | Eurostat | Life expectancy by age and sex (`demo_mlexpec`) | updated 25 Sep 2026 | https://ec.europa.eu/eurostat/databrowser/view/demo_mlexpec/default/table |
| E9 | Eurostat | At-risk-of-poverty rate by poverty threshold, age and sex (EU-SILC) (`ilc_li02`) | updated 20 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/ilc_li02/default/table |
| E10 | Eurostat | At-risk-of-poverty rate before social transfers (pensions included in income) (`ilc_li10`) | updated 20 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/ilc_li10/default/table |
| E11 | Eurostat | Gini coefficient of equivalised disposable income (`ilc_di12`) | updated 20 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/ilc_di12/default/table |
| I1 | Insee | *Le compte des administrations publiques en 2025*, Insee Première n° 2106 (PO 43.6% in 2025, 42.7% in 2024; expenditure 57.3% / 57.0%) (added after verification) | 29 May 2026 | https://www.insee.fr/fr/statistiques/8997691 |
| O1 | OECD | *Revenue Statistics 2025* (report, chapter "Tax revenue trends 1965-2024") and dataset `DSD_REV_COMP_OECD@DF_RSOECD` v2.0 | Dec 2025 | https://www.oecd.org/en/publications/revenue-statistics-2025_3a264267-en/full-report/tax-revenue-trends-1965-2024_98c75833.html (works in a browser; returns HTTP 403 to scripts/curl) ; API: https://sdmx.oecd.org/public/rest/data/OECD.CTP.TPS,DSD_REV_COMP_OECD@DF_RSOECD,2.0/FRA.TAX_REV.S13._T._T.PT_B1GQ.A |
| O2 | OECD | *National Accounts at a Glance*, Chapter 6 General government (`DSD_NAAG_VI@DF_NAAG_VI` v1.0) | API, accessed 2026-10-25 | https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAAG_VI@DF_NAAG_VI,1.0/A.FRA.OTES13._T.PT_B1GQ. |
| O3 | OECD | Social Expenditure Database (SOCX), public and private social expenditure (`DSD_SOCX_AGG@DF_PUB_PRV`) | API, accessed 2026-10-25 | https://sdmx.oecd.org/public/rest/data/OECD.ELS.SPD,DSD_SOCX_AGG@DF_PUB_PRV,1.0/.A.SOCX.PT_B1GQ..._T. |
| O4 | OECD | SOCX, net total social expenditure in % GDP (`DSD_SOCX_AGG@DF_NET_GDP`) | API, accessed 2026-10-25 | https://sdmx.oecd.org/public/rest/data/OECD.ELS.SPD,DSD_SOCX_AGG@DF_NET_GDP,1.0/all |
| S1 | (this project) | Build script and CSV outputs | 2026-10-25 | `research/data/scripts/build_international_comparison.py` ; `research/data/09_intl_*.csv` |

---

## Verification log (2026-10-25)

Adversarial re-check by an independent fact-checker. All series were re-downloaded from the live APIs on 2026-10-25 (Eurostat JSON API `statistics/1.0`; OECD SDMX REST) into `research/data/raw/09_verify/` and `research/data/raw/09_verify_oecd/`. Means, medians and ranks were recomputed from scratch with an independent script (unweighted, competition ranking, EU-27 / EA21 / panel as defined in 1.2), not with the original build script.

**Confirmed exactly (value, unit, year, dataset vintage):**
- `gov_10a_main` (updated 21 Oct 2026): FR TE 2025 = 57.3% of GDP = EUR 1,714,111.7 m; TR 2025 = 52.2% = EUR 1,562,519.7 m; EA20 49.8 / EA21 49.7 / EU-27 49.4; EU-27 MS mean 46.4, median 47.3; FR rank 2/27 behind FI 57.5; TR rank 2/26 (DK missing) behind FI 53.7. TE 2024 57.0 (FI 57.9). D.1 2025 12.4% (EA21 10.0, EU 10.3, rank 6, DK 14.2). D.41 2025 2.2%. D.61 2025 16.7%.
- Gap series vs EA21 (TE): +2.9 (1995), +7.1 (2005), +9.0 (2015), +10.4 (2017), +8.4 (2019), +7.8 (2024), +7.6 (2025). The TE gap vs the EU mean, the TR gap and the debt gap series in section 3.3 are also all confirmed. The figure of about EUR 227 bn (7.6 x EUR 29.9 bn) is confirmed.
- `gov_10dd_edpt1` and Eurostat news release of 21 Oct 2026 (URL works, title confirmed): FR deficit -5.1 (4th after RO -7.8, PL -7.2, BE -5.2), debt 115.7 (3rd after EL 145.4, IT 136.7), EA20 -3.0 / 87.7, EU -3.1 / 81.5, EA21 debt 87.3. The release uses EA20 for 2025, as stated. GDP 2025 = EUR 2,991,056 m; GDP 2024 = EUR 2,935,236 m. 2017-2024: TE 57.7 to 57.0, TR 54.3 to 51.2, deficit -3.4 to -5.8.
- `gov_10a_taxag` 2024: broad 45.3 (DK 45.5, rank 2; EU 40.2; EA21 40.6); excl. D.612/D.614 43.5 (EU 39.3; rank 2); taxes only 28.9 (rank 7; DK 45.2); D.61 16.5 (rank 3 after DE 17.5, SI 17.2).
- `gov_10a_exp` 2024 (p): every COFOG division in the section 3.2 decomposition (GF01-GF10, GF1002, GF0107), the EA21 aggregates, the ranks, the panel means and "France minus panel mean". Total 57.3 vs EA21 49.1 = +8.2 pp, about EUR 240 bn *(published COFOG ratios on the pre-May-2026 GDP; note added 2026-10-25, index pass: at current GDP the canonical values are 57.0 vs 49.2 = +7.8 pp, about EUR 229 bn, and defense 1.8% of GDP, 8th of 27; see 00 rows 8 and 15 and log #6)*. GF10 41.5% of total expenditure, rank 4. Education 5.1% (median 5.0, rank 11). Defense 1.9% (rank 7; EE 3.7, PL 2.9, LV 2.7). Interest 2.0% (IT 4.0).
- `spr_exp_func` (updated 23 Oct 2026) / `spr_exp_type` (7 Oct 2026): benefits 31.96% (p) 2024, EU 27.41, rank 2 (FI 32.46); 2025 (e) 32.12, EU 27.49, rank 3 (AT 32.36, FI 32.20). Total 34.37% rank 1, EU 28.55. 13,557 PPS per inhabitant, rank 6 (LU 19,788, AT 14,934, DE 14,838); benefits 12,606 PPS.
- `nama_10_pc` (22 Oct 2026): FR 40,716 PPS (p) vs EU 41,774, rank 12/27. Derived TE per inhabitant: 23,330 PPS, rank 8/27 (LU, AT, BE, DK, NL, DE, FI above), EU agg. 20,636, EA21 21,424, panel mean 23,036, panel rank 5/8.
- Outcomes: `ilc_li02` 2025 16.3 (EU 16.3, rank 11; 2015 13.6, rank 22); `ilc_li10` 26.5; poverty reduction 10.2 vs EU 8.1; `ilc_di12` Gini 30.4 (2025) vs 29.2 (2015); `demo_mlexpec` 2024 83.0 (p), EU 81.5, rank 7.
- OECD *Revenue Statistics 2025*: verified in the report text (via browser). Quote: "Denmark had the highest tax-to-GDP ratio ... in 2024, at 45.2%. France had the second-highest tax-to-GDP ratio in 2024 (43.5%)". The OECD average is 34.1%, and footnote 2 confirms that the provisional average applies the 36-country average change to the 2023 average. API: FR 2022 45.9 (rank 1), 2023 43.9 (rank 2 behind DK 44.0), 2015 45.4 (rank 2), 2005 43.1 (rank 4).
- OECD NAAG: 2024 FR 56.99, rank 2/37 (FIN 57.9), mean 43.9, median 45.3. 2025 57.31 (28 countries).
- OECD SOCX: net total 2021 FR 32.0 (raw 31.95), rank 2 (USA 33.2), mean 22.0; 2019 30.1, rank 1. Public gross 2022 31.4, rank 1, mean 20.5. Private 2021 3.6, rank 9.
- Insee: PO 43.6% (2025) and public expenditure 57.3% (2025) / 57.0% (2024) confirmed in Insee Première of 29 May 2026 [I1].
- CICE accounting treatment (section 7.3): confirmed with Insee (2019 APU account): recorded as expenditure; the 2019 switch to contribution cuts cost about 0.9 pp of GDP one-off.
- URLs: all Eurostat databrowser/API links and all OECD SDMX links return HTTP 200. The OECD report URL returns 403 to scripts but loads in a browser (kept, with a note).

**Corrected (correction kept visible in the text):**
1. Section 7.1: the France-Netherlands gap mixed years (gross public 2022 vs net 2021). Same-year 2021 figures give 12.9 pp to 4.9 pp (was 13.7 to 4.9).
2. Section 7.1 / 1.1 / 8: SOCX is superseded by newer partial data. In public gross social expenditure, France is 2nd in 2023 (FIN 30.9 vs FR 30.6) and 3rd in 2024 (AUT 31.6, FIN 31.4, FR 30.6; 24 countries, partly estimates). "France rank 1" holds only up to 2022.
3. Section 2 / reconciliation / section 6: the Insee 2024 PO rate is 42.7% (net of tax credits), not equivalent to the Eurostat/OECD 43.5%. The text now warns against equating 43.5% (2024) with Insee's 43.6% (2025).
4. Section 6: the claim that Insee's PO "adjusts for uncollectable amounts" as a source of difference was removed. D.995 is already deducted in the Eurostat measures. The documented difference is that Insee nets out tax credits.
5. Section 4 point 2: "the difference is the structural deficit" was replaced. That is a technical (cyclically adjusted) concept. The difference is mainly the headline deficit gap (2.8 pp in 2024) plus non-tax revenue.
6. Section 7.3: the CICE statement is now confirmed and sourced (was "from memory").

**Flagged / left unverified:**
- [Resolved in pass 3 below] "Cost of tax cuts since 2017 = several tens of billions of euros per year" (section 7.3): no specific source is given in this file.
- [Resolved in pass 3 below] Item-by-item decomposition of the 0.8 pp gap between Insee PO 2024 (42.7%) and Eurostat/OECD (43.5%).
- Not re-computed independently (the method is consistent and the 2024 end-points match): the 1995-2019 values of the "taxes + social contributions gap" row in section 3.3, the economic-classification rows D.62, D.632, P.2 and P.51g, the COFOG sub-group rows (GF07xx, GF09xx, GF100x other than GF1002), the PPS-derived COFOG per capita rows, and the government final consumption per capita rows.
- The explanation that the 57.0% (`gov_10a_main`) vs 57.3% (COFOG) difference for 2024 reflects data vintages is plausible. The same pattern appears for FI (57.9 vs 57.7) and the EU aggregate (48.9 vs 48.8). It is not documented by Eurostat in what was checked.
- Think-tank orientation: OFCE and IPP orientation was added in 7.3. No Institut Montaigne or Fipeco claims appear in this file.
- Steelman fairness: sections 7.1-7.6 present real counter-arguments with data (net vs gross spending, low GDP per capita denominator, revenue-driven deficit since 2017, outcomes). With the SOCX update, the 7.1 steelman gets stronger: France is no longer the top public social spender in 2023-2024.

### Verification pass 3 (2026-10-25): README §7/§8 follow-up

Scope: the README §8 residual inconsistencies that concern this file (#4, #5) and the two unverified items listed for file 09 in README §7. No Ifop 86%, PISA 2025 or PLF 2027 staffing-plan flag exists in this file (checked by grep), so none had to be removed. New raw downloads are in `research/data/raw/09_pass3/` (Eurostat JSON API, Cour des comptes PDF, Insee pages).

**Inconsistencies fixed (aligned with file 00):**
1. README §8 #4: COFOG 10 social protection 2024 is now **23.6% of GDP** in section 2 row 8 (was 23.7). Recomputed: France EUR amount / current GDP (`gov_10a_exp` 21 Oct 2026, `nama_10_gdp` 22 Oct 2026) = 23.61%; EA21 aggregate 20.00, EU-27 aggregate 19.53; still 2nd of 27 behind FI (26.44). The section 3.1 and panel tables keep the published COFOG ratio (23.7) with the canonical value in brackets; section 6 is relabeled.
2. README §8 #5: COFOG 02 defense 2024 is now **1.8% of GDP** (1.85) in section 2 row 13, as in file 00 row 15 (was 1.9). At current GDP for all countries, France is **8th of 27** (SE 1.95 is above it); the earlier "7th" was a tie at 1.9 in the rounded published table. EA21 1.36, EU-27 1.47.
3. New vintage issue found and labeled (same cause as file 00 log #6): `gov_10a_taxag` % of GDP for France 2024 also uses a pre-May-2026 GDP. At current GDP: broad measure 45.0% (published 45.3), and France is 2nd behind **Belgium** (45.2), not Denmark; measure excluding D.612/D.614 43.3% (published 43.5), still 2nd behind Denmark (44.6). Notes added to section 2 rows 5-6.
4. American spelling: "Defence" → "Defense", "labelled" → "labeled", "channelled" → "channeled", "neighbours" → "neighbors" (dataset titles such as "equivalised" kept as published).

**Formerly unverified items, now resolved:**
- "Cost of tax cuts since 2017 = several tens of billions of euros per year" (section 7.3): **replaced by a verified figure**. Cour des comptes, *La situation et les perspectives des finances publiques* (July 2024), p. 35: "*La période 2018-2023 a été marquée par d'importantes baisses d'impôts, dont l'impact est estimé à 62 Md€ en 2023, soit 2,2 pts de PIB.*" Read in the downloaded PDF (`data/raw/09_pass3/rspfp2024.pdf`), https://www.ccomptes.fr/sites/default/files/2024-09/20240715-RSPFP-2024.pdf. Matches file 00 row 28.
- Item-by-item bridge between Insee PO 2024 (42.7%) and Eurostat/OECD (43.5%): **now bridged to within about 0.1 pp** (section 6). Components: GDP vintage about 0.2 pp (Eurostat amount EUR 1,270.2 bn / current GDP = 43.28%); tax credits recorded as expenditure about 0.66 pp (EUR 19-20 bn, derived from HCFP-2026-5 §80-81 and Table 15: expenditure excluding tax credits of EUR 1,742 bn in 2026, +2.8% in 2026, +2.5% in 2025); residual about +0.1 pp unexplained. Insee's own table note confirms the PO concept: "*hors cotisations sociales imputées et crédit d'impôts*", including the EU share (0.1 pt) (https://www.insee.fr/fr/statistiques/2381412, xlsx `econ-fin-pub-prelev-oblig.xlsx`). The tax-credit amount is derived, not published as such: keep the bridge as an explanation, not as a headline figure.

**Still open:** the 0.1 pp residual of the PO bridge (Insee publishes no official reconciliation); the 2024 broad tax-aggregate rank (2nd behind DK as published vs 2nd behind BE at current GDP) should be re-checked when Eurostat updates the `gov_10a_taxag` ratios (expected with the 2025 data).

---

## Addendum of 2026-10-31: new comparison data (Eurostat COFOG and ESSPROS, ILO, OECD, CEPEJ, ratings)

Scope: data read on 31 October 2026 by three research agents and integrated into `platform/data/figures.json` the same night. All Eurostat series were read live from the dissemination API (`gov_10a_exp` updated 21 Oct 2026; `spr_exp_func` updated 26 Oct 2026; `gov_10a_main` updated 21 Oct 2026). Ranks are computed on the 27 member states (1 = highest; Greece is `EL` in the API). Nothing here replaces the values of file 00; where a value differs from file 00, the difference is flagged.

### A.1 EU-27 aggregates, COFOG (% of GDP, 2024, sector S13, published ratios)

| Function (code) | France (published ratio) | EU-27 | France rank of 27 | Neighbors in the ranking | Panel (DE, IT, ES, NL, BE, SE, DK) |
|---|---|---|---|---|---|
| Old age (GF1002) | 13.4 | **10.6** | 4 | above: IT 13.9; below: EL 11.8 | 9.9, 13.9, 10.4, 6.1, 10.2, 10.9, 7.2 |
| Unemployment (GF1005) | 1.7 | **1.2** | 2, tied with DE at 1.7 | below: FI 1.6 | 1.7, 0.9, 1.5, 0.7, 1.1, 1.1, 1.4 |
| Health (GF07) | 8.9 | **7.3** | 4 | above: HR 9.0 (tie CZ 9.0); below: DK 8.3 | 7.6, 6.6, 6.5, 7.3, 8.0, 7.4, 8.3 |
| Education (GF09) | 5.1 | **4.7** | 11 | above: AT 5.3; below: NL 5.1 (tie at one decimal) | 4.5, 4.0, 4.1, 5.1, 6.3, 7.2, 5.6 |
| Social protection (GF10) | 23.7 (file 00: 23.6 at current GDP) | **19.5** | 2 | above: FI 26.5; below: AT 22.8 | 20.4, 21.3, 18.7, 16.6, 20.4, 19.0, 19.6 |
| Total expenditure (TOTAL) | 57.3 | **48.8** | 2 | above: FI 57.7; below: AT 55.2 | 49.4, 50.4, 45.5, 44.4, 54.1, 50.0, 47.3 |

Caveats:
- The COFOG unemployment rank is not robust at one decimal. FR and DE are tied at 1.7 in the published series; recomputed from MIO_EUR and current GDP, FR 1.653, DE 1.635, FI 1.623 (different GDP vintage). Use the ESSPROS series (A.2) for any unemployment rank.
- Health (HR/CZ) and education (AT/NL) have ties at one decimal; the ranks 4 and 11 are indicative.
- The France values above are the published ratios (older GDP vintage). The canonical France values of file 00 stay 13.4, 8.9, 5.1 and 23.6 (social protection, at current GDP: the published ratio is 23.7). The EU-27 aggregate for social protection is 19.5 in both vintages.

### A.2 ESSPROS (SESPROS) unemployment and old-age benefits (% of GDP, 2024, provisional)

| Function | France | EU-27 | France rank of 27 | Neighbors | Panel (DE, IT, ES, NL, BE, SE, DK) |
|---|---|---|---|---|---|
| Unemployment (UNE) | **1.75** | **1.08** | 1 | below: FI 1.65 (gap 0.10 point); then ES 1.53, AT 1.47, IT 1.21, DE 1.04 | 1.04, 1.21, 1.53, 0.67, 0.94, 0.77, 0.91 |
| Old age (OLD) | **13.0** | **11.32** | 4 | above: FI 14.44 (IT 14.53, AT 14.5); below: SE 12.35 | 10.63, 14.53, 10.58, 9.81, 12.23, 12.35, 10.43 |

Revision to note: the vintage of 26 Oct 2026 differs from the local CSV `research/data/eurostat_spr_exp_func.csv` and from older text (France unemployment 1.76, France old age 13.06, EU-27 old age 11.37). EU-27 unemployment is unchanged at 1.08. The CSV has not been re-downloaded; the API values above prevail.

### A.3 Rank after a measure (static simulation, other countries unchanged)

| Measure | Computed France value | Rank of 27 | Comment |
|---|---|---|---|
| Unemployment benefits (ESSPROS) cut by 10% | 1.75 x 0.90 = 1.575 % of GDP | 2 | behind FI (1.65); above ES (1.53); still 0.5 point above EU-27 (1.08) |
| Unemployment benefits (ESSPROS) cut by 25% | 1.75 x 0.75 = 1.31 % of GDP | 4 | behind FI, ES, AT; above IT (1.21) |
| Old-age expenditure (COFOG) cut by 0.5 point of GDP | 13.4 - 0.5 = 12.9 % of GDP | 4 | still above EL (11.8) |
| Old-age expenditure (COFOG) cut by 1 point of GDP | 13.4 - 1.0 = 12.4 % of GDP | 4 | still above EL (11.8); it would take a cut of more than 1.6 points to fall to 5th |

These are own computations from rounded published ratios, ceteris paribus (the EU average also moves, negligibly).

### A.4 ILO: share of unemployed persons receiving unemployment cash benefits, 2023 (SDG 1.3.1)

Source: ILO, *World Social Protection Report 2024-26*, Figure 4.26 (printed p. 160, PDF p. 186; text p. 159), https://www.ilo.org/sites/default/files/2024-09/WSPR_2024_EN_WEB_0.pdf. Read from the rendered page image. Aggregates are weighted by the number of unemployed. The ILO warns that the estimates are not strictly comparable with the previous edition (do not compare with the 2015 values as published earlier), and that 2023 is still affected by COVID-era transfers, notably in the United States. More than 168 million unemployed receive no benefit.

| Group | 2023 | (2015) |
|---|---|---|
| World | 16.7 | 15.4 |
| High-income countries | 56.1 | 44.0 |
| Europe and Central Asia | 49.1 | 45.3 |
| of which Northern, Southern and Western Europe (France's subregion) | 70.3 | 57.5 |
| Americas | 21.0 | 14.3 |
| of which Northern America | 50.1 | 29.6 |
| Asia and the Pacific | 12.8 | 9.1 |
| of which Eastern Asia (Japan, Korea) | 23.8 | 19.1 |
| Africa | 3.8 | 2.7 |
| Arab States | 1.2 | 2.7 |

France in the country annex (Annex 5.2, printed p. 292, PDF p. 318): 100.0 for 2021. This is a ratio of recipients to unemployed persons capped at 100 (footnote 7), which includes recipients in part-time or reduced activity. Do not present it as "every unemployed person in France is paid". Country values for Italy, Spain, Japan, Korea, the US and the UK were not read reliably and are not recorded.

### A.5 OECD net replacement rates (first month of unemployment)

Source: OECD Tax-Benefit Data Portal, dataflow `DSD_TAXBEN_NRR@DF_NRR` (measure NHIDU), SDMX API, CSV. Case: single person, no children, previous earnings 100% of the average wage, unemployment insurance only (no social assistance, no housing benefit), first month. Values are rounded integers in the source, % of previous net household income.

| Country | 2025 (or latest) | 2024 |
|---|---|---|
| France | **68** | 68 |
| Germany | 60 | 60 |
| Italy | 61 | 64 |
| Spain | 52 | 54 |
| Japan | 59 (2024; 2025 not published) | 59 |
| Korea | 50 | 52 |
| United States | 38 | 33 |
| United Kingdom | 11 | 12 |
| Denmark | 59 (2024; 2025 not published) | 59 |
| OECD average | 55 | 55 |

France is the highest of the ten in the first month. Duration profile (insurance only): France 68 through month 24 then 21; Germany 60 through month 12 then 17; Denmark (2024) 59 then 50 from month 4, 0 after month 24; Spain 52 through month 24, 27 months 25-30; Italy falling from 61 to 29 at month 24, 0 from month 25; Japan (2024) 59 for months 1-9 then 0; Korea 50 for months 1-8, 13 for months 9-14; US 38 for months 1-6 then 0; UK flat 11; OECD average 55, 29 at month 12, 20 at month 24. The model-implied insurance durations are read from these profiles, not from legal texts.

Caveats:
- The OECD profile for France shows 24 months, whereas Unedic rules cap the duration at 18 months for under-55s since 1 Feb 2023 (coefficient 0.75). The OECD model person (long record) apparently does not reflect the coefficient. Do not combine the two as if they were consistent. The France month-25 rate (21) is not recorded as a figure.
- Japan and Korea: the OECD method is the same, so the rate is comparable in construction, but it describes a hypothetical eligible worker. Spells are short and coverage is low (ILO: Eastern Asia 23.8%). The US and UK rates reflect other system designs (low insurance benefit, assistance or tax credits).

### A.6 French unemployment insurance (ARE): maximum duration

Source: Unedic, *Fiche thématique "Durée d'indemnisation"*, February 2023, https://www.unedic.org/storage/uploads/2023/08/29/Dure-dindemnisation_uid_64edabcfa8df4.pdf, and the April 2025 edition, https://www.unedic.org/storage/uploads/2025/06/10/Dure-dindemnisation_uid_6847e575cd5df.pdf; Unedic parameters sheet of April 2026.
- Since 1 Feb 2023 a coefficient of 0.75 applies to the duration: maximum 18 months (548 days) under 53, 22.5 months (685 days) at 53-54, 27 months (822 days) at 55+, floor 6 months (182 days). A supplement of up to 182 / 228 / 273 days (back to 730 / 913 / 1,095 days) applies when the INSEE unemployment rate (ILO definition) is at or above 9%, with rise conditions not read in full.
- The convention of 15 Nov 2024 did not cut the duration further: the 18-month cap and the 0.75 coefficient are unchanged. It raises the age bands by two years (18 months now below 55; 22.5 months at 55-56; 27 months at 57+), lowers the cap on non-worked days from 75% to 70% of worked days and opens the training extension to 55+. The start dates (1 Jan 2025; 1 Apr 2025 for the age thresholds) come from a search summary and are to be confirmed on the Unedic page and on Legifrance.
- Not recorded: the pre-2023 maxima (24 / 30 / 36 months), inferred from the end-of-rights supplement totals and not confirmed on Legifrance (HTTP 403). Suggested wording once confirmed: "durée maximale ramenée de 24 à 18 mois pour les moins de 53 ans en 2023", and describe the 2025 change as an age-threshold increase.

### A.7 Justice and investment

- **CEPEJ disposition time, civil and commercial litigious cases, first instance, 2022:** France 333 days (332.62), Council of Europe median 239.43 days (average 273.29; minimum 58.22 Azerbaijan; maximum 745.84 Greece; states reporting NA are excluded). Source: CEPEJ-STAT, Quantitative Data EN, version 2024.01, data refreshed 14/08/2025, question DT091.2, non-standardized values (Tableau: https://public.tableau.com/views/QuantitativeDataEN/Tables; screenshot in `research/data/raw/cepej/`). France is about 93 days (39%) above the median. Context: Spain 336.74, Italy 539.69, Germany 240.90, Portugal 237.95. Disposition time is a calculated indicator (pending cases at year end / resolved cases x 365), not a measured case duration. Do not confuse the median with the EU Justice Scoreboard "EU median", which reads 239 by coincidence on a different country set.
- **Net public investment 2025 (general government, % of GDP):** gross fixed capital formation (P.51G) minus consumption of fixed capital (P.51C), Eurostat `gov_10a_main` (21 Oct 2026). France 4.4 - 3.8 = about 0.6 (2024: 4.3 - 3.8 = 0.5); euro area (EA20 and EA21 identical) 3.7 - 2.9 = about 0.8 (2024: 0.6). The net figures are computed from inputs rounded to 0.1, so they carry an uncertainty of about 0.1 point (France 0.5-0.7; euro area 0.7-0.9). France's gross investment is above the euro area (+0.7 point) while its consumption of fixed capital is also higher (+0.9 point): the net gap (-0.2 point) is within rounding and must not be presented as a clear under-investment.

### A.8 Sovereign-rating actions confirmed on 31 Oct 2026

Sources: Ministry of the Economy press releases read directly (presse.economie.gouv.fr), and Moody's own release for December 2024. The AFT page remained unreachable (Cloudflare).
- Fitch, 28 Apr 2023: downgrade from AA to AA-, outlook stable (before: negative since 15 May 2020). Ministry release of 29 Apr 2023 (no. 810); Fitch release URL already checked on 25 Oct 2026.
- Fitch, 11 Oct 2024: AA- affirmed, outlook revised from stable to negative (Fitch release, checked on 25 Oct 2026).
- Moody's, 14 Dec 2024: downgrade from Aa2 to Aa3, outlook changed from negative to stable (Moody's release, Frankfurt, 14 Dec 2024; rationale: political fragmentation).
- S&P, 29 Nov 2025 (date of the ministry release; the S&P decision date was not read): A+ maintained, outlook stable (ministry release no. 147).
- Fitch, 6 Mar 2026: A+ maintained, outlook stable (ministry release no. 443).
- Fitch, 28 Aug 2026: A+ maintained, outlook stable (ministry release no. 973; replaces the date-only AFT listing).
- S&P, 29 May 2026: A+ maintained, outlook stable (ministry release no. 725). Next S&P review: 27 Nov 2026.
- Moody's, 23 Oct 2026: Aa3 maintained, outlook negative (ministry release no. 1146; replaces the CNBC-only source).
- **New, after the 25 Oct 2026 base: Fitch, 30 Oct 2026: A+ kept, outlook changed from stable to negative** (ministry release no. 1161; Fitch's own release not read). Every statement in the base that says "Fitch A+ stable" is now out of date (file 06 section 3.4, section 1 summary; chapters citing the three agencies' outlooks).

Not verified and not recorded: S&P 31 May 2024 (AA to AA-, only a parliamentary budget report and wires; S&P's release needs a login); S&P outlook to negative on 28 Feb 2025 (press only; if confirmed, `outlook_before` of S&P 17 Oct 2025 should be negative, not null); Moody's 25 Oct 2024 (Aa2, outlook negative; page not opened).
