# Magazine Classic（经典杂志）

> 起点母版。色板与字体来自 EMCP Tools 的免费 brand kit（GPL-2.0-or-later）；「Feel / 形状 / 构图特征 / 不要」由我们自己补充，是**待你验证的起点**，不是定案。用过一两个客户后请回来改成你自己的版本。

- **适合**：Blog / 内容型 Company；新闻、行业媒体、长文内容站
- **适合站型**：company

## Feel
权威、可读、阅读优先。像报纸版面：栏、线、层级。

## 调色（角色 → 色号）
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#18181B` | 主标题、主要按钮、深色区块 |
| Secondary | `#991B1B` | 副标题、次要按钮、页脚 |
| Text | `#27272A` | 正文 |
| Accent | `#DC2626` | **只用在**：主 CTA、关键数字、链接 hover（每屏不超过 2 处） |
| Surface | `#FAFAFA` | 底色 / 分隔线 / 状态色 |
| Border | `#E5E5E5` | 底色 / 分隔线 / 状态色 |

## 字体
| 角色 | 字体 | 字重 | 桌面字号 |
|---|---|---|---|
| Primary Headings | Libre Baskerville | 700 | 56px |
| Secondary Headings | Libre Baskerville | 700 | 30px |
| Body | Source Serif 4 | 400 | 18px |
| Accent | Inter | 600 | 14px |

Google Fonts：Libre Baskerville, Source Serif 4, Inter
**中文内容必须加中文 fallback**：无衬线标题/正文配 `Noto Sans SC`；衬线标题配 `Noto Serif SC`。中文标题不要用斜体。

## 形状与质感
直角；黑色细线分栏；红色只用于栏目标签和链接 hover。

## 构图特征（Design signature）
1. 首页头条大图 + 侧栏 3 条次要文章，栏目名用小型红色大写标签。
2. 文章页正文宽度控制在 65–75 字符，引文用大号衬线 + 左侧红线。
3. 用日期/作者/阅读时长作为元信息层，字号小、颜色淡。

## 不要（这套母版最容易变普通的地方）
所有文章卡片同大小；正文太宽；把红色用作大面积背景。

## Elementor 落地提示
- 全局色/字体由使用者在 Elementor Site Settings 手动设定，Claude 只读 `design.md` 里登记的值，不代改。
- 版式用 Container（flex）+ 原生 widget；分隔线用 Divider 或 Container border，不用自定义 CSS 硬堆。
- 动效只用 Elementor 原生 Motion Effects / Entrance Animation，每页不超过两种。
- 参考页面样式见 `Design Library/README.md` 的「反普通清单」。
