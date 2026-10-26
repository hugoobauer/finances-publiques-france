import json
def load(path):
    d=json.load(open(path))
    dims=d['id']; sizes=d['size']
    cats=[sorted(d['dimension'][k]['category']['index'].items(), key=lambda x:x[1]) for k in dims]
    out={}
    for k,v in d['value'].items():
        k=int(k); idx=[]
        for s in reversed(sizes):
            idx.append(k%s); k//=s
        idx=idx[::-1]
        out[tuple(cats[i][idx[i]][0] for i in range(len(dims)))]=v
    return dims,out
