# Economists' Disagreements and the Strongest Counter-Arguments to the Platform Thesis

*Research file 10. Prepared 2026-10-25. Reference base for a French educational platform on public finances ahead of the 2027 presidential election.*

> **Purpose.** The platform's thesis is: *"France's fiscal problem is mainly the level and structure of public spending; proposals to 'tax the rich' cannot, on their own, restore public accounts."* A rigorous platform must be able to state, in their strongest form, the objections to this thesis, show the evidence on both sides, and say where (if anywhere) economists agree. This file does that for eight debates.

> **Reading convention.** Every ratio says whether it is **% of GDP** or **% of total public expenditure**. Bracketed codes such as [S3] point to the numbered source list at the end. "Computed" means the statistic was calculated in this session from the raw data saved under `research/data/`.

---

## 0. Executive summary (for editors)

1. **The thesis survives scrutiny on orders of magnitude but not as a monocausal story.** The 2025 deficit was EUR 151.6 bn (5.1% of GDP; October 2026 EDP notification, EUR 152.5 bn in the May 2026 vintage used by the Cour) [S1][S30]. The most ambitious wealth-tax proposal (*taxe Zucman*) is costed at EUR 15-25 bn by its proponents and EUR 2-6 bn by critics [S20][S22]. The CAE's empirical work implies that a reform raising EUR 4 bn mechanically from the top 1% has small macro costs [S18]. So "taxing the rich" can contribute roughly 0.1-0.8 points of GDP, against an adjustment need that the *Haut-commissariat à la Stratégie et au Plan* (HCSP) puts at 4.4 points of GDP (about EUR 140 bn, 2025 euros) by 2031 [S8]. On that point, nearly all sources agree.
2. **But "the deficit comes from spending" is contested on the 2017-2024 window.** On Eurostat data, between 2017 and 2024 France's total revenue (ESA TR, not *prélèvements obligatoires*) fell by 3.1 points of GDP while total spending fell by only 0.7 points (computed, [S30]). Over the same window the Insee PO ratio fell by 2.6 points (45.3 → 42.7) and the Cour des comptes values discretionary tax cuts decided in 2018-2023 at EUR 62 bn (2.2 points); part of the TR fall reflects the CICE's conversion into contribution cuts in 2019. The OFCE reads this as "the deficit increase is, in accounting terms, explained by the fall in *prélèvements obligatoires* (compulsory levies)" [S6]. Rexecode (an employer-funded institute) counts EUR 75 bn (2025 euros) of net tax cuts over 2018-2023 [S27]. Fipeco (Ecalle) counted about EUR 44 bn of unfunded tax cuts by 2022 [S28]. **Using 2019 as the base year instead reverses the picture.** Over 2019-2025, spending rose by 2.0 points of GDP and revenue fell by 0.8 points (computed, [S30]). The Cour des comptes stresses a spending "ratchet effect" (*effet de cliquet*) [S1][S2]. **The honest answer: both. The base year decides which half you see.**
3. **The "France just socializes what others buy privately" argument is partly right.** In 2021, France's *net total* social spending (public plus private, after taxes) was 32.0% of GDP (raw value 31.95), second in the OECD behind the United States (33.2%) (computed from OECD SOCX [S32]). Against the European panel, however, France is still first: 32.0% versus a panel mean of 26.9%. The gap barely shrinks relative to gross public spending (computed). The argument works against the US but not against Germany, Belgium or the Nordics.
4. **"You get something for it" is true for poverty reduction, less so for the poverty level.** Social transfers including pensions cut France's at-risk-of-poverty rate by 30.5 points, the 3rd-largest cut in the EU-27 (EU mean 24.5) (EU-SILC 2025, computed, [S33]). Yet France's post-transfer rate (16.3%) is now **at** the EU-27 level (16.3%), up from 13.6% in 2019. Insee's own national measure is at a series high of 15.4% (2024) [S12]. Outcomes in justice and education are middling or weak relative to spending: 11.3 judges per 100,000 inhabitants versus a Council of Europe median of 17.6 (CEPEJ, 2022 data), and in **PISA 2025** mathematics (published 8 Sep 2026) France scored **458 vs an OECD average of 463, 29th of 38 OECD countries** (2022: 474 vs 472; 2012: 495) [S38][S39]. (Corrected 2026-10-25: was "PISA mathematics fell from 495 (2012) to 474 (2022)", the PISA 2022 vintage superseded by PISA 2025; aligned with file 00 row 49.)
5. **Debt sustainability has moved against the "no urgency" camp in 2025-2026.** The monthly 10-year yield (Maastricht definition, Eurostat) reached 4.44% in September 2026, 97 bp above Germany and **8 bp above Italy** [S34]. France's monthly yield was above Italy's in December 2025-February 2026 and again in August-September 2026, but below it from March to July 2026 (corrected after verification: was "at or above Italy's since December 2025"). Non-residents held 59.7% of negotiable State debt in Q2 2026 [S35]. The HCSP baseline assumes r - g = +0.5 point and projects debt at 140% of GDP in 2035 [S8].
6. **The consolidation literature does not support "spending cuts are painless".** The current consensus, endorsed by the Cour des comptes in June 2026 [S1], is as follows. The narrative-approach evidence (Guajardo-Leigh-Pescatori) finds short-run costs of spending-based and tax-based consolidation roughly comparable. What matters is the *type* of spending or tax, the cycle, and credibility. Alesina-Favero-Giavazzi's "spending-based is less costly" result is a minority position, contested on method. Blanchard-Leigh (2013) found crisis-era multipliers well above the 0.5 that forecasters had assumed [S14][S15][S16].
7. **No representative survey of French economists** on these questions was found (see Section 11). Public opinion surveys exist (Ifop for the *Parti socialiste*, study no. 121870, fieldwork 10-11 Sep 2025, n = 1,000: 86% favor "a 2% tax on wealth above EUR 100 million"; verified in file 14), but they are not evidence on economic effects.

---

## 1. Scope and definitions

