# -*- coding: utf-8 -*-
"""生成第一批自有矢量素材（线条 / 形状 / 边框 / 贴纸 / 图标 / 纹理 / 背景）到 library/assets/<类别>/<slug>/。
全部是 SVG，颜色用 currentColor，可以在网站里换色；授权：库内自有，可公开。
用法：  py tools/gen_assets.py          （幂等：每次重写同一批文件）
真实照片 / 抠图 / logo 不在这里生成：放进 _work/inbox/，确认授权后再入库（见 CLAUDE.md「素材库」）。
"""
import json
import math
import random
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "library" / "assets"
ITEMS = []  # (cat, slug, name, zh, tags, width, height, svg)


def svg(vb, body, w=None, h=None, extra=""):
    x, y, vw, vh = [float(n) for n in vb.split()]
    w = w or int(vw)
    h = h or int(vh)
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="{vb}" width="{w}" height="{h}" fill="currentColor"{extra}>{body}</svg>\n', w, h


def add(cat, slug, name, zh, tags, vb, body, w=None, h=None, extra=""):
    s, ww, hh = svg(vb, body, w, h, extra)
    ITEMS.append((cat, slug, name, zh, tags, ww, hh, s))


def stroke(body, sw=6, cap="round", join="round"):
    return f'<g fill="none" stroke="currentColor" stroke-width="{sw}" stroke-linecap="{cap}" stroke-linejoin="{join}">{body}</g>'


def star_pts(cx, cy, n, r_out, r_in, rot=-90):
    pts = []
    for i in range(n * 2):
        r = r_out if i % 2 == 0 else r_in
        a = math.radians(rot + i * 180 / n)
        pts.append(f"{cx + r * math.cos(a):.1f},{cy + r * math.sin(a):.1f}")
    return " ".join(pts)


# ------------------------------------------------------------ lines
add("line", "rule-thick", "Thick rule", "粗横线", ["rule", "divider", "bold"], "0 0 600 24", '<rect y="6" width="600" height="12"/>')
add("line", "rule-double", "Double rule", "双线", ["rule", "divider", "editorial"], "0 0 600 24", '<rect y="4" width="600" height="5"/><rect y="15" width="600" height="3"/>')
add("line", "rule-dashed", "Dashed rule", "虚线", ["rule", "divider", "dashed"], "0 0 600 24", stroke('<path d="M4 12H596" stroke-dasharray="22 14"/>', 5, "butt"))
add("line", "rule-dotted", "Dotted rule", "点线", ["rule", "divider", "dots"], "0 0 600 24", stroke('<path d="M10 12H590" stroke-dasharray="0 20"/>', 10))
add("line", "rule-wave", "Wave line", "波浪线", ["wave", "divider", "playful"], "0 0 600 48", stroke('<path d="M0 24Q25 -2 50 24T100 24T150 24T200 24T250 24T300 24T350 24T400 24T450 24T500 24T550 24T600 24"/>', 6))
add("line", "rule-zigzag", "Zigzag line", "锯齿线", ["zigzag", "divider", "bold"], "0 0 600 40", stroke('<polyline points="0,30 25,10 50,30 75,10 100,30 125,10 150,30 175,10 200,30 225,10 250,30 275,10 300,30 325,10 350,30 375,10 400,30 425,10 450,30 475,10 500,30 525,10 550,30 575,10 600,30"/>', 6, "butt", "miter"))
add("line", "underline-brush", "Brush underline", "毛笔下划线", ["underline", "brush", "handmade"], "0 0 400 40", '<path d="M4 24C60 10 140 32 200 18S340 8 396 20L394 31C330 24 250 38 190 30S60 24 6 34Z"/>')
add("line", "circle-scribble", "Scribble circle", "手绘圈", ["circle", "highlight", "handmade"], "0 0 200 120", stroke('<path d="M100 8C40 6 6 36 12 66c6 32 58 48 100 44 48-4 84-30 78-64C186 22 150 8 104 10 78 11 56 18 40 30"/>', 6))
add("line", "arrow-curved", "Curved arrow", "弧形箭头", ["arrow", "handmade", "pointer"], "0 0 200 160", stroke('<path d="M12 20C60 0 150 20 162 100"/><path d="M138 82l24 28 26-30"/>', 7))
add("line", "arrow-long", "Long arrow", "长箭头", ["arrow", "pointer", "minimal"], "0 0 400 48", stroke('<path d="M4 24H392"/><path d="M366 6l26 18-26 18"/>', 6))
add("line", "crosshair", "Crosshair mark", "准星标记", ["registration", "tech", "print"], "0 0 80 80", stroke('<circle cx="40" cy="40" r="20"/><path d="M40 2v76M2 40h76"/>', 3, "butt"))
add("line", "corner-brackets", "Corner brackets", "四角括号", ["frame", "viewfinder", "tech"], "0 0 200 200", stroke('<path d="M4 44V4h40M156 4h40v40M196 156v40h-40M44 196H4v-40"/>', 8, "square", "miter"))
add("line", "hatch-diagonal", "Diagonal hatch", "斜线阴影", ["hatch", "texture", "lines"], "0 0 200 200", stroke(''.join(f'<path d="M{-20 + i * 24} 220L{40 + i * 24} -20"/>' for i in range(11)), 5, "butt"))

