import csv, statistics as st
D='research/data/'
C={}
for r in csv.DictReader(open(D+'01_eurostat_gov_10a_exp_mioeur.csv')):
    C[(r['cofog99'],r['geo'],int(r['time']))]=float(r['value'])
gdp={(r['geo'],int(r['time'])):float(r['value']) for r in csv.DictReader(open(D+'01_eurostat_nama_10_gdp.csv'))}
pli={(r['geo'],int(r['time'])):float(r['value']) for r in csv.DictReader(open(D+'01_eurostat_prc_ppp_ind_pli.csv'))}
pop={(r['geo'],int(r['time'])):float(r['value']) for r in csv.DictReader(open(D+'01_eurostat_nama_10_pe.csv'))}
EU27=['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK']
EA20=['AT','BE','CY','DE','EE','EL','ES','FI','FR','HR','IE','IT','LT','LU','LV','MT','NL','PT','SI','SK']
PANEL=['DE','IT','ES','NL','BE','SE','DK']
def pct(k,g,y):
    v=C.get((k,g,y)); G=gdp.get((g,y))
    return None if v is None or G is None else 100*v/G
def agg(k,G,y):
    num=sum(C[(k,g,y)] for g in G if (k,g,y) in C and (g,y) in gdp); den=sum(gdp[(g,y)] for g in G if (k,g,y) in C and (g,y) in gdp)
    return 100*num/den
def pps(k,g,y):
    v=C.get((k,g,y)); p=pli.get((g,y)); n=pop.get((g,y))
    return None if None in (v,p,n) else v*1e6/(p/100)/(n*1e3)
keys=['TOTAL','GF01','GF0107','GF02','GF03','GF04','GF05','GF06','GF07','GF08','GF09','GF10','GF1001','GF1002','GF1003','GF1004','GF1005','GF1006','GF1007']
out=open(D+'01_derived_cofog_international_2024.csv','w'); w=csv.writer(out)
w.writerow(['cofog','FR_pcgdp','EU27_w','EA20_w','EU27_mean','EU27_median','FR_rank_EU27','EA20_mean','EA20_median','FR_rank_EA20']+PANEL+['gap_FR_EA20w_2005','gap_FR_EA20w_2024','FR_PPS_pc','EU27_PPS_mean','EU27_PPS_median','FR_PPS_rank']+[p+'_PPS' for p in PANEL])
Y=2024
for k in keys:
    def grp(G):
        vals={g:pct(k,g,Y) for g in G if pct(k,g,Y) is not None}
        srt=[g for g,_ in sorted(vals.items(), key=lambda kv:-kv[1])]
        return round(st.mean(vals.values()),2), round(st.median(vals.values()),2), f"{srt.index('FR')+1}/{len(vals)}"
    e=grp(EU27); a=grp(EA20)
    pv={g:pps(k,g,Y) for g in EU27 if pps(k,g,Y) is not None}
    ps=[g for g,_ in sorted(pv.items(), key=lambda kv:-kv[1])]
    row=[k,round(pct(k,'FR',Y),2),round(agg(k,EU27,Y),2),round(agg(k,EA20,Y),2),*e,*a,*[round(pct(k,g,Y),2) for g in PANEL],
         round(pct(k,'FR',2005)-agg(k,[g for g in EA20 if g!='SK'],2005),2), round(pct(k,'FR',Y)-agg(k,EA20,Y),2),
         round(pv['FR']), round(st.mean(pv.values())), round(st.median(pv.values())), f"{ps.index('FR')+1}/{len(pv)}", *[round(pv[g]) for g in PANEL]]
    w.writerow(row); print(row)
out.close()
print('TOTAL PPS pc by year:')
for y in [2005,2010,2015,2019,2024]:
    pv={g:pps('TOTAL',g,y) for g in EU27 if pps('TOTAL',g,y) is not None}
    ps=[g for g,_ in sorted(pv.items(), key=lambda kv:-kv[1])]
    print(y,'FR',round(pv['FR']),'mean',round(st.mean(pv.values())),'median',round(st.median(pv.values())),'rank',ps.index('FR')+1,len(pv),{g:round(pv[g]) for g in PANEL if g in pv}, ps[:6])
print('Gap FR-EA20w total by year:')
for y in range(1995,2025):
    G=[g for g in EA20 if (('TOTAL',g,y) in C)]
    print(y, round(pct('TOTAL','FR',y),1), round(agg('TOTAL',G,y),1), round(pct('TOTAL','FR',y)-agg('TOTAL',G,y),1), 'SPgap',round(pct('GF10','FR',y)-agg('GF10',G,y),2),'oldage gap',round(pct('GF1002','FR',y)-agg('GF1002',G,y),2),'health gap',round(pct('GF07','FR',y)-agg('GF07',G,y),2))
