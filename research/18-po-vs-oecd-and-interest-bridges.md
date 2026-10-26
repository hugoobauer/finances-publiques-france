# 18 - Measurement bridges: *prélèvements obligatoires* vs OECD/Eurostat tax-to-GDP, interest burden (64.7 vs 65.7 vs budget), COFOG vs SHA health

*Gap-fill research file for the public-finance education platform. Prepared 2026-10-25. All web sources accessed 2026-10-25. It resolves the "unreconciled bridges" listed in README §9.1 item 6 and the file 09 entry in README §7. It does not edit any other file. File 00 remains canonical. Where this file proposes a wording or a value for the website, it is labeled **Recommendation**.*

**Raw data:** `research/data/raw/18/` (Insee xlsx tables 3.201-3.217 for the May 2026 accounts, Eurostat JSON extracts, Insee html pages).
**Computed CSVs:** `research/data/18_po_vs_oecd_bridge_2024.csv`, `research/data/18_interest_bridge.csv`, `research/data/18_cofog_vs_sha_health_2024.csv`.
**Conventions:** "pp" = percentage points of GDP. "Current GDP" = Insee/Eurostat May-October 2026 vintage (2024: EUR 2,935.2 bn; 2025: EUR 2,991.1 bn; Eurostat `nama_10_gdp`, updated 22 Oct 2026). EA21 = euro area including Bulgaria (file 00 convention).

---

## 0. Bottom line (for the platform editors)

