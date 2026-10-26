#!/usr/bin/env python3
"""
Harmonized international comparison backbone for the French public-finance platform.

Downloads Eurostat (dissemination SDMX 2.1 API, SDMX-CSV) and OECD (SDMX REST, CSV)
data, saves raw extracts under research/data/raw/{eurostat,oecd}/, and computes for
each indicator and for 2005, 2015 and the latest available year:

  France value, EU-27 aggregate, euro-area aggregate (EA21 and EA20),
  mean / median / n of EU-27 member states, of euro-area (EA21) members,
  and of the panel (DE, IT, ES, NL, BE, SE, DK; France excluded from panel stats),
  France's rank (1 = highest) in EU-27, in EA21 and in panel+France,
  France minus euro-area aggregate gap, France minus EU-27 member mean gap.

Usage (from anywhere; run Python in isolated mode):
    python3 -I build_international_comparison.py            # use cached raw files
    python3 -I build_international_comparison.py --refresh  # re-download everything

Only the Python standard library is used.
"""
import csv
import io
import os
import statistics
import sys
import time
import urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
DATA = os.path.normpath(os.path.join(HERE, ".."))
RAW_ES = os.path.join(DATA, "raw", "09_intl", "eurostat")
RAW_OECD = os.path.join(DATA, "raw", "09_intl", "oecd")
OUT = DATA
REFRESH = "--refresh" in sys.argv

EU27 = ["AT", "BE", "BG", "HR", "CY", "CZ", "DK", "EE", "FI", "FR", "DE", "EL", "HU", "IE",
        "IT", "LV", "LT", "LU", "MT", "NL", "PL", "PT", "RO", "SK", "SI", "ES", "SE"]
# Euro area, current composition (Bulgaria joined on 1 January 2026 -> EA21)
EA21 = ["AT", "BE", "BG", "HR", "CY", "EE", "FI", "FR", "DE", "EL", "IE", "IT", "LV", "LT",
        "LU", "MT", "NL", "PT", "SK", "SI", "ES"]
PANEL = ["DE", "IT", "ES", "NL", "BE", "SE", "DK"]
AGGS = ["EU27_2020", "EA21", "EA20"]
GEOS = "+".join(EU27 + AGGS)
YEARS_FIXED = [2005, 2015]

OECD38 = ["AUS", "AUT", "BEL", "CAN", "CHL", "COL", "CRI", "CZE", "DNK", "EST", "FIN", "FRA",
          "DEU", "GRC", "HUN", "ISL", "IRL", "ISR", "ITA", "JPN", "KOR", "LVA", "LTU", "LUX",
          "MEX", "NLD", "NZL", "NOR", "POL", "PRT", "SVK", "SVN", "ESP", "SWE", "CHE", "TUR",
          "GBR", "USA"]

ES_BASE = "https://ec.europa.eu/eurostat/api/dissemination/sdmx/2.1/data/"
OECD_BASE = "https://sdmx.oecd.org/public/rest/data/"

COFOG_DIV = {
    "GF01": "General public services", "GF02": "Defence", "GF03": "Public order and safety",
    "GF04": "Economic affairs", "GF05": "Environmental protection",
    "GF06": "Housing and community amenities", "GF07": "Health",
    "GF08": "Recreation, culture and religion", "GF09": "Education",
    "GF10": "Social protection",
}
COFOG_GRP = {
    "GF0107": "Public debt transactions (interest)", "GF1001": "Sickness and disability",
    "GF1002": "Old age", "GF1003": "Survivors", "GF1004": "Family and children",
    "GF1005": "Unemployment", "GF1006": "Housing (social)",
    "GF1007": "Social exclusion n.e.c.", "GF0701": "Health: medical products",
    "GF0702": "Health: outpatient services", "GF0703": "Health: hospital services",
    "GF0704": "Health: public health services", "GF0705": "Health: R&D",
    "GF0706": "Health n.e.c.", "GF0901": "Education: pre-primary and primary",
    "GF0902": "Education: secondary", "GF0904": "Education: tertiary",
}

