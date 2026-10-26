# Social protection in France: risks, amounts, trends, and European comparison

*Research file 02. Compiled 2026-10-25. All figures were checked against the source named in each row. Source codes in square brackets (e.g., [S1]) refer to the full source list at the end. Raw data and computed tables live under `research/data/`.*

---

## 0. Executive summary (for the platform team)

1. **Size.** In 2024 France paid **EUR 932.5 bn of social protection benefits, or 31.9% of GDP** (Drees). Including running costs, total social protection spending was **EUR 982.2 bn (33.6% of GDP)** [S1]. Eurostat's early estimate for **2025 is 32.1% of GDP (EUR 960.6 bn)** [S4]. Drees has not yet published its 2025 figures. They are expected in December 2026. *(Vintage note added 2026-10-25: Drees released semi-final 2024 accounts as open data on 23 Oct 2026, putting 2024 benefits at **EUR 933.2 bn** (was 932.5 bn provisional) [S30]. Divided by the current 2024 GDP (EUR 2,935.2 bn, Eurostat `nama_10_gdp`, 22 Oct 2026), that is **31.8% of GDP**. The published 31.9% (Drees) and 31.96% (Eurostat) use the pre-May-2026 GDP. 31.9% remains the published headline until the Drees 2026 edition.)*
2. **Two risks dominate.** Old age and survivors (mostly pensions) took **45.8%** of benefits and health (sickness, disability and work injury) took **36.3%**, so **82%** of benefits go to these two risks [S1]. Pensions alone cost **EUR 422 bn in 2025 = 14.1% of GDP = 24.3% of all public spending** (COR) [S20].
3. **Europe.** France is **2nd or 3rd in the EU-27 in % of GDP**. It was 2nd in 2024 behind Finland, and the 2025 early estimates put it 3rd behind Austria and Finland. *(Caveat added 2026-10-25: the 2024 rank 2 rests on a 0.05-point lead over Austria (31.96 vs 31.91) computed with France's pre-revision GDP. On current GDP France would be at about 31.8% and 3rd. The website should say "among the top three", with the year.)* Its gap with the EU-27 aggregate is **about 4.5 points of GDP** (31.96% vs 27.41% in 2024; both from Eurostat ESSPROS `spr_exp_func`, 23 Oct 2026; the EU-27 figure is Eurostat's GDP-weighted aggregate, **27.4%** rounded. Drees fiche 12 [S3] shows 27.3% for the EU-27 on its December 2025 vintage. Use 27.4% on the website, as in file 00 row 20) [S4]. **Per inhabitant in purchasing power standards (PPS) it ranks only 7th of 27 (Eurostat ESSPROS benefits, 12,606 PPS, 2024; Drees' France-based PPP gives 9th), below Luxembourg, Austria, Germany, the Netherlands, Denmark and Belgium** (corrected after verification: Luxembourg and Austria were missing from the list) [S4]. Its per-capita lead over the EU average fell from **+27% in 2008 to +14% in 2025** [S4, computed]. This is a key nuance: France's high ratio to GDP partly reflects a comparatively lower GDP per head.
4. **The steelman.** In OECD **net total** social expenditure (after taxes on benefits and including private mandatory and voluntary spending), France ranks **2nd, behind the United States** (32.0% vs 33.2% of GDP in 2021) [S13]. The Netherlands moves from 19.8% gross public to 27.0% net total. **Total resources devoted to social risks differ less across rich countries than public spending does.** The difference lies mostly in *who pays* (taxes and contributions vs private premiums). For the platform's thesis, the argument cuts both ways: a lower public share would mostly mean more private spending, not proportionally lower total costs for households.
5. **Outcomes are mixed.** Old-age poverty is low: **11.6%** at risk of poverty among people 65 and over vs **16.3%** for the EU-27 aggregate (19.5% unweighted mean of countries) (corrected after verification: was "19.5% EU-27 average", which quoted the unweighted mean and overstated the gap), and retirees' living standard is **100.2%** of the population's (2023) [S8, S20]. Out-of-pocket health spending is among the lowest in the EU (**10.2%** of current health spending, 3rd lowest) [S11]. Life expectancy at birth is **83.0 years** (7th in the EU) [S10]. Yet the **headline poverty rate (16.3%) is close to the EU average (rank 17/27)**, **child poverty (22.8%) is among the worst in the EU (rank 22-23/27, tied with Greece; corrected after verification: was "22/27")**, and **healthy life years at birth (63.6) are mid-table (15/26)** [S8, S10].
6. **Social security deficit.** The deficit of the basic schemes plus FSV was **-EUR 21.6 bn in 2025 (-0.7% of GDP)**. Before PLFSS 2027 measures it is projected at **-21.0 bn in 2026 and -22.6 bn in 2027** (CCSS, October 2026). The health branch is the main contributor (**-15.9 bn in 2025**) [S14]. PLFSS 2027 targets **-12.7 bn** in 2027 [S15]. **CADES still had EUR 121.7 bn to amortize at end-2025, plus EUR 40.4 bn of social debt carried elsewhere (mostly by ACOSS)** [S14].

---

## 1. Scope and definitions

| Concept | Definition | Who publishes | Key caveat |
|---|---|---|---|
| *Comptes de la protection sociale* (CPS, social protection accounts) | All public **and private** schemes covering six risks: old age-survivors, health, family, employment, housing, poverty-social exclusion. Includes compulsory supplementary schemes (Agirc-Arrco), *mutuelles* (mutual health insurers), employer schemes, *départements* (county-level social aid), and so on. | Drees, consistent with Eurostat ESSPROS | Not a subset of general government (APU) spending. Some private schemes are inside, and some public spending (e.g., education) is outside. |
| *Prestations de protection sociale* (social benefits) | Cash and in-kind transfers to households under the six risks, excluding administrative costs | Drees / Eurostat ESSPROS | "Total expenditure" = benefits + administrative and other costs (EUR 982.2 bn vs 932.5 bn in 2024) [S1] |
| ESSPROS functions | Sickness/health care (SICK), disability (DIS), old age (OLD), survivors (SRV), family/children (FAM), unemployment (UNE), housing (HOU), social exclusion n.e.c. (EXCL) | Eurostat (`spr_exp_func`) | Drees's French grouping differs slightly. Drees "health" = SICK + DIS + work injury. Drees "employment" = UNE + vocational reintegration. |
| COFOG GF10 "Social protection" | General government spending by function (ESA 2010). **Health is a separate function (GF07)** | Eurostat `gov_10a_exp`, Insee | Excludes private schemes. Most health care is in GF07, not GF10. |
| D.62 + D.632 (national accounts) | Social benefits other than social transfers in kind (cash) + social transfers in kind purchased market production | Insee / Eurostat `gov_10a_main` | General government only |
| OECD SOCX | Gross public, mandatory private, voluntary private, and **net total** (after direct and indirect taxes on benefits and tax breaks for social purposes) | OECD | Net figures are published only every two years and lag (latest: 2021) |
| *Régimes obligatoires de base de sécurité sociale* (ROBSS) + FSV | Basic compulsory social security schemes (health, work injury, pensions, family, autonomy) + old-age solidarity fund (abolished 1 January 2026, absorbed by CNAV) | DSS / CCSS, PLFSS | Narrower than CPS: excludes Agirc-Arrco, Unédic, *départements* and others. |
| ONDAM | *Objectif national de dépenses d'assurance maladie* (national health insurance spending target) voted each year in the LFSS | DSS / CCSS | Covers basic-scheme health spending only |
| CSBM / DCSi | *Consommation de soins et de biens médicaux* (consumption of medical care and goods) / *dépense courante de santé au sens international* (current health expenditure, SHA international definition) | Drees health accounts | DCSi = CSBM + long-term care + prevention + administration |

**Rule used throughout:** every ratio is labeled **"% of GDP"** or **"% of total public expenditure (TPE)"** or **"% of total benefits"**. These are three different denominators.

---

## 2. Key figures table

| # | Indicator | Value | Unit / denominator | Data year | Source |
|---|---|---|---|---|---|
| 1 | Social protection benefits (all schemes) | 932.5 | EUR bn | 2024 | Drees CPS ed. 2025 [S1] |
| 2 | Same, as share of GDP | 31.9 | % of GDP | 2024 | [S1] |
| 3 | Total social protection spending (benefits + costs) | 982.2 (33.6% of GDP) | EUR bn | 2024 | [S1] |
| 4 | Benefits per inhabitant | 13,650 | EUR per head | 2024 | [S1] |
| 5 | Benefits, Eurostat early estimate | 960.6 (32.12% of GDP) | EUR bn | 2025 (e) | Eurostat `spr_exp_func` [S4] |
| 6 | Old age-survivors benefits | 426.7 (45.8% of benefits; about 14.6% of GDP) | EUR bn | 2024 | [S1] (GDP share from [S1] chart 3) |
| 7 | Health benefits (sickness + disability + work injury) | 338.9 (36.3% of benefits; about 11.6% of GDP) | EUR bn | 2024 | [S1] |
| 8 | Pension spending (all schemes, COR scope) | 422 = 14.1% of GDP = 24.3% of TPE | EUR bn | 2025 | COR June 2026 [S20] |
| 9 | General government total expenditure (TPE) | 1,714.1 = 57.3% of GDP | EUR bn | 2025 | Eurostat `gov_10a_main` (Insee-transmitted) [S7] |
| 10 | General government cash social benefits (D.62) | 580.9 = 19.4% of GDP = 33.9% of TPE | EUR bn | 2025 | [S7], computed share |
| 11 | General government social transfers in kind purchased (D.632) | 190.1 = 6.4% of GDP = 11.1% of TPE | EUR bn | 2025 | [S7], computed share |
| 12 | COFOG social protection (GF10) | **23.6% of GDP** at current GDP (41.5% of TPE; EUR 693 bn) (corrected 2026-10-25: was 23.7%, the ratio Eurostat's COFOG table computes on a pre-May-2026 GDP; aligned with file 00 row 11) | % | 2024 | Eurostat `gov_10a_exp` [S6] |
| 13 | COFOG health (GF07) | 8.9% of GDP (15.6% of TPE; corrected after verification: was "about 15.5%") | % | 2024 | [S6] |
| 14 | Resources: social contributions (excl. CSG) | 554.4 = 55.6% of resources | EUR bn | 2024 | [S1] |
| 15 | Resources: earmarked taxes (*Itaf*, mostly CSG and VAT) | 299.4 = 30.0% of resources | EUR bn | 2024 | [S1, S2] |
| 16 | Resources: public contributions (state budget) | 126.9 = 12.7% of resources | EUR bn | 2024 | [S1, S2] |
| 17 | France rank, benefits % GDP, EU-27 | 2nd (2024 p; 0.05 pt ahead of Austria, see §0 item 3 caveat), 3rd (2025 e) | rank | 2024/2025 | [S4], computed |
| 18 | France rank, benefits PPS per head, EU-27 | 7th (12,606 PPS vs EU-27 10,974) | rank | 2024 p | [S4], computed |
| 19 | OECD net total social expenditure | 31.95% (rank 2/38; USA 33.24%) | % of GDP | 2021 | OECD SOCX [S13] |
| 20 | Current health expenditure (DCSi) | 353.2 = 11.8% of GDP | EUR bn | 2025 | Drees health accounts ed. 2026 [S16] |
| 21 | CSBM | 256.5 = 8.6% of GDP | EUR bn | 2025 | [S16] |
| 22 | Household out-of-pocket (share of DCSi) | 9.7% (EUR 495 per head) | % | 2025 | [S16] |
| 23 | ONDAM executed | 265.4 (+3.4%) | EUR bn | 2025 | CCSS Oct. 2026 [S14] |
| 24 | ONDAM forecast | 273.3 (+2.8%) | EUR bn | 2026 | [S14] |
| 25 | Basic schemes + FSV balance | -21.6 (-0.7% of GDP) | EUR bn | 2025 | [S14] |
| 26 | Same, pre-PLFSS forecast | -21.0 (2026), -22.6 (2027) | EUR bn | 2026-27 | [S14] |
| 27 | PLFSS 2027 deficit target | -12.7 | EUR bn | 2027 | Cour des comptes 20 Oct. 2026 [S15] |
| 28 | CADES debt remaining to amortize | 121.7 | EUR bn | end-2025 | [S14] |
| 29 | Unédic debt | 61.5 | EUR bn | end-2026 (f) | Unédic Oct. 2026 [S18] |
| 30 | Minimum income (*minima sociaux*) spending | 33.3 = 1.1% of GDP | EUR bn | 2024 | Drees MS ed. 2025 [S17] |
| 31 | *Minima sociaux* recipients | 4.25 million | persons | end-2024 | [S17] |
| 32 | At-risk-of-poverty rate (60% median, EU-SILC) | 16.3% (EU-27: 16.3%) | % of population | SILC 2025 | Eurostat `ilc_li02` [S8] |
| 33 | Same, before social transfers (pensions counted as income) | 26.5% | % | SILC 2025 | `ilc_li10` [S8] |
| 34 | Child (<18) at-risk-of-poverty rate | 22.8% (EU-27: 19.6%; rank 22-23/27, tied with Greece; corrected after verification: was "rank 22/27") | % | SILC 2025 | [S8] |
| 35 | Insee monetary poverty rate (ERFS) | 15.4% (9.8 m people) | % | 2024 | Insee Première 2117 [S21] |

*Check of the user's starting figures:* (a) **Public expenditure 2025 = EUR 1,714.1 bn = 57.3% of GDP: confirmed** (Eurostat `gov_10a_main`, updated 2026-10-21, which carries Insee's transmission) [S7]. (b) **Social protection benefits 2024 = 31.9% of GDP: confirmed** (Drees, published 2025-12-18) [S1]. (c) **Compulsory levies 2025 = 43.6% of GDP: not checked in this file** (outside the social protection scope; see the taxation file).

---

## 3. Social protection benefits by risk (Drees CPS)

### 3.1 Latest edition and timing

- **Latest published edition:** *La protection sociale en France et en Europe en 2024 - Résultats des comptes de la protection sociale - Édition 2025*, published **18 December 2025** [S1]. PDF chapters were re-uploaded in March and May 2026. The text is unchanged and still reads "Édition 2025".
- **The 2026 edition (2025 data) has not been published as of 2026-10-25.** Based on the usual calendar it is expected in December 2026. For 2025, only **Eurostat's early estimate** (from Drees transmission) exists: **32.12% of GDP, EUR 960.6 bn** [S4].

### 3.2 Benefits by risk, 2019-2024 (EUR bn, current)

| Risk | 2019 | 2020 | 2021 | 2022 | 2023 | 2024 | Growth 2024/23 | Share 2024 | ≈ % of GDP 2024* | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| **Old age-survivors** | 351.9 | 359.5 | 365.4 | 381.7 | 400.7 | **426.7** | +6.5% | 45.8% | 14.6 | [S1] |
| of which old age | 311.9 | 319.6 | 325.2 | 340.3 | 357.6 | 381.6 | +6.7% | 40.9% | 13.0 | [S1] |
| of which survivors | 40.0 | 39.9 | 40.2 | 41.4 | 43.1 | 45.1 | +4.7% | 4.8% | 1.5 | [S1] |
| **Health** | 265.5 | 278.1 | 305.0 | 315.0 | 325.7 | **338.9** | +4.0% | 36.3% | 11.6 | [S1] |
| of which sickness | 215.4 | 226.7 | 252.8 | 260.2 | 267.7 | 277.9 | +3.8% | 29.8% | 9.5 | [S1, S2] |
| of which disability | 43.4 | 44.9 | 45.8 | 48.2 | 51.2 | 53.8 | +5.2% | 5.8% | 1.8 | [S1] |
| of which work injury (AT-MP) | 6.8 | 6.5 | 6.5 | 6.6 | 6.9 | 7.2 | +4.2% | 0.8% | 0.25 | [S1] |
| **Family** | 56.8 | 58.5 | 57.2 | 59.4 | 62.9 | **65.8** | +4.7% | 7.1% | 2.3 | [S1] |
| **Employment** | 47.1 | 74.1 | 61.4 | 47.7 | 49.3 | **51.1** | +3.8% | 5.5% | 1.8 | [S1] |
| of which unemployment | 42.3 | 69.2 | 55.3 | 41.5 | 43.3 | 45.6 | +5.2% | 4.9% | 1.6 | [S1] |
| of which vocational (re)integration | 4.9 | 4.9 | 6.2 | 6.2 | 5.9 | 5.6 | -6.2% | 0.6% | 0.2 | [S1] |
| **Housing** | 16.9 | 16.8 | 15.8 | 15.6 | 15.8 | **16.1** | +1.9% | 1.7% | 0.5 | [S1] |
| **Poverty-social exclusion** | 30.8 | 34.9 | 36.7 | 34.9 | 35.2 | **34.0** | -3.3% | 3.6% | 1.2 | [S1] |
| **Total benefits** | **769.1** | **821.9** | **841.6** | **854.2** | **889.5** | **932.5** | **+4.8%** | 100% | **31.9** | [S1] |

\* % of GDP = share of benefits × 31.9%, cross-checked against Drees chart 3 (old age-survivors 14.6; health 11.6; family 2.3; employment 1.8; housing 0.5; poverty 1.2) [S1, S2].

**Drivers (Drees) [S1]:** 2024 growth was driven by pension indexation (+5.3% average revaluation, a lagged effect of 2023 inflation). In health, it was driven by higher physicians' fees (late-2023 agreements) and costly innovative medicines. The poverty-exclusion risk fell (-3.3%) because the exceptional *chèque énergie* (energy voucher) and the fuel aid were discontinued. Family benefits rose despite fewer births because of indexation and childcare benefits.

### 3.3 Long-run series (share of GDP)

| Year | Benefits, % of GDP (France) | Note | Source |
|---|---|---|---|
| 1959 | 14.8 | Benefits roughly doubled as a share of GDP since then | Drees fiche 02 [S2] |
| 1995 | 28.6 | ESSPROS series | Eurostat [S4] |
| 2000 | 27.5 | | [S4] |
| 2005 | 29.2 | | [S4] |
| 2008 | 28.9 | Last pre-crisis year (corrected after verification: was "Pre-financial-crisis low"; 2007 was lower at 28.6 and 2000 at 27.5) | [S4] |
| 2009 | 31.2 | "Step" increase in a recession | [S4] |
| 2015 | 32.1 | | [S4] |
| 2019 | 31.6 | | [S1, S4] |
| 2020 | 35.5 | COVID peak (GDP -7.4%) | [S1, S2] |
| 2021 | 33.6 | | [S2] |
| 2022 | 32.2 | | [S1] |
| 2023 | 31.5 | | [S1] |
| 2024 | 31.9 | First increase since 2020 | [S1] |
| 2025 (e) | 32.1 | Eurostat early estimate | [S4] |

Full ESSPROS series 1995-2025 by function: `research/data/eurostat_spr_exp_func.csv`.

**Long-run dynamics (Drees fiche 02) [S2]:**
- Real benefits (constant 2024 euros) were multiplied by about 12 between 1959 and 2024, from EUR 71 bn to EUR 825 bn. Real GDP rose about 6-fold over the period, and the GDP share doubled.
- Average real growth slowed: **6.9%/year (1959-1981) → 2.8% (1981-2007) → 1.9% (2007-2019)**, then +2.7%/year (2019-2021) and -0.4%/year after.
- The share of old age-survivors + health rose from **68% (1959) to 82% (2024)** of benefits. Real growth was +4.2%/year for old age-survivors and +4.0%/year for health. Family was the slowest (+1.6%/year), and poverty-exclusion the fastest (+7.0%/year, driven by RMI in 1988, then RSA in 2009 and *prime d'activité* in 2016).
- The share of GDP rises in "steps" during recessions (1975, 1993, 2009) and does not fall back afterwards. 2020 was the exception: the ratio returned to its 2019 level by 2022.
- Five pension reforms (1993, 2003, 2008, 2010, 2023) slowed but did not reverse the trend.

### 3.4 Funding structure

| Resource (excluding internal transfers) | 2024 EUR bn | Share 2024 | Share 1959 | Growth 24/23 | Source |
|---|---|---|---|---|---|
| Social contributions (*cotisations*, excl. CSG) | 554.4 | 55.6% | 77.8% | +4.6% | [S1, S2] |
| Earmarked taxes (*Itaf*: CSG, VAT share, tobacco, etc.) | 299.4 | 30.0% | ≈0 (3.4% in 1990) | +3.5% | [S1, S2] |
| Public contributions (state budget) | 126.9 | 12.7% | 17.7% | +1.5% | [S1, S2] |
| Other resources | 17.0 | 1.7% | n.a. | +6.9% | [S1] |
| **Total resources** | **997.8** | 100% | | +3.9% | [S1] |

*Reading:* Since the CSG was created in 1991 and contribution cuts on low wages started in 1993, financing has shifted from wage contributions to taxes. In 2018-2019, contribution cuts (end of the CICE tax credit) were compensated by more CSG and VAT [S2]. Drees warns that the overall balance is "not interpretable" at the level of all schemes [S1].

**Eurostat comparison of financing (ESSPROS receipts, `spr_rec_sumt`) [S5], 2024:**

| Receipt type, % of total receipts | France | EU-27 | Source |
|---|---|---|---|
| Social contributions (total) | 55.1 | 55.8 | [S5] |
| of which employers | 39.1 | 35.0 | [S5] |
| of which protected persons | 16.0 | 20.8 | [S5] |
| General government contributions | 42.9 | 41.0 | [S5] |
| of which earmarked taxes | **30.0** | **6.3** | [S5] |
| of which general revenue | 13.0 | 34.6 | [S5] |
| Other receipts | 2.0 | 3.3 | [S5] |
| Total receipts, % of GDP (France) | 34.5 | n.a. | [S5] |

France's distinctive feature is its heavy use of **earmarked taxes** (CSG, VAT share), not general taxation. Employers also pay a larger share than in the EU average.

---

## 4. Health

### 4.1 Health accounts 2025 (Drees, edition 2026)

Drees, *Les dépenses de santé en 2025 - Résultats des comptes de la santé - Édition 2026* (PDF dated 2026-09-30; reported in the press on 2026-10-06) [S16].

| Component | 2015 | 2021 | 2022 | 2023 | 2024 | 2025 | Growth 2025 | Share of DCSi 2025 | Source |
|---|---|---|---|---|---|---|---|---|---|
| Hospital care | 85.6 | 105.9 | 110.5 | 117.5 | 120.7 | **124.1** | +2.8% | 35.1% | [S16] |
| - public hospitals | 67.0 | 81.7 | 85.5 | 91.0 | 93.5 | 96.2 | +2.9% | 27.2% | [S16] |
| - private hospitals | 18.6 | 24.2 | 25.0 | 26.5 | 27.2 | 27.9 | +2.6% | 7.9% | [S16] |
| Ambulatory care | 54.2 | 64.6 | 67.0 | 70.2 | 73.2 | **75.4** | +3.0% | 21.3% | [S16] |
| - routine outpatient care | 41.1 | 49.4 | 51.3 | 53.3 | 55.8 | 57.9 | +3.7% | 16.4% | [S16] |
| - labs, imaging, transport | 13.0 | 15.2 | 15.8 | 16.9 | 17.4 | 17.5 | +1.0% | 5.0% | [S16] |
| Medical goods | 46.3 | 50.6 | 52.3 | 53.7 | 55.8 | **56.9** | +2.0% | 16.1% | [S16] |
| - outpatient medicines | 31.1 | 30.9 | 32.3 | 33.2 | 34.5 | **34.9** | +1.3% | 9.9% | [S16] |
| - medical devices | 15.2 | 19.7 | 20.0 | 20.5 | 21.3 | 22.0 | +3.1% | 6.2% | [S16] |
| **CSBM** | 186.1 | 221.1 | 229.9 | 241.3 | 249.7 | **256.5** | +2.7% | 72.6% | [S16] |
| CSBM, % of GDP | 8.5 | 8.8 | 8.7 | 8.5 | 8.5 | **8.6** | | | [S16] |
| Long-term care | 44.6 | 57.4 | 59.7 | 64.2 | 66.8 | **69.9** | +4.7% | 19.8% | [S16] |
| Prevention | 6.0 | 17.6 | 13.4 | 8.7 | 8.6 | 9.2 | +6.8% | 2.6% | [S16] |
| System administration | 14.9 | 15.5 | 15.8 | 16.2 | 17.0 | 17.6 | +3.8% | 5.0% | [S16] |
| **DCSi** | 251.5 | 311.5 | 318.7 | 330.4 | 342.0 | **353.2** | +3.3% | 100% | [S16] |
| DCSi, % of GDP | 11.4 | 12.4 | 12.0 | 11.7 | 11.7 | **11.8** | | | [S16] |

### 4.2 Who pays (2025, EUR bn) [S16]

| Payer | CSBM | DCSi | Share of DCSi | Source |
|---|---|---|---|---|
| *Sécurité sociale* | 201.6 | 249.2 | 70.6% | [S16] |
| Central and local government | 1.7 | 24.3 | 6.9% | [S16] |
| (General government total) | 203.3 (79% of CSBM) | 273.5 | **77.4%** | [S16] |
| Complementary insurers (*organismes complémentaires*, OC) | 33.5 | 43.4 | **12.3%** | [S16] |
| Households (out-of-pocket) | 19.7 (**7.7% of CSBM**) | 34.1 | **9.7%** | [S16] |
| Firms | 0 | 2.2 | 0.6% | [S16] |

- Out-of-pocket = **EUR 495 per head** in 2025: long-term care EUR 207, outpatient care 112, medicines 67, devices 52 (Drees as reported by Hospitalia) [S16b].
- Public coverage by category: hospitals 94%, routine outpatient care 62% (GPs 79%, psychologists 7%), medicines 76%, devices 45% [S16].
- **EU comparison (Drees, 2024):** public financing 74.3% EU vs 77.4% France. Household out-of-pocket is **14.8% EU vs 9.7% France**. Complementary insurers pay 10.9% EU vs 12.3% France [S16].
- **Eurostat SHA (`hlth_sha11_hf`) 2024:** household out-of-pocket (HF3) = **10.17% of current health expenditure in France, 3rd lowest in the EU-27** after Croatia (8.6%) and Luxembourg (8.75%). The EU-27 aggregate is 15.06%, the unweighted mean 19.3% and the median 16.9% [S11, computed]. Panel: DE 11.1, NL 11.85, SE 12.83, DK 14.61, ES 21.47, BE 21.78, IT 22.98 [S11].
- **Total health spending, Eurostat 2024:** France 11.33% of GDP (EU aggregate 10.16%) and **4,491 PPS per head (EU-27 4,075)**, below DE 5,791, NL 5,254, BE 4,892 and SE 4,777, and about equal to DK 4,471 [S11].

### 4.3 ONDAM 2025-2027 [S14]

| Year | Amount (EUR bn) | Growth (constant scope) | Status | Source |
|---|---|---|---|---|
| 2025 | 265.4 | +3.4% | Executed. 0.5 bn under the LFSS 2025 target (265.9) | CCSS Oct. 2026 [S14] |
| 2026 | 273.3 | +2.8% | Forecast. 1.1 bn under the LFSS 2026 target (274.4): 0.9 bn of in-year savings (0.6 bn of frozen reserves + 0.3 bn of mid-year savings: cap on co-payments/deductibles raised to EUR 70/yr; lower AT-MP daily-allowance ceiling) plus 0.2 bn of lower spontaneous growth (completed after verification) | [S14] |
| 2027 (trend, before measures) | n.a. | +3.4% (spontaneous growth +3.6%) | Before PLFSS 2027 measures | [S14] |
| 2027 (PLFSS target) | **278.7** (soins de ville 118.3; établissements de santé 116.0; elderly-care facilities 18.8; disability facilities 16.3; FIR 5.9; other 3.4) | **+2.0%** at constant scope, vs a trend of +3.4% | Bill under debate (first reading, Oct. 2026) | **Confirmed 2026-10-25 in the bill itself:** PLFSS 2027, AN text n° 3211 (tabled 1 Oct 2026), Article 43 and its *exposé des motifs* [S25]. Tripalio's "+2.1%" is wrong; the bill says 2.0% (was: "278.7 (press)", flagged unverified). 2026 rectified ONDAM 273.3 bn also confirmed (Article 2) |

- Sensitivity: **+1% of ONDAM = EUR 2.65 bn** on the balance (based on 2025 spending) [S14].
- PLFSS 2027 ONDAM savings: **EUR 3.9 bn** (Cour des comptes) [S15]. The press reports 5.1 bn of health "savings" including 2.1 bn on medicines and devices [S23]. **Reconciled after verification:** Caducée (citing the PLFSS) states that the 5.1 bn of gross savings finance 1.2 bn of new spending, for a **net 3.9 bn** reduction relative to the trend, which is the Cour des comptes figure.
- ONDAM was regularly exceeded until 2009, then respected from 2010 until COVID [S2].

### 4.4 Health insurance (CNAM) deficit [S14]

| Health branch (all basic schemes) | 2024 | 2025 | 2026 (f) | 2027 (f, pre-PLFSS) | Source |
|---|---|---|---|---|---|
| Balance, EUR bn | -13.8 | **-15.9** | -11.7 | -13.8 | CCSS Oct. 2026 [S14] |

The 2026 improvement relies on **EUR 8.1 bn of net new revenue measures** (e.g., 0.65 pt of CSG reallocated, EUR 1.1 bn exceptional levy on complementary insurers, higher payroll-tax share). "Without these new measures, the health branch deficit would widen by as much" [S14].

---

## 5. Family, unemployment, minimum incomes, housing

### 5.1 Family policy

| Indicator | Value | Year | Source |
|---|---|---|---|
| Family risk benefits (CPS) | EUR 65.8 bn = 7.1% of benefits ≈ 2.3% of GDP | 2024 | [S1] |
| ESSPROS family/children, France vs EU-27 aggregate | **2.24% vs 2.41% of GDP**: France now **below** the EU average, rank 9/27 | 2024 p | [S4] |
| Same, 2005 | 2.66% (rank 7/26 on unweighted comparison) | 2005 | [S4] |
| CNAF (family branch) balance | +1.1 bn (2024), +1.2 bn (2025), +0.3 bn (2026 f), +2.1 bn (2027 f) | | [S14] |
| Legal family benefits | +1.1% in 2025; -0.2% forecast for 2026 and 2027 despite indexation, because of falling births (-6.6% in 2023, -2.5% in 2024, -2.4% in 2025) | | [S14] |
| Total fertility rate, France | 1.61 (EU-27: 1.34). **Rank 2/27** (1.94 and rank 1 in 2005) | 2024 | Eurostat `demo_find` [S12] |

*Reading:* France's family spending is no longer exceptional in the EU (Germany 3.59% and Poland 3.72% of GDP spend more) [S4]. Fertility remains among the highest in the EU but has fallen sharply. The *quotient familial* (family tax splitting), a tax expenditure, is **not** counted in ESSPROS or CPS benefits. Its cost was not checked here (see gaps).

### 5.2 Unemployment insurance (Unédic)

| Indicator | Value | Year | Source |
|---|---|---|---|
| Unemployment benefits (CPS) | EUR 45.6 bn (4.9% of benefits) | 2024 | [S1] |
| ESSPROS unemployment, % of GDP | **1.76 (EU-27 aggregate 1.08) - rank 1/27**. Also 1st in PPS per head (693 vs 434) | 2024 p | [S4] |
| Unédic balance | **-2.3 bn** (would be +1.8 bn without state levies) | 2026 f | Unédic, published 2026-10-21 [S18] |
| Unédic balance | +1.4 bn before any new state levy. The press reports about -0.6 bn if the about EUR 2 bn levy announced in PLF 2027 is kept | 2027 f | [S18]; press [S18b] |
| Unédic debt | 61.5 (end-2026), 60.1 (end-2027), 57.7 (end-2028) | EUR bn | [S18] |
| Debt without 2023-2026 state levies | 45.7 (end-2028) | EUR bn | [S18] |
| Cumulative state levies since 2023 | about 12 bn (Unédic chair). About 14 bn including the newly announced 2 bn (press) | EUR bn | [S18, S18b] |
| Revenue / spending | 44.3 / 46.6 | EUR bn, 2026 | [S18] |
| Contribution to France Travail | 5.2 bn in 2026: 11% of Unédic revenue of year n-2 before state levies, or 11.6% of the effective 2024 revenue after levies; 12% by 2028 (corrected after verification: was "11.6% of revenue", without the n-2 basis) | 2026 | [S18] |
| Indemnified jobseekers | about 2.6 million, stable to 2028 | 2026-28 | [S18] |

**Reforms 2019-2025 (summary):**
- **2019-2021 reform** (decrees 2019, effective in stages to late 2021): longer qualifying period (6 months worked in 24), a new reference-wage calculation that penalizes fragmented work, benefit degressivity for high earners, and a *bonus-malus* on employer contributions in sectors using short contracts. Unédic found that the reform lowered the average monthly allowance (the press cites -16% on average for those affected) [S19].
- **2023 "contracyclicality" reform** (decree 2023-33, effective 1 February 2023): **-25% on all potential benefit durations** when the labor market is "favorable" (minimum 6 months), plus an end-of-rights supplement if conditions worsen. Unédic's ex ante estimate is **about EUR 4.5 bn/year at full effect (2027)**, "the reform with the largest financial impact of the past ten years" [S19].
- **2024 convention** (applied from 2025): changes for seniors and other parameters. The **2026 amendment** covers *ruptures conventionnelles* (negotiated separations) [S18]. Their effects were not quantified on the page consulted.

### 5.3 Minimum incomes (*minima sociaux*) and in-work benefit

| Benefit | Recipients | Spending | Year | Source |
|---|---|---|---|---|
| All 11 *minima sociaux* | **4.25 m** (end-2024, +1.3%); 6.9 m people covered incl. families (end-2023) | **EUR 33.3 bn = 1.1% of GDP** (2024; +3.2% in real terms) | 2024 | Drees MS ed. 2025 (published 2025-12-04) [S17] |
| RSA (*revenu de solidarité active*, minimum income) | 1.84 m (end-2024, -0.5%) | EUR 12.2 bn (2023) = 0.4% of GDP | 2024 / 2023 | [S17] |
| AAH (*allocation aux adultes handicapés*, disabled adults' allowance) | 1.40 m (end-2024, +3.3%) | EUR 12.7 bn (2023), larger than RSA since 2022 | 2024 / 2023 | [S17] |
| *Minimum vieillesse* (ASPA/ASV, old-age minimum) | 754,500 (end-2024, +4.3%) | EUR 4.1 bn (2023) | 2024 / 2023 | [S17] |
| ASS (*allocation de solidarité spécifique*, unemployment assistance) | 253,100 (end-2023); **265,000 (end-2024, +4.7%)** (added after verification, from the Drees landing page) | EUR 1.7 bn (2023) | 2023 / 2024 | [S17] |
| *Prime d'activité* (in-work benefit; not a minimum income) | **4.81 m households** (end-2024); 9.02 m people covered (end-2023) | **EUR 10.5 bn** (2023) | 2024 / 2023 | [S17] |

Monthly amount for a single person (April 2025 scale): *prime d'activité* lump sum EUR 633.21 [S17]. Drees fiche 08 gives the April 2025 scale: RSA EUR 646.52, AAH about EUR 1,033, ASPA about EUR 1,034 [S26].

**2026 amounts, single person, maximum (verified 2026-10-25; was "not verified against an official source"):**
- **RSA (*montant forfaitaire*): EUR 651.69/month from 1 April 2026** (+0.8%). Source: *Décret n° 2026-220 du 30 mars 2026*, JORF n° 0077 of 31 March 2026, Article 1 [S27].
- **AAH (full rate): EUR 1,041.59/month** (April 2026 revaluation; 1,033.32 x 1.008). Source: service-public.gouv.fr (official government portal, DILA), page F12242, checked 14 Sep 2026 [S28]. No dedicated decree: the AAH is revalued by the statutory coefficient (art. L. 161-25 CSS).
- **ASPA (*minimum vieillesse*): EUR 1,043.59/month (EUR 12,523.14/year) from 1 January 2026** (+0.9%). Source: service-public.gouv.fr page F16871 (checked 23 Jun 2026), citing Cnav circular 2025-29 of 22 Dec 2025 [S28].

**Order of magnitude to keep in mind:** RSA (12 bn) is **about 3% of pension spending (422 bn)** and **about 1.3% of all social benefits**. All *minima sociaux* combined (33 bn) equal **about 3.6% of social benefits** and **about 2% of general government spending** (Drees) [S17]. *(Clarified after verification: Drees fiche 07 computes these ratios on **2023** spending, EUR 31.6 bn = 1.1% of GDP = 3.6% of social protection benefits = 2.0% of general government spending. The 2024 total of 33.3 bn gives about 3.6% of 2024 benefits, so the ratio holds.)*

### 5.4 Housing benefits (APL, ALF, ALS)

| Indicator | Value | Year | Source |
|---|---|---|---|
| Households receiving housing benefit | **5.8 m** (Dec. 2024, -1.1%); 5.9 m end-2023 | 2024 | [S17] |
| People living in a recipient household | 11.2 m (about 16% of the population) | end-2023 | [S17] |
| Spending on APL+ALF+ALS | **EUR 15.6 bn** (average EUR 226/month); -3.3% in real terms vs 2022 | 2023 | [S17] |
| CPS housing risk (incl. other aids) | EUR 16.1 bn (+1.9%) after 6 years of decline | 2024 | [S1] |
| ESSPROS housing, % of GDP | 0.55 vs EU-27 0.37 (rank 5/27; 1st in 2005 at 0.80) | 2024 p | [S4] |

The decline since 2017 reflects the *réduction de loyer de solidarité* (RLS, a rent cut imposed on social landlords, offset by lower APL), the end of aid for new home-buyers (2018), and the switch to contemporaneous income assessment (2021) [S1, S17].

---

## 6. Social security accounts (CCSS October 2026, PLFSS 2027)

### 6.1 Balances by branch (EUR bn) [S14]

*Source:* Rapport à la Commission des comptes de la Sécurité sociale, "Résultats 2025 - Prévisions 2026 et 2027", October 2026 (PLFSS 2027 tabled 1 October 2026). Forecasts are **before** PLFSS 2027 measures. *Note:* the table was reconstructed from the PDF layout and cross-checked against the report's text and arithmetic (branch totals add up to the general scheme to within 0.1).

| Scheme / branch | 2024 | 2025 | 2026 (f) | 2027 (f) | Source |
|---|---|---|---|---|---|
| **General scheme (*régime général*)** | -14.4 | -21.4 | -20.8 | -22.9 | [S14] |
| Health (CNAM maladie) | -13.8 | **-15.9** | -11.7 | -13.8 | [S14] |
| Work injury (CNAM AT-MP) | +0.7 | -0.2 | -1.3 | -2.2 | [S14] |
| Old age (CNAV) | -3.6 | -6.6 | -7.9 | -8.9 | [S14] |
| Family (CNAF) | +1.1 | +1.2 | +0.3 | +2.1 | [S14] |
| Autonomy (CNSA) | +1.3 | +0.1 | -0.3 | -0.1 | [S14] |
| Local and hospital civil servants' pensions (CNRACL) | -3.0 | -2.3 | -1.4 | -1.1 | [S14] |
| All basic schemes | -16.4 | -22.0 | -21.0 | -22.6 | [S14] |
| FSV (abolished 1 Jan. 2026) | +1.1 | +0.4 | - | - | [S14] |
| **Basic schemes + FSV** | **-15.3** | **-21.6** | **-21.0** | **-22.6** | [S14] |
| % of GDP | -0.5 | -0.7 | -0.7 | -0.7 | [S14] |

**Historical markers [S14]:** -1.7 bn (2019, near balance) → -39.7 bn (2020, -1.7% of GDP) → -24.3 (2021) → -19.7 (2022) → -10.8 (2023) → -15.3 (2024) → -21.6 (2025).

**Structural reading [S14]:**
- Net expenditure grew faster than net revenue in 2024 (+5.3% vs +4.6%) and 2025 (+3.6% vs +2.6%).
- **New revenue measures masked the drift.** Without them, the deficit would have risen by more than 9 bn in 2024, more than 13 bn in 2025 and nearly 9 bn in 2026.
- About EUR 4.5 bn of the 2026 measures are neutral for overall general government (transfers within the public sector, e.g., higher employer contribution rates for public hospitals compensated through ONDAM).
- The 2023 pension reform saves 0.8 bn (2025), 1.4 bn (2026) and 2.1 bn (2027) gross. Its **suspension** in most schemes reduces this by 0.1 bn (2026) and 0.8 bn (2027), for **net savings of 1.3 bn in 2027**.
- Sensitivities: +1% private payroll = +EUR 2.74 bn. +1 pt of inflation on benefit indexation = -EUR 3.37 bn.

### 6.2 PLFSS 2027 (bill under parliamentary debate)

| Item | Value | Source |
|---|---|---|
| 2027 deficit target (basic schemes) | **-EUR 12.7 bn** (vs -22.6 bn before measures) | Cour des comptes, 2026-10-20 [S15] |
| 2026 deficit (revised in PLFSS 2027) | -21.8 bn (2.4 bn worse than the -19.4 bn LFSS 2026 target). Confirmed in the bill, Article 1 (branches: health -12.5, AT-MP -1.3, old age -8.0, family +0.3, autonomy -0.3) [S25] | [S15, S25] |
| Health branch path after measures | -15.9 (2025), -12.5 (2026), **-7.8 (2027)**, -7.8 (2028), -7.2 (2029), -6.3 (2030) | PLFSS 2027 annex table (added 2026-10-25) [S25] |
| New revenue measures | EUR 6.3 bn (mainly narrowing contribution exemptions), largely offset by lower VAT allocation | [S15] |
| Spending savings | Nearly EUR 9 bn: ONDAM 3.9 bn; partial pension de-indexation 3.0 bn; family benefits 1.6 bn | [S15] |
| HCFP view | 2027 macro scenario "appears optimistic", "downside risks dominate" (opinion HCFP-2026-5, dated 25 Sep 2026 and published with the bills on 1 Oct 2026, quoted by CCSS; corrected 2026-10-25: was "opinion of 1 Oct. 2026", aligned with file 00 log #18) | [S14] |
| Multi-year path | Deficit of the basic schemes (ROBSS) rises again after 2027: **-14.4 bn (2028), -15.8 bn (2029), -17.0 bn (2030)**, assuming ONDAM +2.9% a year from 2028. **Confirmed 2026-10-25 in the official annex** of the bill (consolidated ROBSS table: -22.0 / -21.8 / -12.7 / -14.4 / -15.8 / -17.0 bn for 2025-2030; was flagged unverified, press only) | [S25]; first reported by Caducée [S23] |

### 6.3 Social debt (CADES, ACOSS)

| Indicator | Value | Date | Source |
|---|---|---|---|
| CADES debt amortized in 2025 | EUR 16.2 bn (resources 18.9 bn) | 2025 | [S14] |
| Cumulative debt amortized since 1996 | EUR 274.8 bn | end-2025 | [S14] |
| **Debt remaining at CADES** | **EUR 121.7 bn** (30.7% of debt transferred) | end-2025 | [S14] |
| Social debt carried by other bodies (mainly ACOSS) | EUR 40.4 bn | end-2025 | [S14] |
| Debt transfer voted in LFSS 2026 | EUR 15 bn | 2026 | [S14] |
| Expected CADES extinction | during **2033** (central scenario) | | [S14] |
| Cour des comptes recommendation | Transfer ACOSS-held deficits to CADES before end-2027, once a return-to-balance path for 2030 is documented | 2026-10-20 | [S15] |

---

## 7. European comparison (Eurostat ESSPROS, `spr_exp_func`, updated 2026-10-23)

*Method:* France's rank = position among countries sorted from highest to lowest spending. "Mean" and "median" are **unweighted** across countries. "EU-27 agg." is Eurostat's **GDP-weighted** aggregate. Groups: EU-27 (27 members), euro area EA-20 (20 members as of 2025; *note added after verification: Bulgaria joined the euro on 1 January 2026 and Eurostat now publishes an EA21 aggregate. Recomputed on EA-21, France's ranks are unchanged except disability, 7/21 in 2024*), panel of 8 (FR, DE, IT, ES, NL, BE, SE, DK). 2024 data are provisional (p). Computed table: `research/data/esspros_france_rankings.csv`.

### 7.1 Total benefits, 2024

| Measure | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | EA-20 mean / median | FR rank EA-20 | Panel-8 mean / median | FR rank panel | Source |
|---|---|---|---|---|---|---|---|---|---|
| % of GDP | **31.96** | 27.41 | 23.02 / 22.94 | **2/27** (FI 32.46) | 23.38 / 23.05 | 2/20 | 28.22 / 28.12 | **1/8** | [S4] |
| PPS per inhabitant | **12,606** | 10,974 | 9,218 / 7,939 | **7/27** (LU 19,486) | 9,618 / 8,622 | 6/20 | 12,210 / 12,638 | **5/8** (DE 14,237; NL 13,716; DK 12,982; BE 12,670) | [S4] |

Panel, % of GDP 2024: FR 31.96, DE 30.01, BE 28.69, IT 28.39, DK 27.85, SE 27.32, NL 26.37, ES 25.20 [S4].
*2025 early estimates:* France 32.12% (rank 3/27 behind AT 32.36 and FI 32.20). EU-27 agg. 27.49% [S4].

### 7.2 By function, 2024 (% of GDP and PPS per head)

| Function | FR % GDP | EU-27 agg. % GDP | EU-27 median | FR rank EU-27 (% GDP) | Panel max | FR PPS/head | EU-27 agg. PPS/head | FR rank EU-27 (PPS) | Source |
|---|---|---|---|---|---|---|---|---|---|
| Old age | 13.06 | 11.37 | 9.67 | 4 | IT 14.59 (EU max AT 14.68, not in panel; corrected after verification: was "AT 14.68" in the panel column) | 5,153 | 4,554 | 7 | [S4] |
| Survivors | 1.55 | 1.50 | 1.11 | 7 | IT 2.40 | 611 | 599 | 8 | [S4] |
| Old age + survivors | 14.61 | 12.87* | 10.50 | 4 | IT 16.99 | 5,764 | 5,153* | 7 | [S4] |
| Sickness/health care | 9.52 | 8.15 | 6.44 | 3 | DE 10.11 | 3,757 | 3,262 | 6 | [S4] |
| Disability | 2.10 | 1.92 | 1.55 | 9 | DK 5.14 | 828 | 768 | 8 | [S4] |
| Family/children | 2.24 | 2.41 | 1.92 | 9 | DE 3.59 (EU max PL 3.72) | 885 | 964 | 9 | [S4] |
| Unemployment | **1.76** | 1.08 | 0.72 | **1** | FR | **693** | 434 | **1** (2025 e: 1st in % of GDP at 1.72, but **2nd in PPS per head behind Austria**, 700 vs 745; added after verification) | [S4] |
| Housing | 0.55 | 0.37 | 0.12 | 5 | DE 0.64 | 217 | 150 | 6 | [S4] |
| Social exclusion n.e.c. | 1.17 | 0.60 | 0.40 | 2 | NL 1.35 | 462 | 242 | 4 | [S4] |

\* Sum of components.

**Reading.** France's excess over the EU-27 aggregate (4.55 pts of GDP in 2024) breaks down as: old age + survivors **+1.74 pts**, sickness **+1.37**, unemployment **+0.68**, social exclusion **+0.57**, housing **+0.18**, disability **+0.18**, family **-0.17** [S4, computed]. **Pensions and health explain about two-thirds of the gap.**

### 7.3 Twenty-year evolution of the gap

| Year | FR % GDP | EU-27 agg. | Gap vs EU-27 agg. (pts) | Panel-7 mean (excl. FR) | Gap vs panel-7 | FR PPS/head index (EU-27 = 100) | Source |
|---|---|---|---|---|---|---|---|
| 2005 | 29.19 | n.a. | n.a. | 25.39 | 3.80 | n.a. | [S4] |
| 2008 | 28.87 | 24.77 | 4.10 | 25.58 | 3.29 | **127.4** | [S4] |
| 2010 | 31.13 | 27.20 | 3.93 | 27.97 | 3.16 | 125.7 | [S4] |
| 2015 | 32.11 | 27.16 | 4.95 | 28.11 | 4.00 | 127.5 | [S4] |
| 2019 | 31.62 | 26.69 | 4.93 | 27.34 | 4.28 | 123.3 | [S4] |
| 2022 | 32.19 | 26.76 | 5.43 | 27.01 | 5.18 | 118.2 | [S4] |
| 2024 p | 31.96 | 27.41 | 4.55 | 27.69 | 4.27 | 114.9 | [S4] |
| 2025 e | 32.12 | 27.49 | 4.63 | 27.77 | 4.35 | **114.0** | [S4] |

Full series: `research/data/esspros_france_gap_series.csv`.

**Two diverging stories:**
1. **As a share of GDP, the gap widened** from about 3.3-4.1 points (2008) to a peak of 5.4 (2022) and is about 4.5 points now.
2. **Per head in PPS, France's lead shrank sharply** (+27% → +14% above the EU average). France's GDP per head grew more slowly than the EU average (catch-up of Central and Eastern Europe, Irish GDP effects), and countries such as Germany and the Netherlands overtook France in per-capita spending.

### 7.4 COFOG (general government only), 2024 [S6]

| Function | FR % GDP | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | Panel mean | FR rank panel | Source |
|---|---|---|---|---|---|---|---|
| GF10 Social protection | 23.6 (corrected 2026-10-25: was 23.7, Eurostat's table ratio on the older GDP; see note below) | 19.5 | 17.0 / 17.1 | 2 | 20.0 | 1 | [S6] |
| GF07 Health | 8.9 | 7.3 | 6.8 / 6.6 | 4 | 7.6 | 1 | [S6] |
| Total expenditure | 57.0 (corrected 2026-10-25: was 57.3, Eurostat's COFOG-table ratio on the older GDP; file 00 row 2) | 48.8 | 45.9 / 46.8 | 2 | 49.8 | 1 | [S6] |

In 2005, GF10 was 21.7% for France (EU-27 unweighted mean 15.5) [S6].

*Note added after verification:* the COFOG table puts France's 2024 total expenditure at EUR 1,671.8 bn, almost identical to `gov_10a_main` (EUR 1,672.7 bn). Its 57.3% ratio, however, implies GDP of about EUR 2,918 bn, while the current (post-May 2026) GDP is EUR 2,935.2 bn (`nama_10_gdp`, updated 2026-10-22). The COFOG ratios for France 2024 therefore use an **older GDP vintage**. On current GDP they are about 0.3 pt lower for the total (57.0%) and about 0.1 pt lower for GF10 (about 23.6%). Ranks are unaffected.

### 7.5 OECD SOCX: gross public vs net total, and the rank change

Data downloaded from the OECD SDMX API (dataflows `DSD_SOCX_AGG@DF_SOCX_AGG` and `@DF_NET_GDP`). Local file: `research/data/oecd_socx_totals.csv` [S13].

| Measure (% of GDP) | France | FR rank | OECD avg | DE | IT | ES | NL | BE | SE | DK | USA | Year | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gross public | 32.72 | 1/42 | 22.11 | 28.87 | 29.83 | 28.42 | 19.75 | 29.10 | 26.32 | 28.09 | 21.62 | 2021 | [S13] |
| Gross public | 30.65 | 3/24 reporting | 21.23 | 27.85 | 27.57 | 25.87 | 18.87 | 28.57 | 26.09 | 26.42 | 19.81 | 2024 (prelim.) | [S13] |
| Private (mandatory + voluntary) | 3.62 | 9/42 | 3.00 | 3.60 | 2.08 | 1.32 | **11.44** | 1.94 | 2.80 | 3.43 | **12.82** | 2021 | [S13] |
| Net public | 28.56 | 1/36 | 20.05 | 27.21 | 24.73 | 25.39 | 17.38 | 25.07 | 22.03 | 22.31 | 23.23 | 2021 | [S13] |
| **Net total** | **31.95** | **2/38** | 22.59 | 28.54 | 26.45 | 26.59 | **27.02** | 26.66 | **23.85** | **24.43** | **33.24** | 2021 | [S13] |
| Net total | 30.13 | 1/38 | 21.00 | 26.26 | 24.30 | 22.96 | 24.87 | 25.79 | 23.61 | 24.97 | 29.19 | 2019 | [S13] |

**What changes from gross public to net total:**
- **The USA moves from 23rd of 42 to 1st of 38** (21.6% → 33.2% in 2021; corrected after verification: was "about 20th") because of large private health and pension spending and tax breaks.
- **The Netherlands moves from 19.8% to 27.0%** (mandatory private pensions and health).
- **Denmark (28.1 → 24.4) and Sweden (26.3 → 23.9) fall**, because they tax benefits heavily (benefits are taxable income, and consumption taxes are high).
- **France barely moves (32.7 → 32.0)**. Its benefits are less taxed than in the Nordics, and its private spending is moderate (3.6% of GDP, mostly *mutuelles* and voluntary supplementary pensions).

---

## 8. Outcome indicators: what does the money buy?

All outcomes from Eurostat EU-SILC (survey year 2025 = income year 2024 for most countries), updated 2026-10-20 [S8, S9]. Rank 1 = **best** (lowest poverty or inequality, highest life expectancy). Local CSVs: `eurostat_ilc_li02.csv`, `ilc_li09.csv`, `ilc_li10.csv`, `ilc_di12*.csv`.

### 8.1 Poverty before and after transfers (60% of national median)

| Indicator (SILC 2025) | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | EA-20 mean | FR rank EA-20 | Panel-8 mean | FR rank panel | Source |
|---|---|---|---|---|---|---|---|---|---|
| AROP after all transfers | **16.3** | 16.3 | 16.0 / 15.6 | 17/27 | 16.4 | 12/20 | 15.3 | 6/8 | [S8] |
| Before social transfers, pensions counted as income (`ilc_li10`) | 26.5 | 24.4 | 24.1 / 24.4 | 20/27 | 24.6 | 14/20 | 24.6 | 7/8 | [S8] |
| Before all transfers incl. pensions (`ilc_li09`) | 46.8 | 42.8 | 40.6 / 41.1 | 26/27 | 40.5 | 19/20 | 41.7 | 7/8 | [S8] |
| **Reduction by non-pension transfers** (pts) | **-10.2** | -8.1 | | | | | | | [S8], computed |
| Child (<18) AROP after transfers | **22.8** | 19.6 | 17.9 / 16.9 | **22-23/27** (tied with EL; corrected after verification: was "22/27") | 17.9 | 17-18/20 (tie; was "17/20") | 18.1 | 6/8 | [S8] |
| Child AROP before transfers (excl. pensions) | 38.6 | 32.7 | 29.8 | 27/27 | | | | | [S8] |
| Working-age (18-64) AROP | 15.8 | 15.4 | 14.3 / 14.1 | 20/27 | | | 14.9 | 6/8 | [S8] |
| **Elderly (65+) AROP** | **11.6** | 16.3 | 19.5 / 16.4 | **7/27** | 21.3 | 5/20 | 14.0 | 3/8 | [S8] |

Panel, AROP 2025: BE 10.9, DK 11.8, NL 13.4, SE 15.6, DE 16.1, **FR 16.3**, IT 18.6, ES 19.5 [S8].
Child AROP 2025: DK 9.2, NL 10.9, BE 14.5, DE 16.0, SE 19.9, **FR 22.8**, IT 23.2, ES 28.4 [S8].

**Trend (France):** AROP was 13.0% (SILC 2005), 13.6% (2015), 15.9% (2024) and 16.3% (2025). Child AROP was 14.4% (2005), 18.7% (2015) and 22.8% (2025). Elderly AROP was 16.4% (2005), 8.0% (2015) and 11.6% (2025) [S8].

**National measure (Insee, ERFS, income 2024):** poverty rate **15.4%** (stable, highest since the series began in 1996), 9.8 m people, threshold EUR 1,337/month. Children under 18: **22.4%**. **Retirees 10.4% = active people (employed or unemployed) 10.4%**, unemployed 36.1%. Gini 0.302 (highest since 1996) [S21].

**Drees on redistribution (metropolitan France, ordinary households, ERFS 2022 income):** non-contributory benefits plus direct taxes cut the poverty rate (60% of median) from **21.3% to 14.4%** in 2022 (**-6.9 pts**). Direct taxes alone account for -0.7 pt; non-contributory benefits for the rest [S26, fiche 03, p. 1 and table 1]. Among poor households, non-contributory benefits make up **37%** of disposable income: housing benefits **9.7%** and *prime d'activité* **3.1%** (minimum incomes 13.6%, family benefits 9.6%) [S26, fiche 02, table 1]. *(Verified 2026-10-25 in Drees, Minima sociaux et prestations de solidarité, édition 2025, fiches 02 and 03; was flagged unverified and cited to fiches 07, 30 and 34. The rounded "10%" and "3%" are correct.)* Not a headline figure: file 00 log #19 keeps the Insee 15.4% and Eurostat 16.3% as the poverty headlines.

### 8.2 Inequality (Gini, 0-100)

| Indicator (SILC 2025) | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | Panel-8 mean | FR rank panel | Source |
|---|---|---|---|---|---|---|---|
| Gini disposable income | 30.4 | 29.2 | 29.1 / 29.2 | 17/27 | 28.6 | 6/8 | [S9] |
| Gini before transfers, pensions as income (`di12c`) | 37.4 | 34.1 | 33.6 / 34.1 | 22-23/27 (tied with LU; corrected after verification: was "23/27") | 34.4 | 8/8 | [S9] |
| Gini before all transfers incl. pensions (`di12b`) | 53.7 | 47.8 | 46.3 / 46.7 | **27/27** | 47.6 | 8/8 | [S9] |

*Reading:* France has the **most unequal pre-transfer income distribution in the EU** when pensions are treated as transfers. This is partly mechanical: almost all French pension income is public pay-as-you-go. After transfers, France is mid-table.

### 8.3 Health and longevity

| Indicator | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | Panel-8 mean | FR rank panel | Year | Source |
|---|---|---|---|---|---|---|---|---|
| Life expectancy at birth (years) | **83.0** | 81.5 | 80.9 / 82.0 | 7/27 | 82.8 | 4/8 | 2024 | `demo_mlexpec` [S10] |
| Healthy life years at birth (years) | 63.6 | 65.2 | 64.0 / 63.9 | 15/26 | 65.2 | 5/8 | 2024 | `hlth_hlye` [S10] |
| Healthy life years at 65 (years) | 10.9 | 10.3 | 9.7 / 9.6 | 10/26 | 11.5 | 6/8 | 2024 | [S10] |
| Out-of-pocket, % of current health expenditure (lower = better) | 10.17 | 15.06 | 19.3 / 16.9 | 3/27 | n.a. | 1/8 | 2024 | `hlth_sha11_hf` [S11] |

*Trend:* life expectancy rank fell from 3rd (2005, 80.3 years, tied with Spain) to 7th (2024). Spain (84.0) and Italy (83.7) now exceed France with much lower health spending per head (3,319 and 3,225 PPS vs 4,491). Sweden (83.8) exceeds France with slightly **higher** spending (4,777 PPS) [S10, S11]. (Corrected after verification: was "Spain, Italy and Sweden ... at lower or similar health spending per head".) *Caveat:* healthy life years rely on a self-reported limitation question (GALI) whose cross-country comparability is weak.

### 8.4 Pensioners vs working-age

| Indicator | Value | Year | Source |
|---|---|---|---|
| Retirees' average living standard / whole population | **100.2%** (projected 90.3% in 2070) | 2023 | COR June 2026 [S20] |
| AROP 65+ vs 18-64 (Eurostat) | 11.6% vs 15.8% | SILC 2025 | [S8] |
| Insee poverty, retirees vs active | 10.4% vs 10.4% | 2024 | [S21] |
| Pension spending, rank among COR countries | 2nd in **public** pension spending as % of GDP (after Italy). **6th per head** (behind US, IT, SE, DE, BE; just ahead of NL). The per-head ranking covers **public and private** old-age and survivors spending, **2021**, OECD SOCX, in USD PPP (corrected after verification: was labeled "public pension spending, 2025") | 2021 (chart in COR 2026 report) | [S20] |

---

## 9. Divergences between sources (and why)

| Topic | Figures | Explanation | Sources |
|---|---|---|---|
| Social benefits 2024, % of GDP | Drees 31.9% vs Eurostat 31.96% | Same data (Drees transmits to Eurostat). Rounding and GDP vintage | [S1, S4] |
| France's rank per head in PPS | Drees: **9th** (13,620 "French euros" PPA) vs Eurostat file of Oct. 2026: **7th** (12,606 PPS) | Drees uses France as the PPP reference and early estimates (late 2025). Eurostat PPS uses the EU-27 = 1 base and was revised in Oct. 2026 | [S3, S4] |
| France's EU rank, % of GDP | 2nd (2024, behind FI) vs 3rd (2025 e, behind AT, FI) | Different year. 2025 figures are early estimates | [S3, S4] |
| Benefits (CPS 932.5 bn) vs general government social benefits (D.62 + D.632 = 747 bn in 2024) | | CPS includes private and mutual schemes and some non-APU actors. National accounts D.62 excludes in-kind non-market production (public hospitals are in output, not D.632) | [S1, S7] |
| Social protection: ESSPROS 31.96% vs COFOG GF10 23.6% (2024; corrected 2026-10-25: was 23.7%) | | COFOG classifies most health care in GF07 (8.9%) and excludes private schemes | [S4, S6] |
| EU-27 benchmark for benefits, 2024 | Eurostat ESSPROS 27.41% (GDP-weighted aggregate, 23 Oct 2026) vs Drees fiche 12: 27.3% | Different vintages (Drees Dec 2025). **Use Eurostat 27.4%** (file 00 row 20). Added 2026-10-25 | [S3, S4] |
| Benefits 2024, % of GDP, by GDP vintage | 31.9% (Drees) / 31.96% (Eurostat) vs **31.8%** on current GDP | Drees semi-final 2024 data (933.2 bn, 23 Oct 2026) divided by current GDP (2,935.2 bn). Same GDP-vintage effect as COFOG. Added 2026-10-25 | [S1, S4, S30] |
| Total public expenditure 2024 | 57.0% (`gov_10a_main`) vs 57.3% (`gov_10a_exp` COFOG table) | **Resolved after verification:** the spending levels match (EUR 1,672.7 bn vs 1,671.8 bn). The COFOG ratio uses an older GDP denominator (about EUR 2,918 bn vs 2,935.2 bn now). Use 57.0% for 2024 | [S6, S7] |
| Pensions, share of public spending | COR 24.3% (422 bn) vs 422 / 1,714 = 24.6% using Eurostat TPE | COR's denominator or vintage differs slightly. Verify in the full COR report | [S7, S20] |
| Pensions, % of GDP | COR 14.1% (2025) vs ESSPROS old age + survivors 14.6% (2024) vs Fipeco 14.5% (2023) | Scope: ESSPROS includes non-pension old-age benefits (e.g., APA, long-term care allowances) and survivors. COR covers pensions of all compulsory schemes | [S4, S20, S22] |
| Poverty rate | Insee 15.4% (income 2024, ERFS) vs Eurostat 16.3% (SILC 2025, income 2024) | Different surveys: ERFS uses tax records and covers metropolitan ordinary households. SILC is a survey with different income concepts | [S8, S21] |
| Child poverty | Insee 22.4% vs Eurostat 22.8% | Same as above | [S8, S21] |
| Out-of-pocket health spending | Drees 7.7% of CSBM vs 9.7% of DCSi vs Eurostat 10.17% of current health expenditure | Denominators differ: CSBM excludes long-term care, where out-of-pocket is high (EUR 14.3 bn) | [S11, S16] |
| 2026 social security deficit | CCSS -21.0 bn vs PLFSS 2027 / Cour des comptes -21.8 bn | **Partly reconciled 2026-10-25.** Both cover all basic schemes (ROBSS). The CCSS labels its -21.0 bn "*avant prise en compte des mesures de la loi de financement*". The bill's Article 1 gives -21.8 bn [S25]. The whole 0.8 bn gap is in the **health branch** (CCSS -11.7 bn vs bill -12.5 bn); the other branches sum to -9.3 bn in both. Neither document explains the 0.8 bn. **Website: use -21.8 bn** (the official figure in the bill) and say it is the government's revised 2026 forecast | [S14, S15, S25] |
| ONDAM 2027 growth | +2.0% vs +2.1% (Tripalio) | **Resolved 2026-10-25:** the bill (Article 43) sets 278.7 bn, +2.0% at constant scope. 2.1% is a press error | [S25] |
| ONDAM 2027 savings | Cour des comptes 3.9 bn vs press 5.1 bn | **Resolved after verification:** 5.1 bn gross savings minus 1.2 bn of new spending = 3.9 bn net (Caducée citing the PLFSS) | [S15, S23] |
| Unédic levies since 2023 | about 12 bn (Unédic chair) vs about 14 bn (press, incl. the new 2 bn) | Different cut-off dates | [S18, S18b] |
| Health spending, % of GDP | Drees DCSi 11.8% (2025) vs Eurostat 11.33% (2024) | Different year and GDP vintage | [S11, S16] |

---

## 10. Where economists disagree: counter-arguments to the platform's thesis (steelman)

The platform's thesis: *political proposals promise to restore public finances or purchasing power without questioning the structure of public spending, and social protection is the core of that spending.* Below are the strongest objections, each with evidence, followed by the honest rebuttal or nuance.

### 10.1 "France does not spend more. It spends publicly what others spend privately."
- **Evidence:** In OECD net total social expenditure, the USA (33.2%) is above France (32.0%). The Netherlands (27.0%) is close to Germany (28.5%) despite only 19.8% gross public spending [S13]. Pensions in the Netherlands, Denmark and Sweden rely heavily on funded occupational schemes classified outside government. In France, Agirc-Arrco (compulsory pay-as-you-go supplementary pensions) is classified inside general government, in the social security subsector (*administrations de sécurité sociale*, ASSO), together with Unédic [S29]. *(Verified 2026-10-25: Insee, "Administrations publiques en 2025" (28 Aug 2026), lists "les régimes complémentaires de retraite à statut conventionnel" and "l'UNEDIC" in the ASSO subsector. The Fipeco fiche "Le solde et la dette des administrations sociales" (5 May 2026) says the same ("régimes obligatoires de sécurité sociale, de base et complémentaires"). Was: attributed to the Fipeco note S22 and flagged unverified, which does not discuss it.)*
- **Implication:** Cutting public social spending would partly shift costs to households (premiums, savings), not remove them. The relevant comparison is total cost and outcomes, not public spending alone.
- **Nuance:** Even in net total terms, France ranks 2nd of 38 and 1st in net public spending (28.6%) [S13]. The public/private split matters for deficits and compulsory levies, which is precisely the platform's subject.

### 10.2 "As a share of GDP France is high, but per head it is average among rich countries."
- **Evidence:** France ranks 7th of 27 in PPS per head (2024) and 5th of 8 in the panel, behind Germany, the Netherlands, Denmark and Belgium [S4]. It ranks 6th per head in pensions among COR countries (2021, public + private spending, OECD SOCX; clarified after verification) [S20]. The COR itself draws this conclusion: France's high ratio "s'explique en partie par un PIB par habitant plus faible" (is partly explained by a lower GDP per head) [S20]. Its per-capita lead over the EU fell from +27% (2008) to +14% (2025) [S4].
- **Implication:** The high GDP ratio is partly a **denominator problem** (weak GDP per head growth), not over-generosity per person. The steelman: "France's problem is growth and employment, not benefit levels."
- **Nuance:** Fiscal sustainability depends on the ratio to GDP and to the tax base, not on the per-capita level. Germany can spend more per head because its GDP per head is higher.

### 10.3 "The spending buys real results."
- **Evidence:** Old-age poverty (11.6%) is among the lowest in the EU, and retirees' living standard equals the population's [S8, S20]. Out-of-pocket health costs are 3rd lowest in the EU [S11]. Fertility remains the 2nd highest in the EU (1.61) [S12]. Transfers reduce poverty by 10.2 pts (EU 8.1) [S8].
- **Nuance (supports the thesis):** The headline poverty rate is only average (rank 17/27). Child poverty is among the worst (22.8%, rank 22-23/27, tied with Greece; corrected 2026-10-25: was "rank 22/27", aligned with §8.1). Life expectancy rank slipped from 3rd to 7th. Healthy life years are mid-table. Belgium, Denmark and the Netherlands get lower poverty with less spending as a share of GDP [S8, S10]. The **marginal efficiency** of spending is the open question.

### 10.4 "Pensions are a deferred wage, not a 'transfer'."
- **Evidence:** Eurostat's pre-transfer measures show France with the most unequal pre-transfer income in the EU (Gini 53.7) only when public pensions are treated as transfers [S9]. Pay-as-you-go pensions finance consumption that private savings would otherwise have to fund. The COR projects pensions at about 14% of GDP until 2045 (14.1% in 2025, 14.2% in 2045) thanks to past reforms. Up to 2045 the deficit comes mainly from **falling resources** (13.9% of GDP in 2025, falling to 12.9% by 2070) [S20]. *(Corrected after verification: the earlier wording "not rising spending" holds only to 2045. After 2045 the COR projects spending rising to **15.3% of GDP in 2070**, so in 2070 the -2.4 pt deficit is roughly half rising spending (+1.2 pt) and half falling resources (-1.0 pt).)*
- **Implication:** Some economists (e.g., the COR framing) argue the pension "problem" is about financing choices, not spending drift.
- **Nuance:** With spending at 14.1% of GDP and 24.3% of public spending, pensions are the single largest item. Their growth "explains by itself a large part of the rise in public spending over twenty years" (COR) [S20].

### 10.5 "The deficit is a revenue problem (exemptions, levies, sluggish payroll)."
- **Evidence:** The CCSS shows revenue was hit by contribution exemptions on low wages, VAT shortfalls and weak payroll (employment falling from 2025). The state took about EUR 12-14 bn from Unédic since 2023, which turned a surplus into a deficit [S14, S18]. Narrowing exemptions is the main PLFSS 2027 revenue lever [S15].
- **Nuance:** The CCSS itself states that "spending is trending more dynamically than revenue". It also shows that without about EUR 9-13 bn/year of new revenue measures, deficits would have grown much faster [S14].

### 10.6 Orders of magnitude useful against misperceptions
- **Minimum income (RSA) = EUR 12.2 bn**, while pensions = EUR 422 bn and health benefits = EUR 339 bn [S1, S17, S20]. Cutting "*assistanat*" (welfare dependency) cannot close a gap of this size. **All *minima sociaux* = 3.6% of social benefits** [S17].
- The **basic social security deficit (about EUR 21-22 bn)** is about **2.3% of social benefits** (932.5 bn) and about 0.7% of GDP [S1, S14].
- **Unemployment** is the one function where France is 1st in the EU (1.76% of GDP vs 1.08% in 2024) [S4], but it represents only 5% of benefits. (2025 early estimate: still 1st in % of GDP but 2nd in PPS per head behind Austria; added after verification.)

---

## 11. Open questions and gaps

1. **Drees CPS 2026 edition (2025 data)** is not yet published (expected December 2026). 2025 benefits by risk are only available as the Eurostat early estimate total and functions.
2. ~~**PLFSS 2027 official annexes** were not retrieved.~~ **Resolved 2026-10-25:** the bill (AN text n° 3211) was downloaded from the Assemblée nationale open-data site [S25]. It confirms ONDAM 2027 = 278.7 bn (+2.0%), the 2026 deficit of -21.8 bn, the 2027 target of -12.7 bn and the 2028-2030 path (-14.4 / -15.8 / -17.0 bn). Still open: the 0.8 bn gap with the CCSS 2026 baseline (health branch).
3. **Cost of the *quotient familial*** and other family tax expenditures was not checked (outside CPS and ESSPROS).
4. **Prime d'activité, housing benefit and minimum income spending for 2024** were not found. The Drees 2025 panorama gives 2023 spending by benefit (except the 33.3 bn total for 2024).
5. **OECD SOCX net total after 2021** is not available (two-year cycle). Preliminary gross public for 2024 covers only 24 countries.
6. ~~**2026 benefit amounts** (RSA, AAH, ASPA) were not verified.~~ **Resolved 2026-10-25** (see §5.3): RSA by decree 2026-220; AAH and ASPA from service-public.gouv.fr.7. ~~**Divergence between 57.0% and 57.3% of GDP** for 2024 total public spending (Eurostat main aggregates vs COFOG) was not resolved.~~ **Resolved after verification:** this is a GDP-vintage effect in the COFOG ratio, not a spending difference (see section 9).
8. **Unédic 2025 actual balance and end-2025 debt** were not on the October 2026 page consulted. Ex post evaluation of the 2019-2021 reform savings was not found.
9. **Outcome attribution:** no causal estimate of the efficiency of French social spending (e.g., health outcomes per euro) was located in an official source in this pass. OECD *Health at a Glance* and Cour des comptes efficiency reviews should be added.
10. **CCSS branch table** was reconstructed from a PDF layout. The values were verified against the text for maladie (-15.9), CNAF (+1.1/+1.2), CNSA (+1.3/+0.1) and AT-MP (-0.2 in 2025), but a manual check of the PDF page 21 is advisable before publication. *(2026-10-25: the PLFSS 2027 annex independently gives health -15.9 bn for 2025, matching the CCSS.)*
11. **Drees 2024 semi-final accounts** (23 Oct 2026, open data only) raise 2024 benefits to 933.2 bn. The risk-by-risk table in §3.2 still uses the December 2025 provisional values. Refresh with the December 2026 Drees edition.

---

## 12. Source list (all accessed 2026-10-25)

| Code | Institution | Title | Publication date | URL |
|---|---|---|---|---|
| S1 | Drees | *La protection sociale en France et en Europe en 2024 - Résultats des comptes de la protection sociale - Édition 2025*, Vue d'ensemble | 2025-12-18 (PDF re-uploaded 2026-03) | https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/panoramas-de-la-drees/251217-protection-sociale-france-europe-2024 ; PDF: https://drees.solidarites-sante.gouv.fr/sites/default/files/2026-03/CPS%202025%20-%20Vue%20d'ensemble.pdf |
| S2 | Drees | CPS 2025, Fiche 02 "La protection sociale depuis 1959" | 2025-12-18 | https://drees.solidarites-sante.gouv.fr/sites/default/files/2026-03/CPS2025%20-%20Fiche%2002%20-%20La%20protection%20sociale%20depuis%201959.pdf |
| S3 | Drees | CPS 2025, Fiche 12 "Les dépenses de prestations sociales en Europe" | 2025-12-18 | https://drees.solidarites-sante.gouv.fr/sites/default/files/2026-03/CPS2025%20-%20Fiche%2012%20-%20Les%20d%C3%A9penses%20de%20prestations%20sociales%20en%20Europe.pdf |
| S4 | Eurostat | ESSPROS, Expenditure on social benefits by function (`spr_exp_func`) | updated 2026-10-23 | https://ec.europa.eu/eurostat/databrowser/view/spr_exp_func/default/table ; local: `research/data/eurostat_spr_exp_func.csv`, computed `esspros_france_rankings.csv`, `esspros_france_gap_series.csv` |
| S5 | Eurostat | ESSPROS, Social protection receipts by type (`spr_rec_sumt`) | updated 2026-10-07 | https://ec.europa.eu/eurostat/databrowser/view/spr_rec_sumt/default/table ; local `eurostat_spr_rec_sumt.csv` |
| S6 | Eurostat | General government expenditure by function, COFOG (`gov_10a_exp`) | updated 2026-10-21 | https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table ; local `eurostat_gov_10a_exp.csv` |
| S7 | Eurostat (Insee transmission) | Government revenue, expenditure and main aggregates (`gov_10a_main`) | updated 2026-10-21 | https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table ; local `eurostat_gov_10a_main.csv` |
| S8 | Eurostat | EU-SILC at-risk-of-poverty rates: `ilc_li02` (after transfers), `ilc_li10` (before, pensions excluded from transfers), `ilc_li09` (before, pensions included) | updated 2026-10-20 | https://ec.europa.eu/eurostat/databrowser/view/ilc_li02/default/table ; .../ilc_li10/... ; .../ilc_li09/... ; local CSVs |
| S9 | Eurostat | Gini coefficients `ilc_di12`, `ilc_di12b`, `ilc_di12c` | updated 2026-10-20 | https://ec.europa.eu/eurostat/databrowser/view/ilc_di12/default/table ; local CSVs |
| S10 | Eurostat | Life expectancy (`demo_mlexpec`, updated 2026-09-25); Healthy life years (`hlth_hlye`, updated 2026-07-17) | see left | https://ec.europa.eu/eurostat/databrowser/view/demo_mlexpec/default/table ; https://ec.europa.eu/eurostat/databrowser/view/hlth_hlye/default/table |
| S11 | Eurostat | Health care expenditure by financing scheme (`hlth_sha11_hf`) | updated 2026-10-23 | https://ec.europa.eu/eurostat/databrowser/view/hlth_sha11_hf/default/table ; local CSV |
| S12 | Eurostat | Fertility indicators (`demo_find`) | updated 2026-09-30 | https://ec.europa.eu/eurostat/databrowser/view/demo_find/default/table |
| S13 | OECD | Social Expenditure Database (SOCX): aggregates and net total social expenditure (SDMX `OECD.ELS.SPD`, `DSD_SOCX_AGG@DF_SOCX_AGG`, `@DF_NET_GDP`) | retrieved 2026-10-25 (net total latest year 2021; public 2024 preliminary) | https://sdmx.oecd.org/public/rest/data/OECD.ELS.SPD,DSD_SOCX_AGG@DF_NET_GDP,/all ; https://www.oecd.org/en/topics/sub-issues/social-spending.html ; local `research/data/oecd_socx_totals.csv` |
| S14 | DSS / Commission des comptes de la Sécurité sociale | *Les comptes de la Sécurité sociale - Résultats 2025, prévisions 2026 et 2027* | October 2026 (PDF dated 2026-10-05) | https://www.securite-sociale.fr/files/live/sites/SSFR/files/medias/CCSS/2026/CCSS-octobre-2026_assemble_VDEF.pdf |
| S15 | Cour des comptes | *La situation financière de la sécurité sociale : un redressement impératif en 2027* | 2026-10-20 | https://www.ccomptes.fr/fr/publications/la-situation-financiere-de-la-securite-sociale-un-redressement-imperatif-en-2027 |
| S16 | Drees | *Les dépenses de santé en 2025 - Résultats des comptes de la santé - Édition 2026* | PDF dated 2026-09-30 | https://drees.solidarites-sante.gouv.fr/sites/default/files/2026-09/Embargo_Les%20d%C3%A9penses%20de%20sant%C3%A9%20en%202025_0.pdf (⚠ URL stability only: still serves the PDF on 2026-10-25, but the file name says "Embargo_" and no Drees landing page linking to it was found. Keep with caveat; for the website, link the Drees summary page https://drees.solidarites-sante.gouv.fr/actualites-evenements/combien-coute-la-sante-en-france-qui-paie, which carries the same 353.2 bn / 11.8% / 77.4% figures) |
| S16b | Hospitalia (trade press reporting Drees) | "DREES : les dépenses de santé en 2025" | 2026-10-06 | https://www.hospitalia.fr/DREES-les-depenses-de-sante-en-2025-Resultats-des-comptes-de-la-sante-Edition-2026_a5269.html |
| S17 | Drees | *Minima sociaux et prestations de solidarité - Édition 2025* (landing page and fiches 07, 30, 34) | 2025-12-04 | https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/panoramas-de-la-drees/251204-minima-sociaux-et-prestations-de-solidarite |
| S18 | Unédic | *Prévisions financières de l'Unédic - octobre 2026* | 2026-10-21 | https://www.unedic.org/publications/previsions-financieres-de-lunedic-octobre-2026 |
| S18b | Europe 1 / Boursorama (press, AFP) | Coverage of the Unédic October 2026 forecasts (verified in a browser: -0.6 bn in 2027 with the 2 bn levy; 14 bn cumulative levies. The site returns HTTP 403 to scripts) | 2026-10-21 | https://www.europe1.fr/societe/lassurance-chomage-prevoit-un-deficit-de-600-millions-deuros-en-2027-si-letat-maintient-son-prelevement-1170456 |
| S19 | Unédic | Evaluation syntheses: 2019-2021 reform (March 2025); 2023 contracyclicality reform | 2025 | https://unedic.org/storage/uploads/2025/04/03/Synthese-Principaux-enseignements-de-l-evaluation_uid_67ee965e4dfb9.pdf ; https://www.unedic.org/publications/reforme-2023-premiers-effets-de-la-reforme-de-contracyclicite |
| S20 | Conseil d'orientation des retraites (COR) | *Évolutions et perspectives des retraites en France - Rapport annuel juin 2026*, Synthèse | 2026-06-11 | https://www.cor-retraites.fr/sites/default/files/2026-06/Synth%C3%A8se_RA_2026_0.pdf |
| S21 | Insee | *Niveau de vie et pauvreté en 2024*, Insee Première n° 2117 (C. Rieg, A. Rousset) | 2026-07-09 | https://www.insee.fr/fr/statistiques/9019316 |
| S22 | Fipeco (François Ecalle, independent site, former Cour des comptes magistrate; generally favors spending restraint) | *Les dépenses publiques par fonction (2023)* and *Dépenses France/UE* notes | PDF dated 2025-05-13 (opened during verification on 2026-10-25: "retraites 14,5 % du PIB" in 2023 confirmed) | https://www.fipeco.fr/pdf/D%C3%A9pensesFonctions2023.pdf |
| S23 | Press (Tripalio, Caducée, Weka) | Coverage of PLFSS 2027 (ONDAM, savings, multi-year path) | 2026-10-01 to 2026-10-21 | https://presse.tripalio.fr/plfss-2027-les-mesures-deconomies-prevues-pour-limiter-le-deficit-a-127-mde/ ; https://www.caducee.net/actualite-medicale/16984/plfss-2027-ou-le-gouvernement-veut-trouver-5-1-milliards-d-euros-d-economies-sur-la-sante.html |
| S24 | Drees | *Les comptes de la protection sociale - Données semi-définitives jusque 2023* (open data) | 2025-10-27 | https://drees.solidarites-sante.gouv.fr/communique-de-presse-jeux-de-donnees/jeux-de-donnees/251027_DATA_comptes-de-la-protection-sociale (superseded by S30) |
| S25 | Government / Assemblée nationale | *Projet de loi de financement de la sécurité sociale pour 2027*, text n° 3211 (Articles 1, 2, 43 and annex on the 2027-2030 path) | tabled 2026-10-01 | https://www.assemblee-nationale.fr/dyn/opendata/PRJLANR5L17B3211.pdf ; local `data/raw/02_verify2/plfss2027_an3211.pdf` |
| S26 | Drees | *Minima sociaux et prestations de solidarité - Édition 2025*: Fiche 02 "La composition du revenu des ménages pauvres ou modestes" (table 1); Fiche 03 "Les effets des transferts sociaux et fiscaux sur la réduction de la pauvreté monétaire"; Fiche 08 "Les montants des minima sociaux" | 2025-12-04 | https://drees.solidarites-sante.gouv.fr/sites/default/files/2025-12/MS2025%20-%20Fiche%2002%20-%20La%20composition%20du%20revenu%20des%20m%C3%A9nages%20pauvres%20ou%20modestes.pdf ; https://drees.solidarites-sante.gouv.fr/sites/default/files/2025-12/MS2025%20-%20Fiche%2003%20-%20Les%20effets%20des%20transferts%20sociaux%20et%20fiscaux%20sur%20la%20r%C3%A9duction%20de%20la%20pauvret%C3%A9%20mon%C3%A9taire.pdf ; local `data/raw/02_verify2/ms2025_fiche0{2,3,4,8}.pdf` |
| S27 | Légifrance (JORF) | *Décret n° 2026-220 du 30 mars 2026 portant revalorisation du montant forfaitaire du revenu de solidarité active*, JORF n° 0077, 31 Mar 2026 | 2026-03-31 | https://www.legifrance.gouv.fr/jorf/id/JORFTEXT000053733826 (read in a browser) |
| S28 | service-public.gouv.fr (DILA, official portal) | AAH (F12242, checked 2026-09-14); ASPA (F16871, checked 2026-06-23, citing Cnav circular 2025-29) | 2026 | https://www.service-public.gouv.fr/particuliers/vosdroits/F12242 ; https://www.service-public.gouv.fr/particuliers/vosdroits/F16871 |
| S29 | Insee | *Administrations publiques en 2025* (definition of the ASSO subsector) | 2026-08-28 | https://www.insee.fr/fr/statistiques/8988833 ; cross-check: Fipeco fiche (5 May 2026) https://www.fipeco.fr/fiche/Le-solde-et-la-dette-des-administrations-sociales |
| S30 | Drees | *Les comptes de la protection sociale - Données semi-définitives jusque 2024* (open data; 2024 benefits = EUR 933,160.53 m, sum of sectors, `ps_code` E11-0) | 2026-10-23 | https://drees.solidarites-sante.gouv.fr/communique-de-presse-jeux-de-donnees/jeux-de-donnees/2610236-les-comptes-de-la-protection-sociale-donnees-semi-d%C3%A9finitives-jusque-2024 ; API: https://data.drees.solidarites-sante.gouv.fr/explore/dataset/305_les-comptes-de-la-protection-sociale/ ; local `data/raw/02_verify2/cps_od_E11.json` |

**Raw downloads** (untrusted data, not executed): `research/data/raw/eurostat/*.json`, `research/data/raw/oecd/*.csv`, `research/data/raw/drees/*.pdf|txt`, `research/data/raw/ccss/ccss_oct2026.pdf|txt`, `research/data/raw/cor/cor_synthese_2026.pdf`.

---

## Verification log (2026-10-25)

*Adversarial fact-check of this file. Every figure below was re-opened in the cited source or recomputed from freshly downloaded data. Fresh downloads are in `research/data/raw/02_verify/` (Eurostat JSON, OECD SDMX CSV, CCSS, COR and Fipeco PDFs, plus text extractions of the Drees PDFs). Recomputed statistics are in `research/data/02_verify_recomputed_stats.csv`.*

### Method
- **Eurostat:** re-downloaded through the dissemination API on 2026-10-25: `spr_exp_func` (updated 2026-10-23), `spr_rec_sumt` (2026-10-07), `gov_10a_main` (2026-10-21), `gov_10a_exp` (2026-10-21), `nama_10_gdp` (2026-10-22), `ilc_li02/li10/li09` and `ilc_di12/di12b/di12c` (2026-10-20), `demo_mlexpec` (2026-09-25), `hlth_hlye` (2026-07-17), `hlth_sha11_hf` (2026-10-23), `demo_find` (2026-09-30). Means, medians and ranks were recomputed independently (unweighted; EU-27, EA-20, EA-21 and panel-8). *Note:* the EU-SILC datasets now have new dimensions (`statinfo`, `rskpovth`). The figures used are `MED_EI` and `B_60` (below 60% of the median).
- **OECD SOCX:** re-downloaded `DF_NET_GDP` and `DF_SOCX_AGG` (SDMX, 2026-10-25).
- **Drees:** the site rejects scripted requests ("Request Rejected" WAF page). All cited Drees PDFs and landing pages **return HTTP 200 in a browser** (checked with a headless browser). Text was re-extracted with `pdftotext` from PDF copies whose metadata match the cited editions. CPS 2025: PDFs created 2026-03-10. Health accounts 2026: created 2026-09-30. *Minima sociaux* 2025: created 2025-11-28.
- **CCSS October 2026, COR June 2026, Fipeco:** PDFs re-downloaded directly. **Cour des comptes, Unédic, Insee, Caducée and Tripalio pages:** re-fetched. **Europe 1:** checked in a browser (HTTP 403 to scripts).

### Confirmed (value, unit, year and scope match the source)
- **Drees CPS ed. 2025 (2024 data):**
  - Benefits 932.5 bn = 31.9% of GDP, EUR 13,650 per head. Total spending 982.2 bn = 33.6%. Resources 997.8 bn.
  - All risk amounts for 2019-2024, growth rates and shares in Table 2. GDP shares by risk from chart 3 (14.6 / 11.6, etc.).
  - Resources 554.4 / 299.4 / 126.9 / 17.0 bn.
  - Fiche 02 long-run claims: 14.8% (1959); about x12 real (71 → 825 bn); growth 6.9 / 2.8 / 1.9 / +2.7 / -0.4%; share 68% → 82%; 4.0 / 4.2 / 1.6 / 7.0%/yr; contributions 77.8% → 55.6%; Itaf 3.4% (1990) → 30.0%; public contributions 17.7% → 12.7%.
  - Fiche 12: France 2nd behind Finland (32.5%) in % of GDP, 9th per head at 13,620 PPA (France-based PPP). EU-27 average 27.3% (Drees vintage; the file uses Eurostat's 27.4%, see the 2026-10-25 pass).
- **Eurostat ESSPROS:**
  - Totals: 31.96% (2024 p) and 32.12% (2025 e). EUR 960.6 bn in 2025.
  - Ranks: 2/27 (2024, FI 32.46) and 3/27 (2025, AT 32.36, FI 32.20).
  - EU-27 means and medians: 23.02 / 22.94. EA-20: 23.38 / 23.05. Panel: 28.22 / 28.12.
  - PPS per head: 12,606 vs 10,974; rank 7/27, 6/20, 5/8.
  - The whole function table (% of GDP and PPS ranks), the decomposition of the gap (+1.74 / +1.37 / +0.68 / +0.57 / +0.18 / +0.18 / -0.17), and the gap series 2005-2025 including the PPS index 127.4 → 114.0.
  - Family 2005 (2.66%, 7/26) and housing 2005 (0.80%, 1st). The 1995-2009 series values.
- **ESSPROS receipts (`spr_rec_sumt`) 2024:** every value in the receipts table.
- **`gov_10a_main` 2025:**
  - Total expenditure 1,714.1 bn = 57.3% of GDP (**the user's starting figure is confirmed**).
  - D.62 580.9 bn = 19.4% of GDP = 33.9% of TPE. D.632 190.1 bn = 6.4% = 11.1% of TPE. D.62 + D.632 2024 = 747.4 bn.
- **COFOG 2024:** GF10 23.7% as printed in Eurostat's table (23.6% at current GDP, used in the text since the 2026-10-25 second pass) (rank 2), GF07 8.9% (rank 4), EU aggregates 19.5 / 7.3, means and medians, panel means. GF10 2005: 21.7%.
- **EU-SILC 2025:**
  - AROP 16.3% (rank 17/27; EA 12/20; panel 6/8). Before transfers: 26.5% and 46.8%. Reduction 10.2 vs 8.1 pts.
  - Age groups 22.8 / 15.8 / 11.6. Trend values for 2005, 2015 and 2025.
  - Panel values. Gini 30.4 / 37.4 / 53.7 with means, medians and ranks (subject to the tie corrections below).
- **Health outcomes:** LE 83.0 (7/27). HLY 63.6 (15/26) and 10.9 (10/26). Out-of-pocket 10.17% (3rd lowest after HR and LU; EU 15.06; mean 19.3; median 16.9). Health spending 11.33% of GDP and 4,491 PPS per head. Fertility 1.61 (2/27; 1.94 and 1st in 2005).
- **OECD SOCX 2021:** net total 31.95% (2/38; USA 33.24) and all panel values. Gross public 32.72% (1/42). Gross public 2024: 30.65% (3/24). Private 3.62% (9/42). Net public 28.56% (1/36). Net total 2019: 30.13% (1/38).
- **Drees health accounts ed. 2026:**
  - DCSi 353.2 bn = 11.8%. CSBM 256.5 bn = 8.6%. All component values in table 4.1.
  - Payer table (201.6 / 249.2 / 70.6%; 77.4%; OC 12.3%, 43.4 bn).
  - Out-of-pocket 9.7% of DCSi (34.1 bn), 7.7% of CSBM, EUR 495 per head and its split (207 / 112 / 67 / 52; this is in the Drees PDF itself, not only in Hospitalia).
  - Coverage rates 94 / 62 / 79 / 76 / 45%. EU comparison 74.3 / 14.8 / 10.9%.
- **CCSS October 2026:**
  - ROBSS + FSV -15.3 / -21.6 / -21.0 / -22.6 bn and -0.7% of GDP. Historical markers.
  - Branch table: decoded consistently from the PDF layout; branch sums match the general-scheme total every year. CNRACL -3.0 → -2.3 → -1.4 is confirmed by the text (-0.7 bn, then -0.9 bn).
  - ONDAM 265.4 (+3.4%) and 273.3 (+2.8%). 2027 trend +3.4% and spontaneous +3.6% (CCSS p. 5348 of the text extract).
  - Health-branch 8.1 bn of measures. "More than 9 / more than 13 / nearly 9 bn". 4.5 bn neutral. Pension reform 0.8 / 1.4 / 2.1 gross, 1.3 net.
  - Sensitivities 2.74 / 2.65 / 3.37 bn. Births -6.6 / -2.5 / -2.4%. HCFP quotes.
  - CADES: 16.2 bn amortized (18.9 bn of resources), 274.8 bn cumulative, 121.7 bn remaining (30.7%), 40.4 bn carried elsewhere, extinction in 2033.
- **Cour des comptes (2026-10-20):** -12.7 bn in 2027; -21.8 bn in 2026 (+2.4 bn vs target); 6.3 bn of revenue; nearly 9 bn of savings (3.9 / 3.0 / 1.6); ACOSS → CADES recommendation.
- **Unédic (2026-10-21):** -2.3 / +1.8 bn (2026); +1.4 bn (2027); debt 61.5 / 60.1 / 57.7 bn; 45.7 bn without levies; revenue 44.3 bn and spending 46.6 bn; France Travail 5.2 bn; 2.6 m indemnified jobseekers; the chair's "12 Md€" quote. Press (Europe 1/AFP): -0.6 bn and 14 bn.
- **Drees *minima sociaux* ed. 2025 (2025-12-04):** 4.25 m recipients; 33.3 bn = 1.1% of GDP (2024, +3.2% real); RSA 1.84 m; AAH 1.40 m; *minimum vieillesse* 754,500; RSA 12.2 bn (0.4% of GDP), AAH 12.7 bn, *minimum vieillesse* 4.1 bn, ASS 1.7 bn (2023); *prime d'activité* 4.81 m households, 9.02 m people, 10.5 bn, EUR 633.21; housing 5.8 m / 5.9 m households, 11.2 m people (16%), 15.6 bn, EUR 226/month, -3.3% real.
- **Insee Première 2117 (2026-07-09):** 15.4%; 9.8 m people; EUR 1,337; children 22.4%; retirees = active people at 10.4%; unemployed 36.1%; Gini 0.302 (highest since 1996).
- **COR June 2026 synthesis:** 422 bn = 14.1% of GDP = 24.3% of public spending; 14.2% (2045) and 15.3% (2070); resources 13.9% → 12.9%; living standard 100.2% (2023) → 90.3% (2070); 2nd after Italy in % of GDP; 6th per head.
- **Fipeco:** pensions 14.5% of GDP in 2023 (the note is now opened directly). Fipeco's orientation is flagged in the source list (former Cour des comptes magistrate, generally favors spending restraint).

### Corrected (visible in the text as "corrected after verification")
1. Executive summary: elderly poverty benchmark changed from "19.5% EU-27 average" to the **EU-27 aggregate of 16.3%** (19.5% is the unweighted mean). The old wording exaggerated France's advantage.
2. Child poverty rank: **22-23/27, tied with Greece** (was 22/27). EA-20: 17-18/20 (was 17/20).
3. Gini before transfers excluding pensions: **22-23/27, tied with Luxembourg** (was 23/27).
4. COR per-head pension ranking: this is **2021, public and private** spending (OECD SOCX). It was labeled "public pension spending, 2025".
5. Steelman 10.4: "deficit comes from falling resources, not rising spending" holds **only to 2045**. COR projects spending at 15.3% of GDP in 2070.
6. OECD: USA gross public rank is **23rd of 42** (was "about 20th").
7. Life expectancy comparison: Sweden spends **more** per head than France (4,777 vs 4,491 PPS). The text had said "lower or similar".
8. Function table: the "Panel max" for old age is **IT 14.59**. AT is not in the panel.
9. ESSPROS long-run table: 2008 is not the "pre-crisis low" (2007 was 28.6%).
10. GF07 share of TPE is 15.6% (was "about 15.5%").
11. Unédic: the France Travail share is 11.6% of **2024 (n-2)** effective revenue, not of 2026 revenue.
12. Executive summary: Luxembourg and Austria added to the countries ahead of France in PPS per head.

### Resolved divergences
- **57.0% vs 57.3% (2024 TPE):** the COFOG ratio uses an older GDP vintage (about EUR 2,918 bn vs 2,935.2 bn). Spending levels are identical.
- **ONDAM 2027 savings 5.1 vs 3.9 bn:** gross vs net of 1.2 bn of new spending.

### Added after verification
- 2025 e: France is 2nd (behind Austria) in unemployment benefits per head in PPS.
- ASS recipients at end-2024: 265,000.
- Euro area now has 21 members (Bulgaria, 1 January 2026). France's ranks are unchanged on EA-21 except disability.
- Deficit path 2028-2030 (14.4 / 15.8 / 17.0 bn, press).
- Full breakdown of the ONDAM 2026 under-execution.

### Left unverified after the first pass (all items below were re-examined in the second pass; see its outcomes)
- The Drees redistribution figures (21.3% → 14.4%; housing benefits 10% and *prime d'activité* 3% of poor households' income). Not found in the fiches re-opened.
- Attribution of the Agirc-Arrco classification statement to the Fipeco note (the classification itself is standard ESA 2010).
- PLFSS 2027 official annexes: ONDAM 278.7 bn / +2.0% and the 2028-2030 path are confirmed only in the press. Tripalio says +2.1%.
- 2026 benefit amounts (RSA, AAH, ASPA). These were already flagged by the author.
- CCSS -21.0 bn vs Cour des comptes -21.8 bn for 2026: still not reconciled. The Cour's figure is the PLFSS 2027 forecast; the CCSS figure is "before measures" on the same scope.
- The Drees health-accounts PDF URL contains "Embargo_". It resolves today (HTTP 200 in a browser), but it may be replaced by a final file name. Re-check before publication.

### Fairness of counter-arguments
The steelman section presents real, sourced objections (net total spending, per-head comparison, outcomes, pensions as deferred wages, revenue-side deficit) and does not strawman them. Two passages leaned toward the platform's thesis and have been corrected (items 1 and 5 above). Item 5, the post-2045 rise in pension spending, actually **supports** the thesis; item 1 had **overstated** a pro-system outcome. Think-tank orientation is flagged for Fipeco. No other think tank is cited in this file.

### Second pass (2026-10-25): residual inconsistencies and ⚠ items

*Scope: README §8 rows 3 and 4 (the ones that concern this file) and every ⚠ item in README §7, row 02. New downloads (untrusted data, not executed) are in `research/data/raw/02_verify2/`. Drees PDFs were retrieved through WebFetch (scripted requests are blocked by the Drees firewall), then extracted with `pdftotext`. Légifrance was read in a browser.*

**Residual inconsistencies fixed (aligned with file 00):**
- README §8 #3: the EU-27 benchmark now says which source it uses. **Eurostat ESSPROS GDP-weighted aggregate, 27.41% → 27.4%** (2024, `spr_exp_func`, 23 Oct 2026). Drees fiche 12's 27.3% is labeled as the December 2025 Drees vintage (§0 item 3, §9, log). The website uses 27.4%.
- README §8 #4: COFOG GF10 2024 is now **23.6% of GDP** at current GDP (was 23.7%; §2 row 12, §7.4, §9). Total expenditure 2024 in §7.4 is now **57.0%** (was 57.3%). Both follow file 00 rows 2 and 11.
- HCFP opinion date aligned with file 00 log #18 (HCFP-2026-5, 25 Sep 2026; was "1 Oct. 2026").
- §10.3 child-poverty rank aligned with §8.1 (22-23/27; was 22/27).
- The Ifop 86% poll, PISA 2025 and the PLF 2027 staffing plan do not appear in this file. No flag to remove.

**⚠ items, outcomes:**
1. **Drees redistribution: confirmed, with more precise values.** 21.3% → 14.4% (-6.9 pts), 2022, metropolitan France: Drees MS 2025 **fiche 03**, p. 1. Housing benefits **9.7%** and *prime d'activité* **3.1%** of poor households' disposable income: **fiche 02, table 1** (rounded 10% and 3% were right). The file had cited fiches 07, 30 and 34; the citation is corrected [S26].
2. **Agirc-Arrco classification: confirmed, source replaced.** Insee, *Administrations publiques en 2025* (28 Aug 2026), puts the contractual supplementary pension schemes and Unédic in the ASSO subsector. The Fipeco fiche of 5 May 2026 agrees [S29]. The attribution to the Fipeco note S22 is removed.
3. **PLFSS 2027 ONDAM: confirmed in the bill.** **278.7 bn, +2.0%** at constant scope (Article 43 and *exposé des motifs*; trend +3.4%). 2026 rectified ONDAM 273.3 bn (Article 2). Tripalio's +2.1% is wrong [S25].
4. **2028-2030 deficit path: confirmed in the bill's annex** (-14.4 / -15.8 / -17.0 bn; ONDAM +2.9% a year assumed) [S25].
5. **2026 benefit amounts: confirmed.** RSA EUR 651.69 (decree 2026-220, JORF 31 Mar 2026). AAH EUR 1,041.59 and ASPA EUR 1,043.59 (service-public.gouv.fr; ASPA via Cnav circular 2025-29). Each one equals the April 2025 Drees scale (646.52 / 1,033.32 / 1,034.28) times the legal revaluation (+0.8% / +0.8% / +0.9%) [S26-S28].
6. **CCSS -21.0 vs bill -21.8 bn (2026): narrowed, not fully reconciled.** The gap sits entirely in the health branch (-11.7 vs -12.5 bn); the other branches sum to -9.3 bn in both. The CCSS labels its figure "before the measures of the financing law". No document found explains the 0.8 bn. **Recommendation: keep with caveat.** Show -21.8 bn (the bill) on the website and keep -21.0 bn only as the CCSS pre-measure baseline.
7. **Drees health-accounts "Embargo_" URL: still ⚠, URL stability only.** The figures were verified in the first pass. The PDF still resolves on 2026-10-25, but no landing page was found. **Recommendation: keep with caveat.** On the website, link the Drees summary page "Combien coûte la santé en France ? Qui paie ?", which carries the same headline figures.

**New findings (affect file 00):**
- **Drees semi-final 2024 accounts** (open data, 23 Oct 2026): 2024 benefits **EUR 933.2 bn** (was 932.5 bn provisional); 2023 890.8 bn (was 889.5). Eurostat `spr_exp_func` already carries 933,160.53 m for France 2024.
- **GDP-vintage effect on the 31.9% starting figure.** Drees' 31.9% and Eurostat's 31.96% imply a 2024 GDP of about EUR 2,918-2,920 bn. Current 2024 GDP is EUR 2,935.2 bn (`nama_10_gdp`, 22 Oct 2026). On current GDP the ratio is **31.8%**. This is the same mechanism file 00 log #6 documents for COFOG. Eurostat's 2025 value (32.12%) already uses current GDP (960.6 / 2,991.1).
- **The EU rank for 2024 is fragile.** On Eurostat's published ratios France (31.96) is only 0.05 pt ahead of Austria (31.91). On current French GDP (31.8%) it would be 3rd. Recommendation for file 00 row 21: "**among the top three in 2024 and 2025**" (2nd in 2024 on Eurostat's published ratio, 3rd in 2025 early estimate).

**Still flagged in this file:** only the S16 URL caveat (item 7) and the unexplained 0.8 bn health-branch gap (item 6). No figure in the file is now marked "from memory" or press-only.