1. **The 0.8-point gap between Insee's *prélèvements obligatoires* (PO, compulsory levies) 2024 (42.7%) and the OECD/Eurostat tax-to-GDP ratio (43.5%) is now fully bridged** (our computation from Insee table 3.217, Eurostat and OECD; §1.3):
   - **+0.67 pp (EUR 19.6 bn): refundable tax credits.** Insee subtracts every refundable tax credit (*crédit d'impôt restituable*: research tax credit, home-help credit, etc.) from PO. National accounts (ESA 2010) record those credits as public spending and leave tax revenue gross. Eurostat and, in practice, the OECD use the ESA figure.
   - **-0.03 pp (EUR 1.0 bn): voluntary social contributions.** Insee keeps them in PO; the compulsory Eurostat/OECD measure leaves them out.
   - **+0.11 pp: vintage.** The OECD (Dec 2025) and Eurostat's stored ratio still use the pre-May-2026 GDP (EUR 2,919.9 bn instead of 2,935.2 bn: +0.23 pp) and a slightly older numerator (-0.12 pp).
   - Total: 42.72 + 0.67 - 0.03 + 0.11 = **43.47 ≈ 43.5**.
   - **Not part of the gap:** taxes paid to the EU (EUR 2.6 bn, included in *both*), imputed social contributions (excluded by *both*) and uncollectible taxes (D.995, deducted by *both*). The brief's hypothesis that EU taxes explain part of the gap is wrong for 2024.
2. **Interest 2025: 65.7 vs 64.7 bn is a FISIM presentation choice, not an error.** EUR 65.7 bn is ESA D.41 (Eurostat, Cour des comptes, HCFP). EUR 64.7 bn is Insee's presentation "*hors correction au titre des Sifim*": FISIM (*Sifim*, financial intermediation services indirectly measured) is put back into interest. Since 2023 FISIM on public bank loans has been **negative** (old fixed-rate loans, mostly local-government loans, carry rates below the ESA reference rate). As a result, contractual interest (64.7) is **below** ESA D.41 (65.7) by EUR 1.07 bn (2024: 2.0 bn; before 2023 the sign was the opposite). Local government accounts for EUR 0.74 bn of the 2025 correction.
3. **The State's budget debt charge is a third, different concept:** EUR **51.6 bn** executed in 2025 (programme 117 + SNCF Réseau). It covers the State only, on a budget-accounting basis. The same year, ESA D.41 was EUR 52.5 bn for the State alone and **65.7 bn for all general government**. In 2026-2027 the two series diverge further: State budget **63.4 bn (2026 revised) → 72.9 bn (PLF 2027)** vs general government ESA **79.2 bn → about 91 bn**.
4. **Health: COFOG 8.9% vs SHA 9.44% of GDP (2024)** (our computation; §3.2):
   - SHA HF.1 includes **EUR 22.2 bn (0.76 pp)** of employer-mandated complementary insurance (HF.122), which is outside government.
   - COFOG includes **EUR 12.6 bn (0.43 pp)** of capital spending and EUR 3.3 bn of current R&D, which SHA excludes.
   - The remaining residual of +0.32 pp in SHA's favor reflects classification of long-term-care health services and insurance administration (partly in COFOG function 10, "social protection") and the privately financed part of public-hospital output (in COFOG gross). We could not quantify it line by line.
   - The gap with the euro area is **+1.47 pp (COFOG)** vs **+1.06-1.10 pp (SHA HF.1)**.
5. **Recommendation (canonical use on the website):**
   - France on its own: Insee PO (42.7% in 2024, 43.6% in 2025).
   - International rankings: the ESA/OECD measure (43.5% in 2024, 2nd of 27 in the EU, 1st in the euro area; 2nd of 36 in the OECD; about 44.2-44.3% in 2025 (corrected 2026-10-25: was "about 44.3%"; see §1.3)).
   - Always show the one-line bridge ("+0.7 pt = refundable tax credits counted as spending").
   - Interest: **EUR 65.7 bn (2.2% of GDP, 3.8% of TE) for 2025** as ESA D.41, with "State budget debt charge" always labeled as such.
   - Health: COFOG 8.9% when splitting public spending by function; SHA when talking about the health system. Say "1 to 1.5 points of GDP above the euro area, depending on the definition".

---

## 1. Bridge (a): Insee *prélèvements obligatoires* vs OECD / Eurostat tax-to-GDP

### 1.1 Definitions side by side

| Item | Insee PO | Eurostat `gov_10a_taxag` "taxes and compulsory social contributions" | OECD *Revenue Statistics* "total tax revenue" |
|---|---|---|---|
| Taxes D.2 + D.5 + D.91 | Yes | Yes | Yes (OECD classification 1000-6000) |
| Taxes collected for EU institutions (S.212: customs duties, formerly the Single Resolution Fund levy) | **Yes** (EUR 2.6 bn in 2024) | **Yes** (sector S13_S212) | **Yes** (included in 5000; also shown as a "supranational" memo item) |
| Actual compulsory social contributions | Yes | Yes | Yes (2000) |
| Voluntary social contributions (D.613V) | **Yes** (inside "*cotisations sociales effectives*") | No (compulsory measure) | No |
| Imputed social contributions (D.612) | No | No (they are in the "including imputed" variant, 45.3%) | No |
| Amounts assessed but unlikely to be collected (D.995) | Deducted | Deducted | Deducted (France: allocated pro rata across tax headings, OECD Box 3.1) |
| Refundable (payable) tax credits | **Deducted in full**, both the part offset against tax due and the part paid out | Not deducted (ESA records them as spending: subsidies D.3, benefits D.6, transfers D.7/D.9) | Guidance: deduct only the part offset against tax ("split basis"). **In practice France's OECD figure equals the ESA gross figure** (see 1.4). |
| Denominator | Current Insee GDP | Eurostat GDP at time of computation of the stored ratio | OECD GDP for tax-reporting year (France 2024: EUR 2,919.9 bn) |

Sources: Insee table 3.217 note ("*Prélèvements obligatoires = (I)+(II)+(III)+(IV)*"); Insee definition in *Dépenses et recettes des administrations publiques en 2024* ("*déduction faite des impôts et cotisations dus mais non recouvrables ainsi que des crédits d'impôts*"); Insee PO series note ("*hors cotisations sociales imputées et crédit d'impôts*"); Cour des comptes RSPFP June 2026, footnote 19 ("*Les prélèvements obligatoires mesurés par Eurostat se distinguent de ceux mesurés par l'INSEE ... car les crédits d'impôt n'en sont pas déduits*"); OECD *Revenue Statistics 2025*, ch. 1 "Non-wastable tax credits" and ch. 3 Box 3.1.

### 1.2 Insee's own bridge (table 3.217, May 2026 accounts, EUR bn)

| Line | 2017 | 2024 | 2025 |
|---|---|---|---|
| (I) Total taxes and social contributions (incl. imputed, gross of tax credits) | 1,116.2 | 1,329.5 | 1,383.6 |
| (II) Amounts unlikely to be collected | -5.6 | -4.6 | -6.7 |
| (III) Imputed social contributions | -43.3 | -51.2 | -52.4 |
| (IV) Tax credits | -29.2 | **-19.6** | -19.4 |
| of which offset against tax due | -14.6 | -10.9 | -11.1 |
| of which paid out beyond tax due | -14.6 | -8.8 | -8.3 |
| **PO = (I)+(II)+(III)+(IV)** | 1,038.1 | **1,254.0** | **1,305.1** |
| PO, % of GDP | 45.30 | **42.72** | **43.63** |
| of which EU taxes | 4.0 | 2.6 | 2.9 |

Source: Insee, *Comptes nationaux annuels, base 2020*, table 3.217 "*Principaux impôts par catégorie*", https://www.insee.fr/fr/statistiques/fichier/8988845/t_3217_fr.xlsx (page https://www.insee.fr/fr/statistiques/8988845, May 2026). Cross-check: the Cour des comptes (RSPFP, 25 Jun 2026, Table 1) gives PO EUR 1,254.0 bn (42.7%) for 2024 and EUR 1,305.1 bn (43.6%) for 2025, the same values.

The tax-credit line also explains the Cour's "spending excluding tax credits" concept. The Cour's 2024 TE excluding tax credits (EUR 1,652.8 bn) equals Insee TE (EUR 1,672.6 bn) minus tax credits recorded as spending (EUR 19.8 bn, Insee table 3.201, line (c)) to the decimal. The expenditure-side amount (19.8) and the revenue-side amount (19.6) differ slightly because of recording-date lags, as Insee's note to table 3.201 explains.

### 1.3 Item-by-item bridge, 2024 (our computation, `data/18_po_vs_oecd_bridge_2024.csv`)

| Step | EUR bn | % of GDP | Note |
|---|---|---|---|
| Insee PO | 1,254.0 | **42.72** | current GDP 2,935.2 |
| + refundable tax credits | +19.6 | +0.67 | of which 0.37 offset against tax, 0.30 paid out |
| = ESA taxes + actual contributions - D.995 (current vintage) | 1,273.6 | 43.39 | equals (I)+(II)+(III) |
| - voluntary contributions (D.613V) | -1.0 | -0.03 | Eurostat value 1,010 m |
| = compulsory measure, May-2026 vintage | 1,272.6 | 43.36 | |
| - numerator revision (Eurostat stored figure is an earlier vintage) | -3.4 | -0.12 | Eurostat 1,269.2 vs 1,272.6 |
| = Eurostat compulsory measure at current GDP | 1,269.2 | 43.24 | |
| + GDP vintage (2,919.9 instead of 2,935.2) | | +0.23 | |
| = **Eurostat / OECD published** | 1,269.2 | **43.47 → 43.5** | |

*Total gap 0.745 pp = 0.67 (tax credits) - 0.03 (voluntary contributions) + 0.11 (vintage).* The bridge is exact to rounding. The OECD euro amount is EUR 1,269.05 bn (OECD SDMX `DF_RSOECD`, FRA, S13, total, national currency, re-queried 2026-10-25; corrected 2026-10-25: was "USD 1,373.6 bn × 0.924 EUR/USD = EUR 1,269.2 bn", a rounding artifact of the USD conversion). The OECD ratio is 43.46%, which implies a GDP of EUR 2,919.9 bn. Eurostat stores EUR 1,269.234 bn (S13_S212, compulsory, after D.995) and a ratio of 43.5%.

**Consequence for the 2025 figure.** On the same ESA/Eurostat concept, 2025 = (1,305.1 + 19.4) / 2,991.1 = **44.28%** (our computation). **Correction 2026-10-25 (was "≈ 44.3%"):** that formula omits the voluntary-contribution step (-0.03 pp) that the 2024 bridge itself applies; with D.613V of about EUR 1.0-1.05 bn (2023: 0.95; 2024: 1.01; 2025 not yet published) the strict Eurostat compulsory concept is about **44.25%, i.e., 44.2-44.3%** depending on rounding and on the vintage Eurostat will use. The 44.28% figure (ESA taxes + actual contributions incl. voluntary, net of D.995) matches the Cour's "44.3 points of GDP as measured by Eurostat, now the highest in the euro area" (RSPFP June 2026, p. 32, fn 19; corrected 2026-10-25: was "p. 34"). Eurostat's `gov_10a_taxag` had no 2025 data on 21 Oct 2026; OECD 2025 data are due with *Revenue Statistics 2026* (Dec 2026).

### 1.4 Divergence: the OECD's "split basis" for France

The OECD says it subtracts only the "tax-expenditure component" (the part offset against tax) of non-wastable credits. On that basis France's figure should be about EUR 10-11 bn **below** ESA gross. Yet:

- In 2023, OECD "split basis" = EUR 1,239.6 bn (43.9%), and Eurostat's ESA gross compulsory figure = EUR 1,239.7 bn. They are the same.
- In 2024, OECD = 1,269.05 and Eurostat = 1,269.23. Equal to within EUR 0.2 bn (corrected 2026-10-25: was "1,269.2 and 1,269.2"; OECD value re-queried from the OECD SDMX API).
- The OECD's Table 1.6 shows France 2023 at **43.5% (net), 43.9% (split, published), 44.2% (gross)**: credits 19.4 bn = transfer component 9.2 + tax-expenditure component 10.2.

The French figure reported to the OECD therefore appears to be the ESA figure, and the OECD's "gross" variant (1,249.7) adds the offset component a second time. We found no OECD or Insee note that explains this. ⚠ open question, to put to the OECD Centre for Tax Policy (Revenue Statistics team) or to Insee. **Practical effect:** the OECD "net basis" for France (43.5% in 2023, 1,230.3 bn) is still about 0.3 pp above Insee PO 2023 (43.15%), because it removes only the paid-out part of the credits.

### 1.5 International comparison (2024)

**Eurostat, taxes + compulsory social contributions (excl. imputed), % of GDP, 2024** (`gov_10a_taxag`, updated 21 Oct 2026; our ranks and statistics, `raw/18/taxag_all.json`):

| Measure | France | Rank EU-27 | EU-27 mean / median | EA21 rank | EA21 mean / median | Panel DE IT ES NL BE SE DK: mean / median | EU-27 agg. / EA21 agg. |
|---|---|---|---|---|---|---|---|
| Published ratio | **43.5** | **2nd** (DK 44.9) | 36.9 / 36.7 | **1st** | 37.0 / 37.8 | 40.8 / 40.8 | 39.2 / 39.5 |
| Same, at current GDP (our computation) | 43.2 | 2nd (DK 44.0) | 36.8 / 36.7 | 1st | 36.9 / 37.8 | 40.7 / 40.8 | n.a. |
| Variant incl. imputed contributions | 45.3 | 2nd (DK 45.5) | 37.7 / 37.6 | 1st | 37.8 / 38.0 | 41.8 / 41.8 | 40.2 / 40.6 |

Panel values (published, compulsory excl. imputed): DE 39.6, IT 42.1, ES 36.7, NL 38.8, BE 42.8, SE 40.8, DK 44.9 (also AT 42.9, FI 42.2).

**OECD total tax revenue, % of GDP, 2024p** (*Revenue Statistics 2025*, Table 3.1): **France 43.5, 2nd of 36** behind Denmark 45.2. Austria 43.4, Italy 42.8, Belgium 42.6, Finland 42.2, Sweden 41.4, Netherlands 38.5, Germany 38.0, Spain 36.7; OECD average 34.1. *(Matches file 00 row 30.)*

**On a net-of-credits basis (OECD Table 1.6, 2023):** France 43.5% (net) vs Denmark 44.0, Italy 41.3, Belgium 41.8, Germany 36.8, Spain 36.3. Other countries' net and published ratios differ by 0.0-0.5 pp, so **France's rank does not depend on the tax-credit treatment.** ~~Insee PO 2024 (42.7%) would still rank 2nd in the EU on the 2024 Eurostat list.~~ **Corrected 2026-10-25:** Insee PO 2024 (42.7%) placed on the 2024 Eurostat list would rank **4th in the EU** (behind DK 44.9, AT 42.9, BE 42.8) and **3rd in the euro area**, not 2nd. Like-for-like (ESA/OECD measure) France is 2nd in the EU and 1st in the euro area. This is one more reason never to mix the two measures.

### 1.6 Economists' and institutions' positions

- **Insee and the government (PLF, RESF):** the PO-net-of-credits ratio is the domestic yardstick. Tax credits are economically tax cuts, and the ESA convention of recording them as spending inflates both revenue and spending by about 0.7 pp.
- **Cour des comptes:** uses PO net of credits for France, but cites Eurostat's gross measure (44.3%) for euro-area rankings, with an explicit footnote. It also nets credits from spending ("TE excluding tax credits", 56.6% of GDP in 2025 vs 57.3% gross).
- **OECD:** recommends the "split" treatment as a compromise between net and gross. Its own table shows that the choice moves France by -0.4 pp (net) to +0.3 pp (gross) around the published 43.9% for 2023 (corrected 2026-10-25: was "±0.4 pp").
- **Comparability caveat (not a France-specific bridge item):** the OECD and Eurostat measures include only *government* levies. Countries whose mandatory occupational pensions or health insurance sit outside government look lighter: Dutch basic health insurance (classified as compulsory private insurance), Danish and Swedish occupational pensions. France's complementary pensions (Agirc-Arrco) and health insurance are inside government. The OECD publishes "non-tax compulsory payments" as a memorandum for this reason. ⚠ We did not download those memorandum values in this pass (web-search budget exhausted). File 01's PPS-per-capita caveat applies too.

**Recommendation (a):**
- Domestic narrative: "*Prélèvements obligatoires*: 42.7% of GDP in 2024, 43.6% in 2025 (Insee, net of tax credits)."
- International chart: "Tax and social contributions, ESA/OECD definition: 43.5% in 2024, 2nd in the EU after Denmark and 1st in the euro area; about 44.2-44.3% in 2025 (Cour des comptes: 44.3%)." (corrected 2026-10-25: was "about 44.3%")
- Always add the footnote: "The international measure counts EUR 19-20 bn of refundable tax credits as public spending rather than as reduced taxes (+0.7 point). It also uses an earlier GDP estimate."
- **Never place 42.7 next to other countries' OECD ratios.**

---

## 2. Bridge (b): interest burden 2025 – EUR 64.7 vs 65.7 bn vs the budget debt charge

### 2.1 The three numbers

| Concept | 2023 | 2024 | 2025 | 2026 | 2027 | Scope / basis | Source |
|---|---|---|---|---|---|---|---|
| **ESA D.41 interest payable, general government (consolidated)** | 53.4 | 60.1 | **65.7** (2.2% GDP; 3.83% of TE) | 79.2 (f) | ~91 (f, 2.9% GDP) | S.13, accrual, FISIM-corrected | Insee t_3201; Eurostat `gov_10a_main` / `gov_10dd_edpt1` (65,720.9-65,721.0 m); Cour RSPFP 2026; HCFP Avis 2026-5 §115 |
| **Insee "interest excluding FISIM correction" (D41G)** | 51.0 | 58.1 | **64.7** | | | Same scope; FISIM put back into interest | Insee IP 2106 Fig. 4, footnote 2; Insee t_3201 |
| ESA D.41, **State only** (S.13111) | 40.4 | 45.8 | 52.5 | | | State, accrual | Insee t_3203; Cour RSPFP 2026 fn 23 ("52,5 Md") |
| **State budget debt charge** (*charge de la dette*, programme 117 + SNCF Réseau debt) | | | **51.6** (executed) | 59.3 (LFI) → **63.4** (revised) | **72.9** (PLF) | State, budget accounting (LOLF) | PLF 2027, *exposé général*, State balance table |

### 2.2 FISIM: why 64.7 < 65.7

- In ESA, the interest a borrower pays a bank is split. "Pure" interest at a reference rate is recorded as D.41. The margin (FISIM) is recorded as purchase of a service (intermediate consumption P.2).
- Insee's *Insee Première* moves FISIM back into interest: "*Les dépenses de Sifim des APU sont ici incluses dans les intérêts versés et non dans la consommation intermédiaire comme dans le cadre central*" (IP 2106, methodology box). The resulting figure is closer to the interest actually paid under the loan contracts.
- When the contractual rate on a loan is **below** the reference rate, FISIM is negative. ESA D.41 is then *higher* than the contractual interest. That has been the case since 2023: euro-area reference rates jumped while the stock of local-government fixed-rate bank loans carries old, low rates.

| Year | ESA D.41 | Excl. FISIM correction | Correction (D.41 - D41G) | of which local government (APUL) | of which State |
|---|---|---|---|---|---|
| 2019 | 36.9 | 39.7 | -2.9 | -2.3 | -0.03 |
| 2022 | 50.9 | 52.8 | -1.8 | -1.5 | -0.01 |
| 2023 | 53.4 | 51.0 | +2.4 | +1.7 | +0.1 |
| 2024 | 60.1 | 58.1 | +2.0 | +1.5 | +0.1 |
| 2025 | **65.7** | **64.7** | **+1.07** | **+0.74** | +0.09 |

Source: Insee tables 3.201, 3.203, 3.205 (May 2026), https://www.insee.fr/fr/statistiques/8988845; our computation, `data/18_interest_bridge.csv`. The remaining roughly EUR 0.25 bn of the 2025 correction is split between central-government bodies (ODAC, 0.09) and social security (by difference). **This item-by-item bridge was flagged "not published" in file 00 log #2. It is published by Insee in its detailed tables, and is now documented here.**

The EDP definition of interest (which adds swap and FRA flows) gives the same 65.7 bn for France: Eurostat `gov_10dd_edpt1` reports D41PAY = 65,721 m for 2025, identical to `gov_10a_main`.

Net interest (payable minus receivable, ESA): 65.7 - 3.5 = **EUR 62.2 bn (2.08% of GDP)** in 2025 (Insee t_3201, interest receivable 3.47 bn).

### 2.3 From general-government ESA interest to the State's budget debt charge (2025)

| Bridge item | Direction | Size | Comment |
|---|---|---|---|
| General government D.41 | | 65.7 | |
| - other subsectors (social security incl. CADES/ACOSS, local government, ODAC) net of consolidation | ↓ | -13.2 | 65.7 - 52.5 (State D.41) |
| = State D.41 (ESA, accrual) | | 52.5 | Insee t_3203: 52.514 |
| Accrual (NA) vs budget timing: issue discounts and premiums amortized over the bond's life in NA, but treated as cash/treasury items in the budget; coupon accrual vs payment date | ↕ | | In the 2027 financing table, net "*primes nettes de décotes*" are -8.0 bn of treasury resources (PLF 2027, art. d'équilibre) |
| Inflation indexation of OATi/OAT€i principal: in NA, accrued continuously as interest (HCFP fn 30); in the budget, an annual *provision pour charge d'indexation* (8.5 bn planned for 2027, neutralized in the financing table because it is not cash) | ↕ | | both include indexation, with different timing |
| Treasury items, interest on deposits of *correspondants du Trésor*, swaps | ↕ | | |
| = **State budget debt charge executed (incl. SNCF Réseau)** | | **51.6** | 0.9 bn below State D.41 in 2025 |

