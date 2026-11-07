# Calm Spa（宁静水疗）

> 起点母版。色板与字体来自 EMCP Tools 的免费 brand kit（GPL-2.0-or-later）；「Feel / 形状 / 构图特征 / 不要」由我们自己补充，是**待你验证的起点**，不是定案。用过一两个客户后请回来改成你自己的版本。

- **适合**：Company / Landing / 混合；美容院、Spa、瑜伽、疗愈、诊所形象
- **适合站型**：company, landing, mixed

## Feel
安静、通透、呼吸感。低饱和青绿，大量留白。

## 调色（角色 → 色号）
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#115E59` | 主标题、主要按钮、深色区块 |
| Secondary | `#134E4A` | 副标题、次要按钮、页脚 |
| Text | `#1F2937` | 正文 |
| Accent | `#0F766E` | **只用在**：主 CTA、关键数字、链接 hover（每屏不超过 2 处） |
| Surface | `#F0FDFA` | 底色 / 分隔线 / 状态色 |
| Border | `#CCFBF1` | 底色 / 分隔线 / 状态色 |
| Eucalyptus | `#5EEAD4` | 底色 / 分隔线 / 状态色 |
| Mist | `#A7F3D0` | 底色 / 分隔线 / 状态色 |

## 字体
| 角色 | 字体 | 字重 | 桌面字号 |
|---|---|---|---|
| Primary Headings | Crimson Pro | 600 | 48px |
| Secondary Headings | Crimson Pro | 600 | 24px |
| Body | Mulish | 400 | 16px |
| Accent | Mulish | 600 | 14px |

Google Fonts：Crimson Pro, Mulish
**中文内容必须加中文 fallback**：无衬线标题/正文配 `Noto Sans SC`；衬线标题配 `Noto Serif SC`。中文标题不要用斜体。

## 形状与质感
圆角 16–24px 的图片；柔和淡色块；按钮胶囊形；几乎不用深色。

## 构图特征（Design signature）
1. 首屏用一张安静的空间/手法照片，标题用 Crimson Pro，字距放松。
2. 疗程列表用「名称 + 时长 + 价格 + 一句感受」的清单，而不是图标卡片。
3. 预约 CTA 固定在页面右下（WhatsApp），语气温和不催促。

## 不要（这套母版最容易变普通的地方）
莲花/石头/竹子的库存图堆叠；文字太小太淡；每个区块背景色都不同。

## Elementor 落地提示
- 全局色/字体由使用者在 Elementor Site Settings 手动设定，Claude 只读 `design.md` 里登记的值，不代改。
- 版式用 Container（flex）+ 原生 widget；分隔线用 Divider 或 Container border，不用自定义 CSS 硬堆。
- 动效只用 Elementor 原生 Motion Effects / Entrance Animation，每页不超过两种。
- 参考页面样式见 `Design Library/README.md` 的「反普通清单」。