| Term | Definition used here | Why it matters |
|---|---|---|
| *Dépense publique* (public expenditure), ESA 2010 | Total expenditure of general government (S13: State, social security, local authorities, central agencies), Eurostat `gov_10a_main` item TE. Insee includes tax credits (*crédits d'impôt*) as spending. | Insee/Eurostat 2025 = 57.3% of GDP. The Cour des comptes excludes tax credits (56.6% in its June 2026 report). The IMF quotes 57.5% [S1][S30][S11]. |
| *Prélèvements obligatoires* (PO, compulsory levies) | Taxes plus actual compulsory social contributions, net of uncollected amounts. Insee nets out tax credits; Eurostat does not. | 2024: **Insee 42.7%** (May 2026 accounts, used by the Cour in June 2026; canonical) vs Eurostat 43.5% of GDP; the February 2026 vintage gave 42.8% [S1][S2]. 2025: Insee 43.6% of GDP vs Eurostat-definition 44.3%, the highest in the euro area, per the Cour [S1]. |
| Total revenue (TR) | All general-government revenue, including sales, property income, and so on. | 52.2% of GDP in 2025 (Eurostat) [S30]. |
| Gross vs net social spending | OECD SOCX: *gross public* = cash and in-kind public social benefits. *Net total* = public plus mandatory/voluntary private social spending, minus direct and indirect taxes clawed back on benefits, plus tax breaks for social purposes. | Main tool for counter-argument 1 [S32]. |
| Tax expenditures (*dépenses fiscales*) | Tax provisions that depart from a benchmark (reduced rates, credits, exemptions). They are recorded as lost revenue, not spending, except tax credits paid out, which national accounts record as spending. | About 474 to 500 items worth EUR 85-88 bn (2026), sources differ (Section 9). |
| Multiplier | Change in GDP for a 1-euro change in deficit-reducing measures. | Section 5. |
| r - g | Average effective interest rate on debt minus nominal GDP growth. | Section 6. |

**Groups used for comparisons.** EU-27 (27 member states). Euro area: the unweighted EA-20 means and medians in Section 12.1 use the 2025 composition (Bulgaria joined on 1 January 2026). **For euro-area *aggregates* (GDP-weighted), the website uses EA21 as in file 00** (e.g., spending gap 2025 +7.6 pp vs EA21, about EUR 227 bn; EA20 +7.5 pp); the gaps computed in this file are against the **EU-27 aggregate** and are labeled as such (added 2026-10-25). OECD-38. Panel: France, Germany, Italy, Spain, Netherlands, Belgium, Sweden, Denmark. Means and medians are **unweighted country statistics** computed here. "EU27 aggregate" is Eurostat's GDP-weighted aggregate.

---

## 2. Key figures table

| # | Indicator | Value | Unit | Data year | Publication date | Source |
|---|---|---|---|---|---|---|
| K1 | General government deficit | 151.6 bn / 5.1 (152.5 bn in the May 2026 vintage used by the Cour) | EUR / % of GDP | 2025 | 21 Oct 2026 | Eurostat EDP notification [S30]; Cour des comptes RSPFP 2026 [S1] |
| K2 | Public expenditure (ESA, incl. tax credits) | 57.3 | % of GDP | 2025 | Oct 2026 (Eurostat update 21 Oct 2026) | Eurostat gov_10a_main [S30] |
| K3 | Public expenditure excl. tax credits | 1,694.0 bn / 56.6 | EUR / % of GDP | 2025 | 25 Jun 2026 | Cour des comptes [S1] |
| K4 | *Prélèvements obligatoires* | 1,305.1 bn / 43.6 ("highest in the euro area") | EUR / % of GDP | 2025 | 25 Jun 2026 | Cour des comptes [S1] |
| K5 | New tax increases in 2025 | 23 bn (plus 28 bn spontaneous growth) | EUR | 2025 | 25 Jun 2026 | Cour des comptes [S1] |
| K6 | Gross debt (Maastricht) | 3,460.1 bn / 115.7 (3,460.5 bn in the May 2026 vintage) | EUR / % of GDP | end-2025 | 21 Oct 2026 | Cour des comptes [S1]; Eurostat [S30] |
| K7 | Interest paid (ESA D.41) | 65.7 bn / 2.2 | EUR / % of GDP | 2025 | 25 Jun 2026 | Cour des comptes [S1] |
| K8 | Change in total revenue 2017-2024 | -3.1 | points of GDP | 2017-2024 | computed | Eurostat [S30] |
| K9 | Change in total expenditure 2017-2024 | -0.7 | points of GDP | 2017-2024 | computed | Eurostat [S30] |
| K10 | Change in total expenditure 2019-2025 | +2.0 | points of GDP | 2019-2025 | computed | Eurostat [S30] |
| K11 | Net tax cuts (new measures) 2018-2023 | 75 bn (39 households, 36 firms) | EUR 2025 constant | 2018-2023 | Jul 2025 | Rexecode DT 97 [S27] (employer-funded) |
| K12 | Adjustment needed by 2031 | 4.4 / about 140 bn (6.4 / about 200 bn incl. defense and climate) | % of GDP / EUR 2025 | 2026-2031 | 17 Jul 2026 | HCSP Focus *Finances publiques* [S8] |
| K13 | *Taxe Zucman* yield, proponents | 20 (range 15-25) | EUR bn per year | ex ante | 2025 | Zucman / EU Tax Observatory, as reported [S20][S22] |
| K14 | *Taxe Zucman* yield, critics | 2-6 | EUR bn per year | ex ante | Oct 2026 | Geerolf (OFCE economist, personal paper) [S20] |
| K15 | Annual departures, top 1% capital income | 0.2 (vs 0.38 whole population) | % of group per year | 2017 | Jul 2025 (v2 Sep 2025) | CAE Focus 118 [S18] |
| K16 | Effective tax rate, top 0.1% vs top 0.0002% | 46 vs 26 | % of "economic income" | 2016 | Jun 2023 | IPP Note 92 [S19] |
| K17 | Net total social spending, France / USA / OECD median | 32.0 / 33.2 / 22.5 | % of GDP | 2021 | OECD SOCX (accessed 2026-10-25) | OECD [S32], computed |
| K18 | At-risk-of-poverty rate after transfers, France / EU-27 | 16.3 / 16.3 | % of population | EU-SILC 2025 (2024 incomes) | Oct 2026 | Eurostat ilc_li02 [S33] |
| K19 | Insee monetary poverty rate | 15.4 (series high since 1996) | % of population | 2024 | 9 Jul 2026 | Insee Première 2117 [S12] |
| K20 | D10/D1 before vs after extended redistribution | 26 vs 3.5 | ratio | 2023 | 16 Apr 2026 | Insee Analyses 118 [S13] |
| K21 | 10-year yield, France / Germany / Italy | 4.44 / 3.47 / 4.36 | % (monthly avg) | Sep 2026 | Oct 2026 | Eurostat irt_lt_mcby_m [S34] |
| K22 | Non-resident share of negotiable State debt | 59.7 (scope: negotiable State debt; Banque de France gives 58.4% for all general-government long-term securities, file 06) | % | Q2 2026 | 2026 | AFT / Banque de France [S35] |

---

## 3. Debate 1: "France's high spending reflects socialized provision that others pay privately"

### 3.1 The counter-thesis (steelman)

Pensions and health care must be financed somehow. In the US, Switzerland and the Netherlands, large parts are financed through mandatory or voluntary private schemes (occupational pensions, private health insurance). These do not appear in public spending, but households pay for them just as they pay *cotisations*. Once tax clawbacks on benefits are netted out and private social spending is added, "total social effort" is similar across rich countries. This is the core finding of Willem Adema's OECD work on *net* social expenditure. A related point, made by both Zucman's critics and his supporters: the high French tax rate on middle incomes is largely the mirror of public pensions (deferred wages) [S20].

### 3.2 Evidence

| Country | Gross public social spending, 2021 | Private (mandatory and voluntary), 2021 | Public plus private, 2021 | **Net total**, 2021 | Gross public, 2024 (provisional) |
|---|---|---|---|---|---|
| France | 32.7 | 3.6 | 36.3 | **32.0** | 30.6 |
| Germany | 28.9 | 3.6 | 32.5 | 28.5 | 27.9 |
| Italy | 29.8 | 2.1 | 31.9 | 26.5 | 27.6 |
| Spain | 28.4 | 1.3 | 29.7 | 26.6 | 25.9 |
| Netherlands | 19.8 | 11.4 | 31.2 | 27.0 | 18.9 |
| Belgium | 29.1 | 1.9 | 31.0 | 26.7 | 28.6 |
| Sweden | 26.3 | 2.8 | 29.1 | 23.9 | 26.1 |
| Denmark | 28.1 | 3.4 | 31.5 | 24.4 | 26.4 |
| United States | 21.6 | 12.8 | 34.4 | **33.2** | 19.8 |
| Switzerland | 17.5 | 13.2 | 30.6 | 26.1 | 16.0 |
| OECD mean (38) | 22.1 | 3.0 (OECD aggregate) | 25.1 | 22.0 | 23.0 (24 countries) |

*All values are % of GDP. Source: OECD SOCX dataflows `DSD_SOCX_AGG@DF_NET_GDP` and `@DF_PUB_PRV`, downloaded 2026-10-25. Files: `data/debates/oecd_socx_net_total_pct_gdp.csv` and `oecd_socx_public_private_pct_gdp.csv` [S32]. Statistics computed here. The latest net-total year is 2021, a COVID-affected year.*

**Ranks (computed):**

- **Net total 2021:** France ranks 2nd of 38 OECD countries (US 1st). OECD mean 22.0, median 22.5. In the European panel, France ranks 1st (panel mean 26.9, median 26.6).
- **Net total 2015:** France ranks 1st of 35 (32.0 vs US 28.9). **Net total 2005:** 1st of 27.
- **Gross public 2021:** France ranks 1st of 38 (32.7). Panel mean 27.9, so France's gap to the panel is 4.8 points of GDP.
- **Net total 2021, gap to the panel:** 5.0 points. **The net adjustment does not shrink France's lead over European peers.** It shrinks the lead only over the US and Switzerland.

### 3.3 Assessment

- **Where the counter-thesis is right.** Against the US the comparison flips: US net total social spending exceeds France's. Measured by public spending only, France's apparent "excess" overstates the difference in what society spends on social risks. The Netherlands has the same total social effort as Germany, but it runs through private pensions.
- **Where it fails.** Against the euro-area and Nordic comparators the platform cares about, France remains the highest social spender on a net-total basis. The gap is 5 points of GDP over the panel mean, roughly EUR 150 bn at 2025 GDP. That is about the size of the deficit. The fiscal problem is a *public* financing problem whatever private spending is elsewhere: privately financed pensions do not create public deficits.
- **Note on composition.** The HCSP reports that old-age (26%) and health/disability (20%) together make up 46% of **total public expenditure**, and other social protection a further 11% [S8]. Cash social benefits (ESA D.62) were 19.4% of GDP in France in 2025, versus an EU-27 aggregate of 16.4%, an EA21 aggregate of 16.8% (canonical comparator, file 00 row 19) and an EU-27 country median of 14.1% (Eurostat, computed [S30]).

**Fair presentation.** Show both gross public and net total. State that "France spends more than others" is robust in Europe but not against the US. Explain that the French choice is a *financing-channel* choice (public pay-as-you-go pensions) as much as a level choice. Do not imply that the extra spending is "waste".

---

## 4. Debate 2: "The deficit comes from tax cuts since 2017" vs "it comes from spending drift"

### 4.1 The two narratives

| | Revenue narrative | Spending narrative |
|---|---|---|
| Main proponents | OFCE (Heyer, Plane, Ragot, Sampognaro, Timbeau) [S6]; Fipeco/Ecalle on 2017-2022 [S28]; **Attac** (alter-globalist NGO) with the *Observatoire de la justice fiscale* and CADTM, report *La dette de l'injustice fiscale* (26 Mar 2025): tax and levy cuts since 2017 cost "at least EUR 308.62 bn" net over 2018-2023, "about 35% of the debt increase", of which about EUR 207 bn for the richest households and large firms (Attac's own estimate, advocacy) [S42]. **Terra Nova** (center-left) is closer to a middle position: its note by G. Hannezo (20 Sep 2024) puts the 2017-2024 tax cuts at about EUR 62 bn but argues that taxing the wealthiest yields at most about EUR 15 bn a year and "cannot" cover the roughly EUR 100 bn adjustment [S43] (verified 2026-10-25) | Cour des comptes [S1][S2]; IMF [S11]; OECD [S10]; **Institut Montaigne** (business-funded, liberal-centrist), *Budget base zéro* (Nov 2025): EUR 140 bn of savings needed by 2029; a revenue-only adjustment would mean a 32.5% standard VAT rate or "at least three new Zucman taxes each year for five years" [S44]; **iFRAP** (free-market), *Revue* no. 270 (Sep 2025), "le mirage des milliards de recettes" [S45] (verified 2026-10-25) |
| Key fact | 2017-2024: deficit +2.4 pts of GDP "explained in accounting terms by the fall in the PO rate (-2.5 pts, OFCE on the pre-May-2026 vintage; -2.6 pts, 45.3 → 42.7, on Insee's May 2026 accounts, file 00 row 27)": -1.6 households, -0.9 firms. Spending stable; transfers -0.8, investment +0.5 [S6]. | Spending 2025 = 2.0 points of GDP above pre-crisis (2019) level despite the end of crisis measures: a "ratchet effect" [S1]. France was highest or second-highest spender in the EU in 2025 [S8][S30]. |
| Cost of tax cuts | About EUR 44 bn in 2022 for all measures of 2017-2022, "not offset by equivalent spending savings" (Fipeco, Jan 2022) [S28]. EUR 66 bn current (EUR 75 bn at 2025 prices) net new measures over 2018-2023 (Rexecode, Jul 2025) [S27]. | Spending grew 1.4%/yr in volume on average over 2005-2025 (HCSP) [S8]. In 2025 it grew 1.4% in volume, faster than GDP, so the spending ratio rose for a second year [S1]. |
| Structural deficit | 2.4% of GDP (2017) to 4.7% (2022), per RESF quoted by Fipeco [S28]. | Same figures, but attributed to the failure to deliver the planned spending savings that were supposed to finance the tax cuts. |

### 4.2 What the data say (Eurostat, computed)

| Window | Δ Total expenditure | Δ Total revenue | Δ Balance | Δ Interest | Reading |
|---|---|---|---|---|---|
| 2017 to 2024 | -0.7 | **-3.1** | -2.4 | +0.2 | Revenue-driven (supports OFCE) |
| 2019 to 2024 | **+1.7** | -1.8 | -3.4 | +0.5 | Both |
| 2019 to 2025 | **+2.0** | -0.8 | -2.7 | +0.7 | Mostly spending-driven (supports Cour) |
| 2005 to 2025 | +3.0 | +1.4 | -1.6 | -0.5 | Spending grew twice as fast as revenue (in points of GDP) |

*All values are points of GDP. Source: Eurostat gov_10a_main (S13, PC_GDP), updated 21 Oct 2026. File: `data/debates/computed_fr_vs_eu27_fiscal_series.csv` [S30].*

**Why the windows disagree.** 2017 was a revenue peak (TR 54.3% of GDP, the highest of the series) after the 2011-2013 tax increases. Rexecode counts EUR 74 bn current of tax increases over 2011-2013 [S27], and the Cour counts 3.8 points of GDP of tax hikes over 2010-2014 [S1]. Starting in 2017 makes the subsequent tax cuts look large. Starting in 2019 captures the COVID and energy-shock spending that was never fully withdrawn.

**International angle.** France's spending gap to the EU-27 aggregate went from 7.1 points of GDP (2005) to a peak of 10.8 (2017) and back to 7.9 (2025). Its revenue gap went from 6.0 to 8.2 (2017) and back to 5.9 (2025) (computed [S30]). The Cour notes that France's PO gap to the euro area narrowed every year from 2018 to 2024 except 2022 [S2].

### 4.3 Where consensus lies

- **Agreed by all:** the 2018-2023 tax cuts were not financed by the spending savings that were announced. Fipeco, the Cour and the OFCE all say so explicitly [S1][S6][S28].
- **Agreed by all:** in 2024-2025 the adjustment came mostly from tax increases. The Cour says the 2025 deficit reduction was "essentially due to tax increases" (EUR 23 bn of new measures), while spending kept growing faster than GDP [S1].
- **Disputed:** whether the *remedy* should mirror the *cause*. Revenue-side economists argue that reversing part of the post-2017 cuts is the natural fix. Spending-side economists answer that France's PO rate is already the highest in the euro area. The Cour says this "reduces margins on revenue and orients the adjustment more towards spending" [S1], and the IMF says the revenue ratio "limits scope for further revenue-based adjustment" [S11].

**Fair presentation.** Show the decomposition table with several base years. Say plainly that "tax cuts since 2017 explain the deficit increase since 2017" is arithmetically true. "France has a spending problem" is also true in level terms. The two claims answer different questions.

---

## 5. Debate 3: Taxing high wealth. What can it raise?

### 5.1 The proposals and their costings

| Proposal | Design | Yield claimed | Contrary estimate | Status (Oct 2026) |
|---|---|---|---|---|
| *Taxe Zucman* (minimum tax) | 2% of wealth above EUR 100 m. Pay the difference if all existing taxes are below 2% of wealth. About 1,800 tax households. | EUR 20 bn/yr (range 15-25). Primary: the bill's *exposé des motifs* says the floor tax "could generate between EUR 15 and 25 bn of additional revenue, according to the economist Gabriel Zucman" (Assemblée nationale bill no. 768, 7 Jan 2025) [S22]. The breakdown "12.5 of 19.4 bn attributed to billionaires" is known only through Geerolf [S20]; ⚠ the EU Tax Observatory note itself was not found on taxobservatory.eu (2026-10-25). Recommendation: keep the 15-25 bn range (sourced to the bill); drop the 19.4/12.5 split from the site. | EUR 2-6 bn once corporate tax is imputed and data are corrected (Geerolf, October 2026) [S20]. Heyer (OFCE): 4 families would pay 11 of the 20 bn, as quoted in [S20]. | Adopted by the Assemblée nationale in Feb 2025; rejected by the Senate in Jun 2025; rejected again in the 2026 budget debate [S20]. Not in PLF 2027 [S9]. |
| Return of the ISF (pre-2018 wealth tax) | Progressive tax on net wealth above EUR 1.3 m | The ISF's abolition cost EUR 3-4.5 bn mechanically (CAE) [S18] | Ex post behavioral losses are disputed (⚠ Rexecode claims about EUR 2.5 bn/yr lost through departures; secondary source, not verified. Recommendation: drop from site; use CAE Focus 118's exit estimates instead) | Proposed by several left-wing parties |
| Differential tax on personal wealth (*Conseil des prélèvements obligatoires*, CPO, report of 1 Dec 2025, rec. 16.2) | Uncapped differential tax at a "moderate" rate on non-professional wealth; the CPO notes that the maximum rate admissible without a cap under constitutional case law lies "between 0.5 and 1.8%". Also tighter Dutreil relief (exemption 75% → 50%) and taxation of income parked in holdings. The whole package is designed to be "globally neutral for public finances" (it also cuts inheritance-tax rates). | Illustration: 0.5% on non-professional wealth above EUR 5 m yields **EUR 1.4 bn before behavioral effects** (CPO report, ch. III, p. 203) [S46]. (Corrected 2026-10-25: was "about EUR 2.7 bn/yr", a press figure not found in the primary report, and "rates of 0.5-1.8%", which is the constitutional ceiling range, not the proposed rate.) | n/a | Recommendation |
| CAE scenarios | +2.6 pt or +5.2 pt effective tax rate on the top 1% of capital income | EUR 2 bn or 4 bn mechanical | Long-run expatriation of 0.06-0.6% or 0.12-1.2% of the group. Activity loss at most -0.03% of turnover and -0.05% of value added [S18]. | Analysis |

