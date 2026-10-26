# 20 - Pedagogical Approach: How to Explain French Public Finances Honestly

*Phase 2 deliverable. Written 2026-10-25. It builds on the research base (files 00-18; files 15-18 were integrated in the pass "sync with files 15-18" of 2026-10-25, and the corrections of the platform data review (`platform/data/REVIEW.md`) were applied in a later pass the same day; see the verification log). **Every number below comes from `00-reference-figures.md`** (the canonical file) **or from the topic file named in its footnote.** Where a topic file and file 00 differ, file 00 wins. Computed comparisons (days of spending, per inhabitant, share of the deficit) are reproduced in `data/20_pedagogical_conversions.csv`; the rows added in the 15-18 sync are computed inline in §3.4 (formula shown there) and are not yet in the CSV. Two surveys on public misperception were added in this phase (section 6.2); their raw PDFs are saved in `data/raw/20_perception/`.*

---

## 0. Summary for the editorial team

1. **One governing idea: "orders of magnitude, then trade-offs".** Each page first lets users *guess*, then shows the true size of an item next to a common yardstick, then sets out the choices and their costs. Every page also carries the strongest objection to its own message. The platform does not tell people what to think about fairness. It tells them how big things are.
2. **Four yardsticks used site-wide**, all computed from canonical figures:
   - **Days of public spending.** 2025 total expenditure (TE) was EUR 1,714.1 bn, so **one day of public spending = EUR 4.70 bn**.
   - **EUR per inhabitant.** TE was about **EUR 24,800 per person per year, or EUR 68 per person per day**.
   - **Share of the deficit.** The 2025 deficit was **EUR 151.6 bn = 32.3 days of spending**: from about **29 November**, everything is paid for with borrowed money.
   - **"France as a household".** Scaled to a household with **EUR 3,000 a month** of income, the State spends **EUR 3,291**, borrows **EUR 291 a month**, owes **EUR 79,700** and pays **EUR 126 a month** in interest.
3. **The flagship comparisons** (computation in section 3):
   - The *taxe Zucman* (Zucman tax) funds **0.4 to 4.3 days** of public spending, depending on whose estimate you take.
   - A plausible "tax the rich" package raises **EUR 10-25 bn**, or **2 to 5 days** of spending. That is **7-16% of the deficit**.
   - A general return to retirement at 60 costs **EUR 43-58 bn a year** (1.4-1.9 pt of GDP), or **9.2 to 12.4 days** of spending, **28-38% of the 2025 deficit**, **EUR 623-841 per inhabitant** and **EUR 83-111 a month** at household scale. *(Corrected 2026-10-25: was 35-58; the 35 had no source and is the top of the partial RN-type range. Bounds: Fipeco about 43, Institut Montaigne 58; file 00 row 44.)*
   - Interest on the debt rises by **EUR 25 bn between 2025 and 2027**. That is more than the most optimistic post-behavior yield of any single wealth tax.
   - The tax and contribution cuts decided in 2018-2023 cost **EUR 62 bn a year**, or **13 days** of spending. This is the steelman figure, and it appears on the same page.
4. **Six formats:**
   - (a) a scrollytelling "budget year" calendar;
   - (b) a "guess the order of magnitude" quiz built on *documented* misperceptions;
   - (c) a "balance the budget yourself" simulator with ranges, behavioral toggles and a macro-feedback (fiscal multiplier) toggle: at the official working value of about 0.6, EUR 1 of measures improves the deficit by about EUR 0.66 in year 1 (§5.4);
   - (d) a "your taxes receipt" calculator;
   - (e) country comparison sliders;
   - (f) a proposal checker that converts any campaign promise into days, percent of deficit and EUR per inhabitant.
5. **Credibility is the product.** About 87% of French people think public money is badly used and 87% that the State is not transparent about it (Elabe for BFMTV, fieldwork 2-3 Dec 2025, n = 1,000; verified in file 14 [S7])[^f14]. The platform must therefore show its machinery:
   - a source chip on every number;
   - ranges instead of point estimates where experts disagree;
   - think-tank orientation labels;
   - a public changelog;
   - a symmetric treatment of left-wing and right-wing "easy money" claims (wealth taxes and business aid; fraud, immigration, the EU contribution, development aid and "the State's running costs");
   - a right of reply for campaigns.
6. **New evidence found in this phase.** File 14 found **no French 2023-2026 poll that asks people to estimate a budget number**. One earlier poll does exist: Ipsos (fieldwork 18-21 January 2021, n = 1,000), commissioned by the Ministry of the Economy and Finance (MINEFI) for the Prime Minister's *Commission sur l'avenir des finances publiques* (commission on the future of public finances, chaired by Jean Arthuis) and published as attachment 4 of its report (verified 2026-10-25; was "apparently prepared for … (link to be confirmed)"). It found that French adults put public debt at **76% of GDP on average**, when it was about 98% (end-2019) to 115% (end-2020). **37% could not answer**, and **73% said they felt poorly informed** about the debt. A Toluna-Harris Interactive poll for Observatoire Hexagone (online, 21-24 February 2025, n = 1,101) (a think tank that favors adding a funded pension pillar) found that **47% think retirees have a lower living standard than the population average**. The COR puts retirees at **100.2%** of the average. The quiz is built around these documented gaps, and the platform should run its own numeric-estimate survey (section 6.4).
7. **Added in the sync with files 15-18 (2026-10-25).**
   - **"Easy savings" targets** (§4.16, levers S13-S19): even abolished outright, the net EU contribution, the development-aid mission, the *Pouvoirs publics* mission, public broadcasting, all State payments to associations, AME and strategy consulting add up to **about EUR 29 bn = 6.3 days of spending = 19% of the 2025 deficit** (file 16 §0). Realistic yields are far smaller (agencies: EUR 0.54 bn according to the Senate).
   - **EU contribution:** France's verified net contribution in 2025 is **EUR 9.5 bn** (accounting method) or **EUR 6.4 bn** (Commission operating balance). A EUR 5 bn cap would save **at most EUR 1.4-4.5 bn even if it were legal**, against the EUR 11.1 bn claimed for 2027 (§4.10).
   - **Immigration and AME** (§4.15): the foreign-born's net fiscal contribution is **+1.02% to -0.85% of GDP a year** depending on the accounting convention (OECD); standard AME spending was **EUR 1.34 bn in 2025** (EUR 968 m in 2022 per the Évin-Stefanini report).
   - **Macro feedback** (§5.4): multiplier defaults by instrument, with bands, from file 17.
   - **Methodology page** (§4.17): the three measurement bridges of file 18 (PO vs OECD tax-to-GDP, the three interest figures, COFOG vs SHA health).

---

## 1. Pedagogical principles

| # | Principle | What it means in practice | Why (evidence) |
|---|---|---|---|
| P1 | **Guess before you see** | Each chapter opens with an estimate question (slider). The answer then appears next to the user's guess and the crowd's guess. | Information experiments show that facts move *beliefs* much more than *preferences*. The biggest effects come when people's priors are badly wrong[^kns][^ciani]. Asking for a guess first makes the gap visible to the user. |
| P2 | **One yardstick per page, always the same four** | Days of spending, EUR per inhabitant, % of deficit, household scale. Never switch units without a conversion. | Users cannot compare "EUR 20 bn" with "0.7% of GDP". The yardsticks are computed once in `data/20_pedagogical_conversions.csv`. |
| P3 | **Label the denominator** | "% of GDP" (size of the economy) and "% of total public expenditure" (share of the budget) never appear unlabeled. Each chart axis says which one it uses. | Rankings flip with the denominator. The wage bill is 6th of 27 in % of GDP and 22nd of 27 in % of TE[^f04]. |
| P4 | **Steelman on the same screen** | Every key message has a "The strongest objection" box with a source. The box is not hidden in a footnote. | The platform must be hard to discredit (file 10 §14). |
| P5 | **Separate fairness from sufficiency** | "Should the very rich pay more?" is a value question; the platform does not answer it. "Would it balance the budget?" is a factual question; the platform answers it with ranges. | Support for wealth taxes is driven mainly by fairness views[^stantcheva]. Calling such support a "misperception" is a category error (file 14 §7.8). |
| P6 | **Ranges, not points** | Contested figures appear as a band (low, central, high), with the authors named. | The Zucman tax is costed at EUR 2-25 bn. The ex ante yield of the CDHR was overestimated three to four times (file 07). |
| P7 | **Symmetry test** | Every "easy money" claim gets the same orders-of-magnitude treatment, whichever side makes it: wealth tax and business aid (left), fraud, immigration, the EU contribution and "State running costs" (right). | Misperceptions run both ways (file 14 §7). A one-sided platform will be read as partisan, and readers discount partisan sources[^douenne]. |
| P8 | **Outcomes next to inputs** | Each spending chapter ends with "What do we get for it?", using one outcome indicator per function compared with the same country panel. | The thesis is about *structure* and *efficiency*, not size alone (file 04 §7). |
| P9 | **Name the base year** | Any "since 2017" or "since 2019" claim shows both windows. | The base year decides whether the deficit looks revenue-driven or spending-driven (file 10 §4). |
| P10 | **No "economists agree" without a survey** | Write "the Cour des comptes, the HCFP and the HCSP estimate that…", or "X and Y argue that…". | No representative survey of French economists exists (file 14 §5). |

---

## 2. Site architecture and user journey

### 2.1 Information architecture

```
Home ("How well do you know France's budget?": 3-question teaser quiz)
│
├── 1. THE STORY (scrollytelling, 7 chapters, about 7 to 9 minutes per chapter)
│   ├── Ch.1 How much? (French title « Combien ? », as in the chapter file; spending overview, Europe comparison)
│   ├── Ch.2 Where does it go? (the budget calendar, the 1,000 EUR breakdown, COFOG functions)
│   ├── Ch.3 Who pays? (taxation, your taxes receipt)
│   ├── Ch.4 Why the deficit? (tax cuts vs spending drift, both base years)
│   ├── Ch.5 Debt and interest (the household view, interest vs education and defense)
│   ├── Ch.6 What do we get? (outcomes: poverty, health, education, justice)
│   └── Ch.7 The choices (ageing, employment, the size of the adjustment)
│
├── 2. TOOLS
│   ├── Balance the budget yourself (simulator)
│   ├── Proposal checker (any measure → days, % deficit, EUR per inhabitant)
│   ├── Your taxes receipt
│   ├── Compare with Europe (country slider, indicator picker)
│   └── The full quiz (25 questions, shareable score)
│
├── 3. TOPIC PAGES (one per subject in section 4; each is self-contained and SEO-targeted)
│
├── 4. 2027 PROGRAMS (one card per candidate, same template, right-of-reply box)
│
└── 5. TRUST CENTER
    ├── Methodology (concepts: ESA vs budget accounting, PO vs tax-to-GDP, the three interest figures, COFOG vs SHA vs Drees CPS, PPS, static vs behavioral vs macro costing: see §4.17 and §4.18)
    ├── Sources and data downloads (all CSVs, versioned)
    ├── Debates (the strongest counter-arguments, with authors and orientations)
    ├── Editorial charter, funding, team, scientific committee
    └── Changelog and corrections
```

### 2.2 User journeys (personas)

| Persona | Entry point | Path | Time budget | Success metric |
|---|---|---|---|---|
| Curious citizen on a phone, arriving from a social post | A shared quiz card (for example, "I guessed the Zucman tax pays for 30 days of spending. It's 0.4 to 4.3.") | Teaser quiz → Ch.2 calendar → proposal checker | 3-5 min | Finishes the quiz, opens one topic page |
| Engaged voter during the 2027 campaign | Search for "chiffrage programme Le Pen / Mélenchon / Retailleau" (the French phrase for a program costing) | Program card → proposal checker → simulator | 10-20 min | Builds a scenario, shares it |
| Teacher or student (SES, lycée economics and social sciences) | A "Classroom kit" link from the Trust center | Story → quiz in class mode (anonymous group results) → simulator worksheet | One 55-minute lesson | Downloads the kit |
| Journalist or fact-checker | A direct link to a number card, or a CSV | Topic page → source chip → data download | 2 min | Cites the number with its source |
| Skeptic who suspects bias | "Who funds you?" | Trust center → Debates page → changelog | 5 min | Finds the counter-arguments presented fairly |

### 2.3 Shared components (build once, reuse everywhere)

| Component | Content | Notes |
|---|---|---|
| **Number card** | Value, unit, denominator, data year, source chip, "why this differs from X" link | Never shows a figure without its year and denominator |
| **Source chip** | Institution, dataset or report, publication date, deep link, vintage, link to the CSV | Expands on tap. It shows "superseded" when a newer vintage exists |
| **Yardstick converter** | Any EUR bn → days of TE, % of deficit, % of TE, % of GDP, EUR per inhabitant | Constants from file 00, versioned (section 9) |
| **Steelman box** | "The strongest objection", with author, orientation label and source | Mandatory on each key-message page |
| **Range bar** | Low, central and high estimates, with authors named at each end | Used for every contested costing |
| **Outcome strip** | One outcome indicator, France vs EU-27 and the panel | Bottom of each spending page |
| **Country slider** | Pick an indicator and a year; France is highlighted against EU-27, EA21, OECD and the panel (DE, IT, ES, NL, BE, SE, DK) | Shows the mean, the median and France's rank |

---

## 3. The yardstick toolkit (computed once, used everywhere)

### 3.1 Constants

| Constant | Value | Computation | Source |
|---|---|---|---|
| One day of public spending (2025) | **EUR 4.70 bn** | 1,714.1 / 365 | TE 2025[^ref] |
| Public spending per inhabitant | **EUR 24,843 per year; EUR 68.1 per day** | 1,714.1 bn / 68.998 m inhabitants; ÷ 365 | TE[^ref]; population, file 01 K9 |
| Deficit in days | **32.3 days**; from about **29 November**, spending is financed by borrowing | 151.6 / 4.696 | Deficit 2025[^ref] |
| Deficit per second (illustrative) | **about EUR 4,800 per second** | 151.6 bn / (365 × 86,400) | Deficit 2025[^ref]. Caveat: the deficit is not the same as the change in debt (stock-flow adjustments) |
| Share of TE financed by borrowing | **8.8%, about 1 euro in 11** | 151.6 / 1,714.1 | file 00 row 32[^ref] |
| Debt per inhabitant | **EUR 50,065** | 3,460.1 bn / 69.11 m (population on 1 Jan 2026) | file 00 row 35[^ref] |
| Debt / total revenue | **2.2 years of revenue** | 3,460.1 / 1,562.5 | Debt and TR 2025[^ref] |
| Interest / total revenue | **4.2%** | 65.7 / 1,562.5 | file 06 §3.3[^f06] |
| *Prélèvements obligatoires* (compulsory levies) per inhabitant | **EUR 18,915** | 1,305.1 bn / 68.998 m | PO 2025[^ref] |
| One point of GDP (2025) | **about EUR 30 bn** (EUR 29.9 bn) | 2,991.1 bn × 1% | GDP 2025, file 16 header and file 17 §0 (1,714.1 / 0.573)[^f17] |
| Macro-feedback rule (year 1) | **net deficit improvement = measure × (1 − m × 0.57)**; at the official mixed-package value m ≈ 0.6: **× 0.66** | 1 − 0.6 × 0.57 = 0.658 | m: 00 row 62 (HCFP-2026-5 §36); 0.57: CAE Focus 108 semi-elasticity[^f17] |

### 3.2 "France as a household" (scale factor = EUR 36,000 / EUR 1,562.5 bn of revenue)

| Item (2025) | National value | Household with EUR 3,000/month income | Source |
|---|---|---|---|
| Income (total government revenue, ESA) | 1,562.5 bn | **3,000 / month** | [^ref] row 29 |
| Spending | 1,714.1 bn | **3,291 / month** | [^ref] row 1 |
| Borrowing | 151.6 bn | **291 / month** | [^ref] row 31 |
| Stock of debt | 3,460.1 bn | **79,700** (2.2 years of income) | [^ref] row 35 |
| Interest | 65.7 bn | **126 / month** (4.2% of income) | [^ref] row 39 |
| Pensions (COR scope) | 422.2 bn | **811 / month** | [^ref] row 16 |
| Health insurance (ONDAM executed) | 265.4 bn | **510 / month** | file 02 row 23[^f02] |
| Defense (military programming law, LPM, budget accounting) | 51 bn | **98 / month** | file 06 row 21[^f06] |

**Mandatory steelman box: "A State is not a household."**
- A State does not retire, and its income (the tax base) grows with nominal GDP. A debt ratio can be stable with a permanent deficit: in 2025 the Cour des comptes put the debt-stabilizing primary balance at about +0.1% of GDP[^cour26].
- The government also owns assets. Public non-financial assets were EUR 2,945 bn and net worth was **+EUR 750 bn** at end-2025[^f08].
- Part of the debt finances investment. Gross public investment was 4.4% of GDP in 2025, but **net investment was only 0.6%** (rank 23/27)[^f08].
- **Where the analogy holds:** interest is a fixed charge that crowds out other spending, and lenders can raise the price. The 10-year OAT averaged 4.44% in September 2026, 97 bp above the Bund[^ref].

### 3.3 The budget calendar (COFOG 2024, % of TE spread over the year from 1 January)

| Function | % of TE | Days | "Paid from … to …" | Source |
|---|---|---|---|---|
| Social protection excl. health (pensions, family, unemployment, RSA, housing benefits) | 41.5 | 151.5 | 1 Jan → 30 May | Eurostat COFOG[^cofog] |
| of which old age (pensions, elderly care) | 23.4 | 85.4 | (1 Jan → 26 Mar) | [^cofog] |
| Health | 15.6 | 56.9 | 31 May → 26 Jul | [^cofog] |
| General public services (incl. interest 3.5% ≈ 12.8 days) | 10.8 | 39.4 | 27 Jul → 4 Sep | [^cofog] |
| Economic affairs (incl. transport) | 9.9 | 36.1 | 5 Sep → 10 Oct | [^cofog] |
| Education | 8.9 | 32.5 | 11 Oct → 12 Nov | [^cofog] |
| Defense | 3.2 | 11.7 | 13 Nov → 24 Nov | [^cofog] |
| Public order and safety (police, justice, prisons) | 3.1 | 11.3 | 25 Nov → 5 Dec | [^cofog] |
| Recreation, culture, religion | 2.6 | 9.5 | 6 Dec → 14 Dec | [^cofog] |
| Housing and community amenities | 2.5 | 9.1 | 15 Dec → 24 Dec | [^cofog] |
| Environmental protection | 1.8 | 6.6 | 25 Dec → 30 Dec | [^cofog] |

*Computed on 366 days (2024). 2025 COFOG data are not yet published: Insee's 2025 tables are due in December 2026 and Eurostat's around February 2027 (file 01 §4.1). The deficit overlay (8.8% of TE ≈ 32 days, from about 29 November) uses 2025 data and is labeled as such.*

**Design idea.** A horizontal year-long ribbon that fills day by day as the user scrolls. A red "borrowed money" band covers the last 32 days. A second ribbon lets the user drag a proposal (for example, the Zucman tax) onto the calendar to see how many days it covers.

### 3.4 Master conversion table for proposals and big items

Source: `data/20_pedagogical_conversions.csv` (computed from canonical values; days = EUR bn / 4.696).

| Item | EUR bn / yr | Days of 2025 spending | % of 2025 deficit | EUR per inhabitant | Source |
|---|---|---|---|---|---|
| Zucman tax, Senate low (corporate tax credited) | 2 | 0.4 | 1.3% | 29 | file 07 §3.1[^f07] |
| Zucman tax, critics after behavior | 5 | 1.1 | 3.3% | 72 | [^f07] |
| Zucman tax, author's static central | 20 | 4.3 | 13.2% | 290 | [^f07] |
| Plausible tax-the-rich package (post-behavior) | 10-25 | 2.1-5.3 | 6.6-16.5% | 145-362 | file 07 §5[^f07] |
| Restoring the ISF (gross) | 3-4.5 | 0.6-1.0 | 2-3% | 43-65 | [^f07] |
| CDHR (20% minimum tax on top incomes), observed 2025 | 0.4 | 0.1 | 0.3% | 6 | [^f07] |
| New anti-fraud plan, realistic marginal yield | 1-3 | 0.2-0.6 | 0.7-2% | 14-43 | [^f07] |
| *Année blanche* (one-year freeze of pensions, benefits and tax brackets) | 4.4-5.7 | 0.9-1.2 | 2.9-3.8% | 64-83 | [^f07] |
| +1 pt on all VAT rates (net) | 8.2 | 1.7 | 5.4% | 119 | [^f07] |
| Return to 60 (general, from 64) | 43-58 (cost; corrected 2026-10-25, was 35-58) | 9.2-12.4 | 28-38% | 623-841 | file 03 §4.1[^f03]; 00 row 44[^ref] |
| Tax and contribution cuts decided 2018-2023 | 62 (cost) | 13.2 | 40.9% | 899 | Cour des comptes[^cour24] |
| Interest 2025 (ESA D.41) | 65.7 | 14.0 | 43.3% | 952 | [^ref] |
| Rise in interest, 2025 → 2027 | 25.3 | 5.4 | 16.7% | 367 | [^ref] rows 39-40 |
| Gap to the debt-stabilizing balance (2025) | 89.6 | 19.1 | 59.1% | 1,299 | Cour des comptes[^cour26] |
| Employment rate aligned on Germany (FTE, DG Trésor) | +38 levies | 8.1 | 25.1% | 551 | file 08 row 17[^f08] |
| Spending gap with the euro area (EA21) | 227 | 48.3 | 150% | 3,290 | [^ref] row 7 |
| Pensions (COR scope) | 422.2 | 89.9 | 279% | 6,119 | [^ref] row 16 |