# ------------------------------------------------------------ shapes
add("shape", "circle", "Circle", "圆", ["basic", "circle"], "0 0 200 200", '<circle cx="100" cy="100" r="96"/>')
add("shape", "ring", "Ring", "圆环", ["basic", "ring", "outline"], "0 0 200 200", stroke('<circle cx="100" cy="100" r="88"/>', 16, "butt"))
add("shape", "half-circle", "Half circle", "半圆", ["basic", "arch"], "0 0 200 100", '<path d="M4 100a96 96 0 0 1 192 0z"/>')
add("shape", "quarter-circle", "Quarter circle", "四分之一圆", ["basic", "corner"], "0 0 200 200", '<path d="M0 200V0a200 200 0 0 1 200 200z"/>')
add("shape", "slash-bar", "Slash bar", "斜切条", ["slant", "sport", "bold"], "0 0 400 100", '<path d="M60 0H400L340 100H0Z"/>')
add("shape", "triangle", "Triangle", "三角形", ["basic", "triangle"], "0 0 200 180", '<path d="M100 6L196 174H4Z"/>')
add("shape", "diamond", "Diamond", "菱形", ["basic", "diamond"], "0 0 200 200", '<path d="M100 4L196 100 100 196 4 100Z"/>')
add("shape", "plus", "Plus", "加号", ["basic", "cross"], "0 0 200 200", '<path d="M76 4h48v72h72v48h-72v72H76v-72H4V76h72z"/>')
add("shape", "starburst-16", "Starburst 16", "16 角放射星", ["burst", "badge", "sale"], "0 0 200 200", f'<polygon points="{star_pts(100, 100, 16, 98, 78)}"/>')
add("shape", "star-5", "Star 5", "五角星", ["star", "rating"], "0 0 200 200", f'<polygon points="{star_pts(100, 104, 5, 98, 40)}"/>')
add("shape", "star-8", "Star 8", "八角星", ["star", "sparkle"], "0 0 200 200", f'<polygon points="{star_pts(100, 100, 8, 98, 44)}"/>')
add("shape", "sparkle-4", "Sparkle 4", "四角闪光", ["sparkle", "shine", "tech"], "0 0 200 200", '<path d="M100 0C108 70 130 92 200 100 130 108 108 130 100 200 92 130 70 108 0 100 70 92 92 70 100 0Z"/>')
add("shape", "arch", "Arch", "拱形", ["arch", "luxury", "frame"], "0 0 200 280", '<path d="M0 280V100a100 100 0 0 1 200 0v180z"/>')
add("shape", "pill", "Pill", "胶囊", ["basic", "label"], "0 0 300 100", '<rect width="300" height="100" rx="50"/>')
add("shape", "chevron", "Chevron", "箭头角", ["arrow", "direction"], "0 0 200 200", '<path d="M40 0l100 100L40 200 0 160l60-60L0 40z"/>')
add("shape", "blob-a", "Blob A", "有机团块 A", ["organic", "blob", "soft"], "0 0 200 200", '<path d="M44 30C74-2 140 6 170 40c30 36 28 90-4 124-32 34-92 40-128 8C6 140 2 70 44 30Z"/>')
add("shape", "blob-b", "Blob B", "有机团块 B", ["organic", "blob", "soft"], "0 0 200 200", '<path d="M150 18c32 20 54 62 40 104-14 42-60 76-104 70C42 186 8 148 8 104S44 28 86 12c22-8 46-6 64 6Z"/>')
add("shape", "dot-grid", "Dot grid 6×6", "点阵 6×6", ["dots", "grid", "pattern"], "0 0 200 200", ''.join(f'<circle cx="{16 + c * 34}" cy="{16 + r * 34}" r="7"/>' for r in range(6) for c in range(6)))