**Orders of magnitude (for the platform).** The proponents' central estimate, EUR 20 bn, equals **13% of the 2025 deficit** (EUR 151.6 bn, October 2026 EDP notification, file 00 row 31; corrected 2026-10-25: was computed on the May 2026 vintage, 152.5 bn; the rounded share is unchanged) and about **0.7% of GDP**. Zucman himself frames it as about 0.8 points of GDP, roughly a third of a 2-3-point required effort (as reported in press coverage). Against the HCSP's need of EUR 140 bn by 2031, the range of 2-25 bn covers 1-18%. **No credible source claims that wealth taxation alone closes the deficit.** The steelman is narrower: it is a significant and equitable *contribution*.

### 5.2 Effective tax rates of the very rich (the equity argument)

- **IPP Note 92 (June 2023).** Bach, Bozio, Guillouzouic and Malgouyres used 2016 administrative data linking personal and corporate tax returns. The total effective tax rate rises to 46% for the top 0.1% and then falls to 26% for the top 0.0002% (about 75 households, the "billionaires"). The fall comes from income held as undistributed profits in controlled companies, which pay only corporate tax [S19].
- **Critiques.** These come from Geerolf (an OFCE economist writing in a personal capacity, explicitly polemical) [S20] and from the Senate finance committee.
  1. The IPP base **excludes** pension and unemployment contributions, VAT and property taxes. Comparing it with "the French pay 50%" (the Blanchard/Pisani-Ferry/Zucman op-ed, June 2025) therefore mixes incompatible measures. On the IPP's own base, the top 75 households pay 25.1% versus 26.8% at the P90 threshold, according to the 2025 working-paper update as reported by Geerolf [S20].
  2. Treating a company's retained profits as the owner's personal income conflicts with the principle that tax is personal (Senate report on the Zucman bill, June 2025; Senate information report no. 760, 17 June 2026) [S21].
  3. The data are from 2016, before the PFU flat tax and the ISF-to-IFI reform.
- **What survives.** Even critics concede that taxation becomes *regressive within the top 0.1%* (P99.9 vs P99.999) [S20]. The dispute is about the size and framing, not the sign.

### 5.3 Behavioral responses: ranking the empirical evidence

