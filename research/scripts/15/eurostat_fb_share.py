import json, sys, statistics, csv
d = json.load(open(sys.argv[1])); out = sys.argv[2]
dims, size = d['id'], d['size']; idx = {k: d['dimension'][k]['category']['index'] for k in dims}
def get(**kw):
    pos = 0
    for k, s in zip(dims, size):
        pos = pos * s + (idx[k][kw[k]] if k in kw else 0)
    return d['value'].get(str(pos))
EU27 = "BE BG CZ DK DE EE IE EL ES FR HR IT CY LV LT LU HU MT NL AT PL PT RO SI SK FI SE".split()
EA21 = "BE DE EE IE EL ES FR HR IT CY LV LT LU MT NL AT PT SI SK FI BG".split()
PANEL = "FR DE IT ES NL BE SE DK".split()
rows = []
for yr in ("2024", "2025"):
    sh = {}
    for g in EU27 + ["EU27_2020"]:
        f, t = get(c_birth="FOR", geo=g, time=yr), get(c_birth="TOTAL", geo=g, time=yr)
        if f and t: sh[g] = 100 * f / t
    for name, grp in (("EU27", EU27), ("EA21", EA21), ("panel", PANEL)):
        v = [sh[g] for g in grp if g in sh]
        rank = sorted(v, reverse=True).index(sh["FR"]) + 1
        rows.append([yr, name, len(v), round(sh["FR"], 1), round(statistics.mean(v), 1), round(statistics.median(v), 1), f"{rank}/{len(v)} (1 = highest share)", round(sh.get("EU27_2020", float('nan')), 1) if name == "EU27" else ""])
    rows.append([yr, "panel values", "", "; ".join(f"{g} {sh[g]:.1f}" for g in PANEL if g in sh), "", "", "", ""])
with open(out, "w", newline="") as fh:
    w = csv.writer(fh); w.writerow(["year", "group", "n", "France_%", "mean_unweighted", "median", "France_rank", "EU27_aggregate"]); w.writerows(rows)
for r in rows: print(r)
