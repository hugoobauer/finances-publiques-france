# Adversarial review of `platform/data` (2026-10-25)

## Scope and method

The review sampled well over 40 entries across the four datasets. Each entry was checked against `research/00-reference-figures.md` (file 00) or the topic file it cites. For each one, the review checked value, unit, base (% of GDP vs % of total spending), year, sign, ⚠ unverified items and French terminology.

| Dataset | Entries checked | How |
|---|---|---|
| `figures.json` | All 193 file 00 entries (rows 1-62) and 30 of the 52 topic-file entries | Each value, unit, base and year compared with its file 00 row. Topic-file values were grepped in their source file and checked in context (for example ONDAM, LPM, COFOG GF0102 and GF1007, Drees family and poverty benefits, HCFP interest shock, Bozio-Wasmer, HCSP, hours worked, IR households, top-10% share, COR living standard, civil-service share, file 16 lines, file 07 IPP values, OECD immigration scenarios). |
| `simulator-levers.json` | All 34 levers, all 17 multiplier classes, toggles, anti-double-counting rules, menu groups | Compared with file 20 §5.3-5.4, file 17 §8, file 07, file 11, file 03 and file 16. |
| `proposals.json` | 25 proposals in detail (Zucman, ISF, PFU, index point, retirement at 60 and 62, energy VAT, fuel freeze, SMIC x4, RN and LR immigration, EU cap, agencies, RN program 2027/2031, LR 400k, Renaissance endowment, Dutreil), plus the 14 proposers | Compared with files 00 (rows 44, 45, 52), 07 and 11. |
| `quiz.json` | All 35 questions and all 14 misperceptions | Compared with file 20 §6.2-6.3 and the cited figures. Formulas were recomputed. |

`python3 -I validate.py` returned PASS before and after the fixes. The fixes were followed by `--write-derived`, which recomputed the conversions of the edited proposal.

## Errors found and fixed

| # | File / entry | Error | Fix | Source |
|---|---|---|---|---|
| 1 | `proposals.json` / `energy_vat_rn` | The independent range was -17.4 to -11 bn (midpoint -14.2). The 17.4 bn comes from francebudget.fr. File 07 says this figure "should not be used as a reference": its base excludes fuels, so a larger number from a narrower base is internally inconsistent. File 11 also flags it as unreliable. The 17.4 also had a published conversion (3.7 days). | The range is now Montaigne's "> 11" only (central -11, read as a lower bound on the cost). The francebudget estimate is kept with a "not used as a reference" note. The 17.4 conversion was removed and the derived values were recomputed. | File 07 §3.4 (line 205); file 11 line 162 |
| 2 | `simulator-levers.json` / S9, option `energy_vat_5_5` | Same 17.4 figure (-17.4 to -11). | Option set to central -11 with a note: Montaigne lower bound; RN's own figure is -12.2; 17.4 is not used. The lever's envelope (-26.5 to 0, from the fuel option) is unchanged. | Same |
| 3 | `simulator-levers.json` / S10 (SMIC 1,600-1,700 net) | -3.5 to -4 bn was applied to the whole 1,600-1,700 range. File 11 rescales the 1,600 net target to about -1.8 to -2.2 bn because the SMIC rose in June 2026 (1,600 net is now +8.3%, not +14%). Only 1,700 net costs -3.5 to -4. The value is also our own scaling, but the entry was flagged `computed_by_us: false`. | Range set to -4 to -1.8 (no central), `computed_by_us: true`, with a note giving both ends. Source `f11:S1` added. | File 11 lines 144 and 221; file 07 §3.6 |
| 4 | `proposals.json` / `smic_1600_nfp` | Montaigne's -3.5 bn (2024) was shown with no warning that it is out of date against the SMIC in force since June 2026. | A caveat now says the current-SMIC cost is about 1.8-2.2 bn (file 11) and points to `smic_1600_ps`. Value unchanged: it is the historical 2024 costing. | File 11 line 221 |
| 5 | `simulator-levers.json` / S2 (label) | The label read "one-year freeze of base pensions, lowest pensions protected", but the 4.1 bn is the PLFSS 2027 measure: full indexation only up to EUR 1,260 a month and lower indexation above. That is a partial under-indexation, not a freeze. | `label_en`/`label_fr` now describe the PLFSS 2027 measure, with a note on the file 20 wording. Value unchanged. | File 03 line 151 and verification line 577 |
| 6 | `quiz.json` / Q20 | The answer text attributed 19.8% to "SIASP". File 04 sources it to DGAFP (RAEFP 2026, Insee employment estimates, including subsidized contracts). | Text now says "19.8%, DGAFP/Insee, civil service; 20.7%, OECD general-government definition" (EN and FR). | File 04 K7 |
| 7 | `quiz.json` / Q16 (French) | "paie un impôt sur le revenu net" can be read as "a tax on net income". | Now reads "paie effectivement l'impôt sur le revenu (impôt net positif)"; the explanation was aligned. | Terminology |
| 8 | `quiz.json` / Q24 (French) | "charge d'intérêts de l'État" and "budget de la programmation militaire" are not the official terms for the two budget-accounting aggregates being compared. | Now uses "charge de la dette de l'État" and "enveloppe de la loi de programmation militaire (LPM)" in the question, the options and the answer text. | File 00 row 41; file 06 #21 |
| 9 | `simulator-levers.json` / toggle `behavioral_responses` (French) | "Réactions des comportements" is not idiomatic. | "Réactions comportementales". | Terminology |
| 10 | `simulator-levers.json` / menu group `popular_targets` (French) | "Cibles populaires" reads as "working-class targets" in French. | "Cibles souvent citées". | Terminology |

