"""Flatten selected OECD Health at a Glance 2025 StatLink workbooks into one long CSV (raw rows, as published). python3 -I haag_to_csv.py"""
import openpyxl, csv, glob, os
D='research/data/raw/12/oecd/haag2025/'
links={l.split(' | ')[1].strip().rsplit('/',1)[1]:l.split(' | ')[0] for l in open(D+'statlinks.txt') if ' | ' in l}
w=csv.writer(open('research/data/12_oecd_haag2025_statlinks_long.csv','w',newline=''))
w.writerow(['statlink','figure','row_index','cells'])
for f in sorted(glob.glob(D+'*.xlsx')):
    code=os.path.basename(f)[:-5]
    ws=openpyxl.load_workbook(f,read_only=True,data_only=True).worksheets[0]
    for i,r in enumerate(ws.iter_rows(values_only=True)):
        cells=[str(round(c,3)) if isinstance(c,float) else str(c) for c in r if c is not None]
        if cells: w.writerow(['https://stat.link/'+code, links.get(code,'Figure 5.13. Waiting times for appointment with a GP or nurse, or a specialist, 2023' if code=='fcx732' else ''), i, ' | '.join(cells)])
print('ok')
