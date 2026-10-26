# 15 - Immigration and public finances: net fiscal contribution, the AME, and the costing of "national preference" savings

*Research file 15 for the public-finance education platform (2027 presidential election). Compiled 2026-10-25. All web sources were accessed on 2026-10-25. Figures we computed ourselves are marked "(our computation)" and point to a CSV. Where this file qualifies a statement in another file, it says so in §9; it does not edit the other files. `00-reference-figures.md` remains canonical for every macro aggregate used here (GDP, total expenditure).*

**Scripts** (Python standard library plus `openpyxl`, run with `python3 -I`): `research/scripts/15/dump_xlsx.py`, `oecd_stats.py`, `eurostat_fb_share.py`, `convert_eur.py`.
**Raw data** (untrusted downloads, never executed): `research/data/raw/15/oecd/` (seven OECD StatLink workbooks), `research/data/raw/15/eurostat/migr_pop3ctb.json`, `research/data/raw/15/docs/` (CEPII letters and working paper, Cour des comptes 2020 synthesis, PAP 2027 programme 183, Insee page). RN and Institut de l'Entreprise documents are reused from `research/data/raw/11_rn/` and `research/data/raw/11_verify2/`.
**Computed CSVs:** `research/data/15_oecd_fiscal_immigration_stats.csv`, `research/data/15_eurostat_foreign_born_share.csv`, `research/data/15_conversions_eur_2025.csv`.

**Vocabulary.** *Immigré* (immigrant, Insee definition) = a person born abroad who was not French at birth; they remain an *immigré* after naturalization. *Étranger* (foreign national) = a person without French nationality, wherever born. **Foreign-born** (OECD, Eurostat) = everyone born abroad, **including French citizens born abroad** (1.7 million people in France, many of them repatriates from former colonies). The OECD estimates below use the foreign-born concept; the CEPII estimates use the *immigré* concept. *AME* (*aide médicale de l'État*) = State medical aid for undocumented foreigners. *AMU* (*aide médicale d'urgence*) = the "emergency-only" scheme proposed by the RN and parts of the right. *Préférence/priorité nationale* (national preference/priority) = reserving benefits, jobs or housing to French nationals.

---

## 0. Bottom line (for the platform editors)

1. **There is no single "cost of immigration".** The best comparative estimate for France, OECD *International Migration Outlook 2021* (ch. 4), puts the **net fiscal contribution of the foreign-born at between +1.0% and -0.85% of GDP a year (2006-2018 average)**. The sign depends almost entirely on one accounting convention: how spending on public goods (defense, debt interest, institutions) is shared out.
   - **+1.02% of GDP** counting only spending that can be attributed to individuals (benefits, health, education).
   - **+0.25%** when "congestible" public goods (police, transport, utilities) are also charged per head.
   - **-0.30% / -0.53% / -0.85%** when pure public goods are also charged per head: excluding defense and debt interest / excluding debt interest only / all of them.
   - At 2025 GDP, this range is **about +EUR 30 bn to -EUR 25 bn a year** (our computation, illustrative: 2006-18 ratios applied to 2025 GDP).
2. **Under the convention where immigrants look worst (-0.85%), the native-born look worse in total (-3.25% of GDP)**, because general government ran a deficit in most years. The two contributions add up to the budget balance. **Per head**, however, the foreign-born contribute less than the native-born: -6.5% vs -3.7% of GDP per capita. The gap is 2.8% of GDP per capita, **about EUR 1,200 per foreign-born resident per year** at 2025 GDP per head (our computation, illustrative).
3. **The CEPII's 30-year French study (Chojnicki, Ragot and Sokhna, 2018) agrees on the order of magnitude.** On the primary budget (excluding interest) over 1979-2011, the immigrant contribution was usually negative but small. It ranged from **-0.49% of GDP (2011, after the crisis) to +0.05%**, and immigration "never determined" the primary deficit.
   - Change the convention and the result moves. Counting the French-born children of immigrants (under 16) as part of the immigrant population gives **-1.0% to -1.6% of GDP**. Charging all public goods to natives only gives **+0.02% to +0.55%**.
4. **The French result is weaker than in most comparable countries.** On the all-public-goods convention (C2), France ranks **21st of 25 OECD countries, 16th of 19 EU members in the sample and 7th of 8 in the panel**: France -0.85% vs a panel median of -0.32% and an OECD mean of -0.17%. Likely reasons (our reading; the OECD chapter does not state a France-specific explanation, it only notes that France's working-age share fell for both groups after the mid-2000s): an older foreign-born population (long-standing immigration, including repatriates) and a large employment gap for immigrant women (54% vs 69%, Insee 2025). *(corrected 2026-10-25: was "The reasons are...", presented as established)*
   - Closing the employment gap for prime-aged immigrants would add about **+0.22% of GDP (about EUR 7 bn)** (OECD Table 4.6).
5. **The AME is small relative to the debate.** The PLF 2027 (draft 2027 budget) requests **EUR 1.208 bn** for the AME action (action 02 of programme 183, whose total is EUR 1.216 bn; of which EUR 1.138 bn for standard AME). *Scope label: 1.208 bn = AME action; 1.216 bn = programme 183 as shown in file 16.* **Actual 2025 spending on standard AME was EUR 1.340 bn**: the line is chronically under-budgeted, and the State owed the national health insurance fund (CNAM) EUR 185 m at end-2024. That is **0.045% of GDP and 0.08% of total public expenditure**. Beneficiaries: **454,111 at end-2025** (down 2.4% on 2024).
6. **RN savings claims are large compared with every official measure of the stakes.**
   - The RN's 2027 counter-budget books **+EUR 15.1 bn (2027) rising to +29.0 bn (2031)** from immigration (as transcribed by the Institut de l'Entreprise). Of this, **EUR 18.1 bn in 2031 comes from "reserved benefits"**: solidarity benefits only after five years of work (12.2) and family benefits only with a French parent (5.9).
   - The Institut de l'Entreprise (business-funded) classes **92% of the immigration block as undocumented or legally fragile**.
   - The *Conseil constitutionnel* (Constitutional Council) has already struck down, on substance, a five-year residence / 30-month work condition for family and housing benefits (decision 2024-6 RIP, 11 Apr 2024).
7. **The AME-to-AMU line does not add up.** The RN's 2026 counter-budget claimed **EUR 1.3 bn** from replacing the AME by an AMU. That is **108% of the 2027 AME action credits (1.208 bn; 107% of the programme 183 total of 1.216 bn) and 97% of 2025 AME spending** (our computation). It assumes an emergency scheme that costs almost nothing, and it ignores the existing "soins urgents" (emergency care) envelope and the hospital bad debt that an AMU would shift elsewhere.
8. **Defensible wording:** "Depending on how defense and debt interest are shared, immigrants' net contribution to French public finances lies between about +1% and -1% of GDP; per head it is below that of the native-born; reserving benefits to nationals faces constitutional and EU-law obstacles, so the RN's EUR 15-29 bn is not a bankable saving." **Not defensible:** "immigration costs France EUR X bn" quoted as a single number, and "immigrants pay for our pensions" as a general claim.

---

## 1. Key figures

