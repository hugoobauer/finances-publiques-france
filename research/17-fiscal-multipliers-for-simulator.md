# 17 - Fiscal Multipliers and Macro Feedback for the "Balance the Budget" Simulator

*Research file 17. Prepared 2026-10-25. All web sources accessed 2026-10-25. Raw downloads are saved under `research/data/raw/17_multipliers/` (plus earlier local copies cited by path). This file fills README §9.1 gap 7 ("multipliers for the simulator are not yet read from primary sources"). It does not edit any other file.*

> **How to read this file.** A **fiscal multiplier** (*multiplicateur budgétaire*) is the change in real GDP, in % of GDP, caused by a deficit-reducing measure worth 1% of GDP *ex ante* (before macro feedback). This file uses a **positive number for a GDP loss**: "multiplier 0.8" means a measure that saves 1 point of GDP (about **EUR 30 bn**; 2025 GDP ≈ EUR 2,990 bn, from `00-reference-figures.md` row 1: 1,714.1 / 0.573) lowers GDP by 0.8% relative to the no-measure path. Sources that report negative signs are converted. "Year 1" is the first year of the measure. "Year 3-5" is the **level** effect three to five years after a **permanent** measure, not a cumulative sum, unless the row says "cumulative". Units are always ratios (% of GDP per 1% of GDP of measure), never % of total public expenditure. **[computed]** means the statistic was calculated in this session from the cited table.

---

## 0. Executive summary (for editors and developers)

