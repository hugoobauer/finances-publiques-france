import openpyxl,sys,csv,statistics as st
R=sys.argv[1]
wb=openpyxl.load_workbook(R+'/data/raw/13/eag/eag2026_C1.xlsx',read_only=True,data_only=True)
ws=wb['Table C1.1.']
rows=[list(r) for r in ws.iter_rows(values_only=True)]
hdr=rows[9]; pos={v:i for i,v in enumerate(hdr) if isinstance(v,int)}
names={1:'tot_prim_postsec',2:'tot_secondary',3:'tot_tert_inclRD',4:'tot_tert_exclRD',5:'tot_prim_tert_inclRD',6:'tot_prim_tert_exclRD',
       7:'gov_prim_postsec',8:'gov_secondary',9:'gov_tert_inclRD',10:'gov_tert_exclRD',11:'gov_prim_tert_inclRD',12:'gov_prim_tert_exclRD'}
name_col=0
out={}
for r in rows[10:]:
    if r[0] and isinstance(r[0],str) and not r[0].startswith(('OECD countries','Partner','Note','Source')):
        c=r[0].strip()
        out[c]={n:(r[pos[k]] if isinstance(r[pos[k]],(int,float)) else None) for k,n in names.items()}
with open(R+'/data/13_eag2026_C1_1_spending_per_student_2023.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['country']+list(names.values()))
    for c,v in out.items(): w.writerow([c]+[('' if v[n] is None else round(v[n])) for n in names.values()])
for c in ['France','Germany','Italy','Spain','Netherlands','Belgium','Sweden','Denmark','OECD average','EU25 average']:
    print(c,{k:(round(v) if v else None) for k,v in out.get(c,{}).items()})
print(list(out)[:80])