⚠ The State-level split of the 0.9 bn (discounts vs indexation vs treasury items) is in the Cour des comptes' *note d'analyse de l'exécution budgétaire* for the "*Engagements financiers de l'État*" mission. We did not open it (web-search budget exhausted). **Inflation sensitivity (government figure, cited by HCFP §115):** +1 point of inflation ≈ +EUR 3 bn of interest the same year, through the indexed bonds.

### 2.4 International comparison (ESA D.41, % of GDP)

Eurostat `gov_10a_main` (21 Oct 2026); our ranks and statistics.

| | 2024 | 2025 |
|---|---|---|
| France | 2.0 | **2.2** |
| Rank EU-27 | 9th | **8th** (behind IT 3.8, HU 3.8, EL 3.1, RO 2.8, PL 2.5, ES 2.4, BE 2.3) |
| Rank EA21 | 6th | **5th** |
| EU-27 mean / median | 1.61 / 1.3 | 1.6 / 1.3 |
| EA21 mean / median | 1.49 / 1.3 | 1.5 / 1.3 |
| EU-27 / EA21 aggregate | 1.9 / 1.9 | 1.9 / 1.9 |
| Panel (DE IT ES NL BE SE DK) mean / median | 1.67 / 1.0 | 1.67 / 1.1 |
| Panel values 2025 | | DE 1.1, IT 3.8, ES 2.4, NL 0.7, BE 2.3, SE 0.6, DK 0.8 |
| Interest as % of TE, France | 3.59 (9th) | **3.83 (9th of 27)**; EU-27 agg. 3.82, EU mean 3.41, median 2.9 |

