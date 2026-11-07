"""Blue Hour: drawn travel scenes (SVG, theme variables only). Every call returns an svg with unique ids."""
import random

_n = [0]
V = 'viewBox="0 0 800 1000" preserveAspectRatio="xMidYMid slice" aria-hidden="true" focusable="false"'
S, P, L, A = "var(--c-surface)", "var(--c-primary)", "var(--c-secondary)", "var(--c-accent)"


def mx(a, pct, b):
    return f"color-mix(in srgb,{a} {pct}%,{b})"


def _id(name):
    _n[0] += 1
    return f"ap-{name}{_n[0]}"


def lg(i, stops, x2=0, y2=1):
    s = "".join(f'<stop offset="{o}" style="stop-color:{c};stop-opacity:{op}"/>' for o, c, op in stops)
    return f'<linearGradient id="{i}" x1="0" y1="0" x2="{x2}" y2="{y2}">{s}</linearGradient>'


def rg(i, cx, cy, r, stops):
    s = "".join(f'<stop offset="{o}" style="stop-color:{c};stop-opacity:{op}"/>' for o, c, op in stops)
    return f'<radialGradient id="{i}" cx="{cx}" cy="{cy}" r="{r}">{s}</radialGradient>'


def stars(rnd, n, ymax, op=(.4, .9)):
    out = []
    for _ in range(n):
        x, y, r = rnd.uniform(0, 800), rnd.uniform(0, ymax), rnd.choice([.7, .9, 1.2, 1.6])
        out.append(f'<circle cx="{x:.0f}" cy="{y:.0f}" r="{r}" style="fill:{P};opacity:{rnd.uniform(*op):.2f}"/>')
    return "".join(out)


def aurora():
    r = random.Random(11)
    g1, g2, f, gm = _id("aur"), _id("aur"), _id("aur"), _id("aur")
    return (f'<svg {V}><defs>{lg(g1, [(0, S, 1), (.55, mx(L, 24, S), 1), (1, mx(L, 40, S), 1)])}'
            f'{lg(gm, [(0, A, .0), (.35, A, .85), (.7, mx(L, 70, A), .55), (1, L, 0)])}'
            f'<filter id="{f}" x="-20%" y="-20%" width="140%" height="140%"><feGaussianBlur stdDeviation="16"/></filter></defs>'
            f'<rect width="800" height="1000" fill="url(#{g1})"/>{stars(r, 48, 560)}'
            f'<g filter="url(#{f})"><path d="M-60 360C120 180 260 430 430 250S700 170 880 300V470C700 350 560 500 410 390S120 570-60 470Z" fill="url(#{gm})" opacity=".8"/>'
            f'<path d="M-60 470C140 330 280 540 450 380S720 330 880 430V540C720 470 560 600 420 500S140 660-60 570Z" style="fill:{mx(L, 80, P)}" opacity=".35"/></g>'
            f'<path d="M0 650L90 560 170 612 260 520 360 604 450 540 560 624 650 530 760 602 800 572V1000H0Z" style="fill:{mx(L, 38, S)}"/>'
            f'<path d="M0 740L110 640 220 720 330 610 450 730 560 650 690 740 800 690V1000H0Z" style="fill:{mx(L, 20, S)}"/>'
            f'<path d="M0 850C180 790 330 830 480 800S720 780 800 820V1000H0Z" style="fill:{mx(P, 9, S)}"/>'
            f'<rect x="168" y="772" width="30" height="20" style="fill:{S}"/><path d="M162 772L183 756 204 772Z" style="fill:{S}"/><rect x="176" y="778" width="8" height="9" style="fill:{A}"/></svg>')


def dunes():
    g1, sun, gl = _id("dun"), _id("dun"), _id("dun")
    return (f'<svg {V}><defs>{lg(g1, [(0, S, 1), (.32, mx(L, 40, S), 1), (.6, mx(A, 45, L), 1), (.78, A, 1)])}'
            f'{rg(gl, .5, .5, .5, [(0, A, .55), (1, A, 0)])}</defs>'
            f'<rect width="800" height="1000" fill="url(#{g1})"/><circle cx="520" cy="560" r="280" fill="url(#{gl})"/>'
            f'<circle cx="520" cy="560" r="96" style="fill:{mx(P, 82, A)}"/>'
            f'<path d="M0 700C140 650 260 690 380 650S640 610 800 660V1000H0Z" style="fill:{mx(A, 40, S)}"/>'
            f'<path d="M0 790C160 700 300 780 450 730S700 700 800 750V1000H0Z" style="fill:{mx(A, 24, S)}"/>'
            f'<path d="M0 880C200 790 360 880 520 820S720 800 800 840V1000H0Z" style="fill:{mx(S, 82, A)}"/>'
            f'<path d="M-20 1000C120 900 300 960 460 900S720 900 840 950V1000Z" style="fill:{S}"/>'
            f'<g fill="none" style="stroke:{P}" stroke-width="1.4" opacity=".16"><path d="M80 900C200 870 300 905 420 880"/><path d="M120 930C240 905 340 935 460 915"/><path d="M420 840C520 815 620 845 720 825"/></g>'
            f'<path d="M612 746c0-14 6-22 12-22s12 8 12 22l-3 0-2 20-3 0-2-20-3 20-3 0-2-20z" style="fill:{S}"/><circle cx="624" cy="716" r="6" style="fill:{S}"/></svg>')


