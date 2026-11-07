# -*- coding: utf-8 -*-
"""与网站里的 JS 导出逻辑一一对应：把一个模板（可带自定义值）导出成 HTML 站 / PHP 站 / JSON 站 / Elementor 包。
MCP 的 export_site / get_page 和 build.py 生成默认下载包都用它。"""
import io,json,math,re,zipfile
from html import escape as _e
import dlib
REFW=1440
KEYS=['primary','secondary','text','accent','surface','border']
CJK=",'Noto Sans SC','Noto Serif SC',sans-serif"
PT_EASE='cubic-bezier(.7,0,.2,1)'
def rnd(v): return int(math.floor(v+0.5))
def ns(v):
    v=float(v);return str(int(v)) if v==int(v) else str(v)
def px(v,d):
    m=re.search(r'([\d.]+)px',str(v or ''))
    return float(m.group(1)) if m else float(d)
def lum(h):
    n=int(h.lstrip('#'),16);a=[(n>>16)&255,(n>>8)&255,n&255];r=[]
    for v in a:
        v/=255;r.append(v/12.92 if v<=.03928 else ((v+.055)/1.055)**2.4)
    return .2126*r[0]+.7152*r[1]+.0722*r[2]
def onc(h): return '#111111' if lum(h)>.45 else '#ffffff'
def esc2(s): return s.replace('&','&amp;').replace('<','&lt;').replace('>','&gt;')
def settings(x,over=None):
    """x 的当前设定（等同 JS 里 st('template',x)），over 可覆盖：colors{} head body scale radius pad padU w wU pt ptdur"""
    over=over or {}
    t=dict(x['colors']);t.update(head=x['fonts']['head'],body=x['fonts']['body'],scale=100,radius=px(x['tok'].get('radius'),8),pad=px(x['tok'].get('pad'),88),padU='px',w=1300,wU='px',pt='none',ptdur=600)
    for k,v in (over.get('colors') or {}).items():
        if v: t[k]=v
    for k in ('head','body','scale','radius','pad','padU','w','wU','pt','ptdur'):
        if over.get(k) not in (None,''): t[k]=over[k]
    return t
def sizes(x,t):
    k=float(t['scale'])/100;T=x['tok'];base=px(T.get('pad'),88)
    pad=t['pad'] if t['padU']=='px' else rnd(base*float(t['pad'])/100)
    return dict(h1=f"{rnd(px(T.get('h1'),56)*k)}px",h2=f"{rnd(px(T.get('h2'),40)*k)}px",h3=f"{rnd(px(T.get('h3'),22)*k)}px",
        h1big=f"{rnd(px(T.get('h1big') or T.get('h1'),56)*k)}px",body=f"{rnd(px(T.get('fsb'),16)*k)}px",radius=f"{ns(t['radius'])}px",pad=f"{ns(pad)}px",w=f"{ns(t['w'])}{t['wU']}")
def tpl_vars(x,t):
    z=sizes(x,t);T=x['tok'];v={}
    for k in KEYS: v['--c-'+k]=t[k]
    v.update({'--radius':z['radius'],'--hlh':T.get('hlh'),'--hw':T.get('hw'),'--hcase':T.get('hcase'),'--hls':T.get('hls'),'--h1':z['h1'],'--h2':z['h2'],'--h3':z['h3'],'--h1big':z['h1big'],'--pad':z['pad'],'--ew':T.get('ew'),'--fs-body':z['body'],'--stat':T.get('stat'),'--w':z['w'],'--pt-dur':f"{ns(t['ptdur'])}ms",'--pt-ease':PT_EASE,'--pt-color':t['accent']})
    return v
def gfonts(t):
    fams=[]
    for f in (t['head'],t['body'],'Noto Sans SC'):
        if f not in fams: fams.append(f)
    return 'https://fonts.googleapis.com/css?family='+'|'.join(f.replace(' ','+')+':300,400,500,600,700,800' for f in fams)+'&display=swap'
def root_css(x,t,static=True):
    v=tpl_vars(x,t);v['--f-head']=f"'{t['head']}'{CJK}";v['--f-body']=f"'{t['body']}'{CJK}"
    if static:
        for k in ('primary','secondary','accent','surface'): v['--on-'+k]=onc(t[k])
    return ':root{\n'+'\n'.join(f'  {k}: {a};' for k,a in v.items())+'\n}'
_TR=None
def pt_css(slug):
    global _TR
    if _TR is None: _TR={t['slug']:t['css'] for t in dlib.load_transitions()}
    return _TR.get(slug,'')
