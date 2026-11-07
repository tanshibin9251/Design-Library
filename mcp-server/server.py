# -*- coding: utf-8 -*-
"""Design Library · 本地 MCP 服务（stdio）。

给 VS Code 里的 Claude Code 用：搜索库、取模板（CSS 变量 / Elementor 设定 / JSON / 单页 / 整站导出，可当场换色换字体换宽度）、
取效果、页面转场、色板。库的内容每次调用时现读，往 library/ 里加东西后不用重启（新增模板后跑一次 python build/build.py 更新目录）。

运行：  python mcp-server/server.py
注册：  见 mcp-server/.mcp.json.example
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "build"))

import catalog  # noqa: E402
import dlib  # noqa: E402
import site_export as SE  # noqa: E402
from mcp.server.fastmcp import FastMCP  # noqa: E402

mcp = FastMCP("design-library")


def _items():
    return catalog.make_catalog()["items"]


def _find(kind, slug):
    return next((i for i in _items() if i["kind"] == kind and i["slug"] == slug), None)


def _abs(rel):
    return str(ROOT / rel)


def _brief(it):
    out = {k: it[k] for k in ("id", "kind", "name", "name_zh", "tracks", "summary") if k in it}
    for k in ("domain", "graphic_type", "size", "types", "industries", "styles", "page_count", "category", "group"):
        if k in it:
            out[k] = it[k]
    if it.get("local_only"):
        out["local_only"] = True
    return out


def _hex_ok(**kw):
    for k, v in kw.items():
        if v and not re.fullmatch(r"#[0-9A-Fa-f]{6}", v):
            return f"颜色 {k} 必须是 #RRGGBB 格式，收到：{v}"
    return None


def _dim(v, default_unit="px"):
    """'1300px' / '90%' / '1300' → (数值, 单位)"""
    m = re.fullmatch(r"\s*([\d.]+)\s*(px|%)?\s*", str(v))
    if not m:
        raise ValueError(f"无法识别的尺寸：{v}（示例：1300px 或 90%）")
    n = float(m.group(1))
    return (int(n) if n == int(n) else n), (m.group(2) or default_unit)


def _over(primary="", secondary="", text="", accent="", surface="", border="", heading_font="", body_font="", text_scale=1.0,
          radius_px=0, section_padding="", content_width="", page_transition="", transition_ms=0):
    o = dict(colors=dict(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border),
             head=heading_font, body=body_font)
    if text_scale and float(text_scale) != 1.0:
        o["scale"] = round(float(text_scale) * 100)
    if radius_px:
        o["radius"] = radius_px
    if section_padding:
        o["pad"], o["padU"] = _dim(section_padding)
    if content_width:
        o["w"], o["wU"] = _dim(content_width)
    if page_transition:
        o["pt"] = page_transition
    if transition_ms:
        o["ptdur"] = transition_ms
    return o


OVERRIDE_DOC = ("可选自定义：primary/secondary/text/accent/surface/border（#RRGGBB）、heading_font、body_font、text_scale（1.1=放大10%）、radius_px、"
                "section_padding（'96px' 或 '110%'）、content_width（'1300px' 或 '90%'，默认 1300px）、page_transition（转场 slug 或 'none'）、transition_ms。没填的保持模板原值。")


def _load(slug, full=True):
    x = dlib.load_template(slug, full=full)
    return x


@mcp.tool()
def library_overview() -> str:
    """库的总览：分两条线 —— website（模板/效果/转场）和 graphic（海报/缩略图/横幅/社交帖/产品图），色板共用；各有多少、分类 ID、怎么选用。先调这个。"""
    cat = catalog.make_catalog()
    tax = cat["taxonomy"]
    return json.dumps(dict(
        counts=cat["counts"], by_track=cat["by_track"], by_domain=cat["by_domain"],
        domains=dict(website="模板 / 效果 / 页面转场 / Elementor（网站线）", graphic="海报 / 缩略图 / 横幅 / 社交帖 / 产品图（平面设计线）；色板两条线共用"),
        graphic_types=[dict(id=t["id"], name=t["name"], sizes=t["sizes"]) for t in tax["graphic_types"]],
        taxonomy=dict(types=[t["id"] for t in tax["types"]], industries=[t["id"] for t in tax["industries"]], styles=[t["id"] for t in tax["styles"]],
                      effect_categories=[c["id"] for c in tax["effect_cats"]], palette_categories=[c["id"] for c in tax["palette_categories"]] if "palette_categories" in tax else [c["id"] for c in cat["palette_categories"]],
                      page_transitions=[i["slug"] for i in cat["items"] if i["kind"] == "transition"]),
        how_to=dict(
            web="搜模板 search_library(kind='template', query='dental') → export_site(slug, dest_dir, ext='php', 自定义值…) 一次写出整站；或 get_page 取单页；get_effect / get_transition 取动效和页面转场。",
            elementor="get_template(slug, format='elementor') 得到 Global Colors/Fonts；export_site(ext='elementor') 得到 prompt + 参考 HTML；整站 kit / 零件用 get_elementor_item。",
            graphic="search_library(domain='graphic', graphic_type='poster') 找参考图 → get_graphic(slug, format='doc') 读设计配方（构图特征 + 不要）→ 照配方做一张全新的图（不要抄），颜色字体用 CSS 变量；get_graphic(format='html') 取画布源码；export_graphic 写出 HTML；用浏览器按画布尺寸截图导出 PNG。"),
        rules=["模板、效果、转场是库内自写，可用于任何客户站；占位文案和图片必须替换。",
               "local_only 的项目（Envato Elements 来源的 kit / 零件）不可公开分发：只返回本地路径，不要把内容贴到公开位置。",
               "颜色/字体/圆角/宽度一律通过 CSS 变量，不要写死 hex。"]), ensure_ascii=False, indent=1)


@mcp.tool()
def search_library(query: str = "", kind: str = "", track: str = "", industry: str = "", style: str = "", site_type: str = "", limit: int = 20,
                   domain: str = "", graphic_type: str = "") -> str:
    """搜索库。query 用空格分隔多个关键词（匹配名称、摘要、标签，如 'spa 健身 hover'）；
    domain：website（网站线）/ graphic（平面设计线）；kind：template / effect / transition / graphic / kit / part；track：web / elementor / graphic；
    模板还可按 industry（如 restaurant）、style（如 darkluxury）、site_type（如 ecommerce）筛选；
    平面设计可按 graphic_type（poster / thumbnail / banner / social / product）、industry、style 筛选，ID 见 library_overview。"""
    words = [w.lower() for w in query.split() if w.strip()]
    res = []
    for it in _items():
        if domain and it.get("domain") != domain:
            continue
        if graphic_type and it.get("graphic_type") != graphic_type:
            continue
        if kind and it["kind"] != kind:
            continue
        if track and track not in it["tracks"]:
            continue
        if industry and industry not in it.get("industries", []):
            continue
        if style and style not in it.get("styles", []):
            continue
        if site_type and site_type not in it.get("types", []):
            continue
        hay = " ".join([it["name"], it.get("name_zh", ""), it.get("summary", ""), it.get("fit", ""), it["slug"], " ".join(it.get("tags", []))]).lower()
        if all(w in hay for w in words):
            res.append(_brief(it))
    return json.dumps(res[:max(1, limit)], ensure_ascii=False, indent=1)


@mcp.tool()
def get_template(slug: str, format: str = "info", primary: str = "", secondary: str = "", text: str = "", accent: str = "", surface: str = "",
                 border: str = "", heading_font: str = "", body_font: str = "", text_scale: float = 1.0, radius_px: int = 0,
                 section_padding: str = "", content_width: str = "", page_transition: str = "", transition_ms: int = 0) -> str:
    """取一个模板的设计信息。format：
    info（默认：分类、页面清单、tokens、本地路径）| css（Web：tokens.css 变量 + 字体链接）| elementor（Global Colors/Fonts 设定值）| json（tokens + 页面清单）| doc（完整说明；有 DESIGN.md 的优先给 DESIGN.md，含『构图特征』和『不要』）。
    """ + OVERRIDE_DOC + """
    取整页代码用 get_page，一次写出整站用 export_site。"""
    x = _load(slug, full=False)
    if not x:
        return f"找不到模板 '{slug}'。用 search_library(kind='template') 查看可用的。"
    bad = _hex_ok(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border)
    if bad:
        return bad
    if format == "doc":
        d = ROOT / "library" / "styles" / slug / "DESIGN.md"
        return (d if d.exists() else x["dir"] / "TEMPLATE.md").read_text(encoding="utf-8")
    try:
        t = SE.settings(x, _over(primary, secondary, text, accent, surface, border, heading_font, body_font, text_scale, radius_px, section_padding, content_width, page_transition, transition_ms))
    except ValueError as e:
        return str(e)
    if format == "css":
        return SE.tokens_css(x, t)
    if format == "elementor":
        return SE.el_globals(x, t) + "\n\n" + SE.el_prompt(x, t)
    if format == "json":
        z = SE.sizes(x, t)
        return json.dumps(dict(slug=slug, colors={k: t[k] for k in SE.KEYS}, fonts=dict(heading=t["head"], body=t["body"]), sizes=z, page_transition=t["pt"],
                               pages=x["pagelist"]), ensure_ascii=False, indent=1)
    it = _find("template", slug)
    return json.dumps(dict(brief=_brief(it), pages=x["pagelist"], tokens=it["tokens"], files={k: _abs(v) for k, v in it["files"].items()},
                           tip="get_page 取单页；export_site 把整站写进你的项目文件夹；加自定义值就能换色换字体换宽度。"), ensure_ascii=False, indent=1)


@mcp.tool()
def get_page(slug: str, page: str = "home", ext: str = "html", primary: str = "", secondary: str = "", text: str = "", accent: str = "", surface: str = "",
             border: str = "", heading_font: str = "", body_font: str = "", text_scale: float = 1.0, radius_px: int = 0,
             section_padding: str = "", content_width: str = "", page_transition: str = "", transition_ms: int = 0) -> str:
    """取模板里一个页面的完整独立文件（含内联 CSS）。ext：html 或 php（php 用 includes/header.php + footer.php 的写法，需配合 export_site）。
    page 是页面 slug（先用 get_template 看页面清单，如 home / about / services / pricing / contact）。内部链接已换成 .html/.php。""" + OVERRIDE_DOC
    x = _load(slug)
    if not x or x["format"] != "fragments":
        return f"找不到可定制的模板 '{slug}'（导入的整页模板请直接读 library/templates/{slug}/pages/）。"
    if page not in x["pages"]:
        return f"没有页面 '{page}'。可用：{', '.join(p['slug'] for p in x['pagelist'])}"
    bad = _hex_ok(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border)
    if bad:
        return bad
    t = SE.settings(x, _over(primary, secondary, text, accent, surface, border, heading_font, body_font, text_scale, radius_px, section_padding, content_width, page_transition, transition_ms))
    if ext == "php":
        d = dict(SE.zip_php(x, t))
        return d[SE.href(page, "php")]
    return SE.page_file(x, t, page, "html")


@mcp.tool()
def export_site(slug: str, dest_dir: str, ext: str = "html", overwrite: bool = False, primary: str = "", secondary: str = "", text: str = "", accent: str = "",
                surface: str = "", border: str = "", heading_font: str = "", body_font: str = "", text_scale: float = 1.0, radius_px: int = 0,
                section_padding: str = "", content_width: str = "", page_transition: str = "", transition_ms: int = 0) -> str:
    """把整个模板（所有页面 + tokens.css + style.css）写进你的项目文件夹 dest_dir（绝对路径）。
    ext：html（纯 HTML 站）| php（PHP 站：includes/header.php、footer.php、每页 .php、.htaccess）| elementor（global-style.json、prompt、tokens.css、html/ 参考页）| json（单个 *.site.json）。
    已存在的文件默认不覆盖（overwrite=True 才覆盖）。导入的整页模板（Imported）按原样导出。""" + OVERRIDE_DOC
    x = _load(slug)
    if not x:
        return f"找不到模板 '{slug}'。"
    dest = Path(dest_dir).expanduser()
    if not dest.is_absolute():
        return "dest_dir 必须是绝对路径。"
    if ROOT in dest.resolve().parents or dest.resolve() == ROOT:
        return "不要把导出写进 Design Library 自己的文件夹，请选你的网站项目目录。"
    bad = _hex_ok(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border)
    if bad:
        return bad
    if x["format"] != "fragments":
        files = SE.raw_files(x)
    else:
        t = SE.settings(x, _over(primary, secondary, text, accent, surface, border, heading_font, body_font, text_scale, radius_px, section_padding, content_width, page_transition, transition_ms))
        files = {"html": SE.zip_html, "php": SE.zip_php, "elementor": SE.el_kit}.get(ext)
        if ext == "json":
            files = [(f"{slug}.site.json", SE.json_site(x, t))]
        elif files:
            files = files(x, t)
        else:
            return "ext 只能是 html / php / elementor / json"
    clash = [n for n, _ in files if (dest / n).exists()]
    if clash and not overwrite:
        return "以下文件已存在，未写入任何文件（要覆盖请加 overwrite=True）：\n" + "\n".join(clash[:20])
    written = SE.write_files(files, dest)
    return json.dumps(dict(written=len(written), dest=str(dest), entry=str(dest / ("index.php" if ext == "php" else "index.html")) if ext in ("html", "php") else "",
                           next="改 assets/css/tokens.css 里的变量即可换色换字体；替换占位文案和图片。" if ext in ("html", "php") else ""), ensure_ascii=False, indent=1)


@mcp.tool()
def get_style(slug: str, format: str = "css", primary: str = "", secondary: str = "", text: str = "", accent: str = "", surface: str = "", border: str = "",
              heading_font: str = "", body_font: str = "", text_scale: float = 1.0, radius: str = "") -> str:
    """（兼容旧名）取一套风格的 token，等同于 get_template(slug, format)。format：css | elementor | json | doc。radius 如 '12px'。
    设计时务必同时读 doc：构图特征和『不要』清单是这套风格的灵魂。"""
    r = int(float(re.sub(r"[^\d.]", "", radius) or 0)) if radius else 0
    return get_template(slug, format=format, primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border,
                        heading_font=heading_font, body_font=body_font, text_scale=text_scale, radius_px=r)


@mcp.tool()
def get_effect(slug: str) -> str:
    """取一个动效：说明（EFFECT.md）+ 可直接贴的 snippet.html（含 CSS 变量，改变量即可换色/字体/圆角/字号/速度）。
    Web 线：贴进页面；Elementor 线：贴进 HTML widget。分类和 slug 用 search_library(kind='effect') 查。"""
    it = _find("effect", slug)
    if not it:
        return f"找不到效果 '{slug}'。用 search_library(kind='effect') 查看。"
    f = it["files"]
    return "## 说明\n" + Path(_abs(f["doc"])).read_text(encoding="utf-8") + "\n\n## snippet.html（直接贴）\n```html\n" + Path(_abs(f["snippet"])).read_text(encoding="utf-8") + "\n```"


@mcp.tool()
def get_transition(slug: str, duration_ms: int = 600, easing: str = "cubic-bezier(.7,0,.2,1)", color: str = "") -> str:
    """取一个页面转场的 CSS（View Transitions API）。多页站贴进共用样式表即可，无需 JS；单页应用用 document.startViewTransition 包住 DOM 更新。
    duration_ms 时长、easing 缓动、color 用于 Colour Flash 的闪色（#RRGGBB）。Chrome/Edge 126+、Safari 18.2+ 生效，其它浏览器自动退化为普通跳转。"""
    t = next((t for t in dlib.load_transitions() if t["slug"] == slug), None)
    if not t:
        return f"找不到转场 '{slug}'。可用：{', '.join(i['slug'] for i in dlib.load_transitions())}"
    bad = _hex_ok(color=color)
    if bad:
        return bad
    return f"/* Page transition — {t['name']} */\n:root {{\n  --pt-dur: {duration_ms}ms;\n  --pt-ease: {easing};\n  --pt-color: {color or '#e8590c'};\n}}\n\n{t['css']}"


