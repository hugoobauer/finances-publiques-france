import sys, openpyxl, statistics as st
import os
wb=openpyxl.load_workbook(os.environ.get('PISA',sys.argv[1] if len(sys.argv)>1 else ''),data_only=True,read_only=True)
OECD=['Australia','Austria','Belgium','Canada','Chile','Colombia','Costa Rica','Czechia','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Iceland','Ireland','Israel','Italy','Japan','Korea','Latvia','Lithuania','Luxembourg','Mexico','Netherlands','New Zealand','Norway','Poland','Portugal','Slovak Republic','Slovenia','Spain','Sweden','Switzerland','Türkiye','United Kingdom','United States']
EU=['Austria','Belgium','Bulgaria','Croatia','Cyprus','Czechia','Denmark','Estonia','Finland','France','Germany','Greece','Hungary','Ireland','Italy','Latvia','Lithuania','Luxembourg','Malta','Netherlands','Poland','Portugal','Romania','Slovak Republic','Slovenia','Spain','Sweden']
PAN=['France','Germany','Italy','Spain','Netherlands','Belgium','Sweden','Denmark']
def table(name, col=1):
    ws=wb[name]; v={}
    for row in ws.iter_rows(values_only=True):
        r=[x for x in row if x is not None]
        if len(r)>col and isinstance(r[0],str) and isinstance(r[col],(int,float)):
            v[r[0].rstrip('*').strip()]=r[col]
    return v
def stats(v,grp,label,desc=True):
    d={c:v[c] for c in grp if c in v}
    missing=[c for c in grp if c not in v]
    s=sorted(d.values(),reverse=desc)
    return '%s n=%d mean %.1f med %.1f FRrank %d %s'%(label,len(d),st.mean(s),st.median(s),s.index(d['France'])+1, ('missing '+str(missing)) if missing else '')
if __name__=='__main__':
    for t in sys.argv[2:]:
        v=table(t); print(t,'FR',round(v['France'],1),'OECD avg',round(v.get('OECD average',0),1))
        for g,l in [(OECD,'OECD'),(EU,'EU'),(PAN,'PAN')]: print('  ',stats(v,g,l))
