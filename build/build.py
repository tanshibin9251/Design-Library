# -*- coding: utf-8 -*-
"""Design Library 构建器：library/ → public_html/（可直接上传 Hostinger）。

用法：  python build/build.py            生成 public_html/ 与 library/catalog.json
        python build/build.py --serve    生成后本地预览 http://localhost:8080（有 php 用 php，没有就用 Python 静态预览）
内容全部来自 library/（templates / effects / transitions / palettes / taxonomy.json），新增内容后重跑即可。
"""
import json, os, stat, shutil, sys, subprocess, webbrowser, hashlib, zipfile, datetime
from html import escape as e
from pathlib import Path
import dlib, catalog, paths as PT, site_export as SE, ui_icons
from dlib import ROOT, LIB, read

OUT = ROOT / "public_html"
SRC = Path(__file__).resolve().parent / "src"
SITE_DESC = "Design Library — website templates, effects and page transitions, plus graphic designs (posters, thumbnails, banners, product images), to preview, recolour and export."


def _writable(func, path, exc):
    """Google Drive marks folders read-only; clear the flag and retry."""
    os.chmod(path, stat.S_IWRITE)
    func(path)


def rmtree(p):
    shutil.rmtree(p, onexc=_writable)


def _unlink(p):
    try:
        p.unlink()
    except PermissionError:
        os.chmod(p, stat.S_IWRITE)
        p.unlink()

def w(p, text, binary=False):
    p = Path(p); p.parent.mkdir(parents=True, exist_ok=True)
    if binary: p.write_bytes(text)
    else: p.write_text(text, encoding="utf-8")


def js_safe(s):
    """放进 <script> 里的 JSON：转义 </ 和 <!--，仍是合法 JSON。"""
    return s.replace("</", "<\\/").replace("<!--", "<\\u0021--")


