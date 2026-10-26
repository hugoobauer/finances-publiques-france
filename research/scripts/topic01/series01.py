import csv
D='research/data/'
M={}
for r in csv.DictReader(open(D+'01_eurostat_gov_10a_main.csv')):
    M[(r['unit'],r['sector'],r['na_item'],r['geo'],int(r['time']))]=float(r['value'])
g=lambda u,i,geo,y,s='S13': M.get((u,s,i,geo,y))
out=csv.writer(open(D+'01_derived_fr_series_1995_2025.csv','w'))
hdr=['year','TE_bn','TE_pcgdp','TR_bn','TR_pcgdp','B9_bn','B9_pcgdp','interest_D41_pcgdp','primary_TE_pcgdp','EA20_TE_pcgdp','EU27_TE_pcgdp','gap_vs_EA20_pp','DE_TE','IT_TE','ES_TE','NL_TE','BE_TE','SE_TE','DK_TE']
out.writerow(hdr); print('|'+'|'.join(hdr)+'|')
for y in range(1995,2026):
    te=g('PC_GDP','TE','FR',y); ea=g('PC_GDP','TE','EA20',y); eu=g('PC_GDP','TE','EU27_2020',y); i=g('PC_GDP','D41PAY','FR',y)
    row=[y,round(g('MIO_EUR','TE','FR',y)/1000,1),te,round(g('MIO_EUR','TR','FR',y)/1000,1),g('PC_GDP','TR','FR',y),round(g('MIO_EUR','B9','FR',y)/1000,1),g('PC_GDP','B9','FR',y),i,round(te-i,1),ea,eu,round(te-ea,1)]+[g('PC_GDP','TE',c,y) for c in ['DE','IT','ES','NL','BE','SE','DK']]
    out.writerow(row); print('|'+'|'.join(str(x) for x in row)+'|')
# subsector consolidation 2025
s=sum(g('MIO_EUR','TE','FR',2025,ss) for ss in ['S1311','S1313','S1314']); print('sum subsectors 2025',round(s/1000,1),'consolidated',round(g('MIO_EUR','TE','FR',2025)/1000,1),'diff',round((s-g('MIO_EUR','TE','FR',2025))/1000,1))
for y in [1995,2005,2015,2025]:
    print(y,{ss:(round(g('MIO_EUR','TE','FR',y,ss)/1000,1), g('PC_GDP','TE','FR',y,ss)) for ss in ['S1311','S1313','S1314']})
for it in ['D1PAY','P2','D62PAY','D632PAY','D3PAY','D41PAY','P51G','D7PAY','D9PAY','D29PAY','OP5ANP']:
    print(it, [ (y, round(g('MIO_EUR',it,'FR',y)/1000,1), g('PC_GDP',it,'FR',y), g('PC_GDP',it,'EA20',y), g('PC_GDP',it,'EU27_2020',y)) for y in [1995,2005,2015,2025]])
