import csv, statistics as st
D='research/data/'
C={}
for f,u in [('01_eurostat_gov_10a_exp_pcgdp.csv','PC_GDP'),('01_eurostat_gov_10a_exp_mioeur.csv','MIO_EUR'),('01_eurostat_gov_10a_exp_pctot.csv','PC_TOT')]:
    for r in csv.DictReader(open(D+f)):
        C[(u,r['cofog99'],r['geo'],int(r['time']))]=float(r['value'])
pop={(r['geo'],int(r['time'])):float(r['value']) for r in csv.DictReader(open(D+'01_eurostat_nama_10_pe.csv'))}
def c(u,f,g,y): return C.get((u,f,g,y))
EU27=['AT','BE','BG','CY','CZ','DE','DK','EE','EL','ES','FI','FR','HR','HU','IE','IT','LT','LU','LV','MT','NL','PL','PT','RO','SE','SI','SK']
EA20=['AT','BE','CY','DE','EE','EL','ES','FI','FR','HR','IE','IT','LT','LU','LV','MT','NL','PT','SI','SK']
PANEL=['FR','DE','IT','ES','NL','BE','SE','DK']
names={'TOTAL':'Total','GF01':'General public services','GF0107':'  Public debt transactions (interest)','GF02':'Defence','GF03':'Public order & safety','GF04':'Economic affairs','GF0401':'  General economic, commercial & labour affairs','GF0405':'  Transport','GF05':'Environmental protection','GF06':'Housing & community amenities','GF07':'Health','GF0701':'  Medical products','GF0702':'  Outpatient services','GF0703':'  Hospital services','GF08':'Recreation, culture & religion','GF09':'Education','GF0901':'  Pre-primary & primary','GF0902':'  Secondary','GF0904':'  Tertiary','GF10':'Social protection','GF1001':'  Sickness & disability','GF1002':'  Old age','GF1003':'  Survivors','GF1004':'  Family & children','GF1005':'  Unemployment','GF1006':'  Housing (social)','GF1007':'  Social exclusion n.e.c.'}
Y=2024
print("FR COFOG", Y)
print("| code | function | EUR bn | %GDP | %TE | 1995 %GDP | 2005 %GDP | 2015 %GDP | 2019 %GDP|")
for k,n in names.items():
    v=c('MIO_EUR',k,'FR',Y)
    print('|',k,'|',n,'|',round(v/1000,1) if v else None,'|',c('PC_GDP',k,'FR',Y),'|',c('PC_TOT',k,'FR',Y),'|',c('PC_GDP',k,'FR',1995),'|',c('PC_GDP',k,'FR',2005),'|',c('PC_GDP',k,'FR',2015),'|',c('PC_GDP',k,'FR',2019),'|')
print()
print("International %GDP", Y)
print("| func | FR | EU27agg | EA20agg | EU27 mean | EU27 median | FR rank/27 | EA20 mean | EA20 median | FR rank/20 | DE | IT | ES | NL | BE | SE | DK | gap FR-EA agg 2005 | gap 2024 |")
for k,n in names.items():
    def grp(G): 
        vals={g:c('PC_GDP',k,g,Y) for g in G if c('PC_GDP',k,g,Y) is not None}
        srt=[g for g,_ in sorted(vals.items(), key=lambda kv:-kv[1])]
        return round(st.mean(vals.values()),2), round(st.median(vals.values()),2), (srt.index('FR')+1 if 'FR' in vals else None), len(vals)
    e=grp(EU27); a=grp(EA20)
    g05 = None if c('PC_GDP',k,'EA20',2005) is None else round(c('PC_GDP',k,'FR',2005)-c('PC_GDP',k,'EA20',2005),1)
    g24 = round(c('PC_GDP',k,'FR',Y)-c('PC_GDP',k,'EA20',Y),1)
    print('|',n.strip(),'|',c('PC_GDP',k,'FR',Y),'|',c('PC_GDP',k,'EU27_2020',Y),'|',c('PC_GDP',k,'EA20',Y),'|',e[0],'|',e[1],'|',f"{e[2]}/{e[3]}",'|',a[0],'|',a[1],'|',f"{a[2]}/{a[3]}",'|',' | '.join(str(c('PC_GDP',k,g,Y)) for g in PANEL[1:]),'|',g05,'|',g24,'|')
print()
gdp={(r['geo'],int(r['time'])):float(r['value']) for r in csv.DictReader(open(D+'01_eurostat_nama_10_gdp.csv'))}
def agg(k,G,y):
    num=0;den=0;miss=[]
    for g in G:
        v=c('MIO_EUR',k,g,y); gg=gdp.get((g,y))
        if v is None or gg is None: miss.append(g); continue
        num+=v; den+=gg
    return 100*num/den, miss
for y in [2010,2024]:
    print('check own EA20 weighted vs Eurostat',y,round(agg('TOTAL',EA20,y)[0],2),c('PC_GDP','TOTAL','EA20',y), agg('TOTAL',EA20,y)[1])
print("Gap decomposition FR - EA20 GDP-weighted (own computation from member MIO_EUR / GDP), pp of GDP")
for y in [1995,2000,2005,2010,2015,2019,2024]:
    tot=c('PC_GDP','TOTAL','FR',y)-agg('TOTAL',EA20,y)[0]
    print(y,'missing',agg('TOTAL',EA20,y)[1], 'EA20w total',round(agg('TOTAL',EA20,y)[0],1))
    parts={k:round(c('PC_GDP',k,'FR',y)-agg(k,EA20,y)[0],2) for k in ['GF01','GF02','GF03','GF04','GF05','GF06','GF07','GF08','GF09','GF10','GF1002','GF1003','GF1001','GF1004','GF1005','GF0107']}
    print(y,'total gap',round(tot,2),parts, 'old age+survivors share %', round((parts['GF1002']+parts['GF1003'])/tot*100), 'SP share %', round(parts['GF10']/tot*100), 'health share', round(parts['GF07']/tot*100))
print("Gap vs EU27 agg 2024:", round(c('PC_GDP','TOTAL','FR',Y)-c('PC_GDP','TOTAL','EU27_2020',Y),1), {k:round(c('PC_GDP',k,'FR',Y)-c('PC_GDP',k,'EU27_2020',Y),1) for k in ['GF01','GF02','GF03','GF04','GF05','GF06','GF07','GF08','GF09','GF10','GF1002','GF1003','GF1001']})
print("Gap vs DE 2024:", {k:round(c('PC_GDP',k,'FR',Y)-c('PC_GDP',k,'DE',Y),1) for k in ['TOTAL','GF01','GF02','GF03','GF04','GF05','GF06','GF07','GF08','GF09','GF10','GF1002','GF1003','GF1001']})
print()
# PPS per-capita computations: see analyze01c.py (uses price level indices)
