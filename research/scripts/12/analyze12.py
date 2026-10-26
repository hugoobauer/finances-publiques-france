"""Topic 12: health system international comparison (Eurostat). Run: python3 -I analyze12.py
Reads raw CSVs converted from Eurostat JSON (data/raw/12/eurostat/csv) and writes research/data/12_*.csv"""
import csv, statistics, os, collections
R='research/data/raw/12/eurostat/csv/'
OUT='research/data/'
EU27=['BE','BG','CZ','DK','DE','EE','IE','EL','ES','FR','HR','IT','CY','LV','LT','LU','HU','MT','NL','AT','PL','PT','RO','SI','SK','FI','SE']
EA21=['BE','BG','DE','EE','IE','EL','ES','FR','HR','IT','CY','LV','LT','LU','MT','NL','AT','PT','SI','SK','FI']
PANEL=['FR','DE','IT','ES','NL','BE','SE','DK']
AGGS=['EU27_2020','EA20','EA19','EA21','EA']
def load(fn, filt):
    out={}
    for r in csv.DictReader(open(R+fn)):
        if all(r.get(k)==v for k,v in filt.items()):
            out[(r['geo'],r['time'])]=(float(r['value']),r.get('flag',''))
    return out
IND=[ # name, file, filter, unit label, higher_is_rank1
 ('CHE total % GDP','sha_hf.csv',{'unit':'PC_GDP','icha11_hf':'TOT_HF'},'% of GDP',True),
 ('CHE total PPS per inhabitant','sha_hf.csv',{'unit':'PPS_HAB','icha11_hf':'TOT_HF'},'PPS per inhabitant',True),
 ('CHE total EUR per inhabitant','sha_hf.csv',{'unit':'EUR_HAB','icha11_hf':'TOT_HF'},'EUR per inhabitant',True),
 ('HF1 govt+compulsory schemes % GDP','sha_hf.csv',{'unit':'PC_GDP','icha11_hf':'HF1'},'% of GDP',True),
 ('HF1 govt+compulsory schemes PPS per inhabitant','sha_hf.csv',{'unit':'PPS_HAB','icha11_hf':'HF1'},'PPS per inhabitant',True),
 ('HF1 share of CHE','sha_hf.csv',{'unit':'PC_CHE','icha11_hf':'HF1'},'% of CHE',True),
 ('HF2 voluntary schemes share of CHE','sha_hf.csv',{'unit':'PC_CHE','icha11_hf':'HF2'},'% of CHE',True),
 ('HF3 out-of-pocket share of CHE','sha_hf.csv',{'unit':'PC_CHE','icha11_hf':'HF3'},'% of CHE',True),
 ('HF3 out-of-pocket PPS per inhabitant','sha_hf.csv',{'unit':'PPS_HAB','icha11_hf':'HF3'},'PPS per inhabitant',True),
 ('HP1 hospitals share of CHE','sha_hp.csv',{'unit':'PC_CHE','icha11_hp':'HP1'},'% of CHE',True),
 ('HP1 hospitals % GDP','sha_hp.csv',{'unit':'PC_GDP','icha11_hp':'HP1'},'% of GDP',True),
 ('HP1 hospitals PPS per inhabitant','sha_hp.csv',{'unit':'PPS_HAB','icha11_hp':'HP1'},'PPS per inhabitant',True),
 ('HP7 administration providers share of CHE','sha_hp.csv',{'unit':'PC_CHE','icha11_hp':'HP7'},'% of CHE',True),
 ('HC11 inpatient curative share of CHE','sha_hc.csv',{'unit':'PC_CHE','icha11_hc':'HC11'},'% of CHE',True),
 ('HC1_2 curative+rehab % GDP','sha_hc.csv',{'unit':'PC_GDP','icha11_hc':'HC1_2'},'% of GDP',True),
 ('HC3 long-term care (health) share of CHE','sha_hc.csv',{'unit':'PC_CHE','icha11_hc':'HC3'},'% of CHE',True),
 ('HC51 pharmaceuticals share of CHE','sha_hc.csv',{'unit':'PC_CHE','icha11_hc':'HC51'},'% of CHE',True),
 ('HC6 preventive care share of CHE','sha_hc.csv',{'unit':'PC_CHE','icha11_hc':'HC6'},'% of CHE',True),
 ('HC7 governance and admin share of CHE','sha_hc.csv',{'unit':'PC_CHE','icha11_hc':'HC7'},'% of CHE',True),
 ('HC7 governance and admin % GDP','sha_hc.csv',{'unit':'PC_GDP','icha11_hc':'HC7'},'% of GDP',True),
 ('HC7 governance and admin PPS per inhabitant','sha_hc.csv',{'unit':'PPS_HAB','icha11_hc':'HC7'},'PPS per inhabitant',True),
 ('HC72 admin of health financing share of CHE','sha_hc.csv',{'unit':'PC_CHE','icha11_hc':'HC72'},'% of CHE',True),
 ('Practising physicians per 100k','prs1.csv',{'wstatus':'PRACT','med_spec':'PHYS'},'per 100,000',True),
 ('Practising nurses per 100k','prs1.csv',{'wstatus':'PRACT','med_spec':'NRS'},'per 100,000',True),
 ('Professionally active nurses per 100k','prs1.csv',{'wstatus':'PACT','med_spec':'NRS'},'per 100,000',True),
 ('Hospital beds total per 100k','bds1.csv',{'facility':'HBEDT','hlthcare':'TOTAL'},'per 100,000',True),
 ('Curative care beds per 100k','bds1.csv',{'facility':'HBEDT_CUR','hlthcare':'TOTAL'},'per 100,000',True),
 ('ALOS in-patients all hospitals (old series)','alos.csv',{'age':'TOTAL','sex':'T','icd10':'A-T_Z'},'days',True),
 ('ALOS in-patients all hospitals (new series)','talos.csv',{'icd10':'TOTAL'},'days',True),
 ('Treatable mortality rate','cd_apr.csv',{'mortalit':'TRT','unit':'RT','icd10':'TOTAL'},'per 100,000 (age-std)',False),
 ('Preventable mortality rate','cd_apr.csv',{'mortalit':'PRVT','unit':'RT','icd10':'TOTAL'},'per 100,000 (age-std)',False),
 ('Healthy life years at birth','hlye.csv',{'unit':'YR','sex':'T','hlth_hle':'HLY_Y0'},'years',True),
 ('Healthy life years at 65','hlye.csv',{'unit':'YR','sex':'T','hlth_hle':'HLY_Y65'},'years',True),
 ('Life expectancy at birth (hlye)','hlye.csv',{'unit':'YR','sex':'T','hlth_hle':'LE_Y0'},'years',True),
 ('Unmet needs cost/distance/waiting, total','silc08.csv',{'reason':'TXP_TFAR_WLIST','quant_inc':'TOTAL'},'% of 16+',False),
 ('Unmet needs cost/distance/waiting, bottom quintile','silc08.csv',{'reason':'TXP_TFAR_WLIST','quant_inc':'QU1'},'% of 16+',False),
 ('Unmet needs: waiting list, total','silc08.csv',{'reason':'WLIST','quant_inc':'TOTAL'},'% of 16+',False),
 ('Unmet needs: too expensive, total','silc08.csv',{'reason':'TXP','quant_inc':'TOTAL'},'% of 16+',False),
 ('Unmet needs: too far, total','silc08.csv',{'reason':'TFAR','quant_inc':'TOTAL'},'% of 16+',False),
]
def stats(data, year, group, hi):
    vals={g:data[(g,year)][0] for g in group if (g,year) in data}
    if 'FR' not in vals or len(vals)<3: return None
    s=sorted(vals.values(), reverse=hi)
    return dict(n=len(vals), mean=round(statistics.mean(vals.values()),2), median=round(statistics.median(vals.values()),2), rank=s.index(vals['FR'])+1)
