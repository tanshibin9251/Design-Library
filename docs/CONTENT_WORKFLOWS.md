# 内容收集与复用工作流

项目约束见根目录 `AGENTS.md`；格式字段以 `library/FORMAT.md` 和实际 loader 为准。

## 1. 收集先明确用途

先区分：完整网站 template、局部 effect、页面 transition、平面设计 graphic、可叠加 asset、Elementor kit / part。只有参考价值而无可复用代码的链接或截图，先放 inbox，别伪装成可导出模板。

记录来源 URL / 本地来源、作者、获取日期、许可依据、适合场景、依赖与已知限制。现有格式没有统一承载的字段，先写条目说明；扩展机器字段时同时修改 loader、catalog 和相关 UI，不能只加 JSON 字段就宣称支持。

检查 catalog 与同类条目：同来源同内容更新旧条目；机制相同的效果优先做参数或变体；值得保留的相似参考说明差异。新生成作品重点比较构图、信息层级和交互机制，避免只换文案和颜色。

## 2. 导入模板

来源放 `_work/inbox/<来源名>/`，核对路径与实际入口。不要将所有含 index.html 的嵌套演示页自动当成独立站点。

支持目录、ZIP、Design Library `.site.json`。以下为 PowerShell 单行示例，尖括号占位符须替换后运行：

```powershell
py -X utf8 tools/ingest_template.py "<source>" --slug my-template --name "My Template" --zh "我的模板" --types company --ind restaurant --styles warm --license local_only
```

实际 flags 先查看脚本 / `--help`。`--replace` 会覆盖旧内容，先看目标并保留备份，不默认使用。

- `.site.json` 对应可定制 fragments；目录 / ZIP 对应 documents，保留原始页面样式。
- 模板文件为 `template.json`、`nav.html`、`footer.html`、`pages/*.html`、`TEMPLATE.md`；具体使用取决于 format。
- 内部页面链接使用 `{{p:slug}}`，首页 `{{p:home}}`。核对所有声明页面都有文件，菜单没有死链。
- 更新 `templates/order.json` 展示顺序，分类取自 taxonomy；页面 group 可使用项目适合的名称。
- TEMPLATE.md 写：适用场景、页面清单、定制能力、外部依赖、来源许可与限制。设计配方写在 `library/styles/<slug>/DESIGN.md`，与当前工具读取位置一致。

## 3. 效果、转场、色板

| 类型 | 内容 | 验收重点 |
|---|---|---|
| effect | `effects/<cat>/<slug>/effect.json`、`snippet.html`、`EFFECT.md`，追加 order | 元数据与 snippet 一致；说明触发方式、适用场景、依赖、键盘/触屏及减少动态效果 |
| transition | `transitions/<slug>/transition.json`、`transition.css`，追加 order | 使用现有 `--pt-*` 变量；不支持动画时正常跳转 |
| palette | `palettes/palettes.json` | 六色顺序 primary、secondary、text、accent、surface、border；核对实际文字/背景组合 |

效果使用自身的 `--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed --on-primary --on-accent`；模板则使用 `--c-*` / `--f-*`。不要统一替换变量名。

动画描述要区分 scroll-triggered、scroll-linked、parallax、sticky、scroll snap、horizontal scroll，先找对应机制再实现。鼠标效果不能只复制 hover 到触屏，需要实际点击、拖动或适当静态降级。

正文与背景对比度目标至少 4.5:1；主色不一定用于文字，需核对其实际用途和 on-primary / on-accent。不要仅因某个色板通过检查就认定所有组件可读。

## 4. Graphic 与 Assets

Graphic：`graphics/<slug>/{graphic.json,graphic.html,DESIGN.md}`，类型来自 `graphic_types`，更新 order。HTML 为固定画布，配方说明构图、字体、色彩、口吻、中文适配和不要清单。

Asset：`assets/<cat>/<slug>/{asset.json,<file>}`，类别来自 `asset_cats`。先放 `_work/inbox/assets/`：

```powershell
py -X utf8 tools/ingest_asset.py "<file-or-folder>" --cat cutout --tags gpu,hardware --license local_only --source "来源和许可依据"
```

文件夹导入通常共用类别与标签，先确认适合整批。单色 SVG 用 currentColor；位图保留合理格式与尺寸；复制到实际项目后引用，不引用本机私有绝对路径。

复用 Graphic 前先读设计配方；按需要选主视觉、背景和装饰，不强制每张图叠固定层数。缺真实素材列清单，不凭空补造客户资产。Canva 等外部来源的参考、原文件、素材分别检查许可；只重新排版不等于自动获得公开分发权。

## 5. 交给 AI / 目标项目

已连接 MCP 时可使用：

```text
search_library(kind="template", industry="restaurant", style="warm")
get_template(slug="<slug>", format="doc")
export_site(slug="<slug>", dest_dir="<absolute-project-path>", ext="html")
get_effect(slug="<slug>")
get_graphic(slug="<slug>", format="doc")
get_asset(slug="<slug>")
```

这些是工具调用示意，不是 shell 命令。先读当前工具定义再传参数。品牌色、字体、宽度、间距通过 export 参数输入；documents 模板不保证支持参数定制。

没有 MCP 时读本地 catalog 和条目文件。用网站 My list 复制的提示词时，补齐项目目标、内容和真实绝对路径；浏览器收藏不是备份，不要只靠它保存入库记录。

Elementor 先确认 widget / Free / Pro 能力，按目标项目的工具原生重建；受限 kit / part 只从本地读取，不向公共位置输出原文件。

## 6. 入库完成定义

1. 类型、slug、taxonomy、order、说明文件与实现一致。
2. 来源与许可有据可查；受限内容不会进入公共 catalog、文件、缩略图与下载包。
3. 预览可打开，内部链接正确；复制 / 下载的结果能在目标环境工作。
4. 按改动范围验证桌面、390px、768px，交互检查键盘、触屏、reduced-motion。
5. 内容有视觉修改时刷新缩略图，再构建；纯文档不重建。
6. 回报实际新增 / 更新数量、缺页 / 缺图、依赖、限制与上传清单，不为凑页数给所有模板补相同页面。

## 需要保留的排错经验

- Windows 命令使用 `-X utf8`；末尾输出报编码错误时先核实生成结果，不能直接判定全部构建未执行。
- grid 内有横向滚动容器时，检查父项 `min-width:0`，并测实际页面溢出。
- 8080 被占用时核对标题，别把其它站截图当本项目结果。
- Google Drive 的 `(1)` 副本可能是同步冲突，确认前不删除或替换原件。
- `_work` 和深层临时目录可能触发 Windows 路径长度问题；不要无必要复制整站。
