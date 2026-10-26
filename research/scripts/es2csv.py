import json,sys,itertools,csv
d=json.load(open(sys.argv[1]))
ids=d['id'];size=d['size'];dims=d['dimension']
cats=[sorted(dims[i]['category']['index'].items(),key=lambda x:x[1]) for i in ids]
w=csv.writer(open(sys.argv[2],'w'));w.writerow(ids+['value','flag'])
st=d.get('status',{})
for combo in itertools.product(*cats):
    idx=0
    for (k,p),s in zip(combo,size): idx=idx*s+p
    v=d['value'].get(str(idx))
    if v is None: continue
    w.writerow([k for k,p in combo]+[v,st.get(str(idx),'')])
