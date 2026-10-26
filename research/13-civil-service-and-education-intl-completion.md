# 13 - Civil service and education: completing the international panel (public employment 2000-2024, wage bill in PPS, PISA 2025, TIMSS/PIRLS, PLF 2027 staffing plan, 1980 baseline)

*Gap-fill file for the public-finance education platform. Prepared 2026-10-25. All web sources accessed 2026-10-25. It completes `04-civil-service-and-outcomes.md` (cited below as "file 04") and does not repeat its content. Figures marked "(our computation)" are recomputed from the raw data cited, and every CSV is listed at the end of Section 10. Raw downloads (untrusted, not executed) are in `research/data/raw/13/`. Scripts are in `research/scripts/13/`.*

---

## 0. Bottom line (for the platform editors)

1. **Public employment: France has been about 4-6 points above the EU median for 20 years, and the gap is narrowing.** General government employment as a share of total employment, national-accounts definition:
   - **Balanced sample (the 17 EU member states with an ILO/Eurostat value in both years; unweighted median, not the EU27 aggregate):** 2005: France 22.7% vs. median 15.8%, gap +6.9 pts, rank 6/17. 2023: France 20.9% vs. median 16.8%, gap +4.0 pts, rank 5/17 (Section 2.3a). (corrected 2026-10-25: was "2005: France 22.7% vs. EU median 16.2%, gap 6.5 pts (computed sample). 2023: France 20.9% vs. EU median 17.1%, gap 3.8 pts. France ranks 6th in the EU in both years." Those were the unbalanced yearly samples of Section 2.3b, n = 22 and n = 19, which the file itself says are unsuitable for trend statements.)
   - In the panel France is 3rd, behind Sweden and Denmark, every year since 2000.
   - The OECD's own figures show the same thing. *Government at a Glance* 2021 puts France at 22.35% in 2007 (OECD average 18.2%, OECD rank ~~8/33~~ **8/31** [corrected 2026-10-25: only 31 OECD countries have a 2007 value in the StatLink]). The 2025 edition puts it at 20.7% in 2023 (OECD average 18.4%, rank 8/30). [T1][T2][T3]
2. **Change the scope and France moves to the middle of the northern panel.** One alternative measure counts all employment in public administration, education and health/social work (NACE O+P+Q), whoever the employer. This is a way to neutralize "make-or-buy". On that measure France was 29.2% in 2025, against Germany 27.0%, the Netherlands 29.0%, Belgium 30.4%, Denmark 30.4% and Sweden 32.8%.
   - France ranks 4th of 8 in the panel and 5th of 27 in the EU. It is only 0.1 pt above the panel median. In 2005 it was 2.0 pts above.
   - Germany employs about **6.8 million people in O+P+Q outside general government** (14.8% of total employment). France employs about 2.5 million (8.3%) (our approximation).
   - The German non-profit welfare associations (*Freie Wohlfahrtspflege*) alone reported **2.08 million employees** in 2020 and **2.17 million on 1 Jan 2024** (61.7% part-time; BAGFW, an association source, not official statistics). [T4][T5][T13][T13b]
3. **Wage bill in PPS per capita: France is above the EU, but much less so than when measured in % of GDP, and the gap has halved since 2005.**
   - For reference, in % of GDP (Eurostat `gov_10a_main`, 21 Oct 2026, 2025 data): D.1 is **12.4% of GDP vs. EU27 aggregate 10.3% and EA21 aggregate 10.0%**, rank 6/27 (file 00 row 18).
   - D.1 (compensation of employees) per inhabitant in 2025: France 5,035 PPS vs. EU27 aggregate 4,304, an index of 117 (rank 8/27). In 2005 the index was 139.
   - **"Production costs" (D.1 + P.2 + D.632) per inhabitant: France 9,848 PPS vs. EU27 9,133, an index of 108 (rank 10/27).** That is *below* Germany (11,704), the Netherlands (14,372), Belgium (11,873), Sweden (11,188) and Denmark (12,877). France ranks 6th of 8 in the panel.
   - Measured as a share of GDP, the OECD ranks France's 2023 production costs (wider OECD definition) 3rd of 36 (28.4%) and its D.1 7th of 36 (12.3% of GDP). Measured as a share of total expenditure, D.1 ranks France 26th of 37 (21.5%). [T6][T7][T8][T9]
4. **PISA 2025 country tables (published 8 Sep 2026):**
   - **Mathematics:** France 458 vs. OECD mean 463, OECD median 466, EU mean 460, EU median 464. France ranks **29th of 38 in the OECD**, 20th of 27 in the EU and 7th of 8 in the panel.
   - **Reading:** 456 (OECD rank 23/38, EU rank 14/27). **Science:** 483 (OECD rank 22/38, EU rank 13/27).
   - In 2006 and 2015 France was at the OECD median in mathematics (gap 0.0 and +0.2). In 2025 it is 8.3 points below.
   - France's fall since 2015 is among the steepest: -35 points in mathematics (8th-largest of 38) and -43 in reading (11th-largest). The median OECD country fell 22 and 24 points.
   - **Top performers in mathematics fell from 11.4% to 5.2% (2015 to 2025).** The socio-economic gradient is steeper than the OECD average (R² 14.8% vs. 12.0%; rank 29/37). [T10][T11]
5. **TIMSS 2023 and PIRLS 2021 confirm the primary-school weakness.**
   - TIMSS grade-4 mathematics: France 484, **last of 22 EU entities and 28th of 29 OECD entities**.
   - TIMSS grade-8 mathematics: 479, 18th of 20 OECD entities.
   - PIRLS 2021 reading: 514. ~~18th of 21 OECD entities and 16th of 19 EU entities.~~ **[Corrected 2026-10-25] Among countries tested at the end of grade 4 (IEA Exhibit 1.1): 18th of 22 OECD entities (Türkiye had been omitted) and 16th of 19 EU entities. Among all participants, including the 14 countries tested at the start of grade 5 (IEA Exhibit 1.3: Ireland 577, Croatia 557, Lithuania 552, United States 548, Hungary 539, Latvia 528, etc.): 24th of 28 OECD entities and 21st of 24 EU entities.** The IEA warns that the delayed-assessment pupils were about half a year older, so the narrower comparison is the cautious one. Both should be shown. [T14][T15]