| # | Indicator | Value | Unit | Data year | Published | Institution | URL |
|---|---|---|---|---|---|---|---|
| K1 | Immigrants (*immigrés*) living in France | **7.97 m = 11.6%** of the population (2024: 7.75 m = 11.3%; **series break in 2024**); foreign nationals 6.3 m = 9.1%; born abroad (all) 9.63 m = 14.0% | persons / % of population | 2025 (provisional) | 25 Jun 2026 | Insee, *L'essentiel sur... les immigrés et les étrangers* | https://www.insee.fr/fr/statistiques/3633212 |
| K2 | Employment rate 15-64, immigrants vs non-immigrants | Men 71-72% vs 71-72% (no gap); **women 54% vs 69%**; unemployment 12-13% vs 7% | % | 2025 | 25 Jun 2026 | Insee (same page) | same |
| K3 | Net fiscal contribution of the foreign-born, France | **A +1.02; B +0.25; C2 -0.85**; intermediate -0.30 (excl. defense and debt) and -0.53 (excl. debt) | % of GDP | 2006-18 average | Oct 2021 (StatLinks v1, 28 Oct 2021) | OECD, IMO 2021 ch. 4, Table 4.1 and Annex Table 4.A.3 | https://stat.link/1jovf5 ; https://stat.link/riasgf |
| K4 | Same, native-born, France | A +9.31; B +4.17; C1 -4.35 (pure public goods charged to natives only); **C2 -3.25** | % of GDP | 2006-18 average | Oct 2021 | OECD Table 4.1 | https://stat.link/1jovf5 |
| K5 | Foreign-born **plus their native-born children**, France | A +0.46; B -0.31; **C2 -1.41** | % of GDP | 2006-18 average | Oct 2021 | OECD Table 4.2 | https://stat.link/hsu5gq |
| K6 | Net contribution per capita, France (C2) | foreign-born **-6.54**, native-born **-3.74** | % of GDP per capita | 2006-18 average | Oct 2021 | OECD Annex Table 4.A.4 | https://stat.link/d7pb0g |
| K7 | Fiscal ratio (revenue / expenditure), France | Items at individual level: FB 1.24 vs NB 1.29. All public goods: **FB 0.88 vs NB 0.93** (relative 0.94) | ratio | 2006-18 average | Oct 2021 | OECD Table 4.3 | https://stat.link/xtnvok |
| K8 | Gain if prime-aged immigrants had natives' employment rates (same sex and education), France | **+0.22** (men +0.09, women +0.13) | % of GDP | 2006-18 average | Oct 2021 | OECD Table 4.6 | https://stat.link/v56fn7 |
| K9 | Net contribution of immigrants to the **primary** balance, France | Generally negative, **between -0.49% (2011) and +0.05%**; -8.8 bn in 2011 (EUR 2005 prices); authors' envelope "±0.5%" (±0.2% excluding 2011) | % of GDP / EUR bn | 1979-2011 | Apr 2018 (WP 2018-04); Dec 2018 (*Lettre* 394) | CEPII: Chojnicki, Ragot, Sokhna | http://www.cepii.fr/PDF_PUB/lettre/2018/let394.pdf ; http://www.cepii.fr/PDF_PUB/wp/2018/wp2018-04.pdf |
| K10 | Same, alternative conventions | Second-generation children (< 16) charged to immigrants: **-1.0% to -1.6%** (about -30 bn in 2011). Public goods charged to natives only: **+0.02% to +0.55%** | % of GDP | 1979-2011 | Dec 2018 | CEPII *Lettre* 394 | same |
| K11 | Net contribution of immigration to general government, 2005 | **about +EUR 3.9 bn** (positive; *the Lettre uses the conditional "serait"*). Consistent with CEPII WP 2018-04, which cites Chojnicki (2013) for **+0.2% of GDP** in 2005 | EUR bn | 2005 | 15 Jun 2011 (citing the Drees-MiRe 2010 report and Chojnicki 2011, *Revue économique*) | CEPII *Lettre* 311 (Chojnicki & Ragot) | http://www.cepii.fr/PDF_PUB/lettre/2011/let311.pdf |
| K12 | Dynamic (CGE model): stopping immigration from 2010 | **Widens the social-protection financing need by about 1.3 pts of GDP by 2050** | pts of GDP | projection to 2050 | 15 Jun 2011 | CEPII *Lettre* 311 | same |
| K13 | AME credits, PLF 2027 | Action 02: **EUR 1,208.3 m** (standard AME 1,137.9; *soins urgents* 70; other AME 1); programme 183 total 1,216.3 m. Same total in LFI 2026 and the 2028-2029 indicative forecasts. *(Note 2026-10-25: the components shown in the PAP sum to 1,208.9 m; the Senate's PLF 2026 report gives standard AME 1,137.3 m, which with 70 + 1 sums exactly to 1,208.3 m. The PAP 2027's "1,137.9" is probably a typo for 1,137.3.)* | EUR m | 2027 | 1 Oct 2026 | PAP 2027, programme 183 "Protection maladie" (Direction de la sécurité sociale) | https://www.budget.gouv.fr/documentation/file-download/33907 |
| K14 | AME spending (standard AME), actual | **EUR 1,340 m in 2025**; +6% a year on average since 2009; 65% hospital | EUR m | 2025 | 1 Oct 2026 | PAP 2027, programme 183 | same |
| K15 | AME beneficiaries | **454,111** at 31 Dec 2025 (465,208 in 2024; 456,689 in 2023; 202,503 in 2009); 71% received at least one reimbursement in Q4 2025 | persons | 2025 | 1 Oct 2026 | PAP 2027, programme 183 | same |
| K16 | AME under-budgeting | 2024: credits executed 1,159 m vs actual standard-AME spending 1,255 m; 117.8 m spent without budget; **State debt to the CNAM 185.1 m at end-2024**; 2025 spending estimate 1,314 m (outturn: 1,340 m, K14) | EUR m | 2024-2025 | 24 Nov 2025 | Senate, *rapport général* no. 139 (2025-2026), t. III annex 27 (V. Delahaye) | https://www.senat.fr/rap/l25-139-327/l25-139-3272.html |
| K17 | State spending on immigration and integration policies (DPT scope) | **EUR 6.57 bn = 1.41% of gross general-budget spending**; +48% vs 2012 (asylum explains one-third of the rise, AME one-fifth). The Cour's web page rounds it as "about 1.6% of the State budget, i.e. EUR 6.6 bn". *Update (added 2026-10-25):* the Senate law committee's opinion on the PLF 2026 states that credits allocated to immigration policies "*s'élèvent à 7,8 milliards d'euros*", of which the *Immigration, asile et intégration* mission is 2.16 bn (Senate opinion no. 145 (2025-2026), t. II, 24 Nov 2025, https://www.senat.fr/rap/a25-145-2/a25-145-21.pdf; stated in the committee debate, presumably the DPT scope; ⚠ DPT itself not opened) | EUR bn | 2019 (2026: 7.8) | 5 May 2020 | Cour des comptes, *L'entrée, le séjour et le premier accueil des personnes étrangères* (synthesis, citing the *document de politique transversale*) | https://www.ccomptes.fr/fr/publications/lentree-le-sejour-et-le-premier-accueil-des-personnes-etrangeres |
| K18 | Direct cost of fighting irregular immigration | **about EUR 1.8 bn a year**; about 16,000 full-time staff | EUR bn / yr | about 2022 (⚠ the publication page gives no reference year; check the full report before citing a year) | 4 Jan 2024 | Cour des comptes, *La politique de lutte contre l'immigration irrégulière* | https://www.ccomptes.fr/fr/publications/la-politique-de-lutte-contre-limmigration-irreguliere |
| K19 | RN 2027 counter-budget, immigration block (net balance improvement) | **+15.1 (2027) → +29.0 (2031)**; reserved benefits 12.2 + 5.9 = **18.1 in 2031**; 92% "undocumented or legally fragile" | EUR bn | 2027 / 2031 | 6 Oct 2026 | RN press kit as transcribed by the Institut de l'Entreprise (business-funded think tank) | https://www.institut-entreprise.fr/wp-content/uploads/2026/10/Analyse-primaire-contre-budget-RN-Note-de-contexte-IDEP.pdf |
| K20 | RN 2026 counter-budget, immigration block | **+11.9** = solidarity benefits after 5 years' full-time work 6.1 + AME → AMU 1.3 + end of the 1968 Franco-Algerian agreement 1.3 + expel foreigners without a job for a year 1.11 + higher fees for foreign students 1.1 + end of the "medical visa" 1.0 | EUR bn | 2026 | 24 Oct 2025 (PDF creation date) | Rassemblement national, *Contre-budget 2026* (party document) | https://rassemblementnational.fr/documents/GRN-CONTRE-BUDGET-2026.pdf |
| K21 | Foreign-born share of the population (Eurostat concept) | France **14.0%**; EU-27 aggregate 14.4%; panel median 18.0; France **7th of 8** in the panel and **15th of 26** in the EU | % of population | 1 Jan 2025 | data updated 25 Sep 2026 | Eurostat `migr_pop3ctb` (our computation) | https://ec.europa.eu/eurostat/databrowser/view/migr_pop3ctb/default/table |

---

## 2. Methodology: why honest estimates differ by two points of GDP

### 2.1 Static vs dynamic
- **Static (accounting) studies** split one year's revenue and spending between immigrants and natives (OECD 2021; CEPII 2018). They answer: "what did immigrants living here this year pay and receive?" They say nothing about what would happen *without* them, and nothing about future pensions owed to today's young workers.
- **Dynamic studies** follow cohorts over their life cycle (generational accounting, e.g. Chojnicki 2006 for France), or simulate the economy with a general-equilibrium model (Chojnicki & Ragot, CEPII 2011; *Fiscal Studies* 2015). In those models, stopping immigration in 2010 widens France's social-protection financing need by about 1.3 points of GDP by 2050, because the population ages faster (K12).
- **Model-free macro studies** estimate the response of the budget balance to migration shocks. D'Albis, Boubtane and Coulibaly (*Science Advances*, June 2018; Western European countries, 1985-2015) find that asylum-seeker inflows "do not deteriorate host countries' economic performance or fiscal balance", and that the effects turn positive once asylum seekers become permanent residents. The OECD chapter cites a related VAR (vector autoregression) on 19 OECD countries (1980-2015) with a positive effect on the fiscal balance.
- **Caveat for the platform:** a static figure such as "-0.85% of GDP" is **not** the saving from less immigration. A dynamic or marginal estimate can have a different sign.

### 2.2 Average vs marginal cost, and the allocation of public goods (the decisive choice)
- The OECD sorts spending into three categories (IMO 2021, ch. 4):
  - **individualized** items: benefits, health, education;
  - **congestible public goods**, whose cost rises with population (police, transport, utilities). Following most studies, the OECD assumes marginal cost = average cost and charges them per head;
  - **pure public goods**, with **zero marginal cost** (defense, debt interest, executive and legislative bodies).
- If an extra resident does not raise defense or interest spending, the marginal logic (Rowthorn 2008, cited by the OECD) charges pure public goods to natives only (column C1). The average-cost logic charges them to everyone (column C2).
- **In France this one choice moves the immigrant result from +0.25% to -0.85% of GDP**, i.e. about EUR 33 bn at 2025 GDP. The CEPII shows the same sensitivity (K10).
- **Debt interest is a special case.** Charging today's interest on debt accumulated over decades to recent arrivals is contested. The OECD therefore also publishes variants without debt (-0.53%) and without defense and debt (-0.30%).

### 2.3 Who counts as "the immigrant population"
- **Children born in France to immigrant parents.** Counting them as immigrants while they are young and costly (school, family benefits) and as natives once they work and pay taxes biases the result downwards. The CEPII calls this choice "highly debatable" and keeps them with the natives. The OECD reports both versions (K3 vs K5): France goes from -0.85% to -1.41% of GDP.
- **Foreign-born vs *immigré*.** The OECD's French foreign-born population includes about 1.7 m French citizens born abroad (K1), an older group. This is one reason the OECD finds France and the Netherlands to be the countries where immigrants' relative fiscal ratio fell in the late 2010s.

### 2.4 Cycle, age structure and period
- Both groups' net contributions swing with the cycle. In 2011 the natives' contribution was -2.35% of GDP and the immigrants' -0.49% (CEPII).
- The OECD notes that France's working-age share fell for both groups after the mid-2000s.
- All OECD ratios are **2006-2018 averages**. They predate the post-2022 inflow (Ukraine) and the 2024 Insee series break (K1). Euro conversions in this file apply those ratios to 2025 GDP and are **illustrations, not estimates for 2025**.

### 2.5 Gross budget costs are not net contributions
- The Cour des comptes' **EUR 6.57 bn (2019)** is the State's gross spending on immigration, asylum, integration, naturalization and removal policies (K17). The **EUR 1.8 bn** is the direct cost of fighting irregular immigration (K18). Neither nets out the taxes and contributions immigrants pay, and both exclude social security.
- Putting them next to the OECD range is legitimate only if they are labeled "gross State spending on migration policy".

---

## 3. France: the estimates side by side

| Study | Method | Scope / period | Result | Sign | Source |
|---|---|---|---|---|---|
| OECD IMO 2021, ch. 4 | Static accounting, common method for 25 countries, LFS (labour force survey) + national accounts | Foreign-born, 2006-18 average | +1.02 / +0.25 / -0.30 / -0.53 / -0.85% of GDP depending on public-goods allocation | + to - | K3 |
| OECD IMO 2021, Table 4.2 | Same, with native-born children of immigrants | 2006-18 | +0.46 / -0.31 / -1.41% of GDP | + to - | K5 |
| CEPII, Chojnicki-Ragot-Sokhna (2018) | Static accounting on the **primary** balance (excluding interest), Insee surveys | *Immigrés*, 1979-2011 | -0.49% to +0.05% of GDP (central); -1.6% to +0.55% across their alternative conventions | mostly slightly - | K9, K10 |
| Chojnicki et al. (2010) for Drees-MiRe, as reported by CEPII *Lettre* 311 | Accounting, social protection and general government | 2005 | about +EUR 3.9 bn | + | K11 (⚠ primary report not opened) |
| Chojnicki & Ragot (CEPII 2011; *Fiscal Studies* 2015) | Dynamic CGE model | Projection to 2050 | Zero immigration raises the social-protection financing need by about 1.3 pts of GDP in 2050 | + (immigration helps) | K12 |
| d'Albis, Boubtane, Coulibaly (*Science Advances*, 2018) | Panel VAR, Western European countries | Asylum seekers, 1985-2015 | No deterioration of the fiscal balance; positive once they settle | 0 / + | §2.1 |
| Cour des comptes (2020; 2024) | Gross budget cost of migration policies | State budget, 2019; about 2022 | EUR 6.57 bn; EUR 1.8 bn (irregular immigration) | gross cost only | K17, K18 |

**Synthesis (our reading).** All official and academic estimates for France fall **between about +1% and -1.6% of GDP a year** *(corrected 2026-10-25: was "-1.5%", but the CEPII second-generation variant reaches -1.6%, K10)*. The central "full allocation" figures (OECD C2, CEPII) sit at **-0.5% to -0.85% of GDP**, i.e. roughly **EUR 15-25 bn a year** at 2025 GDP. Those figures are smaller than the native-born deficit computed on the same convention. They become positive once public goods with zero marginal cost are left out.

---

## 4. Range in euros (illustrative, 2025 GDP = EUR 2,991 bn)

*(our computation, `data/15_conversions_eur_2025.csv`; GDP implied by file 00 row 1: 1,714.1 / 0.573)*

| Convention (OECD, France, 2006-18 ratio) | % of GDP | ≈ EUR bn at 2025 GDP |
|---|---|---|
| A: individualized items only | +1.02 | **+30.5** |
| B: + congestible public goods per capita | +0.25 | +7.6 |
| + pure public goods except defense and debt interest | -0.30 | -8.9 |
| + pure public goods except debt interest | -0.53 | -15.9 |
| C2: all public goods per capita | -0.85 | **-25.3** |
| C2, including native-born children of immigrants | -1.41 | -42.1 |
| *Memo:* native-born, C2 | -3.25 | -97.3 |
| *Memo:* gain from closing the employment gap (prime-aged) | +0.22 | +6.7 |
| *Memo:* CEPII central range (primary balance) | -0.50 to +0.05 | -15.0 to +1.5 |
| *Memo:* AME spending 2025 (K14) | 0.045 | 1.34 |

**Per head (C2, OECD Annex Table 4.A.4):** foreign-born -6.5% and native-born -3.7% of GDP per capita, a gap of 2.8%. At 2025 GDP per head (EUR 43,448 = 2,991 bn / 68.85 m), that is **about EUR 2,840 vs EUR 1,620 per person, and about EUR 1,200 per foreign-born resident per year** (our computation, illustrative).

---

## 5. International comparison (OECD IMO 2021, 2006-18 averages)

*Our computation from the OECD StatLinks; `data/15_oecd_fiscal_immigration_stats.csv`. The OECD sample has 25 countries: 19 of them are EU members (EU-27 minus Bulgaria, Croatia, Cyprus, Hungary, Malta, Poland, Romania and Slovakia) and 16 are euro-area members. Means are unweighted. Rank 1 = most favorable (most positive). The UK was an EU member over the period but is excluded from the EU group.*

### 5.1 Net contribution of the foreign-born, % of GDP

| Convention | France | OECD-25 mean / median | France rank, OECD | EU-19 mean / median | France rank, EU | EA-16 mean / median | France rank, EA | Panel (FR + 7) mean / median | France rank, panel |
|---|---|---|---|---|---|---|---|---|---|
| A: individualized | +1.02 | 1.56 / 1.34 | 15/25 | 1.36 / 1.02 | 10/19 | 1.48 / 1.31 | 10/16 | 1.28 / 1.20 | 5/8 |
| B: + congestible | +0.25 | 0.90 / 0.73 | 18/25 | 0.72 / 0.62 | 12/19 | 0.76 / 0.50 | 10/16 | 0.67 / 0.69 | 7/8 |
| Excl. defense and debt | -0.30 | 0.29 / 0.19 | 21/25 | 0.17 / 0.02 | 15/19 | 0.21 / 0.03 | 13/16 | 0.06 / 0.09 | 6/8 |
| Excl. debt | -0.53 | 0.09 / -0.03 | 21/25 | 0.03 / -0.03 | 15/19 | 0.07 / -0.08 | 13/16 | -0.10 / -0.05 | 6/8 |
| **C2: all public goods** | **-0.85** | -0.17 / -0.28 | **21/25** | -0.22 / -0.28 | **16/19** | -0.20 / -0.29 | **13/16** | -0.41 / -0.32 | **7/8** |
| *Native-born, C2* | -3.25 | -1.91 / -1.60 | 17/25 | -2.27 / -1.60 | 13/19 | -2.69 / -1.91 | 10/16 | -1.66 / -1.29 | 6/8 |

**Panel values, C2 (% of GDP):** France -0.85; Germany -0.28; Italy +0.57; Spain -0.15; Netherlands -0.36; Belgium -1.28; Sweden -0.83; Denmark -0.08. *(The OECD's published "Average" row gives -0.158 for C2 and 0.876 for B. Our simple means of the same 25 cells give -0.168 and 0.902; Annex Table 4.A.3 itself prints 0.902 and -0.168. The small difference is in the OECD's Table 4.1 average row, not in the country values.)*

### 5.2 Per head, foreign-born minus native-born, C2 (% of GDP per capita)

| | France | OECD-25 mean / median | France rank | EU-19 mean / median | rank | EA-16 mean / median | rank | Panel mean / median | rank |
|---|---|---|---|---|---|---|---|---|---|
| FB − NB per capita | **-2.80** | +0.80 / -0.94 | 18/25 | +0.39 / -1.16 | 13/19 | +0.91 / -1.24 | 11/16 | -0.64 / -1.61 | 6/8 |

Panel: Italy +10.4, Spain +5.0, Denmark -1.2, Netherlands -1.5, Germany -1.7, **France -2.8**, Sweden -6.3, Belgium -7.0.

### 5.3 Reading
- **Southern Europe** (Italy, Spain, Portugal, Greece) and Luxembourg, Switzerland and the UK show favorable figures: their immigrant populations are young and recently arrived workers.
- **France sits with the old-immigration, generous-welfare group** (Belgium, Sweden), well below Germany and Denmark.
- Over time, the OECD singles out France and the Netherlands for a **fall in immigrants' relative fiscal ratio in the latest years** of the sample (Annex Table 4.A.7: France's relative ratio was 0.96 in 2007 and 0.90 in 2017).
- **Context: France does not have an unusually large immigrant population.** On Eurostat's foreign-born measure, France is at **14.0% in 2025**, against an EU-27 aggregate of 14.4%, an unweighted EA21 mean of 17.8% and a panel median of 18.0%. It ranks **7th of 8 in the panel** (Sweden 20.8, Germany 20.5, Belgium 20.2, Spain 19.3, Netherlands 16.8, Denmark 14.4, Italy 11.8) and 15th of 26 in the EU (`data/15_eurostat_foreign_born_share.csv`). France's weaker fiscal result therefore reflects the *composition* of its foreign-born population (age, women's employment, skills), not its size.
- **What the % of GDP comparison does not do.** Because % of GDP scales with the immigrant share, per-capita measures (§5.2) are the fairer cross-country comparator. On per-capita measures France is in the lower-middle of the pack, not an outlier.

---

## 6. The political claims and their costings

### 6.1 Rassemblement national (RN)

| Program | Immigration savings claimed | Main items | Independent assessment | Legal status |
|---|---|---|---|---|
| 2024 legislative elections | **EUR 8 bn/yr** | Not itemized in the costing | Institut Montaigne (5 Jul 2024; business-funded, liberal-centrist): the RN "*affiche des économies, portant essentiellement sur des mesures d'immigration (8 Md€) et sur la privatisation de l'audiovisuel public (1,6 Md€) dont la faisabilité juridique et politique demeure incertaine*" (file 07 [S13]). *(Precision added 2026-10-25: grammatically the "uncertain feasibility" clause may refer only to the broadcasting privatization or to both items; quote the full sentence rather than attaching it to the 8 bn alone.)* | n/a |
| Counter-budget 2026 (24 Oct 2025) | **EUR 11.9 bn** (0.40% of 2025 GDP) | Solidarity benefits only after 5 years' full-time work 6.1; AME → AMU 1.3; end of 1968 Algeria agreement 1.3; removal of foreigners without a job for a year 1.11; foreign-student fees 1.1; end of medical visa 1.0 (K20) | Fipeco (F. Ecalle): "as hard to cost as to characterize" (file 07, via Public Sénat) | Benefit condition: see 2024-6 RIP below |
| Counter-budget 2027 (press kit, 6 Oct 2026) | **+15.1 (2027) → +29.0 (2031)**; "29 bn in a full year", "20%" of the plan (Public Sénat) | Reserved benefits 18.1 in 2031 (solidarity after 5 years of work 12.2; family benefits only with a French parent 5.9); AME → AMU; tax on remittances; tax on hiring foreigners (K19) | Institut de l'Entreprise: 92% of the immigration block undocumented or legally fragile. Both "reserved benefits" lines are in category C (0% retained in its central case). Whole program: 7.5 bn credible in 2031 vs 141.7 shown (file 11) | Government: "for the most part unconstitutional" (Euronews, file 11) |

**Order-of-magnitude checks (our computation):**
1. **29.0 bn in 2031 = 0.81% of 2032 GDP** (file 11's 2032 GDP assumption). That is about the size of the *entire* OECD C2 estimate of immigrants' net contribution (-0.85% of GDP), and **more than the entire net contribution on any convention that excludes debt interest** (-0.53% or less negative). A package that only trims some benefits for some foreigners cannot plausibly save more than the whole net "cost" estimated under the least favorable convention. This is a consistency check, not a costing.
2. **The AME-to-AMU line (1.3 bn) is 97-108% of total AME spending (1.34 bn in 2025) or credits (1.208 bn for the AME action in 2027; programme 183 total 1.216 bn).** It assumes the AMU costs nothing, whereas emergency hospital care for the same people would continue: the *soins urgents* envelope alone is EUR 70 m, and hospitals would carry unpaid bills. The 2023 government-commissioned Évin-Stefanini report put AME spending at **EUR 968 m in 2022** and found that the scheme does not generate care consumption showing "*atypismes, abus ou fraudes structurelles*" (anomalies, abuse or structural fraud). It recommended adapting the AME, not replacing it. *(Verified 2026-10-25, index pass, in the primary report: Évin and Stefanini, *Rapport sur l'aide médicale de l'État*, December 2023, pp. 8 ff., https://www.vie-publique.fr/files/rapport/pdf/292122.pdf, saved by file 16 at `data/raw/16_factcheck/evin_stefanini_292122.pdf`. Was: "near EUR 1.2 bn", press figure, ⚠ primary not opened. The 1.2 bn for 2023 is a press figure only.)* In the PLF 2026 debate, the Senate voted a EUR 200 m cut together with tighter conditions *(⚠ Public Sénat, not re-verified in the final law. Note added 2026-10-25: the PAP 2027 shows LFI 2026 action 02 credits of 1,208.3 m, identical to the PLF 2026 amount in the Senate report, which suggests the 200 m cut was not kept in the final law; ⚠ to confirm against the LFI 2026 text.)*
3. **Benefit reservation, legal check.**
   - **Conseil constitutionnel, decision 2023-863 DC (25 Jan 2024):** article 19 of the 2024 immigration law (residence or work-duration conditions on several non-contributory benefits for non-EU foreigners) was struck down on procedure (§95-96, *cavalier législatif*, an amendment unrelated to the bill), without a ruling on substance.
   - **Decision 2024-6 RIP (11 Apr 2024):** on the LR shared-initiative referendum bill, the Council held **on substance** that 5 years' residence or 30 months of work for housing rights, housing aid, family benefits and the APA is a **"disproportionate infringement"** of the 1946 Preamble's solidarity requirements (§9-13). Foreigners "residing in a stable and regular manner" are entitled to social protection (§10). The Council left room for *some* duration condition (§12).
   - Hence the RN's insistence on a constitutional referendum.
   - EU law: Directive 2003/109/EC guarantees long-term residents (5 years) equal treatment in social security and social assistance, as cited by the Institut de l'Entreprise. The ECHR (European Convention on Human Rights, Art. 14 with Protocol 1) has also been invoked.
   - **Even with a constitutional amendment, EU-law and ECHR obstacles remain** (⚠ legal analysis: think tank and government statements, not a court ruling on the RN text).

### 6.2 Other candidates (for balance)
- **LR (B. Retailleau, 12 Oct 2026):** immigration **EUR 10 bn**. Public Sénat says "a very large part" of the planned savings is conditional on a constitutional referendum, and names two measures worth 4.5 bn (five years' residence and work before non-contributory benefits; asylum claims examined outside France) that depend on it. *(corrected 2026-10-25: was "of which 4.5 bn is conditional", which understates the conditional share as reported)* Not independently costed (file 11 [S8]).
- **Left programs:** no immigration-savings line was found in the costings reviewed in file 11.

### 6.3 What *could* be saved, and what could not (our assessment from the sources above)
- **Spending lines that are genuinely immigration-specific:**
  - AME 1.34 bn;
  - asylum reception and allowances (inside the Cour's 6.57 bn DPT scope in 2019);
  - removal policy 1.8 bn.
  - These total **about 0.2-0.3% of GDP** on the latest available figures (2019-2025; our computation from K14, K17, K18). The DPT alone is 0.22% of 2025 GDP (6.57 bn, 2019 scope) and about 0.26% on the 7.8 bn PLF 2026 figure (K17); a simple sum of the three lines (9.7 bn) would be 0.32%, but the scopes overlap: the AME is inside the DPT, and the extent to which the Cour's 1.8 bn removal cost is inside it is ⚠ not established. *(corrected 2026-10-25: was "under 0.3% of GDP", which holds only after netting overlaps that are not fully documented)*
  - Cutting them to zero is neither legal (asylum obligations) nor costless (*soins urgents*, public health).
- **Benefits paid to foreign residents** (RSA, family benefits, APL) are the only large pool. They are exactly the lines the *Conseil constitutionnel* has protected for stable legal residents.
- **No official source publishes the total amount of non-contributory benefits paid to foreign nationals** (⚠ data gap; see §10). That is the number a serious costing of "national priority" would need.

---

## 7. Divergences between sources

| Topic | Source A | Source B | Explanation |
|---|---|---|---|
| CEPII range | Working paper and OECD citation: "±0.5% of GDP" | *Lettre* 394: annual values "between -0.5% and +0.05%" | The ±0.5% is the authors' envelope; the observed annual values run from -0.49% (2011) to +0.05% (1989). Excluding 2011, the authors give ±0.2%. Both are faithful. File 14's "-0.5% to +0.5%" quotes the envelope (§9). |
| Sign: CEPII "mostly negative" vs CEPII 2011 "+3.9 bn in 2005" | 2018 accounting (primary balance, *immigrés*) | 2010-2011 Drees-MiRe work (general government, different scope and allocation) | Different allocations and perimeters. The 2018 study is the more recent and more transparent one. |
| OECD 2013 vs 2021 for France | IMO 2013 (2007-09 data) | IMO 2021 (2006-18) | Not re-verified here (⚠). Use 2021. |
| Cost of migration policies | Cour 2020 synthesis: **6.57 bn = 1.41%** of gross general-budget spending (2019, DPT) | Cour web page: "about 1.6% of the State budget, i.e. 6.6 bn" | Same amount, different denominator. Quote 6.57 bn (2019) and say "State spending on immigration and integration policies". |
| AME amount | PLF 2027 credits **1.208 bn** (AME action 02; programme 183 total 1.216 bn), 1.138 bn standard AME | Actual 2025 spending **1.340 bn** | Chronic under-budgeting (Senate: 117.8 m spent without budget in 2024; State debt to the CNAM 185 m). Use spending (1.34 bn) for "what the AME costs" and credits for "what is budgeted". |
| AME 2026 amount | Senate PLF 2026 report: 1,137.3 m for standard AME | Press (Oct 2026): "close to 1.4 bn in 2026" | The press figure is an unsourced spending forecast (⚠, not used). |
| Immigrant share | Insee: 11.6% *immigrés* (2025) | Eurostat: 14.0% foreign-born (2025) | Definitions: Eurostat counts French citizens born abroad (Insee: 14.0% "born abroad", identical). |
| RN immigration yield 2027 | Bardella/Public Sénat: "15 bn in 2027, 29 bn in a full year" | IdE: 15.1 (2027), 29.0 (2031) | Same numbers; "full year" = 2031 level. |

---

## 8. Where economists disagree (steelman both ways)

1. **"Immigrants are a net cost" (strongest version).**
   - On a full average-cost allocation, the foreign-born and their children are net negative in France (C2: -0.85%; with children: -1.41% of GDP).
   - Per head, they are worse than natives by about 2.8% of GDP per capita.
   - France performs worse than most OECD countries, and its relative position deteriorated in 2007-2017.
   - Lifetime (dynamic) studies elsewhere find that low-skilled non-EU migration can be net negative over the life cycle. The OECD summarizes the EU-wide JRC study (Christl et al., 2021) as finding non-EU migrants' lifetime contribution lowest relative to natives "in traditional welfare states".
   - Danish and Dutch government-backed lifetime studies point the same way for non-Western migrants (⚠ not re-verified in this session).
2. **"Immigrants are roughly neutral or positive" (strongest version).**
   - On the items an extra resident actually changes (individual and congestible spending), immigrants are net contributors in every OECD country, including France (+0.25% to +1.02%).
   - Charging debt interest on past deficits to recent arrivals is arbitrary.
   - Dynamic and macro studies (CEPII CGE 2011; d'Albis et al. 2018) find that immigration eases the cost of ageing and does not worsen the fiscal balance.
   - In the CEPII's words, immigration "never determined" France's primary deficit over 30 years.
3. **Points of agreement:**
   - The amounts are **small relative to the deficit** (5.1% of GDP in 2025, file 00 row 31) and to the native-born balance.
   - **Employment is the lever:** closing the immigrant employment gap is worth about +0.2% of GDP in France, mostly through women's employment.
   - The **composition** of immigration (age at arrival, skills, family vs labor migration) matters more than the numbers.
4. **Where the political debate departs from the evidence.** French respondents estimate the immigrant share at 28.8%, against 12.2% at the time of the survey (Alesina, Miano and Stantcheva, file 14 §7.5; the 12.2% is the UN 2017 foreign-born figure used by the authors, not Insee's *immigré* share, which was about 9.7% in 2017). Savings of EUR 15-29 bn are presented as low-hanging fruit, whereas the entire net contribution of immigrants is of that order only on the least favorable convention.

---

## 9. Notes on other files (not edited here)

| File | Statement | Status after this file's checks |
|---|---|---|
| 14 §7.5 | OECD France +1.02 / +0.25 / -0.85; -0.30 / -0.53; native -3.25 | **Confirmed** against StatLinks 1jovf5 and riasgf (re-downloaded 2026-10-25). |
| 14 §7.5 | CEPII "between -0.5% and +0.5% of GDP over 1979-2011" | **Precision suggested:** the authors' envelope is ±0.5% (±0.2% excluding 2011), but the observed annual values run from -0.49% to +0.05% (*Lettre* 394, Table 1). Suggested wording: "slightly negative, between -0.5% and +0.05% of GDP". |
| 11 / 07 | RN immigration 15.1 → 29.0; Montaigne 2024 8 bn "uncertain feasibility" | Consistent; the 18.1 bn reserved-benefit split (12.2 + 5.9) is now itemized here from the IdE primary note. |
| 14 §7.5 | "RN and LR claim immigration savings of EUR 8-15 bn a year, rising to 29 bn by 2031" | Consistent with K19 and §6.2. |

---

## 10. Open items (⚠ unverified)

- ~~⚠ **Évin-Stefanini report (4 Dec 2023):** figures taken from the press; primary PDF not opened.~~ **Resolved 2026-10-25 (index pass):** the primary report was found by file 16 (https://www.vie-publique.fr/files/rapport/pdf/292122.pdf; local `data/raw/16_factcheck/evin_stefanini_292122.pdf`). It confirms EUR 968 m of AME spending in 2022 and the "no structural abuse or fraud" finding. About 466,000 beneficiaries is an extrapolated end-2023 projection (file 16 §9), and "about EUR 1.2 bn" (2023) is press-only: do not use it; use the programme 183 annual performance report instead.
- ⚠ **Drees-MiRe 2010 report** (Chojnicki, Defoort, Drapier, Ragot, Rapoport): the +3.9 bn (2005) comes from CEPII *Lettre* 311, not from the report itself.
- ⚠ **JRC, Christl et al. (2021)** country values for France: the JRC PDF returned HTTP 403 (browser too); only the OECD's qualitative summary is used.
- ⚠ **OECD IMO 2013** France estimate (2007-09): not re-downloaded.
- ⚠ **PLF 2027 DPT "Politique française de l'immigration et de l'intégration"**: not retrieved (budget.gouv.fr bot protection; web-search quota exhausted). The latest verified figure is 6.57 bn for 2019. A 2027 update would modernize K17. *(Partly addressed 2026-10-25: the Senate's PLF 2026 opinion gives 7.8 bn for "credits allocated to immigration policies" (K17); the DPT annex itself is still ⚠ not opened. Recommendation: download the DPT annex from budget.gouv.fr via the laptop browser and replace both figures with the DPT's own 2025 executed / 2026 / 2027 totals.)*
- ⚠ **Higher private estimates** (e.g. by right-leaning associations or think tanks) were not retrieved, so no figure is quoted. If the platform cites one, it must state its convention (public goods, second generation, debt interest) and its orientation.
- ⚠ **Non-contributory benefits paid to foreign nationals** (RSA, APL, family benefits by nationality): no official aggregate found. CNAF/Drees data by nationality would be the basis for a costing of "national priority".
- ⚠ **PLF 2027 parliamentary amendments on the AME** (press reports of an October 2026 committee vote to halve AME credits): not verified on the Assemblée nationale site.
- ⚠ **Danish / Dutch lifetime studies:** cited qualitatively only.

---

## 11. Sources

| Code | Institution (orientation) | Title | Date | URL |
|---|---|---|---|---|
| O1 | OECD | *International Migration Outlook 2021*, ch. 4 "The fiscal impact of immigration in OECD countries since the mid-2000s" (Damas de Matos) | Oct 2021 | https://www.oecd.org/en/publications/international-migration-outlook-2021_29f23e9d-en/full-report/component-8.html |
| O2 | OECD StatLinks (xlsx, v1 28 Oct 2021) | Table 4.1; 4.2; 4.3; 4.6; Annex 4.A.3; 4.A.4; 4.A.7 | Oct 2021 | https://stat.link/1jovf5 ; https://stat.link/hsu5gq ; https://stat.link/xtnvok ; https://stat.link/v56fn7 ; https://stat.link/riasgf ; https://stat.link/d7pb0g ; https://stat.link/rxs4jb (local: `data/raw/15/oecd/`) |
| C1 | CEPII (public research center) | Chojnicki, Ragot, Sokhna, *L'impact budgétaire de 30 ans d'immigration en France : (I) une approche comptable*, WP 2018-04 | Apr 2018 | http://www.cepii.fr/PDF_PUB/wp/2018/wp2018-04.pdf |
| C2 | CEPII | *La Lettre du CEPII* no. 394, *L'impact sur les finances publiques de 30 ans d'immigration en France* | Dec 2018 | http://www.cepii.fr/PDF_PUB/lettre/2018/let394.pdf |
| C3 | CEPII | Chojnicki & Ragot, *La Lettre du CEPII* no. 311, *L'immigration peut-elle sauver notre système de protection sociale ?* | 15 Jun 2011 | http://www.cepii.fr/PDF_PUB/lettre/2011/let311.pdf |
| A1 | Academic | d'Albis, Boubtane, Coulibaly, "Macroeconomic evidence suggests that asylum seekers are not a 'burden' for Western European countries", *Science Advances* 4(6) eaaq0883 | Jun 2018 | https://www.science.org/doi/10.1126/sciadv.aaq0883 (abstract read at https://pmc.ncbi.nlm.nih.gov/articles/PMC6010334/) |
| I1 | Insee | *L'essentiel sur... les immigrés et les étrangers* | 25 Jun 2026 | https://www.insee.fr/fr/statistiques/3633212 |
| E1 | Eurostat | `migr_pop3ctb`, population by country of birth, 1 Jan | updated 25 Sep 2026 | https://ec.europa.eu/eurostat/databrowser/view/migr_pop3ctb/default/table |
| B1 | Direction du Budget / DSS | PLF 2027, *Projet annuel de performances*, programme 183 "Protection maladie" | 1 Oct 2026 | https://www.budget.gouv.fr/documentation/file-download/33907 (local: `data/raw/15/docs/FR_2027_PLF_SA_PGM_183.pdf`) |
| S1 | Senate, finance committee | *Rapport général* no. 139 (2025-2026), t. III annex 27 "Santé" (V. Delahaye) | 24 Nov 2025 | https://www.senat.fr/rap/l25-139-327/l25-139-3272.html |
| CC1 | Cour des comptes | *L'entrée, le séjour et le premier accueil des personnes étrangères* (report and synthesis) | 5 May 2020 | https://www.ccomptes.fr/fr/publications/lentree-le-sejour-et-le-premier-accueil-des-personnes-etrangeres ; synthesis https://www.ccomptes.fr/sites/default/files/2023-10/20200505-synthese-entree-sejour-premier-accueil-personnes-etrangeres_0.pdf |
| CC2 | Cour des comptes | *La politique de lutte contre l'immigration irrégulière* | 4 Jan 2024 | https://www.ccomptes.fr/fr/publications/la-politique-de-lutte-contre-limmigration-irreguliere |
| CO1 | Conseil constitutionnel | Decision 2024-6 RIP | 11 Apr 2024 | https://www.conseil-constitutionnel.fr/decision/2024/20246RIP.htm |
| CO2 | Conseil constitutionnel | Decision 2023-863 DC (immigration law) | 25 Jan 2024 | https://www.conseil-constitutionnel.fr/decision/2024/2023863DC.htm |
| P1 | Rassemblement national (party) | *Contre-budget 2026* | 24 Oct 2025 (PDF metadata) | https://rassemblementnational.fr/documents/GRN-CONTRE-BUDGET-2026.pdf (local: `data/raw/11_rn/`) |
| T1 | Institut de l'Entreprise (business-funded think tank) | *Contre-budget du RN : 140 milliards affichés, moins de 10 milliards crédibles*, note de contexte | 6 Oct 2026 | https://www.institut-entreprise.fr/wp-content/uploads/2026/10/Analyse-primaire-contre-budget-RN-Note-de-contexte-IDEP.pdf (local: `data/raw/11_verify2/ide_rn_note.pdf`) |
| T2 | Institut Montaigne (business-funded, liberal-centrist) | *Législatives 2024 – Chiffrage global des programmes* | 5 Jul 2024 | https://www.institutmontaigne.org/communiques-de-presse/legislatives-2024-chiffrage-global-des-programmes |
| N1 | Public Sénat (press) | "140 milliards d'euros d'économies d'ici 2032..." | 6 Oct 2026 | https://www.publicsenat.fr/actualites/politique/140-milliards-deuros-deconomies-dici-2032-leffort-radical-propose-par-marine-le-pen-pour-redresser-les-f |
| N2 | Public Sénat (press) | Retailleau, plan of about 200 bn of savings | 12 Oct 2026 | https://www.publicsenat.fr/actualites/economie/presidentielle-2027-bruno-retailleau-sengage-sur-un-plan-deconomies-de-pres-de-200-milliards-deuros-sil-est-elu |
| N3 | Banque des Territoires (press, ⚠) | "Aide médicale d'État : adaptable mais pas condamnable, selon le rapport Évin-Stefanini" | Dec 2023 | https://www.banquedesterritoires.fr/aide-medicale-detat-adaptable-mais-pas-condamnable-selon-le-rapport-evin-stefanini |
| L1 | EU | Council Directive 2003/109/EC (long-term residents), as cited by T1 (not opened) | 25 Nov 2003 | https://eur-lex.europa.eu/eli/dir/2003/109/oj |

---

## 12. Verification log (re-check of headline figures against primary sources, 2026-10-25)

| # | Headline figure | Primary source re-checked | Result |
|---|---|---|---|
| 1 | OECD France FB net contribution +1.02 / +0.25 / -0.85% of GDP; native -3.25 | StatLink 1jovf5 xlsx, rows FRA (cells 1.020, 0.253, -0.846; NB C2 -3.252) | **Confirmed** |
| 2 | Intermediate -0.30 / -0.53 | StatLink riasgf, row FRA (-0.299, -0.530) | **Confirmed** |
| 3 | With native-born children: +0.46 / -0.31 / -1.41 | StatLink hsu5gq, row FRA (0.459, -0.308, -1.406) | **Confirmed** |
| 4 | Per capita C2: FB -6.54, NB -3.74 (% of GDP pc) | StatLink d7pb0g, row FRA (-6.535, -3.735) | **Confirmed**; EUR conversion is our illustration |
| 5 | Employment-gap gain +0.22% | StatLink v56fn7, row FRA, Total 0.223 | **Confirmed** |
| 6 | Ranks: C2 21/25 OECD, 16/19 EU, 13/16 EA, 7/8 panel | `scripts/15/oecd_stats.py` on the StatLinks | **Confirmed** (recomputed; ties: none at France's value) |
| 7 | CEPII: -0.49% (2011) to +0.05%; -8.8 bn in 2011; second generation -1.0 to -1.6%; public goods to natives +0.02 to +0.55% | *Lettre* 394 text and Table 1 note; WP 2018-04 abstract (±0.5%, ±0.2% excl. 2011) | **Confirmed**; wording nuance logged in §7 and §9 |
| 8 | CEPII 2011: +3.9 bn (2005); zero immigration +1.3 pts of GDP financing need in 2050 | *Lettre* 311 text (p. 2 and abstract) | **Confirmed as reported by CEPII**; the underlying Drees-MiRe report not opened (⚠) |
| 9 | Immigrants 7.97 m = 11.6% (2025), series break 2024 | Insee page 3633212 (25 Jun 2026), table "Décomposition..." and warning | **Confirmed** |
| 10 | Women's employment rate 54% vs 69% | Same Insee page | **Confirmed** |
| 11 | AME PLF 2027 1,208.3 m (1,137.9 + 70 + 1); spending 2025 1,340 m; 454,111 beneficiaries | PAP 2027 programme 183 PDF (pp. 10-22) | **Confirmed.** Note: the components sum to 1,208.9 m vs 1,208.3 m shown, and the text says the "other AME" envelope is "reconduite pour 2026": apparently copied from the 2026 PAP. Logged as a source inconsistency (EUR 0.6 m). |
| 12 | Senate: 1,255 m actual 2024; 117.8 m unbudgeted; 185.1 m debt to the CNAM | Senate report page (WebFetch) | **Confirmed** |
| 13 | Cour 2020: 6.57 bn = 1.41% (2019) | Cour synthesis PDF, p. "Des dépenses croissantes" | **Confirmed** (web page says "about 1.6%, 6.6 bn": §7) |
| 14 | Cour 2024: about 1.8 bn a year, about 16,000 staff | Cour publication page (WebFetch, verbatim) | **Confirmed** |
| 15 | RN 2026: 11.9 bn = 6.1 + 1.3 + 1.0 + 1.3 + 1.11 + 1.1 | RN PDF annex, lines 184-189 (pdftotext) | **Confirmed** (sum 11.91) |
| 16 | RN 2027: 15.1 → 29.0; reserved benefits 12.2 + 5.9; 92% fragile | IdE note pp. 4-6 (table of contributors and the thirteen-line table) | **Confirmed**. *(Rationale corrected 2026-10-25: was "values and labels align one to one in the extracted text". They do not: from "Suppression ou réinternalisation d'agences" onwards, labels are offset by one line from values. Realigned by the "Motif" column and by the contributor table (electricity 9.3, CEE 8.0, cartels 5.8), the family-benefits line is 5.9, category C, "Condition de nationalité". The 12.2 + 5.9 = 18.1 split is also stated directly in the IdE contributor table, p. 4, and in its text, p. 5.)* |
| 17 | 2024-6 RIP: 5 years' residence / 30 months' work = "atteinte disproportionnée" | conseil-constitutionnel.fr decision text, §9-13 | **Confirmed** |
| 18 | 2023-863 DC: article 19 struck down as *cavalier* | conseil-constitutionnel.fr decision text, §95-96 | **Confirmed** (first 100,000 characters read; the relevant paragraphs are in that part) |
| 19 | Foreign-born share 14.0% (2025), panel 7/8, EU 15/26 | Eurostat API `migr_pop3ctb` (updated 25 Sep 2026); `scripts/15/eurostat_fb_share.py` | **Confirmed** (one EU country has no 2025 value, hence n = 26) |
| 20 | EUR conversions (30.5 / 7.6 / -25.3 bn; 1,200 EUR per head) | `scripts/15/convert_eur.py`; GDP 2025 = 1,714.1 / 0.573 (file 00 row 1) | **Arithmetic confirmed**; illustrative only (2006-18 ratios on 2025 GDP) |

---

## 13. Adversarial fact-check (2026-10-25, second pass)

*Method: every headline figure was re-derived independently from the primary source, not from the first pass's scripts or log. OECD and Eurostat values were recomputed with a fresh script (scratchpad, `python3 -I`) directly from `data/raw/15/oecd/*.xlsx` and `data/raw/15/eurostat/migr_pop3ctb.json`. PDFs and HTML were re-read (`p183.txt`, `let394.txt`, `let311.txt`, `wp.txt`, `cc2020s.txt`, `insee_3633212.html`, `11_rn/rn.txt`, `11_verify2/ide_rn_note.pdf` in layout mode). Web pages were re-fetched: Senate report l25-139-327, Cour des comptes 2024 page, Conseil constitutionnel 2024-6 RIP and 2023-863 DC, Public Sénat (12 Oct 2026), Institut Montaigne (curl, full sentence), Europe PMC abstract of d'Albis et al., and the OECD IMO 2021 ch. 4 full text (through the laptop browser, because the site returns HTTP 403 to scripts). New downloads: `data/raw/15/an/ppl238.pdf`, `data/raw/15/senat/a25-145-21.pdf`.*

| # | Claim attacked | Result | Action |
|---|---|---|---|
| A1 | OECD France FB +1.02 / +0.25 / -0.30 / -0.53 / -0.85; NB -3.25; with children +0.46 / -0.31 / -1.41; per capita -6.54 / -3.74; employment gap +0.22 (men 0.09, women 0.13); fiscal ratios 1.24 / 1.29, 0.88 / 0.93 (relative 0.94); relative ratio 0.96 (2007) → 0.90 (2017) | **Survives.** Every cell matches the StatLinks. Internal check: FB C2 + NB C2 = -4.10% of GDP = FB B + NB C1 (0.25 - 4.35), so the two contributions add up to one balance as stated. | none |
| A2 | All §5 means, medians and ranks (A, B, excl. defense and debt, excl. debt, C2, NB C2, per-capita gap; OECD-25 / EU-19 / EA-16 / panel-8) | **Survives.** Recomputed independently; all 28 mean/median pairs and all ranks reproduce. The EU-19 and EA-16 memberships are correct. | none |
| A3 | "OECD singles out France and the Netherlands" (§5.3); VAR on 19 OECD countries 1980-2015; JRC "traditional welfare states" | **Survives.** Verbatim in the OECD chapter: "Two other countries stand out, namely France and the Netherlands, but for showing a relative fall of the total fiscal ratio..."; "D'Albis, Boubtane and Coulibaly (2019) estimate a VAR model on a panel of 19 OECD countries for 1980-2015". | none |
| A4 | Bottom line 4: "The reasons are an older foreign-born population... and the women's employment gap" | **Overstated.** The OECD chapter gives no France-specific explanation. It only says that France's working-age share fell for both groups. The women's employment gap is supported by Table 4.6 (women +0.13 > men +0.09). | **Corrected** to "likely reasons (our reading)" |
| A5 | §3 synthesis: "between about +1% and -1.5% of GDP" | **Error.** The CEPII second-generation variant reaches -1.6% (*Lettre* 394). | **Corrected** to -1.6% |
| A6 | §6.3: immigration-specific lines "under 0.3% of GDP" | **Fragile.** A plain sum is 0.32%. The claim needs overlap netting that is only partly documented. With the 2026 figure (7.8 bn), the DPT alone is 0.26%. | **Corrected** to "about 0.2-0.3%", with the overlap flagged ⚠ |
| A7 | CEPII: -0.49% (2011) to +0.05%; -8.8 bn; second generation -1% to -1.6%, about -30 bn; public goods to natives +0.02% to +0.55%; ±0.5% / ±0.2%; "never determined" the primary deficit | **Survives** (*Lettre* 394 pp. 2-4 and Table 1; WP 2018-04 key points). | none |
| A8 | CEPII 2011: +3.9 bn (2005); +1.3 pts of GDP in 2050 | **Survives as reported.** The *Lettre* uses the conditional ("*serait positive*"). It is corroborated by WP 2018-04, which cites Chojnicki (2013) at +0.2% of GDP for 2005 (≈ 3.9 / about 1,770 bn). The Drees-MiRe report remains ⚠ unopened. | precision added to K11 |
| A9 | Insee: 7.97 m = 11.6%; 7.75 m = 11.3% (2024, series break); 6.3 m = 9.1%; 9.63 m = 14.0%; 1.66 m French born abroad; women 54% vs 69%; men 71-72%; unemployment 12-13% vs 7%; population 68.85 m | **Survives.** Every value matches the saved Insee page (published 25 Jun 2026). | none |
| A10 | Eurostat 14.0%, EU-27 aggregate 14.4%, 15th of 26 (PT missing), panel 7/8, median 18.0 | **Survives** (recomputed: 13.99%, 14.36%, rank 15/26; panel median 18.05). | none |
| A11 | PAP 2027: 1,208.3 m; 1,216.3 m; 1,340 m spent in 2025 on standard AME; +6% a year; 65% hospital; 454,111 (-2.4%), 465,208, 456,689, 202,503; 71% | **Survives.** The 1,340 m sits under the heading "*Bénéficiaires et dépenses de l'AME de droit commun*", so "standard AME" is correct. The 0.6 m component discrepancy is explained: the PLF 2026 split (Senate: 1,137.3 m) sums exactly to 1,208.3 m, so the PAP 2027's "1,137.9" is probably a typo. | note added to K13 |
| A12 | Senate: 1,159 m executed; 1,255 m actual; 117.8 m unbudgeted; 185.1 m debt to the CNAM; 1,314 m estimate for 2025 | **Survives** (verbatim). | none |
| A13 | Cour 2020: 6.57 bn = 1.41%, +48% vs 2012, asylum one-third, AME one-fifth | **Survives** (synthesis text). There is a newer figure: 7.8 bn for "credits allocated to immigration policies" in the PLF 2026 (Senate opinion no. 145, 24 Nov 2025). | update added to K17 (⚠ DPT itself not opened) |
| A14 | Cour 2024: 1.8 bn a year, 16,000 staff, 4 Jan 2024 | **Survives.** The page gives **no reference year**, so the K18 "about 2022" is unsupported. | ⚠ flag added to K18 |
| A15 | 2024-6 RIP (§9-13: 5 years / 30 months, "*atteinte disproportionnée*", room for some condition in §12); 2023-863 DC art. 19 censured as *cavalier* (§95-96) | **Survives** (verbatim). | none |
| A16 | RN 2026: 6.1 + 1.3 + 1.0 + 1.3 + 1.11 + 1.1 = 11.91 | **Survives** (RN PDF annex). | none |
| A17 | RN 2027 / IdE: 15.1 → 29.0; 92%; 12.2 + 5.9 = 18.1; both category C; 7.5 bn credible vs 141.7 | **Figures survive.** The first-pass rationale was wrong: the thirteen-line table is offset by one line, not aligned one to one. The 5.9 attribution is nonetheless confirmed by the realigned table and by the IdE contributor table and text. | log row 16 **corrected** |
| A18 | Montaigne 2024: RN 8 bn, "legal and political feasibility remains uncertain" | **Ambiguous attribution.** In the single source sentence, the feasibility clause follows "*privatisation de l'audiovisuel public (1,6 Md€)*" and may refer to that item only. | precision added (§6.1) |
| A19 | LR: 10 bn, "of which 4.5 bn conditional on a referendum" | **Understated.** Public Sénat says "*une très grande partie*" is conditional. The 4.5 bn covers the two measures it names. | **Corrected** (§6.2) |
| A20 | d'Albis et al., *Science Advances* 4(6), 20 Jun 2018, 1985-2015 | **Survives** (Europe PMC abstract, verbatim quote matches). | none |
| A21 | "28.8% perceived vs 12.2% actual" (§8.4) | **Survives as a citation.** The 12.2% is the authors' UN 2017 (foreign-born) benchmark, not Insee's *immigré* share (9.7% in 2017). | precision added |
| A22 | Euro conversions: GDP 2,991.4 bn, 43,448 per head; 30.5 / 7.6 / -25.3 / -42.1 / -97.3 bn; about 33 bn swing; 0.045% / 0.078%; 108% / 97%; 0.40%; 0.81% of 2032 GDP | **Arithmetic survives.** The 0.81% rests on file 11's own 2032 GDP assumption (3,582 bn), not an official forecast. | none (already labeled) |
| A23 | Évin-Stefanini (4 Dec 2023) | Date and authors **confirmed** by AN bill no. 238. The figures and the "no structural fraud" finding remain ⚠ press-only. | §10 updated |

**Still ⚠ unverified after this pass (recommendations):** ~~Évin-Stefanini figures (get the primary report)~~ (resolved in the index pass, see §10); Drees-MiRe 2010 report; DPT 2026/2027 totals (open the budget.gouv.fr annex in the laptop browser); K18 reference year (read the full Cour report); JRC Christl et al. country values; OECD IMO 2013; PLF 2027 AME amendments (check the AN amendment database); PLF 2026 Senate EUR 200 m AME cut in the final LFI 2026 (compare against the LFI programme 183 table, which shows the same 1,216.3 m as PLF 2027 and suggests the cut was not kept; ⚠ to confirm); overlap between the Cour's 1.8 bn and the DPT.
