import csv, sys, statistics as st
from collections import defaultdict
f = sys.argv[1]; items = sys.argv[2].split(','); years = [int(y) for y in sys.argv[3].split(',')]
D = defaultdict(dict)
for r in csv.DictReader(open(f)):
    D[(r['na_item'], int(r['time']))][r['geo']] = float(r['value'])
EU27 = "AT BE BG CY CZ DE DK EE EL ES FI FR HR HU IE IT LT LU LV MT NL PL PT RO SE SI SK".split()
EA20 = "AT BE CY DE EE EL ES FI FR HR IE IT LT LU LV MT NL PT SI SK".split()
PANEL = "FR DE IT ES NL BE SE DK".split()
for it in items:
  for y in years:
    d = D.get((it,y),{})
    out=[f"{it} {y}: FR={d.get('FR')} EU27agg={d.get('EU27_2020')} EA20agg={d.get('EA20')}"]
    for name,g in [("EU27",EU27),("EA20",EA20),("PANEL",PANEL)]:
        vals = {c:d[c] for c in g if c in d}
        if not vals or 'FR' not in vals: out.append(f" {name}: n={len(vals)} FR missing"); continue
        rank = sorted(vals.values(), reverse=True).index(vals['FR'])+1
        out.append(f" {name}(n={len(vals)}): mean={st.mean(vals.values()):.1f} median={st.median(vals.values()):.1f} FRrank={rank}")
    if 'PANEL' in sys.argv[4:] : out.append(" panel:"+" ".join(f"{c}={d.get(c)}" for c in PANEL))
    print(" |".join(out))
