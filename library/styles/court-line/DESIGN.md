# Court Line（球场线）

> 自有原创母版，授权 ok。2026-10-13 由 `slant-pro` 改版而来（旧版：Oswald 全大写 + 橙色斜切面板，与 kpsmash / kumpoo 的结构过于接近）。用羽毛球场地的几何当版面语言，不依赖斜切。

- **适合**：Company / Ecommerce；运动用品品牌的公司介绍站（羽毛球为主，也可换成其他球类）

## Feel
浅色、冷静、像一张场地图纸。黑 / 灰 / 白三色（来自 PR Smash logo），所有结构来自细线：分区、标注、尺寸。标题大小写混排，标签和编号用等宽字，不再全大写粗体。

## 调色
严格黑 / 灰 / 白（来自 PR Smash logo 的黑、灰和白色版），不加第四种颜色。
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#0b0b0c` | 标题、主按钮、线条、「去商店」格 |
| Secondary | `#131416` | 页脚底 |
| Text | `#17181a` | 正文 |
| Accent | `#45484f` | 编号、等宽标签、灰色场地面板、hover |
| Surface | `#ffffff` | 页面底 |
| Border | `#dcdde0` | 细线分隔 |

## 字体
标题 Bricolage Grotesque 700，大小写混排，字距 -.025em；正文 Instrument Sans；标签 / 编号 / 按钮 IBM Plex Mono 大写、字距 .08em。中文内容配 Noto Sans SC，中文标题不要斜体。

## 构图特征（Design signature）
1. 首屏：标题和说明横向并排，下方整幅「球场图纸」SVG（场线、网线、1.98 m / 13.40 m / 6.10 m 尺寸标注、一道球的轨迹），logo 放在网线中央的白色标牌里；不再是左文右图 + 斜切面板。
2. 导航：细线页头，链接带编号（01 Home），当前页下划线是黑色粗线；页头底有双线（球场边线）。
3. 内容分区用「场区格子」：品类是 A1 / A2 / B1… 编号格，格与格共用细线，没有卡片、阴影、圆角；hover 底部黑线滑出、格子淡灰。
4. 近黑只出现在页脚和「去商店」格；醒目的面板用石板灰 + 白色场线（外框 + 中线），放门店信息或 WhatsApp。
5. 内页页头：面包屑 + 标题 + 页码（02 / 08），底下是带刻度的基线，像尺子。
6. 页底大字 CTA 用「下划线从左画到右」的 hover，不用色块。

## 不要
- 不要斜切、平行四边形、clip-path 装饰（斜切属于 kpsmash / kumpoo / 旧 slant-pro）。
- 不要全大写粗体标题；全大写只给等宽标签。
- 不要三张一模一样带阴影的图标卡片、不要渐变、不要阴影、不要圆角。
- 不要加黑 / 灰 / 白以外的颜色；灰色面板每屏最多一块。

## Elementor 落地提示
- 全局色/字体由使用者在 Elementor Site Settings 手动设定，Claude 只读 `design.md` 里登记的值。
- 场区格子用 Container grid + 边框（1px），不要用多个带阴影的 widget；球场图纸 SVG 放 HTML widget。
- 动效只用 Elementor 原生 Motion Effects / Entrance Animation，每页不超过两种。