France's interest burden is **not exceptional in Europe** (around the EU aggregate as a share of spending). It is rising quickly (+EUR 25 bn over 2025-2027 per the HCFP). ⚠ unverified (2026-10-25): the earlier wording "rising fastest among large countries" has no cited source; Eurostat 2024→2025 shows FR +0.2 pp vs DE +0.1, ES 0.0, IT -0.1, which is consistent but covers one year only. **Recommendation:** check against the European Commission Autumn 2026 forecast (AMECO, interest % of GDP, 2025-2027) before using the comparative claim, and the government forecast puts it at 2.9% of GDP in 2027.

### 2.5 Debates

- **Gross vs net interest, nominal vs real.** Part of D.41 (the indexation of OATi principal) compensates for inflation, so some economists prefer a "real" interest burden or the r - g differential (see file 10 §7 and file 06). The HCFP and the Cour use nominal ESA interest, which is the figure that enters the Maastricht deficit.
- **Budget vs national accounts.** Political debate often quotes the State budget charge (e.g., "*la charge de la dette devient le premier poste de dépense de l'État*"), which excludes social security and local governments. That is legitimate for the State budget, but it **understates the general-government burden by EUR 14 bn in 2025** and by about **EUR 16-18 bn in 2026-2027**. The gap in 2026-2027 is wider (our computation from the figures in §2.1; the 2026-2027 gap mixes forecast vintages). ⚠ unverified (2026-10-25): the earlier explanation "because indexation accrues faster in NA when inflation rises" is a hypothesis with no source; the widening may equally come from social-security (CADES/ACOSS) and local-government interest. **Recommendation:** check the subsector split in the *Rapport économique, social et financier* 2027 or ask the DG Trésor before giving a cause.

