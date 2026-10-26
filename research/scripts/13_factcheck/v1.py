import sys, statistics as st
sys.path.insert(0, sys.argv[1]); from js import load
D=sys.argv[2]
EU=['BE','BG','CZ','DK','DE','EE','IE','EL','ES','FR','HR','IT','CY','LV','LT','LU','HU','MT','NL','AT','PL','PT','RO','SI','SK','FI','SE']
PAN=['FR','DE','IT','ES','NL','BE','SE','DK']
dims,a=load(D+'/a64e.json')
def g(n,geo,t): return a.get(('A','THS_PER',n,'EMP_DC',geo,t))
def rank(vals,c): s=sorted(vals.values(),reverse=True); return s.index(vals[c])+1
for t in ['2000','2005','2015','2019','2023','2024','2025']:
    sh={}
    for c in EU+['EU27_2020']:
        tot=g('TOTAL',c,t); o=[g(x,c,t) for x in 'OPQ']
        if tot and all(v is not None for v in o): sh[c]=100*sum(o)/tot
    eu={c:v for c,v in sh.items() if c in EU}; pan={c:sh[c] for c in PAN if c in sh}
    print(t,'n',len(eu),'FR %.1f'%sh.get('FR',0),'EU27agg %s'%(round(sh['EU27_2020'],1) if 'EU27_2020' in sh else None),
      'mean %.1f med %.1f'%(st.mean(eu.values()),st.median(eu.values())),'FRrank',rank(eu,'FR'),
      'panel',{c:round(v,1) for c,v in pan.items()},'pmed %.2f'%st.median(pan.values()),'prank',rank(pan,'FR'), 'gap %.2f'%(sh['FR']-st.median(pan.values())))