def peaks():
    r = random.Random(5)
    g1, gl, gw = _id("pea"), _id("pea"), _id("pea")
    return (f'<svg {V}><defs>{lg(g1, [(0, S, 1), (.5, mx(L, 40, S), 1), (.8, mx(A, 25, mx(L, 60, S)), 1)])}{rg(gl, .5, .5, .5, [(0, A, .4), (1, A, 0)])}'
            f'{lg(gw, [(0, mx(L, 40, S), 1), (1, S, 1)])}</defs>'
            f'<rect width="800" height="1000" fill="url(#{g1})"/>{stars(r, 40, 330)}<circle cx="400" cy="720" r="360" fill="url(#{gl})"/>'
            f'<circle cx="610" cy="210" r="56" style="fill:{P};opacity:.12"/><circle cx="610" cy="210" r="40" style="fill:{P};opacity:.92"/>'
            f'<path d="M0 700L120 560 200 640 330 440 430 600 520 500 640 650 720 560 800 640V1000H0Z" style="fill:{mx(L, 42, S)}"/>'
            f'<path d="M-20 820L180 560 260 660 400 320 520 560 565 520 700 770 830 700V1000H-20Z" style="fill:{mx(S, 78, L)}"/>'
            f'<path d="M400 320L330 460 380 440 400 520 440 450 520 560 470 440Z" style="fill:{P};opacity:.22"/>'
            f'<path d="M180 560L150 620 200 600 230 640 260 660Z" style="fill:{P};opacity:.16"/>'
            f'<rect y="800" width="800" height="200" fill="url(#{gw})"/>'
            f'<g fill="none" style="stroke:{P}" stroke-width="1.5" opacity=".14"><path d="M120 850H340M420 870H700M200 900H520M80 940H300M480 930H760"/></g>'
            f'<path d="M0 960C200 930 360 975 520 950S720 940 800 955V1000H0Z" style="fill:{S}"/></svg>')


def sea():
    g1, gs, gl = _id("sea"), _id("sea"), _id("sea")
    refl = "".join(f'<rect x="{285 - w / 2:.0f}" y="{600 + i * 22}" width="{w}" height="5" rx="2.5" style="fill:{P}" opacity="{o:.2f}"/>' for i, (w, o) in enumerate([(60, .8), (90, .65), (120, .5), (150, .38), (180, .28), (200, .18), (220, .1)]))
    waves = "".join(f'<path d="M{-40 + (i % 2) * 40} {600 + i * 38}C{120} {590 + i * 38} {240} {612 + i * 38} {400} {600 + i * 38}S{680} {590 + i * 38} {860} {604 + i * 38}" fill="none" style="stroke:{P}" stroke-width="1.5" opacity="{.16 - i * .012:.2f}"/>' for i in range(8))
    return (f'<svg {V}><defs>{lg(g1, [(0, S, 1), (.5, mx(L, 34, S), 1), (.62, mx(A, 18, mx(L, 55, S)), 1)])}{lg(gs, [(0, mx(L, 38, S), 1), (1, S, 1)])}'
            f'{rg(gl, .5, .5, .5, [(0, P, .35), (1, P, 0)])}</defs>'
            f'<rect width="800" height="600" fill="url(#{g1})"/><circle cx="285" cy="270" r="170" fill="url(#{gl})"/><circle cx="285" cy="270" r="58" style="fill:{P};opacity:.95"/>'
            f'<rect y="560" width="800" height="440" fill="url(#{gs})"/>{refl}{waves}'
            f'<path d="M540 640C560 600 600 590 640 585L690 580C740 585 780 610 820 650V700H520Z" style="fill:{S}"/>'
            f'<path d="M648 585L656 410 676 410 684 585Z" style="fill:{mx(S, 90, L)}"/><rect x="651" y="388" width="30" height="24" style="fill:{S}"/><path d="M646 388L666 368 686 388Z" style="fill:{S}"/>'
            f'<circle cx="666" cy="400" r="9" style="fill:{A}"/><path d="M675 400L800 372V428Z" style="fill:{A};opacity:.22"/></svg>')