def guide_html(cat):
    c = cat["counts"]
    def pre(t): return f'<div class="gc"><button data-gcopy>Copy</button><pre>{e(t)}</pre></div>'
    return f"""<h1>Guide</h1>
<p>Everything in this library is plain HTML, CSS and a little JavaScript. Browse it here, change colours, fonts, width and spacing, then copy the code or download a whole site.</p>
<table><tr><th>Templates</th><th>Effects</th><th>Page transitions</th><th>Palettes</th><th>Graphics</th></tr><tr><td>{c['template']} multi-page sites</td><td>{c['effect']} in {sum(1 for x in cat['taxonomy']['effect_cats'])} categories</td><td>{c['transition']}</td><td>{c['palette']}</td><td>{c.get('graphic', 0)} designs</td></tr></table>
<p>The library has two sides: <b>Website</b> (templates, effects, page transitions) and <b>Graphic</b> (posters, thumbnails, banners, product images). Palettes are shared. Use the Website / Graphic switch at the top.</p>
<h2>1 · Use it from VS Code with Claude Code (MCP)</h2>
<p>The <code>mcp-server/</code> folder in the project lets Claude Code read this library directly. Put a <code>.mcp.json</code> in your website project:</p>
{pre('{\n  "mcpServers": {\n    "design-library": {\n      "command": "python",\n      "args": ["/path/to/Design Library/mcp-server/server.py"]\n    }\n  }\n}')}
<p>Install once: <code>pip install -r "Design Library/mcp-server/requirements.txt"</code>. Then just ask:</p>
<ul><li>“Find a template for a dental clinic and export it as a PHP site into <code>./site</code>, primary colour #0E7490.”</li><li>“Add the <code>pricing-toggle</code> effect to my pricing page.”</li><li>“Use the <code>push</code> page transition across the whole site.”</li><li>“Give me Elementor Global Colors for <code>calm-spa</code>.”</li></ul>
<p>Tools: <code>library_overview</code> · <code>search_library</code> · <code>get_template</code> · <code>get_page</code> · <code>export_site</code> · <code>get_effect</code> · <code>get_transition</code> · <code>get_palettes</code> · <code>get_style</code> · <code>get_elementor_item</code>.</p>
<h2>2 · Use the JSON API (no install)</h2>
<p>Everything below is a plain file on this site. Claude Code can fetch it with a link.</p>
{pre('/api/catalog.json                       whole library: names, tags, pages, tokens\n/api/website/templates/<group>/<slug>/<slug>.json       one template with every page (preview format)\n/api/website/templates/<group>/<slug>/<slug>.site.json  portable site file (design-library-site@1)\n/api/website/templates/<group>/<slug>/<slug>-html-site.zip     ready-to-upload HTML site\n/api/website/templates/<group>/<slug>/<slug>-php-site.zip      ready-to-upload PHP site\n/api/website/templates/<group>/<slug>/<slug>-elementor-kit.zip globals + Claude Code prompt + reference HTML\n/api/website/effects/<effect-group>/<category>/<slug>.html     effect snippet\n/api/website/transitions/<group>/<slug>.css             page-transition CSS\n(old flat paths still redirect; see api/.htaccess)\n/api/palettes.json  /api/taxonomy.json')}
<h2>3 · Add your own templates</h2>
<p>In the project folder, <code>CLAUDE.md</code> explains how to ask Claude Code to collect templates from another folder or from a connection you give it. Under the hood it runs:</p>
{pre('python tools/ingest_template.py <folder | .zip | .site.json> --slug my-site --name "My Site" \\\n    --types company,landing --ind restaurant --styles warm,playful\npython build/build.py')}
<p>Templates exported from this site (<code>.site.json</code>) keep full colour/font customisation. Finished sites imported from elsewhere are shown as <b>Imported</b> templates: browse and download, but colours are edited in their own CSS.</p>
<h2>4 · Page transitions</h2>
<p>Built on the View Transitions API: multi-page sites use <code>@view-transition {{ navigation: auto }}</code>. Works in Chrome / Edge 126+ and Safari 18.2+; other browsers simply navigate normally. Choose one in a template’s <b>Customize › Page transition</b>; it is included in the export.</p>
<h2>5 · Elementor</h2>
<p>The Elementor download is a kit — global colours and fonts, a ready-made prompt for Claude Code, <code>tokens.css</code> and every page as reference HTML. It is not an Elementor import file; rebuild with native widgets through your Elementor MCP.</p>
<h2>6 · Graphic designs</h2>
<p>Each graphic is a fixed-size HTML/CSS composition (poster 1200×1697, YouTube thumbnail 1280×720, banner 1500×500, product image 1080×1080 …) with a <code>DESIGN.md</code> recipe: layout traits, a “don’t” list and copy tone. Open one, recolour it, copy the HTML, then ask Claude Code to make a new design from the recipe. Export PNG by screenshotting the page at its exact size.</p>
{pre('/api/graphic/designs/<type>/<slug>.json   meta + HTML + DESIGN recipe\n/api/graphic/designs/<type>/<slug>.html   standalone page at exact canvas size')}
<h2>Licence</h2>
<p>Templates, effects and transitions in this library are self-made, with placeholder text and no third-party code. Fonts load from Google Fonts. Replace all placeholder copy and images.</p>"""


PV_HASH = {}
TPL_GROUP = {}
FX_DETAIL = {}
FX_PATH = {}
_lm = LIB / "runtime/live-map.json"
LIVE_MAP = json.loads(_lm.read_text(encoding="utf-8")) if _lm.exists() else {}


def live_for(x):
    """哪些「活起来」模块用在这个模板的预览里：先看 live-map.json 的人工指定，否则按风格自动挑。"""
    if x["slug"] in LIVE_MAP: return LIVE_MAP[x["slug"]]
    m = ["reveal", "count", "lift", "progress"]
    st, ty = set(x.get("styles", [])), set(x.get("types", []))
    if st & {"bold", "neobrutal", "maximal", "y2k", "playful"}: m += ["headline", "tilt"]
    if st & {"elegant", "editorial", "photo", "darkluxury", "artdeco"}: m += ["parallax", "headline"]
    if st & {"dark", "futuristic", "glass", "aurora", "bento"}: m += ["magnetic", "cursor"]
    if st & {"minimal", "japanese", "swiss", "scandi", "typographic", "monochrome"}: m += ["headline"]
    if "ecommerce" in ty: m += ["magnetic"]
    return list(dict.fromkeys(m))
_pvf = LIB / "previews" / "hashes.json"
if _pvf.exists():
    try: PV_HASH.update(json.loads(_pvf.read_text(encoding="utf-8")))
    except Exception: pass