# ------------------------------------------------------------ frames
add("frame", "frame-double", "Double border", "双线边框", ["border", "classic", "invitation"], "0 0 400 500", stroke('<rect x="6" y="6" width="388" height="488"/><rect x="22" y="22" width="356" height="456"/>', 3, "butt", "miter"))
add("frame", "frame-arch", "Arch frame", "拱形相框", ["arch", "luxury", "product"], "0 0 300 420", stroke('<path d="M6 414V150a144 144 0 0 1 288 0v264z"/><path d="M22 414V150a128 128 0 0 1 256 0v264" opacity=".5"/>', 3, "butt"))
add("frame", "frame-polaroid", "Polaroid", "拍立得", ["photo", "retro", "snapshot"], "0 0 360 420", '<path fill-rule="evenodd" d="M0 0h360v420H0z M28 28h304v304H28z"/>')
add("frame", "frame-film", "Film strip", "胶卷", ["film", "video", "retro"], "0 0 600 140", '<path fill-rule="evenodd" d="M0 0h600v140H0z M20 30h560v80H20z' + ''.join(f' M{12 + i * 40} 8h18v12h-18z M{12 + i * 40} 120h18v12h-18z' for i in range(15)) + '"/>')
add("frame", "frame-ticket", "Ticket", "票券", ["ticket", "event", "outline"], "0 0 500 200", stroke('<path d="M12 12h476v62a26 26 0 0 0 0 52v62H12v-62a26 26 0 0 0 0-52z"/><path d="M360 20v160" stroke-dasharray="8 10"/>', 5, "round"))
add("frame", "frame-bubble", "Speech bubble", "对话框", ["speech", "comic", "social"], "0 0 300 220", '<path d="M40 8h220a32 32 0 0 1 32 32v100a32 32 0 0 1-32 32H150l-54 46v-46H40a32 32 0 0 1-32-32V40A32 32 0 0 1 40 8Z"/>')
add("frame", "frame-viewfinder", "Viewfinder", "取景框", ["camera", "tech", "focus"], "0 0 400 300", stroke('<path d="M6 60V6h54M340 6h54v54M394 240v54h-54M60 294H6v-54"/><path d="M200 132v36M182 150h36"/>', 6, "square", "miter"))
add("frame", "frame-stamp", "Postage stamp", "邮票边", ["stamp", "retro", "perforated"], "0 0 300 360", stroke('<rect x="8" y="8" width="284" height="344" stroke-dasharray="0 16" stroke-width="14"/><rect x="34" y="34" width="232" height="292" stroke-width="4"/>', 14))
add("frame", "frame-label-tag", "Label tag", "标签牌", ["tag", "price", "label"], "0 0 300 140", '<path fill-rule="evenodd" d="M40 0h240a20 20 0 0 1 20 20v100a20 20 0 0 1-20 20H40L0 70z M44 58a12 12 0 1 0 0 24 12 12 0 0 0 0-24z"/>')

# ------------------------------------------------------------ stickers / badges
add("sticker", "badge-starburst-24", "Starburst badge", "24 角爆炸徽章", ["badge", "sale", "new"], "0 0 240 240", f'<polygon points="{star_pts(120, 120, 24, 118, 98)}"/>')
add("sticker", "badge-seal", "Round seal", "圆形印章", ["seal", "award", "official"], "0 0 240 240", f'<polygon points="{star_pts(120, 120, 40, 118, 108)}"/>' )
add("sticker", "burst-comic", "Comic burst", "漫画爆炸", ["comic", "pop", "sale"], "0 0 240 240", '<polygon points="' + " ".join(
    f"{120 + (112 if i % 2 == 0 else 62 + (i * 7) % 30) * math.cos(math.radians(i * 15)):.1f},{120 + (112 if i % 2 == 0 else 62 + (i * 7) % 30) * math.sin(math.radians(i * 15)):.1f}" for i in range(24)) + '"/>')
add("sticker", "ribbon-banner", "Ribbon banner", "飘带", ["ribbon", "title", "label"], "0 0 400 120", '<path d="M0 20h60v-0h280v0h60l-30 40 30 40h-60v20H60v-20H0l30-40z"/>')
add("sticker", "price-tag", "Price tag", "价签", ["price", "shop", "tag"], "0 0 240 160", '<path fill-rule="evenodd" d="M30 0h130l80 80-80 80H30A30 30 0 0 1 0 130V30A30 30 0 0 1 30 0Z M40 66a14 14 0 1 0 0 28 14 14 0 0 0 0-28z"/>')
add("sticker", "arrow-circle", "Arrow in circle", "圆形箭头", ["arrow", "cta", "button"], "0 0 160 160", stroke('<circle cx="80" cy="80" r="72"/><path d="M52 108L108 52M64 52h44v44"/>', 10))

