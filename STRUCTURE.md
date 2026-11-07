# Design Library 文件结构

以 2026-11-07 检查的本地源码为依据；目录不是部署要求。

```text
AGENTS.md                 Claude / Codex 共用规则
CLAUDE.md                 Claude 入口，引用 AGENTS.md
README.md                 用户入口与常用操作
STRUCTURE.md              文件职责与修改位置
HOW_IT_WORKS.md            数据流、构建与发布边界
docs/
  CONTENT_WORKFLOWS.md     入库、复用和验收步骤
  WEBSITE_REVIEW.md        源码评估、优先级和验收建议
  GITHUB_DEPLOYMENT.md     main → deploy → Hostinger 设置与排错
  archive/                历史说明，不作为当前规则
library/                  内容源
  taxonomy.json           分类与展示分组
  templates/<slug>/       template.json、nav/footer、pages、TEMPLATE.md
  styles/<slug>/          模板 DESIGN.md（部分设计说明放这里）
  effects/<cat>/<slug>/   effect.json、snippet.html、EFFECT.md
  transitions/<slug>/     transition.json、transition.css
  graphics/<slug>/        graphic.json、graphic.html、DESIGN.md
  assets/<cat>/<slug>/    asset.json 与实际素材
  palettes/               palettes.json
  kits/、theme-parts/     本地 Elementor 参考资源
  runtime/                共享预览样式、脚本与 Live 层
  previews/               缩略图源
  catalog.json、INDEX.md   生成目录，不直接维护
build/
  dlib.py                 读取内容的共用入口
  catalog.py              本地 / 公共目录与索引信息
  paths.py                URL 分组辅助函数（最终前缀还由调用方组成）
  build.py                网站、Guide、manifest、API、下载包、上传差异
  site_export.py          HTML / PHP / JSON / Elementor 参考包
  src/app.js、app.css     网站界面源码
  src/library-state.js    项目收藏验证、迁移、备份合并
  src/guide.html          网站使用指南正文
  template_review.py      模板源码检查信号（非浏览器验收）
  deploy.py               真正联网上传的独立脚本
mcp-server/               本地 stdio MCP，server.py 与 requirements.txt
tools/                    导入、缩略图、手机检查、触屏补丁
.github/workflows/         自动构建、检查并发布 deploy 分支
public_html/              生成的 Hostinger 网站
_work/                    inbox、临时文件、上传包与本地基线
UPLOAD_LOG.md             人工维护的变更/上传交接记录
```

## 改哪里

| 想改什么 | 源码位置 |
|---|---|
| 导航、搜索、收藏、筛选和预览 UI | `build/src/app.js`、`build/src/app.css` |
| 网站 Guide | `build/src/guide.html`；构建时注入数量 |
| 模板内容、品牌变量 | `library/templates/<slug>/` |
| 效果的实现和使用说明 | `library/effects/<cat>/<slug>/` |
| 分类名称与分组 | `library/taxonomy.json`，同时检查 paths / 前端映射 |
| 目录字段与公开过滤 | `build/catalog.py`、`build/build.py` |
| AI 读取和导出行为 | `mcp-server/server.py`、共用 dlib / site_export |
| GitHub 自动部署 | `.github/workflows/deploy.yml`、`tools/check_public_build.py`、`tools/publish_deploy.py` |

## 输出目录

公共 API 共用入口在 `/api/catalog.json`、`index.json`、`taxonomy.json`、`palettes.json`。

- 模板：`api/website/templates/<group>/<slug>/`
- 效果 demo：`api/website/effects/<group>/<cat>/<slug>.html`
- 效果数据：`api/website/fx/<group>/<cat>/<slug>.json`
- 转场：`api/website/transitions/<group>/<slug>.css`
- 平面设计：`api/graphic/designs/<type>/<slug>.json|.html`
- 素材：`api/graphic/assets/<cat>/...`
- 缩略图：`previews/website/templates/...`、`previews/website/effects/...`

旧路径兼容跳转由生成的 `.htaccess` 负责；新文档和调用不要继续使用旧 URL。

模板优化全量清单：`docs/TEMPLATE_IMPROVEMENT_QUEUE.md`，结构化数据：`docs/TEMPLATE_IMPROVEMENT_INVENTORY.json`；由 `tools/template_inventory.py` 生成。

模板升级层：`build/template_enhance.py` 和 `library/runtime/template-{ux,commerce}.*`；专属交互：`library/templates/<slug>/interactions.js`。摄影索引与布局记录：`library/photography/`；`tools/apply_template_photography.py` 默认仅预览，显式 --apply 才修改模板源文件，不属于日常构建命令。
