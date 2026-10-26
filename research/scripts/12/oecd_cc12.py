"""OECD cancer 5-year net survival (CONCORD programme via OECD HCQO DF_CC). python3 -I oecd_cc12.py"""
import csv, statistics, shutil
R='research/data/raw/12/oecd/'
OUT='research/data/'
for f,n in (('waiting.csv','12_oecd_waiting_times_raw.csv'),('am.csv','12_oecd_avoidable_mortality_raw.csv'),('cc.csv','12_oecd_cancer_survival_raw.csv')):
    shutil.copy(R+f, OUT+n)
OECD38=['AUS','AUT','BEL','CAN','CHL','COL','CRI','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','ISL','IRL','ISR','ITA','JPN','KOR','LVA','LTU','LUX','MEX','NLD','NZL','NOR','POL','PRT','SVK','SVN','ESP','SWE','CHE','TUR','GBR','USA']
PANEL=['FRA','DEU','ITA','ESP','NLD','BEL','SWE','DNK']
d={}
for r in csv.DictReader(open(R+'cc.csv')):
    if r['STATISTICAL_OPERATION']=='OBS' and r['OBS_VALUE']:
        sex='F' if r['MEASURE'] in ('CCBRNTSR','CCCVNTSR') else '_T'
        if r['SEX']==sex: d[(r['MEASURE'],r['REF_AREA'],r['TIME_PERIOD'])]=float(r['OBS_VALUE'])
names={'CCBRNTSR':'Breast (women)','CCCLNTSR':'Colon','CCRTNTSR':'Rectum','CCLUNTSR':'Lung','CCSTNTSR':'Stomach','CCCVNTSR':'Cervix','CCLKNTSR':'Childhood acute lymphoblastic leukaemia (0-14)'}
w=csv.writer(open(OUT+'12_oecd_cancer_survival_stats.csv','w',newline=''))
w.writerow(['cancer','period_end','group','n','FR','mean','median','FR_rank(1=highest)','DEU','ITA','ESP','NLD','BEL','SWE','DNK'])
for m,nm in names.items():
    for y in ('2004','2009','2014'):
        for gn,g in (('OECD38',OECD38),('Panel8',PANEL)):
            v={c:d[(m,c,y)] for c in g if (m,c,y) in d}
            if 'FRA' not in v: continue
            s=sorted(v.values(),reverse=True)
            row=[nm,y,gn,len(v),v['FRA'],round(statistics.mean(v.values()),1),statistics.median(v.values()),s.index(v['FRA'])+1]+[v.get(c,'') for c in PANEL[1:]]
            w.writerow(row)
            if y=='2014': print(row)
