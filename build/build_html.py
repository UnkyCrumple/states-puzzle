import json, sys
sys.path.insert(0,'/home/claude/build')
import facts
levels=json.load(open('/home/claude/data/out/levels.json'))
meta={m['id']:m for m in facts.LEVELS_META}
out=[]; missing=[]
for lv in levels:
    m=meta[lv['id']]
    for p in lv['pieces']:
        name=facts.RENAME.get(p['label'],p['label']) if p['label'] else ''
        p['name']=name
        if p['role']=='tile':
            t,s,y=facts.fact_for(name)
            if t is None: missing.append((lv['id'],name))
            p['fact']=t; p['src']=s; p['year']=y; p['abbr']=facts.ABBR.get(name)
        p.pop('area_km2',None); p.pop('cat',None)
        p['label_pt']=p['label_pt']
    out.append(dict(id=lv['id'],tag=m['tag'],title=m['title'],intro=m['intro'],notes=m['notes'],pieces=lv['pieces']))
print('missing facts:',missing)
data=dict(levels=out,sources={str(k):v for k,v in facts.SOURCES.items()})
html=open('template.html').read().replace('/*DATA*/null',json.dumps(data,separators=(',',':'),ensure_ascii=False))
open('/home/claude/build/index.html','w').write(html)
print(len(html)//1024,'KB')