**Recommendation (b):**
- Website headline: **"Interest on public debt (all general government, national accounts): EUR 65.7 bn in 2025, 2.2% of GDP, 3.8% of public spending; EUR 79.2 bn forecast for 2026."**
- Wherever EUR 64.7 bn is quoted, label it "Insee, excluding FISIM correction". Better, do not use it.
- Use "State budget debt charge: EUR 51.6 bn (2025), 63.4 bn (2026 revised), 72.9 bn (PLF 2027)" only on pages about the State budget, with the label.

---

## 3. Bridge (c): COFOG health vs SHA (System of Health Accounts) public health spending

### 3.1 Levels, France 2024

| Measure | EUR bn | % of GDP | Source |
|---|---|---|---|
| COFOG GF07 health, total general-government expenditure | **261.2** | **8.90** | Eurostat `gov_10a_exp` (21 Oct 2026) |
| of which gross capital formation (P.5) | 9.9 | 0.34 | same |
| of which capital transfers (D.9) | 2.6 | 0.09 | same |
| of which R&D (GF0705), total | 6.7 | 0.23 | same (3.4 bn of it is capitalized R&D, inside P.5) |
| SHA HF.1 government + compulsory schemes | **276.9** | **9.44** | Eurostat `hlth_sha11_hf` (23 Oct 2026) |
| of which HF.11 government schemes | 11.7 | 0.40 | same |
| of which HF.121 social health insurance | 243.1 | 8.28 | same |
| of which HF.122 compulsory private insurance (ANI collective contracts) | 22.2 | 0.76 | same |
| SHA current health expenditure (CHE), all financing | 332.4 | 11.33 | same |
| Memo: SHA long-term care (social), HCR.1, financed by HF.1 (outside CHE) | 16.0 | 0.54 | `hlth_sha11_hchf` |

### 3.2 Bridge (our computation, EUR bn, 2024)

| Step | EUR bn | % of GDP |
|---|---|---|
| COFOG GF07 | 261.2 | 8.90 |
| - capital (P.5 + D.9) | -12.6 | -0.43 |
| - current R&D (GF0705 excl. capital) | -3.3 | -0.11 |
| = COFOG current health excl. R&D | 245.2 | 8.36 |
| + **residual classification items** (unquantified line by line): health part of long-term care and insurance administration classified by Insee in COFOG GF10 (social protection) but in SHA HC.3/HC.7; *less* the part of public-hospital output paid by households and complementary insurers (in COFOG gross, in SHA HF.2/HF.3) | +9.5 | +0.32 |
| = SHA HF.11 + HF.121 ("strictly public") | 254.8 | 8.68 |
| + HF.122 compulsory private insurance | +22.2 | +0.76 |
| = SHA HF.1 | 276.9 | 9.44 |

⚠ The +9.5 bn residual is not decomposed. The Drees *Comptes de la santé* methodology annex (blocked by the Drees firewall in earlier passes; see README §9.1 item 4) is the source that could split it.

### 3.3 International comparison, 2024 (% of current GDP, our computation, `data/18_cofog_vs_sha_health_2024.csv`)

| Measure | France | Rank EU-27 | EU-27 mean / median | EA21 aggregate | FR gap vs EA21 | Panel mean / median (DE IT ES NL BE SE DK) |
|---|---|---|---|---|---|---|
| COFOG GF07 total | 8.90 | 3rd (AT 9.36, CZ 9.02) | 6.77 / 6.61 | 7.43 | **+1.47** | 7.34 / 7.35 |
| COFOG GF07 excl. P.5 and D.9 | 8.47 | 3rd | 6.44 / 6.35 | 7.15 | +1.31 (corrected 2026-10-25: was +1.32) | 7.05 / 7.19 |
| SHA HF.1 | 9.44 | 3rd (DE 10.35, SE 9.60) | 6.75 (corrected 2026-10-25: was 6.76) / 6.21 | 8.33 | +1.10 (file 12: +1.06 on published ratios) | 8.17 / 8.13 |
| SHA HF.11 + HF.121 | 8.68 | 4th (SE, DE, AT) | 6.50 / 6.20 | 7.58 | +1.10 | 7.31 / 7.78 (NL only 3.29: its basic insurance is HF.122) |
| SHA CHE (all financing) | 11.33 | 3rd | 8.81 / 8.50 | 10.39 | +0.93 (corrected 2026-10-25: was +0.94) (file 12: +0.88 published) | 10.21 / 10.16 |