## Checked and found correct (no change)

- **File 00 rows 1-62.** Every value, unit, base and year in `figures.json` matches its row. Shares of TE (rows 11-15, 32, 39, 54, 61) are labeled `pct_total_spending` and kept separate from the % of GDP entries. Ranges (rows 44, 45) are stored as ranges with `value: null` where file 00 gives no central value. Signs are correct: pension balance -5.1, primary balance -2.9 / -85.9, PO change -2.6, debt gap 2005 -2.0, immigration scenario C2 -0.85. No superseded value (file 00 §4) is used.
- **Statuses.** No ⚠ item was found in figures, levers or proposals. The unverified values that the research flags were checked and are absent: AFT 57.5%, index-point breakdown 2.07 bn, Gechert-Rannenberg, IMF WEO 0.9-1.7, Moneyvox 8.2 bn.
- **Multiplier classes.** All Y1 and Y3-5 defaults and bands match file 17 §8 and file 20 §5.3-5.4. The semi-elasticity is 0.57.
- **Quiz formulas.** The values were recomputed: Q08 32 days (29 Nov), Q11 0.4-4.3 days, Q12 7-16%, Q25 65%, Q27 0.78 per EUR 1,000, Q28 1.315 bn (EUR 19 per inhabitant), Q35 16.3 (band 11.2-21.5).

## Points for the editorial team (not changed in the data)

1. **File 20 needs the same corrections** (research files were not edited in this pass). In §3.4 and §5.3 S9, energy VAT is shown as "-11 to -17.4". In §5.3 S10, "-3.5 to -4" is given for 1,600-1,700. In §5.3 S2, the label says "one-year freeze". In §6.3 Q20, the source is given as "SIASP".
2. **S3 (index point, 2.1-2.4 bn per point).** 2.4 is the minister's office figure (press, labeled as such). File 07 lists "2.1" separately from the ⚠ 2.07 breakdown, and it matches 3.2 bn / 1.5 points (July 2023). The low end should still be traced to its own source before publication.
3. **`rn_back_to_62`.** The independent range uses file 00 row 44's "partial RN-type versions" (26-35 bn). File 11 also cites repeal alone at 16-17 bn by 2030-2032. The card should show both, so that readers do not assume 26-35 is the cost of the 2027 plan specifically.
4. **S5 (ONDAM)** has no default growth rate (file 20 does not set one). The front end needs one before launch.

# Data pass for the chapters (2026-10-25, second pass)

## Scope

This pass covered four items. (1) Every `[[fig-a-creer:...]]` placeholder and every "EN ATTENTE DE DONNÉES" block in `fr/site/chapitres` now has a data entry, and so do the missing figures listed in chapter 3 annex A. (2) The chip `[[yard:household_monthly_income_eur]]` now resolves. (3) The quiz bank is balanced and its draw rule is encoded. (4) `validate.py` now checks the chips in the chapters. Every value comes from a research file, which is cited in the entry's `notes` and `source_file`. Six of them were also checked against the primary Cour des comptes PDF (RSPFP, 25 June 2026): r, g, the debt-stabilizing balance (2025 and 2026), 3.8 points of tax hikes over 2010-2014, and EUR 23.0 bn of tax increases in 2025. The chapters were not edited.

## New figures (`figures.json`, 57 entries) and the placeholders they replace

