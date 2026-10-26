"""OECD avoidable mortality (DSD_HEALTH_STAT@DF_AM), age-standardised per 100k: France vs OECD-38/EU/panel. python3 -I oecd_am12.py"""
import csv, statistics
R='research/data/raw/12/oecd/am.csv'
OECD38=['AUS','AUT','BEL','CAN','CHL','COL','CRI','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','ISL','IRL','ISR','ITA','JPN','KOR','LVA','LTU','LUX','MEX','NLD','NZL','NOR','POL','PRT','SVK','SVN','ESP','SWE','CHE','TUR','GBR','USA']
EU_IN_OECD=['AUT','BEL','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','IRL','ITA','LVA','LTU','LUX','NLD','POL','PRT','SVK','SVN','ESP','SWE']
PANEL=['FRA','DEU','ITA','ESP','NLD','BEL','SWE','DNK']
d={}
for r in csv.DictReader(open(R)):
    if r['UNIT_MEASURE']=='DT_10P5HB' and r['SEX']=='_T' and r['OBS_VALUE']:
        d[(r['MEASURE'],r['REF_AREA'],r['TIME_PERIOD'])]=float(r['OBS_VALUE'])
w=csv.writer(open('research/data/12_oecd_avoidable_mortality_stats.csv','w',newline=''))
w.writerow(['measure','year','group','n','FR','mean','median','FR_rank(1=lowest)','DEU','ITA','ESP','NLD','BEL','SWE','DNK'])
for m in ('TRTM','PREVM','AVM'):
    for y in ('2005','2015','2019','2021','2022','2023'):
        for gn,g in (('OECD38',OECD38),('EU22_in_OECD',EU_IN_OECD),('Panel8',PANEL)):
            v={c:d[(m,c,y)] for c in g if (m,c,y) in d}
            if 'FRA' not in v: continue
            s=sorted(v.values()); row=[m,y,gn,len(v),v['FRA'],round(statistics.mean(v.values()),1),statistics.median(v.values()),s.index(v['FRA'])+1]+[v.get(c,'') for c in PANEL[1:]]
            w.writerow(row); print(row)
