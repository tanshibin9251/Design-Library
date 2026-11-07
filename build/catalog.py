# -*- coding: utf-8 -*-
"""æŠŠ library/ æ‰«ææˆä¸€ä»½æœºå™¨å¯è¯»çš„ç›®å½•ï¼ˆcatalog.jsonï¼‰ï¼Œç»™ç½‘ç«™ /api/ å’Œ MCP å…±ç”¨ã€‚

kindï¼štemplateï¼ˆæ•´ç«™å¤šé¡µæ¨¡æ¿ï¼Œå«é£Žæ ¼/è¡Œä¸šåˆ†ç±»ï¼‰Â· effectï¼ˆåŠ¨æ•ˆï¼‰Â· transitionï¼ˆé¡µé¢è½¬åœºï¼‰Â· kit / partï¼ˆElementorï¼Œlocal_onlyï¼Œåªåœ¨æœ¬åœ°ï¼‰Â· graphicï¼ˆæµ·æŠ¥/ç¼©ç•¥å›¾/æ¨ªå¹…/ç¤¾äº¤å¸–/äº§å“å›¾ï¼‰
domainï¼šwebsite = template / effect / transition / kit / partï¼›graphic = graphic
tracksï¼šweb = æ‰‹å†™ HTML/CSS/JS/PHPï¼›elementor = Elementor / WordPressï¼›graphic = å¹³é¢è®¾è®¡ï¼ˆHTML/CSS æŽ’ç‰ˆ â†’ æˆªå›¾å¯¼å‡º PNGï¼‰
  template / effect / transition â†’ web + elementorï¼ˆåŒä¸€å¥— token å¯å˜æˆ CSS å˜é‡ï¼Œä¹Ÿå¯å˜æˆ Elementor å…¨å±€è®¾å®šï¼‰
  kit / part â†’ elementorï¼ˆEnvato æ¥æºï¼Œä¸å¯¹å¤–ï¼‰
ç”¨æ³•ï¼š python build/catalog.py   # å†™å‡º library/catalog.json å¹¶æ‰“å°ç»Ÿè®¡
"""
import json
import re
import sys
from pathlib import Path

import dlib
import paths as PT
from dlib import LIB, ROOT, read

ROLES = ["primary", "secondary", "text", "accent", "surface", "border"]


def kv(text, key):
    m = re.search(rf"{key}ï¼š([^ã€€\n]+)", text)
    return m.group(1).strip() if m else ""


def title_of(text):
    return re.search(r"^# (.+)$", text, re.M).group(1).strip()


def rel(p):
    return Path(p).relative_to(ROOT).as_posix()