@mcp.tool()
def get_graphic(slug: str, format: str = "info", primary: str = "", secondary: str = "", text: str = "", accent: str = "", surface: str = "", border: str = "",
                heading_font: str = "", body_font: str = "") -> str:
    """取一张平面设计（海报 / 缩略图 / 横幅 / 社交帖 / 产品图）。format：
    info（默认：类型、尺寸、tokens、本地路径）| canva（给 Claude Desktop + Canva 用的完整提示词）| doc（设计配方 DESIGN.md：构图特征 + 『不要』清单 + 文案口吻，做新图前必读）| html（完整独立 HTML，固定画布尺寸，可用 primary…border、heading_font、body_font 换色换字体）。
    用法：读 doc → 照配方做一张全新的图（不要抄），颜色字体只走 CSS 变量，文案图片换成客户的，缺图的位置标「缺图」；最后用浏览器按画布尺寸截图导出 PNG。"""
    g = dlib.load_graphic(slug)
    if not g:
        return f"找不到平面设计 '{slug}'。用 search_library(domain='graphic') 查看。"
    bad = _hex_ok(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border)
    if bad:
        return bad
    if format == "doc":
        return g["design"] or "（这张图还没有 DESIGN.md）"
    if format == "canva":
        c = dict(g["colors"]); c.update({k: v for k, v in dict(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border).items() if v})
        return (f"Use Canva to create a NEW {g['type']} design in the style of \"{g['name']}\". Do not copy or reuse any existing Canva template; build it from scratch using the recipe below.\n\n"
                f"## Canvas\nCustom size {g['size']['w']} x {g['size']['h']} px ({g['size']['label']}).\n\n"
                f"## Colors (use exactly these hex values)\nPrimary {c['primary']} · Secondary {c['secondary']} · Text {c['text']} · Accent {c['accent']} · Surface {c['surface']} · Border {c['border']}\n\n"
                f"## Fonts\nHeadings: {heading_font or g['fonts']['head']} · Body: {body_font or g['fonts']['body']}. If a font is not in Canva, pick the closest and say which. Chinese: Noto Sans SC / Noto Serif SC, no italic.\n\n"
                f"## Design recipe (follow closely)\n{g['design'] or g['tag']}\n\n"
                "## Rules\n- Replace all placeholder text with my content.\n- Where no image is given, leave a labelled placeholder (缺图) and list what is missing.\n- Give me the Canva edit link and export a PNG.\n\n## My content\n<fill in>")
    if format == "html":
        return dlib.graphic_doc(g, dict(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border), heading_font, body_font)
    it = _find("graphic", slug)
    return json.dumps(dict(brief=_brief(it), tokens=it["tokens"], files={k: _abs(v) for k, v in it["files"].items()},
                           tip="get_graphic(slug, format='doc') 读配方；format='html' 取源码；export_graphic 写出文件。"), ensure_ascii=False, indent=1)


