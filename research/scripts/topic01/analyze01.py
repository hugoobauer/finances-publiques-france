import csv, statistics as st, collections, sys
D='research/data/'
def load(f):
    return list(csv.DictReader(open(D+f)))
main=load('01_eurostat_gov_10a_main.csv')
M={}
for r in main:
    M[(r['unit'],r['sector'],r['na_item'],r['geo'],r['time'])]=(float(r['value']),r['flag'])
def g(u,s,i,geo,t):
    v=M.get((u,s,i,geo,str(t))); return v[0] if v else None
print("== FR series S13 ==")
print("year TE_bn TE%GDP TR_bn TR% B9_bn B9%")
for y in range(1995,2026):
    print(y, *[ (round(g(u,'S13',i,'FR',y)/1000,1) if u=='MIO_EUR' else g(u,'S13',i,'FR',y)) for i in ['TE','TR','B9'] for u in ['MIO_EUR','PC_GDP']])
print("== EU/EA TE%GDP ==")
for y in [1995,2000,2005,2007,2010,2015,2019,2020,2022,2023,2024,2025]:
    print(y,'FR',g('PC_GDP','S13','TE','FR',y),'EU27',g('PC_GDP','S13','TE','EU27_2020',y),'EA20',g('PC_GDP','S13','TE','EA20',y),
      'gapEA', None if g('PC_GDP','S13','TE','EA20',y) is None else round(g('PC_GDP','S13','TE','FR',y)-g('PC_GDP','S13','TE','EA20',y),1))
EU27=['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK']
EA20=['AT','BE','CY','DE','EE','EL','ES','FI','FR','HR','IE','IT','LT','LU','LV','MT','NL','PT','SI','SK']
PANEL=['FR','DE','IT','ES','NL','BE','SE','DK']
def stats(vals,geo='FR'):
    xs=[v for v in vals.values() if v is not None]
    srt=sorted(vals.items(), key=lambda kv:-kv[1])
    rank=[k for k,_ in srt].index(geo)+1 if geo in vals else None
    return round(st.mean(xs),1), round(st.median(xs),1), rank, len(xs)
print("== TE %GDP cross-country stats (unweighted) ==")
for y in [2005,2010,2015,2019,2024,2025]:
    for name,grp in [('EU27',EU27),('EA20',EA20)]:
        vals={c:g('PC_GDP','S13','TE',c,y) for c in grp if g('PC_GDP','S13','TE',c,y) is not None}
        print(y,name,'mean,median,FRrank,n',stats(vals), 'max', max(vals.items(), key=lambda kv:kv[1]))
print("2025 panel TE%:", {c:g('PC_GDP','S13','TE',c,2025) for c in PANEL})
print("2025 panel TR%:", {c:g('PC_GDP','S13','TR',c,2025) for c in PANEL})
print("2025 panel B9%:", {c:g('PC_GDP','S13','B9',c,2025) for c in PANEL})
print("2025 ranking all EU27:", sorted([(c,g('PC_GDP','S13','TE',c,2025)) for c in EU27], key=lambda kv:-kv[1]))
# economic nature FR 2025 and EA
items=['D1PAY','P2','D62PAY','D632PAY','D3PAY','D41PAY','P51G','D7PAY','D9PAY','D29PAY','D8','OP5ANP']
print("== Economic nature, S13 ==")
for y in [1995,2005,2015,2024,2025]:
    print(y,'FR bn', {i:(round(g('MIO_EUR','S13',i,'FR',y)/1000,1) if g('MIO_EUR','S13',i,'FR',y) else None) for i in items})
    print(y,'FR %GDP', {i:g('PC_GDP','S13',i,'FR',y) for i in items})
    print(y,'EA20 %GDP', {i:g('PC_GDP','S13',i,'EA20',y) for i in items})
    print(y,'EU27 %GDP', {i:g('PC_GDP','S13',i,'EU27_2020',y) for i in items})
print("2025 panel econ nature %GDP")
for c in PANEL: print(c,{i:g('PC_GDP','S13',i,c,2025) for i in ['D1PAY','P2','D62PAY','D632PAY','D3PAY','D41PAY','P51G']})
print("== Subsectors FR (unconsolidated) ==")
for y in [1995,2005,2015,2024,2025]:
    for s in ['S1311','S1313','S1314','S13']:
        print(y,s,'TE bn',round(g('MIO_EUR',s,'TE','FR',y)/1000,1),'%GDP',g('PC_GDP',s,'TE','FR',y),'TR bn',round(g('MIO_EUR',s,'TR','FR',y)/1000,1),'B9 bn',round(g('MIO_EUR',s,'B9','FR',y)/1000,1), 'B9%',g('PC_GDP',s,'B9','FR',y))
for s in ['S1311','S1313','S1314']:
    print('2025',s,{i:(round(g('MIO_EUR',s,i,'FR',2025)/1000,1) if g('MIO_EUR',s,i,'FR',2025) is not None else None) for i in items})
