# -*- coding: utf-8 -*-
"""把图片素材（照片 / 抠图 / 样机 / logo / SVG）收进素材库 library/assets/<类别>/<slug>/。

用法：
  py tools/ingest_asset.py <文件 | 文件夹> --cat cutout --tags gpu,hardware,pc [--name "RTX card front"] [--zh 显卡正面]
        [--license local_only|ok] [--source "自己拍的 / Unsplash 链接 / Canva Pro"] [--subject gpu] [--replace]
  然后：py build/build.py

类别（taxonomy.json 的 asset_cats）：line shape frame sticker icon texture background photo cutout mockup logo
授权：
  ok          自己拍的 / 自己做的 / 明确可再分发（会进入 public_html，网站上可预览）
  local_only  图库、Canva、Envato、客户 logo（默认；只留本地，不进 public_html）
文件夹 = 批量：里面每个 png / jpg / jpeg / webp / svg 各成一个素材（同一类别、同一组标签）。
"""
import argparse
import json
import re
import shutil
import struct
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIB = ROOT / "library"
EXT = {".png", ".jpg", ".jpeg", ".webp", ".svg"}


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-") or "asset"


def size_of(p):
    b = p.read_bytes()
    ext = p.suffix.lower()
    try:
        if ext == ".png":
            return struct.unpack(">II", b[16:24])
        if ext in (".jpg", ".jpeg"):
            i = 2
            while i < len(b):
                if b[i] != 0xFF:
                    i += 1
                    continue
                m = b[i + 1]
                if m in (0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF):
                    h, w = struct.unpack(">HH", b[i + 5:i + 9])
                    return w, h
                i += 2 + struct.unpack(">H", b[i + 2:i + 4])[0]
        if ext == ".webp":
            if b[12:16] == b"VP8X":
                return 1 + int.from_bytes(b[24:27], "little"), 1 + int.from_bytes(b[27:30], "little")
            if b[12:16] == b"VP8 ":
                w, h = struct.unpack("<HH", b[26:30])
                return w & 0x3FFF, h & 0x3FFF
            if b[12:16] == b"VP8L":
                v = int.from_bytes(b[21:25], "little")
                return (v & 0x3FFF) + 1, ((v >> 14) & 0x3FFF) + 1
        if ext == ".svg":
            t = b.decode("utf-8", "ignore")
            m = re.search(r'viewBox="[\d.\-]+\s+[\d.\-]+\s+([\d.]+)\s+([\d.]+)"', t)
            if m:
                return int(float(m.group(1))), int(float(m.group(2)))
    except Exception:
        pass
    return 0, 0


def ingest(p, a, cats):
    slug = slugify(a.slug if (a.slug and not p.is_dir()) else p.stem)
    name = a.name if (a.name and not a.folder) else p.stem.replace("-", " ").replace("_", " ").title()
    d = LIB / "assets" / a.cat / slug
    if d.exists() and not a.replace:
        print(f"  skip {slug}（已存在，加 --replace 覆盖）")
        return False
    d.mkdir(parents=True, exist_ok=True)
    fname = slug + p.suffix.lower().replace(".jpeg", ".jpg")
    shutil.copy(p, d / fname)
    w, h = size_of(p)
    meta = dict(slug=slug, name=name, zh=a.zh if not a.folder else "", cat=a.cat, file=fname, format=fname.rsplit(".", 1)[1], width=w, height=h,
                tags=[t.strip() for t in a.tags.split(",") if t.strip()], license=a.license, source=a.source or "未记录",
                recolor=(fname.endswith(".svg") and "currentColor" in p.read_text("utf-8", "ignore")))
    if a.subject:
        meta["subject"] = a.subject
    (d / "asset.json").write_text(json.dumps(meta, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    order = LIB / "assets" / "order.json"
    o = json.loads(order.read_text(encoding="utf-8")) if order.exists() else []
    if slug not in o:
        o.append(slug)
        order.write_text(json.dumps(o, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"  + {a.cat}/{slug}  {w}×{h}  {meta['format']}  [{a.license}]")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("src")
    ap.add_argument("--cat", required=True)
    ap.add_argument("--tags", default="")
    ap.add_argument("--name", default="")
    ap.add_argument("--zh", default="")
    ap.add_argument("--slug", default="")
    ap.add_argument("--subject", default="")
    ap.add_argument("--source", default="")
    ap.add_argument("--license", default="local_only", choices=["ok", "local_only"])
    ap.add_argument("--replace", action="store_true")
    a = ap.parse_args()
    cats = {c["id"] for c in json.loads((LIB / "taxonomy.json").read_text(encoding="utf-8"))["asset_cats"]}
    if a.cat not in cats:
        sys.exit(f"× 类别 {a.cat} 不在 taxonomy.asset_cats：{sorted(cats)}")
    src = Path(a.src)
    if not src.exists():
        sys.exit(f"× 找不到 {src}")
    files = sorted(f for f in src.rglob("*") if f.suffix.lower() in EXT) if src.is_dir() else [src]
    a.folder = src.is_dir()
    if not files:
        sys.exit("× 没找到 png / jpg / webp / svg")
    n = sum(ingest(f, a, cats) for f in files)
    print(f"收入 {n} 个素材 -> library/assets/{a.cat}/。接着运行：py build/build.py")
    if a.license == "local_only":
        print("提示：local_only 不会进入 public_html；Claude Code 通过 library/catalog.json 和 MCP 读取本地文件。")


if __name__ == "__main__":
    main()
