import csv,statistics as st,sys
rows=list(csv.DictReader(open('data/eurostat_gov_10dd_edpt1_deficit_debt_interest.csv')))
EU27=['BE','BG','CZ','DK','DE','EE','IE','EL','ES','FR','HR','IT','CY','LV','LT','LU','HU','MT','NL','AT','PL','PT','RO','SI','SK','FI','SE']
EA20=['BE','DE','EE','IE','EL','ES','FR','HR','IT','CY','LV','LT','LU','MT','NL','AT','PT','SI','SK','FI']
EA21=EA20+['BG']
PANEL=['FR','DE','IT','ES','NL','BE','SE','DK']
v={}
for r in rows:
    if r['unit']=='PC_GDP': v[(r['na_item'],r['geo'],r['time'])]=float(r['value'])
def stats(item,yr,grp,name,higher_bad):
    vals=[(g,v[(item,g,yr)]) for g in grp if (item,g,yr) in v]
    xs=[x for _,x in vals]
    fr=v.get((item,'FR',yr))
    # rank: 1 = worst (largest debt / largest deficit / largest interest)
    key=(lambda t:-t[1]) if higher_bad else (lambda t:t[1])
    srt=sorted(vals,key=key); rank=[g for g,_ in srt].index('FR')+1
    return f"{item} {yr} {name}: n={len(xs)} mean={st.mean(xs):.1f} median={st.median(xs):.1f} FR={fr} rank_worst={rank}/{len(xs)}"
for yr in ['2005','2007','2015','2019','2024','2025']:
  for item,hb in [('B9',False),('GD',True),('D41PAY',True)]:
    for grp,n in [(EU27,'EU27'),(EA20,'EA20'),(PANEL,'Panel8')]:
        print(stats(item,yr,grp,n,hb))
    print(f"   aggregates: EU27={v.get((item,'EU27_2020',yr))} EA20={v.get((item,'EA20',yr))} EA21={v.get((item,'EA21',yr))}")
print('Panel 2025:')
for g in PANEL:
    print(g,[v.get((i,g,'2025')) for i in ['B9','GD','D41PAY']], 'debt2005',v.get(('GD',g,'2005')),'debt2007',v.get(('GD',g,'2007')))
print('FR vs EA20 deficit gap:')
for y in range(2000,2026):
    y=str(y); print(y,v.get(('B9','FR',y)),v.get(('B9','EA20',y)),'gap',round(v[('B9','FR',y)]-v[('B9','EA20',y)],1) if ('B9','EA20',y) in v else None, 'debtFR',v.get(('GD','FR',y)),'debtEA20',v.get(('GD','EA20',y)),'debtEU27',v.get(('GD','EU27_2020',y)))
