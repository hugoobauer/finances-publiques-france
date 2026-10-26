import sys, openpyxl
for p in sys.argv[1:]:
    wb = openpyxl.load_workbook(p, data_only=True, read_only=True)
    for ws in wb.worksheets:
        print("=====", p, ws.title)
        for row in ws.iter_rows(values_only=True):
            if any(c is not None for c in row):
                print(" | ".join("" if c is None else (f"{c:.3f}" if isinstance(c,float) else str(c)) for c in row))
