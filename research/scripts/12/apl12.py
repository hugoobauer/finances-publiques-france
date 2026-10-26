"""Population living in communes with GP APL below thresholds (Drees APL file, 2022-2024). python3 -I apl12.py"""
import openpyxl, csv
F='research/data/raw/12/drees/apl_mg.xlsx'
out=csv.writer(open('research/data/12_drees_apl_gp_underserved.csv','w',newline=''))
out.writerow(['year','apl_variant','threshold','population_below','total_population','share_pct','pop_weighted_mean_apl_std'])
wb=openpyxl.load_workbook(F,read_only=True)
for y in (2022,2023,2024):
    ws=wb[f'APL {y}']; rows=list(ws.iter_rows(values_only=True))
    hdr_i=next(i for i,r in enumerate(rows) if r[0]=='Code commune INSEE'); hdr=rows[hdr_i]
    data=[r for r in rows[hdr_i+2:] if r[0] and isinstance(r[2],(int,float))]
    ipop=next(i for i,h in enumerate(hdr) if h and str(h).startswith('Population totale'))
    istd=next(i for i,h in enumerate(hdr) if h and str(h).startswith('Population standardis'))
    for col,lab in ((2,'all GPs'),(3,'GPs aged 65 or under')):
        tot=sum(r[ipop] or 0 for r in data)
        mean=sum((r[col] or 0)*(r[istd] or 0) for r in data)/sum(r[istd] or 0 for r in data)
        for th in (1.5,2.5,4.0):
            below=sum(r[ipop] or 0 for r in data if r[col] is not None and r[col]<th)
            out.writerow([y,lab,th,round(below),round(tot),round(100*below/tot,2),round(mean,3)])
            print(y,lab,th,round(below/1e6,2),'M',round(100*below/tot,2),'% mean',round(mean,2))
