import sys, csv, statistics as st
sys.path.insert(0,sys.argv[1]); from js import load
D=sys.argv[2]
iso={'BGR':'BG','CYP':'CY','DNK':'DK','FRA':'FR','DEU':'DE','GRC':'EL','HUN':'HU','ITA':'IT','LVA':'LV','LTU':'LT','LUX':'LU','MLT':'MT','NLD':'NL','SVK':'SK','SVN':'SI','ESP':'ES','SWE':'SE','BEL':'BE','AUT':'AT','CZE':'CZ','EST':'EE','FIN':'FI','IRL':'IE','POL':'PL','PRT':'PT','ROU':'RO','HRV':'HR','NOR':'NO'}
gg={}; src={}
for r in csv.DictReader(open(D+'/ilo_gov.csv')):
    if r['GOV']=='GOV_LVL_GG' and r['REF_AREA'] in iso:
        gg[(iso[r['REF_AREA']],r['TIME_PERIOD'])]=float(r['OBS_VALUE']); src[(iso[r['REF_AREA']],r['TIME_PERIOD'])]=r['SOURCE']
_,a=load(D+'/a64e.json')
def sh(c,t):
    n=gg.get((c,t)); d=a.get(('A','THS_PER','TOTAL','EMP_DC',c,t))
    return 100*n/d if n and d else None
print('FR', {t:round(sh('FR',t),3) for t in ['2000','2005','2010','2015','2019','2022','2023','2024'] if sh('FR',t)}, src.get(('FR','2023')))
for c in ['DE','IT','ES','NL','BE','SE','DK']:
    print(c,{t:(round(sh(c,t),1) if sh(c,t) else None) for t in ['2005','2023']})
S17='BG CY DK FR DE EL HU IT LV LT LU MT NL SK SI ES SE'.split()
for t in ['2005','2023']:
    v={c:sh(c,t) for c in S17}; miss=[c for c,x in v.items() if x is None]
    v={c:x for c,x in v.items() if x}
    s=sorted(v.values(),reverse=True)
    print(t,'n',len(v),'mean %.2f med %.2f FR %.2f rank %d gap %.2f'%(st.mean(s),st.median(s),v['FR'],s.index(v['FR'])+1,v['FR']-st.median(s)),'miss',miss)
for c in ['FR','DE','NL']:
    for t in ['2005','2024']:
        o=sum(a[('A','THS_PER',x,'EMP_DC',c,t)] for x in 'OPQ'); tot=a[('A','THS_PER','TOTAL','EMP_DC',c,t)]; g=gg.get((c,t))
        if g: print(c,t,'OPQ-GG %.0f thousand, %.1f%% of total'%(o-g,100*(o-g)/tot))