| Placeholder (chapter) | New id(s) | Value | Source (research file; primary) |
|---|---|---|---|
| `te_change_2017_2024_pp`, `balance_change_2017_2024_pp`, `te_change_2019_2025_pp`, `total_revenue_change_2019_2025_pp`, `balance_change_2019_2025_pp` (ch. 4) | same ids | -0.7 / -2.4 / +2.0 / -0.8 / -2.7 points of GDP | File 10 §4.2; Eurostat gov_10a_main |
| `tax_hikes_2010_2014_pts` (ch. 4) | same | 3.8 points of GDP | File 10 §4.2; Cour RSPFP 2026 (checked in PDF) |
| `rexecode_levies_2024_2026_eur_bn`, `_pts` (ch. 4) | same | 36.7 bn; 1.2 points of GDP (caveat: employer-funded institute) | File 08 §2 row 4, §3.2; Rexecode DT 105 |
| `cour_2025_tax_increases_eur_bn` (ch. 4) | same | 23.0 bn | File 10 §4.3; Cour RSPFP 2026 (checked in PDF) |
| `deficit_state/odac/apul/asso_2025_eur_bn` (ch. 4) | same | 128.1 / 2.2 / 15.6 / 5.8 bn (positive = deficit) | File 06 §2 row 4; Insee 2381402 (28 Aug 2026) |
| `cofog_general_public_services/interest/economic_affairs/public_order/recreation_culture/housing_amenities/environment/family/unemployment_2024_pct_te` (ch. 2) | same | 10.8 / 3.5 / 9.9 / 3.1 / 2.6 / 2.5 / 1.8 / 4.0 / 2.9 % of total public expenditure | File 01 §4.1; Eurostat gov_10a_exp |
| `drees_old_age_survivors/health/four_other_risks_2024_share_pct` (ch. 2) | same | 45.8 / 36.3 / 17.9 % of social protection benefits | File 02 §3.2 [S1]; file 20 §4.3; Drees CPS 2025 |
| `gap2024_health_sha_pp` (ch. 2) | same | +1.06 points of GDP (caveat) | File 12 [E1]; file 00 log 35; Eurostat hlth_sha11_hf |
| Ch. 5 "notation" block, `credit_ratings_oct2026` | `rating_moodys_oct2026_notches` (Aa3 negative), `rating_sp_oct2026_notches` (A+ stable), `rating_fitch_oct2026_notches` (A+ stable); `rating_actions` (7 dated actions 2025-2026); `rating_tables/credit_ratings_oct2026` (a `[[fig:credit_ratings_oct2026]]` chip resolves) | Notches below AAA/Aaa: 3 / 4 / 4 | File 06 §3.4; AFT ratings page |
| Ch. 5 r and g sliders, `apparent_interest_rate_2025_pct`, `nominal_gdp_growth_2025_pct`, `debt_stabilizing_primary_balance_2025_pct_gdp` | same ids, plus `apparent_interest_rate_2026f_pct` (2.2), `nominal_gdp_growth_2026f_pct` (2.2), `debt_stabilizing_primary_balance_2026f_pct_gdp` (0.0) | r 2.0%, g 1.9%, +0.1% of GDP (a primary surplus) | File 06 §3.5; Cour RSPFP 2026 tables 8 and 18 (checked in PDF) |
| Ch. 5 `debt_eu_rank_2025` | same | 3rd of 27 | File 06 §2 row 33 |
| Ch. 3 annex A1 | `social_contributions_2025_eur_bn`, `vat_2025_eur_bn`, `csg_crds_2025_eur_bn`, `ir_net_2025_eur_bn`, `corporate_tax_net_2025_eur_bn` | 446.3 / 208.8 / 165.9 / 94.3 / 59.3 bn | File 05 §2 rows 13-18; Insee table 3.217 |
| Ch. 3 annex A3 (indirect taxes) | `levies_share_income_d1_2022_pct`, `levies_share_income_d10_2022_pct` | 64 / 48 % of pre-transfer income | File 05 §6.2; Insee Première 2022 |
| Ch. 3 annex A4 | `ipp_effective_rate_top01_2016_pct` (46), `ipp_effective_rate_billionaires_2016_pct` (26), `geerolf_rate_billionaires_homogeneous_pct` (25.1), `geerolf_rate_top10_threshold_pct` (26.8), `oecd_tax_wedge_single_2025_pct` (47.2), `oecd_tax_wedge_single_2025_rank` (3 of 38), `employer_ssc_2024_pct_gdp` (10.0) | | File 05 §2 rows 14, 21, 27, §6.3; IPP note 92, Geerolf, OECD Taxing Wages 2026 |
| Ch. 3 annex A5 | `po_2017_eur_bn` (1,038.1), `po_change_2017_2025_nominal_pct` (+25.7), `po_change_2017_2025_real_pct` (+2.5) | | File 14 §7.1; Insee table 3.216 |
| Ch. 3 annex A6 | `refundable_tax_credits_2024_eur_bn` (19.6), `tax_revenue_per_capita_pps_2024` (17,800), `tax_revenue_per_capita_pps_2024_rank` (9th of 27) | | File 18 §1.3; file 05 §2 row 12 |
| Quiz input (Q38) | `isf_repeal_mechanical_loss_eur_bn` | range 3-4.5 bn | File 07 §3.2; CAE Focus 118 |

Schema: `base` gains `notches` and `pct_change`. `figures.json` gains `rating_actions` and `rating_tables`.

## New yardsticks (`yardsticks.json`, 12 entries)

These are the derived values the chapters compute in `[[calc:]]`:

- `calendar_days_*` for the seven new COFOG functions, plus `calendar_days_gps_excl_interest` (26.6 days, with its caveat).
- `deficit_state_share_pct` (84.5%).
- `te_change_2019_2025_days` (12.7).
- `rexecode_levies_2024_2026_days` (7.8).
- `r_minus_g_2025_pp` (0.1).

**`[[yard:household_monthly_income_eur]]`.** It stays a parameter: it is an editorial choice, not a computed value. Chips now resolve against `yardsticks[]` first, then `parameters[]`. This is documented in the parameter's `notes` and in README §3, and checked by `validate.py`.

## Quiz

Q36-Q40 are new left-coded rotation items. Every answer comes from `figures.json`, and each item carries a steelman.

