# 12 - Health system and hospitals: spending, inputs, efficiency, access and outcomes vs EU/OECD (2005-2025)

*Gap-fill research file for the public-finance education platform. Prepared 2026-10-25. All web sources accessed 2026-10-25. Figures we computed from raw data are marked "(our computation)", and the CSV is cited. This file adds to file 04 (§6.2 Health) and file 09 (COFOG health rows); it does not replace them. Where this file corrects or qualifies a statement in files 04 or 10, it says so explicitly (§10).*

**Scripts** (pure Python standard library plus `openpyxl`, run with `python3 -I`): `research/scripts/12/analyze12.py` (Eurostat), `who12.py` (WHO GHED), `oecd_am12.py` (OECD avoidable mortality), `oecd_cc12.py` (OECD cancer survival), `haag_stats12.py` and `haag_to_csv.py` (OECD *Health at a Glance 2025* StatLinks), `apl12.py` (Drees APL), `oecd_retry.sh` (OECD API downloads, which were rate-limited with HTTP 429).
**Raw data:** `research/data/raw/12/{eurostat,oecd,oecd/haag2025,who,drees,docs}/`.
**Computed CSVs:** `research/data/12_*.csv` (listed in §11.3).

---

## 0. Bottom line (for the platform editors)

1. **France spends a lot on health relative to GDP, but much less in per-person purchasing power.** Current health expenditure (CHE, System of Health Accounts concept) was **11.33% of GDP in 2024** (Eurostat). That is **3rd of 27 in the EU** (after Germany 12.21% and Austria 11.71%), **3rd of 21 in the euro area**, and **5th of 38 in the OECD** (OECD: 11.54%, behind the US, Germany, Austria and Switzerland). Provisional 2025: 11.48% (Eurostat). Drees's new edition gives 11.8% for 2025, on a revised series. **Per inhabitant in PPS, France ranks only 8th of 27** (4,491 PPS in 2024, against an EU-27 aggregate of 4,075 and an EA21 aggregate of 4,312 [EA20: 4,342]; added 2026-10-25 to align with file 00's EA21 convention). It ranks **5th of 8 in the panel**, below Germany, the Netherlands, Belgium and Sweden, and **12th of 38 in the OECD** (USD 7,367 PPP). The high GDP ratio therefore reflects lower GDP per head as well as high spending.
2. **The gap is stable, not widening.** France minus the unweighted EU-27 mean (WHO GHED, % of GDP): +2.5 pp in 2005, +3.3 pp in 2015, +2.9 pp in 2019, +2.9 pp in 2023. France minus the GDP-weighted EA21 aggregate (Eurostat, CHE % of GDP): +1.21 pp in 2014, +0.88 in 2019, +0.88 in 2024 [EA20: +1.20, +0.86, +0.87] (EA21 added 2026-10-25). **On the SHA concept, the "public" gap with the euro-area aggregate is about 1.0 pp of GDP** (compulsory schemes HF.1 9.44% vs EA21 8.38% [EA20 8.40%] in 2024, about EUR 30 bn). That is smaller than the **COFOG health gap of +1.5 pp (+1.47 pp in 2024 vs the EA21 aggregate; file 00, row 9)** quoted in files 01 and 09. The two measures cover different perimeters (§1.3).
3. **France is not a hospital-heavy spender as a share of health spending.** Hospitals (provider HP.1) take **37.0% of CHE** (EU mean 40.0%, rank 20/27, 2024). In % of GDP, however, hospitals take 4.19% (EU-27 aggregate 3.70%, rank ~~5/27~~ **5th-6th of 27, tied with Spain at 4.19** [corrected 2026-10-25]). In COFOG, the excess over the euro area is larger for **outpatient services (+0.7 pp of GDP) than for hospital services (+0.5 pp)**.
4. **Administration is where France is a clear outlier, and the reason is structural.** Governance and financing administration (SHA HC.7) was **5.09% of CHE**, **EUR 16.9 bn**, or **0.58% of GDP** in 2024. That is **1st of 27 in the EU** as a share of CHE (EU-27 aggregate 3.50%, median 2.32%) and 1st as a % of GDP (EU-27 aggregate 0.36%). Roughly 0.2 pp of GDP (about EUR 6 bn) separates France from the EU or euro-area aggregate. France runs a **double layer of insurance**: compulsory social insurance plus near-universal complementary insurance. Drees reports that complementary insurers (*organismes complémentaires*) account for **52% of the health system's ~~EUR 18 bn~~ EUR 17.6 bn management costs in 2025** (5.0% of DCSi; corrected 2026-10-25, Drees table value), while financing only 12.3% of spending. Drees Table 2 splits the EUR 17.6 bn as Social Security EUR 7.2 bn, central and local government EUR 1.2 bn, complementary insurers EUR 9.2 bn (verified 2026-10-25). This is the most solid "structure of spending" argument in health.
5. **Inputs: many beds and hospital staff, few doctors, relatively low pay.**
   - France has 5.4 beds per 1,000 people (OECD 4.2, rank 10/38). Beds fell 26% from 2005 to 2024.
   - France has 20.2 hospital workers per 1,000 people (OECD 15.5, 2nd in the panel). "Other staff" alone is 6.9 per 1,000, twice the OECD's 3.4.
   - Practising doctors: 3.9 per 1,000, at the OECD mean (3.9) but **17th of 26 in the EU** (Eurostat). Nurses: 8.8 per 1,000, below the OECD mean (9.2).
   - The average curative stay is short (5.5 days vs OECD 6.4).
   - Health-sector price levels are low: **68 (OECD = 100) vs 96 economy-wide**, the lowest relative price in the panel. Hospital nurses earn **0.97 times the average wage** (OECD 1.17). OECD's price/volume split puts French health **volumes per capita at 128 (OECD = 100), 4th of 37**.
   - In short, France buys a lot of care and pays health workers relatively little. "Overpaid staff" is not the driver.
   - Public-hospital pay (COFOG GF0703, D.1) is **2.2% of GDP**, which is **17.6% of total general-government compensation of employees** (2024). That ranks 8th of 27; the EU mean is 13.2% (our computation).
6. **Outcomes: good on mortality and financial protection, average on cancer survival, deteriorating on access.**
   - Treatable mortality is among the lowest in Europe: **58.8 per 100,000 in 2023 (Eurostat), 3rd of 27**. In the OECD it is 46 (2023), 4th of 30. Preventable mortality is middling (10th of 27).
   - Out-of-pocket payments are 10.2% of CHE (3rd lowest in the EU) and **2.0% of household consumption, 5th lowest of 38 in the OECD**.
   - Healthy life years at birth are 63.6, about the EU median (15th of 26).
   - **Cancer five-year net survival (CONCORD-3, 2010-14 diagnoses) is average, not top**: breast 86.7% (12th of 34 OECD), colon 63.7% (16th), lung 17.3% (17th), rectum 60.9% (21st).
   - Access:
     - **France does not report elective-surgery waiting times to the OECD** (we checked: no French rows in the OECD waiting-time database).
     - In the Commonwealth Fund 2023 survey, **65% of French respondents waited a month or more for a specialist (10-country average 52%)** and **45.5% waited two months or more, the 2nd-worst after Canada**.
     - On the Drees APL indicator, **29% of the population (19.6 million people) lived in a commune with fewer than 2.5 GP consultations per year per inhabitant in 2024** (GPs aged 65 or under), up from 25% in 2022 (our computation). The threshold is not comparable with the old "6% in 2018" figure (§6.6).
7. **The EU-SILC "unmet needs" jump is partly a statistical break, and this changes how the indicator can be quoted.**
   - Eurostat flags France's series **"b" (break in series) in 2020 and in 2022**, after Insee's IESS redesign of the SRCV survey.
   - Unmet needs due to cost, distance or waiting went from 1.2% (2019) to 2.7% (2020, break), 3.2% (2022, break), 4.1% (2024) and 3.7% (2025). The **cost component jumped at the 2020 break** (0.8 to 2.0%) and has been flat since.
   - The **waiting-list component rose progressively within the unbroken 2022-2025 segment** (1.0 to 1.8% in 2024, 1.4% in 2025). The EU-27 also rose from 1.7 to 2.4% over 2019-2025.
   - **Defensible wording:** "unmet needs due to waiting lists have risen since 2021 and France is now in the bottom third of the EU". **Not defensible:** "unmet needs have tripled since 2019", as files 04 and 10 say.
8. **Strongest steelman.**
   - France delivers top-tier treatable mortality and the best financial protection in the panel. It does so at a per-capita PPS spend below Germany, the Netherlands, Belgium and Sweden.
   - Its spending growth has been among the slowest in the OECD: real per-capita growth 0.7%/yr in 2014-19 against an OECD average of 2.7%, and 0.9%/yr in 2019-24 against 2.5%.
   - Public hospitals are in deficit (EUR 2.9-3.1 bn in 2024; 2.1% of revenue in 2025). IGAS documents EUR 1.7 bn of unfunded pay measures in 2020-2024.
   - So the case for large *cuts* in health is weak. The case for *restructuring* is strong: administration, complementary-insurance duplication, hospital "other staff", low-volume surgical sites, prevention (2.3% of CHE vs OECD 3.4%), and medical-desert organization. The Cour des comptes (Apr 2026) adds **EUR 22 bn of low-value or unnecessary care** and **over EUR 11 bn of avoidable harm**. These are extrapolations from OECD ratios, not audited figures.

---

## 1. Scope and definitions

### 1.1 Concepts used in this file

| Concept | Definition | Source and code | What it includes / excludes |
|---|---|---|---|
| **CHE** (current health expenditure) | System of Health Accounts (SHA 2011) total, all financing sources (public, compulsory private, voluntary, out-of-pocket) | Eurostat `hlth_sha11_hf` (TOT_HF); OECD `DSD_SHA@DF_SHA`; WHO GHED `GHED_CHEGDP_SHA2011` | Includes long-term care (health part, HC.3) and administration (HC.7). Excludes capital spending (investment) and health R&D. **Same concept as Drees's *DCSi* (*dépense courante de santé au sens international*).** |
| **HF.1** "government and compulsory schemes" | HF.11 government schemes + HF.121 social health insurance + HF.122 compulsory private insurance | Eurostat `hlth_sha11_hf` | The usual "public" measure in OECD/EU comparisons. **In France, HF.122 has included employer-mandated collective complementary contracts (ANI reform) since 2016: EUR 15.7 bn in 2016, EUR 22.2 bn (0.76% of GDP) in 2024.** HF.1's share of CHE jumped from 74.7% (2015) to 81.1% (2016) with no flag. This is a reclassification, not a policy change. |
| **HF.11 + HF.121** | Government schemes + social security only | Eurostat (our sum) | Our "strictly public" measure. Not comparable for the Netherlands, whose basic insurance is HF.122 (5.1% of GDP). |
| **HF.3** out-of-pocket | Direct household payments | Eurostat, OECD | Drees's *reste à charge* (out-of-pocket) is the same concept. |
| **HP.1** hospitals | Spending at hospital providers, all functions (inpatient, day, outpatient, LTC) | Eurostat `hlth_sha11_hp` | **% of CHE** or **% of GDP**, as labelled. |
| **HC.7** governance and administration | HC.71 governance and health-system administration + HC.72 administration of health financing (insurer management) | Eurostat `hlth_sha11_hc`, `hlth_sha11_hchf` | Includes the management costs of complementary insurers when they are financing schemes (HF.2 or HF.122). |
| **COFOG GF07** health | General-government expenditure on health, ESA 2010 | Eurostat `gov_10a_exp` (files 01, 09) | Public sector only (S.13). Includes investment and health R&D. Excludes private and compulsory private insurance. Some long-term care is in GF10 (social protection). |
| **CSBM** | *Consommation de soins et de biens médicaux* (consumption of care and medical goods) | Drees | Narrower than CHE: excludes long-term care, prevention and administration. EUR 256.5 bn in 2025 [D1]. |
| **ONDAM** | *Objectif national de dépenses d'assurance maladie* (national health-insurance spending target voted in the PLFSS) | LFSS/PLFSS, HCFP, Cour des comptes | A budget target covering basic health insurance only. Not an international concept. |

### 1.2 Groups and statistics

- **EU-27** (27 Member States), **EA21** (21 current euro-area members incl. Bulgaria from 1 Jan 2026, fixed composition for all years, as in file 09), **OECD-38**, **Panel** = FR, DE, IT, ES, NL, BE, SE, DK (8 countries incl. France).
- **Euro-area aggregate (note added 2026-10-25):** file 00 makes **EA21** the canonical euro-area aggregate. The SHA tables below were built with Eurostat's **EA20** aggregate. Eurostat also publishes EA21 for SHA, and the two differ by less than 0.05 pp of GDP in every headline row (2024: CHE 10.45 vs 10.46; HF.1 8.38 vs 8.40; HC.7 0.38 vs 0.38% of GDP and 3.62 vs 3.63% of CHE; CHE per inhabitant 4,312 vs 4,342 PPS). For the website, quote EA21 with EA20 in brackets where they differ. Source: Eurostat `hlth_sha11_hf`, `hlth_sha11_hc` API, queried 2026-10-25.
- **"Aggregate"** = Eurostat's GDP-weighted EU27_2020 or EA20 figure (EA21 in the bottom line and §1.3). **"Mean"** and **"median"** are unweighted across countries (our computation). **Rank 1** = highest value unless stated otherwise ("1 = best" for mortality and unmet needs).
- Unless labelled otherwise, **every ratio is % of GDP**. Shares "of CHE" are % of current health expenditure. Where a figure is a % of **total general-government expenditure**, the label says so.

### 1.3 Why "the health gap" differs across files (reconciliation)