def build_manifest(cat):
    tax = dlib.taxonomy(); pal = dlib.palettes()
    tpls = []
    for s in dlib.template_slugs():
        x = dlib.load_template(s, full=False); x.pop("dir")
        if x["license"] == "local_only": continue          # 授权不允许公开分发：只留在本地库，不进 public_html
        x["live"] = live_for(x)
        x["pg"] = PT.template_group(x["ind"], s)           # template group: api/templates/<pg>/<slug>, previews/templates/<pg>/<slug>.jpg
        if PV_HASH.get("t-" + s) and (LIB / "previews" / "templates" / x["pg"] / f"{s}.jpg").exists():
            x["pv"] = PV_HASH["t-" + s]                    # 有静态缩略图：首页不再内联 nav / foot / home，点开时再读 api/templates
            for k in ("nav", "foot", "pages"): x.pop(k, None)
        tpls.append(x)
    fx = []
    FX_DETAIL.clear(); FX_PATH.clear()
    for f in dlib.load_effects():
        d = dict(slug=f["slug"], cat=f["cat"], eg=PT.effect_group(f["cat"]), name=f["name"], zh=f["zh"], tech=f["tech"], tag=f["tag"], bleed=f.get("bleed", False), css=f["css"], html=f["html"], js=f.get("js", ""))
        if PV_HASH.get("e-" + f["slug"]) and (LIB / "previews" / "effects" / d["eg"] / f["cat"] / f"{f['slug']}.jpg").exists():
            FX_DETAIL[f["slug"]] = dict(css=d.pop("css"), html=d.pop("html"), js=d.pop("js"))
            FX_PATH[f["slug"]] = f"{d['eg']}/{f['cat']}/{f['slug']}.json"
            d["pv"] = PV_HASH["e-" + f["slug"]]; d["slim"] = True
        fx.append(d)
    gfx = [dict(slug=g["slug"], name=g["name"], zh=g["zh"], tag=g["tag"], type=g["type"], size=g["size"], styles=g["styles"], ind=g["ind"], colors=g["colors"], fonts=g["fonts"], html=g["html"], design=g["design"])
           for g in dlib.load_graphics() if g["license"] != "local_only"]
    ast = [dict(slug=a["slug"], name=a["name"], zh=a["zh"], cat=a["cat"], format=a["format"], w=a["width"], h=a["height"], tags=a["tags"], recolor=bool(a.get("recolor")), file=a["file"])
           for a in dlib.load_assets() if a["license"] != "local_only"]
    trs = [dict(slug=t["slug"], name=t["name"], zh=t["zh"], tag=t["tag"], group=t["group"], css=t["css"]) for t in dlib.load_transitions()]
    return dict(templates=tpls, graphics=gfx, assets=ast, acats=tax["asset_cats"], agroups=tax["asset_groups"], gtypes=tax["graphic_types"], domains=tax["domains"], transitions=trs, ptgroups=tax["transition_groups"], effects=fx, palettes=pal["palettes"], pcats=pal["cats"], ecats=tax["effect_cats"], egroups=tax["effect_groups"],
                types=[[t["id"], t["name"]] for t in tax["types"]], inds=tax["industries"], styletax=tax["styles"], css=dlib.runtime_css(), runtime=dlib.runtime_js(),
                fxbase=read(LIB / "runtime/fx-demo.html"), ptbase=read(LIB / "runtime/pt-demo.html"), ptbaseAuto=read(LIB / "runtime/pt-demo-auto.html"), guide=guide_html(cat),
                livejs=read(LIB / "runtime/live.js"), livecss=read(LIB / "runtime/live.css"))


INDEX_PHP = r"""<?php
// Design Library — entry point. Serves the app shell with the library index inlined; template pages load from /api/.
declare(strict_types=1);
$root = __DIR__;
$manifestFile = $root . '/data/manifest.json';
$shellFile = $root . '/includes/shell.html';
if (!is_file($manifestFile) || !is_file($shellFile)) {
    http_response_code(500);
    header('Content-Type: text/plain; charset=utf-8');
    exit("Design Library: data files are missing. Upload the whole folder (data/, includes/, assets/, api/), or run: python build/build.py");
}
$cssV = (string) @filemtime($root . '/assets/app.css');
$jsV  = (string) @filemtime($root . '/assets/app.js');
$etag = '"dl-' . filemtime($manifestFile) . '-' . $cssV . '-' . $jsV . '"';
header('ETag: ' . $etag);
header('Cache-Control: no-cache');
if (($_SERVER['HTTP_IF_NONE_MATCH'] ?? '') === $etag) { http_response_code(304); exit; }
header('Content-Type: text/html; charset=utf-8');
header('X-Content-Type-Options: nosniff');
header('Referrer-Policy: strict-origin-when-cross-origin');
header('X-Frame-Options: SAMEORIGIN');
if (extension_loaded('zlib') && !ini_get('zlib.output_compression')) { ob_start('ob_gzhandler'); }
echo strtr((string) file_get_contents($shellFile), [
    '{{CSS_V}}' => $cssV,
    '{{JS_V}}'  => $jsV,
    '{{DATA}}'  => (string) file_get_contents($manifestFile),
]);
"""

