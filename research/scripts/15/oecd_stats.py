import sys, csv, statistics, openpyxl
raw = sys.argv[1]; out = sys.argv[2]
def load(fn, sheet_first_rows, ncols):
    wb = openpyxl.load_workbook(f"{raw}/{fn}", data_only=True, read_only=True)
    ws = wb.worksheets[0]; d = {}
    for row in ws.iter_rows(values_only=True):
        if row[0] and isinstance(row[0], str) and len(row[0]) == 3 and row[0].isupper() and isinstance(row[1], (int, float)):
            if row[0] not in d: d[row[0]] = list(row[1:1+ncols])
    return d
t41 = load("1jovf5.xlsx", 0, 7)   # FB A, FB B/C1, FB C2, NB A, NB B, NB C1, NB C2
a43 = load("riasgf.xlsx", 0, 4)   # FB: no PPG, PPG ex def&debt, PPG ex debt, all PPG
a44 = load("d7pb0g.xlsx", 0, 4)   # per capita / GDP pc: FB A, FB C2, NB A, NB C2
EU27 = "AUT BEL CZE DEU DNK ESP EST FIN FRA GRC IRL ITA LTU LUX LVA NLD PRT SVN SWE".split()
EA = "AUT BEL DEU ESP EST FIN FRA GRC IRL ITA LTU LUX LVA NLD PRT SVN".split()
PANEL = "FRA DEU ITA ESP NLD BEL SWE DNK".split()
OECD = sorted(t41)
measures = {
 "FB_A_items_individual_pctGDP": {k: v[0] for k, v in t41.items()},
 "FB_B_congestible_pctGDP": {k: v[1] for k, v in t41.items()},
 "FB_C2_all_public_goods_pctGDP": {k: v[2] for k, v in t41.items()},
 "NB_C2_all_public_goods_pctGDP": {k: v[6] for k, v in t41.items()},
 "FB_ex_defence_debt_pctGDP": {k: v[1] for k, v in a43.items()},
 "FB_ex_debt_pctGDP": {k: v[2] for k, v in a43.items()},
 "FBminusNB_percap_C2_pctGDPpc": {k: v[1]-v[3] for k, v in a44.items()},
 "FB_percap_C2_pctGDPpc": {k: v[1] for k, v in a44.items()},
}
rows = []
for m, d in measures.items():
    for gname, g in (("OECD25", OECD), ("EU27_members_in_sample", EU27), ("euro_area_in_sample", EA), ("panel_FR+7", PANEL)):
        vals = [d[c] for c in g]
        rank = sorted(vals, reverse=True).index(d["FRA"]) + 1
        rows.append([m, gname, len(vals), round(d["FRA"], 3), round(statistics.mean(vals), 3), round(statistics.median(vals), 3), f"{rank}/{len(vals)} (1 = most favorable)"])
    rows.append([m, "panel values", "", "; ".join(f"{c} {d[c]:.2f}" for c in PANEL), "", "", ""])
with open(out, "w", newline="") as f:
    w = csv.writer(f); w.writerow(["measure", "group", "n", "France", "mean_unweighted", "median", "France_rank"]); w.writerows(rows)
for r in rows: print(r)
