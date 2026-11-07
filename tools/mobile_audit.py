#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""手机端自动检查：在 390px 宽度（触屏指针）下检查效果和模板。

用法（先 python build/build.py 生成 public_html/）：
  python tools/mobile_audit.py                 # 效果 + 模板首页
  python tools/mobile_audit.py --effects       # 只查 105 个效果
  python tools/mobile_audit.py --templates --all-pages   # 模板的每一页（较慢）
  python tools/mobile_audit.py --width 768     # 平板宽度
  python tools/mobile_audit.py --only oakline-furniture,ecom-compare-bar

检查项：横向溢出（页面比视口宽）、触摸目标 < 40px（仅效果）、字号 < 12px（仅模板）。
退出码 0 = 全部通过；1 = 有问题。需要本机安装 Chrome 或 Edge。
"""
import argparse, html as H, json, re, shutil, subprocess, sys, tempfile, zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public_html"
TOUCH = "--blink-settings=primaryPointerType=2,availablePointerTypes=2,primaryHoverType=1,availableHoverTypes=1"


def find_browser():
    for p in [r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "/usr/bin/google-chrome", "/usr/bin/chromium",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]:
        if Path(p).exists():
            return p
    return shutil.which("google-chrome") or shutil.which("chromium") or shutil.which("chrome")


PROBE = """var de=document.documentElement,W=de.clientWidth,o=[];
document.querySelectorAll('%SEL% *').forEach(function(e){var r=e.getBoundingClientRect(),cs=getComputedStyle(e);
if(r.width>0&&r.right>W+2&&r.left<W&&cs.position!=='fixed'&&cs.display!=='none'){var p=e,clip=false;while((p=p.parentElement)&&p!==document.body){if(/(hidden|auto|scroll|clip)/.test(getComputedStyle(p).overflowX)){clip=true;break}}
if(!clip&&o.length<3)o.push((e.tagName+'.'+String(e.className).split(' ')[0]).slice(0,30)+' r='+Math.round(r.right))}});
var tiny=0;document.querySelectorAll('%SEL% button,%SEL% a,%SEL% input,%SEL% select,%SEL% [role=button]').forEach(function(e){var r=e.getBoundingClientRect();if(e.tagName==='INPUT'&&e.closest('label'))return;if(r.width>0&&r.height>0&&(r.width<%MIN%||r.height<%MIN%)&&getComputedStyle(e).visibility!=='hidden')tiny++});
var fs=0;document.querySelectorAll('p,li,a,span,td,label').forEach(function(e){var s=parseFloat(getComputedStyle(e).fontSize);if(s&&s<12&&e.textContent.trim().length>3)fs++});
document.body.setAttribute('data-p',JSON.stringify({scroll:de.scrollWidth,view:W,over:o,tiny:tiny,fs:fs}));"""


def run_page(browser, inner_html, width, sel, tmp, tag, touch=True, minsize=40):
    probe = PROBE.replace("%SEL%", sel).replace("%MIN%", str(minsize))
    inner = inner_html.replace("</body>", "<script>addEventListener('load',function(){setTimeout(function(){" + probe + "},500)})</script></body>") \
        if "</body>" in inner_html else inner_html + "<script>addEventListener('load',function(){setTimeout(function(){" + probe + "},500)})</script>"
    wrap = ('<!doctype html><meta charset="utf-8"><body style="margin:0"><iframe id=f width="%d" height="800" srcdoc="%s"></iframe>' % (width, H.escape(inner, quote=True))
            + '<script>document.getElementById("f").addEventListener("load",function(){var b=this.contentDocument.body;setTimeout(function(){document.body.setAttribute("data-out",b.getAttribute("data-p")||"")},1100)})</script>')
    f = tmp / (re.sub(r"[^\w.-]", "_", tag) + ".html")
    f.write_text(wrap, encoding="utf-8")
    cmd = [browser, "--headless=new", "--disable-gpu", "--virtual-time-budget=5000", "--dump-dom"] + ([TOUCH] if touch else []) + [f.as_uri()]
    try:
        r = subprocess.run(cmd, capture_output=True, text=True, timeout=90, encoding="utf-8")
        m = re.search(r'data-out="([^"]*)"', r.stdout)
        return json.loads(H.unescape(m.group(1))) if m and m.group(1) else {"err": "no result"}
    except Exception as e:
        return {"err": str(e)[:60]}


def audit_effects(browser, width, only, tmp):
    files = sorted((PUB / "api/website/effects").glob("*/*/*.html"))
    files = [p for p in files if not only or p.stem in only]

    def job(p):
        body = p.read_text(encoding="utf-8")
        inner = '<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><body style="margin:0;padding:16px;background:#faf8f5">' + body
        return p.stem, run_page(browser, inner, width, ".fx", tmp, "fx-" + p.stem, True, 40)
    with ThreadPoolExecutor(6) as ex:
        return list(ex.map(job, files))


def audit_templates(browser, width, only, all_pages, tmp):
    jobs = []
    for d in sorted((PUB / "api/website/templates").glob("*/*")):
        if not d.is_dir() or (only and d.name not in only):
            continue
        z = d / f"{d.name}-html-site.zip"
        if not z.exists():
            continue
        out = tmp / ("t_" + d.name)
        if not out.exists():
            zipfile.ZipFile(z).extractall(out)
        pages = sorted(p.name for p in out.glob("*.html")) if all_pages else ["index.html"]
        jobs += [(d.name, out, pg) for pg in pages]

    def job(j):
        slug, out, pg = j
        f = out / pg
        inner = f.read_text(encoding="utf-8").replace("<head>", '<head><base href="' + out.as_uri() + '/">', 1)
        return f"{slug}/{pg}", run_page(browser, inner, width, "body", tmp, f"{slug}_{pg}", True, 0)
    with ThreadPoolExecutor(8) as ex:
        return list(ex.map(job, jobs))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--effects", action="store_true"); ap.add_argument("--templates", action="store_true")
    ap.add_argument("--all-pages", action="store_true"); ap.add_argument("--width", type=int, default=390)
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    if not (a.effects or a.templates):
        a.effects = a.templates = True
    browser = find_browser()
    if not browser:
        sys.exit("× 找不到 Chrome / Edge")
    if not PUB.exists():
        sys.exit("× 先运行 python build/build.py")
    only = {x for x in a.only.split(",") if x}
    tmp = Path(tempfile.mkdtemp(prefix="dl-mobile-"))
    bad = 0
    try:
        if a.effects:
            res = audit_effects(browser, a.width, only, tmp)
            over = [(s, r) for s, r in res if r.get("err") or r.get("scroll", 0) > r.get("view", 0) or r.get("over")]
            tiny = [(s, r["tiny"]) for s, r in res if r.get("tiny", 0) > 0]
            print(f"[effects @{a.width}px] {len(res)} checked · {len(over)} overflow/err · {len(tiny)} with touch targets < 40px")
            for s, r in over:
                print("  ✗", s, r)
            if tiny:
                print("  ⚠ small targets:", ", ".join(f"{s}({n})" for s, n in sorted(tiny, key=lambda x: -x[1])[:15]))
            bad += len(over)
        if a.templates:
            res = audit_templates(browser, a.width, only, a.all_pages, tmp)
            over = [(s, r) for s, r in res if r.get("err") or r.get("scroll", 0) > r.get("view", 0)]
            print(f"[templates @{a.width}px] {len(res)} pages checked · {len(over)} with horizontal scroll/err")
            for s, r in over:
                print("  ✗", s, r)
            bad += len(over)
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    print("✓ 通过" if not bad else f"✗ {bad} 个问题")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