| Item | Question | Answer |
|---|---|---|
| Q36 | Share of the 2025 deficit represented by the 2018-2023 tax cuts | about 41%, by formula |
| Q37 | Change in public spending, 2019-2025 | +2.0 points of GDP |
| Q38 | ISF restoration, in days of public spending | 0.64-0.96 days, by range formulas |
| Q39 | New levies decided in 2024-2026 | 36.7 bn |
| Q40 | Effective tax rate of the top 0.1% | 46%; the billionaires' 26% and Geerolf's critique are in the steelman |

**Counts by camp.** Right 11, left 11, general 11, both 3, anti_tax 2, pessimism 2 (40 items).

**Draw rule.** `design.draw_rule` requires exactly as many left- as right-coded items in every draw, with a reference procedure. `validate.py` checks four things: the bank is balanced, every draw size is feasible (teaser 3: k in 0-1; full 25: k in 4-11), the 500 seeded draws of each mode all respect the rule, and every `camp_coding` is either coded or neutral.

## Validator

`python3 -I validate.py` now also checks the chips in the chapters and the rating history. Chapter problems are reported as errors with the prefix `chapters/` and counted separately; `--data-only` skips them. Run on 2026-10-25, it reported:

- **Data errors: 0.**
- **Chapter errors: 60.**
  - 56 `[[fig-a-creer:...]]` chips whose ids now exist. They need to be renamed `[[fig:...]]`.
  - 4 "EN ATTENTE DE DONNÉES" blocks in chapter 5.
- **47 warnings** for the `[[yd:]]` alias in chapter 5, which should use `[[yard:]]`.

`--write-derived` changed only `yardsticks.json`: `proposals.json` and `simulator-levers.json` are byte-identical.

## Not added (could not be verified, or not a number)

1. **Rating actions of 2023-2024.** These are Fitch AA → AA- (April 2023), S&P AA → AA- (May 2024) and Moody's Aa2 → Aa3 (December 2024). They are not in the research base. The primary pages could not be opened on 2026-10-25: the AFT page returned HTTP 403, Fitch could not be fetched, and S&P and Moody's returned 403 or require a login. Only press articles and search snippets confirm them. A primary release must be checked before they are added. The gap is noted in `rating_tables[0].not_included`.
2. **Outlook at the time of the Fitch (12 Sep 2025) and S&P (17 Oct 2025) downgrades.** It is stored as `null`. The research base gives only the current outlook.
3. **Type of the AFT-listed actions of 10 Apr, 29 May and 28 Aug 2026.** The AFT gives dates only, so they are stored as `review_listed_by_aft`.
4. **Moody's affirmation of 23 Oct 2026.** It is added with status `caveat`. Its source is press (CNBC) via file 06, and the AFT page had not yet been updated.
5. **Share of income tax paid by the top 10% (annex A2).** The DGFiP gives only "près des trois quarts", with no number, so no figure was created. Cite it with a `[[src:]]` chip.
6. **Annex A3 decile series (Insee Analyses 118) and annex A6 OECD values for every country.** These are chart series and belong in data files (`research/data`), not in single figures.
7. **Annex A5 poll result (Elabe, 72%).** It is already misperception M10, not a figure.
8. **2026 apparent rate.** The misaligned extraction of table 18 shows 2.5; the Cour's body text says 2.2. The body text is used and the entry is flagged as a caveat.

## For the editorial team

- File 20 §6.3 should list Q36-Q40 and the tightened draw rule.
- Chapter 4 says the deficit is "85%" State. The yardstick gives 84.5%: keep "environ 85 %".
- Chapter 5: `[[fig:credit_ratings_oct2026]]` resolves to the rating table. The three grade figures and the dated actions are what a timeline should display. Do not state the 2023-2024 actions until item 1 above is resolved.

## Data pass of 2026-10-25 (plan decisions D-return60, D-data-pass, D-rounding)

Every value below was checked against its research file **and** its primary source the same day. `python3 -I validate.py --write-derived` followed by `python3 -I validate.py --strict` gives **Data errors: 0**. Derived values were rewritten only in `proposals.json`. `yardsticks.json` and `simulator-levers.json` are byte-identical.

### D-return60 (general return to retirement at 60)

- `return_60_general_cost_eur_bn.range.low` changed from 35 to **43**. The bounds are now Fipeco (about 43) and Institut Montaigne (58). The 35 had no source: it is the top of the 26-35 range for partial returns.
- `return_60_general_cost_pct_gdp.range.low` changed from 1.2 to **1.4** (43 / 2,991.1 = 1.44).
- Proposal `retirement_60_general_nfp`: the range is now -58 to -43 and the midpoint is -50.5. Its derived values were rewritten. For 43 bn the published conversions are **9.2 days, 28% of the deficit and EUR 623 per inhabitant**. For 58 bn they are 12.4 days, 38% and EUR 841. The household scale gives EUR 83-111 a month.
- Quiz Q13: the correct option and `correct_value` now read « de 43 à 58 milliards d'euros ».
- Row 44 of `research/00-reference-figures.md` and of `fr/00-chiffres-de-reference.md` now gives 43-58 bn and 1.4-1.9 points of GDP, with a dated correction note.
- **Still to do (owned elsewhere):**
  - Chapter 7, line 135, still shows the values for 35 bn (7,5 jours ; 23,1 % ; 67 €). This causes 3 `calc-value` errors until the chapter uses 9,2-12,4 jours, 28-38 % and 83-111 €.
  - Lever S1 in `simulator-levers.json` still has `yield_high` -35.
  - File 20 §3.4 / §4.10 still publishes the conversions for 35 bn.
  - 35 is not listed in file 00 §4 (superseded values), so no `superseded` entry was added.

