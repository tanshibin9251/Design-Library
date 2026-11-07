import hashlib,pathlib,json,sys
r=pathlib.Path('public_html')
d={f.relative_to(r).as_posix():hashlib.md5(f.read_bytes()).hexdigest() for f in r.rglob('*') if f.is_file() and '.vscode' not in f.parts}
if sys.argv[1]=='save':
    json.dump(d,open('_work/snap_cur.json','w')); print('saved',len(d))
else:
    old=json.load(open('_work/snap_cur.json'))
    add=[k for k in d if k not in old]; dele=[k for k in old if k not in d]
    mod=[k for k in d if k in old and d[k]!=old[k] and not k.endswith('.zip')]
    z=[k for k in d if k in old and d[k]!=old[k] and k.endswith('.zip')]
    print('added dirs/files:'); 
    seen=set()
    for k in add:
        p='/'.join(k.split('/')[:3]) if k.startswith('api/templates') else k
        if p not in seen: seen.add(p); print('  +',p)
    print('deleted',dele); print('modified',mod); print('zip byte-diff only',len(z))
