# Modern SaaS（现代 SaaS）

> 起点母版。色板与字体来自 EMCP Tools 的免费 brand kit（GPL-2.0-or-later）；「Feel / 形状 / 构图特征 / 不要」由我们自己补充，是**待你验证的起点**，不是定案。用过一两个客户后请回来改成你自己的版本。

- **适合**：Landing Page / Company；软件、App、初创、线上课程平台
- **适合站型**：landing, company

## Feel
干净、自信、偏产品感。信息层级清楚，动效克制。

## 调色（角色 → 色号）
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#4F46E5` | 主标题、主要按钮、深色区块 |
| Secondary | `#0F172A` | 副标题、次要按钮、页脚 |
| Text | `#1E293B` | 正文 |
| Accent | `#0E7490` | **只用在**：主 CTA、关键数字、链接 hover（每屏不超过 2 处） |
| Surface | `#F8FAFC` | 底色 / 分隔线 / 状态色 |
| Border | `#E2E8F0` | 底色 / 分隔线 / 状态色 |
| Success | `#15803D` | 底色 / 分隔线 / 状态色 |
| Danger | `#B91C1C` | 底色 / 分隔线 / 状态色 |

## 字体
| 角色 | 字体 | 字重 | 桌面字号 |
|---|---|---|---|
| Primary Headings | Inter | 700 | 48px |
| Secondary Headings | Inter | 600 | 24px |
| Body | Inter | 400 | 16px |
| Accent | Inter | 500 | 14px |

Google Fonts：Inter
**中文内容必须加中文 fallback**：无衬线标题/正文配 `Noto Sans SC`；衬线标题配 `Noto Serif SC`。中文标题不要用斜体。

## 形状与质感
圆角 8–12px；淡边框 + 极浅阴影；Indigo 只用于主 CTA 和链接，深色区块用 Slate。

## 构图特征（Design signature）
1. 首屏放产品截图或界面示意（真实的），标题不超过两行。
2. 用「功能 → 结果」的交替左右布局代替网格卡片；每个功能配一张截图。
3. 定价/方案区用三栏，但推荐方案用深色底反白，形成唯一视觉重点。

## 不要（这套母版最容易变普通的地方）
到处都是紫色渐变光斑；空泛的「赋能」「一站式」标题；截图全是模糊的假数据。

## Elementor 落地提示
- 全局色/字体由使用者在 Elementor Site Settings 手动设定，Claude 只读 `design.md` 里登记的值，不代改。
- 版式用 Container（flex）+ 原生 widget；分隔线用 Divider 或 Container border，不用自定义 CSS 硬堆。
- 动效只用 Elementor 原生 Motion Effects / Entrance Animation，每页不超过两种。
- 参考页面样式见 `Design Library/README.md` 的「反普通清单」。