| Measure | France 2024 | Euro-area comparator | Gap (pp of GDP) | Source |
|---|---|---|---|---|
| COFOG GF07, general government | 8.9 | EA21 aggregate 7.4 | **+1.5** (+1.47; file 00 row 9 and log #8) | file 09 [gov_10a_exp] |
| Fipeco, "health incl. health-related cash benefits", EU average | 11.8 | 10.2 | **+1.6** | file 01 (Fipeco, 8 Jul 2026) |
| SHA CHE, all financing | 11.33 | EA21 aggregate 10.45 [EA20 10.46] | **+0.88** [EA20 +0.87] | [E1] |
| SHA HF.1 government + compulsory | 9.44 | EA21 aggregate 8.38 [EA20 8.40] | **+1.06** [EA20 +1.04] | [E1] |
| SHA HF.11 + HF.121 (strictly public) | 8.68 | EA20 aggregate 7.63 (EA21 not recomputed) | **+1.05** | [E1] (our sum) |

*(Comparator labels aligned with file 00 on 2026-10-25: the COFOG row was "EA aggregate" without a composition; the SHA rows were EA20 only.)*

The COFOG gap is larger than the SHA public gap. The COFOG decomposition (file 09) puts the excess at medical products +0.3, **outpatient +0.7**, **hospital +0.5**, public health +0.1, R&D 0.0 and n.e.c. -0.1 pp. COFOG includes general-government health investment and R&D, which SHA excludes. COFOG excludes compulsory private insurance, which SHA HF.1 includes (0.76 pp in France, 0.87 in Germany, 5.1 in the Netherlands). Part of the long-term care that SHA counts in HC.3 sits in COFOG GF10. **We did not decompose the residual line by line (gap).** Recommended wording: "Health explains 1 to 1.5 pp of GDP of France's spending gap with the euro area, depending on the definition (SHA or COFOG)."

---

## 2. Health expenditure: totals, public share, per capita (2005, 2015, 2019, latest)

### 2.1 Total current health expenditure, % of GDP

| Year | France | EU-27 agg. | EA20 agg. | EU-27 mean / median (n) | FR rank EU-27 | EA21 mean / median | FR rank EA21 | OECD-38 mean / median | FR rank OECD | Panel mean / median | FR rank panel | DE | IT | ES | NL | BE | SE | DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2005 (WHO) | **10.24** | n/a | n/a | 7.72 / 7.99 (27) | **1** | 7.88 / 8.05 | 1 | 7.88 / 8.02 | 2 (after US) | 9.00 / 9.06 | 1 | 10.11 | 8.31 | 7.78 | 9.06 | 9.25 | 8.16 | 9.07 | [W1] |
| 2015 (Eurostat) | **11.28** | 9.86 | 10.11 | 8.21 / 8.27 (27) | **1** | 8.34 / 8.60 | 1 | 8.69 / 8.71 (WHO) | 2 (WHO) | 10.33 / 10.63 | 1 | 10.92 | 8.85 | 9.18 | 10.19 | 10.88 | 10.93 | 10.38 | [E1][W1] |
| 2019 (Eurostat) | **10.98** | 9.84 | 10.12 | 8.27 / 8.12 | **2** (DE 11.42) | 8.40 / 8.57 | 2 | 8.81 / 8.63 (WHO) | 4 (WHO) | 10.27 / 10.52 | 2 | 11.42 | 8.62 | 9.22 | 9.94 | 10.85 | 10.96 | 10.18 | [E1][W1] |
| 2024 (Eurostat) | **11.33** | 10.16 | 10.46 | 8.87 / 8.54 | **3** (DE 12.21, AT 11.71) | 9.02 / 8.54 | 3 | 9.31 / 9.28 (OECD) | **5** (US 17.2, DE, AT, CH) | 10.40 / 10.59 | 2 | 12.21 | 8.46 | 9.25 | 10.10 | 11.07 | 11.16 | 9.59 | [E1][O1 Fig 7.1] |
| 2024 (OECD) | 11.54 | | | | | | | 9.31 (published OECD38 avg 9.3) | 5/38 | | | 12.27 | 8.44 | 9.17 | 10.01 | 10.97 | 11.31 | 9.39 | [O1 Fig 7.1, stat.link/15fht6] |
| 2025 (Eurostat, provisional) | **11.48 (p)** | n/a | n/a | 15 countries reporting | 3 of 15 | | | | | | | 12.73 | 8.42 | | 10.19 | | 10.91 | 9.58 | [E1] |
| 2025 (Drees, DCSi, 2026 edition) | **11.8** (EUR 353.2 bn) | EU 10.5 (Drees) | | | "among the 3 highest in the EU" | | | | | | | | | | | | | | [D1] |

*Notes.* (a) Eurostat's France series starts in 2006, so the 2005 value comes from WHO GHED. WHO 2005 France 10.24; Eurostat 2006 France 10.40. (b) **Divergence 2025:** Eurostat 11.48% (EUR 343.4 bn, provisional transmission) vs Drees 11.8% (EUR 353.2 bn, 2026 edition with revised series [D1, annex 3 "*Les révisions de l'édition 2026*"]). Quote Drees for France alone and Eurostat for comparisons. (c) The OECD 2024 France value (11.54) is about 0.2 pp above Eurostat's (11.33) because of vintage differences. WHO's France series is also about 0.2 pp above Eurostat (e.g. 2023: 11.52 vs 11.33).

**Gap evolution, 20 years** (`research/data/12_fr_che_gap_timeseries.csv`, our computation):

| Year | FR - EU-27 mean (WHO) | FR - EA21 mean (WHO) | FR - OECD-38 mean (WHO) | FR - panel mean (WHO) | FR - EU-27 agg. (Eurostat) | FR - EA20 agg. (Eurostat) |
|---|---|---|---|---|---|---|
| 2000 | +2.70 | +2.51 | +2.48 | +1.51 | | |
| 2005 | +2.52 | +2.36 | +2.36 | +1.24 | | |
| 2010 | +2.76 | +2.54 | +2.57 | +1.28 | | |
| 2015 | +3.28 | +3.16 | +2.81 | +1.15 | +1.42 | +1.17 |
| 2019 | +2.89 | +2.76 | +2.36 | +0.88 | +1.14 | +0.86 |
| 2022 | +3.13 | +2.92 | +2.70 | +1.34 | +1.44 | +1.09 |
| 2023 | +2.89 | +2.73 | +2.42 | +1.24 | +1.39 | +1.10 |
| 2024 | | | | | +1.17 | +0.87 |

Reading: the gap with the typical EU country (unweighted mean) is about 2.5-3.3 pp and roughly stable over 20 years. The gap with the weighted aggregates is about 1 pp and has narrowed since 2015. Germany has overtaken France since 2019.

### 2.2 Public (government and compulsory) health spending

| Indicator | Year | France | EU-27 agg. | EA20 agg. | EU-27 mean / median | FR rank EU | EA21 mean / median | FR rank EA21 | OECD mean / median | FR rank OECD | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HF.1, % of GDP | 2015 | 8.42 | 7.65 | 7.81 | 5.98 / 5.50 | 4 | 5.93 / 5.50 | 2 | | | 8.14 / 8.36 | 4 | 9.23 / 6.55 / 6.45 / 8.29 / 8.26 / 9.16 / 8.74 | [E1] |
| HF.1, % of GDP | 2019 | 8.95 | 7.78 | 7.98 | 6.13 / 5.56 | 3 | 6.08 / 5.56 | 2 | | | 8.18 / 8.38 | 3 | 9.67 / 6.31 / 6.40 / 8.23 / 8.07 / 9.30 / 8.53 | [E1] |
| HF.1, % of GDP | 2024 | **9.44** | 8.17 | 8.40 | 6.80 / 6.31 | **3** | 6.81 / 6.31 | 2 | 7.08 / 7.01 (OECD, 2024) | **3/38** (DE, US) | 8.36 / 8.26 | 3 | 10.48 / 6.23 / 6.68 / 8.39 / 8.13 / 9.60 / 7.93 | [E1][O1 Fig 7.1] |
| HF.11+HF.121 (strictly public), % of GDP | 2024 | 8.68 | 7.51 | 7.63 | 6.54 / 6.30 | 4 | | | | | | | 9.61 / 6.23 / 6.68 / 3.27* / 8.12 / 9.60 / 7.93 | [E1] (our sum) |
| HF.1, PPS per inhabitant | 2015 | 2,521 | 2,123 | 2,303 | 1,696 / 1,429 | 8 | 1,699 / 1,429 | 6 | | | 2,587 / 2,805 | 6 | 3,268 / 1,695 / 1,579 / 2,937 / 2,692 / 3,087 / 2,918 | [E1] |
| HF.1, PPS per inhabitant | 2019 | 2,946 | 2,460 | 2,645 | 1,959 / 1,767 | 7 | 1,965 / 1,767 | 5 | | | 2,868 / 3,049 | 5 | 3,823 / 1,852 / 1,767 / 3,257 / 2,876 / 3,273 / 3,152 | [E1] |
| HF.1, PPS per inhabitant | 2024 | **3,741** | 3,273 | 3,486 | 2,732 / 2,411 | **6** | 2,773 / 2,411 | 5 | USD PPP 4,620 / 4,836 (OECD) | 9/38 (USD 6,219) | 3,656 / 3,720 | 4 | 4,973 / 2,374 / 2,398 / 4,363 / 3,590 / 4,111 / 3,698 | [E1][O1 Fig 7.4] |
| HF.1, % of CHE | 2024 | 83.3 | 80.3 | 80.3 | 76.5 / 77.3 | 7 | 75.4 / 76.6 | 5 | | | 80.0 / 82.9 | 3 | 85.9 / 73.6 / 72.3 / 83.0 / 73.4 / 86.1 / 82.7 | [E1] |
| Public health spending, % of **total general-government expenditure** | 2023 | 15.8 | | | | | | | OECD38 15.1 | | | 4 of 8 | 19.2 / 11.4 / 14.9 / 15.6 / 14.9 / 19.4 / 16.8 | [O1 Fig 7.12, stat.link/bquoys] |

\* The Netherlands' basic insurance is classified as compulsory private insurance (HF.122), so the "strictly public" line understates Dutch public effort.

**Caution on the French HF.1 series:** the 2015-2016 jump from 74.7% to 81.1% of CHE (HF.2 voluntary insurance falling from 13.6% to 7.4%) is the 2016 reclassification of employer-mandated complementary contracts into HF.122. The flag "b" in 2010 marks an earlier break. Do not present 2005-2024 changes in the public share of CHE as policy-driven.

**WHO divergence:** WHO's "domestic general government health expenditure" (GGHE-D) for France falls from 75.3% of CHE (2022) to 67.7% (2023), and from 8.91% to 7.80% of GDP. Neither Eurostat nor Drees shows this break, so it is very probably a WHO classification artifact. **Do not use WHO GGHE-D for France in 2023** (`12_who_ghed_che_stats.csv`).

### 2.3 Total health spending per capita in PPS (purchasing power)

| Year | France | EU-27 agg. | EA20 agg. | EU-27 mean / median | FR rank EU-27 | EA21 mean / median | FR rank EA21 | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 2006 | 2,723 | n/a | n/a | 2,078 / 2,275 (n = 12 only) | 4/12 | | | | 3/6 | 2,766 / n.a. / 1,905 / 3,027 / 2,525 / 2,373 / n.a. | [E1] |
| 2015 | 3,375 | 2,738 | 2,979 | 2,277 / 1,944 | 8 | 2,330 / 2,245 | 6 | 3,259 / 3,504 | 6 | 3,864 / 2,290 / 2,245 / 3,609 / 3,546 / 3,684 / 3,463 | [E1] |
| 2019 | 3,617 | 3,112 | 3,352 | 2,599 / 2,324 | 8 | 2,658 / 2,528 | 6 | 3,578 / 3,810 | 6 | 4,517 / 2,528 / 2,544 / 3,933 / 3,865 / 3,855 / 3,766 | [E1] |
| 2024 | **4,491** | 4,075 | 4,342 | 3,519 / 3,247 | **8** | 3,620 / 3,251 | 7 | 4,527 / 4,634 | **5** | 5,791 / 3,225 / 3,319 / 5,254 / 4,892 / 4,777 / 4,471 | [E1] |
| 2024 (OECD, USD PPP) | 7,367 | | | OECD-38 mean 5,967; median 5,658 | **12/38** | | | 7,296 / 7,558 | 5 | 9,365 / 5,164 / 5,346 / 8,436 / 7,750 / 7,871 / 7,071 | [O1 Fig 7.4, stat.link/rkae5h] |

In PPS per head, France was 10% above the EU-27 aggregate and 4% above the EA21 aggregate (4,312 PPS; 3% above EA20) in 2024. It sits 23% below Germany. Drees gives EUR 5,130 per inhabitant in 2025 (DCSi), of which EUR 3,620 Social Security, 630 complementary insurers, 353 State and local government, and 495 households [D1].

### 2.4 Growth: France has been one of the slowest-growing health spenders

| Indicator | France | OECD-38 average | DE | IT | ES | NL | BE | SE | DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|
| Real growth in health spending per capita, % per year, 2014-2019 | **0.68** | 2.69 | 2.77 | 0.84 | 2.76 | 0.94 | 1.76 | 1.25 | 1.70 | [O1 Fig 7.5, stat.link/nwmzh5] |
| Same, 2019-2024 | **0.87** | 2.53 | 1.57 | 0.89 | 0.74 | 0.00 | 0.64 | 0.95 | 0.01 | [O1 Fig 7.5] |
| Nominal DCSi growth 2025 | +3.3% | EU +5.9% (Drees) | | | | | | | | [D1] |

### 2.5 Price vs volume: what the high spending buys

| Indicator (2023) | France | OECD (=100) | OECD rank | DE | IT | ES | NL | BE | SE | DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Health-sector price level (OECD = 100) | **68.1** | 100 (computed mean 81.6) | 22/37 | 75.9 | 79.1 | 66.7 | 92.8 | 82.8 | 105.6 | 96.2 | [O1 Fig 7.6, stat.link/zw0b9d] |
| Economy-wide price level (OECD = 100) | 96.1 | 100 | | 98.5 | 84.7 | 79.0 | 103.5 | 99.4 | 103.7 | 116.6 | [O1 Fig 7.8, stat.link/lmb3wn] |
| Relative price of health (health PLI / economy PLI) | **0.71** (lowest in panel) | 1.00 | | 0.77 | 0.93 | 0.84 | 0.90 | 0.83 | 1.02 | 0.83 | our computation |
| Health volume per capita (OECD = 100) | **127.7** | 100 | **4/37** (US, DE, CH) | 139.6 | 70.1 | 79.5 | 115.5 | 121.4 | 99.1 | 114.4 | [O1 Fig 7.7, stat.link/tfnguq] |

*Caveat (OECD note to Fig 7.6):* hospital PPPs are estimated mainly with the **input method**, i.e. from the salaries of medical and non-medical staff. France's low "price" therefore largely reflects lower health-worker pay (§4.4), and the volume figure is a residual. The direction is robust: France has **high volumes and low unit prices**, not the reverse.

---

## 3. Where the money goes: hospitals, administration, prevention

### 3.1 Hospital share of spending

| Indicator | Year | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | EA21 mean / median | FR rank EA21 | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hospitals (HP.1), **% of CHE** | 2015 | 36.1 | 36.1 | 38.6 / 37.9 | 18 | 38.3 / 36.9 | 13 | 38.0 / 37.0 | 5 | 29.0 / 44.9 / 42.9 / 33.8 / 33.1 / 37.9 / 46.0 | [E3] |
| Hospitals (HP.1), **% of CHE** | 2024 | **37.0** | 36.4 | 40.0 / 40.5 | **20** | 39.2 / 37.8 | 14 | 38.3 / 38.1 | 5 | 27.5 / 43.7 / 45.3 / 34.2 / 34.3 / 39.1 / 45.3 | [E3] |
| Hospitals (HP.1), **% of GDP** | 2015 | 4.07 | 3.56 | 3.17 / 3.20 | 3 | 3.18 / 3.40 | 1 | 3.88 / 3.95 | 3 | 3.16 / 3.97 / 3.93 / 3.44 / 3.60 / 4.14 / 4.77 | [E3] |
| Hospitals (HP.1), **% of GDP** | 2024 | **4.19** | 3.70 | 3.52 / 3.51 | **5-6** (tied with ES; corrected from "5") | 3.50 / 3.51 | 3 | 3.93 / 4.00 | 3 | 3.36 / 3.70 / 4.19 / 3.45 / 3.80 / 4.37 / 4.35 | [E3] |
| Hospitals, PPS per inhabitant | 2024 | 1,662 | 1,481 | 1,377 / 1,410 | 7 | 1,382 / 1,439 | 5 | 1,692 / 1,670 | 5 | 1,593 / 1,410 / 1,505 / 1,795 / 1,679 / 1,869 / 2,027 | [E3] |
| Inpatient curative care (HC.1.1), % of CHE | 2024 | 22.2 | n/a | 24.5 / 22.5 (n = 24) | 13 | | | | | 22.8 / n.a. / 24.7 / 13.5 / 19.7 / n.a. / 21.7 | [E2] |
| Hospitals, % of CHE (OECD) | 2023 | 39.8 | OECD35 39.2 | | 17/35 | | | 38.7 / 39.4 | 4 | 27.2 / 43.5 / 45.4 / 34.2 / 35.3 / 38.9 / 45.6 | [O1 Fig 7.18, stat.link/7ah6wr] |
| Hospital spending: share inpatient / day / outpatient | 2023 | 63.8 / 10.8 / 12.8 | OECD33 62.5 / 6.5 / 24.5 | | | | | | | DE 91.2 / 4.1 / 4.2; DK 48.2 / 0 / 51.8; NL 38.2 / 8.4 / 45.3 | [O1 Fig 7.19, stat.link/ze0c6k] |
| Drees: hospital care (*soins hospitaliers*), EUR bn | 2025 | **124.1** (35.1% of DCSi), of which public 96.2, private 27.9 | | | | | | | | | [D1] |

Reading: compared internationally, French hospitals are not oversized relative to the rest of the health system. They are large relative to GDP, as is the whole system. French hospitals do comparatively **little outpatient activity** (12.8% vs OECD 24.5%) because specialist consultations are largely provided by self-employed doctors in town.

### 3.2 Administration and insurance management (SHA HC.7)

| Indicator | Year | France | EU-27 agg. | EA20 agg. | EU-27 mean / median | FR rank EU-27 | EA21 mean / median | FR rank EA21 | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| HC.7, **% of CHE** | 2006 | 6.01 | n/a | n/a | 3.94 / 3.96 (n = 6) | 1 | | | | | 5.45 / n.a. / 3.21 / n.a. / 4.71 / n.a. / n.a. | [E2] |
| HC.7, **% of CHE** | 2015 | 6.00 | 3.87 | 4.07 | 3.12 / 2.81 (n = 13) | 1 | 3.17 / 3.00 | 1 | 4.26 / 4.12 (n = 4) | 1 | 4.82 / n.a. / 2.81 / n.a. / 3.41 / n.a. / n.a. | [E2] |
| HC.7, **% of CHE** | 2019 | 5.66 | 3.68 | 3.85 | 2.70 / 2.34 | 1 | 2.74 / 2.52 | 1 | 3.47 / 3.60 | 1 | 4.42 / 1.56 / 2.72 / 3.71 / 3.50 / 1.46 / 4.72 | [E2] |
| HC.7, **% of CHE** | 2024 | **5.09** | 3.50 | 3.63 | 2.60 / 2.32 | **1** | 2.62 / 2.32 | 1 | 3.20 / 3.13 | 1 | 4.17 / 1.92 / 2.83 / 3.06 / 3.20 / 1.20 / 4.15 | [E2] |
| HC.7, **% of GDP** | 2024 | **0.58** | 0.36 | 0.38 | 0.23 / 0.19 | **1** | 0.24 / 0.22 | 1 | 0.34 / 0.33 | 1 | 0.51 / 0.16 / 0.26 / 0.31 / 0.35 / 0.13 / 0.40 | [E2] |
| HC.7, PPS per inhabitant | 2024 | 228 | 142 | 158 | 97 / 68 | 3 (DE 242, AT 233) | 102 / 74 | 3 | 148 / 159 | 2 | 242 / 62 / 94 / 161 / 157 / 58 / 186 | [E2] |
| HC.72 administration of health financing, % of CHE | 2024 | 4.73 | n/a | n/a | 1.50 / 1.03 (n = 25) | 1 | 1.81 / 1.65 | 1 | 2.25 / 2.14 (n = 7) | 1 | 4.11 / 1.73 / n.a. / 2.14 / 2.76 / 0.16 / 0.10 | [E2] |

**France's HC.7 by financing scheme, 2024** (EUR m; Eurostat `hlth_sha11_hchf` [E4]):

| Scheme | EUR m | % of GDP | % of CHE | Comparators (% of GDP) |
|---|---|---|---|---|
| HF.11 government | 1,171 | 0.04 | 0.35 | DE 0.01; NL 0.13; DK 0.39 |
| HF.12/13 social security + compulsory private insurance | 10,985 | 0.37 | 3.30 | DE 0.46; NL 0.14; BE 0.19 |
| HF.2 voluntary insurance (mainly *complémentaires*) | 4,750 | 0.16 | 1.43 | DE 0.04; NL 0.04; BE 0.11; ES 0.14; IT 0.10 |
| **Total HC.7** | **16,905** | **0.58** | **5.09** | EU-27 agg. 0.36; DE 0.51 |

Drees (2026 edition, 2025 data) puts the health system's management costs (*gestion du système de santé*) at ~~**EUR 18 bn**~~ **EUR 17.6 bn** (5.0% of DCSi) [corrected 2026-10-25], with complementary insurers bearing **52%** of them while financing 12.3% of DCSi [D1]. **Split by financer (Drees, Table 2 "DCSi par financeur en 2025", EUR bn):** Social Security 7.2, central and local government 1.2, complementary insurers 9.2, total 17.6. Drees adds that the public share (48% in 2025) "reflects the relative weight of public management costs ... not a coverage rate" and has fallen steadily since 2010 (verified 2026-10-25 in the *Vue d'ensemble* PDF; this resolves the earlier gap). Part of the complementary insurers' costs sits in HF.122 (collective mandatory contracts), not HF.2. That explains why the SHA split (HF.2 = 28% of HC.7) is lower than Drees's 52%.