# ------------------------------------------------------------ icons (24 grid, stroke)
def icon(slug, name, zh, tags, body, fill=False):
    inner = body if fill else stroke(body, 2)
    add("icon", slug, name, zh, tags, "0 0 24 24", inner, 96, 96)


icon("arrow-up-right", "Arrow up-right", "右上箭头", ["arrow", "link"], '<path d="M7 17 17 7M8 7h9v9"/>')
icon("arrow-right", "Arrow right", "右箭头", ["arrow", "next"], '<path d="M5 12h14M13 6l6 6-6 6"/>')
icon("play", "Play", "播放", ["video", "media"], '<polygon points="7,4 20,12 7,20"/>', True)
icon("plus", "Plus", "加", ["add"], '<path d="M12 5v14M5 12h14"/>')
icon("check", "Check", "对勾", ["done", "ok"], '<path d="M5 13l4 4L19 7"/>')
icon("heart", "Heart", "爱心", ["like", "love"], '<path d="M12 21s-7-4.6-9.5-9A5.5 5.5 0 0 1 12 6a5.5 5.5 0 0 1 9.5 6C19 16.4 12 21 12 21z"/>')
icon("star", "Star", "星星", ["rating", "favorite"], f'<polygon points="{star_pts(12, 12.5, 5, 10, 4.2)}"/>')
icon("map-pin", "Map pin", "定位", ["location", "venue"], '<path d="M12 21s7-6.2 7-11a7 7 0 0 0-14 0c0 4.8 7 11 7 11z"/><circle cx="12" cy="10" r="2.5"/>')
icon("calendar", "Calendar", "日历", ["date", "event"], '<rect x="3" y="5" width="18" height="16" rx="2"/><path d="M3 10h18M8 3v4M16 3v4"/>')
icon("clock", "Clock", "时钟", ["time", "event"], '<circle cx="12" cy="12" r="9"/><path d="M12 7v5l3 2"/>')
icon("ticket", "Ticket", "门票", ["event", "entry"], '<path d="M3 8a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2v2a2 2 0 0 0 0 4v2a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-2a2 2 0 0 0 0-4z"/><path d="M14 6v12" stroke-dasharray="2 2"/>')
icon("bolt", "Bolt", "闪电", ["power", "energy", "gaming"], '<polygon points="13,2 4,14 11,14 9,22 20,9 13,9"/>')
icon("monitor", "Monitor", "显示器", ["screen", "pc", "tech"], '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M8 20h8M12 16v4"/>')
icon("cpu", "Chip", "芯片", ["cpu", "tech", "hardware"], '<rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9" y="9" width="6" height="6"/><path d="M9 2v4M15 2v4M9 18v4M15 18v4M2 9h4M2 15h4M18 9h4M18 15h4"/>')
icon("gamepad", "Gamepad", "手柄", ["gaming", "controller"], '<path d="M7 6h10a5 5 0 0 1 5 5v2a4 4 0 0 1-7.5 2L14 14h-4l-.5 1A4 4 0 0 1 2 13v-2a5 5 0 0 1 5-5z"/><path d="M7 10v4M5 12h4"/><circle cx="15" cy="11" r=".6"/><circle cx="17.5" cy="13" r=".6"/>')

# ------------------------------------------------------------ textures (SVG filters; use as overlay with mix-blend-mode)
def noise(freq, octaves=2, contrast=1.0, size=600):
    f = (f'<filter id="n" x="0" y="0" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="{freq}" numOctaves="{octaves}" seed="7" stitchTiles="stitch"/>'
         f'<feColorMatrix type="matrix" values="0 0 0 0 0  0 0 0 0 0  0 0 0 0 0  0 0 0 {contrast} 0"/></filter>')
    return f'<defs>{f}</defs><rect width="{size}" height="{size}" filter="url(#n)"/>'


add("texture", "grain-fine", "Fine grain", "细颗粒", ["grain", "film", "overlay"], "0 0 600 600", noise(0.9, 2, 1.1))
add("texture", "grain-coarse", "Coarse grain", "粗颗粒", ["grain", "risograph", "overlay"], "0 0 600 600", noise(0.45, 2, 1.6))
add("texture", "paper-fibers", "Paper fibres", "纸纤维", ["paper", "organic", "overlay"], "0 0 600 600", noise(0.04, 5, 0.9))
add("texture", "halftone-dots", "Halftone dots", "半调圆点", ["halftone", "pop", "overlay"], "0 0 200 200",
    '<defs><pattern id="h" width="20" height="20" patternUnits="userSpaceOnUse"><circle cx="10" cy="10" r="4.5"/></pattern></defs><rect width="200" height="200" fill="url(#h)"/>')
