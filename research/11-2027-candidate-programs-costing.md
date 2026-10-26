# 11: The 2027 presidential programs, costed one proposal at a time (annual 2027 and 2032 EUR and % of GDP)

*Research file for the public-finance education platform. Status as of 2026-10-25. All amounts are in billions of euros (bn EUR) at current prices, unless stated otherwise. Sign convention used throughout: **+ improves the general-government balance** (new revenue or a saving); **− worsens it** (a cost). This file extends file 07 (§3.8, "2027 presidential packages"). It does not repeat 07's analysis of the Zucman tax, the ISF, the CDHR or the energy shields. It reuses 07's denominators, so the two files stay consistent.*

---

## 0. Scope, method and definitions

**What this file adds to file 07.** File 07 covered the 2024 legislative costings (Institut Montaigne) and five partial 2027 packages, with annual, cumulative and end-of-term amounts mixed together. This file does five things:

1. It lists every declared or likely 2027 candidate as of 2026-10-25, with the date and URL of each primary program or counter-budget, where one exists (§2).
2. For each measure with fiscal weight, it gives the party's claimed amount and every independent estimate found (§4).
3. It converts every figure to an **annual amount in a stated year** (2027 and 2032), in bn EUR and % of GDP. It compares those amounts with the 2026 deficit, the 2027 target and the debt-stabilizing gap, and it gives a net balance per program (§3, §5).
4. It reviews the non-budget economic evidence on price freezes for rents, fuel and essential goods (§6).
5. It checks whether any independent costing or simulator of the 2027 programs (Institut Montaigne, IPP, OFCE) existed on 2026-10-25 (§7).

The machine-readable companion is `research/data/11_candidate_measures.csv` (72 rows). It is built by `research/scripts/11_build_csv.py`.

**Conversion rules (read before using any number below)**

