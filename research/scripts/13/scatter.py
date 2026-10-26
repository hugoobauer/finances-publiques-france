import csv,sys,statistics as st
R=sys.argv[1]
sp={r['country']:r for r in csv.DictReader(open(R+'/data/13_eag2026_C1_1_spending_per_student_2023.csv'))}
pi={r['country']:r for r in csv.DictReader(open(R+'/data/13_pisa2025_country_values.csv'))}
EU=[c for c in pi if pi[c]['eu27']=='True']; OE=[c for c in pi if pi[c]['oecd']=='True']; PAN=[c for c in pi if pi[c]['panel']=='True']
rows=[]
for c in sorted(set(sp)&set(pi)):
    s=sp[c]['tot_prim_postsec']; g=sp[c]['gov_prim_postsec']
    if not s: continue
    m=float(pi[c]['math_2025']); rd=float(pi[c]['reading_2025']); sc=float(pi[c]['science_2025'])
    rows.append([c,c in OE,c in EU,c in PAN,int(s),int(g) if g else '',round(m,1),round(rd,1),round(sc,1),round((m+rd+sc)/3,1)])
def fit(xs,ys):
    mx,my=st.mean(xs),st.mean(ys); b=sum((x-mx)*(y-my) for x,y in zip(xs,ys))/sum((x-mx)**2 for x in xs); a=my-b*mx
    r=st.correlation(xs,ys); return a,b,r
for lab,sel in [('OECD',lambda r:r[1]),('EU',lambda r:r[2])]:
    rr=[r for r in rows if sel(r)]
    xs=[r[4]/1000 for r in rr]; ys=[r[9] for r in rr]
    a,b,rc=fit(xs,ys)
    fr=[r for r in rr if r[0]=='France'][0]
    pred=a+b*fr[4]/1000
    srt=sorted([r[4] for r in rr],reverse=True)
    print(lab,'n',len(rr),'slope pts per 1000 USD',round(b,2),'r',round(rc,2),'R2',round(rc*rc,2),'FR pred',round(pred,1),'actual',fr[9],'resid',round(fr[9]-pred,1),'FR spend rank',srt.index(fr[4])+1,'median spend',st.median([r[4] for r in rr]))
    # restrict to spending > 10k
    rr2=[r for r in rr if r[4]>=10000]; a2,b2,rc2=fit([r[4]/1000 for r in rr2],[r[9] for r in rr2]); print('   >=10k USD: n',len(rr2),'slope',round(b2,2),'r',round(rc2,2),'FR resid',round(fr[9]-(a2+b2*fr[4]/1000),1))
with open(R+'/data/13_scatter_spending_vs_pisa2025.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['country','oecd','eu27','panel','eag2026_total_spend_per_student_prim_to_postsec_2023_usd_ppp','eag2026_gov_spend_per_student_prim_to_postsec_2023_usd_ppp','pisa2025_math','pisa2025_reading','pisa2025_science','pisa2025_avg3']); w.writerows(rows)
for r in rows:
    if r[3] or r[0] in ('Finland','Estonia','Poland','Portugal','Ireland','Japan','Korea','United States','United Kingdom','Luxembourg','Norway','Austria'): print(r)