1. **There is no single "French multiplier".** The answer depends on (i) the instrument, (ii) the horizon, (iii) the cycle and monetary stance, (iv) credibility and confidence effects. Official French institutions currently use **about 0.6 for a mixed package in year 1**: the HCFP (25 Sep 2026) calls "credible" the administration's estimate that the PLF 2027 primary adjustment of 0.8 point of GDP costs 0.5 point of growth [S1].
2. **Spending on goods, services and public wages has the highest short-run multiplier, about 0.8 in year 1** (Mésange 0.78 [S6]; OFCE 0.7-0.8 for 2026 structural savings [S8]; ESCB model comparison 0.92 for France, EAGLE model run by the Banque de France [S11] (corrected 2026-10-25: was "ESCB central-bank models"); Banque de France EA-BDF about 1.0 [S12]). **Public investment is higher still (1.31 in year 1 in Mésange)** [S6].
3. **Household tax rises and transfer or pension cuts start lower, about 0.3-0.4 in year 1, and build up to 0.6-0.9 by years 3-5** (Mésange income tax 0.41 → 0.88; e-mod.fr pension cut 0.3 → 0.7) [S6][S9]. **VAT is the instrument on which French models disagree most**: Mésange 0.32 → 0.81 by year 5; OFCE e-mod.fr 0.2 → 0.1 [S6][S9].
4. **Taxes on large firms, capital income and high wealth have low short-run multipliers (about 0.0-0.3)** (OFCE implied multipliers for the 2026 measures [S8]; ESCB models 0.07 for a capital-tax rise in France [S11]). Some models show **large long-run costs** for permanent capital-tax rises [S11]. There is **no direct French estimate for a wealth tax**.
5. **Raising the pension age is a supply measure, not a demand shock.** GDP effects run from **-0.1% (OFCE e-mod.fr) to +0.3% (Mésange) after 10 years, and +1.1% in micro-based estimates by 2030**, for 2 years of legal age. The net gain for the public balance ranges from **+0.1 to +0.9 point of GDP** [S10].
6. **The international literature brackets these values.** Blanchard-Leigh (2013): forecasters assumed about 0.5 in 2010-11; actual multipliers were "substantially above 1" in the crisis [S2]. Guajardo-Leigh-Pescatori (narrative, 17 OECD countries): a 1%-of-GDP consolidation lowers GDP by **0.62% within two years**; **0.43 if spending-based, 1.29 if tax-based** [S3]. Alesina-Favero-Giavazzi: spending-based plans cost **0.28-0.46** (cumulative, 5 years); tax-based plans cost **0.96-1.50** [S4]. Both narrative studies find tax-based consolidations costlier. The Cour des comptes (June 2026) reads the narrative evidence as "comparable" costs and stresses composition [S5]; see §6 for this divergence.
7. **Internationally, France's model-based spending multiplier is among the highest in Europe**: in the ESCB 15-model comparison, France ranks **2nd of 14** for a cut in government consumption in year 1 (0.92 vs a 14-country median of 0.75 and mean of 0.73) [S11] [computed]. Germany is 0.52 and Spain 0.50. Denmark is not covered.
8. **Recommended simulator defaults (§8):** spending on goods, services and wages 0.8 → 0.7; public investment 1.0 → 0.9; cash transfers 0.5 → 0.7; pension indexation 0.3 → 0.6; VAT 0.3 → 0.5; income tax and CSG 0.4 → 0.8; employer contributions 0.3 → 0.7; corporate and high-income taxes 0.3 → 0.4; wealth tax 0.1 → 0.2; pension age (2 years): GDP +0.0 → +0.3% at 10 years. **Budget feedback:** the deficit worsens by about **0.57 × the GDP loss** (CAE's semi-elasticity [S13]). So a EUR 30 bn spending cut nets about EUR 16 bn in year 1 (1 - 0.8 × 0.57 = 0.54), before any debt-ratio denominator effect.
9. **Uncertainty is large.** Every default should be shown with a band: roughly ±50% in year 1. The "zero multiplier" used in the government's 2024 medium-term plan (PSMT) is called "very favorable" and "particularly strong" by the July 2026 IGF mission [S15]. Values above 1.5 are crisis or zero-lower-bound values [S2][S11]; they do not fit the 2027 baseline (ECB not at the lower bound).

---

## 1. What a multiplier is, and why the simulator needs one

- **Definition used by the Cour des comptes:** "*Le multiplicateur budgétaire mesure l'effet d'un euro de consolidation sur le PIB. Un multiplicateur de 0,5 signifie qu'un euro de consolidation réduit le PIB de 0,5 euro*" (the fiscal multiplier measures the effect of one euro of consolidation on GDP; a multiplier of 0.5 means one euro of consolidation reduces GDP by 0.5 euro) [S5, p. 119, fn. 122].
- **Why it matters for a "balance the budget" game.** A user who cuts EUR 30 bn does not improve the deficit by EUR 30 bn. Lower GDP (i) reduces tax revenue and raises unemployment benefits, and (ii) raises the debt-to-GDP ratio through the denominator. The CAE formalizes this as output gap = *m* × budgetary adjustment, with a deficit semi-elasticity to the output gap of **ε = 0.57** for France [S13, p. 3-4].
- **Three horizons.** Year 1 (Keynesian demand effect); years 3-5 (prices and wages adjust; supply-side effects of taxes on labor and capital begin to dominate); long run (10+ years; in Mésange the demand effects mostly fade, while tax distortions persist) [S6].

---

## 2. International academic evidence (primary sources)

| Study | Sample and method | Headline result (converted to "positive = GDP loss") | Horizon | Source |
|---|---|---|---|---|
| **Blanchard & Leigh (2013)** | 26 European economies; growth forecast errors 2010-11 regressed on planned consolidation (IMF WEO Apr 2010) | β = **-1.095** (t = -4.29): each extra point of planned consolidation meant GDP **about 1% below forecast**. Forecasters assumed multipliers of **about 0.5**, so actual multipliers were "**substantially above 1** in the early years of the crisis". Spending coefficient 1.244 vs revenue -0.865 (difference not significant, p = 0.102). Later vintages (2011-12, 2012-13): coefficients "typically between 0.3 and 0.5" and "less statistically significant". No bias in 1997-2008. | 2 years | [S2] NBER WP 18779, pp. 2-3, Tables 1 and 5 (local copy `data/raw/papers_debates/blanchard_leigh_w18779.txt`) |
| IMF WEO Oct 2012, Box 1.1 (same authors) | Same method, first version | Range of actual multipliers **0.9-1.7** since 2008. ⚠ unverified in this file: imf.org returned 403/404/429 to curl, WebFetch and the browser on 2026-10-25; the range is carried over from file 10 §6.1, where it was checked earlier. Re-tried on 2026-10-25 in the adversarial pass: imf.org PDF still returned 403. Only press coverage (Slate, New Statesman, Oct 2012) confirms "0.9 to 1.7", which is not an acceptable source. Recommendation: do not show this range on the website until the WEO PDF is read in the laptop browser | 2 years | [S2b] |
| **Guajardo, Leigh & Pescatori (2014)**, narrative approach | 17 OECD countries (France included), 1978-2009; consolidations identified from policy documents | 1% of GDP consolidation: GDP **-0.62%** and private consumption -0.75% within 2 years. **Spending-based: GDP -0.43** (t = -2.38). **Tax-based: GDP -1.29** (t = -4.67). Effects are smaller under floating exchange rates (0.33) than under pegs (0.84). The CAPB-based approach wrongly suggests expansionary effects (+0.16 within a year). | 2 years | [S3] IMF WP 11/158, PDF pp. 6, 13, 24, 26 (the JEEA 2014 version is cited by the Cour; its abstract was checked on RePEc, but its exact numbers were not re-read; JEEA page paywalled) |
| **Alesina, Favero & Giavazzi (2018 NBER; 2019 book)** | 16 OECD countries, "fiscal plans" (narrative), panel VAR with recession/expansion states | Spending-based (EB) plan of 1% of GDP: GDP loss "about half of a percentage point", lasting under 2 years. Tax-based (TB): "a two percent fall in GDP". STAR model, cumulative 5-year multipliers: **expansion EB 0.46, TB 1.50; recession EB 0.28, TB 0.96**. Primary-surplus multipliers: EB 0.75, TB 3.70 (expansion). | 5 years (t = 0 to 4) | [S4] NBER WP 24246, pp. 5-8 and Table 1 |
| **Gechert (2013 WP; *Oxford Economic Papers* 2015)**, meta-regression of 104 studies | Mixed methods | Public spending multipliers "close to one", **0.3-0.4 larger than tax and transfer multipliers**; public investment about **0.5 larger** than spending in general. Simulation-based "crisis scenario" multipliers close to 2. Orientation: IMK is the trade-union-funded Hans-Böckler Foundation institute. | Mixed | [S16] IMK WP 117, abstract and p. 2 |
| **Ramey (2019, *JEP*)**, survey | US-dominated | Bulk of spending multipliers **0.6-1**; tax-change multipliers **2-3** (US, mostly Romer-Romer-type estimates) | Mixed | [S17] AEA abstract |

**Takeaway for France.** Two of the three narrative studies above find tax-based packages costlier than spending-based packages (GLP, AFG). The model-based French evidence (§3) finds the opposite ranking in year 1, because government purchases enter GDP directly. The two families answer different questions. Model variants isolate *one instrument at a time*, with interest rates fixed. Narrative packages bundle measures, often with monetary or exchange-rate responses and credibility effects. On whether accompanying policies explain the EB/TB gap, the two narrative teams disagree: AFG report that Guajardo et al. (2014) attribute much of it to differences in the monetary-policy response, while AFG themselves find that "only a small fraction" of the gap is related to monetary policy [S4, p. 9] (corrected 2026-10-25: was "AFG themselves note that the EB/TB gap is partly explained by accompanying policies").

---

## 3. French model multipliers by instrument

### 3.1 Mésange (Insee / DG Trésor, 2017 re-estimation)

*Variants of 1% of GDP ex ante (EUR 22 bn in 2015), permanent, at constant real interest rates and nominal exchange rates, with no fiscal rule. Real GDP, % deviation from baseline. Signs converted to "consolidation" where the source simulates a tax cut or a spending rise. Model behavior is linear for small shocks.* [S6, Ch. 4, pp. 100-117 (PDF pp. 102-119)] (corrected 2026-10-25: was "pp. 102-119 (PDF pp. 104-119)"; the variant conventions are on printed p. 100 and the last table used, income tax, on printed p. 117)

| Instrument (direction simulated in source) | Year 1 | Year 2 | Year 3 | Year 5 | Year 10 | Long run | Primary balance, year 1 (pts of GDP) |
|---|---|---|---|---|---|---|---|
| Public investment (+1 pt) | **1.31** | 1.38 | 1.22 | **0.93** | 0.57 | 0.22 | -0.49 |
| Generic public spending (+1 pt) | **0.78** | 1.06 | 1.03 | **0.86** | 0.53 | 0.16 | -0.53 |
| Employer social contributions (cut 1 pt) | **0.20** | 0.55 | 0.76 | **0.97** | 1.29 | 1.73 | -0.72 |
| Employee social contributions (cut 1 pt) | 0.38 | 0.72 | 0.75 | 0.77 | 1.14 | 1.74 | -0.73 |
| VAT (rise 1 pt; source sign negative) | **0.32** | 0.66 | 0.72 | **0.81** | 0.78 | 0.70 | +0.80 |
| CSG (cut 1 pt) | 0.41 | 0.84 | 0.90 | 0.81 | 0.80 | 0.88 | -0.81 |
| Household income tax, IR (cut 1 pt) | **0.41** | 0.83 | 0.88 | **0.81** | 0.87 | 1.05 | -0.81 |

*Reading:* the year-1 multiplier of generic spending is 0.78 ("*un choc de dépense publique composite aboutirait à un multiplicateur de première année de 0,78 seulement*", a composite public spending shock would give a first-year multiplier of only 0.78) [S6, p. 103]. Tax rises on labor (employer contributions) cost little in year 1 but more over time, because they raise labor costs. The long-run effect is the largest of all instruments (1.73). The primary-balance column gives the year-1 self-financing implied by the model: a VAT rise of 1 pt of GDP ex ante improves the primary balance by 0.80 pt in year 1.

*Caveats from the source:* (i) the results are at **constant real interest rates**. With an endogenous national monetary response, demand shocks would be "*encore davantage évincé[s]*" (crowded out even more) [S6, p. 104]. (ii) The productivity of public capital is not modeled, so public investment is a pure demand shock. (iii) There is no separate "social transfer" variant in 2017. CSG and IR are the closest proxies for a cut in cash transfers to working-age households.

### 3.2 OFCE e-mod.fr (OFCE for the HCFiPS, Oct 2021)

*OFCE is the Sciences Po economic research center, generally Keynesian in orientation. Shocks are 1 pt of GDP of consolidation, permanent and fully implemented at once. Real GDP, % deviation (loss shown positive).* [S9, Tables 1, 5, 11, 13, 15, 20, 22, 24]

| Instrument | Year 1 | Year 2 | Year 3 | Year 5 | Year 10 | Net public-balance gain, year 1 / year 5 (pts of GDP, ex ante 1.0) |
|---|---|---|---|---|---|---|
| Pension benefits cut (-7.5% of the pension bill) | 0.3 | 0.7 | 0.7 | 0.7 | 0.4 | 0.9 / 0.5 |
| Social transfers in kind (*transferts en nature des ASSO*, e.g. health) cut | **1.0** | 1.0 | 0.9 | 0.7 | 0.3 | 0.6 / 0.4 |
| Employer contributions rise | 0.4 | 0.6 | 0.6 | 0.7 | 0.6 | 0.7 / 0.2 |
| Employee contributions rise | 0.4 | 0.7 | 0.7 | 0.6 | 0.4 | 0.9 / 0.4 |
| CSG rise (replacement or capital income; identical in the model) | 0.3 | 0.7 | 0.7 | 0.6 | 0.4 | 0.9 / 0.5 |
| **VAT rise** | **0.2** | 0.3 | 0.2 | **0.1** | 0.0 | 0.5 / 0.5 (0.6 at year 10) |
| Pension age +2 years (one quarter per cohort) | 0.0 | 0.1 | 0.2 | 0.2 | 0.1 | see §3.5 |

*Notes:* the net balance gains are from Table 1 of the source ("*l'amélioration du solde est maximale (+0,9 point de PIB) pour une hausse de la CSG, des CSS ou une baisse des pensions*", the balance improvement is largest, +0.9 pt of GDP, for a CSG rise, employee contributions or a pension cut) [S9, p. 10-11]. In the extracted PDF, two table titles do not match their sections: the table under "Variante 2" (pension cut) is titled "*dépenses de santé*", and the table under "Variante 7" (VAT) carries the CSG title. Values are assigned here to the section they sit in. That assignment is consistent with the source's own reading note ("*une hausse du taux de TVA moyen équivalente à 1 point de PIB ex ante se traduit par une baisse du PIB de 0,3 % au bout de 2 ans*", a VAT rise of 1 pt of GDP ex ante lowers GDP by 0.3% after 2 years) [S9, p. 11].

### 3.3 OFCE implied multipliers for the 2026 budget (Policy Brief 154, 26 Feb 2026)

*Year-1 GDP impact divided by measure size [computed from S8, Table 4]. OFCE: "les économies structurelles sur l'État, les collectivités locales et la sécurité sociale ont des multiplicateurs à court terme relativement élevés (compris entre 0,7 et 0,8)" (structural savings by the State, local authorities and social security have relatively high short-run multipliers, between 0.7 and 0.8). Defense and the* prime d'activité *(in-work benefit) are "close to 1"; interest charges, the EU contribution and development aid are "zero or very low".*

| Measure (LF 2026) | Size (% of GDP) | GDP impact 2026 (pts) | Implied year-1 multiplier [computed] |
|---|---|---|---|
| State primary-spending savings | -0.53 | -0.43 | **0.81** |
| Local-government savings | -0.11 | -0.09 | 0.82 |
| Social-security savings | -0.13 | -0.09 | 0.69 |
| Defense effort (spending rise) | +0.17 | +0.17 | 1.0 |
| *Prime d'activité* rise | +0.02 | +0.02 | 1.0 |
| Interest charges | +0.19 | +0.03 | 0.16 |
| New exceptional surtax on large companies | 0.24 | -0.07 | **0.29** |
| +1.4 pt CSG on financial income and flat tax | 0.05 | -0.02 | 0.4 (rounded inputs) |
| Extension of the high-income minimum tax (CDHR) | 0.02 | 0.00 | **≈ 0** |
| Rise in CNRACL employer contribution rate | 0.06 | -0.03 | 0.5 |
| All new compulsory-levy measures | 0.54 | -0.16 | **0.30** |
| **Total primary fiscal impulse** | -0.72 | -0.48 | **0.67** |

The OFCE total: the 2026 budget lowers growth by **0.5 pt** (-0.46 total impulse) [S8].

### 3.4 Banque de France (EA-BDF / FR-BDF) and the ESCB model comparison

- **Banque de France WP 883 (Sep 2022), EA-BDF model:** a government consumption shock of 1 pt of GDP, held for 2 years. France's multiplier averages about **1.1** (backward-looking expectations) and **1.0** (model-consistent expectations) over the first two years when the shock hits the whole euro area. It averages **1.0 and 0.9** when only France moves. At 10 years, in the France-only (asymmetric) case, it falls to 0.13 (backward-looking) and 0.16 (model-consistent) [S12, fn. 36] (clarified 2026-10-25: the 10-year values were not tied to a case). The rest of the euro area: 0.9 [S12, pp. 52-55] (corrected 2026-10-25: was "pp. 53-55"; section 5 starts on p. 52).
- **ESCB comparison (Kilponen et al., ECB WP 1760, Mar 2015; IJCB 2019):** 15 central-bank models. France (EAGLE model, Jacquinot and Lemoine 2013, run by the Banque de France [S11, Table A1]; corrected 2026-10-25: was "Banque de France model". EAGLE is a multi-country ESCB DSGE model, not the Banque de France's own FR-BDF or Mésange-type forecasting model): temporary cut in government consumption **0.92 (year 1) / 0.71 (year 2)**; 1.05 / 0.87 under a two-year zero lower bound. Labor income tax rise: 0.13 / 0.30. Capital tax: 0.07 / 0.08. Consumption tax (VAT): 0.14 / 0.23 [S11, Tables 1-4]. Permanent capital-income tax rise with lump-sum offset: France **0.36 (year 1), 0.61 (year 2), 3.27 (long run)** [S11, Table 6]. This is the strongest model evidence that capital taxes are cheap in the short run but costly in the long run.
- **Banque de France projections (25 Mar 2026):** the bank assumes the positive effect of a smaller-than-planned consolidation in 2026 "*est compensé par un attentisme accru des ménages et des entreprises*" (is offset by greater wait-and-see behavior by households and firms) [S14, PDF p. 2] (corrected 2026-10-25: was "p. 1"). In practice, the BdF applies a **near-zero net multiplier** on the 2026 slippage because of an uncertainty channel. That is a judgment, not a model estimate.

### 3.5 Pension age: a supply shock

| Estimate, 2 years of legal age (2023 reform type) | GDP | Pension-system balance | General-government balance | Horizon | Source |
|---|---|---|---|---|---|
| Mésange (DG Trésor, Jan 2022) | **+0.3%** | +0.4 pt | **+0.4 pt** | 2033 (10 years) | [S10, Table 4] |
| OFCE e-mod.fr | **-0.1%** | n/a | **+0.1 pt** | 2033 | [S10, Table 4]; [S9, Table 5] |
| DG Trésor accounting model (micro-based) | **+1.1%** | +0.4 pt | **+0.9 pt** | 2030 | [S10, Table 4] |
| Rexecode (employer-funded institute; micro-based) | +1.1% | +0.4 pt | +0.6 pt | 2030 | [S10, Table 4] |

The Cour des comptes leans toward the micro evidence. Macro models "*doivent être pris avec précaution à un horizon de 10 ans*" (should be treated with caution at a 10-year horizon) because they predict a rise in unemployment (+0.7 pt in Mésange, +0.5 pt in e-mod.fr at 10 years). After the 2010 reform, the probability of unemployment for people already in work rose only from 1.2% to 1.7% [S10, p. 66-67]. Spillover costs to other benefits are about **20% of gross pension savings** (Drees/Dares on the 2010 reform) [S10]. File 03 §225 already carries the Fipeco long-run decomposition (0.9 pt). This file is consistent with it.

### 3.6 Official aggregate assumptions currently in use

| Institution | Aggregate assumption | Implied average multiplier | Source |
|---|---|---|---|
| Administration (PLF 2027), endorsed as "credible" by the **HCFP** | Adjustment of 0.5 pt of GDP (0.8 pt primary) costs **0.5 pt of growth** in 2027. Mixes measures with a multiplier "close to 1" (cuts in public demand), "moderate" ones (some revenue rises) and near-zero ones (levy on the CNIEG surplus) | **≈ 0.6** on the primary effort [computed: 0.5 / 0.8 = 0.625] | [S1, §36, p. 13] (corrected 2026-10-25: was "p. 12") |
| OFCE, LF 2026 | -0.48 pt of GDP growth for a 0.72 pt primary impulse | **0.67** [computed] | [S8] |
| Government PSMT (Oct 2024), as reported by the IGF mission (Jul 2026) | Zero multiplier each year of the adjustment | 0 ("*hypothèse extrême*", an extreme assumption) | [S15, synthesis and adjustment-scenario section] |
| CAE Focus 108 (Jul 2024), illustrative | *m* = 1, ε = 0.57 | 1.0 | [S13, p. 4] |
| Banque de France, Mar 2026 | Effect of a smaller consolidation offset by caution | ≈ 0 (net, judgment) | [S14] |

---

## 4. State dependence: when multipliers are larger

- **Cycle.** The Cour des comptes: the growth cost is "*significativement plus élevé lorsque l'économie est en bas de cycle*" (significantly higher when the economy is at a cyclical low), citing Auerbach-Gorodnichenko (2012) [S5, p. 139]. Blanchard-Leigh cite Auerbach-Gorodnichenko's US estimates: from "near zero in normal times to about 2.5 during recessions" [S2, p. 3]. Note that AFG find slightly *smaller* multipliers in recessions for their plans [S4, Table 1]. This is a live disagreement.
- **Monetary constraint.** In the ESCB models, a two-year zero lower bound raises the euro-area spending multiplier from 0.98 to **1.39** (year 1), and France's from 0.92 to 1.05 [S11, Table 1]. In 2026-27 the ECB is not at the lower bound (10-year OAT 4.44% in Sep 2026, `00-reference-figures.md` row 43), so baseline (non-ZLB) values apply.
- **Exchange-rate regime.** GLP: 0.84 under pegs vs 0.33 under floating rates [S3, PDF p. 24]. France inside the euro area behaves like a peg vis-à-vis its main partners. This argues against using very low "floating" values.
- **Credibility and financial stress.** The Cour: when debt sustainability is questioned through sovereign spreads, "*une concentration de l'effort en début de période est à privilégier*" (front-loading the effort is preferable). When multipliers are high, "*un étalement de l'effort minimise la perte cumulée*" (spreading the effort minimizes the cumulative loss) [S5, p. 140]. The administration's footnote to the HCFP makes the same point. Without consolidation, uncertainty and higher rates would also cost growth [S1, fn. 9].
- **Hysteresis.** Fatás-Summers (2018), cited by the Cour, find that consolidations can lower potential output permanently [S5, p. 138, fn. 208 and 214]; the Cour puts the persistent loss at 4-6 points of GDP in the most exposed euro-area countries [S5, fn. 213]. (Corrected 2026-10-25: Gechert et al. (2019) was listed as a hysteresis source; the Cour cites it, fn. 212, for the underestimated short-run recessive impact of the Greek, Portuguese and Irish programs, not for hysteresis.)

---

## 5. International comparison

### 5.1 ESCB model comparison: temporary 1%-of-GDP shocks, no zero lower bound [S11, Tables 1, 2, 4]

*Positive = GDP loss. EU-27 or OECD aggregates do not exist for model multipliers; the comparison set is the 14 countries modeled (Belgium, Czech Republic, Estonia, Finland, France, Germany, Greece, Italy, Malta, Netherlands, Portugal, Slovenia, Spain, Sweden). The euro-area row is a separate area-wide model, not an average. Rank 1 = highest multiplier. Denmark is not covered, so the requested panel has 7 countries (FR, DE, IT, ES, NL, BE, SE); the Netherlands is missing from Table 4.* [computed]

| Shock | Year | France | Euro area model | 14-country mean | 14-country median | France rank (of 14) | Panel (FR DE IT ES NL BE SE) mean / median | France rank in panel |
|---|---|---|---|---|---|---|---|---|
| Government consumption cut | 1 | **0.92** | 0.98 | 0.73 | 0.75 | **2nd** (behind BE 0.93) | 0.71 / 0.74 | 2nd of 7 |
| Government consumption cut | 2 | 0.71 | 0.91 | 0.59 | 0.65 | 5th | 0.63 / 0.67 | 3rd of 7 |
| Labor income tax rise | 1 | 0.13 | 0.11 | 0.19 | 0.12 | 6th (tied with ES) | 0.12 / 0.11 | 2nd of 7 (tied with ES) |
| Labor income tax rise | 2 | 0.30 | 0.19 | 0.30 | 0.20 | 6th | 0.17 / 0.13 | 2nd of 7 |
| Consumption tax (VAT) rise | 1 | 0.14 | 0.48 | 0.28 (n = 13) | 0.19 | 12th of 13 (tied with ES) | 0.18 / 0.17 (n = 6) | 5th of 6 (tied with ES) |
| Consumption tax (VAT) rise | 2 | 0.23 | 0.62 | 0.30 | 0.23 | 7th of 13 | 0.27 / 0.23 | 3rd of 6 |

Panel values for the government-consumption cut, year 1: FR 0.92, BE 0.93, IT 0.79, NL 0.74, SE 0.60, DE 0.52, ES 0.50 [S11, Table 1].

**Reading.** France's spending multiplier is high by European standards: a fairly closed services economy with a low import content for public demand (Mésange makes the same point for public investment [S6, p. 103]). Its tax multipliers are near the median. Differences across countries also reflect model design (some models fix monetary policy exogenously: Finland, Greece, Netherlands, Portugal), so ranks should be read as indicative only.

### 5.2 Narrative cross-country evidence

GLP and AFG are pooled OECD panels; they do not give country-specific values. GLP's 17 countries include France, Germany, Italy, Spain, Netherlands, Belgium, Sweden and Denmark [S3, PDF p. 10]. Blanchard-Leigh's 26 European economies also include France [S2]. **No published primary source gives a France-only narrative multiplier.** The simulator should therefore use French model values for the level and the narrative literature for the band and the composition debate.

---

## 6. Divergences and economists' disagreements

| Issue | Position A | Position B | Status |
|---|---|---|---|
| **Spending-based vs tax-based** | Alesina-Favero-Giavazzi: spending-based plans cost 0.3-0.5 over 5 years, tax-based 1.0-1.5 [S4]; GLP also find tax-based costlier, 1.29 vs 0.43 [S3] | French macro models: spending cuts cost *more* in year 1 (0.78 vs 0.3-0.4 for taxes) [S6][S9]. The Cour des comptes summarizes the narrative approach as "*quel que soit le levier retenu, en dépense ou en recette, le coût à court terme serait comparable*" (whatever the lever, spending or revenue, the short-run cost would be comparable) [S5, p. 139] | **Divergence within the sources.** The Cour's summary of GLP is softer than GLP's own point estimates. GLP find spending-based adjustments "less contractionary ... particularly after the first year", but still contractionary [S3, PDF p. 26]. Composition *within* spending and taxes matters more than the split, per the Cour. |
| **VAT** | Mésange: VAT is as costly as income tax by year 3-5 (0.72-0.81) [S6] | e-mod.fr: VAT is the least costly instrument (0.1-0.3), because the price rise feeds into nominal wages and lowers imports [S9]; ESCB France model: 0.14-0.23 [S11] | Unresolved. Use a wide band. |
| **Pension age** | Micro-based: GDP +1.1%, balance +0.9 pt by 2030 [S10] | Keynesian models: GDP -0.1% to +0.3% at 10 years, balance +0.1 to +0.4 pt [S10] | The Cour leans toward the micro evidence [S10, p. 67]. |
| **Capital and wealth taxes** | Short-run cost near zero (OFCE CDHR ≈ 0; ESCB capital tax 0.07) [S8][S11]. The Cour: higher property or inheritance taxes (excluding business assets) have a low cost for potential growth [S5, p. 139] | ESCB permanent capital-income tax: long-run GDP loss 3.27 for France [S11, Table 6]. Mobility and emigration effects (CAE Focus 118, file 10 §5) | **No direct macro multiplier for a wealth tax exists** in the sources reviewed. |
| **Size in normal times** | Blanchard-Leigh: crisis multipliers above 1 [S2]; Gechert: spending close to 1 [S16] | Ramey: 0.6-1 [S17]; Government PSMT: 0 [S15]. (Corrected 2026-10-25: this cell listed "later-vintage B-L coefficients 0.3-0.5" as low multipliers. They are *forecast-error* coefficients, i.e. the amount by which multipliers were *underestimated*; with assumed multipliers of about 0.5 they imply actual multipliers of about 0.8-1.0 in 2011-13, which supports Position A's range, not a low value [S2, p. 3].) | Consensus range for 2027 (normal times, euro area): **0.5-1.0** for spending. |
| **Greece example** | The Cour: Greek program assumed 0.5; actual multiplier was "*trois à quatre fois plus élevé (entre 1,5 et 2)*" (three to four times higher, between 1.5 and 2), citing Blanchard-Leigh (AER 2013) [S5, p. 119] | Blanchard-Leigh estimate a *European average* underestimation of about 1 (implying about 1.5 on average), not a Greece-specific multiplier [S2] | Minor attribution divergence in the Cour report. The 1.5-2 range is the Cour's reading. |
| **Confidence channel** | Banque de France (Mar 2026): less consolidation gives no extra growth because of wait-and-see behavior [S14] | OFCE: the 2026 budget cuts growth by 0.5 pt [S8] | Both can be true. The net effect depends on the credibility of the path. |

**Orientation flags:** OFCE (Sciences Po, Keynesian-leaning); IMK (trade-union-funded); Rexecode (employer-funded); Alesina-Favero-Giavazzi (Bocconi, associated with the "expansionary austerity" thesis). Insee/DG Trésor, Banque de France, ECB/ESCB, IMF, HCFP, Cour des comptes and CAE are official or official-advisory bodies.

---

## 7. Instrument-by-instrument evidence summary

*Positive = GDP loss per 1 pt of GDP of consolidation. "Y1" = year 1; "Y3-5" = level effect at years 3-5 of a permanent measure.*

| Instrument | Y1 evidence | Y3-5 evidence | Notes |
|---|---|---|---|
| Spending on goods and services, public wages, operating costs | Mésange 0.78; OFCE 0.7-0.8; ESCB FR 0.92; BdF ≈ 1.0; GLP spending-based 0.43 (2 years); AFG 0.28-0.46 (5-year cumulative) | Mésange 1.03 (y3), 0.86 (y5); ESCB FR 0.71 (y2) | Highest short-run demand effect. |
| Public investment | Mésange 1.31; Gechert +0.5 vs spending in general | Mésange 1.22 (y3), 0.93 (y5) | Mésange omits public-capital productivity, so long-run costs are understated. |
| Health and other transfers in kind | e-mod.fr 1.0 | e-mod.fr 0.9 (y3), 0.7 (y5) | Behaves like public consumption. |
| Cash social transfers (working-age) | Proxy: Mésange CSG/IR 0.41; OFCE *prime d'activité* ≈ 1 (targeted at low incomes) | Proxy: Mésange 0.81-0.90 | Targeted low-income transfers sit at the top of the band (high propensity to consume). |
| Pension benefits and indexation | e-mod.fr 0.3 | e-mod.fr 0.7 | The Cour: low cost for *potential* growth [S5]. |
| VAT | Mésange 0.32; e-mod.fr 0.2; ESCB FR 0.14 | Mésange 0.72-0.81; e-mod.fr 0.1-0.2 | Largest model disagreement. |
| Income tax and CSG | Mésange 0.41; e-mod.fr CSG 0.3; ESCB FR labor tax 0.13 | Mésange 0.81-0.90; e-mod.fr 0.6-0.7 | |
| Employer contributions and production taxes | Mésange 0.20; e-mod.fr 0.4 | Mésange 0.76-0.97 (long run 1.73); e-mod.fr 0.6-0.7 | Costs rise over time (labor-cost channel). |
| Corporate surtaxes, capital-income taxes | OFCE 0.29 (large-firm surtax), 0.4 (CSG on financial income); ESCB FR capital tax 0.07 | ESCB permanent capital tax 0.61 (y2), 3.27 (long run) | Low short run, potentially high long run. |
| Wealth tax (*taxe Zucman*-type) | No direct estimate. Proxies: OFCE CDHR ≈ 0; ESCB capital tax 0.07 | No direct estimate | ⚠ simulator default is an expert proxy, not a published value. |
| Pension age +2 years | ≈ 0 (e-mod.fr 0.0) | GDP -0.1% to +0.3% at 10 years (macro); +1.1% by 2030 (micro) | Supply gain; model as a GDP *gain* over time. |
| Interest charges, EU contribution | OFCE ≈ 0-0.16 | n/a | Not a user lever. |

---

## 8. Recommended simulator defaults and uncertainty ranges

*Design rule: show the central value, a low-high band, and the source. All values are for 2027 "normal times" (no zero lower bound, euro-area monetary policy unchanged). Positive = GDP loss per euro of consolidation. For measures that lower the deficit by raising spending or cutting taxes, apply the same value with the opposite sign (the models are approximately linear for small shocks [S6, p. 100]).*

| Simulator lever | Default Y1 | Range Y1 | Default Y3-5 | Range Y3-5 | Main basis |
|---|---|---|---|---|---|
| Cuts in operating spending and public wage bill | **0.8** | 0.5-1.1 | **0.7** | 0.4-1.0 | Mésange; OFCE PB 154; ESCB; BdF; GLP (low end) |
| Cuts in public investment | **1.0** | 0.6-1.4 | **0.9** | 0.5-1.3, plus a long-run potential-growth warning | Mésange; Gechert; Cour (investment cuts "*pas nécessairement gagnante à moyen terme*", not necessarily a winner in the medium term) |
| Cuts in health and other transfers in kind | **0.8** | 0.5-1.0 | **0.7** | 0.4-0.9 | e-mod.fr; OFCE social-security savings 0.69 |
| Cuts in cash social benefits (working-age, means-tested) | **0.5** | 0.3-1.0 | **0.7** | 0.4-0.9 | Mésange CSG/IR proxy; OFCE *prime d'activité* ≈ 1 |
| Pension under-indexation or freeze | **0.3** | 0.2-0.5 | **0.6** | 0.3-0.8 | e-mod.fr; Cour 2026 (low potential-growth cost) |
| VAT rise | **0.3** | 0.1-0.5 | **0.5** | 0.1-0.8 | Mésange vs e-mod.fr vs ESCB |
| Income tax or CSG rise | **0.4** | 0.1-0.5 | **0.8** | 0.4-0.9 | Mésange; e-mod.fr; ESCB |
| Employer contributions or production taxes | **0.3** | 0.2-0.4 | **0.7** | 0.6-1.0, rising in the long run | Mésange; e-mod.fr |
| Corporate surtax, taxes on capital income | **0.3** | 0.1-0.4 | **0.4** | 0.2-0.8, with a long-run warning | OFCE PB 154; ESCB |
| Wealth tax on very large fortunes | **0.1** | 0.0-0.3 | **0.2** | 0.0-0.5 | Expert proxy (OFCE CDHR ≈ 0; ESCB capital tax). ⚠ no direct estimate. The revenue uncertainty (EUR 2-25 bn, file 10) dominates the multiplier uncertainty |
| Pension age +2 years (or -2 to 60: reverse sign) | GDP effect **0.0** | -0.1 to +0.1 | GDP **+0.3% at 10 years** | -0.1% to +1.1% | Cour 2025 model comparison; net balance gain **+0.4 pt** (range +0.1 to +0.9) |
| Cuts in interest charges or EU contribution | 0 | 0-0.2 | 0 | 0 | OFCE PB 154 (not a user lever) |

**Feedback to the deficit.** Use ε = **0.57** (deficit semi-elasticity to the output gap, from CAE Focus 108 [S13]). Net deficit improvement ≈ measure × (1 - multiplier × 0.57). Cross-check [computed 2026-10-25]: the rule matches the models' year-1 balance responses within ±0.05 pt for Mésange generic spending (rule 0.56 vs model 0.53), VAT (0.82 vs 0.80), CSG and income tax (0.77 vs 0.81) and employee contributions (0.78 vs 0.73) [S6]. It does **not** match for Mésange public investment (0.25 vs 0.49) and employer contributions (0.89 vs 0.72), nor for e-mod.fr VAT (0.89 vs 0.5), transfers in kind (0.43 vs 0.6) and employee contributions (0.77 vs 0.9) [S9]. The main reason is that price effects (indexed benefits, the public wage bill, the tax base) move the balance independently of real GDP. (Corrected 2026-10-25: this paragraph said the model results "are consistent with this rule" without qualification.) Recommendation: keep the 0.57 rule as the v1 default, but for VAT and employer contributions show the model's own balance gain as an alternative. ⚠ The European Commission's own semi-elasticity for France was not re-read in this file.

**Optional "context" toggles** (v2, as in file 20 §451):
- *Recession or zero lower bound:* multiply spending multipliers by about 1.4 (ESCB euro-area ZLB variant 0.98 → 1.39 [S11]; Gechert-Rannenberg's downturn increase of 0.6-0.8, reported in a search summary and not re-read here, is ⚠ unverified).
- *Credible, pre-announced path:* allow the user to see the "zero multiplier" bound (the PSMT assumption, called "very favorable" by the IGF [S15]).
- *Front-loaded vs gradual:* for the cumulative GDP loss, sum annual effects. The Cour recommends spreading the effort when multipliers are high and front-loading under market stress [S5, p. 140].

**What the simulator should not do:** present any multiplier as a known constant; show a "self-financing" spending cut (no source in this file supports a multiplier above 1/0.57 ≈ 1.75 in normal times, the threshold at which a cut would *worsen* the deficit); or apply crisis-era values (1.5-2) to 2027.

---

## 9. Gaps and caveats

1. **No France-only narrative multiplier** exists in the sources reviewed (§5.2).
2. **No direct wealth-tax multiplier** (§7). The default is a proxy.
3. The **2017 Mésange** variants are the latest published full set. A newer Mésange version, if any, was not found. The DG Trésor's January 2022 pension-age note is cited through the Cour [S10], not read directly.
4. **IMF sources** (WEO Oct 2012 Box 1.1; Batini et al. 2014 multiplier note) could not be downloaded: imf.org returned 403/404/429 to curl, WebFetch and the puppeteer browser on 2026-10-25. GLP was read through a WebFetch cached copy of IMF WP 11/158.
5. **Multipliers are not additive with behavioral revenue effects.** Static costings in file 11 (e.g., the *taxe Zucman* EUR 2-25 bn range) already include, or should include, behavioral responses. The simulator should apply the macro multiplier on top of the *expected* yield, not the mechanical yield.
6. Model results assume **constant real interest rates** (Mésange) or a common ECB policy (BdF, ESCB). A France-specific sovereign-spread channel is not modeled in any of them.

---

## 10. Sources (all accessed 2026-10-25)

| # | Institution / authors | Title | Publication date | URL |
|---|---|---|---|---|
| S1 | Haut Conseil des finances publiques (HCFP) | *Avis n° HCFP-2026-5 relatif aux projets de lois de finances et de financement de la sécurité sociale pour l'année 2027*, §36 and fn. 9 | 25 Sep 2026 | https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf (local: `data/raw/hcfp/a.txt`) |
| S2 | Blanchard, O. & Leigh, D. (IMF) | *Growth Forecast Errors and Fiscal Multipliers*, NBER WP 18779 / IMF WP 13/1; AER 103(3): 117-120 | Jan-May 2013 | https://www.nber.org/papers/w18779 (local: `data/raw/papers_debates/blanchard_leigh_w18779.pdf`) |
| S2b | IMF | *World Economic Outlook*, Oct 2012, Box 1.1 "Are We Underestimating Short-Term Fiscal Multipliers?" | Oct 2012 | https://www.imf.org/en/Publications/WEO/Issues/2016/12/31/World-Economic-Outlook-October-2012-Coping-with-High-Debt-and-Sluggish-Growth-25845 (⚠ PDF blocked) |
| S3 | Guajardo, J., Leigh, D. & Pescatori, A. (IMF) | *Expansionary Austerity: New International Evidence*, IMF WP 11/158; published as *Expansionary Austerity? International Evidence*, JEEA 12(4): 949-968 | Jul 2011; Aug 2014 | https://www.imf.org/external/pubs/ft/wp/2011/wp11158.pdf ; https://ideas.repec.org/a/bla/jeurec/v12y2014i4p949-968.html (local: `data/raw/17_multipliers/glp_wp11158.pdf`) |
| S4 | Alesina, A., Favero, C. & Giavazzi, F. (Bocconi/Harvard; "expansionary austerity" school) | *What Do We Know About the Effects of Austerity?*, NBER WP 24246 (AEA P&P 108, 2018); book *Austerity: When It Works and When It Doesn't*, Princeton UP | Jan 2018; 2019 | https://www.nber.org/papers/w24246 (local: `data/raw/17_multipliers/afg_w24246.pdf`) |
| S5 | Cour des comptes | *La situation et les perspectives des finances publiques* (RSPFP), ch. 3, pp. 96-140 | 25 Jun 2026 | https://www.ccomptes.fr/sites/default/files/2026-07/20260625_RSPFP-2026.pdf (local: `data/raw/ccomptes_debates/rspfp_2026.txt`) |
| S6 | DG Trésor & Insee (Dufernez, Elezaar, Leblanc, Masson, Partouche; Bardaji, Campagne, Khder, Lafféter, Simon) (corrected 2026-10-25: was "Bardaji et al."; Dufernez is listed first on the DG Trésor edition) | *Le modèle macroéconométrique Mésange : réestimation et nouveautés*, Document de travail DG Trésor n° 2017/04 (Insee G2017/04), Ch. 4 | May 2017 | https://www.tresor.economie.gouv.fr/Articles/2017/05/12/le-modele-macroeconometrique-mesange-reestimation-et-nouveautes ; PDF https://www.tresor.economie.gouv.fr/Articles/88381f48-797c-4e76-8f03-ef78d0bff99e/files/1c29ff21-585d-488b-8f4b-497540e9fc62 (local: `data/raw/17_multipliers/tresor_dt201704.pdf`) |
| S8 | OFCE (Madec, Plane, Sampognaro) | *Budget 2026 : un déficit de compromis*, Policy Brief n° 154, Table 4 | 26 Feb 2026 (modified 1 Mar 2026) | https://ofce.github.io/budget2026/ (local: `data/raw/17_multipliers/ofce_budget2026.html`) |
| S9 | OFCE for the HCFiPS (reproduced by the COR) | *Les effets macroéconomiques de leviers possibles de redressement des comptes sociaux - 10 variantes à partir du modèle e-mod.fr de l'OFCE* (HCFiPS report *Pour des finances sociales soutenables, adaptées aux nouveaux défis*, vol. 2) | OFCE report Oct 2021; HCFiPS report Jan 2022; COR session 27 Jan 2022 | https://www.cor-retraites.fr/sites/default/files/2022-01/Doc13_Effets%20macro_OFCE.pdf (local: `data/raw/17_multipliers/cor_doc13_ofce.pdf`) |
| S10 | Cour des comptes | *Situation financière et perspectives du système de retraites*, Table 4, pp. 65-67 | 20 Feb 2025 | https://www.vie-publique.fr/files/rapport/pdf/297428.pdf (local: `data/raw/pensions/ccomptes_retraites_fev2025.txt`) |
| S11 | ECB / ESCB (Kilponen, Pisani, Schmidt et al.; Banque de France: Lemoine) | *Comparing Fiscal Multipliers across Models and Countries in Europe*, ECB WP 1760, Tables 1-6 and A1 (published as *Comparing Fiscal Consolidation Multipliers across Models in Europe*, IJCB 15(3): 285-320, 2019; journal reference confirmed via the bibliography of S12) | Mar 2015 | https://www.ecb.europa.eu/pub/pdf/scpwps/ecbwp1760.en.pdf (local: `data/raw/17_multipliers/ecb_wp1760.pdf`) |
| S12 | Banque de France (Aldama, Gaulier, Lemoine, Robert, Turunen, Zhutova) | *The EA-BDF Model and Government Spending Multipliers in a Monetary Union*, WP 883, section 5 | Sep 2022 | https://www.banque-france.fr/system/files/2023-01/wp883.pdf (local: `data/raw/17_multipliers/bdf_wp883.pdf`) |
| S13 | CAE (Auclert, Philippon, Ragot) | *Fiscal Consolidation: An Optimal Control Approach* (*Consolider les finances publiques : quelques enseignements simples de la théorie du contrôle optimal*, consolidating public finances: some simple lessons from optimal control theory), Focus n° 108, companion to CAE Note n° 82. X. Ragot is also president of the OFCE | 24 Jul 2024 | https://www.cae-eco.fr/static/pdf/focus-108-240712-en.pdf (local: `data/raw/17_multipliers/cae_focus108_en.pdf`) |
| S14 | Banque de France | *Projections macroéconomiques - France*, interim projections | 25 Mar 2026 | https://www.banque-france.fr/system/files/2026-03/Projections-macroeconomiques_mars-2026_web2.pdf (local: `data/raw/17_multipliers/bdf_proj_mar2026.pdf`) |
| S15 | Mission on public-finance transparency (Jaravel, Ragot, Tavernier, Valla), hosted by the IGF | *Mission sur la transparence des finances publiques : situation tendancielle à horizon 2030* | Jul 2026 | https://www.igf.gouv.fr/files/igf/files/contributed/Rapports%20de%20mission/2026/Transparence-finances-publiques.pdf (local: `data/raw/06_verify/igf.txt`) |
| S16 | Gechert, S. (IMK, Hans-Böckler Foundation, trade-union funded) | *What Fiscal Policy Is Most Effective? A Meta Regression Analysis*, IMK WP 117 (published in *Oxford Economic Papers* 67(3), 2015) | Sep 2013 | https://www.imk-boeckler.de/fpdf/HBS-005632/p_imk_wp_117_2013.pdf (local: `data/raw/17_multipliers/gechert_imk117.pdf`) |
| S17 | Ramey, V. | *Ten Years After the Financial Crisis: What Have We Learned from the Renaissance in Fiscal Research?*, *Journal of Economic Perspectives* 33(2): 89-114 | Spring 2019 | https://www.aeaweb.org/articles?id=10.1257/jep.33.2.89 |

Related files in this base: file 03 §189, §225 (pension-age feedback); file 06 §422-424 (austerity multipliers, IGF zero multiplier); file 10 §6 (Debate 4); file 11 §9 (LFI growth argument); file 20 §451, §671 (simulator v1/v2 plan).

---

## 11. Verification log

*Second pass on 2026-10-25: each headline figure was re-read in the primary text (grep on the saved PDF text or table re-extraction), not from memory or from the first-pass notes.*

| # | Figure | Primary check | Result |
|---|---|---|---|
| 1 | Blanchard-Leigh β = -1.095 (t = -4.294); "substantially above 1"; later vintages 0.3-0.5 "less statistically significant"; spending 1.244 vs revenue -0.865 | NBER WP 18779 text, pp. 2-3, 9, Table 1 and Table 5 | **Confirmed** |
| 2 | WEO 2012 Box 1.1 range 0.9-1.7 | imf.org blocked (403/404/429) | ⚠ **Not re-verified**; carried from file 10 |
| 3 | GLP: -0.62 GDP / -0.75 consumption within 2 years; spending-based -0.43; tax-based -1.29; peg 0.84 vs float 0.33 | IMF WP 11/158 text, PDF pp. 6, 13, 24, 26 | **Confirmed** (WP version; JEEA 2014 numbers not re-read) |
| 4 | AFG: EB 0.46 / TB 1.50 (expansion); EB 0.28 / TB 0.96 (recession); "about half of a percentage point"; "a two percent fall" | NBER WP 24246, pp. 5-8, Table 1 | **Confirmed** |
| 5 | Mésange: spending 0.78 / 1.03 / 0.86; investment 1.31 / 1.22 / 0.93; VAT 0.32 / 0.72 / 0.81; IR 0.41 / 0.88 / 0.81; CSG 0.41 / 0.90 / 0.81; employer contributions 0.20 / 0.76 / 0.97 (LT 1.73) | Re-extracted PDF pp. 104, 107, 109, 112, 114, 117, 119 with `pdftotext -raw` (the `-layout` output had scrambled columns, so it was discarded) | **Confirmed** |
| 6 | e-mod.fr GDP paths and balance table | COR Doc 13 text, Tables 1, 5, 11, 13, 15, 20, 22, 24 | **Confirmed**, with a note on two table titles that do not match their sections (§3.2) |
| 7 | OFCE PB 154: 0.7-0.8; defense and *prime d'activité* about 1; -0.5 pt of growth; Table 4 rows | HTML page text, Table 4 | **Confirmed**. Implied ratios are [computed]; small items are sensitive to rounding |
| 8 | HCFP: 0.5 pt growth cost for a 0.5 pt (0.8 pt primary) adjustment, "credible" | Avis HCFP-2026-5 §36 | **Confirmed**. The ≈ 0.6 ratio is [computed] |
| 9 | Cour 2026: "comparable" quote; Greece 0.5 vs "1.5-2"; front-loading vs spreading | RSPFP 2026 text, pp. 119, 138-140 | **Confirmed** (attribution divergence noted in §6) |
| 10 | Cour 2025 pension table: GDP +0.3 / -0.1 / +1.1 / +1.1; balance +0.4 / +0.1 / +0.9 / +0.6 | Cour Feb 2025 text, Table 4 | **Confirmed** |
| 11 | ESCB: France 0.92 / 0.71; euro area 0.98 / 0.91, ZLB 1.39; panel statistics and ranks | ECB WP 1760, Tables 1, 2, 4, 6; statistics recomputed by script | **Confirmed**. The permanent-shock Table 5 extracted with scrambled rows and is **not used** |
| 12 | BdF WP 883: France about 1.1 (VBE) / 1.0 (MCE) symmetric; 1.0 / 0.9 asymmetric | WP 883 text, pp. 53-55 | **Confirmed** |
| 13 | BdF Mar 2026 "*attentisme accru*" (greater wait-and-see behavior) | Projections PDF, p. 1 | **Confirmed** |
| 14 | CAE ε = 0.57, *m* = 1 | Focus 108 text, p. 4 | **Confirmed** |
| 15 | IGF: zero multiplier "*hypothèse très favorable*" (a very favorable assumption) / "*particulièrement forte*" (particularly strong) | Local IGF text, synthesis and adjustment-scenario section (lines 67-73 and 1307-1319 of `data/raw/06_verify/igf.txt`) | **Confirmed** |
| 16 | Gechert: spending close to 1, +0.3-0.4 over taxes and transfers, investment +0.5 | IMK WP 117 abstract | **Confirmed** (WP; OEP 2015 version not re-read) |
| 17 | Ramey: spending 0.6-1; taxes 2-3 | AEA abstract page | **Confirmed** |
| 18 | Gechert-Rannenberg downturn increase of 0.6-0.8 | Search summary only | ⚠ **Not verified**. Used only as an optional toggle note |
| 19 | "EUR 30 bn per point of GDP" | 1,714.1 / 0.573 = 2,991 bn (`00-reference-figures.md` row 1) | **Confirmed** [computed] |

**Unverified items still flagged in the text:** WEO 2012 range (row 2); European Commission semi-elasticity for France (§8); Gechert-Rannenberg (row 18); the wealth-tax default (an expert proxy, not a published value).

---

## 12. Verification log: adversarial pass (2026-10-25)

*Third pass, by an adversarial fact-checker, on 2026-10-25. Each headline figure was re-read in the saved primary text and the computations were re-run. Mésange tables: `pdftotext -raw` per page. ESCB tables: fresh `pdftotext -layout` extraction. ESCB rank statistics: recomputed by script. The aim was to refute figures, not to re-confirm the earlier log.*

| # | Claim tested | Primary check | Verdict |
|---|---|---|---|
| A1 | HCFP: 0.5 pt of growth for a 0.5 pt (0.8 pt primary) adjustment; "credible"; fn. 9 | `hcfp/a.txt`, §36 and fn. 9 | **Confirmed.** The page was wrong: §36 is on p. 13, not p. 12. **Corrected in §3.6** |
| A2 | Mésange, all 7 variants (year 1/2/3/5/10/LT and year-1 primary balance) | PDF pp. 104, 107, 109, 112, 114, 117, 119 | **Confirmed**, all 49 GDP cells and 7 balance cells. The chapter page range and the author attribution were wrong. **Corrected in §3.1 and S6** |
| A3 | e-mod.fr GDP paths (Tables 5, 11, 13, 15, 20, 22, 24; columns are years 1-5 and 10) and Table 1 balance gains | `emod_u.txt` | **Confirmed**, including the year-5 values (taken from column 5, not column 4). The source date was refined to "OFCE Oct 2021; HCFiPS Jan 2022" (S9) |
| A4 | OFCE PB 154 Table 4 and implied ratios 0.81 / 0.82 / 0.69 / 0.29 / 0.30 / 0.67 / 0.16 | HTML text, Table 4 | **Confirmed** [computed] |
| A5 | ESCB: France 0.92 / 0.71 / ZLB 1.05; EA 0.98 → 1.39; labor tax 0.13 / 0.30; capital 0.07 / 0.08; VAT 0.14 / 0.23; permanent capital tax 0.36 / 0.61 / 3.27; every mean, median and rank in §5.1 | ECB WP 1760, Tables 1-4 and 6; script | **Numbers confirmed.** The model for France was mislabeled. It is **EAGLE** (Jacquinot and Lemoine 2013, Table A1), a multi-country ESCB model, not "the Banque de France model". **Corrected in §0 item 2 and §3.4.** IJCB 15(3): 285-320 confirmed via the bibliography of S12; the journal title differs from the WP title |
| A6 | BdF WP 883: about 1.1 / 1.0 (symmetric), 1.0 / 0.9 (asymmetric), REA 0.9; 10-year 0.13-0.16 | `bdf883.txt`, pp. 52-55, fn. 36 | **Confirmed.** The 10-year values apply to the asymmetric case, and the page range starts at p. 52. **Clarified in §3.4** |
| A7 | BdF Mar 2026 "*attentisme accru*" | PDF page scan | **Confirmed**, but the quote is on PDF p. 2, not p. 1. **Corrected** |
| A8 | CAE ε = 0.57, *m* = 1 | `cae108.txt` | **Confirmed.** The CAE listing confirms the date (24 Jul 2024) and the full French title (**S13 updated**). ε is the CAE's "elasticity of the conjunctural deficit to the output gap" for the 2023 application |
| A9 | Budget-feedback cross-check ("model balances are consistent with the 0.57 rule") | Rule 1 - 0.57*m* vs Mésange and e-mod.fr year-1 balances [computed] | **Refuted in part.** The rule fails for Mésange investment (0.25 vs 0.49) and employer contributions (0.89 vs 0.72), and for e-mod.fr VAT (0.89 vs 0.5), transfers in kind and employee contributions. **Corrected in §8**, with a recommendation |
| A10 | Blanchard-Leigh β = -1.095; about 0.5 assumed; "substantially above 1"; later vintages 0.3-0.5; A-G "near zero ... about 2.5" | NBER WP 18779 text | **Figures confirmed.** §6 ("Size in normal times") misused them: it cited the later-vintage *coefficients* 0.3-0.5 as if they were low *multipliers*. They measure underestimation, so the implied multipliers are about 0.8-1.0. **Corrected in §6** |
| A11 | GLP -0.62 / -0.75; spending-based -0.43 (t = -2.38); tax-based -1.29 (t = -4.67); peg 0.84 vs float 0.33; 17 countries incl. FR, DE, IT, ES, NL, BE, SE, DK | `glp.txt`, PDF pp. 10, 24, 26 | **Confirmed** |
| A12 | AFG EB 0.46 / TB 1.50 (expansion), 0.28 / 0.96 (recession); 0.75 / 3.70; "half of a percentage point"; "two percent" | `afg.txt`, pp. 5-8, Table 1 | **Numbers confirmed.** The §2 takeaway was wrong: it said AFG attribute the EB/TB gap partly to accompanying policies. AFG (p. 9) say that GLP argue this, and that they themselves find "only a small fraction" is due to monetary policy. **Corrected in §2** |
| A13 | Cour RSPFP 2026: definition (fn. 122, p. 119); Greece 0.5 vs 1.5-2 (fn. 123, B-L); "comparable" (p. 139, fn. 217 = GLP 2014); bottom of the cycle (fn. 216 = A-G); spreading vs front-loading (p. 140); investment "*pas nécessairement gagnante*" (p. 139) | `rspfp_2026.txt` | **Confirmed.** The hysteresis citation was wrong: Gechert et al. (2019) is cited in fn. 212 for an underestimated short-run impact, not for hysteresis. **Corrected in §4.** The Cour also conditions front-loading on "*la situation conjoncturelle n'est pas trop dégradée*" (the cyclical situation not being too bad) and cites the IMF (fn. 219) |
| A14 | Cour Feb 2025 Table 4: GDP +0.3 / -0.1 / +1.1 / +1.1; GG balance +0.4 / +0.1 / +0.9 / +0.6; unemployment +0.7 / +0.5; 1.2% → 1.7%; 20% spillover | `ccomptes_retraites_fev2025.txt`, pp. 66-67 | **Confirmed.** Caveat: the "pension-system balance" row extracts with only three values for four columns. The assignment (Mésange +0.4, e-mod.fr n/a, DG Trésor +0.4, Rexecode +0.4) is plausible but should be checked visually on the PDF before it is shown on the website. Rexecode funding (Medef, UIMM) is confirmed in the Cour's fn. 121 |
| A15 | IGF: zero multiplier "*hypothèse très favorable*" / "*hypothèse extrême*" / "*particulièrement forte*", as in the PSMT | `igf.txt`, lines 70 and 1310-1319; authors and date (Jul 2026) from the title page | **Confirmed** |
| A16 | Gechert: 104 studies; spending close to 1; +0.3-0.4 over taxes and transfers; investment about +0.5; crisis scenario close to 2 | IMK WP 117 abstract and p. 2 | **Confirmed.** The body text gives investment at "0.3 to 0.8 units above" spending in general; the abstract says "approximately 0.5" |
| A17 | Ramey: spending 0.6-1; tax 2-3 | AEA abstract (WebFetch, 2026-10-25): "0.6 to 1 for spending multipliers and -2 to -3 for tax change multipliers" | **Confirmed** (sign convention converted) |
| A18 | WEO Oct 2012 Box 1.1 range 0.9-1.7 | imf.org PDF: HTTP 403 again; only press sources found | **⚠ Still unverified.** Recommendation: read it in the laptop browser (puppeteer) before website use |
| A19 | Arithmetic: EUR 30 bn per GDP point; 1 - 0.8 × 0.57 = 0.544 (EUR 16 bn net); 1/0.57 = 1.75 | Recomputed | **Confirmed** [computed] |

**Still ⚠ unverified after this pass:** the WEO 2012 range (A18); the European Commission's semi-elasticity for France (§8); Gechert-Rannenberg's 0.6-0.8 downturn increase (§8); the wealth-tax default (an expert proxy, §7-§8); the column assignment of the Cour 2025 pension-system balance row (A14); the JEEA 2014 published GLP numbers (WP version used). None of these changes a simulator default in §8.

**Recommendation for README §7:** add a row for file 17 that lists the items above. The README has no row for this file yet.
