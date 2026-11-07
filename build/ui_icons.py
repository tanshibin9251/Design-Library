# -*- coding: utf-8 -*-
"""网站界面（index.php 外壳）用的自绘 SVG：图标精灵 + 横向长方形 Logo。

- 图标：24×24 网格，1.7 描边、圆头，颜色跟随 `currentColor`。在 app.js 里用 `I('name')` 引用（→ `<use href="#i-name">`）。
- Logo：`<symbol id="logo">`，横向长方形锁定：左边是「D + 书架条」方块（与 favicon 同一个形状），右边是两行手绘字母 DESIGN / LIBRARY。
  方块跟随 currentColor，D 镂空用 `var(--bg)`，书架条用橙色；字母是描边路径，不依赖任何字体。
- 想改图形只改这里，然后 `python build/build.py`。
"""

ICONS = {
    # 分区 / 领域
    "tpl": '<rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><path d="M3.5 9h17M9 9v10.5"/>',
    "fx": '<path d="M11 3.8l1.9 5.5 5.5 1.9-5.5 1.9L11 18.6l-1.9-5.5-5.5-1.9 5.5-1.9z"/><path d="M19 3.5v3.6M17.2 5.3h3.6M18.4 15.2v3.3M16.8 16.85h3.3"/>',
    "tr": '<rect x="3" y="5.5" width="11.5" height="13" rx="2"/><path d="M17.5 8.5L21 12l-3.5 3.5"/>',
    "gr": '<rect x="3.5" y="4.5" width="17" height="15" rx="2.5"/><circle cx="9" cy="10" r="1.8"/><path d="M4 17.8l5-4.6 3.4 3 3-2.6 4.6 4.2"/>',
    "as": '<rect x="4" y="4" width="7" height="7" rx="1.6"/><circle cx="16.5" cy="7.5" r="3.5"/><path d="M4.2 20l3.3-6.6L10.8 20z"/><rect x="13" y="13" width="7" height="7" rx="3.5" transform="rotate(0)"/>',
    "web": '<circle cx="12" cy="12" r="8.5"/><path d="M3.5 12h17M12 3.5c2.5 2.3 3.8 5.1 3.8 8.5S14.5 18.2 12 20.5C9.5 18.2 8.2 15.4 8.2 12S9.5 5.8 12 3.5z"/>',
    "gfx": '<path d="M4.5 19.5l1.1-4.2L16.3 4.6a2.1 2.1 0 0 1 3 3L8.7 18.4z"/><path d="M14.3 6.6l3 3"/>',
    # 工具
    "sun": '<circle cx="12" cy="12" r="3.8"/><path d="M12 3.2v2.2M12 18.6v2.2M3.2 12h2.2M18.6 12h2.2M5.8 5.8l1.5 1.5M16.7 16.7l1.5 1.5M18.2 5.8l-1.5 1.5M7.3 16.7l-1.5 1.5"/>',
    "moon": '<path d="M19.8 14.4A8 8 0 0 1 9.6 4.2a8 8 0 1 0 10.2 10.2z"/>',
    "check": '<path d="M5 12.6l4.6 4.6L19 7.6" style="stroke-width:2.2"/>',
    "x": '<path d="M6.2 6.2l11.6 11.6M17.8 6.2L6.2 17.8"/>',
    "chd": '<path d="M6 9.5l6 6 6-6"/>',
    "chr": '<path d="M9.5 6l6 6-6 6"/>',
    "chl": '<path d="M14.5 6l-6 6 6 6"/>',
    "reset": '<path d="M4.2 12a7.8 7.8 0 1 0 2.4-5.6L4 8.6"/><path d="M4 4.2v4.4h4.4"/>',
    "ext": '<path d="M14 4h6v6M20 4l-9 9"/><path d="M18 14v4.5a1.5 1.5 0 0 1-1.5 1.5h-11A1.5 1.5 0 0 1 4 18.5v-11A1.5 1.5 0 0 1 5.5 6H10"/>',
    "search": '<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5 5"/>',
    "filter": '<path d="M4 5.5h16l-6.2 7.4V19l-3.6-1.8v-4.3z"/>',
    "heart": '<path d="M12 20.2S3.8 15.1 3.8 9.3A4.3 4.3 0 0 1 12 7.2a4.3 4.3 0 0 1 8.2 2.1c0 5.8-8.2 10.9-8.2 10.9z"/>',
    "dl": '<path d="M12 4v11M7.2 10.8L12 15.6l4.8-4.8M5 20h14"/>',
    "imp": '<path d="M4 13l2.4-7.5h11.2L20 13v5a1.5 1.5 0 0 1-1.5 1.5h-13A1.5 1.5 0 0 1 4 18z"/><path d="M4 13h4.6l1 2.6h4.8l1-2.6H20"/>',
    "info": '<circle cx="12" cy="12" r="8.5"/><path d="M12 11v5.4"/><circle cx="12" cy="7.9" r=".7" fill="currentColor"/>',
    "play": '<path d="M8 5.6v12.8L18.8 12z" fill="currentColor"/>',
    "cmp": '<path d="M4 8h13M13.2 4.2L17 8l-3.8 3.8M20 16H7M10.8 12.2L7 16l3.8 3.8"/>',
    "code": '<path d="M8.6 7.2L3.8 12l4.8 4.8M15.4 7.2l4.8 4.8-4.8 4.8M13.4 5l-2.8 14"/>',
    "layers": '<path d="M12 4l8.5 4.5L12 13 3.5 8.5z"/><path d="M3.5 12.5L12 17l8.5-4.5M3.5 16.5L12 21l8.5-4.5"/>',
    "palette": '<path d="M12 3.6a8.4 8.4 0 0 0 0 16.8c1.4 0 2-1 1.6-2.1-.4-1.1.3-2.4 1.6-2.4H17a3.5 3.5 0 0 0 3.5-3.5C20.5 7.1 16.7 3.6 12 3.6z"/><circle cx="7.8" cy="11.2" r="1.1"/><circle cx="10.6" cy="7.4" r="1.1"/><circle cx="15.2" cy="7.9" r="1.1"/>',
}

