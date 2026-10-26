"""WHO GHED current health expenditure (% GDP) 2000-2023: France vs EU27, EA21, OECD38, panel. python3 -I who12.py"""
import json, csv, statistics
D='research/data/raw/12/who/'
EU27=['BEL','BGR','CZE','DNK','DEU','EST','IRL','GRC','ESP','FRA','HRV','ITA','CYP','LVA','LTU','LUX','HUN','MLT','NLD','AUT','POL','PRT','ROU','SVN','SVK','FIN','SWE']
EA21=['BEL','BGR','DEU','EST','IRL','GRC','ESP','FRA','HRV','ITA','CYP','LVA','LTU','LUX','MLT','NLD','AUT','PRT','SVN','SVK','FIN']
OECD38=['AUS','AUT','BEL','CAN','CHL','COL','CRI','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','ISL','IRL','ISR','ITA','JPN','KOR','LVA','LTU','LUX','MEX','NLD','NZL','NOR','POL','PRT','SVK','SVN','ESP','SWE','CHE','TUR','GBR','USA']
PANEL=['FRA','DEU','ITA','ESP','NLD','BEL','SWE','DNK']
out=csv.writer(open('research/data/12_who_ghed_che_stats.csv','w',newline=''))
out.writerow(['indicator','year','FR','group','n','mean','median','FR_rank(1=highest)','FR_minus_mean','DEU','ITA','ESP','NLD','BEL','SWE','DNK','USA','CHE','GBR'])
raw=csv.writer(open('research/data/12_who_ghed_raw.csv','w',newline='')); raw.writerow(['indicator','iso3','year','value'])
for ind in ['GHED_CHEGDP_SHA2011','GHED_GGHE-DGDP_SHA2011','GHED_GGHE-DCHE_SHA2011','GHED_OOPSCHE_SHA2011'] if False else ['GHED_CHEGDP_SHA2011','GHED_GGHE-DGDP_SHA2011','GHED_GGHE-DCHE_SHA2011']:
    d={}
    for r in json.load(open(D+ind+'.json'))['value']:
        if r['SpatialDimType']=='COUNTRY' and r['NumericValue'] is not None:
            d[(r['SpatialDim'],r['TimeDim'])]=r['NumericValue']
            if r['SpatialDim'] in OECD38+EU27: raw.writerow([ind,r['SpatialDim'],r['TimeDim'],r['NumericValue']])
    for y in (2005,2010,2015,2019,2022,2023):
        for gname,g in (('EU27',EU27),('EA21',EA21),('OECD38',OECD38),('Panel8',PANEL)):
            v={c:d[(c,y)] for c in g if (c,y) in d}
            if 'FRA' not in v: continue
            s=sorted(v.values(),reverse=True)
            out.writerow([ind,y,round(v['FRA'],2),gname,len(v),round(statistics.mean(v.values()),2),round(statistics.median(v.values()),2),s.index(v['FRA'])+1,round(v['FRA']-statistics.mean(v.values()),2)]+[round(d.get((c,y),float('nan')),2) for c in ['DEU','ITA','ESP','NLD','BEL','SWE','DNK','USA','CHE','GBR']])
print('ok')
