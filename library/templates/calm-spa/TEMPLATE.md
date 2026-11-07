# Calm Spa（宁静水疗）

Quiet, airy and breathable. Muted teal and generous whitespace.

- **站型**：Company Website, Landing Page, E-commerce
- **行业**：Health & Wellness
- **风格**：Organic & Natural, Minimal & Clean, Pastel & Soft
- **字体**：标题 Crimson Pro · 正文 Mulish

## 色板
| 角色 | 色值 |
|---|---|
| Primary | `#115E59` |
| Secondary | `#134E4A` |
| Text | `#1F2937` |
| Accent | `#0F766E` |
| Surface | `#F0FDFA` |
| Border | `#CCFBF1` |

## 形状与字号
圆角 `24px` · H1 `64px` · H2 `42px` · 区块间距 `96px`

## 页面（25）
- **Main**：Home（`home`）、About（`about`）、Treatments（`services`）、Single Treatment（`service`）、Packages（`pricing`）、Contact（`contact`）
- **Shop**：Shop（`shop`）、Single Product（`product`）、Cart（`cart`）、Checkout（`checkout`）
- **Proof**：Testimonials（`testimonials`）、Team（`team`）、Rituals（`projects`）、Single Ritual（`project`）、Gallery（`gallery`）
- **Content**：Journal（`blog`）、Single post（`post`）、FAQ（`faq`）
- **Special**：Booking（`booking`）、Gift cards（`gift-cards`）、Rooms（`rooms`）
- **Utility**：Careers（`careers`）、Privacy policy（`privacy`）、404 error（`404`）、Coming soon（`coming-soon`）

## 使用
- 内部链接统一写成 `{{p:slug}}`（首页 = `{{p:home}}`），导出时换成 `.html` / `.php`。
- 页面只含 `<main>` 里的内容；导航在 `nav.html`，页脚在 `footer.html`；共用 CSS 在 `library/runtime/site.css`，颜色/字体等通过 `tokens.css` 变量控制。
- 换色换字体：用 MCP `export_site` / `get_page` 的 overrides，或在网站里 Customize 后下载。

## 高清外链摄影版本（2026-11-07）
已添加按行业选择的外链示意摄影，来源、作者、原始宽高见 images.json。首图/特色图维持比例、按位置裁切，非首屏延迟加载；加载失败显示缺图。照片不保存在仓库或导出包内，预览及导出需要联网。库存图不代表实际产品、人员、房源、客户项目或成果；未找到对应真实资产的占位保留，不冒用照片。

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。