**Order of magnitude (our computation):** France's excess over the EU-27 aggregate is 0.58 - 0.36 = 0.22 pp of GDP, about **EUR 6.4 bn**. Over the EA20 aggregate it is 0.20 pp, about EUR 5.9 bn (2024 GDP of about EUR 2,934 bn implied by Eurostat SHA). This is an upper bound for "administrative savings". Germany, also a multi-insurer social-insurance system, is at 0.51%. Eliminating the double layer would mean a major reform, not a trim.

**Older official assessment:** the EC-EPC *Joint Report on Health Care and Long-Term Care Systems* (2019 country document) noted that French **public** spending on health administration and insurance (0.34% of GDP, 3.9% of CHE in 2015) was "amongst the highest in the Union". It concluded that "there is perhaps scope to reduce administrative costs and improve the general management of the sector" [EC1]. No newer edition of the Joint Report was found (the 2019 update is the latest on the Commission site).

### 3.3 Other functions (shares of CHE)

| Function, % of CHE | Year | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | Panel | Src |
|---|---|---|---|---|---|---|---|
| Long-term care (health, HC.3) | 2024 | 15.7 | 17.2 | 12.9 / 11.5 | 10 | DE 21.9; NL 29.3; SE 27.6; BE 22.9; DK 21.0; IT 10.4; ES 10.1 | [E2] |
| Pharmaceuticals (HC.51) | 2024 | 11.5 | 13.4 | 15.9 / 14.7 | 19 | DE 14.0; IT 17.9; ES 14.9; NL 6.4; BE 10.5; SE 9.6; DK 7.3 | [E2] |
| Preventive care (HC.6) | 2024 | **2.65** | 3.30 | 2.90 / 2.89 | **17** | DE 3.84; IT 4.47; ES 3.09; NL 4.83; BE 1.80; SE 2.97; DK 2.40 | [E2] |
| Prevention (OECD) | 2023 | 2.31 | OECD32 3.37 | | | NL 5.17; DE 4.80; IT 4.64 | [O1 Fig 7.17] |
| Primary health care (OECD definition) | 2023 | 11.6 | OECD25 13.6 | | | ES 17.0; BE 15.6; DE 12.0; SE 12.0; NL 8.4 | [O1 Fig 7.16] |

---

## 4. Inputs: staff, beds, length of stay, pay

### 4.1 Doctors and nurses

| Indicator | Year | France | EU-27 mean / median (n) | FR rank EU | EA21 mean / median | FR rank EA21 | OECD mean / median (n) | FR rank OECD | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Practising physicians per 100,000 | 2005 | 310 (flag d, e) | 308 / 310 (21) | 11 | 315 / 310 | 8 | | | 335 / 340 | 6 | 340 / 372 / 355 / n.a. / 287 / 345 / 333 | [E5] |
| Practising physicians per 100,000 | 2015 | 311 (d) | 352 / 341 (23) | 19 | 359 / 345 | 16 | | | 370 / 386 | 7 | 414 / 387 / 385 / 349 / 302 / 417 / 393 | [E5] |
| Practising physicians per 100,000 | 2019 | 316 (d) | 383 / 369 (24) | 23 | 385 / 369 | 17 | | | 393 / 415 | 7 | 439 / 405 / 441 / 375 / 316 / 429 / 425 | [E5] |
| Practising physicians per 100,000 | 2024 | **394** (break "b" in 2020) | 436 / 420 (26) | **17** | 441 / 421 | 14 | | | 446 / 465 | 7 | 475 / 575 / 464 / 396 / 334 / 466 / 466 | [E5] |
| Practising doctors per 1,000 (OECD) | 2023 | 3.9 | | | | | 3.90 / 3.82 (37) | 17 | 4.32 / 4.43 | 7 | 4.66 / 5.35 / 4.39 / 3.91 / 3.37 / 4.47 / 4.53 | [O1 Fig 8.4] |
| Practising nurses per 100,000 | 2014 | 837 | 683 / 679 (23) | 8 | 692 / 679 | 6 | | | 892 / 1,013 | 6 | 1,072 / 532 / 515 / 1,033 / 1,058 / 1,096 / 993 | [E5] |
| Practising nurses per 100,000 | 2023 | **887** | 773 / 719 (26) | 10 | 800 / 719 | 8 | | | 973 / 1,073 | 6 | 1,225 / 683 / 588 / 1,113 / 1,143 / 1,100 / 1,047 | [E5] |
| Practising nurses per 1,000 (OECD) | 2023 | 8.83 | | | | | 9.17 / 9.31 (34) (published OECD37 average **9.2**; corrected label 2026-10-25) | 20 of 34 (22 of 37 if all reporting countries are counted) | 9.74 / 10.73 | 6 | 12.25 / 6.86 / 5.88 / 11.11 / 11.51 / 10.97 / 10.48 | [O1 Fig 8.13] |

**Series break:** France's practising-physician count jumps from 316 (2019) to 374 (2020) per 100,000, with flag "b". This is a change of source and definition (residents/interns included from 2020). The OECD removed France's 2013 value for the same reason ("Break in 2020"). **Do not compute a 2005-2024 French growth rate in doctors.** The *Country Health Profile 2025* says the French doctor density "has remained stable ... over the last decade" while it rose in most EU countries [O5].

### 4.2 Hospital capacity and activity

| Indicator | Year | France | EU-27 agg. | EU-27 mean / median | FR rank EU | EA21 mean / median | FR rank EA21 | OECD mean / median | FR rank OECD | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Hospital beds per 100,000 | 2005 | 722 | n/a | 592 / 646 | 8 | 592 / 611 | 6 | | | 509 / 424 | 2 | 847 / 404 / 334 / 444 / 644 / 293 / 380 | [E6] |
| Hospital beds per 100,000 | 2015 | 613 | 550 | 521 / 530 | 9 | 504 / 482 | 5 | | | 460 / 349 (n = 7) | 2 | 813 / 322 / 297 / 349 / 583 / 244 / n.a. | [E6] |
| Hospital beds per 100,000 | 2024 | **534** (-26% vs 2005) | 507 | 466 / 423 | **12** | 454 / 413 | 8 | | | 382 / 298 | 3 | 759 / 312 / 283 / 221 / 536 / 187 / 226 | [E6] |
| Hospital beds per 1,000 (OECD) | 2023 | 5.4 | | | | | | 4.20 / 3.34 (38) | 10 | 3.86 / 2.96 | 2 | 7.66 / 3.04 / 2.88 / 2.31 / 5.39 / 1.87 / 2.33 | [O1 Fig 5.19] |
| Curative bed occupancy, % | 2023 | 74.3 | | | | | | 71.4 / 70.8 (30) | 12 | 69.7 / 72.4 | 2 | 72.0 / 75.5 / 72.8 / 61.2 / 62.5 / n.a. / n.a. | [O1 Fig 5.20] |
| ALOS, curative (acute) care, days | 2019 / 2023 | 5.5 / **5.5** | | | | | | 6.42 / 6.10 (37) | 28 (short) | 6.01 / 5.75 | 5 | 7.5 / 7.1 / 6.1 / 5.2 / 6.0 / 5.3 / 5.4 | [O1 Fig 5.23] |
| ALOS, all in-patients, all hospitals (Eurostat, new series) | 2023 | 9.09 | 7.96 | 7.30 / 7.36 | 4 (long) | 7.37 / 7.56 | 2 | | | 6.92 / 6.96 | 1 | 9.0 / 8.27 / 8.11 / 4.36 / 5.8 / 5.33 / 5.44 | [E7] |
| Curative discharges per 1,000 | 2023 | 134.6 | | | | | | 128.0 / 133.0 (36) | 17 | 126.7 / 123.7 | 3 | 201.5 / 94.9 / 107.5 / 80.2 / 147.7 / 120.3 / 127.1 | [O1 Fig 5.22] |
| ED visits per 100 population | 2023 | 30.0 | | | | | | 30.8 (28) | 15 | 29.8 / 30.0 | 4 | 14.9 / 31.3 / 68.9 / 12.3 / 33.7 / 17.3 / n.a. | [O1 Fig 5.24] |
| Cataract surgery done as day case, % | 2023 | 97.3 | | | | | | 94.9 (34) | 19 | 97.2 / 98.6 | 6 | 87.9 / 98.2 / 99.1 / 99.7 / 97.0 / 98.9 / 99.5 | [O1 Fig 5.26] |

**ALOS divergence:** OECD *curative* ALOS puts France among the shortest stays (5.5 days, rank 28/37). Eurostat's *all in-patient, all hospitals* ALOS puts France among the longest (9.1 days). The Eurostat series includes rehabilitation (SMR) and psychiatric stays, which are numerous in French hospitals. The old Eurostat series (`hlth_co_inpst`) also jumps from 5.5 (2015) to 8.8 (2016) for France without a flag, which is a scope change. Use the OECD curative figure for "efficiency of acute care" and say so.

### 4.3 Hospital workforce and its weight in public pay

