# Revenue Cuts Since 2017 and Structural Drivers of French Public Finances

*Research file 08. Reference base for the public-finance education platform (2027 presidential election). Accessed and compiled 2026-10-25. Written in American English; French institutional terms are kept in italics with a short English gloss.*

---

## 0. How to read this file

- **Scope.** This file covers the topics that sit *around* the spending-versus-revenue debate rather than inside a single spending program:
  1. The revenue cost of tax and contribution cuts since 2017 (the left's main counter-argument: "the deficit is a revenue problem").
  2. Public aid to businesses (*aides publiques aux entreprises*): 82 to 211 bn EUR, depending on definitions.
  3. Local governments (*collectivités territoriales*, *administrations publiques locales*, APUL).
  4. Employment rate, hours worked and productivity.
  5. Demographics and ageing, including long-term care (*dépendance* / *perte d'autonomie*).
  6. Upward pressure on spending: climate investment and defense.
  7. Public investment and public-sector net worth.
- **Units.** Every ratio is labeled as either **% of GDP** or **% of total public expenditure**. Where a source only provides euros, the conversion to % of GDP is mine and is labeled "(my conversion)". For 2025 conversions I use nominal GDP of about **2,990 bn EUR**. Eurostat's October 2026 GDP is **2,991.1 bn EUR** (nama_10_gdp). The canonical 2025 values are expenditure **1,714.1 bn EUR = 57.3% of GDP** and deficit **151.6 bn EUR = 5.1%** (October 2026 vintage); Insee's March 2026 release gave 57.2% and 152.5 bn EUR on an earlier GDP.[^insee-apu2025]
- **Accounting frameworks.** National accounts (ESA 2010, *comptabilité nationale*, published by Insee and Eurostat) differ from budget accounting (*comptabilité budgétaire*: the State budget in the PLF and LFI, or local-government budget accounts published by the DGFiP). The two frameworks give different numbers for the same concept: local-government deficit and debt, the State deficit, and so on. Each section says which framework a figure uses.
- **Raw data.** All series I downloaded are saved under `research/data/` (files prefixed `08_`). Source PDFs are under `research/data/raw/08/`. I computed the cross-country statistics (means, medians, ranks) myself from Eurostat and OECD API extracts. They are stored in `08_computed_international_stats.csv`.
- **Group definitions for my computed statistics.** "EU-27 mean/median" is the unweighted mean or median of the 27 member states. "EU-27 aggregate" is Eurostat's weighted aggregate (EU27_2020). "EA-20" is the 20 euro-area members before Bulgaria's 2026 entry; Eurostat's EA20 aggregate is used where shown. Rank 1 means the highest value. **Canonical euro-area aggregate (file 00):** EA21 (fixed composition incl. Bulgaria). Where this file quotes EA-20, the EA21 value is given alongside for headline gaps (2025: TE 49.7% EA21 vs 49.8% EA20; France's gap +7.6 pp ≈ 227 bn EUR vs EA21, +7.5 pp ≈ 225 bn EUR vs EA20).

---

## 1. Key figures (summary table)

| # | Indicator | Value | Unit | Data year | Source (publication date) |
|---|---|---|---|---|---|
| 1 | Cumulative impact of tax and contribution cuts decided 2018-2023 | **62 bn EUR (2.2 pts)** | bn EUR / % of GDP | 2023 | Cour des comptes, RSPFP (July 2024)[^cdc2024] |
| 2 | Fall in the compulsory-levy ratio 2017→2024 (households −1.6 / firms −0.9 per the key points; −1.7 / −0.8 in OFCE's own Table 3 and body text) | **−2.5 pts** | % of GDP | 2017-2024 | OFCE Policy Brief 146 (July 11, 2025)[^ofce146]. *Concept: Insee PO ratio, pre-May-2026 vintage. On the May 2026 vintage the fall is −2.6 pts (45.3 → 42.7). Not the same as the Eurostat total-revenue fall (−3.1 pp, files 09 and 10) or the Cour's 2.2 pts of discretionary measures (row 1).* |
| 3 | Increase in the public deficit 2017→2024 (3.4%→5.8%) | **+2.4 pts** | % of GDP | 2017-2024 | OFCE PB 146[^ofce146] |
| 4 | New levies decided 2024-2026 (partial reversal of cuts) | **+36.7 bn EUR (+1.2 pts)** | bn EUR / % of GDP | 2024-2026 | Rexecode DT 105 (Sept. 2026)[^rexecode105] |
| 5 | Compulsory-levy ratio (*taux de prélèvements obligatoires*) | **43.6% (2025) vs 42.7% (2024), 45.3% (2017)** | % of GDP | 2017-2025 | Insee, *Insee Première* 2106 (May 29, 2026) and PO series 2381412 (2024 revised from 42.8% in IR 78, Mar. 27, 2026)[^insee-apu2025]; Cour des comptes 2024[^cdc2024] |
| 6 | Revenue cost of replacing ISF with IFI (counterfactual) | **> 4 bn EUR (4.5 bn est.)** | bn EUR | 2022 | France Stratégie capital-tax committee (Oct. 2023)[^fs-isf] |
| 7 | General employer contribution reliefs (*allègements généraux*) | **75 bn EUR (2.7 pts)** | bn EUR / % of GDP | 2023 | Bozio-Wasmer report (Oct. 3, 2024)[^bw2024] |
| 8 | Business aid, Senate commission of inquiry (broad) | **211 bn EUR** (narrow: 108) | bn EUR | 2023 | Sénat, report 808 (July 8, 2025)[^senat-aides] |
| 9 | Business aid, HCSP perimeter 1 (direct, targeted) / perimeter 2 (broad) | **82 / 187 bn EUR** | bn EUR | 2023 | HCSP report to the PM (July 2026)[^hcsp-aides] |
| 10 | Business aid, EU "State aid" definition | **≈ 45 bn EUR** | bn EUR | 2023 | HCSP (July 2026)[^hcsp-aides] |
| 11 | Local governments' share of public expenditure (APUL) | **19.3%** (local authorities alone: 17.8%) | % of total public expenditure | 2024 | HCSP Note 159 (Apr. 2026)[^hcsp159] |
| 12 | Local government (S1313) expenditure | **11.2%** (EU-27 aggregate 11.3%) | % of GDP | 2025 | Eurostat gov_10a_main (my extract, Oct. 21, 2026)[^es-gov] |
| 13 | Local authorities' financial debt (budget accounts, incl. *syndicats*) | **225.4 bn EUR (7.5%)** | bn EUR / % of GDP | 2025 | Cour des comptes, *Finances publiques locales* (July 2026)[^cdc-fpl2026] |
| 14 | Employment rate 15-64 | **69.3%** (DE 77.2, NL 82.3, EU-27 agg. 71.0); rank 21/27 | % of population 15-64 | 2025 | Eurostat lfsi_emp_a (my extract)[^es-emp] |
| 15 | Employment rate 55-64 | **61.7%** (DE 75.3, SE 78.3, EU-27 agg. 66.4) | % of population 55-64 | 2025 | Eurostat lfsi_emp_a[^es-emp] |
| 16 | Hours worked per inhabitant | **666 h/yr**, last of 27 (EU-27 agg. 783; DE 734; NL 821) | hours per inhabitant per year | 2025 | Eurostat nama_10_lp_ulc (my extract)[^es-lp] |
| 17 | Revenue gain if France matched Germany's employment rate (FTE-adjusted scenario) | **≈ +38 bn EUR** of compulsory levies (*prélèvements obligatoires*, all general government; corrected after verification: was "total public revenue"); +1.5 m jobs; GDP +3.2% | bn EUR | 2022 base | DG Trésor note for HCFiPS (Aug. 2024), box 1, p. 9[^hcfips] |
| 18 | Real labor productivity per hour, change 2019→2025 | **FR −0.8%** vs EU-27 +3.4%, DE +2.2% | % change | 2019-2025 | Eurostat nama_10_lp_ulc (my computation)[^es-lp] |
| 19 | Total fertility rate | **1.56** (2025, Insee); 1.61 in 2024 (2nd highest in EU-27) | children per woman | 2025 | Insee Première 2087 (Jan. 2026)[^insee-demo]; Eurostat demo_find[^es-demo] |
| 20 | Natural balance (births − deaths) | **−6,000**, first negative since WWII | persons | 2025 | Insee Première 2087[^insee-demo] |
| 21 | Old-age dependency ratio (65+/15-64), projection | **35.7 (2025) → 45.3 (2040) → 52.3 (2070)** | % | 2025-2070 | Eurostat EUROPOP2023 proj_23ndbi[^es-proj] |
| 22 | Public long-term care (LTC) spending, EC baseline | **1.9% (2022) → 2.6% (2070)** | % of GDP | 2022-2070 | EC/EPC 2024 Ageing Report (Apr. 2024)[^ar2024] |
| 23 | Total age-related spending (pensions, health, LTC, education) | **29.9%**, highest in EU (EU 24.4%) | % of GDP | 2022 | EC 2024 Ageing Report[^ar2024] |
| 24 | Additional climate investment needed by 2030 (all sectors) | **≈ 66 bn EUR/yr (2.3 pts)**, of which public **25-34 bn EUR/yr** | bn EUR / % of GDP | 2030 | Pisani-Ferry & Mahfouz (May 2023)[^pisani] |
| 25 | Defense spending (NATO "core defence" definition) | **2.04% (2025e); 2.22% (2026e)** (2017: 1.78%) (corrected after verification: was 2.05% for 2025e, from the Aug. 2025 release superseded by NATO's July 2026 release) | % of GDP | 2025e-2026e | NATO, *Defence Investment of NATO Countries (2014-2026)* (July 2026)[^nato] |
| 26 | LPM (military programming law) budget credits | **51 → 57 → 63 bn EUR** (2025 exec. → 2026 LFI → 2027 PLF; 2026 revised: 58) | bn EUR | 2025-2027 | PLF 2027 (Oct. 1, 2026)[^plf2027] |
| 27 | Gap to the NATO 3.5% "core defense" target (2035) | **≈ 1.46 pts ≈ 44 bn EUR/yr at 2025 GDP; ≈ 1.28 pts from the 2026e level** (my conversion; corrected after verification: was 1.45 pts ≈ 43 bn) | % of GDP / bn EUR | 2025-2026 base | NATO July 2026[^nato]; NATO Hague summit June 2025 via Sénat[^senat-lpm] |
| 28 | General government GFCF (public investment) | **4.4%** (EU-27 agg. 3.9; EA-20 agg. 3.7; DE 3.5) | % of GDP | 2025 | Eurostat gov_10a_main[^es-gov] |
| 29 | General government **net** investment (GFCF minus depreciation) | **0.6%**, rank 23/27 | % of GDP | 2025 | Eurostat gov_10a_main (my computation)[^es-gov] |
| 30 | General government net worth (*patrimoine net des APU*) | **750 bn EUR** (non-financial assets 2,945; net financial position −2,195) | bn EUR | end-2025 | Insee, patrimoine national (July 30, 2026)[^insee-patrimoine] |
| 31 | Public expenditure / total revenue, France vs euro area | **57.3% / 52.2%** vs EA-20 agg. 49.8% / 46.8% (canonical EA21 expenditure aggregate: 49.7%, gap **+7.6 pp ≈ 227 bn EUR**; file 00 row 7) | % of GDP | 2025 | Eurostat gov_10a_main[^es-gov] |

> **Checks on the user's starting figures.** (a) *Public expenditure 2025 ≈ 1,714 bn EUR = 57.3% of GDP*: **confirmed (canonical value 57.3%).** Insee's March 2026 first estimate gives 1,714.1 bn EUR and 57.2% of GDP.[^insee-apu2025] Eurostat's October 2026 extract, which reflects Insee's May 29, 2026 revised accounts, gives **57.3%**.[^es-gov] *(Verification note: the expenditure level is unchanged at 1,714.1 bn EUR in Eurostat; the 0.1-pt difference comes from a downward GDP revision to 2,991.1 bn EUR (nama_10_gdp). The deficit was revised to 151.6 bn EUR, still 5.1% of GDP.)* (b) *Compulsory levies 2025 = 43.6% of GDP*: **confirmed** (Insee, March and May 2026; 2024 = 42.7% in the May 2026 vintage, 42.8% in March).[^insee-apu2025] (c) *Social protection benefits 2024 = 31.9% of GDP (Drees)*: outside this file's scope and not re-verified here; see the social-protection file.

---

## 2. Scope and definitions

| Term | Definition used here | Why it matters |
|---|---|---|
| *Prélèvements obligatoires* (PO, compulsory levies) | Taxes plus actual social contributions received by general government and EU institutions, net of amounts unlikely to be collected. They exclude imputed social contributions. Insee deducts tax credits from gross tax revenue. | The PO ratio (43.6% of GDP in 2025) is narrower than **total public revenue** (52.2% of GDP in 2025, Eurostat TR). Rexecode notes that international bodies compute the ratio differently: the Commission's DG TAXUD series (43.5% in 2024) excludes imputed contributions but does not deduct tax credits; the Eurostat national-accounts "maximal" definition (45.3% in 2024) is broader still (corrected after verification: was "do not deduct tax credits and do count imputed contributions", which applies only to the maximal variant).[^rexecode105] |
| *Mesures nouvelles* (discretionary measures) | The ex-ante yield or cost of new legislated tax and contribution measures for a given year, as recorded in the RESF annex to the budget. | This is the basis of the Cour des comptes' 62 bn EUR and Rexecode's +36.7 bn EUR. It differs from the change in the PO ratio, which also includes spontaneous elasticity of revenue to GDP. |
| *Élasticité des PO* (revenue elasticity) | Spontaneous growth of levies divided by nominal GDP growth, at constant legislation. | An elasticity above 1 in 2021-2022 masked the cuts; 2023 showed them (Cour des comptes).[^cdc2024] |
| *Aides publiques aux entreprises* (business aid) | No legal or statistical definition exists. Perimeters range from EU "State aid" (≈ 45 bn EUR) to broad "economic support", which includes general contribution reliefs, reduced VAT rates and Bpifrance loans (187-211 bn EUR). | This is the single biggest source of confusion in the debate (Section 4). |
| *APU / APUC / APUL / ASSO* | General government / central government (State + ODAC) / local government (local authorities + ODAL) / social security funds. | Local authorities (*collectivités*) are a subset of APUL. |
| *Dépense publique* | ESA 2010 total general-government expenditure (Eurostat TE). France includes tax credits paid out as spending. | 57.3% of GDP in 2025. |
| *Patrimoine net des APU* | Total assets (non-financial + financial) minus financial liabilities in the national balance sheet. | It excludes implicit pension liabilities and future tax claims. |

---

## 3. Revenue cuts since 2017: the "revenue problem" argument (steelman and quantification)

### 3.1 What was cut (main measures, 2017-2024)

| Measure | Year(s) | Order of magnitude | Source |
|---|---|---|---|
| Abolition of *taxe d'habitation* (TH, residence tax) on primary residences, phased in for 80% then 100% of households | 2018-2023 | OFCE: **−1.0 pt of GDP** of household levies 2017→2024. Fipeco: local revenue loss **23.5 bn EUR** (2020). Senate finance committee: total cost **≈ 18 bn EUR** (10.2 bn for the bottom 80%, 7.8 bn for the top 20%) | OFCE PB 146[^ofce146]; Fipeco (Apr. 25, 2018; a 2018 *projection* for 2020, of which 5 bn EUR was already paid by the State) and Sénat finance committee, *rapport général* 163 (2021-2022), vol. III, annex 27 (Nov. 18, 2021), both re-read 2026-10-25, pass 2[^th-cost] |
| ISF (wealth tax on all assets) replaced by IFI (real-estate-only wealth tax) | 2018 | Initial loss 3.1 bn EUR (2018). ISF yield in 2017 was 4.2 bn EUR. IFI yield rose from 1.29 bn EUR (2018) to 1.83 bn EUR (2022). Counterfactual loss **≈ 4.5 bn EUR in 2022** ("likely above 4 bn"). OFCE: −0.1 pt of GDP | France Stratégie committee (Oct. 2023)[^fs-isf]; OFCE[^ofce146] |
| PFU (flat tax of 30% on capital income) | 2018 | The committee concluded the PFU was **"self-financed in its first years"** because dividends paid to households jumped (≈ 23 bn EUR a year declared in 2018-2020 vs 14 bn EUR in 2013-2017). No detectable effect on investment or wages | France Stratégie committee[^fs-isf] |
| Corporate income tax (*IS*) rate cut from 33.3% to 25% | 2018-2022 | OFCE: **−0.2 pt of GDP** (before credits). Gross static cost **≈ 11 bn EUR** at full effect: "*le coût final de la baisse du taux normal d'IS de 33 1/3 % à 25 %, qui restera de l'ordre de 11 milliards d'euros*" (Assemblée nationale finance committee, *rapporteur général* J. Giraud, report 1838, Apr. 3, 2019, citing the DGFiP) (verified 2026-10-25, pass 2: was "could not re-verify"). This is an ex-ante static estimate; OFCE's 2017 ex-ante range was 7-17 bn EUR depending on base assumptions | OFCE[^ofce146]; AN report 1838[^is-cost] |
| CICE (tax credit) converted into permanent employer-contribution cuts | 2019 | Double cost in 2019 (credit refunds plus new reliefs): Rexecode records −1.2 pt of GDP of measures in 2019. OFCE shows a −1.1 pt drop in employer contributions, offset by +0.6 pt from the disappearance of the tax credit | Rexecode DT 105[^rexecode105]; OFCE[^ofce146] |
| Production taxes: CVAE (value-added business tax) halved, industrial property tax bases halved | 2021 | **≈ 10 bn EUR/yr** (France Relance), of which **7.25 bn EUR** for removing the regions' share of the CVAE (i.e., halving its rate from 1.5% to 0.75%), **1.54 bn EUR** of built-property tax (TFPB) and **1.75 bn EUR** of CFE on industrial establishments (verified 2026-10-25, pass 2, in Banque des Territoires, Oct. 12, 2020; the DGE confirms "more than 10 bn EUR" centered on halving the CVAE) | DGE; Banque des Territoires (Caisse des Dépôts)[^prod-tax] |
| CVAE: further cut, final abolition postponed | 2023 → 2030 | 4.1 bn EUR cut in 2023 (9.3 bn total planned) (DGE, Oct. 3, 2022). Full removal pushed back to 2027 (LFI 2024), then to **2030** by art. 62 of the LFI 2025 (law 2025-127 of Feb. 14, 2025): top rate frozen at 0.28% in 2026-2027, then 0.09% in 2029 (CGI art. 1586 *quater*, consolidated version on Légifrance, 2026 and 2029 versions read 2026-10-25). The LFI 2026 did **not** bring the end forward to 2028 (the Assembly's amendment was dropped; the article is not modified by it on Légifrance) (verified 2026-10-25, pass 2) | DGE; Légifrance[^prod-tax] |
| *Contribution à l'audiovisuel public* (TV license fee) abolished | 2022 | OFCE: −0.1 pt of GDP | OFCE[^ofce146] |
| Income-tax cuts (first bracket lowered, tax-free overtime) | 2019-2020 | OFCE: −0.3 pt of GDP (income tax and credits) | OFCE[^ofce146] |
| Offsets: CSG (broad-based social contribution) increase | 2018 | +0.9 pt of GDP (offsetting a −0.6 pt cut in employee contributions) | OFCE[^ofce146] |

### 3.2 The aggregate estimates

| Estimate | Value | Scope and method | Source |
|---|---|---|---|
| Cour des comptes | **62 bn EUR in 2023 = 2.2 pts of GDP** ("more than 60 bn EUR"), "not offset by spending savings" | Cumulative ex-ante cost of tax and contribution cuts decided 2018-2023. The PO ratio stayed near its 2017 level until 2022 (45.0% vs 45.3%) only because elasticity exceeded 1 in 2021-2022. The −1.8 pt drop in 2023 was −1.6 pt spontaneous and −0.2 pt new measures | Cour des comptes, RSPFP July 2024, pp. 35-36[^cdc2024] |
| OFCE | **−2.5 pts of GDP** in the PO ratio 2017→2024 (households −1.6, firms −0.9 in the key points; Table 3 gives −1.7 / −0.8, an internal inconsistency in the brief). Deficit **+2.4 pts**. Primary spending excluding investment **−0.8 pt** of potential GDP, **but only −0.2 pt once the subsidy line is corrected** (the CICE's conversion into contribution cuts removed ≈ 0.6 pt of recorded subsidies; added after verification). Total spending stable | Accounting decomposition of the change in ratios. It does **not** separate discretionary measures from base effects (stated in the authors' footnote 9) | OFCE Policy Brief 146, July 11, 2025[^ofce146] |
| Rexecode (business-oriented think tank) | Measures 2018-2023: −0.4, −1.2, +0.2, −0.6, −0.3, −0.3 pt (**sum ≈ −2.6 pts**). Reversed 2024-2026: **+1.2 pts (+36.7 bn EUR)**. Relative to 2014: 1.2 of 2.7 pts of cuts erased. **Relative to 2010, net measures are still +2 pts (+65 bn EUR)** | RESF *mesures nouvelles*, cumulated by year | Rexecode DT 105, Sept. 2026[^rexecode105] |
| IPP (household side only) | Household levies cut by **24.4 bn EUR** over the 2017-2022 term. Average household gain +1.9% of living standard; bottom 5% +0.8%; top 1% +3.3%; unemployed −1.1% | Microsimulation of measures *decided* in the term | IPP Note 81, March 2022[^ipp81] |

**My reconciliation (illustrative, labeled as my computation).**
- *Gross* cuts 2018-2023: **2.2-2.6 pts of GDP**, or **≈ 66-78 bn EUR at 2025 GDP**.
- *Partial reversal* 2024-2026: **+1.2 pts** (36.7 bn EUR).
- *Net* discretionary cuts still in place in 2026 relative to 2017: **≈ 1.0-1.4 pts of GDP ≈ 30-42 bn EUR.**

The order of magnitude to teach is "about 60-75 bn EUR of cuts at the peak, of which roughly half has since been taken back". It is not "70 bn EUR a year still missing".

### 3.3 Steelman: "the deficit is a revenue problem"

The strongest version, mainly from OFCE[^ofce146] and supported by figures from the Cour des comptes[^cdc2024]:
1. **Timing.** Between 2017 and 2024 the deficit rose by 2.4 pts of GDP while the PO ratio fell by 2.5 pts (OFCE, pre-May-2026 vintage; **−2.6 pts, 45.3 → 42.7, on Insee's May 2026 vintage**, the canonical value in file 00 row 27) and total spending was stable as a share of GDP. In pure accounting terms, the deterioration is on the revenue side. *(Nuance added after verification: OFCE's own decomposition attributes 2.1 pts to the structural primary balance, 0.6 pt to exceptional measures such as the energy price shield, and 0.3 pt to interest, offset by 0.6 pt of cyclical and NGEU effects. "The whole deterioration" overstates the claim.)*
2. **Primary spending fell.** Primary spending excluding investment fell by 0.8 pt of potential GDP (wage bill −0.4, intermediate consumption +0.3, subsidies −0.6, cash benefits −0.1, transfers in kind +0.1). Investment rose by 0.5 pt. Interest rose by 0.3 pt. *(Caveat added after verification: OFCE itself notes the fall is only −0.2 pt "if one corrects for public subsidies", because most of the −0.6 pt subsidy drop is the accounting disappearance of the CICE tax credit, which mirrors part of the PO fall.)*
3. **Unfunded cuts.** The Cour des comptes itself writes that the cuts were "*non compensées par des économies en dépenses*" and "*ont creusé le déficit de l'État et accru sa dette*". The State bore the cost through VAT transfers to local governments and social security.[^cdc2024]
4. **Weak evidence of supply-side returns for capital-tax cuts.** The France Stratégie committee found **no detectable effect of the PFU on investment or wages**. The ISF→IFI cost exceeded 4 bn EUR by 2022. Dividends rose, which partly financed the PFU; reading this as a tax-timing effect rather than new growth is my interpretation, not the committee's wording. *Fairness note added after verification:* the committee itself warns that identifying PFU-exposed firms is imprecise, which "weakens the robustness" of the no-effect finding, and that investment effects may take time to materialize.[^fs-isf]
5. **Distribution.** The IPP found the 2017-2022 measures gave the top 1% roughly four times the relative gain of the bottom 5% (+3.3% vs +0.8%).[^ipp81]
6. **Scale.** Reversing the gross cuts (≈ 2.2-2.5 pts) would cover most of the ≈ 3 pts of GDP (≈ 89.6 bn EUR) of adjustment that the Cour des comptes says is needed to stabilize the debt ratio. *Verified in the primary June 2026 RSPFP: "Un effort supplémentaire de réduction du déficit de 89,6 Md€, soit 3,0 points de PIB" (deficit that would have stabilized the ratio: 62.9 bn EUR).*[^cdc2026-rspfp]

### 3.4 Counter-arguments (the platform's thesis)

1. **Choice of baseline.** Rexecode shows that against **2010** rather than 2017, net tax measures are still **+2 pts of GDP** (+65 bn EUR a year). The 2018-2023 cuts only partly reversed the **2011-2013 "fiscal shock" of +3.5 pts**. "Spending stable as a % of GDP since 2017" assumes spending should grow with GDP indefinitely, at a level already **7.6 pp of GDP above the EA21 aggregate in 2025** (57.3% vs 49.7%; 7.5 pp vs EA20) (corrected 2026-10-25, pass 2: was "7.5 pts above the euro-area aggregate", aggregate and year unstated).[^rexecode105][^es-gov]
2. **Revenue is already the 2nd highest in the EU.** Total revenue is 52.2% of GDP in 2025, ranked 2nd of 26 reporting EU states. That is 5.4 pts above the EA-20 aggregate (≈ 160 bn EUR; my conversion). The Cour des comptes (Feb. 2026) states the PO ratio "*est déjà le plus élevé de la zone euro*".[^es-gov][^cdc-feb2026]
3. **Tax hikes since 2024 did not reduce the deficit.** Rexecode: +36.7 bn EUR of new levies 2024-2026 went with a deficit stuck around 5.4% of GDP (2023 vs 2026 forecast). About half was absorbed by higher interest (1.9 → 2.5 pts of GDP).[^rexecode105] *Caveat:* Insee's 2025 out-turn shows the deficit falling to 5.1%,[^insee-apu2025] and the Cour (June 2026, primary text) attributes that fall "*exclusivement*" to 23 bn EUR of tax increases, one third of them labeled temporary, while primary spending grew faster than GDP (corrected after verification: was "mainly").[^cdc2026-rspfp]
4. **Contribution reliefs are not "gifts" in a high-labor-cost system.** Bozio and Wasmer estimate that abolishing the general reliefs (75 bn EUR) would destroy about **980,000 FTE jobs**. Net revenue would be ≈ **48 bn EUR**, not the 67 bn EUR static gain, before unemployment-benefit costs.[^bw2024]
5. **The spending gap dwarfs the cuts.** Spending is 57.3% of GDP vs 49.7% for the EA-21 aggregate, a gap of 7.6 pts (≈ 227 bn EUR; my conversion). Against EA-20 (49.8%) the gap is 7.5 pts, ≈ 225 bn EUR. The net 2017-2026 cuts are about 1.0-1.4 pts.[^es-gov]

**Where economists genuinely disagree:** the *counterfactual* path of spending; how much of the 2023 revenue shortfall is structural; whether a ratio of 2017 or 2010 or a euro-area benchmark is the right norm; the long-run supply effects of CIT and production-tax cuts. Evidence on the latter is still thin; see the CICE evaluation in 4.3.

---

## 4. Public aid to businesses

### 4.1 Competing estimates

| Estimate | Year of data | Amount | What is included | Source |
|---|---|---|---|---|
| Senate commission of inquiry (broad), report 808 | 2023 | **211 bn EUR ("at least")** | Tax expenditures incl. *déclassées* and VAT-related (88 bn); social-contribution reliefs (75); Bpifrance loans and guarantees at face value (41); State subsidies (7). Excludes municipal, regional (≈ 2 bn) and EU aid. *Composition (7 + 41 + 88 + 75 = 211) verified via HCSP 2026, Annex 4* | Sénat, report deposited July 1, 2025, presented July 8, 2025[^senat-aides] |
| Senate (narrow, EU State-aid logic) | 2023 | **108 bn EUR** | Excludes Bpifrance (41) and 62 bn EUR of reclassified and VAT tax expenditures | Sénat, July 2025, via HCSP table[^hcsp-aides] |
| HCSP note 157 (Harfi, July 2025) | 2023 | **112 bn EUR** (excluding general contribution reliefs) | Budget aid, tax aid, targeted contribution exemptions | HCSP 2025 via Public Sénat[^publicsenat] |
| **HCSP report to the PM (Beaune / Harfi), perimeter 1** | 2023 | **82 bn EUR** | Direct, targeted aid: targeted budget spending, classified tax expenditures, 28 targeted contribution exemptions, loans and guarantees in subsidy-equivalent, local direct aid | HCSP, July 2026[^hcsp-aides] |
| **HCSP perimeter 2** | 2023 | **187 bn EUR** | Perimeter 1 + **general contribution reliefs**, sector-identifiable reduced VAT rates, indirect local interventions | HCSP, July 2026[^hcsp-aides] |
| EU State-aid aggregate | 2023 | **≈ 45 bn EUR** | EU-law definition; used for comparisons across member states | HCSP, July 2026[^hcsp-aides] |
| Clersé (Univ. Lille) for IRES/CGT | 2019 | **157 bn EUR** (205 bn incl. reclassified tax expenditures) | Broad. Commissioned by a trade-union research institute; note the orientation | Clersé 2022, via HCSP and Sénat[^hcsp-aides][^senat-aides] |
| France Stratégie | 2019 | **139-223 bn EUR** (by perimeter) | Range by scope | France Stratégie 2020, via Sénat[^senat-aides] |
| Minister É. Lombard (2025) | ≈ 2024 | ≈ 150 bn EUR (40 tax + 30 budget + 80 contribution reliefs) | Political statement | Public Sénat[^publicsenat] |

**Teaching point.** Whether the number is 45, 82, 108, 187 or 211 bn EUR depends almost entirely on two classification choices: (1) whether the **general reduction of employer contributions** (≈ 75-80 bn EUR) counts as "aid", and (2) whether **Bpifrance loans and guarantees** count at face value or in subsidy-equivalent. The Senate commission chair, O. Rietmann (LR), argues that general reliefs are compensation for high French labor costs, not aid. The rapporteur, F. Gay (PCF), defends the 211 bn EUR figure. The HCSP stresses that its work "does not aim to redo a costing" but to set stable definitions.[^publicsenat][^hcsp-aides]

### 4.2 Interpretation for the platform

- Business aid is **not** "spending that can simply be cut". About 75 bn EUR (2023; 2.7 pts of GDP) is the general contribution relief targeted at low wages. It exists because of the high social-contribution wedge on labor.[^bw2024]
- Removing it would raise labor costs at the minimum wage. The Bozio-Wasmer estimate is −980,000 FTE jobs for full abolition, with net yield ≈ 48 bn EUR (72% of the 67 bn EUR static gain they use, or 64% of the 75 bn EUR cost; corrected after verification: was "64% of gross").[^bw2024]
- The HCSP (2026) and Senate (2025) agree on one point: France **lacks systematic evaluation** of the 2,200+ schemes.[^senat-aides][^hcsp-aides]

### 4.3 Effectiveness evidence (contested)

| Scheme | Finding | Source |
|---|---|---|
| CICE (2013-2018) | ≈ 100,000 jobs (micro-econometric, 2013-2016) to ≈ 160,000 (macro, after financing, 2013-2017), for a cost "*de l'ordre de 18 milliards d'euros en 2016*" (≈ 68 bn EUR cumulated 2014-2018). Banque de France: **≈ 240,000 market-sector jobs created between end-2015 and end-2019** (260,000 from end-2012 to end-2019) for CICE + Responsibility Pact, assuming full financing (verified 2026-10-25, pass 2; corrected: was "≈ 240,000 jobs over 2013-2019") | France Stratégie, Sept. 2020; Banque de France *Bulletin* 231-6 (Sept.-Oct. 2020)[^cice] |
| PFU (2018) | No effect detected on investment or wages | France Stratégie, Oct. 2023[^fs-isf] |
| General contribution reliefs | Strong employment effects near the minimum wage; weak or none above ≈ 2.5 SMIC. They contribute to low-wage traps: at 1.15 SMIC, raising a worker's disposable income by 100 EUR costs the employer 483-518 EUR, depending on method | Bozio-Wasmer 2024[^bw2024]; Rexecode 2026[^rexecode105] |

---

## 5. Local governments (*collectivités territoriales*, APUL)

### 5.1 Key figures

| Indicator | Value | Unit | Year | Framework | Source |
|---|---|---|---|---|---|
| APUL expenditure | **322 bn EUR**, **11 pts of GDP**, **19.3% of total public expenditure** (local authorities alone 10.2 pts, 17.8%) | bn EUR / % of GDP / % of total public expenditure | 2024 | National accounts | HCSP Note 159[^hcsp159] |
| Change in APUL spending since 1995 | **+1.5 pts of GDP** (EU average +0.4); ASSO +2.9 pts | % of GDP | 1995-2024 | National accounts (consolidated) | HCSP Note 159[^hcsp159] |
| Local consolidated spending, EU average | 15.6 pts of GDP vs 11 in France (France is less decentralized) | % of GDP | 2024 | Eurostat | HCSP Note 159[^hcsp159] **⚠ divergence flagged after verification:** Eurostat's S1313 (local government only) gives an EU-27 aggregate of 11.3% and unweighted mean of 10.5% in 2025, essentially France's level (11.2%; see 5.2). HCSP's 15.6 most likely also counts the state/regional tier (S1312) of federal countries; its annex methodology was not checked. Do not quote 15.6 without this scope note. |
| Local authorities' balance | **−9.3 bn EUR** (improved by 2.7 bn) | bn EUR | 2025 | National accounts | Cour des comptes, July 2026[^cdc-fpl2026] |
| Same, budget accounts | **−11.3 bn EUR** (2024: −11.8 bn) (note: the Cour's chapter I conclusion gives −11.6 bn EUR for the same aggregate, an internal inconsistency in the report) | bn EUR | 2025 | Budget accounts (DGFiP) | Cour des comptes, July 2026[^cdc-fpl2026] |
| Operating expenses growth | +3.2 bn EUR (+1.4%) in 2025, after **+30.4 bn EUR cumulated over the three years 2022-2024** (corrected after verification: was "2021-2024"; the Cour's chapter text says "*au cours des trois années 2022 à 2024*") | bn EUR | 2025 | Budget accounts | Cour des comptes, July 2026[^cdc-fpl2026] |
| Real investment spending | **79.1 bn EUR** (excl. *syndicats*), +2.2% | bn EUR | 2025 | Budget accounts | Cour des comptes, July 2026[^cdc-fpl2026] |
| Gross savings (*épargne brute*) | **40.2 bn EUR** (+7.2%) | bn EUR | 2025 | Budget accounts | Cour des comptes, July 2026[^cdc-fpl2026] |
| Financial debt (incl. intercommunalities and *syndicats*) | **225.4 bn EUR** (+10.0 bn), **7.5% of GDP**; flat in constant euros vs 2019 | bn EUR / % of GDP | end-2025 | Budget accounts | Cour des comptes, July 2026[^cdc-fpl2026] |
| APUL Maastricht debt (S1313) | **9.3% of GDP**, rank 3/27 (EU-27 agg. 5.2%) | % of GDP | 2025 | ESA/EDP | Eurostat gov_10dd_edpt1[^es-gov] |
| VAT allocated to local authorities | **52.7 bn EUR**, one quarter of net VAT; their 1st tax resource since 2023 | bn EUR | 2025 | Budget accounts | Cour des comptes, July 2026[^cdc-fpl2026] |
| *Dotation globale de fonctionnement* (DGF, main State operating grant) | **27.4 bn EUR** (+150 m EUR, fully offset by lower investment grants) | bn EUR | 2025 | Budget | Cour des comptes, July 2026[^cdc-fpl2026] |
| Share of State transfers in local revenue | **53.6%** | % of local revenue | 2024 | — | HCSP Note 159, citing Cour des comptes[^hcsp159] |
| Net contribution of local authorities to deficit reduction | **4.3 bn EUR** (commitments; 1.7 bn in cash) in 2025; **3.5 bn** (2.4 bn cash) in 2026 | bn EUR | 2025-2026 | Budget | Cour des comptes, July 2026[^cdc-fpl2026] |
| PLF 2027 target | Local operating spending to grow "at inflation" | — | 2027 | — | PLF 2027[^plf2027] |
| Territorial civil service (FPT) headcount | **2.04 million** (2,039,400 incl. subsidized contracts; 2,018,300 excl.) (+0.3%, +6,400) end-2024; growth driven by contract staff (+2.6%, +13,500), while *fonctionnaires* (tenured civil servants) fell by 4,200 (corrected 2026-10-25, pass 2: was 2.06 million, via Maire-info; Insee's figure 1 gives 2,039.4 thousand) | persons | 2024 | Insee/DGAFP (SIASP) | Insee Première 2094 (Feb. 10, 2026), figure 1 and text[^insee-fp] |
| FPT growth 2011-2021 | **+100,000 agents (+5.5%)**, with no new transfers of competences; Cour suggested ≈ −100,000 posts by 2030 (≈ 4.1 bn EUR/yr savings). Scope: 1.94 m agents in local authorities (end-2021, DGAFP; the end-2024 FPT total is 2.04 m, corrected 2026-10-25 from 2.06 m) | persons | 2011-2021 | — | Cour des comptes, *Les finances publiques locales 2024 - fascicule 2*, Oct. 2, 2024, ch. on staff (PDF pp. 63 and 76): 1.94 m agents at end-2021 (DGAFP); "*un peu plus de 100 000 agents (soit + 5,5 %)*" over 2011-2021; returning to the end-2011 level (1.76 m) by 2030 would save **4.1 bn EUR a year from 2030** (2023 euros) (verified in the primary report 2026-10-25, pass 2)[^cdc-fpt] |
| FPT growth 1998-2008 excl. transfers | ≈ +350,000 agents | persons | 1998-2008 | — | Cour des comptes, July 2012 (via Banque des Territoires)[^cdc-fpt2012] |
| CNRACL (local civil-servant pension fund) contribution increase | +12 pts over 2025-2028, cumulated cost 4.3 bn EUR | — | 2025-2028 | — | HCSP Note 159[^hcsp159] |

### 5.2 International comparison (Eurostat S1313, my computation)[^es-gov]

| Indicator (2025) | France | EU-27 agg. | EU-27 mean / median | France rank EU-27 | EA-20 mean / median | DE | IT | ES | NL | BE | SE | DK |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Local gov. expenditure, % of GDP | 11.2 | 11.3 | 10.5 / 9.4 | 10/27 | 8.9 / 9.2 | 9.5* | 14.6 | 6.1* | 13.3 | 7.2* | 24.5 | 30.7 |
| Local gov. GFCF, % of GDP | 2.4 | 1.6 | 1.6 / 1.5 | 5/27 | 1.4 / 1.3 | 1.1* | 2.2 | 0.7* | 1.7 | 0.8* | 2.7 | 1.4 |
| Local gov. debt (EDP), % of GDP | 9.3 | 5.2 | 3.9 / 2.4 | 3/27 | 3.7 / 3.1 | 5.0* | 4.7 | 1.2* | 4.6 | 4.3* | 14.8 | 9.3 |
| Local gov. GFCF, % of GDP, 2005 | 2.3 | 1.5 | 1.4 / 1.4 | 2/27 | — | 0.8* | 2.1 | 1.1* | 2.1 | 0.8* | 1.6 | 1.4 |

\* Federal or quasi-federal countries (DE, ES, BE, and AT) record their regional tier in S1312 (state government), not S1313. Their S1313 figures understate sub-national spending. Comparisons with France are meaningful mainly for unitary states (IT, NL, SE, DK).

### 5.3 Local-tax reform and the "VAT-ization" of local finance

- The abolition of the *taxe d'habitation* was compensated by two transfers: the departments' share of the built-property tax (TFPB) went to municipalities, and **fractions of national VAT** went to departments and intercommunalities. The 2021 production-tax cut and the CVAE abolition were also compensated by VAT fractions.[^th-cost]
- The Cour des comptes (July 2024) noted that compensation rules gave local authorities "*l'intégralité de l'augmentation des recettes de TVA*" while the State bore the cost. Local and social-security revenues grew by +21% and +24% from 2017 to 2023, versus +4% for the State.[^cdc2024]
- Consequence: local authorities' tax autonomy fell sharply (State transfers are 53.6% of revenue in 2024).[^hcsp159] The Cour recommends a **single expenditure norm covering all State transfers, including VAT** (today's norm covers only one third). It also recommends ending the DILICO (a temporary reserve levy on local tax revenue) and strengthening equalization (*péréquation*).[^cdc-fpl2026]

### 5.4 Disagreements

- **Local elected officials' associations** (AMF, ADCF) argue that local governments must balance their operating budgets by law (the "golden rule") and borrow only for investment. They also argue that local debt is small (7.5% of GDP) and that they carry ≈ 70% of civil public investment, so cutting them hurts investment. The Cour broadly agrees that their finances are "*solides*" on average.[^cdc-fpl2026]
- **Counter-argument:** local authorities ran a deficit of 9-12 bn EUR in 2024-2025 and operating costs rose 30.4 bn EUR over the three years 2022-2024 (corrected 2026-10-25, pass 2: was "30 bn EUR in 2021-2024", inconsistent with the corrected row in 5.1). Staff grew by 100,000 over 2011-2021 with no new competences. Their spending share is ≈ 18-19% of public spending, so the Cour finds a contribution justified.[^cdc-fpl2026][^cdc-fpt]

---

## 6. Employment, hours worked and productivity

### 6.1 Employment rates: international comparison (Eurostat lfsi_emp_a, my computation)[^es-emp]

| Indicator | Year | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | EA-20 agg. | EA-20 mean / median | FR rank EA-20 | DE | IT | ES | NL | BE | SE | DK |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Employment rate 15-64 (% of pop.) | 2009 | 64.4 | 62.8 | 63.4 / 63.0 | 11/27 | 64.0 | 63.8 / 63.3 | 8/20 | 69.4 | 56.9 | 60.0 | 76.2 | 61.6 | 71.9 | 73.5 |
| | 2015 | 64.6 | 64.1 | 65.0 / 64.7 | 16/27 | 64.3 | 64.6 / 64.7 | 12/20 | 73.1 | 56.0 | 57.8 | 75.6 | 61.8 | 75.2 | 72.0 |
| | 2025 | **69.3** | 71.0 | 72.5 / 72.9 | **21/27** | 70.7 | 72.3 / 72.6 | **15/20** | 77.2 | 62.5 | 67.0 | 82.3 | 67.4 | 76.4 | 76.9 |
| Employment rate 55-64 | 2009 | 40.2 | 43.2 | 44.6 / 43.0 | 17/27 | 44.6 | 44.7 / 42.7 | 13/20 | 55.3 | 35.3 | 44.0 | 51.6 | 35.3 | 69.1 | 54.7 |
| | 2025 | **61.7** | 66.4 | 66.8 / 69.4 | **17/27** | 66.5 | 65.6 / 64.5 | 12/20 | 75.3 | 61.2 | 62.4 | 75.8 | 61.5 | 78.3 | 74.7 |
| Employment rate 20-64 | 2009 | 69.8 | 67.3 | 68.3 / 68.2 | 12/27 | 68.3 | — | 9/20 | 73.2 | 61.1 | 64.0 | 77.6 | 67.1 | 77.9 | 76.1 |
| | 2025 | **75.4** | 76.1 | 77.7 / 78.3 | **20/27** | 75.6 | 77.3 / 78.2 | 14/20 | 81.1 | 67.6 | 72.4 | 83.4 | 72.8 | 81.8 | 79.8 |

- **OECD (38 members, my computation from the OECD SDMX API):** France's 15-64 employment rate in 2024 was 68.8% vs an OECD unweighted mean of 72.1% and median of 73.0%; France ranked **29/38**. The OECD aggregate was 70.2%. In 2025 France ranked 27/37 (US not yet reported).[^oecd-emp] **Do not mix the two series:** the platform's canonical figure is the Eurostat LFS rate (69.3% in 2025, 21st of 27); the OECD figure (68.8% in 2024, 29th of 38) is only for OECD-wide rankings.
- **Gap evolution:** in 2009 France was *above* the EU-27 aggregate (64.4 vs 62.8). By 2025 it was 1.7 pts *below* (69.3 vs 71.0). France improved by +4.9 pts while the EU aggregate rose by +8.2 pts. The gap with Germany is 7.9 pts (5.0 pts in 2009). The senior (55-64) rate rose strongly, +21.5 pts since 2009 after the 2010, 2014 and 2023 pension reforms, but remains 13.6 pts below Germany.

### 6.2 Hours worked (Eurostat nama_10_lp_ulc, HW_HAB)[^es-lp]

| Hours worked per inhabitant per year | 2005 | 2015 | 2025 |
|---|---|---|---|
| France | 638 | 625 | **666** |
| EU-27 aggregate | 742 | 731 | 783 |
| EU-27 mean / median | 799 / 781 | 785 / 772 | 852 / 844 |
| France rank (EU-27) | 27/27 | 27/27 | **27/27** |
| EA-20 aggregate | 730 | 707 | 759 |
| DE / IT / ES / NL / BE / SE / DK (2025) | — | — | 734 / 781 / 751 / 821 / 684 / 799 / 735 |

France works the fewest hours per inhabitant in the EU: **−15% vs the EU-27 aggregate and −9% vs Germany** in 2025 (my computation). The reasons are low youth and senior employment and an early effective retirement age, *not* short hours per worker. Hours per employed person in France (**1,499.9 h in 2025**) exceed Germany's (1,336.4 h) and the Netherlands' (1,433.8 h), where part-time work is widespread, but are **below the EU-27 aggregate (1,604.8 h)** (Eurostat nama_10_lp_ulc, indicator HW_EMP, updated Oct. 22, 2026; verified 2026-10-25, pass 2, replacing my earlier computation from nama_10_a10_e).[^es-lp]

### 6.3 What higher employment would bring to public finances

| Estimate | Scenario | Effect | Source |
|---|---|---|---|
| DG Trésor (for HCFiPS, the high council on social-protection financing) | Align France's employment rate on Germany's by age and sex, **in full-time equivalent** (realistic scenario) | **+1.5 m jobs**; GDP **+3.2%**; social-protection revenue +15 bn EUR, spending −5 bn EUR → balance **+≈ 20 bn EUR**; compulsory levies of all general government **≈ +38 bn EUR** (mechanical, assuming a PO elasticity of 1 to GDP on the 2022 base of 1,194 bn EUR). Part of the saving is later eaten by higher pension spending | DG Trésor note for HCFiPS (Aug. 2024), pp. 1 and 9 (box 1)[^hcfips] |
| DG Trésor, headcount scenario | Align headcount rates (ignores German part-time) | +3.6 m jobs; GDP +7.0%; PO up to **≈ 84 bn EUR** (range 38-84 bn by scenario) | Same, box 1, p. 9 (corrected after verification: the range **is** in the primary note; it was previously labeled "via search summary")[^hcfips] |
| My illustration (2025 data) | 7.9-pt gap with Germany × ≈ 41 m people aged 15-64 | ≈ **+3.2 m employed** (headcount). With the EU-27 aggregate instead (1.7-pt gap): ≈ +0.7 m | My computation; population ≈ 40.8 m in 2022 per DG Trésor[^hcfips] |

**Caveats (DG Trésor):** the exercise is "purely illustrative". New entrants would have lower productivity, which the note discounts by 36-45%. It does not cost the policies needed, such as SMIC moderation or tighter unemployment-insurance rules. For scale, France spent 178.7 bn EUR on labor-market policies in 2022 (Dares).[^hcfips]

### 6.4 Productivity

| Indicator | France | Comparison | Source |
|---|---|---|---|
| Nominal labor productivity per hour (PPS, EU-27 = 100), 2025 | **114.6** (2005: 131.7; 2015: 124.3) | DE 124.1, NL 125.9, BE 130.4, DK 137.6, IT 96.2, ES 95.3; France rank 8/27 (4/27 in 2005) | Eurostat nama_10_lp_ulc[^es-lp] |
| Real productivity per hour, 2005→2025 | **+9.0%** | EU-27 +18.2% (catch-up of Central and Eastern Europe), EA-20 +14.1%, DE +15.3%, NL +9.6%, ES +17.4%, IT +1.0%, SE +16.5%, DK +23.1% | Eurostat (my computation, index 2020=100)[^es-lp] |
| Real productivity per hour, 2019→2025 | **−0.8%** | EU-27 +3.4%, EA-20 +1.9%, DE +2.2%, ES +2.0%, NL +2.7%, IT −0.6% | Eurostat (my computation)[^es-lp] |
| Productivity per head vs 2019 (CNP, 2026) | Only **0.7 pt below 2019**, but **≈ 4 pts below the 2010s trend**. Hourly productivity is **≈ 5 pts below its pre-crisis trend** in 2025 (Insee) | Market-sector employees: back to pre-crisis level end-2023, +2.6% above it in Q1 2026 | Conseil national de productivité, 6th report (July 1, 2026)[^cnp2026] |

**Explanations (CNP 2026):** employment-rich growth after 2019, driven by **apprenticeships**, micro-entrepreneurs and job retention after Covid. Composition effects explain part of the gap, not all of it. Large statistical revisions in the 2025 national accounts (2023 productivity per head revised from −3.5% to −2.5% vs 2019) changed the diagnosis.[^cnp2026]

**Steelman for France:** high hourly productivity is partly a **selection effect**: low-skilled people are more often out of work. Raising employment would mechanically lower average productivity (the DG Trésor discount above). France's problem is the *quantity* of labor more than its quality.

---

## 7. Demographics and ageing

### 7.1 Key demographic facts

| Indicator | Value | Year | Source |
|---|---|---|---|
| Births | **645,000** (−2.1% on 2024; −24% vs 2010) | 2025 | Insee Première 2087 (Jan. 2026)[^insee-demo] |
| Deaths | **651,000** (+1.5%) | 2025 | Insee[^insee-demo] |
| Natural balance | **−6,000**, first negative since WWII | 2025 | Insee[^insee-demo] |
| Total fertility rate (France) | **1.56** (metropolitan France 1.53), the lowest since 1918; 1.61 in 2024 | 2025 | Insee[^insee-demo] |
| Population on Jan. 1, 2026 | **69.1 million** (+0.25%) | 2026 | Insee[^insee-demo] |
| Life expectancy at birth | Women 85.9, men 80.3 | 2025 | Insee[^insee-demo] |

**International comparison: fertility (Eurostat demo_find, my computation).**[^es-demo]

| TFR | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | EA-20 mean / median | DE | IT | ES | NL | BE | SE | DK |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 2005 | 1.94 | 1.47 | 1.49 / 1.40 | 1/27 | 1.50 / 1.41 | 1.34 | 1.33 | 1.33 | 1.71 | 1.76 | 1.77 | 1.80 |
| 2015 | 1.96 | 1.54 | 1.55 / 1.57 | 1/27 | 1.53 / 1.50 | 1.50 | 1.36 | 1.33 | 1.66 | 1.70 | 1.85 | 1.71 |
| 2024 | 1.61 | 1.34 | 1.35 / 1.38 | 2/27 | 1.32 / 1.33 | 1.36 | 1.18 | 1.10 | 1.43 | 1.44 | 1.43 | 1.47 |

France's fertility advantage remains (≈ +0.27 over the EU aggregate in 2024), but it has narrowed from +0.47 in 2005.

### 7.2 Old-age dependency ratio (65+ / 15-64, %)

| | 2005 | 2025 | 2030 (proj.) | 2040 | 2050 | 2070 | 2100 |
|---|---|---|---|---|---|---|---|
| France | 25.1 | 35.5 | 39.0 | 45.3 | 48.0 | 52.3 | 59.2 |
| EU-27 | 24.7 | 34.5 | 38.0 | 45.4 | 50.4 | 54.1 | 59.7 |
| Germany | 27.8 | 35.9 | 40.3 | 45.2 | 45.7 | 50.2 | 56.9 |
| Italy | 29.4 | 39.0 | 43.7 | 56.2 | 61.3 | 60.7 | 65.7 |
| Spain | 24.0 | 31.2 | 36.2 | 48.4 | 59.0 | 59.5 | 64.3 |
| Netherlands | 20.8 | 32.4 | 36.5 | 42.5 | 42.3 | 51.3 | 58.4 |
| Sweden | 26.5 | 33.4 | 34.2 | 36.9 | 38.5 | 45.7 | 54.8 |

Source: Eurostat demo_pjanind (observed) and proj_23ndbi (EUROPOP2023 baseline). Projected 2025 values (35.7 for France) differ slightly from observed values (35.5).[^es-proj] France's 2025 rank is 8/27; the EU-27 unweighted mean is 32.8. **France ages earlier than the EU average up to ≈ 2035 (baby-boom cohorts) but less afterwards**, thanks to higher past fertility. Note that EUROPOP2023 assumed fertility above the 1.56 actually observed in 2025, so the projection may understate future ageing (my caveat).

### 7.3 Age-related spending projections (EC/EPC 2024 Ageing Report, baseline)[^ar2024]

| % of GDP | Pensions 2022 | Δ 2022-70 | Health 2022 | Δ | **Long-term care 2022** | **Δ 2022-45** | **Δ 2022-70** | Education 2022 | Total 2022 | Δ 2022-70 |
|---|---|---|---|---|---|---|---|---|---|---|
| **France** | 14.4 | −0.9 | 8.8 | +0.3 | **1.9** | **+0.4** | **+0.7** | 4.8 | **29.9** | **−0.7** |
| EU | 11.4 | +0.4 | 6.9 | +0.4 | 1.7 | +0.5 | +0.8 | 4.4 | 24.4 | +1.2 |
| EA | 11.9 | +0.6 | 7.1 | +0.4 | 1.8 | +0.5 | +0.8 | 4.3 | 25.1 | +1.4 |
| DE | 10.2 | +1.2 | 8.0 | +0.1 | 1.9 | +0.5 | +0.5 | 4.3 | 24.3 | +2.0 |
| IT | 15.6 | −1.9 | 6.3 | +0.1 | 1.6 | +0.3 | +0.5 | 3.8 | 27.3 | −2.0 |
| ES | 13.1 | +3.6 | 5.9 | +1.2 | 0.8 | +0.4 | +0.9 | 4.1 | 23.9 | +5.1 |
| NL | 6.5 | +2.0 | 5.7 | +0.7 | 3.8 | +1.2 | +1.9 | 4.9 | 21.0 | +3.5 |
| BE | 12.7 | +3.5 | 6.1 | +0.6 | 2.3 | +0.9 | +1.7 | 5.6 | 26.8 | +5.1 |
| SE | 7.4 | −0.2 | 7.3 | +0.4 | 3.2 | +0.6 | +1.3 | 5.8 | 23.6 | +0.8 |
| DK | 8.3 | −1.4 | 7.4 | +0.4 | 3.0 | +2.0 | +3.3 | 5.8 | 24.4 | +1.4 |

**Interpretation.** France has the **highest age-related spending in the EU (29.9% of GDP in 2022)**. Paradoxically, the EC projects it to *fall* by 0.7 pt by 2070. The fall comes from pensions (−0.9 pt), driven by indexation rules and reforms that lower the pension-to-wage ratio. **The steelman against "ageing will explode spending" is that the official baseline does not show an explosion for France.** The counter-argument is that the baseline relies on a falling relative standard of living of pensioners, which is politically fragile. The COR (pension advisory council) reports cover this; see the pensions file.

**Long-term care (*dépendance*).** EC baseline: 1.9% of GDP (2022) → 2.3% (2045) → 2.6% (2070). Drees (*Études et Résultats* 1032, R. Roussel, Oct. 12, 2017, reference scenario; verified 2026-10-25, pass 2, on the Drees publication page): public spending on dependent older people (health, care and accommodation, measured as the extra cost of dependency) rises from **1.11% of GDP (23.7 bn EUR) in 2014 to 2.07% in 2060**; total spending, all funders, from 1.40% (30.0 bn EUR) to 2.78%; the steepest rise is in 2030-2045. Sensitivity: −0.22 to +0.18 pt by 2060 across dependency-prevalence variants, ±0.11 pt across price vs wage indexation.[^drees-ltc] The two scopes differ: the EC figure includes disabled persons and health-related LTC; Drees covers elderly *dépendance* only. **I did not find an updated Drees projection published after 2017.**

---

## 8. Upward pressures: climate and defense

### 8.1 Climate transition (Pisani-Ferry & Mahfouz, France Stratégie, May 2023)[^pisani]

| Item | Value | Unit |
|---|---|---|
| Additional investment needed by 2030 vs a no-transition scenario | **≈ 66 bn EUR/yr = 2.3 pts of GDP** (≈ 80 bn if car sales keep rising; ≈ 51 bn if tertiary renovation is half spontaneous) | bn EUR / % of GDP |
| Public share | **25-34 bn EUR/yr by 2030** | bn EUR |
| Public-debt risk | **≈ +10 pts of GDP by 2030, +15 by 2035, +25 by 2040** (with energy-tax losses offset by new taxes) | % of GDP |
| Of which (2040) | ≈ 13 pts from cumulative spending net of carbon-auction revenue; ≈ 8 pts from slower potential growth (−0.3 pt/yr 2024-2030) | % of GDP |
| Local share (I4CE 2024) | ≈ **+11 bn EUR/yr** in local budgets by 2030 | bn EUR | 

Sources: France Stratégie (2023); HCSP Note 159 citing I4CE (2024).[^pisani][^hcsp159] The report recommended debt financing plus a temporary levy on the financial wealth of the richest households. That proposal is itself a source of the "wealth tax" debate.

### 8.2 Defense

| Indicator | Value | Unit | Year | Source |
|---|---|---|---|---|
| France defense spending (NATO "core defence" definition) | **2.04% (2025e); 2.22% (2026e)** (2014: 1.82; 2017: 1.78; 2024: 2.04) (corrected after verification: was 2.05% for 2025e and 2.03% for 2024, from the Aug. 2025 release, superseded by NATO's July 2026 release) | % of GDP | 2025e-2026e | NATO, July 2026[^nato] |
| Same, in euros | ≈ **61.0 bn EUR (2025e); 67.6 bn EUR (2026e)** (2017: 40.9 bn) (corrected: was 61.8 bn for 2025e) | bn EUR, current prices | 2025e-2026e | NATO, July 2026[^nato] |
| NATO Europe and Canada / NATO total | 2.31% / 2.75% (2025e); 2.53% / 2.86% (2026e) (corrected: was 2.27% / 2.76%) | % of GDP | 2025e-2026e | NATO, July 2026[^nato] |
| Panel (2025e → 2026e, % of GDP) | DE 2.22 → 2.69; IT 2.09 → 2.10; ES 2.00 → 2.00; NL 2.53 → 2.58; BE 2.00 → 2.00; SE 2.85 → 3.22; DK 3.27 → 3.49 (corrected: the Aug. 2025 values were DE n/a, IT 2.01, NL 2.49, SE 2.51, DK 3.22) | % of GDP | 2025e-2026e | NATO, July 2026[^nato] |
| New NATO target (Hague summit, June 2025) | **3.5% of GDP core defense by 2035** (plus 1.5% related spending) | % of GDP | 2035 | Sénat, citing NATO[^senat-lpm] |
| LPM credits (*mission Défense* budget) | **51 bn EUR (2025 exec.) → 57 (LFI 2026) → 63 (PLF 2027)** | bn EUR | 2025-2027 | PLF 2027[^plf2027] |
| LPM 2024-2030 updated (Law 2026-791 of Aug. 16, 2026, JORF Aug. 18, 2026; verified on Légifrance in a browser 2026-10-25, pass 2) | Art. 3 of the law: **+36 bn EUR** of new resources over 2026-2030 (Senate opinion on the bill: 35.7 bn). *Mission Défense* payment credits 2024-2030 total **435.7 bn EUR** (436 rounded; initial 2023 path 400 bn). Annual credits **47.2 (2024), 50.5 (2025), 57.1 (2026), 63.3 (2027), 69.5 (2028), 72.6 (2029), 75.7 bn EUR (2030)**, excl. pensions (corrected 2026-10-25, pass 2: was 76.3 bn EUR in 2030, from the Senate opinion on the bill). Art. 1 sets the goal of a national defense effort of **2% of GDP in 2025 → at least 2.5% in 2030, with 3.5% targeted by 2035**. The 441.6 bn EUR figure incl. extra-budgetary resources comes from the Senate opinion on the bill and was not found in the law's article 3 | bn EUR | 2024-2030 | Loi 2026-791, arts. 1 and 3[^lpm-law]; Sénat finance committee, May 26, 2026[^senat-lpm] |
| Shortfall vs a linear path to 3.5% | ≈ **0.22 pt of GDP (> 7 bn EUR/yr) in 2030** | % of GDP | 2030 | Sénat[^senat-lpm] |
| Gap 2.04% → 3.5% at 2025 GDP (2,991 bn EUR) | ≈ **44 bn EUR/yr** (≈ 38 bn from the 2.22% 2026e level) (corrected: was 43 bn from 2.05%) | bn EUR | — | My conversion |
| HCFP warning | From 2027, increases under programming laws (including, not only, the updated LPM) exceed **8 bn EUR**, leaving only ≈ **11 bn EUR** of growth for all other spending (excluding interest) under EU net-expenditure rules | bn EUR | 2027 | HCFP opinion on the LPM bill, via Sénat[^senat-lpm] |
| Interest burden | ≈ **100 bn EUR by end of decade** (30 bn in 2020) "*précisément le « poids de forme » … du budget annuel de la défense*" | bn EUR | ≈ 2030 | Sénat[^senat-lpm] |

**Implication for the platform:** ageing, climate (25-34 bn EUR public), defense (+12 bn EUR on the 2025 LPM path by 2027 and ≈ +44 bn EUR to reach 3.5% from the 2025 level) and interest (≈ +35 bn EUR by 2030) all push spending up by **several points of GDP** over 2025-2035. **These pressures are of the same order as, or larger than, the yield of any single tax proposal.**

---

## 9. Public investment and public net worth

### 9.1 Public investment (Eurostat gov_10a_main, my computation)[^es-gov]

| % of GDP | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | EA-20 agg. | DE | IT | ES | NL | BE | SE | DK |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Gross GFCF 2005 | 4.4 | 3.4 | 3.8 / 3.7 | 7/27 | 3.4 | 2.2 | 3.1 | 4.2 | 3.9 | 2.1 | 3.8 | 2.7 |
| Gross GFCF 2015 | 3.9 | 3.2 | 4.0 / 3.8 | 12/27 | 2.9 | 2.4 | 2.4 | 2.6 | 3.6 | 2.5 | 4.5 | 3.6 |
| Gross GFCF 2025 | **4.4** | 3.9 | 4.4 / 4.4 | 14/27 | 3.7 | 3.5 | 3.9 | 3.0 | 3.5 | 3.2 | 5.8 | 3.3 |
| Average gross GFCF 2005-2025 | 4.30 | 3.42 | — | — | 3.26 | 2.62 | 2.85 | 3.18 | 3.69 | 2.49 | 4.78 | 3.30 |
| **Net** investment 2025 (GFCF − depreciation) | **0.6** | 1.0 | 1.5 / 1.3 | **23/27** | 0.8 | 0.7 | 1.2 | 0.6 | 0.6 | 0.8 | 2.0 | 1.0 |
| Average net investment 2005-2025 | 0.56 | 0.55 | — | — | 0.41 | 0.16 | 0.01 | 0.78 | 0.58 | 0.22 | 1.40 | 0.56 |

- In euros: APU investment was ≈ **131.6 bn EUR in 2025** (+3.2%). It rose strongly in municipalities (+7.6%, pre-election cycle) and fell sharply in departments (−12.7%) (Insee, March 2026).[^insee-apu2025]
- **Reading:** France's *gross* public investment is above the EU and euro-area aggregates and above Germany. But France also has a large capital stock to maintain, so *net* investment is low (rank 23/27 in 2025). **Low public investment is not the explanation for high French spending.** It is also not proof of under-investment: quality-adjusted outcome data (infrastructure quality, maintenance backlogs) are fragmentary. The Cour notes that cuts by departments in 2024-2025 came "*potentiellement au détriment de la qualité de la voirie et du patrimoine bâti*".[^cdc-fpl2026]

### 9.2 Public-sector net worth (Insee, national balance sheet, end-2025, provisional)[^insee-patrimoine]

| bn EUR | General government | Whole economy |
|---|---|---|
| Non-financial assets | **2,945** (of which other buildings and civil engineering 1,430; land under buildings 941) | 20,292 |
| Financial assets | 1,718 (of which equity and fund shares 798) | 47,044 |
| Financial liabilities | 3,913 (of which debt securities 2,871) | 47,101 |
| Net financial position | **−2,195** | −57 |
| **Net worth** | **750 (≈ 25% of GDP, my conversion)** | 20,235 |

- **Earlier vintage:** Insee Première 2081 (*Le patrimoine économique national en 2024*, Nov. 6, 2025) gives general-government net worth of **690 bn EUR at end-2024** (3.5% of national wealth), after falls of **−234 bn EUR in 2023 and −50 bn EUR in 2024**; non-financial assets 2,821 bn, net financial position −2,132 bn (verified 2026-10-25, pass 2: was "secondary source, not re-verified"). The 690 (end-2024, Nov. 2025 vintage) and 750 (end-2025, July 2026 provisional) figures come from different vintages; do not present the difference as a 2025 rise without Insee's revised end-2024 value. FIPECO notes that **the State's own net worth is negative**, while local governments hold most public non-financial assets (≈ 66% of GDP at end-2024).[^fipeco-apul] Implicit pension liabilities are excluded from the balance sheet. Including them would make public net worth strongly negative.
- **Gap:** I could not retrieve a long Insee series to document the trend since 2007. The claim that net worth "fell sharply since the 2008 crisis" remains ⚠ unverified. **Recommendation: drop from site;** use the verified 2023-2024 falls above instead.

---

## 10. Outcome indicators (what France gets for the money)

| Domain | Outcome | France | Comparison | Source |
|---|---|---|---|---|
| Labor input | Hours per inhabitant | 666 h (EU-27 last) | EU-27 agg. 783 | Eurostat[^es-lp] |
| Labor quality | Productivity per hour (PPS) | 114.6 (EU=100) | DE 124.1, NL 125.9 | Eurostat[^es-lp] |
| Fiscal outcome | Deficit 2025 | 5.1% of GDP (rank 4/26 worst in EU) | EA-20 agg. 3.0% | Eurostat[^es-gov] |
| Business support | Jobs per CICE euro | 100-160k jobs for a cost of **≈ 18 bn EUR in 2016** (≈ 68 bn EUR cumulated 2014-2018) (corrected 2026-10-25, pass 2: was "≈ 18-20 bn EUR/yr, from memory"; source: France Stratégie, *Évaluation du CICE*, Sept. 2020, PDF pp. 8 and 55) | — | France Stratégie 2020[^cice] |
| Local investment | Local GFCF | 2.4% of GDP (rank 5/27) | EU-27 agg. 1.6% | Eurostat[^es-gov] |

---

## 11. Divergences between sources

| Topic | Source A | Source B | Why they differ |
|---|---|---|---|
| Cost of tax cuts since 2017 | Cour des comptes: 62 bn EUR = 2.2 pts (2018-2023 measures, valued in 2023) | OFCE: −2.5 pts of PO ratio (2017-2024); Rexecode: ≈ −2.6 pts (2018-2023 measures). (Removed 2026-10-25, pass 2: "−66 bn EUR current" per a secondary summary; the figure does not appear in Rexecode DT 105 itself, which gives 65 bn EUR only for net measures vs 2010) | The Cour uses discretionary measures. OFCE uses ratio changes, which mix measures with base and elasticity effects (OFCE footnote 9). Rexecode cumulates RESF measures by year, including the one-off 2019 CICE double cost |
| Net cuts still in place | "≈ 60-70 bn EUR" (common political usage) | ≈ 30-42 bn EUR (my netting of the 2024-2026 reversals) | Whether one counts the +36.7 bn EUR of 2024-2026 increases |
| PO ratio 2024 | Insee: **42.7%** (May 2026 vintage; 42.8% in March 2026) | Rexecode key figures: "42.7% in 2024" in its summary box but "43.2 in 2024" in its body text | Internal inconsistency in Rexecode DT 105, or different vintages. **Use Insee.** |
| PO rate definition | Insee: 43.6% (2025); 42.7-42.8% (2024) | Commission DG TAXUD: 43.5% (2024); Eurostat national-accounts maximal definition: 45.3% (2024) | DG TAXUD excludes imputed contributions but does not deduct tax credits; the Eurostat maximal variant is broader (corrected after verification)[^rexecode105] |
| Public expenditure 2025 | Insee (Mar. 2026): 57.2% of GDP | Eurostat (Oct. 2026) and Insee (May 2026): **57.3% (canonical)** | Insee's May 29, 2026 accounts revised **GDP** (to 2,991.1 bn EUR); expenditure is unchanged at 1,714.1 bn EUR in Eurostat (corrected after verification: was "revised GDP and spending") |
| Local-government debt | Cour des comptes: 225.4 bn EUR, 7.5% of GDP (budget accounts, incl. *syndicats*). On a narrower scope (main and annex budgets, **excluding *syndicats***), the same July 2026 report's annex 1 gives **194.5 bn EUR at end-2024 and 203.3 bn EUR at end-2025** (verified 2026-10-25, pass 2, annex 1, PDF pp. 179-180; corrected attribution: was "the 2025 edition gave 194.5 bn EUR for 2024") | Eurostat S1313: 9.3% of GDP | EDP debt covers all APUL (incl. ODAL such as the Société des Grands Projets) at face value. *(Corrected after verification: the earlier text also listed "public hospitals' local entities"; French public hospitals are classified in the social-security sub-sector (ASSO, S1314), not in APUL.)* |
| Local-government deficit | National accounts: −9.3 bn EUR | Budget accounts: −11.3 bn EUR | DILICO reserve (1 bn EUR) and accounting differences[^cdc-fpl2026] |
| Business aid | 211 bn (Sénat) | 187 / 82 bn (HCSP), 45 bn (EU State aid) | Treatment of general contribution reliefs, Bpifrance loans (face value vs subsidy-equivalent), VAT reduced rates, reclassified tax expenditures |
| Taxe d'habitation cost | ≈ 18 bn EUR (Senate, Ecalle) | 23.5 bn EUR (Fipeco local loss 2020); OFCE −1.0 pt of GDP (≈ 29 bn, my conversion) | Net State cost vs gross local revenue loss vs change in ratio (incl. base growth) |
| Productivity gap | Eurostat: real hourly productivity −0.8% 2019-2025 | CNP: per-head productivity 0.7 pt below 2019; Insee: hourly ≈ 5 pts below trend | Per head vs per hour; level vs trend; 2025 national-accounts revisions |
| Fertility 2024 | Insee: 1.61 | Eurostat: 1.61 | Consistent. Insee's 2025 figure (1.56) is not yet in Eurostat |
| Defense effort | NATO (July 2026): 2.04% of GDP, 61.0 bn EUR (2025e) (was 2.05% / 61.8 bn in the Aug. 2025 release) | Budget (LPM): 51 bn EUR executed in 2025 | The NATO definition includes pensions and parts of the gendarmerie; the LPM figure excludes pensions |

---

## 12. Economists' disagreements and the strongest counter-arguments to the platform's thesis

1. **"It's a revenue problem" (OFCE; left-leaning economists; reinforced by the Cour des comptes 2024 wording).** The 2017-2024 deficit deterioration matches the PO cut almost point for point, and primary spending fell. *Response:* the baseline matters. Against 2010 or euro-area norms, revenue is already very high. Revenue increases since 2024 (+1.2 pts) did not stabilize debt, because interest and social spending kept rising.[^ofce146][^rexecode105]
2. **"Capital-tax cuts gave nothing" (France Stratégie committee: no investment effect of the PFU; ISF→IFI cost > 4 bn EUR).** This is a strong argument for targeted increases (e.g., on dividends or large estates). *But* the yields are small (≈ 4-5 bn EUR) relative to a 151.6 bn EUR deficit in 2025 (5.1% of GDP; October 2026 EDP vintage) (corrected 2026-10-25, pass 2: was 152.5 bn EUR, the March/May 2026 vintage). The PFU partly self-financed through higher dividends, and expatriation flows reversed after 2018 (380 returns vs 260 departures per year).[^fs-isf]
3. **"Business aid is 211 bn EUR; cut it."** *Response:* most of it is general contribution relief. Removing it would cost ≈ 1 m jobs (Bozio-Wasmer), and the net yield is ≈ 48 bn EUR, not 75 (nor the 67 bn EUR static gain). The aid perimeter "that a government can plausibly cut" (HCSP perimeter 1) is 82 bn EUR, much of it R&D tax credit, overseas-territory and agriculture schemes.[^bw2024][^hcsp-aides]
4. **"Ageing will not explode spending in France" (EC 2024 Ageing Report: −0.7 pt by 2070).** This is a genuine counter-point to alarmist narratives. *But* it relies on pensions falling relative to wages. LTC still rises by +0.7 pt, and the fertility drop to 1.56 is not in the projections.[^ar2024]
5. **"Raise employment instead of cutting spending."** A strong argument: the DG Trésor estimates ≈ +38 bn EUR of revenue for alignment with Germany (FTE). *But* it takes years, requires reforms that are themselves contested (pension age, unemployment insurance, SMIC), and is partly offset by future pension costs.[^hcfips]
6. **"Public investment is too low, so don't cut."** Not supported for France in gross terms (4.4% of GDP, above the EA and DE). *But* net investment is low (0.6%), and climate (+25-34 bn EUR public) and defense needs are real.[^es-gov][^pisani]
7. **"Local governments are well-managed and not responsible for the deficit."** Largely true on debt and savings ratios. *But* they ran a 9-12 bn EUR deficit in 2024-2025, and staff grew without new competences in 2011-2021.[^cdc-fpl2026][^cdc-fpt]

---

## 13. Open questions and gaps

- **HCFP opinion on the PLF 2027**: *resolved in file 00.* Avis HCFP-2026-5 is dated Sept. 25, 2026 and was published with the PLF on Oct. 1, 2026 (https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf). This file still cites the HCFP's LPM opinion only via the Senate.
- **Cour des comptes RSPFP June 2026:** *resolved during verification.* The primary PDF (https://www.ccomptes.fr/sites/default/files/2026-06/20260625-RSPFP-2026.pdf) confirms the 3.0-pt (89.6 bn EUR) debt-stabilizing adjustment and attributes the 2025 deficit fall "exclusively" to 23 bn EUR of tax increases. An updated cumulative cost of the 2018-2023 cuts was not located in it.
- **CIT-cut cost (≈ 11 bn EUR static)** and **CICE cost**: *resolved 2026-10-25, pass 2.* CIT: Assemblée nationale report 1838 (Apr. 2019), "of the order of 11 bn EUR". CICE: France Stratégie (Sept. 2020), "of the order of 18 bn EUR in 2016", ≈ 68 bn EUR cumulated 2014-2018 (was "18-20 bn EUR a year, from memory").
- **Drees long-term care projections**: the 2017 projection (ER 1032) is now verified on the Drees page; none more recent than 2017 was found. The *Panorama* "*L'aide et l'action sociales*" and the 2024 *Dépenses de soutien à l'autonomie* should be checked.
- **Local civil-service headcount growth**: *resolved 2026-10-25, pass 2.* The 2011-2021 Cour figure (+100,000, +5.5%) is in the primary report, *Les finances publiques locales 2024 - fascicule 2* (Oct. 2, 2024). The 1998-2008 figure (≈ +350,000 excl. transfers) still rests on a 2012 press article (Banque des Territoires).
- **Public net worth time series** (2007-2025) not retrieved; only the end-2025 level is verified.
- **Institut Montaigne / CAE estimates** of the employment-gap fiscal dividend were not found. Only DG Trésor/HCFiPS and IFRAP (not used: think tank, liberal orientation) were found.
- **Spending per capita in PPS** for the APU total could not be retrieved directly through the Eurostat API (empty response for PPS_HAB). It is derived in file 09 (TE/GDP x GDP per capita in PPS): **23,330 PPS per inhabitant in 2025, 8th of 27** (canonical, see `00-reference-figures.md`).
- **OECD hours per worker / per capita** were not downloaded; Eurostat data are used instead.
- **I4CE Panorama des financements climat 2025** (national public climate-investment gap) not retrieved.
- **PLF 2027 local-government contribution** (corrected 2026-10-25, pass 2: was "5.5 bn EUR, press reports (Euronews), not verified"). The PLF 2027 text (Oct. 1, 2026) creates a *contribution progressive à l'effort budgétaire* (CPEB, progressive contribution to the budget effort) with an expected yield of **2.5 bn EUR** and cuts the FCTVA (VAT compensation fund for local investment) rate by 5 points, **−2.1 bn EUR** vs LFI 2026 (PLF 2027, *exposé général* and the CPEB article's *exposé des motifs*, https://www.budget.gouv.fr/documentation/file-download/33478). The total of **≈ 5.4 bn EUR** is the government's own presentation to the Comité des finances locales on Sept. 30, 2026, known only via Banque des Territoires (https://www.banquedesterritoires.fr/budget-2027-les-collectivites-appelees-un-effort-de-54-milliards-deuros); local-government associations put it at 7-7.5 bn EUR including higher CNRACL pension contributions. Keep with caveat; quote the two primary components (2.5 + 2.1 bn EUR).

---

## 14. Full source list (all accessed 2026-10-25)

| # | Institution | Title | Publication date | URL |
|---|---|---|---|---|
| 1 | Cour des comptes | *La situation et les perspectives des finances publiques* (RSPFP) | July 15, 2024 | https://www.ccomptes.fr/sites/default/files/2024-07/20240715-RSPFP-2024_0.pdf |
| 2 | Cour des comptes | *La situation des finances publiques début 2026* (synthèse) | Feb. 19, 2026 | https://www.ccomptes.fr/sites/default/files/2026-02/20260219-synthese-situation-des-finances-publiques-debut-2026_0.pdf |
| 3 | Cour des comptes | *La situation et les perspectives des finances publiques* (RSPFP), June 2026 (primary, verified; replaces the Legifiscal secondary summary) | June 25, 2026 | https://www.ccomptes.fr/sites/default/files/2026-06/20260625-RSPFP-2026.pdf |
| 4 | Cour des comptes | *Les finances publiques locales - Résultats 2025 et perspectives 2026* | July 9, 2026 | https://medias.amf.asso.fr/upload/files/20260709-Finances-publiques-locales-2026.pdf |
| 5 | OFCE (Heyer, Plane, Ragot, Sampognaro, Timbeau) | *Quelles trajectoires pour les finances publiques de la France ?* Policy Brief 146 | July 11, 2025 | https://www.ofce.fr/pdf/pbrief/2025/OFCEpbrief146.pdf |
| 6 | Rexecode (business-funded think tank) | *Bilan des prélèvements obligatoires 2026*, Document de travail 105 | Sept. 2026 | https://www.rexecode.fr/media/documents/document-de-travail/2026/bilan-des-prelevements-obligatoires-document-de-travail-n.105-septembre-2026 |
| 7 | France Stratégie (now HCSP) | *Comité d'évaluation des réformes de la fiscalité du capital - Avis du comité* (4th report) | Oct. 2023 | https://www.strategie-plan.gouv.fr/files/files/Publications/Rapport/fs-2023-rapport-isf-quatrieme_rapport_complet_17octobre_avis_0.pdf |
| 8 | IPP (Fabre et al.) | Redistributive effects of the 2017-2022 socio-fiscal measures, Note 81 | March 2022 | https://www.ipp.eu/en/publication/redistributive-effects-of-the-socio-fiscal-measures-implemented-during-the-2017-2022-five-year-term-aimed-at-households/ |
| 9 | Bozio & Wasmer (report to the PM) | *Les politiques d'exonérations de cotisations sociales : une inflexion nécessaire* | Oct. 3, 2024 | https://vie-publique.fr/files/rapport/pdf/295596.pdf |
| 10 | Sénat | Commission of inquiry on public aid to large companies, report 808 (2024-2025) | July 8, 2025 | https://www.senat.fr/rap/r24-808-1/r24-808-17.html |
| 11 | Public Sénat | *211 milliards d'euros d'aides publiques aux entreprises : sur quoi repose le calcul…* | July 2025 | https://www.publicsenat.fr/actualites/economie/211-milliards-deuros-daides-publiques-aux-entreprises-sur-quoi-repose-le-calcul-de-la-commission-denquete-du-senat |
| 12 | Haut-commissariat à la Stratégie et au Plan (HCSP; Beaune, Harfi) | *Les aides aux entreprises : définition, périmètres, cadre de suivi et d'évaluation* | July 2026 | https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-07-16%20-%20Rapport%20Aides%20aux%20entreprises/HCSP-2026-RAPPORT-AIDES-ENTREPRISES.pdf |
| 13 | HCSP | *Dépenses locales : pour un nouveau contrat entre collectivités et État*, Note d'analyse 159 | April 1, 2026 | https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-04-01%20-%20NA%20159%20-%20D%C3%A9penses%20locales/HCSP-2026-NA159-D%C3%A9penses-locales-1avril18h-FINAL.pdf |
| 14 | Conseil national de productivité | 6th report, *Les nouveaux contours de la productivité française* | July 1, 2026 | https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-07-01%20-%20CNP%20-%20Rapport%20et%20NS/CNP-2026-Sixi%C3%A8me-Rapport-1juillet15h-FINAL-COUV.pdf |
| 15 | DG Trésor for HCFiPS | *Quels seraient les effets sur les finances sociales d'un alignement du taux d'emploi français sur celui de l'Allemagne ?* | Aug. 7, 2024 | https://www.securite-sociale.fr/files/live/sites/SSFR/files/medias/HCFIPS/2024/20240807_Annexe_emploi_FR_ALL_vf.pdf |
| 16 | Insee | *Comptes nationaux des administrations publiques - premiers résultats - année 2025*, Informations Rapides 78 | March 27, 2026 | https://www.insee.fr/fr/statistiques/fichier/version-html/8956575/IR78-APU-ann%C3%A9e2025.pdf |
| 17 | Insee | *Patrimoine national par secteur institutionnel et grand type d'actif fin 2025* | July 30, 2026 | https://www.insee.fr/fr/statistiques/2830290 |
| 18 | Insee | *Bilan démographique 2025*, Insee Première 2087 | Jan. 2026 | https://www.insee.fr/fr/statistiques/8719824 |
| 19 | Insee | *L'emploi dans la fonction publique en 2024*, Insee Première 2094 | Feb. 2026 | https://www.insee.fr/fr/statistiques/8732435 |
| 20 | Ministère de l'Économie | *Projet de loi de finances pour 2027* | Oct. 1, 2026 | https://www.budget.gouv.fr/documentation/file-download/33478 |
| 21 | Sénat, finance committee (D. de Legge) | *Actualisation de la programmation militaire 2024-2030*, avis 654 synthesis | May 26, 2026 | https://www.senat.fr/rap/a25-654/a25-654-syn.pdf |
| 22 | Légifrance | Loi n° 2026-791 actualisant la programmation militaire 2024-2030 (JORF n° 191, Aug. 18, 2026; read in a browser 2026-10-25) | Aug. 16, 2026 | https://www.legifrance.gouv.fr/jorf/id/JORFSCTA000054694833 |
| 23 | NATO | *Defence Investment of NATO Countries (2014-2026)*, press release (supersedes the Aug. 2025 *Defence Expenditure of NATO Countries (2014-2025)*: https://nato.int/content/dam/nato/webready/documents/finance/def-exp-2025-en.pdf) | July 7, 2026 (data cut-off July 3, 2026) | https://www.nato.int/content/dam/nato/webready/documents/finance/def-exp-2026-en.pdf |
| 24 | France Stratégie (Pisani-Ferry, Mahfouz) | *Les incidences économiques de l'action pour le climat* | May 2023 | https://www.strategie-plan.gouv.fr/files/files/Publications/Rapport/2023-incidences-economiques-rapport-pisani-5juin.pdf |
| 25 | European Commission / EPC | *2024 Ageing Report*, Institutional Paper 279 | April 2024 | https://economy-finance.ec.europa.eu/document/download/971dd209-41c2-425d-94f8-e3c3c3459af9_en?filename=ip279_en.pdf |
| 26 | Drees | *Personnes âgées dépendantes : les dépenses de prise en charge pourraient doubler en part de PIB d'ici à 2060*, Études et Résultats 1032 (corrected 2026-10-25: old URL redirects elsewhere) | Oct. 12, 2017 | https://drees.solidarites-sante.gouv.fr/publications/etudes-et-resultats/personnes-agees-dependantes-les-depenses-de-prise-en-charge |
| 27 | France Stratégie | CICE evaluation, press release on the synthesis | Sept. 1, 2020 | https://www.strategie.gouv.fr/files/files/Presse/CP%202020/2020-09-01_Evaluation%20du%20CICE%20%3B%20France%20Strat%C3%A9gie%20publie%20une%20synth%C3%A8se%20des%20travaux%20d%27approfondissement.pdf |
| 28 | Banque de France | Bulletin 231-6, *Politiques économiques* (CICE/PRS jobs) | Sept.-Oct. 2020 (corrected 2026-10-25: was Jan. 2023) | https://www.banque-france.fr/system/files/2023-01/bdf231-6_politiques-economiques.pdf |
| 29 | Eurostat | gov_10a_main, gov_10dd_edpt1 (government finance) | Updated Oct. 21, 2026 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_main |
| 30 | Eurostat | lfsi_emp_a (employment rates) | Updated Sept. 10, 2026 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsi_emp_a |
| 31 | Eurostat | nama_10_lp_ulc (productivity, hours per capita); nama_10_a10_e | Updated Oct. 22, 2026 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_lp_ulc |
| 32 | Eurostat | demo_find, demo_pjanind, demo_gind, proj_23ndbi | Updated Sept. 2026 (proj. May 2026) | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/proj_23ndbi |
| 33 | OECD | Infra-annual labour statistics, employment rate 15-64 (SDMX DSD_LFS@DF_IALFS_EMP_WAP_Q) | Accessed 2026-10-25 | https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_EMP_WAP_Q,1.0/ |
| 34 | Fipeco (F. Ecalle; independent, fiscally conservative) | *Patrimoine des APUL 2024* | 2025 | https://fipeco.fr/pdf/Patrimoine%20APUL%202024.pdf |
| 35a | Cour des comptes | *Les finances publiques locales 2024 - fascicule 2* (primary for the +100,000 agents and 4.1 bn EUR figures) | Oct. 2, 2024 | https://www.ccomptes.fr/sites/default/files/2024-10/20241002-finances-publiques-locales-fascicule-2.pdf |
| 35b | Assemblée nationale | Report 1838 (J. Giraud) on the digital services tax and CIT trajectory bill (CIT cut ≈ 11 bn EUR) | Apr. 3, 2019 | https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L15B1838.html |
| 35c | Insee | *Le patrimoine économique national en 2024*, Insee Première 2081 | Nov. 6, 2025 | https://www.insee.fr/fr/statistiques/8661938 |
| 35 | Acteurs publics | *La Cour des comptes pousse à la suppression de 100 000 postes dans les collectivités* (secondary) | Oct. 2024 | https://acteurspublics.fr/articles/la-cour-des-comptes-pousse-a-la-suppression-de-100-000-postes-dans-les-collectivites |
| 36 | Banque des Territoires | *Effectifs du bloc local pointés par la Cour des comptes* (secondary) | July 4, 2012 | https://www.banquedesterritoires.fr/effectifs-du-bloc-local-pointes-par-la-cour-des-comptes-les-associations-delus-reagissent |
| 37 | Maire-info | *Emploi dans la fonction publique territoriale : une légère hausse…* (secondary on Insee/DGCL) | Feb. 16, 2026 | https://www.maire-info.com/fonction-publique-territoriale/emploi-dans-la-fonction-publique-territoriale-une-legere-hausse-du-nombre-dagents-portee-par-les-contractuels-article-30485 |
| 38 | Sénat / Fipeco (TH cost) | Senate finance report on TH; Fipeco note on TH (2018) | 2018-2021 | https://www.senat.fr/rap/l21-163-327/l21-163-32711.html ; https://fipeco.fr/pdf/0.95368400%201524838078.pdf |
| 39 | DGE / Banque des Territoires (production taxes, CVAE) | *La suppression définitive de la CVAE*; PLF 2021 production taxes | 2020-2025 | https://www.entreprises.gouv.fr/la-dge/publications/la-suppression-definitive-de-la-cotisation-sur-la-valeur-ajoutee-des ; https://www.banquedesterritoires.fr/que-prevoit-le-projet-de-loi-de-finances-pour-2021-concernant-les-impots-dits-de-production ; https://formation.lefebvre-dalloz.fr/actualite/cvae-report-de-la-suppression-2030-et-contribution-complementaire-pour-2025 |

**Local raw-data files (this research):**
`research/data/08_eurostat_*.csv`, `08_oecd_employment_rate_15_64.csv`, `08_computed_international_stats.csv`. Source PDFs are in `research/data/raw/08/pdf/`.

---

### Footnotes

[^cdc2024]: Cour des comptes, *La situation et les perspectives des finances publiques*, July 2024, chapter I.II.C, pp. 35-39 (62 bn EUR = 2.2 pts in 2023; PO 45.3% in 2017, 45.0% in 2022, 43.2% in 2023; "more than 60 bn EUR"; local revenue +21%, ASSO +24%, State +4% since 2017). https://www.ccomptes.fr/sites/default/files/2024-07/20240715-RSPFP-2024_0.pdf
[^ofce146]: OFCE Policy Brief 146, July 11, 2025, key points and Tables 3-4. https://www.ofce.fr/pdf/pbrief/2025/OFCEpbrief146.pdf
[^rexecode105]: Rexecode, Document de travail 105, *Bilan des prélèvements obligatoires 2026*, Sept. 2026: synthesis, pp. 5-7, 16-20. Business-oriented think tank. https://www.rexecode.fr/media/documents/document-de-travail/2026/bilan-des-prelevements-obligatoires-document-de-travail-n.105-septembre-2026
[^insee-apu2025]: Insee, Informations Rapides 78, March 27, 2026 (deficit 152.5 bn EUR = 5.1% of GDP; expenditure 1,714.1 bn EUR = 57.2%; PO 43.6% in 2025, 42.8% in 2024; interest 64.7 bn EUR = 2.2% of GDP, footnoted by Insee as excluding the FISIM correction; the canonical ESA D.41 value is **65.7 bn EUR** (file 00 row 39); investment 131.6 bn EUR). Canonical 2025 deficit: 151.6 bn EUR (October 2026 EDP vintage). https://www.insee.fr/fr/statistiques/fichier/version-html/8956575/IR78-APU-ann%C3%A9e2025.pdf
[^fs-isf]: France Stratégie, Comité d'évaluation des réformes de la fiscalité du capital, *Avis du comité*, Oct. 2023, pp. 12-14 and investment section. https://www.strategie-plan.gouv.fr/files/files/Publications/Rapport/fs-2023-rapport-isf-quatrieme_rapport_complet_17octobre_avis_0.pdf
[^bw2024]: A. Bozio and É. Wasmer, *Les politiques d'exonérations de cotisations sociales : une inflexion nécessaire*, Oct. 2024, ch. 1, §4, pp. 67-68. https://vie-publique.fr/files/rapport/pdf/295596.pdf
[^senat-aides]: Sénat, commission of inquiry on public aid to large companies and their subcontractors (chair O. Rietmann, rapporteur F. Gay), report 808 (2024-2025), tome I, deposited July 1, 2025 (presented July 8, 2025). The cited page (section V, "Plusieurs tentatives pour établir le coût des aides") gives the France Stratégie 139-223 bn, Clersé 205 bn (2019) and ministerial 150 bn estimates; the 211 / 108 bn figures are elsewhere in the report and were verified via the HCSP 2026 report, Annex 4. https://www.senat.fr/rap/r24-808-1/r24-808-17.html
[^hcsp-aides]: Haut-commissariat à la Stratégie et au Plan, *Les aides aux entreprises : définition, périmètres, cadre de suivi et d'évaluation*, report to the Prime Minister (C. Beaune; rapporteur M. Harfi), July 2026, pp. 16, 27-29. https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-07-16%20-%20Rapport%20Aides%20aux%20entreprises/HCSP-2026-RAPPORT-AIDES-ENTREPRISES.pdf
[^publicsenat]: Public Sénat, "211 milliards d'euros d'aides publiques aux entreprises : sur quoi repose le calcul de la commission d'enquête du Sénat ?", July 2025. https://www.publicsenat.fr/actualites/economie/211-milliards-deuros-daides-publiques-aux-entreprises-sur-quoi-repose-le-calcul-de-la-commission-denquete-du-senat
[^hcsp159]: HCSP, Note d'analyse 159, *Dépenses locales : pour un nouveau contrat entre collectivités et État*, April 2026, pp. 1-3, Table 1. https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-04-01%20-%20NA%20159%20-%20D%C3%A9penses%20locales/HCSP-2026-NA159-D%C3%A9penses-locales-1avril18h-FINAL.pdf
[^cdc-fpl2026]: Cour des comptes, *Les finances publiques locales - Résultats 2025 et perspectives 2026*, July 2026, synthesis pp. 9-16; ch. I §II-IV (VAT 52.7 bn EUR; DGF 27.4 bn EUR; investment 79.1 bn EUR; gross savings 40.2 bn EUR; debt 225.4 bn EUR = 7.5% of GDP). https://medias.amf.asso.fr/upload/files/20260709-Finances-publiques-locales-2026.pdf
[^cdc-feb2026]: Cour des comptes, *La situation des finances publiques début 2026*, synthesis, Feb. 19, 2026. https://www.ccomptes.fr/sites/default/files/2026-02/20260219-synthese-situation-des-finances-publiques-debut-2026_0.pdf
[^cdc2026-rspfp]: Cour des comptes, *La situation et les perspectives des finances publiques*, June 25, 2026, synthesis pp. 13-14 and ch. I (89.6 bn EUR = 3.0 pts of GDP; deficit fall "exclusivement imputable à des hausses d'impôts" of 23 bn EUR; debt 3,460.5 bn EUR = 115.7% of GDP, May 2026 vintage; canonical end-2025 value 3,460.1 bn EUR, file 00 row 35). Primary verified 2026-10-25. https://www.ccomptes.fr/sites/default/files/2026-06/20260625-RSPFP-2026.pdf (secondary summary: https://www.legifiscal.fr/actualites-fiscales/4544-cour-comptes-situation-perspectives-finances-publiques.html)
[^es-gov]: Eurostat gov_10a_main (sector S13 and S1313; na_item TE, TR, B9, P51G, P51C, D1PAY; unit PC_GDP) and gov_10dd_edpt1 (S1313 GD), updated Oct. 21, 2026; my extracts and computations in `data/08_eurostat_gov_10a_main*.csv`, `data/08_eurostat_gov_10dd_edpt1_s1313.csv`, `data/08_computed_international_stats.csv`. https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_main
[^es-emp]: Eurostat lfsi_emp_a (EMP_LFS, PC_POP), updated Sept. 10, 2026; `data/08_eurostat_lfsi_emp_a.csv`. Break in series before 2009 for most countries, so 2009 is used as the base year. https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/lfsi_emp_a
[^es-lp]: Eurostat nama_10_lp_ulc (HW_HAB; NLPR_HW in PC_EU27_2020_MPPS_CP; RLPR_HW indices I15/I20), updated Oct. 22, 2026, and nama_10_a10_e (hours and persons) with demo_gind (average population); `data/08_eurostat_nama_10_lp_ulc*.csv`, `data/08_eurostat_nama_10_a10_e.csv`. https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/nama_10_lp_ulc
[^oecd-emp]: OECD SDMX, DSD_LFS@DF_IALFS_EMP_WAP_Q, annual 15-64 employment rate 2024-2025, accessed 2026-10-25; `data/08_oecd_employment_rate_15_64.csv`. https://sdmx.oecd.org/public/rest/data/OECD.SDD.TPS,DSD_LFS@DF_IALFS_EMP_WAP_Q,1.0/
[^hcfips]: DG Trésor (J. Ducoulombier), note for the HCFiPS, Aug. 7, 2024, pp. 1-9. *Corrected after verification:* the "38 to 84 bn EUR" increase in compulsory levies of all general government (on the 2022 base of 1,194 bn EUR) **is** in the primary note, box 1, p. 9; it is a PO figure, not total public revenue. The earlier statement that it came only from secondary summaries was wrong. https://www.securite-sociale.fr/files/live/sites/SSFR/files/medias/HCFIPS/2024/20240807_Annexe_emploi_FR_ALL_vf.pdf
[^cnp2026]: Conseil national de productivité, 6th report, July 1, 2026, pp. 15-18. https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-07-01%20-%20CNP%20-%20Rapport%20et%20NS/CNP-2026-Sixi%C3%A8me-Rapport-1juillet15h-FINAL-COUV.pdf
[^insee-demo]: Insee Première 2087, *Bilan démographique 2025*, Jan. 2026. https://www.insee.fr/fr/statistiques/8719824
[^es-demo]: Eurostat demo_find (TOTFERRT), updated Sept. 30, 2026; `data/08_eurostat_demo_find.csv`.
[^es-proj]: Eurostat proj_23ndbi (OLDDEP1, BSL), updated May 13, 2026, and demo_pjanind (OLDDEP1), updated Sept. 25, 2026; `data/08_eurostat_proj_23ndbi.csv`, `data/08_eurostat_demo_pjanind.csv`.
[^ar2024]: European Commission and EPC, *2024 Ageing Report*, Institutional Paper 279, April 2024, Table 5 (baseline). https://economy-finance.ec.europa.eu/document/download/971dd209-41c2-425d-94f8-e3c3c3459af9_en?filename=ip279_en.pdf
[^drees-ltc]: Drees, R. Roussel, "*Personnes âgées dépendantes : les dépenses de prise en charge pourraient doubler en part de PIB d'ici à 2060*", *Études et Résultats* 1032, Oct. 12, 2017. Verified 2026-10-25 (pass 2) on the publication page, read in a browser: https://drees.solidarites-sante.gouv.fr/publications/etudes-et-resultats/personnes-agees-dependantes-les-depenses-de-prise-en-charge (PDF: https://drees.solidarites-sante.gouv.fr/sites/default/files/er1032.pdf). (Corrected 2026-10-25: the earlier URL, `.../2021-01/Le financement de la dépendance de 2017 à 2060.pdf`, now redirects to an unrelated Drees page and should not be used.)
[^pisani]: J. Pisani-Ferry and S. Mahfouz, *Les incidences économiques de l'action pour le climat*, France Stratégie, May 2023, synthesis points 11-12, ch. 7 (66 bn EUR) and ch. 10 (25-34 bn EUR public; debt +10/+15/+25 pts). https://www.strategie-plan.gouv.fr/files/files/Publications/Rapport/2023-incidences-economiques-rapport-pisani-5juin.pdf
[^nato]: NATO, *Defence Investment of NATO Countries (2014-2026)*, press release, July 7, 2026 (cut-off July 3, 2026), Table 1 (core defence expenditure, current prices: France 61,002 m EUR in 2025e, 67,632 m EUR in 2026e) and Table 3 (share of real GDP: France 2.04% in 2025e, 2.22% in 2026e). Image-only PDF, read from rendered pages. https://www.nato.int/content/dam/nato/webready/documents/finance/def-exp-2026-en.pdf . Superseded edition: Aug. 2025, https://nato.int/content/dam/nato/webready/documents/finance/def-exp-2025-en.pdf
[^senat-lpm]: Sénat, finance committee, avis 654 (2025-2026) on the bill updating the LPM 2024-2030, synthesis, May 26, 2026. https://www.senat.fr/rap/a25-654/a25-654-syn.pdf
[^plf2027]: *Projet de loi de finances pour 2027*, Oct. 1, 2026, *Exposé général des motifs*, pp. 12-16, and the PDE table ("dont LPM": 51 / 57 / 58 / 63 bn EUR). https://www.budget.gouv.fr/documentation/file-download/33478
[^insee-patrimoine]: Insee, *Patrimoine national par secteur institutionnel et grand type d'actif fin 2025*, July 30, 2026 (provisional). https://www.insee.fr/fr/statistiques/2830290
[^fipeco-apul]: FIPECO (F. Ecalle), *Patrimoine des APUL 2024*. https://fipeco.fr/pdf/Patrimoine%20APUL%202024.pdf
[^insee-fp]: Insee Première 2094, *L'emploi dans la fonction publique en 2024* (E. Esbelin, T. Moreau, S. Touzé), Feb. 10, 2026, figure 1 (FPT 2,039.4 thousand incl. subsidized contracts at Dec. 31, 2024) and text (+0.3%, +6,400; contract staff +2.6%, +13,500). Read directly 2026-10-25, pass 2. Insee warns of declaration and processing changes in 2023-2024. https://www.insee.fr/fr/statistiques/8732435
[^cdc-fpt]: Cour des comptes, *Les finances publiques locales 2024 - fascicule 2*, Oct. 2, 2024, PDF pp. 63 and 76 (primary, verified 2026-10-25, pass 2). https://www.ccomptes.fr/sites/default/files/2024-10/20241002-finances-publiques-locales-fascicule-2.pdf . Press coverage: Acteurs publics, https://acteurspublics.fr/articles/la-cour-des-comptes-pousse-a-la-suppression-de-100-000-postes-dans-les-collectivites
[^cdc-fpt2012]: Cour des comptes, report of July 2, 2012, as reported by Banque des Territoires, July 4, 2012 (secondary). https://www.banquedesterritoires.fr/effectifs-du-bloc-local-pointes-par-la-cour-des-comptes-les-associations-delus-reagissent
[^th-cost]: Taxe d'habitation cost: Sénat finance committee report (≈ 18 bn EUR; split 10.2/7.8 bn) https://www.senat.fr/rap/l21-163-327/l21-163-32711.html ; Fipeco (2018, 23.5 bn EUR local loss in 2020) https://fipeco.fr/pdf/0.95368400%201524838078.pdf ; DGCL FAQ on the local-tax overhaul (dead link, HTTP 404 on 2026-10-25; **replaced 2026-10-25, pass 2** by the Senate report above, which documents the compensation: departmental TFPB of 15 bn EUR to municipalities, 22.8 bn EUR of VAT fractions (15 bn departments, 7.2 bn intercommunalities, 0.6 bn Paris) plus a 0.4 bn EUR grant, against 5.3 bn EUR of TH relief the State no longer pays). Both the Senate (≈ 18 bn; 10.2 / 7.8 bn) and Fipeco (23.5 bn) figures were re-read in the primary texts on 2026-10-25, pass 2.
[^prod-tax]: Production taxes: Banque des Territoires on PLF 2021 (10 bn EUR/yr; CVAE ≈ 7.25 bn) https://www.banquedesterritoires.fr/que-prevoit-le-projet-de-loi-de-finances-pour-2021-concernant-les-impots-dits-de-production ; DGE on CVAE abolition (4.1 bn in 2023, 9.3 bn total) https://www.entreprises.gouv.fr/la-dge/publications/la-suppression-definitive-de-la-cotisation-sur-la-valeur-ajoutee-des ; postponement to 2030: verified 2026-10-25 (pass 2) in the consolidated CGI art. 1586 *quater* on Légifrance (modified by law 2025-127, art. 62; 2026 version: top rate 0.28%; 2029 version: 0.09%) https://www.legifrance.gouv.fr/codes/article_lc/LEGIARTI000048860944 (secondary, not needed: Lefebvre Dalloz, https://formation.lefebvre-dalloz.fr/actualite/cvae-report-de-la-suppression-2030-et-contribution-complementaire-pour-2025)
[^ipp81]: IPP, Policy Brief / Note 81 (Fabre, Lallemand, Loisel, Puschnig, Dutronc-Postel), March 2022, as summarized on the IPP page. https://www.ipp.eu/en/publication/redistributive-effects-of-the-socio-fiscal-measures-implemented-during-the-2017-2022-five-year-term-aimed-at-households/
[^cice]: France Stratégie, *Évaluation du crédit d'impôt pour la compétitivité et l'emploi*, synthesis report, Sept. 2020, PDF p. 8 (cost ≈ 18 bn EUR in 2016) and p. 55 (≈ 68 bn EUR cumulated 2014-2018) https://www.strategie-plan.gouv.fr/files/files/Publications/2020/CICE/fs-2020-rapport-cice2020-16septembre-final18h.pdf ; press release, Sept. 1, 2020 https://www.strategie.gouv.fr/files/files/Presse/CP%202020/2020-09-01_Evaluation%20du%20CICE%20%3B%20France%20Strat%C3%A9gie%20publie%20une%20synth%C3%A8se%20des%20travaux%20d%27approfondissement.pdf ; Banque de France, *Bulletin* 231/6, Sept.-Oct. 2020 (corrected 2026-10-25, pass 2: was dated Jan. 2023, the upload folder of the URL) https://www.banque-france.fr/system/files/2023-01/bdf231-6_politiques-economiques.pdf

[^is-cost]: Assemblée nationale, finance committee, report 1838 (15th legislature) by J. Giraud, *rapporteur général*, on the bill creating a digital services tax and amending the CIT-cut trajectory, Apr. 3, 2019 (source of the table: finance committee and DGFiP). https://www.assemblee-nationale.fr/dyn/opendata/RAPPANR5L15B1838.html . Ex-ante alternative: OFCE, *Fiche 6, réforme de l'IS*, July 12, 2017 (7-17 bn EUR by scenario, 15.4 bn central) https://www.ofce.sciences-po.fr/pdf/pbrief/2017/OFCE-Fiche6-Reforme-IS-12-07.pdf
[^lpm-law]: Loi n° 2026-791 du 16 août 2026 actualisant la programmation militaire pour les années 2024 à 2030, JORF n° 191 of Aug. 18, 2026, arts. 1 and 3 (amending arts. 2 and 4 of law 2023-703). Read on Légifrance in a browser 2026-10-25 (pass 2). https://www.legifrance.gouv.fr/jorf/id/JORFSCTA000054694833

---

## Verification log (2026-10-25)

*Adversarial fact-check of this file. Every cited source PDF was re-downloaded fresh into `research/data/raw/08_verify/pdf/`, and Eurostat and OECD series were re-pulled from the APIs into `research/data/raw/08_verify/`. The researcher's extracts were not reused. Recomputed statistics are in `research/data/08_verification_recomputed_2026-10-25.csv`. I recomputed EU-27 and EA-20 means, medians and ranks with rank = 1 + number of countries strictly above France.*

### Confirmed (value, unit, year and source match)

| Claim | Check performed |
|---|---|
| Cour des comptes: 62 bn EUR = 2.2 pts of GDP in 2023; "more than 60 bn"; "non compensées par des économies en dépenses"; PO 45.3% (2017), 45.0% (2022), 43.2% (2023); revenue +24% ASSO / +21% APUL / +4% State | RSPFP July 2024, pp. 35-36, exact wording found |
| OFCE: PO −2.5 pts and deficit +2.4 pts 2017-2024 (3.4% → 5.8%); primary spending excl. investment −0.8 pt of potential GDP; investment +0.5; interest +0.3 | PB 146 key points and Table 4 (caveats added, see below) |
| Rexecode: measures 2018-2023 −0.4/−1.2/+0.2/−0.6/−0.3/−0.3 (sum −2.6); 2024-2026 +0.1/+0.7/+0.4 = +1.2 pts; 36.7 bn EUR (3.0 + 20.9 + 12.9); +12.9 bn in 2026; +2 pts ≈ 65 bn EUR vs 2010 (2.1 pts in the key figures box); 3.5-pt shock 2011-2013; interest 1.9 → 2.5 pts; deficit ≈ 5.4% in 2023 and 2026; 518 / 483 EUR employer cost at 1.15 SMIC | DT 105 synthesis, pp. 5-7, 15-19, and chart table p. 16 |
| Insee IR 78: deficit 152.5 bn EUR = 5.1%; expenditure 1,714.1 bn EUR = 57.2%; PO 43.6% (2025), 42.8% (2024); interest 64.7 bn EUR = 2.2%; investment 131.6 bn EUR (+3.2%); municipalities +7.6%, departments −12.7% | IR 78 text and table |
| Eurostat gov_10a_main (updated Oct. 21, 2026): TE 57.3% (2/27; EA-20 agg. 49.8); TR 52.2% (2/26; EA-20 agg. 46.8); deficit 5.1% (4th worst of 26); GFCF 4.4% (EU agg. 3.9, EA-20 agg. 3.7, DE 3.5; 14/27); net investment 0.6% (23/27); all S1313 rows of table 5.2, incl. means, medians and ranks | Recomputed from a fresh API pull |
| Eurostat gov_10dd_edpt1: S1313 debt 9.3% of GDP, rank 3/27, EU-27 agg. 5.2%, mean 3.9 / median 2.4 | Recomputed |
| France Stratégie committee: IFI 1.29 → 1.83 bn EUR; ISF 4.2 bn in 2017; 3.1 bn loss in 2018; counterfactual loss 4.5 bn ("vraisemblablement supérieur à 4 milliards"); PFU "autofinancée les premières années"; dividends ≈ 23 vs 14 bn EUR; no detectable effect on investment or wages; 380 returns vs 260 departures | Avis du comité, Oct. 2023, pp. 12-19 |
| Bozio-Wasmer: 75 bn EUR = 2.7 pts of GDP (2023); −980,000 FTE; 67 bn static gain; 48 bn EUR net | Report, pp. 67-68 |
| Sénat 211 bn (7 + 41 + 88 + 75) and 108 bn; Clersé 157 / 205 bn (2019); France Stratégie 139-223 bn (2019); minister 150 bn (40 + 30 + 80) | Sénat page r24-808-17 and HCSP 2026 Annex 4 |
| HCSP 2026: perimeter 1 = 82 bn, perimeter 2 = 187 bn, EU State aid ≈ 45 bn EUR (2023) | HCSP report, pp. 27-29 |
| HCSP NA 159: APUL 322 bn EUR, 11 pts of GDP, 19.3% of total public expenditure (local authorities 10.2 pts / 17.8%); +1.5 pts since 1995 (EU +0.4; ASSO +2.9); 53.6% transfers; CNRACL +12 pts, 4.3 bn EUR; I4CE ≈ 11 bn EUR/yr | Note pp. 1-3, Table 1 |
| Cour des comptes, local finances July 2026: −9.3 bn (NA), −11.3 bn (budget, synthesis), +3.2 bn (+1.4%) operating costs, 79.1 bn investment (+2.2%), gross savings 40.2 bn (+7.2%), debt 225.4 bn (+10.0 bn) = 7.5% of GDP, VAT 52.7 bn = 25% of net VAT, DGF 27.4 bn (+150 m EUR), contribution 4.3 bn AE / 1.7 bn CP (2025), 3.5 / 2.4 bn (2026) | Report text |
| Eurostat lfsi_emp_a (updated Sept. 10, 2026): all values, means, medians and ranks in table 6.1 for 15-64, 55-64 and 20-64 (2009 and 2025) | Recomputed |
| OECD 15-64 employment rate: France 68.8% in 2024, rank 29/38, mean 72.1, median 73.0, OECD agg. 70.2; 2025 rank 27/37 (US missing) | Recomputed from a fresh SDMX pull |
| Eurostat nama_10_lp_ulc (updated Oct. 22, 2026): hours per inhabitant 666 (27/27; EU agg. 783; DE 734; NL 821); real hourly productivity 2019-2025 FR −0.8%, EU +3.4%, EA +1.9%, DE +2.2%; 2005-2025 FR +9.0%; PPS productivity 114.6, rank 8/27 (4/27 in 2005) | Recomputed |
| CNP 2026: per-head productivity 0.7 pt below 2019 and ≈ 4 pts below the 2010s trend; Insee hourly ≈ 5 pts below trend; market sector +2.6% above pre-crisis in Q1 2026; 2023 revision from −3.5% to −2.5% | Report, pp. 16-17 |
| Insee Première 2087: TFR 1.56 (metro 1.53; 1.61 in 2024); births 645,000; deaths 651,000; natural balance −6,000; population 69.1 m; life expectancy 85.9 / 80.3 | Insee page |
| Eurostat proj_23ndbi (May 13, 2026): France 35.7 / 45.3 / 52.3; EU-27 34.4 / 45.4 / 54.1. demo_pjanind 2025: France 35.5, rank 8/27, mean 32.8. demo_find 2024: France 1.61, 2/27 (BG 1.72 first) | Recomputed |
| EC 2024 Ageing Report, Table 5: France total 29.9% (highest in the EU; Norway 30.1 is not in the EU), −0.7 pt by 2070; LTC 1.9%, +0.4 by 2045, +0.7 by 2070; panel rows | Table 5 |
| Pisani-Ferry & Mahfouz: 66 bn EUR = 2.3 pts; ≈ 80 bn; −15 bn variant; public share 25-34 bn EUR/yr; debt +10 / +15 / +25 pts | Report, ch. 7 and ch. 10 |
| PLF 2027 PDE table: LPM 51 / 57 (58 revised) / 63 bn EUR. Sénat avis 654: +35.7 bn, 435.7 / 441.6 bn, 44 → 76.3 bn EUR, 0.22 pt (> 7 bn) gap, HCFP 8 bn / 11 bn, interest ≈ 100 bn EUR | Primary texts |
| Insee national balance sheet end-2025: general government non-financial assets 2,945; net financial position −2,195; net worth 750 bn EUR | Insee table 2830290 |
| IPP Note 81: 24.4 bn EUR levy cut; +1.9% average; +0.8% bottom 5%; +3.3% top 1%; −1.1% unemployed | IPP page |
| Cour des comptes, Feb. 2026: PO ratio "*déjà le plus élevé de la zone euro*" | Synthesis text |
| Acteurs publics (Oct. 2, 2024): +100,000 agents (+5.5%) over 2011-2021, no new competence transfers; ≈ −100,000 posts by 2030; 4.1 bn EUR/yr | Article text (still a secondary source) |

### Corrected

| Item | Was | Now | Why |
|---|---|---|---|
| NATO defense spending 2025e | 2.05% of GDP, 61.8 bn EUR; 2024 2.03%; NATO Europe and Canada 2.27%, total 2.76%; panel IT 2.01, NL 2.49, SE 2.51, DK 3.22, DE n/a | 2.04%, 61.0 bn EUR; 2026e 2.22%, 67.6 bn; 2024 2.04%; NATO Europe and Canada 2.31%, total 2.75%; panel 2025e DE 2.22, IT 2.09, NL 2.53, SE 2.85, DK 3.27 | Superseded by NATO's July 7, 2026 release (2014-2026) |
| Gap to 3.5% | 1.45 pts ≈ 43 bn EUR | 1.46 pts ≈ 44 bn EUR (2025 base); ≈ 1.28 pts ≈ 38 bn from 2026e | Follows from the NATO update |
| DG Trésor +38 bn EUR and the 38-84 bn range | "Total public revenue", "from secondary summaries" | Compulsory levies (PO); the range is in the primary note, box 1, p. 9 | Primary text located |
| Cour June 2026 RSPFP | Secondary only; deficit fall "mainly" due to taxes | Primary verified; "exclusively" due to 23 bn EUR of tax increases; 89.6 bn = 3.0 pts confirmed | Primary PDF retrieved |
| 57.2% vs 57.3% divergence | "Revised GDP and spending" | GDP revised to 2,991.1 bn EUR; spending unchanged at 1,714.1 bn | Eurostat MIO_EUR and nama_10_gdp |
| OFCE spending decomposition | −0.8 pt with no caveat; "the whole deterioration is on the revenue side" | Added OFCE's own −0.2 pt subsidy-corrected figure and its 2.1 / 0.6 / 0.3 attribution | Fairness and accuracy: the CICE reclassification inflates both sides |
| OFCE households / firms split | −1.6 / −0.9 | Same, plus a flag that OFCE's Table 3 says −1.7 / −0.8 | Internal inconsistency in the source |
| PO definitions (Rexecode box) | International bodies "count imputed contributions" | DG TAXUD 43.5% excludes imputed contributions and does not deduct credits; Eurostat maximal 45.3% | Rexecode's box |
| APUL EDP debt scope | Included "public hospitals' local entities" | Removed | Hospitals are in ASSO (S1314) |
| Local operating-cost increase | +30.4 bn over 2021-2024 | Over the three years 2022-2024 | Cour chapter wording |
| Bozio-Wasmer net yield ratio | "64% of gross" / "not 75" | 72% of the 67 bn static gain (64% of the 75 bn cost) | The authors' comparison base is 67 bn |
| Sénat report date | July 8, 2025 | Deposited July 1, 2025; presented July 8, 2025 | Sénat page |

### Flagged (not errors, but presentation risks)

- **HCSP "EU average 15.6 pts" for local spending** conflicts with Eurostat S1313 (EU-27 agg. 11.3%, mean 10.5% vs France 11.2%). This probably reflects a scope difference (S1312 state governments); the scope note was added.
- **Cour local-finance report**: budget-account balance −11.3 bn (synthesis) vs −11.6 bn (chapter I conclusion).
- **France Stratégie PFU finding**: the committee itself flags weak robustness and possible delayed effects; a fairness note was added to the steelman.
- **"Tax-timing effect, not new growth"** (PFU dividends) is the researcher's interpretation, now labeled as such.
- **Rexecode** is correctly flagged as business-oriented. **Clersé/IRES** is correctly flagged as union-commissioned. **OFCE** (Sciences Po; often described as left-leaning or Keynesian) is labeled "left-leaning" only in section 12. Fipeco is flagged.

### Left unverified (⚠) (first pass; superseded by "Pass 2" below, where most items were resolved)

- Drees 2017 LTC projections (1.11% → 2.07% of GDP): the URL returns a JavaScript bot-challenge page.
- Law 2026-791 of Aug. 16, 2026 (Légifrance returned 403 to automated access); LPM figures come from the Senate opinion on the bill.
- DGCL local-tax FAQ: **dead link (404)**. No replacement was found because the web-search budget was exhausted.
- Lefebvre Dalloz (CVAE postponement to 2030): 403; not re-checked. The DGE page responds (200) but was not re-read.
- FPT headcount level 2.06 m (only +0.3% and +6,400 are confirmed on the Insee page); the Cour 2024 report itself (only the Acteurs publics article was checked); Cour 2025 edition's 194.5 bn EUR.
- CIT-cut cost (≈ 11 bn EUR) and CICE annual cost (≈ 18-20 bn EUR): from memory, as the researcher already stated.
- Taxe d'habitation cost figures (Sénat 18 bn; Fipeco 23.5 bn), production-tax figures (10 bn; 7.25 bn; CVAE 4.1 / 9.3 bn), CICE job estimates (France Stratégie 2020; Banque de France 2023), the 690 bn EUR end-2024 net-worth vintage, hours per employed person (≈ 1,500 / 1,336 / 1,434): the links respond, but the figures were not re-read line by line.
- No later NATO, Cour or Insee editions were found to supersede the other sources. A broader search for newer editions could not be run because the web-search budget was exhausted.

### Pass 2 (2026-10-25): README §7/§8 follow-up

*Scope: (1) README §8 lists no residual inconsistency for file 08; I nevertheless aligned the remaining non-canonical values with `00-reference-figures.md` (aggregate and year now stated). (2) Every item in README §7, row 08, was re-checked against its primary source. Sites blocked to scripts (Drees, Légifrance) were read in a browser. Downloads are in `research/data/raw/08_pass2/`. The Ifop 86% poll, PISA 2025 and the PLF 2027 staffing plan do not appear in this file, so there were no flags of that kind to remove.*

**Aligned with file 00**

| Location | Was | Now |
|---|---|---|
| §0 group definitions; §1 row 31 | EA-20 only | EA21 canonical aggregate added: TE 49.7%, gap +7.6 pp ≈ 227 bn EUR (2025); EA20 kept as 49.8% / +7.5 pp ≈ 225 bn |
| §3.3 item 1 | "PO ratio fell by 2.5 pts" | Same (OFCE, earlier vintage), plus the canonical −2.6 pts (45.3 → 42.7, Insee May 2026) |
| §3.4 item 1 | "7.5 pts above the euro-area aggregate" | 7.6 pp above EA21 in 2025 (7.5 pp vs EA20) |
| §5.4 | operating costs +30 bn "2021-2024" | +30.4 bn over 2022-2024 (consistent with §5.1) |
| §12 item 2 | 152.5 bn EUR deficit | 151.6 bn EUR (2025, October 2026 EDP vintage) |
| Footnotes insee-apu2025 / cdc2026-rspfp | Interest 64.7 bn; debt 3,460.5 bn | Canonical 65.7 bn (D.41) and 3,460.1 bn noted |
| §13 | HCFP opinion on the PLF 2027 "not retrieved" | Points to HCFP-2026-5 (Sept. 25, 2026), as in file 00 |

**README §7 items: outcome**

| Item | Outcome | Primary source |
|---|---|---|
| Drees 2017 LTC projection 1.11% → 2.07% of GDP | **Confirmed** (23.7 bn EUR in 2014; total 1.40% → 2.78%). The old PDF URL now redirects to an unrelated page and was replaced | Drees ER 1032, Oct. 12, 2017 (browser) |
| Law 2026-791 of Aug. 16, 2026 | **Confirmed, with one correction:** 435.7 bn EUR total confirmed; new resources 36 bn (law) vs 35.7 (bill); **2030 credits 75.7 bn EUR, not 76.3**; annual path 57.1 / 63.3 / 69.5 / 72.6 / 75.7; target 2.5% of GDP in 2030, 3.5% in 2035. The 441.6 bn EUR incl. extra-budgetary resources was not found in art. 3 (Senate figure kept) | Légifrance, JORF Aug. 18, 2026, arts. 1 and 3 (browser) |
| DGCL local-tax FAQ (dead link) | **Replaced** by the Senate *rapport général* 163 (2021-2022), vol. III, annex 27 (compensation mechanics, 22.8 bn EUR of VAT) | senat.fr |
| *Taxe d'habitation* cost (Senate ≈ 18 bn, 10.2 / 7.8; Fipeco 23.5 bn) | **Confirmed** in both primaries. Fipeco's 23.5 bn is a 2018 projection for 2020 | senat.fr; fipeco.fr |
| CVAE postponement to 2030 | **Confirmed:** LFI 2025 art. 62 (law 2025-127); 0.28% top rate in 2026-2027, 0.09% in 2029. The LFI 2026 did not bring the end forward | Légifrance, CGI art. 1586 *quater* (browser) |
| Production-tax cut (10 bn; 7.25 bn CVAE) | **Confirmed, clarified:** 7.25 bn = regions' CVAE share; plus TFPB 1.54 bn and CFE 1.75 bn; 2023 CVAE cut 4.1 / 9.3 bn confirmed (DGE, Oct. 3, 2022) | DGE; Banque des Territoires |
| FPT headcount 2.06 m | **Corrected to 2.04 m** (2,039,400 incl. subsidized contracts, end-2024) | Insee Première 2094, figure 1 |
| Cour 2024 report on +100,000 local agents | **Confirmed in primary** (1.94 m at end-2021; +100,000 / +5.5% over 2011-2021; 4.1 bn EUR/yr from 2030) | Cour des comptes, Oct. 2, 2024, PDF pp. 63, 76 |
| Cour "2025 edition" 194.5 bn EUR local debt | **Corrected attribution:** 194.5 bn (end-2024) and 203.3 bn (end-2025) are in annex 1 of the **July 2026** report, excluding *syndicats* | Cour, July 2026, PDF pp. 179-180 (ratio check: 203.3 / 40.2 = 5.1 years, as printed) |
| CIT-cut cost ≈ 11 bn (from memory) | **Sourced:** "of the order of 11 bn EUR" (ex-ante, static) | AN report 1838, Apr. 3, 2019 |
| CICE cost 18-20 bn/yr (from memory) | **Corrected:** ≈ 18 bn EUR in 2016; ≈ 68 bn EUR cumulated 2014-2018 | France Stratégie, Sept. 2020, PDF pp. 8, 55 |
| CICE job estimates | **Confirmed** (100,000 micro; 160,000 macro after financing). BdF 240,000 = end-2015 to end-2019 (260,000 from end-2012); **bulletin date corrected to Sept.-Oct. 2020** | France Stratégie press release and report; BdF Bulletin 231/6 |
| 690 bn EUR net worth, end-2024 | **Confirmed** (−234 bn in 2023, −50 bn in 2024) | Insee Première 2081, Nov. 6, 2025 |
| Hours per employed person | **Confirmed and sourced directly:** FR 1,499.9; DE 1,336.4; NL 1,433.8; **EU-27 1,604.8 (France below)** (2025) | Eurostat nama_10_lp_ulc HW_EMP (Oct. 22, 2026) |
| PLF 2027 local contribution "5.5 bn" (press) | **Corrected / partly verified:** CPEB 2.5 bn + FCTVA −2.1 bn in the PLF text; government total ≈ 5.4 bn via Banque des Territoires only | PLF 2027 |
| Rexecode "−66 bn EUR current" (secondary) | **Removed:** not in DT 105 | Rexecode DT 105 |

**Still unverified (⚠) after pass 2**

| Item | Why | Recommendation |
|---|---|---|
| "Public net worth fell sharply since 2008" | No long Insee series retrieved; series breaks between bases 2014 and 2020 | Drop from site; use the verified 2023-2024 falls |
| LPM 441.6 bn EUR incl. extra-budgetary resources | Not in the law's art. 3; only in the Senate opinion on the bill | Keep with caveat ("Senate, on the bill"), or quote only the 435.7 bn in the law |
| PLF 2027 local effort total ≈ 5.4 bn EUR | Government CFL presentation known only via the press | Keep with caveat; prefer the two primary components (2.5 + 2.1 bn EUR) |
| FPT 1998-2008 ≈ +350,000 (Cour, 2012) | Still via a 2012 press article | Keep with caveat or drop |
| HCSP "EU average 15.6 pts" of local spending (divergence flag) | Scope in the HCSP online annexes (not opened); conflicts with Eurostat S1313 | Replace with Eurostat S1313 (EU-27 aggregate 11.3%, France 11.2%, 2025) on the site |