@mcp.tool()
def export_graphic(slug: str, dest_dir: str, overwrite: bool = False, primary: str = "", secondary: str = "", text: str = "", accent: str = "", surface: str = "",
                   border: str = "", heading_font: str = "", body_font: str = "") -> str:
    """把一张平面设计的独立 HTML（固定画布尺寸）写进你的项目文件夹 dest_dir（绝对路径），文件名 <slug>.html。可传 primary…border / heading_font / body_font 换色换字体。
    已存在的文件默认不覆盖（overwrite=True 才覆盖）。写出后用浏览器按画布尺寸截图即可导出 PNG。"""
    g = dlib.load_graphic(slug)
    if not g:
        return f"找不到平面设计 '{slug}'。"
    dest = Path(dest_dir).expanduser()
    if not dest.is_absolute():
        return "dest_dir 必须是绝对路径。"
    if ROOT in dest.resolve().parents or dest.resolve() == ROOT:
        return "不要把导出写进 Design Library 自己的文件夹，请选你的项目目录。"
    bad = _hex_ok(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border)
    if bad:
        return bad
    f = dest / f"{slug}.html"
    if f.exists() and not overwrite:
        return f"{f} 已存在，未写入（要覆盖请加 overwrite=True）。"
    dest.mkdir(parents=True, exist_ok=True)
    f.write_text(dlib.graphic_doc(g, dict(primary=primary, secondary=secondary, text=text, accent=accent, surface=surface, border=border), heading_font, body_font), encoding="utf-8")
    return json.dumps(dict(written=str(f), canvas=f"{g['size']['w']}x{g['size']['h']}", next="用浏览器按画布尺寸截图导出 PNG；替换占位文案，缺图位换真实素材。"), ensure_ascii=False, indent=1)