def style_css(t):
    css=dlib.runtime_css().replace('main[data-page]{display:none}main[data-page].on{display:block}\n','')
    if t['pt']!='none': css+=f"\n/* page transition: {t['pt']} */\n"+pt_css(t['pt'])
    return css
def tokens_css(x,t): return f"/* {x['name']} — design tokens. Edit here, every page updates. */\n@import url('{gfonts(t)}');\n\n{root_css(x,t,True)}\n"
def href(slug,ext): return f'index.{ext}' if slug=='home' else f'{slug}.{ext}'
def links(html,fn): return re.sub(r'\{\{p:([\w-]+)\}\}',lambda m:fn(m.group(1)),html)
def label(x,slug): return next(p['label'] for p in x['pagelist'] if p['slug']==slug)
def page_file(x,t,slug,ext):
    pg=x['pages'].get(slug) or x['pages']['home']
    dk=' class="dk"' if lum(t['surface'])<.25 else ''
    return links(f"""<!doctype html>\n<html lang="en"><head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1">\n<title>{esc2(label(x,slug))} · {esc2(x['name'])}</title>\n<link rel="stylesheet" href="{gfonts(t)}">\n<style>\n{root_css(x,t,True)}\n{style_css(t)}</style>\n</head><body{dk}>\n{x['nav']}\n<main>{pg}</main>\n{x['foot']}\n</body></html>\n""",lambda s:href(s,ext))
def readme(x,kind):
    n=len(x['pages'])
    ph='- includes/header.php, includes/footer.php  ← shared header and footer\n- *.php  ← one file per page\n' if kind=='PHP' else '- *.html  ← one file per page\n'
    return f"# {x['name']}\n\nExported from Design Library · {n} pages · {kind}\n\n## Structure\n- assets/css/tokens.css  ← colours, fonts, sizes, content width, section spacing\n- assets/css/style.css   ← components and layout (uses the tokens)\n{ph}\n## Customise\nOpen assets/css/tokens.css and change the variables. Pages: {', '.join(p['label'] for p in x['pagelist'])}.\n\nAll text and images are placeholders — replace them with your own.\n"
def zip_html(x,t):
    f=[]
    for s in x['pages']:
        d=page_file(x,t,s,'html')
        d=re.sub(r'<style>[\s\S]*?</style>','<link rel="stylesheet" href="assets/css/tokens.css">\n<link rel="stylesheet" href="assets/css/style.css">',d,count=1)
        d=re.sub(r'<link rel="stylesheet" href="https://fonts[^>]*>\n','',d,count=1)
        f.append((href(s,'html'),d))
    f+=[('assets/css/tokens.css',tokens_css(x,t)),('assets/css/style.css',style_css(t)),('README.md',readme(x,'HTML'))]
    return f
def zip_php(x,t):
    q=lambda s:s.replace("'","\\'")
    nav=links(x['nav'],lambda s:href(s,'php'));foot=links(x['foot'],lambda s:href(s,'php'))
    dark='true' if lum(t['surface'])<.25 else 'false'
    f=[('includes/header.php',f"<?php\n// Usage in a page:  $title = 'About'; include 'includes/header.php';\n$title = $title ?? '{q(x['name'])}';\n$dark = {dark};\n?>\n<!doctype html>\n<html lang=\"en\"><head>\n<meta charset=\"utf-8\">\n<meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">\n<title><?= htmlspecialchars($title) ?> · {esc2(x['name'])}</title>\n<link rel=\"stylesheet\" href=\"assets/css/tokens.css\">\n<link rel=\"stylesheet\" href=\"assets/css/style.css\">\n</head><body<?= $dark ? ' class=\"dk\"' : '' ?>>\n{nav}\n<main>\n"),
       ('includes/footer.php',f"</main>\n{foot}\n</body></html>\n")]
    for s,h in x['pages'].items():
        f.append((href(s,'php'),f"<?php $title = '{q(label(x,s))}'; include 'includes/header.php'; ?>\n{links(h,lambda p:href(p,'php'))}\n<?php include 'includes/footer.php'; ?>\n"))
    f+=[('assets/css/tokens.css',tokens_css(x,t)),('assets/css/style.css',style_css(t)),('.htaccess','# Optional: serve /about instead of /about.php\nRewriteEngine On\nRewriteCond %{REQUEST_FILENAME} !-f\nRewriteCond %{REQUEST_FILENAME} !-d\nRewriteRule ^([a-z0-9-]+)/?$ $1.php [L]\n'),('README.md',readme(x,'PHP'))]
    return f
