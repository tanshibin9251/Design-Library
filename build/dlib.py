# -*- coding: utf-8 -*-
"""读取 library/ 的统一入口（build.py、catalog.py、site_export.py、MCP 都用它）。"""
import json,re
from pathlib import Path
HERE=Path(__file__).resolve().parent
ROOT=HERE.parent
LIB=ROOT/'library'
def read(p): return Path(p).read_text(encoding='utf-8')
def jload(p): return json.loads(read(p))
def taxonomy(): return jload(LIB/'taxonomy.json')
def palettes(): return jload(LIB/'palettes/palettes.json')
def runtime_css(): return read(LIB/'runtime/site.css')
def runtime_js(): return read(LIB/'runtime/preview.js')
def template_slugs():
    s=sorted(p.parent.name for p in (LIB/'templates').glob('*/template.json'))
    f=LIB/'templates'/'order.json'
    o=jload(f) if f.exists() else []
    return sorted(s,key=lambda a:o.index(a) if a in o else 999+s.index(a))
def load_template(slug,full=True):
    d=LIB/'templates'/slug
    if not (d/'template.json').exists(): return None
    m=jload(d/'template.json')
    x=dict(slug=m['slug'],name=m['name'],zh=m.get('zh',''),tag=m.get('tag',''),colors=m.get('colors',{}),fonts=m.get('fonts',{}),tok=m.get('tok',{}),
           types=m.get('types',[]),ind=m.get('industries',[]),styles=m.get('styles',[]),license=m.get('license','库内自有'),format=m.get('format','fragments'),
           pagelist=m['pages'],nav='',foot='')
    if x['format']=='fragments':
        x['nav']=read(d/'nav.html') if (d/'nav.html').exists() else ''
        x['foot']=read(d/'footer.html') if (d/'footer.html').exists() else ''
    homes={}
    for p in x['pagelist']:
        f=d/'pages'/f"{p['slug']}.html"
        if f.exists() and (full or p['slug']=='home'): homes[p['slug']]=read(f)
    x['pages']=homes
    x['dir']=d
    from template_enhance import enhance
    return enhance(x)
def load_effect(cat,slug):
    return jload(LIB/'effects'/cat/slug/'effect.json')
def load_effects():
    out=[]
    for f in sorted((LIB/'effects').glob('*/*/effect.json')):
        out.append(jload(f))
    o=jload(LIB/'effects'/'order.json') if (LIB/'effects'/'order.json').exists() else []
    out.sort(key=lambda e:o.index(e['slug']) if e['slug'] in o else 999)
    return out
def load_transitions():
    out=[]
    for f in sorted((LIB/'transitions').glob('*/transition.json')):
        t=jload(f);t['css']=read(f.parent/'transition.css');out.append(t)
    gi={g:i for i,g in enumerate(taxonomy()['transition_groups'])}
    out.sort(key=lambda t:gi.get(t['group'],9))   # 稳定排序，组内保持字母序以外的原顺序见 order.json
    order=LIB/'transitions'/'order.json'
    if order.exists():
        o=jload(order);out.sort(key=lambda t:o.index(t['slug']) if t['slug'] in o else 99)
    return out
# ---- Graphic 线（海报 / 缩略图 / 横幅 / 社交帖 / 产品图）：library/graphics/<slug>/{graphic.json, graphic.html, DESIGN.md}
def _lum(h):
    n=int(h[1:],16);a=[]
    for v in (n>>16&255,n>>8&255,n&255):
        v/=255;a.append(v/12.92 if v<=.03928 else ((v+.055)/1.055)**2.4)
    return .2126*a[0]+.7152*a[1]+.0722*a[2]
def on_color(h): return '#111111' if _lum(h)>.45 else '#ffffff'
def graphic_slugs():
    s=sorted(p.parent.name for p in (LIB/'graphics').glob('*/graphic.json'))
    f=LIB/'graphics'/'order.json'
    o=jload(f) if f.exists() else []
    return sorted(s,key=lambda a:o.index(a) if a in o else 999+s.index(a))
def load_graphic(slug):
    d=LIB/'graphics'/slug
    if not (d/'graphic.json').exists(): return None
    m=jload(d/'graphic.json')
    return dict(slug=m['slug'],name=m['name'],zh=m.get('zh',''),tag=m.get('tag',''),type=m['type'],size=m['size'],styles=m.get('styles',[]),ind=m.get('industries',[]),
                colors=m['colors'],fonts=m['fonts'],license=m.get('license','库内自有'),html=read(d/'graphic.html'),
                design=read(d/'DESIGN.md') if (d/'DESIGN.md').exists() else '',dir=d)
def load_graphics():
    return [load_graphic(s) for s in graphic_slugs()]
# ---- 素材库：library/assets/<类别>/<slug>/{asset.json, <file>}
def load_assets():
    out=[]
    for f in sorted((LIB/'assets').glob('*/*/asset.json')):
        m=jload(f);m['dir']=f.parent;m.setdefault('license','local_only');m.setdefault('tags',[]);m.setdefault('zh','')
        m['format']=m.get('format') or Path(m['file']).suffix.lstrip('.').lower()
        out.append(m)
    o=jload(LIB/'assets'/'order.json') if (LIB/'assets'/'order.json').exists() else []
    out.sort(key=lambda a:(o.index(a['slug']) if a['slug'] in o else 999,a['cat'],a['slug']))
    return out
def graphic_doc(g,colors=None,head=None,body=None):
    """一张图的完整独立 HTML（颜色 / 字体写成 :root 变量，可覆盖）。固定画布尺寸，用浏览器视口截图导出 PNG。"""
    c=dict(g['colors']);c.update({k:v for k,v in (colors or {}).items() if v})
    h=head or g['fonts']['head'];b=body or g['fonts']['body']
    fam='|'.join(f.replace(' ','+')+':300,400,500,600,700,800' for f in dict.fromkeys([h,b,'Noto Sans SC']))
    v=[f'--c-{k}:{x}' for k,x in c.items()]+[f'--on-{k}:{on_color(c[k])}' for k in ('primary','secondary','accent','surface')]
    v+=[f"--f-head:'{h}','Noto Sans SC','Noto Serif SC',sans-serif",f"--f-body:'{b}','Noto Sans SC','Noto Serif SC',sans-serif"]
    return (f'<!doctype html>\n<html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width={g["size"]["w"]}">\n'
            f'<title>{g["name"]} · {g["size"]["w"]}×{g["size"]["h"]}</title>\n<link rel="stylesheet" href="https://fonts.googleapis.com/css?family={fam}&display=swap">\n'
            f'<style>\n:root{{{";".join(v)}}}\nhtml,body{{margin:0;background:#fff}}\n</style></head><body>\n{g["html"]}\n</body></html>\n')