| Rank (credibility for France 2027) | Study | Setting | Main result | Relevance and caveat |
|---|---|---|---|---|
| 1 | **CAE Focus 118** (Bach, Bozio, Grimprel, Guillouzouic, Landais, Malgouyres, Jul 2025) [S18] | France, administrative data, 2012-2018 reforms (PFL abolition 2013, ISF/IFI and PFU 2017-2018) | 0.2% of the top 1% of capital-income households (about 380,000) leave each year. The 2013 increase raised net departures by 0.04-0.09 pt; the 2017-2018 cuts reduced them by 0.01-0.07 pt. Stock elasticity 0.02-0.18% (0.4-3.6 times the Swedish estimate). (Verification note: these are the figures of the Focus's summary box, *Constat 3*; the body text of the same v2 PDF gives 0.01-0.06 pt and a long-run range of 0.02-0.23%, i.e. 0.3-3.8 times the Swedish estimate. The inconsistency is in the source.) "About 380,000" is the size of the group (households with declared capital income of EUR 30,000 or more in 2016), not the number of departures. Even with a +EUR 4 bn reform, macro losses are ≤0.05% of value added. | Best French evidence. **Caveat stated by the authors:** it covers *exit only*, not the intensive margin (avoidance, base erosion). It cannot be extrapolated to a 2% tax on fortunes above EUR 100 m, which targets households barely affected by past reforms. |
| 2 | **Jakobsen, Jakobsen, Kleven & Zucman (QJE 2020)** [S24] | Denmark, 1989 cut and 1997 abolition | Wealth-tax responses are larger at the very top. The long-run elasticity of taxable wealth to the net-of-tax return is "sizeable at the top". Taxable wealth rises by about **19% after 8 years** for the moderately wealthy (a 1-point cut; simulated **30% after 30 years**) and **31% after 8 years** for the very wealthy (simulated **65% after 30 years**, which the authors call an upper bound on real accumulation responses); mechanical effects are more than one-third of the 30-year total (QJE accepted version, Aug 2019, Section I) [S24]. (Corrected 2026-10-25: was "a permanent 1-point cut raises top wealth by about 30% over 30 years", the Senate report's wording [S21], taken from the CPO; in the paper, 30% over 30 years is the *moderately wealthy* (98th-99th percentile) result, and the top result is 65%.) | Co-authored by Zucman. Shows that the *base* responds a lot, mainly through saving and accumulation. |
| 3 | **Brülhart, Gruber, Krapf & Schmidheiny (AEJ: Policy 2022)** [S25] | Swiss cantons | A 1 pt lower wealth-tax rate raises reported wealth by at least 43% after 6 years. 24% of this is mobility and 21% house prices; savings explain little, which suggests **evasion and under-reporting**. | Intra-national mobility (cantons) is much easier than international mobility. Strongest evidence that the *declared* base is elastic. |
| 4 | **Agrawal, Foremny & Martínez-Toledano** (Spain, Madrid) [S26] | Madrid's 0% regional wealth tax after 2011 | Published version (*AEJ: Applied Economics* 17(1), Jan 2025, pp. 402-430): the wealthy population in Madrid rose by **about 7.5% by six years** after the 2011 reintroduction, and fell by 1.7% in other regions (elasticity to the net-of-tax rate on wealth 7.96). Other regions forgo 5% of wealth-tax revenue through mobility. "Wealth tax mobility responses generate losses to personal income tax revenues that are six times larger than the direct losses to wealth taxes" (abstract). (Corrected 2026-10-25: was "+9-10% after 5 years", the figures of the 2020-2021 working-paper drafts.) [S26] | Again intra-national, and the authors warn against generalizing to international mobility; some moves were fraudulent changes of fiscal residence. Shows fiscal externalities. |
| 5 | **Ring (NBER WP 35854, Oct 2026)**, Norway 2021-2025 [S23] | 2022 rate increase, followed by high-profile moves to Switzerland | Reform-driven out-migration cut the revenue gain only from +75% (counterfactual, absent any out-migration, 2021-2024) to +71.5%. "At most 100 individuals" left because of the reforms (an upper bound); firms kept operating and investing. Norwegian Ministry of Finance count: 82 relocations in 2022-2023 (secondary). | Recent and directly relevant to the "exodus" narrative. Only the summary was read; not peer-reviewed at the time of writing. |
| 6 | **Pichet** (2007) on the French ISF | France, back-of-envelope | Claimed large capital flight (order of EUR 200 bn) and net fiscal losses. | ⚠ **Not verified** (primary paper not retrieved; web search budget exhausted on 2026-10-25). Methodology criticized as non-causal. Recommendation: drop from site (CAE Focus 118 supersedes it as French evidence). |
| — | "26 cents per euro" (Scandinavian estimate reported by the CAE) | CAE Focus 118 (Jul 2025, section on the intensive margin) reports that, "in the Scandinavian context", Jakobsen et al. (2024) find that for each euro mechanically raised by higher taxation of high wealth, **54 cents disappear through intensive-margin responses and 20 cents through the extensive margin (exit)**, i.e. behavioral responses cut revenue by **74%** relative to the mechanical effect; 26 cents remain [S18]. | — | **Source located (verified 2026-10-25).** It is a Scandinavian estimate *quoted* by the CAE, not a CAE estimate for France; Geerolf's phrasing "the CAE estimates that one euro of tax brings in only 26 cents" [S20] overstates it. This 74% is also the "75% revenue loss" behind the press's "5 bn, not 20 bn" reading; co-author Landais said it does not transfer to the Zucman design (press report). The CAE draws the opposite emphasis: the public debate "probably targets the wrong margin" (exit) rather than avoidance. |

**Synthesis on behavioral responses.**

- *Exit (extensive margin):* the evidence for France and Scandinavia points to small effects, with low single-digit percentages of the stock over the long run. The "mass exodus" narrative is not supported.
- *Base erosion (intensive margin):* the evidence (Switzerland, Denmark) points to **large** responses through under-reporting, valuation and asset restructuring. This is the stronger objection to high revenue estimates. It matters even more for a tax concentrated on a few hundred households holding mostly unlisted or controlling stakes, where valuation is hard and liquidity is low. The 2% rate is 33-67% of a 3-6% return (Geerolf's arithmetic) [S20].
- *Concentration risk:* three families reportedly hold 45% of the base, so the departure of the top three taxpayers would halve the yield (sources quoted in [S20]; secondary). This is a feature of the French base, not a general result.

### 5.4 Positions of prominent economists (as documented)

| Economist | Position | Source |
|---|---|---|
| Gabriel Zucman | For a 2% floor above EUR 100 m; EUR 15-25 bn; exit contained by an exit tax | Bill no. 768 (7 Jan 2025) citing Zucman [S22]; op-ed and book 2025, via [S20] |
| Olivier Blanchard, Jean Pisani-Ferry | Co-signed the June 2025 op-ed backing a 2% floor. Blanchard later wrote (18 Jun 2025, per Geerolf) that leaving transfers out of the chart is "potentially misleading", while the finding for the top 0.1% stands. ⚠ That he "expected 10-20 bn at most, preferring 1%" is known only through Geerolf, who gives no date or link. | As quoted by Geerolf [S20]; **primary not retrieved** (web search budget exhausted 2026-10-25). Recommendation: keep the "potentially misleading" quote with caveat (dated); drop "10-20 bn, 1%" from the site. |
| CAE (Landais, Bozio et al.) | Exit effects are modest; the authors take no position on the Zucman tax | [S18] |
| François Geerolf (OFCE) | Critic: wrong diagnosis; yield 2-6 bn; constitutional risk | [S20] |
| ~~Greg Mankiw~~ | ⚠ General critique of wealth taxes as a tax on saving. **From memory; not sourced.** Recommendation: drop from site; replace with the CPO and Montaigne rows (verified French institutional positions). | Not sourced |
| CPO (attached to the Cour des comptes) | Fix distortions (Dutreil, holdings); an uncapped differential tax at a moderate rate on non-professional wealth (illustration: 0.5% above EUR 5 m, EUR 1.4 bn before behavioral effects), within a package that is "globally neutral for public finances" | CPO report, 1 Dec 2025 [S46] (verified 2026-10-25) |
| Institut Montaigne (business-funded, liberal-centrist) | Adjustment must come mainly from spending; a revenue-only path would require "at least three new Zucman taxes each year for five years" | *Budget base zéro*, Nov 2025 [S44] |
| Terra Nova (center-left), G. Hannezo | Taxing the wealthiest is justified but yields about EUR 15 bn a year at most; do not count on Zucman-type yields | Note, 20 Sep 2024 [S43] |

**Fair presentation.** (1) Wealth taxation is a legitimate *equity* argument backed by serious evidence of regressivity at the very top. (2) Its *budgetary* contribution ranges from about 0.1% to about 0.8% of GDP, depending on design and behavioral assumptions. (3) Exit is not the main risk; base erosion is. (4) Even at the proponents' high end, it covers a minority of the needed adjustment.

---

## 6. Debate 4: Austerity multipliers, growth effects and the composition of consolidation

### 6.1 Evidence

| Study | Finding | Implication for the thesis |
|---|---|---|
| **Blanchard & Leigh (2013)**, AER P&P / IMF WP 13/1 [S14] | In 2010-2011, each extra point of planned consolidation was associated with GDP about 1% below forecast (β = -1.095, t = -4.29). Forecasters assumed multipliers of about 0.5; the paper concludes that actual multipliers were "substantially above 1" early in the crisis. (Corrected after verification: the "0.9-1.7" range was attributed to this paper; it comes from the authors' earlier box in the IMF *World Economic Outlook*, October 2012, Box 1.1, not from WP 18779 itself.) For later forecast vintages, coefficients were "typically between 0.3 and 0.5" and "less statistically significant" (corrected after verification: was "became insignificant"). No bias before the crisis (1997-2008). | Fast consolidation in a weak economy can be self-defeating. Multipliers are state-dependent. |
| **Alesina, Favero & Giavazzi** (2012 WP; book 2019, *Austerity: When It Works and When It Doesn't*) [S15] | Tax-based plans of 1% of GDP lead to a cumulative contraction of about 2% over 3 years. Spending-based plans cause small, often insignificant recessions. The difference is not explained by monetary policy. | Supports "consolidate through spending". |
| **Guajardo, Leigh & Pescatori (2014, JEEA)**, narrative approach; cited by the Cour [S1] | Consolidations are contractionary. With narrative identification, the evidence for "expansionary austerity" disappears. The Cour's 2026 reading: "whatever the lever, spending or revenue, the short-term cost would be comparable". | Neutral on composition; what matters is *which* taxes or spending. |
| **Fatás & Summers (2018)**; Gechert et al. (2019), cited by the Cour [S1] | Consolidations can have permanent effects on potential output (hysteresis). Spending multipliers may exceed 1. | Supports gradualism. |
| **Cour des comptes, RSPFP June 2026, ch. 3** [S1] | The cost depends on (i) the cycle, (ii) the *nature* of measures, (iii) competitiveness needs. Pension under-indexation and property or inheritance tax have low growth costs. Cuts to education and research, or higher taxes on labor and capital costs, are damaging. Front-load when markets are stressed; spread out when multipliers are high. Spending-based consolidations "can induce a higher short-term social cost for the most modest households". | The official French synthesis: neither camp's simple view. |
| **OFCE (July 2025)** [S6] | A gradual path (2.8% of GDP, about EUR 80 bn by 2029) instead of the PSMT's EUR 110 bn limits the rise in unemployment. Under the PSMT, unemployment would reach 9% in 2027. | Pace matters; this is not an argument against adjustment. |
| **Heimberger (2020)** via the Cour [S1] | In 17 OECD countries (1978-2013), consolidations raised inequality and lengthened unemployment. | Distributional cost. |

### 6.2 Where consensus lies

- *Consensus:* consolidation has short-run costs. "Expansionary fiscal contractions" are rare and context-specific: confidence and devaluation (Denmark/Ireland in the 1980s, the Nordics in the 1990s) [S1].
- *Contested:* whether spending-based consolidation is systematically cheaper. Alesina et al. say yes; Guajardo-Leigh-Pescatori and the Cour say it depends on the content.
- *Implication:* the platform should not say that spending cuts are free. The defensible claim is that **some** spending measures (pension indexation, efficiency savings, untargeted subsidies) have low growth costs, as do some revenue measures (inheritance and property taxes, removing tax expenditures).

### 6.3 A key counterpoint on feasibility (HCSP, July 2026)

The HCSP translated the needed adjustment (4.4 points of GDP by 2031) into historical frequencies [S8]:

| Single lever | Required | Historical record |
|---|---|---|
| Spending only | Real spending **-0.2%/yr** to 2031 (vs +1.2% trend) | A fall of 0.2% or more happened **only 3 times since 1959** (never in 1959-2000, 3 times since 2000), and it would have to happen five years in a row; average 2005-2025 +1.4%/yr |
| Revenue only | Real revenue **+2.7%/yr** (vs +1.0% trend) | Happened **32 times since 1959** per the HCSP's reading note. (Verification note: the HCSP's own Table 2 column reads "32 times between 1959 and 1999, 7 times since 2000", which would sum to 39; the source is internally ambiguous. Either way, the order of magnitude is unchanged.) |
| Structural reforms only | Employment rate +0.6 pt/yr to 84% in 2050, or productivity +2.7%/yr | Employment-rate gains of that size: 5 times since 2000 and never before. Productivity gains of that size: 33 times before 1999 but only 2 times since 2000 (refined after verification: was "rarely or never seen since 2000") |

**This is a strong counter-argument to a "spending-only" platform:** historically, France has raised revenue far more often than it has cut real spending. The HCSP's conclusion is that "no single lever will suffice" [S8]. The thesis needs to be framed as "spending must contribute substantially". It cannot be "spending is the only lever".

---

## 7. Debate 5: Debt sustainability. Is there an emergency?

### 7.1 The "no panic" case (steelman)

- The apparent interest rate is still low. Interest was 2.2% of GDP in 2025 [S1] against debt of 115.7% of GDP, an implicit rate of about 1.9%. This is close to 2025 nominal GDP growth (about 2%, per the Cour's February 2026 estimate [S2]). So r - g is close to 0 on the *stock*. Blanchard's 2019 AEA presidential address argued that when r < g the fiscal cost of debt may be small.
- The maturity is long: the average life of negotiable State debt was **8 years and 158 days (about 8.4 years) at 30 September 2026** (9 years 33 days for medium and long-term debt; outstanding negotiable debt EUR 2,896.2 bn), per the AFT page *Encours de la dette négociable au 30 septembre 2026* (updated 1 Oct 2026, read in a browser) [S35]. (Corrected 2026-10-25: was "about 8.5 years ... 8 years 180-200 days, mid-2026" from search snippets.) Rate shocks pass through slowly.
- France has never missed a payment. Demand at auctions is deep, and the ECB has backstop tools (TPI).

### 7.2 The "risk is rising" case

| Indicator | Value | Source |
|---|---|---|
| 10-year yield, France, monthly average | 3.40% (Feb 2026) to **4.44% (Sep 2026)** | Eurostat irt_lt_mcby_m [S34] |
| Spread vs Germany | 66 bp (Feb 2026) to **97 bp (Sep 2026)** | computed [S34] |
| Spread vs Italy | -107 bp (Jan 2024) to **+8 bp (Sep 2026)**; France above Italy in Dec 2025-Feb 2026 and Aug-Sep 2026, below Italy in Mar-Jul 2026 (by 3-10 bp) (corrected after verification: was "France at or above Italy since Dec 2025") | computed [S34] |
| Official daily values, October 2026 | 10-year OAT **5.126% at the close of 22 Oct 2026** (Banque de France TEC 10); spread over the Bund **169 bp (22 Oct) and 166 bp (23 Oct)** (TEC 10 minus the Bundesbank 10-year yield, ±5 bp across methods); above Eurostat's monthly-average maximum of 154 bp (Nov 2011) | Verified in file 06 (§5, 2026-10-25) from Banque de France and Bundesbank series (https://api.statistiken.bundesbank.de/rest/data/BBSIS/D.I.ZST.ZI.EUR.S1311.B.A604.R10XX.R.A.A._Z._Z.A?startPeriod=2026-09-01&format=csv&lang=en). *(Corrected 2026-10-25, index pass: was "⚠ OAT 10y briefly above 5%; spread vs Bund of 140-170 bp", press market trackers, recommendation "drop from site".)* See 00 row 43. |
| Interest burden | General-government interest in national accounts: EUR 65.7 bn in 2025 (+9%); EUR 77.4 bn forecast for 2026 by the Cour (June 2026), raised to EUR 79.2 bn by the government in the PLF 2027 (Sept 2026), then about EUR 91 bn in 2027 (2.9% of GDP). All on the same APU national-accounts basis (HCFP opinion 2026-5, §115). The State's budget-accounting debt charge is a separate, smaller concept (EUR 63.4 bn in 2026, EUR 72.9 bn in 2027) (corrected 2026-10-25: the earlier text called 79.2 bn a budget-scope figure) | [S1][S9] |
| Debt path at unchanged policies | 115.6% (2025) → 140% (2035) → 186% (2050), assuming r - g = +0.5. Range in 2050: 146% (favorable) to 245% (adverse). | HCSP [S8] |
| Non-resident holdings | 49.8% (Dec 2022) → **59.7% (Jun 2026)** | AFT / Banque de France [S35] |
| PLF 2027 | Deficit 5.4% (2026e) → 5.0% (2027). Debt 119.3% → 121.7%. Effort EUR 54 bn. Spending 57.1% → 56.9% of GDP. The HCFP judges that the government's 2027 growth figure (1.0%) "appears optimistic in light of recent developments" (*apparaît comme optimiste au regard des dernières évolutions*), most other forecasters being 0.1-0.3 point lower (HCFP opinion no. 2026-5, 25 Sep 2026, synthesis) [S47]. (Updated 2026-10-25: was sourced to press coverage only.) | [S9][S47] |

*Ranks (Eurostat, computed):* gross debt 2025 is 3rd-highest in the EU-27 (after Greece and Italy), vs 7th in 2005. Interest payments 2025 (2.2% of GDP) rank 5th of 20 in the euro area (median 1.4%).

**Assessment.** On the *stock*, r - g is still near zero. On the *margin*, new 10-year issuance costs 3.5-4.5%, against nominal growth of about 2-2.5%, and the primary deficit is about 2.9% of GDP (computed, 2025). The debt-stabilizing primary balance is positive. Both the HCSP and the Cour therefore conclude that debt keeps rising without adjustment [S1][S8]. A high non-resident share is a double-edged indicator: it reflects deep demand but also greater sensitivity to sentiment.

**Fair presentation.** Avoid "bankruptcy" rhetoric. Do say that convergence with Italy's spread and a yield above 4.4% signal that markets now price French fiscal risk. The steelman ("r ≈ g, long maturity") is correct for the next 2-3 years but does not hold over a 10-year horizon.

---

## 8. Debate 6: Underfunded public services vs inefficient spending

### 8.1 The underfunding case (steelman)

| Domain | Indicator | France | Comparator | Source |
|---|---|---|---|---|
| Justice | Professional judges per 100,000 inhabitants | 11.3 | Council of Europe median 17.6 (some sources say 17.8); the CEPEJ press release gives a European *average* of about 22 | CEPEJ 2024 cycle (2022 data; still the latest cycle as of Oct 2026), via secondary sources [S38] |
| Justice | Prosecutors per 100,000 | 3.2 | Median 11.2; average 12.2 (France lowest of all member states and entities) | CEPEJ 2024 cycle (2022 data), as transcribed by the *Union syndicale des magistrats* (USM) note to the Assemblée nationale, 29 Oct 2024 [S38] (re-opened 2026-10-25; values match. The CEPEJ primary PDF on rm.coe.int blocks automated download.) |
| Justice | Judicial-system budget per inhabitant (excl. prisons) | EUR 77.2 (0.20% of GDP) | European average EUR 85.4 (0.31% of GDP); **European median EUR 74.8**; GDP-per-capita group C average EUR 92.1 | Same USM notes (29 Oct 2024 and 18 Oct 2024) quoting CEPEJ 2024 (2022 data) [S38] (re-opened 2026-10-25; the 2020-data value was EUR 72.5). **Note: France is below the European average but *above* the European median per inhabitant**; the gap is larger in % of GDP. |
| Education | Teacher statutory salary after 15 years, primary (USD PPP) | 51,038 | OECD average 64,349; EU-25 average 62,650 | OECD *Education at a Glance 2026* (29 Sep 2026; 2025 salaries), Table D3.1 [S40] (corrected after verification: was 49,462 vs 59,673 from the superseded EAG 2025) |
| Education | Teacher statutory salary after 15 years, lower secondary (USD PPP) | 54,778 | OECD average 66,583; EU-25 average 65,122 | Same [S40] (corrected after verification: was 53,086 vs 61,563, EAG 2025) |
| Health | Hospital strain (beds, staff shortages) | n/a | n/a | Not quantified in this session (gap) |

The argument: France's high *total* spending coexists with *under-spending* on core state functions such as justice, security and teacher pay. The excess is concentrated in pensions and social transfers. This is consistent with the Section 3 composition data. Cuts across the board would worsen already-stretched services.

### 8.2 The efficiency case

- **IMF 2026 Article IV** (concluding statement 21 May 2026; Board 17-22 July 2026) [S11]: "Fiscal consolidation should rationalize inefficient spending and reallocate current and social spending." It recommends a structural effort of about 0.8% of GDP a year over 2027-2029, an automatic pension adjustment mechanism, and cuts to inefficient tax expenditures.
- **OECD, *Restaurer les finances publiques* (27 May 2026)** [S10]: across OECD countries, 2025-2026 consolidation measures mostly target health, government operations and pensions, and their ambition "seems relatively modest" relative to the challenges. The detailed France content was not retrieved (403 error).
- **Outcome-per-euro indicators:**
  - **PISA 2025** mathematics (published 8 Sep 2026): France **458 vs OECD 463**, 29th of 38 OECD countries, now below the OECD average (474 vs 472 in PISA 2022; 495 in 2012) [S39]. The OECD average also fell, so part of the French decline is common to the OECD; France's fall since 2015 is among the steepest (-35 points in mathematics) (file 13). (Updated 2026-10-25: the earlier text said PISA 2025 was not yet published.)
  - Life expectancy 2024: 83.0 years. France ranks 4th of 8 in the panel, behind Spain (84.0), Sweden (83.8) and Italy (83.7), all of which spend less publicly on health and social protection. France ranks 7th in the EU-27 (EU-27 aggregate 81.5) (Eurostat demo_mlexpec, computed [S36]).
  - Government compensation of employees: 12.4% of GDP in France (2025) vs an EU-27 aggregate of 10.3% and an EA21 aggregate of 10.0% (canonical comparator, file 00 row 18) (Eurostat [S30]).
- **Cour des comptes:** repeated diagnosis of a "ratchet effect" and no overall effort to save money in 2025 [S2].

### 8.3 Assessment

Both are true at once: France spends a lot in total and too little in some core functions. The policy implication is **reallocation**, not only reduction. The platform should avoid implying that every spending line is too high; on judges, prosecutors and teacher pay, the evidence points the other way.

---

## 9. Debate 7: "You get something for that spending". Redistribution outcomes

### 9.1 The steelman

France's tax-and-transfer system is among the most redistributive in the world. Insee's *extended* redistribution (including public services in kind) shows the following for 2023 [S13]:
- the top 10% have a pre-transfer income **26 times** that of the bottom 10%, but only **3.5 times** after redistribution;
- 56% of people are net beneficiaries (99% of the bottom decile, 96% of households whose adults average 65 or older);
- in-kind transfers (health, education, housing) explain 51% of the reduction in inequality, cash benefits 36%, collective spending 20%;
- **but:** redistribution is not balanced. It adds about EUR 1,400 per consumption unit on average, **financed by debt** (balance of about -EUR 66 bn in 2023).

### 9.2 Poverty and inequality outcomes: international comparison (EU-SILC, computed)

| Indicator | France | EU-27 aggregate | EU-27 country mean / median | France rank in EU-27 | Panel |
|---|---|---|---|---|---|
| At-risk-of-poverty rate after transfers, SILC 2025 | **16.3%** | 16.3% | 16.0 / 15.6 | 11th highest of 27 | BE 10.9, DK 11.8, NL 13.4, SE 15.6, DE 16.1, IT 18.6, ES 19.5 |
| Same, SILC 2015 | 13.6% | 17.4% | 17.1 / 16.3 | 22nd highest of 27 (i.e., low) | — |
| Rate before all transfers (pensions counted as transfers), 2025 | 46.8% | 42.8% | 40.6 / 41.1 | 2nd highest | — |
| **Reduction by all transfers incl. pensions**, 2025 | **30.5 pts** | — | 24.5 / 25.0 | **3rd largest** | BE 30.7, IT 28.3, SE 25.5, DK 25.7, DE 25.0 |
| Reduction by transfers excl. pensions, 2025 | 10.2 pts (38.5% relative) | — | 8.1 / 8.2 | 6th largest | BE 12.1, DK 12.7, SE 9.7 |
| Gini, disposable income, 2025 | 30.4 | 29.2 | 29.1 / 29.2 | 11th highest | BE 23.4, NL 25.9, DK 28.2, SE 28.6, DE 30.1, IT 31.0 |
| S80/S20, 2025 | 4.74 | 4.62 | 4.6 / 4.6 | 10th highest | BE 3.25, NL 3.76 |

*Sources: Eurostat ilc_li02, ilc_li09, ilc_li10, ilc_di12, ilc_di11 (updated 20 Oct 2026) [S33]. Files: `data/debates/eurostat_ilc_*.csv` and `computed_poverty_reduction_by_transfers.csv`. "SILC 2025" refers to the survey year; incomes refer to 2024.*

**France's AROP series** (EU-SILC): 13.0 (2005), 13.6 (2015), 13.6 (2019), 14.2 (2020), 15.6 (2022), 15.9 (2024), 16.3 (2025). Insee's national measure (ERFS) confirms the rise: 15.4% in 2024, the highest since the series began in 1996. Gini 0.302 is also a series high [S12]. **Eurostat flags a break in series ("b") for France in 2020 and 2022** in `ilc_li02` (checked 2026-10-25, file `data/raw/10_verify2/ilc_li02_FR.json`): 13.6 (2019) → 14.2 (2020, b) → 14.3 (2021) → 15.6 (2022, b) → 15.4 (2023) → 15.9 → 16.3. Part of the 2019-2025 rise may therefore be methodological; the 2022-2025 rise (+0.7 pt) is on a consistent series, and Insee's ERFS confirms a rise. (Updated 2026-10-25: was "not checked".)

### 9.3 Assessment

- **True:** French transfers do far more redistributive *work* than the EU average. Pre-transfer poverty is among the highest in the EU, and post-transfer poverty was well below average for most of the 2005-2019 period.
- **Weakening:** by 2025 France's post-transfer poverty rate is *at* the EU average and above the Benelux and Nordic countries, some of which spend less. Belgium achieves a similar poverty reduction with a lower poverty level. The "results justify the spending" claim is therefore weaker than it was a decade ago.
- **Caveat:** most of the 30.5-point reduction comes from pensions. These are partly a deferred-income mechanism rather than redistribution in the narrow sense. Excluding pensions, France is 6th in the EU, not 3rd.

**Fair presentation.** Acknowledge the large redistributive effect. Show that it is largely financed by debt (Insee) and that poverty outcomes have deteriorated relative to peers since 2019.

---

## 10. Debate 8: Measurement issues

| Issue | Effect on France's apparent spending or tax level | Evidence |
|---|---|---|
| **% of GDP denominators** | Spending of 57% of GDP does not mean the state "consumes" 57% of output. Government final consumption is 24.1% of GDP; the rest is mostly transfers that households spend. | Eurostat 2025: P.3 24.1%, cash social benefits 19.4%, compensation of employees 12.4%, interest 2.2% (all % of GDP) [S30]. Geerolf makes the same point about the "500 fortunes = 42% of GDP" chart (a stock compared with a flow) [S20]. |
| **Tax credits** | Insee and Eurostat count them as spending; the Cour excludes them. | Spending 2025: 57.3% (Insee) vs 56.6% (Cour). PO 2024: **42.7%** (Insee, May 2026 accounts, canonical; 42.8% in the earlier vintage) vs 43.5% (Eurostat). PO 2025: 43.6% (Insee) vs 44.3% (Eurostat definition) [S1][S2]. |
| **Tax expenditures** | Countries that subsidize through tax breaks (US, Netherlands) look smaller in *spending*. France also uses tax expenditures heavily. | About 474-500 *dépenses fiscales*, EUR 85-88.3 bn in 2026 (sources differ; *Voies et moyens* tome II not retrieved). OECD SOCX net includes "tax breaks for social purposes" [S32]. |
| **Gross vs net social spending** | France taxes benefits (CSG on pensions) more than some peers do. Net adjustments reduce French figures somewhat. | Gross public 32.7% vs net total 32.0% of GDP (2021) [S32]. |
| **Pensions** | Public pay-as-you-go pensions inflate both spending and levies; funded systems keep them off the books. | Netherlands: 19.8% public vs 11.4% private (% of GDP, 2021) [S32]. |
| **PO definitions** | Different sources give different numbers for "the same" ratio. | 2025: 43.6% (Insee via Cour [S1]) vs 42.8% (HCSP [S8]). Verification: 42.8% is exactly Insee's 2024 PO rate in the pre-May-2026 vintage, so the HCSP figure is most likely the 2024 value labeled "2025"; not confirmed with the HCSP. Eurostat taxes plus social contributions: 45.3% (2024) [S30]. |
| **Effective tax rates by income group** | Results depend on including contributory contributions, VAT and transfers. | IPP excludes pension/unemployment contributions and VAT; Zucman's "50%" includes them [S19][S20]. |

---

## 11. Surveys of economists: what exists

| Item | Content | Status |
|---|---|---|
| Representative survey of French economists on spending vs taxes or the Zucman tax | **None found.** | Gap |
| Clark Center (Kent A. Clark Center) European Economic Experts Panel | ⚠ A "UK and Europe" poll dated 30 June 2026 exists; whether it covers wealth taxes is unknown. Earlier panels on wealth taxes not verified (not re-checked 2026-10-25: web search budget exhausted). | **Unverified.** Recommendation: drop from site until a specific poll is opened. |
| Collective op-eds | June 2025 op-ed by Blanchard, Pisani-Ferry and Zucman backing a 2% floor; a later op-ed by 13 economists, including Nobel laureates, in favor | Advocacy, not a survey |
| CAE | An independent council of economists attached to the Prime Minister. Its Focus 118 is an empirical study. Authors' responsibility; not a consensus statement. | Evidence, not a survey |
| Public opinion | Ifop for the *Parti socialiste* (study no. 121870, fieldwork 10-11 Sep 2025, n = 1,000, online quotas): 86% favor "a 2% tax on wealth above EUR 100 million" (verified in file 14 against the Ifop PDF; corrected 2026-10-25: was dated "17 Sep 2025"; the Ifop PDF gives fieldwork 10-11 Sep 2025). Flash Eurobarometer 562 (Ipsos for DG TAXUD, fieldwork 9-17 Apr 2025): 65% support in France and 65% in the EU-27 for a minimum tax on the richest 0.001% (verified by file 14 in the primary report; corrected 2026-10-25, index pass: was "⚠ known only via Euronews, keep with caveat"). | Public opinion only |

**Recommendation.** If the platform wants an "economists' consensus" indicator, it should either run its own structured survey (IGM-style: statement plus agree/disagree plus confidence) or quote institutional syntheses (Cour, HCFP, HCSP, CAE, IMF, OECD) and label them as such.

---

## 12. International comparison: summary tables

### 12.1 Fiscal aggregates, 2025 (% of GDP; Eurostat, updated 21 Oct 2026; computed)

| Indicator | France | EU-27 agg. | EU-27 mean / median | FR rank EU-27 | EA-20 mean / median | FR rank EA-20 | Panel mean / median | FR rank panel |
|---|---|---|---|---|---|---|---|---|
| Total expenditure | 57.3 | 49.4 | 46.4 / 47.3 | 2 (Finland 57.5) | 46.5 / 47.5 | 2 | 50.0 / 49.7 | 1 |
| Total revenue | 52.2 | 46.3 | 43.8 / 43.6 (26 countries) | 2 | 44.4 / 45.0 | 2 | 47.3 / 47.8 (7 countries) | 1 |
| Balance | -5.1 | -3.1 | -2.6 / -2.5 | 23rd of 26 (4th worst) | -2.0 / -2.5 | 19 of 20 | -3.1 / -2.9 | 6 of 7 |
| Interest paid | 2.2 | 1.9 | 1.6 / 1.3 | 8 | 1.5 / 1.4 | 5 | 1.7 / 1.7 | 4 |
| Gross debt | 115.7 | 81.5 | 64.9 / 58.9 | 3 | 71.1 / 61.6 | 3 | 78.8 / 81.7 | 2 |
| Taxes plus net social contributions (2024) | 45.3 | 40.2 | 37.7 / 37.6 | 2 (Denmark 45.5) | 38.1 / 38.4 | 1 | 42.2 / 42.0 | 2 |

*Denmark's total revenue was missing from the API extract for 2024-2025, so revenue statistics use 26 EU countries and 7 panel countries. Source [S30]. File `data/debates/computed_fr_vs_eu27_fiscal_series.csv`.*

### 12.2 Evolution of France's gap over 20 years (points of GDP vs EU-27 aggregate; computed)

| Year | Spending gap | Revenue gap | Taxes plus SSC gap | Debt gap |
|---|---|---|---|---|
| 2005 | +7.1 | +6.0 | +5.0 | +1.0 |
| 2010 | +7.0 | +5.9 | +5.2 | n/a |
| 2015 | +9.3 | +7.3 | +6.9 | +12.0 |
| 2017 | +10.8 | +8.2 | +7.5 | n/a |
| 2019 | +8.7 | +6.9 | +6.4 | n/a |
| 2024 | +8.1 | +5.4 | +5.1 | +32.3 |
| 2025 | +7.9 | +5.9 | n/a | +34.2 |

**Reading.** France's revenue gap to the EU is about where it was in 2005. Its spending gap is about 1 point wider. Its debt gap went from 1 point to 34 points of GDP. The persistent difference between the spending gap and the revenue gap (about 2 points) is the structural financing gap. (Verification note: the difference is 1.1 pt in 2005, 1.1 in 2010, 2.0 in 2015, 2.6 in 2017, 1.8 in 2019, 2.7 in 2024 and 2.0 in 2025. "About 2 points" holds from 2015 onward, not over the whole 20 years.) This is the most defensible single fact behind the platform's thesis, and it does not depend on the choice of base year.

### 12.3 Outcome indicators (computed where noted)

| Outcome | France | EU-27 / OECD reference | Panel position | Source |
|---|---|---|---|---|
| AROP after transfers, 2025 | 16.3% | EU 16.3% | 3rd highest of 8 | [S33] |
| Poverty reduction by transfers (incl. pensions), 2025 | 30.5 pts | EU mean 24.5 | 2nd of 8 (Belgium 30.7) | [S33] |
| Gini, 2025 | 30.4 | EU 29.2 | 3rd highest of 8 | [S33] |
| Life expectancy at birth, 2024 | 83.0 | EU 81.5 | 4th of 8 | [S36] |
| PISA mathematics, 2025 | 458 | OECD 463 | 29/38 | [S39] |
| Judges per 100,000, 2022 | 11.3 | CoE median 17.6 | n/a | [S38] |

---

## 13. Divergences between sources

| Variable | Source A | Source B | Explanation |
|---|---|---|---|
| Public spending 2025 | Insee/Eurostat 57.3% of GDP [S30] | Cour 56.6% (Jun 2026) and 57.0% (Feb 2026 estimate), excl. tax credits [S1][S2]; IMF 57.5% [S11] | Tax-credit treatment, data vintage, IMF definitions |
| PO 2025 | 43.6% of GDP (Insee via Cour) [S1]; 44.3% on the Eurostat definition (Cour, same report) | 42.8% "in 2025" (HCSP) [S8] | Most likely the HCSP quotes Insee's 2024 value from the pre-May-2026 vintage (42.8%); not confirmed. |
| PO 2024 | Insee 42.8% (Feb 2026 vintage), revised to 42.7% (May 2026 accounts, used by the Cour in June 2026) | Eurostat 43.5% | Eurostat does not net out tax credits; Insee vintage revision [S1][S2] |
| Public spending 2025, rank | Eurostat (Oct 2026): France 57.3%, 2nd in EU behind Finland 57.5% [S30]; HCSP agrees [S8] | IMF (May 2026): 57.5%, "highest in the euro area" [S11] | IMF used an earlier vintage/definition; on the Oct 2026 Eurostat release France is 2nd, not 1st |
| Deficit 2025 | 5.1% (Insee final, Cour, IMF) | 5.4% (earlier government forecast and the Cour's Feb 2026 estimate) | Vintage |
| Debt 2025 | 115.7% (Cour, Eurostat) | 115.6% (HCSP) | Rounding or vintage |
| Interest 2026 | EUR 77.4 bn (Cour, June 2026), 78 bn (government response) [S1] | EUR 79.2 bn (government forecast in the PLF 2027, reported by the HCFP) [S9] | **Same concept (APU, national accounts), different vintages**: the upward revision comes from inflation-indexed bonds and the September 2026 rate rise. Canonical: 79.2 bn. Not the State budget debt charge (63.4 bn) |
| Poverty 2024 | Insee ERFS 15.4% [S12] | Eurostat EU-SILC 2025 AROP 16.3% [S33] | Different surveys (ERFS uses administrative tax data; SILC is a survey) and income definitions |
| Cost of tax cuts | OFCE: -2.5 pts PO 2017-2024 [S6] | Rexecode: EUR 75 bn (2025 euros) 2018-2023 [S27]; Fipeco: EUR 44 bn in 2022 [S28] | Ratio vs discretionary measures; windows; whether temporary measures count |
| Zucman yield | 15-25 bn (Zucman) | 2-6 bn (Geerolf); "5 bn" (a reading of a CAE note, disputed) | Behavioral assumptions, base definition, corporate tax imputation |
| Billionaires' effective rate | 26% (IPP 2023, 2016 data) | 25.1% vs 26.8% at the P90 threshold on the same base (2025 WP via Geerolf) | Comparison base; whether contributions and VAT are included |
| Net social spending rank | France 1st (2015, 2019) | US 1st (2021) | COVID-year effects; US private health spending |
| 10-year spread | Eurostat Sep 2026 monthly average: FR-DE 97 bp | Press Oct 2026: 140-172 bp | Monthly average vs intraday or daily; October not yet in Eurostat |

---

## 14. How the platform should present these debates fairly

1. **Say "tax the rich cannot balance the budget alone"**, not "taxing the rich is useless". Give the range (0.1-0.8% of GDP) next to the need (4.4-6.4% of GDP).
2. **Show the base-year sensitivity** of "tax cuts vs spending". Use at least two windows (2017-2024 and 2019-2025) and the 20-year gap table.
3. **Use net total social spending alongside gross public spending.** Acknowledge the US comparison.
4. **Do not claim that spending cuts are costless.** Cite the Cour's 2026 synthesis: composition and timing matter more than the spending/revenue label.
5. **Separate equity from yield.** The regressivity at the very top is a serious finding (IPP); the yield is uncertain.
6. **Acknowledge outcomes on both sides.** Redistribution is strong; core-service underfunding (justice, teacher pay) is documented; poverty is rising.
7. **Present debt risk in market terms** (spread vs Italy, yields, non-resident share), not in bankruptcy terms.
8. **Label think-tank orientation** every time: OFCE (Keynesian-leaning, Sciences Po), Rexecode (employer-funded), Institut Montaigne (business-funded, liberal-centrist), iFRAP (free-market), Terra Nova (center-left), Attac (alter-globalist NGO), Fipeco (independent, former Cour magistrate, fiscally orthodox).

---

## 15. Open questions and gaps

- **Resolved on 2026-10-25** (see the verification log, second pass): Terra Nova, Attac, Institut Montaigne and iFRAP positions; the CAE "26 cents" (a Scandinavian estimate quoted in CAE Focus 118) and the "75% Danish loss"; the CPO primary text (EUR 1.4 bn illustration; the "2.7 bn" is not in it); AFT average maturity; EU-SILC break flags; Insee Q1 2026 debt; HCFP opinion text; Agrawal et al. and Jakobsen et al. figures; CEPEJ prosecutors and budget (via the union's transcription).
- **Still unverified (⚠)**, web search budget exhausted on 2026-10-25:
  - The primary EU Tax Observatory note (19.4 bn split; 1,800 households is in the press and the bill debate).
  - Pichet's ISF estimates; Mankiw's position (recommend dropping both).
  - Blanchard's "10-20 bn, 1%" statement (known only through Geerolf).
  - Clark Center panel coverage.
- ~~**October 2026 market data** (yield above 5%, spread 140-170 bp) come from press trackers; the latest official month is September 2026.~~ Resolved 2026-10-25 (index pass): official daily values from Banque de France (TEC 10: 5.126% on 22 Oct 2026) and the Bundesbank (spread 169 bp on 22 Oct, 166 bp on 23 Oct), verified in file 06.
- **OECD SOCX net total** latest year is 2021 (a COVID year). Net figures for 2022-2024 were not available.
- **OECD *Études économiques: France 2026*** (30 Jun 2026) and *Restaurer les finances publiques* France content not retrieved (403 error).
- **Hospital-sector indicators** (beds, staff, waiting times) not compiled.
- **No representative survey of economists** found (Section 11).
- **PLF/PLFSS 2027 details** (split of the EUR 54 bn effort between spending and revenue; HCFP opinion text) not retrieved from primary sources.
- **Insee quarterly debt** (checked 2026-10-25 in Insee BDM, dataflow `DETTE-TRIM-APU-2020`): Q1 2026 EUR 3,535.9 bn = 117.5% of GDP (corrected: was 3,536.1 bn from a search snippet); **latest, Q2 2026: EUR 3,595.5 bn = 119.0% of GDP**. File `data/raw/10_verify2/insee_DETTE-TRIM-APU-2020_2025Q3-2026Q2.xml`.

---

## 16. Data files produced in this session

All under `research/data/`:

- `debates/eurostat_gov_*.csv`: Eurostat gov_10a_main items TE, TR, B9, D41PAY, D62PAY, D632PAY, D1PAY, P2, P3, P51G, D3PAY, D2REC, D5REC, D61REC (S13, % of GDP).
- `debates/eurostat_debt.csv` (gov_10dd_edpt1); `debates/eurostat_gov_tax_ag.csv` (gov_10a_taxag).
- `debates/eurostat_ilc_li02.csv`, `ilc_li09.csv`, `ilc_li10.csv`, `ilc_di11.csv`, `ilc_di12.csv` (poverty and inequality).
- `debates/eurostat_irt_lt_mcby_m.csv`, `eurostat_irt_lt_mcby_a.csv` (long-term yields).
- `debates/eurostat_demo_mlexpec.csv` (life expectancy).
- `debates/oecd_socx_net_total_pct_gdp.csv`, `oecd_socx_public_private_pct_gdp.csv`.
- `debates/aft_nonresident_share.csv`.
- `debates/computed_fr_vs_eu27_fiscal_series.csv`, `computed_poverty_reduction_by_transfers.csv`.
- Raw files: `raw/eurostat_debates/`, `raw/oecd_debates/`, `raw/ccomptes_debates/` (Cour reports, PDF and text), `raw/ofce_debates/`, `raw/hcsp_debates/`, `raw/wealthtax_debates/` (CAE Focus 118, Geerolf), `raw/papers_debates/` (Blanchard-Leigh), `raw/thinktanks_debates/` (Rexecode DT 97, Fipeco), `raw/aft_debates/` (chart screenshot).
- Scripts: `research/scripts_debates/es2csv.py`, `stats.py`.

---

## 17. Sources (all accessed 2026-10-25)

| # | Institution | Title | Publication date | URL |
|---|---|---|---|---|
| S1 | Cour des comptes | *La situation et les perspectives des finances publiques* (report, synthesis and responses) | 25 Jun 2026 (synthesis dated Jul 2026) | https://www.ccomptes.fr/fr/publications/la-situation-et-les-perspectives-des-finances-publiques-17 ; full report https://www.ccomptes.fr/sites/default/files/2026-07/20260625_RSPFP-2026.pdf |
| S2 | Cour des comptes | *The State of French Public Finances at the Start of 2026* (English) | 19 Feb 2026 | https://www.ccomptes.fr/sites/default/files/2026-03/20260219-report-The-state-of-french-public-finances-at-the-start-of-2026.pdf |
| S6 | OFCE (Heyer, Plane, Ragot, Sampognaro, Timbeau) | *Quelles trajectoires pour les finances publiques de la France ?* (blog summarizing an OFCE working paper) | 11 Jul 2025 | https://www.ofce.sciences-po.fr/blog2024/fr/2025/20250711_PSMT/blog.fr.pdf |
| S8 | Haut-commissariat à la Stratégie et au Plan (HCSP), ed. C. Beaune | *Focus Finances publiques: Faire des choix budgétaires à la hauteur des défis des 10 et 25 prochaines années* | 17 Jul 2026 | https://www.strategie-plan.gouv.fr/files/files/Publications/2026/2026-07-17%20-%20Focus%20Finances%20publiques/HCSP-2026-FRANCE%202035-2050_Focus-Finances%20publiques_0.pdf |
| S9 | Legifiscal (secondary), Assemblée nationale | *PLF 2027: principales mesures*; PLF 2027 bill text | 1 Oct 2026 | https://www.legifiscal.fr/actualites-fiscales/4656-presentation-plf-2027.html ; https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf |
| S10 | OECD | *Restaurer les finances publiques: Créer les conditions d'un État efficace* | 27 May 2026 | https://www.oecd.org/fr/publications/restaurer-les-finances-publiques_e9a64552-fr |
| S11 | IMF | France: Staff Concluding Statement of the 2026 Article IV Mission; Board press release PR26/255 | 21 May 2026; 22 Jul 2026 | https://www.imf.org/en/news/articles/2026/05/21/mcs-052126-france-staff-concluding-statement-of-the-2026-article-iv-mission ; https://www.imf.org/en/news/articles/2026/07/22/pr26255-france-imf-executive-board-concludes-2026-article-iv-consultation |
| S12 | Insee (Rieg, Rousset) | *Niveau de vie et pauvreté en 2024*, Insee Première no. 2117 | 9 Jul 2026 | https://www.insee.fr/fr/statistiques/9019316 |
| S13 | Insee (André, Barrau, Renaud) | *Revenus des ménages élargis à l'ensemble de l'économie en 2023*, Insee Analyses no. 118 | 16 Apr 2026 | https://www.insee.fr/fr/statistiques/8974371 |
| S14 | NBER / IMF (Blanchard, Leigh) | *Growth Forecast Errors and Fiscal Multipliers*, NBER WP 18779; AER 103(3) | Feb 2013 / May 2013 | https://www.nber.org/papers/w18779 (the 0.9-1.7 multiplier range is from IMF *World Economic Outlook*, Oct 2012, Box 1.1, not from this paper) |
| S15 | NBER (Alesina, Favero, Giavazzi) | *What Do We Know About the Effects of Austerity?* (WP 24246); *Austerity: When It Works and When It Doesn't* (Princeton UP, 2019) | 2018; 2019 | https://www.nber.org/papers/w24246 |
| S16 | Guajardo, Leigh, Pescatori | *Expansionary Austerity? International Evidence*, JEEA 12(4) (cited via S1) | 2014 | (cited in S1, footnote 217) |
| S18 | CAE (Bach, Bozio, Grimprel, Guillouzouic, Landais, Malgouyres) | *Fiscalité du capital: quels sont les effets de l'exil fiscal sur l'économie ?*, Focus no. 118 | Jul 2025 (v2 2 Sep 2025) | https://cae-eco.fr/static/pdf/Focus_118_emigration_fiscale_250725_v2.pdf |
| S19 | IPP (Bach, Bozio, Guillouzouic, Malgouyres) | *Quels impôts les milliardaires paient-ils ?*, Note IPP no. 92 | Jun 2023 (updated PDF posted May 2025; 46%/26% headline unchanged) | https://www.ipp.eu/publication/note-ipp-n92-quels-impots-les-milliardaires-paient-ils/ ; PDF https://www.ipp.eu/wp-content/uploads/2025/05/92_Note_IPP_Billionaires-version-actualisee.pdf (replaced after verification: the former link .../2023/09/Note_IPP_92-OLD.pdf returns 404) |
| S20 | François Geerolf (OFCE economist; personal paper, critical of the proposal) | *Les mensonges de la taxe Zucman* | Oct 2026 | https://fgeerolf.com/mensonges-taxe-zucman.pdf |
| S21 | Sénat, Commission des finances (Husson, Raynal) | *Imposition des hauts patrimoines*, information report no. 760 (2025-2026) | 17 Jun 2026 | https://www.senat.fr/rap/r25-760/r25-7602.html |
| S22 | Assemblée nationale (primary); press coverage (Public Sénat) | *Proposition de loi* no. 768 creating an *impôt plancher sur la fortune* (2% for wealth above EUR 100 m; "between 15 and 25 bn" according to G. Zucman); press: about 1,800 households, EUR 20 bn | 7 Jan 2025; 2025 | https://www.assemblee-nationale.fr/17/pdf/propositions/pion0768.pdf ; https://www.publicsenat.fr/actualites/economie/la-taxe-zucman-arrive-au-senat-on-vous-explique-les-enjeux-qui-se-cachent-derriere-cette-taxe-qui-vise-les-ultras-riches |
| S23 | NBER (M. Ring) | *Taxing Entrepreneurial Wealth: Evidence from Norway, 2021-2025*, WP 35854 | 2026 | https://www.nber.org/papers/w35854 |
| S24 | QJE (Jakobsen, Jakobsen, Kleven, Zucman) | *Wealth Taxation and Wealth Accumulation: Theory and Evidence from Denmark*, QJE 135(1), 329-388 | Feb 2020 (accepted version Aug 2019) | Accepted version (figures used): https://www.econ.ku.dk/cebi/news/JJKZ_QJE_Aug2019.pdf ; NBER WP 24371 (2018, earlier figures): https://nber.org/system/files/working_papers/w24371/w24371.pdf |
| S25 | AEJ: Economic Policy (Brülhart, Gruber, Krapf, Schmidheiny) | *Behavioral Responses to Wealth Taxes: Evidence from Switzerland*, 14(4) | 2022 | https://www.aeaweb.org/content/file?id=15737 |
| S26 | Agrawal, Foremny, Martínez-Toledano | *Wealth Tax Mobility and Tax Coordination*, *American Economic Journal: Applied Economics* 17(1): 402-430 (earlier title *Paraísos fiscales, Wealth Taxation, and Mobility*) | Jan 2025 (author version Oct 2023) | https://www.aeaweb.org/doi/10.1257/app.20220615 ; open author version: https://hdl.handle.net/2445/220290 (CESifo WP 11048 link blocks automated clients) |
| S27 | Rexecode (employer-funded institute) | *Bilan des prélèvements obligatoires*, Document de travail no. 97 | Jul 2025 | https://www.rexecode.fr/media/documents/document-de-travail/2025/bilan-des-prelevements-obligatoires-en-france-document-de-travail-n.97-juin-2025 |
| S28 | Fipeco (F. Ecalle) | *Les principales réformes fiscales du quinquennat* | 27 Jan 2022 | https://www.fipeco.fr/pdf/Mesures%20fiscales.pdf |
| S30 | Eurostat | gov_10a_main, gov_10dd_edpt1, gov_10a_taxag | updated 21 Oct 2026 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/gov_10a_main |
| S32 | OECD | Social Expenditure Database (SOCX): DF_NET_GDP, DF_PUB_PRV | accessed 2026-10-25 | https://sdmx.oecd.org/public/rest/data/OECD.ELS.SPD,DSD_SOCX_AGG@DF_NET_GDP,/all |
| S33 | Eurostat | EU-SILC ilc_li02, ilc_li09, ilc_li10, ilc_di11, ilc_di12 | updated 20 Oct 2026 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/ilc_li02 |
| S34 | Eurostat | irt_lt_mcby_m: EMU convergence criterion bond yields (monthly) | accessed 2026-10-25 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/irt_lt_mcby_m |
| S35 | Agence France Trésor / Banque de France | *Principaux chiffres dette*: non-resident share chart; *Encours de la dette négociable au 30 septembre 2026* (average life) | Q2 2026 data; updated 1 Oct 2026 | https://www.aft.gouv.fr/fr/principaux-chiffres-dette ; https://www.aft.gouv.fr/fr/node/452 (browser only; 403 to scripts) |
| S36 | Eurostat | demo_mlexpec: life expectancy | accessed 2026-10-25 | https://ec.europa.eu/eurostat/api/dissemination/statistics/1.0/data/demo_mlexpec |
| S38 | CEPEJ (Council of Europe), via secondary sources (USM magistrates' union notes, Le Club des juristes) | European judicial systems, 2024 evaluation cycle (2022 data) | 16 Oct 2024 (USM notes 18 and 29 Oct 2024) | https://www.leclubdesjuristes.com/en-bref/rapport-de-la-cepej-quelle-efficacite-de-la-justice-en-france-7312/ ; https://union-syndicale-magistrats.org/wp-content/uploads/2024/11/2024.10.18_note-AN_PLF2025.pdf ; https://union-syndicale-magistrats.org/wp-content/uploads/2024/10/2024.10.18_note-USM-sur-rapport-CEPEJ-2024.pdf ; CEPEJ France country fiche (primary, blocks automated download): https://rm.coe.int/france-country-fiche/48802c1521 |
| S39 | OECD *PISA 2025 Results (Volume I)* (8 Sep 2026; summary table https://www.oecd.org/fr/publications/resultats-du-pisa-2025-volume-i-version-abregee_72cbf7bd-fr/full-report/component-5.html ; country ranks recomputed in file 13); earlier: OECD PISA 2022 (via DEPP/Trésor); OECD *Education at a Glance* 2025 (via Assemblée nationale documents) | PISA 2025 and 2022 results for France; teacher salaries | Sep 2026; Dec 2023; Sep 2025 | DEPP note (open mirror; the education.gouv.fr link returns 403 to automated clients): https://halshs.archives-ouvertes.fr/halshs-04325922v1/file/NI-23-48-PISA-maths-pdfa.pdf ; OECD PISA 2022 France country note: https://oecd.org/publication/pisa-2022-results/webbooks/dynamic/pisa-country-notes/8008535b/pdf/france.pdf ; original https://education.gouv.fr/media/159228/download ; teacher salaries (superseded by S40): https://www.assemblee-nationale.fr/dyn/17/amendements/1906C/CION_FIN/CF1907.pdf |
| S40 | OECD | *Education at a Glance 2026*, Indicator D3, Table D3.1 (statutory teacher salaries, 2025) | 29 Sep 2026 | https://www.oecd.org/en/publications/2026/09/education-at-a-glance-2026_3bce4131/full-report/how-much-are-teachers-and-school-heads-paid_a6233c97.html ; data `research/data/04_oecd_eag2026_D3_1_teacher_statutory_salaries_2025.csv` |
| S41 | Public Sénat | *Budget 2027: le Haut Conseil des finances publiques pointe des prévisions « optimistes » du gouvernement* (secondary, HCFP opinion) | Oct 2026 | https://www.publicsenat.fr/actualites/economie/budget-2027-le-haut-conseil-des-finances-publiques-pointe-des-previsions-optimistes-du-gouvernement |
| S42 | Attac France, *Observatoire de la justice fiscale*, CADTM (advocacy NGO) | *La dette de l'injustice fiscale* (report) | 26 Mar 2025 | https://france.attac.org/nos-publications/notes-et-rapports/article/rapport-la-dette-de-l-injustice-fiscale |
| S43 | Terra Nova (center-left), G. Hannezo | *Quel rendement peut-on réellement attendre de la taxation des plus fortunés ?* | 20 Sep 2024 | https://tnova.fr/economie-social/finances-macro-economie/quel-rendement-peut-on-rellement-attendre-de-la-taxation-des-plus-fortunes/ |
| S44 | Institut Montaigne (business-funded, liberal-centrist) | *Budget base zéro : décider sous la contrainte*, note d'éclairage | Nov 2025 | https://institutmontaigne.org/ressources/pdfs/publications/note-budget-base-zero-decider-sous-la-contrainte.pdf |
| S45 | Fondation iFRAP (free-market) | *Fiscalité des riches : le mirage des milliards de recettes*, Revue no. 270 | Sep 2025 | https://www.ifrap.org/sites/default/files/documents/2025-09/ifrap270_etude_fiscalite_des_plus_riches.pdf |
| S46 | Conseil des prélèvements obligatoires (CPO) | *Corriger les principales distorsions de l'imposition du patrimoine* (report and synthesis) | 1 Dec 2025 | https://www.ccomptes.fr/sites/default/files/2025-12/20251201-Corriger-les-principales-distorsions-de-l-imposition-du-patrimoine.pdf ; https://www.ccomptes.fr/sites/default/files/2025-11/20251201-synthese-Corriger-les-principales-distorsions-de-l-imposition-du-patrimoine.pdf |
| S47 | Haut Conseil des finances publiques (HCFP) | *Avis n° HCFP-2026-5 relatif aux PLF et PLFSS pour 2027* | 25 Sep 2026 | https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf |

---

## Verification log (2026-10-25)

*Adversarial fact-check of this file. Each source was re-opened independently: fresh downloads under `research/data/raw/10_verify/` (Eurostat JSON, OECD SOCX CSV, Cour, HCSP, OFCE, Rexecode, Fipeco, CAE, Geerolf, IPP, Blanchard-Leigh and Brülhart et al. PDFs, Insee pages). Statistics were recomputed with Python, not copied from the original session's CSVs. New derived file: `research/data/debates/verify_fr_de_it_10y_yields_2023_2026.csv`.*

### Confirmed (value, unit, year and source match)

| Claim | Check performed | Result |
|---|---|---|
| Deficit 2025 EUR 152.5 bn = 5.1% of GDP; spending excl. tax credits EUR 1,694.0 bn = 56.6%; PO EUR 1,305.1 bn = 43.6% (+0.9 pt, "highest in the euro area"); EUR 23 bn new tax measures + EUR 28 bn spontaneous; debt EUR 3,460.5 bn = 115.7%; interest EUR 65.7 bn = 2.2% of GDP (+9.3%); 3.8 pts of GDP of tax hikes 2010-2014; interest 2026 EUR 77.4 bn; quoted passages on margins and composition | Cour RSPFP 2026 PDF re-downloaded (HTTP 200) and text-searched | Confirmed. The Cour also gives PO on the Eurostat definition: 44.3% in 2025 (added). |
| Eurostat gov_10a_main (updated 21 Oct 2026): TE 57.3, TR 52.2, B9 -5.1, D41 2.2, D62 19.4, D1 12.4, P3 24.1 (% of GDP, 2025); all windows in Section 4.2; all gaps in Section 12.2; all EU-27, EA-20 and panel means, medians and ranks in Section 12.1; debt rank 3rd (7th in 2005) | Recomputed from fresh API pulls | All reproduced to the decimal (EA-20 revenue mean/median 44.45/44.95 rounds to 44.4-44.5 / 45.0). |
| Taxes plus net social contributions 2024: 45.3% vs EU-27 40.2%; rank 2 (Denmark 45.5); gaps 5.0 (2005) to 5.1 (2024) | gov_10a_taxag recomputed | Confirmed |
| OECD SOCX net total 2021: France 31.95, US 33.24, OECD mean 21.98, median 22.47, France 2nd of 38; panel mean 26.94, median 26.62; 1st in 2015 and 2005; gross public 2021 32.7 vs OECD 22.1; 2024 gross 30.6 (24 countries); private 3.6 | OECD SDMX re-downloaded, recomputed | Confirmed |
| EU-SILC 2025: AROP FR 16.3 = EU-27 16.3; 2015 13.6 vs 17.4; pre-transfer 46.8; reduction 30.5 pts (3rd; EU mean 24.5, median 25.0); excl. pensions 10.2 (6th; 38.5% relative); Gini 30.4 (11th; panel 3rd); S80/S20 4.74 (10th); AROP series 2005-2025 | ilc_li02/li09/li10/di11/di12 re-downloaded (updated 20 Oct 2026) | Confirmed |
| Life expectancy 2024: 83.0 vs EU-27 81.5; 4th of 8 in panel; 7th in EU-27 | demo_mlexpec (updated 25 Sep 2026) | Confirmed |
| 10-year yields Sep 2026: FR 4.44, DE 3.473, IT 4.362 (97 bp; +8 bp); Feb 2026 spread vs DE 66 bp; Jan 2024 vs IT -107 bp | irt_lt_mcby_m (updated 13 Oct 2026) | Confirmed (but see correction 1) |
| Non-resident share 59.66% (Q2 2026) vs 49.82% (Dec 2022) | AFT page opened in a browser (Q2 2026 chart present); values match chart | Confirmed (the page blocks curl with 403) |
| HCSP: 4.4% of GDP / about EUR 140 bn by 2031; 6.4% / about EUR 200 bn; debt 115.6 → 140 (2035) → 186 (2050), r - g = +0.5, range 146-245; -0.2%/yr vs +1.2% trend, 3 times since 1959; +2.7%/yr; 26%/20%/11% of total spending; 57.3% 2nd behind Finland | HCSP PDF re-downloaded | Confirmed, with nuances (correction 4) |
| OFCE: deficit +2.4 pts since 2017 "explained in accounting terms" by PO -2.5 (-1.6 households, -0.9 firms); transfers -0.8, investment +0.5; 2.8% / EUR 80 bn vs EUR 110 bn; unemployment 9% in 2027 | OFCE blog PDF re-downloaded | Confirmed |
| Rexecode DT 97 (Jul 2025): EUR 75 bn constant 2025 (39 households, 36 firms), EUR 66 bn current 2018-2023, EUR 74 bn 2011-2013 | PDF re-downloaded | Confirmed |
| Fipeco (27 Jan 2022): about EUR 44 bn in 2022, not offset; structural deficit 2.4% → 4.7% (RESF/PLF 2022) | PDF re-downloaded | Confirmed. Note: the 4.7% was a 2021 *forecast* for 2022 ("passerait"). |
| CAE Focus 118: 0.2% vs 0.38%; 380,000 households; scenarios +2.6/+5.2 pt = EUR 2/4 bn; expatriation 0.06-0.6% / 0.12-1.2%; at most -0.03% turnover, -0.05% value added, -0.04% employment; ISF EUR 3-4.5 bn | PDF re-downloaded | Confirmed (note on internal inconsistency added) |
| IPP Note 92: 46% (top 0.1%) vs 26% (top 0.0002%), 2016 data, June 2023 | Updated PDF downloaded | Confirmed; dead link replaced |
| Geerolf (PDF created 17 Oct 2026): 2-6 bn; 19.4 bn, 12.5 attributed to billionaires; 25.1% vs 26.8%; Heyer 11 of 20 bn; 3 families 45%; CAE "26 cents"; Blanchard 10-20 bn | PDF re-downloaded | Confirmed as reported by Geerolf (secondary for the claims about others) |
| Brülhart et al.: at least 43% after 6 years; 24% mobility; 21% house prices; evasion | AEA PDF re-downloaded | Confirmed |
| Ring NBER WP 35854: 75% → 71.5%; "at most 100 individuals" | NBER page | Confirmed; wording made precise (75% is a counterfactual; 100 is an upper bound) |
| Blanchard-Leigh β = -1.095 (t = -4.294); no bias 1997-2008 | NBER PDF re-downloaded | Confirmed (but see correction 2) |
| Insee Première 2117 (9 Jul 2026): poverty 15.4%, highest since 1996; Gini 0.302 | insee.fr page | Confirmed |
| Insee Analyses 118 (16 Apr 2026): 26 vs 3.5; 56% net beneficiaries; 99% / 96%; 51% / 36% / 20%; EUR 1,400 per CU; EUR 66 bn | insee.fr page | Confirmed |
| PLF 2027 (1 Oct 2026): 5.4% → 5.0%; debt 119.3% → 121.7%; EUR 54 bn; spending 57.1% → 56.9%; interest EUR 79.2 → 91.2 bn; growth 1% | Legifiscal page | Confirmed |
| IMF concluding statement (21 May 2026): about 0.8% of GDP/yr over 2027-2029; revenue ratio "limits scope for further revenue-based adjustment"; 57.5% spending; deficit 5.1% | imf.org page (via web fetch; curl gets 403) | Confirmed |
| CEPEJ: 11.3 judges per 100,000 vs median 17.6 (2022 data, published 16 Oct 2024; no newer cycle found) | Le Club des juristes page | Confirmed (secondary) |
| PISA 2022 math: FR 474 (473.9) vs OECD 472 (472.4); 495 in 2012 | Local OECD extract `04_oecd_pisa2022_mean_scores.csv`; OECD 2012 France note | Confirmed (context added) |

### Corrected

1. **France-Italy spread.** "France's yield has been at or above Italy's since December 2025" was wrong. On Eurostat monthly data, France was above Italy in Dec 2025-Feb 2026 and Aug-Sep 2026, but **below** it from March to July 2026 (by 3-10 bp). Fixed in Section 0 and Section 7.2.
2. **Blanchard-Leigh.** The "multipliers 0.9-1.7" range is not in NBER WP 18779 / AER 2013; it comes from IMF WEO Oct 2012 Box 1.1. The paper says multipliers were "substantially above 1". Later-vintage coefficients were "less statistically significant", not "insignificant". Fixed in Section 6.1 and S14.
3. **Teacher salaries.** OECD *Education at a Glance 2026* (29 Sep 2026) supersedes EAG 2025. Primary, 15 years: USD PPP 51,038 vs OECD 64,349 (was 49,462 vs 59,673). Lower secondary: 54,778 vs 66,583 (was 53,086 vs 61,563). Fixed in Section 8.1; S40 added.
4. **HCSP feasibility table.** Made precise: the spending fall must be sustained five years in a row; the "32 times" figure is internally ambiguous in the HCSP (the table column says 32 times in 1959-1999 plus 7 since 2000); the structural-reform frequencies are now quoted exactly.
5. **PO 2024 vintage.** Insee's 2024 PO rate was revised from 42.8% (Feb 2026) to 42.7% (May 2026 accounts, used by the Cour in June 2026). The HCSP's "42.8% in 2025" is most likely the old 2024 value. The Eurostat-definition PO 2025 (44.3%) was added. Fixed in Sections 1, 10 and 13.
6. **Spending rank divergence.** The IMF calls 2025 spending (57.5%) "the highest in the euro area"; the Oct 2026 Eurostat release puts France 2nd behind Finland. Added to Section 13.
7. **Dead link.** IPP Note 92 (`.../2023/09/Note_IPP_92-OLD.pdf`, 404) replaced with the IPP publication page and the current PDF.
8. **PISA framing.** Added that the OECD average also fell by about 15 points, so the France-specific relative decline is about 6 points.
9. **HCFP "optimistic".** This was attributed to Legifiscal [S9], which does not contain it. It is now sourced to Public Sénat / Euronews coverage [S41]; the HCFP primary text is still not retrieved.
10. **Section 12.2 reading.** "About 2 points" for the spending-gap/revenue-gap difference holds only from 2015 (1.1 pt in 2005 and 2010).

### Left unverified (⚠)

*(Status as of the first pass. Most items were resolved in the second pass below.)*


- Agrawal-Foremny-Martínez-Toledano figures (the CESifo link returns a bot-challenge page).
- CEPEJ prosecutors per 100,000 (3.2 vs 11.2) and judicial budget per inhabitant (EUR 77.2 vs 85.4): union note not re-opened.
- Already flagged by the author and not resolved here: CAE "26 cents"; EU Tax Observatory primary note; CPO EUR 2.7 bn; Pichet; Mankiw; Blanchard's "10-20 bn, 1%"; AFT average maturity (about 8.5 years); October 2026 market data; Insee Q1 2026 debt; Terra Nova, Attac, Montaigne and iFRAP positions; EU-SILC break flags; Ifop 86%; Clark Center panel.
- Jakobsen et al. "about 30% over 30 years" (via the Senate summary) was not re-opened.

### Links

- Dead: IPP Note 92 old PDF (404), replaced.
- Blocked for automated clients but live in a browser: aft.gouv.fr (403), imf.org (403 to curl; WebFetch OK), oecd.org *Restaurer les finances publiques* (403), education.gouv.fr DEPP download (403; HAL mirror added), cesifo.org (bot challenge).
- All other cited URLs returned HTTP 200 on 2026-10-25.

### Fairness of the debate presentation

The counter-arguments are presented in strong form, not as strawmen. Examples: the OFCE revenue narrative, net social spending putting the US above France, the HCSP feasibility frequencies against a spending-only strategy, consolidation multipliers, and redistribution outcomes. Think-tank and author orientation is flagged: OFCE, Rexecode (employer-funded), Fipeco, Institut Montaigne, iFRAP, Terra Nova, Attac, Geerolf's personal and polemical paper, Zucman as the proponent, and the Ifop poll commissioned by the Socialist Party. One residual point: the Section 3.3 "EUR 150 bn" comparison is arithmetically correct (5 pts × about EUR 2,990 bn GDP), but it compares a net-total public+private gap with a public deficit. The text already says private spending does not create public deficits.

---

## Verification log, second pass (2026-10-25)

*Scope: README §7 row "10" and §8 item 6, plus every remaining ⚠ in this file. New raw files under `research/data/raw/10_verify2/` (CPO report and synthesis, USM notes, Agrawal et al. author version, Jakobsen et al. NBER and QJE accepted versions, Senate report pages, Zucman bill no. 768, iFRAP no. 270, Montaigne note, HCFP opinion 2026-5, Eurostat `ilc_li02` France, Insee quarterly debt SDMX). The AFT maturity page was read in a browser (403 to scripts). The web search budget ran out mid-pass.*

### Cross-file alignment with file 00

| Item | Change |
|---|---|
| README §8 #6: §0 item 4 still showed PISA 2012/2022 | Now PISA 2025: 458 vs OECD 463, 29th of 38 (file 00 row 49). |
| Deficit base for shares (README note) | §5.1 share of the deficit now computed on EUR 151.6 bn (file 00 row 31); 13% unchanged. |
| PO 2024 and change since 2017 | §10 now leads with 42.7% (canonical); §4.1 labels OFCE's -2.5 pts as the earlier vintage and gives -2.6 pts (file 00 rows 26-27). |
| Euro-area comparator | §1 states that euro-area aggregates on the site use EA21 (file 00 conventions). EA21 values are added next to EU-27 aggregates for D.62 (16.8%) and D.1 (10.0%) (file 00 rows 18-19). |
| Ifop 86% | ⚠ removed after checking file 14's verification (Ifop PDF no. 121870; fieldwork 10-11 Sep 2025). The date was corrected. |
| PISA 2025, PLF 2027 staffing plan | PISA was already updated in §8.2 and §12.3; the staffing plan does not appear in this file. |

### Confirmed (⚠ removed)

| Item | Primary check | Result |
|---|---|---|
| CEPEJ prosecutors 3.2 per 100,000 (median 11.2, average 12.2) | USM note of 29 Oct 2024 quoting CEPEJ 2024 (2022 data) | Confirmed. The CEPEJ primary PDF blocks automated download, so the source is the union's transcription. |
| CEPEJ judicial budget EUR 77.2 per inhabitant vs average 85.4 | USM notes of 18 and 29 Oct 2024 | Confirmed. Added the **European median of EUR 74.8**: France is above the median, so the text now says so. |
| Terra Nova, Attac, Montaigne and iFRAP positions | Primary pages and PDFs [S42]-[S45] | Confirmed and quoted with dates. Terra Nova's note is skeptical of high wealth-tax yields, so it is no longer listed as a plain "revenue narrative" proponent. |
| HCFP "optimistic" | HCFP opinion 2026-5, 25 Sep 2026, synthesis | Confirmed from the primary text [S47]. |
| Zucman 15-25 bn | Bill no. 768, 7 Jan 2025 | Confirmed as the proponents' own claim [S22]. |
| EU-SILC break flags | Eurostat `ilc_li02` France | Breaks are flagged in 2020 and 2022; the text was updated. |

### Corrected

1. **Agrawal-Foremny-Martínez-Toledano:** the published AEJ: Applied 2025 version gives **about 7.5% by six years** (was "+9-10% after 5 years", from the working-paper drafts). The "six times" PIT loss is confirmed in the abstract.
2. **Jakobsen et al.:** "1-point cut, about 30% over 30 years at the top" (Senate/CPO wording) is the paper's *moderately wealthy* result. The very top is **65% after 30 years** (an upper bound), from 31% after 8 years.
3. **CAE "26 cents":** located in CAE Focus 118. It is Jakobsen et al. (2024) for Scandinavia (54 + 20 cents lost, i.e. 74%), *quoted* by the CAE, not a CAE estimate for France.
4. **CPO:** the primary report contains no "EUR 2.7 bn". Its illustration is **EUR 1.4 bn** (0.5% on non-professional wealth above EUR 5 m, before behavioral effects), within a package designed to be revenue-neutral. "0.5-1.8%" is the constitutional ceiling range, not a proposed rate.
5. **AFT average maturity:** 8 years 158 days (about 8.4 years) at 30 Sep 2026 (was "about 8.5 years", from snippets).
6. **Insee Q1 2026 debt:** EUR 3,535.9 bn (was 3,536.1); the latest quarter is Q2 2026, EUR 3,595.5 bn = 119.0% of GDP.

### Still unverified (⚠ kept, with recommendation)

| Item | Why | Recommendation |
|---|---|---|
| EU Tax Observatory 19.4 / 12.5 bn split | Note not found on taxobservatory.eu; known only via Geerolf | Drop from site; keep the 15-25 bn range sourced to bill no. 768 |
| Blanchard "10-20 bn, 1%" | Only via Geerolf (no link); search budget exhausted | Drop from site |
| Pichet (2007) | Primary not retrieved | Drop from site |
| Mankiw | From memory | Drop from site; replace with the verified CPO, Montaigne and Terra Nova rows |
| Rexecode "2.5 bn/yr lost through departures" | Secondary, no primary located | Drop from site |
| ~~October 2026 yields and spreads (> 5%, 140-170 bp)~~ | Resolved 2026-10-25 (index pass) by file 06: TEC 10 5.126% (22 Oct), spread 169 / 166 bp (22 / 23 Oct) | Use the official daily values (00 row 43) |
| Clark Center panel | Not re-checked | Drop from site |
| ~~Eurobarometer 65%~~ | Resolved 2026-10-25 (index pass): verified by file 14 in the primary Flash Eurobarometer 562 (Ipsos for DG TAXUD, fieldwork 9-17 Apr 2025; FR 65%, EU-27 65%) | Usable, cite Flash Eurobarometer 562 |

