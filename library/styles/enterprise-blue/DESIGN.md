# Enterprise Blue（企业蓝）

> 起点母版。色板与字体来自 EMCP Tools 的免费 brand kit（GPL-2.0-or-later）；「Feel / 形状 / 构图特征 / 不要」由我们自己补充，是**待你验证的起点**，不是定案。用过一两个客户后请回来改成你自己的版本。

- **适合**：Company；B2B 服务、IT、工程顾问、物流、会计/法律事务所
- **适合站型**：company, landing

## Feel
可靠、克制、有秩序。像一份排版很好的年报，而不是科技广告。

## 调色（角色 → 色号）
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#1E3A5F` | 主标题、主要按钮、深色区块 |
| Secondary | `#334155` | 副标题、次要按钮、页脚 |
| Text | `#1F2937` | 正文 |
| Accent | `#2563EB` | **只用在**：主 CTA、关键数字、链接 hover（每屏不超过 2 处） |
| Surface | `#F9FAFB` | 底色 / 分隔线 / 状态色 |
| Border | `#E5E7EB` | 底色 / 分隔线 / 状态色 |

## 字体
| 角色 | 字体 | 字重 | 桌面字号 |
|---|---|---|---|
| Primary Headings | Source Sans 3 | 700 | 46px |
| Secondary Headings | Source Sans 3 | 600 | 24px |
| Body | Source Sans 3 | 400 | 16px |
| Accent | Source Sans 3 | 600 | 13px |

Google Fonts：Source Sans 3
**中文内容必须加中文 fallback**：无衬线标题/正文配 `Noto Sans SC`；衬线标题配 `Noto Serif SC`。中文标题不要用斜体。

## 形状与质感
圆角 4–6px；用细分隔线和大量留白，阴影几乎不用；蓝色只出现在按钮、链接和一个关键数字上。

## 构图特征（Design signature）
1. 首屏用大标题 + 一句话价值主张 + 单一主要 CTA，右侧放真实项目/办公室照片或一张干净的数据卡，不放插画。
2. 「信任数字」做成一条横向数据带（成立年份 / 完成项目 / 客户数），数字用超大字号，标签很小。
3. 服务列表用「问题 → 我们怎么做」两列表格式排版，不用一排图标卡片。

## 不要（这套母版最容易变普通的地方）
三张一模一样带阴影的图标卡片；蓝紫渐变背景；配图全是握手/笔记本电脑的图库照。

## Elementor 落地提示
- 全局色/字体由使用者在 Elementor Site Settings 手动设定，Claude 只读 `design.md` 里登记的值，不代改。
- 版式用 Container（flex）+ 原生 widget；分隔线用 Divider 或 Container border，不用自定义 CSS 硬堆。
- 动效只用 Elementor 原生 Motion Effects / Entrance Animation，每页不超过两种。
- 参考页面样式见 `Design Library/README.md` 的「反普通清单」。