@mcp.tool()
def get_asset(slug: str, color: str = "") -> str:
    """取一个素材（线条 / 形状 / 边框 / 贴纸 / 图标 / 纹理 / 背景 / 照片 / 抠图 / 样机 / logo）。
    SVG：返回可直接内联的源码，color（#RRGGBB）把 currentColor 换成指定色；位图：返回本地文件的绝对路径和尺寸（local_only 的只给路径，不要贴到公开位置）。
    素材是一张图的「一层」：先 search_library(kind='asset', query='…') 找，再叠成海报 / 横幅 / 产品图。"""
    a = next((x for x in dlib.load_assets() if x["slug"] == slug), None)
    if not a:
        return f"找不到素材 '{slug}'。用 search_library(kind='asset') 查看。"
    bad = _hex_ok(color=color)
    if bad:
        return bad
    f = a["dir"] / a["file"]
    if a["format"] == "svg":
        t = f.read_text(encoding="utf-8")
        return t.replace("currentColor", color) if color else t
    return json.dumps(dict(path=str(f), format=a["format"], width=a["width"], height=a["height"], tags=a["tags"], license=a["license"],
                           note="位图素材：在 HTML 里用 <img> / background-image 引用这个路径（导出时复制到项目的 assets/ 里）。"), ensure_ascii=False, indent=1)