SHELL = """<!doctype html>
<html lang="en" data-theme="dark"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Design Library</title><meta name="description" content="%(desc)s"><meta name="robots" content="noindex,nofollow">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<script>try{var t=localStorage.getItem('theme');if(t)document.documentElement.setAttribute('data-theme',t)}catch(e){}</script>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Lora:wght@400;500;600;700&family=Mulish:wght@400;500;600;700&family=Noto+Serif+SC:wght@400;600&family=Noto+Sans+SC:wght@400;500;700&display=swap">
<link rel="stylesheet" href="assets/app.css?v={{CSS_V}}">
</head><body>
%(sprite)s<div id="app"></div><div class="toast" id="toast"></div>
<noscript><div class="ns"><h1>%(logo)s</h1><p>This library needs JavaScript to preview templates. The raw files are available at <a href="api/catalog.json">api/catalog.json</a>.</p></div></noscript>
<script>window.DL_DATA={{DATA}};</script>
<script src="assets/app.js?v={{JS_V}}"></script>
</body></html>
""" % dict(desc=e(SITE_DESC), sprite=ui_icons.sprite()[0], logo=ui_icons.logo_svg())

HTACCESS = """# Design Library — Hostinger / Apache / LiteSpeed
Options -Indexes
DirectoryIndex index.php
AddDefaultCharset UTF-8
AddType application/json .json
AddType image/svg+xml .svg

<IfModule mod_deflate.c>
  AddOutputFilterByType DEFLATE text/html text/css text/plain application/javascript application/json image/svg+xml
</IfModule>

<IfModule mod_headers.c>
  Header always set X-Content-Type-Options "nosniff"
  Header always set Referrer-Policy "strict-origin-when-cross-origin"
  <FilesMatch "\\.(css|js|svg)$">
    Header set Cache-Control "public, max-age=31536000, immutable"
  </FilesMatch>
  <FilesMatch "\\.(json|zip)$">
    Header set Cache-Control "public, max-age=300"
  </FilesMatch>
</IfModule>

# keep source/data folders private (the app reads them through PHP)
RewriteEngine On
RewriteRule ^(data|includes)(/|$) - [F,L]
"""
API_HTACCESS = """# public read-only JSON / downloads, usable from any page or tool
<IfModule mod_headers.c>
  Header set Access-Control-Allow-Origin "*"
</IfModule>
"""
DENY = "# private folder\n<IfModule mod_authz_core.c>\n  Require all denied\n</IfModule>\n<IfModule !mod_authz_core.c>\n  Deny from all\n</IfModule>\n"
FAVICON = ui_icons.favicon()


