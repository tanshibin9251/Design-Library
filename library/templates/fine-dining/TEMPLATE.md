# Fine Dining（高端餐饮）

Hushed, dark and restrained. Like a printed tasting menu.

- **站型**：Company Website, Landing Page
- **行业**：Restaurant & Cafe
- **风格**：Elegant & Luxury, Dark & Moody
- **字体**：标题 Cormorant Garamond · 正文 EB Garamond

## 色板
| 角色 | 色值 |
|---|---|
| Primary | `#1C1917` |
| Secondary | `#44403C` |
| Text | `#292524` |
| Accent | `#A16207` |
| Surface | `#FAFAF9` |
| Border | `#E7E5E4` |

## 形状与字号
圆角 `0` · H1 `76px` · H2 `48px` · 区块间距 `104px`

## 页面（26）
- **Main**：Home（`home`）、About（`about`）、Experiences（`services`）、Single service（`service`）、Gift Vouchers（`pricing`）、Contact（`contact`）
- **Shop**：Cellar Shop（`shop`）、Single Bottle（`product`）、Cart（`cart`）、Checkout（`checkout`）
- **Proof**：Testimonials（`testimonials`）、Team（`team`）、Press（`projects`）、Single Feature（`project`）、Gallery（`gallery`）
- **Content**：Journal（`blog`）、Single post（`post`）、FAQ（`faq`）
- **Special**：Menu（`menu`）、Wine list（`wine`）、Private dining（`private-dining`）、Reservations（`reservations`）
- **Utility**：Careers（`careers`）、Privacy policy（`privacy`）、404 error（`404`）、Coming soon（`coming-soon`）

## 使用
- 内部链接统一写成 `{{p:slug}}`（首页 = `{{p:home}}`），导出时换成 `.html` / `.php`。
- 页面只含 `<main>` 里的内容；导航在 `nav.html`，页脚在 `footer.html`；共用 CSS 在 `library/runtime/site.css`，颜色/字体等通过 `tokens.css` 变量控制。
- 换色换字体：用 MCP `export_site` / `get_page` 的 overrides，或在网站里 Customize 后下载。
