# Nexus AI（未来科技）v2

> 自有原创母版，授权 ok。

- **适合**：Landing / Company；AI API 平台、开发者工具、模型公司官网

## Feel
纸质感的 AI 实验室：不是霓虹深色，是暖白纸、墨黑、一点余烬橙。文档型、开发者友好、少装饰。

## 调色
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#1a1a1a` | 墨黑：标题、描边、按钮 |
| Secondary | `#6b6a63` | 灰：说明、标签 |
| Text | `#1f1e1b` | 正文 |
| Accent | `#ff5c35` | 余烬橙：强调词、运行按钮、进度 |
| Surface | `#f6f4ef` | 暖纸白 |
| Border | `#dcd8cd` | 细线 |

## 字体
标题 Rethink Sans 700（字距 -.04em）；正文 Karla；代码区使用系统等宽字体。
中文内容配 Noto Sans SC / Noto Serif SC，中文标题不要斜体。

## 构图特征（Design signature）
1. 首屏不放插画或样机，直接是一块「请求 / 响应」双栏：左 curl 请求、右按 Run 逐字流出 JSON，光标闪烁。
2. 模型是「价格表」：模型名与副标、上下文、每百万 token 价格、速度条（橙色），不是卡片。
3. 账单估算器：滑块（月 token 量）+ 模型下拉，实时算月费。
4. 更新日志是带日期与标签（New / Improved / Fixed）的细线列表。
5. 顶栏最右只有一个黑色「Get API key」按钮；没有渐变、没有发光。

## 不要
- 不要青色 / 粉色霓虹、深色玻璃拟态（旧版 / aurora / commit-camp）。
- 不要终端窗口外壳（commit-camp 用过）：这里的双栏是平的细线框。
- 不要「机器人」「神经网络」插画。
- 不要超过三个字号层级。
