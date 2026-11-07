"""Where every public file lives (api/ and previews/). One place, so build.py, catalog.py, gen_previews.py and the audit tools agree.

Layout (2026-10-14):
  api/templates/<template-group>/<slug>/<slug>.json …
  api/effects/<effect-group>/<category>/<slug>.html
  api/fx/<effect-group>/<category>/<slug>.json
  api/transitions/<group>/<slug>.css
  previews/templates/<template-group>/<slug>.jpg
  previews/effects/<effect-group>/<category>/<slug>.jpg
Groups come from library/taxonomy.json (template_groups, effect_cats[].group, transition group) so a new item lands in a known folder by itself.
"""
import re
import dlib

_T = None


def _tax():
    global _T
    if _T is None:
        _T = dlib.taxonomy()
    return _T


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def template_group(industries, slug=""):
    m = {}
    for g in _tax()["template_groups"]:
        for i in g["industries"]:
            m[i] = g["id"]
    for i in industries or []:
        if i in m:
            return m[i]
    raise SystemExit(f"× 模板 {slug or '?'} 的行业 {industries} 没有归入任何 template_groups（编辑 library/taxonomy.json）")


def effect_group(cat):
    for c in _tax()["effect_cats"]:
        if c["id"] == cat:
            return slugify(c["group"])
    raise SystemExit(f"× 效果分类 {cat} 不在 taxonomy.effect_cats 里")


def transition_group(name):
    return slugify(name)


def tpl_rel(slug, industries):
    return f"{template_group(industries, slug)}/{slug}"


def effect_rel(cat, slug, ext):
    return f"{effect_group(cat)}/{cat}/{slug}.{ext}"


def check_no_clash(template_slugs, cats):
    """Old URLs are redirected with .htaccess rules; a group id must never equal a slug / category id or the rules could loop."""
    tg = {g["id"] for g in _tax()["template_groups"]}
    eg = {slugify(c["group"]) for c in _tax()["effect_cats"]}
    bad = (tg & set(template_slugs)) | (eg & set(cats))
    if bad:
        raise SystemExit(f"× 分组名和 slug / 分类名重复：{sorted(bad)}")
