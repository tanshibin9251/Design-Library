# Design Library 如何运作

## 数据流

1. 资源文件先放 `_work/inbox/`，检查来源、许可、依赖和重复情况。
2. 导入工具或人工把规范化内容写入 `library/`，更新必要的 order / taxonomy。
3. `build/dlib.py` 读取原始数据，`catalog.py` 组织目录；同一批读取与导出模块供 MCP 使用。
4. `build/build.py` 写本地 catalog / INDEX，再生成不含受限条目的公共目录、manifest、API、缩略图副本及下载包。
5. Hostinger 的 `index.php` 输出外壳并嵌入 manifest。前端由 hash 路由切换列表和预览，较重的详情在打开时加载。
6. 用户在浏览器预览、定制、复制、下载，或由本地 MCP 搜索及导出。

## 网站与本地库不同

网站是公开资源的浏览与复用端；目前没有网页端入库后台。新增资源仍通过本地文件及脚本完成。

本地目录包含受限条目，公共目录排除 `local_only`。色板为共用资源。Website / Graphic 是内容领域；web / elementor 是使用路线，不能混为同一层分类。

`fragments` 模板由 nav、footer 与页面内容组成，可按参数定制；`documents` 是导入整页，保留原 CSS，不保证可以用相同参数换色。Elementor 下载包提供 tokens、提示词和 HTML 参考，不是原生 Elementor 导入文件。

## 浏览器状态

`build/src/app.js` 把列表筛选写入 hash 查询参数，支持刷新和返回。搜索主要在当前领域 / 类别匹配，并提供其它类别命中提示；不是全库搜索结果页。

My list 使用浏览器 localStorage，当前只是本浏览器收藏，不等于素材已入库，也不跨设备同步。收藏可复制条目清单和 AI 提示词；未实现项目文件夹、同步或网页入库。

Newest 当前通过反转条目数组实现，不是按真实入库时间排序。Live 是预览增强层，不能单凭预览就断言导出包含同样行为。

## 本地构建与预览

在项目根目录执行：

```powershell
py -X utf8 build/build.py
py -X utf8 build/build.py --serve
```

`--serve` 会先构建，并使用 8080；有 PHP 时启动 PHP 服务，否则复制输出到临时目录并拼出静态首页。当前 fallback 仍可能遇到 Windows 长路径问题；旧笔记描述的「不复制、内存拼首页」不是目前代码实现。不要为了预览复制整棵目录到很深的路径。

预览前确认端口未被其它站占用，并核对页面标题。不要停止用户其它 PHP 进程。浏览器不能直接访问受 `.htaccess` 保护的 data / includes；前端公开请求使用 API。

## 构建副作用与上传

- 构建清理 `public_html/` 子项，保留根目录与 `.vscode/`，随后重建输出。不要把手工内容放在输出目录。
- 正常 CLI 构建还生成 `_work/upload/files/` 和 `UPLOAD.md`，会重建该上传暂存目录。
- 差异基于上次 `--mark-uploaded` 基线；没有基线时列出全量。文本哈希忽略 CRLF 差异，ZIP 按条目名和 CRC 比较，不是直接比较 ZIP 字节。
- 本地构建不会上传。`build/deploy.py` 会真正联网读取部署配置并上传，不可作为验证命令。
- 上传清单出现删除项时，用户先核对再处理；不要照旧文档直接清空服务器目录。
- 用户确认上传完成后才运行 `py -X utf8 build/build.py --mark-uploaded`。该操作写入本地基线并追加 `_work/upload_log.md`；它与根目录人工维护的 `UPLOAD_LOG.md` 用途不同。

## MCP

依赖在 `mcp-server/requirements.txt`；入口为 `mcp-server/server.py`。客户端注册方式各自管理，仓库提供 `.mcp.json.example` 供 Claude 配置参考。

常用流程：`library_overview` → `search_library` → 读取对应说明 → `get_template` / `get_effect` / `get_graphic` / `get_asset` → 导出。

MCP `_items()` 直接调用目录生成逻辑读取源文件，不依赖已生成 catalog 才能发现新增条目。网站仍需构建才能更新。导出目的目录使用绝对路径，默认不覆盖已存在文件。

## 检查范围

手机审计针对模板页面和效果 demo，不覆盖库网站全部导航、弹窗和 Guide。UI 改动需另外检查。小目标目前按 40px 警告，不会单独导致失败；项目设计目标为 44px。

当前未见统一的全库 schema / 许可 / 重复 / 坏链检查入口。构建成功不等于所有内容均已验收。建议实现的检查与验收条件见 `docs/WEBSITE_REVIEW.md`。