# (local file stem, dataset, key, extra query)
ES_REQUESTS = [
    ("gov_10a_main", "gov_10a_main",
     "A.PC_GDP+MIO_EUR.S13.TE+TR+B9+D1PAY+D62PAY+D632PAY+P51G+D41PAY+P2+D61REC+D2REC+D5REC." + GEOS, ""),
    ("gov_10dd_edpt1", "gov_10dd_edpt1", "A.PC_GDP.S13.B9+GD." + GEOS, ""),
    ("gov_10a_exp", "gov_10a_exp",
     "A.PC_GDP+PC_TOT.S13." + "+".join(["TOTAL"] + list(COFOG_DIV) + list(COFOG_GRP)) + ".TE." + GEOS, ""),
    ("gov_10a_taxag", "gov_10a_taxag",
     "A.PC_GDP.S13_S212.D2_D5_D91_D61_M_D995+D2_D5_D91_D61_M_D612_M_D614_M_D995+D2_D5_D91+D61." + GEOS, ""),
    ("spr_exp_type", "spr_exp_type", "A.TOTAL+SPR.PC_GDP+PPS_HAB." + GEOS, ""),
    ("spr_exp_func", "spr_exp_func", "A.SPR.TOTAL+OLD+SICK.PC_GDP+PPS_HAB." + GEOS, ""),
    ("nama_10_pc", "nama_10_pc", "A.CP_PPS_EU27_2020_HAB.B1GQ+P3_S13." + GEOS, ""),
    ("demo_mlexpec", "demo_mlexpec", "A.YR.T.Y_LT1." + GEOS, ""),
    ("ilc_li02", "ilc_li02", "A.MED_EI.PC.B_60.T.TOTAL." + GEOS, ""),
    ("ilc_li10", "ilc_li10", "A.MED_EI.B_60.T.TOTAL.PC." + GEOS, ""),
    ("ilc_di12", "ilc_di12", "A.TOTAL.GINI_HND." + GEOS, ""),
]

OECD_REQUESTS = [
    ("oecd_revenue_statistics_total_tax_pc_gdp",
     "OECD.CTP.TPS,DSD_REV_COMP_OECD@DF_RSOECD,2.0",
     "." .join(["+".join(OECD38 + ["OECD_REP"]), "TAX_REV", "S13", "_T", "_T", "PT_B1GQ", "A"])),
    ("oecd_naag_general_government_pc_gdp",
     "OECD.SDD.NAD,DSD_NAAG_VI@DF_NAAG_VI,1.0",
     "A." + "+".join(OECD38) + ".OTES13+OTRS13+B9S13+LES13_FD4+D1S13+ODAS13_D2_D5_D91_D611_D613._T.PT_B1GQ."),
]


def fetch(url, path, headers=None):
    if os.path.exists(path) and not REFRESH:
        return url
    req = urllib.request.Request(url, headers=headers or {"User-Agent": "research-script"})
    for attempt in range(3):
        try:
            with urllib.request.urlopen(req, timeout=300) as r:
                data = r.read()
            with open(path, "wb") as f:
                f.write(data)
            return url
        except Exception as e:  # noqa: BLE001
            print("retry", attempt, url, e, file=sys.stderr)
            if "400" in str(e) and "+EA20" in url:  # EA20 not defined in some datasets (e.g. EU-SILC)
                url = url.replace("+EA20", "")
                req = urllib.request.Request(url, headers=headers or {"User-Agent": "research-script"})
                continue
            time.sleep(5)
    raise RuntimeError("download failed: " + url)