def write_index(cat):
    """library/INDEX.md：生成物，列出库里所有内容（不要手改）。"""
    tax = cat["taxonomy"]; yl = {t["id"]: t["name"] for t in tax["styles"]}; il = {t["id"]: t["name"] for t in tax["industries"]}
    L = ["# 总索引（自动生成，不要手改）", "", "> 重新生成：`python build/build.py`。想看着选：打开网站；让 Claude Code 选：见 `CLAUDE.md`（MCP 或 /api/）。", "",
         "## 🌐 Website 网站（模板 · 效果 · 页面转场 · Elementor）", "", f"### 模板（{cat['counts']['template']}）", "", "| 模板 | 页数 | 行业 | 风格 | 格式 |", "|---|---|---|---|---|"]
    for i in cat["items"]:
        if i["kind"] == "template":
            L.append(f"| [{i['name']}](./templates/{i['slug']}/TEMPLATE.md)（`{i['slug']}`） | {i['page_count']} | {', '.join(il.get(x, x) for x in i['industries'])} | {', '.join(yl.get(x, x) for x in i['styles'])} | {'完整可定制' if i['format'] == 'fragments' else 'Imported 整页'} |")
    L += ["", f"### 效果（{cat['counts']['effect']}）", ""]
    for c in tax["effect_cats"]:
        fx = [i for i in cat["items"] if i["kind"] == "effect" and i["category"] == c["id"]]
        L.append(f"- **{c['name']}**（`{c['id']}`，{len(fx)}）：" + "、".join(f"[{i['name']}](./effects/{c['id']}/{i['slug']}/EFFECT.md)" for i in fx))
    L += ["", f"### 页面转场（{cat['counts']['transition']}）", ""]
    for g in tax["transition_groups"]:
        L.append(f"- **{g}**：" + "、".join(f"{i['name']}（`{i['slug']}`）" for i in cat["items"] if i["kind"] == "transition" and i["group"] == g))
    L += ["", f"### 色板（{cat['counts']['palette']}，两条线共用）", "", "、".join(f"{c['name']} {c['count']}" for c in cat["palette_categories"]), "",
          "### Elementor（仅本地，Envato 来源，不对外）", "", "| 类型 | 名称 | 需要 |", "|---|---|---|"]
    for i in cat["items"]:
        if i["kind"] in ("kit", "part"):
            L.append(f"| {i['kind']} | {i['name']} | {'、'.join(i.get('needs', []))} |")
    gt = {t["id"]: t["name"] for t in tax["graphic_types"]}
    L += ["", f"## 🖼 Graphic 平面设计（{cat['counts'].get('graphic', 0)}）", "", "| 设计 | 类型 | 尺寸 | 风格 | 行业 |", "|---|---|---|---|---|"]
    for i in cat["items"]:
        if i["kind"] == "graphic":
            L.append(f"| [{i['name']}](./graphics/{i['slug']}/DESIGN.md)（`{i['slug']}`） | {gt.get(i['graphic_type'], i['graphic_type'])} | {i['size']['w']}×{i['size']['h']} | {', '.join(yl.get(x, x) for x in i['styles'])} | {', '.join(il.get(x, x) for x in i['industries'])} |")
    at = {c["id"]: c["name"] for c in tax["asset_cats"]}
    L += ["", f"### 素材库 Assets（{cat['counts'].get('asset', 0)}，Graphic 领域）", ""]
    for c in tax["asset_cats"]:
        xs = [i for i in cat["items"] if i["kind"] == "asset" and i["category"] == c["id"]]
        if xs: L.append(f"- **{c['name']}**（`{c['id']}`，{len(xs)}）：" + "、".join(f"{i['name']}（`{i['slug']}`）" for i in xs))
    (LIB / "INDEX.md").write_text("\n".join(L) + "\n", encoding="utf-8")


