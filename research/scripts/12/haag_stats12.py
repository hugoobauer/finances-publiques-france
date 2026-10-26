"""OECD-38 mean/median/France rank from HaaG 2025 StatLinks (selected figures). python3 -I haag_stats12.py"""
import openpyxl, csv, statistics, re
D='research/data/raw/12/oecd/haag2025/'
OECD=['Australia','Austria','Belgium','Canada','Chile','Colombia','Costa Rica','Czechia','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Ireland','Israel','Italy','Japan','Korea','Latvia','Lithuania','Luxembourg','Mexico','Netherlands','New Zealand','Norway','Poland','Portugal','Slovak Republic','Slovenia','Spain','Sweden','Switzerland','Türkiye','United Kingdom','United States']
ISO={'AUS':'Australia','AUT':'Austria','BEL':'Belgium','CAN':'Canada','CHL':'Chile','COL':'Colombia','CRI':'Costa Rica','CZE':'Czechia','DNK':'Denmark','EST':'Estonia','FIN':'Finland','FRA':'France','DEU':'Germany','GRC':'Greece','HUN':'Hungary','ISL':'Iceland','IRL':'Ireland','ISR':'Israel','ITA':'Italy','JPN':'Japan','KOR':'Korea','LVA':'Latvia','LTU':'Lithuania','LUX':'Luxembourg','MEX':'Mexico','NLD':'Netherlands','NZL':'New Zealand','NOR':'Norway','POL':'Poland','PRT':'Portugal','SVK':'Slovak Republic','SVN':'Slovenia','ESP':'Spain','SWE':'Sweden','CHE':'Switzerland','TUR':'Türkiye','GBR':'United Kingdom','USA':'United States'}
PANEL=['France','Germany','Italy','Spain','Netherlands','Belgium','Sweden','Denmark']
def clean(n): return ISO.get(str(n).strip(), re.sub(r'[¹²³⁴⁵⁶*\d]+$','',str(n)).strip())
SPECS=[ # file, label, value column index (0-based among non-None cells after name), higher_is_rank1
 ('15fht6','CHE % GDP 2024 (total)',3,True),('15fht6','CHE % GDP 2024 (government/compulsory)',1,True),
 ('rkae5h','CHE per capita USD PPP 2024 (total)',3,True),('rkae5h','CHE per capita USD PPP 2024 (government/compulsory)',1,True),
 ('zw0b9d','Health price level 2023 (OECD=100)',1,True),('tfnguq','Health volume per capita 2023 (OECD=100)',1,True),
 ('mzifb7','Practising doctors per 1000, 2023',2,True),('fr3n8d','Practising nurses per 1000, 2023',2,True),
 ('9zdx04','Hospital beds per 1000, 2023',2,True),('4sxvgp','ALOS curative care 2023',2,True),('0urtay','Curative bed occupancy 2023',2,True),
 ('9ari8w','Hospital workforce per 1000, 2023 (total)',6,True),('it5m0j','Hospital discharges per 1000, 2023',2,True),
 ('rqt74h','In-person doctor consultations per capita 2023',3,True),('7ah6wr','Hospitals share of CHE 2023',1,True),
 ('zjfk7p','Treatable mortality 2023 (OECD std)',2,False),('if1ugq','Preventable mortality 2023 (OECD std)',2,False),
 ('bos5wh','Financial coverage, all services (share of spending covered)',1,True),('v23mqi','OOP share of household consumption 2023',1,False),
 ('59ftvc','ED visits per 100 pop 2023',2,True),('rf68c2','Ambulatory share, cataract 2023',1,True),
]
LASTNUM={'mzifb7','fr3n8d','9zdx04','4sxvgp','0urtay','it5m0j','9ari8w','rqt74h'}
w=csv.writer(open('research/data/12_oecd_haag2025_computed_stats.csv','w',newline=''))
w.writerow(['indicator','statlink','n_OECD','FR','OECD_mean_computed','OECD_median','FR_rank','rank_direction','OECD_avg_published','panel_mean','panel_median','FR_rank_panel']+PANEL[1:])
for code,label,col,hi in SPECS:
    ws=openpyxl.load_workbook(D+code+'.xlsx',read_only=True,data_only=True).worksheets[0]
    vals={}; pub=''
    for r in ws.iter_rows(values_only=True):
        c=[x for x in r if x is not None]
        if not c or not isinstance(c[0],str): continue
        name=clean(c[0])
        nums=[x for x in c[1:] if isinstance(x,(int,float))]
        if code in LASTNUM: v=nums[-1] if nums else None
        else:
            try: v=c[col] if col<len(c) else None
            except: v=None
        if isinstance(v,str):
            try: v=float(v)
            except: v=None
        if v is None: continue
        if name.startswith('OECD'): pub=v
        elif name in OECD and name not in vals: vals[name]=float(v)
    if 'France' not in vals: print('no FR',label); continue
    s=sorted(vals.values(),reverse=hi); p={k:vals[k] for k in PANEL if k in vals}; ps=sorted(p.values(),reverse=hi)
    row=[label,'https://stat.link/'+code,len(vals),vals['France'],round(statistics.mean(vals.values()),2),round(statistics.median(vals.values()),2),s.index(vals['France'])+1,'1=highest' if hi else '1=lowest',pub,round(statistics.mean(p.values()),2),round(statistics.median(p.values()),2),ps.index(vals['France'])+1]+[vals.get(k,'') for k in PANEL[1:]]
    w.writerow(row); print(row)