| Indicator | Year | France | Comparators | Src |
|---|---|---|---|---|
| Hospital workforce per 1,000 population, total | 2023 | **20.2** | OECD34 15.5 (rank ~~7/32~~ **5/32**, behind CH 27.4, UK 26.2, NO 22.9, DK 22.2 [corrected 2026-10-25]); DK 22.2; DE 18.4; NL 16.6; ES 14.3; BE 13.1; IT 11.7 | [O1 Fig 8.17, stat.link/9ari8w] |
| of which physicians / nurses and midwives / healthcare assistants / other health providers / **other staff** | 2023 | 2.78 / 5.65 / 3.68 / 1.13 / **6.93** | OECD34: 2.19 / 5.50 / 1.57 / 2.78 / **3.43**; DE 2.65 / 6.71 / 0.89 / 4.33 / 3.82; ES 2.66 / 3.99 / 3.13 / 1.25 / 3.31; DK 3.50 / 7.10 / 1.99 / 5.02 / 4.54 | [O1 Fig 8.17] |
| Public-hospital compensation of employees (COFOG GF0703, D.1), % of GDP | 2024 | **2.2** (2005: 2.1) | EU-27 agg. 1.1 (file 04) | [E11], file 04 §4.3 |
| Same, **% of total general-government compensation of employees** | 2005 / 2015 / 2019 / 2024 | 16.2 / 16.2 / 16.2 / **17.6** | EU-27 mean 2024 13.2, median 12.9, FR rank 8/27; EU-27 agg. 10.5; EA20 agg. 9.9; DK 22.5; IT 12.2; ES 10.4; SE 10.2; DE 0.0; NL 0.0; BE 0.6 | [E11] (our computation, `12_eurostat_cofog_health_pay_share.csv`) |
| All public health pay (GF07, D.1), % of total GG compensation | 2024 | 19.3 | EU-27 agg. 16.8; DK 29.1; SE 23.0; IT 22.6; ES 26.8 | [E11] |
| Social transfers in kind (D.632), % of GF07 spending | 2024 | 52.2 | EU-27 agg. 51.6; DE 85.4; NL 83.5; BE 83.4; IT 29.9; ES 22.2; SE 20.4; DK 13.6 | [E11] |

Reading:
- The 2.2% of GDP in file 04 is about **one-sixth of the French public wage bill**. It explains why France's wage bill looks larger than Germany's or the Netherlands', whose hospitals are outside general government (file 04 §4.4).
- France's half-public, half-reimbursed model (D.632 = 52% of GF07) is close to the EU average.
- The **"other staff" line (6.9 per 1,000, twice the OECD level)** is the closest international proxy for non-clinical hospital staff (administrative, technical, logistics). Classifications differ across countries (the Netherlands reports no separate "assistants" category), so treat it as indicative.

### 4.4 Pay of health professionals

| Indicator | Year | France | OECD average | DE | IT | ES | NL | BE | SE | DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Hospital nurses' remuneration / average wage | 2021 (FR) | **0.97** | 1.17 (OECD33) | 1.17 (2022) | 0.94 | 1.34 | 1.19 | n.a. | 1.00 | 1.04 | [O1 Fig 8.15, stat.link/sm9rdl] |
| Hospital nurses' remuneration, USD PPP | 2021 (FR) | 48,377 | 60,798 | 73,086 | n.a. | n.a. | 82,231 | n.a. | 56,339 | 76,965 | [O1 Fig 8.15] |
| Salaried specialists / average wage | 2021 (FR) | 2.3 | 2.79 (OECD31) | 3.2 (salaried) | 2.79 | 2.6 | 3.31 | 2.42 | 2.2 | 2.43 | [O1 Fig 8.11] |
| GP remuneration | | **France not reported** in HaaG 2025 Fig 8.9 | | | | | | | | | [O1] |

---

## 5. Outcomes

### 5.1 Avoidable mortality (age-standardized deaths per 100,000; 1 = lowest = best)

| Indicator | Year | France | EU-27 agg. | EU-27 mean / median | FR rank EU | EA21 mean / median | FR rank EA21 | OECD mean / median (n) | FR rank OECD | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Treatable (Eurostat) | 2014 | 62.9 | 94.8 | 113.3 / 89.2 | **1** | 107.5 / 87.4 | 1 | | | 72.5 / 69.8 | 1 | 87.4 / 69.0 / 68.5 / 68.6 / 74.9 / 70.5 / 78.0 | [E8] |
| Treatable (Eurostat) | 2019 | 60.3 | 89.2 | 104.5 / 79.1 | 2 | 98.0 / 77.1 | 1 | | | 65.2 / 63.1 | 2 | 81.8 / 63.7 / 62.6 / 61.4 / 65.2 / 60.2 / 66.2 | [E8] |
| Treatable (Eurostat) | 2023 | **58.8** | 86.8 | 99.2 / 74.2 | **3** (LU, SE) | 92.5 / 68.5 | 2 | | | 63.4 / 60.1 | 2 | 83.3 / 61.9 / 60.2 / 60.0 / 58.8 / 58.4 / 66.1 | [E8] |
| Treatable (OECD std pop.) | 2005 | 67 | | | | | | 110.6 / 92 (33) | 3 | 80.4 / 78.5 | 1 | 92 / 72 / 76 / 81 / 84 / 75 / 96 | [O2] |
| Treatable (OECD) | 2015 | 51 | | | | | | 81.4 / 69 (37) | 2 | 59.9 / 59 | 1 | 73 / 59 / 57 / 57 / 60 / 59 / 63 | [O2] |
| Treatable (OECD) | 2019 | 49 | | | | | | 77.8 / 61 (37) | 4 | 53.5 / 52 | 1 | 66 / 52 / 52 / 50 / 53 / 50 / 56 | [O2] |
| Treatable (OECD) | 2023 | **46** | | | | | | 78.6 / 57 (30 reporting) | **4** | 48.6 / 49 (5 reporting) | 1 | n.a. / 51 / 50 / 49 / n.a. / 47 / n.a. | [O2] |
| Preventable (Eurostat) | 2023 | 127.2 | 150.9 | 169.3 / 149.8 | 10 | 160.9 / 136.9 | 9 | | | 124.8 / 125.2 | 5 | 157.1 / 98.4 / 110.4 / 123.1 / 136.9 / 105.7 / 139.2 | [E8] |
| Preventable (OECD) | 2005 / 2023 | 141 / 103 | | | | | | 190.8 / 161 (33); 136.8 / 123.5 (30) | 10 / 11 | | 5 / 5 | 2023: IT 82; SE 86; ES 92; NL 100 | [O2] |

*Divergence:* Eurostat (2013 European standard population) gives 58.8 for 2023. OECD (2010 OECD standard population) gives 46 for 2023 and 48 for 2022 (*HaaG 2025* Fig 3.6). The levels differ because the standard populations differ; rankings are consistent. **France's treatable mortality is genuinely among the best; its preventable mortality (alcohol, tobacco, road deaths) is average to mediocre for its income level.**

### 5.2 Life expectancy and healthy life years

| Indicator | Year | France | EU-27 agg. | EU-27 mean / median | FR rank EU | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|---|---|
| Life expectancy at birth | 2005 | 80.3 | 78.4 | 77.1 / 78.7 | 3 | 79.8 / 80.0 | 3 | 79.4 / 80.9 / 80.3 / 79.6 / 79.1 / 80.7 / 78.3 | [E9] |
| Life expectancy at birth | 2024 | 83.0 | 81.5 | 80.8 / 82.0 (n = 26) | 6 | 82.8 / 82.7 | 4 | 81.2 / 83.7 / 84.0 / 81.9 / 82.4 / 83.8 / 82.0 | [E9] |
| Healthy life years at birth | 2005 | 63.5 | 60.9 | 60.1 / 60.7 | 8 | 63.5 / 63.7 | 5 | 54.6 / 67.3 / 63.3 / 64.5 / 62.4 / 63.8 / 68.4 | [E9] |
| Healthy life years at birth | 2024 (p) | 63.6 | 65.2 | 64.0 / 63.9 (26) | 15 | 65.2 / 63.8 | 5 | 62.4 / 73.4 / 68.6 / 59.5 / 63.9 / 67.5 / 62.4 | [E9] |
| Healthy life years at 65 | 2024 (p) | 10.9 | 10.3 | 9.7 / 9.6 | 10 | 11.5 / 11.6 | 6 | 8.6 / 13.1 / 12.5 / 9.6 / 11.8 / 14.2 / 11.3 | [E9] |

*Caveat:* healthy life years come from the EU-SILC self-reported limitation question (GALI) and are notoriously sensitive to national wording. For example, Italy jumped from 69.1 (2023) to 73.4 (2024); Eurostat flags Italy, Spain and Denmark "b" (break in series) in 2024, and France's 2024 value is provisional "p" (checked 2026-10-25). Do not use HLY rankings as a hard outcome measure.

### 5.3 Cancer survival (five-year age-standardized net survival, CONCORD programme via OECD)

| Cancer (patients diagnosed 2010-14) | France | OECD mean / median (n = 34) | FR rank OECD (1 = best) | Panel mean / median | FR rank panel | DE / IT / ES / NL / BE / SE / DK | Src |
|---|---|---|---|---|---|---|---|
| Breast (women) | **86.7** | 84.3 / 86.2 | 12 | 86.5 / 86.3 | 2 | 86.0 / 86.0 / 85.3 / 86.6 / 86.4 / 88.8 / 86.1 | [O3] |
| Colon | 63.7 | 61.2 / 63.5 | 16 | 64.2 / 64.0 | 5 | 64.8 / 64.2 / 63.3 / 63.1 / 67.9 / 64.9 / 61.6 | [O3] |
| Rectum | 60.9 | 59.8 / 62.4 | 21 | 63.2 / 63.5 | 7 | 62.3 / 61.3 / 59.5 / 65.3 / 66.6 / 64.7 / 64.8 | [O3] |
| Lung | 17.3 | 17.1 / 17.3 | 17 | 17.1 / 17.3 | 4 | 18.3 / 15.9 / 13.5 / 17.3 / 18.2 / 19.5 / 16.6 | [O3] |
| Stomach | 26.7 | 29.6 / 27.4 | 20 | 28.1 / 27.0 | 5 | 33.5 / 30.5 / 27.2 / 25.0 / 37.5 / 24.8 / 19.9 | [O3] |
| Cervix | 65.0 | 65.5 / 65.9 | 21 | 66.5 / 66.1 | 7 | 65.2 / 66.8 / 64.6 / 67.5 / 65.4 / 68.3 / 69.5 | [O3] |
| Childhood acute lymphoblastic leukaemia | 88.6 | 85.6 / 88.1 | 15 | 89.5 / 89.7 | 6 | 91.1 / 87.8 / 84.7 / 90.4 / 90.8 / 89.0 / 94.0 | [O3] |

*Notes.* (a) These are the latest internationally harmonized survival figures (CONCORD-3, published 2018). They are **more than a decade old**; no newer OECD-wide comparison was found. (b) France's survival estimates come from cancer registries covering about 20-25% of the population, not national data. (c) National French data show large gains from 1990 to 2015: colorectal 53% to 65%, prostate 71% to 92%, breast 79% to 89%, lung up to 22% (Coureau et al. 2021, cited in [O5]). These are not comparable with CONCORD figures. (d) Screening uptake is weak: breast 47% vs EU average 58%, colorectal 34% vs 48% (2023) [O5]. **The common claim that France has "the best cancer survival" is not supported by CONCORD-3; "around the OECD average, good for breast cancer" is accurate.**

### 5.4 Financial protection

| Indicator | Year | France | Comparator | FR rank | Src |
|---|---|---|---|---|---|
| Out-of-pocket, % of CHE | 2024 | **10.2** | EU-27 agg. 15.1; mean 19.3; median 17.0 | 3rd lowest of 27 | [E1] |
| Out-of-pocket, PPS per inhabitant | 2024 | 457 | EU-27 agg. 614; DE 643; NL 623; BE 1,065 | 21st of 27 (7th lowest) | [E1] |
| Out-of-pocket, % of household final consumption | 2023 | **2.0** | OECD38 3.2; DE 2.5; NL 2.7; DK 3.1; SE 3.3; IT 3.5; ES 3.5; BE 4.6 | **5th lowest of 38; lowest in panel** | [O1 Fig 5.8, stat.link/v23mqi] |
| Share of spending covered by public/compulsory schemes, all services | 2023 | 0.84 | OECD32 0.75; DE 0.86; SE 0.86 | 7/32 | [O1 Fig 5.7] |
| Household out-of-pocket share of DCSi (Drees) | 2025 | 9.7% (EUR 495 per inhabitant) | EU 14.8% (2024) | | [D1] |

---

## 6. Access and waiting times

### 6.1 Elective surgery waiting times (OECD): France does not report

The OECD waiting-time database (`DSD_HEALTH_PROC@DF_WAITING`, downloaded 25 Oct 2026, 7,185 records for 25 countries) contains **no records for France** (`12_oecd_waiting_times_raw.csv`). *HaaG 2025* Figs 5.11-5.12 therefore show no French data. Among reporting panel countries, median waits for hip replacement in 2024 were Sweden 67 days, Spain 67 days and Denmark 18.9% waiting over three months. Italy, Denmark, Sweden and Spain report; Germany, Belgium and the Netherlands do not appear in these figures either [O1 Figs 5.11-5.12, O4]. *(Fact-check note 2026-10-25: the Netherlands does have rows in the OECD waiting-time database (NLD among the 25 reporting countries); Germany, Belgium and France have none.)* **France cannot be ranked on elective waiting times. This is itself a transparency gap worth flagging on the platform.**

### 6.2 Patient-reported waits (Commonwealth Fund 2023 survey, via OECD *HaaG 2025*)

| % of adults | France | 10-country average (OECD10) | DE | NL | SE | UK | Canada | Src |
|---|---|---|---|---|---|---|---|---|
| Waited 2-5 days for a GP/nurse appointment | 35.3 | 30.8 | 22.5 | 31.8 | 29.7 | 23.4 | 26.6 | [O1 Fig 5.13, stat.link/fcx732] |
| Waited 6-7 days | 8.4 | 8.4 | 6.1 | 5.6 | 7.4 | 8.9 | 13.1 | idem |
| Waited more than a week | 19.8 | 17.7 | 19.5 | 6.7 | 23.3 | 18.1 | 31.7 | idem |
| **Waited 2 days or more (sum)** | **63.5** | 57.0 | 48.2 | 44.1 | 60.3 | 50.4 | 71.5 | our sum |
| Specialist: 1 month to < 2 months | 19.9 | 21.8 | 21.1 | 21.0 | 25.1 | 18.9 | 19.9 | idem |
| Specialist: 2 months to < 1 year | **43.3** | 26.4 | 22.1 | 14.7 | 29.1 | 31.7 | 37.9 | idem |
| Specialist: 1 year or more | 2.2 | 4.1 | 1.6 | 0.7 | 5.2 | 11.0 | 10.0 | idem |
| **Specialist: 1 month or more (sum)** | **65.4** | 52.3 | 44.8 | 36.4 | 59.3 | 61.6 | 67.8 | our sum |
| **Specialist: 2 months or more (sum)** | **45.5** (2nd worst of 10, after Canada ~~47.9~~ 48.0) | ~~30.5~~ 30.4 | 23.7 | 15.4 | 34.2 | 42.7 | 47.9 | our sum |

The OECD text names France with Canada and New Zealand as the countries with the longest primary-care waits [O1]. *Caveats:* subjective questions, small samples in some countries; the survey covers 10 high-income countries only (no IT, ES, BE, DK).

**Commonwealth Fund *Mirror, Mirror 2024* (10 countries):** France ranks **5th overall**. By domain: access to care 6th, care process 7th, administrative efficiency 4th, equity 6th, health outcomes 5th. Australia, the Netherlands and the UK lead; the US is last [CF1]. *Orientation:* the Commonwealth Fund is a US private foundation. Its composite ranking is sensitive to weighting, and its own simulations place France among countries "varying between the fourth and eighth ranks".

