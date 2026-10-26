import json, sys, csv, itertools
src, dst = sys.argv[1], sys.argv[2]
d = json.load(open(src))
ids = d['id']; size = d['size']
dims = d['dimension']
labels = []
for i in ids:
    idx = dims[i]['category']['index']
    inv = sorted(idx.items(), key=lambda kv: kv[1])
    labels.append([k for k,_ in inv])
vals = d['value']
status = d.get('status', {})
with open(dst, 'w', newline='') as f:
    w = csv.writer(f); w.writerow(ids + ['value','flag'])
    # iterate only over present values
    strides = []
    s = 1
    for n in reversed(size):
        strides.insert(0, s); s *= n
    for k, v in (vals.items() if isinstance(vals, dict) else enumerate(vals)):
        k = int(k); rem = k; row = []
        for st, lab in zip(strides, labels):
            row.append(lab[rem // st]); rem %= st
        w.writerow(row + [v, status.get(str(k), '') if isinstance(status, dict) else ''])
print(d.get('updated'), dst)