# ---- 手绘字母（线条字体，10 宽 × 14 高格；I 为 3 宽）----
GLYPH = {
    "D": ("M1 1V13H4.6C8 13 10 10.5 10 7S8 1 4.6 1Z", 10),
    "E": ("M10 1H1V13H10M1 7H8", 10),
    "S": ("M9.2 3.4C8.6 1.9 7.1 1 5.2 1 3 1 1.5 2.2 1.5 3.8 1.5 5.5 2.8 6.1 5.2 6.7 7.6 7.3 9 8 9 9.6 9 11.4 7.4 13 5 13 3 13 1.5 12.1 .9 10.5", 10),
    "I": ("M1.5 1V13", 3),
    "G": ("M9.6 3.4C8.8 2 7.3 1 5.6 1 2.9 1 1 3.5 1 7s1.9 6 4.6 6C8 13 9.6 11.4 9.6 8.4V7.8H5.8", 10),
    "N": ("M1 13V1L9 13V1", 10),
    "L": ("M1 1V13H9", 9),
    "B": ("M1 13V1H5.4C7.5 1 8.6 2.2 8.6 4S7.5 7 5.4 7H1M5.8 7C8.1 7 9.3 8.2 9.3 10S8.1 13 5.8 13H1", 10),
    "R": ("M1 13V1H5.4C7.5 1 8.7 2.2 8.7 4S7.5 7 5.4 7H1M5.4 7L9.4 13", 10),
    "A": ("M1 13L5 1l4 12M2.6 9H7.4", 10),
    "Y": ("M1 1L5 7.2 9 1M5 7.2V13", 10),
}


def _word(word, x0, tracking):
    out, x = [], x0
    for c in word:
        out.append(f'<path d="{GLYPH[c][0]}" transform="translate({x:.2f} 0)"/>')
        x += GLYPH[c][1] + tracking
    return "".join(out), x - tracking


LOGO_H = 44


def logo():
    """单行锁定：方块 + 「DESIGN」(跟随 currentColor) + 「LIBRARY」(橙色)。returns (symbol_svg, width, height)"""
    SC, TR, SP, TX = 1.5, 3.0, 9.0, 57
    w1, e1 = _word("DESIGN", 0, TR)
    w2, e2 = _word("LIBRARY", e1 + SP, TR)
    W = round(TX + (e2) * SC + 2)
    mark = ('<rect width="44" height="44" rx="11" fill="currentColor"/>'
            '<path d="M12.5 10.5h9.5a8.5 8.5 0 0 1 0 17h-9.5z" style="fill:var(--bg,#fff)"/>'
            '<rect x="12.5" y="31.2" width="19" height="4" rx="2" style="fill:var(--logo-bar,#e8590c)"/>')
    word = (f'<g transform="translate({TX} {(LOGO_H - 14 * SC) / 2:.2f}) scale({SC})" fill="none" stroke-width="2.3" stroke-linecap="round" stroke-linejoin="round">'
            f'<g stroke="currentColor">{w1}</g><g style="stroke:var(--logo-bar,#e8590c)">{w2}</g></g>')
    return f'<symbol id="logo" viewBox="0 0 {W} {LOGO_H}">{mark}{word}</symbol>', W, LOGO_H


def logo_svg(cls="logo"):
    _, W, H = logo()
    return f'<svg class="{cls}" viewBox="0 0 {W} {H}" role="img" aria-label="Design Library"><use href="#logo"/></svg>'


def sprite():
    lg, W, H = logo()
    syms = "".join(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>' for k, v in ICONS.items())
    return (f'<svg width="0" height="0" style="position:absolute" aria-hidden="true" focusable="false"><defs>{syms}{lg}</defs></svg>', W, H)


def favicon():
    return ('<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 44 44"><rect width="44" height="44" rx="11" fill="#191919"/>'
            '<path d="M12.5 10.5h9.5a8.5 8.5 0 0 1 0 17h-9.5z" fill="#fff"/><rect x="12.5" y="31.2" width="19" height="4" rx="2" fill="#e8590c"/></svg>')


if __name__ == "__main__":
    s, W, H = sprite()
    print(len(s), W, H)
