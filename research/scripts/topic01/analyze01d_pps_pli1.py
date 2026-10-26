# Recompute file 01 §6.4 (PPS per capita by COFOG function) on the current
# Eurostat PLI vintage prc_ppp_ind_1 (API "updated" 2026-07-09), replacing the
# superseded prc_ppp_ind (July 2025) used by analyze01c.py.
# Method: EUR value / (PLI_EU27_2020 for GDP / 100) / population.
# Inputs (all already in research/data):
#   01_eurostat_gov_10a_exp_mioeur.csv      COFOG, MIO_EUR, S13, TE
#   13_eurostat_prc_ppp_ind_1_PLI_GDP.csv   prc_ppp_ind_1, PLI_EU27_2020, ppp_cat18=GDP
#   01_eurostat_nama_10_pe.csv              POP_NC, THS_PER
# Output: data/01_derived_cofog_pps_pc_pli1.csv
import csv, statistics as st
D = 'research/data/'
C = {}
for r in csv.DictReader(open(D + '01_eurostat_gov_10a_exp_mioeur.csv')):
    if r['na_item'] == 'TE' and r['sector'] == 'S13' and r['value']:
        C[(r['cofog99'], r['geo'], int(r['time']))] = float(r['value'])
pli = {}
for r in csv.DictReader(open(D + '13_eurostat_prc_ppp_ind_1_PLI_GDP.csv')):
    if r['indic_ppp'] == 'PLI_EU27_2020' and r['ppp_cat18'] == 'GDP' and r['value']:
        pli[(r['geo'], int(r['time']))] = float(r['value'])
pop = {(r['geo'], int(r['time'])): float(r['value'])
       for r in csv.DictReader(open(D + '01_eurostat_nama_10_pe.csv')) if r['value']}
EU27 = ['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT',
        'LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK']
PANEL = ['DE','IT','ES','NL','BE','SE','DK']
NAMES = {'TOTAL': 'Total expenditure', 'GF10': 'Social protection', 'GF1002': 'Old age',
         'GF07': 'Health', 'GF09': 'Education', 'GF01': 'General public services',
         'GF04': 'Economic affairs', 'GF02': 'Defense', 'GF03': 'Public order and safety',
         'GF06': 'Housing and community amenities'}


def pps(k, g, y):
    v, p, n = C.get((k, g, y)), pli.get((g, y)), pop.get((g, y))
    return None if None in (v, p, n) else v * 1e6 / (p / 100) / (n * 1e3)


def table(k, y):
    pv = {g: pps(k, g, y) for g in EU27 if pps(k, g, y) is not None}
    srt = [g for g, _ in sorted(pv.items(), key=lambda kv: -kv[1])]
    return pv, srt


out = open(D + '01_derived_cofog_pps_pc_pli1.csv', 'w', newline='')
w = csv.writer(out)
w.writerow(['year', 'cofog', 'label', 'FR_PPS_pc', 'EU27_unweighted_mean', 'EU27_median',
            'FR_rank', 'n_countries'] + [p + '_PPS' for p in PANEL] + ['pli_source'])
for y in [2024]:
    for k, lab in NAMES.items():
        pv, srt = table(k, y)
        row = [y, k, lab, round(pv['FR']), round(st.mean(pv.values())), round(st.median(pv.values())),
               srt.index('FR') + 1, len(pv)] + [round(pv[g]) for g in PANEL] + ['prc_ppp_ind_1 (2026-07-09)']
        w.writerow(row)
        print(row)
print('TOTAL history (gov_10a_exp TOTAL, prc_ppp_ind_1):')
for y in [2005, 2010, 2015, 2019, 2024]:
    pv, srt = table('TOTAL', y)
    row = [y, 'TOTAL', 'Total expenditure (history)', round(pv['FR']), round(st.mean(pv.values())),
           round(st.median(pv.values())), srt.index('FR') + 1, len(pv)] + \
          [round(pv[g]) if g in pv else '' for g in PANEL] + ['prc_ppp_ind_1 (2026-07-09)']
    if y != 2024:
        w.writerow(row)
    print(row, 'above FR:', srt[:srt.index('FR')])
out.close()
