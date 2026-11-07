# 库格式规范（FORMAT）

```
library/
├─ taxonomy.json              站型 / 行业 / 风格 / 效果分类 / 色板分类 / 转场分组 / 页面分组
├─ templates/<slug>/          template.json · nav.html · footer.html · pages/<page>.html · TEMPLATE.md
├─ templates/order.json       展示顺序（Featured）
├─ effects/<分类>/<slug>/     effect.json · snippet.html · EFFECT.md；effects/order.json
├─ transitions/<slug>/        transition.json · transition.css；transitions/order.json
├─ graphics/<slug>/          graphic.json · graphic.html · DESIGN.md；graphics/order.json（Graphic 领域：海报 / 缩略图 / 横幅 / 社交帖 / 产品图）
├─ palettes/palettes.json     {cats:[{id,name,zh}], palettes:[{cat,name,c:[6 色]}]}
├─ runtime/                   site.css（所有模板共用）· preview.js · 演示外壳
├─ styles/<slug>/DESIGN.md    模板设计说明（构图特征 + 不要，以实际文件为准）
├─ kits/ theme-parts/         Elementor（Envato 来源，仅本地）
├─ catalog.json · INDEX.md    生成物（python build/build.py）
└─ FORMAT.md                  本文件
```

## template.json
```json
{ "format": "fragments | documents", "slug": "dental-care", "name": "Smile Dental", "zh": "微笑牙科", "tag": "一句话",
  "colors": {"primary":"#123456","secondary":"#E8EEF4","text":"#15202B","accent":"#925400","surface":"#FFFFFF","border":"#CCD4DC"},
  "fonts": {"head": "Manrope", "body": "Inter"},
  "tok": {},
  "types": ["company"], "industries": ["medical"], "styles": ["minimal"], "license": "local_only",
  "pages": [{"slug": "home", "label": "Home", "group": "Main"}] }
```
- **fragments**（完整可定制）：`pages/*.html` 只含 `<main>` 内的内容；导航在 `nav.html`，页脚在 `footer.html`；样式用 `runtime/site.css`，值来自 CSS 变量（`--c-primary --f-head --radius --pad --w` …）。
- `tok` 是可选设计参数对象，具体键和值以 `build/dlib.py`、导出代码及现有模板为准；示例为空对象，不代表所有模板都没有参数。
- 示例的 `license` 取单一值；现有常见值为 `库内自有`、`ok`、`local_only`，不能把带竖线的候选列表原样写成实际许可。来源依据另记在元数据或条目说明。
- **documents**（Imported 整页）：`pages/*.html` 是完整 HTML 文档（CSS/JS 已内联）。
- 内部链接统一写 `{{p:slug}}`（首页 `{{p:home}}`），导出时换成 `x.html` / `x.php`（首页 `index.*`）。
- `license: local_only` 的模板不会进入 `public_html`。

## 新增方式
- 模板：`python tools/ingest_template.py …`（见 CLAUDE.md）。
- 效果 / 转场 / 色板：按上面结构加文件，并更新对应 `order.json`；然后 `python build/build.py`。

## 两条硬规则
1. **可定制内容的颜色字体走变量。**fragments 模板与 Graphic 使用 `--c-*` / `--f-*`；effect 使用 `--primary` / `--font-heading` 等自身变量。documents 保留导入 CSS，不承诺同样的定制能力。
2. **每一项必须有来源与授权。**自己做的写「库内自有」；抓来的写原 URL + 授权；授权不明的只放 `_work/inbox/`，不入库。

## graphic.json（Graphic 领域）
```json
{ "slug": "swiss-event-poster", "name": "Swiss Event Poster", "zh": "瑞士网格活动海报", "tag": "一句话",
  "type": "poster", "size": {"label": "A-series poster", "w": 1200, "h": 1697},
  "styles": ["swiss"], "industries": ["events"],
  "colors": {"primary":"#123456","secondary":"#E8EEF4","text":"#15202B","accent":"#925400","surface":"#FFFFFF","border":"#CCD4DC"}, "fonts": {"head": "Archivo", "body": "IBM Plex Mono"},
  "license": "local_only" }
```
- `graphic.html`：`<style>` + 一个固定宽高的根元素（类名用 `g-xx` 前缀）；颜色字体只用 `--c-*`、`--on-*`、`--f-head`、`--f-body`；缺图的位置标「缺图」。
- `DESIGN.md`：设计配方（构图特征 · 不要 · 文案口吻 · 中文版 · 用法）。
- `type` 取自 `taxonomy.json` 的 `graphic_types`；`license: local_only` 的图不会进入 `public_html`。
- 每个条目在 catalog 里有 `domain`：`website`（template / effect / transition / kit / part）或 `graphic`。

## asset.json（素材库）
```json
{ "slug": "frame-arch", "name": "Arch frame", "zh": "拱形相框", "cat": "frame", "file": "frame-arch.svg", "format": "svg",
  "width": 300, "height": 420, "tags": ["arch", "luxury"], "recolor": true,
  "license": "local_only", "source": "来源 / 授权说明", "subject": "（可选）主体，如 gpu" }
```
- 位置 `library/assets/<类别>/<slug>/`，类别取自 `taxonomy.json` 的 `asset_cats`；`assets/order.json` 决定展示顺序。
- SVG 单色、用 `currentColor`（`recolor: true`）；位图建议透明 PNG（cutout / sticker）或 WebP / JPG（photo / background）。
- `license: local_only` 是导入的保守默认值，不会进入 `public_html`；是否可以公开使用某个素材，需核对该项实际许可，不能仅按来源平台判断。
- 入库：`py tools/ingest_asset.py …`；自有矢量批量生成：`py tools/gen_assets.py`。