@mcp.tool()
def export_asset(slug: str, dest_dir: str, color: str = "", overwrite: bool = False) -> str:
    """把一个素材文件复制 / 写进你的项目文件夹 dest_dir（绝对路径）。SVG 可用 color 换色（#RRGGBB）。已存在默认不覆盖。"""
    a = next((x for x in dlib.load_assets() if x["slug"] == slug), None)
    if not a:
        return f"找不到素材 '{slug}'。"
    dest = Path(dest_dir).expanduser()
    if not dest.is_absolute():
        return "dest_dir 必须是绝对路径。"
    if ROOT in dest.resolve().parents or dest.resolve() == ROOT:
        return "不要写进 Design Library 自己的文件夹。"
    bad = _hex_ok(color=color)
    if bad:
        return bad
    out = dest / a["file"]
    if out.exists() and not overwrite:
        return f"{out} 已存在，未写入（overwrite=True 才覆盖）。"
    dest.mkdir(parents=True, exist_ok=True)
    src = a["dir"] / a["file"]
    if a["format"] == "svg" and color:
        out.write_text(src.read_text(encoding="utf-8").replace("currentColor", color), encoding="utf-8")
    else:
        out.write_bytes(src.read_bytes())
    return json.dumps(dict(written=str(out), license=a["license"]), ensure_ascii=False)


