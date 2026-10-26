import csv,statistics as st,sys
R=sys.argv[1]
s={}
for r in csv.DictReader(open(R+'/data/13_gg_employment_share_ilo_2000_2024.csv')): s.setdefault(r['geo'],{})[int(r['year'])]=float(r['gg_share_pct'])
EXCL={'CAN','ISR','PL','MEX','CRI','IE','HR'}  # ILO series inconsistent with OECD GaaG (>1 pt gap) -> excluded
EU=['AT','BE','BG','HR','CY','CZ','DK','EE','FI','FR','DE','EL','HU','IE','IT','LV','LT','LU','MT','NL','PL','PT','RO','SK','SI','ES','SE']
OECD=['AUS','AT','BE','CAN','CHL','COL','CRI','CZ','DK','EE','FI','FR','DE','EL','HU','IS','IE','ISR','IT','JPN','KOR','LV','LT','LU','MEX','NL','NZL','NO','PL','PT','SK','SI','ES','SE','CH','TUR','GBR','USA']
P=['FR','DE','IT','ES','NL','BE','SE','DK']
out=[]
for y0,y1 in [(2000,2023),(2005,2023),(2005,2022),(2007,2023)]:
  for g,L in [('EU27',EU),('OECD38',OECD),('Panel8',P)]:
    C=[c for c in L if c not in EXCL and y0 in s.get(c,{}) and y1 in s.get(c,{})]
    res=[g,y0,y1,len(C)]
    for y in (y0,y1):
        v={c:s[c][y] for c in C}; srt=sorted(v.values(),reverse=True)
        res+= [round(st.mean(v.values()),2),round(st.median(v.values()),2),round(v['FR'],2),srt.index(v['FR'])+1,round(v['FR']-st.mean(v.values()),2),round(v['FR']-st.median(v.values()),2)]
    res.append(' '.join(C)); out.append(res); print(res)
with open(R+'/data/13_gg_employment_balanced_gap.csv','w',newline='') as f:
    w=csv.writer(f); w.writerow(['group','y0','y1','n','mean_y0','median_y0','fr_y0','fr_rank_y0','fr_gap_mean_y0','fr_gap_median_y0','mean_y1','median_y1','fr_y1','fr_rank_y1','fr_gap_mean_y1','fr_gap_median_y1','countries'])
    w.writerows(out)