def el_globals(x,t):
    z=sizes(x,t)
    return json.dumps(dict(template=x['slug'],global_colors=dict(primary=t['primary'],secondary=t['secondary'],text=t['text'],accent=t['accent'],custom=dict(surface=t['surface'],border=t['border'])),global_fonts=dict(headings=t['head'],body=t['body']),sizes=dict(h1=z['h1'],h2=z['h2'],h3=z['h3'],body=z['body']),radius=z['radius'],section_padding=z['pad'],content_width=z['w'],pages=[p['slug'] for p in x['pagelist']]),indent=2,ensure_ascii=False)
def el_prompt(x,t):
    z=sizes(x,t);pg='\n'.join(f"- {p['label']} ({p['slug']}) — html/{p['slug']}.html" for p in x['pagelist'])
    return f"# Build \"{x['name']}\" in Elementor\n\nYou are working in WordPress with Elementor (Pro) through MCP. Recreate this template.\n\n## 1. Site Settings › Global Colors\nPrimary {t['primary']} · Secondary {t['secondary']} · Text {t['text']} · Accent {t['accent']} · Surface {t['surface']} · Border {t['border']}\n\n## 2. Global Fonts\nHeadings: {t['head']} · Body: {t['body']}\nH1 {z['h1']} / H2 {z['h2']} / H3 {z['h3']} / Body {z['body']}\n\n## 3. Layout\nContent width {z['w']} · Section padding {z['pad']} vertical · Border radius {z['radius']}\n\n## 4. Pages to create (use the HTML files in /html as the visual reference)\n{pg}\n\n## Rules\n- Bind every colour and font to the Global Colors / Fonts above. Never hard-code hex.\n- Use native widgets (Heading, Text, Button, Image Box, Icon List, Form). Use the HTML widget only for effects.\n- Build the header and footer once as Theme Builder templates; use the Menu widget for navigation.\n"
def el_kit(x,t):
    f=[('README.md',f"# {x['name']} — Elementor kit\n\n- global-style.json: colours, fonts, sizes\n- prompt-for-claude-code.md: paste into Claude Code (with your Elementor MCP) to build the site\n- html/: every page as standalone HTML — open in a browser for reference or paste into an Elementor HTML widget\n- tokens.css: Additional CSS for Elementor › Site Settings\n\nNote: this is not an Elementor .json import file. Elementor builds are best recreated with native widgets; the prompt and globals make that fast.\n"),('global-style.json',el_globals(x,t)),('prompt-for-claude-code.md',el_prompt(x,t)),('tokens.css',tokens_css(x,t))]
    for s in x['pages']: f.append((f'html/{s}.html',page_file(x,t,s,'html')))
    return f
def json_site(x,t):
    z=sizes(x,t);c={k:t[k] for k in KEYS}
    return json.dumps(dict(format='design-library-site@1',template=x['slug'],name=x['name'],tokens=dict(colors=c,fonts=dict(heading=t['head'],body=t['body']),sizes=dict(h1=z['h1'],h2=z['h2'],h3=z['h3'],body=z['body']),radius=z['radius'],section_padding=z['pad'],content_width=z['w']),
        page_transition=dict(name=t['pt'],duration_ms=t['ptdur'],css='' if t['pt']=='none' else pt_css(t['pt'])),taxonomy=dict(types=x['types'],industries=x['ind'],styles=x['styles']),nav_html=x['nav'],footer_html=x['foot'],css=style_css(t),
        pages=[dict(slug=p['slug'],label=p['label'],group=p['group'],html=x['pages'][p['slug']]) for p in x['pagelist']]),indent=2,ensure_ascii=False)
def make_zip(files):
    b=io.BytesIO()
    with zipfile.ZipFile(b,'w',zipfile.ZIP_DEFLATED) as z:
        for n,d in files: z.writestr(n,d)
    return b.getvalue()
def write_files(files,dest):
    from pathlib import Path
    dest=Path(dest);out=[]
    for n,d in files:
        p=dest/n;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(d,encoding='utf-8');out.append(str(p))
    return out

def raw_files(x):
    """导入的整页模板（format=documents）：原样导出，内部链接改成 .html"""
    return [(href(k,'html'),links(v,lambda q:href(q,'html'))) for k,v in x['pages'].items()]