def download_all():
    os.makedirs(RAW_ES, exist_ok=True)
    os.makedirs(RAW_OECD, exist_ok=True)
    log = []
    for stem, ds, key, extra in ES_REQUESTS:
        url = f"{ES_BASE}{ds}/{key}?format=SDMX-CSV&startPeriod=1995{extra}"
        url = fetch(url, os.path.join(RAW_ES, stem + ".csv"))
        log.append((stem + ".csv", url))
    for stem, flow, key in OECD_REQUESTS:
        url = f"{OECD_BASE}{flow}/{key}?startPeriod=1995"
        url = fetch(url, os.path.join(RAW_OECD, stem + ".csv"),
              {"Accept": "application/vnd.sdmx.data+csv; charset=utf-8", "User-Agent": "research-script"})
        log.append((stem + ".csv", url))
    with open(os.path.join(DATA, "09_intl_download_log.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["file", "url", "extracted_utc"])
        for fn, u in log:
            p = os.path.join(RAW_ES if not fn.startswith("oecd") else RAW_OECD, fn)
            w.writerow([fn, u, time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime(os.path.getmtime(p)))])


def read_es(stem):
    """Return dict {(dims tuple without geo/time): {geo: {year: (value, flag)}}} and last-update."""
    path = os.path.join(RAW_ES, stem + ".csv")
    with open(path, encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    out = {}
    updates = set()
    skip = {"DATAFLOW", "LAST UPDATE", "freq", "geo", "TIME_PERIOD", "OBS_VALUE", "OBS_FLAG", "CONF_STATUS"}
    for r in rows:
        if r["OBS_VALUE"] in ("", None):
            continue
        updates.add(r["LAST UPDATE"])
        dims = tuple((k, r[k]) for k in r if k not in skip)
        out.setdefault(dims, {}).setdefault(r["geo"], {})[int(r["TIME_PERIOD"])] = (float(r["OBS_VALUE"]), r.get("OBS_FLAG", ""))
    return out, sorted(updates)


def series(data, **filt):
    for dims, val in data.items():
        d = dict(dims)
        if all(d.get(k) == v for k, v in filt.items()):
            return val
    return {}


def rank_desc(values, target):
    """1 = highest. Competition rank."""
    return 1 + sum(1 for v in values if v > target)


def stats_for(ser, year, invert=False):
    """ser: {geo: {year: (v, flag)}}. invert: rank on -value (e.g. deficit)."""
    g = lambda c: ser.get(c, {}).get(year, (None, ""))[0]  # noqa: E731
    fr = g("FR")
    if fr is None:
        return None
    sgn = -1 if invert else 1
    eu_vals = {c: g(c) for c in EU27 if g(c) is not None}
    ea_vals = {c: g(c) for c in EA21 if g(c) is not None}
    pa_vals = {c: g(c) for c in PANEL if g(c) is not None}
    pf = dict(pa_vals, FR=fr)
    res = {
        "year": year, "FR": fr, "FR_flag": ser.get("FR", {}).get(year, (None, ""))[1],
        "EU27_agg": g("EU27_2020"), "EA21_agg": g("EA21"), "EA20_agg": g("EA20"),
        "EU27_mean": statistics.mean(eu_vals.values()) if eu_vals else None,
        "EU27_median": statistics.median(eu_vals.values()) if eu_vals else None,
        "EU27_n": len(eu_vals),
        "EU27_rank": rank_desc([sgn * v for v in eu_vals.values()], sgn * fr),
        "EA21_mean": statistics.mean(ea_vals.values()) if ea_vals else None,
        "EA21_median": statistics.median(ea_vals.values()) if ea_vals else None,
        "EA21_n": len(ea_vals),
        "EA21_rank": rank_desc([sgn * v for v in ea_vals.values()], sgn * fr),
        "PANEL_mean": statistics.mean(pa_vals.values()) if pa_vals else None,
        "PANEL_median": statistics.median(pa_vals.values()) if pa_vals else None,
        "PANEL_n": len(pa_vals),
        "PANEL_rank": rank_desc([sgn * v for v in pf.values()], sgn * fr),
        "PANEL_n_incl_FR": len(pf),
        "top3_EU27": "; ".join(f"{c} {v:.1f}" for c, v in sorted(eu_vals.items(), key=lambda kv: -sgn * kv[1])[:3]),
        "missing_EU27": " ".join(c for c in EU27 if c not in eu_vals),
    }
    for c in PANEL:
        res[c] = g(c)
    ea = res["EA21_agg"] if res["EA21_agg"] is not None else res["EA20_agg"]
    res["gap_FR_minus_EA_agg"] = fr - ea if ea is not None else None
    res["gap_FR_minus_EU27_agg"] = fr - res["EU27_agg"] if res["EU27_agg"] is not None else None
    res["gap_FR_minus_EU27_mean"] = fr - res["EU27_mean"] if eu_vals else None
    return res


def latest_year(ser, min_n=20):
    yrs = sorted({y for c in ser for y in ser[c]}, reverse=True)
    for y in yrs:
        if "FR" in ser and y in ser["FR"] and sum(1 for c in EU27 if y in ser.get(c, {})) >= min_n:
            return y
    return None


def main():
    download_all()
    ind = []  # (indicator_id, label, unit, dataset, series, invert)

    main_d, upd_main = read_es("gov_10a_main")
    for item, lab in [("TE", "Total general government expenditure"), ("TR", "Total general government revenue"),
                      ("D1PAY", "Compensation of employees (D.1, payable)"),
                      ("D62PAY", "Social benefits other than in kind (D.62)"),
                      ("D632PAY", "Social transfers in kind via market producers (D.632)"),
                      ("P51G", "Gross fixed capital formation (P.51g)"), ("D41PAY", "Interest payable (D.41, ESA)"),
                      ("P2", "Intermediate consumption (P.2)"), ("D61REC", "Net social contributions received (D.61)")]:
        ind.append((f"main_{item}", lab, "% of GDP", "gov_10a_main", series(main_d, unit="PC_GDP", na_item=item), False))
    edp_d, upd_edp = read_es("gov_10dd_edpt1")
    ind.append(("edp_B9", "Net lending(+)/borrowing(-) (EDP deficit)", "% of GDP", "gov_10dd_edpt1",
                series(edp_d, unit="PC_GDP", na_item="B9"), True))
    ind.append(("edp_GD", "Gross debt (Maastricht)", "% of GDP", "gov_10dd_edpt1",
                series(edp_d, unit="PC_GDP", na_item="GD"), False))
    tax_d, upd_tax = read_es("gov_10a_taxag")
    ind.append(("tax_total", "Total taxes and net social contributions (S13+S212, after D.995)", "% of GDP",
                "gov_10a_taxag", series(tax_d, na_item="D2_D5_D91_D61_M_D995"), False))
    ind.append(("tax_total_excl_imputed", "Taxes and actual compulsory social contributions (excl. imputed D.612 and households' voluntary D.614; closest to Insee 'prelevements obligatoires')",
                "% of GDP", "gov_10a_taxag", series(tax_d, na_item="D2_D5_D91_D61_M_D612_M_D614_M_D995"), False))
    ind.append(("tax_excl_ssc", "Taxes only (D.2+D.5+D.91, S13+S212)", "% of GDP", "gov_10a_taxag",
                series(tax_d, na_item="D2_D5_D91"), False))
    ind.append(("tax_ssc", "Net social contributions (D.61, S13+S212)", "% of GDP", "gov_10a_taxag",
                series(tax_d, na_item="D61"), False))
    exp_d, upd_exp = read_es("gov_10a_exp")
    for code, lab in [("TOTAL", "Total expenditure (COFOG total)")] + list(COFOG_DIV.items()) + list(COFOG_GRP.items()):
        ind.append((f"cofog_{code}", f"COFOG {code} {lab}", "% of GDP", "gov_10a_exp",
                    series(exp_d, unit="PC_GDP", cofog99=code), False))
        if code != "TOTAL":
            ind.append((f"cofogshare_{code}", f"COFOG {code} {lab}", "% of total GG expenditure", "gov_10a_exp",
                        series(exp_d, unit="PC_TOT", cofog99=code), False))
    spr_d, upd_spr = read_es("spr_exp_type")
    ind.append(("spr_total_gdp", "Social protection expenditure, total (ESSPROS, incl. admin)", "% of GDP",
                "spr_exp_type", series(spr_d, spdeps="TOTAL", unit="PC_GDP"), False))
    ind.append(("spr_total_pps", "Social protection expenditure, total (ESSPROS)", "PPS per inhabitant",
                "spr_exp_type", series(spr_d, spdeps="TOTAL", unit="PPS_HAB"), False))
    ind.append(("spr_benef_gdp", "Social protection benefits (ESSPROS)", "% of GDP",
                "spr_exp_type", series(spr_d, spdeps="SPR", unit="PC_GDP"), False))
    sprf_d, upd_sprf = read_es("spr_exp_func")
    for fn, lab in [("TOTAL", "Social protection benefits, all functions"), ("OLD", "Social benefits: old age function"),
                    ("SICK", "Social benefits: sickness/health care function")]:
        ind.append((f"sprf_{fn}_gdp", lab + " (ESSPROS, incl. 2025 early estimates)", "% of GDP", "spr_exp_func",
                    series(sprf_d, spfunc=fn, unit="PC_GDP"), False))
        ind.append((f"sprf_{fn}_pps", lab + " (ESSPROS)", "PPS per inhabitant", "spr_exp_func",
                    series(sprf_d, spfunc=fn, unit="PPS_HAB"), False))
    pc_d, upd_pc = read_es("nama_10_pc")
    gdp_pps = series(pc_d, na_item="B1GQ")
    ind.append(("gdp_pc_pps", "GDP per capita", "PPS (EU27_2020) per inhabitant", "nama_10_pc", gdp_pps, False))
    ind.append(("p3s13_pc_pps", "Government final consumption expenditure per capita", "PPS per inhabitant",
                "nama_10_pc", series(pc_d, na_item="P3_S13"), False))
    # derived: expenditure in PPS per inhabitant = (% GDP / 100) x GDP per capita in PPS
    def derived(src):
        out = {}
        for c, ys in src.items():
            for y, (v, fl) in ys.items():
                if c in gdp_pps and y in gdp_pps[c]:
                    out.setdefault(c, {})[y] = (v / 100.0 * gdp_pps[c][y][0], fl)
        return out
    te_ser = series(main_d, unit="PC_GDP", na_item="TE")
    ind.append(("te_pc_pps", "Total GG expenditure per capita (TE % GDP x GDP per capita PPS)",
                "PPS per inhabitant (derived)", "gov_10a_main x nama_10_pc", derived(te_ser), False))
    for code in ["GF07", "GF09", "GF10", "GF1002", "GF02", "GF01"]:
        ind.append((f"cofogpps_{code}", f"COFOG {code} per capita (derived)", "PPS per inhabitant (derived)",
                    "gov_10a_exp x nama_10_pc", derived(series(exp_d, unit="PC_GDP", cofog99=code)), False))
    le_d, upd_le = read_es("demo_mlexpec")
    ind.append(("life_exp", "Life expectancy at birth", "years", "demo_mlexpec", series(le_d), False))
    ar_d, upd_ar = read_es("ilc_li02")
    ind.append(("arop_after", "At-risk-of-poverty rate after social transfers (60% median)", "% of population",
                "ilc_li02", series(ar_d), False))
    ab_d, upd_ab = read_es("ilc_li10")
    ind.append(("arop_before", "At-risk-of-poverty rate before social transfers (pensions counted as income)",
                "% of population", "ilc_li10", series(ab_d), False))
    gi_d, upd_gi = read_es("ilc_di12")
    ind.append(("gini", "Gini coefficient of equivalised disposable income", "index 0-100", "ilc_di12",
                series(gi_d), False))
    # derived: poverty reduction by social transfers (pp)
    pr = {}
    arop_a, arop_b = series(ar_d), series(ab_d)
    for c in arop_a:
        for y in arop_a[c]:
            if c in arop_b and y in arop_b[c]:
                pr.setdefault(c, {})[y] = (arop_b[c][y][0] - arop_a[c][y][0], "")
    ind.append(("arop_reduction", "Poverty reduction by social transfers excl. pensions (before - after)",
                "percentage points", "ilc_li10 - ilc_li02", pr, False))

    updates = {"gov_10a_main": upd_main, "gov_10dd_edpt1": upd_edp, "gov_10a_taxag": upd_tax,
               "gov_10a_exp": upd_exp, "spr_exp_type": upd_spr, "spr_exp_func": upd_sprf, "nama_10_pc": upd_pc,
               "demo_mlexpec": upd_le, "ilc_li02": upd_ar, "ilc_li10": upd_ab, "ilc_di12": upd_gi}

    # ---- outputs
    cols = ["indicator", "label", "unit", "dataset", "year_type", "year", "FR", "FR_flag", "EU27_agg", "EA21_agg",
            "EA20_agg", "EU27_mean", "EU27_median", "EU27_n", "EU27_rank", "EA21_mean", "EA21_median", "EA21_n",
            "EA21_rank", "PANEL_mean", "PANEL_median", "PANEL_n", "PANEL_rank", "PANEL_n_incl_FR"] + PANEL + [
            "gap_FR_minus_EA_agg", "gap_FR_minus_EU27_agg", "gap_FR_minus_EU27_mean", "top3_EU27", "missing_EU27"]
    long_rows = []
    with open(os.path.join(OUT, "09_intl_comparison_stats.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols)
        w.writeheader()
        for iid, lab, unit, ds, ser, inv in ind:
            ly = latest_year(ser)
            yrs = [("y2005", 2005), ("y2015", 2015), ("latest", ly)]
            if ly and ly - 1 >= 2016:
                yrs.append(("latest_minus_1", ly - 1))
            for yt, y in yrs:
                if y is None:
                    continue
                s = stats_for(ser, y, inv)
                if s is None:
                    continue
                row = {"indicator": iid, "label": lab, "unit": unit, "dataset": ds, "year_type": yt}
                row.update(s)
                w.writerow({k: (round(v, 3) if isinstance(v, float) else v) for k, v in row.items() if k in cols})
            for c, ys in ser.items():
                for y, (v, fl) in ys.items():
                    long_rows.append((iid, unit, ds, c, y, v, fl))
    with open(os.path.join(OUT, "09_intl_long_eurostat.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["indicator", "unit", "dataset", "geo", "year", "value", "flag"])
        w.writerows(sorted(long_rows))
    # France gap time series 1995-latest for headline indicators
    with open(os.path.join(OUT, "09_intl_fr_gap_timeseries.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["indicator", "year", "FR", "EA21_agg", "EU27_agg", "EU27_mean", "PANEL_mean",
                    "FR_minus_EA21_agg", "FR_minus_EU27_mean"])
        for iid, lab, unit, ds, ser, inv in ind:
            if iid not in ("main_TE", "main_TR", "edp_B9", "edp_GD", "tax_total", "cofog_GF10", "cofog_GF1002",
                           "cofog_GF07", "cofog_GF09", "main_D1PAY", "spr_benef_gdp", "te_pc_pps"):
                continue
            for y in sorted(ser.get("FR", {})):
                s = stats_for(ser, y, inv)
                if not s or s["EU27_n"] < 20:
                    continue
                ea = s["EA21_agg"]
                w.writerow([iid, y, s["FR"], ea, s["EU27_agg"], round(s["EU27_mean"], 3),
                            round(s["PANEL_mean"], 3) if s["PANEL_mean"] is not None else "",
                            round(s["FR"] - ea, 3) if ea is not None else "", round(s["FR"] - s["EU27_mean"], 3)])
    # per-country table, latest year, headline indicators
    with open(os.path.join(OUT, "09_intl_country_values_latest.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        heads = [i for i in ind if i[0] in ("main_TE", "main_TR", "edp_B9", "edp_GD", "tax_total", "cofog_GF10",
                                            "cofog_GF1002", "cofog_GF07", "cofog_GF09", "cofog_GF02", "cofog_GF0107",
                                            "main_D1PAY", "spr_total_gdp", "spr_total_pps", "te_pc_pps", "gdp_pc_pps")]
        w.writerow(["geo"] + [f"{i[0]} ({latest_year(i[4])})" for i in heads])
        for c in EU27 + AGGS:
            w.writerow([c] + [i[4].get(c, {}).get(latest_year(i[4]), ("", ""))[0] for i in heads])
    with open(os.path.join(OUT, "09_intl_eurostat_last_updates.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["dataset", "last_update_values_dd/mm/yy"])
        for k, v in updates.items():
            w.writerow([k, " | ".join(v)])

    # ---- OECD
    def read_oecd(stem, measure_col="MEASURE"):
        with open(os.path.join(RAW_OECD, stem + ".csv"), encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        out = {}
        for r in rows:
            if not r["OBS_VALUE"]:
                continue
            out.setdefault(r[measure_col], {}).setdefault(r["REF_AREA"], {})[int(r["TIME_PERIOD"])] = float(r["OBS_VALUE"])
        return out
    rs = read_oecd("oecd_revenue_statistics_total_tax_pc_gdp")["TAX_REV"]
    naag = read_oecd("oecd_naag_general_government_pc_gdp")
    with open(os.path.join(OUT, "09_intl_oecd_stats.csv"), "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        w.writerow(["indicator", "year", "FRA", "OECD_mean_computed", "OECD_median", "n", "FRA_rank", "OECD_REP_published",
                    "top5", "missing"])
        def emit(name, ser, years, pub=None):
            for y in years:
                vals = {c: ser[c][y] for c in OECD38 if c in ser and y in ser[c]}
                if "FRA" not in vals:
                    continue
                top = sorted(vals.items(), key=lambda kv: -kv[1])[:5]
                w.writerow([name, y, round(vals["FRA"], 2), round(statistics.mean(vals.values()), 2),
                            round(statistics.median(vals.values()), 2), len(vals), rank_desc(vals.values(), vals["FRA"]),
                            round(pub[y], 2) if pub and y in pub else "",
                            "; ".join(f"{c} {v:.1f}" for c, v in top),
                            " ".join(c for c in OECD38 if c not in vals)])
        rs_years = sorted({y for c in rs for y in rs[c]})
        emit("total_tax_revenue_pc_gdp", rs, [y for y in rs_years if y in (2005, 2015) or y >= 2019],
             rs.get("OECD_REP"))
        for m, name in [("OTES13", "gg_total_expenditure_pc_gdp"), ("OTRS13", "gg_total_revenue_pc_gdp"),
                        ("B9S13", "gg_net_lending_pc_gdp"), ("LES13_FD4", "gg_gross_debt_pc_gdp"),
                        ("D1S13", "gg_compensation_employees_pc_gdp")]:
            if m in naag:
                ys = sorted({y for c in naag[m] for y in naag[m][c]})
                emit(name, naag[m], [y for y in ys if y in (2005, 2015) or y >= 2019])
    print("done")


if __name__ == "__main__":
    main()