| Rule | Application |
|---|---|
| R1. Denominators | **2027 GDP = 3,135.0 bn EUR** (PLF 2027 article liminaire, via HCFP opinion 2026-5 [S3]). **2032 GDP ≈ 3,582 bn EUR**: this is **our own assumption**, not an official forecast. It extrapolates 2027 at +2.7% nominal growth a year, the PLF's 2026→2027 nominal growth rate. Sensitivity: at +2.0% a year it is 3,461 bn; at +3.5% a year it is 3,723 bn. No official 2032 GDP was found. The PLF 2027 and the HCFP opinion stop at 2029-2030. |
| R2. "2027" amounts | These are a full-year effect at 2027 prices, unless flagged "first year". LFI's inheritance line and its tax on multinationals are explicitly "first year". |
| R3. "2032" amounts | (a) Where the party or an independent body gives a 2032 (or 2030-2031) **level**, we use it as is and divide it by 2032 GDP. (b) Where only a 2027 amount exists for a measure whose base grows with the economy (taxes, wage bills), we scale it by nominal GDP (×1.1425), which keeps it at the same % of GDP. (c) Where a measure ramps up (pension age), we use the independent ramp-up estimate. |
| R4. Cumulative vs. annual | A five-year **cumulative** sum is never shown as an annual figure. Where a source is ambiguous (LR's "197 bn over five years"), both readings are shown (§5.3). |
| R5. Static vs. behavioral | Party figures are static (rate × base). Independent ranges include behavioral responses only when the source does (CAE, Senate report, IPP). |
| R6. % of GDP vs. % of spending | Every ratio is **% of GDP** unless labeled "% of total public expenditure". For the latter, 2025 total public expenditure is **1,714.1 bn EUR = 57.3% of 2025 GDP** (Eurostat `gov_10a_main`, 21 Oct 2026, canonical in `00-reference-figures.md` row 1; Insee May 2026: 1,714.2 bn, incl. tax credits) [07/S1]. *(corrected 2026-10-25: was "1,714.2 bn (Insee)" only)* |

**Benchmarks**

| Benchmark | bn EUR | % of GDP | Source |
|---|---|---|---|
| 2025 deficit (outturn, Maastricht, general government) | **151.6** *(corrected 2026-10-25: was 152.5, the May 2026 Insee vintage; 151.6 is the October 2026 EDP notification, canonical in `00-reference-figures.md` row 31)* | 5.1 | Eurostat `gov_10dd_edpt1`, Oct 2026 EDP notification (21 Oct 2026); PLF 2027 article liminaire via HCFP [S3]; earlier vintage: Insee Première 2106 (2026-05-29) [07/S1] |
| **2026 deficit (forecast)** | **164.9** | **5.4** | PLF 2027 / HCFP 2026-5 (2026-09-25) [S3] |
| **2027 deficit target** | **158.1** | **5.0** (5.04 on unrounded figures) | PLF 2027 / HCFP [S3] |
| **Gap to the debt-stabilizing balance** | **89.6** (2025) ≈ **94** at 2027 GDP ≈ **107** at our 2032 GDP | **3.0 pts** | Cour des comptes, RSPFP June 2026 (2025 gap = 3.0 pts = 89.6 bn) [S28]; 2027/2032 conversions are ours |
| Adjustment needed to stabilize debt by 2032 vs. the unchanged-policy trend | ~125 | **structural** primary surplus of 0.8% of GDP | IGF mission on public-finance transparency (Jaravel, Ragot, Tavernier, Valla), July 2026 [S29]. ~~LFI cites this "Bercy-commissioned report" as its benchmark [S1].~~ *Fact-check 2026-10-25: no reference to the IGF report, to "125 bn" or to Bercy appears in the text of the LFI PDF [S1]; LFI's written benchmark is debt-ratio stabilization "within one term". **Verified 2026-10-25 (third pass):** at his 14 Oct 2026 press conference, Mélenchon said his plan was "dans l'épure" of a "*rapport d'économistes rendu à Bercy*" calling for "at least 125 bn" of effort over the term (Public Sénat/AFP, 2026-10-14 [S4b]). The description matches the IGF mission [S29]; the IGF is not named in the article. Use "Mélenchon cited, orally, the economists' report submitted to Bercy", not "the LFI document cites the IGF report".* |
| Total public expenditure 2025 | **1,714.1** (Eurostat; Insee 1,714.2) | 57.3 | Eurostat `gov_10a_main` (21 Oct 2026); Insee [07/S1] *(corrected 2026-10-25: was 1,714.2, Insee only)* |
| Compulsory levies (*prélèvements obligatoires*, PO, Insee concept, net of tax credits) | n/a | 43.6 (2025) → 44.2 (2027f) | Insee; HCFP [S3] |
| Interest payable, general government (ESA D.41, national accounts) | **65.7** (2025) → 79.2 (2026f) → ~91 (2027f) | 2.2 → 2.6 → 2.9 | Eurostat `gov_10a_main` (21 Oct 2026) for 2025; PLF 2027 via HCFP [S3] for 2026-2027 *(corrected 2026-10-25: was "66 (2025)"; the HCFP's 66 is Eurostat's 65.7 rounded, canonical in `00-reference-figures.md` rows 39-40; Insee IP 2106 shows 64.7 bn in a table footnoted as excluding the FISIM correction on interest)* |

*The user's starting figures (1,714 bn = 57.3% of GDP in spending; 43.6% PO) were confirmed in files 07 and 05 and are not re-verified here. Drees's 31.9% is outside this file's scope.*

---

## 1. Key figures (headline table)

| # | Indicator | Value | Unit | Year | Source (publication date) |
|---|---|---|---|---|---|
| 1 | LFI 2027 "budget orientations": revenue / new spending / net | +106.4 / −81.7 / **+24.7** | bn EUR (0.79% of 2027 GDP net) | 2027 | LFI, *Comment nous allons remettre de l'ordre dans les comptes publics* (2026-10-14) [S1] |
| 2 | LFI items announced in the same document but **not costed** | SMIC 1,700 EUR net; fuel-price freeze at 1.70 EUR/l; retirement at 60 "within the term"; end of contribution relief above 2 SMIC | n/a | 2027 | [S1] |
| 3 | Our cost estimate of LFI's fuel freeze, if financed by tax cuts at 16 Oct 2026 pump prices | **−26.5** (0.85% of GDP) **if Oct-2026 spot prices (Brent 127.7 $/b) persisted through 2027**; ~0 at 2025 average prices. *Fact-check: the PLF 2027 assumes Brent at 80.3 $/b in 2027 (HCFP [S3]). ~~At such a price the cost would be of the order of a few bn (⚠ own rough approximation).~~ **Recomputed 2026-10-25 (own scenario, see §6.2):** about **−12 bn/yr** at the PLF's 80.3 $/b and about **−20 bn/yr** at the 105.8 $/b ICE futures price, if a lower Brent passes fully into pump prices and refining and distribution margins stay at their October 2026 level; toward 0 if margins also return to 2025 levels. Rule of thumb: each 0.10 EUR/l above 1.70 on all road fuel ≈ 4.6 bn/yr.* | bn EUR / yr | Oct 2026 prices (scenario for 2027) | Own computation from DGEC weekly bulletin (2026-10-16) [S20]; HCFP [S3] |
| 4 | LFI net, our measure-by-measure independent range | **−83.8 to +17.5** (−57.3 excluding the fuel freeze) | bn EUR | 2027 | Own aggregation (§5.1); **not an institutional costing** |
| 5 | RN counter-budget: net savings target | **140** by 2032 (a **level** vs. 2026; 3.9% of 2032 GDP); 30 net tax cuts over the term; deficit 3.7% in 2027, < 3% in 2030, 2.2% in 2032; debt 112.1% in 2032. The RN press kit itself shows a net balance improvement of **71.6 (2027) and 141.7 (2031)** | bn EUR | 2027-2032 | Public Sénat (2026-10-06) [S5]; Euronews (2026-10-07) [S6]; RN press kit figures as transcribed by the Institut de l'Entreprise [S7a] |
| 6 | RN: Institut de l'Entreprise (IdE, business-funded) assessment | RN net balance improvement recalculated line by line: **69.3 (2027) / 140.3 (2031)** (RN prints 71.6 / 141.7). **Credible net improvement: 2.9 in 2027 and ~7.5 in 2031 (range −25 to +50)**; 80% of 2031 gross financing undocumented, legally fragile or without Maastricht effect. Deficit **5.9% in 2027 and 6.5% in 2031** (RN: 3.7% and 2.3%); debt ~130% in 2031; the 2027 balance about **25 bn worse than the government's PLF 2027**. *(corrected 2026-10-25: primary note now opened. The earlier "⚠ blocks sum to 89.3 / 183.4" flag is resolved: the press relay [S7] dropped the IdE table's negative rows (all firms −12.0 / −11.1; household taxes −24.7 / −22.1; household benefits +0.1 / −19.1) and two positive rows (large firms +13.1 / +5.6; PLF measures kept +3.6 / +3.6). With all eleven rows the sums are 69.4 / 140.3. The 69.3 / 140.3 are **net**, not gross, amounts.)* | bn EUR | 2027-2031 | IdE, *Contre-budget du RN : 140 milliards affichés, moins de 10 milliards crédibles*, note de contexte (2026-10-06) [S7a]; press relay [S7] |
| 7 | LR (Retailleau): savings | **197** "over five years" (146 to the deficit, 51 returned as tax cuts; the source also prints 56); deficit < 3% in 2031, 2.2% at end of term | bn EUR | 2027-2032 | Public Sénat (2026-10-12) [S8] |
| 8 | Renaissance (Attal): savings | 150 over the term (not itemized); 20 "emergency brake" from May 2027; < 3% before 2032; balance in 2037 | bn EUR | 2027-2032 | iFRAP comparator (accessed 2026-10-25) [S11]. **No primary document found.** |
| 9 | Horizons (Philippe): alternative 2027 budget | +10 savings / −10 tax rises cancelled = **0 net** vs. PLF 2027; undo the pension suspension +1 | bn EUR | 2027 | Moneyvox/AFP (2026-10-13) [S9] |
| 10 | Glucksmann (PS–Place publique): wage-levy cut financed by inheritance taxes | −15 / +15 (2 + 3 + 10) | bn EUR | term | Parlons-politique (2026-08-24) [S12]; iFRAP [S11] |
| 11 | Independent (institutional or academic) costings of 2027 programs | **None found** (Montaigne, IPP, OFCE, Terra Nova, Rexecode, Fipeco, Cour des comptes) | n/a | as of 2026-10-25 | §7 |
| 12 | Rent control (*encadrement des loyers*): rent moderation | **−2% to −4%**, reaching −5% at the end of the period; ~**0.6 bn/yr** transferred to tenants, **one-third borne by public finances** via lower taxes on rents | %; bn EUR | 2019-2024 | IPP Note n° 125 (Chapelle, Fack, May 2026) [S18] |
| 13 | Rent-control compliance: share of new leases above the upper cap | Paris 35.6%; Est Ensemble 41.3%; Plaine Commune 42.1%; Bordeaux 43.5%; Lille 32.8% | % of leases | 2020-2024 | IPP Note 125, Table 1 (DGFiP GMBI data) [S18] |
| 14 | Energy shields 2021-2024 | ~72 gross, 36 net; "for the most part, not targeted by income" | bn EUR cumulative | 2021-2024 | Cour des comptes (2024-03-15) [S19] |
| 15 | Pump prices, week of 2026-10-16 | Diesel 2.346 EUR/l; SP95-E10 2.149 EUR/l (Brent spot 127.7 $/b) | EUR/l | Oct 2026 | DGEC weekly bulletin [S20] |

---

## 2. Declared and likely candidates as of 2026-10-25 and their primary documents

**Calendar.** First round **18 April 2027**, second round **2 May 2027** (Public Sénat, 2026-10-14 [S2]; the LFI document gives the same date [S1]). The official list of candidates will only be known once the 500 elected-official sponsorships are validated. Franceinfo counted 34 declared candidates on 2026-10-22 [S3b].

| Party / camp | Candidate (status on 2026-10-25) | Primary program or counter-budget: date and URL | Fiscal content | Costing status |
|---|---|---|---|---|
| **La France insoumise (LFI)** | **Jean-Luc Mélenchon**, declared (4th run) [S2] | *Comment nous allons remettre de l'ordre dans les comptes publics* (22 pp.), presented 2026-10-14: https://melenchon2027.fr/wp-content/uploads/2026/10/Comment-nous-allons-remettre-de-l-ordre-dans-les-comptes-publics.pdf . Program *L'Avenir en commun* (1,069 measures; book "available 6 November"): https://melenchon2027.fr/programme/decouvrir/ | Itemized 2027 budget (§4.1) | **Party only.** The document "does not constitute a full costing" of the program [S1]. The full costing is announced for early 2027 [S4]. |
| **Rassemblement national (RN)** | **Marine Le Pen**, declared on 2026-07-07 [S3b]. Jordan Bardella was re-elected RN president on 2026-10-24 (98.98%) and is **not** a declared candidate [S2]. | Counter-budget presented 2026-10-06 (press conference). **No PDF of the 2027 counter-budget was found on rassemblementnational.fr.** The only document posted there is the *Contre-budget 2026* (PDF created 2025-10-24): https://rassemblementnational.fr/documents/GRN-CONTRE-BUDGET-2026.pdf . *Re-checked 2026-10-25 in a browser (homepage "documents" block and *Conférences de presse* page): still not posted.* The press kit is titled *Pour la Renaissance de la France : l'urgence de réparer les finances publiques* (dossier de presse, 2026-10-06; 125 measures in an annex, slides 24-26), per the IdE note [S7a]. The figures below come from the press [S5], [S6] and from the IdE's line-by-line transcription of the annex [S7a]. | 140 bn net savings by 2032 (§4.2) | Institut de l'Entreprise note (2026-10-06), **primary opened** [S7a] |
| *RN: eligibility* | Appeal ruling of **2026-07-07**: 3 years of prison (1 firm, under electronic tag), 100,000 EUR fine, ineligibility cut to **45 months, 30 of them suspended, without provisional execution** (first instance: 5 years with provisional execution). Le Pen announced a **cassation appeal**. The Cour de cassation said it could rule "**at the latest in early April 2027**". Jurists disagree on whether the cassation appeal leaves her eligible in the meantime, and the Conseil constitutionnel will rule on the candidate list [S10]. | | | **Open legal risk.** If she cannot stand, Bardella is the obvious substitute (our inference; no RN statement found). |
| **Les Républicains (LR)** | **Bruno Retailleau**, designated by LR members in April 2026 [S2]. Dissident right: David Lisnard (Nouvelle Énergie), Xavier Bertrand and Gilles Platret have declared intentions [S2]. | Plan presented 2026-10-12. Campaign site https://avecretailleau.fr/ (its FAQ refers to a PDF "booklet" as the authoritative costing; **the booklet was not located**) [S8], [S8b] | 197 bn savings (§4.3) | Party only |
| **Horizons** | **Édouard Philippe**, declared [S2] | Alternative 2027 budget (Horizons, via L. Marcangeli, 2026-10-13) [S9]; program interview on France 2, reported on 2026-10-09 [S9b]. **No primary document found.** | §4.4 | Party only |
| **Renaissance** | **Gabriel Attal**, declared per Franceinfo [S3b] (Public Sénat describes him as competing with Philippe for the center [S2]) | **No primary program document found.** Figures come from the iFRAP comparator [S11] and secondary press. | §4.5 | Party only |
| **PS / Place publique** | **Raphaël Glucksmann** won the social-democratic primary on 2026-10-11 with 66%, ahead of **Olivier Faure** (now withdrawn) [S2], [S3b]. He declared on 2026-08-23 on TF1 [S12]. Karim Bouamrane (PS mayor) runs outside the primary [S2]. | **No official program PDF found.** Sources: iFRAP [S11]; Parlons-politique [S12]. | §4.6 | **None** ("no global costing" according to trackers) |
| **Les Écologistes** | **Marine Tondelier**, declared (Oct. 2025 per Franceinfo). Her candidacy needs a **members' vote on 2026-12-13** [S2], [S3b]. | **No program document found.** Sources: iFRAP [S11]; Franceinfo pensions survey [S13]. | §4.7 | None |
| **PCF** | **Fabien Roussel**, declared on 2026-09-06 [S2] | **No program document found**; iFRAP [S11] | §4.8 | None |
| **Reconquête** | **Éric Zemmour**, declared on 2026-09-17 [S2] | **No 2027 program document found**; iFRAP [S11]; Franceinfo [S13] | §4.8 | None for 2027 (2022 costings exist; see §4.8) |
| Others | Ruffin (Debout !), Batho, Arthaud, Kazib, Labib, Dupont-Aignan, Philippot, Lassalle, Asselineau, Polony (2026-10-14), Becht, Lisnard, etc. [S2] | iFRAP lists Lisnard (200 bn of savings by 2032, 80 bn in year one) and Dupont-Aignan (~130 bn by 2032, incl. +15 from leaving the EU) [S11] | n/a | None |

---

## 3. Converting claims to annual amounts: the comparability problem

Party headlines are not comparable as published:

| Program | Headline | What it is | Annual equivalent we use |
|---|---|---|---|
| LFI | +106.4 / −81.7 / +24.7 | One budget year (2027) | 2027: as given |
| RN | 140 bn | A **level** in 2032 vs. 2026 ("by 2032"); the 2027 items mix first-year and full-year amounts (immigration 15.1 in 2027, 29 in a full year) | 2032 level = 3.9% of 2032 GDP; 2027 **net** improvement 71.6 claimed (69.3 on the IdE's recalculation; gross revenue and savings 140.8, offset by 53.2 of tax cuts and 16.1 of new spending) [S7a] *(corrected 2026-10-25: was "2027 gross savings 69.3")* |
| LR | 197 bn "over five years" | **Ambiguous.** The pension line (42) is described by Franceinfo as "cumulative over five years" (40) [S13]. But the 25 bn for 400,000 non-replacements only makes sense as an **annual level at the end of the term** (400,000 × ~63k EUR ≈ 25 bn a year). | Both readings shown in §5.3 |
| Renaissance | 150 bn | "Over the term", not itemized | Treated as an end-of-term level (upper reading) |
| Horizons | 10 bn | 2027 budget year | 2027 |

**Order of magnitude for the public.** 1% of 2027 GDP ≈ **31 bn EUR**. 1% of 2032 GDP ≈ **36 bn EUR** (our assumption).

---

## 4. Measure by measure: claimed vs. independent estimates

*Columns: "Claimed" is the party's own figure. "Independent" is every non-party estimate found; the orientation flags follow file 07 (Montaigne: business-funded, liberal; iFRAP: liberal, favors spending cuts; Institut de l'Entreprise: business-funded; Fipeco: ex-Cour des comptes, fiscal-discipline orientation; CAE and IPP: public/academic; francebudget.fr: **non-institutional** citizen simulator, open code, no named authors, used only as a flagged cross-check). "2027" and "2032" are annual amounts in bn EUR and % of GDP (rules R1-R3).*

### 4.1 LFI (Mélenchon): the 2027 "budget orientations" (primary document, 2026-10-14) [S1]

We verified in the PDF that the revenue lines sum to 106.4 and the spending blocks to 81.7 (37.5 + 22.2 + 10 + 12). The document's net is "24.7 bn of deficit reduction". The press rounds it to 25.

**Revenue (+)**

| Measure | Claimed 2027 | Independent estimate(s) | 2027, % GDP (claimed / indep.) | 2032 (bn, scaled) | Source |
|---|---|---|---|---|---|
| Zucman tax (2% floor > 100 M EUR) | +15 | +2 to +3 (Senate report, if CIT is credited); ~+5 (seven economists incl. Aghion, post-behavior); +20 (15-25) (Zucman, static) | 0.48 / 0.06-0.64 | 17.1 claimed | [S1]; Senate report n° 689 [07/S4]; file 07 §3.1 |
| "Reinforced" ISF (press: "ISF climatique") | +10 | +3 to +4.5 (CAE: mechanical loss from ISF repeal); 2017 ISF net yield 4.1. It **overlaps** with the Zucman base, so the two cannot be added in full. | 0.32 / 0.10-0.14 | 11.4 | CAE Focus 118 [07/S5] |
| Abolish the flat tax (PFU) | +9 | +3.2 (Montaigne 2024, incl. exit tax; liberal); France Stratégie: the PFU's static cost (~1) was offset by higher dividends, so repeal could yield little | 0.29 / 0.03-0.10 | 10.3 | [07/S14], [07/S4] |
| Inheritance reform | +20 "the first year" | CAE Note 69: **+9 to +19 in steady state** (base-broadening scenarios). Current DMTG yield (inheritance and gift duties) is 21.1 (2025), so LFI's figure implies **nearly doubling** it in year one. First-year cash is lower because duties are paid within 6 months of death (our caveat). | 0.64 / 0.29-0.61 | 22.8 | CAE [S16]; Insee via file 05 |
| Trim "unjust" tax and social expenditures (CIR, Dutreil, home-employment credit…) | +22 (in 2027) | **None.** Context: tax expenditures total 91.8 bn (2025); CIR 7.1, home-employment credit 7.1, *pacte Dutreil* 3.8 (Cour des comptes, April 2026) | 0.70 / n/a | 25.1 | [S1]; Cour NEB [S17] |
| Restore CVAE (business value-added tax) on largest firms | +3 | None (CVAE yielded 3.7 in 2025 vs. 15.2 in 2019; file 05) | 0.10 | 3.4 | [S1] |
| Progressive corporate income tax (IS) | +3 | None | 0.10 | 3.4 | [S1] |
| "Universal tax on multinationals" | +5 (first year) | None. Unilateral design; legal and treaty feasibility not assessed. | 0.16 | 5.7 | [S1] |
| Digital tax ("GAFAM") to 15% | +3.9 | None | 0.12 | 4.5 | [S1] |
| Windfall-profits tax | +5 | None | 0.16 | 5.7 | [S1] |
| Financial transactions tax | +5 | None. Context: the current FTT yielded **2.53 bn in 2025** (rate 0.4% since April 2025; 121 companies; 95% of traded amounts exempt). The Cour des comptes found "no obvious, immediately practicable way" to broaden the base and warns of rapid relocation of transactions [S33]. +5 implies roughly tripling the yield. *(corrected 2026-10-25: was "current FTT ~2 bn, ⚠ unverified")* | 0.16 | 5.7 | [S1]; Cour des comptes [S33] |
| Share-buyback tax / crypto-assets | +2.5 / +1 | None | 0.08 / 0.03 | 2.9 / 1.1 | [S1] |
| Anti-fraud | +2 (first year) | +1 to +3 at the margin (file 07 synthesis). The HCFP calls budgeted anti-fraud yields "optimistic, even hypothetical". | 0.06 | 2.3 | [S1]; HCFP [S3] |
| End of contribution relief above 2 SMIC | **not costed** | None found | n/a | n/a | [S1] |
| **Total revenue** | **+106.4** | **Our range +34 to +100** (sum of measure ranges; Zucman and ISF not double-counted) | **3.39** / 1.1-3.2 | 121.6 | Own |

**Spending (−)**

| Measure | Claimed 2027 | Independent estimate(s) | 2027, % GDP | 2032 | Source |
|---|---|---|---|---|---|
| Civil-service index point +10% | −17 | **−24** (2.4 bn per +1%, minister's office, July 2026; secondary); −20 (Montaigne 2024 for +10%) | −0.54 / −0.64 to −0.77 | −19.4 to −27.4 | [S1]; [07/S33]; [07/S15] |
| Indexation of all pensions, family allowances and APL, "raised by 10%" | −8 | None. **The wording is ambiguous.** A 10% rise in *all pensions* alone would cost ~36 bn (363 bn × 10%; HCFP pension envelope). The 8 bn is plausible only for indexation plus +10% on family and housing benefits. | −0.26 | −9.1 | [S1]; [S3] |
| Youth "autonomy guarantee" (1,337 EUR/month) | −9.5 | −12.3 (Montaigne 2024 for the NFP version; design may differ) | −0.30 / −0.39 | −10.9 to −14.1 | [S1]; [07/S15] |
| Repeal of the 2023 pension reform (back to 62) | −9 (2027) | ~~−3.4 to −5 in the first year (CNAV figures via press, ⚠ unverified)~~ **−3.4 in the first year (2025 repeal) and −16 in 2032**, CNAV estimate as quoted in Assemblée nationale amendment n° 728 to PPL n° 613 (25 Nov 2024, MoDem group, opposed to repeal) [S34] and in the Senate; the CNAV note itself is still not public (⚠ keep with caveat: "CNAV estimate, as cited in Parliament"; the "−5" upper bound had no source and is dropped; the estimate assumed a 2025 repeal, before the 2025-2026 suspension) / **−17 in 2030** (Fipeco, incl. accompanying measures) | −0.29 / −0.11 to −0.16 | **−16 to −17 (0.45-0.47% of 2032 GDP)** | [S1]; file 03 |
| Retirement at 60 with 40 years ("objective within the term") | **not costed** | Montaigne 2022 (LFI 2022 version): **−85.8** (range −36 to −112.8), pension schemes only, in 2027. *Fact-check: the 85.8 median is a broader package (reversal of age measures since 1993, pension computed on the 10 best years, minimum pension at SMIC level, RSA years counted). The **age-and-quarters-only** reading is the low scenario, **−36**; LFI's own 2022 counter-costing put the 60/40 item at −27. The 2026 PDF also promises "the minimum pension at SMIC level for a full career", so the broader range remains relevant.* 2024 NFP package (repeal + 60 + other items): −58. | n/a / −1.15 to −3.60 | −41 to −129 if fully in force | [07/S14]; Montaigne 2022 [S15] |
| Repeal of unemployment-insurance reforms | −3 | None | −0.10 | −3.4 | [S1] |
| Other emergency spending: free canteens 3.6, 250,000 university places 3.5, hospitals 3, violence plans 4.6, ministries' budgets restored 7, 10,000 teachers 0.5, homelessness 3, ecological planning 10 | −35.2 | None | −1.12 | −40.2 | [S1] |
| **SMIC to 1,700 EUR net** | **not costed** | Own scaling of Montaigne 2024 (−3.5 for 1,600 net, i.e. +14% at the time). 1,700 net is **+15%** vs. ~1,478 net in force since June 2026 (file 07) → **about −3.5 to −4** (public finances only: public wage bill + contribution relief) | −0.11 to −0.13 | −4.0 to −4.6 | [07/S17]; own |
| **Fuel-price freeze at 1.70 EUR/l "by decree"** | **not costed** | Own computation, §6.2: **−26.5** if achieved through tax cuts at 16 Oct 2026 prices *(spot scenario; at the PLF's 80.3 $/b Brent for 2027, about −12, and at the 105.8 $/b futures price about −20, own scenario with full crude pass-through and unchanged margins (corrected 2026-10-25: was "a few bn, ⚠ own approximation"))*; ~0 at 2025 average prices | −0.85 (spot scenario) | price-dependent | [S20]; [S3]; own |
| **Total spending** | **−81.7** | Our range **−79 to −88** for the costed lines; **−83 to −118** including the SMIC and fuel freeze | −2.61 | −93.3 | Own |

**Debt and financing devices outside the budget.** These carry no Maastricht value: "100 bn a year" of investment by a public banking pole, the Livret A ceiling raised to 30,000 EUR (30-40 bn mobilized), and an ECB "freeze or cancellation" of public debt it holds [S1]. ECB cancellation would require the agreement of the ECB Governing Council. Debt cancellation by a central bank is widely regarded as incompatible with the monetary-financing prohibition of Art. 123 TFEU. LFI asserts the opposite [S1]. This is a **legal disagreement**; we have not verified a legal opinion on it this session.

### 4.2 RN (Le Pen): 2027 counter-budget (press conference 2026-10-06) [S5], [S6], [S7]

| Measure | Claimed | Year | Independent estimate(s) | 2027 % GDP / 2032 % GDP | Source |
|---|---|---|---|---|---|
| **Net savings** | **+140** (15 more than at the Medef debate in late August); press-kit net balance improvement 71.6 (2027) and 141.7 (2031) | level in 2032 vs. 2026 | Institut de l'Entreprise: **credible net +2.9 in 2027 and +7.5 in 2031 (range −25 to +50)**; 80% of 2031 gross financing undocumented, legally fragile or with no Maastricht effect (13 lines carry 127.8 bn), incl. 23.5 bn of entries with no Maastricht effect (precounted-interest bills 4.2, transfers between government subsectors 7.0, double-counted interest saving 3.0, energy-certificate rebudgeting 9.3) and 18 bn from withholding VAT at source (vs. a total VAT collection gap of 12 bn in 2023, European Commission). IdE method: category A 100%, B 50%, C and D 0%, all costs 100% [S7a] | 2032: **3.9%** claimed / 0.2% (IdE central) | [S5], [S7a] |
| Net balance improvement by contributor, 2027 → 2031 (IdE transcription of the RN annex; + = improves the balance) | large firms (taxes) +13.1 → +5.6; all firms incl. SMEs (taxes) −12.0 → −11.1; household taxes −24.7 → −22.1; household benefits and rights +0.1 → −19.1; immigration +15.1 → +29.0; EU +11.1 → +19.5; energy/networks/concessions +20.6 → +29.0; fraud +1.1 → +23.8; social security +19.0 → +53.1; State, operators and local authorities +22.4 → +29.0; PLF 2027 measures kept +3.6 → +3.6; **total 69.3 → 140.3** (RN prints 71.6 / 141.7). *(corrected 2026-10-25 from the primary note [S7a]: was a six-block "gross savings" list relayed by [S7] that omitted five rows and therefore summed to 89.3 / 183.4; the ⚠ flag is removed.)* | 2027 / 2031 | see above | 2027: 2.21% net (IdE) / 2.28% (RN) | [S7a] |
| Net tax cuts | −30 | over the term | none | 2032: −0.84% | [S5], [S6] |
| Cap the **net** EU contribution at 5 bn | +9 (Bardella); +11.1 (2027) → +19.5 (2031) in the IdE tabulation; +13.1 elsewhere in the same note | 2027 | **Legal yield ~0**: the contribution follows from the Own Resources Decision, adopted unanimously and ratified by every member state (Economy Minister R. Lescure; IdE [S7a]). Context: France's gross contribution (*PSR UE*, EU levy on State revenue) is 31.2 bn expected in 2027 (Cour des comptes via IdE; HCFP: 31). **Net contribution (verified 2026-10-25, own computation from European Commission data [S35]):** in 2025 France paid 25.1 bn (own resources 25.9 incl. 2.1 of customs duties, −0.8 of balances and adjustments) and received 16.4 bn of EU-budget spending (excl. NextGenerationEU), a net contribution of about 8.7 bn on our own method. **The official figures (Budget Directorate, PLF 2027 *Jaune* "Relations financières avec l'Union européenne", pp. 157-158; file 16 §3.1) are EUR 9.5 bn on the accounting method (total own resources 25,865 m minus EU spending in France 16,391 m; 0.31% of GNI) and EUR 6.4 bn on the Commission's operating-balance convention (0.21% of GNI)**; the website uses these. The IdE gives "about 9 bn". Capping the net contribution at 5 bn would therefore "save" at most **about 1.4-4.5 bn**, not 9-13, even if it were legal. *(corrected 2026-10-25: was "the net figure was not verified"; then corrected again in the index pass of 2026-10-25: was "about 8.7 bn; operating balance about 7.2 bn (2024: 6.4 bn); at most 2-4 bn". Our 8.7 bn subtracted the "balances and adjustments" line (-0.77 bn), which the official method does not, and the "2024: 6.4 bn" was a mislabeled value)* | 0.29-0.35% claimed; ≤ 0.1% even if legal | [S6], [S7a], [S3], [S35] |
| Immigration (incl. "national priority" on benefits) | +15.1 (2027), +29 full year | 2027 / 2031 | None quantified. The government calls the measures "for the most part unconstitutional"; the IdE classes them as legally fragile; 18.1 bn of "reserved benefits" in 2031. Montaigne 2024 had displayed the RN's 8 bn as of "uncertain feasibility". | 0.48% / 0.81% (2031 level / 2032 GDP) | [S6], [S7], [07/S13] |
| Agencies ("parasitic" bodies) | +3.4 (OFB, Anses, water agencies, Ademe…) in 2027; **10.1 by 2031** in the annex (IdE, category B); 85,000 posts unfilled by 2032 | 2027 / 2031 | Senate inquiry: ~**0.5** without abolishing the policies themselves. IdE: operators include the universities, so 10 bn is "hard to reach without cutting essential missions" [S7a] | 0.11% vs. 0.02% | [S5], [S7a], [07/S19] |
| Local authorities | +8.2 (plus 116,000 posts unfilled; abolition of EPCI and metropolises +0.25) | 2027 | None | 0.26% | [S5], [S7] |
| Posts not filled (85,000 agencies + 116,000 local) | n/a | 2032 | Own: 201,000 × ~63k EUR (D.1 370 bn / 5.85 m agents, file 04) = **+12.7 gross**; +6.4 if half is returned to agents. *(verified 2026-10-25: the RGPP rule, set in the President's speech of 4 April 2008, returned "half of the budget savings" from post cuts to civil servants through category-specific pay measures. In 2009 the gross saving was 860 M EUR, the planned return 430 M EUR, and the actual return about 700 M EUR, i.e. about 80% (Senate, *Rapport général* n° 111 (2010-2011), t. III, annexe 14, 18 Nov 2010 [S36]). So "half returned" is the stated rule; the 2009 outturn was closer to 80%, which would cut the net saving to about +2.5.)* francebudget.fr: ≈ +13.5 in 2032 (non-institutional). | 2032: 0.07-0.35% | own; [S14]; [S36] |
| Energy VAT 20% → 5.5% (electricity, gas, fuels) | −12.2 | 2027 | Montaigne 2024: "> 11"; francebudget.fr: 17.4 (flagged unreliable in 07). At Oct-2026 fuel prices, the fuel share of the cut is larger than at 2024 prices (our caveat). | −0.39% | [07/S13], [S14] |
| 0% VAT on "100 essential products" | **−3.5** (RN annex, per IdE) *(corrected 2026-10-25: was "not separately costed")* | 2027 | IdE: assumes full pass-through to prices, whereas the 2009 restaurant VAT cut was mostly captured by margins (Benzarti and Carloni 2019, as cited by the IdE) [S7a] | −0.11% | [S7a] |
| Abolish CFE, CVAE, C3S (local business taxes) | **−17.1** (RN annex, per IdE) *(corrected 2026-10-25: was "not separately costed")* | 2027 | francebudget.fr encoding −17 (non-institutional). IdE: offset in 2027 by 18.4 bn of new levies on large groups (share-buyback tax 11.35 in 2027 then 0.34/yr, turnover-based corporate tax, "super-dividends", etc.), so firms as a whole gain ~nothing in year one [S7a] | −0.55% | [S7a], [S14] |
| Back to 62 (60 with 40 years for early starters) | −9 (full year, the candidate's own estimate, Franceinfo); **−9.5 in 2031** in the RN annex (IdE: "largely underestimated according to many experts") | full effect | Montaigne 2022: −23.5 to −38.5 (60 with 40 years); repeal alone −16 (2032, CNAV estimate cited in Parliament, ⚠ CNAV note not public) to −17 (2030, Fipeco) | 2032: −0.45 to −1.07% | [S13]; [S7a]; [S15]; [S34]; file 03 |
| "Correction of unjust pension measures" / "repair of the pension system" | +15 to +20 (press); **+15.0 in 2031** in the annex | undated / 2031 | IdE: category B, "no concrete measure described" [S7a] | n/a | [S5], [S7a] |
| Fraud (VAT withholding, procurement) | +1.1 (2027) → +23.8 (2031), of which VAT withheld at source 18.0 and public-procurement cartels 5.8; "4 in 2027" elsewhere | 2027-2031 | Realistic marginal yield +1 to +3 (file 07); HCFP skeptical; IdE: 18.0 is 1.5 times France's entire VAT gap (12 bn in 2023, European Commission) [S7a] | 2027: 0.04-0.13% | [S7a], [S14] |
| Growth assumption | 1.8% (press); the annex claims +2.8 points of extra growth over five years from tax cuts and new spending and only −0.5 point from spending cuts (IdE) | 2027-2032 | Lescure: "well above what all serious economists project". HCFP: even the government's 1.0% for 2027 is "optimistic". IdE, using the IMF's rule of thumb (1 pt of GDP of consolidation ≈ −0.5 pt of activity after two years, *WEO* Oct 2010), puts the recessive effect at ~1.6 pts, three times the RN's [S7a] | n/a | [S6], [S3], [S7a] |

### 4.3 LR (Retailleau): plan of 2026-10-12 [S8]

| Measure | Claimed | Independent estimate(s) | % of 2032 GDP (claimed) | Source |
|---|---|---|---|---|
| **Total "over five years"** | **197** (State 96, social 91, local 10); 146 to the deficit, 51 returned (the source also prints 56) | **None.** francebudget.fr did not encode the 197 bn and finds 6.8% of GDP in 2030 without it (non-institutional, not usable as a costing). | 5.5% (if a 2032 level) | [S8], [S14b] |
| Pensions: *décote* (early-retirement penalty) 7%/yr between 63 and 65 with 43 years, full rate at 65 indexed to life expectancy, partial capitalization, Agirc-Arrco convergence, end of special regimes | +42 ("improve the accounts"); parametric part +12; "about 9 by 2032" for the age measure (candidate) | None. Franceinfo reports 40 "cumulative over five years". | 1.17% | [S8], [S13], [S14b] |
| Unemployment insurance aligned on "European standards" + cap on cumulated non-contributory aid at 70% of the SMIC | +30 | None | 0.84% | [S8] |
| Sick leave (reviews, prescriber monitoring, a non-reimbursed "public-order" waiting day in the private sector) | +4 | None found | 0.11% | [S8] |
| Non-replacement of **400,000** retiring public agents (of 5.9 m) | +25 | Own: 400,000 × 63k = **25.3 gross**; **12.6** if half returned to agents. In early 2026 the figure was 200,000-250,000 (iFRAP still lists 250,000 → ~15). | 0.70% | [S8], [S11] |
| Agencies/operators (incl. 5 from voluntary departures) | +7.5 | Senate benchmark ~0.5 | 0.21% | [S8] |
| Zero-based budgeting / outsourcing / vocational training to regions / other cuts | +11.5 / +5 / +6 / +23 | None | 1.27% together | [S8] |
| Immigration | +10 (4.5 of it conditional on a constitutional referendum) | None | 0.28% | [S8] |
| Fraud | ~~+5 tax/subsidy + 4 social~~ **+5 (tax and social fraud combined)**. *Fact-check: Public Sénat gives a single 5 bn for "fraude fiscale et sociale"; the 4 bn is the sick-leave line above and was double-counted.* | Realistic +1 to +3 | ~~0.25%~~ **0.14%** | [S8] |
| Associations "challenging the law" | +3 | None | 0.08% | [S8] |
| Local authorities (operating spending, 2,232 largest only) | +10 | None | 0.28% | [S8] |
| Tax cuts: firms 30 (incl. production taxes), households 21 (incl. social-contribution exemption of overtime) | −51 | None | −1.42% | [S8] |

### 4.4 Horizons (Philippe) [S9], [S9b], [S13]

| Measure | Claimed | Independent estimate(s) | 2027 / 2032 % GDP | Source |
|---|---|---|---|---|
| Alternative 2027 budget: +10 savings (half State, half social), −10 planned tax rises cancelled | **net 0**; shares the PLF's 5.0% target | None | 0 | [S9] |
| Undo the 2023-reform suspension | +1 (2027) | The suspension costs 1.9 in 2027 (government, Nov. 2025) → up to +1.9 | 0.03-0.06% | [S9], [07/S27] |
| Social-security funds' spending −3% a year | not costed | None | n/a | [S9] |
| Two waiting days (*jours de carence*) for public-sector sick leave | not costed | **+0.17 bn/yr** for a second waiting day across the three branches of the civil service (State 67 M, local 74 M, hospitals 33 M EUR); 289 M EUR for a second and third day; 900 M EUR for cutting sick pay to 90% (Budget Directorate estimates in the IGF-IGAS spending review on health-related absences, July 2024 [S37]). ~~⚠ From memory: the PLF 2025 proposal (3 days + 90% pay) ~1.2 bn~~ *(corrected 2026-10-25: the PLF 2025 package of 3 days + 90% pay sums to about 1.2 bn (0.29 + 0.9) on these figures, but Horizons proposes 2 days only, so the relevant figure is 0.17 bn.)* Behavioral evidence: Insee found that the 2012 waiting day in the State civil service **halved two-day absences but raised absences of one week to three months by about 25%**, leaving the overall absence rate unchanged (Insee Analyses n° 36, Nov 2017 [S38]); an Insee-DEPP study (March 2023) found −23% in teachers' ordinary sick-leave episodes and −6% in total days [S37]. | 2032: ~0.005% | [S37], [S38] |
| Replace only 2 of 3 departing civil servants (~250,000 fewer posts over 5 years, per Euronews) | not costed | Own: 250,000 × 63k = **15.8 gross** (7.9 if half returned) | 2032: 0.22-0.44% | [S9b] |
| Pensions: 45 years of contributions and age 65 within 10 years | **+30 per full year** (candidate) | None | 2032: 0.84% at full effect | [S13] |
| Unemployment benefits: 18 → 12 months for under-50s; single family allowance of 350 EUR/month from the 1st child; ~3,000 EUR tax cut for working families; climate fund 2/yr | not costed (except 2/yr) | None. The family allowance could be **large** and is not costed. | n/a | [S9b] |
| Deficit target | 2% of GDP by 2032 (iFRAP listing) | n/a | n/a | [S11] |
| "Deal fiscal" of 250 bn (production taxes −50 bn a year for 5 years) | listed by iFRAP | **Not confirmed** by any press source opened. It is implausible as an annual cut, since it would exceed the total yield of production taxes. Do not use. | n/a | [S11] |

### 4.5 Renaissance (Attal) [S11], [S13]

| Measure | Claimed | Independent estimate(s) | % GDP | Source |
|---|---|---|---|---|
| Savings over the term (not itemized) | +150 | None | 4.19% of 2032 GDP (if a level) | iFRAP [S11]; cited by Public Sénat [S8] |
| Emergency savings brake from May 2027 | +20 | None | 0.64% of 2027 GDP | [S11] |
| 100,000 fewer **State** civil-service posts via non-replacement of some retirements and voluntary departures, sparing Education, Armed Forces, Justice and Interior *(verified 2026-10-25: Public Sénat and Acteurs publics, 2026-07-03, reporting Attal's *Le Parisien* interview of 2 July 2026 [S39]; these four ministries employ more than two-thirds of State civil servants, so the cuts would fall on the remaining ~800,000 agents)* | +7/yr | Own: 100,000 × 63k = 6.3 gross (3.2 if half returned). Voluntary departures carry **one-off severance costs** that are not netted. | 0.20% (2032) | [S11]; [S39] |
| Unemployment-insurance reform | +5 | None | 0.14% | secondary [S11] |
| *Année blanche* (benefits frozen at their nominal level) on social benefits in budget 2028, small pensions protected | not costed | IPP: a full *année blanche* (pensions + benefits + tax brackets) yields 4.4-5.7 → **upper bound** | ≤ 0.17% | [07/S8] |
| Middle-class tax cut | −2 | None | −0.06% | [S11] |
| Pensions: abolish the legal age (contribution length only, with *décote* and *surcote*, i.e. reduction and bonus); 1,000 EUR capitalization endowment per newborn | not costed. The endowment, at **643,905 births in 2025** (Insee, definitive, 6 Jul 2026 [S40]), would cost ~**0.64/yr**. *(corrected 2026-10-25: was "~650,000 births, ⚠ not re-verified")* | None | 0.02% | [S13]; [S40] |
| Targets | deficit < 3% before 2032; balance in 2037; ten-year economic and fiscal programming law; constitutional budget rule | n/a | n/a | [S11] |

### 4.6 PS–Place publique (Glucksmann) [S11], [S12], [S13]

| Measure | Claimed | Independent estimate(s) | % GDP | Source |
|---|---|---|---|---|
| Cut social levies on wages (CSG, per iFRAP), "to raise net pay" | −15 | None | −0.48% (2027) | [S12], [S11] |
| Financing: top inheritance rate 45% → 50% above 1.8 M EUR (+2); *pacte Dutreil* reform (+3); tax unrealized capital gains on inherited assets (+10) | **+15** | CAE: +9 to +19 for a broad base-broadening reform; Cour: Dutreil costs 3.8, so +3 is plausible for a strong reform. **No estimate exists for taxing unrealized gains at death**; the OFCE (Allègre, Timbeau, 2026-10-19) argues for the principle without a yield. Franceinfo reportedly called the package "optimistic" (⚠ still not found on 2026-10-25; **drop from site**). | +0.48% claimed | [S11], [S16], [S17], [S21] |
| Zucman tax | supported, not costed | +2 to +20 (see 4.1) | — | [S11] |
| SMIC 1,600 EUR net | not costed | Own scaling: +8.3% vs. the SMIC in force → ~−1.8 to −2.2 | −0.06% | [S11]; own |
| State operating savings | +2.3 to +3 | None | 0.07-0.10% | [S11] |
| Triple the *chèque énergie* (energy voucher); cancel the 2024 electricity-excise rise; social leasing for caregivers (< 1/yr) | not costed (except < 1) | None | n/a | [S11] |
| EU: 500 bn common-borrowing defense fund; mobilize 210 bn of frozen Russian assets; EU tax on very large fortunes | EU level: no direct French budget effect claimed | None | n/a | [S11] |
| **Net** | roughly neutral as claimed (−15 / +15); **no global costing published** | n/a | n/a | [S11] |

### 4.7 Les Écologistes (Tondelier) [S11], [S13]

| Measure | Claimed | Independent / own | Source |
|---|---|---|---|
| Back to 62 now, 60 later (priority to early starters and arduous jobs), financed by "taking 10%" of 77 bn of contribution relief | +7.7 financing (claim); cost of 62 not stated | Repeal costs about −3.4 in the first year and −16 to −17 by 2030-2032 (see 4.1; corrected 2026-10-25: was "−3.4 to −5"). **On its own, 7.7 does not finance repeal at full effect.** | [S13]; file 03 |
| Inheritance surtaxes (10% above 4 M EUR, +10% above 13 M EUR); Dutreil exemption 75% → 50%; Zucman 2%; DST 5%; FTT 0.7%; flat tax +3 pts; 60% income-tax bracket above 250,000 EUR | not costed | Dutreil 75→50% recovers about one-third of a 3.8 bn tax expenditure, i.e. ~1.3 (own, static) | [S11], [S17] |
| SMIC 2,000 EUR gross from 2027 | not costed | +7.1% vs. ~1,867 gross → ~−1.5 to −2 (own scaling) | [S11] |
| Index point indexed to inflation; categories B and C revalued | not costed | ~2.4 bn per point of inflation (own, from the minister's figure) | [S11] |
| Climate-adaptation plan | −7/yr by 2032 | — | [S11] |
| Justice hiring over 10 years (9,000 magistrates, 10,000 clerks, 7,000 attachés) | not costed | — | [S11] |

### 4.8 PCF (Roussel), Reconquête (Zemmour), others

| Party | Measures | Fiscal weight | Source |
|---|---|---|---|
| PCF (Roussel) | Triple the ISF; 15 income-tax brackets; **phase out the CSG** | Not costed. **Scale warning:** the CSG yielded **156.6 bn in 2025** (Insee, file 05), i.e. ~5% of GDP. Phasing it out requires an equivalent replacement. | [S11]; file 05 |
| Reconquête (Zemmour) | Lower CSG for modest workers; zero employer and employee contributions at SMIC level for 2 years; apprentices exempt up to 100% of SMIC; small pensions (< 1,300 EUR) up to +600 EUR/yr through CSG/CRDS exemption; legal age 64-65; asylum capped at ~100/yr | Not costed for 2027. **2022 references only** (different program): iFRAP (liberal) found in April 2022 that the 2022 Zemmour program would "*aggraver le déficit de +5 milliards en 2027*", i.e. **worsen** the 2027 balance by 5 bn (iFRAP, 2022-04-07 [S41]; *verified 2026-10-25*). ~~a Montaigne 2022 figure from the same search summary was not verified~~ (not re-found; dropped). | [S11], [S13], [S41] |
| Lisnard (Nouvelle Énergie) | 200 savings by 2032 (80 in year one; 120 returned as net wages, 40 production taxes, 40 to debt); CIT 20%; legal age 65; abolish half of 1,200 agencies by ordinance | Party claim | [S11] |
| Dupont-Aignan | ~130 by 2032 (leave the EU +15, administrative simplification +30, anti-fraud +20, social-security control +20, end of renewables support +12, Ukraine aid +7…) | Party claim (itemized total 127) | [S11] |

---

## 5. Net balance per program (annual, in a stated year)

### 5.1 LFI: 2027

| Scenario | Net, bn EUR | % of 2027 GDP | Share of the 2027 deficit target (158.1) | Share of the 3-pt gap (~94 in 2027) |
|---|---|---|---|---|
| **Claimed** | **+24.7** | **+0.79** | 15.6% | 26% |
| Independent range, costed lines only (our aggregation) | **−53.3 to +21.0** | −1.70 to +0.67 | n/a | n/a |
| + SMIC 1,700 (−3.5 to −4) | −57.3 to +17.5 | −1.83 to +0.56 | | |
| + fuel freeze at Oct-2026 prices (−26.5 to 0) | **−83.8 to +17.5** | **−2.67 to +0.56** | | |
| *Variant: fuel freeze at the PLF's 80.3 $/b Brent (about −12 to 0; own scenario, §6.2; added 2026-10-25)* | −69.3 to +17.5 | −2.21 to +0.56 | | |
| + retirement at 60 at full effect (Montaigne 2022: −36 to −113) | not a 2027 item; adds 1.0-3.2% of GDP by end of term if done | | | |

*Method: for each line, the independent low and high from the CSV. Where no independent estimate exists, the low end halves the party claim (our convention for undocumented yields; the multinationals tax, the windfall tax, the FTT, the buyback and crypto taxes and the CVAE line are all halved) and the high end keeps it. Revenue range +34.2 to +100.1; costed spending −87.5 to −79.1. Zucman and ISF are not double-counted. **This is an illustrative aggregation, not a costing. It is static and has no macroeconomic feedback.** LFI's own argument is that the spending raises growth from 2028 [S1]; the IMF and most institutional forecasters find that multipliers on transfers are below 1, so the feedback does not finance the measures (see §9).*

**Reading.** On LFI's own figures, the 2027 deficit would fall by about 0.8 pt of GDP. That is roughly what the PLF 2027 targets (5.4% → 5.0%), but it would come from +3.4 pts of GDP in new levies and +2.6 pts of new spending, which would take the PO rate from 44.2% to about 47.6% of GDP (own arithmetic, static). The independent range straddles zero. The two largest uncosted items, the fuel freeze and retirement at 60, are each of the same order as the whole claimed net improvement.

### 5.2 RN: 2027 and 2032

| Item | 2027 | 2032 (level) |
|---|---|---|
| Claimed net balance improvement (RN press kit) | **+71.6 (2.28% of GDP)** | +141.7 in 2031; **+140** "by 2032" (3.9% of 2032 GDP) incl. −30 net tax cuts |
| IdE line-by-line recalculation of the same annex | +69.3 (2.21%) | +140.3 in 2031 |
| Gross revenue and savings / tax cuts / new spending (RN) | 140.8 / −53.2 / −16.1 | 244.4 / −49.1 / −53.7 (2031) |
| **Independent (IdE, business-funded)** | **+2.9 credible** (0.09% of GDP); deficit **5.9%** of GDP (vs. 5.0% PLF target and **3.7% RN**); the IdE itself puts the 2027 balance about **25 bn worse than the government's PLF 2027**, which the RN rejects (24.4 bn of PLF measures) [S7a]. *(corrected 2026-10-25 from the primary note: the earlier "~−28 bn vs. the PLF" conversion was struck as an over-reading; the note confirms a deterioration of the same order, about −25 bn. The 5.9% is the RN trajectory corrected by the IdE, not the IGF unchanged-policy figure, even though both equal 5.9%.)* | **+7.5 credible net in 2031 (−25 to +50)**, i.e. **0.2% of GDP** (−0.7 to +1.4); deficit 6.5% in 2031 (RN: 2.3%) |
| Share of the 3-pt gap (~107 in 2032) | n/a | claimed 131%; IdE central **7%** |
| Debt | **119.3% (2027) → 112.1% (2032)** claimed (113.3% in 2031); 136.9% in 2032 at unchanged policy per the RN *(corrected 2026-10-25: was "121% (2027) → 112% (2032)"; 121.7% is the PLF 2027 figure for 2027)* | IdE: ~130% in 2031 |

### 5.3 LR: two readings of "197 bn over five years"

| Reading | Net deficit effect | % of GDP | Consistent with the candidate's own targets? |
|---|---|---|---|
| A. **2032 level** (annual by end of term) | +146 net (197 − 51) | **4.1% of 2032 GDP** | **Yes**: moving from a ~5-6% trend deficit to 2.2% in 2032 needs roughly this (our inference) |
| B. **Cumulative** over 2027-2031 | ~+29 a year on average (146 / 5) | ~0.9% of GDP a year on average | **No**: it cannot deliver 2.2% at end of term without large unstated measures. It is, however, consistent with Franceinfo's "40 cumulative" for pensions. |

The 400,000-post line (25 bn) only works under reading A. **The platform should ask the campaign which reading is meant** and should not quote "197 bn" without the horizon.

### 5.4 Summary of all programs

| Program | 2027 net (bn; % GDP) | 2032 net (bn; % GDP) | Deficit target | Independent assessment | vs. 2026 deficit (164.9; 5.4%) |
|---|---|---|---|---|---|
| LFI | claimed **+24.7 (0.79%)**; independent range −83.8 to +17.5 (−2.7% to +0.6%) | not published (full costing "early 2027") | "stabilize debt in one term" | none institutional | claimed: 15% of it |
| RN | claimed net +71.6 (2.3%); IdE credible +2.9 (0.1%), deficit 5.9% *(corrected 2026-10-25: was "gross savings +69.3 (2.2%) claimed")* | claimed +140 (3.9%); IdE +7.5 (0.2%) | < 3% in 2030; ≤ 2.5% in 2032 (francebudget reading of the RN target) | IdE (business-funded) | claimed 2032: 85% of the 2026 deficit in bn terms |
| LR | not split by year | +146 (4.1%) under reading A | < 3% in 2031; 2.2% end of term | none | reading A: 89% |
| Renaissance (Attal) | +20 (0.64%) | +150 (4.2%) if a level; not itemized | < 3% before 2032; balance 2037 | none | 91% (if a level) |
| Horizons (Philippe) | **0 vs. PLF** (+1 from undoing the suspension) | not quantified; +30 pensions at full effect; 2% deficit by 2032 | 5.0% in 2027; 2% in 2032 | none | n/a |
| PS–PP (Glucksmann) | ~0 claimed (−15 / +15) | not published | not stated in the sources opened | none | n/a |
| Écologistes / PCF / Reconquête | not costed | not costed | not stated | none | n/a |

**What the comparison shows.** Every program on the right and in the center claims an end-of-term improvement of **3.9-4.2% of GDP**, more than the 3-pt debt-stabilizing gap and the IGF mission's ~125 bn requirement. **None** of these claims has been independently costed. The only independent look (IdE on the RN) finds about **5%** of the claim credible. The left programs (LFI, Glucksmann) claim much smaller net improvements (0 to 0.8% of GDP), built on large gross tax increases (LFI +3.4% of GDP).

---

## 6. Price freezes: budget cost and non-budget economic effects

### 6.1 Rent freezes and rent control (*encadrement des loyers*)

**Proposals.** LFI wants rents blocked and rent control generalized (program teaser; the 2027 budget document does not cost it). Les Écologistes propose rent controls. LR proposes repealing them [S11], [S1b].

**Budget cost.** A rent freeze has **no direct spending cost**, but it is **not budget-neutral**. IPP Note 125 estimates that existing rent control transfers ~**0.6 bn a year** to tenants. **About one-third** of that is borne by the State and social security through lower income tax and social levies on rental income (in Paris: −282 m EUR for landlords, −118 m EUR for public revenue) [S18]. A general national freeze would scale this up. No estimate was found.

**Evidence on economic effects**

| Study | Setting | Finding | Source |
|---|---|---|---|
| **IPP Note n° 125**, Chapelle and Fack (May 2026) | Rent-control experiment under the ELAN law, rolled out from 2019 (Paris, Plaine Commune, Est Ensemble, Lille, Lyon, Montpellier, Bordeaux…); difference-in-differences on 30 million ads (Yanport, 2015-2024) | Advertised rents **2-4% lower** than in comparable cities, ~~reaching **~5%** after 5 semesters~~ **about 4% after five semesters and reaching 5% at the end of the period** *(fact-check: wording corrected against the note's summary and Figure 1 caption)*. Transfer ~**0.6 bn/yr**, two-thirds from mostly well-off landlords, one-third from public finances. **Poorly targeted**: in Paris the gains go relatively more to fairly affluent tenants; top-decile tenants gain 70 m EUR vs. 22 m EUR for the bottom decile. **Compliance is weak**: 35.6% of Paris leases signed 2020-2024 are above the upper cap (32.8-43.5% elsewhere), though some of this may be legitimate *compléments de loyer* (rent supplements). Rental **ads fell** in controlled provincial city centers (about 1 fewer ad per 100 dwellings); Paris is atypical (post-Covid rise in ads). The supply effect is "to be confirmed". Conclusion: a prolonged cap "risks, in the long run, disrupting the rental market". | [S18] |
| Breuillé et al. (2025), cited by IPP | Paris since 2019 | −5.2% in Paris; no significant negative effect on the volume of ads | cited in [S18] (not opened) |
| Malard and Poulhès (2020), cited by IPP | Paris 2015-2017 (first episode) | Limited effectiveness | cited in [S18] (not opened) |
| Diamond, McQuade and Qian, *AER* 109(9), 2019 | San Francisco 1994 expansion | Landlords subject to control **cut their rental supply by 15%** (conversions, redevelopment), which "likely drove up market rents in the long run" | [S22] |
| Autor, Palmer and Pathak, *JPE* 122(3), 2014 | End of rent control in Cambridge, MA (1995) | Decontrol added ~**1.8 bn USD** to housing values in 1994-2004, about a quarter of total appreciation. More than half came from spillovers to never-controlled properties (controlled buildings had depressed neighborhood quality). | [S23] |
| Kholodilin, *Journal of Housing Economics* 63, 2024 (literature review) | ~200 studies worldwide | Rent controls are "quite effective in terms of slowing the growth of rents" for covered units, but have a wide range of adverse side effects: lower supply and quality, reduced mobility, spillovers to uncovered segments. | [S24] |
| CLCV (consumer association, pro-control), ~1,000 Paris listings, reported by Franceinfo/Radio France (2018-07-18) | Paris, 2017 vs. mid-2018 (after the Nov 2017 court annulment) | ~~Compliant new leases fell from ~40% to 13%~~ *(corrected 2026-10-25 after reading the article in a browser: in 2017 "four rents in ten" **exceeded** the cap; after the annulment the share of compliant listings **fell by 13 points in six months** (to just under half). Agency listings: 77% compliant in 2017, about 20 points fewer in 2018; direct and online listings: under 40% compliant.)* Advocacy sample of listings, not leases; **keep with caveat** or replace by IPP's 35.6% non-compliance (2020-2024, DGFiP data) [S18] | [S25] |

**Steelman (pro-control).** The French "second-generation" controls cap only the **level at re-letting** around a local reference. They are not a nominal freeze, and the IPP and Breuillé et al. find modest, real rent moderation with no clear supply collapse in Paris over five years. Tenants' welfare gains are real, and the fiscal cost is small (~0.2 bn) [S18]. **Counter-argument.** The literature on hard caps and freezes (Kholodilin; Diamond et al.) consistently finds supply and quality losses over longer horizons. A *general freeze* is a much stronger instrument than the existing *encadrement*.

### 6.2 Fuel-price freeze (LFI: 1.70 EUR/l "by decree")

| Item | Value | Source |
|---|---|---|
| Pump price, week of 2026-10-16 | diesel **2.346** EUR/l (pre-tax 1.347); SP95-E10 **2.149** (pre-tax 1.121) | DGEC weekly bulletin [S20]; series saved in `research/data/11_fuel_prices_weekly_2020_2026.csv` |
| Brent | 127.7 $/b spot (114.1 EUR/b) | [S20] |
| Road-fuel consumption, rolling 12 months to Sept. 2026 | **45.8 bn liters** (diesel 30.2, gasoline 15.6) | [S20] |
| Implied per-liter excise (derived: TTC/1.2 − pre-tax) | diesel ~0.61 EUR/l; E10 ~0.67 EUR/l | own derivation |
| **Price-ceiling feasibility** | At 1.70 EUR/l with taxes unchanged, the maximum pre-tax diesel price is **0.81 EUR/l**, against a market price of **1.35**. Retailers would sell below cost, so a decree alone means shortages unless the State pays the difference. | own |
| **Budget cost if the State finances the freeze (tax cut or rebate)** | (2.346 − 1.70) × 30.2 + (2.149 − 1.70) × 15.6 ≈ **26.5 bn/yr (0.85% of 2027 GDP)** at Oct-2026 prices; **~0** at 2025 average prices (diesel 1.62, E10 1.69). *Fact-check (recomputed: 26.52): arithmetic confirmed. Caveats: (i) it is a **spot-price scenario**. Brent futures were already 105.8 $/b (ICE, same bulletin) and the PLF assumes 80.3 $/b for 2027 [S3], so the expected 2027 cost is lower. ~~(⚠ a few bn, own approximation)~~ *Recomputed 2026-10-25 (own scenario): a Brent fall from 127.7 to 80.3 $/b (1.120 $/EUR, 159 l/barrel, +20% VAT) lowers pump prices by about 0.32 EUR/l, to ~2.03 (diesel) and ~1.83 (E10); the freeze then costs (2.03 − 1.70) × 30.2 + (1.83 − 1.70) × 15.6 ≈ **11.9 bn/yr**. At the 105.8 $/b futures price: ≈ **19.7 bn/yr**. Both assume full pass-through of crude prices and refining and retail margins frozen at their October 2026 level; if margins also return to 2025 levels, the cost tends to 0. Not an institutional estimate.* (ii) Applying the E10 price to all gasoline (incl. SP98) slightly understates it. (iii) Lower prices would raise volumes and fuel tourism, which raises the cost. Sensitivity: 0.10 EUR/l ≈ 4.6 bn/yr.* | own; [S3] |
| Comparison: 2022 fuel rebate (*remise carburant*) | ~7.5 bn in one year | [07/S39] |
| EU comparison (9 Oct 2026) | France diesel 2.33 vs. EU-27 weighted average 2.14 and euro area 2.19; SP95 2.21 vs. 2.01 / 2.08 | [S20] (EC Oil Bulletin via DGEC) |

**Takeaway.** The cost of a fuel freeze depends entirely on the oil price and is open-ended. At Oct-2026 prices it is larger than LFI's whole claimed 2027 net improvement. The government ruled out a general fuel-tax cut in May 2026 on cost grounds and preferred targeted payments [07/S40].

### 6.3 Energy price shields 2021-2024: the Cour des comptes verdict (2024-03-15) [S19]

| Finding | Value / quote |
|---|---|
| Gross cost of the price shields (*boucliers tarifaires*) | ~**72 bn** |
| Net State financing need, 2021-2024 | **36 bn** (after lower renewable-support charges and 4.5 bn of windfall contributions) |
| Net cost to public finances 2022-2023 | ~9 bn |
| Gas and fuel support 2021-2022 | > 17 bn |
| Wholesale market margins captured, 2022-2023 | > 30 bn (net) |
| Targeting | ~25 schemes, "for the most part, not targeted" by income |
| Pass-through | Some support "may not have reduced prices" and may have overcompensated price rises |
| Macro effect | The shields had a positive effect on prices and GDP; French household prices stayed below neighbors'. Firms faced higher electricity prices than major neighbors in early 2023. |
| Climate | Gas and fuel support ran counter to the energy transition |
| Inflation effect | **Not quantified on the Cour page.** *(verified 2026-10-25)* Insee: between Q2 2021 and Q2 2022, energy prices contributed 3.1 points of the 5.3% inflation; the shield measures (*bouclier tarifaire* and pump rebate) halved these effects, and **without them inflation over the year to Q2 2022 would have been 3.1 points higher** (Insee Analyses n° 75, Sept 2022 [S42]). *(corrected 2026-10-25: was "roughly 3 points less inflation in 2022, ⚠ from memory"; the period is Q2 2021 to Q2 2022, not calendar 2022.)* |

### 6.4 Essential-goods price freezes (LFI "blocage des prix"; RN 0% VAT on 100 products)

No costing or evaluation was found for either proposal. A **price freeze** has no direct budget cost but transfers margins from producers and retailers to consumers. Under rising input costs it creates shortage and quality risks: the same mechanism as §6.2, with no State compensation. A **VAT cut** has a direct budget cost. Pass-through to prices is incomplete: in the energy case the Cour warned that some support "may not have reduced prices". We found no French institutional evaluation of VAT pass-through on food this session.

---

## 7. Independent costings and simulators of the 2027 programs (status on 2026-10-25)

| Institution | Status | Evidence |
|---|---|---|
| **Institut Montaigne** | **No "Chiffrage 2027" exists.** Its 2027 hub (`/presidentielle-2027/`) redirects to *Les Repères de Montaigne*, 25 thematic notes with no candidate costing and no announced costing date. Its other 2027 items are an Ipsos survey (Sept. 2026) and an op-ed (2026-10-21). | [S26] |
| **IPP** | **No simulator or program evaluation.** The latest items are on education and rent control (Note 125). | [S27] |
| **OFCE** | **No program evaluation or simulator.** Related: blog "Budget 2027: an unequally shared effort" (P. Madec, 2026-10-16); "To tax the richest better, income must be better defined" (Allègre, Timbeau, 2026-10-19); WP 2026-10 "Why and How Should the Richest Be Taxed?" | [S21] |
| **Terra Nova** (center-left) | No costing found on its homepage | [S30] |
| **Rexecode** (employer-funded) | No program costing. Related: "Bilan des prélèvements obligatoires 2026: le choc fiscal s'installe" (2026-09-29). | [S31] |
| **Fipeco** | No program note. Latest: "Les options envisagées face à la dérive de la dette publique" (2026-10-07). | [S32] |
| **Cour des comptes / HCFP / Senate / AN** | No program costing (by mandate they do not cost party programs) | n/a |
| **iFRAP** (liberal) | A **comparator** listing 14 candidates' proposals, with **no costing or assessment** in the text extracted | [S11] |
| **Institut de l'Entreprise** (business-funded) | Note de contexte on the RN counter-budget (2026-10-06, 9 pp.), the only independent look at a 2027 package. **Primary opened 2026-10-25** (found through the institute's media library; it is not listed on its publications page). Its own disclaimer: it does not re-estimate the RN's per-measure amounts, and its A-D classification "is an analytical judgment". | [S7a] |
| **francebudget.fr** | Citizen open-source macro simulator (engine v0.6.8, 2026-10-07; GitHub `cturkieh/france-budget-simulateur`; no named authors). It runs LFI, RN and LR scenarios but explicitly does **not** encode the bulk of the savings packages. **Not an institutional source.** | [S14], [S14b] |

**Conclusion: no institutional or academic costing of any 2027 program exists as of 2026-10-25.** Every program figure in this file is either a party claim or our own static arithmetic.

---

## 8. International comparison (relevant to this file)

The full indicator comparisons (deficit, debt, spending, PO) are in files 07 (§6) and 09. Three points are specific to the measures here:

| Indicator | France | Comparison | Source |
|---|---|---|---|
| Deficit 2025 | 5.1% of GDP, 4th largest in the EU-27 | See file 07 §6.1 | Eurostat gov_10dd_edpt1 (2026-10-21) |
| Inheritance and gift taxes | 0.70% of GDP (2024), **1st** in the OECD | File 05 | OECD Revenue Statistics |
| Pump prices (9 Oct 2026) | diesel 2.33, SP95 2.21 EUR/l | EU-27 2.14 / 2.01; euro area 2.19 / 2.08 | [S20] |
| Rent control | Second-generation, local caps at re-letting (since 2019) | Hard caps and freezes abroad (Berlin *Mietendeckel* 2020-21, struck down; San Francisco; Sweden) show supply losses (Kholodilin review) | [S18], [S24] |

---

## 9. Where economists disagree, and the steelman

1. **Do tax-financed spending packages pay for themselves through growth?** LFI argues that cuts are self-defeating ("fiscal consolidation does not on average reduce debt ratios", attributed to the IMF) and that its spending will lift activity from 2028 [S1]. **Strongest version:** at the zero lower bound or in recessions, multipliers can exceed 1, and France's 2026 consolidation coincided with weak growth (0.4-0.5%). **Counter:** in 2026-27 the ECB is not at the zero lower bound, interest rates are high (10-year OAT **4.44%**, monthly average for Sept. 2026, 97 bp over the Bund, Eurostat `irt_lt_mcby_m`, canonical in `00-reference-figures.md` row 43; *corrected 2026-10-25: was "4.7% in Sept. 2026, file 06"*; the RN press kit quotes 4.9% on 2 Oct 2026, a daily quote [S7a]), and the HCFP and IGF use multipliers well below 1. A "zero multiplier" is described as "very favorable" by the IGF mission (file 06).
2. **Can the right's and center's savings be achieved?** **Steelman:** the Cour des comptes and the IGF agree that ~125 bn of adjustment by 2032 is needed. The LR/RN/Renaissance packages are of that size and target the right items: pensions, social transfers and the wage bill. **Counter:** only the IdE has looked at one package (RN) and found ~5% credible (7.5 of 141.7 bn in 2031) [S7a]. The savings that rely on EU unanimity, constitutional change (immigration, "national priority") or unspecified "efficiency" are legally or operationally uncertain. Agency savings are 0.5 bn according to the Senate inquiry, against 3.4-7.5 claimed.
3. **Wealth and inheritance taxes.** See file 07 §5. The new 2027 element is the **inheritance base**. The CAE (9-19 bn steady state) and the OFCE (taxing gains at transfer) give academic support to the yields Glucksmann claims (15). LFI's 20 bn **first-year** claim is above the CAE's steady-state range.
4. **Rent control.** See §6.1. Short-run moderation without a clear supply collapse in Paris (IPP, Breuillé et al.) vs. long-run supply losses in the international literature (Kholodilin, Diamond et al.).
5. **Civil-service attrition.** The savings per post depend on whether savings are partly returned to remaining agents, as in 2007-2012. Non-replacement of retirees does not cut pension spending. File 04 shows France's headcount (20.7% of employment) is above the OECD average but far below the Nordics.

---

## 10. Divergences between sources

| Item | Divergence | Explanation |
|---|---|---|
| LFI wealth tax | "ISF climatique" (press, Public Sénat, Moneyvox) vs. "impôt sur la fortune renforcé" (LFI PDF) | The PDF wording is used here. |
| LFI spending list | LCP lists index point 17 and APL 8; Moneyvox lists back-to-62 at 9 | Both are in the PDF; neither article lists everything. |
| LFI SMIC | 1,700 net (LFI PDF and program teaser; iFRAP) vs. 1,600 net (francebudget, from the 2025 program edition) | The 2026 document says 1,700. |
| RN EU contribution | 9 (Bardella) vs. 11.1 (2027) and 19.5 (2031) (IdE tabulation) vs. 13.1 (IdE, other passage) | *Resolved 2026-10-25 from the primary note [S7a]:* 13.1 is the unilateral contribution cut alone (2031 amount in the IdE's thirteen-line table); 11.1 (2027) / 19.5 (2031) are the whole "EU" contributor block, which also includes customs duties and tobacco taxation. Bardella's 9 is an annual figure quoted in the press. France's actual net contribution in 2025 is EUR 9.5 bn (accounting method) or 6.4 bn (Commission operating balance), per the PLF 2027 EU annex (file 16 §3.1) *(corrected 2026-10-25, index pass: was "about 7-9 bn (2025) [S35]", own computation)* |
| RN 140 bn | "by 2032" (Public Sénat, PGE) vs. 141.7 in 2031 (RN file per IdE) vs. 140.3 (IdE recalculation) | Rounding / year; the IdE notes that only the line for the total of positive contributions diverges from the sum of its components |
| RN net vs. gross | 69.3 / 140.3 called "gross savings" in this file's first pass and in [S7] | *Corrected 2026-10-25:* they are **net** balance improvements; gross revenue and savings are 140.8 (2027) and 244.4 (2031) [S7a] |
| RN deficit target | < 3% in 2030 (Euronews, PGE) | Consistent |
| LR tax cuts | 56 vs. 51 in the same article | Unreconciled in the source |
| LR horizon | "over five years" vs. Franceinfo "40 cumulative" for pensions vs. 25 bn/yr for non-replacement | See §5.3 |
| LR non-replacement | 400,000 / 25 bn (Public Sénat, Oct. 2026) vs. 250,000 / ~15 bn (iFRAP) vs. 300,000 (francebudget) | Campaign revisions (200-250k in early 2026) |
| Philippe pensions | +30/yr (Franceinfo, candidate) vs. nothing in Horizons' 2027 budget | The program differs from the 2027 budget alternative |
| Glucksmann levy cut | "certain social levies" (Parlons-politique) vs. "CSG" (iFRAP) | iFRAP is more specific; primary not found |
| Repeal of 2023 reform, first-year cost | LFI 9 vs. CNAV 3.4 (for a 2025 repeal; 15.7 in 2032; the Cnav answer is reproduced in AN report no. 613, verified by file 03 on 2026-10-25, index pass; was "⚠ CNAV note not public") | Different baselines (with or without the suspension already in force), and LFI's figure possibly includes the full-year effect on several generations |

---

## 11. Gaps and open questions

- **The web-search quota for this session was exhausted midway through the research.** Pages were then reached only through known URLs. The following could therefore not be searched: the RN 2027 counter-budget PDF (*2026-10-25 third pass: still not posted on rassemblementnational.fr*); ~~the Institut de l'Entreprise note itself~~ (*found and read 2026-10-25 [S7a]*); Attal's, Glucksmann's, Tondelier's and Roussel's primary program documents; Retailleau's PDF booklet; Franceinfo's assessment of Glucksmann's inheritance plan; Terra Nova and OFCE items beyond their homepages; the Senate inquiry report on agencies (only the press figure ~0.5 bn); the CPO (*Conseil des prélèvements obligatoires*) study of Sept. 2026 that LFI cites on the top 1%.
- **2032 GDP** is our assumption (+2.7% nominal a year).
- ~~**Unverified from memory (⚠):** the PLF 2025 waiting-day costing (~1.2 bn); Insee's evaluation of the 2012 waiting day; Insee's ~3-pt effect of the shield on 2022 inflation; the RGPP "50% returned" rule; ~650,000 births a year; France's net EU contribution.~~ *All six sourced on 2026-10-25 (third pass): IGF-IGAS 2024 [S37], Insee Analyses 36 [S38], Insee Analyses 75 [S42], Senate 2010 [S36], Insee 2026 [S40], European Commission data [S35]. See the verification log.*
- **CNAV 3.4 → 16 bn** for repeal remains secondary (file 03); now traced to Assemblée nationale amendments of Nov 2024 [S34], but the CNAV note itself is not public.
- The **LFI "+10%"** indexation wording (8 bn) needs clarification from LFI.
- **Le Pen's eligibility** depends on the cassation ruling (by early April 2027 at the latest) and on the Conseil constitutionnel.

---

## 12. Sources

All accessed 2026-10-25. Downloads (untrusted, not executed) are in `research/data/raw/11_lfi/`, `11_rn/`, `11_ipp/` and `11_fuel/`. "07/Sx" refers to the sources of file 07.

| ID | Institution / author | Title | Date | URL |
|---|---|---|---|---|
| S1 | La France insoumise (party) | *Comment nous allons remettre de l'ordre dans les comptes publics* (PDF, 22 pp.) | 2026-10-14 | https://melenchon2027.fr/wp-content/uploads/2026/10/Comment-nous-allons-remettre-de-l-ordre-dans-les-comptes-publics.pdf (local: `data/raw/11_lfi/`) |
| S1b | LFI | Program pages (*L'Avenir en commun*) | 2026 | https://melenchon2027.fr/programme/decouvrir/ ; https://lafranceinsoumise.fr/ |
| S2 | Public Sénat (press) | Élection présidentielle 2027 : qui sont les candidats déclarés ou presque ? | 2026-10-14 | https://www.publicsenat.fr/actualites/politique/election-presidentielle-2027-qui-sont-les-candidats-declares-ou-presque |
| S3 | HCFP | Avis n° HCFP-2026-5 (PLF/PLFSS 2027) | 2026-09-25 | https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf |
| S3b | Franceinfo (press) | Portraits : qui sont les candidats déclarés… (34 at 22/10/2026) | 2026-10-22 | https://www.franceinfo.fr/elections/presidentielle/portraits-qui-sont-les-candidats-declares-a-l-election-presidentielle-de-2027_8208032.html |
| S4 | Moneyvox; LCP (press) | LFI promet 106 milliards…; Contre-budget : LFI propose 106,4 milliards… | 2026-10-14 | https://www.moneyvox.fr/votre-argent/actualites/110808/presidentielle-lfi-promet-106-milliards-de-recettes-supplementaires-pour-2027-et-se-dit-raisonnable ; https://lcp.fr/actualites/contre-budget-lfi-propose-1064-milliards-d-euros-de-recettes-supplementaires-et-817 |
| S5 | Public Sénat (press) | 140 milliards d'euros d'économies d'ici 2032 : « l'effort radical » proposé par Marine Le Pen | 2026-10-06 | https://www.publicsenat.fr/actualites/politique/140-milliards-deuros-deconomies-dici-2032-leffort-radical-propose-par-marine-le-pen-pour-redresser-les-f |
| S6 | Euronews (press) | Le gouvernement tire à boulets rouges sur le contre-budget de Marine Le Pen | 2026-10-07 | https://fr.euronews.com/2026/10/07/france-le-gouvernement-tire-a-boulets-rouges-sur-le-contre-budget-de-marine-le-pen |
| S4b | Public Sénat / AFP (press) | Présidentielle 2027 : Jean-Luc Mélenchon table sur 106 milliards de recettes supplémentaires et 82 milliards de dépenses nouvelles pour 2027 | 2026-10-14 | https://www.publicsenat.fr/actualites/politique/presidentielle-2027-jean-luc-melenchon-table-sur-106-milliards-de-recettes-supplementaires-et-82-milliards-de-depenses-nouvelles-pour-2027 |
| S7 | Planète Grandes Écoles (press, secondary), reporting the Institut de l'Entreprise note (business-funded) | Budget de Marine Le Pen pour 2027 : les mesures… passées au crible | 2026-10-08 (note 2026-10-06) | https://www.planetegrandesecoles.com/budget-marine-le-pen-2027-mesures-contre-budget-rn |
| S7a | Institut de l'Entreprise (think tank of company executives, business-funded) | *Contre-budget du RN : 140 milliards affichés, moins de 10 milliards crédibles*, note de contexte (9 pp.) | 2026-10-06 | https://www.institut-entreprise.fr/wp-content/uploads/2026/10/Analyse-primaire-contre-budget-RN-Note-de-contexte-IDEP.pdf (local: `data/raw/11_verify2/ide_rn_note.pdf`) |
| S8 | Public Sénat (press) | Bruno Retailleau s'engage sur un plan d'économies de près de 200 milliards | 2026-10-12 | https://www.publicsenat.fr/actualites/economie/presidentielle-2027-bruno-retailleau-sengage-sur-un-plan-deconomies-de-pres-de-200-milliards-deuros-sil-est-elu |
| S8b | LR campaign | avecretailleau.fr (home, FAQ) | 2026 | https://avecretailleau.fr/projet/faq |
| S9 | Moneyvox / AFP (press) | Budget 2027 : Horizons propose un budget alternatif avec 10 milliards d'économies | 2026-10-13 | https://www.moneyvox.fr/actu/110762/budget-2027-horizons-propose-un-budget-alternatif-avec-10-milliards-economies-supplementaires |
| S9b | Euronews (press) | Édouard Philippe mise sur le travail et la réduction des dépenses publiques | 2026-10-09 | https://fr.euronews.com/2026/10/09/presidentielle-2027-edouard-philippe-mise-sur-le-travail-et-la-reduction-des-depenses-publ |
| S10 | Public Sénat (press) | Condamnation de Marine Le Pen : malgré son pourvoi en cassation, est-elle toujours inéligible ? | 2026-07-08 | https://www.publicsenat.fr/actualites/politique/condamnation-de-marine-le-pen-malgre-son-pourvoi-en-cassation-est-elle-toujours-ineligible-comme-laffirment-plusieurs-juristes |
| S11 | Fondation iFRAP (think tank, liberal; favors spending cuts) | Comparateur Présidentielles 2027 | accessed 2026-10-25 (images dated 2026-10) | https://www.ifrap.org/comparateurs/presidentielles-2027 |
| S12 | Parlons-politique (press) | Glucksmann mise sur le salaire net… | 2026-08-24 | https://www.parlons-politique.fr/elections/presidentielle-2027-glucksmann-mise-sur-le-salaire-net-pour-rassembler-une-gauche-sans-accord-avec-la-france-insoumise_25614/ |
| S13 | Franceinfo (press) | Changement de système, passage à 60 ou à 65 ans, capitalisation… retraites | 2026-09-30 | https://www.franceinfo.fr/economie/retraite/reforme-des-retraites/changement-de-systeme-passage-a-60-ou-a-65-ans-capitalisation-que-proposent-les-principaux-candidats-a-l-election-presidentielle-pour-les-retraites_8215784.html |
| S14 | francebudget.fr (**non-institutional citizen simulator**) | Scénario RN 2027; Scénario LFI 2027 | engine v0.6.8, 2026-10-07 | https://francebudget.fr/scenarios/rn-2027 ; https://francebudget.fr/scenarios/lfi-2027 |
| S14b | francebudget.fr | Scénario LR 2027 | page dated 2026-06-01, content to 2026-10-21 | https://francebudget.fr/scenarios/lr-2027 |
| S15 | Institut Montaigne (business-funded, liberal) | Présidentielle 2022: LFI "retraite à 60 ans" (85.8 bn); RN "retraite à 60 ans" (26.5 bn, 23.5-38.5) | 2022 | https://www.institutmontaigne.org/presidentielle-2022/jean-luc-melenchon/retablir-la-retraite-a-60-ans-apres-40-ans-annees-de-cotisation/ ; https://www.institutmontaigne.org/presidentielle-2022/legislatives-2022/rassemblement-national/restaurer-la-retraite-a-60-ans-a-taux-plein-avec-40-annuites-et-revaloriser-le-minimum-vieillesse-2 |
| S16 | Conseil d'analyse économique | Note n° 69, *Repenser l'héritage* (Dherbécourt, Fack, Landais, Stantcheva) | Dec. 2021 | https://www.cae-eco.fr/staticfiles/pdf/cae-note069.pdf |
| S17 | Cour des comptes | Analyse de l'exécution budgétaire 2025 – Dépenses fiscales (NEB) | April 2026 | https://www.ccomptes.fr/sites/default/files/2026-04/NEB-2026-Depenses-fiscales.pdf |
| S18 | Institut des politiques publiques | Note n° 125, *L'encadrement des loyers : quels effets redistributifs ?* (G. Chapelle, G. Fack) | May 2026 | https://www.ipp.eu/wp-content/uploads/2026/06/Note_IPP_Encadrement_des_loyers.pdf (local: `data/raw/11_ipp/note125.pdf`) |
| S19 | Cour des comptes | Les mesures exceptionnelles de lutte contre la hausse des prix de l'énergie | 2024-03-15 | https://www.ccomptes.fr/fr/publications/les-mesures-exceptionnelles-de-lutte-contre-la-hausse-des-prix-de-lenergie |
| S20 | Ministère de la Transition écologique (DGEC) | Weekly oil bulletin NPG 2026-10-16; database *Prix HTT et TTC depuis janvier 2020* | 2026-10-16 | https://www.ecologie.gouv.fr/sites/default/files/documents/NPG-2026.10.16.pdf ; https://www.ecologie.gouv.fr/sites/default/files/documents/Prix%20HTT%20et%20TTC%20depuis%20janvier%202020_0.xlsx (CSV: `data/11_fuel_prices_weekly_2020_2026.csv`) |
| S21 | OFCE (academic, Keynesian-leaning) | Allègre and Timbeau, "Pour mieux taxer les plus riches…" (blog); homepage listing | 2026-10-19 | https://www.ofce.fr/blog2024/fr/2026/20261019_GAXT/index.html ; https://www.ofce.fr/ |
| S22 | Diamond, McQuade and Qian | The Effects of Rent Control Expansion on Tenants, Landlords, and Inequality: Evidence from San Francisco, *AER* 109(9): 3365-94 | 2019 | https://www.aeaweb.org/articles?id=10.1257/aer.20181289 |
| S23 | Autor, Palmer and Pathak | Housing Market Spillovers: Evidence from the End of Rent Control in Cambridge, MA, *JPE* 122(3) (NBER WP 18125) | 2014 | https://www.nber.org/papers/w18125 |
| S24 | Kholodilin | Rent control effects through the lens of empirical research: An almost complete review of the literature, *J. Housing Econ.* 63 | 2024 | https://ideas.repec.org/a/eee/jhouse/v63y2024ics1051137724000020.html |
| S25 | Francetvinfo (press, secondary) | Paris : les prix des locations s'envolent depuis la fin de l'encadrement des loyers | 2018-07-18 | https://www.francetvinfo.fr/economie/immobilier/encadrement-des-loyers/paris-les-prix-des-locations-s-envolent-depuis-la-fin-de-l-encadrement-des-loyers_2854739.html |
| S26 | Institut Montaigne | Présidentielle 2027 hub → *Les Repères de Montaigne* | accessed 2026-10-25 | https://institutmontaigne.org/presidentielle-2027/les-reperes-de-montaigne/ |
| S27 | IPP | Homepage and search (no 2027 program evaluation) | accessed 2026-10-25 | https://www.ipp.eu/ |
| S28 | Cour des comptes | La situation et les perspectives des finances publiques (RSPFP) | 2026-06-25 | https://www.ccomptes.fr/sites/default/files/2026-07/20260625_RSPFP-2026.pdf |
| S29 | IGF mission (Jaravel, Ragot, Tavernier, Valla) | Transparence des finances publiques | July 2026 | https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/Transparence-finances-publiques.pdf |
| S30 | Terra Nova (center-left) | Homepage | accessed 2026-10-25 | https://tnova.fr/ |
| S31 | Rexecode (employer-funded) | Homepage; Bilan des prélèvements obligatoires 2026 | 2026-09-29 | https://www.rexecode.fr/ |
| S32 | Fipeco (F. Ecalle) | Homepage | accessed 2026-10-25 | https://www.fipeco.fr/ |
| S33 | Cour des comptes | *La taxe sur les transactions financières : un équilibre délicat entre rendement et régulation* (citizen-initiative thematic report; press release, synthesis) | 2026-09-10 | https://www.ccomptes.fr/fr/publications/la-taxe-sur-les-transactions-financieres ; https://www.ccomptes.fr/sites/default/files/2026-09/20260910-communique-Taxe-sur-les-transactions-financieres.pdf |
| S34 | Assemblée nationale | Amendment n° 728 (MoDem group) to PPL n° 613 *Abrogation de la retraite à 64 ans*, citing the CNAV estimate (3.4 bn in 2025, 16 bn in 2032) | 2024-11-25 | https://www.assemblee-nationale.fr/dyn/17/amendements/0613/AN/728.pdf |
| S35 | European Commission (DG BUDG) | *EU spending and revenue 2000-2025* (xlsx; France sheet 2024-2025: expenditure, NGEU, own resources, balances) | accessed 2026-10-25 | https://commission.europa.eu/strategy-and-policy/eu-budget/long-term-eu-budget/2021-2027/spending-and-revenue_en (local: `data/raw/11_verify2/ec_eu_budget_2000-2025.xlsx`) |
| S36 | Sénat | *Rapport général* n° 111 (2010-2011), tome III, annexe 14 (PLF 2011, Gestion des finances publiques et des ressources humaines): RGPP 50% return rule, 2009 outturn | 2010-11-18 | https://www.senat.fr/rap/l10-111-314/l10-111-3143.html |
| S37 | IGF and IGAS | *Revue de dépenses relative à la réduction des absences dans la fonction publique* (IGF 2024-M-013-03, IGAS 2024-026R; supervised by A. Triolle) | July 2024 | https://vie-publique.fr/files/rapport/pdf/295386.pdf (local: `data/raw/11_verify2/igf_igas_absences_2024.pdf`) |
| S38 | Insee (A. Cazenave-Lacroutz, A. Godzinski) | *Le jour de carence dans la fonction publique de l'État : moins d'absences courtes, plus d'absences longues*, Insee Analyses n° 36 | 2017-11 | https://www.insee.fr/fr/statistiques/3181789 |
| S39 | Public Sénat; Acteurs publics (press) | *Réduction du nombre de fonctionnaires : le virage à 180 degrés de Gabriel Attal*; *Gabriel Attal propose 100 000 fonctionnaires en moins…* | 2026-07-03 | https://www.publicsenat.fr/actualites/politique/reduction-de-nombre-de-fonctionnaires-le-virage-a-180-degres-de-gabriel-attal ; https://acteurspublics.fr/articles/gabriel-attal-propose-100-000-fonctionnaires-en-moins-et-limpunite-zero-pour-les-ministres-depensiers/ |
| S40 | Insee | *Les naissances en 2025 et en séries longues*, Insee Résultats (definitive: 643,905 births) | 2026-07-06 | https://www.insee.fr/fr/statistiques/9000195 |
| S41 | Fondation iFRAP (liberal) | *Macron, Le Pen, Zemmour, Mélenchon : le coût de leur programme pour les finances publiques* | 2022-04-07 | https://www.ifrap.org/budget-et-fiscalite/macron-le-pen-zemmour-melenchon-le-cout-de-leur-programme-pour-les-finances-publiques |
| S42 | Insee | *La flambée des prix de l'énergie : un effet sur l'inflation réduit de moitié par le « bouclier tarifaire »*, Insee Analyses n° 75 | 2022-09 | https://www.insee.fr/fr/statistiques/6524161 (local: `data/raw/11_verify2/insee_ia75.pdf`) |

---

## Verification log (2026-10-25)

| Claim | Check | Result |
|---|---|---|
| LFI: 106.4 / 81.7 / 24.7; each revenue line; the four spending blocks (37.5 / 22.2 / 10 / 12); SMIC 1,700 net; fuel 1.70 EUR/l by decree; repeal = 9 bn; 60 "objective within the term" | Read in the primary PDF (pdftotext) | **Confirmed.** The revenue lines sum exactly to 106.4; the spending items sum to 81.7. |
| IPP Note 125: −2% to −4% / −5%; 0.6 bn; two-thirds / one-third; Table 1 compliance; Paris −282 / −118; decile 22 vs. 70 m EUR | Read in the primary PDF | **Confirmed** |
| Pump prices and consumption | Read in the DGEC bulletin and xlsx | **Confirmed**; the derived excise and the 26.5 bn are our computations |
| RN, LR, Horizons, Attal, Glucksmann figures | Press and iFRAP only | **Confirmed as reported**; no primary documents |
| Le Pen appeal ruling (2026-07-07) and cassation timing | Public Sénat 2026-07-08 | **Confirmed as reported** |
| No Montaigne, IPP or OFCE costing | Homepages / hubs fetched | **Confirmed absent** on 2026-10-25 |

## Verification log (2026-10-25)

*Adversarial fact-check pass (second pass, same day). Every key claim was re-tested against the primary document where one exists, or against the cited page re-downloaded on 2026-10-25. Raw copies (untrusted, never executed) are in `research/data/raw/11_factcheck/` (press pages, iFRAP, Montaigne, Cour, CAE, AER, Euronews extract via headless browser), plus the existing `11_lfi/`, `11_fuel/`, `11_ipp/`, `hcfp/`, `ccomptes_debates/` and `06_verify/igf.txt`. All 21 cited URLs returned HTTP 200, except Euronews, which returned 406 to scripts and was read in a browser.*

| # | Claim | Checked against | Verdict | Correction / note |
|---|---|---|---|---|
| 1 | LFI 2027: +106.4 / −81.7 / +24.7 bn | LFI PDF (2026-10-14), "BILAN" box p. 14 and spending box p. 12 | **Confirmed** | Recomputed: the 14 revenue lines sum to 106.4; 37.5 (17 + 8 + 3 + 9.5) + 22.2 (0.5 + 3.6 + 3.5 + 3 + 2.6 + 2 + 7) + 10 + 12 (9 + 3) = 81.7. 24.7/3,135 = 0.79% of 2027 GDP. |
| 2 | LFI uncosted items: SMIC 1,700 net; fuel 1.70 EUR/l by decree; 60 with 40 years "objective within the term"; end of relief above 2 SMIC | LFI PDF pp. 9, 11, 14 | **Confirmed** | None of the four carries an amount in the PDF. |
| 2b | "LFI cites the IGF report as its benchmark" (§0 benchmarks) | LFI PDF full text | **Not found → ⚠ unverified** | Struck through in place. |
| 3 | Fuel freeze ≈ 26.5 bn/yr at 16-Oct-2026 prices; ~0 at 2025 prices | DGEC NPG 2026-10-16 (TTC diesel 234.58 / E10 214.89 c/l; HTT 134.74 / 112.05; rolling-12-month road fuel 45,828 thousand m³ = diesel 30,190 + gasoline 15,638; Brent 127.73 $/b = 114.09 EUR/b; EU-27 diesel 2.14, SP95 2.01; euro area 2.19 / 2.08); weekly CSV (2025 means: diesel 1.619, E10 1.690) | **Arithmetic confirmed (26.52)**; **labeling corrected** | It was presented as a 2027 cost. It is a spot-price scenario. The PLF 2027 assumes Brent at 80.3 $/b in 2027 (HCFP §13); the bulletin shows ICE Brent futures at 105.8 $/b. The 2027 cost at the PLF oil price is likely a few bn (⚠ own approximation). Sensitivity added: 0.10 EUR/l ≈ 4.6 bn/yr. |
| 4 | RN: 140 bn by 2032; 30 bn net tax cuts; deficit < 3% in 2030; growth 1.8% | Public Sénat 2026-10-06; PGE; Euronews 2026-10-07 (browser) | **Confirmed as reported** | "Net" and "level vs. 2026" come from PGE, which relays France Transactions and Europe 1 (tertiary). Public Sénat says only "140 bn of savings by 2032". 1.8% growth: Euronews quotes the government ("Le gouvernement note…"), with no period given. |
| 5 | Institut de l'Entreprise: 69.3 / 140.3; 7.5 credible (−25/+50); 80%; 2027 deficit 5.9% | PGE page (secondary); primary note searched, not found | **Reported figures confirmed; source internally inconsistent; interpretation corrected** | (a) The six printed blocks sum to 89.3 and 183.4, not 69.3 / 140.3 → ⚠ flagged. (b) The 5.9% 2027 deficit equals the IGF unchanged-policy deficit for 2027, so the file's "−28 bn deterioration vs. PLF" conversion was struck. (c) Added: the RN's own 2027 deficit hypothesis is 3.7% (per IdE via PGE). |
| 6 | LR: 197 bn over five years; 146 / 51 (56); pensions 42; unemployment/aid 30; 400,000 = 25; immigration 10; < 3% in 2031, 2.2% end of term | Public Sénat 2026-10-12 | **Confirmed**, with one **error found** | The file's "+5 tax/subsidy + 4 social" fraud line is wrong. The source gives a single 5 bn for tax and social fraud, and the 4 bn is the sick-leave line, which was double-counted. Corrected to +5 (0.14% of 2032 GDP). The 7.5 bn operators line includes the 5 bn of departures; this is consistent with the State total of 96. Also in the source: a primary surplus in 2030. |
| 7 | Horizons: +10 savings / −10 tax rises cancelled; +1 bn from undoing the suspension | Moneyvox/AFP 2026-10-13 | **Confirmed** | Half State, half social; shares the 5.0% 2027 target. Items also include non-replacement of 1 in 3 civil servants, 2 waiting days and social-security funds' spending −3%/yr. |
| 8 | Philippe: 65 and 45 years ≈ 30 bn per full year | Franceinfo 2026-09-30 | **Confirmed** | Candidate's estimate ("gain pour les caisses de l'État"); "in less than 10 years". |
| 9 | Attal: 150 bn over the term; 20 bn brake from May 2027; 100,000 posts = 7 bn/yr; < 3% before 2032 | iFRAP comparator (re-downloaded) | **Confirmed as listed** | Also listed: balance by 2037 and a 2028 *année blanche*. The exclusion of education, armed forces, justice and interior from the 100,000 posts is **not** in iFRAP's text → ⚠ unverified. |
| 10 | Glucksmann: −15 CSG / +15 (2 + 3 + 10) | iFRAP; Parlons-politique 2026-08-24 | **Confirmed** | iFRAP elsewhere says "inheritances above 2 M EUR" (vs. 1.8 M for the top rate). Parlons-politique says "certain social levies", not CSG. |
| 11 | Benchmarks: 2026 deficit 164.9 (5.4%); 2027 158.1 (5.0%); GDP 3,135.0 | HCFP Avis 2026-5 (2026-09-25), annex table | **Confirmed** | Same table: 2025 outturn **151.6** (vs. Insee 152.5) → divergence note added. Also confirmed: PO 44.2% (2027); interest 66 → 79 → 91; pensions 363; PSR UE 31; growth 1.0% judged "optimiste"; anti-fraud "optimiste voire hypothétique". The interest note adds Insee's 64.7 for 2025. |
| 12 | Debt-stabilizing gap 3.0 pts = 89.6 bn; IGF 125 bn by 2032, primary surplus 0.8% | Cour RSPFP June 2026 (local PDF); IGF report July 2026 (local text) | **Confirmed** | Cour: the 89.6 bn is the extra effort needed to stabilize the ratio **at its 2024 level** given 2025. IGF: the 0.8% is a **structural** primary surplus. The IGF also calls a zero multiplier a "very favorable" assumption. Both RSPFP URLs (2026-06 and 2026-07 folders) resolve. |
| 13 | IPP Note 125: −2 to −4% (−5%); 0.6 bn; one-third public; Paris 35.6% | IPP PDF (May 2026) | **Confirmed**, with one **wording error** | The note says ~4% after five semesters and 5% at the end of the period; the §6.1 text said "~5% after 5 semesters" and has been corrected. Table 1 (35.6 / 41.3 / 42.1 / 43.5 / 32.8), −282 / −118 and 22 vs. 70 m EUR are confirmed. |
| 14 | Diamond, McQuade, Qian (AER 2019): −15% rental supply | AEA abstract | **Confirmed** | Also: tenant mobility −20%. |
| 15 | Energy shields ~72 gross / 36 net; mostly untargeted | Cour des comptes page 2024-03-15 | **Confirmed** | Also confirmed: > 30 bn of wholesale margins, ~9 bn net cost in 2022-23, > 17 bn for gas and fuels, 4.5 bn of windfall contributions. |
| 16 | CAE Note 69: +9 to +19 bn | CAE PDF (Dec 2021) | **Confirmed**, with a nuance | 9 bn = base 1 with the current schedule; 19 bn = base 2 with current effective rates. Both are static/mechanical. "Steady state" is the CAE's wording for the > 10 bn scenario (base 2, schedule 4). |
| 17 | Montaigne 2022: 85.8 (36-112.8), pension schemes only | Montaigne page | **Figures confirmed; scope clarified** | 85.8 is a broader package, not 60/40 alone. The pure age-and-quarters reading is 36 bn, and LFI's own 2022 counter-costing for 60/40 was 27 bn. Note added in §4.1. |
| 18 | Le Pen: appeal 2026-07-07, 45 months (30 suspended) without provisional execution; cassation "at the latest early April 2027"; disputed eligibility | Public Sénat 2026-07-08 | **Confirmed** | 3 years (1 firm, at home under an electronic tag), 100,000 EUR fine. First instance: 5 years with provisional execution. The Conseil constitutionnel will rule on admissibility. |
| 19 | No Montaigne 2027 costing | Montaigne site; web search 2026-10-25 | **Confirmed** | `/presidentielle-2027/` redirects to *Les Repères de Montaigne* (25 notes, 4 "ambitions"). A web search found no 2027 costing by Montaigne, IPP or OFCE; only iFRAP's 2022 and 2024 costings exist. |
| 20 | Derived ratios (0.79%; 15.6% of 158.1; 26% of ~94; 3.9% / 4.1% / 4.19% of 2032 GDP; 131% of ~107; IdE ≈ 5% of the claim) | Recomputed | **Confirmed** | All rest on the 2032 GDP assumption (3,582 bn = 3,135 × 1.027⁵), which is our own and not an official figure. |

**Still ⚠ unverified after this pass:** the primary Institut de l'Entreprise note (and hence the reconciliation of its block totals); the RN 2027 counter-budget PDF; the source of the "LFI cites the IGF report" statement; Attal's exclusion list for the 100,000 posts; the expected 2027 fuel-freeze cost at the PLF oil price (own approximation only); the items already listed in §11 (waiting-day costing, RGPP 50% rule, births, net EU contribution, CNAV repeal figures).

## Verification log (2026-10-25, third pass: README §7 and §8 follow-up)

*Scope: every item listed for file 11 in README §7, every ⚠ left in this file, and alignment with `00-reference-figures.md`. README §8 lists no residual inconsistency for file 11, and the three flags it says were resolved elsewhere (Ifop 86% poll, PISA 2025, PLF 2027 staffing plan) do not appear in this file, so no change was needed for them. Raw downloads (untrusted, never executed) are in `research/data/raw/11_verify2/`. Blocked pages (rassemblementnational.fr, francetvinfo.fr, ccomptes.fr search) were read with a headless browser.*

**A. Alignment with `00-reference-figures.md`**

| # | Location | Was | Now | Canonical row |
|---|---|---|---|---|
| A1 | §0 benchmarks, 2025 deficit | 152.5 bn (May 2026 vintage), with a note | **151.6 bn = 5.1% of GDP** (Oct 2026 EDP notification) | 31 |
| A2 | §0 benchmarks and R6, total public expenditure 2025 | 1,714.2 bn (Insee) | **1,714.1 bn (Eurostat) = 57.3% of GDP**; Insee 1,714.2 in brackets | 1 |
| A3 | §0 benchmarks, interest | "66 (2025) → 91 (2027f)" | **65.7 (2025, ESA D.41) → 79.2 (2026f) → ~91 (2027f)**, general government, national accounts | 39, 40 |
| A4 | §9 item 1, 10-year OAT | "4.7% in Sept. 2026 (file 06)" | **4.44%**, monthly average Sept 2026, 97 bp over the Bund (Eurostat) | 43 |

**B. Items from README §7 and remaining ⚠ flags**

| # | Item | Primary source checked | Outcome |
|---|---|---|---|
| B1 | Institut de l'Entreprise note on the RN (block totals 89.3/183.4 vs 69.3/140.3) | IdE PDF, 2026-10-06, found through the institute's WordPress media library [S7a] | **Confirmed and corrected.** The note exists, and 69.3 / 140.3 / 7.5 / −25 to +50 / 80% / 5.9% are confirmed. The "inconsistency" came from the press relay, which dropped 5 of 11 rows; with all rows the totals are 69.4 / 140.3. They are **net**, not gross, improvements. New from the primary: credible gain **2.9 bn in 2027** (vs 71.6 shown); 2031 deficit 6.5% (RN 2.3%); **about 25 bn worse than the PLF 2027 in 2027** (the struck "−28 bn" was the right order of magnitude; the "IGF unchanged-policy" reinterpretation was wrong); RN debt path 119.3% (2027) → 112.1% (2032), not "121% → 112%". |
| B2 | RN 2027 counter-budget PDF | rassemblementnational.fr homepage, documents block and press-conference page (browser); 7 guessed URLs (404) | **Still unverifiable.** Not posted. Its title and slide references are known from [S7a]. Recommendation: **keep with caveat** ("RN press kit, figures as transcribed by the Institut de l'Entreprise"). |
| B3 | "LFI cites the IGF report" | LFI PDF full text (re-extracted); Public Sénat/AFP 2026-10-14 [S4b] | **Confirmed in modified form.** Not in the PDF, but Mélenchon said orally that the plan was "dans l'épure" of the "economists' report submitted to Bercy" (≥ 125 bn), which matches the IGF mission. Wording corrected in §0. |
| B4 | Attal's exclusion list for 100,000 posts | Public Sénat and Acteurs publics, 2026-07-03 [S39] | **Confirmed**: Education, Armed Forces, Justice and Interior are spared; the cuts concern **State** posts; 7 bn of savings. ⚠ removed. |
| B5 | Fuel-freeze cost at the PLF oil price | Own computation from DGEC data [S20] and HCFP's 80.3 $/b [S3] | **Corrected**: "a few bn" → **about 12 bn/yr** at 80.3 $/b and **about 20 bn/yr** at the 105.8 $/b futures price (full crude pass-through, October 2026 margins). Labeled as our scenario, not an institutional estimate. |
| B6 | CNAV repeal cost 3.4 (→5) / 16 bn | Assemblée nationale amendment n° 728 to PPL 613 (2024-11-25) [S34] | **Partly sourced, keep with caveat.** 3.4 bn (2025) and 16 bn (2032) are quoted as CNAV estimates in official parliamentary documents. The CNAV note is not public. The "−5" upper bound had no source and was removed. |
| B7 | Current FTT yield (~2 bn) | Cour des comptes report and press release, 2026-09-10 [S33] | **Corrected: 2.53 bn in 2025** (rate 0.4% since April 2025). |
| B8 | PLF 2025 waiting-day costing (~1.2 bn) | IGF-IGAS spending review, July 2024 [S37]; AN amendments II-2322 and II-3140 (Nov 2024) | **Corrected and made relevant**: 2nd waiting day **174 M EUR**, 2nd + 3rd **289 M EUR**, 90% sick pay **900 M EUR** (about 1 bn per the amendments). Horizons' two days ≈ **0.17 bn/yr**. |
| B9 | Insee 2012 waiting-day study | Insee Analyses n° 36 (Nov 2017) [S38]; summary in [S37] | **Confirmed**: two-day absences more than halved, absences of one week to three months +25%, total absence rate unchanged. |
| B10 | Insee's ~3-point effect of the shield on 2022 inflation | Insee Analyses n° 75 (Sept 2022) [S42] | **Confirmed with a period correction**: without the shield, inflation from Q2 2021 to Q2 2022 would have been **3.1 points higher** (actual 5.3%). |
| B11 | RGPP "50% returned" rule | Senate *Rapport général* n° 111 (2010-2011), t. III, annexe 14 [S36] | **Confirmed and qualified**: the rule (speech of 4 Apr 2008) was 50%; in 2009 the return was about 700 of 860 M EUR (about 80%). |
| B12 | ~650,000 births a year | Insee Résultats, 2026-07-06 [S40] | **Corrected: 643,905 births in 2025** (definitive). Endowment cost ≈ 0.64 bn/yr. |
| B13 | France's net EU contribution | European Commission *EU spending and revenue 2000-2025* xlsx [S35]; IdE [S7a] | **Sourced (own computation)**: 2025 net contribution ≈ **8.7 bn** (all own resources incl. customs, minus EU spending in France excl. NGEU) or ≈ **7.2 bn** on the operating-balance convention (excl. customs and administration); 2024 ≈ 6.4 bn on the same convention. The IdE says "about 9 bn". A 5 bn cap would "save" at most 2-4 bn. *(Superseded 2026-10-25, index pass: use the official PLF 2027 *Jaune UE* figures, EUR 9.5 bn accounting method / 6.4 bn operating balance, 2025; a 5 bn cap would save at most about 1.4-4.5 bn. See file 16 §3.1 and 00 row 52.)* |
| B14 | Paris rent-control compliance 40% → 13% | Franceinfo/Radio France article (2018-07-18), read in a browser [S25] | **Corrected (misreading)**: in 2017, 4 rents in 10 *exceeded* the cap; after the annulment, compliance fell **by 13 points** in six months (CLCV advocacy sample of ~1,000 listings). Recommendation: **keep with caveat** or **replace by** IPP's 35.6% non-compliance (2020-2024). |
| B15 | Franceinfo calling Glucksmann's package "optimistic" | Web search 2026-10-25 | **Still unverifiable** → **drop from site**. |
| B16 | iFRAP 2022 on Zemmour (+5 bn) | iFRAP article 2022-04-07 [S41] | **Confirmed and clarified**: the program would **worsen** the 2027 deficit by 5 bn. The unverified Montaigne 2022 mention was dropped. |

**C. Additional corrections found while reading the IdE primary note**

- RN 0% VAT on 100 products: **3.5 bn** (was "not separately costed"); abolition of CFE, CVAE and C3S: **17.1 bn** (was "not separately costed"); RN pension reform cost **9.5 bn in 2031**; "repair of the pension system" **+15.0 bn** with no measure described; agencies **10.1 bn by 2031**; VAT withheld at source 18.0 and procurement cartels 5.8.
- The components of the 23.5 bn of "no Maastricht effect" entries (4.2 + 7.0 + 3.0 + 9.3) are now named in §4.2.

**Still ⚠ after this pass:** the RN 2027 press kit (not public; figures via the IdE transcription, keep with caveat); ~~the CNAV repeal note (cited in Parliament only, keep with caveat)~~ (resolved in the index pass: file 03 verified the Cnav figures, 3.4 bn in 2025 to 15.7 bn in 2032, in AN report no. 613); the Franceinfo "optimistic" remark on Glucksmann (drop from site); CLCV 2018 compliance figures (advocacy sample, keep with caveat or replace by IPP 35.6%).