def make_catalog(public=False):
    tax = dlib.taxonomy()
    items = []
    for slug in dlib.template_slugs():
        x = dlib.load_template(slug, full=False)
        if public and x["license"] == "local_only":
            continue
        d = x["dir"]
        sd = LIB / "styles" / slug / "DESIGN.md"
        files = dict(dir=rel(d), meta=rel(d / "template.json"), doc=rel(d / "TEMPLATE.md"), pages=rel(d / "pages"))
        if sd.exists():
            files["design_doc"] = rel(sd)
        items.append(dict(
            id=f"template:{slug}", kind="template", slug=slug, name=x["name"], name_zh=x["zh"], tracks=["web", "elementor"], local_only=(x["license"] == "local_only"),
            summary=x["tag"], tags=x["types"] + x["ind"] + x["styles"], types=x["types"], industries=x["ind"], styles=x["styles"],
            page_count=len(x["pagelist"]), pages=x["pagelist"], needs=["å…è´¹"], license=x["license"], format=x["format"],
            tokens=dict(colors=x["colors"], fonts=x["fonts"], tok=x["tok"]), files=files,
            api=dict(full=f"/api/website/templates/{PT.tpl_rel(slug, x['ind'])}/{slug}.json", site_json=f"/api/website/templates/{PT.tpl_rel(slug, x['ind'])}/{slug}.site.json",
                     html_zip=f"/api/website/templates/{PT.tpl_rel(slug, x['ind'])}/{slug}-html-site.zip", php_zip=f"/api/website/templates/{PT.tpl_rel(slug, x['ind'])}/{slug}-php-site.zip"),
            preview=f"/#/template/{slug}"))
    cn = {c["id"]: c for c in tax["effect_cats"]}
    for e in dlib.load_effects():
        d = LIB / "effects" / e["cat"] / e["slug"]
        items.append(dict(
            id=f"effect:{e['slug']}", kind="effect", slug=e["slug"], name=e["name"], name_zh=e["zh"], tracks=["web", "elementor"],
            summary=e["tag"], tags=[e["cat"], e["tech"]], category=e["cat"], category_name=cn[e["cat"]]["name"], tech=e["tech"],
            needs=["çº¯ CSS" if e["tech"] == "css" else "CSS + åŽŸç”Ÿ JS"], license="è‡ªå†™ï¼Œæ— ç¬¬ä¸‰æ–¹ä»£ç ï¼Œå¯ç”¨äºŽä»»ä½•å®¢æˆ·ç«™",
            files=dict(doc=rel(d / "EFFECT.md"), snippet=rel(d / "snippet.html"), json=rel(d / "effect.json")),
            api=dict(snippet=f"/api/website/effects/{PT.effect_rel(e['cat'], e['slug'], 'html')}"), preview=f"/#/effect/{e['slug']}",
            usage=dict(web="æŠŠ snippet.html æ•´æ®µè´´è¿›é¡µé¢ï¼›é¢œè‰²/å­—ä½“/åœ†è§’/å­—å·/é€Ÿåº¦éƒ½æ¥è‡ªé¡¶éƒ¨ :root å˜é‡ã€‚",
                       elementor="è´´è¿› HTML widget æˆ– WPCodeï¼›å˜é‡æ”¾è¿› Site Settings â€º Custom CSS å¯å…¨ç«™å…±ç”¨ã€‚")))
    for t in dlib.load_transitions():
        items.append(dict(
            id=f"transition:{t['slug']}", kind="transition", slug=t["slug"], name=t["name"], name_zh=t["zh"], tracks=["web", "elementor"],
            summary=t["tag"], tags=[t["group"].lower(), "page-transition"], group=t["group"], needs=["çº¯ CSSï¼ˆView Transitions APIï¼‰"], license="è‡ªå†™",
            files=dict(css=rel(LIB / "transitions" / t["slug"] / "transition.css")), api=dict(css=f"/api/website/transitions/{PT.transition_group(t['group'])}/{t['slug']}.css"),
            preview=f"/#/transition/{t['slug']}"))
    for g in dlib.load_graphics():
        if public and g["license"] == "local_only":
            continue
        d = g["dir"]
        sd = g["size"]
        items.append(dict(
            id=f"graphic:{g['slug']}", kind="graphic", slug=g["slug"], name=g["name"], name_zh=g["zh"], tracks=["graphic"], local_only=(g["license"] == "local_only"),
            summary=g["tag"], tags=[g["type"]] + g["styles"] + g["ind"], graphic_type=g["type"], size=sd, industries=g["ind"], styles=g["styles"],
            needs=["HTML/CSSï¼ˆæµè§ˆå™¨æˆªå›¾å¯¼å‡º PNGï¼‰"], license=g["license"], tokens=dict(colors=g["colors"], fonts=g["fonts"]),
            files=dict(dir=rel(d), meta=rel(d / "graphic.json"), html=rel(d / "graphic.html"), doc=rel(d / "DESIGN.md")),
            api=dict(full=f"/api/graphic/designs/{g['type']}/{g['slug']}.json", html=f"/api/graphic/designs/{g['type']}/{g['slug']}.html"),
            preview=f"/#/graphic/{g['slug']}"))
    for a in dlib.load_assets():
        if public and a["license"] == "local_only":
            continue
        d = a["dir"]
        items.append(dict(
            id=f"asset:{a['slug']}", kind="asset", slug=a["slug"], name=a["name"], name_zh=a["zh"], tracks=["graphic"], local_only=(a["license"] == "local_only"),
            summary=f"{a['cat']} Â· {a['width']}Ã—{a['height']} Â· {a['format']}", tags=[a["cat"]] + a["tags"], category=a["cat"], format=a["format"],
            width=a["width"], height=a["height"], recolor=bool(a.get("recolor")), needs=["ç´ æï¼ˆSVG å¯ç”¨ CSS å˜è‰²ï¼‰" if a["format"] == "svg" else "ç´ æï¼ˆä½å›¾ï¼‰"],
            license=a["license"], source=a.get("source", ""),
            files=dict(dir=rel(d), meta=rel(d / "asset.json"), file=rel(d / a["file"])),
            api=dict(file=f"/api/graphic/assets/{a['cat']}/{a['file']}"), preview=f"/#/asset/{a['slug']}"))
    if not public:
        for f in sorted((LIB / "kits").glob("*/KIT.md")):
            t = read(f)
            d = f.parent
            pages = sorted(p.stem for p in (d / "pages").glob("*.json"))
            items.append(dict(
                id=f"kit:{d.name}", kind="kit", slug=d.name, name=title_of(t), name_zh=title_of(t), tracks=["elementor"],
                summary=f"{len(pages)} ä¸ªé¡µé¢ Â· {kv(t, 'è¡Œä¸š')}", tags=[kv(t, "è¡Œä¸š")], needs=[n for n in ("Elementor Pro", "LA-Studio Element Kit", "UAE", "WooCommerce") if n in kv(t, "éœ€è¦") or n in t.split("| é¡µé¢")[-1]] or ["è§ KIT.md"],
                license="Envato Elementsï¼šæ¯ä¸ªæ–°å®¢æˆ·é¡¹ç›®éœ€ç™»è®°æŽˆæƒï¼›ä¸å¯è½¬å”®/å…¬å¼€åˆ†å‘ï¼ŒJSON åªä¿ç•™åœ¨æœ¬åœ°åº“",
                local_only=True, status=kv(t, "çŠ¶æ€") or "è‰ç¨¿", pages=pages,
                files=dict(doc=rel(f), kit_json=rel(d / "kit.json"), pages_dir=rel(d / "pages")), preview=f"/kits/{d.name}/"))

        for f in sorted((LIB / "theme-parts").glob("*/*/PART.md")):
            t = read(f)
            d = f.parent
            need = kv(t, "éœ€è¦")
            lic = re.search(r"æŽˆæƒï¼š([^\n]+?)(?:ã€€å¯¼å‡º|$)", t)
            items.append(dict(
                id=f"part:{d.name}", kind="part", slug=d.name, name=d.name, name_zh=d.name, tracks=["elementor"],
                summary=kv(t, "é£Žæ ¼") or "", tags=[d.parent.name], part_type=d.parent.name,
                needs=[x.strip() for x in re.split(r"[ã€,ï¼Œ]", need) if x.strip()], requires_pro="Pro" in need,
                license=(lic.group(1).strip() if lic else "è§ PART.md"), local_only=d.name.startswith("luxenest"),
                status="è‰ç¨¿", files=dict(doc=rel(f), part_json=rel(d / "part.json")), preview=f"/parts/{d.parent.name}/{d.name}/"))


    for i in items:
        i["domain"] = "graphic" if i["kind"] in ("graphic", "asset") else "website"
    counts = {}
    for i in items:
        counts[i["kind"]] = counts.get(i["kind"], 0) + 1
    pal = dlib.palettes()
    counts["palette"] = len(pal["palettes"])
    by_track = {tr: sum(1 for i in items if tr in i["tracks"]) for tr in ("web", "elementor", "graphic")}
    by_domain = {d: sum(1 for i in items if i["domain"] == d) for d in ("website", "graphic")}
    return dict(version=2, generated_by="build/catalog.py", counts=counts, by_track=by_track, by_domain=by_domain, taxonomy=tax,
                palette_categories=[dict(id=c["id"], name=c["name"], count=sum(1 for p in pal["palettes"] if p["cat"] == c["id"])) for c in pal["cats"]], items=items)


def write_catalog():
    cat = make_catalog()
    (LIB / "catalog.json").write_text(json.dumps(cat, ensure_ascii=False, indent=1), encoding="utf-8")
    return cat


if __name__ == "__main__":
    c = write_catalog()
    print("catalog.json å·²å†™å‡ºï¼š", c["counts"], "æŒ‰çº¿ï¼š", c["by_track"], "æŒ‰åŸŸï¼š", c["by_domain"])
