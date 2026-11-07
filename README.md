# Design Library 设计资源库

个人设计工作台：收集模板、效果、转场、平面设计配方与素材，再搜索、预览、定制和复用。支持 HTML / CSS / JS / PHP，也提供 Elementor 重建参考包与本地 MCP。

Website 收网站模板、局部效果与转场；Graphic 收平面设计与素材；色板共用。实际数量见生成的 [目录](library/INDEX.md)，新增资源后需构建刷新，不在多份说明里手工维护总数。

## 用网站挑选设计

1. 选择 Website / Graphic，再选模板、效果或素材类别。
2. 用行业 / 风格等筛选，或输入中英文关键词。搜索主要针对当前类别，留意其它类别命中提示。
3. 打开条目预览；可定制模板支持换色、字体、宽度等。Imported 整页模板保留自己的样式，定制能力不同。
4. 点击爱心加入 My list，挑好后复制清单或 AI 提示词，也可以直接复制代码 / 下载。

My list 只存在当前浏览器，不会自动同步或成为库里的新资源。复制 AI 提示词后补目标、素材及项目绝对路径；现有按钮虽然写 Claude Code，使用时仍需核对实际客户端工具。

## 本地维护

在项目根目录运行（需实际可用的 Python 环境）：

```powershell
py -X utf8 build/build.py
py -X utf8 build/build.py --serve
```

预览默认使用 http://localhost:8080；`--serve` 会先构建。有 PHP 时使用 PHP 服务，没有时走静态 fallback。不要双击 PHP 文件预览；先核对页面标题以避免端口指向其它站。

新增内容：先放 `_work/inbox/` → 检查来源与许可 → 分类和去重 → 导入 `library/` → 验收 → 构建。详细见 [内容工作流](docs/CONTENT_WORKFLOWS.md) 与 [格式规范](library/FORMAT.md)。目前没有网页端入库后台。

## Claude Code 与 Codex

共用项目规则在 [AGENTS.md](AGENTS.md)，Claude 入口 [CLAUDE.md](CLAUDE.md) 引用同一份文件，避免维护两套规则。

已配置 design-library MCP 时：搜索 → 阅读条目说明 → 获取或导出。依赖在 `mcp-server/requirements.txt`，入口 `mcp-server/server.py`；Claude 配置示例在 `mcp-server/.mcp.json.example`，Codex 按自身客户端配置注册。不安装 MCP 也可读本地 catalog 与条目文件。

提示词示例：「帮我找适合餐厅的模板，比较最相关的几个；读设计说明后导出到我指定的绝对路径，列出缺素材和使用限制。」

## 上传 Hostinger

`public_html/` 是生成输出，不能只改它而不改源文件。构建会重建输出并生成 `_work/upload/UPLOAD.md` 与待上传文件。差异依据上次已上传基线；没有基线时为全量，不等于所有文件都在本轮修改。

由用户核对清单并上传，保留 `.htaccess`。待删除项先核对；不要直接清空服务器目录。`build/deploy.py` 会实际联网上传，不是只生成部署包。

用户确认上传完成后才运行：

```powershell
py -X utf8 build/build.py --mark-uploaded
```

本地构建、GitHub push 和网站上线是三个不同动作。纯规则 / Markdown 更新无需上传 Hostinger。

## 阅读地图

| 文件 | 用途 |
|---|---|
| [STRUCTURE.md](STRUCTURE.md) | 文件职责，想改功能应去哪里 |
| [HOW_IT_WORKS.md](HOW_IT_WORKS.md) | 数据流、预览、导出、上传基线 |
| [docs/CONTENT_WORKFLOWS.md](docs/CONTENT_WORKFLOWS.md) | 各类内容入库、设计复用与验收 |
| [docs/WEBSITE_REVIEW.md](docs/WEBSITE_REVIEW.md) | 网站现状、问题证据与分阶段建议 |
| [library/FORMAT.md](library/FORMAT.md) | 内容文件格式 |
| [UPLOAD_LOG.md](UPLOAD_LOG.md) | 变更和上传交接记录 |

Elementor 下载包包含设定、提示词和 HTML 参考，**不是原生可导入 Kit**。受限资源只保留本地；收藏、下载或重新排版不会改变其许可条件。