def build(quiet=False):
    if OUT.exists():                                         # 只清子项并保留 .vscode（sftp.json 不能被 build 删掉）
        for ch in OUT.iterdir():
            if ch.name == ".vscode": continue
            rmtree(ch) if ch.is_dir() else _unlink(ch)
    full_cat = catalog.write_catalog()                       # library/catalog.json（含 Elementor kit/part，仅本地）
    write_index(full_cat)
    cat = catalog.make_catalog(public=True)                  # 对外 /api/ 用，不含 local_only
    man = build_manifest(cat)
    w(OUT / "data/manifest.json", js_safe(json.dumps(man, ensure_ascii=False, separators=(",", ":"))))
    for slug, dd in FX_DETAIL.items():
        w(OUT / f"api/website/fx/{FX_PATH[slug]}", json.dumps(dd, ensure_ascii=False, separators=(",", ":")))
    pvdir = LIB / "previews"
    for kind in ("templates", "effects"):                     # same folder structure as api/
        for f in sorted((pvdir / kind).rglob("*.jpg")):
            dst = OUT / "previews" / "website" / f.relative_to(pvdir)
            dst.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy(f, dst)
    w(OUT / "data/.htaccess", DENY); w(OUT / "includes/.htaccess", DENY)
    w(OUT / "includes/shell.html", SHELL)
    w(OUT / "index.php", INDEX_PHP)
    w(OUT / ".htaccess", HTACCESS); w(OUT / "api/.htaccess", API_HTACCESS)
    w(OUT / "robots.txt", "User-agent: *\nDisallow: /\n")
    (OUT / "assets").mkdir(parents=True, exist_ok=True)
    shutil.copy(SRC / "app.js", OUT / "assets/app.js")
    shutil.copy(SRC / "app.css", OUT / "assets/app.css"); w(OUT / "assets/favicon.svg", FAVICON)
    # ---- api
    tax = dlib.taxonomy(); pal = dlib.palettes()
    w(OUT / "api/catalog.json", json.dumps(cat, ensure_ascii=False))
    w(OUT / "api/taxonomy.json", json.dumps(tax, ensure_ascii=False, indent=1)); w(OUT / "api/palettes.json", json.dumps(pal, ensure_ascii=False))
    for s in dlib.template_slugs():
        x = dlib.load_template(s, full=True); d = x.pop("dir")
        if x["license"] == "local_only": continue
        tr = PT.tpl_rel(s, x.get("ind") or x.get("industries"))
        TPL_GROUP[s] = tr.split("/")[0]
        w(OUT / f"api/website/templates/{tr}/{s}.json", json.dumps(x, ensure_ascii=False, separators=(",", ":")))
        if x["format"] == "fragments":
            t = SE.settings(x)
            w(OUT / f"api/website/templates/{tr}/{s}-html-site.zip", SE.make_zip(SE.zip_html(x, t)), True)
            w(OUT / f"api/website/templates/{tr}/{s}-php-site.zip", SE.make_zip(SE.zip_php(x, t)), True)
            w(OUT / f"api/website/templates/{tr}/{s}-elementor-kit.zip", SE.make_zip(SE.el_kit(x, t)), True)
            w(OUT / f"api/website/templates/{tr}/{s}.site.json", SE.json_site(x, t))
        else:
            w(OUT / f"api/website/templates/{tr}/{s}-site.zip", SE.make_zip(SE.raw_files(x)), True)
    for f in dlib.load_effects():
        w(OUT / f"api/website/effects/{PT.effect_rel(f['cat'], f['slug'], 'html')}", read(LIB / "effects" / f["cat"] / f["slug"] / "snippet.html"))
    for t in dlib.load_transitions():
        w(OUT / f"api/website/transitions/{PT.transition_group(t['group'])}/{t['slug']}.css", t["css"])
    gtypes = {t["id"] for t in tax["graphic_types"]}
    for g in dlib.load_graphics():
        if g["type"] not in gtypes: raise SystemExit(f"× 图 {g['slug']} 的类型 {g['type']} 不在 taxonomy.graphic_types 里")
        if g["license"] == "local_only": continue
        gd = {k: g[k] for k in ("slug", "name", "zh", "tag", "type", "size", "styles", "ind", "colors", "fonts", "html", "design")}
        w(OUT / f"api/graphic/designs/{g['type']}/{g['slug']}.json", json.dumps(gd, ensure_ascii=False, separators=(",", ":")))
        w(OUT / f"api/graphic/designs/{g['type']}/{g['slug']}.html", dlib.graphic_doc(g))
    acats = {c["id"] for c in tax["asset_cats"]}
    for a in dlib.load_assets():
        if a["cat"] not in acats: raise SystemExit(f"× 素材 {a['slug']} 的类别 {a['cat']} 不在 taxonomy.asset_cats 里")
        if a["license"] == "local_only": continue
        w(OUT / f"api/graphic/assets/{a['cat']}/{a['file']}", (a["dir"] / a["file"]).read_bytes(), True)
    write_redirects()
    w(OUT / "api/index.json", json.dumps(dict(name="Design Library API", counts=cat["counts"], endpoints=["catalog.json", "taxonomy.json", "palettes.json", "website/templates/<group>/<slug>/<slug>.json", "website/templates/<group>/<slug>/<slug>.site.json", "website/templates/<group>/<slug>/<slug>-html-site.zip", "website/templates/<group>/<slug>/<slug>-php-site.zip", "website/templates/<group>/<slug>/<slug>-elementor-kit.zip", "website/effects/<effect-group>/<category>/<slug>.html", "website/transitions/<group>/<slug>.css", "graphic/designs/<type>/<slug>.json", "graphic/designs/<type>/<slug>.html", "graphic/assets/<category>/<file>"]), indent=1))
    n = sum(1 for _ in OUT.rglob("*") if _.is_file())
    size = sum(f.stat().st_size for f in OUT.rglob("*") if f.is_file()) / 1e6
    if not quiet: print(f"public_html 已生成：{n} 个文件 · {size:.1f} MB · 模板 {cat['counts']['template']} · 效果 {cat['counts']['effect']} · 转场 {cat['counts']['transition']} · 色板 {cat['counts']['palette']} · 图 {cat['counts'].get('graphic', 0)} · 素材 {cat['counts'].get('asset', 0)}")
    return cat


