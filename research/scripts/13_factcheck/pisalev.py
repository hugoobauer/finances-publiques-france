import sys, statistics as st
sys.path.insert(0, sys.argv[1]); from pisa import wb, OECD, EU
from pisatrend import rows
num=lambda x: x if isinstance(x,(int,float)) else None
for name,ncyc,i15 in [('Table I.B1.2a.35',8,4),('Table I.B1.2a.34',9,5),('Table I.B1.2a.33',7,3)]:
    R=rows(name); print('==',name)
    for lab,off in [('low',0),('top',2)]:
        for cyc,ci in [('2025',ncyc-1),('2015',i15)]:
            for gname,g in [('OECD',OECD),('EU',EU)]:
                d={c:num(R[c][1+4*ci+off]) for c in g if c in R and num(R[c][1+4*ci+off]) is not None}
                s=sorted(d.values(), reverse=(lab=='top'))
                print(' ',lab,cyc,gname,'n',len(d),'mean %.1f med %.1f FR %.1f rank %d'%(st.mean(s),st.median(s),d['France'],s.index(d['France'])+1))
