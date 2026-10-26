import csv,sys,statistics as st
R=sys.argv[1]; D=R+'/data/'
g={};p={};l={};lo={}
for r in csv.DictReader(open(D+'13_eurostat_gov_10a_main_D1_P2_D632_mioeur.csv')): g[(r['na_item'],r['geo'],int(r['time']))]=float(r['value'])
for r in csv.DictReader(open(D+'13_eurostat_nama_10_pe_pop.csv')): p[(r['geo'],int(r['time']))]=float(r['value'])
for r in csv.DictReader(open(D+'13_eurostat_prc_ppp_ind_1_PLI_GDP.csv')): l[(r['geo'],int(r['time']))]=float(r['value'])
for r in csv.DictReader(open(D+'raw/13/pli_old.csv')): lo[(r['geo'],int(r['time']))]=float(r['value'])
EU=['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','EL','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE']
P=['FR','DE','IT','ES','NL','BE','SE','DK']
def val(item,c,y,pli=l):
    try:
        if item=='PROD': v=g[('D1PAY',c,y)]+g[('P2',c,y)]+g[('D632PAY',c,y)]
        else: v=g[(item,c,y)]
        return v*1e6/(p[(c,y)]*1e3)/(pli[(c,y)]/100)
    except KeyError: return None
rows=[];stats=[]
for item in ['D1PAY','D11PAY','PROD','TE']:
    for y in (2005,2015,2019,2024,2025):
        vals={c:val(item,c,y) for c in EU}; vals={c:v for c,v in vals.items() if v}
        for c in EU+['EU27_2020','EA20']:
            v=val(item,c,y)
            if v: rows.append([item,c,y,round(v),round(100*v/val(item,'EU27_2020',y),1) if val(item,'EU27_2020',y) else ''])
        if 'FR' in vals:
            s=sorted(vals.values(),reverse=True); pv={c:vals[c] for c in P if c in vals}; ps=sorted(pv.values(),reverse=True)
            stats.append([item,y,len(vals),round(st.mean(vals.values())),round(st.median(vals.values())),round(vals['FR']),s.index(vals['FR'])+1,round(val(item,'EU27_2020',y) or 0),round(st.median(pv.values())),ps.index(vals['FR'])+1,len(pv)])
with open(D+'13_pps_per_capita_wagebill_production_costs.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['item','geo','year','PPS_per_capita','index_EU27_100']); w.writerows(rows)
with open(D+'13_pps_per_capita_stats.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['item','year','n_EU','EU_mean_unweighted','EU_median','FR','FR_rank_EU_1_highest','EU27_aggregate','panel_median','FR_rank_panel','n_panel']); w.writerows(stats)
for s in stats: print(s)
for item in ['D1PAY','D11PAY','PROD','TE']:
    for y in (2005,2024,2025):
        print(item,y,{c:round(val(item,c,y) or 0) for c in P+['EU27_2020','EA20']})
print('old-vintage 2024 D1 FR',round(val('D1PAY','FR',2024,lo)),'new',round(val('D1PAY','FR',2024)))
print('PLI 2024 old/new', {c:(lo.get((c,2024)),l.get((c,2024))) for c in P})
print('PLI 2025', {c:l.get((c,2025)) for c in P})