TEXT_EXT = {".json", ".html", ".css", ".js", ".php", ".md", ".txt", ".svg", ".xml"}
LAST = ROOT / "_work" / "last_uploaded.json"
UPLOAD = ROOT / "_work" / "upload"


def write_redirects():
    """Every older URL keeps working via 301: flat (api/templates/<slug>/...), grouped-but-unprefixed (api/templates/<group>/<slug>/...) and previews/t-<slug>.jpg."""
    tax = dlib.taxonomy()
    cats = sorted({c["id"] for c in tax["effect_cats"]})
    PT.check_no_clash(list(TPL_GROUP), cats)
    R = ["", "<IfModule mod_rewrite.c>", "RewriteEngine On"]
    for s, g in sorted(TPL_GROUP.items()):                    # oldest: api/templates/<slug>/...
        R.append(f"RewriteRule ^templates/{s}/(.*)$ website/templates/{g}/{s}/$1 [R=301,L]")
    for c in tax["effect_cats"]:                              # oldest: api/effects/<cat>/...
        R.append(f"RewriteRule ^effects/{c['id']}/(.*)$ website/effects/{PT.slugify(c['group'])}/{c['id']}/$1 [R=301,L]")
    for slug, path in sorted(FX_PATH.items()):
        R.append(f"RewriteRule ^fx/{slug}\\.json$ website/fx/{path} [R=301,L]")
    for t in dlib.load_transitions():
        R.append(f"RewriteRule ^transitions/{t['slug']}\\.css$ website/transitions/{PT.transition_group(t['group'])}/{t['slug']}.css [R=301,L]")
    for d in ("templates", "effects", "fx", "transitions"):    # previous: api/<d>/<group>/...
        R.append(f"RewriteRule ^{d}/(.*)$ website/{d}/$1 [R=301,L]")
    R.append("RewriteRule ^graphics/(.*)$ graphic/designs/$1 [R=301,L]")
    R.append("</IfModule>")
    w(OUT / "api/.htaccess", API_HTACCESS + "\n".join(R) + "\n")
    P = ["# old preview URLs -> previews/website/...", "<IfModule mod_rewrite.c>", "RewriteEngine On"]
    for s, g in sorted(TPL_GROUP.items()):
        P.append(f"RewriteRule ^t-{s}\\.jpg$ website/templates/{g}/{s}.jpg [R=301,L]")
    for f in dlib.load_effects():
        P.append(f"RewriteRule ^e-{f['slug']}\\.jpg$ website/effects/{PT.effect_group(f['cat'])}/{f['cat']}/{f['slug']}.jpg [R=301,L]")
    P.append("RewriteRule ^templates/(.*)$ website/templates/$1 [R=301,L]")
    P.append("RewriteRule ^effects/(.*)$ website/effects/$1 [R=301,L]")
    P.append("</IfModule>")
    w(OUT / "previews/.htaccess", "\n".join(P) + "\n")


def content_hash(p):
    """Hash of what a file means: CRLF-insensitive for text, CRC list for zips (zip bytes differ on every build)."""
    if p.suffix == ".zip":
        h = hashlib.md5()
        with zipfile.ZipFile(p) as z:
            for i in sorted(z.infolist(), key=lambda i: i.filename):
                h.update(f"{i.filename}:{i.CRC}".encode())
        return h.hexdigest()
    b = p.read_bytes()
    if p.suffix.lower() in TEXT_EXT or p.name == ".htaccess":
        b = b.replace(b"\r\n", b"\n")
    return hashlib.md5(b).hexdigest()


def snapshot():
    return {f.relative_to(OUT).as_posix(): content_hash(f) for f in sorted(OUT.rglob("*")) if f.is_file() and ".vscode" not in f.relative_to(OUT).parts}


def folder_of(rel):
    parts = rel.split("/")
    if rel.startswith("api/website/templates/") and len(parts) >= 6: return "/".join(parts[:5]) + "/"
    if len(parts) >= 2: return "/".join(parts[:-1]) + "/"
    return rel


