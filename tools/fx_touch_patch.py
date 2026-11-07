#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给 library/effects 的每个效果补「手机 / 触屏」支持（幂等，可重复运行）。

1. 根元素也用 border-box，避免 390px 宽度下 padding 撑出横向滚动。
2. 触屏（pointer:coarse）下按钮 / 输入框 / 下拉最小 44px。
3. 所有 `:hover` 规则复制一份 `.is-tap`；JS 在触摸时给被点的元素加 `.is-tap`，等同于手机上的悬停。
4. 个别靠 mousemove 的效果（magnetic / tilt / spotlight / cursor-*）加触屏版本。
改完请跑：python build/build.py
"""
import json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
FX = ROOT / "library/effects"
MARK = "/* fx-touch */"

PRELUDE_OLD = ".fx *,.fx *::before,.fx *::after{box-sizing:border-box}"
COARSE = ("@media (pointer:coarse){.fx :not(.dots)>button,.fx select,.fx summary,.fx [role=button],.fx input:not([type=checkbox]):not([type=radio]):not([type=range]){min-height:44px}"
          ".fx :not(.dots)>button{min-width:44px}"
          ".fx nav a,.fx footer a,.fx header a,.fx li>a{display:inline-flex;align-items:center;min-height:44px}"
          ".fx .dots button{min-width:28px;min-height:28px}}")
COARSE_RE = re.compile(r"@media \(pointer:coarse\)\{\.fx[^\n]*\}\}")
PRELUDE_NEW = (".fx,.fx *,.fx *::before,.fx *::after{box-sizing:border-box}\n.fx{max-width:100%}\n" + COARSE)

TAP_JS = (MARK + "\n(function(){if(window.__fxTap)return;window.__fxTap=1;var cur=[];function clr(){cur.forEach(function(e){e.classList.remove('is-tap')});cur=[]}\n"
          "document.addEventListener('pointerdown',function(e){if(e.pointerType!=='touch')return;clr();var n=e.target.closest&&e.target.closest('.fx');if(!n)return;"
          "for(var el=e.target;el&&el!==n.parentNode;el=el.parentNode){if(el.classList){el.classList.add('is-tap');cur.push(el)}}},{passive:true});\n"
          "document.addEventListener('pointerup',function(){setTimeout(clr,1400)},{passive:true})})();")


# ── css: duplicate every :hover selector as .is-tap ───────────────────────────
def split_blocks(css):
    """yield (prelude, body) for each top-level block; body is None for statements"""
    i, n, out = 0, len(css), []
    while i < n:
        j = css.find("{", i)
        if j < 0:
            out.append((css[i:], None)); break
        depth, k = 1, j + 1
        while k < n and depth:
            c = css[k]
            depth += (c == "{") - (c == "}")
            k += 1
        out.append((css[i:j], css[j + 1:k - 1]))
        i = k
    return out


def clone_sel(sel):
    parts = [p.strip() for p in re.split(r",(?![^(]*\))", sel) if p.strip()]
    add = [p.replace(":hover", ".is-tap") for p in parts if ":hover" in p]
    return add


def process(css):
    """returns css + clones; clones keep reduced-motion wrappers, but leave @media(hover:hover) wrappers"""
    if ".is-tap" in css:
        return css
    top_clones, body_out = [], []
    for pre, body in split_blocks(css):
        if body is None:
            body_out.append(pre); continue
        head = pre.strip()
        if head.startswith("@keyframes") or head.startswith("@-webkit-keyframes") or head.startswith("@font-face") or head.startswith("@property"):
            body_out.append(pre + "{" + body + "}"); continue
        if head.startswith("@"):  # @media / @supports
            inner_clones = []
            for p2, b2 in split_blocks(body):
                if b2 is None: continue
                for s in clone_sel(p2.strip()):
                    inner_clones.append(s + "{" + b2 + "}")
            hov = "hover:hover" in head.replace(" ", "")
            if hov:
                top_clones += inner_clones
                body_out.append(pre + "{" + body + "}")
            else:
                body_out.append(pre + "{" + body + ("\n" + "\n".join(inner_clones) if inner_clones else "") + "}")
        else:
            for s in clone_sel(head):
                top_clones.append(s + "{" + body + "}")
            body_out.append(pre + "{" + body + "}")
    res = "".join(body_out)
    if top_clones:
        res += "\n/* touch: :hover mirrored as .is-tap */\n" + "\n".join(top_clones) + "\n"
    return res


# ── per-effect JS upgrades ─────────────────────────────────────────────────────
SPECIAL_JS = {}
SPECIAL_CSS = {}

SPECIAL_JS["button-magnetic"] = (
    "\n/* touch: nudge toward the finger on press */\n"
    "if(matchMedia('(pointer:coarse)').matches&&!matchMedia('(prefers-reduced-motion:reduce)').matches){\n"
    "document.querySelectorAll('.fx-mag .zone').forEach(function(z){var b=z.querySelector('.b'),s=b.querySelector('span');\n"
    "z.addEventListener('pointerdown',function(e){var r=b.getBoundingClientRect(),x=e.clientX-(r.left+r.width/2),y=e.clientY-(r.top+r.height/2);\n"
    "b.style.transform='translate('+x*.3+'px,'+y*.4+'px) scale(.96)';s.style.transform='translate('+x*.1+'px,'+y*.14+'px)'});\n"
    "function up(){b.style.transform='';s.style.transform=''}z.addEventListener('pointerup',up);z.addEventListener('pointercancel',up)})}\n")
# the original returns early on touch devices, so run the touch block first
SPECIAL_JS["button-magnetic"] = SPECIAL_JS["button-magnetic"]

SPECIAL_JS["card-tilt-3d"] = (
    "\n/* touch: tilt while the finger is down */\n"
    "if(matchMedia('(pointer:coarse)').matches&&!matchMedia('(prefers-reduced-motion:reduce)').matches){\n"
    "document.querySelectorAll('.fx-tilt .card').forEach(function(c){function t(e){var r=c.getBoundingClientRect(),x=(e.clientX-r.left)/r.width,y=(e.clientY-r.top)/r.height;"
    "c.style.transform='rotateY('+(x-.5)*14+'deg) rotateX('+(.5-y)*14+'deg) translateZ(8px)';c.style.setProperty('--gx',x*100+'%');c.style.setProperty('--gy',y*100+'%')}\n"
    "c.addEventListener('pointerdown',t);c.addEventListener('pointermove',function(e){if(e.pressure>0||e.buttons)t(e)});\n"
    "function up(){c.style.transform=''}c.addEventListener('pointerup',up);c.addEventListener('pointercancel',up)})}\n")

SPECIAL_JS["card-spotlight"] = (
    "\n/* touch: light follows the tap */\n"
    "document.querySelectorAll('.fx-spot .card').forEach(function(c){c.addEventListener('pointerdown',function(e){var r=c.getBoundingClientRect();"
    "c.style.setProperty('--mx',e.clientX-r.left+'px');c.style.setProperty('--my',e.clientY-r.top+'px')})});\n")

SPECIAL_CSS["cursor-follower-dot"] = (
    "\n.fx-cf .rip{position:absolute;width:3.2em;height:3.2em;margin:-1.6em 0 0 -1.6em;border-radius:50%;border:2px solid var(--accent);pointer-events:none;animation:fxcf-rip calc(.7s/var(--speed)) ease-out forwards}\n"
    "@keyframes fxcf-rip{from{transform:scale(.2);opacity:.9}to{transform:scale(1.6);opacity:0}}\n"
    "@media(prefers-reduced-motion:reduce){.fx-cf .rip{animation-duration:.01s}}\n")
SPECIAL_JS["cursor-follower-dot"] = (
    "\n/* touch: tap ripple instead of a pointer follower */\n"
    "if(!matchMedia('(hover:hover) and (pointer:fine)').matches){document.querySelectorAll('.fx-cf').forEach(function(r){\n"
    "r.addEventListener('pointerdown',function(e){var b=r.getBoundingClientRect(),i=document.createElement('i');i.className='rip';i.style.left=(e.clientX-b.left)+'px';i.style.top=(e.clientY-b.top)+'px';r.appendChild(i);setTimeout(function(){i.remove()},800)})})}\n")

SPECIAL_JS["cursor-trail"] = (
    "\n/* touch: tap bursts a ring of dots */\n"
    "if(!matchMedia('(hover:hover) and (pointer:fine)').matches&&!matchMedia('(prefers-reduced-motion:reduce)').matches&&Element.prototype.animate){document.querySelectorAll('.fx-ct').forEach(function(r){\n"
    "r.addEventListener('pointerdown',function(e){var b=r.getBoundingClientRect(),x=e.clientX-b.left,y=e.clientY-b.top;for(var k=0;k<9;k++){var d=document.createElement('i');d.className='tr';d.style.setProperty('--t',k/8);d.style.setProperty('--c',(k/8*100)+'%');"
    "d.style.width=d.style.height='.7em';d.style.marginLeft=d.style.marginTop='-.35em';d.style.opacity=1;r.appendChild(d);var a=k/9*6.283,dx=Math.cos(a)*46,dy=Math.sin(a)*46;"
    "(function(el){el.animate([{transform:'translate3d('+x+'px,'+y+'px,0) scale(1)',opacity:1},{transform:'translate3d('+(x+dx)+'px,'+(y+dy)+'px,0) scale(.2)',opacity:0}],{duration:650,easing:'ease-out'}).onfinish=function(){el.remove()}})(d)}})})}\n")

SPECIAL_JS["cursor-spotlight"] = (
    "\n/* touch: spotlight jumps to the tap and follows a drag */\n"
    "if(!matchMedia('(hover:hover) and (pointer:fine)').matches){document.querySelectorAll('.fx-cs').forEach(function(r){function m(e){var b=r.getBoundingClientRect();r.style.setProperty('--mx',(e.clientX-b.left)+'px');r.style.setProperty('--my',(e.clientY-b.top)+'px')}\n"
    "r.addEventListener('pointerdown',m);r.addEventListener('pointermove',function(e){if(e.pointerType==='touch')m(e)})})}\n")
SPECIAL_CSS["cursor-spotlight"] = "\n.fx-cs{touch-action:pan-y}\n"


def fix_prelude(s):
    if PRELUDE_OLD in s and ".fx,.fx *" not in s:
        return s.replace(PRELUDE_OLD, PRELUDE_NEW, 1)
    if COARSE_RE.search(s):
        return COARSE_RE.sub(lambda m: COARSE, s, count=1)
    return s


def patch(effect_json: Path):
    d = json.loads(effect_json.read_text(encoding="utf-8"))
    slug = d["slug"]
    old_css, old_js = d["css"], d["js"]
    css = old_css
    js = old_js
    if slug in SPECIAL_CSS and SPECIAL_CSS[slug].strip() not in css:
        css += SPECIAL_CSS[slug]
    css = process(css)
    has_hover = ".is-tap" in css
    if slug in SPECIAL_JS and SPECIAL_JS[slug].strip() not in js:
        # touch block must come first for effects that early-return on touch devices
        js = SPECIAL_JS[slug].strip() + "\n" + js if slug in ("button-magnetic", "card-tilt-3d") else js + SPECIAL_JS[slug]
    if has_hover and MARK not in js:
        js = (js + "\n" if js else "") + TAP_JS
    changed = (css != old_css) or (js != old_js)
    d["css"], d["js"] = css, js
    if d.get("tech") == "css" and js:
        d["tech"] = "css+js"
    effect_json.write_text(json.dumps(d, ensure_ascii=False, indent=1), encoding="utf-8")

    sn = effect_json.parent / "snippet.html"
    s = sn.read_text(encoding="utf-8")
    s = fix_prelude(s)
    if old_css and old_css in s and css != old_css:
        s = s.replace(old_css, css, 1)
    if js != old_js:
        if old_js and old_js in s:
            s = s.replace(old_js, js, 1)
        else:  # snippet had no script yet
            s = s.rstrip("\n") + "\n\n<script>\n" + js + "\n</script>\n"
    sn.write_text(s, encoding="utf-8")
    return changed


def patch_runtime():
    f = ROOT / "library/runtime/fx-demo.html"
    s = f.read_text(encoding="utf-8")
    f.write_text(fix_prelude(s), encoding="utf-8")


if __name__ == "__main__":
    n = 0
    for ej in sorted(FX.glob("*/*/effect.json")):
        if patch(ej): n += 1
    patch_runtime()
    print(f"patched {n} effects")