**Rows added in the sync with files 15-18 (2026-10-25).** Computed here, not yet in the CSV: days = EUR bn / 4.696; % of deficit = EUR bn / 151.6; EUR per inhabitant = EUR bn × 1,000 / 68.998. Budget figures for 2026-2027 are set against 2025 denominators, so they are orders of magnitude (file 16 header).

| Item | EUR bn / yr | Days of 2025 spending | % of 2025 deficit | EUR per inhabitant | Source |
|---|---|---|---|---|---|
| Net EU contribution 2025, accounting / Commission operating balance | 9.5 / 6.4 | 2.0 / 1.4 | 6.3% / 4.2% | 138 / 93 | 00 row 52[^ref]; file 16 §3[^f16] |
| "Cap the EU contribution at EUR 5 bn": RN claim (2027) | 11.1 | 2.4 | 7.3% | 161 | file 07; file 11 §4[^f11] |
| Same: maximum saving even if legal (6.4 − 5; 9.5 − 5) | 1.4-4.5 | 0.3-1.0 | 0.9-3.0% | 20-65 | 00 log #31[^ref]; file 16 §3.3[^f16] |
| Official development assistance (OECD-DAC, 2025; not a budget line) | 12.9 | 2.7 | 8.5% | 187 | 00 row 53[^ref] |
| Budget mission *Aide publique au développement* (PLF 2027, payment credits) | 3.17 | 0.7 | 2.1% | 46 | file 16 §2[^f16] |
| State medical aid (AME), standard AME spending 2025 | 1.34 | 0.3 | 0.9% | 19 | 00 row 54[^ref]; file 15 K14[^f15] |
| AME → emergency-only care (AMU), RN 2026 claim | 1.3 | 0.3 | 0.9% | 19 | file 15 K20 (= 97% of 2025 AME spending)[^f15] |
| Net fiscal contribution of the foreign-born (OECD 2006-18 ratios applied to 2025 GDP, illustrative): +1.02% to -0.85% of GDP | +30.5 to -25.3 | +6.5 to -5.4 | +20% to -17% | +442 to -367 | 00 row 55[^ref]; file 15 §4[^f15] |
| RN immigration block, claimed (2027 → 2031) | 15.1 → 29.0 | 3.2 → 6.2 | 10.0% → 19.1% | 219 → 420 | file 15 K19[^f15] |
| State operators, total public funding (PLF 2027; a channel for universities, research, employment, not overhead) | 72.6 | 15.5 | 47.9% | 1,052 | file 16 §4[^f16] |
| Agencies reform: Senate realistic saving / government 2025 claim (method not shown) | 0.54 / 2-3 | 0.1 / 0.4-0.6 | 0.4% / 1.3-2.0% | 8 / 29-43 | file 16 §4[^f16] |
| Strategy and organization consulting, State budget 2025 | 0.06 | 0.01 | 0.04% | 0.9 | file 16 §5[^f16] |
| *Pouvoirs publics* mission + ministerial cabinets' gross pay | 1.3 | 0.3 | 0.9% | 19 | file 16 §6[^f16] |
| Public broadcasting grant (PLF 2027) | 3.82 | 0.8 | 2.5% | 55 | file 16 §7[^f16] |
| State payments to associations (2025) | 10.5 | 2.2 | 6.9% | 152 | file 16 §8[^f16] |
| All the "easy targets" above at full gross value (EU net 9.47 + APD 3.17 + *Pouvoirs publics* 1.16 + broadcasting 3.82 + associations 10.50 + AME credits 1.22 + consulting 0.06) | 29.4 | 6.3 | 19.4% | 426 | file 16 §0, §13 #15[^f16] |
| Social fraud, estimated losses (not a recoverable yield) | 13-14 | 2.8-3.0 | 8.6-9.2% | 188-203 | 00 row 59[^ref] |
| Interest: general government (ESA, 65.7) minus State budget debt charge (51.6), 2025 | 14.1 | 3.0 | 9.3% | 204 | file 18 §2.5[^f18] |

---

## 4. Subject-by-subject pedagogical cards

Each card has the same five parts: **Key message** (honest, non-partisan), **Steelman on the same page**, **Tangible comparisons** (computation shown), **Format**, **Data needed (file / source)**.

### 4.1 Spending overview (size of government)

| Part | Content |
|---|---|
| **Key message** | "France spends **57.3% of GDP** in public money (EUR 1,714 bn in 2025), the **2nd-highest ratio in the EU-27** after Finland (2024 and 2025). It was 1st every year from 2014 to 2023. In 2025 the gap with the euro-area aggregate (**EA21**) is **7.6 points of GDP, about EUR 227 bn a year** (EA20: 7.5 pp, 225 bn). In the latest functional breakdown (COFOG **2024**, gap 7.8 pp vs EA21), about **two-thirds** of the gap is social protection plus health; old age (mainly pensions) alone accounts for **about one-third** (+2.5 pp)."[^ref] *(Clarified 2026-10-25: the two-thirds/one-third split is the 2024 COFOG decomposition, not the 2025 gap; file 00 rows 7-9.)* |
| **Steelman (same page)** | (1) **Per inhabitant in purchasing power, France is not an outlier.** It ranks **8th of 27 (23,330 PPS)**, below Luxembourg, Austria, Belgium, Denmark, the Netherlands, Germany and Finland, and tied with Sweden. Part of the high ratio reflects a GDP per head that is below the EU-27 level (40,716 vs 41,774 PPS, 12th of 27)[^ref][^f09]. (2) **Public vs private financing:** OECD net total social spending (public plus private, after tax) puts France at **32.0% of GDP vs the US at 33.2%** (2021, latest SOCX net year; France 2nd of 38)[^ref]. Our answer, on the same screen: against the European panel France is still first (32.0% vs a panel mean of 26.9%) (file 10 §3). (3) The ratio is **not** "the share of GDP spent by the State": transfers are not part of GDP (file 01 §1). |
| **Tangible comparisons** | **EUR 68 per inhabitant per day** (1,714.1 bn / 68.998 m / 365). **"For every EUR 1,000 of public spending in 2024, about 460 went to pensions and health, 89 to education, 35 to debt interest and 32 to defense"** (Fipeco/Insee grouping, file 01 §4.2). **The euro-area gap of EUR 227 bn equals 48 days of spending**, or about 1.5 times the 2025 deficit. |
| **Format** | Opening animation: a stack of 57 coins out of 100 (GDP) morphs into a bar chart of the EU-27 with France highlighted. A toggle switches "% of GDP" ↔ "PPS per inhabitant" and France slides from 2nd to 8th, which makes the steelman visual. Then a line chart of France's gap vs EA21 (1995-2025: +2.9 → +10.4 peak in 2017 → +7.6) with the 2008, 2020 and 2022 shocks annotated. |
| **Data** | `data/09_intl_fr_gap_timeseries.csv`; `data/eurostat_gov_10a_main.csv`; `data/eurostat_nama_10_pc_gdp_pps_per_capita.csv`; `data/09_intl_country_values_latest.csv`; `data/oecd_socx_totals.csv`; file 01 §4.2 (EUR 1,000 table). |

### 4.2 Each COFOG function

General rule: show **% of TE** (budget priority) **and** % of GDP (international comparison), the France minus EA21 gap, and one outcome. COFOG figures are 2024 (latest available). Source for every row: Eurostat `gov_10a_exp` (21 Oct 2026)[^cofog]; gaps from file 09 §3.2[^f09]; outcomes from the topic file named.

