#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把一个网站模板收进 library/templates/<slug>/ 。

输入（三选一）：
  1) Design Library 导出的 *.site.json（design-library-site@1）→ 完整入库，网站里可继续换色/字体/宽度/转场（format=fragments）
  2) 文件夹 或 .zip（HTML 站，或 PHP 站含 includes/header.php+footer.php）→ 按"整页模板 Imported"入库（format=documents）：
     本地 CSS / JS 会内联进每个页面，小图片转 data URI，内部链接改成 {{p:slug}}；网站里可预览、复制、下载，但不能换色。
用法：
  python tools/ingest_template.py <路径> --slug my-site --name "My Site" --zh 中文名 \\
      --types company,landing --ind restaurant --styles warm,playful [--replace]
入库后：python build/build.py 更新网站、catalog.json 和 /api/。
分类 ID 见 library/taxonomy.json。
"""
import argparse, base64, json, mimetypes, re, sys, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LINK = re.compile(r'''href=(["'])([\w./-]+?)\.(?:html|php)(#[\w-]*)?\1''')
PHP_BLOCK = re.compile(r"<\?(?:php|=).*?\?>", re.S)
DEFAULT_COLORS = dict(primary="#1f2a44", secondary="#4b5675", text="#1f2328", accent="#e8590c", surface="#faf8f5", border="#e6e0d6")
DEFAULT_TOK = dict(hlh="1.1", hw="600", hcase="none", hls="0", h1="60px", h2="40px", h3="22px", h1big="60px", pad="88px", ew="600", stat="var(--c-primary)", radius="8px", fsb="16px")


def die(m):
    sys.exit("× " + m)


def jw(p, o):
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(json.dumps(o, ensure_ascii=False, indent=1), encoding="utf-8")


def to_ph(html):
    def r(m):
        base = m.group(2).split("/")[-1]
        if re.match(r"^[a-z][a-z0-9+.-]*:|^//", m.group(2)):
            return m.group(0)
        return f'href={m.group(1)}{{{{p:{"home" if base == "index" else base}}}}}{m.group(3) or ""}{m.group(1)}'
    return LINK.sub(r, html)


def title_of(html, slug):
    m = re.search(r"<title>(.*?)</title>", html, re.S | re.I)
    t = re.split(r"[·|–—-]", m.group(1))[0].strip() if m else ""
    return t or slug.replace("-", " ").title()


class Source:
    """统一读文件夹 / zip：names() 相对路径，read(name) 字节"""
    def __init__(self, p):
        self.p = Path(p)
        self.z = zipfile.ZipFile(p) if self.p.is_file() and zipfile.is_zipfile(p) else None
        if self.z:
            names = [n for n in self.z.namelist() if not n.endswith("/") and not n.startswith("__MACOSX")]
            tops = {n.split("/")[0] for n in names}
            self.strip = (tops.pop() + "/") if len(tops) == 1 and all("/" in n for n in names) else ""
            self._n = [n[len(self.strip):] for n in names if n[len(self.strip):]]
        else:
            self._n = [f.relative_to(self.p).as_posix() for f in self.p.rglob("*") if f.is_file() and ".git/" not in f.as_posix()]

    def names(self): return self._n

    def read(self, n):
        return self.z.read(self.strip + n) if self.z else (self.p / n).read_bytes()

    def text(self, n): return self.read(n).decode("utf-8", "replace")


def resolve(base, ref):
    ref = ref.split("?")[0].split("#")[0]
    parts = [] if ref.startswith("/") else [x for x in base.split("/") if x][:-1]
    for seg in ref.lstrip("/").split("/"):
        if seg == "..":
            parts and parts.pop()
        elif seg and seg != ".":
            parts.append(seg)
    return "/".join(parts)


def inline_assets(html, page_path, src, names):
    def css(m):
        h = m.group(0)
        href = re.search(r'href=["\']([^"\']+)["\']', h)
        if not href or re.match(r"^[a-z]+:|^//", href.group(1)) or "stylesheet" not in h:
            return h
        f = resolve(page_path, href.group(1))
        return f"<style>/* {f} */\n{src.text(f)}\n</style>" if f in names else h
    html = re.sub(r"<link\b[^>]*>", css, html, flags=re.I)

    def js(m):
        s = m.group(1)
        if re.match(r"^[a-z]+:|^//", s):
            return m.group(0)
        f = resolve(page_path, s)
        return f"<script>{src.text(f).replace('</script', '<' + chr(92) + '/script')}</script>" if f in names else m.group(0)
    html = re.sub(r'<script\b[^>]*\bsrc=["\']([^"\']+)["\'][^>]*>\s*</script>', js, html, flags=re.I)

    def img(m):
        s = m.group(2)
        if re.match(r"^[a-z]+:|^//|^data:", s):
            return m.group(0)
        f = resolve(page_path, s)
        if f in names:
            b = src.read(f)
            if len(b) <= 400_000:
                mt = mimetypes.guess_type(f)[0] or "application/octet-stream"
                return f'{m.group(1)}"data:{mt};base64,{base64.b64encode(b).decode()}"'
        return m.group(0)
    return re.sub(r'(\bsrc=)["\']([^"\']+)["\']', img, html, flags=re.I)


def ingest_documents(src, slug):
    names = set(src.names())
    pages = {}
    hdr, ftr = ("includes/header.php", "includes/footer.php")
    shared = (src.text(hdr), src.text(ftr)) if hdr in names and ftr in names else None
    for n in sorted(names):
        q = Path(n)
        if q.suffix.lower() not in (".html", ".htm", ".php") or "includes" in q.parts or q.parent.as_posix() not in (".", ""):
            continue
        t = src.text(n)
        if shared and q.suffix == ".php":
            body = PHP_BLOCK.sub("", t)
            t = PHP_BLOCK.sub("", shared[0]) + body + PHP_BLOCK.sub("", shared[1])
        elif q.suffix == ".php":
            t = PHP_BLOCK.sub("", t)
        s = "home" if q.stem == "index" else q.stem
        pages[s] = to_ph(inline_assets(t, n, src, names))
    if "home" not in pages:
        die("没找到 index.html / index.php（首页）")
    return pages


def main():
    ap = argparse.ArgumentParser(description="把模板收进 library/templates/")
    ap.add_argument("src"); ap.add_argument("--slug", required=True); ap.add_argument("--name"); ap.add_argument("--zh", default="")
    ap.add_argument("--tag", default=""); ap.add_argument("--types", default=""); ap.add_argument("--ind", default=""); ap.add_argument("--styles", default="")
    ap.add_argument("--license", default="ok", choices=["ok", "local_only"], help="local_only：授权不允许公开分发（Envato 等），不会进入 public_html")
    ap.add_argument("--replace", action="store_true"); ap.add_argument("--out", default=str(ROOT / "library" / "templates"))
    a = ap.parse_args()
    if not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", a.slug):
        die("slug 只能是小写字母、数字和连字符，如 my-cafe")
    tax = json.loads((ROOT / "library/taxonomy.json").read_text(encoding="utf-8"))
    ok = dict(types={t["id"] for t in tax["types"]}, ind={t["id"] for t in tax["industries"]}, styles={t["id"] for t in tax["styles"]})
    split = lambda s: [x for x in s.split(",") if x]
    types, ind, sty = split(a.types), split(a.ind), split(a.styles)
    for lab, vals, valid in (("types", types, ok["types"]), ("ind", ind, ok["ind"]), ("styles", sty, ok["styles"])):
        bad = [v for v in vals if v not in valid]
        if bad:
            die(f"--{lab} 里有不认识的 ID：{bad}。可用：{sorted(valid)}")
    out = Path(a.out) / a.slug
    if out.exists() and not a.replace:
        die(f"{out} 已存在（要覆盖请加 --replace）")
    src_p = Path(a.src).expanduser()
    if not src_p.exists():
        die(f"找不到 {src_p}")
    meta = dict(slug=a.slug, name=a.name or a.slug.replace("-", " ").title(), zh=a.zh, tag=a.tag, types=types, industries=ind, styles=sty,
                license="local_only" if a.license == "local_only" else "ok")
    if src_p.suffix.lower() == ".json" or (src_p.is_file() and not zipfile.is_zipfile(src_p)):
        j = json.loads(src_p.read_text(encoding="utf-8"))
        if j.get("format") != "design-library-site@1":
            die("这不是 design-library-site@1 文件")
        tk, tx = j["tokens"], j.get("taxonomy", {})
        z = tk["sizes"]
        meta.update(format="fragments", name=a.name or j.get("name", meta["name"]), colors=tk["colors"], fonts=dict(head=tk["fonts"]["heading"], body=tk["fonts"]["body"]),
                    tok=dict(DEFAULT_TOK, h1=z["h1"], h2=z["h2"], h3=z["h3"], h1big=z["h1"], fsb=z["body"], radius=tk["radius"], pad=tk["section_padding"]),
                    types=types or tx.get("types", []), industries=ind or tx.get("industries", []), styles=sty or tx.get("styles", []),
                    pages=[dict(slug=p["slug"], label=p["label"], group=p.get("group", "Main")) for p in j["pages"]])
        if j.get("page_transition", {}).get("name", "none") != "none":
            meta["page_transition"] = j["page_transition"]["name"]
        files = {"nav.html": j["nav_html"], "footer.html": j["footer_html"]}
        for p in j["pages"]:
            files[f"pages/{p['slug']}.html"] = p["html"]
        kind = "完整可定制模板"
    else:
        pages = ingest_documents(Source(src_p), a.slug)
        css_vars = {}
        meta.update(format="documents", colors=DEFAULT_COLORS, fonts=dict(head="Inter", body="Inter"), tok=DEFAULT_TOK,
                    pages=[dict(slug=s, label=title_of(h, s), group="Main") for s, h in pages.items()])
        files = {f"pages/{s}.html": h for s, h in pages.items()}
        kind = "整页模板（Imported）"
    if out.exists():
        import shutil
        shutil.rmtree(out)
    jw(out / "template.json", meta)
    for n, t in files.items():
        (out / n).parent.mkdir(parents=True, exist_ok=True)
        (out / n).write_text(t, encoding="utf-8")
    (out / "TEMPLATE.md").write_text(f"# {meta['name']}\n\n{meta.get('tag', '')}\n\n- 类型：{kind}\n- 站型：{', '.join(types) or '—'}\n- 行业：{', '.join(ind) or '—'}\n- 风格：{', '.join(sty) or '—'}\n- 页面（{len(meta['pages'])}）：{', '.join(p['slug'] for p in meta['pages'])}\n- 授权：{meta['license']}\n- 来源：{src_p.name}\n", encoding="utf-8")
    of = Path(a.out) / "order.json"
    order = json.loads(of.read_text(encoding="utf-8")) if of.exists() else []
    if a.slug not in order:
        order.append(a.slug)
        of.write_text(json.dumps(order), encoding="utf-8")
    print(f"✓ 已入库 {a.slug}：{kind}，{len(meta['pages'])} 页 → {out}\n  下一步：python build/build.py")


if __name__ == "__main__":
    main()