6. **Spending vs. scores.** Spending per student, primary to post-secondary non-tertiary (EaG 2026, 2023 data): France USD 14,932 PPP vs. OECD average 14,436. France is 16th of 35 OECD countries and 6th of 8 in the panel. Across OECD countries, spending explains only about 6% of the variance in PISA 2025 scores (r = 0.24). Among countries that spend at least USD 10,000 the slope is slightly negative. France scores about 6 points below the fitted line (13 points below in the ≥ USD 10,000 group). [T12][T10] (our computation)
7. **PLF 2027 *schéma d'emplois* (staffing plan), from the bill itself** (PLF 2027, AN no. 3210, 1 Oct 2026):
   - **State: +8,025 FTE** (ETP). Of this, +4,742 comes from the teacher-training reform, so +3,283 excluding it.
   - **State operators: -1,209 FTE**. State plus operators: **+6,816 FTE**.
   - Including social security funds (-1,000) and excluding the teacher-training reform and the military programming law (LPM) trajectory: **-1,076 FTE**.
   - Education ministry (*Éducation nationale*): +3,257 FTE = **-1,588 FTE teachers** (public and private; -1,250 in public schools) + 1,804 support posts (incl. 1,300 AESH, *accompagnants d'élèves en situation de handicap*, special-needs assistants) + 3,041 trainee teachers. [T16][T19]
   - State employment ceiling: 2,032,750 ETPT (annual average FTE), +16,162. Operators' ceiling: 397,282 ETPT, -4,107. [T16]
8. **An official 1980 baseline exists.** The Cour des comptes (Dec. 2009 thematic report, DGAFP data processing) gives **3,864,960 agents in the three civil-service branches at 31 Dec. 1980** and 4,257,653 in 1990. The civil service made up 17.8% of total employment in 1980 and 19.0% in 1990. These figures exclude La Poste/France Télécom and private-school teachers under contract.
   - **Do not chain these to the 2024 SIASP figure (5.85 million) without stating the series break.** [T17]

---

## 1. Scope, definitions and method

| Concept | Definition used here | Source | Why it matters |
|---|---|---|---|
| General government (GG, S.13) employment | Persons employed by central, state and local government and social security funds, incl. non-market NPIs controlled by government (SNA/ESA). | ILOSTAT dataflow `DF_EMP_XPSE_GOV_NB` ("Public employment by sectors and sub-sectors of national accounts", flagged *discontinued* but updated to 2024). National sources are mostly national accounts (France: Insee national accounts, ESA 2010). | This is the concept used by OECD *Government at a Glance* (GaaG). GaaG itself takes ILOSTAT data for several countries [T2]. |
| Total employment (denominator) | Eurostat national accounts, persons, domestic concept (`nama_10_a64_e`, TOTAL, EMP_DC). ILO modelled estimates (persons 15+) for non-European OECD countries. | [T4][T5] | GaaG also uses domestic national-accounts employment. |
| NACE O+P+Q proxy | Employment in Public administration and defense (O), Education (P), Human health and social work (Q), **whatever the employer** (public, private, non-profit). | Eurostat `nama_10_a64_e` [T4] | It is not "public employment". It measures the size of the sectors that welfare states finance, and so neutralizes make-or-buy choices. It includes private clinics, private schools and private doctors, and excludes public employees working in other industries. |
| LFS "public sector" | Survey-based self-declaration of employer type; includes public corporations. | ILOSTAT `DF_EMP_TEMP_SEX_INS_NB` [T5] | Poor coverage for the panel. Used here only as a third perimeter for France. |
| PPS per capita | EUR value / population / (GDP price-level index, EU27 = 100). | Eurostat `gov_10a_main`, `nama_10_pe`, **`prc_ppp_ind_1` (new COICOP 2018 vintage, updated 9 Jul 2026, data to 2025)** [T6] | It gives the real volume per inhabitant at a common price level, but it uses the GDP-wide PPP, not a government-specific one (see Section 3.4). |
| "% of GDP" vs "% of total public expenditure" | Each table states which denominator it uses. | | The ranks differ sharply (Section 3). |

**Validation of the employment series.** For every country we compared the ILO-based shares with the OECD's published GaaG 2025 values for 2019 and 2023 and with the GaaG 2021 values for 2007 and 2019. France, Germany, the Netherlands, Sweden, Denmark, Spain, Norway, Finland, Japan, Korea, the UK and most others match within 0-0.9 pt. **Seven series deviate by more than 1 pt and were excluded from group statistics:** Canada, Israel, Poland, Mexico, Costa Rica, Ireland and Croatia. The ILO series for these countries cover a narrower scope or are broken. Italy deviates by 1.4 pts in 2023 (12.3% vs. GaaG 13.7%) and is kept but flagged. Comparison file: `data/13_gg_employment_share_ilo_2000_2024.csv` vs. `data/04_oecd_gaag2025_gg_employment_share.csv` and `data/13_oecd_gaag2021_fig3_1_gg_emp_share_2007_2019.csv`.

**OECD SDMX API.** The OECD national-accounts dataflow "Annual employment by institutional sector" (`OECD.SDD.NAD, DSD_NAMAIN10@DF_TABLE3_EMP_SECTOR`) and the GaaG yearly-update dataflow (`DSD_GOV@DF_GOV_EMPPS_REP_YU`) exist, and the structure listing was retrieved. Data queries returned a Cloudflare challenge (HTTP 429/403), including from a headless browser. **The OECD database values were therefore not downloaded directly.** The ILO dataset (same national sources) and the published GaaG StatLinks were used instead.

---

## 2. General government employment as a share of total employment, 2000-2024

### 2.1 OECD published values (official benchmarks)

| Country / group | 2007 (GaaG 2021) | 2019 (GaaG 2021) | 2019 (GaaG 2025) | 2023 (GaaG 2025) | Source |
|---|---|---|---|---|---|
| **France** | **22.4** | **21.2** | **21.7** | **20.7** | [T2][T3] |
| Germany | 11.4 | 10.6 | 11.1 | 11.5 | [T2][T3] |
| Italy | 14.5 | 13.2 | 13.4 | 13.7 | [T2][T3] |
| Spain | 13.4 | 15.6 | 15.3 | 15.3 | [T2][T3] |
| Netherlands | 12.8 | 11.7 | 12.0 | 12.3 | [T2][T3] |
| Belgium | 18.5 | 18.3 | 18.4 | 18.3 | [T2][T3] |
| Sweden | 30.4 | 28.7 | 28.5 | 28.1 | [T2][T3] |
| Denmark | 28.3 | 27.6 | 27.6 | 27.3 | [T2][T3] |
| OECD average (as published) | 18.2 | 17.9 | 18.1 | 18.4 | [T2][T3] |
| OECD mean / median, all countries in figure (our computation) | ~~17.7 / 17.4 (n = 33)~~ **18.2 / 18.0 (n = 31)** [corrected] | ~~17.9 / 16.7 (n = 31)~~ **17.4 / 16.7 (n = 33, incl. Korea and Switzerland); 17.9 / 16.7 (n = 31, countries in the OECD average)** [corrected] | | 18.4 / 17.4 (n = 30, file 04) | [T2][T3] |
| **France rank, OECD** | ~~8/33~~ **8/31** [corrected] | ~~8/31~~ **8/33 (8/31 excl. Korea, Switzerland)** [corrected] | | **8/30** | [T2][T3] (our computation) |
| EU mean / median (our computation) | 18.2 / 17.4 (n = 23) | 18.0 / 16.7 (n = 23) | | 18.8 / 17.8 (n = 25, file 04) | [T2][T3] |
| **France rank, EU** | **5/23** | **6/23** | | **8/25** | [T2][T3] (our computation) |
| France rank, panel | 3/8 | 3/8 | 3/8 | 3/8 | [T2][T3] |

*Vintage divergence:* France 2019 is 21.2% in GaaG 2021 and 21.7% in GaaG 2025. Insee's 2020-base national accounts revision (2024) reclassified employment across institutional sectors, and total employment was revised too. The two editions must not be mixed in one chart.

### 2.2 Computed series 2000-2024 (ILO national-accounts numerators / Eurostat denominators)

| Country | 2000 | 2005 | 2010 | 2015 | 2019 | 2022 | 2023 | 2024 | Source |
|---|---|---|---|---|---|---|---|---|---|
| **France** | **22.2** | **22.7** | **22.5** | **22.1** | **21.7** | ~~21.0~~ **20.9** (20.946; minor rounding correction) | **20.9** | ~~21.0~~ **20.9** (20.947; idem) | [T5][T4] |
| Germany | 11.0 | 10.9 | 10.8 | n.a. | 10.2 | 10.9 | 11.4 | 11.7 | [T5][T4] |
| Italy (flag: 1.4 pt below GaaG in 2023) | 16.0 | 15.1 | 14.3 | 13.7 | 13.2 | 12.4 | 12.3 | 12.2 | [T5][T4] |
| Spain (LFS-based numerator) | 13.2 | 13.8 | 15.6 | 15.1 | n.a. | 15.9 | 15.2 | n.a. | [T5][T4] |
| Netherlands | 12.4 | 12.4 | 13.4 | 12.5 | 12.0 | 12.3 | 12.4 | 12.6 | [T5][T4] |
| Belgium | 17.9 | 18.6 | 18.9 | 18.9 | 18.4 | 18.4 | n.a. | n.a. | [T5][T4] |
| Sweden | 27.8 | 30.5 | 28.5 | 28.3 | 28.5 | 28.2 | 28.1 | 28.0 | [T5][T4] |
| Denmark | 30.7 | 30.3 | 30.2 | 29.0 | 27.6 | 27.5 | 27.4 | n.a. | [T5][T4] |
| Norway (reference) | 30.0 | 30.6 | 30.2 | 30.1 | 30.2 | 30.0 | 29.9 | 30.0 | [T5][T4] |
| United Kingdom (reference) | n.a. | 19.7 | 19.5 | 16.4 | 15.8 | 17.0 | 16.7 | 16.3 | [T5] (ILO modelled denominator) |
| United States (reference) | 14.8 | 15.0 | 16.0 | 14.5 | 13.9 | 13.6 | 13.7 | 13.8 | [T5] |
| Japan (reference) | 6.4 | 6.5 | 5.0 | 4.8 | 4.9 | 5.1 | 5.0 | n.a. | [T5] |

Data: `research/data/13_gg_employment_share_ilo_2000_2024.csv`. Notes: the German numerator is the administrative *Personalstandstatistik* (June reference). The jump in 2022-2023 (+250,000) coincides with a change in coverage in the source and should not be read as a real hiring wave without checking (not checked). The Swedish 2005 peak (30.5%) reflects a source change in the ILO series.

### 2.3 Group statistics and France's 20-year gap

**(a) Balanced samples: same countries in both years.** This is the preferred measure of the change in the gap. Inconsistent ILO series are excluded (Section 1).

| Group (countries with data in both years) | n | 2005 mean | 2005 median | France 2005 | FR rank 2005 | FR gap vs. median 2005 | 2023 mean | 2023 median | France 2023 | FR rank 2023 | FR gap vs. median 2023 | Source |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| EU27 (BG CY DK FR DE EL HU IT LV LT LU MT NL SK SI ES SE) | 17 | 18.4 | 15.8 | 22.7 | 6 | **+6.9** | 17.9 | 16.8 | 20.9 | 5 | **+4.0** | [T5][T4] (our computation) |
| OECD (above + JPN NZL NO GBR USA, minus EU-only members) | 19 | 17.9 | 15.8 | 22.7 | 6 | **+6.9** | 17.7 | 16.7 | 20.9 | 6 | **+4.2** | [T5][T4] (our computation) |
| Panel (excl. Belgium, no 2023 value) | 7 | 19.4 | 15.1 | 22.7 | 3 | +7.5 | 18.2 | 15.2 | 20.9 | 3 | +5.7 | [T5][T4] (our computation) |
| Panel, 2005 vs. 2022 (incl. Belgium) | 8 | 19.3 | 16.9 | 22.7 | 3 | +5.8 | 18.3 | 17.2 | 20.9 (corrected 2026-10-25: was 21.0; raw 20.946) | 3 | +3.8 | [T5][T4] (our computation) |
| EU27, 2000 vs. 2023 | 16 | 18.9 | 18.2 | 22.2 | 6 | +4.0 | 18.1 | 17.0 | 20.9 | 5 | +3.9 | [T5][T4] (our computation) |

Data: `research/data/13_gg_employment_balanced_gap.csv`.

**(b) Unbalanced yearly statistics** (all validated countries with data that year). The country set changes from year to year, so these are not suitable for trend statements.

| Year | EU n | EU mean | EU median | FR | FR rank EU | OECD n | OECD mean | OECD median | FR rank OECD | Source |
|---|---|---|---|---|---|---|---|---|---|---|
| 2000 | 20 | 18.4 | 16.9 | 22.2 | 6 | 21 | 17.8 | 16.0 | 6 | [T5][T4] |
| 2005 | 22 | 18.1 | 16.2 | 22.7 | 6 | 24 | 17.7 | 16.2 | 6 | [T5][T4] |
| 2010 | 22 | 19.1 | 18.5 | 22.5 | 7 | 26 | 18.7 | 17.7 | 9 | [T5][T4] |
| 2015 | 18 | 18.8 | 18.1 | 22.1 | 7 | 24 | 18.1 | 16.8 | 9 | [T5][T4] |
| 2019 | 17 | 18.9 | 18.4 | 21.7 | 6 | 24 | 17.5 | 16.4 | 8 | [T5][T4] |
| 2023 | 19 | 18.3 | 17.1 | 20.9 | 6 | 22 | 17.4 | 16.0 | 7 | [T5][T4] |

Data: `research/data/13_public_employment_stats.csv` (indicator `GG_share_ILO`).

**Reading.** Measured in national-accounts terms, France's public-employment share fell by 1.8 pts between 2005 and 2023 (22.7% to 20.9%). The sample average fell by only 0.5 pt, so France's gap to the EU median narrowed from about 7 pts to about 4. France's rank barely moved: 5th-6th in the EU, 6th-9th in the OECD and 3rd in the panel throughout. This agrees with the OECD's own observation that France was among the largest decreases from 2019 to 2023 (file 04, Section 5.1).

### 2.4 The make-or-buy-neutral proxy: NACE O+P+Q employment

| Country / group | 2000 | 2005 | 2015 | 2019 | 2025 | Change 2005-2025 (pt) | Source |
|---|---|---|---|---|---|---|---|
| **France** | **29.7** | **30.0** | **30.9** | **29.9** | **29.2** | -0.7 | [T4] |
| Germany | 22.7 | 23.7 | 24.3 | 24.9 | 27.0 | +3.3 | [T4] |
| Italy | 20.2 | 19.3 | 19.2 | 18.9 | 19.3 | 0.0 | [T4] |
| Spain | 18.0 | 17.6 | 22.0 | 21.4 | 22.0 | +4.4 | [T4] |
| Netherlands | 24.7 | 27.4 | 28.2 | 27.5 | 29.0 | +1.6 | [T4] |
| Belgium | 26.8 | 28.6 | 30.1 | 30.1 | 30.4 | +1.9 | [T4] |
| Sweden | 32.2 | 33.4 | 32.9 | 32.6 | 32.8 | -0.7 | [T4] |
| Denmark | 30.5 | 31.1 | 31.4 | 30.2 | 30.4 | -0.7 | [T4] |
| EU27 aggregate | 21.9 | 22.5 | 23.7 | 23.5 | 24.2 (2024) | | [T4] |
| EU27 mean / median (n = 27) | 21.3 / 20.6 | 21.9 / 20.8 | 23.1 / 22.6 | 22.8 / 21.7 | 23.7 / 22.7 | | [T4] (our computation) |
| **France rank EU27** | 3 | 3 | 3 | 4 | **5** | | [T4] (our computation) |
| Panel mean / median | 25.6 / 25.7 | 26.4 / 28.0 | 27.4 / 29.2 | 27.0 / 28.7 | 27.5 / 29.1 | | [T4] (our computation) |
| **France rank panel; gap vs. panel median** | 3; +3.9 | 3; +2.0 | 3; +1.7 | 4; +1.2 | **4; +0.1** | | [T4] (our computation) |
| France gap vs. EU median | +9.1 | +9.2 | +8.3 | +8.2 | +6.5 | | [T4] (our computation) |

Data: `research/data/13_eurostat_OPQ_share_2000_2025.csv`, `13_public_employment_stats.csv` (indicator `OPQ_share_Eurostat`; the OECD group in that file covers only the 25 European OECD members, so it is not an OECD-wide statistic).

**Scope difference (must be stated with any chart).** The NACE O+P+Q proxy is *broader* than general government: it adds private and non-profit schools, clinics, nursing homes and doctors' practices. It is also *narrower* in one respect: it omits public employees classified in other industries, e.g. public transport authorities or water services run by government units. In France, O+P+Q exceeds GG by about 2.5 million persons, versus 6.8 million in Germany (Section 2.5).

### 2.5 Germany's publicly financed non-profit and private provision: an order of magnitude

| Indicator | France | Germany | Netherlands | Year | Source |
|---|---|---|---|---|---|
| O+P+Q employment minus GG employment (thousand persons) | 2,526 | 6,813 | 1,667 | 2024 | [T4][T5] (our approximation) |
| Same, % of total employment | 8.3 | 14.8 | 16.2 | 2024 | [T4][T5] (our approximation) |
| Same, 2005 (% of total employment) | 7.3 | 12.8 | 15.0 | 2005 | [T4][T5] (our approximation) |
| Employees of the six German non-profit welfare associations (*Freie Wohlfahrtspflege*: Caritas, Diakonie, AWO, Paritätischer, DRK, ZWST), headcount | | 2,076,535 (1.67 m in 2012; 1.12 m in 1996; 0.75 m in 1990) | | 2020 (reference date: the methodology section says 1 Jan 2020, the foreword says 31 Dec 2020; the 2024 edition uses "Stand 1. Januar 2020") | [T13] BAGFW *Gesamtstatistik 2020*, published **December 2023** (verified 2026-10-25: cover page reads "Dezember 2023"; full report file dated 2023-12-14) |
| **Update: same, latest edition** | | **2,174,073** (+4.7% vs. 2020) | | 1 Jan 2024 | [T13b] BAGFW *Gesamtstatistik 2024* (imprint dated June 2026) |
| of which elderly care (*Altenhilfe*) | | 551,278 | | 2020 | [T13] |
| of which health care (*Gesundheitshilfe*, incl. non-profit hospitals) | | 437,263 | | 2020 | [T13] |
| of which youth services (*Jugendhilfe*) | | 472,822 | | 2020 | [T13] |
| 2024 edition: elderly care / health care / youth services | | 576,844 / 428,501 / 558,104 | | 1 Jan 2024 | [T13b] |

Data: `research/data/13_OQ_employment_outside_gg.csv`.

Caveats: (1) The BAGFW is the umbrella body of the welfare associations, **not an official statistical office**. Its census is self-reported. **59% of these employees worked part-time in 2020 (1,232,979 part-time vs. 843,556 full-time; the 2024 edition recomputes it as 59.3%) and 61.7% on 1 Jan 2024 (1,340,639 of 2,174,073)** (verified 2026-10-25 in the full 2020 report [T13] and the 2024 overview [T13b]; was "about 60%", flagged unverified). BAGFW counts marginal (*geringfügig*) jobs as part-time, so headcounts overstate FTE. (2) The O+P+Q-minus-GG figure is an approximation: GG employees outside O-Q are not netted out, so the true "outside-government O-Q" figure is somewhat larger. Not all of that employment is publicly financed (private schools and clinics are partly privately paid). (3) Destatis hospital staff by ownership (*Grunddaten der Krankenhäuser*) was not retrieved (gap).

**Implication:** about 2 million German welfare-sector workers, and several million O-Q workers in total, are financed largely by social insurance or taxes but do not count as "government employees". This is the quantitative core of the make-or-buy caveat in file 04, Section 5.2.

### 2.6 France: three perimeters side by side

| Perimeter | 2005 | 2023 | 2024 | Source |
|---|---|---|---|---|
| GG (national accounts) / total employment | 22.7 | 20.9 | 20.9 (corrected 2026-10-25: was 21.0; 20.947 rounds to 20.9, as in Section 2.2) | [T5][T4] |
| OECD GaaG (national accounts) | 22.35 (2007) | 20.7 | | [T2][T3] |
| LFS "public sector" (incl. public corporations) / LFS employment | 22.0 | 20.1 | 20.2 | [T5] `13_ilo_lfs_public_sector_share.csv` |
| Civil service (legal perimeter, DGAFP/Insee, incl. subsidized contracts) | 21.0-21.5 (2002-2017) | | 19.8 | file 04, [S1] |
| NACE O+P+Q / total employment | 30.0 | 29.0 | 29.2 | [T4] |

---

## 3. Wage bill and production costs per capita in PPS

### 3.1 PPP vintage check

| Dataset | Last update | Coverage | France GDP PLI (EU27 = 100) | Source |
|---|---|---|---|---|
| `prc_ppp_ind` (COICOP 1999), the vintage used in files 01 and 04 | **10 Jul 2025** | to 2024 | 2024: 108.9 | [T6] |
| **`prc_ppp_ind_1` (COICOP 2018), the new vintage used here** | **9 Jul 2026** (structure 25 Mar 2026) | to 2025 | 2024: 108.6; **2025: 106.5**; 2005: 111.9 | [T6] |

A newer PPP vintage exists. It revises 2024 slightly: France's D.1 per capita in 2024 is 4,861 PPS with the new vintage vs. 4,847 with the old one. It also adds 2025. ~~File 01 reports TE per capita 2024 = 22,321 PPS (old vintage); the new vintage gives 22,395. File 09 reports 23,330 PPS for 2025 through `nama_10_pc`; our method gives 23,327 (consistent).~~ (aligned 2026-10-25 with file 00 row 5 and log #10) **Canonical value (file 00): TE per inhabitant 23,330 PPS in 2025, 8th of 27 EU member states (EU27 aggregate 20,653 on our method), statistically tied with Sweden; 2024 = 22,398 PPS, 8th of 27, on the current vintage.** Our recomputation with `prc_ppp_ind_1` gives 23,327 (2025) and 22,395 (2024), i.e. the same values within rounding. The 22,321 PPS / 9th of 27 for 2024 that file 01 used came from the superseded July 2025 PLI vintage and should no longer be shown.

### 3.2 Per inhabitant in PPS, 2025 (and 2005)

| Country / group | D.1 compensation 2025 | Index EU = 100 (2005 → 2025) | D.11 gross wages 2025 | Production costs D.1+P.2+D.632 2025 | Index EU = 100 (2005 → 2025) | Total expenditure TE 2025 | Index EU = 100 (2005 → 2025) | Source |
|---|---|---|---|---|---|---|---|---|
| **France** | **5,035** | **139 → 117** | **3,369** | **9,848** | **131 → 108** | **23,327** | **130 → 113** | [T6] (our computation) |
| Germany | 4,118 | 94 → 96 | 3,096 | 11,704 | 117 → 128 | 24,357 | 120 → 118 | [T6] |
| Italy | 3,596 | 111 → 84 | 2,536 | 6,878 | 101 → 75 | 20,473 | 111 → 99 | [T6] |
| Spain | 4,099 | 94 → 95 | n.a. | 7,287 | 84 → 80 | 17,306 | 83 → 84 | [T6] |
| Netherlands | 4,898 | 118 → 114 | 3,601 | 14,372 | 156 → 157 | 24,935 | 129 → 121 | [T6] |
| Belgium | 5,984 | 136 → 139 | 4,036 | 11,873 | 134 → 130 | 25,912 | 135 → 125 | [T6] |
| Sweden | 5,718 | 152 → 133 | 4,680 | 11,188 | 145 → 122 | 22,851 | 140 → 111 | [T6] |
| Denmark | 7,652 | 186 → 178 | 7,446 | 12,877 | 155 → 141 | 25,483 | 137 → 123 | [T6] |
| Euro area (EA20) aggregate | 4,346 | 110 → 101 | n.a. | 9,537 | 111 → 104 | 21,601 | 112 → 105 | [T6] |
| **EU27 aggregate** | **4,304** | 100 | n.a. | **9,133** | 100 | **20,653** | 100 | [T6] |
| EU27 unweighted mean / median | 4,762 / 4,405 | | 3,812 / 3,369 (n = 25) | 8,982 / 7,659 | | 19,863 / 17,218 | | [T6] (our computation) |
| **France rank EU27** (1 = highest) | **8/27** (5/27 in 2005) | | **13/25** (6/23 in 2005) | **10/27** (7/27 in 2005) | | **8/27** (6/27 in 2005) | | [T6] (our computation) |
| Panel median; **France rank panel** | 4,967; **4/8** | | 3,601; 5/7 | 11,446; **6/8** | | 23,842; 5/8 | | [T6] (our computation) |

Data: `research/data/13_pps_per_capita_wagebill_production_costs.csv`, `13_pps_per_capita_stats.csv`; inputs `13_eurostat_gov_10a_main_D1_P2_D632_mioeur.csv` (updated 21 Oct 2026), `13_eurostat_nama_10_pe_pop.csv` (updated 21 Oct 2026), `13_eurostat_prc_ppp_ind_1_PLI_GDP.csv` (updated 9 Jul 2026). Unit: PPS (EU27_2020 = 1) per inhabitant, current prices.

**Reading.**
- In % of GDP, France's D.1 ranks 6th/27 in 2025 (12.4% vs. EU27 aggregate 10.3%, EA21 aggregate 10.0%; Eurostat `gov_10a_main`, 21 Oct 2026; file 00 row 18; file 04). In PPS per capita it ranks 8th/27, and its excess over the EU fell from +39% (2005) to +17% (2025).
- For production costs, France spends **less per inhabitant than all northern panel members**. Its "excess" in GDP terms (24.3% vs. EU27 aggregate 21.8%, 2025, file 04 K17) is partly a denominator effect: French GDP per capita is below the EU27 average in PPS (40,716 vs. 41,774 in 2025, file 09).
- D.11 (gross wages only) per capita in France is at the EU *median* (3,369 PPS, rank 13/25). The French wage-bill excess again comes from employer contributions (incl. imputed pension contributions).
- *Caveat on convergence:* part of France's falling index reflects the catching-up of central and eastern EU members, which raises the EU27 aggregate. It is not only French restraint.

### 3.3 OECD-wide ranks (GaaG 2025, 2023 data)

| Indicator | France | OECD avg. (published) | OECD mean / median (our comp.) | FR rank OECD | EU mean / median | FR rank EU | Panel: DE / IT / ES / NL / BE / SE / DK | Source |
|---|---|---|---|---|---|---|---|---|
| Compensation of government employees, **% of GDP** | **12.3** | 8.8 (OECD-EU 10.0) | 10.2 / 10.4 (n = 36) | **7/36** | 10.7 / 10.7 (n = 25) | 5/25 | 8.1 / 8.8 / 10.9 / 8.3 / 12.3 / 12.3 / 14.2 | [T7] Fig. 16.12 |
| Production costs (D.1 + goods and services used and financed + other production costs), **% of GDP** | **28.4** | 20.8 | 22.6 / 23.1 (n = 36) | **3/36** (after FI 31.1, SE 30.3; *note: 31.1 is the value in the OECD text; the three Fig. 16.12 StatLink components for Finland sum to 31.9, an inconsistency inside the OECD source. The rank is unaffected*) | 23.4 / 23.0 | 3/25 | 25.8 / 20.3 / 21.8 / 27.7 / 26.7 / 30.3 / 25.9 | [T7] |
| Compensation of employees, **% of total government expenditure** | **21.5** | 20.6 (OECD-EU 20.3) | 23.4 / 23.2 (n = 37) | **26/37** | | | 16.7 / 16.4 / 24.0 / 19.3 / 23.2 / 25.0 / 30.3 | [T8] Table 15.3 |

Data: `research/data/13_oecd_gaag2025_fig16_12_production_costs.csv`, `13_oecd_gaag2025_tab15_3_D1_share_TE_2023.csv`. 2023 is used because 2024 values are missing for 10 OECD countries.

*Divergence:* the OECD production-cost concept (28.4% of GDP) is wider than our Eurostat one (24.3% in 2025, file 04 K17). It adds consumption of fixed capital and other taxes on production, which make up 4.2 pts of GDP for France, one of the highest values in the OECD.

### 3.4 Method caveats for PPS comparisons

1. **GDP PPP is not a "government services" PPP.** Public services are labor-intensive, so a government-output PPP would track wage levels more closely. Eurostat's "actual collective consumption" PPP (`ppp_cat18 = A04`, downloaded to `raw/13/ppp1_aic.json`) is an alternative, but it is built largely from input (compensation) prices. Using it would partly cancel the comparison of pay levels. The GDP PPP is the convention used by Eurostat for per-capita aggregates and by files 01 and 09.
2. **Per capita vs. % of GDP.** Economists disagree about the right denominator. % of GDP measures the burden on the economy. Per capita PPS measures the volume of resources per resident. A country with lower GDP per capita (France vs. the northern panel) looks "big" on the first and "average" on the second. **The platform should show both** (steelman, Section 6).

---

## 4. PISA 2025, TIMSS 2023, PIRLS 2021 and spending per student

### 4.1 PISA 2025: mean scores and ranks (15-year-olds; OECD, *PISA 2025 Results, Volume I*, Annex B1, published 8 Sep 2026)

| Indicator | France | OECD avg. (published) | OECD mean / median (38, our comp.) | **FR rank OECD (38)** | EU27 mean / median (our comp.) | **FR rank EU (27)** | Panel median | **FR rank panel (8)** | Source |
|---|---|---|---|---|---|---|---|---|---|
| Mathematics | **457.7** | 463.0 | 463.0 / 466.0 | **29** | 460.4 / 463.8 | **20** | 466.0 | **7** | [T10] Table I.B1.2a.3 |
| Reading | **456.3** | 460.9 | 460.9 / 464.7 | **23** | 451.3 / 456.3 | **14** | 462.6 | **6** | [T10] I.B1.2a.2 |
| Science (main domain) | **483.4** | 481.9 | 481.9 / 485.3 | **22** | 475.9 / 483.0 | **13** | 484.3 | **5** | [T10] I.B1.2a.1 |

Panel values (math / reading / science): Germany 464 / 465 / 486; Italy 468 / 474 / 483; Spain 457 / 451 / 477; Netherlands* 483 / 441 / 485; Belgium 480 / 466 / 490; Sweden 464 / 466 / 485; Denmark 471 / 460 / 478 [T10]. \* PISA sampling standards not met (asterisk in the OECD tables; also Canada, New Zealand, Norway, United States and Albania).

Note: France's math score (457.7) is statistically indistinguishable from Spain (457.4) and Luxembourg (458.1). Ranks must be presented with that caveat. The OECD publishes "range of ranks" confidence intervals (Annex A3), which were not extracted.

### 4.2 PISA trends: France vs. OECD, 2000/2003/2006/2015/2025

| Domain | France 2000/2003 | France 2006 | France 2015 | France 2022 | France 2025 | Change 2006→2025 (OECD median change; FR rank of fall, 1 = largest) | Change 2015→2025 (OECD median change; FR rank of fall) | Source |
|---|---|---|---|---|---|---|---|---|
| Mathematics | 510.8 (2003) | 495.5 | 492.9 | 473.9 | 457.7 | **-37.9** (-28.3; 13/37) | **-35.3** (-21.9; **8/38**) | [T10] I.B1.2a.38 |
| Reading | 504.7 (2000) | 487.7 | 499.3 | 473.9 | 456.3 | -31.4 (-25.0; 14/36) | **-43.0** (-23.5; 11/38) | [T10] I.B1.2a.37 |
| Science | | 495.2 | 495.0 | 487.2 | 483.4 | -11.8 (-12.6; 21/37) | -11.6 (-5.5; 15/38) | [T10] I.B1.2a.36 |

**France vs. OECD median (gap in points), constant-definition check:**

| Domain | 2006 | 2015 | 2022 | 2025 | Source |
|---|---|---|---|---|---|
| Mathematics | 0.0 (median 495.5, n = 37) | +0.2 (492.7, n = 38) | -5.2 (479.1, n = 37) | **-8.3** (466.0, n = 38) | [T10] (our computation) |
| Reading | -1.3 (489.0, n = 36) | +1.8 (497.5) | -5.0 (478.9) | **-8.4** (464.7) | [T10] |
| Science | -2.6 (497.8) | -0.6 (495.6) | -4.1 (491.3) | -1.9 (485.3) | [T10] |

**OECD trend averages for reference** (constant country sets, published) [T10]: OECD-23 mathematics 501.1 (2006) → 495.5 (2015) → 469.4 (2025); OECD-35 mathematics 490.7 (2006) → 487.2 (2015) → 465.5 (2025); OECD-23 reading 499.5 (2000) → 497.2 (2015) → 465.8 (2025); OECD-35 science 495.2 (2006) → 490.8 (2015) → 483.9 (2025).

**Reading.** In mathematics and reading, France sat at the OECD median in 2006 and 2015. It fell clearly below it after 2015, declining about 1.5 times faster than the median OECD country. In science its decline matches the OECD's. The fall is therefore partly OECD-wide (common shocks: COVID-19, smartphones, test mode) and partly French-specific (mathematics, reading). The OECD's Annex A1 discusses whether motivation and test-context effects contributed to the broad reading decline in 2018-2025. It concludes that they do not explain it away (annex not extracted in detail; see [T10]).

### 4.3 Low and top performers, socio-economic gradient (PISA 2025)

| Indicator | France 2025 | France 2015 | OECD mean 2025 / median | FR rank OECD 2025 | FR rank OECD 2015 | EU mean / median 2025 | FR rank EU 2025 | Source |
|---|---|---|---|---|---|---|---|---|
| Low performers in mathematics (below level 2), % | 35.7 | 23.5 | 34.9 / 32.5 | 28/38 (1 = fewest) | 24/38 | 34.8 / 33.4 | 20/27 | [T10] I.B1.2a.35 |
| **Top performers in mathematics (level 5+), %** | **5.2** | **11.4** | 7.8 / 6.9 | **28/38** (1 = most) | 14/38 | 6.7 / 6.0 | 20/27 | [T10] |
| Low performers in reading, % | 32.7 | 21.5 | 31.0 / 29.1 | 25/38 | 24/38 | 33.9 / 31.5 | 17/27 | [T10] I.B1.2a.34 |
| **Top performers in reading, %** | **4.5** | **12.5** | 5.5 / 4.6 | **20/38** | **5/38** | 4.2 / 3.8 | 10/27 | [T10] |
| Low performers in science, % | 25.8 | 22.1 | 25.7 / 24.1 | 25/38 | 25/38 | 27.3 / 24.9 | 17/27 | [T10] I.B1.2a.33 |
| Top performers in science, % | 6.7 | 8.0 | 7.2 / 7.1 | 21/38 | 16/38 | 6.1 / 5.7 | 12/27 | [T10] |
| Math: % of variance explained by ESCS (strength of gradient) | **14.8** | (21.5 in 2022, other scale; file 04) | 12.0 / 10.9 (n = 37) | **29/37** (1 = weakest link) | | 12.9 / 11.5 | 19/27 | [T10] I.B1.2b.4 |
| Math: score-point slope per unit of ESCS | 37.1 | | 34.7 / 34.2 | 25/37 | | 35.7 / 35.7 | 18/27 | [T10] |
| Math: top-quarter minus bottom-quarter ESCS gap (points) | 94.5 | | 82.9 / 81.4 | 27/37 | | 86.0 / 81.4 | 18/27 | [T10] |
| Reading: % variance explained by ESCS | 10.8 | | 9.2 / 9.0 | 31/37 | | 9.9 / 10.1 | 22/27 | [T10] I.B1.2b.3 |
| Science: % variance explained by ESCS | 13.5 | | 11.6 / 11.0 | 27/37 | | 12.5 / 11.9 | 17/27 | [T10] I.B1.2b.2 |

Data: `research/data/13_pisa2025_country_values.csv` (all 91 participants, all variables) and `13_pisa2025_group_stats.csv`. Raw StatLink workbooks: `raw/13/pisa25_mrq53f.xlsx` (I.B1.2), `pisa25_k68msa.xlsx` (I.B1.3), `pisa25_9i7u4g.xlsx` (I.B1.1).

**Key insight for the platform:** France's decline is concentrated at the **top** as well as the bottom. Top performers in mathematics fell from 11.4% to 5.2% and in reading from 12.5% to 4.5%. France was 5th of 38 for top readers in 2015 and is 20th in 2025. This contradicts the common story that only disadvantaged pupils are falling behind.

### 4.4 TIMSS 2023 and PIRLS 2021: ranks

| Assessment | France | OECD entities: n, mean, median | FR rank OECD | EU entities: n, mean, median | FR rank EU | Panel entities (FR rank) | Source |
|---|---|---|---|---|---|---|---|
| TIMSS 2023, grade 4 mathematics | **484** | 29; 525.3; 524 | **28/29** | 22; 523.6; 524 | **22/22 (last)** | 9 (incl. two Belgian communities): **9/9** (NL 537, SE 530, DE 524, DK 524, BE-Fl 521, IT 513, ES 498, BE-Fr 489) | [T14] Exhibit 1.1.1 |
| TIMSS 2023, grade 4 science | 488 | 29; 525.8; 526 | 26/29 | 22; 518.0; 523 | 19/22 | 7/9 | [T14] Exhibit 2.1.1 |
| TIMSS 2023, grade 8 mathematics | 479 | 20; 507.9; 507.5 | 18/20 | 13; 502.8; 504 | 12/13 | 3/3 (SE 517, IT 501) | [T14] Exhibit 1.2.1 |
| TIMSS 2023, grade 8 science | 486 | 20; 513.6; 519.5 | 18/20 | 13; 506.2; 512 | 11/13 | 3/3 (SE 521, IT 501) | [T14] Exhibit 2.2.1 |
| PIRLS 2021, grade 4 reading | 514 | ~~21; 529.3; 529~~ **22; 527.8; 528** (end-of-grade-4 countries; Türkiye 496 added) [corrected]. **All participants incl. delayed assessment: 28; 532.9; 533.5** | ~~18/21~~ **18/22 (end of grade 4); 24/28 (all)** [corrected] | 19; 527.1; 527 (end of grade 4). **All incl. delayed: 24; 532.0; 529.5** | **16/19 (end of grade 4); 21/24 (all)** [corrected] | 7/9 (SE 544, DK 539, IT 537, NL 527, DE 524, ES 521; then BE-Fl 511, BE-Fr 494) | [T15] Exhibit 1.1; Exhibit 1.3 (all participants, PIRLS 2021 International Results, ch. 1, p. 28: https://pirls2021.org/wp-content/uploads/2022/files/P21_1-reading-achievement.pdf) |

Data: `research/data/13_timss2023_ranks.csv`, `13_pirls2021_ranks.csv` (each row lists every entity and score). "Entities" include England and Northern Ireland separately (UK) and the two Belgian communities, which is why counts differ from country counts. Benchmarking participants (e.g. Quebec) are excluded. The OECD and EU averages match those quoted by the DEPP (file 04: 525 and 524 at grade 4).

### 4.5 Spending per student (EaG 2026, 2023 data) and the spending-vs-score scatter

| Country | Total expenditure per FTE student, primary to post-secondary non-tertiary (USD PPP, GDP PPPs) | of which government | Lower and upper secondary, total | PISA 2025 mean of 3 domains | Source |
|---|---|---|---|---|---|
| **France** | **14,932** | **13,400** | **16,745** | **465.8** | [T12] Table C1.1; [T10] |
| Germany | 17,123 | 14,918 | 18,924 | 471.5 | [T12][T10] |
| Italy | 14,848 | 13,970 | 14,541 | 475.0 | [T12][T10] |
| Spain | 14,009 | 11,963 | 15,051 | 462.0 | [T12][T10] |
| Netherlands | 18,363 | 16,248 | 20,142 | 470.0 | [T12][T10] |
| Belgium | 19,027 | 18,168 | 20,739 | 478.6 | [T12][T10] |
| Sweden | 16,353 | 16,323 | 16,247 | 471.9 | [T12][T10] |
| Denmark | 17,055 | 15,934 | 16,947 | 469.4 | [T12][T10] |
| OECD average | 14,436 | 13,231 | 15,003 | 468.6 (avg. of 3 OECD means) | [T12][T10] |
| EU25 average (EaG) | 14,004 | 12,860 | 14,598 | | [T12] |
| OECD median (35 with both data, our comp.) | 14,717 | | | | [T12] |
| **France rank** | **16/35 OECD; 9/25 EU; 6/8 panel** | | | 7/8 panel | [T12][T10] (our computation) |

**Scatter statistics (our computation, `research/data/13_scatter_spending_vs_pisa2025.csv`):**

| Sample | n | Slope (PISA points per USD 1,000) | Correlation r | R² | France residual (points) | Source |
|---|---|---|---|---|---|---|
| OECD, all | 35 | +1.2 | 0.24 | 0.06 | **-6.4** | [T12][T10] |
| OECD, spending ≥ USD 10,000 | 29 | -1.2 | -0.26 | 0.07 | **-13.4** | [T12][T10] |
| EU (OECD-EaG coverage) | 25 | +1.3 | 0.30 | 0.09 | -1.5 | [T12][T10] |
| EU, spending ≥ USD 10,000 | 19 | -0.9 | -0.35 | 0.12 | -9.9 | [T12][T10] |

Notable points: Estonia (USD 11,418; PISA average 511), Poland (11,056; 487), Japan (12,013; 522), Ireland (15,496; 493). Luxembourg (32,766; 458) and Norway (20,528; 458) spend far more for lower scores. Spending is 2023 (latest EaG year) and scores are 2025. Cross-country correlations say nothing about causality within a country (Section 6).

---

## 5. PLF 2027: the official staffing plan (*schéma d'emplois*)

Source: *Projet de loi de finances pour 2027*, Assemblée nationale no. 3210, registered **1 Oct 2026**. The figures come from the Exposé général des motifs (p. 17-18, table "Emplois État / Opérateurs") and from Articles 63 (state ceiling) and 64 (operators' ceiling) with their exposés des motifs [T16]. Local copy: `raw/13/plf/plf2027_an3210.pdf`. Units: *schéma d'emplois* = net change in FTE (ETP) over the year. *Plafond d'emplois* (employment ceiling) = annual average full-time-equivalent jobs worked (ETPT).

### 5.1 Totals

| Item | Value | Unit | Source |
|---|---|---|---|
| State *schéma d'emplois* (general budget + annexed budgets) | **+8,025** | ETP | [T16] p. 18 and Art. 63 |
| of which teacher-training reform (*réforme de la formation initiale des enseignants*) | +4,742 | ETP | [T16] |
| State excl. that reform | +3,283 | ETP | [T16] Art. 63 |
| of which re-internalized digital jobs | +404 | ETP | [T16] |
| of which central administrations (*administration centrale*) | -812 (text: "-800") | ETP | [T16] |
| State operators' *schéma d'emplois* | **-1,209** | ETP | [T16] Art. 64 |
| State + operators | **+6,816** | ETP | [T16] |
| Total incl. social security funds (-1,000) and excl. teacher-training reform and LPM trajectory | **-1,076** | ETP | [T16] p. 17-18 |
| State employment ceiling 2027 | 2,032,750 (+16,162 vs. LFI 2026) | ETPT | [T16] Art. 63 |
| Breakdown of +16,162: 2027 schéma +3,987; full-year effect of 2026 changes +5,575; transfers/scope +2,929 (mainly AED education assistants moved onto the state payroll); technical corrections +3,671 (incl. the new national military service with 4,000 conscripts and a 2,627 ETPT structural-vacancy abatement) | | ETPT | [T16] |
| Operators' ceiling 2027 | 397,282 (-4,107) | ETPT | [T16] Art. 64 |
| Breakdown: schéma -998; 2026 full-year effect -235; structural-vacancy abatements -3,248 (of which research and higher education -3,040); transfers/corrections +374 | | ETPT | [T16] |

### 5.2 By ministry (State *schéma d'emplois*, ETP; operators in parentheses)

| Ministry | State | Operators | State + operators | Source |
|---|---|---|---|---|
| Éducation nationale | **+3,257** (incl. +4,742 training reform, so -1,485 excl.) | (-150) | +3,107 | [T16] |
| Armées et anciens combattants | **+2,090** (military +1,540) | (+41) | +2,131 | [T16] |
| Intérieur | **+1,381** (police and gendarmerie +1,355) | (+19) | +1,400 | [T16] |
| Justice | **+1,301** (magistrates, clerks, prison staff +1,078) | (0) | +1,301 | [T16] |
| Services du Premier ministre | +89 | (-15) | +74 | [T16] |
| Aménagement du territoire et décentralisation | +50 | (-10) | +40 | [T16] |
| Travail et solidarités | +20 | **(-689)** | -669 | [T16] |
| Transition écologique | -73 | (-156) | -229 | [T16] |
| Économie, finances et souveraineté | -81 | (-119) | -200 | [T16] |
| Agriculture | -84 | (-12) | -96 | [T16] |
| Europe et affaires étrangères | -38 | (-15) | -53 | [T16] |
| Culture | +6 | (-31) | -25 | [T16] |
| Sports, jeunesse et vie associative | -12 | (-23) | -35 | [T16] |
| Enseignement supérieur, recherche et espace | +7 | (0) | +7 | [T16] |
| Transports | ~~(row incomplete in the extracted text; operators -44)~~ no State line (greyed cell in the bill table) [corrected after reading the rendered p. 18] | (-44) | -44 | [T16] |
| Outre-mer | -3 | (-10) | -13 | [T16] |
| Action et comptes publics | 0 (Plan Douane 2030 +200, offset elsewhere) | (0) | 0 | [T16] |
| Budget annexe Contrôle et exploitation aériens | +110 | (+5) | +115 | [T16] |
| Budget annexe Publications officielles | +5 | | +5 | [T16] |
| **Total** | **+8,025** | **(-1,209)** | **+6,816** | [T16] |

**Divergence with file 04 / the press:** file 04 cited *Café pédagogique* for "1,588 teaching posts cut" in education. The bill shows Éducation nationale at -1,485 ETP once the teacher-training reform is excluded. The two figures cover different scopes (teachers only vs. the whole ministry). ~~The *Café pédagogique* figure was **not verified** against the "Enseignement scolaire" *Bleu* (PAP).~~ **Verified 2026-10-25 against the ministry's own PLF 2027 press kit** (*Budget 2027 pour l'École*, Ministère de l'Éducation nationale, 1 Oct 2026, p. 7) [T19]: "le solde net est donc une reprise de 1 588 ETP enseignants" (public and private; -1,250 in public schools), against -4,000 in the LFI 2026. Full reconciliation with the bill: -1,588 teachers + 1,804 support posts (incl. 1,300 AESH) + 3,041 trainee teachers (*élèves fonctionnaires et stagiaires*) = **+3,257 FTE**, exactly the bill's Éducation nationale line. The press kit counts the demographic adjustment as -3,644 teaching posts offset by +2,056 posts reallocated to schools. The "-1,485 excl. training reform" in the bill and the "-1,588 teachers" in the press kit are different cuts of the same +3,257 and should not be added. The IFRAP (liberal-leaning think tank) reading "+8,025 ETP" matches the bill. The detailed programme-level *Bleus budgétaires* and the *Jaune* "Rapport sur l'état de la fonction publique et les rémunérations" annexed to the PLF 2027 were not retrieved. The bill is the primary legal source for the totals.

---

## 6. Steelman, economists' disagreements and implications for the thesis

**Evidence in this file that supports the platform's thesis** ("spending structure, not only amounts, must be questioned"):
- France's public-employment share has been 4-7 pts above the EU median for 20 years, and its OECD production costs are 3rd-highest as a share of GDP (28.4%) [T3][T7].
- School spending per student is at or slightly above the OECD average while PISA mathematics and reading fell 1.5 times faster than in the median OECD country since 2015, and TIMSS grade-4 mathematics is last in the EU [T10][T12][T14].
- Cross-country, spending per student barely correlates with PISA scores (R² 0.06). Countries such as Estonia, Poland and Japan obtain much better results with less money [T10][T12].

**The strongest counter-arguments (to be presented fairly):**
1. **Per capita, the French state is not large.** In PPS per inhabitant, France's production costs (9,848) are 8% above the EU average and *below* Germany, the Netherlands, Belgium, Sweden and Denmark. Its wage bill per inhabitant is below Belgium, Sweden and Denmark. "% of GDP" overstates France's size because its GDP per capita is lower than in these countries [T6]. *Disagreement:* fiscal economists (e.g. Fipeco, Institut Montaigne) usually argue that % of GDP is the relevant burden measure. Proponents of public services (OFCE, many public-finance academics) argue that per-capita volume is the relevant service measure. Both are valid for different questions.
2. **Make-or-buy explains much of the headcount gap.** On the O+P+Q measure France is at the panel median (+0.1 pt in 2025). Germany finances roughly 6.8 million O+P+Q workers outside government, including about 2.1 million in non-profit welfare associations [T4][T13]. "Fewer civil servants" in Germany largely means "the same workers on a different payroll".
3. **The gap is closing without reforms of the statute.** France's GG employment share fell 1.8 pts (2005-2023) while the sample median rose. The gap to the EU median shrank from about 7 to about 4 pts [T5].
4. **Spending-outcome correlations are weak in both directions.** A near-zero cross-country correlation shows that money is not sufficient. It does not show that cutting money is harmless. Quasi-experimental studies find causal effects of school spending on outcomes in some settings: Jackson, Johnson and Persico (*Quarterly Journal of Economics* 131(1), Feb 2016, pp. 157-218, doi:10.1093/qje/qjv036) find for US cohorts born 1955-1985 that a 10% increase in per-pupil spending in every year of K-12 school leads to 0.31 more completed years of education, about 7% higher adult wages and a 3.2-point lower annual incidence of adult poverty, with much larger effects for children from low-income families. The production-function literature finds weak links: Hanushek ("The Failure of Input-based Schooling Policies", *Economic Journal* 113(485), Feb 2003, pp. F64-F98, doi:10.1111/1468-0297.00099) reviews US and international evidence and concludes that large resource increases "have yielded little in the way of general improvement in student achievement", in contrast with teacher-quality effects. (Verified 2026-10-25 against the publishers' abstracts via Crossref and NBER [T20][T21]; was "cited from memory".) France also under-spends at **primary** level, where TIMSS shows the weakest results (file 04, Section 6.1.1), and pays teachers below the OECD average (file 04, Section 6.1.2).
5. **Part of the PISA decline is common to all OECD countries.** In science, France's decline matches the OECD median [T10]. The PLF 2027 increases education staff mainly through the teacher-training reform, which aims at teacher quality rather than headcount [T16].

**Where the evidence is clear against the defense of the status quo:** the joint collapse of French top *and* bottom performers in mathematics and reading after 2015 is larger than the OECD median decline [T10]. So is the steeper socio-economic gradient (rank 29/37) [T10]. These are allocation and pedagogy questions, and they cannot be answered by more money alone.

---

## 7. Divergences between sources

| Topic | Source A | Source B | Explanation |
|---|---|---|---|
| France GG employment share 2019 | GaaG 2021: 21.2% [T2] | GaaG 2025: 21.7% [T3]; ILO/Eurostat computed: 21.7% [T5] | Insee 2020-base national accounts revision (sector reclassification) and different employment vintages |
| France GG employment share 2023 | GaaG 2025: 20.7% [T3] | Computed: 20.9% [T5][T4] | Different denominator vintage (Eurostat Oct 2026 vs. OECD early 2025) |
| Italy GG share 2023 | GaaG 2025: 13.7% [T3] | ILO-based: 12.3% [T5] | ILO numerator narrower (excl. some units). Flagged |
| Canada, Israel, Poland, Mexico, Costa Rica, Ireland, Croatia | GaaG | ILO-based | ILO series partial (e.g. Canada 6.3% vs. 20.2%). Excluded from group stats |
| Production costs France | Eurostat D.1+P.2+D.632: 24.3% GDP (2025; file 04) | OECD GaaG: 28.4% GDP (2023) [T7] | OECD adds consumption of fixed capital and other taxes on production (4.2 pts of GDP for France) |
| PPS per capita TE 2024 | File 01 (superseded): 22,321, 9th of 27 (prc_ppp_ind, 2025-07-10) | This file: 22,395 (prc_ppp_ind_1, 2026-07-09); file 00 canonical: 22,398, 8th of 27 (2024) and **23,330, 8th of 27 (2025)** | New PPP vintage (COICOP 2018); the 8th/9th difference is a near-tie with Sweden |
| PISA 2025 France rank in mathematics | Ministry document: "lost 8 places" (file 04 [S12c]) | Our computation: 22nd/37 (2022) to 29th/38 (2025) = 7 places among OECD members | Different country sets (all participants vs. OECD; Costa Rica and Colombia membership) |
| 1980 civil-service headcount | Cour des comptes 2009 text: "3.86 million in 1980 to 5.27 million in 2006" | Same report, Table 2: 5,267,935 is the **2007** value; 2006 is 5,226,801 | Internal inconsistency in the report text; the table is used here |
| Education posts PLF 2027 | *Café pédagogique*: -1,588 teaching posts (file 04 [S7]) | PLF 2027 bill: Éducation nationale +3,257 ETP, -1,485 excl. training reform [T16] | Scope (teachers vs. ministry). The -1,588 is confirmed by the ministry press kit [T19] (corrected 2026-10-25: was "press figure unverified"); +3,257 = -1,588 teachers + 1,804 support + 3,041 trainees |

---

## 8. Historical baseline: civil-service headcount 1980-2007 (official)

**Source:** Cour des comptes, *Les effectifs de l'État 1980-2008 - Un état des lieux*, thematic public report, December 2009, Table 2. Data: "INSEE, DREES, DHOS - Traitement DGAFP". Scope: main jobs, all statuses, excluding subsidized jobs. Headcount at 31 December [T17].

| Year | FPE (state) | FPT (local) | FPH (hospital) | Total three branches | Population | Civil service share of total employment (Table 5) | Source |
|---|---|---|---|---|---|---|---|
| **1980** | 2,173,169 | 1,021,000 | 670,791 | **3,864,960** | 53,731,000 | **17.8%** | [T17] |
| 1986 | 2,287,458 | 1,121,383 | 756,201 | 4,165,042 | 55,411,000 | 19.4% | [T17] |
| **1990** | 2,307,816 | 1,166,364 | 783,473 | **4,257,653** | 56,577,000 | **19.0%** | [T17] |
| 1996 | 2,401,791 | 1,262,361 | 825,710 | 4,489,862 | 57,936,000 | 20.1% | [T17] |
| 2000 | 2,472,102 | 1,371,928 | 855,660 | 4,699,690 | 60,508,000 | 19.4% | [T17] |
| 2006 | 2,546,091 | 1,662,360 | 1,018,351 | 5,226,801 | 63,186,000 | 20.8% | [T17] |
| 2007 | 2,484,484 | 1,748,378 | 1,035,073 | 5,267,935 | 63,578,000 | 20.6% | [T17] |
| Change 1980-2007 | +14.3% | +71.2% | +54.3% | **+36.3%** | +18.3% | | [T17] |
| FTE (Table 3): 1986 / 2007 | 2,189,942 / 2,350,922 | 1,028,163 / 1,590,723 | 702,088 / 955,899 | 3,920,193 / 4,897,544 (+24.9%) | | | [T17] |
| *For comparison:* 2024 (SIASP, new series) | 2,581,900 | 2,017,800 | 1,248,600 | 5,848,300 | | 19.8% | file 04 [S1] |

Exclusions (Table 2, notes a-b): La Poste and France Télécom (about 450,000 agents in 1990) are excluded throughout. Private-school teachers under contract paid outside the employment ceilings are excluded: 99,650 in 1980 and 154,000 in 2006. **Including them, growth 1980-2006 was +40.3%** [T17]. Hospital contract staff on replacement credits are also excluded. Total employment in Table 5 covers metropolitan France excluding conscripts.

**Usability:** this is an official, DGAFP-processed series, so the "1980 baseline: not confirmed" open item in file 04 (Section 3.3 and gap 1) is now resolved. **However, 1980-2007 (Cour des comptes/DGAFP, pre-SIASP sources) and 1996/2011-2024 (SIASP) are different series.** The scope of private-school teachers differs: they are excluded here but included in SIASP 2024 "other categories" (file 04, Section 1). There are also methodological breaks (2009 SIASP introduction, 2024 DSN change). **A 1980-2024 growth rate (5.85 m / 3.86 m = +51%) mixes these scopes and should not be published as such.** A defensible statement: "about 3.9 million agents in 1980 and 4.3 million in 1990 (excluding La Poste/France Télécom and contract private-school teachers), against 5.85 million in 2024 on a broader perimeter." Insee's national-accounts S.13 employment series back to 1980 would provide a consistent alternative but was not located (gap).

---

## 9. Open questions and gaps

1. **OECD SDMX downloads** (employment by institutional sector, GaaG yearly updates) were blocked by Cloudflare. If the OECD database series becomes reachable, re-run `scripts/13/pubemp.py` with it to replace the ILO-based numerators.
2. **Germany 2022-2023 jump** in the ILO GG series (+250,000) was not explained. Belgium has no ILO GG data after 2022.
3. **Destatis hospital personnel by ownership** (public, non-profit, private) was not retrieved. BAGFW is an association source.
4. **PISA "range of ranks"** confidence intervals (Annex A3) were not extracted. Ranks are point ranks.
5. **PLF 2027 *Bleus* (PAP by programme) and the *Jaune* on the civil service** were not retrieved. The Transports row of the bill table was garbled in text extraction.
6. **Insee national-accounts S.13 employment 1980-1999** (consistent long series) was not located.
7. **Government-output PPP** sensitivity (PPS per capita using the collective-consumption PPP) was not computed. The data are downloaded (`raw/13/ppp1_aic.json`).
8. ~~Literature references in Section 6, item 4 (Jackson et al. 2016; Hanushek) are cited from memory and were not re-checked today.~~ Resolved 2026-10-25: both references verified (Section 6, item 4; [T20][T21]).

---

## 10. Sources

| ID | Institution | Title / dataset | Publication / update date | URL (accessed 2026-10-25) |
|---|---|---|---|---|
| T1 | OECD | *Government at a Glance 2021*, Section 3.1 "Employment in general government" (text: OECD 18.2% in 2007, 17.9% in 2019) | 9 Jul 2021 | https://www.oecd.org/en/publications/government-at-a-glance-2021_1c258f55-en/full-report/component-23.html |
| T2 | OECD | GaaG 2021, Figure 3.1 StatLink "Employment in general government as a percentage of total employment, 2007 and 2019" | 9 Jul 2021 | https://doi.org/10.1787/888934257337 (local `raw/13/gaag2021_fig3_1.xlsx`; CSV `data/13_oecd_gaag2021_fig3_1_gg_emp_share_2007_2019.csv`) |
| T3 | OECD | GaaG 2025, Figure 13.1 (2019 and 2023) | 19 Jun 2025 | https://stat.link/8htodn ; CSV `data/04_oecd_gaag2025_gg_employment_share.csv` (file 04) |
| T4 | Eurostat | `nama_10_a64_e` employment by NACE (TOTAL, O, P, Q, O-Q; EMP_DC, thousand persons) | Updated 21 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/nama_10_a64_e/default/table ; API: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_a64_e?format=JSON&unit=THS_PER&na_item=EMP_DC&nace_r2=TOTAL&nace_r2=O&nace_r2=P&nace_r2=Q&nace_r2=O-Q ; CSV `data/13_eurostat_nama_10_a64_e_OPQ.csv` |
| T5 | ILO (ILOSTAT) | `DF_EMP_XPSE_GOV_NB` Public employment by sectors and sub-sectors of national accounts (discontinued series, data to 2024); `DF_EMP_2EMP_SEX_AGE_NB` modelled employment; `DF_EMP_TEMP_SEX_INS_NB` LFS employment by public/private sector | Accessed 25 Oct 2026 | https://sdmx.ilo.org/rest/data/ILO,DF_EMP_XPSE_GOV_NB,1.0/?startPeriod=2000 ; https://sdmx.ilo.org/rest/data/ILO,DF_EMP_2EMP_SEX_AGE_NB,1.0/ ; https://sdmx.ilo.org/rest/data/ILO,DF_EMP_TEMP_SEX_INS_NB,1.0/ (raw `raw/13/ilo_*.csv`; derived `data/13_gg_employment_share_ilo_2000_2024.csv`, `13_ilo_lfs_public_sector_share.csv`) |
| T6 | Eurostat | `gov_10a_main` (D1PAY, D11PAY, P2, D632PAY, TE; S.13; MIO_EUR), `nama_10_pe` (POP_NC), **`prc_ppp_ind_1`** (PLI_EU27_2020, GDP; COICOP 2018) and `prc_ppp_ind` (old vintage) | 21 Oct 2026; 21 Oct 2026; **9 Jul 2026**; 10 Jul 2025 | https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table ; https://ec.europa.eu/eurostat/databrowser/view/prc_ppp_ind_1/default/table ; catalogue: https://ec.europa.eu/eurostat/api/dissemination/catalogue/toc/txt?lang=en ; CSVs `data/13_eurostat_gov_10a_main_D1_P2_D632_mioeur.csv`, `13_eurostat_nama_10_pe_pop.csv`, `13_eurostat_prc_ppp_ind_1_PLI_GDP.csv` |
| T7 | OECD | GaaG 2025, Section 16.5 "Production costs and outsourcing", Figure 16.12 | 19 Jun 2025 | https://www.oecd.org/en/publications/government-at-a-glance-2025_0efd0bcd-en/full-report/production-costs-and-outsourcing_af2e6a54.html ; data https://stat.link/mepiad (CSV `data/13_oecd_gaag2025_fig16_12_production_costs.csv`) |
| T8 | OECD | GaaG 2025, Table 15.3 "Structure of government expenditures by economic transaction" | 19 Jun 2025 | https://www.oecd.org/en/publications/government-at-a-glance-2025_0efd0bcd-en/full-report/structure-of-government-expenditures-by-economic-transaction_72b48e08.html ; data https://stat.link/xwvmru (CSV `data/13_oecd_gaag2025_tab15_3_D1_share_TE_2023.csv`) |
| T9 | Eurostat (via file 09) | `nama_10_pc` GDP per capita in PPS (cross-check) | 22 Oct 2026 | https://ec.europa.eu/eurostat/databrowser/view/nama_10_pc/default/table |
| T10 | OECD | *PISA 2025 Results (Volume I)*, Annex B1 Tables I.B1.2a.1-50 and I.B1.2b.1-38 | 8 Sep 2026 | https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/results-for-countries-and-economies_33854635.html ; data https://stat.link/mrq53f , https://stat.link/k68msa , https://stat.link/9i7u4g (CSVs `data/13_pisa2025_country_values.csv`, `13_pisa2025_group_stats.csv`) |
| T11 | OECD | PISA 2025 Vol. I, Annex A1 "Trends in reading scores over three PISA cycles (2018-2025)" | 8 Sep 2026 | https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report/trends-in-reading-scores-over-three-pisa-cycles-2018-2025_3fb6c775.html |
| T12 | OECD | *Education at a Glance 2026*, Chapter C1, Table C1.1 "Expenditure on educational institutions per full-time equivalent student (2023)" | Sep 2026 (data cut-off 17 Jun 2026) | https://www.oecd.org/en/publications/education-at-a-glance-2026_b4968bbc-en/full-report/key-system-level-indicators-of-education-finance_d143f855.html ; data https://stat.link/ax7gjn (CSV `data/13_eag2026_C1_1_spending_per_student_2023.csv`; scatter `data/13_scatter_spending_vs_pisa2025.csv`) |
| T13 | BAGFW (Bundesarbeitsgemeinschaft der Freien Wohlfahrtspflege; umbrella association, **not an official statistics office**) | *Gesamtstatistik 2020 - Einrichtungen und Dienste der Freien Wohlfahrtspflege*, overview 1970-2020 and full report (44 pp.) | Dec 2023 (verified: cover "Dezember 2023", file dated 14 Dec 2023); reference date 1 Jan 2020 per methodology (foreword says 31 Dec 2020) | https://alt2024.bagfw.de/fileadmin/user_upload/Veroeffentlichungen/Publikationen/Statistik_2020/Einzelseiten/BAGFW_Gesamtstatistik_2020_Ueberblick_Entwicklung_Arbeitsbereiche.pdf ; full report https://alt2024.bagfw.de/fileadmin/user_upload/Veroeffentlichungen/Publikationen/Statistik_2020/Einzelseiten/BAGFW_Gesamtstatistik_2020_2023-12-14_ES.pdf (local `raw/13/bagfw/`) |
| T13b | BAGFW (association source, as T13) | *BAGFW-Gesamtstatistik 2024*, "Gesamtüberblick" and "Arbeitsbereiche" (2,174,073 employees on 1 Jan 2024; 61.7% part-time) | Imprint June 2026; PDFs posted Sep 2026 | https://www.bagfw.de/veroeffentlichungen/statistik ; https://www.bagfw.de/fileadmin/user_upload/Veroeffentlichungen/Publikationen/Statistik_2024/Einzelseite_Gesamtueberblick-Entwicklungen.pdf ; https://www.bagfw.de/fileadmin/user_upload/Veroeffentlichungen/Publikationen/Statistik_2024/BAGFW_Gesamtstatistik_2024_Arbeitsbereiche.pdf (local `raw/13/bagfw/`) |
| T14 | IEA (TIMSS & PIRLS International Study Center, Boston College) | *TIMSS 2023 International Results*, Exhibits 1.1.1, 2.1.1 (grade 4), 1.2.1, 2.2.1 (grade 8) | 4 Dec 2024 | https://timss2023.org/wp-content/uploads/2024/11/1-1-1_ach-g4m-dist.xlsx ; .../2-1-1_ach-g4s-dist.xlsx ; .../1-2-1_ach-g8m-dist.xlsx ; .../2-2-1_ach-g8s-dist.xlsx (CSV `data/13_timss2023_ranks.csv`) |
| T15 | IEA | *PIRLS 2021 International Results in Reading*, Exhibit 1.1 | 16 May 2023 | https://pirls2021.org/wp-content/uploads/2022/files/1_1-2_achievement-results-1.xlsx (CSV `data/13_pirls2021_ranks.csv`) |
| T16 | Government of France / Assemblée nationale | *Projet de loi de finances pour 2027*, no. 3210, Exposé général des motifs (p. 17-18) and Articles 63-64 | Registered 1 Oct 2026 | https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf (local `raw/13/plf/plf2027_an3210.pdf`) |
| T17 | Cour des comptes (DGAFP data processing) | *Les effectifs de l'État 1980-2008 - Un état des lieux*, rapport public thématique, Tables 2, 3, 5 | Dec 2009 (released 17 Dec 2009) | https://www.vie-publique.fr/sites/default/files/rapport/pdf/094000601.pdf (local `raw/13/hist/ccomptes_effectifs_etat_1980_2008.pdf`) |
| T19 | Ministère de l'Éducation nationale | *Budget 2027 pour l'École - dossier de presse* (PLF 2027), p. 7 | 1 Oct 2026 | https://www.education.gouv.fr/sites/default/files/document/budget-2027-pour-l-cole-le-dossier-de-presse-521314.pdf (local `raw/13/plf/men_dp_budget2027.pdf`) |
| T20 | Oxford University Press / *QJE* | Jackson, C. K., R. C. Johnson and C. Persico, "The Effects of School Spending on Educational and Economic Outcomes: Evidence from School Finance Reforms", *Quarterly Journal of Economics* 131(1): 157-218 | Online 1 Oct 2015; print Feb 2016 | https://doi.org/10.1093/qje/qjv036 (abstract read via https://api.crossref.org/works/10.1093/qje/qjv036 ; NBER WP 20847: https://www.nber.org/papers/w20847) |
| T21 | Royal Economic Society / *Economic Journal* | Hanushek, E. A., "The Failure of Input-based Schooling Policies", *Economic Journal* 113(485): F64-F98 | Feb 2003 | https://doi.org/10.1111/1468-0297.00099 (abstract: NBER WP 9040, https://www.nber.org/papers/w9040) |
| T18 | iFRAP (Fondation pour la recherche sur les administrations et les politiques publiques; liberal-leaning think tank) | "Encore 8 000 agents en plus pour l'État en 2027" (secondary reading of PLF 2027; consistent with T16) | Oct 2026 | https://www.ifrap.org/etat-et-collectivites/encore-8-000-agents-en-plus-pour-letat-en-2027 |

### CSV files produced (all under `research/data/`)

`13_eurostat_nama_10_a64_e_OPQ.csv`, `13_eurostat_OPQ_share_2000_2025.csv`, `13_gg_employment_share_ilo_2000_2024.csv`, `13_public_employment_stats.csv`, `13_gg_employment_balanced_gap.csv`, `13_ilo_lfs_public_sector_share.csv`, `13_OQ_employment_outside_gg.csv`, `13_oecd_gaag2021_fig3_1_gg_emp_share_2007_2019.csv`, `13_eurostat_gov_10a_main_D1_P2_D632_mioeur.csv`, `13_eurostat_nama_10_pe_pop.csv`, `13_eurostat_prc_ppp_ind_1_PLI_GDP.csv`, `13_pps_per_capita_wagebill_production_costs.csv`, `13_pps_per_capita_stats.csv`, `13_oecd_gaag2025_fig16_12_production_costs.csv`, `13_oecd_gaag2025_tab15_3_D1_share_TE_2023.csv`, `13_pisa2025_country_values.csv`, `13_pisa2025_group_stats.csv`, `13_timss2023_ranks.csv`, `13_pirls2021_ranks.csv`, `13_eag2026_C1_1_spending_per_student_2023.csv`, `13_scatter_spending_vs_pisa2025.csv`.

Scripts: `research/scripts/13/pubemp.py`, `balanced.py`, `pps.py`, `pisa.py`, `timss.py`, `eag.py`, `scatter.py` (run with `python3 -I <script> <research_dir>`).

---

## Verification log (2026-10-25)

*Adversarial fact-check. Every primary source was re-downloaded independently into `research/data/raw/13_factcheck/` (untrusted data, not executed). Figures were recomputed with fresh scripts rather than the author's (Eurostat API pulls of 25 Oct 2026; `nama_10_a64_e` and `nama_10_pe` updated 21 Oct 2026, `gov_10a_main` updated 21 Oct 2026, `prc_ppp_ind_1` updated 9 Jul 2026). Corrections are shown in place with strikethrough.*

| # | Claim | Verdict | Evidence / correction |
|---|---|---|---|
| 1 | FR GG employment share 22.7% (2005) to 20.9% (2023); balanced EU-17 gap +6.9 to +4.0; EU rank 6 to 5 | **Confirmed** | ILO `DF_EMP_XPSE_GOV_NB` (re-downloaded, source "SNA - Comptes Nationaux") / Eurostat EMP_DC: 22.68% and 20.86%; medians 15.80 and 16.82; gaps +6.88 and +4.04; ranks 6 and 5. Minor: 2022 and 2024 are 20.95%, so they round to 20.9, not 21.0 (corrected in Section 2.2). |
| 2 | GaaG 2021: France 22.35% in 2007, rank 8/33, OECD average 18.2% | **Partly corrected** | Value and OECD average confirmed (StatLink 888934257337, and the GaaG 2021 text "18.2% of total employment in 2007"). **Only 31 OECD countries have a 2007 value, so the rank is 8/31, not 8/33.** The 2007 OECD mean and median are 18.2 / 18.0, not 17.7 / 17.4. For 2019 the n = 33 figure (with Korea and Switzerland) gives 17.4 / 16.7 and rank 8/33. The EU statistics (18.2 / 17.4, rank 5/23) are confirmed. |
| 3 | NACE O+P+Q 2025: FR 29.2, DE 27.0, NL 29.0, BE 30.4, SE 32.8, DK 30.4; FR rank 5/27, 4/8, +0.1 pt | **Confirmed** | Recomputed exactly (panel median 29.13, gap +0.11). The whole 2000-2025 series is confirmed, except the 2000 EU mean (21.2 vs. 21.3, rounding). |
| 4 | BAGFW: 2,076,535 employees (2020) | **Confirmed** | Gesamtstatistik 2020 overview PDF, "Gesamt / Beschäftigte" column. Also confirmed: 1,673,861 (2012), 1,121,043 (1996), 751,126 (1990); elderly care 551,278; health care 437,263; youth services 472,822. ~~Unverified: the "about 60% part-time" share and the "published Dec 2023" date do not appear in this PDF.~~ Both resolved in the second pass below (59% part-time; Dec 2023 confirmed). |
| 5 | D.1 per inhabitant in PPS 2025: FR 5,035 vs. EU27 4,304 (index 117; 139 in 2005), rank 8/27 | **Confirmed** | Exact recomputation (France PLI 106.5 in 2025, 111.9 in 2005). |
| 6 | Production costs per inhabitant in PPS: FR 9,848 vs. EU 9,133 (108); DE 11,704; NL 14,372; BE 11,873; SE 11,188; DK 12,877; rank 10/27, 6/8 | **Confirmed** | Exact recomputation. Also confirmed: TE 23,327 PPS (index 113), D.11 3,369 (rank 13/25) and EA20 values. |
| 7 | GaaG 2025: D.1 12.3% of GDP, rank 7/36 (OECD 8.8); 21.5% of total expenditure, rank 26/37 | **Confirmed** | Fig. 16.12 (stat.link/mepiad) and Table 15.3 (stat.link/xwvmru), both versions of 19 Jun 2025. Rank 7 holds with or without Chile (n = 36 or 37). |
| 8 | GaaG 2025 production costs: FR 28.4% of GDP, rank 3/36, OECD 20.8% | **Confirmed**, with a source caveat | The OECD text (page visited in a headless browser) reads "Finland (31.1%), Sweden (30.3%) and France (28.4%)". The StatLink components for Finland add up to **31.9%**. The inconsistency is inside the OECD source (annotated in Section 3.3), and France's rank is unaffected. |
| 9 | PISA 2025 math: 457.7 vs. OECD 463.0, median 466.0; rank 29/38, 20/27 (EU median 463.8), 7/8 | **Confirmed** | StatLink mrq53f, "PISA 2025 Results (Volume I)", last updated 08-Sep-2026, Table I.B1.2a.3. |
| 10 | Reading 456.3 (OECD 460.9; 23/38; EU 14/27); science 483.4 (481.9; 22/38; 13/27) | **Confirmed** | Tables I.B1.2a.2 and I.B1.2a.1. |
| 11 | Math change -35.3 since 2015 (median -21.9; 8th-largest fall); -37.9 since 2006 (median -28.3); gap to the median 0.0 / +0.2 / -8.3 | **Confirmed** | Table I.B1.2a.38. The median change since 2015 (-21.9) happens to equal the published OECD-average change. The 2025 gap is -8.3 or -8.4 depending on rounding. Reading -43.0 (rank 11) and science -11.6 (rank 15) are also confirmed. |
| 12 | Top performers in math: 5.2% (11.4% in 2015); OECD 7.8%; rank 28/38 | **Confirmed** | Table I.B1.2a.35. All other low- and top-performer rows in Section 4.3 are also confirmed. |
| 13 | ESCS: 14.8% of variance vs. OECD 12.0%; rank 29/37 | **Confirmed** | stat.link/k68msa, Table I.B1.2b.4 (Costa Rica missing, hence n = 37). The slope (37.1, 25/37) and the top-minus-bottom-quarter gap (94.5, 27/37) are also confirmed. |
| 14 | TIMSS 2023 grade 4 math: France 484; last of 22 EU entities (mean 523.6); 28/29 OECD (mean 525.3) | **Confirmed** | IEA Exhibit 1.1.1 xlsx. |
| 15 | PIRLS 2021: 514; 16/19 EU (median 527); 18/21 OECD | **Corrected** | (a) The OECD set omitted Türkiye (496): the correct figure is 18/22, with mean 527.8 and median 528. (b) Exhibit 1.1 covers only countries tested at the end of grade 4. Exhibit 1.3 also covers the 14 delayed-assessment countries (Ireland 577, Croatia 557, Lithuania 552, US 548, Hungary 539, Latvia 528, etc.). On that basis France is **21/24 in the EU and 24/28 in the OECD**. The IEA advises caution because those pupils were about 0.5 year older. Both readings are now shown in Sections 0 and 4.4. |
| 16 | Spending per student USD 14,932 PPP vs. OECD 14,436; rank 16/35, 6/8; r = 0.24, R² 0.06 | **Confirmed** | EaG 2026 Table C1.1 (stat.link/ax7gjn), column 1. Also confirmed: government 13,400; secondary 16,745; EU25 14,004; OECD median 14,717. Scatter recomputed: slope +1.19, r 0.24, R² 0.06, France residual -6.4; ≥ USD 10k: r -0.26, residual -13.4. |
| 17 | PLF 2027 staffing: +8,025 ETP (+3,283 excl. reform); operators -1,209; +6,816; -1,076; ceiling 2,032,750 ETPT | **Confirmed** | Bill no. 3210 (AN PDF, registered 1 Oct 2026). Exposé général p. 17-18 (table checked on the rendered page) and Art. 63-64 exposés: +16,162, +3,987, +5,575, +2,929, +3,671, 2,627; operators 397,282, -4,107, -998, -235, -3,248. The bill also states that operators plus social security funds give -2,209 ETP. All ministry rows match. Transports row fixed: no State line, operators -44. |
| 18 | Civil service 3,864,960 (1980) and 4,257,653 (1990); 17.8% and 19.0% | **Confirmed** | Cour des comptes Dec 2009 PDF (vie-publique, behind a JS redirect), Tables 2 and 5. Note: plain text extraction shifts the year labels of Table 2 by one row. The population column (53.7 m 1980, 55.4 m 1986, 56.6 m 1990, 63.6 m 2007) and Table 5 shares confirm the mapping used in the file. Table 5 gives 20.6% in 2007; the report's text says "20,5 %". |

**Links checked:** all the StatLinks, the IEA xlsx files, BAGFW, the AN bill, IFRAP and the Eurostat API return 200. The OECD HTML pages (T1, T7, T10, T12) return 403 to curl but open in a headless browser, with correct titles and dates (GaaG 2025: 19 Jun 2025; PISA 2025 Vol. I: 8 Sep 2026). vie-publique.fr serves the PDF only after a JavaScript redirect.

**Not re-checked here (outside the key-claim list):** TIMSS grade 8 and science rows, the PISA 2022 values, the LFS public-sector perimeter, file 04 cross-references, and the literature cited from memory in Section 6 (already flagged by the author).

Fact-check downloads: `research/data/raw/13_factcheck/`; scripts: `research/scripts/13_factcheck/`.

### Verification log, second pass (2026-10-25): README §7/§8 follow-up

*Scope: (a) align the file with `00-reference-figures.md` and README §8; (b) resolve every item listed for file 13 in README §7. Downloads are under `research/data/raw/13/bagfw/` and `research/data/raw/13/plf/` (untrusted, not executed).*

| # | Item | Outcome | Evidence |
|---|---|---|---|
| A1 | §0 item 1: "EU median 16.2% (2005) / 17.1% (2023), gap 6.5 → 3.8, rank 6th in both years" | **Corrected (internal consistency)** | Those numbers came from the unbalanced yearly samples (n = 22 / 19), which §2.3b says are unsuitable for trends. Replaced with the balanced 17-country sample of §2.3a: median 15.8 → 16.8, gap +6.9 → +4.0, rank 6/17 → 5/17. The aggregate (unweighted median of EU member states with data in both years) is now stated. |
| A2 | France GG employment share 2022 and 2024 shown as 21.0 in §2.3a (panel row) and §2.6 | **Corrected** | Raw values 20.946 and 20.947 round to 20.9, as already corrected in §2.2 by the first pass. |
| A3 | TE per capita PPS (README §8 row 1, file 00 row 5, log #10) | **Aligned** | §3.1 and §7 now give the canonical 23,330 PPS, 8th of 27 (2025) and 22,398, 8th of 27 (2024). Our 23,327 / 22,395 match within rounding. File 01's 22,321 / 9th is labeled superseded. |
| A4 | D.1 in % of GDP (file 00 row 18) | **Confirmed and made explicit** | Eurostat `gov_10a_main` API (updated 21 Oct 2026), PC_GDP, S13, D1PAY: France 12.4% in 2025 vs. EU27 10.3%, EA21 10.0% (EA20 10.0%); rank 6/27 (2024: 12.4%, rank 7/27). Production costs 24.3% vs. EU27 aggregate 21.8% (file 04 K17) labeled likewise. |
| A5 | PISA 2025 (file 00 row 49) | **Consistent, no change** | 457.7 ≈ 458 vs. OECD 463, 29th of 38 matches file 00. This file had no "unverified" flag on it. |
| A6 | PLF 2027 staffing plan; Ifop 86% poll | **No flag to remove** | The PLF 2027 figures were already confirmed in the first pass (#17). The Ifop poll does not appear in this file. |
| B1 | BAGFW publication date "Dec 2023" | **Confirmed** | Full *Gesamtstatistik 2020* report (44 pp.): cover reads "Dezember 2023"; file name `..._2023-12-14_ES.pdf`; the overview PDF was created 14 Dec 2023. The reference date is given as 1 Jan 2020 in the methodology section (31 Dec 2020 in the foreword); the table now says "2020" and notes both. |
| B2 | BAGFW "about 60% part-time" | **Corrected/sharpened** | Full 2020 report: 59% part-time (1,232,979) vs. 41% full-time (843,556), summing to 2,076,535. |
| B3 | BAGFW newer edition | **Added** | *Gesamtstatistik 2024* (imprint June 2026): 2,174,073 employees on 1 Jan 2024, 61.7% part-time; elderly care 576,844, health care 428,501, youth services 558,104 [T13b]. |
| B4 | Jackson, Johnson and Persico (2016), cited from memory | **Confirmed** | *QJE* 131(1): 157-218, doi:10.1093/qje/qjv036 (online 1 Oct 2015, print Feb 2016). Abstract (Crossref): 10% more per-pupil spending over 12 years → +0.31 years of education, about 7% higher wages, -3.2 pts adult poverty. Text now cites these. |
| B5 | Hanushek reviews, cited from memory | **Confirmed (specific reference chosen)** | Hanushek (2003), *Economic Journal* 113(485): F64-F98, doi:10.1111/1468-0297.00099; abstract via NBER WP 9040. |
| B6 | *Café pédagogique* "-1,588 teaching posts" (noted as unverified in §5.2 and §7) | **Confirmed against a primary source** | Ministry PLF 2027 press kit (1 Oct 2026), p. 7: "solde net ... reprise de 1 588 ETP enseignants", -1,250 in public schools. Reconciles exactly with the bill: -1,588 + 1,804 + 3,041 = +3,257 ETP. |
| B7 | iFRAP link [T18] | **Live** | HTTP 200 on 25 Oct 2026. |

**Items still unverified in this file after this pass:** none flagged as unverified. Remaining known gaps (not flags) stay in Section 9: OECD SDMX database values (Cloudflare), the Germany 2022-2023 ILO jump, Destatis hospital staff by ownership, PISA range-of-ranks, PLF 2027 *Bleus* and *Jaune*, and the Insee S.13 1980-1999 series.