### D-data-pass: figures added (19)

| id | value | source checked |
|---|---|---|
| pension_state_balancing_contribution_2025_eur_bn | 49.3 bn | COR RA 2026 (PDF; 11.7% of resources) |
| pension_balance_convention_range_pct_gdp | range 0.2-1.9 (% of GDP, deficit), caveat | COR RA 2026: -0.2% (legal convention); balancing contributions and subsidies 1.9% of GDP in 2025 |
| tax_gap_cour_range_eur_bn | range 30-130 bn, caveat | Cour des comptes, 16 Dec 2025 (PDF) |
| tax_audit_assessed_2024_eur_bn | 20.1 bn | same report |
| tax_audit_collected_2024_eur_bn | 11.4 bn | same report |
| ipp81_gain_top1_pct | +3.3% | IPP Note 81 page |
| ipp81_gain_bottom5_pct | +0.8% | IPP Note 81 page |
| ipp81_gain_unemployed_pct | -1.1% (loss) | IPP Note 81 page |
| bozio_wasmer_threshold_smic | 2.5 SMIC, caveat (parameter) | Bozio-Wasmer report, Oct 2024 (PDF) |
| multiplier_operating_spending_y1 | 0.8 (range 0.5-1.1), caveat | OFCE PB 154 (« compris entre 0,7 et 0,8 »); file 17 §8 |
| productivity_per_hour_pps_2025 | 114.6 (EU-27 = 100) | Eurostat API nama_10_lp_ulc, recomputed |
| productivity_per_hour_pps_2025_rank | 8 of 27 | same, recomputed |
| poverty_reduction_transfers_2025_pp | 30.5 pts, caveat | Eurostat ilc_li09 - ilc_li02, recomputed |
| poverty_reduction_transfers_2025_rank | 3 of 27 | same (BE and PL 30.7) |
| poverty_reduction_excl_pensions_2025_pp | 10.2 pts, caveat | Eurostat ilc_li10 - ilc_li02, recomputed |
| poverty_reduction_excl_pensions_2025_rank | 6 of 27 | same |
| arop_before_transfers_2025_pct | 46.8% | Eurostat ilc_li09 (2nd of 27, after IT 46.9) |
| net_debt_2025_pct_gdp | 108.5% | Insee, 29 May 2026 |
| public_gfcf_2025_pct_gdp | 4.4% | Eurostat API gov_10a_main P51G |

**Other changes**

- `tax_rich_package_eur_bn` and proposal `tax_rich_package`:
  - The CDHR line (0.5-1) was removed from the components. The CDHR has been in force since the 2025 budget, so it is not new revenue.
  - The 10-25 range is kept: the remaining components sum to 8-25, which still rounds to « about 10-25 » in file 07.
  - Note added: « synthèse de la plateforme ; composante succession sans chiffrage indépendant ».
- **Sources added (8):**
  - `f06:imf_aiv2026`: IMF PR 26/255 of 22 Jul 2026 (Board meeting 17 Jul). It gives a primary balance of -1.7% and gross debt of 121.1% of GDP in 2028. Page opened.
  - Publication entries for the new figures: `f03:cor26`, `f08:ipp81`, `f08:bw2024`, `f08:es-lp`, `f08:es-gov`, `f01:es-silc`, `f10:S33`.

### Skipped: primary source not verifiable

- **avg_maturity_state_debt_2026_years.** The AFT pages and Monthly Bulletin no. 437 return HTTP 403 to automated access. Files 06 and 10 record a browser reading of **8 years 158 days at 30 Sep 2026, about 8.4 years**. The 8.5 is the end-2025 value (8 years 184 days, Cour des comptes). Add the figure once someone confirms it in a browser.
- **judges_per_100k_2022 (11.3) and cepej_median_judges_2022 (17.6).** The decision requires the CEPEJ primary source, but coe.int and rm.coe.int return 403. Only the secondary source (Le Club des juristes) could be opened, and it confirms 11.3 and 17.6 (2022 data). The symmetry gate for ch6 s6 stays open.

### Quiz rounding (D-rounding: one display per indicator)

- Q01 `correct_value.text_fr`/`text_en` changed from « 23,4 » to « 23,40 € » (and « 24,30 € » for the COR concept), the form the chapters use.
- Q39 explanation changed from « 23 milliards » to « 23,0 milliards » (EN: EUR 23.0 bn).
- Both `quiz-rounding` warnings are gone. D-quiz wording changes (Q18, Q25, Q37, Q38, Q39 answer text, Q40) were not part of this pass.

## Pass of 25 October 2026 (evening): S1, D-quiz, display, exemptions, missing entries