### 6.3 Emergency departments (Drees, *Enquête Urgences*, 13 June 2023)

| Indicator | 2023 | 2013 | Src |
|---|---|---|---|
| Median total length of ED stay (complete care) | just over 3 h 10 min | 2 h 15 min | [D3] ER 1372 (via file 04, verified there) |
| Median stay, patients then hospitalized | over 6 h 30 min | +1 h 45 vs 2013 | [D3] |
| Registration to triage: half of patients under / 1 in 10 over | 8 min / 30 min | | [D3] ER 1373 |
| Triage to start of medical care: half under / 1 in 10 over | 16 min / 2 h | | [D3] ER 1373 |
| Registration to start of care: half under / 1 in 10 over | 30 min / **2 h 30** | | [D3] ER 1373 |
| Search for an inpatient bed after ED: half under / 1 in 10 over | 15 min (as in 2013) / **6 h 10** (+2 h 20 vs 2013) | | [D3] ER 1373 |
| ED visits (all), change 2025 | +0.8% (after +2.5% in 2024) | | [D4] ER 1380 |

ER 1373 published 2 June 2026, updated 8 Oct 2026. The lengthening of ED stays is driven by **bed availability downstream** (the 9th-decile bed-search time rose by 2 h 20) rather than by the initial wait. This is consistent with the bed reductions in §4.2. **No harmonized international ED waiting-time indicator exists;** OECD Fig 5.24 compares ED visit rates only.

### 6.4 Physical distance

| Indicator | Year | France | OECD | Others | Src |
|---|---|---|---|---|---|
| Rural population unable to reach a hospital within 45 min drive | 2023 | **1.7%** | OECD14 16.9% | IT 4.3% (2020-21); ES 23.8%; SE 33.6% | [O1 Fig 5.15, stat.link/sun2e7] |
| Physicians per 1,000, remote vs metropolitan regions | 2022 | 2.52 vs 3.76 | OECD18 3.15 vs 4.98 | BE 3.02 vs 3.29; SE 3.87 vs 4.72 | [O1 Fig 5.14] |

France's problem is **GP availability**, not distance to a hospital.

### 6.5 Doctor activity

| Indicator | Year | France | OECD | Panel | Src |
|---|---|---|---|---|---|
| In-person doctor consultations per capita | 2013 / 2019 / 2023 | 6.3 / 5.9 / **5.4** | 2023 mean 6.5 (31) | DE 9.7; IT 9.4; NL 10.1; BE 7.9; ES 5.9; DK 5.0; SE 2.4 | [O1 Fig 5.16] |
| In-person consultations per doctor | 2023 | 1,386 | OECD33 1,908 | NL 2,580; DE 2,080; BE 2,077; IT 1,756; ES 1,344; DK 1,104; SE 514 | [O1 Fig 5.18] |

### 6.6 Medical deserts: Drees APL indicator (latest: 2024, published 22 Jul 2026)

APL (*accessibilité potentielle localisée*, local potential accessibility) is the number of GP consultations, visits or teleconsultations accessible per year per age-standardized inhabitant at commune level. It accounts for GPs in neighbouring communes and their activity.

| Indicator (GPs aged 65 or under, France excl. Mayotte) | 2022 | 2023 | 2024 | Src |
|---|---|---|---|---|
| National average APL (consultations per standardized inhabitant per year) | 3.34 | 3.29 | **3.26** (-1.1% vs 2023) | [D2] deciles file |
| Average APL of the least-served 10% of the population | 1.47 | 1.38 | **1.32** | [D2] |
| Average APL of the best-served 10% | 5.67 | 5.63 | 5.65 | [D2] |
| Ratio best-served / least-served 10% | 3.86 | 4.07 | **4.28** | [D2] |
| **Population in communes with APL < 2.5** (our computation, unstandardized population, as Drees recommends) | 16.8 m (25.0%) | 18.5 m (27.4%) | **19.6 m (29.0%)** | [D2] commune file; `12_drees_apl_gp_underserved.csv` |
| Population in communes with APL < 1.5 | 2.8 m (4.1%) | 3.4 m (5.0%) | **4.0 m (5.8%)** | idem |
| Same, all GPs (no age limit), APL < 2.5 | 10.0 m (14.9%) | 11.2 m (16.6%) | 12.3 m (18.2%) | idem |
| Nurses: APL, FTE per 100,000 standardized inhabitants | 156.4 | 156.0 | 154.8 | [D2] |
| Physiotherapists | 114.5 | 119.3 | 123.2 | [D2] |
| Dentists | 59.5 | 60.6 | 61.5 | [D2] |

**Comparability warning:**
- The "6% of the population (3.8 million) in under-served areas in 2018" figure quoted in file 04 used the **first APL methodology** (*méthode concertée V1*). Under V1 the national average was about 3.9-4.1, and the 2.5 threshold sat further below the mean. The current V2 methodology counts activity differently and includes teleconsultations, and its national mean is 3.3.
- **The 2.5 threshold therefore captures a much larger share of the population under V2 (25-29%) than under V1 (6-9%).** The two series cannot be chained, and Drees itself warns that the standardized APL "should not be used to compare trends over long periods".
- What *is* comparable: within V2 (2022-2024), all indicators deteriorate. The population below 2.5 rose by 2.8 million in two years, and the gap between best- and least-served deciles widened (ratio 3.86 to 4.28).
- Drees did not publish an official national "share under 2.5" for 2024 that we could find; the figures above are our computation from Drees's commune file. ~~The government's 2025 regulatory zoning (*zones d'intervention prioritaire*) covers a much larger share (36.7% of the population, per secondary sources [D2-sec]; not verified in the *arrêté*).~~ (corrected 2026-10-25: was "36.7% of the population") The only source found for 36.7% is *Le Quotidien du Médecin* (3 Apr 2026), which says the *zones d'intervention prioritaire* (ZIP, priority intervention zones for GP installation aid) grew "*de 30 à 36,7 % du territoire entre 2023 et 2026*", i.e. a share of **territory**, not of population, compiled from the regional ARS maps that apply the methodology *arrêté* of 9 May 2025. No national population share was found in an official source; regional ARS figures range from 16.4% (Brittany ceiling) to 28.5% (Auvergne-Rhône-Alpes) and 37% (Île-de-France) of the regional population. ⚠ unverified. **Recommendation: drop from site**; use the Drees APL figure above (29% of the population below 2.5 consultations, 2024) instead.

### 6.7 EU-SILC self-reported unmet needs: the series-break check

**France, % of population aged 16+, unmet need for a medical examination in the last 12 months** (Eurostat `hlth_silc_08`, updated 20 Oct 2026; flags as published; `12_eurostat_silc_unmet_fr_flags.csv`) [E10]:

| Year | Total: cost, distance or waiting | Waiting list | Too expensive | Too far | EU-27 total | FR flag |
|---|---|---|---|---|---|---|
| 2008 | 1.9 | 0.2 | 1.6 | | n/a | |
| 2014 | 2.8 | 0.4 | 2.3 | 0.1 | 3.9 | |
| 2015 | 1.2 | 0.3 | 0.8 | 0.0 | 3.3 | (unflagged drop) |
| 2019 | **1.2** | 0.4 | 0.8 | 0.1 | 1.7 | |
| 2020 | 2.7 | 0.5 | 2.0 | | 1.9 | **b** (break) |
| 2021 | 2.8 | 1.0 | 1.6 | | 2.0 | |
| 2022 | 3.2 | 1.0 | 2.0 | | 2.2 | **b** (break) |
| 2023 | 3.7 | 1.6 | 1.8 | | 2.4 | |
| 2024 | **4.1** | 1.8 | 2.0 | 0.3 | 2.5 | |
| 2025 | **3.7** | 1.4 | 1.9 | 0.4 | 2.4 | |

*(Component values do not always sum to the total because of rounding.)*

**Findings of the check:**
1. **Yes, there are official breaks.** Eurostat flags France "b" in **2020** and **2022**. The 2020 break coincides with Insee's redesign of the SRCV survey to comply with the EU IESS framework regulation (2019/1700). The redesign covered the new questionnaire, the weighting and imputation procedures, and a rewritten processing chain [F1]. We did not find an Insee estimate of the size of the break for this variable. The 2015 fall (2.8 to 1.2) is unflagged and unexplained.
2. **The "cost" component jumped at the break and then stopped rising** (0.8% in 2019, 2.0% in 2020 with the break flag, then 1.6-2.0% through 2025). The bulk of the 2019-2020 jump in the headline indicator (+1.5 pp) is therefore **most likely a methodological effect**, although COVID-19 in 2020 is a confounder.
3. **The "waiting list" component rose within unbroken segments:** 0.5 (2020) to 1.0 (2021), and 1.0 (2022) to 1.6 (2023) to 1.8 (2024), before easing to 1.4 (2025). This rise is a credible signal, consistent with the Commonwealth Fund specialist waits and the APL deterioration.
4. **Within the unbroken 2022-2025 segment**, the headline rose from 3.2 to 3.7%, while the EU-27 rose from 2.2 to 2.4%.
5. **Rank:** France was 10th of 27 (1 = lowest) in 2019 and **23rd of 27 in 2025**. EU-27 mean 2.77, median 2.1. Panel: DE 1.0, IT 2.5, ES 1.6, NL 0.5, BE 0.9, SE 2.1, DK 2.9. Bottom income quintile: 5.8% vs EU-27 3.7% (rank 22/27).

**OECD presentation:** *HaaG 2025* Fig 5.4 shows France at 4.1% in 2024 (waiting 1.8, cost 2.0, distance 0.3) vs OECD28 3.4%; the lowest quintile is at 6.3% vs 4.9% [O1]. The *Country Health Profile 2025* quotes **4.5%** for 2024. That figure uses a different denominator (people who reported a medical need, `hlth_silc_08b`), not the whole population. Do not mix the two.

**Recommended platform wording:** "Since the 2020-2022 redesign of the French survey, the share of people reporting a care need unmet because of waiting lists has risen, from 0.5% to 1.4-1.8%. France now ranks in the bottom third of the EU on this indicator. Part of the increase observed since 2019 comes from the change in the survey."

---

## 7. Efficiency: what the evidence says

### 7.1 Spending vs outcomes, panel (simple juxtaposition, no causal claim)

| Country | CHE, PPS per inhabitant (2024) | CHE % of GDP (2024) | Treatable mortality (2023, Eurostat) | Preventable mortality (2023) | Life expectancy (2024) | OOP % of CHE (2024) | Unmet needs (2025) | Src |
|---|---|---|---|---|---|---|---|---|
| France | 4,491 | 11.33 | 58.8 | 127.2 | 83.0 | 10.2 | 3.7 | [E1][E8][E9][E10] |
| Germany | 5,791 | 12.21 | 83.3 | 157.1 | 81.2 | 11.1 | 1.0 | idem |
| Italy | 3,225 | 8.46 | 61.9 | 98.4 | 83.7 | 23.0 | 2.5 | idem |
| Spain | 3,319 | 9.25 | 60.2 | 110.4 | 84.0 | 21.5 | 1.6 | idem |
| Netherlands | 5,254 | 10.10 | 60.0 | 123.1 | 81.9 | 11.9 | 0.5 | idem |
| Belgium | 4,892 | 11.07 | 58.8 | 136.9 | 82.4 | 21.8 | 0.9 | idem |
| Sweden | 4,777 | 11.16 | 58.4 | 105.7 | 83.8 | 12.8 | 2.1 | idem |
| Denmark | 4,471 | 9.59 | 66.1 | 139.2 | 82.0 | 14.6 | 2.9 | idem |

Reading:
- **Germany spends 29% more per head than France and does worse on every outcome in this table except unmet needs.**
- Italy and Spain obtain similar treatable mortality and longer lives with about 28% less spending per head. They do so with twice France's out-of-pocket share and with lifestyle and diet advantages that health spending does not control. Their lower preventable mortality points to the same factors.
- **France's distinctive weakness is access (waits, GP availability), not mortality.**

### 7.2 Institutional assessments

| Source | Date | Key findings relevant to efficiency | Src |
|---|---|---|---|
| Cour des comptes, *La politique d'amélioration de la qualité des soins dans les établissements de santé* (public policy evaluation) | Apr 2026 | 2,965 health establishments (1,330 public, 978 private for-profit, 667 private non-profit), about 13 million patients a year. Extrapolating OECD ratios, avoidable harm costs **over EUR 11 bn** and **unnecessary or low-value care EUR 22 bn**; hospital-acquired infections EUR 2.2-5.2 bn and about 4,000 direct deaths per year. Serious adverse events are heavily under-reported: 160,000-375,000 per year against fewer than 7,200 declared in 2024. Minimum activity thresholds are often not met (bariatric and ovarian-cancer surgery). Quality indicators are process-based rather than outcome-based. 7 recommendations. | [C2] |
| Cour des comptes, *La sécurité sociale - Rapport sur l'application des lois de financement de la sécurité sociale* (RALFSS) 2026 | May 2026 (presented 27 May 2026) | Deficit of the compulsory basic schemes plus FSV **EUR 21.6 bn in 2025** (revenue 644.4, spending 666.0), "*niveau le plus élevé depuis 2012 hors années covid*", doubled in two years. Return to balance by 2030 needs about **EUR 10 bn a year** over four years from 2027: about EUR 6 bn a year on top of the **EUR 4 bn a year already in the LFSS 2026 multi-year trajectory** (which Bernard Lejeune, president of the Court's 6th chamber, told the National Assembly's social affairs committee on 27 May 2026 "*reste à documenter*", is still to be documented; the report itself notes that the government's extra EUR 8 bn a year plan gives "*aucune piste*", no concrete lead, to substantiate it). The ONDAM 2025 was **under-executed by EUR 0.5 bn** (EUR 265.4 bn vs a EUR 265.9 bn target), after the alert committee's warning of 18 June 2025 and a summer savings plan of EUR 1.74 bn, of which EUR 1.5 bn judged "certain, probable or likely" by the committee (17 Sep 2025). ~~The multi-year ONDAM trajectory is judged not credible~~ (corrected 2026-10-25: the report calls for a "more demanding" ONDAM trajectory of 2-2.5% a year and asks the government to "define and substantiate" it). Recommendations 1 and 4: publish the ONDAM construction methodology from 2027; send the alert committee's opinion on the PLFSS ONDAM to the HCFP. (Verified in the primary 2026-10-25.) | [C1] |
| IGAS-IGF, *Face à la gravité de la situation financière des hôpitaux publics, renforcer l'efficience par une intégration territoriale* | Report dated Sep 2025 (IGAS no. 2025-030R / IGF 2025-E-023-02), published 18 Feb 2026 | Public-hospital deficit ~~"*près de 3 milliards d'euros fin 2024*"~~ "*près de 2,9 milliards d'euros fin 2024*" (report: "*estimé à -2,9 Md€ en 2024*") [corrected 2026-10-25 against the IGAS page and PDF], growing about EUR 1 bn a year over two years. Supplier, tax and social debts "*quasiment doublé entre 2015 et 2023*" (confirmed). About EUR 11 bn of new charges in 2026-2029 (**restored 2026-10-25, verified in the primary**: §1.4, PDF p. 32: "*Les charges nouvelles que le système hospitalier devrait avoir à supporter de 2026 à 2029, pourraient représenter près de 11 Md€, soit près de 3 Md€ de charges supplémentaires chaque année*"; the summary separately gives financing needs rising by "*+3 Md€ par an en moyenne*", excluding new measures and volume effects). Recommends a consolidation plan back to balance by about 2030; hospital groupings (GHT) with legal personality; pooling of support and medical-technical services; more outpatient and home hospitalization; tiered territorial care. | [I1] (IGAS page and report PDF) |
| IGAS, *La compensation financière des revalorisations salariales et de l'inflation dans les établissements publics de santé entre 2020 et 2024* | Report dated ~~Nov 2025~~ Oct 2025 (IGAS no. 2025-007R), published 18 Feb 2026 [corrected] | **EUR 1.7 bn of pay measures not compensated** to public hospitals by end-2024 (excluding inflation): EUR 1.1 bn career-progression effect (GVT), EUR 457 m Ségur measures, EUR 137 m intern pay. 2024 public-hospital deficit EUR 3.1 bn **according to DGOS forecasts cited by IGAS**; the report notes Drees's consolidated estimate is EUR 2.7-2.9 bn. | [I2] (verified in the IGAS page and PDF, 2026-10-25) |
| IGAS-IGF, *Revue de dépenses sur les prescriptions en ville et à l'hôpital* (IGF no. 2025-E-045-03 / IGAS no. 2025-048R) | Report dated Nov 2025, published 11 Jun 2026 | Prescription-driven spending in the mission's scope (health products, paramedical acts, sick-leave benefits, patient transport, laboratory tests) **EUR 81 bn in 2024, 31.6% of ONDAM**, +28.5% since 2019 (ONDAM excl. COVID: +28%). ~~measurable savings below EUR 3 bn~~ (corrected 2026-10-25: was "below EUR 3 bn") **Savings potential identified: EUR 0.8-1.4 bn**, reachable only in the medium term, against the EUR 3 bn target set for the mission. The *liste en sus* (costly drugs and devices billed outside hospital tariffs) rose 57% in 2020-2024; hospital prescriptions dispensed in town (PHEV) reached EUR 19.7 bn (+49% since 2019) and are poorly traceable. (Verified in the primary 2026-10-25.) | [I3] |
| Drees, ER 1380 | 28 Jul 2026 | Public-hospital deficit **2.1% of revenue in 2025** (first estimate), down from 2024. Investment effort down. Health-establishment headcount +1.0% (after +0.7%). | [D4] |
| EC-EPC Joint Report, France country document | Jun 2019 | Public administration costs among the EU's highest; scope to reduce administrative costs; unclear division of responsibilities between the State, regions (ARS) and insurance funds. | [EC1] |
| OECD *Country Health Profile 2025* | Dec 2025 | Strong treatable mortality; GP shortages in under-served areas; beds 5.4 per 1,000 vs EU 5.1; doctor density stable and below EU average; nurses 8.8 vs EU 8.5; screening below average; 597 days average time to reimbursement for new medicines (EU 578); over 40% of patients over 75 receive at least one potentially inappropriate prescription. | [O5] |

