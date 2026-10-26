# 01 - French Public Spending: Total and Breakdown by Function and Subsector, 1995-2025

*Research file for the public-finance education platform. Prepared 2026-10-25. All web sources accessed 2026-10-25.*

> **How to read this file.** Every figure states its unit. **"% of GDP"** means the item divided by nominal GDP. **"% of TE"** means the item as a share of total general government expenditure (TE). These two are never interchangeable. Figures marked **[computed]** were calculated by the author of this file from official raw data. The raw data, the derived CSVs and the scripts are listed in Section 11.

---

## 0. Summary for the editorial team (10 lines)

1. In 2025, French general government (*administrations publiques*, APU) spent **EUR 1,714.1 bn = 57.3% of GDP** (Eurostat, October 2026 EDP-consistent release; Insee May 2026 gives EUR 1,714.2 bn). Revenue was 52.2% of GDP and the deficit was 5.1% of GDP (EUR 151.6 bn, October 2026 EDP notification; Insee's May 2026 vintage gave 152.5 bn) (corrected 2026-10-25: was "EUR 151.6-152.5 bn"). The user's starting figures (57.3%, 43.6% for *prélèvements obligatoires*, 31.9% for Drees social benefits in 2024) are **confirmed** by the sources.
2. That works out to **about EUR 24,800 per inhabitant** [computed]. Roughly **1 euro in 11 of public spending (8.8%)** was financed by borrowing in 2025 [computed].
3. **Social protection plus health accounts for 57% of TE** (COFOG 2024: 41.5% + 15.6%). **Old-age pensions alone account for 23.4% of TE** (COFOG "old age"). The COR's broader pension concept gives 24.3% of TE and 14.1% of GDP in 2025.
4. France ranks **2nd of 27 in the EU** for TE/GDP in 2024 and 2025, just behind Finland. On the October 2026 Eurostat vintage it ranked 1st in 2005 and in every year from 2014 to 2023 (2023: 56.8% vs Finland 56.1%) *(Reconciled 2026-10-25, see `00-reference-figures.md`.)*. It is also 2nd in the OECD (32 countries with data, 2024) [computed].
5. In 2024, France's TE was **7.8 pp of GDP above the euro-area (EA21) GDP-weighted aggregate** (57.0% vs 49.2%, gov_10a_main; EA20: 7.7 pp) [computed]. That is roughly **EUR 229 bn**. In 2025 the gap was **7.6 pp vs EA21, about EUR 227 bn** (EA20, used in Eurostat's 2025 news release: 7.5 pp, about EUR 225 bn) *(Reconciled 2026-10-25, see `00-reference-figures.md`.)*. **Social protection explains 46% of the gap, health 19%, old-age pensions 32% (29% net of survivors' pensions), housing and community amenities 9%, and defense, education and economic affairs about 6% each** [computed]. The often-quoted claim that "pensions explain about half the gap" is **not supported** by COFOG data. What is supported is that **pensions plus health explain about half**.
6. Measured **per capita in purchasing power standards (PPS)**, France is **not an outlier**. It ranks **8th of 27** in 2025 and 8th or 9th in 2024 depending on the PPP vintage (2025: **23,330 PPS per inhabitant**, TE/GDP x GDP per capita in PPS from nama_10_pc, Oct 2026), below Luxembourg, Austria, Belgium, Denmark, the Netherlands, Germany and Finland, and statistically tied with Sweden (2024: 22,398 vs 22,386). The PLI-based method of §6.4 (current `prc_ppp_ind_1` vintage) gives 22,383-22,395 PPS and 9th place in 2024 (22,321 on the superseded July 2025 vintage) [computed] *(Reconciled 2026-10-25, see `00-reference-figures.md`.)*. France's high spending/GDP ratio partly reflects a GDP per capita that is lower than in these countries. This is the strongest single counter-argument to the platform's thesis, and the platform must address it.
7. OECD SOCX shows that once private mandatory and voluntary social spending and the tax treatment of benefits are taken into account (**net total social expenditure**), the **United States (33.2% of GDP) exceeds France (32.0%; raw value 31.95)** in 2021 (corrected after verification: was 31.9%, a truncation of 31.95). In 2019, France was 30.1% and the US 29.2%. Total social effort is similar. What differs is whether it is financed through compulsory levies.
8. In France's 2025 spending mix (corrected after verification: was "2024"; the figures quoted are 2025 values. The 2024 values are 12.4% vs 9.9% and 19.2% vs 16.7%), **compensation of employees (12.4% of GDP vs 10.0% in the euro area)** and **cash social benefits (19.4% vs 16.9%)** explain most of the gap by economic nature. **Intermediate consumption is *below* the euro-area average** (5.5% vs 5.9% of GDP).
9. From 1995 to 2024, old-age pensions (+2.35 pp of GDP) and health (+2.0 pp) rose by about 4.4 pp of GDP. Falling interest (-1.6 pp), defense (-0.65), education (-0.74) and economic affairs (-0.74) largely offset the rise, so TE/GDP rose only about 0.9 pp over the period [computed from COFOG].
10. Government plans (PLF 2027 filed 1 Oct 2026; HCFP opinion HCFP-2026-5 dated 25 Sep 2026, published with the PLF) put spending excluding tax credits at **56.6% of GDP (2025) → 57.1% (2026) → 56.9% (2027)**. General-government interest charges (national accounts) are projected to rise from **EUR 65.7 bn (2025; HCFP rounds to 66) to 79.2 bn (2026) and about 91 bn (2027)** (corrected 2026-10-25: was "EUR 66 bn to 79 bn to 91 bn"; aligned with `00-reference-figures.md` rows 39-40). On the HCFP's estimate, the 2027 structural effort is **mostly on the revenue side** (EUR 17 bn of revenue vs EUR 11 bn of spending).

---

## 1. Scope and definitions

| Term | Definition | Note |
|---|---|---|
| *Administrations publiques* (APU, general government, ESA code S13) | The State, *organismes divers d'administration centrale* (ODAC, central agencies), *administrations publiques locales* (APUL, local governments) and *administrations de sécurité sociale* (ASSO, social-security funds, including the compulsory supplementary pension scheme Agirc-Arrco and unemployment insurance Unédic) | Units are classified by ESA 2010 rules: non-market, controlled by government. Eurostat polices the boundary. |
| *Dépenses publiques* (total expenditure, TE) | The sum of ESA 2010 expenditure transactions (P2, P5, D1, D3, D4, D5, D62, D632, D7, D8, D9, NP), **consolidated** for flows between subsectors | Non-financial account only. Loans and equity injections at market value are financial transactions and are excluded (e.g., the 2022 EDF nationalization was recorded as financial; [Insee blog, Oct 2025][insee-blog]). |
| *Dépenses hors crédits d'impôt* (spending excluding tax credits) | TE minus refundable tax credits, which ESA records as spending | Concept used by the government and the HCFP. It has been a target indicator in programming law at least since the *loi de programmation des finances publiques* (LPFP, public-finance programming law) 2018-2022 (law no. 2018-32 of 22 Jan 2018, art. 5: "*Dépense publique, hors crédits d'impôts*", 54.7% of GDP in 2017 → 51.1% in 2022 target) ([Légifrance](https://www.legifrance.gouv.fr/loda/id/JORFTEXT000036526027)) (corrected 2026-10-25: was "since about 2023", previously flagged as unverified). 2025: 56.6% of GDP vs 57.3% of GDP for total TE (about EUR 20 bn of tax credits). |
| COFOG | UN Classification of the Functions of Government: 10 divisions (GF01-GF10) and 69 groups | Allocation conventions differ by country. For example, debt interest is in GF01 and imputed pension contributions of civil servants are allocated to each function. |
| *Prélèvements obligatoires* (PO, compulsory levies) | Taxes plus actual social contributions, net of tax credits (Insee definition) | 43.6% of GDP in 2025 (Insee). The Eurostat concept is higher. **Canonical 2024 value: 42.7% (Insee, May 2026 accounts)**; the 42.8% figure is the earlier (Oct 2025-Mar 2026) vintage, quoted by the [Insee blog][insee-blog] against Eurostat's 45.2%. *(Reconciled 2026-10-25, see `00-reference-figures.md`.)* |
| % of GDP vs % of TE | % of GDP compares an item to the size of the economy (the tax base). % of TE shows priorities *within* the budget | TE/GDP is **not** "the share of GDP spent by the State". Transfers (pensions, benefits) are not GDP components, so the ratio could theoretically exceed 100%. |
| PPS | Purchasing power standard (EU27 = 1). PPS per capita = EUR value / price level index (PLI) / population | Used to compare real volumes per inhabitant. |

Accounting bases: everything below is **national accounts (ESA 2010, base 2020)** unless stated otherwise. It is **not** State budget accounting (*comptabilité budgétaire*, e.g., the EUR 502 bn *périmètre des dépenses de l'État*), which covers only the State, on a cash/credit basis.

---

## 2. Key figures

| # | Indicator | Value | Unit | Data year | Source (publication date) | Src |
|---|---|---|---|---|---|---|
| K1 | General government total expenditure (TE) | 1,714.1 | EUR bn | 2025 | Eurostat gov_10a_main (updated 2026-10-21) | [^es-main] |
| K2 | TE | 57.3 | % of GDP | 2025 | Eurostat gov_10a_main; Insee IP 2106 (May 2026) | [^es-main] [^ip2106] |
| K3 | Total revenue | 1,562.5 (Eurostat) / 1,561.7 (Insee) | EUR bn | 2025 | Eurostat; Insee IP 2106 | [^es-main] [^ip2106] |
| K4 | Total revenue | 52.2 | % of GDP | 2025 | Insee IP 2106 | [^ip2106] |
| K5 | Deficit (net borrowing, B9) | -151.6 (Eurostat, Oct 2026) / -152.5 (Insee, May 2026) | EUR bn | 2025 | Eurostat; Insee | [^es-main] [^ip2106] |
| K6 | Deficit | -5.1 | % of GDP | 2025 | Insee IP 2106 | [^ip2106] |
| K7 | *Prélèvements obligatoires* (net of tax credits) | 43.6 | % of GDP | 2025 | Insee IP 2106 | [^ip2106] |
| K8 | Maastricht gross debt | 115.7 (EUR 3,460.1 bn, Insee Aug 2026 / Eurostat Oct 2026 EDP notification; May 2026 vintage: 3,460.5) | % of GDP | end-2025 | Insee; Eurostat gov_10dd_edpt1 | [^ip2106] [^es-main] |
| K9 | TE per inhabitant | ≈24,800 | EUR per capita | 2025 | [computed] K1 / Eurostat population (68.998 m) | [^es-main] [^es-pop] |
| K10 | Social protection (COFOG GF10, excl. health) | 693.0; 23.6% of GDP; **41.5% of TE** | EUR bn / % | 2024 | Eurostat gov_10a_exp; Insee IP 2093 (Feb 2026) | [^es-cofog] [^ip2093] |
| K11 | Old age (COFOG GF1002) | 392.0; 13.35% of GDP; **23.4% of TE** | EUR bn / % | 2024 | Eurostat gov_10a_exp | [^es-cofog] |
| K12 | Pension spending, all legally compulsory schemes incl. FSV, excl. RAFP (COR concept) | 422.2; **14.1% of GDP; 24.3% of public spending** (COR's own ratio, Figure 2.1, numerator excl. financial charges) | EUR bn / % | 2025 | COR annual report (June 2026), Part 2 ch. 2, pp. 65-66 | [^cor] |
| K13 | Health (COFOG GF07) | 261.2; 8.9% of GDP; **15.6% of TE** | EUR bn / % | 2024 | Eurostat; Insee IP 2093 | [^es-cofog] [^ip2093] |
| K14 | Education (COFOG GF09) | 148.6; 5.1% of GDP; **8.9% of TE** | EUR bn / % | 2024 | Eurostat; Insee IP 2093 | [^es-cofog] [^ip2093] |
| K15 | Defense (COFOG GF02) | 54.2; 1.85% of GDP (website: **1.8%**, per `00-reference-figures.md` row 15); **3.2% of TE** | EUR bn / % | 2024 | Eurostat; Insee IP 2093 | [^es-cofog] [^ip2093] |
| K16 | Interest (ESA D41 paid) | 65.7; 2.2% of GDP; 3.8% of TE | EUR bn / % | 2025 | Eurostat gov_10a_main | [^es-main] |
| K17 | Social benefits in cash and in kind (D62 + D632) | 771.0; 25.8% of GDP; 45.0% of TE | EUR bn / % | 2025 | Insee IP 2106; Eurostat | [^ip2106] [^es-main] |
| K18 | Social protection benefits | France 31.9 (Drees CPS concept); EU27 **27.4** (Eurostat ESSPROS `spr_exp_func`, 27.41, updated 23 Oct 2026; France 31.96 and Finland 32.46 on the same table). Drees' own EU27 benchmark, 27.3, is an earlier ESSPROS vintage and is not used on the website (corrected 2026-10-25: was "EU27: 27.3" with no source stated) | % of GDP | 2024 | Drees, *La protection sociale en France et en Europe en 2024* (Dec 2025); Eurostat `spr_exp_func` | [^drees] [^es-spr] |
| K19 | Compensation of employees (D1) | 370.0; 12.4% of GDP; 21.6% of TE | EUR bn / % | 2025 | Eurostat; Insee | [^es-main] [^ip2106] |
| K20 | France's rank, TE/GDP, EU27 | 2nd of 27 (Finland 57.5%) | rank | 2025 | [computed] Eurostat | [^es-main] |
| K21 | Gap France vs euro area (**EA21** GDP-weighted aggregate, canonical), TE/GDP | **+7.6 (57.3 vs 49.7) ≈ EUR 227 bn** [EA20, used in Eurostat's 2025 news release: +7.5, ≈ EUR 225 bn] (corrected 2026-10-25: was "+7.5 vs EA20", unlabeled as non-canonical) | pp of GDP | 2025 | [computed] Eurostat gov_10a_main; `00-reference-figures.md` row 7 | [^es-main] |
| K22 | TE per capita, PPS | **23,330 PPS, 8th of 27** (2025; TE/GDP x GDP per capita in PPS, `nama_10_pc` Oct 2026). 2024: 22,398, 8th (same method); 22,395, 9th on the new PLI table `prc_ppp_ind_1`: a statistical tie with Sweden (22,386-22,399) (corrected 2026-10-25: was "22,321 (EU27 unweighted mean 18,735); rank 9/27, 2024", based on the superseded July 2025 PLI vintage) | PPS per capita | 2025 (2024) | [computed] Eurostat; `00-reference-figures.md` row 5 | [^es-main] [^es-pc] [^es-pli] |
| K23 | Spending excl. tax credits: 2025 → 2026 (forecast) → 2027 (PLF) | 56.6 → 57.1 → 56.9 (EUR 1,694 → 1,742 → 1,782 bn) | % of GDP | 2025-2027 | HCFP opinion HCFP-2026-5 (dated 25 Sep 2026, published with the PLF on 1 Oct 2026) | [^hcfp] |

---

## 3. Total general government expenditure, revenue and balance, 1995-2025

### 3.1 Annual series (ESA 2010, consolidated general government)

The table shows EUR bn (current prices) and % of GDP. "Primary" means excluding interest (D41). The EA20 and EU27 columns are Eurostat GDP-weighted aggregates. The gap is France minus EA20, in pp of GDP. **This historical table uses EA20; the canonical website aggregate is EA21** (2025: +7.6 pp ≈ EUR 227 bn; 2024: +7.8 pp ≈ EUR 229 bn; `00-reference-figures.md` rows 7-8, 10). Do not quote the EA20 column on the website without saying so. Source for every row: Eurostat gov_10a_main (extracted 2026-10-25, dataset updated 2026-10-21), sector S13 [^es-main]. Derived file: `data/01_derived_fr_series_1995_2025.csv`.

| Year | TE (EUR bn) | TE (% GDP) | Revenue (EUR bn) | Revenue (% GDP) | Balance (EUR bn) | Balance (% GDP) | Interest (% GDP) | Primary TE (% GDP) | EA20 TE (% GDP) | EU27 TE (% GDP) | Gap vs EA20 (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| 1995 | 684.0 | 56.1 | 621.6 | 50.9 | -62.4 | -5.1 | 3.5 | 52.6 | 53.3* | 53.5* | 2.8* | [^es-main] |
| 1996 | 705.7 | 56.0 | 656.6 | 52.1 | -49.1 | -3.9 | 3.6 | 52.4 | 50.7 | 51.1 | 5.3 | [^es-main] |
| 1997 | 710.9 | 55.6 | 663.4 | 51.9 | -47.5 | -3.7 | 3.6 | 52.0 | 49.5 | 49.7 | 6.1 | [^es-main] |
| 1998 | 722.1 | 54.0 | 690.1 | 51.6 | -32.0 | -2.4 | 3.4 | 50.6 | 48.6 | 48.8 | 5.4 | [^es-main] |
| 1999 | 748.6 | 53.7 | 727.0 | 52.1 | -21.5 | -1.5 | 3.1 | 50.6 | 48.1 | 48.4 | 5.6 | [^es-main] |
| 2000 | 775.3 | 52.6 | 756.0 | 51.3 | -19.3 | -1.3 | 3.0 | 49.6 | 47.3 | 47.4 | 5.3 | [^es-main] |
| 2001 | 808.2 | 52.8 | 786.5 | 51.4 | -21.7 | -1.4 | 3.1 | 49.7 | 47.3 | 47.4 | 5.5 | [^es-main] |
| 2002 | 851.1 | 53.9 | 801.0 | 50.7 | -50.1 | -3.2 | 3.0 | 50.9 | 47.6 | 47.8 | 6.3 | [^es-main] |
| 2003 | 881.8 | 54.4 | 815.5 | 50.3 | -66.3 | -4.1 | 2.9 | 51.5 | 47.9 | 48.1 | 6.5 | [^es-main] |
| 2004 | 915.9 | 54.0 | 855.6 | 50.4 | -60.3 | -3.6 | 2.8 | 51.2 | 47.4 | 47.4 | 6.6 | [^es-main] |
| 2005 | 956.1 | 54.3 | 894.3 | 50.8 | -61.8 | -3.5 | 2.7 | 51.6 | 47.2 | 47.2 | 7.1 | [^es-main] |
| 2006 | 992.2 | 53.8 | 943.2 | 51.1 | -49.1 | -2.7 | 2.6 | 51.2 | 46.6 | 46.6 | 7.2 | [^es-main] |
| 2007 | 1,039.3 | 53.6 | 981.4 | 50.6 | -57.9 | -3.0 | 2.7 | 50.9 | 45.9 | 45.8 | 7.7 | [^es-main] |
| 2008 | 1,080.2 | 54.3 | 1,010.5 | 50.8 | -69.7 | -3.5 | 2.9 | 51.4 | 47.1 | 47.0 | 7.2 | [^es-main] |
| 2009 | 1,122.6 | 58.0 | 979.8 | 50.6 | -142.8 | -7.4 | 2.5 | 55.5 | 51.2 | 50.9 | 6.8 | [^es-main] |
| 2010 | 1,152.0 | 57.7 | 1,009.2 | 50.6 | -142.8 | -7.2 | 2.5 | 55.2 | 51.1 | 50.7 | 6.6 | [^es-main] |
| 2011 | 1,175.7 | 57.0 | 1,066.3 | 51.7 | -109.4 | -5.3 | 2.7 | 54.3 | 49.6 | 49.3 | 7.4 | [^es-main] |
| 2012 | 1,209.0 | 57.9 | 1,101.0 | 52.7 | -108.0 | -5.2 | 2.6 | 55.3 | 50.3 | 50.0 | 7.6 | [^es-main] |
| 2013 | 1,242.4 | 58.6 | 1,137.6 | 53.7 | -104.7 | -4.9 | 2.3 | 56.3 | 50.3 | 50.0 | 8.3 | [^es-main] |
| 2014 | 1,257.6 | 58.4 | 1,159.1 | 53.8 | -98.5 | -4.6 | 2.2 | 56.2 | 49.6 | 49.3 | 8.8 | [^es-main] |
| 2015 | 1,268.0 | 57.6 | 1,182.3 | 53.7 | -85.7 | -3.9 | 2.0 | 55.6 | 48.6 | 48.3 | 9.0 | [^es-main] |
| 2016 | 1,280.6 | 57.4 | 1,196.6 | 53.6 | -84.0 | -3.8 | 1.9 | 55.5 | 47.9 | 47.5 | 9.5 | [^es-main] |
| 2017 | 1,321.4 | 57.7 | 1,244.4 | 54.3 | -77.1 | -3.4 | 1.8 | 55.9 | 47.4 | 46.9 | 10.3** | [^es-main] |
| 2018 | 1,327.6 | 56.4 | 1,273.0 | 54.0 | -54.6 | -2.3 | 1.8 | 54.6 | 47.0 | 46.6 | 9.4 | [^es-main] |
| 2019 | 1,346.2 | 55.3 | 1,287.9 | 53.0 | -58.2 | -2.4 | 1.5 | 53.8 | 47.0 | 46.6 | 8.3 | [^es-main] |
| 2020 | 1,430.4 | 61.7 | 1,223.3 | 52.8 | -207.1 | -8.9 | 1.3 | 60.4 | 53.5 | 52.8 | 8.2 | [^es-main] |
| 2021 | 1,491.4 | 59.5 | 1,326.2 | 52.9 | -165.1 | -6.6 | 1.4 | 58.1 | 51.9 | 51.1 | 7.6 | [^es-main] |
| 2022 | 1,550.3 | 58.4 | 1,424.4 | 53.7 | -125.9 | -4.7 | 1.9 | 56.5 | 49.8 | 49.1 | 8.6 | [^es-main] |
| 2023 | 1,608.3 | 56.8 | 1,456.4 | 51.4 | -151.9 | -5.4 | 1.9 | 54.9 | 49.2 | 48.8 | 7.6 | [^es-main] |
| 2024 | 1,672.7 | 57.0 | 1,503.6 | 51.2 | -169.1 | -5.8 | 2.0 | 55.0 | 49.3 | 48.9 | 7.7 | [^es-main] |
| 2025 | 1,714.1 | 57.3 | 1,562.5 | 52.2 | -151.6 | -5.1 | 2.2 | 55.1 | 49.8 | 49.4 | 7.5 | [^es-main] |

\* The 1995 euro-area and EU figures are inflated by a one-off in Germany: the federal government took over the debts of the *Treuhandanstalt*, which was recorded as a capital transfer (German TE/GDP was 55.2% in 1995 vs 49.6% in 1996 in the same dataset). Use 1996-2000 as the late-1990s benchmark, not 1995.
\** The 2017 French figure includes the CICE tax credit, recorded as a subsidy (spending). Insee estimates the France-EU gap at 10.7 pp in 2017, or 9.7 pp if the CICE is treated as reduced revenue, as its 2019 replacement (cuts in contributions) was [^insee-blog].

**Key observations**

- **Nominal TE multiplied by 2.5 between 1995 (EUR 684 bn) and 2025 (EUR 1,714 bn)** [computed]. As a share of GDP, TE fell from 56.1% to 52.6% (2000), then rose in steps with each crisis: 2009 (58.0%), 2013 peak (58.6%), Covid 2020 (61.7%). It never returned to its pre-crisis level. The ratio stood at 57.3% in 2025.
- France's gap with the euro area widened from about **5.3 pp in 2000 to 7.1 pp in 2005, about 9-10 pp in 2015-2017, and 7.5-7.7 pp in 2024-2025**. It narrowed after 2017 partly because of the CICE reclassification (see \** above).
- The 2025 deficit fell from 5.8% to 5.1% of GDP. Insee and the Cour des comptes attribute the improvement **mainly to revenue increases (about EUR 23 bn of new measures)**. Spending grew by +2.5%, faster than nominal GDP (+2.0%) [^ip2106] [^ccomptes].
- **Interest**: interest charges fell from 3.5% of GDP (1995) to 1.3% (2020) despite rising debt. They have been rising again since 2022 and reached 2.2% in 2025. The HCFP expects 2.6% in 2026 and 2.9% in 2027 [^hcfp].

### 3.2 Short-term outlook (official forecasts, autumn 2026)

| Indicator | 2025 (outturn) | 2026 (forecast) | 2027 (PLF) | Unit | Source | Src |
|---|---|---|---|---|---|---|
| Public spending excl. tax credits | 1,694 | 1,742 | 1,782 | EUR bn | HCFP opinion 2026-5, Table 10 | [^hcfp] |
| Public spending excl. tax credits | 56.6 | 57.1 | 56.9 | % of GDP | HCFP opinion 2026-5, §80, §86 | [^hcfp] |
| Spending growth, value / volume (GDP deflator) | +2.5 / +1.4 | +2.8 / +1.3 | +2.3 / +0.6 | % | HCFP Tables 8-9 | [^hcfp] |
| Interest charges, all general government | 66 | 79 | 91 | EUR bn | HCFP Table 10 | [^hcfp] |
| Pensions (social-security field) | 346 | 354 | 363 | EUR bn | HCFP Table 10 | [^hcfp] |
| Military programming law (LPM) | 51 | 57 | 63 | EUR bn | HCFP Table 10 | [^hcfp] |
| Health (*Ondam*) | 265 | 273 | 279 | EUR bn | HCFP Table 10 | [^hcfp] |
| Balance | -5.1 | -5.4 | -5.0 | % of GDP | HCFP Table 12 | [^hcfp] |
| Debt | 115.7 | ≈119.3 | 121.7 | % of GDP | HCFP; Insee | [^hcfp] [^ip2106] |
| Structural effort 2027: revenue / spending | - | - | 17 / 11 (0.5 / 0.4 pp) | EUR bn (pp of potential GDP) | HCFP §96, §98 | [^hcfp] |

The HCFP notes that interest charges account for 28% (2026) and 30% (2027) of the increase in total spending [^hcfp].

---

## 4. Breakdown by function (COFOG)

### 4.1 Latest year available: 2024

COFOG data for 2025 had not been published by 2026-10-25. Insee lists its 2025 tables 3.301-3.307 as "to be published in December 2026" [^insee-cofog25]. Eurostat's 2025 COFOG release normally follows around February 2027.

The table below is in EUR bn, % of TE (Eurostat PC_TOT) and % of GDP. The 2024 % of GDP is **recomputed with current GDP** (EUR 2,935.2 bn), which reproduces Insee's 57.0%. Eurostat's published COFOG PC_GDP for 2024 gives 57.3%, apparently based on an older GDP vintage (see §9). Historical columns use Eurostat published PC_GDP. Source for every row: Eurostat gov_10a_exp, sector S13, TE (2024 provisional, flag "p") [^es-cofog]. Insee publishes the same data in its Insee Résultats tables [^insee-cofog24].

| COFOG | Function | 2024 EUR bn | 2024 % of TE | 2024 % of GDP | 1995 % GDP | 2005 % GDP | 2015 % GDP | 2019 % GDP | Change 1995→2024 (pp GDP) | Src |
|---|---|---|---|---|---|---|---|---|---|---|
| TOTAL | Total expenditure | 1,671.8 | 100.0 | 56.96 | 56.1 | 54.3 | 57.6 | 55.3 | +0.9 | [^es-cofog] |
| GF01 | General public services | 181.1 | 10.8 | 6.17 | 8.3 | 7.4 | 6.6 | 6.0 | -2.1 | [^es-cofog] |
| GF0107 | of which public debt transactions (interest) | 58.9 | 3.5 | 2.01 | 3.6 | 2.8 | 2.2 | 1.6 | -1.6 | [^es-cofog] |
| GF02 | Defense | 54.2 | 3.2 | 1.85 | 2.5 | 1.8 | 1.7 | 1.7 | -0.65 | [^es-cofog] |
| GF03 | Public order and safety | 52.1 | 3.1 | 1.78 | 1.5 | 1.5 | 1.6 | 1.7 | +0.3 | [^es-cofog] |
| GF04 | Economic affairs | 166.1 | 9.9 | 5.66 | 6.4 | 5.2 | 6.2 | 5.3 | -0.74 | [^es-cofog] |
| GF0401 | of which general economic, commercial and labor affairs (incl. many business subsidies and employment aid) | 45.3 | 2.7 | 1.54 | 1.3 | 0.9 | 2.0 | 1.1 | +0.2 | [^es-cofog] |
| GF0405 | of which transport | 60.7 | 3.6 | 2.07 | 2.9 | 2.3 | 2.3 | 2.4 | -0.8 | [^es-cofog] |
| GF05 | Environmental protection | 30.3 | 1.8 | 1.03 | 0.6 | 0.8 | 0.9 | 0.9 | +0.4 | [^es-cofog] |
| GF06 | Housing and community amenities | 42.1 | 2.5 | 1.44† | 1.1 | 1.1 | 1.2 | 1.1 | +0.3† | [^es-cofog] [^ip2093] |
| GF07 | Health | 261.2 | 15.6 | 8.90 | 6.9 | 7.8 | 8.2 | 8.1 | +2.0 | [^es-cofog] |
| GF0701 | of which medical products | 43.7 | 2.6 | 1.49 | 0.9 | 1.3 | 1.5 | 1.4 | +0.6 | [^es-cofog] |
| GF0702 | of which outpatient services | 91.8 | 5.5 | 3.13 | 2.4 | 2.7 | 2.9 | 3.0 | +0.7 | [^es-cofog] |
| GF0703 | of which hospital services | 109.3 | 6.5 | 3.72 | 3.3 | 3.4 | 3.4 | 3.3 | +0.4 | [^es-cofog] |
| GF08 | Recreation, culture and religion | 43.1 | 2.6 | 1.47 | 1.1 | 1.5 | 1.5 | 1.5 | +0.4 | [^es-cofog] |
| GF09 | Education | 148.6 | 8.9 | 5.06 | 5.8 | 5.5 | 5.3 | 5.0 | -0.74 | [^es-cofog] |
| GF0901 | of which pre-primary and primary | 42.2 | 2.5 | 1.44 | 1.5 | 1.4 | 1.4 | 1.4 | -0.1 | [^es-cofog] |
| GF0902 | of which secondary | 63.8 | 3.8 | 2.17 | 2.7 | 2.5 | 2.4 | 2.2 | -0.5 | [^es-cofog] |
| GF0904 | of which tertiary | 12.3 | 0.7 | 0.42 | 0.6 | 0.5 | 0.5 | 0.5 | -0.2 | [^es-cofog] |
| GF10 | Social protection (excl. health) | 693.0 | 41.5 | 23.61 | 22.0 | 21.7 | 24.3 | 23.9 | +1.6 | [^es-cofog] |
| GF1001 | of which sickness and disability (cash: daily allowances, disability pensions, AAH) | 83.9 | 5.0 | 2.86 | 2.9 | 2.5 | 2.7 | 2.8 | 0.0 | [^es-cofog] |
| GF1002 | of which old age (pensions, elderly care) | 392.0 | 23.4 | 13.35 | 11.0 | 11.4 | 13.5 | 13.4 | +2.35 | [^es-cofog] |
| GF1003 | of which survivors | 40.6 | 2.4 | 1.38 | 1.7 | 1.5 | 1.6 | 1.5 | -0.3 | [^es-cofog] |
| GF1004 | of which family and children | 66.7 | 4.0 | 2.27 | 2.7 | 2.4 | 2.5 | 2.3 | -0.4 | [^es-cofog] |
| GF1005 | of which unemployment | 48.5 | 2.9 | 1.65 | 1.8 | 1.9 | 1.9 | 1.8 | -0.15 | [^es-cofog] |
| GF1006 | of which housing (personal housing benefits, APL) | 21.1 | 1.3 | 0.72 | 0.8 | 1.0 | 0.9 | 0.8 | -0.1 | [^es-cofog] |
| GF1007 | of which social exclusion n.e.c. (RSA, *prime d'activité*) | 36.5 | 2.2 | 1.24 | 0.9 | 0.8 | 1.0 | 1.2 | +0.3 | [^es-cofog] |

† Insee warns that the 2024 jump in "housing and community amenities" (+18.3%, +EUR 7 bn) is **partly an artifact** of a change in local-government accounting nomenclature, offset by a fall in "economic affairs". The effect will be neutralized in the final 2024 data [^ip2093].

**Key observations**

- **Social protection plus health = 57.1% of TE** (41.5% + 15.6%), or 32.5% of GDP, in 2024. Insee's own reading: social protection is 41% (EUR 693 bn), health 16% (EUR 261 bn), general services 11% (EUR 181 bn), economic affairs 10% (EUR 166 bn), education 9% (EUR 149 bn). Each of the other functions is 3% or less [^ip2093].
- **Composition shift, 1995-2024**: the share of old age plus health rose by **about 4.4 pp of GDP**. Lower interest (-1.6 pp), defense (-0.65 pp), education (-0.74 pp), economic affairs (-0.74 pp), family (-0.4 pp) and survivors (-0.3 pp) **largely offset** the rise [computed]. Spending was redeployed toward older people and health rather than simply added on top. This supports the thesis that the *structure* of spending, not only its level, is the issue. Caveat: 1995 COFOG data are back-casts.
- **Over the last 10 years (2014-2024)** Insee reports: social protection spending +EUR 165 bn, but **-0.8 pp of GDP**. Health +EUR 82 bn and **+0.6 pp of GDP**. Health's share of TE rose by 1.3 pp, defense by 0.4 pp and public order by 0.3 pp. Social protection's share fell by 0.5 pp: pensions +0.2, family -0.4, unemployment -0.4, sickness +0.4, social exclusion +0.4 [^ip2093].
- **2024 drivers**: TE +4.0% (+EUR 64 bn). Contributions: social protection +2.2 pts (of which pensions +1.4 pts, +EUR 23 bn, after the 5.3% indexation of basic pensions in January 2024), health +0.7, education +0.4, debt charge +0.5, defense +0.2, economic affairs -0.7 (end of the energy price shield, about -EUR 14 bn) [^ip2093].
- **Defense**: EUR 54.2 bn in 2024 (1.85% of GDP at current GDP, shown as **1.8%** on the website per `00-reference-figures.md` row 15; Insee IP 2093 prints 1.9% on the earlier GDP vintage) (corrected 2026-10-25: was "1.9% of GDP"), of which compensation EUR 21.5 bn. Military spending proper is 88% (EUR 48 bn). Growth averaged +7.8%/yr in 2021-2024 vs +2.7%/yr in 2014-2021 [^ip2093].

### 4.2 Where do 1,000 EUR of public spending go?

Three official or recognized decompositions exist. **They differ because of grouping choices**, so the platform should pick one and state its convention.

| Category | A. Eurostat COFOG 2024, % of TE × 10 [computed] | B. Fipeco 2024 (health grouped inside social protection) | C. Government site *À quoi servent mes impôts* (2024 data, Insee/DG Trésor) | Src |
|---|---|---|---|---|
| Social protection (total as defined by the source) | 415 (excl. health) | 571 (incl. health) | 561 (incl. health and housing benefits) | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| of which old-age pensions | 234 (+24 survivors) | 259 (old age + survivors) | n.a. | [^es-cofog] [^fipeco-ap] |
| of which health | 156 (separate division) | 206 (health and disability) | included | [^es-cofog] [^fipeco-ap] |
| of which family | 40 | 40 | n.a. | [^es-cofog] [^fipeco-ap] |
| of which unemployment | 29 | 29 | n.a. | [^es-cofog] [^fipeco-ap] |
| of which social exclusion | 22 | 22 | n.a. | [^es-cofog] [^fipeco-ap] |
| of which personal housing benefits | 13 | 13 | n.a. | [^es-cofog] [^fipeco-ap] |
| Education | 89 | 89 | 88 | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| Economic affairs / business support | 99 (incl. transport 36) | 99 (63 aid and subsidies + 36 transport) | 59 economic affairs + 50 transport + 11 infrastructure | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| General public services / support functions | 108 (incl. interest 35) | 61 (excl. interest and basic research) | 66 | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| Interest on public debt | 35 (inside GF01) | 35 | 31 | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| Defense | 32 | 32 | 31 | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| Public order, security and justice | 31 | 31 | 25 security + 5 justice | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| Recreation and culture | 26 | 26 | 25 | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| Housing and community amenities | 25 | 25 (*aides à la pierre* and amenities) | not listed in the alt text | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| Environmental protection | 18 | 18 | 17 | [^es-cofog] [^fipeco-ap] [^aqsmi] |
| Basic research | in GF01 | 12 | 30 (all research) | [^fipeco-ap] [^aqsmi] |
| **Total** | **≈1,000** | **1,000** | **≈1,000** | |

Notes:

- (A) and (B) both rest on Insee/Eurostat COFOG 2024 (TE EUR 1,672 bn). Fipeco states 57.2% of GDP.
- The government figures (C) were read from the official infographic's alternative text on economie.gouv.fr. The image itself could not be downloaded (403/redirect). (Verification note: on 2026-10-25 the page returned 403 to curl but loaded in a browser. The alt text was re-read and matches all 13 categories, which sum to 999. Image: https://www.economie.gouv.fr/files/files/directions_services/aqsmi/AQSMI_infographie_Que_financent_1000euros_impots.jpg) The interest figure (31) is lower than the COFOG figure (35). ⚠ Still not reconciled (second pass, 2026-10-25): the page says only "*données 2024 source Insee/DG Trésor*" and that the debt item "*correspond au montant dû au titre des intérêts de la dette publique*", with a link to the *direction du Budget*; it gives no method. A plausible but unconfirmed explanation is that the item uses the State budget debt charge (LFI 2024 appropriation EUR 50.86 bn, per the Senate) rather than general-government D.41: 50.86 / 1,672 ≈ 30 per 1,000. **Recommendation: on the website, use the COFOG/Fipeco value (35) and do not cite the infographic's 31.**
- Fipeco cautions that the "1,000 EUR of taxes" framing assumes all revenues fund all spending pro rata, whereas taxes are earmarked to subsectors [^fipeco-ap].
- **Recommended platform wording:** "For every 1,000 euros of public spending in 2024, about 460 went to pensions and health (Fipeco/Insee), 89 to education, 35 to debt interest and 32 to defense."

---

## 5. Breakdown by subsector and by economic nature

### 5.1 Subsectors (unconsolidated; transfers between subsectors are counted in the paying subsector)

The table shows EUR bn and % of GDP. Source: Eurostat gov_10a_main, sectors S1311 (central = State + ODAC), S1313 (local), S1314 (social security) [^es-main]. The 2025 values are confirmed by Insee IP 2106 [^ip2106].

| Subsector | 1995 EUR bn (% GDP) | 2005 EUR bn (% GDP) | 2015 EUR bn (% GDP) | 2025 EUR bn (% GDP) | 2025 share of unconsolidated sum | 2025 balance (EUR bn) | Src |
|---|---|---|---|---|---|---|---|
| Central government (*APUC*: State + ODAC) | 331.1 (27.1) | 436.9 (24.8) | 532.3 (24.2) | 681.1 (22.8) | 37% | -130.3 (State -128.1; ODAC -2.2) | [^es-main] [^ip2106] |
| Local government (*APUL*) | 120.3 (9.9) | 186.6 (10.6) | 246.2 (11.2) | 335.5 (11.2) | 18% | -15.6 | [^es-main] [^ip2106] |
| Social security (*ASSO*) | 285.7 (23.4) | 427.7 (24.3) | 578.1 (26.3) | 803.2 (26.9) | 44% | -5.8 (Eurostat Oct 2026) / -6.7 (Insee May 2026) | [^es-main] [^ip2106] |
| Unconsolidated sum | 737.1 | 1,051.2 | 1,356.6 | 1,819.7 | 100% | | [^es-main] |
| Consolidated general government | 684.0 (56.1) | 956.1 (54.3) | 1,268.0 (57.6) | 1,714.1 (57.3) | | -151.6 | [^es-main] |
| Intra-government flows removed by consolidation | 53.1 | 95.1 | 88.6 | 105.6 | | | [computed] |

**Transfers between subsectors (2025)**: central government current transfers to other subsectors were **EUR 63.0 bn** (-3.0%): **EUR 40.7 bn to local governments** and **EUR 22.4 bn to social security** [^ip2106].

Two caveats about these transfers:

- They understate how much the State finances local governments and social security. Most of that financing now goes through **shares of tax revenue assigned by law** (VAT fractions to regions, *départements*, intercommunal bodies and social security; CSG; excise duties), which are recorded as tax revenue of the recipient, not as transfers.
- Insee estimates total intra-government transfers, consolidated out of the totals, at about **EUR 400 bn in 2024** [^insee-blog]. That figure includes flows within subsectors.

**Trend**: since 1995, social security has grown from 23.4% to 26.9% of GDP and local governments from 9.9% to 11.2%. Central government has shrunk from 27.1% to 22.8% (unconsolidated). Central government nevertheless carries **most of the deficit** (EUR 130 bn of EUR 151.6 bn in 2025; corrected 2026-10-25: was "152 bn", the May 2026 vintage), because it finances other subsectors and bears the interest charge (EUR 53.3 bn of EUR 64.7 bn in 2025, Insee concept) [^ip2106].

### 5.2 By economic nature (consolidated general government)

The table shows EUR bn, % of GDP and % of TE, with euro-area and EU benchmarks in % of GDP (GDP-weighted aggregates). Source: Eurostat gov_10a_main [^es-main]; Insee IP 2106 table 4 for the Insee concepts [^ip2106].

| ESA item | 1995 FR (% GDP) | 2005 FR (% GDP) | 2015 FR (% GDP) | 2025 FR EUR bn | 2025 FR % GDP | 2025 FR % of TE | 2025 EA20 (% GDP) | 2025 EU27 (% GDP) | FR - EA20 2025 (pp) | Src |
|---|---|---|---|---|---|---|---|---|---|---|
| Compensation of employees (D1, incl. imputed pension contributions) | 13.5 | 13.0 | 13.0 | 370.0 | 12.4 | 21.6 | 10.0 | 10.3 | +2.4 | [^es-main] |
| Intermediate consumption (P2) | 5.5 | 5.1 | 5.3 | 163.5 | 5.5 | 9.5 | 5.9 | 6.1 | **-0.4** | [^es-main] |
| Social benefits other than in kind (D62: pensions, allowances) | 17.7 | 17.5 | 19.7 | 580.9 | 19.4 | 33.9 | 16.9 | 16.4 | +2.5 | [^es-main] |
| Social transfers in kind purchased from market producers (D632: reimbursements of private doctors, drugs, housing aid…) | 4.7 | 5.6 | 6.2 | 190.1 | 6.4 | 11.1 | 6.0 | 5.4 | +0.4 | [^es-main] |
| Subsidies (D3) | 1.5 | 1.4 | 2.5 | 56.5 | 1.9 | 3.3 | 1.4 | 1.4 | +0.5 | [^es-main] |
| Interest (D41) | 3.5 | 2.7 | 2.0 | 65.7 | 2.2 | 3.8 | 1.9 | 1.9 | +0.3 | [^es-main] |
| Gross fixed capital formation (P51G) | 4.6 | 4.4 | 3.9 | 132.2 | 4.4 | 7.7 | 3.7 | 3.9 | +0.7 | [^es-main] |
| Other current transfers (D7, incl. EU contribution) | 2.7 | 2.9 | 3.1 | 94.0 | 3.1 | 5.5 | 2.2 | 2.2 | +0.9 | [^es-main] |
| Capital transfers (D9) | 1.7 | 1.0 | 1.3 | 41.5 | 1.4 | 2.4 | 1.4 | 1.4 | 0.0 | [^es-main] |
| Other taxes on production paid (D29, e.g., *taxe sur les salaires*) | 0.4 | 0.4 | 0.5 | 13.9 | 0.5 | 0.8 | 0.2 | 0.3 | +0.3 | [^es-main] |
| **Total expenditure** | 56.1 | 54.3 | 57.6 | 1,714.1 | 57.3 | 100 | 49.8 | 49.4 | +7.5 (vs EA21, canonical: +7.6) | [^es-main] |

Insee's grouping for 2025 is as follows (EUR bn; % growth 2024/25):

- operating expenditure 548.8 (+1.4%), of which intermediate consumption 164.6 (+0.1%) and compensation 370.0 (+1.9%)
- interest 64.7 (+11.2%)
- social benefits in cash and in kind 771.0 (+3.2%)
- other transfers and subsidies 192.1 (-0.6%)
- net acquisitions of non-financial assets 137.7 (+3.9%), of which GFCF 132.2 (+3.7%) [^ip2106]

Pensions rose by EUR 13.2 bn (+3.3%) in 2025 after +EUR 24.9 bn (+6.7%) in 2024 [^ip2106].

**Panel comparison, 2025, % of GDP** (Eurostat gov_10a_main [^es-main]):

| Country | Compensation D1 | Interm. consumption P2 | Cash benefits D62 | In-kind purchased D632 | Subsidies D3 | Interest D41 | GFCF P51G | Src |
|---|---|---|---|---|---|---|---|---|
| France | 12.4 | 5.5 | 19.4 | 6.4 | 1.9 | 2.2 | 4.4 | [^es-main] |
| Germany | 8.5 | 6.4 | 16.5 | 9.2 | 1.2 | 1.1 | 3.5 | [^es-main] |
| Italy | 9.0 | 5.8 | 20.3 | 2.3 | 1.6 | 3.8 | 3.9 | [^es-main] |
| Spain | 10.7 | 5.7 | 16.9 | 2.7 | 1.2 | 2.4 | 3.0 | [^es-main] |
| Netherlands | 8.9 | 6.6 | 10.7 | 10.6 | 1.3 | 0.7 | 3.5 | [^es-main] |
| Belgium | 12.6 | 4.3 | 17.6 | 8.1 | 3.5 | 2.3 | 3.2 | [^es-main] |
| Sweden | 12.3 | 8.3 | 11.5 | 3.5 | 1.1 | 0.6 | 5.8 | [^es-main] |
| Denmark | 14.2 | 8.4 | 14.1 | 1.2 | 1.2 | 0.8 | 3.3 | [^es-main] |

**Reading**: the split between D1/P2 (public production) and D632 (public reimbursement of private provision) depends on how health and care are organized. Germany and the Netherlands reimburse non-government hospitals and insurers through D632, while France and the Nordic countries employ staff directly. Comparisons of the "public wage bill" must therefore be read alongside D632. France's employee compensation also includes **imputed employer contributions for State civil-servant pensions**, about 1.8% of GDP for the State. All public employers together pay about 4% of GDP in pension contributions, the highest in the EU together with Belgium [^insee-blog] [^fipeco-fn].

---

## 6. International comparison

### 6.1 Total expenditure, % of GDP: EU27, euro area, OECD, panel

Source: Eurostat gov_10a_main [^es-main]; OECD Table 11 plus OECD Table 1 GDP [^oecd-t11]. Means and medians are **unweighted across countries** [computed]. "EU27 agg." and "EA20 agg." are Eurostat's GDP-weighted aggregates.

| Year | France | EU27 agg. | EA20 agg. | EU27 unweighted mean | EU27 median | France rank / 27 | EA20 unweighted mean | EA20 median | France rank / 20 | Src |
|---|---|---|---|---|---|---|---|---|---|---|
| 2005 | 54.3 | 47.2 | 47.2 | 43.8 | 44.1 | 1 | 43.7 | 45.0 | 1 | [^es-main] |
| 2010 | 57.7 | 50.7 | 51.1 | 48.2 | 48.2 | 2 (Ireland 65.0, bank bailout) | 49.0 | 48.5 | 2 | [^es-main] |
| 2015 | 57.6 | 48.3 | 48.6 | 45.4 | 44.4 | 1 | 45.5 | 44.8 | 1 | [^es-main] |
| 2019 | 55.3 | 46.6 | 47.0 | 43.1 | 42.5 | 1 | 43.2 | 43.1 | 1 | [^es-main] |
| 2024 | 57.0 | 48.9 | 49.3 | 45.7 | 46.5 | 2 (Finland 57.9) | 45.8 | 46.6 | 2 | [^es-main] |
| 2025 | 57.3 | 49.4 | 49.8 | 46.4 | 47.3 | 2 (Finland 57.5) | 46.5 | 47.5 | 2 | [^es-main] |

**2025 EU27 ranking (TE % of GDP)**: Finland 57.5, **France 57.3**, Austria 54.6, Belgium 54.4, Italy 51.1, Poland 50.9, Germany 50.1, Croatia 49.4, Sweden 49.3, Slovenia 48.9, Luxembourg 48.7, Greece 47.8, Hungary 47.6, Slovakia 47.3, Denmark 47.2, Estonia 45.6, Spain 45.3, Latvia 45.3, Netherlands 45.2, Romania 43.4, Czechia 43.3, Portugal 42.3, Bulgaria 42.1, Lithuania 41.1, Cyprus 37.9, Malta 37.1, Ireland 22.3 (distorted by multinational GDP) [^es-main].

**Panel, 2025** (TE / revenue / balance, % of GDP): France 57.3 / 52.2 / -5.1; Germany 50.1 / 47.2 / -2.9; Italy 51.1 / 48.0 / -3.1; Spain 45.3 / 42.9 / -2.4; Netherlands 45.2 / 43.6 / -1.6; Belgium 54.4 / 49.2 / -5.2; Sweden 49.3 / 47.8 / -1.6; Denmark 47.2 / n.a. / n.a. (Danish 2025 revenue was missing in the extraction) [^es-main].

**OECD** [computed from OECD SDMX Table 11 "General government expenditure by function", national currency, divided by OECD Table 1 nominal GDP]. The figures are unweighted means across the OECD countries with data, **not** an official OECD aggregate. The 2024 sample has 32 countries; Canada, Costa Rica, Korea, Mexico, New Zealand and Türkiye are missing.

| Year | France | OECD mean | OECD median | France rank | n | USA | Japan | UK | Src |
|---|---|---|---|---|---|---|---|---|---|
| 2005 | 54.3 | 42.6 | 43.4 | 1 | 31 | 37.0 | 34.7 | 41.3 | [^oecd-t11] |
| 2015 | 57.6 | 43.4 | 43.0 | 1 | 33 | 37.8 | 38.2 | 42.1 | [^oecd-t11] |
| 2019 | 55.3 | 41.8 | 42.1 | 1 | 34 | 38.2 | 37.9 | 40.3 | [^oecd-t11] |
| 2024 | 57.0 | 44.7 | 46.0 | 2 (Finland 57.7) | 32 | 39.6 | 39.0 | 45.8 | [^oecd-t11] |

### 6.2 Each COFOG division, 2024, % of GDP

All values are recomputed from Eurostat EUR millions divided by current GDP, so France's total is 57.0% (not the published 57.3%). EU27w and EA20w are GDP-weighted. Ranks run from highest (1) to lowest. Source: Eurostat gov_10a_exp, nama_10_gdp [^es-cofog] [^es-gdp]. File: `data/01_derived_cofog_international_2024.csv`.

| Function | FR | EU27w | EA20w | EU27 mean | EU27 median | FR rank /27 | EA20 mean | EA20 median | FR rank /20 | DE | IT | ES | NL | BE | SE | DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| **Total** | 56.96 | 48.83 | 49.18 | 45.60 | 46.40 | 2 | 45.68 | 46.33 | 2 | 48.77 | 50.17 | 45.35 | 44.70 | 54.13 | 50.03 | 46.40 | [^es-cofog] |
| General public services | 6.17 | 6.04 | 6.12 | 5.53 | 5.45 | 7 | 5.49 | 5.47 | 6 | 6.33 | 7.71 | 5.79 | 4.14 | 7.15 | 5.44 | 5.58 | [^es-cofog] |
| of which interest | 2.01 | 1.92 | 1.93 | 1.69 | 1.43 | 9 | 1.61 | 1.41 | 6 | 1.12 | 3.97 | 2.48 | 0.72 | 2.34 | 0.78 | 0.78 | [^es-cofog] |
| Defense | 1.85 | 1.47 | 1.36 | 1.58 | 1.44 | 8 | 1.49 | 1.39 | 5 | 1.34 | 1.28 | 0.89 | 1.64 | 1.28 | 1.95 | 1.81 | [^es-cofog] |
| Public order and safety | 1.78 | 1.73 | 1.69 | 1.81 | 1.72 | 11 | 1.75 | 1.68 | 8 | 1.61 | 1.77 | 1.79 | 1.94 | 1.72 | 1.58 | 0.96 | [^es-cofog] |
| Economic affairs | 5.66 | 5.26 | 5.21 | 5.29 | 5.46 | 13 | 5.16 | 5.36 | 9 | 5.35 | 5.08 | 5.06 | 4.44 | 6.43 | 4.78 | 2.99 | [^es-cofog] |
| Environmental protection | 1.03 | 0.82 | 0.85 | 0.77 | 0.71 | 6 | 0.82 | 0.73 | 6 | 0.56 | 0.90 | 0.97 | 1.61 | 1.16 | 0.54 | 0.39 | [^es-cofog] |
| Housing and community amenities | 1.44 | 0.73 | 0.72 | 0.76 | 0.60 | 4 | 0.72 | 0.57 | 3 | 0.47 | 0.77 | 0.48 | 0.62 | 0.39 | 0.79 | 0.34 | [^es-cofog] |
| Health | 8.90 | 7.33 | 7.44 | 6.77 | 6.61 | 3 | 6.85 | 6.71 | 2 | 7.51 | 6.61 | 6.44 | 7.31 | 8.00 | 7.35 | 8.14 | [^es-cofog] |
| Recreation, culture, religion | 1.47 | 1.18 | 1.13 | 1.26 | 1.25 | 8 | 1.21 | 1.23 | 6 | 1.05 | 0.85 | 1.20 | 1.20 | 1.22 | 1.39 | 1.50 | [^es-cofog] |
| Education | 5.06 | 4.74 | 4.61 | 5.00 | 4.95 | 12 | 4.96 | 5.01 | 9 | 4.44 | 4.03 | 4.12 | 5.12 | 6.34 | 7.21 | 5.44 | [^es-cofog] |
| Social protection | 23.61 | 19.53 | 20.04 | 16.83 | 17.05 | 2 | 17.23 | 17.33 | 2 | 20.13 | 21.18 | 18.61 | 16.68 | 20.43 | 18.99 | 19.25 | [^es-cofog] |
| of which old age | 13.35 | 10.64 | 10.85 | 9.46 | 9.74 | 4 | 9.64 | 9.95 | 4 | 9.74 | 13.86 | 10.32 | 6.17 | 10.17 | 10.89 | 7.08 | [^es-cofog] |
| of which survivors | 1.38 | 1.45 | 1.59 | 0.95 | 0.94 | 8 | 1.07 | 1.17 | 7 | 1.84 | 2.41 | 2.22 | 0.04 | 1.42 | 0.13 | 0.01 | [^es-cofog] |
| of which sickness and disability | 2.86 | 2.76 | 2.80 | 2.40 | 2.17 | 11 | 2.42 | 2.66 | 9 | 3.28 | 1.71 | 2.75 | 4.35 | 3.92 | 3.54 | 4.67 | [^es-cofog] |
| of which family and children | 2.27 | 1.98 | 1.88 | 2.07 | 1.81 | 9 | 1.99 | 1.81 | 6 | 1.91 | 1.46 | 0.96 | 2.44 | 2.18 | 2.28 | 3.99 | [^es-cofog] |
| of which unemployment | 1.65 | 1.18 | 1.30 | 0.76 | 0.68 | **1** | 0.85 | 0.78 | **1** | 1.64 | 0.92 | 1.51 | 0.68 | 1.06 | 1.07 | 1.36 | [^es-cofog] |
| of which housing benefits | 0.72 | 0.35 | 0.38 | 0.25 | 0.14 | 2 | 0.27 | 0.17 | 2 | 0.44 | 0.04 | 0.04 | 0.44 | 0.23 | 0.28 | 0.56 | [^es-cofog] |
| of which social exclusion n.e.c. | 1.24 | 0.89 | 0.94 | 0.72 | 0.55 | 3 | 0.77 | 0.58 | 3 | 0.61 | 0.68 | 0.68 | 2.55 | 1.22 | 0.78 | 1.15 | [^es-cofog] |

**OECD view of selected divisions, 2024** [computed, unweighted, see §6.1] [^oecd-t11]:

| Division | FR | OECD mean | OECD median | FR rank | n | Top country | USA | Src |
|---|---|---|---|---|---|---|---|---|
| Social protection | 23.6 | 16.1 | 16.9 | 2 | 32 | Finland 26.4 | 7.8 | [^oecd-t11] |
| Old age | 13.4 | 8.9 | 8.8 | 4 | 30 | Finland 15.5 | n.a. | [^oecd-t11] |
| Health | 8.9 | 7.0 | 7.3 | 5 | 32 | **USA 10.3** | 10.3 | [^oecd-t11] |
| Education | 5.1 | 5.1 | 5.1 | 17 | 32 | Sweden 7.2 | 5.6 | [^oecd-t11] |
| Defense | 1.8 | 1.8 | 1.5 | 13 | 32 | Israel 9.0 | 3.1 | [^oecd-t11] |
| General public services | 6.2 | 5.6 | 5.5 | 10 | 32 | Hungary 10.0 | 6.9 | [^oecd-t11] |

### 6.3 Which functions explain France's excess spending?

Decomposition of the France minus euro-area (EA20, GDP-weighted) gap, in pp of GDP [computed]. *(Reconciliation note: against EA21, the canonical aggregate, the 2024 COFOG gap is +7.84 pp, with the same shares: social protection +3.61 (46%), of which old age +2.51 (32%), health +1.47 (19%). See `data/00_reconcile_cofog_gap_2024_EA20_EA21.csv`.)* The 2005 EA20 aggregate excludes Slovakia, for which 2005 COFOG data were missing. Source: Eurostat gov_10a_exp, nama_10_gdp [^es-cofog] [^es-gdp].

| Function | Gap 2005 (pp GDP) | Gap 2024 (pp GDP) | Share of 2024 gap | ≈ EUR bn 2024 | Src |
|---|---|---|---|---|---|
| **Total** | **+6.98** | **+7.77** | 100% | ≈228 | [^es-cofog] |
| Social protection | +3.38 | +3.57 | 46% | ≈105 | [^es-cofog] |
| of which old age | +1.88 | +2.50 | 32% | ≈73 | [^es-cofog] |
| of which survivors | -0.27 | -0.21 | -3% | | [^es-cofog] |
| of which family | +0.93 | +0.39 | 5% | | [^es-cofog] |
| of which unemployment | +0.14 | +0.35 | 5% | | [^es-cofog] |
| of which housing benefits | +0.56 | +0.34 | 4% | | [^es-cofog] |
| of which social exclusion | +0.27 | +0.30 | 4% | | [^es-cofog] |
| of which sickness and disability | +0.04 | +0.06 | 1% | | [^es-cofog] |
| Health | +1.14 | +1.45 | 19% | ≈43 | [^es-cofog] |
| Housing and community amenities | +0.33 | +0.71 | 9% (partly artifact, see §4.1) | ≈21 | [^es-cofog] |
| Defense | +0.51 | +0.49 | 6% | | [^es-cofog] |
| Education | +0.77 | +0.46 | 6% | | [^es-cofog] |
| Economic affairs | +0.34 | +0.44 | 6% | | [^es-cofog] |
| Recreation, culture | +0.29 | +0.33 | 4% | | [^es-cofog] |
| Environmental protection | +0.04 | +0.18 | 2% | | [^es-cofog] |
| Public order and safety | -0.12 | +0.09 | 1% | | [^es-cofog] |
| General public services | +0.31 | +0.05 | 1% | | [^es-cofog] |
| of which interest | -0.24 | +0.07 | 1% | | [^es-cofog] |

**Evolution of the gap vs EA20 (pp of GDP)** [computed]: 1996-2000 about 5.3-6.1; 2005 7.0; 2010 6.6; 2015 9.0; 2017 10.3 (CICE); 2019 8.4; 2022 8.6; 2023 7.5; 2024 7.8. (Verification note: these COFOG-based gaps use current nama_10_gdp GDP and the COFOG totals. They differ by about 0.1 pp from the gov_10a_main gaps in §3.1, which are 8.3 in 2019, 7.6 in 2023 and 7.7 in 2024. Quote one series consistently.) The social-protection component went from about 2.6 pp (late 1990s) to 3.4 (2005), peaked at 4.6-4.8 (2017-2020), and stood at 3.6 in 2024. The old-age component rose from about 1.8-2.0 pp (late 1990s) to about 2.8-2.9 (2015-2018), then 2.5 (2024). The health component stood at about 1.0-1.1 pp in 1996-2019 and widened to 1.45 in 2023-2024.

**Cross-checks with other analysts**:

- **Fipeco (8 Jul 2026), France vs EU average 2024**: TE 57.3 vs 49.1% of GDP (gap 8.2 pp). The largest gaps are **pensions 14.8 vs 12.2% (+2.6 pp, ≈32% of the gap)** and **health 11.8 vs 10.2% (+1.6 pp)**. Housing policy is 2.1 vs 1.1%. Transport and energy policies are the only functions *below* the EU average (corrected after verification: was "Transport is the only function well below"; Fipeco says "à l'exception des politiques des transports et de l'énergie"). In Fipeco's convention, pensions include survivors and health includes all health-related cash benefits [^fipeco-fn].
- **Insee blog (Oct 2025)**: the France-EU gap was **7.9 pp in 2024**, vs 5.2 pp in the early 2000s and 10.7 pp at the 2017 peak (9.7 pp with the CICE reclassified) [^insee-blog].
- **Conclusion on the "pensions ≈ half" claim**: under COFOG, **pensions explain about one third** of France's excess spending vs the euro area or EU (29-32%), and **pensions plus health about one half** (48-51%). The "half" figure is reached only when health is added, or when the comparison is with a low-pension country (vs Germany 2024: old age +3.5 pp out of a +7.9 pp gap, but survivors -0.5 pp).

### 6.4 PPS per capita (volume comparison)

Method: EUR value / (price level index for GDP, EU27 = 100) / population [computed]. Source: Eurostat gov_10a_exp (COFOG, MIO_EUR), **prc_ppp_ind_1** (PLI_EU27_2020, ppp_cat18 = GDP; API "updated" 2026-07-09, covers 2025), nama_10_pe [^es-cofog] [^es-pli] [^es-pop]. COFOG stops at 2024, so the function rows are 2024. Script: `scripts/topic01/analyze01d_pps_pli1.py`; output: `data/01_derived_cofog_pps_pc_pli1.csv`.

> **Recomputed on the current PLI vintage (2026-10-25).** All rows below now use `prc_ppp_ind_1`. They replace the earlier table on the superseded `prc_ppp_ind` (July 2025 PLIs), whose total was 22,321 PPS (9th). The COFOG total (22,383 PPS, 9th) is a few PPS below the canonical-method value for 2024 because the COFOG table carries an older vintage of total expenditure (EUR 1,671.8 bn vs 1,672.7 bn in `gov_10a_main`, Oct 2026; see `00-reference-figures.md` log #6). Other 2024 totals: 22,395 (9th, `gov_10a_main` TE with `prc_ppp_ind_1`) and 22,398 (8th, TE/GDP x GDP per capita in PPS, `nama_10_pc`). The website value is **2025: 23,330 PPS, 8th of 27** (`00-reference-figures.md` row 5). The 2024 rank (8th or 9th) depends on a gap of a few PPS with Sweden (22,399) and should not be displayed without that caveat. Function-level ranks are 2024 COFOG values; next to a % of GDP ranking, state the year and that these are **per inhabitant in PPS**, not % of GDP or % of total spending.

| Indicator (2024, PPS per inhabitant) | France | EU27 unweighted mean | EU27 median | FR rank /27 | DE | IT | ES | NL | BE | SE | DK | Src |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| Total expenditure (COFOG vintage) | 22,383 | 18,744 | 16,392 | **9** (8th-9th, see note) | 22,937 | 19,679 | 16,556 | 23,760 | 25,195 | 22,399 | 24,032 | [^es-cofog] [^es-pli] |
| Social protection | 9,279 | 7,044 | 5,733 | 7 | 9,467 | 8,306 | 6,794 | 8,867 | 9,509 | 8,502 | 9,970 | [^es-cofog] [^es-pli] |
| Old age | 5,248 | 3,855 | 3,282 | 5 | 4,580 | 5,435 | 3,769 | 3,281 | 4,733 | 4,874 | 3,669 | [^es-cofog] [^es-pli] |
| Health | 3,497 | 2,820 | 2,592 | 8 | 3,529 | 2,592 | 2,351 | 3,885 | 3,726 | 3,292 | 4,218 | [^es-cofog] [^es-pli] |
| Education | 1,990 | 2,062 | 1,973 | 11 | 2,086 | 1,582 | 1,504 | 2,724 | 2,952 | 3,229 | 2,819 | [^es-cofog] [^es-pli] |
| General public services | 2,425 | 2,246 | 2,113 | 10 | 2,979 | 3,023 | 2,113 | 2,202 | 3,329 | 2,436 | 2,889 | [^es-cofog] [^es-pli] |
| Economic affairs | 2,223 | 2,139 | 1,978 | 8 | 2,514 | 1,994 | 1,848 | 2,359 | 2,995 | 2,142 | 1,551 | [^es-cofog] [^es-pli] |
| Defense | 726 | 596 | 605 | 8 | 628 | 502 | 325 | 871 | 597 | 871 | 936 | [^es-cofog] [^es-pli] |
| Public order and safety | 698 | 700 | 694 | 12 | 757 | 694 | 654 | 1,029 | 800 | 708 | 496 | [^es-cofog] [^es-pli] |
| Housing and community amenities | 564 | 303 | 268 | 2 | 220 | 301 | 174 | 330 | 180 | 353 | 176 | [^es-cofog] [^es-pli] |

Changes from the superseded table: values move by less than 1.5%; ranks are unchanged except **education, 11th of 27 (was 12th)**.

**Evolution of TE per capita (PPS)** [computed, COFOG TE with `prc_ppp_ind_1`]: 2005: France 13,571 (rank 6/26; mean 9,779). 2010: 15,759 (rank 9/27). 2015: 16,997 (rank 6/27). 2019: 18,409 (rank 6/27). 2024: 22,383 (rank 9/27; 22,395-22,398, 8th-9th with `gov_10a_main` TE). 2025: **23,330 (8th)** on the canonical method. Countries above France in 2025: Luxembourg, Austria, Belgium, Denmark, the Netherlands, Germany and Finland. (Recomputed 2026-10-25 on `prc_ppp_ind_1`: 2005-2015 are unchanged from the old vintage; 2019 moves from 18,392 to 18,409; rank unchanged.)

**Interpretation**: in volume per inhabitant, France spends **about the same as Germany, Sweden or the Netherlands**, and less than Belgium or Denmark. The ratio to GDP is high because **GDP per capita is lower** than in these countries. The COR makes the same point for pensions: France is 2nd (after Italy) in public pensions/GDP but **6th per inhabitant** among the countries it follows (behind the US, Italy, Sweden, Germany and Belgium, just ahead of the Netherlands) [^cor]. (Verification note: the COR per-capita ranking uses **2021 OECD SOCX data, public plus private old-age and survivors' spending, in USD PPP**, not 2025 data.) Drees makes the same point for all social benefits: France is 2nd in the EU for benefits/GDP (31.9% vs Finland 32.5%) but **9th per inhabitant** (EUR 13,620 PPP, France-based PPP) in 2024 [^drees]. On Eurostat ESSPROS in EU-27 PPS (Oct 2026 release), France ranks **7th of 27** (12,606 PPS of social protection benefits per inhabitant, 2024); this is the canonical rank for the platform *(Reconciled 2026-10-25, see `00-reference-figures.md`.)*. Fipeco's rebuttal is that GDP is the tax base, so the ratio to GDP is what matters for the tax burden and sustainability [^fipeco-ratio]. **Both statements are true. They answer different questions**: generosity of provision vs the tax effort needed to finance it.

---

## 7. Outcome indicators (what is obtained)

These are broad indicators only. Detailed health and education outcome files are separate topics.

| Outcome | France | EU27 | Panel | France's EU rank | Year | Source | Src |
|---|---|---|---|---|---|---|---|
| At-risk-of-poverty rate after social transfers (60% of median) | 16.3% | 16.3% | DE 16.1, IT 18.6, ES 19.5, NL 13.4, BE 10.9, SE 15.6, DK 11.8 | 17th lowest of 27 (median 15.6) | EU-SILC 2025 (incomes 2024) | Eurostat ilc_li02 | [^es-silc] |
| Poverty rate before social transfers, pensions counted as income | 26.5% | 24.4% | DE 24.4, IT 26.8, NL 21.2, BE 23.0, SE 25.3, DK 24.5 | 20th lowest | 2025 | Eurostat ilc_li10 | [^es-silc] |
| Reduction in poverty from non-pension transfers [computed] | **-10.2 pp** | mean -8.1 | DE -8.3, IT -8.2, ES -5.9, NL -7.8, BE -12.1, SE -9.7, DK -12.7 | 6th largest of 27 | 2025 | Eurostat ilc_li02 / ilc_li10 | [^es-silc] |
| Poverty rate before all transfers incl. pensions | 46.8% | 42.8% | DE 41.1, IT 46.9 | 2nd highest of 27 | 2025 | Eurostat ilc_li09 | [^es-silc] |
| Life expectancy at birth | 83.0 years | 81.5 | DE 81.2, IT 83.7, ES 84.0, NL 81.9, BE 82.4, SE 83.8, DK 82.0 | 7th of 27 | 2024 | Eurostat demo_mlexpec | [^es-le] |

Reading:

- French transfers achieve **above-average poverty reduction**, but the final poverty rate is only **average** (16.3%, equal to the EU27). Pre-transfer market-income poverty is high, especially once pensions are counted as transfers. This reflects the large pension system and the low employment rates of seniors and young people.
- Life expectancy is high (7th), but below Spain and Italy, which spend less on health per capita in PPS.
- Spending outcomes are not attributable to spending levels alone. These indicators show **correlation, not efficiency**.
- Insee's national poverty measure (ERFS survey) differs from EU-SILC and was **not** used here.

---

## 8. Methodological notes from Insee and Eurostat (what the ratio does and does not measure)

1. **TE/GDP is not a share of GDP.** About 45% of TE consists of social benefits paid to households, who then spend them privately. Government *value added* was **18.4% of total value added in 2023**: euro area 14.1%, EU 14.5%, Germany 11.6%, where hospitals sit outside general government [^fipeco-ratio].
2. **Tax credits** (EUR 19.8 bn in 2024; peak EUR 39.8 bn in 2017 with the CICE) are recorded as spending when refundable. Comparable tax expenditures structured as exemptions reduce revenue instead [^insee-blog].
3. **Imputed pension contributions** for State civil servants (1.8% of GDP in 2024) are recorded both as spending (compensation) and as revenue. The State employer rate (78.3% in 2025 for civil servants, vs 16.7% for private employers) is set to balance the regime, so part of it is effectively a balancing subsidy. Insee is studying an alternative convention. **It would lower spending by function without changing the deficit** [^insee-blog] [^fipeco-fn].
4. **Own-account production** (software, R&D) was EUR 33 bn in 2024 (1.1% of GDP; 1.9% of TE). It appears both in compensation and in GFCF, with an offsetting revenue entry [^insee-blog].
5. **Double counting**: if one removes employer contributions paid by government, taxes on production paid by government and own-account production (Fipeco using Eurostat data, 2023), France's ratio falls from 57.0% to **51.4%**. (Verification note: this is the early-2025 data vintage. On it, France was 1st on the usual ratio, at 57.0% vs Finland 55.7%. Current Eurostat data give France 56.8% for 2023, so the corrected figures have not been updated.) France moves to **2nd place behind Finland (52.3%)**, ahead of Italy (50.0%), with Germany at 45.8% [^fipeco-ratio].
6. **Privatizations and nationalizations** at market value are financial transactions and have no effect on TE [^insee-blog].
7. **Provisional data**: COFOG 2024 values are provisional. They will be revised in autumn 2026 (semi-final) and autumn 2027 (final) [^ip2093].

---

## 9. Divergences between sources

| Item | Source A | Source B | Explanation | Src |
|---|---|---|---|---|
| TE 2024, % of GDP | Insee and Eurostat gov_10a_main: **57.0%** (EUR 1,672.7 bn) | Eurostat gov_10a_exp (COFOG) and Fipeco: **57.3%** (EUR 1,671.8 bn) | Same numerator (±EUR 1 bn). The COFOG dataset's PC_GDP appears to use a **pre-May-2026 GDP vintage** (implied GDP ≈ EUR 2,918 bn vs EUR 2,935 bn now) [computed]. Use 57.0% for 2024. | [^es-main] [^es-cofog] [^fipeco-fn] |
| TE 2025 | Insee/Eurostat total: **57.3%** | Government/HCFP excluding tax credits: **56.6%** | Refundable tax credits (≈EUR 20 bn) are excluded in the government concept | [^ip2106] [^hcfp] |
| Deficit 2025 | Insee (May 2026): **EUR 152.5 bn** | Eurostat (Oct 2026 EDP notification): **EUR 151.6 bn** | Routine revision (revenue +EUR 0.8 bn). Both give 5.1% of GDP. Social-security balance revised from -6.7 to -5.8 | [^ip2106] [^es-main] |
| Interest 2025 | Eurostat D.41 (gov_10a_main and EDP notification, Oct 2026): **EUR 65.7 bn = 2.2% of GDP** (canonical; same value as the Cour des comptes) | Insee IP 2106 table: **EUR 64.7 bn**, footnoted *hors correction au titre des Sifim sur les intérêts versés*; HCFP 66 bn = 65.7 rounded | Presentation of FISIM (indirectly measured financial intermediation services) in the Insee table; about EUR 1 bn. The HCFP figure is not a different accounting basis | [^es-main] [^ip2106] [^hcfp] |
| Pensions | COFOG "old age" 2024: **13.35% of GDP** (EUR 392 bn), excluding survivors (EUR 40.6 bn) and disability | COR 2025: **14.1% of GDP** (EUR 422 bn), all compulsory schemes. Fipeco 2024: **14.8%**, including survivors and other items | Scope: COFOG old age includes elderly care (e.g., APA) but excludes survivors' pensions. The COR covers pensions of all legally compulsory schemes incl. FSV, excl. RAFP (verified 2026-10-25 in the full COR report, figure notes: "*Champ : ensemble des régimes de retraite français légalement obligatoires, y compris FSV, hors RAFP*"; the FSV, *Fonds de solidarité vieillesse*, old-age solidarity fund, has been merged into the Cnav since 2026; the RAFP is the civil servants' additional pension scheme) | [^es-cofog] [^cor] [^fipeco-fn] |
| Social protection | COFOG social protection 23.6% + health 8.9% = **32.5% of GDP** (2024, general government only, incl. operating costs) | Drees CPS benefits **31.9% of GDP** (2024). Insee D62 + D632 **25.8%** (2025) | Drees (ESSPROS concept) counts benefits from all social-protection schemes, including private mutual insurers and employer schemes, and excludes administration costs. D62 + D632 excludes benefits produced directly by government (public hospitals' staff and purchases) | [^es-cofog] [^drees] [^ip2106] |
| Education | COFOG: **EUR 148.6 bn, 5.1% of GDP** (2024) | DEPP *dépense intérieure d'éducation*: **EUR 197.1 bn, 6.8% of GDP** (2024) | DEPP covers all funders (households, firms, all levels of government), includes extracurricular spending and is a different accounting framework | [^ip2093] |
| Defense | Insee COFOG: **EUR 54.2 bn, 1.85% of GDP at current GDP (website: 1.8%)** (accrual basis; IP 2093 prints 1.9% on the earlier GDP vintage) (corrected 2026-10-25: was "1.9% of GDP") | NATO definition (budget basis, includes parts of the gendarmerie and pensions) | Different scope. **The NATO figure was not verified in this file** | [^ip2093] |
| France vs EU gap 2024 | Fipeco: 8.2 pp (57.3 vs 49.1) | Insee blog: 7.9 pp. This file: 8.1 pp (57.0 vs 48.9, gov_10a_main) | The COFOG table `gov_10a_exp` still shows France at 57.3% for 2024 because its % of GDP uses a pre-May-2026 GDP; its euro level (EUR 1,671.8 bn) divided by current GDP gives 57.0%. **Canonical: 57.0% (2024).** Fipeco's 8.2 pp mixes the two vintages | [^fipeco-fn] [^insee-blog] [^es-main] |
| Compulsory levies 2024 | Insee: **42.7%** of GDP (May 2026 vintage; 42.8% in the earlier vintage quoted by the Insee blog) | Eurostat: 45.2% of GDP | Definitions: imputed contributions, tax credits net or gross, EU taxes | [^insee-blog] |
| 1,000 EUR decomposition | COFOG/Fipeco interest = 35 EUR | Government infographic = 31 EUR | ⚠ Not reconciled (no method published). Most plausible: State budget debt charge (LFI 2024: EUR 50.86 bn ≈ 30 per 1,000) instead of general-government D.41. Use 35 on the website (see §4.2) | [^fipeco-ap] [^aqsmi] |

---

## 10. Economists' disagreements and the strongest counter-arguments to the platform's thesis

The platform's thesis is that political proposals avoid questioning the *structure* of public spending, and that the public misjudges orders of magnitude. Below, each counter-argument is presented in its strongest form, followed by the best available reply. The platform should present both.

### 10.1 "France spends a lot relative to GDP because its GDP per capita is low, not because its State is extravagant"

- **Steelman**: in PPS per capita, France ranks 8th of 27 in 2025 (23,330 PPS, Eurostat Oct 2026 vintage) and 8th or 9th in 2024 depending on method (9th with the PLI method of §6.4). It is below Germany (2024: 23,034 vs 22,398), the Netherlands, Belgium, Denmark and Finland, and level with Sweden [computed]. For pensions per inhabitant, France ranks 6th among the COR's countries (2021 SOCX data, public plus private) [^cor]. For all social-protection benefits per inhabitant, France ranks 7th of 27 in EU-27 PPS (Eurostat ESSPROS, 2024) and 9th in Drees' France-based PPP [^drees]. The "French exception" is largely an exception in GDP per capita (productivity × employment rate), which links to low employment rates among young people and seniors.
- **Reply**: the tax base is GDP. With a lower GDP per capita, delivering the same per-capita services requires a higher tax rate, which is precisely the sustainability problem. Fipeco argues the GDP ratio is the relevant comparator [^fipeco-ratio]. **Both facts can be shown together**: "France spends about like Germany per inhabitant, but has to raise it from a smaller income per inhabitant."

### 10.2 "Public vs private is a choice of financing, not of size: total social effort is similar in the US"

- **Steelman**: on OECD SOCX **net total social expenditure** (public plus mandatory and voluntary private, after taxes), the **US (33.2% of GDP) exceeded France (32.0%; raw 31.95) in 2021** (38 countries, France 2nd; corrected after verification: was 31.9%). In 2019 it was France 30.1% vs the US 29.2%. Gross public social spending in 2021 was France 32.7% vs the US 21.6% (OECD average about 22%). Private social spending was **12.8% of GDP in the US vs 3.6% in France** [^socx]. US *public* health spending (COFOG) is **10.3% of GDP, above France's 8.9%** (2024) [^oecd-t11]. Agirc-Arrco supplementary pensions are classified as public in France, whereas the equivalent second-pillar schemes are private in most countries.
- **Reply**: compulsory levies leave households no choice of insurer or coverage, and that is what defines public spending [^fipeco-ratio]. Even adding private pensions, France stays 2nd behind Italy for total pension spending (14.2% of GDP in 2019 per COR/Fipeco) [^fipeco-ratio]. Also, SOCX net data stop at 2021, a Covid-affected year.

### 10.3 "The ratio is inflated by accounting conventions (double counting, imputed pensions, tax credits)"

- **Steelman**: about 4% of GDP of employer pension contributions, own-account production (1.1% of GDP) and taxes paid between administrations inflate TE. Corrected, France falls to 51.4% of GDP and is 2nd behind Finland [^fipeco-ratio]. The State employer contribution rate of 78% looks like a disguised balancing subsidy [^fipeco-fn].
- **Reply**: the conventions are common to all EU countries. The correction lowers France by about 5.6 pp but **does not change the ranking much** (Finland and France swap places). The gap with Germany (45.8% corrected) remains about 5.6 pp [^fipeco-ratio].

### 10.4 "The deficit problem since 2017 is a revenue problem (tax cuts), not a spending problem"

- **Steelman**: revenue fell from **54.3% of GDP (2017) to 51.2% (2024)**, -3.1 pp, while spending moved from 57.7% to 57.0% (-0.7 pp) [^es-main]. Even after adjusting for the CICE reclassification (about 1 pp of GDP in both spending and revenue; [^insee-blog]), revenue fell by about 2 pp while spending was roughly stable or rising by about 0.3 pp. The deterioration of the balance (-3.4% → -5.8%) is therefore **mostly on the revenue side**. The Cour des comptes estimates that the tax and contribution cuts decided over **2018-2023 cost EUR 62 bn in 2023, or 2.2 points of GDP** ("*d'importantes baisses d'impôts, dont l'impact est estimé à 62 Md€ en 2023, soit 2,2 pts de PIB*"), citing the corporate income tax cut, the cut in the CVAE (*cotisation sur la valeur ajoutée des entreprises*, a business value-added levy), the abolition of the *taxe d'habitation* (housing tax) and cuts in social contributions; it adds that these cuts, "*non compensées par des économies en dépenses*" (not offset by spending savings), widened the State deficit, and that weak spontaneous revenue growth (-1.6 pts of GDP of the PO ratio's -1.8 pt fall in 2023) explains most of the 2023 drop [^ccomptes24] (corrected 2026-10-25: was an unsourced list, "housing tax, CVAE, corporate tax cut to 25%, wealth-tax reform, flat tax", with amounts previously flagged as unverified; the wealth-tax reform and the flat tax are not itemized by the Cour and no separate amounts are given here). The Cour des comptes' June 2026 report also refers to "une longue séquence de baisse des prélèvements obligatoires entre 2015 et 2023" (a long sequence of cuts in compulsory levies from 2015 to 2023) [^ccomptes].
- **Reply**: compared with 2019 (a pre-Covid year after most tax cuts), spending is +2.0 pp of GDP (55.3 → 57.3) while revenue is -0.8 pp (53.0 → 52.2). Since 2019, the spending drift dominates. France's revenue/GDP (52.2%) remains among the highest in the EU. **This is a genuine disagreement on the counterfactual**, and the platform should show both base years. *Discretionary measures 2018-2023 are now quantified by the Cour (EUR 62 bn = 2.2 pts, see above; `00-reference-figures.md` row 28). A measure-by-measure breakdown (DG Trésor/RESF) was not done here.*

### 10.5 "Spending is redeployed, not out of control; pensions are stabilized"

- **Steelman**: TE/GDP is only +0.9 pp vs 1995 [computed]. The COR projects pensions at **14.1% of GDP in 2030 and 14.2% in 2045** (15.3% in 2070) [^cor]. Social-protection spending fell by 0.8 pp of GDP over 2014-2024 [^ip2093].
- **Reply**: COR resources fall from 13.9% to 12.9% of GDP, so the deficit widens from -0.2% (2025) to -2.4% of GDP (2070) [^cor]. Interest is rising (EUR 65.7 → about 91 bn in 2025-2027, general government) and squeezes everything else [^hcfp]. Stabilization at a high level, with lower fertility assumptions (1.45), is not stabilization of the system's balance.

### 10.6 "Level does not imply inefficiency"

- **Steelman**: transfers reduce poverty by 10.2 pp, more than the EU mean (8.1) [computed]. Life expectancy ranks 7th in the EU. France spends less than the average **share of TE** on education, transport and support functions (Fipeco) [^fipeco-fn]. OFCE economists (Ducoudré, Plane, Sampognaro, April 2017) make three points [^ofce]:
  - France's high spending is explained first by its social and tax model, more dynamic demography and a substantial defense budget.
  - **Public pension and health spending in the US is 8 pp of GDP lower than in France, but total (public plus private) pension and health spending is 2 pp of GDP higher**.
  - Public employment (20% of total employment) is not a French singularity: it is slightly below the OECD average. The rise in the spending ratio since 2008 reflects mainly weak growth (the denominator).
- **Reply**: the final poverty rate is only average (16.3% = EU27), and outcome-per-euro comparisons (education PISA, health) are covered in separate files. Institutional analysts who regard the level itself as a problem include the CAE, whose 2017 note no. 43 by Bacache-Beauvallet, Bureau, Giavazzi and Ragot makes three points [^cae]:
  - French spending was 57% of GDP in 2015 vs 48.5% on average in the OECD.
  - The excess is not driven by public employment. It is concentrated in economic affairs and social protection.
  - A selective, structural reduction is compatible with growth.

  The Cour des comptes is in the same camp. In June 2026 it noted that spending excluding tax credits (56.6% of GDP in 2025) is 2.0 points above its pre-crisis level, an "effet de cliquet" (ratchet effect), and that the 2026 targets "reportent encore les efforts" (postpone the effort again) [^ccomptes]. (Corrected after verification: the sentence was garbled and duplicated.)

### 10.7 Where economists broadly agree

- Pensions and health are the two functions where France's spending/GDP is structurally above peers. Together they explain about half the gap with the euro area.
- Interest is becoming a major driver of spending growth. It accounts for 28-30% of spending growth in 2026-2027 [^hcfp].
- Revenue measures carried most of the 2025 consolidation and most of the 2027 plan [^ccomptes] [^hcfp].

---

## 11. Open questions, gaps and data files

### 11.1 Gaps and items not verified

- **COFOG 2025** (Insee and Eurostat) is not yet published: Insee scheduled December 2026. The functional breakdown stops at 2024 (provisional).
- **Drees 2026 edition** (2025 data) was not found. The latest is the December 2025 edition (2024 data: 31.9% of GDP).
- **PPS price level indices**: the old table (prc_ppp_ind, last updated 2025-07-10) stops at 2024. (Update 2026-10-25: it is superseded by `prc_ppp_ind_1`, updated 2026-07-09, covering 2025; §6.4, including the function-level rows, was recomputed on it.) *(Reconciliation note: file 09 computes 2025 with TE/GDP x GDP per capita in PPS from nama_10_pc, updated Oct 2026: 23,330 PPS, 8th of 27. That is the canonical value.)*
- **OECD SOCX net total** stops at 2021. Gross public 2024 values are estimates for 24 countries only.
- **OECD averages** are this file's unweighted computations from OECD national-accounts tables. Six OECD members are missing for 2024 (Canada, Costa Rica, Korea, Mexico, New Zealand, Türkiye).
- **Euro area**: the historical tables in this file (§3.1, §5.2, §6.1-6.3) use **EA20** (the composition before Bulgaria's entry in 2026). **The canonical website aggregate is EA21** (`00-reference-figures.md` §1); EA21 values are given in §0, K21 and §6.3 notes.
- The **government "1,000 euros" infographic** was read from its alt text only. The image could not be downloaded, and the housing category and the interest figure (31 vs 35 EUR) are not reconciled (see §4.2 for the most plausible explanation and the recommendation to use 35).
- The **PLF 2027 *Rapport économique, social et financier*** (6 Oct 2026) was not read directly. Projections come from the HCFP opinion of 1 Oct 2026.
- **NATO defense figure**, **IMF Article IV 2026**, **European Commission** fiscal assessments and **IPP** work were not consulted for this topic.
- **Discretionary tax cuts**: the aggregate for 2018-2023 is now sourced (Cour des comptes, EUR 62 bn = 2.2 pts of GDP in 2023). A measure-by-measure breakdown, and 2024, were not quantified.
- **COFOG by subsector** (State vs ODAC vs APUL vs ASSO) was not computed. Insee publishes it (State/ODAC split from 2009).
- **Real (volume) growth of spending over 1995-2025** was not computed. Only nominal growth and ratios are given.

### 11.2 Data files and scripts produced for this file (all under `research/`)

| File | Content | Origin |
|---|---|---|
| `data/01_eurostat_gov_10a_main.csv` | TE, TR, B9 and economic-nature items; S13, S1311, S1313, S1314; MIO_EUR and PC_GDP; 1995-2025; all countries | Eurostat API gov_10a_main (updated 2026-10-21) |
| `data/01_eurostat_gov_10a_exp_{pcgdp,mioeur,pctot}.csv` | COFOG divisions and groups, S13, 1995-2024 | Eurostat API gov_10a_exp (updated 2026-10-21) |
| `data/01_eurostat_nama_10_gdp.csv`, `01_eurostat_nama_10_pe.csv`, `01_eurostat_prc_ppp_ind_pli.csv` | GDP, population, price level indices | Eurostat API |
| `data/01_eurostat_ilc_li02.csv`, `ilc_li09`, `ilc_li10`, `01_eurostat_demo_mlexpec.csv` | Poverty before and after transfers; life expectancy | Eurostat API |
| `data/01_derived_fr_series_1995_2025.csv` | France annual series with EA/EU benchmarks and panel | [computed] |
| `data/01_derived_cofog_international_2024.csv` | COFOG 2024 comparison: means, medians, ranks, gaps, PPS (PPS columns on the superseded July 2025 PLI vintage; use the next file) | [computed] |
| `data/01_derived_cofog_pps_pc_pli1.csv` | §6.4 PPS per capita by COFOG function (2024) and TE history, on `prc_ppp_ind_1` (2026-07-09); script `scripts/topic01/analyze01d_pps_pli1.py` | [computed] |
| `data/01_oecd_cofog_pcgdp_derived.csv` | OECD COFOG ratios | [computed] from OECD SDMX |
| `data/01_oecd_socx_gross_net_pcgdp.csv` | SOCX gross public, net public and net total | OECD SDMX |
| `data/raw/eurostat_01/`, `data/raw/oecd_01/`, `data/raw/insee/`, `data/raw/fipeco/`, `data/raw/hcfp/`, `data/raw/cor/` | Raw downloads (JSON, CSV, PDF, text extracts) | Sources below |
| `scripts/topic01/*.py` | JSON-stat converter and analysis scripts | Author |

---

## 12. Sources (accessed 2026-10-25)

[^es-main]: Eurostat, *Government revenue, expenditure and main aggregates* (gov_10a_main), dataset updated 2026-10-21. https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table. API: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_main
[^es-cofog]: Eurostat, *General government expenditure by function (COFOG)* (gov_10a_exp), dataset updated 2026-10-21 (2024 provisional). https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table. API: https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_exp
[^es-gdp]: Eurostat, *GDP and main components* (nama_10_gdp), updated 2026-10-22. https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table
[^es-pop]: Eurostat, *Population and employment* (nama_10_pe), updated 2026-10-21. https://ec.europa.eu/eurostat/databrowser/view/nama_10_pe/default/table
[^es-pli]: Eurostat, *Purchasing power parities, price level indices* (prc_ppp_ind), API "updated" 2025-07-10 (confirmed on re-download 2026-10-25; latest year 2024). **Superseded** (checked 2026-10-25): Eurostat's current table is `prc_ppp_ind_1` (dimension `ppp_cat18`), API "updated" 2026-07-09, years to 2025; §6.4 now uses it (local extract `data/13_eurostat_prc_ppp_ind_1_PLI_GDP.csv`). https://ec.europa.eu/eurostat/databrowser/view/prc_ppp_ind/default/table ; https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/prc_ppp_ind_1?geo=FR&indic_ppp=PLI_EU27_2020&ppp_cat18=GDP
[^es-pc]: Eurostat, *Main GDP aggregates per capita* (nama_10_pc), API "updated" 2026-10-22. https://ec.europa.eu/eurostat/databrowser/view/nama_10_pc/default/table
[^es-spr]: Eurostat, ESSPROS *Expenditure on social protection by function* (spr_exp_func), unit PC_GDP, spfunc TOTAL, 2024; API "updated" 2026-10-23 (EU27_2020 27.41, FR 31.96, FI 32.46). https://ec.europa.eu/eurostat/databrowser/view/spr_exp_func/default/table
[^ccomptes24]: Cour des comptes, *La situation et les perspectives des finances publiques*, July 2024 (dated 15 July 2024), ch. 1, section C "*Des baisses d'impôts et de cotisations depuis six ans qui ont contribué à la dégradation du déficit public*", pp. 35-36. https://www.ccomptes.fr/sites/default/files/2024-09/20240715-RSPFP-2024.pdf
[^es-silc]: Eurostat, EU-SILC: ilc_li02 (updated 2026-10-20), ilc_li10 and ilc_li09 (updated 2026-10-20). https://ec.europa.eu/eurostat/databrowser/view/ilc_li02/default/table ; https://ec.europa.eu/eurostat/databrowser/view/ilc_li10/default/table ; https://ec.europa.eu/eurostat/databrowser/view/ilc_li09/default/table
[^es-le]: Eurostat, *Life expectancy by age and sex* (demo_mlexpec), updated 2026-09-25. https://ec.europa.eu/eurostat/databrowser/view/demo_mlexpec/default/table
[^ip2106]: Insee, Beaujour Bourget M., Guessé N. et al., « Le compte des administrations publiques en 2025 », *Insee Première* no. 2106, May 2026. https://www.insee.fr/fr/statistiques/8997691 (PDF: https://www.insee.fr/fr/statistiques/fichier/version-html/8997691/ip2106.pdf). Related data: « Finances publiques en 2025 », https://www.insee.fr/fr/statistiques/8988841 ; first estimate *Informations Rapides* no. 78 (26 March 2026), https://www.insee.fr/fr/statistiques/8956575
[^ip2093]: Insee, Diaz M., « Usage de l'argent public : les dépenses publiques par fonction en 2024 », *Insee Première* no. 2093, February 2026. https://www.insee.fr/fr/statistiques/8735252 (PDF: https://www.insee.fr/fr/statistiques/fichier/8735252/IP2093.pdf)
[^insee-cofog24]: Insee, « Dépenses des administrations publiques ventilées par fonction en 2024 », Insee Résultats, comptes nationaux base 2020 (27 March 2026). https://www.insee.fr/fr/statistiques/8574707 (English: https://www.insee.fr/en/statistiques/8574788)
[^insee-cofog25]: Insee, « Dépenses des administrations publiques ventilées par fonction en 2025 » (tables 3.301-3.307 announced for December 2026). https://www.insee.fr/fr/statistiques/8988847
[^insee-blog]: Insee, Hauseux Y., Houriez G., « Privatisations ou nationalisations, retraites des fonctionnaires, crédits d'impôts : quelles conséquences sur les dépenses et les recettes dans les comptes publics ? », *Le blog de l'Insee*, 24 October 2025. https://blog.insee.fr/depenses-et-recettes-des-comptes-publics/
[^drees]: Drees, *La protection sociale en France et en Europe en 2024 - Résultats des comptes de la protection sociale*, Panoramas de la Drees, 2025 edition (17 December 2025). https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/panoramas-de-la-drees/251217-protection-sociale-france-europe-2024
[^cor]: Conseil d'orientation des retraites (COR), *Rapport annuel - Évolutions et perspectives des retraites en France*, June 2026, synthesis. https://www.cor-retraites.fr/sites/default/files/2026-06/Synth%C3%A8se_RA_2026.pdf ; full report: https://www.cor-retraites.fr/sites/default/files/2026-06/RA_2026_def.pdf (read 2026-10-25: 422.2 bn, 14.1% of GDP and 24.3% of public spending, Part 2 ch. 2, pp. 65-66, Figure 2.1; scope "y compris FSV, hors RAFP")
[^hcfp]: Haut Conseil des finances publiques (HCFP), *Avis no. 2026-5 relatif aux projets de lois de finances et de financement de la sécurité sociale pour l'année 2027*, dated 25 September 2026 (cover page), published with the PLF on 1 October 2026 (corrected 2026-10-25: was "1 October 2026"). https://www.hcfp.fr/liste-avis/avis-ndeg2026-5-lois-de-finances-2027 (PDF: https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf)
[^ccomptes]: Cour des comptes, *La situation et les perspectives des finances publiques*, June 2026 (synthesis dated 25 June 2026). https://www.ccomptes.fr/fr/publications/la-situation-et-les-perspectives-des-finances-publiques-17 (synthesis PDF: https://www.ccomptes.fr/sites/default/files/2026-06/20260625-synthese-RSPFP-2026.pdf). *Content used here comes from search summaries of the synthesis and press coverage; the PDF was not read in full.* (Verification note: the synthesis PDF was downloaded and read on 2026-10-25. It confirms EUR 23 bn of tax increases plus EUR 28 bn of spontaneous revenue growth in 2025, spending excluding tax credits of EUR 1,694.0 bn (56.6% of GDP, +1.4% in volume) and the "reportent encore les efforts" wording.)
[^fipeco-fn]: Fipeco (François Ecalle, former Cour des comptes magistrate; independent site, generally favoring spending restraint), « Les dépenses par politique publique en Europe en 2024 », 8 July 2026. https://www.fipeco.fr/pdf/D%C3%A9pensesFonctions2024.pdf
[^fipeco-ap]: Fipeco (F. Ecalle), « A quoi l'argent public a servi en 2024 », 22 January 2026. https://www.fipeco.fr/pdf/Argent%20public%202024.pdf
[^fipeco-ratio]: Fipeco (F. Ecalle), « Le rapport des dépenses publiques au PIB : pertinence et comparabilité », 15 January 2025. https://fipeco.fr/pdf/D%C3%A9pensesPIB2025.pdf
[^aqsmi]: Ministère de l'Économie / Ministère de l'Action et des Comptes publics, *À quoi servent mes impôts ? - Comment sont utilisés mes impôts ?* (infographic "Que financent 1000 € d'impôts", 2024 data, Insee/DG Trésor). https://www.economie.gouv.fr/aqsmi/comment-sont-utilises-mes-impots
[^oecd-t11]: OECD, *Annual government expenditure by function (COFOG)*, Table 11 (DSD_NASEC10@DF_TABLE11), and *Annual GDP and components - expenditure approach*, Table 1 (DSD_NAMAIN10@DF_TABLE1_EXPENDITURE), OECD Data Explorer/SDMX. https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NASEC10@DF_TABLE11,/ ; https://sdmx.oecd.org/public/rest/data/OECD.SDD.NAD,DSD_NAMAIN10@DF_TABLE1_EXPENDITURE,/
[^socx]: OECD, Social Expenditure Database (SOCX): *Net total social expenditure in % GDP* (DSD_SOCX_AGG@DF_NET_GDP) and *SOCX aggregates* (DSD_SOCX_AGG@DF_SOCX_AGG). https://sdmx.oecd.org/public/rest/data/OECD.ELS.SPD,DSD_SOCX_AGG@DF_NET_GDP,1.0/all ; https://www.oecd.org/en/data/datasets/social-expenditure-database-socx.html
[^ofce]: OFCE, Ducoudré B., Plane M., Sampognaro R., « Dépenses publiques : quels enjeux pour le prochain quinquennat ? », *OFCE Policy Brief* no. 17, 19 April 2017 (OFCE: Sciences Po's economic research center, generally Keynesian-leaning). https://www.ofce.sciences-po.fr/pdf/pbrief/2017/pbrief17.pdf. *The summary page was read; the full text was not.*
[^cae]: Conseil d'analyse économique, Bacache-Beauvallet M., Bureau D., Giavazzi F., Ragot X., « Quelle stratégie pour les dépenses publiques ? », *Note du CAE* no. 43, July 2017. https://cae-eco.fr/static/pdf/cae-note043v2.pdf. *The summary page was read.*

---

## Verification log (2026-10-25)

An adversarial fact-check was run on 2026-10-25. Fresh downloads were saved under `data/raw/factcheck_01/` and the check scripts were kept outside the project. Every check below was re-run against the live source or API, not the researcher's own derived files, except where stated.

### Checked and confirmed

| Claim | Check performed | Result |
|---|---|---|
| TE 2025 EUR 1,714.1 bn, 57.3% of GDP; revenue 52.2% (EUR 1,562.5 bn); deficit EUR -151.6 bn, -5.1% | Eurostat gov_10a_main re-downloaded (updated 2026-10-21) | Confirmed |
| Insee: TE EUR 1,714.2 bn; revenue EUR 1,561.7 bn; deficit EUR 152.5 bn; *prélèvements obligatoires* 43.6%; debt 115.7% (EUR 3,460.5 bn); D62+D632 EUR 771.0 bn; D1 EUR 370.0 bn; interest EUR 64.7 bn (State EUR 53.3 bn); central government transfers EUR 63.0 / 40.7 / 22.4 bn; pensions +EUR 13.2 bn (+3.3%); new tax measures EUR 23.0 bn; State balance -128.1, ODAC -2.2, APUL -15.6, ASSO -6.7 | Insee IP 2106 PDF re-downloaded from insee.fr | Confirmed |
| Per capita ≈ EUR 24,800 | 1,714,111.7 / 68,998 thousand = EUR 24,843 | Confirmed |
| Full 1995-2025 series (TE, revenue, balance, interest, EA20/EU27 aggregates, gaps incl. 10.3 pp in 2017) | Recomputed from gov_10a_main PC_GDP | Confirmed (all rows) |
| EU27/EA20 unweighted means, medians and France's ranks for 2005, 2010, 2015, 2019, 2024 and 2025; 2025 ranking list; panel TE/revenue/balance (Denmark's 2025 revenue really is missing) | Recomputed | Confirmed |
| Economic-nature table (D1, P2, D62, D632, D3, D41, P51G) for FR/EA20/EU27 and the panel, 2025 | Recomputed | Confirmed |
| Subsectors 1995/2005/2015/2025 (S1311, S1313, S1314), balances, consolidation | Eurostat re-download | Confirmed |
| COFOG 2024 EUR bn, % of TE and % of GDP (recomputed on GDP EUR 2,935.2 bn); published PC_GDP 57.3% vs recomputed 56.96% | gov_10a_exp re-download (2024 still flagged "p") | Confirmed |
| COFOG EU27/EA20 means, medians and ranks (spot-checked: total, GF07, GF10, GF1002, GF1005, GF09, GF02, GF06) | Recomputed | Confirmed |
| Gap decomposition vs EA20 (7.77 / 3.57 / 2.50 / 1.45 / 0.71 / 0.49 / 0.46 / 0.44 pp; 2005 column) | Recomputed GDP-weighted | Confirmed |
| PPS per capita 2024: FR 22,321, rank 9/27, mean 18,735, median 16,537, panel values | Recomputed (PLI dataset last updated 2025-07-10) | Confirmed on that vintage; **superseded**: recomputed on `prc_ppp_ind_1` on 2026-10-25 (22,383, 9th; see §6.4) |
| OECD Table 11 by division 2024 (social protection 23.6, rank 2/32; health 8.9, rank 5, US 10.3; old age 13.4, rank 4/30) | Fresh OECD SDMX download of numerators; GDP denominators from the researcher's OECD Table 1 file (fresh GDP download blocked by a Cloudflare challenge; France's GDP matches Eurostat exactly) | Confirmed |
| OECD total 2024: FR 57.0, rank 2/32, mean 44.7, median 46.0, US 39.6, Finland 57.7; 2005/2015/2019 rows | Recomputed from researcher's raw OECD files | Confirmed (not independently re-downloaded) |
| SOCX net total 2021: US 33.24, FR 31.95 (2nd of 38); 2019: FR 30.13, US 29.19; gross public 2021 FR 32.7, US 21.6, OECD 22.1; private FR 3.6, US 12.8 | Fresh OECD SDMX download | Confirmed (France's value rounding corrected, see below) |
| Poverty: AROP 16.3% = EU27, rank 17, median 15.6; before transfers 26.5%; reduction -10.2 pp, 6th, mean -8.1; before all transfers 46.8%, 2nd highest; life expectancy 83.0, 7th | Eurostat ilc_li02/li10/li09 (MED_EI, B_60) and demo_mlexpec re-downloaded | Confirmed |
| HCFP: 56.6 → 57.1 → 56.9% of GDP; EUR 1,694 / 1,742 / 1,782 bn; interest 66 / 79 / 91; pensions 346 / 354 / 363; LPM 51 / 57 / 63; Ondam 265 / 273 / 279; 28% / 30% contributions; value / volume growth (Tables 8-9); EUR 17 bn vs 11 bn (0.5 / 0.4 pt); interest 2.2 / 2.6 / 2.9% of GDP; debt 119.3 / 121.7% | HCFP Avis 2026-5 PDF re-downloaded | Confirmed |
| COR: EUR 422 bn, 14.1% of GDP, 24.3% of public spending; 14.1% (2030), 14.2% (2045), 15.3% (2070); resources 13.9% → 12.9%; balance -0.2% → -2.4%; fertility 1.45; 6th per capita | COR June 2026 synthesis re-downloaded | Confirmed (per-capita data year added, see below) |
| Drees: 31.9% of GDP (2024), EU27 27.3%, 2nd after Finland | Drees CPS 2025 edition, fiche 12 (the Drees web page is JavaScript-only; text read from the PDF archived in `data/raw/drees/`) | Confirmed. No 2026 edition (2025 data) has been published yet; it is normally released in December. |
| IP 2093: shares 41/16/11/10/9%; EUR 693 / 261 / 181 / 166 / 149 bn; defense EUR 54.2 bn incl. EUR 21.5 bn compensation; +7.8%/yr growth 2021-24; 2014-24 changes (+165 bn, -0.8 pt; health +82 bn, +0.6 pt; share changes); +18.3% housing artifact; provisional status; DEPP EUR 197.1 bn = 6.8% of GDP | IP 2093 PDF re-downloaded | Confirmed |
| Insee: COFOG 2025 tables to be published December 2026 | insee.fr/fr/statistiques/8988847 (page dated 29/05/2026) | Confirmed |
| Insee blog: tax credits EUR 19.8 bn (peak 39.8 in 2017); imputed contributions 1.8% of GDP; own-account production EUR 33 bn (1.1% of GDP, 1.9% of TE); France-EU gap 5.2 → 7.9 pp, 10.7 / 9.7 in 2017; PO 42.8 vs 45.2; about EUR 400 bn of transfers; EDF as a financial transaction | Blog page re-downloaded | Confirmed |
| Fipeco 8 Jul 2026: 57.3 vs 49.1; pensions 14.8 vs 12.2 (+2.6 pp); health 11.8 vs 10.2 (+1.6 pp); housing 2.1 vs 1.1; employer pension contributions 0.9-4.0% of GDP (France and Belgium 4.0%); 78.3% vs 16.7% rate | PDF re-downloaded | Confirmed (one wording corrected, see below) |
| Fipeco 22 Jan 2026: 571 / 259 / 206 / 40 / 29 / 89 / 99 (63 + 36) / 61 / 32 / 35; EUR 1,672 bn = 57.2% of GDP | PDF re-downloaded | Confirmed |
| Fipeco 15 Jan 2025: 51.4% corrected (2nd), Finland 52.3, Italy 50.0, Germany 45.8; government value added 18.4% (EA 14.1, EU 14.5, DE 11.6); pensions public plus private 14.2% in 2019, 2nd after Italy | PDF re-downloaded | Confirmed (vintage note added) |
| Government infographic "1,000 EUR of taxes" (561 / 88 / 66 / 59 / 50 / 31 / 31 / 25 / 25 / 30 / 17 / 11 / 5) | Page loaded in a headless browser; alt text re-read | Confirmed |
| Cour des comptes June 2026: EUR 23 bn of tax increases; efforts postponed | Synthesis PDF re-downloaded and read | Confirmed |
| OFCE Policy Brief 17 (US public pensions and health -8 pp, total +2 pp; public employment 20%, slightly below the OECD average; post-2008 ratio rise due to weak growth) and CAE Note 43 (57% vs 48.5% OECD in 2015; excess in economic affairs and social protection; not driven by public employment) | PDFs re-downloaded | Confirmed |
| Think-tank orientation flags (Fipeco: restraint-leaning; OFCE: Keynesian-leaning) | Read | Present and fair. The steelman sections present opposing views with sources and are not strawmen. |

### Corrected

1. **Summary item 8**: the figures for compensation (12.4 vs 10.0) and cash benefits (19.4 vs 16.9) were labeled "2024" but are **2025** values. The 2024 values are 12.4 vs 9.9 and 19.2 vs 16.7.
2. **SOCX France 2021 net total**: the raw value is 31.95, which rounds to **32.0%**, not 31.9% (summary item 7 and §10.2). The conclusion (US > France) is unchanged.
3. **Fipeco July 2026**: "transport is the only function well below the EU average" was changed to **"transport and energy policies"**, as the source says.
4. **§10.6**: a garbled, duplicated sentence about the Cour des comptes was rewritten with the verified content of its June 2026 synthesis.
5. **COR per-capita ranking**: added that it uses **2021 SOCX data, public plus private** (it is not a 2025 figure) and that France is 2nd *after Italy* on pensions/GDP. Added the Drees 2024 corroboration (France 9th per capita in PPP, Finland 32.5% of GDP).
6. **2024 *prélèvements obligatoires***: Insee revised the rate to 42.7% in IP 2106 (May 2026); 42.8% is the October 2025 vintage.
7. **§6.3 gap series**: flagged a 0.1 pp inconsistency between the COFOG-based gap series (8.4 / 7.5 / 7.8) and the gov_10a_main series in §3.1 (8.3 / 7.6 / 7.7).
8. **Fipeco double-counting correction (§8.5)**: flagged that it rests on the early-2025 data vintage (France 57.0%, ranked 1st at the time).

### Left unverified / caveats

*(Status after the second pass of 2026-10-25 in brackets; details in the next section.)*

- "Since about 2023" as the start date of the government's "excluding tax credits" concept. [Corrected: in law since at least the LPFP 2018-2022.]
- The list of 2017-2024 tax measures in the §10.4 steelman and their EUR amounts. [Replaced by the Cour des comptes' EUR 62 bn = 2.2 pts (2018-2023) and its own list of measures.]
- The 1,000 EUR interest discrepancy (31 vs 35). [Still ⚠ unreconciled; use 35.]
- PLI (prc_ppp_ind) last updated 2025-07-10. [Confirmed superseded by prc_ppp_ind_1; total and function-level rows recomputed (2026-10-25).]
- OECD total spending ratios (2005-2024). [Confirmed on a fresh OECD download.]
- NATO defense figures, IMF, European Commission and IPP sources were not consulted, as the original file already states. [Unchanged; out of scope.]
- Scope of the COR pension aggregate ("incl. FSV, excl. RAFP"). [Confirmed in the full COR report.]

### Second pass (2026-10-25): residual inconsistencies and ⚠ items

Scope: README §7 (row 01) and §8 (items 1-3), aligned with `00-reference-figures.md`. New downloads are under `data/raw/verify2_01/`. File 01 contained no flag for the Ifop 86% poll, PISA 2025 or the PLF 2027 staffing plan, so none had to be removed.

**Residual inconsistencies fixed (README §8)**

| # | Location | Was | Now |
|---|---|---|---|
| 1 | §2 K22; §0 item 6; §6.4 | 22,321 PPS, 9th of 27 (2024), unlabeled as superseded | **23,330 PPS, 8th of 27 (2025)**; 2024: 22,398 (8th, `nama_10_pc` method) or 22,395 (9th, new PLI table), a tie with Sweden. The §6.4 table has since been recomputed on `prc_ppp_ind_1` (all rows). |
| 2 | §2 K21; §3.1 header; §5.2 total; §11.1 | +7.5 pp vs EA20, unlabeled | **+7.6 pp vs EA21 ≈ EUR 227 bn** (canonical), EA20 +7.5 / 225 bn in brackets; EA20 tables now say they are not canonical. |
| 3 | §2 K18 | Drees EU-27 27.3% with no source stated | **Eurostat ESSPROS EU-27 27.4% (27.41)**, re-downloaded (`spr_exp_func`, 23 Oct 2026); Drees' 27.3 is named as an earlier vintage. |
| - | §2 K15, §4.1, §9 | Defense 1.9% of GDP | 1.85%, shown as **1.8%** (00 row 15; README §8 item 5 "use it everywhere"). |
| - | §0 item 1, §5.1 | Deficit "151.6-152.5 bn", "152 bn" | **151.6 bn** (152.5 = May 2026 vintage). |
| - | §0 item 10, §10.5 | Interest "66 → 79 → 91" | **65.7 → 79.2 → about 91** (00 rows 39-40). |
| - | K23, [^hcfp] | HCFP opinion "1 Oct 2026" | Dated **25 Sep 2026**, published 1 Oct 2026 (00 log #18). |

**⚠ items resolved**

| Item | Outcome | Evidence |
|---|---|---|
| "Excluding tax credits" concept "since about 2023" | **Corrected.** The indicator "*Dépense publique, hors crédits d'impôts*" is in art. 5 of the LPFP 2018-2022 (law 2018-32 of 22 Jan 2018): 54.7% of GDP in 2017 → 51.1% target for 2022. | https://www.legifrance.gouv.fr/loda/id/JORFTEXT000036526027 (read via WebFetch) |
| §10.4 list of tax measures, amounts | **Replaced** by a primary source: Cour des comptes RSPFP July 2024, pp. 35-36: tax cuts 2018-2023 = **EUR 62 bn in 2023 = 2.2 pts of GDP**, listing corporate tax, CVAE, *taxe d'habitation*, social-contribution cuts. Wealth-tax reform and flat tax no longer listed (not itemized by the Cour). | https://www.ccomptes.fr/sites/default/files/2024-09/20240715-RSPFP-2024.pdf (`verify2_01/rspfp2024.pdf`) |
| Newer Eurostat PPP table | **Confirmed superseded**: `prc_ppp_ind_1`, updated 2026-07-09, covers 2025. Recomputed TE per capita: 2024 FR 22,395 (9th, Sweden 22,399); 2025 FR 23,327 (8th). Matches file 13 (22,395; 23,327) and is within 3 PPS of the canonical 23,330. | `verify2_01/pps_recheck_2026-10-25.txt` |
| OECD TE ratios (fresh download blocked) | **Confirmed.** OECD SDMX Table 11 (S13, total) and Table 1 (B1GQ, current prices) fetched through the laptop browser (curl got a Cloudflare 524). OECD-38 only: 2005 FR 54.3, 1st/31, mean 42.6, median 43.4; 2015 57.6, 1st/33, 43.4, 43.0; 2019 55.3, 1st/34, 41.8, 42.1; 2024 57.0, 2nd/32 (Finland 57.7), 44.7, 46.0; US/JP/UK all identical to §6.1. France's 2024 GDP (EUR 2,935,236.2 m) equals Eurostat's. | `verify2_01/oecd_te_recheck_2026-10-25.json` |
| COR aggregate scope | **Confirmed.** Every COR figure note reads "*ensemble des régimes de retraite français légalement obligatoires, y compris FSV, hors RAFP*"; 422.2 bn = 14.1% of GDP and 24.3% of public spending (pp. 65-66, Figure 2.1, numerator excl. financial charges and provisions). | https://www.cor-retraites.fr/sites/default/files/2026-06/RA_2026_def.pdf (`verify2_01/cor_ra2026.pdf`) |

**Still ⚠ unverified**

| Item | Why | Recommendation |
|---|---|---|
| Government infographic "1,000 EUR": interest 31 vs COFOG 35 | The page (loaded in the browser) gives no method, only "*données 2024 source Insee/DG Trésor*" and a link to the *direction du Budget*. Most plausible: State budget debt charge (LFI 2024 EUR 50.86 bn ≈ 30 per 1,000, Senate figure via search), not confirmed. | **Replace by the verified COFOG/Fipeco value (35 per 1,000)**; do not cite the infographic's 31. |
| §6.4 function-level PPS rows (old PLI vintage) | **Recomputed** with `prc_ppp_ind_1` (2026-10-25): values move by less than 1.5%; only education's rank changes (12th to 11th). | Resolved; `data/01_derived_cofog_pps_pc_pli1.csv`. |

### Link status (2026-10-25)

All cited insee.fr, blog.insee.fr, hcfp.fr, cor-retraites.fr, ccomptes.fr, fipeco.fr, ofce.sciences-po.fr, cae-eco.fr and Eurostat URLs returned HTTP 200. **economie.gouv.fr/aqsmi** and **oecd.org/.../social-expenditure-database-socx.html** return 403 to command-line clients (bot protection) but are not dead: the aqsmi page loads in a browser. The **Drees** page requires JavaScript. No dead links were found.