add("texture", "scanlines", "Scanlines", "扫描线", ["crt", "tech", "overlay"], "0 0 200 200",
    '<defs><pattern id="s" width="200" height="6" patternUnits="userSpaceOnUse"><rect width="200" height="2"/></pattern></defs><rect width="200" height="200" fill="url(#s)" opacity=".6"/>')
add("texture", "vignette", "Vignette", "暗角", ["vignette", "photo", "overlay"], "0 0 600 600",
    '<defs><radialGradient id="v" cx="50%" cy="50%" r="72%"><stop offset="55%" stop-color="currentColor" stop-opacity="0"/><stop offset="100%" stop-color="currentColor" stop-opacity=".9"/></radialGradient></defs><rect width="600" height="600" fill="url(#v)"/>')

# ------------------------------------------------------------ backgrounds
add("background", "glow-spot", "Glow spot", "光晕", ["glow", "light", "tech"], "0 0 600 600",
    '<defs><radialGradient id="g"><stop offset="0" stop-color="currentColor" stop-opacity=".9"/><stop offset="100%" stop-color="currentColor" stop-opacity="0"/></radialGradient></defs><circle cx="300" cy="300" r="300" fill="url(#g)"/>')
add("background", "mesh-soft", "Soft mesh", "柔和渐变团", ["gradient", "soft", "mesh"], "0 0 800 600",
    '<defs><filter id="b" x="-30%" y="-30%" width="160%" height="160%"><feGaussianBlur stdDeviation="70"/></filter></defs><g filter="url(#b)"><circle cx="220" cy="200" r="170" opacity=".9"/><circle cx="560" cy="170" r="130" opacity=".55"/><circle cx="460" cy="420" r="190" opacity=".7"/><circle cx="140" cy="460" r="110" opacity=".4"/></g>')
add("background", "rays-burst", "Light rays", "放射光线", ["rays", "burst", "retro"], "0 0 600 600",
    ''.join(f'<path d="M300 300L{300 + 520 * math.cos(math.radians(i * 20)):.0f} {300 + 520 * math.sin(math.radians(i * 20)):.0f}L{300 + 520 * math.cos(math.radians(i * 20 + 10)):.0f} {300 + 520 * math.sin(math.radians(i * 20 + 10)):.0f}Z"/>' for i in range(18)))
add("background", "grid-lines", "Grid lines", "网格线", ["grid", "tech", "blueprint"], "0 0 400 400",
    '<defs><pattern id="gr" width="40" height="40" patternUnits="userSpaceOnUse"><path d="M40 0H0V40" fill="none" stroke="currentColor" stroke-width="1.5"/></pattern></defs><rect width="400" height="400" fill="url(#gr)"/>')
add("background", "dot-field", "Dot field", "点阵背景", ["dots", "pattern", "soft"], "0 0 400 400",
    '<defs><pattern id="d" width="24" height="24" patternUnits="userSpaceOnUse"><circle cx="12" cy="12" r="2.4"/></pattern></defs><rect width="400" height="400" fill="url(#d)"/>')
add("background", "stripes-diagonal", "Diagonal stripes", "斜纹", ["stripes", "sport", "pattern"], "0 0 400 400",
    '<defs><pattern id="st" width="40" height="40" patternUnits="userSpaceOnUse" patternTransform="rotate(45)"><rect width="18" height="40"/></pattern></defs><rect width="400" height="400" fill="url(#st)"/>')

CATS = {"line": "Line", "shape": "Shape", "frame": "Frame", "sticker": "Sticker", "icon": "Icon", "texture": "Texture", "background": "Background"}


def main():
    n = 0
    for cat, slug, name, zh, tags, w, h, s in ITEMS:
        d = OUT / cat / slug
        d.mkdir(parents=True, exist_ok=True)
        (d / f"{slug}.svg").write_text(s, encoding="utf-8")
        meta = dict(slug=slug, name=name, zh=zh, cat=cat, file=f"{slug}.svg", format="svg", width=w, height=h, tags=tags,
                    recolor=True, license="库内自有", source="Design Library generated (tools/gen_assets.py)")
        (d / "asset.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        n += 1
    order = [slug for _, slug, *_ in ITEMS]
    (OUT / "order.json").write_text(json.dumps(order, ensure_ascii=False) + "\n", encoding="utf-8")
    from collections import Counter
    print(f"{n} assets ->", dict(Counter(c for c, *_ in ITEMS)))


if __name__ == "__main__":
    main()
