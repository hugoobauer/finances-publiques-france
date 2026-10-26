import sys, openpyxl
wb=openpyxl.load_workbook(sys.argv[1], data_only=True, read_only=True)
lim=int(sys.argv[2]) if len(sys.argv)>2 else 80
for ws in wb.worksheets:
    print('### sheet', ws.title)
    for i,row in enumerate(ws.iter_rows(values_only=True)):
        if i>=lim: break
        r=[x for x in row if x is not None]
        if r: print(i, r)
