import sys, statistics as st
sys.path.insert(0, sys.argv[1]); from js import load
D=sys.argv[2]
EU=['BE','BG','CZ','DK','DE','EE','IE','EL','ES','FR','HR','IT','CY','LV','LT','LU','HU','MT','NL','AT','PL','PT','RO','SI','SK','FI','SE']
PAN=['FR','DE','IT','ES','NL','BE','SE','DK']
_,m=load(D+'/main.json'); _,p=load(D+'/pop.json'); _,l=load(D+'/pli1.json')
def M(i,c,t): return m.get(('A','MIO_EUR','S13',i,c,t))
def P(c,t): return p.get(('A','THS_PER','POP_NC',c,t))
def L(c,t): return l.get(('A','PLI_EU27_2020','GDP',c,t))
print('PLI FR 2005,2024,2025',L('FR','2005'),L('FR','2024'),L('FR','2025'))
def pc(items,c,t):
    try:
        v=sum(M(i,c,t) for i in items); return v*1e6/(P(c,t)*1e3)/(L(c,t)/100)
    except TypeError: return None
def rank(vals,c): s=sorted(vals.values(),reverse=True); return s.index(vals[c])+1
for lab,items in [('D1',['D1PAY']),('D11',['D11PAY']),('PC',['D1PAY','P2','D632PAY']),('TE',['TE'])]:
    for t in ['2005','2024','2025']:
        v={c:pc(items,c,t) for c in EU+['EU27_2020','EA20']}
        eu={c:x for c,x in v.items() if c in EU and x}
        ag=v['EU27_2020']
        pan={c:v[c] for c in PAN if v.get(c)}
        print(lab,t,'FR %.0f EU %s EA %s idx %.0f'%(v['FR'],ag and round(ag),v['EA20'] and round(v['EA20']),100*v['FR']/ag if ag else 0),
          'n',len(eu),'mean %.0f med %.0f'%(st.mean(eu.values()),st.median(eu.values())),'rank',rank(eu,'FR'),
          'panel',{c:round(x) for c,x in pan.items()},'pmed %.0f'%st.median(pan.values()),'prank',rank(pan,'FR'))
        if t=='2025' or t=='2005':
            print('   idx', {c:round(100*v[c]/ag) for c in PAN+['EA20'] if v.get(c) and ag})
