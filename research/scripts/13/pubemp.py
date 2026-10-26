"""Part 1: general-government employment share 2000-2024 (ILO national-accounts/admin series
over national-accounts total employment) + Eurostat NACE O+P+Q proxy.
Usage: python3 -I pubemp.py <research_dir>"""
import csv, sys, statistics as st
R = sys.argv[1]
raw = R + '/data/raw/13/'
I2 = {'AUT':'AT','BEL':'BE','BGR':'BG','HRV':'HR','CYP':'CY','CZE':'CZ','DNK':'DK','EST':'EE','FIN':'FI','FRA':'FR',
      'DEU':'DE','GRC':'EL','HUN':'HU','IRL':'IE','ITA':'IT','LVA':'LV','LTU':'LT','LUX':'LU','MLT':'MT','NLD':'NL',
      'POL':'PL','PRT':'PT','ROU':'RO','SVK':'SK','SVN':'SI','ESP':'ES','SWE':'SE','NOR':'NO','CHE':'CH','ISL':'IS'}
EU = ['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','EL','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE']
OECD = ['AUS','AUT','BEL','CAN','CHL','COL','CRI','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','ISL','IRL','ISR','ITA','JPN',
        'KOR','LVA','LTU','LUX','MEX','NLD','NZL','NOR','POL','PRT','SVK','SVN','ESP','SWE','CHE','TUR','GBR','USA']
PANEL = ['FR','DE','IT','ES','NL','BE','SE','DK']
def key(c):  # unify to 2-letter for Europe, ISO3 otherwise
    return I2.get(c, c)
# Eurostat employment
es = {}
for r in csv.DictReader(open(R + '/data/13_eurostat_nama_10_a64_e_OPQ.csv')):
    es.setdefault((r['geo'], r['nace_r2']), {})[int(r['time'])] = float(r['value'])
# ILO modelled total employment (fallback denominators outside Europe)
ilotot = {}
for r in csv.DictReader(open(raw + 'ilo_DF_EMP_2EMP_SEX_AGE_NB.csv')):
    ilotot.setdefault(key(r['REF_AREA']), {})[int(r['TIME_PERIOD'])] = float(r['OBS_VALUE'])
gg, src = {}, {}
for r in csv.DictReader(open(raw + 'ilo_DF_EMP_XPSE_GOV_NB.csv')):
    if r['GOV'] != 'GOV_LVL_GG' or not r['TIME_PERIOD'].isdigit():
        continue
    k = key(r['REF_AREA'])
    gg.setdefault(k, {})[int(r['TIME_PERIOD'])] = float(r['OBS_VALUE'])
    src.setdefault(k, set()).add(r['SOURCE'])
rows = []
share = {}
for k, ser in gg.items():
    for y, v in ser.items():
        den = es.get((k, 'TOTAL'), {}).get(y)
        dsrc = 'Eurostat nama_10_a64_e EMP_DC'
        if den is None:
            den = ilotot.get(k, {}).get(y); dsrc = 'ILO modelled estimates (EMP_2EMP, 15+)'
        if den:
            s = 100 * v / den
            share.setdefault(k, {})[y] = s
            rows.append([k, y, round(v, 1), round(den, 1), round(s, 2), dsrc, '; '.join(sorted(src[k]))])
with open(R + '/data/13_gg_employment_share_ilo_2000_2024.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['geo', 'year', 'gg_employment_ths', 'total_employment_ths', 'gg_share_pct', 'denominator_source', 'numerator_source_ILO'])
    w.writerows(sorted(rows))
# OPQ proxy
opq = {}
for g in set(k[0] for k in es):
    t = es.get((g, 'TOTAL'), {}); o = es.get((g, 'O-Q'), {})
    for y in t:
        if y in o and t[y]:
            opq.setdefault(g, {})[y] = 100 * o[y] / t[y]
with open(R + '/data/13_eurostat_OPQ_share_2000_2025.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['geo', 'year', 'O', 'P', 'Q', 'O_Q', 'TOTAL', 'OPQ_share_pct'])
    for g in sorted(opq):
        for y in sorted(opq[g]):
            w.writerow([g, y] + [es.get((g, n), {}).get(y, '') for n in ('O', 'P', 'Q', 'O-Q', 'TOTAL')] + [round(opq[g][y], 2)])
EXCL = {'CAN', 'ISR', 'PL', 'MEX', 'CRI', 'IE', 'HR'}  # ILO GG series >1 pt away from OECD GaaG 2021/2025 -> excluded from GG stats
def stats(data, members, y, fr='FR', excl=()):
    vals = {c: data[c][y] for c in members if c in data and y in data[c] and c not in excl}
    if fr not in vals or len(vals) < 3:
        return None
    srt = sorted(vals.values(), reverse=True)
    return dict(n=len(vals), mean=st.mean(vals.values()), median=st.median(vals.values()),
                fr=vals[fr], rank=srt.index(vals[fr]) + 1, missing=[c for c in members if c not in vals])
out = []
OE = [key(c) for c in OECD]
for label, data in [('GG_share_ILO', share), ('OPQ_share_Eurostat', opq)]:
    for gname, mem in [('EU27', EU), ('OECD38', OE), ('Panel8', PANEL)]:
        for y in range(2000, 2026):
            s = stats(data, mem, y, excl=EXCL if label == 'GG_share_ILO' else ())
            if s:
                out.append([label, gname, y, s['n'], round(s['mean'], 2), round(s['median'], 2), round(s['fr'], 2), s['rank'],
                            round(s['fr'] - s['mean'], 2), round(s['fr'] - s['median'], 2), ' '.join(s['missing'])])
with open(R + '/data/13_public_employment_stats.csv', 'w', newline='') as f:
    w = csv.writer(f); w.writerow(['indicator', 'group', 'year', 'n', 'mean', 'median', 'france', 'fr_rank_1_highest', 'fr_minus_mean', 'fr_minus_median', 'missing'])
    w.writerows(out)
for r in out:
    if r[2] in (2000, 2005, 2010, 2015, 2019, 2022, 2023, 2024, 2025):
        print(r[:10], 'missing:', r[10][:80])
print('\nPanel GG share:')
for c in PANEL + ['NO', 'FI', 'USA', 'GBR', 'JPN']:
    print(c, {y: round(share.get(c, {}).get(y, float('nan')), 1) for y in (2000, 2005, 2010, 2015, 2019, 2023, 2024)})
print('\nPanel OPQ share:')
for c in PANEL + ['EU27_2020']:
    print(c, {y: round(opq.get(c, {}).get(y, float('nan')), 1) for y in (2000, 2005, 2010, 2015, 2019, 2023, 2024, 2025)})