@mcp.tool()
def get_palettes(category: str = "", query: str = "") -> str:
    """列出 Quick Palettes（每组 [primary, secondary, text, accent, surface, border]）。category 是分类 ID（neutral blue green warm rose purple earth pastel dark neon food health edu luxury a11y season duo），
    query 按名称筛选。不填则列出各分类数量。选好后把六个色值传给 get_template / export_site 的 primary…border。"""
    pal = dlib.palettes()
    if not category and not query:
        return json.dumps([dict(id=c["id"], name=c["name"], zh=c["zh"], count=sum(1 for p in pal["palettes"] if p["cat"] == c["id"])) for c in pal["cats"]], ensure_ascii=False, indent=1)
    out = [dict(category=p["cat"], name=p["name"], primary=p["c"][0], secondary=p["c"][1], text=p["c"][2], accent=p["c"][3], surface=p["c"][4], border=p["c"][5])
           for p in pal["palettes"] if (not category or p["cat"] == category) and (not query or query.lower() in p["name"].lower())]
    return json.dumps(out, ensure_ascii=False, indent=1)


@mcp.tool()
def get_elementor_item(kind: str, slug: str) -> str:
    """查 Elementor 线的整站 kit（kind='kit'）或 Theme Builder 零件（kind='part'）：返回说明、所需插件、授权、本地 JSON 路径。
    来自 Envato 的项目 local_only：只给路径，不返回 JSON 内容，也不要放到公开位置。"""
    if kind not in ("kit", "part"):
        return "kind 只能是 kit 或 part"
    it = _find(kind, slug)
    if not it:
        return f"找不到 {kind} '{slug}'。用 search_library(kind='{kind}', track='elementor') 查看。"
    doc = Path(_abs(it["files"]["doc"])).read_text(encoding="utf-8")
    paths = {k: _abs(v) for k, v in it["files"].items() if k != "doc"}
    warn = "⚠ Envato Elements 来源：每个新客户项目需登记授权；不可转售/公开分发。" if it.get("local_only") else ""
    return json.dumps(dict(needs=it["needs"], license=it["license"], warning=warn, local_files=paths), ensure_ascii=False, indent=1) + "\n\n" + doc


if __name__ == "__main__":
    mcp.run()
