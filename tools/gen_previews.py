#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""给模板和效果生成静态缩略图（640×400 JPEG），网站首页用图片代替几十个 iframe，加载快很多。

用法（先 python build/build.py 生成 public_html/）：
  python tools/gen_previews.py            # 只重新生成有变化的
  python tools/gen_previews.py --force    # 全部重新生成
  python tools/gen_previews.py --only oakline-furniture,ecom-compare-bar
输出：library/previews/templates/<模板大组>/<slug>.jpg、library/previews/effects/<效果大组>/<分类>/<slug>.jpg 和 hashes.json（键仍是 t-<slug> / e-<slug>）。
然后再跑一次 python build/build.py，网站会自动使用这些图片。
需要：本机 Chrome 或 Edge；JPEG 转换用 Pillow，没有就用 Windows 自带的 System.Drawing；都没有则保留 PNG。
"""
import argparse, hashlib, json, os, shutil, subprocess, sys, tempfile, zipfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public_html"
LIB = ROOT / "library"
OUT = LIB / "previews"


def browser():
    for p in [r"C:\Program Files\Google\Chrome\Application\chrome.exe", r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
              r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe", "/usr/bin/google-chrome", "/usr/bin/chromium",
              "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"]:
        if Path(p).exists():
            return p
    return shutil.which("google-chrome") or shutil.which("chromium")


def sha(*parts):
    h = hashlib.sha1()
    for p in parts:
        h.update(p if isinstance(p, bytes) else str(p).encode("utf-8"))
    return h.hexdigest()[:10]


def shoot(chrome, url, png, w, h, scale):
    cmd = [chrome, "--headless=new", "--disable-gpu", "--hide-scrollbars", f"--window-size={w},{h}", f"--force-device-scale-factor={scale}",
           "--virtual-time-budget=5000", f"--screenshot={png}", url]
    try:
        subprocess.run(cmd, capture_output=True, timeout=90)
    except subprocess.TimeoutExpired:
        return False
    return Path(png).exists()


def to_jpeg(pngs, quality=78):
    """PNG -> JPEG in place (same stem). returns list of produced jpg paths"""
    out = []
    try:
        from PIL import Image
        for p in pngs:
            im = Image.open(p).convert("RGB")
            j = Path(p).with_suffix(".jpg")
            im.save(j, "JPEG", quality=quality, optimize=True)
            os.remove(p)
            out.append(j)
        return out
    except ImportError:
        pass
    if os.name == "nt":
        lst = ";".join(str(p) for p in pngs)
        ps = (r"Add-Type -AssemblyName System.Drawing;"
              r"$enc=[System.Drawing.Imaging.ImageCodecInfo]::GetImageEncoders()|Where-Object{$_.MimeType -eq 'image/jpeg'};"
              r"$ep=New-Object System.Drawing.Imaging.EncoderParameters(1);"
              r"$ep.Param[0]=New-Object System.Drawing.Imaging.EncoderParameter([System.Drawing.Imaging.Encoder]::Quality,[long]%d);"
              r"foreach($p in '%s'.Split(';')){$im=[System.Drawing.Image]::FromFile($p);$j=[System.IO.Path]::ChangeExtension($p,'.jpg');$im.Save($j,$enc,$ep);$im.Dispose();Remove-Item $p}" % (quality, lst.replace("'", "''")))
        subprocess.run(["powershell", "-NoProfile", "-Command", ps], capture_output=True, timeout=300)
        return [Path(p).with_suffix(".jpg") for p in pngs if Path(p).with_suffix(".jpg").exists()]
    return []


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--only", default="")
    a = ap.parse_args()
    chrome = browser()
    if not chrome:
        sys.exit("× 找不到 Chrome / Edge")
    if not (PUB / "api/catalog.json").exists():
        sys.exit("× 先运行 python build/build.py")
    only = {x for x in a.only.split(",") if x}
    OUT.mkdir(exist_ok=True)
    hf = OUT / "hashes.json"
    hashes = json.loads(hf.read_text(encoding="utf-8")) if hf.exists() else {}
    tmp = Path(tempfile.mkdtemp(prefix="dl-prev-"))
    jobs = []
    runtime_hash = sha((LIB / "runtime/site.css").read_bytes())
    # templates
    for d in sorted((PUB / "api/website/templates").glob("*/*")):
        if not d.is_dir() or (only and d.name not in only):
            continue
        z = d / f"{d.name}-html-site.zip"
        if not z.exists():
            continue
        src = LIB / "templates" / d.name
        key = "t-" + d.name
        h = sha(runtime_hash, (src / "template.json").read_bytes() if (src / "template.json").exists() else b"",
                (src / "nav.html").read_bytes() if (src / "nav.html").exists() else b"",
                (src / "pages/home.html").read_bytes() if (src / "pages/home.html").exists() else b"")
        dest = OUT / "templates" / d.parent.name / f"{d.name}.jpg"
        if not a.force and hashes.get(key) == h and dest.exists():
            continue
        jobs.append(("t", d.name, key, h, z, dest))
    # effects
    for p in sorted((PUB / "api/website/effects").glob("*/*/*.html")):
        if only and p.stem not in only:
            continue
        key = "e-" + p.stem
        h = sha(p.read_bytes(), runtime_hash)
        dest = OUT / "effects" / p.parent.parent.name / p.parent.name / f"{p.stem}.jpg"
        if not a.force and hashes.get(key) == h and dest.exists():
            continue
        jobs.append(("e", p.stem, key, h, p, dest))
    print(f"{len(jobs)} previews to render")

    def run(j):
        kind, slug, key, h, src, dest = j
        png = tmp / f"{key}.png"
        if kind == "t":
            d = tmp / ("x_" + slug)
            zipfile.ZipFile(src).extractall(d)
            ok = shoot(chrome, (d / "index.html").as_uri(), png, 1280, 800, 0.5)
        else:
            w = tmp / f"{key}.html"
            w.write_text('<!doctype html><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">'
                         '<body style="margin:0;padding:34px;display:grid;place-items:center;min-height:100vh;background:#faf8f5">' + src.read_text(encoding="utf-8"), encoding="utf-8")
            ok = shoot(chrome, w.as_uri(), png, 960, 600, 0.6667)
        return key, h, png if ok else None, dest

    with ThreadPoolExecutor(6) as ex:
        res = list(ex.map(run, jobs))
    pngs = [p for _, _, p, _ in res if p]
    made = to_jpeg(pngs) if pngs else []
    for key, h, png, dest in res:
        j = (png.with_suffix(".jpg") if png else None)
        dest.parent.mkdir(parents=True, exist_ok=True)
        if j and j.exists():
            shutil.copy(j, dest)
            hashes[key] = h
        elif png and png.exists():          # no converter: keep PNG
            shutil.copy(png, dest.with_suffix(".png"))
            hashes[key] = h
    hf.write_text(json.dumps(hashes, indent=1), encoding="utf-8")
    shutil.rmtree(tmp, ignore_errors=True)
    n = len(list(OUT.rglob("*.jpg"))) + len(list(OUT.rglob("*.png")))
    print(f"done · {len(made)} converted · {n} images in library/previews/")


if __name__ == "__main__":
    main()