Why the COFOG gap is larger than the SHA gap:
- France's COFOG health includes relatively more capital spending (public hospitals are inside general government in France).
- Germany (HF.122 0.86 pp) and the Netherlands (5.14 pp) carry much of their compulsory health financing outside government, so it is invisible in COFOG.
- On the SHA HF.1 basis, Germany and Sweden spend more than France.

**Recommendation (c):**
- For the "where does public money go" pages (COFOG breakdown consistent with TE = 57.0% of GDP in 2024), use **COFOG health 8.9% of GDP, EUR 261 bn, 15.6% of TE** (file 00 row 13).
- For health-system pages, use **SHA**: CHE 11.3% of GDP; public + compulsory 9.4%; France 3rd in the EU behind Germany and Sweden.
- Standard sentence: "*Health explains 1 to 1.5 points of GDP of France's spending gap with the euro area, depending on the definition (SHA or COFOG).*" This keeps file 12's wording.

---

## 4. Summary of divergences still open

| # | Divergence | Status |
|---|---|---|
| 1 | OECD's France figure is labeled "split basis" but equals ESA gross (2023 and 2024) | ⚠ open; ask the OECD/Insee. It does not change France's rank. |
| 2 | Eurostat `gov_10a_taxag` EUR values for France 2024 are an earlier vintage than Insee's May-2026 accounts (numerator -3.4 bn) and its % of GDP uses the old GDP | Documented. Same issue as COFOG TE 57.3 vs 57.0 (file 00 log #6). |
| 3 | State D.41 (52.5) vs budget charge (51.6) in 2025: the split into discounts/indexation/treasury items is unquantified | ⚠ needs the Cour NEB "*Engagements financiers de l'État*" 2025 |
| 4 | COFOG vs SHA residual of +9.5 bn (LTC, administration, hospital sales) | ⚠ needs the Drees methodology annex |
| 5 | International comparability of the tax ratio when mandatory private schemes are outside government (NL, DK, SE) | ⚠ OECD non-tax compulsory payments memo not downloaded |

---

## 5. Sources

