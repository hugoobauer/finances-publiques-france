import sys, openpyxl, statistics as st
wb=openpyxl.load_workbook(sys.argv[1], data_only=True, read_only=True); ws=wb.worksheets[0]
EU=set('AUT BEL CZE DNK EST FIN FRA DEU GRC HUN IRL ITA LVA LTU LUX NLD POL PRT SVK SVN ESP SWE ROU BGR HRV CYP MLT'.split())
v07={};v19={}
for row in ws.iter_rows(min_row=3,max_row=42,values_only=True):
    if not row[0] or len(row[0])!=3 or row[0]=='OEC': continue
    c=row[0]
    if isinstance(row[1],(int,float)): v07[c]=row[1]
    if isinstance(row[2],(int,float)): v19[c]=row[2]
    print(c,row[1],row[2])
for lab,v in [('2007',v07),('2019',v19)]:
    o={c:x for c,x in v.items() if c!='ROU'}; e={c:x for c,x in v.items() if c in EU}
    r=lambda d: sorted(d.values(),reverse=True).index(d['FRA'])+1
    print(lab,'OECD n',len(o),'mean %.1f med %.1f rank %d'%(st.mean(o.values()),st.median(o.values()),r(o)),'| EU n',len(e),'mean %.1f med %.1f rank %d'%(st.mean(e.values()),st.median(e.values()),r(e)))
    print('  incl ROU n',len(v))
