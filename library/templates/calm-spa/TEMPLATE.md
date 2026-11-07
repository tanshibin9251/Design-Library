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