**Not found (gap):** a 2026 Cour des comptes thematic report specifically on hospital efficiency or productivity; the HCFP opinion on PLFSS 2027 health lines; and the ONDAM 2026-2027 figures (not re-extracted here; see files 01 and 06).

---

## 8. Economists' disagreements and the steelman

### 8.1 The platform's thesis applied to health

"Health spending is high (3rd in the EU in % of GDP). Its structure (administration, duplicated insurance, hospital-centric model, weak prevention) should be questioned before adding money." Supported by: HC.7 rank 1 (§3.2); hospital "other staff" twice the OECD level (§4.3); prevention below average (§3.3); Cour des comptes low-value care estimate (§7.2); stable outcome rankings despite the highest spending ratio in 2005-2015.

### 8.2 Steelman: the strongest counter-arguments

1. **"France does not spend that much per patient."** In PPS per inhabitant France ranks 8th of 27 and 5th of 8 in the panel, below Germany, the Netherlands, Belgium and Sweden [E1]. The high GDP ratio partly reflects France's lower GDP per head, not a lavish system.
2. **"It is cheap per unit and has been tightly controlled."** Health prices are 32% below the OECD average and the lowest relative to the economy in the panel [O1 Figs 7.6/7.8]. Hospital nurses earn less than the average worker (0.97 vs OECD 1.17) [O1 Fig 8.15]. Real per-capita spending grew 0.7%/yr in 2014-19, a quarter of the OECD pace [O1 Fig 7.5]. The ONDAM was executed below target in 2025 [C1]. Cuts would hit wages and capacity already under strain: hospital deficits of EUR 2.9-3.1 bn in 2024 and EUR 1.7 bn of uncompensated pay measures [I1][I2].
3. **"Outcomes are among the best where the health system matters most."** Treatable mortality is 3rd lowest in the EU and 4th in the OECD [E8][O2]. Financial protection is the best in the panel (OOP 2.0% of household consumption) [O1 Fig 5.8]. Hospitals are physically accessible (1.7% of rural residents beyond 45 min vs OECD 16.9%) [O1 Fig 5.15].
4. **"Low out-of-pocket costs are a deliberate social choice with measurable equity value."** France's OOP share (10.2% of CHE) is half that of Italy, Spain or Belgium [E1]. Moving to their model would shift several points of GDP of spending onto households, not save it.
5. **"High administration is the price of solidarity plus choice."** The complementary-insurance layer covers about 96% of the population [EC1] and is partly mandated by law (ANI 2016, *complémentaire santé solidaire*). Germany, also a multi-insurer system, has similar administration costs (0.51% of GDP).
6. **"The access problem calls for more, not less."** Doctor density is below the EU median and its growth lagged the EU (§4.1). APL is deteriorating (§6.6). Specialist waits are among the longest in the Commonwealth Fund sample (§6.2). These point to under-capacity in primary and specialist care.

### 8.3 Replies (what the steelman does not settle)

- Low unit prices and high volumes (volume index 128, 4th in the OECD) suggest the inefficiency lies in **utilization**: too many low-value acts, long rehabilitation and psychiatric stays, prescriptions. The Cour des comptes' EUR 22 bn low-value-care estimate and IGAS-IGF's prescription review point the same way, but both are extrapolations.
- Administration and complementary-insurance overheads (EUR 16.9-17.6 bn; SHA 2024 vs Drees 2025) do not produce care. At constant coverage, a single-payer or better-integrated design could save a few billion euros. The order of magnitude is **about EUR 5-6 bn at most**, small relative to the overall spending gap with the euro area of **+7.6 pp of GDP, about EUR 227 bn, vs the EA21 aggregate in 2025** (file 00, row 7; EA20: +7.5 pp, EUR 225 bn) (corrected 2026-10-25: was "about EUR 225 bn", unlabeled).
- **Cancer survival is average** (§5.3). Preventable mortality is mediocre and prevention spending is low (§3.3, §5.1). "Best health system in the world" (the WHO 2000 ranking) is obsolete and should not be quoted.

### 8.4 Points of genuine disagreement

| Question | Position A | Position B | Sources |
|---|---|---|---|
| Is French health spending "too high"? | Yes, % of GDP 3rd in the EU, and the structure (admin, duplication) is inefficient (EC 2019, Cour des comptes) | No, per capita in PPS it is mid-pack among rich peers, unit costs are low and outcomes good (OECD price/volume data) | [EC1][C2][O1] |
| Do complementary insurers add value? | They duplicate management costs (52% of system admin for 12.3% of financing) | They provide choice and cover what basic insurance does not (optical, dental, audio) | [D1] |
| Are hospitals over- or under-funded? | Deficits reflect inefficiency and fragmentation (IGAS-IGF: integration, pooling) | Deficits reflect uncompensated pay and inflation (IGAS: EUR 1.7 bn) | [I1][I2] |
| Is the access deterioration real? | Yes: APL, CMWF waits, ED times | Partly measurement: SILC break, APL methodology change | §6.6, §6.7 |

---

## 9. Divergences between sources (summary)

| Item | Source A | Source B | Reason |
|---|---|---|---|
| CHE 2025 | Eurostat 11.48% of GDP (EUR 343.4 bn, provisional) | Drees 11.8% (EUR 353.2 bn) | Drees 2026 edition revised series; Eurostat holds the earlier transmission |
| CHE 2024 | Eurostat 11.33% | OECD *HaaG 2025* 11.54%; Drees 11.7% | Vintages and revisions |
| CHE 2023 | Eurostat 11.33% | WHO GHED 11.52%; Country Health Profile 11.5% | Vintages |
| Public share of CHE | Eurostat HF.1 83.3% (2024) | Drees 77.4% (public administrations, 2025); OECD Fig 7.11 78.0% (government + social insurance, France 2022) | HF.1 includes compulsory private insurance (HF.122, about 6.7% of CHE in France) |
| Health gap vs euro area | COFOG +1.5 pp of GDP | SHA HF.1 +1.0 pp | Perimeter (§1.3) |
| Treatable mortality 2023 | Eurostat 58.8 per 100,000 | OECD 46 | Standard population (ESP 2013 vs OECD 2010) |
| ALOS | OECD curative 5.5 days | Eurostat all in-patient 9.1 days | Scope (SMR/psychiatry included in Eurostat) |
| Unmet needs 2024 | Eurostat/OECD 4.1% (all 16+) | Country Health Profile 4.5% | Denominator (people with a need) |
| Under-served GP population | Drees V1: 6% (3.8 m), 2018 | Our V2 computation: 29% (19.6 m), 2024, APL < 2.5 | APL methodology change; not chainable |
| Physicians per 100,000 | 316 (2019) | 374 (2020) | Series break in 2020 (Eurostat "b"; OECD "break") |
| WHO GGHE-D France 2023 | 67.7% of CHE | Eurostat/Drees about 77-83% | Probable WHO classification artifact; do not use |

---

## 10. Corrections and qualifications to earlier files

