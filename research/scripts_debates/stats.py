import csv, sys, statistics, collections
EU27 = "AT BE BG CY CZ DE DK EE EL ES FI FR HR HU IE IT LT LU LV MT NL PL PT RO SE SI SK".split()
EA = "AT BE CY DE EE EL ES FI FR HR IE IT LT LU LV MT NL PT SI SK BG".split()  # BG joined euro area 1 Jan 2026
EA20 = [c for c in EA if c != 'BG']
PANEL = "FR DE IT ES NL BE SE DK".split()
def load(path, filt=None):
    data = collections.defaultdict(dict)
    for r in csv.DictReader(open(path)):
        if filt and not all(r.get(k)==v for k,v in filt.items()): continue
        data[r['time']][r['geo']] = float(r['value'])
    return data
def summ(data, year, group, name, higher_is_rank1=True):
    vals = {g: data[year][g] for g in group if g in data.get(year, {})}
    if 'FR' not in vals: return f"{name} {year}: FR missing"
    s = sorted(vals.items(), key=lambda x: -x[1] if higher_is_rank1 else x[1])
    rank = [g for g,_ in s].index('FR')+1
    return f"{name} {year}: n={len(vals)} mean={statistics.mean(vals.values()):.1f} median={statistics.median(vals.values()):.1f} FR={vals['FR']:.1f} rank={rank}/{len(vals)} (1=highest)"
if __name__ == '__main__':
    path = sys.argv[1]; years = sys.argv[2].split(','); filt = dict(a.split('=') for a in sys.argv[3:])
    d = load(path, filt)
    for y in years:
        print(f"[{y}] aggregates: EU27_2020={d[y].get('EU27_2020')} EA={d[y].get('EA20', d[y].get('EA21'))}")
        for grp,n in [(EU27,'EU27'),(EA20,'EA20'),(PANEL,'Panel')]:
            print('  ', summ(d, y, grp, n))
        print('   panel:', {g: d[y].get(g) for g in PANEL})