def city():
    r = random.Random(21)
    g1, gr, b = _id("cit"), _id("cit"), _id("cit")
    bl, win = [], []
    x = -10
    while x < 810:
        w = r.randint(44, 96)
        h = r.randint(130, 420)
        shade = mx(S, r.choice([88, 92, 95]), L)
        bl.append(f'<rect x="{x}" y="{700 - h}" width="{w}" height="{h}" style="fill:{shade}"/>')
        for wy in range(700 - h + 14, 690, 28):
            for wx in range(x + 8, x + w - 8, 18):
                if r.random() < .2:
                    win.append(f'<rect x="{wx}" y="{wy}" width="6" height="9" style="fill:{A}" opacity="{r.uniform(.3, .95):.2f}"/>')
        x += w + r.randint(-6, 8)
    tiers = "".join(f'<path d="M{200 - 70 + i * 8} {640 - i * 46}H{200 + 70 - i * 8}L{200 + 54 - i * 8} {616 - i * 46}H{200 - 54 + i * 8}Z" style="fill:{S}"/>' for i in range(5))
    return (f'<svg {V}><defs>{lg(g1, [(0, S, 1), (.7, mx(L, 40, S), 1)])}{lg(gr, [(0, mx(L, 30, S), 1), (1, S, 1)])}</defs>'
            f'<rect width="800" height="700" fill="url(#{g1})"/>{stars(r, 40, 300, (.3, .7))}'
            f'<circle cx="590" cy="220" r="64" style="fill:{P};opacity:.1"/><circle cx="590" cy="220" r="46" style="fill:{P};opacity:.95"/>'
            f'<g id="{b}">{"".join(bl)}{"".join(win)}</g>{tiers}<rect x="196" y="380" width="8" height="44" style="fill:{S}"/>'
            f'<rect y="700" width="800" height="300" fill="url(#{gr})"/>'
            f'<g transform="translate(0 1400) scale(1 -1)" opacity=".2"><use href="#{b}"/></g>'
            f'<g fill="none" style="stroke:{P}" stroke-width="1.5" opacity=".12"><path d="M0 760H800M0 800H800M0 850H800M0 910H800"/></g></svg>')


def forest():
    r = random.Random(33)
    g1, sh, fg = _id("for"), _id("for"), _id("for")

    def row(y0, n, hmin, hmax, shade):
        out = []
        for i in range(n):
            x = r.uniform(-20, 820)
            h = r.uniform(hmin, hmax)
            w = h * .34
            out.append(f'<path d="M{x:.0f} {y0 - h:.0f}L{x + w:.0f} {y0:.0f}H{x - w:.0f}Z" style="fill:{shade}"/>')
            out.append(f'<path d="M{x:.0f} {y0 - h * .72:.0f}L{x + w * 1.3:.0f} {y0 + h * .12:.0f}H{x - w * 1.3:.0f}Z" style="fill:{shade}"/>')
        return "".join(out) + f'<rect x="0" y="{y0}" width="800" height="{1000 - y0}" style="fill:{shade}"/>'

    return (f'<svg {V}><defs>{lg(g1, [(0, S, 1), (1, mx(L, 34, S), 1)])}{lg(sh, [(0, A, .26), (1, A, 0)])}{lg(fg, [(0, mx(L, 40, S), 0), (.6, mx(L, 45, S), .6), (1, mx(L, 40, S), 0)])}</defs>'
            f'<rect width="800" height="1000" fill="url(#{g1})"/>{stars(r, 30, 260, (.3, .6))}'
            f'<path d="M560 0L720 0 520 760 260 760Z" fill="url(#{sh})"/><path d="M660 0L800 0 800 520 600 700Z" fill="url(#{sh})" opacity=".7"/>'
            f'{row(560, 15, 130, 220, mx(L, 30, S))}<rect y="470" width="800" height="150" fill="url(#{fg})"/>'
            f'{row(720, 11, 190, 300, mx(S, 80, L))}<rect y="620" width="800" height="170" fill="url(#{fg})"/>'
            f'{row(900, 7, 260, 400, mx(S, 94, L))}<rect y="840" width="800" height="160" style="fill:{S}"/></svg>')


def person(seed=1):
    g1 = _id("per")
    hair = ["M142 244c0-62 36-92 62-92 34 0 56 30 54 92-14-30-30-44-58-46-22 0-42 16-58 46z", "M150 236c-10-70 30-96 56-96 38 0 60 36 48 98-12-26-26-40-52-42-24 0-40 14-52 40z"][seed % 2]
    return (f'<svg {V}><defs>{lg(g1, [(0, mx(L, 40, S), 1), (1, S, 1)])}</defs><rect width="800" height="1000" fill="url(#{g1})"/>'
            f'<g transform="translate(0 120) scale(2)"><path d="M10 500c0-95 55-150 130-150s130 55 130 150z" transform="translate(60 0)" style="fill:{mx(P, 22, S)}"/>'
            f'<rect x="178" y="310" width="44" height="52" rx="14" style="fill:{mx(S, 70, P)}"/><ellipse cx="200" cy="255" rx="58" ry="70" style="fill:{mx(S, 70, P)}"/>'
            f'<path d="{hair}" style="fill:{S}"/></g></svg>')


SCENES = dict(aurora=aurora, dunes=dunes, peaks=peaks, sea=sea, city=city, forest=forest)


def art(name, label=None, cls="bh-art"):
    """wrapper div + svg"""
    svg = person() if name == "person" else SCENES[name]()
    lab = label or f"{name} scene, drawn placeholder"
    return f'<div class="{cls}" role="img" aria-label="{lab}">{svg}</div>'


def svg_only(name):
    return SCENES[name]()
