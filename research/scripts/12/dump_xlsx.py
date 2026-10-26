import openpyxl,sys
for f in sys.argv[1:]:
    wb=openpyxl.load_workbook(f,read_only=True,data_only=True)
    ws=wb.worksheets[0]
    print('=====',f)
    for r in ws.iter_rows(values_only=True):
        r=[ (round(c,2) if isinstance(c,float) else c) for c in r if c is not None]
        if r: print(r[:16])