long=open(OUT+'12_eurostat_health_long.csv','w',newline=''); lw=csv.writer(long); lw.writerow(['indicator','unit','geo','year','value','flag'])
st=open(OUT+'12_computed_stats.csv','w',newline=''); sw=csv.writer(st)
sw.writerow(['indicator','unit','year','FR','FR_flag','EU27_agg','EA_agg(code)','EU27_n','EU27_mean','EU27_median','FR_rank_EU27','EA21_n','EA21_mean','EA21_median','FR_rank_EA21','panel_n','panel_mean','panel_median','FR_rank_panel','rank_direction','FR_minus_EU27_mean','DE','IT','ES','NL','BE','SE','DK'])
for name,fn,filt,unit,hi in IND:
    d=load(fn,filt)
    for (g,y),(v,f) in sorted(d.items()):
        if g in EU27+AGGS or g in ('NO','CH','IS','UK','TR'): lw.writerow([name,unit,g,y,v,f])
    years=sorted({y for (g,y) in d if g=='FR'})
    for y in years:
        a=stats(d,y,EU27,hi); b=stats(d,y,EA21,hi); c=stats(d,y,PANEL,hi)
        if not a: continue
        eu=d.get(('EU27_2020',y),('',''))[0]
        ea=next((f"{d[(k,y)][0]} ({k})" for k in ['EA20','EA19','EA'] if (k,y) in d),'')
        fr,fl=d[('FR',y)]
        sw.writerow([name,unit,y,fr,fl,eu,ea,a['n'],a['mean'],a['median'],a['rank'],
          b['n'] if b else '',b['mean'] if b else '',b['median'] if b else '',b['rank'] if b else '',
          c['n'] if c else '',c['mean'] if c else '',c['median'] if c else '',c['rank'] if c else '',
          '1=highest' if hi else '1=lowest(best)', round(fr-a['mean'],2)]+[d.get((p,y),('',''))[0] for p in PANEL[1:]])
long.close(); st.close()
# SILC France flags full series
with open(OUT+'12_eurostat_silc_unmet_fr_flags.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['reason','quant_inc','geo','year','value','flag'])
    for r in csv.DictReader(open(R+'silc08.csv')):
        if r['geo'] in ('FR','EU27_2020','DE','ES','IT','BE','NL','SE','DK') and r['reason'] in ('TXP_TFAR_WLIST','WLIST','TXP','TFAR','NTIME','HOPE','FEAR_DR_HSP','OTH','NUMT_ND','GDOC_UNK'):
            w.writerow([r['reason'],r['quant_inc'],r['geo'],r['time'],r['value'],r['flag']])
print('done')
