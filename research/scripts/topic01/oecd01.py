import csv, statistics as st
R='research/data/raw/oecd_01/'
gdp={}
for r in csv.DictReader(open(R+'oecd_gdp.csv')):
    if r['OBS_VALUE']: gdp[(r['REF_AREA'],int(r['TIME_PERIOD']))]=float(r['OBS_VALUE'])*10**int(r['UNIT_MULT'] or 0)
ex={}
for r in csv.DictReader(open(R+'oecd_t11_ote.csv')):
    if r['OBS_VALUE']: ex[(r['REF_AREA'],r['EXPENDITURE'],int(r['TIME_PERIOD']))]=float(r['OBS_VALUE'])*10**int(r['UNIT_MULT'] or 0)
OECD=['AUS','AUT','BEL','CAN','CHL','COL','CRI','CZE','DNK','EST','FIN','FRA','DEU','GRC','HUN','ISL','IRL','ISR','ITA','JPN','KOR','LVA','LTU','LUX','MEX','NLD','NZL','NOR','POL','PRT','SVK','SVN','ESP','SWE','CHE','TUR','GBR','USA']
out=csv.writer(open('research/data/01_oecd_cofog_pcgdp_derived.csv','w'))
out.writerow(['country','cofog','year','pct_gdp'])
for y in [2005,2015,2019,2022,2023,2024]:
    for f in ['_T','GF10','GF1002','GF07','GF09','GF02','GF01']:
        vals={c:100*ex[(c,f,y)]/gdp[(c,y)] for c in OECD if (c,f,y) in ex and (c,y) in gdp}
        for c,v in vals.items(): out.writerow([c,f,y,round(v,2)])
        if not vals: continue
        srt=[c for c,_ in sorted(vals.items(), key=lambda kv:-kv[1])]
        print(y,f,'n',len(vals),'mean',round(st.mean(vals.values()),1),'median',round(st.median(vals.values()),1),'FR',round(vals.get('FRA',float('nan')),1),'rank',srt.index('FRA')+1 if 'FRA' in vals else None,
              'top5',[(c,round(vals[c],1)) for c in srt[:5]], 'USA',round(vals.get('USA',float('nan')),1),'JPN',round(vals.get('JPN',float('nan')),1),'GBR',round(vals.get('GBR',float('nan')),1))
        missing=[c for c in OECD if c not in vals]
        if f=='_T': print('   missing',missing)