def make_delta():
    """Only files that are new / changed since the last --mark-uploaded, laid out exactly as on the server, in _work/upload/files/."""
    snap = snapshot()
    last = json.loads(LAST.read_text(encoding="utf-8")) if LAST.exists() else None
    if UPLOAD.exists(): rmtree(UPLOAD)
    new = [k for k in snap if last is None or k not in last]
    mod = [k for k in snap if last is not None and k in last and last[k] != snap[k]]
    dele = [k for k in (last or {}) if k not in snap]
    for k in new + mod:
        d = UPLOAD / "files" / k
        d.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy(OUT / k, d)
    L = [f"# 上传清单（自动生成于 {datetime.datetime.now():%Y-%m-%d %H:%M}）", ""]
    if last is None:
        L += ["> 还没有「已上传」基线，下面是**全部文件**。上传完成后运行 `python build/build.py --mark-uploaded` 建立基线，之后只会列出变化。",
              "> 首次迁移到分类结构：先在服务器上删掉旧的 `api/templates/`、`api/effects/`、`api/fx/`、`api/transitions/`、`api/graphics/`、`previews/`，再把 `files/` 里的内容整体上传到网站根目录。", ""]
    L += [f"- 新增 {len(new)} · 修改 {len(mod)} · 需在服务器删除 {len(dele)}", "- 文件已按服务器路径放在 `_work/upload/files/`，把里面的内容拖到网站根目录即可。", ""]

    def section(title, keys):
        if not keys: return
        L.append(f"## {title}")
        by = {}
        for k in keys: by.setdefault(folder_of(k), []).append(k)
        for f in sorted(by):
            n = len(by[f])
            L.append(f"- `{f}`" + (f" · {n} 个文件" if f.endswith("/") else ""))
        L.append("")
    section("新增", new); section("修改", mod)
    if dele:
        L.append("## 服务器上要删除")
        for k in sorted(dele): L.append(f"- `{k}`")
        L.append("")
    UPLOAD.mkdir(parents=True, exist_ok=True)
    (UPLOAD / "UPLOAD.md").write_text("\n".join(L), encoding="utf-8")
    return len(new), len(mod), len(dele), last is None


def mark_uploaded():
    snap = snapshot()
    LAST.parent.mkdir(parents=True, exist_ok=True)
    LAST.write_text(json.dumps(snap, indent=0), encoding="utf-8")
    log = ROOT / "_work" / "upload_log.md"
    note = (UPLOAD / "UPLOAD.md").read_text(encoding="utf-8") if (UPLOAD / "UPLOAD.md").exists() else ""
    with log.open("a", encoding="utf-8") as fh:
        fh.write(f"\n\n---\n## 已标记为已上传 {datetime.datetime.now():%Y-%m-%d %H:%M}\n\n{note}\n")
    print(f"marked {len(snap)} files as uploaded (log appended to _work/upload_log.md)")


def serve():
    port = 8080
    if shutil.which("php"):
        print(f"PHP 预览：http://localhost:{port}  （Ctrl+C 结束）")
        try: subprocess.run(["php", "-S", f"localhost:{port}", "-t", str(OUT)])
        except KeyboardInterrupt: pass
        return
    import http.server, socketserver, functools, tempfile
    prev = Path(tempfile.mkdtemp(prefix="dl-preview-"))
    shutil.copytree(OUT, prev / "site")
    s = (OUT / "includes/shell.html").read_text(encoding="utf-8")
    for k, v in {"{{CSS_V}}": "1", "{{JS_V}}": "1", "{{DATA}}": (OUT / "data/manifest.json").read_text(encoding="utf-8")}.items(): s = s.replace(k, v)
    (prev / "site/index.html").write_text(s, encoding="utf-8")
    print(f"没找到 php，使用静态预览：http://localhost:{port}  （Ctrl+C 结束）")
    h = functools.partial(http.server.SimpleHTTPRequestHandler, directory=str(prev / "site"))
    with socketserver.TCPServer(("", port), h) as srv:
        try: srv.serve_forever()
        except KeyboardInterrupt: pass


if __name__ == "__main__":
    if "--mark-uploaded" in sys.argv:
        mark_uploaded()
    else:
        build()
        n, m, d, first = make_delta()
        print(f"upload list: new {n} · changed {m} · delete-on-server {d}" + (" (first run: every file)" if first else "") + " -> _work/upload/UPLOAD.md")
        if "--serve" in sys.argv: serve()