`python3 -I validate.py --write-derived` followed by `python3 -I validate.py --strict` gives **Data errors: 0; chapter errors: 0; 0 warnings** (the three warnings of open item 1 are gone). `--write-derived` changed nothing in `proposals.json` or `simulator-levers.json`: S1 has no midpoint or ceiling to derive.

### 1. Lever S1 (D-return60)

- In `simulator-levers.json`, the setting 60 (`positions[0].static_eur_bn`), `yield_high` and `yield_static.high` changed from -35 to **-43**. The range is now **-58 to -43** (Institut Montaigne 58, Fipeco about 43), matching `return_60_general_cost_eur_bn`.
- The `yield_static.note` now says that 26-35 bn applies only to partial (RN-type) versions.
- The README example of a range changed from « EUR 35-58 bn » to « EUR 43-58 bn ».
- Derived values: for 43-58 bn, the platform gives 9.2-12.4 days, 28-38% of the 2025 deficit, EUR 623-841 per inhabitant and EUR 83-111 a month for the household. These were already in proposal `retirement_60_general_nfp`. Nothing else is derived from S1.

### 2. Quiz (D-quiz)

- **Q40** is now about the billionaires. Its answer is **about 26%** (IPP, about 75 households, 2016), and the top 0.1% (46%) is given as the comparison. It is coded **both**. The steelman gives each side: the drop at the very top (left), and Geerolf's 25.1% vs 26.8% plus the timing argument (right, file 05 §6.3).
- **Q38**: the targeted claim now reads « restoring the ISF would bring in a large share of the money needed to cut the deficit ».
- **Q39**:
  - The answer gives both counts: Cour des comptes 23.0 bn for 2025 alone, and Rexecode 36.7 bn over 2024-2026 (1.2 points of GDP).
  - It is now a range answer (`range_formulas` 23.0-36.7), and the question no longer names Rexecode.
  - Rexecode carries the glossary §1.13 label: « institut de conjoncture proche des organisations patronales » (EN: « a business-cycle institute close to employers' organizations »).
  - The same label fix was applied to **Q36**, which still had the old label.
- **Q18**: the one-sided steelman « Part of it is debt-financed » was removed. The new one is about concepts and age: health and education counted at cost, pensions seen as deferred pay, and 96% net beneficiaries in households aged 65 or over against 43% for the rest (Insee IA 118, file 14 §3).
- **Q25**: option a is now « Les dépenses de fonctionnement de l'État » (EN: « State operating expenditure »).
- **Q37**: the explanation adds the 2019-2024 window, which file 10 §4.2 reads as « both »: +1.7 for spending and -1.8 for revenue, in roughly equal parts. The new figure ids are in `figure_ids`.
- **Q41 (new, rotation, left)** restores the balance after Q40 was recoded.
  - The question asks how much of the 20.1 bn of tax-audit assessments in 2024 was collected. The answer is **11.4 bn** (Cour des comptes, 16 Dec 2025, `f07:S10`; figures added in the previous pass after a primary check).
  - The targeted belief is « fighting tax fraud harder would easily bring in tens of billions more each year », linked to M13.
  - The steelman: the Cour cannot tell whether fraud is closer to 30 or 130 bn.
  - It mirrors Q21, the right-coded question on the anti-fraud plan.
- **Bank: 41 items.** Left 11, right 11, both 4, anti-tax 2, pessimism 2, general 11. The draw rule holds for every format (full and classroom: k in [3, 11]), and the 500 seeded draws pass.
- **To report in file 20 §6.3 (not my file):** Q36-Q41, the Q40 recoding and the 41-item count.

### 3. Yardsticks

- The `display_decimals` of `gap_to_3pct_eur_bn` changed from 0 to **1**, to match the « 61,9 » shown in chapter 7. The `rounding` warning is gone.

### 4. validate.py: documented lint exemptions (check 10)

- New file **`lint-exemptions.json`**. Each entry has `number`, `unit`, `ids`, `reason_en`, `decided_by` and `date`.
- An entry silences a `same-number-ids` warning only when the number, the unit **and** the whole set of ids match. A third id showing the same number is still reported.
- Malformed entries, unknown ids and duplicate entries are data errors. Applied exemptions are listed as INFO. An entry that matches no finding gives a `stale-exemption` warning.
- The mechanism is documented in the docstring of `validate.py` and in README §5 item 10.
- **Registered entries:**
  - « 25 Md€ »: `tax_rich_package_eur_bn` vs `zucman_proponents_eur_bn`. Both are upper bounds of different ranges.
  - « 47,2 % »: `ir_households_paying_pct` vs `oecd_tax_wedge_single_2025_pct`. These are unrelated shares.

### 5. Entries added to figures.json (12) and sources.json (3)

| id | value | primary source checked on 2026-10-25 |
|---|---|---|
| te_change_2019_2024_pp | +1.7 pts of GDP | Eurostat API gov_10a_main (updated 21 Oct 2026): TE 55.3 → 57.0 |
| total_revenue_change_2019_2024_pp | -1.8 pts | same: TR 53.0 → 51.2 |
| te_change_2005_2025_pp | +3.0 pts (ch. 1 denominator) | same: TE 54.3 → 57.3 |
| total_revenue_change_2005_2025_pp | +1.4 pts (ch. 1 denominator) | same: TR 50.8 → 52.2 |
| balance_change_2005_2025_pp | -1.6 pts (requested by ch. 4) | same: B9 -3.5 → -5.1 |
| te_volume_growth_avg_2005_2025_pct | 1.4% a year in volume (ch. 1 denominator) | HCSP *Focus Finances publiques*, 17 Jul 2026 (PDF): « les dépenses publiques ont en moyenne augmenté de 1,4 % par an de 2005 à 2025 » |
| pensions_cor_2045f_pct_gdp | 14.2% of GDP, caveat (projection) | COR RA 2026 (PDF): « 14,1 % du PIB en 2025, contre 14,2 % en 2045 » |
| pensions_cor_2070f_pct_gdp | 15.3% (range 14.5-16.1 by productivity), caveat | COR RA 2026 (PDF) |
| pension_resources_2025_pct_gdp | 13.9% | COR RA 2026 (PDF) |
| pension_resources_2070f_pct_gdp | 12.9%, caveat | COR RA 2026 (PDF) |
| antifraud_2026_announced_eur_bn | 1.5 bn, caveat (government claim) | HCFP avis 2026-5 §68 (PDF): the measure « précédemment chiffrée à 1,5 Md » disappeared from the 2026 forecast |
| avg_maturity_state_debt_2026_years | 8.4 years | AFT page *Encours de la dette négociable au 30 septembre 2026* (updated 1 Oct 2026), read in a browser: « 8 ans et 158 jours » (8.43). The PDF of Monthly Bulletin no. 437 was not re-opened; the AFT page gives the same data. |

- **Sources added:** `f10:S8` (HCSP), `f10:S30` (Eurostat) and `f10:S35` (AFT), from the source table of file 10.
- **Rating actions of 2023-2024:**
  - Verified on Fitch's own releases: the downgrade from AA to AA- (outlook stable) on 28 Apr 2023, and the outlook change to negative (AA- affirmed) on 11 Oct 2024.
  - They are **not added** as `rating_actions`, because file 06 does not record them and every action needs a `match_text` there. Instead, they are listed with their URLs in `rating_tables[0].not_included`.
  - S&P (31 May 2024, AA → AA-) and Moody's (Dec 2024, Aa2 → Aa3): the releases need a login, so these are confirmed by press only and not verified.
  - The AFT page still lists Moody's at 10 Apr 2026, so `moodys_2026_10_23` stays « caveat ».

### Skipped (not verifiable today)

- **`judges_per_100k_2022` and `cepej_median_judges_2022`:**
  - rm.coe.int returns 403 to scripts and 503 in the browser, for Part 1, the country profiles and the presentation. The CEPEJ pages on www.coe.int open but only link to rm.coe.int. The CEPEJ-STAT Tableau views could not be exported.
  - **New discrepancy to resolve:** a search result quotes the USM magistrates' union note as giving **11.16** judges per 100,000 for France (median 17.60). The research base has **11.3** (Le Club des juristes).
  - It also mentions a later CEPEJ fiche on 2024 data (11.6 vs an EU median of 23.4), which may mean a newer cycle exists. That would contradict file 04 S31, which reports no newer cycle.
  - The ch. 6 symmetry gate stays open.
- **2017-2025 windows** (`te_change_2017_2025_pp` -0.4, `total_revenue_change_2017_2025_pp` -2.1, `balance_change_2017_2025_pp` -1.7), requested by chapter 4: the Eurostat API confirms these values, but file 10 does not state them, so they would fail check 4. File 10 §4.2 needs a 2017-2025 row first.
- **Not in this task:** the remaining items of open item 4 (chart series, the `year` of `finland_te_2025_pct_gdp`, the note of `cdhr_observed_2025_eur_bn`, the `source` of `zucman_critics_eur_bn`), `te_volume_growth_2025_pct` and `po_2022_pct_gdp`.

## Confrontation aux sources publiques (2026-10-30)

Scope: `proposals.json` and `simulator-levers.json` only, checked against published positions (left, right, institutions). Every new citation below names a text the reviewer opened (URL + date). Sources not yet in `sources.json` are cited in the text fields with their URL; they need `sources.json` entries (owner of that file): Terra Nova (G. Hannezo, 2024-09-20), F. Geerolf "Les mensonges de la taxe Zucman" (rev. 2026-10), Fondation iFRAP Revue 270 (2025-09), Fipeco "Mesures fiscales" (2022-01-27), CPO "Corriger les principales distorsions de l'imposition du patrimoine" (2025-12-01), Rexecode WP 97 (2025-06/07), Attac "La dette de l'injustice fiscale" (2025-03-26), OFCE blog (2025-07-11), IPP Note 92 (2023-06; today only reachable through f07:S50). Glossary §1.13 also needs labels for the CPO (public body) and F. Geerolf (person: "économiste à l'OFCE") before they appear on the site.

### Changes

1. `zucman_tax` (points 01, 03, 05; left and right critiques): "~75 richest households" replaced by the IPP wording (top 0.0002%); "fewer than 350 departures" (not in the CAE text) replaced by the CAE metrics (+0.04-0.09 pt, elasticity 0.02-0.18%); added the disputed baseline (iFRAP 42.1%; Geerolf/OFCE 25.1% vs 26.8%), iFRAP's reading of the CAE study, both sides of the legal argument (Capus majority, Sas minority, CPO cap at about 1.8%), and the convergence of Terra Nova and Geerolf with the Senate and iFRAP; the Senate 2-3 now states its design assumption; range label relabeled "independent and critical estimates".
2. `isf_restoration` (point 06): unconfirmed "4.5 bn France Stratégie" replaced by CAE 3-4.5 (mechanical) and Fipeco about 3; stated that the range is the cost of the 2018 repeal; CPO supply-side warning added.
3. `isf_climate_lfi` (point 06): counter-argument added (Institut Montaigne 3.5 vs 15 claimed, f07:S15); different base from the repeal cost.
4. `pfu_abolition_lfi` (point 07): Montaigne 3.2 = PFU plus exit tax; static cost "about 1" replaced by Fipeco 1.5-1.8 (probably nil ex post, dividends 14 to 23 bn); no investment effect (Fipeco; France Stratégie via Terra Nova); Terra Nova variant added.
5. `inheritance_reform_lfi`, `inheritance_package_ps` (points 08, 12): Terra Nova (4 + 1.4) and CPO design added; "no estimate exists for taxing unrealized gains at death" corrected (Terra Nova about 4, phased in); CAE 9-19 described as a broad-reform steady state, 14 as a midpoint.
6. `cdhr` (points 09, 16): 2026 expectation 0.7 -> 0.65 (Legifiscal, f07:S35; derived conversions recomputed); Cour des comptes reading (deferrable income, yield still subject to adjustment, extended until deficit < 3%) and the caveat that the lesson is about design, not taxation in principle.
7. `tax_rich_package` (point 11): "62 bn a year" -> "62 bn in 2023"; Terra Nova 10-15 benchmark; 17.5 flagged as a midpoint above it; one-sixth bound tied to upper estimates.
8. `tax_cuts_2018_2023` (point 10): unverified Rexecode "1.2 pts erased" removed; Rexecode WP 97 (66 bn cumulated cuts, 25 bn of increases 2024-2025) and Cour 2026 (23 bn in 2025) added; left readings added (Attac 308.6 bn cumulated, 207 bn; OFCE 2.5 pt vs 2.4 pt).
9. `fuel_freeze_lfi` (point 18): estimates and range marked `computed_by_us`; no published costing found; HCFP energy-price uncertainty.
10. `energy_vat_rn` (point 19): EU-rules risk (Public Sénat, f07:S19).
11. `lr_tax_cuts` (right critique): 56 vs 51 bn discrepancy flagged (f07:S21), not resolved.
12. Labels: "business-funded" removed from orientation fields (Institut Montaigne -> "liberal-centrist"; Institut de l'Entreprise -> "close to business"); Rexecode no longer "employer-linked" but carries its glossary label, like every source cited in these fields (glossary §1.13 rules 2 and 4).
13. Levers: R1 headline (yield_low/central/high) is now the independent band 2/5/6, with the static 15-25 shown next to it; behavioral note relabeled; legal note gives both sides. R2: gross mechanical shown next to net; CPO warning. R3: 3.2 = package; Fipeco behavior note. R4: "no independent costing" -> partial costings of different designs; CPO option not modeled; 6.5 flagged as midpoint. R5: design caveat. S4: rule for "enabled with a range" stated for both sides. Classes `wealth_tax` (demand only, CPO supply warning) and `corporate_capital` (Rexecode, Cour 2026; OFCE PB 154 values to re-check).

### Rejected or not applied (with reason)

- Left, PFU: "IPP/CAE note a rise in the returns of high-wealth people after 2018": no opened text with URL supports it in the critique; not added.
- Left, multiplier classes: "low multipliers make top-income taxes cheap in growth terms": a reading of the site's own numbers, no published source; not added.
- Right, S4 vs R1/R4 asymmetry: rejected as stated; the rule is the same on both sides (R1 and R4 have independent estimates, S4 has none). The rule is now written in S4's note.
- Right, R4 "Montaigne about 9": not used; the reviewer flagged the PDF layout as ambiguous.
- Point 15 (R11 "-980,000 FTE", "rule 0.89 vs model 0.72"): kept. The figures are attributed to Bozio-Wasmer and to Mésange documentation the reviewer did not open; not shown to be wrong. To re-check.
- Point 20: the verdict text was truncated in the task input; nothing applied.
- Changing the global `behavioral_responses` default: not done (it would also move R11); the R1 fix is lever-level.

### Figures still needed (not available from opened sources)

- IPP Note 92 as its own `sources.json` entry; Rexecode WP 97 URL in `sources.json` (f07:S49 is a different, Sept 2026 paper with no URL).
- Inheritance and gift duties 2025 (21.1 bn) and the six-month payment rule: primary source to re-open.
- OFCE PB 154 class values (surtax 0.29, CDHR about 0): to re-open.
- LR tax cuts: 51 or 56 bn, from the LR plan document.
- A published costing of the LFI fuel freeze (none found).
