import json, sys, csv, itertools, statistics, os
src, out = sys.argv[1], sys.argv[2]
d = json.load(open(src))
dims = d['id']; sizes = d['size']
cats = [sorted(d['dimension'][k]['category']['index'].items(), key=lambda x: x[1]) for k in dims]
vals = d['value']
rows = []
for idx, combo in enumerate(itertools.product(*cats)):
    v = vals.get(str(idx))
    if v is None: continue
    rows.append({k: c[0] for k, c in zip(dims, combo)} | {'value': v})
with open(out, 'w', newline='') as f:
    w = csv.DictWriter(f, fieldnames=dims + ['value']); w.writeheader(); w.writerows(rows)
print(out, len(rows))