1. Insee, *Comptes nationaux annuels, base 2020 – Dépenses et recettes des administrations publiques en 2025*, tables 3.201-3.206, 3.216, 3.217 (May 2026). https://www.insee.fr/fr/statistiques/8988845 ; table 3.217: https://www.insee.fr/fr/statistiques/fichier/8988845/t_3217_fr.xlsx ; table 3.201: https://www.insee.fr/fr/statistiques/fichier/8988845/t_3201_fr.xlsx
2. Insee, same tables for the 2024 accounts (May 2025; definitions of PO and tax credits). https://www.insee.fr/fr/statistiques/8574705?sommaire=8574832
3. Insee, *Insee Première* no. 2106, "*Le compte des administrations publiques en 2025*" (29 May 2026), Fig. 1, Fig. 4 footnote 2 and methodology box on FISIM. https://www.insee.fr/fr/statistiques/8997691
4. Insee, PO rate series 1959-2025 ("*hors cotisations sociales imputées et crédit d'impôts*"). https://www.insee.fr/fr/statistiques/2381412 (xlsx: https://www.insee.fr/fr/statistiques/fichier/2381412/econ-fin-pub-prelev-oblig.xlsx)
5. Insee, *Prélèvements obligatoires – Les comptes de la Nation en 2020* (definition: "*Les crédits d'impôts sont comptabilisés en moindres prélèvements obligatoires dans leur totalité*"). https://www.insee.fr/fr/statistiques/5412401?sommaire=5354786
6. Eurostat, `gov_10a_taxag` (Main national accounts tax aggregates, updated 21 Oct 2026). https://ec.europa.eu/eurostat/databrowser/view/gov_10a_taxag/default/table
7. Eurostat, `gov_10a_main` and `gov_10dd_edpt1` (21 Oct 2026). https://ec.europa.eu/eurostat/databrowser/view/gov_10a_main/default/table ; https://ec.europa.eu/eurostat/databrowser/view/gov_10dd_edpt1/default/table
8. Eurostat, `gov_10a_exp` (COFOG, 21 Oct 2026). https://ec.europa.eu/eurostat/databrowser/view/gov_10a_exp/default/table
9. Eurostat, `hlth_sha11_hf`, `hlth_sha11_hchf` (23 Oct 2026). https://ec.europa.eu/eurostat/databrowser/view/hlth_sha11_hf/default/table
10. Eurostat, `nama_10_gdp` (22 Oct 2026). https://ec.europa.eu/eurostat/databrowser/view/nama_10_gdp/default/table
11. OECD, *Revenue Statistics 2025* (Dec 2025), ch. 3 Tables 3.1, 3.2, 3.5, 3.19, 3.20 and Box 3.1. https://www.oecd.org/en/publications/revenue-statistics-2025_3a264267-en/full-report/tax-levels-and-tax-structures-1965-2024_2033f3ea.html (read in a browser; plain HTTP returns 403)
12. OECD, *Revenue Statistics 2025*, ch. 1 "Non-wastable tax credits", Table 1.6. https://www.oecd.org/en/publications/revenue-statistics-2025_3a264267-en/full-report/tax-revenue-trends-1965-2024_98c75833.html
13. Cour des comptes, *La situation et les perspectives des finances publiques* (25 Jun 2026), pp. 26-36 and fn 19, 23. https://www.ccomptes.fr/sites/default/files/2026-07/20260625_RSPFP-2026.pdf
14. Haut Conseil des finances publiques, *Avis no. 2026-5* on PLF/PLFSS 2027, §114-115 and fn 30. https://www.hcfp.fr/sites/default/files/2026-10/Avis%20HCFP%202026-5%20-%20PLF-PLFSS%202027.pdf
15. PLF 2027, *projet de loi* (State balance table and article d'équilibre, financing table). Local copy `data/raw/06/plf2027/plf2027_budget.pdf`; https://www.budget.gouv.fr/documentation/file-download/33478 (URL as recorded in file 06)

---

## 6. Verification log (re-check of headline figures against primary sources, 2026-10-25)

| # | Headline figure | Re-checked against | Result |
|---|---|---|---|
| 1 | PO 2024 = 42.7% / EUR 1,254.0 bn | Insee t_3217 (42.7231; 1,254.024) and Insee PO series xlsx (42.7231); Cour RSPFP Table 1 (1,254.0; 42.7) | ✅ confirmed |
| 2 | PO 2025 = 43.6% / EUR 1,305.1 bn | Insee t_3217 (43.632; 1,305.067); IP 2106 Fig. 1 (43.6) | ✅ |
| 3 | Refundable tax credits 2024 = EUR 19.6 bn (10.9 + 8.8) | Insee t_3217 lines (IV); t_3201 line (c') = 19.624 | ✅ |
| 4 | OECD 2024 = 43.5%, 2nd of 36, DK 45.2, OECD avg 34.1 | OECD RS 2025 Table 3.1, read in a browser | ✅ |
| 5 | OECD France 2024 euro amount = 1,269.2 bn; GDP 2,919.9 | OECD Tables 3.2 (USD 1,373.6 bn), 3.20 (0.924), 3.19 (2,919.9) | ✅ (computed) |
| 6 | Eurostat compulsory 2024 = 1,269.234 bn, 43.5%; incl. imputed 45.3% | `gov_10a_taxag` API, S13_S212 | ✅ |
| 7 | EU taxes 2024 = 2.6 bn in both | Insee t_3217 "*dont impôts de l'UE*" 2.6; Eurostat S212 = 2,600 m | ✅ |
| 8 | 2025 ESA-concept ratio 44.3% | Computed (1,324.5 / 2,991.1 = 44.28); Cour RSPFP p. 34 "44,3" | ✅ |
| 9 | Interest 2025 ESA = 65.7 bn; excl. FISIM = 64.7 bn | Insee t_3201 (65.721 / 64.652); Eurostat `gov_10a_main` 65,720.9 m and `gov_10dd_edpt1` 65,721 m; IP 2106 Fig. 4 (64.7, fn 2) | ✅ |
| 10 | State D.41 2025 = 52.5 bn | Insee t_3203 (52.514); Cour fn 23 | ✅ |
| 11 | State budget debt charge 2025 = 51.6; 2026 = 63.4 (revised); 2027 = 72.9 | PLF 2027 State balance table (local text, lines 760-769) | ✅ |
| 12 | Interest rank 2025: 8th EU-27, 5th EA21; 3.83% of TE | `gov_10a_main` 2025 (D41PAY, TE) | ✅ (computed) |
| 13 | COFOG health 2024 = 261.2 bn, 8.90% | `gov_10a_exp` GF07 TE 261,156.3 m / GDP 2,935.2 bn | ✅ (matches file 00 row 13) |
| 14 | SHA HF.1 2024 = 276.9 bn, 9.44%; HF.122 = 22.2 bn, 0.76% | `hlth_sha11_hf` (276,949.1 m; PC_GDP 9.44; 22,175.6 m; 0.76) | ✅ (matches file 12) |
| 15 | COFOG gap vs EA21 +1.47 pp | `gov_10a_exp` EA21 aggregate / EA21 GDP | ✅ (matches file 00 row 9) |
| 16 | SHA HF.1 gap vs EA21 | Recomputed at current GDP: +1.10; file 12 (published ratios): +1.06 | ⚠ 0.04 pp difference from the denominator. Use +1.06 (file 12, published) on the site. |
| 17 | OECD France 2023 split/net/gross 43.9/43.5/44.2 | OECD RS 2025 Table 1.6, read in a browser | ✅, but see the open divergence in §1.4 |
| 18 | Cour TE excl. tax credits 2024 = 1,652.8 | Insee TE 1,672.589 - credits recorded as spending 19.771 = 1,652.818 | ✅ |

*Limitations:* the web-search budget for this session ran out midway. Items flagged ⚠ in §4 were not pursued through search; primary documents already on disk or reached by direct URL were used instead. No figure in this file relies on memory.

---

## 7. Adversarial verification log (2026-10-25, second pass)

*Method: every headline figure re-derived from the primary source, not from the first-pass log in §6. Live re-queries on 2026-10-25: Eurostat API (`gov_10a_taxag`, `gov_10a_main`, `gov_10a_exp`, `hlth_sha11_hf`, `nama_10_gdp`); OECD SDMX API `OECD.CTP.TPS,DSD_REV_COMP_OECD@DF_RSOECD` (https://sdmx.oecd.org/public/rest/data/OECD.CTP.TPS,DSD_REV_COMP_OECD@DF_RSOECD,/FRA..S13._T._T..A); OECD* Revenue Statistics 2025 *ch. 1 and ch. 3 read in a browser (Table 1.6, Box 3.1). Local primary copies: Insee xlsx t_3201-3205, 3217 (`data/raw/18/`); Cour RSPFP June 2026 (`data/raw/08_verify/pdf/cdc_rspfp2026.pdf`); HCFP Avis 2026-5 (`data/raw/hcfp/avis2026-5.pdf`); PLF 2027 (`data/raw/06/plf2027/`); Insee IP 2106 (`data/raw/insee/ip2106.pdf`).*

| # | Claim | Result | Evidence |
|---|---|---|---|
| A1 | PO 2024 42.72% / 1,254.0; 2025 43.63% / 1,305.1; tax credits 19.624 (10.868 + 8.756); (I) 1,329.5; D.995 -4.6; D.612 -51.2; EU taxes 2.6 | ✅ confirmed | Insee t_3217 |
| A2 | Eurostat compulsory 2024 = 1,269,234 m, 43.5%; incl. imputed 45.3%; D.613V 1,010 m | ✅ | `gov_10a_taxag` live |
| A3 | OECD France 2024 = 43.5%, 2nd of 36 (DK 45.18; JPN missing), AT 43.4, IT 42.8, BE 42.6, FI 42.2, SE 41.4, NL 38.5, DE 38.0, ES 36.7, OECD avg 34.06 | ✅ | OECD SDMX API |
| A4 | OECD France 2024 euro amount 1,269.2 bn | ❌ **corrected**: 1,269.05 bn (national currency series); "OECD = Eurostat" holds within 0.2 bn | OECD SDMX API (XDC 1,269.053; USD 1,373.598) |
| A5 | OECD Table 1.6 France 2023: 19.4 = 9.2 + 10.2; 1,230.3 / 1,239.6 / 1,249.7; 43.5 / 43.9 / 44.2; DK 44.0, IT 41.3, BE 41.8, DE 36.8, ES 36.3 | ✅ | OECD RS 2025 ch. 1 (browser) |
| A6 | "Choice moves France by ±0.4 pp" | ❌ **corrected**: -0.4 / +0.3 pp | same |
| A7 | Box 3.1: France's uncollectible-tax capital transfers allocated pro rata across tax headings | ✅ | OECD RS 2025 ch. 3 (browser) |
| A8 | Ranks 2024 Eurostat: FR 2nd EU (DK 44.9), 1st EA21; means/medians, aggregates, panel; current-GDP row (DK 44.04, FR 43.24) | ✅ | recomputed from live API |
| A9 | "Insee PO 2024 (42.7%) would still rank 2nd in the EU" | ❌ **corrected**: 4th in the EU (AT 42.9, BE 42.8 above), 3rd in the EA | `gov_10a_taxag` live |
| A10 | 2025 ESA-concept ratio "≈ 44.3%" | ⚠ **corrected to 44.2-44.3%**: 44.28% includes voluntary contributions; strict compulsory concept ≈ 44.25%. Cour's 44.3% confirmed verbatim, but on **p. 32** (not p. 34). **Recommendation:** cite "44.3% (Cour des comptes)" until Eurostat publishes 2025 in `gov_10a_taxag`, then replace. | Insee t_3217; Cour RSPFP p. 32 fn 19 |
| A11 | Interest D.41 2025 65.721; excl. FISIM 64.652; 2024 60.131 / 58.147; 2023 53.410 / 51.046; FISIM subsector split (APUL 0.741, State 0.087, ODAC 0.087) | ✅ | Insee t_3201, t_3203, t_3204, t_3205; `gov_10a_main` 65,720.9; `gov_10dd_edpt1` 65,721 |
| A12 | 64.7 = Insee "*hors correction au titre des Sifim*" | ✅ | IP 2106 Fig. 4 note 2 and methodology box; text "+6,5 Md (+11,2 %)" |
| A13 | Interest received 2025 3.473; net interest 62.2 bn = 2.08% | ✅ | Insee t_3201 |
| A14 | 2.2% of GDP, 3.83% of TE (9th EU; EU-27 agg. 3.82, mean 3.41, median 2.9); 2024 3.59% (9th) | ✅ | `gov_10a_main` live, recomputed |
| A15 | Interest rank 2025: 8th EU (IT 3.8, HU 3.8, EL 3.1, RO 2.8, PL 2.5, ES 2.4, BE 2.3), 5th EA; 2024 9th/6th; panel 1.67 / 1.1 | ✅ | `gov_10a_main` live |
| A16 | State D.41 2025 52.5 (Cour fn 23 "52,5 Md€") | ✅ | Insee t_3203 52.514; Cour RSPFP p. 35 fn 23 |
| A17 | State budget debt charge 51.6 / 59.3 (LFI) / 63.4 (revised) / 72.9 (PLF 2027); primes nettes de décotes -8.0; indexation provision neutralized -8.5 | ✅ | PLF 2027 State balance and financing tables (local text) |
| A18 | HCFP: 79.2 bn 2026; 2.9% of GDP = 91 bn 2027; "+ de 25 Md" vs 2025; +1 pt inflation ≈ +3 bn; fn 30 continuous accrual of indexation | ✅ | HCFP Avis 2026-5 §115, fn 30 |
| A19 | "Rising fastest among large countries" | ⚠ unverified, reworded; see §2.4 recommendation | none cited |
| A20 | "Gap wider in 2026-2027 because indexation accrues faster in NA" | ⚠ unverified hypothesis, removed as a stated cause; see §2.5 | none cited |
| A21 | COFOG GF07 2024 261,156.3 m, 8.9%, 15.6% of TE; P.5 9,938; D.9 2,626; GF0705 6,708 (P.5 3,360) | ✅ | `gov_10a_exp` live |
| A22 | SHA HF.1 276,949 m (9.44%); HF.11 11,687; HF.121 243,087; HF.122 22,176 (0.76%); CHE 332,435 (11.33%); HCR.1 via HF.1 15,966 | ✅ | `hlth_sha11_hf` live; `hlth_sha11_hchf` raw |
| A23 | Health ranks (COFOG 3rd, HF.1 3rd, HF.11+121 4th, CHE 3rd) and panel stats | ✅ | recomputed from `data/18_cofog_vs_sha_health_2024.csv` |
| A24 | Health gaps vs EA21: COFOG excl. capital +1.32; CHE +0.94; HF.1 EU mean 6.76 | ❌ **corrected**: +1.31; +0.93; 6.75 (rounding) | same CSV |
| A25 | Published SHA HF.1 gap vs EA21 +1.06 (FR 9.44 - EA21 8.38) | ✅ | `hlth_sha11_hf` live |
| A26 | Cour TE excl. tax credits 1,652.8 (2024), 56.6% (2025) | ✅ | Cour RSPFP 2026 |

**Still open (not resolvable in this pass):** §4 items 1 (OECD "split" = ESA gross), 3 (State D.41 vs budget charge split), 4 (COFOG-SHA +9.5 bn residual), 5 (OECD non-tax compulsory payments memo). §1.6 attributions to "Insee and the government (PLF, RESF)" are paraphrases without a direct quote: ⚠ unverified; **recommendation:** add a verbatim citation (e.g., RESF 2027 PO annex) before quoting them on the site. **For file 00 / README §8:** any place that states "2025 ESA/OECD tax ratio 44.3%" as our computation should say 44.2-44.3% or cite the Cour; and "Cour RSPFP p. 34" for the 44.3% quote should read p. 32.