| COFOG | % of TE / % of GDP (2024) | Gap vs EA21 (pp GDP; EUR bn) | Key message | Steelman / nuance on the same page | Tangible comparison | Outcome strip | Format |
|---|---|---|---|---|---|---|---|
| **GF01 General public services** (incl. interest) | 10.8% / 6.2% | +0.1 (≈2) | "The 'bureaucracy' people want to cut is not where France's spending gap is." Excluding interest, GF01 = 4.2% of GDP vs EU-27 aggregate 4.1% (rank 10/27)[^f04] | COFOG spreads administrative staff across all functions, so "administration" in a broad sense is larger than GF01 (file 09 §3.2) | 67% name the "State's running costs" (*train de vie de l'État*) as a top lever[^elabe26]. GF01 excluding interest is about 7% of TE (10.8 − 3.5); the whole GF01 = **39 days** of spending, of which interest is 13 | World Bank government effectiveness, well below its 2005 level (file 04 §6.6) | "Where is the bureaucracy?" treemap with a drill-down |
| **GF02 Defense** | 3.2% / 1.8% (corrected 2026-10-25: was 1.9%; file 00 row 15, raw 1.85% rounded to 1.8 site-wide) | +0.5 (≈14) | "Defense is small in the budget (11.7 days), but it is the item that must grow." LPM: 51 → 57 → 63 bn (2025-2027)[^f06] | Reaching NATO's 3.5% "core defense" target means **about +EUR 44 bn a year** at 2025 GDP[^f08] | In budget accounting, the State's **interest bill in 2027 (EUR 72.9 bn) exceeds the LPM envelope (EUR 63 bn)** and roughly equals the whole Defense mission including pensions (73.9)[^f06] | n/a (no outcome indicator; show NATO % of GDP) | Side-by-side bars: "interest vs defense", 2025-2027 |
| **GF03 Public order and safety** | 3.1% / 1.8% | +0.1 (≈2) | "Justice is under-resourced by European standards." | Judge counts depend on the judicial model (lay judges, clerks); show prosecutors once collected (gap, file 04 §10) | **11.2 judges per 100,000 inhabitants vs an EU median of 17.1** (18th of 26); first-instance civil cases take 434 days[^f04] | Homicide 1.28 per 100,000 vs EU median 0.85 (22nd of 27, 1 = lowest)[^f04] | Small-multiples bar chart of judges per 100,000 |
| **GF04 Economic affairs** | 9.9% / 5.7% | +0.4 (≈13) | "Business support and transport." Link to §4.12 (business aid) *(corrected 2026-10-25: was "§4.14")* | 2024 numbers are distorted by a local-accounting nomenclature change (Insee warning, file 01 §4.1) | Transport 3.6% of TE = 13 days | Public net investment 0.6% of GDP, 23rd of 27[^f08] | Treemap drill-down |
| **GF05 Environment** | 1.8% / 1.0% | +0.2 (≈5) | "Small today; the climate transition needs EUR 25-34 bn a year of extra public money by 2030." | Pisani-Ferry and Mahfouz is a 2023 estimate (France Stratégie); update it when the HCSP refreshes it[^f08] | 6.6 days of spending today; the climate need is 5-7 more days | n/a | "Upward pressures" panel (with defense and ageing) |
| **GF06 Housing and community amenities** | 2.5% / 1.4% | +0.7 (≈21) | "A visible gap, partly an accounting artifact in 2024." | Insee: the +18% jump in 2024 is partly a nomenclature change[^f01] | 9 days | n/a | Footnoted bar |
| **GF07 Health** | 15.6% / 8.9% | +1.5 (≈43) on COFOG; +1.06-1.10 on SHA HF.1 (file 18 §3.3). Website wording: "1 to 1.5 points of GDP above the euro area, depending on the definition" (00 log #35) | See §4.5 | See §4.5; the COFOG vs SHA bridge is on the methodology page (§4.17) | 57 days | Treatable mortality, 3rd lowest in the EU | See §4.5 |
| **GF08 Recreation, culture, religion** | 2.6% / 1.5% | +0.3 (≈10) | "Culture is 2.6% of the budget." 22% of people would cut it first[^elabe26] | n/a | 9.5 days | n/a | Quiz item |
| **GF09 Education** | 8.9% / 5.1% | +0.5 (≈13) | "Average money, below-average and falling results." | Teachers are paid **about 18% below the OECD/EU average** at 15 years (lower secondary); spending is skewed toward upper secondary. "More money" and "better use" are both defensible readings[^f04] | 32.5 days. Interest in 2025 (65.7) = **44% of 2024 education spending** (148.6). PLF 2027, same accounting basis: State interest (72.9) = **80%** of the school-education mission (91.1)[^f06] | **PISA 2025 maths 458 vs OECD 463**, 29th of 38; -35 points since 2015; TIMSS grade-4 maths last of 22 EU entities[^f13] | Scatter: spending per student vs PISA 2025 (r = 0.24), France highlighted |
| **GF10 Social protection** | 41.5% / 23.6% | +3.6 (≈106) | See §4.3 and §4.4 | See §4.3 | 151.5 days: from 1 January to 30 May | Poverty after transfers 16.3% = EU-27 | See §4.3 |

### 4.3 Social protection by risk (Drees / ESSPROS scope)

| Part | Content |
|---|---|
| **Key message** | "Social protection benefits are **31.9% of GDP** (EUR 932.5 bn in 2024, Drees, published edition of Dec 2025)." *(Note 2026-10-25, 15-18 sync: Drees' semi-final accounts of 23 Oct 2026 give EUR 933.2 bn = 31.8% on current GDP; keep 31.9% as the headline until the Dec 2026 edition, 00 row 20.)* "On Eurostat's ESSPROS basis (32.0%, 2024) France is **2nd of 27 in 2024**, behind Finland (32.5%), against an EU-27 aggregate of 27.4%; it is **3rd in the 2025 early estimate** (32.1%, behind Austria and Finland)." *(Clarified 2026-10-25: source, year and EU-27 aggregate now stated; file 00 rows 20-21.)* "**82% goes to two risks: old age-survivors (45.8%) and health (36.3%).** The benefits people most often want to cut (family, unemployment, minimum incomes, housing) together make up **about 18% of benefits**."[^f02] |
| **Steelman** | (1) Per inhabitant in PPS France ranks **7th** (12,606 PPS), and its lead over the EU average fell from +27% (2008) to +14% (2025)[^f02]. (2) **Redistribution works on the reduction:** transfers including pensions cut the poverty rate by 30.5 points, the 3rd-largest cut in the EU; old-age poverty is low (11.6% vs EU-27 16.3%)[^f10]. (3) A lower public share would partly mean higher private premiums, not lower total costs (SOCX net). Our answer on the same page: the **level** of poverty after transfers (16.3%) is only at the EU-27 level and rising (13.6% in 2015), child poverty is 22.8% (rank 22-23 of 27), and the national measure is at its highest since 1996 (15.4%)[^ref]. |
| **Tangible comparisons** | Shares of total benefits 2024 (Drees): family **7.1%**, employment **5.5%**, housing **1.7%**, poverty-exclusion **3.6%** → **17.9%** together. Old age-survivors + health → **82.1%**. **Per inhabitant: EUR 13,650 a year** (Drees). In days of 2025 public spending, the 2024 benefits (932.5 / 4.696 = 198.6; 933.2 on the semi-final accounts = 198.7) would equal 199 days, a caveated comparison because the Drees scope includes private schemes (Agirc-Arrco, *mutuelles*); use it only with the scope note. |
| **Format** | **"Where people want to cut vs where the money is"** (file 14 §9.2 calls it the strongest single graphic). Left column: the Elabe Sept 2026 cut ranking (family 34%, business aid 33%, unemployment 30% … pensions 7%, health 6%, education 5%). Right column: each item's share of TE (family 4.0%, unemployment 2.9%, old age 23.4%, health 15.6%, education 8.9%). Animated connector lines. Then a stacked area chart of benefits by risk, 2019-2024. |
| **Data** | file 02 §3.2 (Drees CPS); `data/eurostat_spr_exp_func.csv`; `data/esspros_france_rankings.csv`; `data/14_perception_surveys.csv`; `data/eurostat_ilc_li02.csv`; `data/debates/computed_poverty_reduction_by_transfers.csv`. |

### 4.4 Pensions

| Part | Content |
|---|---|
| **Key message** | "Pensions are the largest single item: **EUR 422 bn = 14.1% of GDP**, about a quarter of all public spending (COR, 2025). Old-age spending explains **about one-third of France's spending gap** with the euro area (+2.5 of 7.8 pp of GDP vs EA21, COFOG 2024). France works the fewest hours per inhabitant in the EU, largely because of low employment among seniors (60-64: 44.4% vs EU-27 55.0%)."[^ref][^f03][^f08] |
| **Steelman** | (1) **"Pensions are deferred wages, not transfers"** (file 02 §10.4). (2) **They buy something real:** old-age poverty 6.1% (OECD, 50% threshold) vs an OECD average of 14.8%[^ref]. (3) **The system is close to balance on the COR's convention:** -5.1 bn (-0.2% of GDP) in 2025, -0.2% in 2030[^f03]. (4) The "hidden deficit" controversy depends on the accounting convention for State employer contributions (file 03 §5, views A and B side by side). Answer: balance is reached partly through the State's balancing contribution (EUR 49.3 bn) and earmarked taxes (EUR 64.7 bn)[^f03]. |
| **Tangible comparisons** | **1.16 bn per day**; the year's pensions are paid by **about 26 March** in the budget calendar (COFOG old age 23.4%, 85 days). **Household scale: EUR 811 of a EUR 3,000 monthly income.** **Return to 60 vs Zucman:** a general return costs 43-58 bn a year; even the author's central Zucman yield (20 bn) covers **34-47%** of it *(corrected 2026-10-25: was 35-58 bn and 34-57%)*. **Return to 62:** 10-17 bn a year for the pension system around 2030-2035, up to about 26 bn once lost tax revenue is counted. For scale, the 2025 pension-system deficit was **5.1 bn**[^f03]. **Ratio of people aged 20-64 to people 65+: 3.6 (2009) → 2.5 (2025) → 1.62 (2070).** |
| **Format** | (a) Animated population pyramid 2005 → 2025 → 2070 with a "contributors per retiree" counter (1.8 → 1.3). (b) A **retirement-age slider (60-66)** that shows the cost or saving with **short-run and long-run toggles**. It shows the range across sources (Cour, COR, Fipeco, Montaigne) and labels the macro models (DG Trésor long run vs OFCE e-mod short run). For 2 years of legal age, the GDP effect runs from **-0.1% (OFCE e-mod.fr) to +0.3% (Mésange) after 10 years, and +1.1% in micro-based estimates by 2030**; the general-government balance gain runs from **+0.1 to +0.9 point of GDP** (Cour des comptes, Feb 2025, Table 4, via file 17 §3.5)[^f17]. Pension age is a supply measure: no year-1 demand multiplier applies (§5.4). (c) A "perception" card: 47% (Harris/Hexagone 2025) or 44% (Drees 2025) think retirees are worse off than average; the measured value is 100.2%. |
| **Data** | file 03 §1, §4.1, §6, §7; `data/pensions_*.csv`; `data/pensions_oecd_pag2025_extract.csv`; `data/08_eurostat_proj_23ndbi.csv`; COR 2026 report. |

### 4.5 Health

| Part | Content |
|---|---|
| **Key message** | "France spends a lot on health relative to GDP (11.3% of GDP, 3rd in the EU), but it ranks only **8th per inhabitant in purchasing power**. It gets **excellent results on treatable mortality and financial protection**. Its clearest structural problem is **administration**: 5.09% of health spending, **1st of 27**, because of a double layer of insurance (compulsory plus complementary)."[^f12] |
| **Steelman** | Real per-capita growth has been among the slowest in the OECD (0.7%/yr in 2014-2019 vs OECD 2.7%); public hospitals are in deficit; health workers are relatively low-paid (hospital nurses earn 0.97 times the average wage vs an OECD average of 1.17). **The case for large cuts is weak; the case for restructuring is strong** (file 12 §0.8). |
| **Tangible comparisons** | **Administration gap ≈ EUR 6 bn** (0.2 pp of GDP vs the EU aggregate) = **1.3 days** of public spending. Complementary insurers account for **52% of management costs while financing 12.3% of spending**[^f12]. Cour des comptes: **EUR 22 bn of low-value or unnecessary care** (an extrapolation from OECD ratios, not an audited figure; show it as a "pool", not a yield)[^f12]. Each **0.1 pt of ONDAM growth ≈ EUR 0.27 bn** (0.001 × 273.3 bn, ONDAM 2026; computed). |
| **Format** | A "price × volume" explainer: France buys **a lot of care (volumes 128, OECD = 100, 4th of 37) at low prices (health price level 68)**. Two-axis bubble chart, panel countries. Cancer survival table ("average, not top"). |
| **Data** | file 12; `data/12_*.csv` (SHA, avoidable mortality, cancer survival, WHO GHED). |

### 4.6 Civil service and outcomes

| Part | Content |
|---|---|
| **Key message** | "France has a large public workforce but not an outlier: **5.85 m agents, 1 job in 5**; 20.7% of employment on the OECD definition (8th of 30), far below Sweden and Denmark. The wage bill is **12.4% of GDP but only 21.6% of public spending (22nd of 27)**. Once 'make-or-buy' is neutralized (own staff plus purchases plus services bought from private providers), France (24.3% of GDP) is level with Germany (24.1%)."[^f04][^f13] |
| **Steelman** | This is a steelman *against* the right-wing "too many civil servants" story. The French specificity is **how** staff are paid and financed (high employer contributions and imputed pensions push D.1 up; gross wages D.11 are *below* the EU median at 8.3% vs 8.9% of GDP) and **where** they work (secondary vs primary, back office vs front line). Teachers and judges are relatively low-paid. |
| **Tangible comparisons** | D.1 = EUR 370 bn = **79 days** of spending. **"Cutting 100,000 posts"**: no costing in the research base. LR claims 400,000 posts = EUR 25 bn under its "2032 level" reading (file 11 §5.3; party claim, unverified). Show it as a claim with a "not independently costed" flag. PLF 2027 staffing plan: State **+8,025 FTE**, of which +4,742 from the teacher-training reform (verified in file 13 against bill no. 3210, Art. 63)[^f13]. |
| **Format** | Country slider with **three perimeters** (general government employment / NACE O+P+Q / production costs per inhabitant in PPS). France moves from 6th to the middle of the panel: the lesson is "the definition matters". A "means vs results" synthesis table per domain (file 04 §7). |
| **Data** | `data/13_gg_employment_share_ilo_2000_2024.csv`; `data/13_eurostat_OPQ_share_2000_2025.csv`; `data/13_pps_per_capita_wagebill_production_costs.csv`; `data/04_oecd_gaag2025_gg_employment_share.csv`; `data/13_pisa2025_country_values.csv`. |

### 4.7 Taxation (level, structure, who pays)

| Part | Content |
|---|---|
| **Key message** | "Compulsory levies (*prélèvements obligatoires*) are **43.6% of GDP** (EUR 1,305 bn) in 2025, **2nd in the OECD** on the tax-to-GDP measure (43.5% in 2024, behind Denmark). The ratio fell from **45.3% (2017) to 42.7% (2024)**. The system is progressive mainly **through transfers and public services**: the top 10% pay **33.3% of all levies**, while indirect taxes weigh more on the bottom."[^ref][^f05] **Mandatory one-line bridge under the key message (file 18 §1.3):** "Insee's levies (42.7% in 2024) and the OECD figure (43.5%) differ by +0.7 pt because the OECD and Eurostat count refundable tax credits (EUR 19.6 bn) as spending rather than as a tax cut." Never place Insee's PO on an OECD or Eurostat ranking: 42.7% placed on the 2024 Eurostat list would show France 4th in the EU instead of 2nd (file 18 §1.5). On the ESA/OECD concept, 2025 is about **44.2-44.3%** (Cour des comptes: 44.3%)[^f18]. |
| **Steelman** | (1) *Left:* the very top pays less than the merely rich. The IPP finds an effective rate of **about 26% for the ~75 richest households vs about 46% for the top 0.1%** (2016 data). Contested by F. Geerolf (not peer-reviewed): on a homogeneous base the gap largely disappears[^f05]. (2) *Right:* the tax wedge on an average single worker is **47.2%** (3rd of 38), and employer contributions are 10% of GDP (2nd in the OECD)[^f05]. (3) *Perception:* 72% think taxes rose since 2017. That is wrong as a ratio but right in nominal euros (+25.7%), and roughly flat after inflation (+2.5%) (file 14 §7.1). **Recommended wording:** "As a share of national income, levies are lower than in 2017. In euros they have grown, but more slowly than the economy and only slightly faster than prices." |
| **Tangible comparisons** | **EUR 18,915 of levies per inhabitant.** Composition 2025: social contributions 446.3 bn, VAT 208.8, CSG+CRDS 165.9, income tax (IR) 94.3, corporate tax 59.3[^f05]. **52.8% of tax households pay no net IR**, but everyone pays CSG (about 1.7 times IR), VAT and other levies. **56% of people are net beneficiaries** once public services are counted (2023), yet 59% feel they "contribute more than they benefit"[^f14]. |
| **Format** | (a) **"Your taxes receipt"** calculator (spec below). (b) A Sankey diagram from revenue to function, with Fipeco's caveat that revenue is earmarked by subsector, so a pro rata allocation is a convention. (c) A decile chart: levies paid vs transfers received (Insee *redistribution élargie* (extended redistribution), 2023). |
| **Data** | `data/insee_t_3217_T_3217.csv`; `data/insee_taux_prelevements_obligatoires_1959_2025.csv`; `data/oecd_revenue_statistics_2025_pct_gdp.csv`; `data/oecd_taxing_wages_2026_tax_wedge_single.csv`; `data/14_factcheck_PO_2017_2025_real.csv`; Insee Analyses n°118 (2023 deciles). |

**"Your taxes receipt" calculator (spec).**
- **Inputs:** either the user's annual income tax and, optionally, salary (to estimate social contributions and CSG), or the "average person" default (EUR 18,915 of levies).
- **Output:** a receipt-style list allocating the amount across COFOG functions with the EUR 1,000 shares (file 01 §4.2, column A or B, chosen once and stated), plus a final line: **"+ 8.8% paid by future taxpayers (borrowing)"**.
- **Mandatory caveats:**
  - Taxes are earmarked: CSG and contributions go to social security, while IR goes mostly to the State. The pro rata allocation is a convention (Fipeco).
  - Benefits received are shown on a second receipt, using Insee's net-beneficiary logic, so the tool does not feed the "I pay for everything" impression.
- **Benchmark:** the government already runs *À quoi servent mes impôts* (economie.gouv.fr). Cite it and explain the differences: its interest line shows 31 per 1,000 vs 35 in COFOG (file 01 §4.2).

### 4.8 Deficit and debt

| Part | Content |
|---|---|
| **Key message** | "In 2025 France borrowed **EUR 151.6 bn (5.1% of GDP)**, 1 euro in 11 of public spending. Debt reached **115.7% of GDP (EUR 3,460 bn), about EUR 50,000 per inhabitant**, the 3rd-highest ratio in the EU. France's deficit has been worse than the euro area's **every year since 2007**. Its debt ratio was 2.0 points *below* the euro-area aggregate (EA21) in 2005 and was **28.4 points above** it in 2025 (EA20: -2.1 and +28.0)."[^ref][^f06] |
| **Steelman** | (1) **No bankruptcy:** "bankruptcy" is not a defined state for a euro-area sovereign; ratings are A+ to Aa3; non-residents hold 59.7% of negotiable State debt, which is a sign of demand (file 10 §7.1). (2) **Net worth is positive** (+EUR 750 bn)[^f08]. (3) Do not feed alarmism: 60% think France is "close to bankruptcy" (Odoxa/iFRAP), which **overestimates** immediacy (file 14 §7.7). **The honest framing is a rising cost, not an imminent collapse:** the EC rates medium-term risk "HIGH" and projects debt at 144% of GDP in 2036; the OAT spread over Italy turned positive in 2026[^f06]. |
| **Tangible comparisons** | **32.3 days**: from about 29 November, spending runs on credit. **Household: EUR 291 borrowed every month on a EUR 3,000 income; EUR 79,700 of debt.** **What it takes to stop debt rising: about EUR 90 bn a year** (3.0 pts of GDP, Cour des comptes, 2025) = 19 days of spending. **Debt clock: about EUR 4,800 of deficit per second.** |
| **Format** | (a) An animated debt line 1978-2025 with euro-area overlay and the 2008, 2020 and 2022 shocks. (b) A "snowball" explainer (r vs g): in 2025 the apparent interest rate (2.0%) exceeded nominal growth (1.9%) for the first time since Covid[^f06]. Interactive: the user moves r and g and the primary balance, and watches the debt ratio converge or diverge. (c) An EU-27 deficit/debt scatter. |
| **Data** | `data/insee_dette_maastricht_1978_2025_by_subsector.csv`; `data/derived_06_france_vs_ea_deficit_primary_debt_1995_2025.csv`; `data/eurostat_gov_10dd_edpt1_deficit_debt_interest.csv`; `data/eurostat_irt_lt_mcby_m_10y_yields_monthly.csv`. |

### 4.9 Interest burden

| Part | Content |
|---|---|
| **Key message** | "Interest is the fastest-growing item: **EUR 65.7 bn in 2025 → 79.2 bn in 2026 → about 91 bn in 2027** (general government, national accounts), and over EUR 100 bn by 2029 according to the Cour des comptes."[^ref][^f06] |
| **Steelman** | At 2.2% of GDP, France's interest burden is **not yet exceptional**: 8th of 27, below Italy and Hungary (3.8%) and Greece (3.1%)[^f06]. The risk is the trajectory: 2.9% of GDP in 2027, close to Greece's level today. |
| **Tangible comparisons** | **Interest 2025 = 14 days of spending = EUR 952 per inhabitant = EUR 126/month for the EUR 3,000 household.** **Interest vs education:** interest in 2025 (65.7) = 44% of 2024 education spending (148.6, COFOG). **Same-basis comparison (PLF 2027, State budget accounting):** State interest **72.9 > LPM 63**; it roughly equals the Defense mission including pensions (73.9) and is **80% of the school-education mission (91.1)**[^f06]. **The rise between 2025 and 2027 (+EUR 25 bn) exceeds the most optimistic post-behavior yield of any single wealth tax** (Zucman critics: about 5; author: 20). **Never mix concepts:** the all-government national-accounts interest (91 bn in 2027) must not be compared with a budget-accounting mission (file 06 §1). **Three interest figures for 2025 (file 18 §2)[^f18]:** EUR 65.7 bn = ESA D.41, all general government (the headline); EUR 64.7 bn = Insee's presentation "excluding the FISIM correction" (contractual interest, EUR 1.07 bn lower because FISIM on old low-rate public loans has been negative since 2023; label it or do not use it); EUR 51.6 bn = State budget debt charge (State only, budget accounting). Quoting the State charge as "the cost of the debt" understates the general-government burden by **EUR 14.1 bn in 2025** (65.7 − 51.6 = 3.0 days of spending). |
| **Format** | A "race" bar chart (2019-2027): interest vs defense vs justice vs higher education, two sets of bars labeled by accounting basis. A sensitivity slider: +100 bp on all maturities costs **+EUR 3.4 bn in year 1 and +8.1 bn in year 2** (government, HCFP §116). |
| **Data** | file 06 §3.3; `data/eurostat_gov_10dd_edpt1_deficit_debt_interest.csv`; HCFP 2026-5; PLF 2027. |

### 4.10 Party proposals (one card per measure, same template)

**Template ("proposal checker"):**
1. what the measure is;
2. who proposes it (and who opposes it);
3. the claimed yield or cost;
4. independent estimates as a range bar with authors and orientations;
5. conversion into the four yardsticks;
6. behavioral, legal and macroeconomic caveats;
7. the "fairness vs sufficiency" box;
8. the campaign's right of reply.

| Measure | Claimed / range (EUR bn/yr) | Yardsticks (computed) | Key message | Steelman on the same card | Source |
|---|---|---|---|---|---|
| ***Taxe Zucman*** (2% floor on wealth above EUR 100 m, about 1,800 households) | Author 20 (15-25); critics about 5; Senate 2-3 if corporate tax is credited | 0.4-4.3 days; 1.3-13.2% of the deficit; EUR 29-290 per inhabitant | "Even at the author's estimate, it pays for about 4 days of public spending, or one-eighth of the deficit." | Fairness: the IPP finds the ~75 richest households pay about 26% vs 46% for the top 0.1%. Exile is small in absolute terms (CAE: fewer than 350 extra departures a year after 2013). Blanchard and Pisani-Ferry support the principle. Constitutional risk is a genuine uncertainty. **86%** support it in an Ifop poll for the PS (study no. 121870, 10-11 Sep 2025, n = 1,000; verified in file 14 [S1]); **59%** say MPs were wrong to reject it in Elabe for BFMTV (4-5 Nov 2025) when the base is described. | file 07 §3.1[^f07]; CAE[^cae118]; file 14[^f14] |
| **ISF restoration** | +3 to +4.5 gross (+2 to +3 net of the IFI, which yields 2.3) | 0.6-1.0 days; 2-3% | "A return of the ISF would cover about 2-3% of the deficit." | The ISF → IFI reform cost about 4.5 bn (France Stratégie evaluation committee); no effect of the PFU (flat tax) on investment or wages was found | [^f07] |
| **Ending the PFU (flat tax on capital income)** | +3.2 (Montaigne) to +9 (LFI claim) | 0.7-1.9 days | — | France Stratégie found no investment effect of the 2018 reform | [^f07] |
| **CDHR** (20% minimum tax on incomes above 250k/500k) | Announced about 2; collected below 0.4 (2025), 0.65-0.7 forecast (2026) | 0.1 days | **The real-world test:** observed yield was about a quarter to a third of the announcement | Timing effects may raise later yields (IPP) | [^f07] |
| **Retirement at 60** | General return: 43-58 cost *(corrected 2026-10-25, was 35-58; 00 row 44)*. **RN 2027 plan (back to 62, 60 with 40 years for early starters): RN's own figure about 9** (candidate, full year; 9.5 in 2031 in the RN annex). The `rn_back_to_62` card always shows **two independent references side by side**: **repeal of the 2023 reform alone, 16-17** (Cnav estimate as cited in Assemblée nationale report no. 613: 15.7 in 2032; Fipeco: 17 in 2030, incl. accompanying measures) and **partial RN-type versions with 60 for early starters, 26-35** (Institut Montaigne: 26.5 in 2022, 34.7 in 2024, for earlier RN programs; 00 row 44). Neither is a costing of the 2027 plan itself. *(Added 2026-10-25, REVIEW.md point 3: the card showed only 26-35.)* | General return: 9.2-12.4 days, 28-38% of the deficit, EUR 623-841 per inhabitant *(was 7.5-12.4 days, 23-38%)*. Repeal alone: 3.4-3.6 days, 10.6-11.2%, EUR 232-246 per inhabitant. Partial RN-type: 5.5-7.5 days, 17-23%, EUR 377-507. RN claim 9: 1.9 days, 5.9%, EUR 130 (computed as in §3.4) | "A general return to 60 costs more than any wealth tax raises." | Costs ramp up over 2-4 years; models differ on the macro feedback (DG Trésor vs OFCE); this is a social choice that can be financed in other ways (higher contributions: Odoxa finds 61% prefer EUR 150-250 more tax to retirement at 66) | file 03 §4[^f03]; 00 row 44[^ref]; file 11 §4.2[^f11] |
| **Fuel-price freeze at EUR 1.70/l** (LFI) | 0 to 26.5, depending on the oil price; **4.6 bn per EUR 0.10/l** | 0-5.6 days | "The cost is open-ended: it is set by the oil market." | At 2025 average prices the cost is about 0; the PLF assumes Brent at USD 80.3 in 2027, so the expected cost is a few bn (own approximation, flagged) | file 11 §6.2[^f11] |
| **Rent freeze / rent control** | No direct spending; the existing *encadrement* moves about 0.6 bn/yr to tenants, one-third borne by public revenue | ≈0.04 days | "Cheap for the budget; the costs are elsewhere (supply, quality, mobility)." | IPP 2026: rents 2-4% lower with no clear supply collapse in Paris over five years; the international literature on hard freezes finds supply losses (Diamond et al. 2019) | file 11 §6.1[^f11][^ipp125] |
| **Energy VAT 20% → 5.5%** (RN) / energy price shields | VAT cut: cost **more than 11** (Institut Montaigne 2024: "> 11", a lower bound and the only independent costing); RN's own figure 12.2 (2027 counter-budget, fuels included), shown as a claim. The 17.4 of francebudget.fr is not used: its base excludes fuels, so a larger number from a narrower base is inconsistent (file 07 §3.5; flagged unreliable in file 11 §4.2). / Shields 2021-2024: 72 gross, 36 net. *(Corrected 2026-10-25, REVIEW.md #1: was "-11 to -17.4".)* | VAT cut: more than 2.3 days, more than 7.3% of the deficit, more than EUR 159 per inhabitant (RN figure 12.2: 2.6 days) *(was "2.3-3.7 days")* | "Largely untargeted support" (Cour des comptes) | The shields kept French inflation below its neighbors' | [^f07][^f11][^cour-bouclier] |
| **SMIC at EUR 1,600-1,700 net** | -1.8 to -4 (public-finance effect only; own scaling of Montaigne 2024, labeled "illustrative"): **1,600 net about -1.8 to -2.2** (+8.3% vs the SMIC in force since 1 June 2026); **1,700 net about -3.5 to -4** (+15%). Montaigne's -3.5 for 1,600 net dates from 2024, when 1,600 was about +14% above the SMIC. *(Corrected 2026-10-25, REVIEW.md #3-4: was "-3.5 to -4" for the whole range.)* | 0.4-0.9 days (1,600: 0.4-0.5; 1,700: 0.7-0.9) | — | Non-budget effects on employment are not costed | [^f07][^f11] |
| **Civil-service index point** | +1% = -2.1 to -2.4 (2.4: minister's office, July 2026, as reported by the press; 2.1: our computation from the July 2023 +1.5% rise, about 3.2 in a full year / 1.5; see §5.3 S3); +10% (NFP) = -20 | 0.5 days per point | — | Teacher pay is about 18% below the OECD average at 15 years | [^f07][^f04] |
| **Anti-fraud** | +1 to +3 marginal (HCFP: the 1.5 bn government figure was "not credible") | 0.2-0.6 days | "Fraud is real; the realistic recoverable yield is small." Same role on the right as "tax the rich" on the left | Estimated social fraud is **about EUR 13 bn** (12.98 = 7.25 contributions + 5.73 benefits and health-care providers; HCFiPS July 2024, primary), updated to **about EUR 14 bn** (HCFiPS, Dec 2025); error items must not be added (00 row 59). *(Corrected 2026-10-25, 15-18 sync: was "about EUR 13 bn (HCFiPS, secondary source)".)* Tax-fraud estimates range widely | [^f07][^f14] |
| **Immigration-related savings** (RN, LR) | RN: 8 (2024 legislative claim, as reported by Institut Montaigne), 11.9 (2026 counter-budget), **15.1 (2027) → 29.0 (2031)** (2027 counter-budget); LR: 10 (not independently costed) | 8-15.1: 1.7-3.2 days, 5.3-10.0% of the deficit, EUR 116-219 per inhabitant; 29.0: 6.2 days, 19.1%, EUR 420 (computed as in §3.4) | "Legally fragile, undocumented": the Institut de l'Entreprise (business-funded) classes 92% of the RN immigration block as undocumented or legally fragile; the Constitutional Council struck down, on substance, a five-year residence / 30-month work condition for family and housing benefits (decision 2024-6 RIP, 11 Apr 2024) (file 15 §6.1) | **Net fiscal contribution of the foreign-born: +1.02% to -0.85% of GDP a year** depending on how public goods (defense, debt interest) are shared (OECD IMO 2021, 2006-18 average; France 21st of 25 OECD countries on the all-public-goods basis; 00 row 55). At 2025 GDP that is about **+EUR 30.5 bn to -25.3 bn** (illustrative, file 15 §4). Per head, the foreign-born contribute less than the native-born (-6.5% vs -3.7% of GDP per capita, C2 convention). **AME:** standard AME spending **EUR 1.34 bn in 2025** (0.045% of GDP, 0.08% of TE), credits **EUR 1.208 bn** for the AME action in PLF 2027 (programme 183: 1.216 bn), 454,111 beneficiaries at end-2025 (00 row 54); the government-commissioned Évin-Stefanini report (Dec 2023, primary) put AME spending at **EUR 968 m in 2022** and found no "structural abuse or fraud" (00 log #32). **The RN's 29.0 bn for 2031 is larger than the whole OECD net-contribution estimate on any convention that excludes debt interest** (file 15 §6.1). *(Updated 2026-10-25, 15-18 sync: claims itemized, AME 968 m and AME credits added, "8 (Montaigne's view of the claims)" corrected: the 8 bn is the RN's own 2024 figure as reported by Montaigne.)* | file 15[^f15]; [^f07][^f14] |
| **Capping the EU contribution at EUR 5 bn** (RN) | **11.1 (2027) → 19.5 (2031) claimed** (Institut de l'Entreprise tabulation of the RN "EU" block, which also includes customs duties and tobacco taxation; the contribution cut alone is 13.1 in 2031; J. Bardella quoted 9 in the press) (file 11). **Verified net contribution 2025: EUR 9.5 bn (accounting method) / 6.4 bn (Commission operating balance)** (00 row 52). **Maximum saving of a 5 bn cap, even if legal: 6.4 − 5 = 1.4 to 9.5 − 5 = 4.5** | Claimed 11.1: 2.4 days, 7.3% of the deficit, EUR 161 per inhabitant. Maximum if legal 1.4-4.5: 0.3-1.0 days, 0.9-3.0%, EUR 20-65 (computed as in §3.4) | "**The claim exceeds France's entire net contribution** (9.5 bn on the most unfavorable method). Even if it were legal, a 5 bn cap would save 1.4-4.5 bn, **2.5 to 8 times less than claimed**. Legally, the contribution follows from the Own Resources Decision, adopted unanimously and ratified by every member state: the unilateral yield is about zero." | France is the **2nd-largest net contributor in euros** and 4th of 27 as % of GNI (0.31%); the gross levy (PSR-UE) rises from EUR 23.0 bn executed in 2025 to **30.9 bn in PLF 2027** (file 16 §3.1): the cost is real and rising. Counter, on the same card: the Budget Directorate warns that the net balance omits single-market gains and spending that cannot be allocated to countries (file 16 §3.3). *(Updated 2026-10-25, 15-18 sync: was "11.1 (2027) claimed", with no verified net figure and an empty steelman cell.)* | 00 row 52 and log #31[^ref]; file 16 §3[^f16]; file 11 §4[^f11]; [^f07] |
| **Whole programs, 2027** | LFI claims +24.7 net in 2027 (independent range -83.8 to +17.5); RN claims +140 by 2032 (Institut de l'Entreprise: about +7.5 credible); LR 197 "over five years" (two possible readings); Renaissance 150; Horizons 0 vs the PLF | — | "**No 2027 program has been independently costed** by an institutional body." | The platform's own aggregation is static, illustrative and labeled as such; every campaign is invited to respond | file 11 §5.4[^f11] |

**Format for programs.** One card per candidate with the same template, so programs look **visually identical**. Each card shows a waterfall chart from the 2026 deficit (164.9 bn) to the claimed end-of-term deficit, with claimed and independent bars side by side and a confidence color. **Rule:** if any measure lacks an independent estimate, the card shows a grey "not costed" segment rather than the party figure alone.

### 4.11 Tax cuts since 2017 (the steelman chapter)

| Part | Content |
|---|---|
| **Key message** | "Both stories are true. **Since 2017**, the deficit rose because revenue fell: ESA total revenue -3.1 pts of GDP over 2017-2024 (54.3 → 51.2) while spending fell only 0.7 pts. The Cour des comptes values the tax and contribution cuts decided in 2018-2023 at **EUR 62 bn a year (2.2 pts)**, not offset by spending savings. **Since 2019** (2019-2025), spending rose by 2.0 pts of GDP while revenue fell by 0.8 pts: the Cour's 'ratchet effect'. **The base year decides which half you see.**"[^f10][^cour24] |
| **Steelman (both directions)** | (1) For the revenue camp: OFCE PB 146, Fipeco (about 44 bn by 2022), Rexecode (75 bn at 2025 prices; an employer-funded institute). (2) For the spending camp: 2017 was a revenue peak after 2011-2013 tax increases (3.8 pts of GDP of hikes in 2010-2014); France's levies are still 2nd in the OECD; the Cour and the IMF say this limits the revenue route. **Where all agree:** the cuts were not financed by the announced spending savings; the 2025 adjustment came mainly from tax increases (EUR 23 bn) (file 10 §4.3). |
| **Tangible comparisons** | **EUR 62 bn = 13 days of spending = 41% of the 2025 deficit.** Rexecode: about **EUR 36.7 bn** (+1.2 pts) of new levies in 2024-2026 already reversed part of it[^f08]. **HCSP feasibility test:** closing 4.4 pts of GDP by 2031 through spending alone needs real spending to *fall* 0.2%/yr for five years in a row, something that happened only 3 times since 1959. Through revenue alone, real revenue must grow 2.7%/yr, which happened 32+ times (file 10 §6.3). |
| **Format** | **A base-year slider:** the user picks the start year (2005-2019) and the end year; a waterfall splits the change in the deficit into Δ spending, Δ revenue and Δ interest. The page title changes dynamically ("Since 2017: mostly revenue" / "Since 2019: mostly spending"). This is the clearest way to show honesty. |
| **Data** | `data/debates/computed_fr_vs_eu27_fiscal_series.csv`; `data/eurostat_gov_10a_main.csv`; file 08 §3; file 10 §4. |

### 4.12 Business aid

| Part | Content |
|---|---|
| **Key message** | "'Aid to business' is **EUR 45, 82, 108, 187 or 211 bn** depending on the definition. Two choices drive the range: whether the **general low-wage contribution relief (about EUR 75 bn)** counts as aid, and whether Bpifrance loans count at face value." [^f08][^hcsp-aides] |
| **Steelman** | Left: 33% of people want to cut business aid first, and the Senate inquiry found "at least EUR 211 bn" with little evaluation. Right: the general relief exists because of the high contribution wedge. Full abolition would raise about **48 bn net with -980,000 FTE jobs** (Bozio-Wasmer). Both the HCSP and the Senate agree that evaluation is lacking. |
| **Tangible comparisons** | The range runs from **10 to 45 days** of spending (45 / 4.70 = 9.6; 211 / 4.70 = 44.9). **At 1.15 SMIC, raising a worker's disposable income by EUR 100 costs the employer EUR 483-518** (the low-wage trap)[^f08]. |
| **Format** | **"Build your own definition"**: checkboxes (budget subsidies / targeted tax expenditures / general contribution relief / reduced VAT rates / Bpifrance at face value / at subsidy equivalent) with a live total. It teaches that the number is a definition, not a fact. |
| **Data** | file 08 §4; file 05 §7; `data/plf2027_vm_tome2_tax_expenditures_summary.csv` (sums of items, verified by file 05 on 2026-10-25 but not an official total; recommendation: replace by the Cour des comptes total of EUR 91.83 bn for 2025, as lever R9 already does). |

### 4.13 Employment rate, hours and productivity

| Part | Content |
|---|---|
| **Key message** | "France's problem is the **quantity** of work, not its quality: **69.3% employment rate (21st of 27)** and **the fewest hours worked per inhabitant in the EU (666 h/yr, last of 27)**. Raising employment to Germany's level (in full-time equivalent) would bring **about EUR 38 bn of levies**, a quarter of the deficit."[^f08] |
| **Steelman** | Hours *per worker* are higher than in Germany or the Netherlands (part-time work). High hourly productivity is partly a selection effect. The DG Trésor exercise is "purely illustrative": new entrants would be less productive (discounted 36-45%), and it does not cost the policies needed. Hourly productivity fell 0.8% in 2019-2025. |
| **Tangible comparisons** | **+38 bn = 8 days of spending = 25% of the deficit**; the headcount scenario goes up to 84 bn. In 2009 France was above the EU employment rate (64.4 vs 62.8); in 2025 it is 1.7 pts below. |
| **Format** | Slope chart 2009 → 2025 (France vs EU-27, DE, NL, SE). Then a "what if" slider: "close X% of the employment gap with Germany" → levies (linear approximation of the DG Trésor figure, flagged). |
| **Data** | `data/08_eurostat_lfsi_emp_a.csv`; `data/08_eurostat_nama_10_lp_ulc.csv`; `data/08_oecd_employment_rate_15_64.csv`. |

### 4.14 Other subjects (shorter cards)

| Subject | Key message | Steelman | Comparison / format | Data |
|---|---|---|---|---|
| **Local government** | Local spending 11.2% of GDP, **in line with the EU (11.3%)**; local deficit EUR 15.6 bn of 151.6 (2025) | "Local authorities are not the problem" is supported; but the State finances them through VAT fractions recorded as their own tax revenue | Pie of the 2025 deficit by subsector: **State 128.1 (84.5%), ODAC 2.2 (1.5%), local 15.6 (10.3%), social security 5.8 (3.8%)** (Insee update of 28 Aug 2026; the parts sum to 151.7 by rounding vs a total of 151.6; shares computed on 151.6). *(Corrected 2026-10-25, 15-18 sync: social security was 6.7, the superseded May 2026 vintage; 00 §4 and log #27.)* The public is roughly right here: 55% blamed State deficits for the debt in Ipsos 2021 | file 08 §5; `data/08_eurostat_gov_10a_main_s1313.csv` |
| **Demographics and ageing** | Age-related spending **29.9% of GDP, the highest in the EU** (2022); natural balance **-6,000 in 2025**, the first negative since WWII; fertility 1.56 | Fertility is still among the highest in the EU (2nd in 2024) | Animated pyramid; dependency ratio 35.7 → 52.3 (2025-2070) | file 08 §7; `data/08_eurostat_proj_23ndbi.csv` |
| **Upward pressures** (defense, climate, interest) | Even with no new promise, spending pressure rises: NATO 3.5% (+44 bn), climate (+25-34 bn public), interest (+25 bn by 2027) | Some of this is investment (climate) or a security necessity | "Pressure gauge": bars adding to **about +EUR 94-103 bn a year** of potential pressure (44 + 25-34 + 25), presented with each item's horizon (2027, 2030, 2035) and **not as a single sum** | file 08 §8; file 06 |
| **Poverty and redistribution** | Redistribution cuts poverty more than in most countries (-30.5 pts, 3rd), but poverty after transfers (16.3%) is at the EU-27 level and rising | Insee's extended redistribution: the D10/D1 income ratio falls from 26 to 3.5 after transfers and services | Before/after dot plot by country | `data/debates/computed_poverty_reduction_by_transfers.csv`; `data/eurostat_ilc_li*.csv` |
| **Public investment and net worth** | Gross investment 4.4% of GDP (above the EU), net only 0.6% (23rd of 27); net worth +750 bn | Debt partly finances assets | Balance-sheet graphic (assets 2,945 vs net financial position -2,195) | file 08 §9 |

### 4.15 Immigration and public finances (including the AME) *(added 2026-10-25, 15-18 sync)*

| Part | Content |
|---|---|
| **Key message** | "There is no single 'cost of immigration'. The best comparative estimate (OECD, 2006-2018 average) puts the net fiscal contribution of the foreign-born **between +1.02% and -0.85% of GDP a year**, about **+EUR 30 bn to -25 bn** at 2025 GDP (illustrative). The sign depends almost entirely on one convention: whether defense and debt interest are charged per head. On the least favorable convention, France ranks **21st of 25** OECD countries. State medical aid (AME) cost **EUR 1.34 bn in 2025**, 0.08% of public spending."[^ref][^f15] |
| **Steelman (both directions)** | *Right:* per head, the foreign-born contribute less than the native-born (-6.5% vs -3.7% of GDP per capita, all-public-goods convention), about EUR 1,200 per foreign-born resident per year (file 15 §4, illustrative); France's result is weaker than in most comparable countries (panel median -0.32% vs France -0.85%); AME credits are chronically under-budgeted (actual 1.34 bn vs credits 1.208 bn; State debt to the CNAM EUR 185 m at end-2024) (file 15 K13-K16). *Left / pro-immigration:* under the same convention, the native-born look worse in total (-3.25% of GDP), because government ran deficits; the CEPII's 30-year French study finds immigration "never determined" the primary deficit (-0.49% to +0.05% of GDP, 1979-2011); a static figure is not the saving from less immigration (dynamic estimates can change sign); closing the employment gap for prime-aged immigrants would add about +0.22% of GDP (about EUR 7 bn) (file 15 §0, K8-K10)[^f15]. |
| **Tangible comparisons** | AME 2025: **EUR 1.34 bn = 0.3 days of spending = 0.9% of the deficit = EUR 19 per inhabitant** (computed as in §3.4). Évin-Stefanini (Dec 2023, primary report): **EUR 968 m in 2022**, no "structural abuse or fraud". RN "AME → AMU" line (1.3 bn) = **97% of 2025 AME spending**: it assumes emergency care for the same people costs nothing, although the *soins urgents* envelope (EUR 70 m) and hospital bad debt would remain (file 15 §6.1). RN immigration block 29.0 bn (2031) ≈ the whole OECD net contribution on the least favorable convention (-25.3 bn at 2025 GDP). |
| **Format** | (a) **"Choose the convention" toggle:** five buttons (individualized items only / + congestible goods / + pure public goods excl. defense and interest / excl. interest only / all public goods) move one bar from +1.02 to -0.85% of GDP, with the EUR bn and France's OECD rank shown live. It teaches that the sign is a convention, not a fact. (b) A "claims vs stakes" bar chart: RN 15.1 → 29.0, LR 10, next to AME 1.34 and the OECD range. (c) Legal chip: Constitutional Council decision 2024-6 RIP. |
| **Data** | `data/15_oecd_fiscal_immigration_stats.csv`; `data/15_conversions_eur_2025.csv`; `data/15_eurostat_foreign_born_share.csv`; PAP 2027 programme 183; Évin-Stefanini report (`data/raw/16_factcheck/evin_stefanini_292122.pdf`). |
| **Do not publish** | "Immigration costs France EUR X bn" as a single number; "immigrants pay for our pensions" as a general claim; the press figures "AME about 1.2 bn (2023)" and "466,000 beneficiaries" (an extrapolation) (00 §4; file 16 §9). |

### 4.16 Popular "easy savings" targets (development aid, EU contribution, agencies, consultancies, politicians, broadcasting, associations) *(added 2026-10-25, 15-18 sync)*

**Shared key message:** "None of these targets, even abolished outright, closes the deficit. At full gross value they add up to **about EUR 29 bn = 6.3 days of spending = 19% of the 2025 deficit**, and most cannot legally or practically go to zero. Realistic yields are much smaller." (file 16 §0)[^f16]. **Steelman shared by all cards:** cutting visible running costs may be a precondition for public consent to larger reforms (iFRAP and parties of the right); the counter, on the same card, is the Senate rapporteur's own warning that those who announce "billions of savings" from agencies are misleading people (C. Lavarde, LR; file 16 §11). **Symmetry:** these cards are mainly right-coded checks; they are published alongside the left-coded checks of §4.10 (wealth taxes) and §4.12 (business aid), and the quarterly symmetry audit (§7.1) counts them.

| Target | Key message | Steelman on the same card | Tangible comparison (computed as in §3.4) | Format | Source |
|---|---|---|---|---|---|
| **Development aid** | "Three numbers: the budget mission (EUR 3.17 bn, PLF 2027), COFOG foreign economic aid (EUR 4.9 bn, 2024) and OECD ODA (EUR 12.9 bn = 0.42% of GNI, 2025). Only the first is what next year's budget can cut, and the PLF 2027 already cuts it by 0.40 bn (commitments -43%)." | *For cuts:* ODA includes loans, the EU share and refugee costs, so budget cuts overstate the fall in aid. *Against:* France is 11th of 33 DAC donors, below its northern peers (SE 0.85, DK 0.72, NL 0.58, DE 0.56); the 2027 cut is the sixth in a row (Coordination SUD, NGO) | Mission 3.17 bn = 0.7 days = 2.1% of the deficit = EUR 46 per inhabitant; ODA 12.9 bn = 2.7 days | "Three numbers, one word" explainer; DAC % of GNI bar chart | 00 row 53; file 16 §2 |
| **EU contribution** | See the proposal card in §4.10: net 9.5 / 6.4 bn (2025); a 5 bn cap saves at most 1.4-4.5 bn even if legal | See §4.10 | Net 9.5 bn = 2.0 days = 6.3% of the deficit | Gross → returns → net waterfall (own resources 25.9 → EU spending in France 16.4 → net 9.5) with the Commission method as a toggle | 00 row 52; file 16 §3 |
| **State operators and agencies** | "Operators receive EUR 72.6 bn of public funding (423 operators, 397,282 FTE), but 39% of their operating subsidies go to universities; the rest funds research, employment, training and housing. The Senate puts the recurrent saving from reorganizing them at about **EUR 0.54 bn**." | The government claimed 2-3 bn in 2025 but "could not explain the calculation" (Senate); an 8% cut of all staff and running costs would yield 2.2 bn, "not at constant missions". Counts of "agencies" range from 103 to 1,244 depending on the definition | 72.6 bn = 15.5 days, but realistic saving 0.54 bn = 0.1 days = 0.4% of the deficit | "What is inside an operator?" treemap (France compétences 15.1, AFITF 4.6, ANAH 3.8, France Travail 2.0, water agencies 1.9) | file 16 §4 |
| **Consultancies** | "Strategy consulting by the State fell from EUR 271.5 m (2021) to **EUR 60 m (2025)**; the Senate's 'more than EUR 1 bn' (2021) covered all intellectual services, IT included." | Different perimeters and years, not a contradiction; IT services bought from digital-services firms are still EUR 720 m (2025) | 60 m = 0.01 days = 0.04% of the deficit | Before/after bar, two perimeters labeled | file 16 §5 |
| **Politicians, the Presidency and cabinets** | "The *Pouvoirs publics* mission (Presidency, Parliament, Constitutional Council) plus all ministerial cabinets' gross pay cost about **EUR 1.3 bn, 0.08% of public spending**. Halving it would close about 0.4% of the deficit." | Symbolic value for public consent (see shared steelman). Gross pay excludes employer contributions and running costs; no official full-cost figure exists | 1.3 bn = 0.3 days = EUR 19 per inhabitant; Presidency 122.6 m | "Per inhabitant per year" coins: Presidency EUR 1.8, Parliament EUR 14 (computed: 0.1226 / 68.998; 0.9803 / 68.998) | file 16 §6 |
| **Public broadcasting** | "EUR 3.82 bn a year (France Télévisions 2.38). This is the one item where France is above the EU average: 0.26% of GDP, 5th of 27 (COFOG 08.3, wider scope)." | *For privatization:* spending above the EU average; RN shows a 1.6 bn saving. *Against:* feasibility "uncertain" (Institut Montaigne); most of the gain would be a one-off sale price, not a recurrent saving; pluralism | 3.82 bn = 0.8 days = 2.5% of the deficit = EUR 55 per inhabitant | EU-27 bar chart of COFOG 08.3 with France highlighted | file 16 §7 |
| **Subsidies to associations** | "The State paid associations EUR 10.5 bn in 2025, mostly to deliver public services (emergency shelters, asylum reception, legal aid). A 10% cut by the State and local authorities would yield about EUR 1.6 bn (iFRAP), about 1% of the deficit." | Cutting means cutting the service or re-internalizing it at a cost; 3% of payments carry 69% of the money | 10.5 bn = 2.2 days; the State-only 10% cut = 1.05 bn (computed) | "Who receives the money?" treemap by policy area | file 16 §8 |
| **AME** | See §4.15 | See §4.15 | 1.34 bn = 0.3 days | See §4.15 | 00 row 54; file 15 |

*Parliament per inhabitant: National Assembly 619.8 m + Senate 360.5 m = 980.3 m (PLF 2027, file 16 §6) / 68.998 m = EUR 14.2; Presidency 122.6 m / 68.998 m = EUR 1.8.*

### 4.17 Methodology page: three measurement bridges *(added 2026-10-25, 15-18 sync)*

| Part | Content |
|---|---|
| **Key message** | "Three pairs of official numbers look contradictory and are not. Each page that quotes one of them links here." |
| **Bridge 1: levies** | Insee PO 2024 **42.7%** + refundable tax credits counted as spending by ESA (**+0.67 pt, EUR 19.6 bn**) − voluntary contributions (−0.03) + OECD/Eurostat GDP and data vintage (+0.11) = **43.47 ≈ 43.5%** (OECD tax-to-GDP, 2nd of 36). EU taxes are in *both* measures and are not part of the gap. 2025 on the ESA/OECD concept: about **44.2-44.3%** (Cour: 44.3%). Rule: Insee PO for France over time; the ESA/OECD measure for rankings; never mix (00 log #33; file 18 §1)[^f18]. |
| **Bridge 2: interest 2025** | **65.7 bn** ESA D.41, all general government (headline: 2.2% of GDP, 3.8% of TE) vs **64.7 bn** Insee "excluding FISIM correction" (−1.07 bn, of which local government −0.74: old fixed-rate loans below the reference rate) vs **51.6 bn** State budget debt charge (State only, budget accounting; State-level D.41 is 52.5). 2026-2027: general government 79.2 → about 91 bn vs State budget 63.4 → 72.9 bn (00 rows 39-41, log #34; file 18 §2)[^f18]. |
| **Bridge 3: health** | COFOG health **8.9% of GDP** (EUR 261.2 bn, 2024) vs SHA government + compulsory schemes **9.44%** (EUR 276.9 bn): SHA adds 22.2 bn of employer-mandated complementary insurance; COFOG adds 12.6 bn of capital spending and 3.3 bn of R&D; a residual of about 9.5 bn is not decomposed. Gap with EA21: **+1.47 pp (COFOG) vs +1.06-1.10 pp (SHA)**: say "1 to 1.5 points of GDP depending on the definition" (00 log #35; file 18 §3)[^f18]. |
| **Steelman / open points** | The OECD labels France's figure "split basis" but it equals the ESA gross figure (open question to the OECD); the State D.41 vs budget-charge split (0.9 bn) and the 9.5 bn health residual are not quantified (file 18 §4). Say so on the page. |
| **Format** | Three waterfall charts (one per bridge), each with a one-sentence plain-French summary and a "which number should I quote?" box. |
| **Data** | `data/18_po_vs_oecd_bridge_2024.csv`; `data/18_interest_bridge.csv`; `data/18_cofog_vs_sha_health_2024.csv`. |

### 4.18 Explainer: "why EUR 30 bn of cuts does not cut the deficit by EUR 30 bn" (macro feedback) *(added 2026-10-25, 15-18 sync)*

| Part | Content |
|---|---|
| **Key message** | "A measure that saves 1 point of GDP (about EUR 30 bn) slows growth in the short run, which lowers tax revenue. French official bodies currently work with a multiplier of **about 0.6** for a mixed package in year 1 (HCFP), and the deficit worsens by about **0.57 × the GDP loss** (CAE). So EUR 30 bn of cuts in operating spending (multiplier 0.8) nets about **EUR 16 bn** in year 1 (30 × (1 − 0.8 × 0.57) = 16.3)."[^ref][^f17] |
| **Steelman (both directions)** | *Spending-cut camp:* narrative studies (Guajardo-Leigh-Pescatori; Alesina-Favero-Giavazzi) find tax-based consolidations costlier than spending-based ones (GLP: 1.29 vs 0.43). *Tax camp:* French macro models find the opposite in year 1 (spending 0.78 vs income tax 0.41 in Mésange), and taxes on capital and very high wealth have low short-run multipliers (about 0.0-0.3). The Cour des comptes reads the evidence as "comparable" costs and stresses composition. **Both camps' "painless" claims fail**: no source supports a multiplier above 1.75 (the threshold at which a cut would worsen the deficit) in normal times, and the government's 2024 zero multiplier was called "very favorable" by the IGF mission (file 17 §6, §8)[^f17]. |
| **Tangible comparisons** | At m = 0.6, closing the gap to 3% (EUR 62 bn net) needs about **EUR 94 bn of measures** (61.9 / 0.658); see §5.2. |
| **Format** | A slider "multiplier 0 → 1.5" next to a EUR 30 bn cut, with the net deficit gain and the GDP loss updating live, and labeled markers at 0 (PSMT 2024), 0.6 (HCFP 2027), 0.8 (operating spending default) and 1.5-2 ("crisis values, not 2027"). |
| **Data** | file 17 §8 (defaults table) and §3 (model tables); no CSV yet. |

---

## 5. "Balance the budget yourself": simulator specification

### 5.1 Design goals

1. **Teach trade-offs, not a right answer.** No "score". The user sees the consequences: debt in 2032, the PO rate, the spending ratio, who is affected (deciles where known) and confidence.
2. **Every EUR value comes from the research base**, with a source chip and a range. No lever has a value the research base does not contain. Missing values are shown as "not costed" and disabled, or allowed only in a "custom" mode with a warning.
3. **Symmetric menu**: an equal number of revenue and spending levers, plus "growth/structural" levers, and left-coded and right-coded proposals in equal visibility. *(Note 2026-10-25, 15-18 sync: the "popular targets" levers S13-S19 are shown as one collapsible group, "Popular targets", placed at the same level and with the same visibility as the revenue group "Taxing the very wealthy" (R1-R5), so the top-level menu stays balanced.)*
4. **Macro feedback is shown, not hidden.** A measure's effect on growth feeds back into the deficit (§5.4). The default uses published multipliers by instrument with bands (file 17 §8); the user can switch it off to see the static figure.

### 5.2 Goals the user can choose

| Goal | EUR bn to find (2025 base, static) | Computation | Source |
|---|---|---|---|
| A. Stop the debt ratio from rising | **≈ 90** | Gap to the debt-stabilizing primary balance, 3.0 pts of GDP | Cour des comptes, June 2026[^cour26] |
| B. Reach the 3% Maastricht limit | **≈ 62** | 151.6 − 3% × 2,991.1 = 151.6 − 89.7 | Computed from [^ref] |
| C. Balance the budget | **151.6** | Whole deficit | [^ref] |
| D. Stabilize debt durably by 2032 (advanced) | **≈ 125** vs the unchanged-policy trend | Primary surplus of 0.8% of GDP | IGF mission, July 2026[^igf] |
| "Automatic headwind" toggle (on by default) | **+25** | Interest 65.7 → 91 bn (2025 → 2027) | [^ref] rows 39-40 |
| Pressure toggles (off by default) | Defense to NATO 3.5%: +44; climate (public): +25-34 | | file 08[^f08] |
| Macro feedback (on by default, §5.4): gross measures needed | Goal B: **≈ 94** of measures to net 62 at m = 0.6; goal A: ≈ 137 to net 90 | 61.9 / (1 − 0.6 × 0.57) = 61.9 / 0.658 = 94.1; 90 / 0.658 = 136.8. The actual figure depends on the lever mix (each lever uses its own multiplier) | 00 row 62; file 17 §8[^f17] |

*Version 1 is a single-year static simulator on a 2025 base (clearly labeled "if applied to 2025"). Version 2 (after the March 2027 Insee release) adds a 2027-2032 path using the HCFP/IGF trajectory, with ramp-up profiles for pensions and behavioral responses.*

### 5.3 Lever list (version 1)

Positive = improves the balance. "Static" = mechanical yield; "Behavioral" = after the documented responses. Confidence follows file 07: H (high) / M (medium) / L (low).

**A. Revenue levers**

| # | Lever | Range of the control | Static (EUR bn) | With behavioral / legal response (EUR bn) | Conf. | Source | Notes shown to the user |
|---|---|---|---|---|---|---|---|
| R1 | Zucman tax (2% floor above EUR 100 m) | on/off | 20 (15-25) | 5 (2-6) | L | file 07 §3.1 | Constitutional risk flag; the base is concentrated (three departures would halve it) |
| R2 | Restore the ISF (net of the IFI) | on/off | 3-4.5 gross / 2-3 net | lower (not quantified) | M | file 07 | Cannot be stacked in full with R1 (overlapping bases): the tool caps the R1+R2 combination at the file 07 §5 band (3-10) |
| R3 | End the flat tax (PFU) | on/off | 3.2 (Montaigne) to 9 (LFI claim) | — | M/L | file 07 | Show both; default 3.2 |
| R4 | Inheritance reform targeting large estates | 0-3 positions | 3-10 | not costed | L | file 07 §5 | "No independent costing found" |
| R5 | Strengthen the CDHR | on/off | 0.5-1 | observed basis | H | file 07 | The real-world test of top-income taxation |
| R6 | Corporate-tax surtax on large firms (renewed) | on/off | 8.0 (2025 one-off) | — | H | file 07 | One-off in 2025; renewal is a choice |
| R7 | VAT, all rates | -1 to +2 pts | 8.2 net per pt (13 gross) | — | M/H | file 07 | Regressive: Insee finds levies on consumption raise inequality by 3.9 Gini points |
| R8 | *Année blanche* (freeze of IR brackets, pensions and benefits) | on/off | 4.4-5.7 | — | M/H | IPP via file 07 | Regressive overall (IPP) |
| R9 | Tax expenditures (*niches*): cut x% of the EUR 91.8 bn | 0-30% | x% × 91.8 | lower; not modeled | M | file 05 §7.1 | 474 measures; actual cost known for only 55%; the largest items are listed (CIR 7.1, home-employee credit 7.1, 10% pension allowance 5.6, Dutreil 3.8) |
| R10 | Cap the 10% pension allowance at EUR 3,000 | on/off | 1.4 | — | M | PLF 2027 via file 07 | |
| R11 | General employer contribution relief (*allègements généraux*, about 75 bn) | 0-100% removal | linear, up to 75 | up to about 48 net at 100%, with **-980,000 FTE jobs** | M | Bozio-Wasmer via file 08 | Employment-loss counter shown alongside |
| R12 | Anti-fraud plan | on/off | 1-3 | — | M | file 07 | "Not credible" label above 3 (HCFP) |
| R13 | Party-specific revenue claims (buyback tax 8.4, "climate ISF" 10, multinationals tax…) | custom | claim | halved (convention, file 11 §5.1) | L | file 07, 11 | Shown under "claims", grey |

**B. Spending levers**

| # | Lever | Range | Static (EUR bn) | Behavioral / macro | Conf. | Source | Notes |
|---|---|---|---|---|---|---|---|
| S1 | Legal retirement age | 60 ↔ 66 | 64 → 63: -5.8 (pension system) / -13 (all public finances, 2035); to 62: -10 to -17 (system), about -26 incl. induced revenue; to 60 (general): -43 to -58 *(corrected 2026-10-25, was -35 to -58; 00 row 44)*. +1 yr: +0.3 to +0.65 pt of GDP (≈ +9 to +19) in 10-20 years | Ramp-up 2-4 yrs; DG Trésor vs OFCE models | M | file 03 §4 | Short-run / long-run toggle |
| S2 | Pension indexation (PLFSS 2027 measure: pensions, base plus complementary, fully indexed only up to EUR 1,260 a month, lower indexation above; a partial under-indexation, not a freeze) *(label corrected 2026-10-25, REVIEW.md #5: was "one-year freeze of base pensions, lowest pensions protected")* | on/off | about 4.1 (PLFSS 2027 savings: 3.0 basic schemes + 1.1 State, net of CSG/CASA) | — | M/H | file 03 | Overlaps R8 (the tool prevents double counting) |
| S3 | Civil-service index point | -1 to +10% vs freeze | 2.1-2.4 per pt | — | M | file 07 §3.6 | Each end has its own source *(added 2026-10-25, REVIEW.md point 2)*: **2.4** = minister's office, July 2026, reported by Acteurs publics and Selectra (press; labeled "minister's office figure, as reported"); **2.1** = our computation: the July 2023 +1.5% rise cost about 3.2 in a full year across the three branches (press citing the decree's impact sheet), and 3.2 / 1.5 = 2.13; consistent with Institut Montaigne's 20 for +10% (2 per point). Partial official check: the State-branch cost of the 2023 rise, 1.5, is confirmed by the Senate (avis no. 134 on the PLF 2024). No DGAFP primary found; the ⚠ 2.07 breakdown is not used |
| S4 | Public headcount | slider | **not costed in the research base** | — | — | — | Disabled in v1; v2 needs an average cost per FTE from DGAFP |
| S5 | ONDAM growth (health) | 0-5%; **default +3.4%** | 0.27 per 0.1 pt (on 273.3 bn), measured from the default | Quality and access trade-off | M (computed) | file 02 §4.3; file 12 §7.2 | Shows access indicators (GP shortages: 29% of the population). **Default and markers** *(set 2026-10-25, REVIEW.md point 4)*: the slider starts at the **2027 trend growth of +3.4%** (CCSS, as stated in the PLFSS 2027), the no-policy baseline, so the default yield is 0. Labeled markers: **+2.0%** = PLFSS 2027 target (EUR 278.7 bn, bill no. 3211, Art. 43); **2-2.5%** = the "more demanding" path the Cour des comptes calls for (RALFSS, May 2026). Check: 3.4% → 2.0% = 14 × 0.27 ≈ 3.8 bn, close to the Cour's 3.9 bn of net ONDAM savings in the PLFSS 2027 |
| S6 | Health restructuring (administration, low-value care) | on/off | **pool, not yield**: admin gap ≈ 6; low-value care 22 (Cour, extrapolated) | Multi-year, uncertain | L | file 12 | Shown as "potential, not a budget figure" |
| S7 | Targeted business aid (HCSP perimeter 1, 82 bn) | cut 0-30% | linear | Effects unknown (evaluation lacking) | L | file 08 | |
| S8 | Family / minimum-income benefits | cut 0-10% | x% × (family 65.8 + poverty 34.0, Drees 2024) | Poverty-rate effect not modeled; child-poverty warning | M | file 02 §3.2 | Drees scope (all schemes): flagged |
| S9 | Price freezes and energy VAT | on/off | Energy VAT 5.5%: about -11, a lower bound (Montaigne 2024: "more than 11"; RN's own figure -12.2); francebudget.fr's -17.4 is not used (file 07 §3.5). Fuel at 1.70: 0 to -26.5 (oil slider). *(Corrected 2026-10-25, REVIEW.md #2: energy VAT was "-11 to -17.4".)* | Untargeted (Cour) | M | file 07, 11 | |
| S10 | SMIC 1,600-1,700 net | on/off | -1.8 to -4: 1,600 net about -1.8 to -2.2; 1,700 net about -3.5 to -4 (own scaling of Montaigne 2024 to the SMIC in force since June 2026; file 11) *(corrected 2026-10-25, REVIEW.md #3: was "-3.5 to -4")* | Employment effect not costed | M | file 07, 11 | Flagged "illustrative" (our computation) |
| S11 | Immigration-related savings (claims) | on/off | +8 (RN 2024) to +15.1 (RN 2027) claimed; LR +10 | Legal fragility (Constitutional Council 2024-6 RIP); 92% of the RN block "undocumented or legally fragile" (Institut de l'Entreprise) | L | file 07; file 15 §6 | Grey "claim". Context chip: net fiscal contribution +1.02% to -0.85% of GDP (00 row 55); AME 1.34 bn (00 row 54). Overlaps S19 (the AME → AMU line is inside the RN block) |
| S12 | EU contribution cap at EUR 5 bn | on/off | +11.1 claimed (2027). **Ceiling even if legal: 1.4-4.5** (net 6.4 or 9.5 minus 5) | Treaty conflict: Own Resources Decision (unanimity, ratified); legal unilateral yield ≈ 0 | Very low | file 07; file 16 §3; 00 row 52 | Grey "claim"; the control shows the claimed bar next to the 1.4-4.5 ceiling and the verified net contribution (9.5 / 6.4). *(Updated 2026-10-25, 15-18 sync.)* |

**B2. "Popular targets" group (added 2026-10-25, 15-18 sync; file 16)**

| # | Lever | Range | Static (EUR bn) | Behavioral / legal | Conf. | Source | Notes |
|---|---|---|---|---|---|---|---|
| S13 | Development-aid budget mission (programmes 110, 209, 365, 370, 384) | cut 0-100% of 3.17 (PLF 2027 CP) | x% × 3.17 | International commitments; cutting the mission does not cut OECD ODA (12.9) one-for-one | H (budget line) | file 16 §2; 00 row 53 | The PLF 2027 baseline already includes a 0.40 cut vs LFI 2026. Overlap: 0.20 of State payments to associations is aid (S18) |
| S14 | State operators and agencies | 3 positions: Senate structural reform / 8% cut of all staff and running costs / government 2025 figure | 0.54 / 2.2 / 2-3 | 2.2 is "not at constant missions" (Senate); 2-3 has no published method | M / L / grey "claim" | file 16 §4 | Treemap link: most funding is universities, research, training and housing |
| S15 | Strategy and organization consulting | 0-100% | max 0.06 | — | H | file 16 §5 | The slider's maximum shows how small the line now is (Senate 2021: 1.07 on a wider scope) |
| S16 | *Pouvoirs publics* mission + ministerial cabinets | cut 0-50% of 1.3 | max 0.65 | Parliament's and the Constitutional Council's budgets are set by their own bodies | H | file 16 §6 | Presidency 0.123; Parliament 0.98 |
| S17 | Public broadcasting | cut 0-100% of 3.82; or RN "privatize" (claim 1.6) | x% × 3.82 / 1.6 claimed | Privatization brings a one-off sale price, not a recurrent saving; feasibility "uncertain" (Montaigne) | M / grey "claim" | file 16 §7 | External broadcasting (France Médias Monde, TV5) and INA are likely to stay public |
| S18 | State payments to associations | cut 0-20% of 10.5 | x% × 10.5 (10% = 1.05) | Service-delivery cuts (shelters, asylum reception, legal aid) | M | file 16 §8 | iFRAP's 1.6 includes local authorities (outside this lever). Overlaps S13 (0.20) and S11 (immigration associations 0.94) |
| S19 | AME | cut 0-100% of 1.34 (2025 spending); or RN "AME → AMU" (claim 1.3) | x% × 1.34 / 1.3 claimed | No official costing of an emergency-only scheme; *soins urgents* (0.07) and hospital bad debt remain; Évin-Stefanini advised against replacement | L / grey "claim" | 00 row 54; file 15 §6.1 | Credits 1.208 (AME action, PLF 2027) are below actual spending: the line is chronically under-budgeted. Overlaps S11 |

**Macro-feedback mapping by lever (version 1, year 1; "Y3-5" values are used on the "2032" tab).** Values from file 17 §8 (positive = GDP loss per euro of consolidation; same value with the opposite sign for measures that raise spending or cut taxes). "Mapping" = the file 17 category we assign the lever to; where file 17 has no category, v1 uses the official mixed-package value 0.6 (00 row 62) with a ±50% band (file 17 §0 item 9), flagged "fallback".

| Levers | File 17 category | Y1 default (band) | Y3-5 default (band) | Note |
|---|---|---|---|---|
| R1, R2, R4 | Wealth tax on very large fortunes | 0.1 (0.0-0.3) | 0.2 (0.0-0.5) | ⚠ expert proxy, no direct estimate (file 17 §7); R4 (inheritance) mapped here by us, flagged |
| R3, R5, R6 | Corporate surtax, taxes on capital income (and high incomes) | 0.3 (0.1-0.4) | 0.4 (0.2-0.8), long-run warning | OFCE implied: large-firm surtax 0.29, CDHR ≈ 0 |
| R7; S9 (energy VAT cut, fuel freeze: opposite sign) | VAT | 0.3 (0.1-0.5) | 0.5 (0.1-0.8) | Largest model disagreement; show the model's own balance gain as an alternative (file 17 §8). Mapping the fuel-price freeze to VAT is ours, flagged |
| R9, R10 | Income tax or CSG | 0.4 (0.1-0.5) | 0.8 (0.4-0.9) | R9 mapping is ours (most large tax expenditures reduce income or corporate tax) |
| R8 (*année blanche*) | Mix: income tax 0.4 / pension indexation 0.3 / cash benefits 0.5 | 0.4 (0.3-0.5), our midpoint of the components | 0.7 (0.6-0.8), our midpoint | Flagged as our composite |
| R11 | Employer contributions or production taxes | 0.3 (0.2-0.4) | 0.7 (0.6-1.0), rising in the long run | When the behavioral toggle shows the Bozio-Wasmer net yield (48, with -980,000 FTE), the macro toggle adds no second employment effect |
| S3, S14, S15, S16, S17 | Operating spending and public wage bill | 0.8 (0.5-1.1) | 0.7 (0.4-1.0) | |
| S5, S6, S19 | Health and other transfers in kind | 0.8 (0.5-1.0) | 0.7 (0.4-0.9) | |
| S8 | Cash social benefits (working-age, means-tested) | 0.5 (0.3-1.0) | 0.7 (0.4-0.9) | Low-income transfers sit at the top of the band |
| S2 | Pension under-indexation or freeze | 0.3 (0.2-0.5) | 0.6 (0.3-0.8) | |
| S7 | Firms' taxes and subsidies (our mapping: employer-contribution / corporate rows) | 0.3 (0.1-0.4) | 0.4-0.7 | Flagged as our mapping |
| S18 | Operating spending / transfers in kind (our mapping) | 0.8 (0.5-1.0) | 0.7 (0.4-0.9) | Associations deliver services: flagged |
| S12, S13 | EU contribution; development aid | 0 (0-0.2) | 0 | OFCE: "zero or very low" for the EU contribution and development aid (file 17 §3.3) |
| S1 | Pension age (supply measure) | GDP effect 0.0 (-0.1 to +0.1) | GDP +0.3% at 10 years (-0.1% to +1.1%); balance gain +0.4 pt for 2 years (+0.1 to +0.9) | Applied to the pension-system figures only: the "all public finances" figures of file 03 already include induced effects |
| R12, R13, S10, S11 | none | 0.6 (0.3-0.9), fallback | 0.6 (0.3-0.9), fallback | R13 and S11 are claims: the multiplier is applied to the claimed amount only when Toggle 3 is on |
| G1, G2 | n/a | — | — | Growth levers and risk scenarios: no multiplier |

**C. Growth and structural levers (long-run, shown on a separate "2032" tab)**

| # | Lever | Range | Effect | Source | Notes |
|---|---|---|---|---|---|
| G1 | Employment rate | close 0-100% of the gap with Germany (FTE) | up to +38 bn of levies (illustrative; up to 84 in the headcount scenario) | DG Trésor via file 08 | Linear interpolation flagged; policies to get there not costed |
| G2 | Interest-rate shock | -100 to +200 bp | +3.4 bn yr 1, +8.1 bn yr 2 per +100 bp | HCFP §116 | Shown as risk, not as a choice |

### 5.4 Uncertainty bands and toggles

- **Every lever carries a (low, central, high) triplet.** The summary bar shows the total as a band, not a single number. Example: R1 + R7 (+1 pt) + S1 (age 63) = static 20 + 8.2 − 13 = **+15.2**; behavioral 5 + 8.2 − 13 = **+0.2**. With the macro toggle on (year-1 defaults; S1 is a supply measure with no year-1 multiplier): static 20 × (1 − 0.1 × 0.57) + 8.2 × (1 − 0.3 × 0.57) − 13 = 18.9 + 6.8 − 13 = **+12.7**; behavioral 5 × 0.943 + 8.2 × 0.829 − 13 = 4.7 + 6.8 − 13 = **−1.5**. *(Example extended 2026-10-25, 15-18 sync.)*
- **Toggle 1, "behavioral responses":** switches from static to post-behavior values where the research base has them (R1, R2, R5, R11). Elsewhere it shows "no behavioral estimate available".
- **Toggle 2, "short run / long run":** retirement age, contribution relief, employment.
- **Toggle 3, "include party claims not independently costed":** off by default.
- **Toggle 4, "macro feedback" (on by default in v1; replaces "no multiplier applied in v1", 2026-10-25, 15-18 sync).** Source: file 17 §8, verified in primary sources there[^f17].
  - **Rule:** net deficit improvement = measure × (1 − m × 0.57), where *m* is the lever's year-1 multiplier (mapping table in §5.3) and 0.57 is the deficit semi-elasticity to the output gap (CAE Focus 108; 00 row 62). The same rule with the opposite sign applies to measures that raise spending or cut taxes.
  - **Defaults (year 1, band):** operating spending and public wages 0.8 (0.5-1.1); public investment 1.0 (0.6-1.4); health and other transfers in kind 0.8 (0.5-1.0); working-age cash benefits 0.5 (0.3-1.0); pension indexation 0.3 (0.2-0.5); VAT 0.3 (0.1-0.5); income tax and CSG 0.4 (0.1-0.5); employer contributions 0.3 (0.2-0.4); corporate and capital-income taxes 0.3 (0.1-0.4); wealth tax 0.1 (0.0-0.3, proxy); EU contribution and development aid 0 (0-0.2); pension age: GDP 0.0 in year 1, +0.3% at 10 years (-0.1% to +1.1%). Levers with no file 17 category use the official mixed-package value 0.6 with a ±50% band (0.3-0.9).
  - **Display:** the balance meter shows three numbers: static (or behavioral) total, **net after macro feedback (central)**, and the band computed with the low and high multipliers. A one-line GDP effect is shown ("your plan lowers 2027 GDP by about X%", X = 100 × Σ measure × m / 2,991.1). Example: EUR 30 bn of operating-spending cuts nets 30 × (1 − 0.8 × 0.57) = **16.3** (band 11.2-21.5 for m = 1.1-0.5).
  - **Exceptions shown to the user:** for VAT and employer contributions the rule and the models diverge (year-1 balance gain per point of GDP: Mésange employer contributions, rule 0.89 vs model 0.72; e-mod.fr VAT, rule 0.89 vs model 0.5); the lever card shows the model's own balance gain as an alternative (file 17 §8).
  - **Order of operations:** the multiplier applies to the *expected* (behavioral) yield, not to the mechanical yield (file 17 §9 item 5). With Toggle 1 off, the card warns "macro feedback applied to a static yield".
  - **Wording on screen:** "Spending cuts and tax rises both slow growth in the short run; the evidence does not show one type is painless" (Cour des comptes 2026 synthesis, file 10 §6), kept from v1, now with the numbers.
  - **What the simulator must not do (file 17 §8):** present any multiplier as a known constant; show a "self-financing" cut (no source supports m above 1/0.57 ≈ 1.75 in normal times); apply crisis-era values (1.5-2) to 2027. The IMF WEO 2012 range (0.9-1.7) is ⚠ unverified in file 17 and is not shown.
  - **Context toggles (v2):** recession or zero lower bound (spending multipliers × about 1.4, ESCB euro-area variant 0.98 → 1.39); "credible pre-announced path" (shows the zero-multiplier bound assumed in the 2024 PSMT, called "very favorable" by the IGF mission); front-loaded vs gradual (cumulative GDP loss). The Gechert-Rannenberg downturn increase is ⚠ unverified and is not used.
- **Anti-double-counting rules:** R1×R2 (overlapping wealth bases), R8×S2 (pension freeze), R9×R10 (the 10% allowance is a tax expenditure); added 2026-10-25: S11×S19 (the AME → AMU line is inside the RN immigration block), S13×S18 (EUR 0.20 bn of aid flows through associations), S11×S18 (EUR 0.94 bn of immigration-related payments to associations), R11 behavioral × macro (no second employment effect), S1 "all public finances" × macro (already includes induced effects).

### 5.5 Outputs

| Output | Content |
|---|---|
| Balance meter | Gap closed vs the chosen goal, as a band; static / behavioral and **net after macro feedback** side by side (§5.4) |
| Growth effect | Year-1 GDP effect of the plan as a band (Σ measure × m, low and high multipliers), labeled "illustrative, model-based" |
| Yardsticks | Total in days of spending, EUR per inhabitant, % of GDP |
| Structure indicators | PO rate after the choices (base 43.6%); spending ratio (base 57.3%), with the user's position marked in the EU-27 distribution |
| Who is affected | Qualitative tags per lever (retirees, workers, top 1%, firms, families, all consumers); deciles only where an IPP/Insee distributional estimate exists |
| Confidence | Share of the total that comes from H/M/L levers |
| Citation panel | A list of every source used in the scenario, exportable |
| Share card | "My plan closes EUR X-Y bn: Z days of spending", with a link to the exact scenario (URL-encoded) |
| Compare with campaigns | Overlay of each 2027 program's claimed vs independent totals |

### 5.6 Benchmarks

Point to existing simulators in the Trust center and explain the differences: the IPP tax-benefit simulator (micro), the OFCE and iFRAP comparators (file 11 §7). Do not copy their numbers without citation.

---

## 6. The perception-gap quiz

### 6.1 Design

- **Mechanics:** a numeric slider or a multiple choice → reveal → "how others answered" histogram → "why it matters" (2 lines) → source chip → "the strongest objection" (1 line).
- **Modes:** teaser (3 questions), full (25), classroom (anonymous group aggregate), "by electorate" (optional self-reported party proximity, used only for aggregate research with consent).
- **Scoring:** a log-distance score, because orders of magnitude matter more than decimals. A guess within ×1.25 of the true value scores full points.
- **Symmetry rule:** the 25 questions are balanced. Roughly equal numbers correct misperceptions that serve left-wing narratives (wealth-tax yield, the size of business aid), right-wing narratives (fraud, immigration, *assistanat* (welfare dependency), "running costs", number of civil servants) and general pessimism (retirees, bankruptcy, mobility).
- **Data collection:** answers are stored anonymously with GDPR consent (CNIL guidelines). This creates the **first French dataset of numeric budget estimates** and fills the main gap identified in file 14 §10. Publish the results quarterly with methodology, and note that respondents are self-selected (not a representative sample).

### 6.2 Documented misperceptions the quiz exploits (polling evidence)

| # | Belief or answer | Survey (sponsor, pollster, fieldwork, n) | True value | Gap | Source |
|---|---|---|---|---|---|
| 1 | **Debt estimated at 76% of GDP on average**; 37% "don't know"; only 25% say "above 100%" | Ipsos, **18-21 Jan 2021, n = 1,000**, online access panel, quotas. Client: **MINEFI** (Ministry of the Economy and Finance), "to inform the work of the *Commission sur l'avenir des finances publiques*" set up by the Prime Minister on 4 Dec 2020 (Ipsos report, slides "Rappel des objectifs"). Published as *pièce jointe 4* of the Arthuis commission report (submitted 18 Mar 2021), vie-publique.fr report 279092. *(Verified 2026-10-25: was "probable sponsor … not confirmed".)* | 98.2% (end-2019); 114.9% (end-2020, current vintage) | Underestimated by about 22-39 pts | [^ipsos21]; `data/insee_dette_maastricht_1978_2025_by_subsector.csv` |
| 2 | 73% feel poorly informed about the level and cost of the debt | same | — | — | [^ipsos21] |
| 3 | Causes of the debt (up to 3 answers): "bad political choices" 54%, "crises" 50%, "poor management by administrations and local authorities" 45%; "high social protection" **30%**; "lost revenue from certain reforms" **21%** | same | Social protection + health = 57% of TE; tax cuts 2018-2023 = EUR 62 bn/yr | Both structural explanations (social spending and tax cuts) are under-cited | [^ipsos21]; [^ref] |
| 4 | Main source of the debt: State 55%, social security 22%, local authorities 8% | same | Share of Maastricht debt at end-2020: **State 78%**, social security 10%, local authorities 8.5% (computed: 2,089 / 273 / 228 of 2,664 bn) | **The public is broadly right here.** Show this as a "you got it right" moment | [^ipsos21]; `data/insee_dette_maastricht_1978_2025_by_subsector.csv` |
| 5 | Spending to cut first: running costs of the State and public services 67%, social benefits incl. pensions 14%, local authorities 8% | same | Social protection 41.5% + health 15.6% of TE | Cut preferences fall on the smaller items | [^ipsos21] |
| 6 | Cut ranking: family 34%, business aid 33%, unemployment 30% … pensions 7%, health 6%, education 5% | Elabe for *Les Echos*, 1-2 Sep 2026, n = 1,005 | Family 4.0%, unemployment 2.9%, old age 23.4%, health 15.6%, education 8.9% of TE (COFOG 2024) | The most-cited items (family + unemployment) ≈ 7% of TE (business aid excluded: no COFOG line); the protected items (old age + health + education) ≈ 48% of TE. *Old age + health alone = 39%, the figure used in file 14's summary: name the items whenever either number is shown.* | [^elabe26]; file 14 |
| 7 | 79% / 74% find taxing big firms / the wealthiest "effective" against the debt | Elabe for *Les Echos* and Institut Montaigne, 1-2 Oct 2024, n = 1,007 | Wealth taxes: 0.1-0.8 pt of GDP vs an adjustment need of 4.4 pts | Overstated weight | file 14 |
| 8 | **47%** think retirees' living standard is below the population average (57% of 18-24s); **18%** think the French system is funded (capitalization), 9% don't know; **50%** think current contributions will pay today's workers pensions at least as high as today's | **Toluna-Harris Interactive for Observatoire Hexagone** (a think tank favoring a funded pillar: flag its orientation), **online, 21-24 Feb 2025**, n = 1,101 adults 18+, quotas and weighting; released 24 Mar 2025 *(fieldwork dates verified 2026-10-25 in the pollster's report, p. 3)* | 100.2% (COR, 2023); the system is pay-as-you-go; the COR projects the relative living standard of retirees falling to about 90% by 2070 | Pessimism about current retirees; optimism about future pensions | [^hexagone]; [^f03] |
| 9 | 44% think retirees are worse off | Drees Baromètre, Oct-Dec 2025, n = 4,000, face to face | 100.2% | — | file 14 |
| 10 | 72% think taxes have risen since 2017 | Elabe for BFMTV, 4-5 Nov 2025, n = 1,000 | PO ratio 45.3 → 43.6% of GDP; +25.7% in nominal euros; +2.5% after inflation | Wrong as a ratio, right in euros | file 14 §7.1 |
| 11 | 59% contribute more than they receive | Elabe for BFMTV, 2-3 Dec 2025 | 56% are net beneficiaries (Insee, 2023) | Perception vs accounting | file 14 |
| 12 | 60% "close to bankruptcy" | Odoxa for iFRAP (free-market), 3-4 Sep 2025 | Spread 97 bp; ratings A+/Aa3 | Overestimated immediacy | file 14 |
| 13 | 84% / 82% say social / tax fraud is not fought enough | Elabe for BFMTV, Nov 2025 | Realistic marginal yield EUR 1-3 bn | Overestimated recoverable pot | file 14 |
| 14 | Perceived immigrant share 28.8% vs actual 12.2% | Alesina-Miano-Stantcheva, 2018 fieldwork, France n = 4,000 | — | ×2.4 | file 14 |

*Note on the two new sources (rows 1-5 and 8):* the PDFs are saved at `data/raw/20_perception/vp_279092_pj4.pdf` (with the UTF-8 text in `vp_utf8.txt`) and `data/raw/20_perception/hexagone_retraites_2025-02.pdf`, plus the pollster's full report `data/raw/20_perception/toluna/toluna_harris_hexagone_retraites.pdf` (methodology page and result charts). The Ipsos survey is the **only representative French survey found that asks for a numeric budget estimate**. It is five years old, so the quiz should cite it as "the last time anyone asked" and use the platform's own data (§6.4) to update it. The Hexagone report also repeats the "pensions explain half the debt increase" claim (J.-P. Beaufret; F. Bayrou, January 2025). That is **view A** of the contested "hidden deficit" debate (file 03 §5). Do not quote it without view B.

### 6.3 Question bank (25 items; true values from the research base)

| # | Question (French version to be written) | Answer type | True value | Steelman / nuance shown after | Camp challenged | Source |
|---|---|---|---|---|---|---|
| 1 | Out of EUR 100 of public spending, how much goes to pensions (old age)? | slider 0-60 | **23.4** (COFOG 2024); 24.3 (COR concept, 2025) | Pensions are also partly financed by contributions linked to past work | General | [^cofog] |
| 2 | … to health? | slider | **15.6** | Health outcomes are good | General | [^cofog] |
| 3 | … to education? | slider | **8.9** | — | General | [^cofog] |
| 4 | … to defense? | slider | **3.2** | It must rise (NATO) | General | [^cofog] |
| 5 | … to interest on the debt? | slider | **3.8** (2025, ESA) | Not yet exceptional in the EU | General | [^ref] |
| 6 | … to foreign economic aid? | slider | **0.3** (COFOG GF0102, EUR 4.9 bn, 2024) | Not the same as OECD ODA (broader: EUR 12.9 bn = 0.42% of GNI in 2025, OECD-DAC; 00 row 53, file 16) *(corrected 2026-10-25, index pass: was "not verified")* | Right | file 14 §9 |
| 7 | … to the RSA and *prime d'activité* (in-work benefit)? | slider | **2.2** (GF1007) | Child poverty is high | Right | [^cofog] |
| 8 | How many days of public spending does the deficit represent? | slider 0-120 | **32** | — | General | [^conv] |
| 9 | Public debt as % of GDP? | slider 0-200 | **115.7** (end-2025); 119.0 (Q2 2026) | Ipsos 2021: average guess 76% | General | [^ref] |
| 10 | Debt per inhabitant? | choice | **≈ EUR 50,000** | Net worth is positive (+750 bn) | General | [^ref] |
| 11 | The Zucman tax would pay for how many days of public spending? | slider 0-60 | **0.4 to 4.3** | Fairness is a separate question; the very top pays lower effective rates (IPP) | Left | [^conv] |
| 12 | What share of the deficit would a "tax the rich" package close? | choice | **7-16%** | Not negligible: 2-6 times an *année blanche* | Left | file 07 §5 |
| 13 | What does a general return to retirement at 60 cost each year? | choice | **EUR 43-58 bn** *(corrected 2026-10-25, was 35-58)* | Repeal of the 2023 reform alone costs 16-17 bn (2030-2032); partial RN-type versions with 60 for early starters 26-35 bn; the RN's own figure for its 2027 plan is about 9 *(both ranges shown, 2026-10-25)* | Left/RN | [^f03]; [^f11] |
| 14 | Rank of France in the EU for public spending / GDP? | choice | **2nd** (1st 2014-2023) | 8th per inhabitant in PPS | General | [^ref] |
| 15 | Since 2017, have compulsory levies (% of GDP) risen or fallen? | choice | **Fallen (45.3 → 43.6)** | Risen in euros, roughly flat after inflation | Anti-tax | file 14 §7.1 |
| 16 | Share of tax households paying net income tax? | slider | **47.2%** | Everyone pays CSG and VAT | Right | [^f05] |
| 17 | Share of all levies paid by the top 10%? | slider | **33.3%** (2023) | Indirect taxes weigh more on the poorest (64% vs 48% of income, 2022) | Both | [^f05] |
| 18 | Share of people who receive more than they pay (incl. public services)? | slider | **56%** | Part of it is debt-financed | Anti-tax | [^f14] |
| 19 | Retirees' living standard vs the average? | choice | **About equal (100.2%)** | Projected to fall to about 90% by 2070 | Pessimism | [^f03] |
| 20 | Share of jobs in the civil service? | slider | **≈ 20%** (19.8%, DGAFP/Insee, civil-service perimeter incl. subsidized contracts, 2024; 20.7%, OECD general-government definition, 2023) *(corrected 2026-10-25, REVIEW.md #6: was "19.8% SIASP")* | Sweden 28%, Germany 11.5% (definitions differ) | Right | [^f04] |
| 21 | Realistic extra yield of a new anti-fraud plan per year? | choice | **EUR 1-3 bn** | Social fraud is estimated at about 13 bn (12.98, HCFiPS 2024), about 14 bn in the Dec 2025 update (00 row 59); the recoverable share is small | Right | [^f07] |
| 22 | How much is "aid to business"? | choice incl. "it depends" | **"It depends": 45 to 211 bn** | Definitions | Left | [^f08] |
| 23 | Where does France rank for hours worked per inhabitant? | choice | **Last of 27** | Hours per worker are higher than in DE and NL | Pessimism / left | [^f08] |
| 24 | In 2027, which is larger: State interest or the defense programming budget? | choice | **Interest (72.9 vs 63)** | Budget accounting, State only | General | [^f06] |
| 25 | What explains most of France's spending gap with the euro area? | choice | **Social protection + health (about two-thirds)** | Per inhabitant, the gap is smaller | Right ("bureaucracy") | [^ref] |

**Rotation pool (items 26-40; items 26-35 added 2026-10-25 in the 15-18 sync, items 36-40 added the same day to balance the pool).** The full quiz still shows 25 questions; items are drawn from the 40-item bank (`platform/data/quiz.json`: 25 core + 15 rotation) under the symmetry rule (§6.1): every draw contains exactly as many left-coded as right-coded items (`draw_rule` in quiz.json). Items 26-32 are mostly right-coded because files 15-16 cover right-coded targets; items 33-35 and the left-coded items 36-40 rebalance them.

| # | Question | Answer type | True value | Steelman / nuance shown after | Camp challenged | Source |
|---|---|---|---|---|---|---|
| 26 | How much does France pay the EU budget, net of what it gets back (2025)? | choice | **EUR 9.5 bn** (accounting method); 6.4 bn (Commission method) | 2nd-largest net contributor in euros; the gross levy is 23.0 bn (2025) and 30.9 bn (PLF 2027). A 5 bn cap would save at most 1.4-4.5 bn, even if legal | Right (sovereigntist) | 00 row 52; file 16 §3 |
| 27 | Out of EUR 1,000 of public spending, how much goes to State medical aid for undocumented migrants (AME)? | slider 0-50 | **about EUR 0.8** (1.34 bn = 0.08% of TE, 2025) | Credits are under-budgeted (1.208 bn in PLF 2027 vs 1.34 bn spent); beneficiaries 454,111 | Right | 00 row 54; file 15 |
| 28 | What do the Presidency, Parliament and all ministerial cabinets cost per year? | choice | **about EUR 1.3 bn** (0.08% of TE; EUR 19 per inhabitant) | Gross pay only; no official full-cost figure | Populist (both) | file 16 §6 |
| 29 | What could reorganizing State agencies save each year, according to the Senate's inquiry? | choice | **about EUR 0.54 bn** (government 2025 claim: 2-3 bn, method not shown) | Operators receive 72.6 bn, but mostly for universities, research, training and housing | Right | file 16 §4 |
| 30 | France's development aid as % of national income, and its rank among 33 donors? | slider 0-2% + choice | **0.42% of GNI, 11th of 33** (2025, OECD-DAC) | The budget mission is only 3.17 bn; ODA includes loans, the EU share and refugee costs | Right | 00 row 53; file 16 §2 |
| 31 | Do immigrants cost or contribute to French public finances? | choice incl. "it depends" | **"It depends on the convention": +1.02% to -0.85% of GDP a year** (OECD, 2006-18) | Per head, the foreign-born contribute less than natives; on the least favorable convention natives look worse in total (deficit years) | Right (and pro-immigration claims of a large surplus) | 00 row 55; file 15 |
| 32 | Is France's tax burden 42.7%, 43.5% or 44.3% of GDP? | choice incl. "all three" | **All three, by definition** (Insee PO 2024 / OECD 2024 / ESA-OECD concept 2025, Cour) | +0.7 pt = refundable tax credits counted as spending; never rank Insee's figure against OECD figures | General (methodology) | file 18 §1 |
| 33 | How much did the State spend on strategy consulting in 2025? | choice | **about EUR 60 m** (271.5 m in 2021) | The Senate's "over EUR 1 bn" (2021) covered all intellectual services | Left (the 2022 consultancy controversy) | file 16 §5 |
| 34 | The 20% minimum tax on top incomes (CDHR) was announced at about EUR 2 bn. How much did it raise in 2025? | choice | **under EUR 0.4 bn** | Timing effects may raise later yields (IPP) | Left | file 07 (§4.10 above) |
| 35 | A EUR 30 bn cut in operating spending: how much does the deficit fall in year 1? | choice | **about EUR 16 bn** (multiplier 0.8, band 11-21) | Tax rises also slow growth; French models and narrative studies disagree on which costs more | Both ("cuts are painless" and "tax rises are painless") | file 17 §8; §4.18 |
| 36 | The tax and contribution cuts decided in 2018-2023 (EUR 62 bn a year, valued in 2023): what share of the 2025 deficit? | choice | **about 41%** (62 / 151.6) | Measured from 2017, lower revenue explains the whole rise in the deficit (revenue -3.1 pt of GDP, deficit +2.4 pt, Eurostat 2017-2024); part of the cuts has since been reversed (Rexecode: EUR 36.7 bn of new levies 2024-2026) | Left ("the tax cuts since 2017 explain the whole deficit") | 00 rows 28, 31; files 08, 10 |
| 37 | Between 2019 and 2025, did public spending rise or fall as a share of GDP? | choice | **Risen by 2.0 pt of GDP** (revenue -0.8 pt; Eurostat) | The answer depends on the base year: 2017-2024, spending -0.7 pt and revenue -3.1 pt; a ratio to GDP also rises when growth slows | Left ("public spending has been cut") | file 10 (K10) |
| 38 | Restoring the 2017 wealth tax (ISF): how many days of public spending would it fund each year? | choice | **Less than 1 day** (EUR 3-4.5 bn gross, CAE; 0.64-0.96 day) | Yield is not the only argument (fairness at the top); the CAE finds limited tax-motivated departures after 2013 | Left ("restoring the ISF would restore public finances") | file 07 [S5] |
| 39 | From 2024 to 2026, how much in new compulsory levies was decided (Rexecode count)? | choice | **EUR 36.7 bn** (1.2 pt of GDP); Cour des comptes: 23.0 bn of increases in 2025 alone | The reversal is partial: 1.2 of the 2.7 pt of GDP of cuts since 2014 by the same count; the Cour's 62 bn of 2018-2023 cuts is larger | Left ("the cuts since 2017 have never been reversed") | file 08; Cour des comptes[^cour26] |
| 40 | Counting all direct taxes (incl. corporate tax on firms they own), what effective rate did the richest 0.1% pay in 2016? | choice | **about 46%** (IPP, 2016 data) | About 26% for the ~75 richest households (IPP); F. Geerolf (OFCE, not peer-reviewed) contests it: 25.1% for billionaires vs 26.8% at the top-10% threshold on a homogeneous base | Left ("the rich pay little tax") | file 05 |

### 6.4 Commission a representative numeric-estimate survey (recommended)

- **Sample:** n ≥ 2,000, quota or probability sample, preferably two waves (before the campaign, and after the first round in April 2027).
- **Items:** questions 1-13 above, plus "would it balance the budget?" for each proposal.
- **Randomized information arm:** half the sample sees the yardstick before answering policy questions. This replicates Kuziemko et al. (2015) for France.
- **Publication:** pre-register the design; publish the questionnaire, the microdata and the results whatever they show.
- **Expected value:** it fills the gap in file 14 §10 and is a publishable public good, cited by the media.

---

## 7. Credibility safeguards

### 7.1 Mechanisms

| Safeguard | Implementation |
|---|---|
| **Source on every number** | The number-card component cannot render without `source_id`, `data_year`, `denominator` and `vintage`. Source chips deep-link to the table (Eurostat databrowser, Insee page, PDF page anchor). |
| **Canonical file** | One machine-readable `reference_figures.json` generated from `00-reference-figures.md`. Pages pull values from it; nothing is typed by hand into a page. The "superseded values" list (file 00 §4) is enforced by a build-time check that fails if a superseded value appears. |
| **Methodology pages** | One per concept: ESA 2010 vs budget accounting; PO vs OECD tax-to-GDP vs ESA total revenue (bridge: §4.17); the three interest figures (65.7 / 64.7 / 51.6, §4.17); COFOG vs SHA health (§4.17) vs Drees CPS vs ESSPROS; PPS; EA20 vs EA21; gross vs net SOCX; static vs behavioral vs macro-feedback costing (§4.18, §5.4); "conventions decide the sign" for the immigration net contribution (§4.15). |
| **Versioning** | Each page shows "data as of [date], vintage [X]". A public Git repository holds the data, scripts and changelog. Each release is tagged (for example `2027.03-insee-first-estimate`), and old versions remain reachable. |
| **Ranges** | Contested costings always use the range bar with authors at each end. |
| **Disagreements** | A Debates page and an inline steelman box. Orientation labels: OFCE (Keynesian-leaning, Sciences Po), Rexecode (employer-funded), Institut Montaigne (business-funded, liberal-centrist), iFRAP (free-market), Terra Nova (center-left), Fipeco (independent, former Cour magistrate, fiscally orthodox), Observatoire Hexagone (favors a funded pension pillar), Institut de l'Entreprise (business-funded), Attac (alter-globalist NGO), Clersé for IRES/CGT (union-commissioned). |
| **Poll hygiene** | Never quote a sponsored poll without its sponsor, wording, n and fieldwork dates (file 14 §9). |
| **Right of reply** | Before publishing a program card, send the costing to the campaign with a 7-day reply window. Publish the reply verbatim (with a length cap). |
| **Corrections log** | A public page listing each error, date, fix and impact. A correction is never silent. |
| **Scientific committee** | 4-6 economists from different schools (for example OFCE, IPP, CAE alumni, a former Cour magistrate, a market economist), named publicly. They review the methodology, not each sentence. |
| **Red-team review** | Before launch, two reviewers, one left-leaning and one right-leaning, try to find bias. Publish their reports. |
| **Funding transparency** | List every funder above a threshold; no party, campaign or single-interest funding; a conflict-of-interest policy for authors. |
| **Neutral vocabulary guide** | Use "spending" (*dépense*), not "waste" (*gaspillage*); "levies" (*prélèvements*), not "fiscal bludgeoning" (*matraquage fiscal*); "tax expenditures" (*dépenses fiscales*), not "loopholes" (*cadeaux*); "the very wealthy", not "the parasites" or "the job creators". |
| **Symmetry audit** | A quarterly count of how many pages challenge left-coded vs right-coded claims, published in the Trust center. |
| **Uncertainty language** | A fixed scale: "measured" (official statistics), "estimated" (institutional estimate), "projected" (forecast), "claimed" (party), "illustrative" (our computation). |

### 7.2 Editorial charter (draft, 10 articles)

1. We publish orders of magnitude, not voting advice.
2. Every figure is sourced, dated and labeled with its denominator.
3. Official statistics (Insee, Eurostat, OECD, Drees, Cour des comptes, HCFP, COR) come first. Think tanks are cited with their orientation.
4. Where experts disagree, we show the range and name the authors.
5. Every key message is published with the strongest counter-argument we know.
6. We treat all parties' proposals with the same method and the same template.
7. We distinguish facts (sizes, yields) from values (fairness, priorities), and we do not arbitrate values.
8. We correct errors publicly and quickly.
9. We give campaigns a right of reply.
10. Our data and code are open.

### 7.3 Pre-empting bias accusations (anticipated attacks and answers)

| Attack | Pre-emptive answer on the site |
|---|---|
| "Neoliberal propaganda against the social model" | The steelman boxes on SOCX net spending, poverty reduction, PPS rankings and the tax cuts since 2017 are visible on the first screens, not buried. The thesis is framed as "spending must contribute substantially", not "spending is the only lever" (HCSP finding). |
| "Leftist: you attack the RN and LR claims" | The same treatment is applied to the Zucman tax, the ISF and business aid; a published symmetry audit. |
| "Your numbers are wrong" | Source chips, open data, a corrections log, canonical vintages. |
| "You cherry-pick 2017" | Base-year slider (§4.11). |
| "Funded by X" | Funding page. |

---

## 8. Accessibility and mobile

| Area | Requirement |
|---|---|
| Standard | **RGAA 4.1** (the French public-sector accessibility reference, based on WCAG 2.1 AA) as the target, with an accessibility statement page. |
| Charts | Every chart has (a) a text summary of its message in one sentence, (b) a "see the data" table toggle, (c) a downloadable CSV. Never encode by color alone: use patterns and direct labels. Use a color-blind-safe palette (validated), with contrast ≥ 4.5:1 for text and ≥ 3:1 for graphical elements. |
| Interactions | Sliders are keyboard-operable (arrows, Page Up/Down), with ARIA value text that reads the formatted value ("EUR 20 billion, 4.3 days of spending"). Minimum touch target 44 × 44 px. Focus states are visible. |
| Motion | Respect `prefers-reduced-motion`: scrollytelling becomes stepped static panels. No autoplay. |
| Language | Plain French (target: B1 reading level for main text). A *FALC* (*facile à lire et à comprendre*, easy-read) summary for each chapter. A glossary tooltip for every technical term (PO, COFOG, ONDAM, AOD…). |
| Numbers | French formatting (*1 714 milliards d'euros*; decimal comma), and "billion" wording that is never ambiguous ("milliard" vs "billion"). Always round consistently (one decimal for % of GDP). |
| Mobile | Mobile-first: vertical scrollytelling; one chart per screen; charts simplified to the top 8 items plus "others"; a simulator with a sticky balance meter at the bottom; levers grouped in collapsible accordions. |
| Performance | Page weight < 1 MB initial, charts lazy-loaded, works on 3G; server-side rendered text so content is readable without JavaScript. |
| Sharing | Auto-generated share cards (image) that **embed the source and date in the image**, so screenshots stay sourced. |
| Classroom | Printable PDF worksheets; quiz in "class mode" with no login. |

---

## 9. Maintenance plan

### 9.1 Data refresh calendar (recurring)

| Month | Release | What changes on the site | Owner action |
|---|---|---|---|
| **Late March** | Insee first estimate of the public accounts (deficit, debt, PO, TE for year N-1); Insee quarterly debt (Q4) | Headline numbers, yardstick constants, household metaphor | Regenerate `reference_figures.json`; new vintage tag |
| **~22 April** | Eurostat April EDP notification | EU rankings for deficit and debt | Re-run the Eurostat scripts |
| **Late May** | Insee detailed public-accounts publication (*compte des APU*, May vintage, revisions) | Revised TE/GDP, interest, PO | Check the superseded list |
| **June** | COR annual report; Cour des comptes *RSPFP* (state and outlook of public finances, late June); Insee quarterly debt (Q1) | Pensions page, debt-stabilizing gap (simulator goal A) | Update the S1 lever if the COR changes its projections |
| **July** | Insee poverty (ERFS); IGF/HCSP reports (variable); NATO defense figures | Outcomes, defense pressure | |
| **Late Sept** | Drees health accounts; OECD *Education at a Glance*; Insee quarterly debt (Q2); HCFP opinion on the PLF | Health and education pages | |
| **~1 October** | **PLF/PLFSS** (budget and social-security bills); CCSS report; PAP programme 183 (AME); HCFP opinion (multiplier assumption) | Forecasts N and N+1, interest path, package size, staffing plan, AME, macro-feedback working value | Major refresh of the simulator baseline |
| **Mid-October** | PLF *Jaunes* (EU financial relations, operators, consulting, ministerial cabinets, associations) | "Easy savings" cards and levers S12-S19 | Save the PDFs and xlsx annexes (browser-only downloads) |
| **~21 October** | Eurostat October EDP notification; ESSPROS early estimates | Canonical deficit and debt (October vintage) | New vintage tag |
| **Nov** | OECD *Pensions at a Glance* (biennial, odd years); DGFiP income-tax statistics | Pensions international comparison, IR concentration | |
| **December** | **Drees *La protection sociale en France et en Europe***; **OECD *Revenue Statistics***; Insee COFOG tables (N-1); Insee quarterly debt (Q3) | Social protection, tax-to-GDP ranking, COFOG preliminary | |
| **Feb-March** | Eurostat COFOG release; Cour des comptes annual public report | Budget calendar, EUR 1,000 breakdown, gap decomposition | |
| **April** | OECD *Taxing Wages*; DG TAXUD *Taxation Trends* (end of March); OECD-DAC preliminary ODA data | Tax wedge; development-aid card and quiz item 30 | |
| **Irregular** | PISA (next cycle after 2025); TIMSS/PIRLS; CEPEJ (October of even years); OECD *Government at a Glance* (odd years); EC Ageing Report (triennial) | Outcome strips | |

### 9.2 Campaign-period plan (October 2026 → May 2027)

| Period | Cadence |
|---|---|
| Now → March 2027 | A program card is updated within 7 days of any costed announcement; a weekly "proposal checker" digest |
| March 2027 | Insee first estimate for 2026 → full number refresh **before** the first round (April 2027) |
| Two weeks before each round | A content freeze except for corrections, so no new costing appears without time for replies |
| After the election | Archive the 2027 program cards (permalinks kept) |

### 9.3 Process

- **Automated pulls** (Eurostat and OECD SDMX APIs) run in CI. A diff report flags any value change above 0.1 pp or 1%, and a human verifies before publication.
- **Two-person rule:** every figure change needs an author and a reviewer.
- **Quarterly content audit:** link checks (many PDF URLs move), the symmetry audit and the accessibility audit.
- **Annual methodology review** with the scientific committee.

---

## 10. Data inventory for the platform (by page)

| Page / tool | Files (under `research/data/`) | Primary sources |
|---|---|---|
| Yardsticks and household view | `20_pedagogical_conversions.csv`; `eurostat_gov_10a_main.csv`; `eurostat_tps00001_population.csv` | Eurostat, Insee |
| Budget calendar, EUR 1,000 breakdown | `eurostat_gov_10a_exp_pctot.csv`, `eurostat_gov_10a_exp_mioeur.csv`, `00_reconcile_cofog_gap_2024_EA20_EA21.csv` | Eurostat COFOG |
| Europe comparison | `09_intl_*.csv`, `09_intl_fr_gap_timeseries.csv`, `eurostat_nama_10_pc_gdp_pps_per_capita.csv` | Eurostat, OECD |
| Social protection | `eurostat_spr_exp_func.csv`, `esspros_*.csv`, `oecd_socx_totals.csv` | Drees, Eurostat, OECD |
| Pensions | `pensions_*.csv`, `08_eurostat_proj_23ndbi.csv` | COR, Eurostat, OECD |
| Health | `12_*.csv` | Eurostat SHA, OECD, WHO, Drees |
| Civil service and education | `13_*.csv`, `04_*.csv` | DGAFP, OECD, Eurostat, IEA |
| Taxation and receipt | `insee_t_3216_T_3216.csv`, `insee_t_3217_T_3217.csv`, `insee_taux_prelevements_obligatoires_1959_2025.csv`, `oecd_revenue_statistics_2025_pct_gdp.csv`, `14_factcheck_PO_2017_2025_real.csv` | Insee, OECD |
| Deficit, debt, interest | `insee_dette_maastricht_1978_2025_by_subsector.csv`, `derived_06_*.csv`, `eurostat_gov_10dd_edpt1_deficit_debt_interest.csv`, `eurostat_irt_lt_mcby_m_10y_yields_monthly.csv` | Insee, Eurostat, Cour, HCFP |
| Base-year slider | `debates/computed_fr_vs_eu27_fiscal_series.csv` | Eurostat |
| Simulator levers | `11_candidate_measures.csv`; files 03, 05, 07, 08, 11, 12 tables | as per lever |
| Quiz | `14_perception_surveys.csv`; `raw/20_perception/*` | Pollsters as listed |
| Employment | `08_eurostat_lfsi_emp_a.csv`, `08_eurostat_nama_10_lp_ulc.csv` | Eurostat, OECD |
| Immigration and AME (§4.15) | `15_oecd_fiscal_immigration_stats.csv`, `15_conversions_eur_2025.csv`, `15_eurostat_foreign_born_share.csv`; `raw/15/`; `raw/16_factcheck/evin_stefanini_292122.pdf` | OECD IMO 2021, CEPII, PAP 2027 programme 183, Évin-Stefanini |
| "Easy savings" targets (§4.16, S13-S19) | file 16 tables; `raw/14_verify2/oda_*.xlsx`; `raw/11_verify2/ec_eu_budget_2000-2025.xlsx`; `raw/16/browser_extracts_2026-10-25.txt` (Jaunes transcribed from a browser session) | OECD-DAC, PLF 2027 and its *Jaunes*, European Commission, Senate reports 578 and 807 |
| Methodology bridges (§4.17) | `18_po_vs_oecd_bridge_2024.csv`, `18_interest_bridge.csv`, `18_cofog_vs_sha_health_2024.csv`; `raw/18/` | Insee tables 3.201-3.217, Eurostat, OECD |
| Macro feedback (§4.18, §5.4) | file 17 §8 defaults table (no CSV yet); `raw/17_multipliers/` | HCFP, CAE, Mésange, OFCE, ESCB, Banque de France |

---

## 11. Gaps and items to verify before publishing

1. ~~**Ipsos 2021 sponsor attribution.**~~ **Resolved 2026-10-25:** the Ipsos report names MINEFI as client and the commission on the future of public finances as the purpose, and vie-publique.fr lists it as attachment 4 of the Arthuis commission report (see the verification log).
2. **COR "24.3% of TE" vs computed 24.6%** (422.2 / 1,714.1): unresolved denominator (file 03). The site should use 23.4% (COFOG old age, 2024) for "share of the budget" and 14.1% of GDP for the COR concept, and avoid 24.3% unless the denominator is explained.
3. **Public headcount lever (S4).** It needs an average fully loaded cost per FTE (DGAFP/Insee), which is not in the research base.
4. ~~**Macro multipliers** for the simulator v2 must be read from Guajardo-Leigh-Pescatori and the Cour 2026 synthesis, with values verified.~~ **Resolved 2026-10-25 (15-18 sync):** file 17 read them in primary sources; defaults by instrument are now in v1 (§5.3 mapping, §5.4 Toggle 4). Remaining caveats: the wealth-tax multiplier is an expert proxy (no direct estimate); the IMF WEO 2012 range (0.9-1.7) and the Gechert-Rannenberg downturn increase are ⚠ unverified and not shown; the European Commission's own semi-elasticity for France was not re-read (file 17 §8-§9).
5. ~~**Net fiscal cost of immigration** and **OECD-DAC ODA**: not verified.~~ Resolved 2026-10-25 (index pass): both are now verified in primary sources (00 rows 53 and 55; files 14, 15, 16).
6. **PLF 2027 tax-expenditure sums:** the annex 1 sums (91.7 / 92.0 / 83.9 bn, 459 items) were verified by file 05 against the re-downloaded spreadsheet (2026-10-25), but they are sums of items, not an official total. Keep the Cour des comptes total of 91.83 bn (2025) as the headline (00 row 56). *(Updated in the index pass: was "⚠ unverified, raw file not saved")*
7. ~~**October 2026 market data** (OAT above 5%, spread about 170 bp): replace with Banque de France or AFT end-of-day data before publication (file 06).~~ **Resolved (index pass, 00 log #29):** official values are now canonical: 5.126% on 22 Oct 2026, spread 169 bp (22 Oct) / 166 bp (23 Oct) (00 row 43).
8. **Insee 2025 COFOG** (December 2026) will replace every 2024 functional share; the budget calendar must be regenerated then.
9. **Drees 2026 edition of the social protection accounts** (expected December 2026) will replace the 31.9% / 2024 figures with 2025 data.
10. **Program costings**: none are independent yet. Check the IPP, OFCE, Montaigne, Fipeco and the Cour des comptes monthly.
11. *(added 2026-10-25, 15-18 sync)* **File 16 *Jaunes* transcribed from a browser session** (operators, cabinets incl. the 154.7 m own sum, consulting, associations, EU p. 149-158): save the PDFs/xlsx before publishing cards §4.16 and levers S14-S18 (file 16 §14).
12. *(added 2026-10-25)* **AME:** the press "about EUR 1.2 bn (2023)" stays unused (use the programme 183 RAP 2023); the Senate's EUR 200 m AME cut in the PLF 2026 debate does not appear in the LFI 2026 credits (⚠ to confirm against the LFI 2026 text); reported October 2026 committee votes on AME credits are ⚠ unverified (file 15 §10).
13. *(added 2026-10-25)* **No official total of non-contributory benefits paid to foreign nationals** exists, so "national preference" savings cannot be costed (file 15 §6.3, §10). Lever S11 stays a grey claim.
14. *(added 2026-10-25)* **`data/20_pedagogical_conversions.csv`** does not yet contain the rows added in §3.4 (15-18 sync) or the macro-feedback mapping (§5.3); regenerate it before the build-time check (§7.1) relies on it.
15. *(added 2026-10-25, REVIEW.md pass)* **Resolved here:** the source of each end of S3, the S5 default (+3.4%, with markers) and the two ranges of the `rn_back_to_62` card (see the verification log). **Still open:** no DGAFP primary for the index-point cost; the Cnav note behind the repeal cost (15.7 bn in 2032) is not public and is cited through Assemblée nationale report no. 613; `platform/data/simulator-levers.json` (S5 `default` is still null) and the front end of the `rn_back_to_62` card must be updated by their owners.

---

## Verification log

### Pass of 2026-10-25 (README §7 and §8 follow-up)

**A. ⚠ items from README §7 (row 20)**

| Item | Outcome | Evidence |
|---|---|---|
| Ipsos 2021 sponsor (commission on the future of public finances) | **Confirmed.** The client is MINEFI, and the survey was commissioned "to inform the work of the *Commission sur l'avenir des finances publiques*" (Ipsos report, "Rappel des objectifs"; footer "© Ipsos \| MINEFI"). The PDF is *pièce jointe n° 4* of the Arthuis commission report (submitted 18 Mar 2021). The PDF metadata title is "PJ N4-1 Etude d'opinion", created 19 Mar 2021. | `data/raw/20_perception/vp_utf8.txt` (lines about 824-845); report page https://www.vie-publique.fr/rapport/279092-commission-sur-lavenir-des-finances-publiques (read in the laptop browser; the old short URL /rapport/279092 now returns a 404) |
| Observatoire Hexagone poll fieldwork dates | **Confirmed: online, 21-24 Feb 2025**, n = 1,101, quotas plus weighting. The pollster is now styled Toluna-Harris Interactive. The headline figures were re-checked in the pollster's charts: 47% "less good" (57% among 18-24s), 18% "funded system", 9% "don't know", and 72% who correctly describe pay-as-you-go. | Toluna-Harris report p. 3, 9-10; `data/raw/20_perception/toluna/toluna_harris_hexagone_retraites.pdf` |

**B. ⚠ flags resolved in other files and checked here**

| Item | Status in this file |
|---|---|
| Ifop 86% (Zucman tax) | Confirmed in file 14 (Ifop no. 121870, 10-11 Sep 2025, n = 1,000). Citation added in §4.10. |
| PISA 2025 (458 vs 463, 29th of 38) | Already canonical (file 00 row 49; file 13). No change was needed. |
| PLF 2027 staffing plan (+8,025 / +4,742 FTE) | Confirmed in file 13 against bill no. 3210, Art. 63. Note added in §4.6. |
| "87% badly used / not transparent" (§0 item 5, previously unsourced here) | Confirmed in file 14 (Elabe/BFMTV, 2-3 Dec 2025, n = 1,000). Citation added. |

**C. Alignment with file 00 (README §8 and the same checks applied to this file)**

| Location | Change |
|---|---|
| §4.2 GF02 Defense | 1.9% → **1.8% of GDP** (§8 #5; file 00 row 15). |
| §4.1 key message | The year (2025) and aggregate (EA21, with EA20 in brackets) are now stated for the 7.6 pp / 227 bn gap. The "two-thirds / one-third" split is now labeled as the **2024 COFOG** decomposition of a 7.8 pp gap (§8 #1-2 logic; file 00 rows 7-9). The SOCX year is now given (2021). |
| §4.3 key message | The source (Drees 31.9% vs Eurostat 32.0%), the year, the EU-27 aggregate (27.4%) and the ranks (2nd in 2024, 3rd in 2025e) are now stated (§8 #3, #7; file 00 rows 20-21). |
| §4.4 | Old-age share of the gap now reads "+2.5 of 7.8 pp vs EA21, COFOG 2024". |
| §4.8 | Debt gap now reads "-2.0 (2005) → +28.4 pp (2025) vs EA21; EA20 -2.1 / +28.0" (file 00 row 38). |
| §4.11 | Windows now labeled: ESA TR -3.1 pp over **2017-2024**; spending +2.0 / revenue -0.8 over **2019-2025**. |
| §6.2 row 6 | The items behind "≈ 7%" and "≈ 48%" are now named, with the 39% variant explained (§8 #8). |
| Already consistent | TE per capita 23,330 PPS, 8th (2025); PISA 2025; deficit 151.6 bn; debt 3,460.1 bn; interest 65.7 bn; PO 2024 42.7%. |

**D. Still open (owned elsewhere)**: the PLF 2027 tax-expenditure sums (file 05). Recommendation: replace them with the Cour des comptes total of 91.83 bn. The October 2026 intraday market data (file 06) is not used in this file's figures. `data/20_pedagogical_conversions.csv` was not edited in this pass, and none of its values changed.

### Pass 2026-10-25 – sync with files 15-18

*Scope: files 15, 16, 17, 18 and file 00 (rows 52-62, log #23-37, §4 superseded values) were read; this file was grepped for every superseded value of file 00 §4 and for each canonical row 52-62. Only this file was edited. Derived yardsticks use days = EUR bn / 4.696 (1,714.1 / 365), % of deficit = EUR bn / 151.6, EUR per inhabitant = EUR bn × 1,000 / 68.998.*

**A. Corrections of values (superseded or imprecise)**

| Location | Was | Now | Basis |
|---|---|---|---|
| §4.14 Local government (deficit by subsector) | social security **6.7** | **5.8**; shares added (State 84.5%, ODAC 1.5%, local 10.3%, social security 3.8% = 5.8 / 151.6); parts sum to 151.7 by rounding | 00 §4 and log #27; file 06 row 4 |
| §4.10 EU-cap card; §5.3 S12 | "11.1 (2027) claimed"; no verified net figure; empty steelman | claim 11.1 → 19.5 explained (whole RN "EU" block); **net 9.5 / 6.4 bn (2025)**; **ceiling 1.4-4.5 bn even if legal** (6.4 − 5; 9.5 − 5); yardsticks 2.4 days / 7.3% / EUR 161 (claim) vs 0.3-1.0 days / 0.9-3.0% / EUR 20-65 (ceiling); steelman added | 00 row 52, log #31; file 16 §3; file 11 |
| §4.10 Immigration card | "8 (Montaigne's view of the claims)"; AME 1.34 only | 8 = the RN's own 2024 figure as reported by Montaigne; claims itemized (11.9; 15.1 → 29.0; LR 10); **AME 968 m (2022, Évin-Stefanini primary)**, credits 1.208 bn (action) / 1.216 bn (programme 183), 454,111 beneficiaries; net contribution in EUR (+30.5 to -25.3 bn, illustrative); legal chip 2024-6 RIP | 00 rows 54-55, log #32; file 15 §0, §4, §6 |
| §4.10 Anti-fraud card; quiz item 21 | "about EUR 13 bn (HCFiPS, secondary source)" | about 13 bn (12.98 = 7.25 + 5.73, primary), about 14 bn (Dec 2025); error items not added | 00 row 59 |
| §4.3 Social protection | EUR 932.5 bn with no vintage note | 932.5 kept as the published Drees value; semi-final 933.2 bn (31.8% on current GDP) noted; 199 days re-computed on both (198.6 / 198.7) | 00 row 20, log #25 |
| §5.4 Macro feedback | "No multiplier is applied in v1" | Toggle 4 on by default, defaults and bands by instrument, rule × (1 − m × 0.57), example re-computed (+12.7 static, −1.5 behavioral) | 00 row 62; file 17 §8 |
| §11 items 4 and 7 | open | resolved (file 17; 00 row 43 / log #29) | |
| §0 item 4(c), §0 item 5 | simulator without macro feedback; symmetric list without the EU contribution and aid | updated | |

**B. Additions**

| Location | Addition | Source |
|---|---|---|
| §0 item 7 | Summary of the 15-18 sync | files 15-18 |
| §2.1, §7.1 | Methodology page scope extended (interest figures, COFOG vs SHA, macro feedback, immigration conventions) | file 18; file 17; file 15 |
| §3.1 | Constants: 1 pt of GDP ≈ EUR 30 bn; macro-feedback rule (× 0.658 at m = 0.6) | 00 row 62; file 17 |
| §3.4 | 18 new conversion rows (EU, ODA, AME, immigration, operators, agencies, consulting, *Pouvoirs publics*, broadcasting, associations, the 29.4 bn total, social fraud, the 14.1 bn interest gap) | files 15, 16, 18; 00 rows 52-59 |
| §4.2 GF07 | SHA gap (+1.06-1.10) and "1 to 1.5 points" wording | file 18 §3; 00 log #35 |
| §4.4 | Pension-age macro range (GDP -0.1% to +1.1%; balance +0.1 to +0.9 pt) | file 17 §3.5 |
| §4.7 | One-line PO vs OECD bridge; never rank Insee PO against OECD (would show 4th instead of 2nd); 2025 ESA/OECD concept 44.2-44.3% | file 18 §1; 00 log #33 |
| §4.9 | Three interest figures (65.7 / 64.7 / 51.6) and the 14.1 bn understatement | file 18 §2; 00 row 39, log #34 |
| §4.15 | Immigration and AME card | file 15; 00 rows 54-55 |
| §4.16 | "Easy savings" cards: ODA, EU, operators, consultancies, politicians, broadcasting, associations, AME | file 16 |
| §4.17 | Methodology page: three bridges | file 18 |
| §4.18 | Macro-feedback explainer | file 17 |
| §5.1-§5.3 | Design goal 4; goal row "gross measures needed" (≈ 94 for goal B: 61.9 / 0.658); levers S13-S19; macro mapping table for every lever | files 16, 17 |
| §5.4-§5.5 | Toggle 4 specification; new anti-double-counting rules; growth-effect output | file 17 |
| §6.3 | Rotation pool, items 26-40 (36-40 added 2026-10-25, left-coded), with a symmetry rule for draws | files 15-18, 07, 05, 08, 10; `platform/data/quiz.json` |
| §9.1 | PLF *Jaunes* (mid-October), PAP 183, OECD-DAC (April) | file 16 |
| §10, §11 | Data inventory rows; gaps 11-14 | files 15-18 |

**C. Checked and unchanged**

| Value in this file | Check |
|---|---|
| Deficit 151.6 bn, debt 3,460.1 bn, interest 65.7 bn, PO 2024 42.7%, TE 2025 57.3% / 2024 57.0%, gaps 7.6 pp / 227 bn and 7.8 pp, TE per capita 23,330 PPS (8th), SOCX 32.0%, COFOG social protection 23.6%, defense 1.8%, EU-27 27.4%, PISA 2025, non-resident 59.7%, OAT 169 bp | Grep against 00 §4: no superseded value remains (the 64.7 in §4.4 is the pensions' earmarked taxes, not interest; 64.7 as interest now appears only with its FISIM label in §4.9 and §4.17) |
| Yardsticks of §3.1-§3.4 (one day 4.70 bn; 32.3 days; EUR 24,843; interest 14.0 days / 43.3% / EUR 952; rise in interest 25.3 = 5.4 days / 16.7% / EUR 367; Zucman 0.4-4.3 days) | Re-computed on 1,714.1 / 151.6 / 68.998: unchanged |
| COFOG foreign economic aid (quiz item 6: 0.3% of TE, EUR 4.9 bn) | Matches file 16 §2 (4.88 bn = 0.29% of TE) |

### Pass 2026-10-25 – platform data review (`platform/data/REVIEW.md`) and site open items

*Scope: the ten fixes and four editorial points of `platform/data/REVIEW.md`, and the open items of `fr/LISEZMOI-site.md` §5.1 (items 2, 3 and 5) that concern values or labels shown in this file. Values were re-read in files 00, 02, 03, 04, 07, 11 and 12; no new figure was introduced. Yardsticks are computed as in §3.4 (days = EUR bn / 4.696; % of deficit = EUR bn / 151.6; EUR per inhabitant = EUR bn × 1,000 / 68.998). The French translation (`fr/20-approche-pedagogique.md`, `fr/20-approche-pedagogique-partie2.md`) was updated in the same pass.*

**A. Corrections of values and labels**

| Location | Was | Now | Basis |
|---|---|---|---|
| §4.10 Energy VAT card | "-11 to -17.4"; 2.3-3.7 days | Cost "more than 11" (Montaigne 2024, a lower bound and the only independent costing); RN's own 12.2 shown as a claim; 17.4 (francebudget.fr) not used; more than 2.3 days, 7.3% of the deficit, EUR 159 per inhabitant | REVIEW #1; file 07 §3.5 (17.4 "should not be used as a reference": its base excludes fuels); file 11 §4.2 |
| §5.3 S9 | Energy VAT "-11 to -17.4" | About -11, a lower bound; RN -12.2; 17.4 not used | REVIEW #2; same |
| §4.10 SMIC card; §5.3 S10 | "-3.5 to -4" for the whole 1,600-1,700 range; 0.7-0.9 days | -1.8 to -4: 1,600 net about -1.8 to -2.2 (+8.3% vs the SMIC in force since 1 June 2026); 1,700 net about -3.5 to -4 (+15%); own scaling, flagged; 0.4-0.9 days | REVIEW #3-4; file 07 §3.6 (SMIC raised by 2.41% on 1 June 2026); file 11 §4.1 (1,700) and §4.6 (1,600) |
| §5.3 S2 label | "one-year freeze of base pensions, lowest pensions protected" | PLFSS 2027 partial under-indexation (full indexation only up to EUR 1,260 a month, lower above); value 4.1 unchanged (3.0 basic schemes + 1.1 State) | REVIEW #5; file 03 (chronology, 1 Oct 2026, and verification table) |
| §6.3 Q20 | "19.8% SIASP" | 19.8% DGAFP/Insee (civil-service perimeter, Insee employment estimates incl. subsidized contracts, 2024); 20.7% OECD (2023) | REVIEW #6; file 04 K7 and §4 item 4 |
| §4.2 GF04 | link to "§4.14 (business aid)" | §4.12 | Internal cross-reference (flagged by the French translator) |

**B. Open items resolved**

| Item | Resolution | Basis |
|---|---|---|
| S3, source of the low end (REVIEW point 2; LISEZMOI-site §5.1 item 3) | 2.4 = minister's office figure (July 2026, press), labeled as such. 2.1 = our computation, 3.2 bn (full-year cost of the July 2023 +1.5% rise, press citing the decree's impact sheet) / 1.5 = 2.13; Montaigne's 20 bn for +10% (2 per point) is consistent. Partial official check: State branch 1.5 bn (Senate, avis no. 134, PLF 2024). The ⚠ 2.07 breakdown stays unused. Range unchanged; each end is now labeled with its source in §4.10 and §5.3 | File 07 §3.6 and divergence table; file 07 [S15], [S33], [S47] |
| `rn_back_to_62` card (REVIEW point 3) | The card and quiz item 13 now show both independent ranges: repeal alone 16-17 bn (Cnav as cited in AN report no. 613: 15.7 in 2032; Fipeco 17 in 2030) and partial RN-type versions 26-35 bn (00 row 44); neither is a costing of the 2027 plan; RN claim about 9 (9.5 in 2031 in its annex) | File 11 §4.2; file 03 §4.1 and its Cnav row; 00 row 44 |
| S5 default growth rate (REVIEW point 4; LISEZMOI-site §5.1 item 3) | Default +3.4% (2027 trend, no-policy baseline, default yield 0); markers +2.0% (PLFSS 2027 target) and 2-2.5% (Cour des comptes). Check: (3.4 − 2.0) × 10 × 0.27 ≈ 3.8 bn vs the Cour's 3.9 bn of net ONDAM savings | File 02 §4.3 (PLFSS 2027, bill no. 3211, Art. 43; trend +3.4%; Cour 3.9 bn net); file 12 §7.2 (RALFSS 2026) |
| Chapter 1 title (LISEZMOI-site §5.1 item 2) | The chapter file's title is kept: « Combien ? » ("How much?"). §2.1 updated here; the French plan also now uses the chapter files' titles for chapters 5 and 6 (« La dette et ses intérêts », « Qu'obtient-on en échange ? ») | `fr/site/chapitres/01-combien.md`, `05-dette-et-interets.md`, `06-ce-que-l-on-obtient.md` |

**C. Checked and unchanged**

| Item | Check |
|---|---|
| REVIEW #1 locates the 17.4 figure in "§3.4" | §3.4 has no energy VAT row; the value appeared only in the §4.10 card and §5.3 S9, both corrected |
| §4.4 ("Return to 62: 10-17 bn … up to about 26 bn") and §5.3 S1 ("to 62: -10 to -17 (system), about -26") | Consistent with the two ranges above (file 03 §4.1) |
| §4.5 and S5 "0.27 per 0.1 pt" | 0.001 × 273.3 = 0.273 (ONDAM 2026, file 02 row 24): unchanged |
| REVIEW #7-#10 (French wording of quiz items 16 and 24, toggle and menu labels) | Concern the French version only; applied in the French translation (« impôt net positif », « charge de la dette de l'État » vs « enveloppe de la loi de programmation militaire (LPM) », « Cibles souvent citées ») |
| Not edited | `data/20_pedagogical_conversions.csv` (still to regenerate, §11 item 14) and `platform/data/*` (owned elsewhere) |

---

## Sources

[^ref]: `00-reference-figures.md` (canonical values, 2026-10-25), and the sources listed in its table: Eurostat `gov_10a_main` and `gov_10dd_edpt1` (21 Oct 2026) https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table ; Insee, *Insee Première* 2106 (29 May 2026) https://www.insee.fr/fr/statistiques/8997691 ; Insee PO series https://www.insee.fr/fr/statistiques/2381412 ; HCFP opinion 2026-5 (25 Sep 2026) https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf ; COR annual report (June 2026) https://www.cor-retraites.fr/sites/default/files/2026-06/RA_2026_def.pdf
[^cofog]: Eurostat `gov_10a_exp`, COFOG, general government, 2024 provisional (21 Oct 2026). https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table ; files `data/eurostat_gov_10a_exp_pctot.csv`, `data/eurostat_gov_10a_exp_mioeur.csv`; file 01 §4.1.
[^conv]: Own computation, `data/20_pedagogical_conversions.csv` (2026-10-25), from canonical values in file 00.
[^f01]: `01-spending-overview.md` (Insee *Insee Première* 2093, Feb 2026; Eurostat COFOG).
[^f02]: `02-social-protection.md` (Drees, *La protection sociale en France et en Europe en 2024*, 17 Dec 2025, https://drees.solidarites-sante.gouv.fr/publications-communique-de-presse/panoramas-de-la-drees/251217-protection-sociale-france-europe-2024 ; Drees health accounts 2026 edition; CCSS Oct 2026).
[^f03]: `03-pensions.md` (COR June 2026; Cour des comptes Feb 2025; Fipeco June 2024; Institut Montaigne 3 Jul 2024).
[^f04]: `04-civil-service-and-outcomes.md` (DGAFP RAEFP 2026; Eurostat `gov_10a_main`, `crim_just_job`; OECD *Government at a Glance 2025*; OECD *Education at a Glance 2026*).
[^f05]: `05-taxation.md` (Insee tables 3.216/3.217, 28 Aug 2026; OECD *Revenue Statistics 2025*; OECD *Taxing Wages 2026*; DGFiP Statistiques n°41; Insee Analyses n°118, 16 Apr 2026; IPP Note n°92; Cour des comptes NEB 2025).
[^f06]: `06-deficit-and-debt.md` (Insee; Eurostat EDP; Cour des comptes RSPFP June 2026; PLF 2027 https://www.assemblee-nationale.fr/dyn/17/textes/l17b3210_projet-loi.pdf ; HCFP 2026-5; EC *Debt Sustainability Monitor 2025*).
[^f07]: `07-proposals-costing.md` (Senate report n° 689, 4 Jun 2025; IPP June 2026; Institut Montaigne 2024; CAE Focus 118; Cour des comptes 15 Jul 2024 and 15 Mar 2024).
[^f08]: `08-revenue-cuts-since-2017-and-structural.md` (OFCE PB 146; Rexecode DT 105; Senate report 808; HCSP July 2026; Bozio-Wasmer 2024; DG Trésor note for HCFiPS Aug 2024; Eurostat `lfsi_emp_a`, `nama_10_lp_ulc`; Insee national balance sheet 30 Jul 2026; NATO July 2026; Pisani-Ferry and Mahfouz 2023).
[^f09]: `09-international-comparison-tables.md` (Eurostat, OECD; computed group statistics).
[^f10]: `10-counterarguments-and-debates.md` (HCSP July 2026; OFCE; Cour des comptes; IMF; Eurostat computed series).
[^f11]: `11-2027-candidate-programs-costing.md` (LFI 14 Oct 2026; RN 6 Oct 2026; LR 12 Oct 2026; Institut de l'Entreprise via PGE; IPP Note 125; DGEC weekly fuel bulletin 16 Oct 2026).
[^f12]: `12-health-hospital-outcomes-international.md` (Eurostat SHA `hlth_sha11_*`; OECD *Health at a Glance 2025*; WHO GHED; Drees; Cour des comptes April 2026).
[^f13]: `13-civil-service-and-education-intl-completion.md` (OECD *PISA 2025 Results, Volume I*, 8 Sep 2026, https://www.oecd.org/en/publications/pisa-2025-results-volume-i_73451bc5-en/full-report.html ; IEA TIMSS 2023, PIRLS 2021; PLF 2027 staffing plan).
[^f14]: `14-public-perception-orders-of-magnitude.md` (Elabe, Ifop, Odoxa, Drees *Baromètre*, Cevipof; academic literature).
[^f15]: `15-immigration-and-public-finances.md` (OECD *International Migration Outlook 2021*, ch. 4, https://www.oecd.org/en/publications/international-migration-outlook-2021_29f23e9d-en/full-report/component-8.html ; CEPII *Lettres* 311 and 394; PAP 2027 programme 183, https://www.budget.gouv.fr/documentation/file-download/33907 ; Évin-Stefanini report, Dec 2023, https://www.vie-publique.fr/files/rapport/pdf/292122.pdf ; Constitutional Council decision 2024-6 RIP; RN counter-budgets; Institut de l'Entreprise, 6 Oct 2026).
[^f16]: `16-oda-eu-contribution-and-other-popular-targets.md` (OECD-DAC preliminary 2025 data, 9 Apr 2026; PLF 2027 and its *Jaunes*, incl. *Relations financières avec l'Union européenne*, https://www.budget.gouv.fr/documentation/file-download/34459 ; Senate reports 578 (2022) and 807 (2025); European Commission *EU spending and revenue 2000-2025*; iFRAP; Institut Montaigne).
[^f17]: `17-fiscal-multipliers-for-simulator.md` (HCFP-2026-5 §36, 25 Sep 2026; CAE Focus 108, 24 Jul 2024, https://www.cae-eco.fr/static/pdf/focus-108-240712-en.pdf ; DG Trésor/Insee Mésange 2017; OFCE e-mod.fr for the HCFiPS, 2021, and Policy Brief 154, 2026; ECB WP 1760; Banque de France WP 883; Cour des comptes RSPFP June 2026 and pensions report Feb 2025; Guajardo-Leigh-Pescatori; Alesina-Favero-Giavazzi; IGF mission July 2026).
[^f18]: `18-po-vs-oecd-and-interest-bridges.md` (Insee national accounts tables 3.201-3.217, May 2026, https://www.insee.fr/fr/statistiques/8988845 ; Eurostat `gov_10a_taxag`, `gov_10a_main`, `hlth_sha11_hf`; OECD *Revenue Statistics 2025*; Cour des comptes RSPFP June 2026; PLF 2027).
[^cour24]: Cour des comptes, *La situation et les perspectives des finances publiques* (15 Jul 2024). https://www.ccomptes.fr/sites/default/files/2024-09/20240715-RSPFP-2024.pdf
[^cour26]: Cour des comptes, *La situation et les perspectives des finances publiques* (25 Jun 2026). https://www.ccomptes.fr/sites/default/files/2026-07/20260625_RSPFP-2026.pdf
[^cour-bouclier]: Cour des comptes, energy price shields report (15 Mar 2024), via file 07 [S12] and file 11 [S19].
[^igf]: Mission on public-finance transparency (Jaravel, Ragot, Tavernier, Valla), IGF, July 2026. https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/Transparence-finances-publiques.pdf
[^hcsp-aides]: HCSP report to the Prime Minister on aid to business (July 2026), via file 08.
[^cae118]: CAE, *Focus* n°118 (July 2025). https://cae-eco.fr/static/pdf/Focus_118_emigration_fiscale_250725_v2.pdf
[^ipp125]: IPP Note n°125, Chapelle and Fack (May 2026), via file 11 [S18].
[^elabe26]: Elabe for *Les Echos*, *Les Français et la dette publique* (fieldwork 1-2 Sep 2026, n = 1,005). https://elabe.fr/fichier-pdf/13231-20260903_elabe_les-echos_les-francais-et-la-dette-publique/
[^ipsos21]: Ipsos (M. Gallard, L. Boisson), *Enquête sur la perception de la dette publique par les Français*, fieldwork 18-21 Jan 2021, n = 1,000 adults 18+, online access panel, quotas. Published as attachment 4 to vie-publique report 279092: https://www.vie-publique.fr/files/rapports/fichiers_joints/279092-pi%C3%A8ce%20jointe%204.pdf (downloaded 2026-10-25 to `data/raw/20_perception/vp_279092_pj4.pdf`). Client: MINEFI, for the *Commission sur l'avenir des finances publiques* (Ipsos report, "Rappel des objectifs (1/2)": "Une enquête pour nourrir la réflexion de la Commission sur l'avenir des finances publiques"). Parent report: *Rapport de la Commission sur l'avenir des finances publiques*, J. Arthuis, submitted 18 Mar 2021, https://www.vie-publique.fr/rapport/279092-commission-sur-lavenir-des-finances-publiques (page read in browser 2026-10-25; lists "Annexes - Pièce jointe n° 4").
[^hexagone]: Observatoire Hexagone, *Système de retraites : les Français divisés mais réformistes* (24 Mar 2025), Harris Interactive poll, n = 1,101. https://observatoire-hexagone.org/wp-content/uploads/2025/03/20250224_Hexagone_Retraites-2.pdf (downloaded to `data/raw/20_perception/hexagone_retraites_2025-02.pdf`). Fieldwork: online, 21-24 Feb 2025, n = 1,101 adults 18+, quotas (sex, age, occupation, region, urban-area size) with weighting, per Toluna-Harris Interactive, *Les Français et le système de retraite* (March 2025), p. 3: https://observatoire-hexagone.org/wp-content/uploads/2025/03/Rapport-Toluna-Harris-Les-Francais-et-le-systeme-de-retraite-Hexagone.pdf (downloaded to `data/raw/20_perception/toluna/toluna_harris_hexagone_retraites.pdf`). *(Verified 2026-10-25: was "fieldwork dates not stated (⚠)".)* Orientation: advocates a mixed pay-as-you-go/funded system.
[^kns]: Kuziemko, Norton, Saez, Stantcheva (2015), "How Elastic Are Preferences for Redistribution?", *American Economic Review* 105(4): 1478-1508 (via file 14).
[^stantcheva]: Stantcheva (2021), "Understanding Tax Policy: How do People Reason?", *Quarterly Journal of Economics* 136(4): 2309-2369 (via file 14).
[^douenne]: Douenne and Fabre (2022), "Yellow Vests, Pessimistic Beliefs, and Carbon Tax Aversion", *AEJ: Economic Policy* 14(1): 81-110 (via file 14).
[^ciani]: Ciani, Fréget, Manfredi (2021), OECD Papers on Well-being and Inequalities, meta-analysis of informational experiments (via file 14).
