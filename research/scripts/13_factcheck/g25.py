import sys, openpyxl, statistics as st
wb=openpyxl.load_workbook(sys.argv[1], data_only=True, read_only=True); ws=wb.worksheets[0]
NON={'OECD','OECD-EU','BRA','HRV','BGR','ROU','IDN'}
EU=set('AUT BEL CZE DNK EST FIN FRA DEU GRC HUN IRL ITA LVA LTU LUX NLD POL PRT SVK SVN ESP SWE ROU BGR HRV CYP MLT'.split())
d1={};pc={};d1e={};pce={}
for row in ws.iter_rows(min_row=34,values_only=True):
    if not row or not row[1]: continue
    c=row[1].strip()
    if c in ('OECD','OECD-EU'): print(c,row[2:5]); 
    if c in NON-{'HRV','BGR','ROU'} : continue
    if isinstance(row[2],(int,float)):
        if c in EU: d1e[c]=row[2]
        if c not in NON: d1[c]=row[2]
    if all(isinstance(x,(int,float)) for x in row[2:5]):
        s=sum(row[2:5])
        if c in EU: pce[c]=s
        if c not in NON: pc[c]=s
r=lambda d: sorted(d.values(),reverse=True).index(d['FRA'])+1
for lab,d in [('D1 OECD',d1),('PC OECD',pc),('D1 EU',d1e),('PC EU',pce)]:
    print(lab,'n',len(d),'mean %.1f med %.1f'%(st.mean(d.values()),st.median(d.values())),'FR %.2f rank %d'%(d['FRA'],r(d)), sorted(((round(v,2),k) for k,v in d.items()),reverse=True)[:4])