1. **File 04, §6.2 and line 484; file 10 (health access):** "Unmet needs tripled between 2019 and 2025" should be qualified. The French EU-SILC series has official breaks in 2020 and 2022 (§6.7). Replace with the wording in §6.7.
2. **File 04, §6.2 caution** ("We did not check whether a change in the French EU-SILC questionnaire contributed"): **now checked.** Eurostat flags breaks in 2020 and 2022, and the cost component's jump coincides with the 2020 break.
3. **File 04, medical deserts** ("6% ... 2018 ... a 2023-2025 update was not found"): the update exists (Drees APL 2022-2024, published 22 Jul 2026). It is not comparable with 2018 because of the methodology change (§6.6).
4. **File 04, §6.2 physicians "below EU median":** confirmed (17th of 26 in 2024). Add the warning that the 2020 series break prevents any long-run growth comparison.
5. **File 10, "Hospital-sector indicators (beds, staff, waiting times) not compiled":** compiled in §4 and §6. France does not report elective waiting times to the OECD.
6. **File 01/09 health gap:** ~~+1.45 pp COFOG~~ (corrected 2026-10-25) **+1.47 pp of GDP in 2024 vs the EA21 aggregate, 19% of the 7.84 pp gap** (file 00, row 9 and log #8). Consistent. Add that on the SHA concept the public gap is about 1.0 pp (§1.3).

---

## 11. Sources

### 11.1 Source table

| ID | Institution | Title / dataset | Publication / update date | URL |
|---|---|---|---|---|
| E1 | Eurostat | Health care expenditure by financing scheme (`hlth_sha11_hf`) | Updated 23 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_sha11_hf/default/table |
| E2 | Eurostat | Health care expenditure by function (`hlth_sha11_hc`) | Updated 23 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_sha11_hc/default/table |
| E3 | Eurostat | Health care expenditure by provider (`hlth_sha11_hp`) | Updated 16 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_sha11_hp/default/table |
| E4 | Eurostat | Health care expenditure by function and financing scheme (`hlth_sha11_hchf`) | Updated 23 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_sha11_hchf/default/table |
| E5 | Eurostat | Health personnel (`hlth_rs_prs2`) | Updated 13 Jul 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_rs_prs2/default/table |
| E6 | Eurostat | Hospital beds by function and type of care (`hlth_rs_bds1`) | Updated 13 Jul 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_rs_bds1/default/table |
| E7 | Eurostat | In-patient average length of stay (`hlth_talos1`, 2022-2023; historical `hlth_co_inpst`, to 2021) | 12 Mar 2026; 3 Jan 2024 | https://ec.europa.eu/eurostat/databrowser/view/hlth_talos1/default/table ; https://ec.europa.eu/eurostat/databrowser/view/hlth_co_inpst/default/table |
| E8 | Eurostat | Treatable and preventable mortality (`hlth_cd_apr`) | Updated 17 Mar 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_cd_apr/default/table |
| E9 | Eurostat | Healthy life years and life expectancy (`hlth_hlye`) | Updated 17 Jul 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_hlye/default/table |
| E10 | Eurostat | Self-reported unmet needs for medical examination (`hlth_silc_08`) | Updated 20 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/hlth_silc_08/default/table |
| E11 | Eurostat | General government expenditure by function (`gov_10a_exp`), D.1, D.632, TE, MIO_EUR | Updated 21 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table |
| O1 | OECD | *Health at a Glance 2025: OECD Indicators* (revised version March 2026); StatLinks cited per figure | 13 Nov 2025 (rev. Mar 2026) | https://doi.org/10.1787/8f9e3f98-en ; PDF: https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/11/health-at-a-glance-2025_a894f72e/8f9e3f98-en.pdf ; waiting times: https://www.oecd.org/en/publications/2025/11/health-at-a-glance-2025_a894f72e/full-report/waiting-times_3a1021fa.html |
| O2 | OECD | OECD Health Statistics, Avoidable mortality (`DSD_HEALTH_STAT@DF_AM`), API | Downloaded 25 Oct 2026 | https://sdmx.oecd.org/public/rest/data/OECD.ELS.HD,DSD_HEALTH_STAT@DF_AM,/all?startPeriod=2004 |
| O3 | OECD | Health Care Quality and Outcomes, Cancer care (`DSD_HCQO@DF_CC`; CONCORD-3 net survival) | Downloaded 25 Oct 2026 | https://sdmx.oecd.org/public/rest/data/OECD.ELS.HD,DSD_HCQO@DF_CC,/all |
| O4 | OECD | Waiting times (`DSD_HEALTH_PROC@DF_WAITING`) | Downloaded 25 Oct 2026 | https://sdmx.oecd.org/public/rest/data/OECD.ELS.HD,DSD_HEALTH_PROC@DF_WAITING,/all?startPeriod=2004 |
| O5 | OECD / European Observatory / European Commission | *State of Health in the EU - France: Country Health Profile 2025* | Dec 2025 | https://www.oecd.org/content/dam/oecd/en/publications/reports/2025/12/country-health-profile-2025-country-notes_7e72146d/france_37ac3463/b3c2743a-en.pdf |
| W1 | WHO | Global Health Expenditure Database via GHO OData API (`GHED_CHEGDP_SHA2011`, `GHED_GGHE-DGDP_SHA2011`, `GHED_GGHE-DCHE_SHA2011`) | Downloaded 25 Oct 2026 | https://ghoapi.azureedge.net/api/GHED_CHEGDP_SHA2011 |
| D1 | Drees | *Les dépenses de santé en 2025 - Résultats des comptes de la santé - Édition 2026* (Panorama), and *Combien coûte la santé en France ? Qui paie ?* | 1 Oct 2026; 14 Oct 2026 | https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse-infographie-documents-de-reference/261001-les-d%C3%A9penses-de-sant%C3%A9-en-2025-edition-2026-panorama-de-la-drees ; https://drees.solidarites-sante.gouv.fr/actualites-evenements/combien-coute-la-sante-en-france-qui-paie ; overview PDF saved at `data/raw/12/drees/cns2026/cns2025_vue_ensemble.pdf` |
| D2 | Drees | *L'accessibilité potentielle localisée (APL)*: dataset (commune files 2022-2024, deciles file) and data release "Accessibilité aux soins de premier recours en 2024" | 22 Jul 2026 | https://data.drees.solidarites-sante.gouv.fr/explore/dataset/530_l-accessibilite-potentielle-localisee-apl/information/ ; https://drees.solidarites-sante.gouv.fr/communique-de-presse-jeux-de-donnees/jeux-de-donnees/260722-accessibilite-aux-soins-de-premier-recours-en-2024 |
| D2-sec | *Le Quotidien du Médecin* (press) | ZIP coverage "*de 30 à 36,7 % du territoire entre 2023 et 2026*" (share of territory, from regional ARS maps under the *arrêté* of 9 May 2025) (corrected 2026-10-25: was described as "36.7% of the population" from the *arrêté*) | 3 Apr 2026 | https://www.lequotidiendumedecin.fr/jeunes-medecins/installation/en-trois-ans-les-zones-dintervention-prioritaire-zip-ont-progresse-de-pres-de-7-sur-lensemble-du (⚠ no official national figure found) |
| D3 | Drees | *Études et Résultats* no. 1372 (ED length of stay) and no. 1373 (*Attente aux urgences : des durées contrastées*) | 2 Jun 2026 (updated 8 Oct 2026) | https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/etudes-et-resultats/260602-urgences-duree-de-passage-augmente-en-dix-ans-patients-parcours-longs ; https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/etudes-et-resultats/260602-attente-urgences-durees-contrastees |
| D4 | Drees | *Études et Résultats* no. 1380, *Le déficit des hôpitaux publics diminue en 2025 mais reste à un niveau élevé* | 28 Jul 2026 | https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/etudes-et-resultats/260728-deficit-des-hopitaux-publics |
| C1 | Cour des comptes | *La sécurité sociale - Rapport sur l'application des lois de financement de la sécurité sociale*, May 2026 (RALFSS 2026); hearing of B. Lejeune, Assemblée nationale social affairs committee, *compte rendu* no. 79 | May 2026; hearing 27 May 2026 | https://www.vie-publique.fr/files/rapport/pdf/303409.pdf (official copy of the Cour PDF; saved at `data/raw/12/docs/ralfss2026_vp.pdf`); https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L17S2026PO420120N079.html ; press: https://acteurspublics.fr/articles/la-cour-des-comptes-appelle-a-un-choc-de-10-milliards-deconomies-par-an-sur-les-comptes-sociaux-des-2027-la-rue-cambon-appelle-a-rendre-a-lobjectif-national-des-depenses-dassurance-maladie/ |
| C2 | Cour des comptes | *La politique d'amélioration de la qualité des soins dans les établissements de santé*, public policy evaluation | Apr 2026 | https://www.vie-publique.fr/files/rapport/pdf/303029.pdf (copy at `data/raw/12/docs/ccomptes_qualite_soins_2026.pdf`) |
| I1 | IGAS-IGF | *Face à la gravité de la situation financière des hôpitaux publics, renforcer l'efficience par une intégration territoriale* (IGAS 2025-030R / IGF 2025-E-023-02) | Sep 2025, published 18 Feb 2026 | https://igas.gouv.fr/face-la-gravite-de-la-situation-financiere-des-hopitaux-publics-renforcer-lefficience-par-une-integration-territoriale ; PDF: https://igas.gouv.fr/sites/igas/files/2025-12/Sitiuation_financi%C3%A8re_des_h%C3%B4pitaux%20publics%2C_renforcer_l%27efficience_par_une_int%C3%A9gration_territoriale_%28Igas-IGF%29.pdf (copy at `data/raw/12_factcheck/igas_igf_hopitaux.pdf`) |
| I2 | IGAS | *La compensation financière des revalorisations salariales et de l'inflation dans les établissements publics de santé entre 2020 et 2024* | Oct 2025 (published 18 Feb 2026) | https://igas.gouv.fr/la-compensation-financiere-des-revalorisations-salariales-et-de-linflation-dans-les-etablissements-publics-de-sante-entre-2020-et-2024 |
| I3 | IGAS-IGF | *Revue de dépenses sur les prescriptions en ville et à l'hôpital* (IGF 2025-E-045-03 / IGAS 2025-048R) | Nov 2025, published 11 Jun 2026 | https://igas.gouv.fr/revue-de-depenses-sur-les-prescriptions-en-ville-et-lhopital ; PDF: https://igas.gouv.fr/sites/igas/files/2026-06/Rapport%20Igas-IGF%20Revue%20de%20d%C3%A9penses%20Prescriptions%20en%20ville%20et%20%C3%A0%20l%27h%C3%B4pital%20%282026%29.pdf (copy at `data/raw/12/docs/igas_igf_prescriptions_2026.pdf`) |
| EC1 | European Commission (DG ECFIN) and Economic Policy Committee | *Joint Report on Health Care and Long-Term Care Systems and Fiscal Sustainability - Country Documents 2019 Update*, France (Institutional Paper 105) | Jun 2019 | https://economy-finance.ec.europa.eu/publications/joint-report-health-care-and-long-term-care-systems-and-fiscal-sustainability-country-documents-2019_en |
| CF1 | Commonwealth Fund (US private foundation) | Blumenthal et al., *Mirror, Mirror 2024: A Portrait of the Failing U.S. Health System*, Exhibit 1 | Sep 2024 | https://www.commonwealthfund.org/publications/fund-reports/2024/sep/mirror-mirror-2024 ; https://doi.org/10.26099/ta0g-zp66 |
| F1 | Insee | SRCV survey metadata (*Statistiques sur les ressources et conditions de vie*): "*En 2020, l'enquête SRCV a été refondue, afin de se conformer au règlement IESS*" | Metadata pages 2021-2025 | https://www.insee.fr/fr/metadonnees/source/operation/s2111/processus-statistique |
| R01 / R04 / R09 / R10 | This project | Files 01 (spending overview), 04 (civil service and outcomes), 09 (international tables), 10 (debates) | 2026-10-25 | `research/0x-*.md` |

### 11.2 Raw files

- Eurostat JSON and CSV: `research/data/raw/12/eurostat/*.json`, `research/data/raw/12/eurostat/csv/*.csv` (sha_hf, sha_hc, sha_hp, hchf, hf_fr, hf_pub, prs1, nrs, bds1, alos, talos, cd_apr, hlye, silc08, cofog_d1)
- OECD: `research/data/raw/12/oecd/{waiting,am,cc}.csv`; HaaG 2025 PDF, text and 41 StatLink workbooks in `research/data/raw/12/oecd/haag2025/` (`statlinks.txt` maps figures to StatLinks)
- WHO GHED JSON: `research/data/raw/12/who/`
- Drees: `research/data/raw/12/drees/apl_mg.xlsx`, `apl_deciles.xlsx`, `apl_lisezmoi.pdf`, `cns2026/cns2025_vue_ensemble.pdf`
- Documents: `research/data/raw/12/docs/` (Cour des comptes April 2026, Country Health Profile 2025, EC Joint Report 2019 France, CMWF Exhibit 1 PNG; added 2026-10-25: `ralfss2026_vp.pdf` (Cour RALFSS May 2026), `igas_igf_prescriptions_2026.pdf`, text extracts `r.txt`, `p.txt`, `hop.txt`, `chpu.txt`)
- Second-pass OECD StatLinks (fresh download 2026-10-25): `research/data/raw/12_factcheck/haag_pass2/` (23 workbooks plus `.txt` dumps); Eurostat `hlye_pass2.json`, `talos_pass2.json` in `research/data/raw/12_factcheck/`

### 11.3 Computed CSVs (`research/data/`)

| File | Content |
|---|---|
| `12_computed_stats.csv` | Eurostat indicators x year: France, EU-27 and EA aggregates, EU-27/EA21/panel mean, median, rank, panel values |
| `12_eurostat_health_long.csv` | All Eurostat series used, long format, with flags |
| `12_eurostat_silc_unmet_fr_flags.csv` | EU-SILC unmet needs by reason, FR and panel, with break flags |
| `12_eurostat_sha_public_excl_compulsory_private.csv` | HF.11 + HF.121, % of GDP and of CHE |
| `12_eurostat_cofog_health_pay_share.csv` | Hospital and health D.1 as % of total GG D.1; D.632 and D.1 as % of GF07 |
| `12_who_ghed_che_stats.csv`, `12_who_ghed_raw.csv` | WHO CHE % of GDP, 2000-2023, group statistics |
| `12_fr_che_gap_timeseries.csv` | France gap vs EU-27/EA21/OECD/panel means (WHO) and EU-27/EA20 aggregates (Eurostat) |
| `12_oecd_avoidable_mortality_stats.csv`, `12_oecd_avoidable_mortality_raw.csv` | OECD treatable/preventable/avoidable mortality |
| `12_oecd_cancer_survival_stats.csv`, `12_oecd_cancer_survival_raw.csv` | CONCORD five-year net survival via OECD |
| `12_oecd_waiting_times_raw.csv` | OECD waiting-time database (no France rows) |
| `12_oecd_haag2025_computed_stats.csv`, `12_oecd_haag2025_statlinks_long.csv` | HaaG 2025 StatLink extracts and OECD-38 statistics |
| `12_drees_apl_gp_underserved.csv` | Population below APL thresholds, 2022-2024 |

---

## 12. Open questions and gaps

1. **OECD SHA 2005 per capita in PPP and OECD-38 2005 public share:** the OECD SDMX API returned HTTP 429 (rate limit) and then "NoResultsFound" for our SHA key; WHO GHED per-capita PPP returned no data. For 2005 we used WHO CHE % of GDP only. Eurostat SHA starts in 2006 for France (12 countries only before 2014).
2. **Size of the 2020 SRCV break** for unmet needs: no Insee or Eurostat estimate found.
3. **Cour des comptes 2026 documents:** ~~the RALFSS was read via press coverage only~~ the RALFSS 2026 was read in the primary PDF on 2026-10-25 (resolved). No 2026 thematic report on hospital productivity was found.
4. **Drees full CNS 2026 PDF** blocked by the Drees web application firewall (HTTP "Request Rejected"). ~~The management-cost breakdown by financer (beyond "52% complementary insurers") was not extracted.~~ Resolved 2026-10-25: the overview PDF's Table 2 gives the split (Social Security 7.2, State and local government 1.2, complementary insurers 9.2 of EUR 17.6 bn).
5. **Elective-surgery waiting times for France:** not reported to the OECD. A national source (ATIH/PMSI-based waits) was not searched.
6. **Cancer survival after 2014:** no newer international comparison (CONCORD-4 not yet published as far as we found).
7. **COFOG vs SHA reconciliation** (about 0.5 pp of GDP): not decomposed line by line.
8. **OECD HaaG "other staff" in hospitals:** classification comparability not documented country by country.
9. **The figure of 36.7% in priority GP zones (*ZIP*):** the only source is press, and it describes a share of **territory** (2026), not of population. No official national population share was found (2026-10-25). Drop from site.

---

## Verification log (2026-10-25)

*An adversarial fact-check of the key figures, made against primary sources on 2026-10-25. Every value below was recomputed from a fresh download or re-read in the original document, not taken from this file's own CSVs. The fresh raw files are in `research/data/raw/12_factcheck/`, and the recomputed values are in `research/data/12_factcheck_recomputed_2026-10-25.csv`. Struck-through text in the body shows each correction.*

### A. Confirmed (recomputed or read in the primary source)

| Claim | Result | Primary source checked |
|---|---|---|
| CHE 11.33% of GDP (2024), EU rank 3/27 (DE 12.21, AT 11.71); EU-27 agg. 10.16; EA20 agg. 10.46; EU mean 8.87, median 8.54 | Exact match | Eurostat `hlth_sha11_hf` API (updated 23 Oct 2026) |
| 2025 provisional: 11.48% (p), EUR 343.4 bn; rank 3 of 15 reporting | Exact match | Same |
| CHE 4,491 PPS per inhabitant (2024), EU rank 8/27, panel rank 5/8; EU-27 4,075; EA20 4,342; DE 5,791 | Exact match (4,490.89) | Same |
| HF.1 9.44% of GDP, rank 3/27; EA20 8.40; EU-27 8.17; HF.122 0.76% of GDP (EUR 22.2 bn); HF.122 = 0 in 2015 | Exact match | Same |
| HC.7 5.09% of CHE, 0.58% of GDP, EUR 16,905 m, rank 1/27; EU-27 agg. 3.50% / 0.36%; scheme split 1,171 / 10,985 / 4,750 | Exact match | Eurostat `hlth_sha11_hc`, `hlth_sha11_hchf` (23 Oct 2026) |
| HP.1 37.0% of CHE, rank 20/27, EU mean 40.0; 4.19% of GDP | Match; **GDP rank is a tie** (see B) | Eurostat `hlth_sha11_hp` (16 Oct 2026) |
| WHO GHED gap vs unweighted EU-27 mean: +2.52 (2005), +3.28 (2015), +2.89 (2019), +2.89 (2023); EA20 agg. gap +0.87 (2024) | Exact match | WHO GHO API `GHED_CHEGDP_SHA2011`; Eurostat |
| Drees: DCSi 2025 EUR 353.2 bn = 11.8% of GDP (11.7% in 2024); complementary insurers 52% of management costs, 12.3% of DCSi; EU average 10.5% | Match (management costs are EUR 17.6 bn, see B) | Drees, *Les dépenses de santé en 2025*, 2026 edition, *Vue d'ensemble* PDF |
| OECD Fig 7.4: USD 7,367 PPP, OECD-38 average 5,967, rank 12/38 | Exact match | stat.link/rkae5h (fresh download) |
| OECD Fig 7.1: France 11.54%, rank 5/38 (US, DE, AT, CH) | Exact match | stat.link/15fht6 |
| OECD Fig 7.5: 0.68 and 0.87 %/yr (OECD 2.69 and 2.53) | Exact match | stat.link/nwmzh5 |
| OECD Figs 7.6-7.8: health price level 68.1 (rank 22/37), economy-wide 96.1, volume 127.7 (rank 4/37, after US, DE, CH) | Exact match | stat.link/zw0b9d, lmb3wn, tfnguq |
| OECD Fig 8.17: 20.2 hospital workers per 1,000; OECD34 15.5; "other staff" 6.93 vs 3.43 | Values match; **rank wrong** (see B) | stat.link/9ari8w |
| COFOG GF0703 D.1: 17.6% of GG compensation, 2.2% of GDP (2005: 2.1), EU rank 8/27, mean 13.2, median 12.9, EU-27 agg. 10.5, EA20 agg. 9.9 | Exact match | Eurostat `gov_10a_exp` (21 Oct 2026) |
| Beds 534 per 100,000 (2024), 722 (2005), -26%, rank 12/27, EU-27 agg. 507 | Exact match | Eurostat `hlth_rs_bds1` (13 Jul 2026) |
| Physicians 394 per 100,000 (2024), rank 17/26, median 420; 316 (2019, flag d) to 374 (2020, flag b) | Exact match | Eurostat `hlth_rs_prs2` (13 Jul 2026) |
| Treatable mortality 58.8 (2023), rank 3/27 (LU 51.7, SE 58.4), EU-27 86.8; OECD 46, rank 4/30 (CH, LU, KR) | Exact match | Eurostat `hlth_cd_apr` (17 Mar 2026); OECD `DF_AM` API |
| CONCORD-3: breast 86.7 (12), colon 63.7 (16), lung 17.3 (17), rectum 60.9 (21) of 34; means 84.3 / 61.2 / 17.1 / 59.8 | Match. Breast, colon and lung ranks are **ties** (two countries on the same value). Ranks shown are "1 + number strictly higher". | OECD `DF_CC` API (point estimates only; the dataflow also holds CI bounds) |
| OOP 2.0% of household consumption, 5th lowest of 38 (after TR, LU, CO, PL); OECD-38 3.2 | Match (2.035; PL 1.998) | stat.link/v23mqi |
| CMWF 2023: 65.4% wait 1 month or more (OECD10 52.3); 45.5% wait 2 months or more, 2nd worst after Canada | Match | stat.link/fcx732 |
| No French rows in the OECD waiting-time database | Confirmed: 7,185 records, 25 countries, no FRA, no DEU, no BEL | OECD `DF_WAITING` API (fresh download) |
| APL < 2.5 (GPs aged 65 or under): 19.6 m (29.0%) in 2024; 25.0% in 2022 | Reproduced exactly (19,620,523; 28.96%) | Drees APL commune file; dataset modified 22 Jul 2026 (API metadata) |
| EU-SILC unmet needs FR: 1.2 (2019), 2.7 b (2020), 3.2 b (2022), 4.1 (2024), 3.7 (2025); rank 23/27 (2025); components and flags | Exact match | Eurostat `hlth_silc_08` (20 Oct 2026) |
| ED waits: 1 in 10 waits more than 2 h 30 before care starts; 9th-decile bed search more than 6 h 10 (+2 h 20 vs 2013) | Verbatim match | Drees ER 1373 page (published 2 Jun 2026, updated 8 Oct 2026), read in a browser |
| Drees ER 1380: deficit 2.1% of revenue in 2025; ED visits +0.8% after +2.5% | Verbatim match | Drees ER 1380 page (28 Jul 2026), read in a browser |
| Cour des comptes: avoidable harm "over EUR 11 bn", low-value or unnecessary care "EUR 22 bn" (OECD-based extrapolations); 2,965 establishments; 160,000-375,000 serious adverse events vs fewer than 7,200 declared; about 4,000 deaths from hospital-acquired infections | Verbatim match | Cour des comptes PDF (Apr 2026), vie-publique.fr/files/rapport/pdf/303029.pdf |
| IGAS: EUR 1.7 bn uncompensated (1.1 bn GVT, 457 m, 137 m) | Verbatim match | IGAS web page and report PDF no. 2025-007R |
| Commonwealth Fund *Mirror, Mirror 2024*: France 5th overall; access 6, care process 7, administrative efficiency 4, equity 6, outcomes 5; "between the fourth and eighth ranks" | Match | CMWF Exhibit 1 and the live report page (read in a browser; curl gets HTTP 403) |

### B. Corrections made in the body

| Location | Original | Corrected | Evidence |
|---|---|---|---|
| §0.3 and §3.1 table | HP.1 % of GDP "rank 5/27" | **Rank 5-6/27, tied with Spain (both 4.19)** | Eurostat `hlth_sha11_hp` |
| §0.4, §3.2, §8.3 | Drees management costs "EUR 18 bn" | **EUR 17.6 bn** (5.0% of DCSi, 2025) | Drees *Vue d'ensemble*, table line "*Gestion du système de santé* 17,6" |
| §4.3 | Hospital workforce "rank 7/32" | **Rank 5/32** (after CH 27.4, UK 26.2, NO 22.9, DK 22.2) | stat.link/9ari8w |
| §6.2 | OECD10 "2 months or more" 30.5; Canada 47.9 | **30.4; 48.0** (26.35 + 4.08; 37.92 + 10.03) | stat.link/fcx732 |
| §7.2, IGAS-IGF row | "*près de 3 milliards d'euros fin 2024*" | **"*près de 2,9 milliards*"** (report: -2.9 Md€). The report is dated Sep 2025 and was published 18 Feb 2026. | IGAS page and PDF |
| §7.2, IGAS-IGF row | "About EUR 11 bn of new charges in 2026-2029" | ~~**⚠ unverified.**~~ The primary gives "+3 Md€ per year on average" of extra financing needs. **Superseded in the second pass:** the EUR 11 bn is in the report body (§1.4, p. 32) and was restored (E.1). | IGAS-IGF PDF, summary and §1.4 |
| §7.2 and §11.1, IGAS row | Dated "Nov 2025"; "2024 deficit EUR 3.1 bn" | **Report Oct 2025 (2025-007R), published 18 Feb 2026.** EUR 3.1 bn is a **DGOS forecast** cited by IGAS; IGAS notes that Drees estimates EUR 2.7-2.9 bn. | IGAS PDF, §[2] and footnote 3 |
| §6.1 | Implied that the Netherlands is absent | **NLD is in the OECD waiting-time database.** It is only absent from HaaG Figs 5.11-5.12. | OECD `DF_WAITING` |

The headline 2024 public-hospital deficit should be quoted as **"EUR 2.7-3.1 bn depending on source (Drees 2.7-2.9; IGAS-IGF 2.9; DGOS forecast 3.1)"**. The §0.8 wording "EUR 2.9-3.1 bn" is acceptable but narrower than the published range.

### C. Not verified in the primary source (⚠ unverified)

*(Status updated in the second pass, section E.)*

- ~~⚠ RALFSS 2026 figures: read via *Acteurs publics* only.~~ Verified in the primary (E.1).
- ~~⚠ IGAS-IGF prescription review: secondary source (*Caducée*) only.~~ Verified in the primary; savings figure corrected (E.1).
- ⚠ 36.7% in priority GP zones (*ZIP*): still unverified; the only source describes a share of territory, not population. Recommendation: drop from site (E.3).
- ~~⚠ The Drees management-cost split by financer beyond "52%" was not extracted.~~ Verified (E.1).
- ~~Not re-checked: OECD Figs 5.4, 5.7, 5.14-5.26, 7.12, 7.16-7.19, 8.4, 8.9-8.15; Eurostat HLY/LE and ALOS.~~ Re-checked (E.1); one label corrected (E.2).

### D. Robustness notes

- Several Eurostat ranks involve ties or near-ties. Examples: HP.1 % of GDP (FR = ES); treatable mortality FR 58.76 vs BE 58.83 (3rd vs 4th by 0.07). Quote ranks with "about" where the margin is under 0.1.
- The URLs in §11 resolve as of 2026-10-25. Drees pages serve a bot-challenge page to scripts (HTTP 200, 6.8 KB) but render normally in a browser. commonwealthfund.org returns HTTP 403 to scripts and renders in a browser.

### E. Second pass (2026-10-25): README §7/§8 follow-up

*Scope: every item listed for file 12 in README §7, plus consistency with file 00 (README §8 lists no row for file 12, but the file 00 conventions on EA21 and the canonical spending gap apply). No ⚠ flag in this file related to the Ifop 86% poll, PISA 2025 or the PLF 2027 staffing plan (grep checked), so none had to be removed. The puppeteer browser was shared with other agents and kept being redirected, so all checks below used direct downloads of official PDFs and APIs.*

**E.1 Verified in the primary source**

| Item | Result | Primary source |
|---|---|---|
| RALFSS 2026: 2025 deficit of basic schemes + FSV EUR 21.6 bn, "highest since 2012 outside COVID years" | Confirmed (revenue 644.4, spending 666.0 bn) | Cour des comptes, *La sécurité sociale - RALFSS*, May 2026, ch. I, https://www.vie-publique.fr/files/rapport/pdf/303409.pdf |
| RALFSS 2026: EUR 10 bn a year of savings, of which EUR 4 bn already planned | Confirmed with nuance: balance by 2030 "in four years" needs about EUR 6 bn a year on top of the EUR 4 bn a year already in the LFSS 2026 trajectory; "*reste à documenter*" was said at the 27 May 2026 hearing | Same, ch. I §C; Assemblée nationale, *compte rendu* no. 79, 27 May 2026, https://www.assemblee-nationale.fr/dyn/opendata/CRCANR5L17S2026PO420120N079.html |
| ONDAM 2025 under-executed by EUR 0.5 bn after a mid-year plan of about EUR 1.5 bn | Confirmed: 265.4 vs 265.9 bn (Table 15); summer plan EUR 1.74 bn, of which 1.5 bn judged "certain, probable or likely" by the alert committee (17 Sep 2025) | Same, ch. II, pp. 89-93 |
| RALFSS recommendations on ONDAM transparency and HCFP | Confirmed (recommendations 1 and 4); "trajectory judged not credible" reworded (see E.2) | Same, *Récapitulatif des recommandations* |
| IGAS-IGF prescription review: EUR 81 bn in 2024 = 31.6% of ONDAM | Confirmed; the report is dated Nov 2025 (IGF 2025-E-045-03 / IGAS 2025-048R), published 11 Jun 2026 | https://igas.gouv.fr/revue-de-depenses-sur-les-prescriptions-en-ville-et-lhopital (PDF linked there) |
| IGAS-IGF hospital report: "about EUR 11 bn of new charges in 2026-2029" (struck in the first pass) | Confirmed and restored: "*près de 11 Md€, soit près de 3 Md€ de charges supplémentaires chaque année*" (§1.4, PDF p. 32) | IGAS-IGF 2025-030R, PDF on igas.gouv.fr |
| Drees management-cost split beyond "52%" | Confirmed: Social Security 7.2, State and local government 1.2, complementary insurers 9.2, total 17.6 bn (Table 2); public share 48% | Drees, *Les dépenses de santé en 2025*, 2026 edition, *Vue d'ensemble* PDF (local copy) |
| OECD HaaG 2025 figures "taken as reported" (fresh StatLink downloads) | Confirmed: Fig 5.4 (4.1%; 1.8/2.0/0.3; OECD28 3.4), 5.7 (0.84, OECD32 0.75, rank 7 excl. partner Croatia), 5.14, 5.15, 5.16 (5.4, OECD31 6.5), 5.18, 5.19 (5.4, OECD38 4.2, rank 10), 5.20 (74.3, rank 12/30), 5.22 (134.6, OECD36 128.0, rank 17/36), 5.23 (5.5, rank 28/37), 5.24 (30.0, OECD28 30.8, rank 15/28), 5.26 (97.3, rank 19), 7.11 (78.0), 7.12 (15.8 vs OECD38 15.1, 4th of 8 in panel), 7.16 (11.6 vs 13.6), 7.17 (2.31 vs 3.37), 7.18 (39.8, rank 17/35), 7.19, 8.4 (3.9, rank 17/37), 8.9 (France absent), 8.11 (2.3 vs 2.79), 8.15 (0.97 vs 1.17) | stat.link/{0krovl, bos5wh, 3mrto9, sun2e7, rqt74h, pm3teq, 9zdx04, 0urtay, it5m0j, 4sxvgp, 59ftvc, rf68c2, g0u6rj, bquoys, ainpf8, tx25z8, 7ah6wr, ze0c6k, mzifb7, j7nh45, xq8zct, sm9rdl}; files in `data/raw/12_factcheck/haag_pass2/` |
| Eurostat LE and HLY (2005, 2024), panel and EU-27 | Exact match on all 54 values; IT, ES, DK flagged "b" in 2024, FR "p" | Eurostat `hlth_hlye` API, https://ec.europa.eu/eurostat/databrowser/view/hlth_hlye/default/table |
| Eurostat ALOS 2023 (all in-patients): FR 9.09, EU-27 7.96, mean 7.30, median 7.36, rank 4 | Exact match | Eurostat `hlth_talos1` API |
| Country Health Profile 2025: beds 5.4 vs EU 5.1; doctors 3.9 vs 4.3, stable; nurses 8.8 vs 8.5; 597 vs 578 days; over 40% of over-75s with a potentially inappropriate prescription; screening 47% vs 58%, 34% vs 48%; unmet needs 4.5% | Verbatim match | OECD/Observatory, CHP 2025 France PDF (local copy) |
| EC Joint Report 2019: 96% of the population with complementary cover | Verbatim match | EC Institutional Paper 105, France (local copy) |
| EA21 SHA aggregates (file 00 convention) | Retrieved: CHE 10.45% (EA20 10.46), HF.1 8.38 (8.40), HC.7 0.38% of GDP / 3.62% of CHE, 4,312 PPS (4,342) | Eurostat `hlth_sha11_hf`, `hlth_sha11_hc` API |

**E.2 Corrections made in this pass**

| Location | Was | Now |
|---|---|---|
| §0.1, §0.2, §1.2, §1.3, §2.3 | Euro-area comparisons on EA20 only; COFOG row "EA aggregate" | EA21 first (file 00 convention), EA20 in brackets: CHE gap +0.88 pp, HF.1 gap +1.06 pp, COFOG +1.47 pp vs EA21 (2024) |
| §8.3 | Spending gap "about EUR 225 bn" (unlabeled) | +7.6 pp of GDP, about EUR 227 bn, vs EA21, 2025 (file 00 row 7) |
| §10 item 6 | COFOG health gap "+1.45 pp" | +1.47 pp vs EA21, 2024 (file 00 row 9, log #8) |
| §7.2 RALFSS row | "trajectory judged not credible"; "EUR 4 bn already planned (*peu documentées*)" | Report calls for a "more demanding" ONDAM path (2-2.5% a year) and asks the government to "define and substantiate" it; the EUR 4 bn is in the LFSS 2026 trajectory and "*reste à documenter*" (hearing) |
| §7.2 prescription row | "measurable savings below EUR 3 bn" | Savings potential EUR 0.8-1.4 bn against a EUR 3 bn target; report dated Nov 2025 |
| §7.2 IGAS-IGF hospital row | EUR 11 bn struck and flagged ⚠ | Restored with primary citation |
| §4.1 nurses (OECD) | Mean 9.17 shown without the published average | Published OECD37 average 9.2; rank 20 of 34 (22 of 37 counting all reporting countries) |
| §6.6, §11 D2-sec, §12 item 9 | "36.7% of the population" in ZIP, attributed to the 2025 *arrêté* | Press figure for share of **territory** (2026); no official national population share; ⚠ kept |

**E.3 Still unverified**

- ⚠ 36.7% in *zones d'intervention prioritaire*: only *Le Quotidien du Médecin* (3 Apr 2026), as a share of territory. No ministry, DGOS or CartoS@nté national total found. **Recommendation: drop from site**; replace by the Drees APL figure (29.0% of the population, 19.6 million, below 2.5 GP consultations a year in 2024, our computation from Drees data).
