# Bold Studio（粗犷工作室）

> 起点母版。色板与字体来自 EMCP Tools 的免费 brand kit（GPL-2.0-or-later）；「Feel / 形状 / 构图特征 / 不要」由我们自己补充，是**待你验证的起点**，不是定案。用过一两个客户后请回来改成你自己的版本。

- **适合**：Portfolio / Company；设计工作室、创意代理商、摄影、活动策划
- **适合站型**：portfolio, company

## Feel
高对比、有态度、大字压场。黑底/白底 + 一个跳出来的珊瑚红。

## 调色（角色 → 色号）
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#18181B` | 主标题、主要按钮、深色区块 |
| Secondary | `#BE123C` | 副标题、次要按钮、页脚 |
| Text | `#18181B` | 正文 |
| Accent | `#E11D48` | **只用在**：主 CTA、关键数字、链接 hover（每屏不超过 2 处） |
| Surface | `#FAFAFA` | 底色 / 分隔线 / 状态色 |
| Border | `#E4E4E7` | 底色 / 分隔线 / 状态色 |
| Coral | `#FB7185` | 底色 / 分隔线 / 状态色 |
| Electric Rose | `#FF4D6D` | 底色 / 分隔线 / 状态色 |

## 字体
| 角色 | 字体 | 字重 | 桌面字号 |
|---|---|---|---|
| Primary Headings | Anton | 400 | 64px |
| Secondary Headings | Anton | 400 | 32px |
| Body | Work Sans | 400 | 16px |
| Accent | Work Sans | 700 | 13px |

Google Fonts：Anton, Work Sans
**中文内容必须加中文 fallback**：无衬线标题/正文配 `Noto Sans SC`；衬线标题配 `Noto Serif SC`。中文标题不要用斜体。

## 形状与质感
几乎直角（0–2px）；粗线条分隔；大字标题用 Anton 全大写，紧行距。

## 构图特征（Design signature）
1. 首屏只有超大标题 + 一张满版作品图，导航极简。
2. 作品网格不对称：一大三小交错，悬停时整块反色，而不是统一 3 列方格。
3. Footer 做成一个巨大的联络 CTA（邮箱/WhatsApp 用超大字）。

## 不要（这套母版最容易变普通的地方）
把 Anton 用在正文；红色铺满整个区块；作品图统一裁成同尺寸正方形，失去节奏。

## Elementor 落地提示
- 全局色/字体由使用者在 Elementor Site Settings 手动设定，Claude 只读 `design.md` 里登记的值，不代改。
- 版式用 Container（flex）+ 原生 widget；分隔线用 Divider 或 Container border，不用自定义 CSS 硬堆。
- 动效只用 Elementor 原生 Motion Effects / Entrance Animation，每页不超过两种。
- 参考页面样式见 `Design Library/README.md` 的「反普通清单」。
