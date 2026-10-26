import sys, statistics as st
sys.path.insert(0, sys.argv[1]); import pisa
from pisa import wb, OECD, EU, PAN
def rows(name):
    out={}
    for r in wb[name].iter_rows(values_only=True):
        r=[x for x in r if x is not None]
        if r and isinstance(r[0],str): out.setdefault(r[0].rstrip('*').strip(), r)
    return out
num=lambda x: x if isinstance(x,(int,float)) else None
def trend(name, years, chg):
    R=rows(name)
    sc={y:{} for y in years}; ch={k:{} for k in chg}
    for c in OECD:
        r=R.get(c)
        if not r: print('missing',c); continue
        for i,y in enumerate(years):
            v=num(r[1+2*i]); 
            if v is not None: sc[y][c]=v
        base=1+2*len(years)
        for j,k in enumerate(chg):
            v=num(r[base+2*j])
            if v is not None: ch[k][c]=v
    print('==',name)
    for y in years:
        d=sc[y]
        if 'France' in d: print(' ',y,'n',len(d),'median %.1f FR %.1f gap %.1f'%(st.median(d.values()),d['France'],d['France']-st.median(d.values())))
    for k in chg:
        d=ch[k]
        if 'France' in d:
            s=sorted(d.values()); print('  change vs',k,'n',len(d),'median %.1f mean %.1f FR %.1f fallrank %d'%(st.median(s),st.mean(s),d['France'],s.index(d['France'])+1))
#trend('Table I.B1.2a.38',['2003','2006','2009','2012','2015','2018','2022','2025'],['2003','2006','2009','2012','2015','2018','2022'])
#trend('Table I.B1.2a.37',['2000','2003','2006','2009','2012','2015','2018','2022','2025'],['2000','2003','2006','2009','2012','2015','2018','2022'])
#trend('Table I.B1.2a.36',['2006','2009','2012','2015','2018','2022','2025'],['2006','2009','2012','2015','2018','2022'])
