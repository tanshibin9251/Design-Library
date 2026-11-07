# Pixel Arena（像素竞技场）

Chunky, loud esports and gaming-cafe theme: lilac, bubblegum and violet with big rounded type.

- **站型**：Landing Page, Company Website, E-commerce
- **行业**：Gaming & Esports
- **风格**：Y2K, Neo-Brutalism, Maximalist
- **字体**：标题 Orbitron · 正文 Archivo

## 色板
| 角色 | 色值 |
|---|---|
| Primary | `#3b1a8f` |
| Secondary | `#7a1fa2` |
| Text | `#1a1033` |
| Accent | `#c4126f` |
| Surface | `#f2ecff` |
| Border | `#1a1033` |

## 形状与字号
圆角 `20px` · H1 `84px` · H2 `50px` · 区块间距 `84px`

## 页面（25）
- **Main**：Home（`home`）、About（`about`）、Arena Cafe（`services`）、Single Package（`service`）、Memberships（`pricing`）、Contact（`contact`）
- **Shop**：Merch Shop（`shop`）、Single Item（`product`）、Cart（`cart`）、Checkout（`checkout`）
- **Proof**：Testimonials（`testimonials`）、Roster（`team`）、Highlights（`projects`）、Single Highlight（`project`）、Gallery（`gallery`）
- **Content**：News（`blog`）、Single post（`post`）、FAQ（`faq`）
- **Special**：Events（`schedule`）、Book a station（`booking`）、Free first hour（`trial`）
- **Utility**：Careers（`careers`）、Privacy policy（`privacy`）、404 error（`404`）、Coming soon（`coming-soon`）

## 使用
- 内部链接统一写成 `{{p:slug}}`（首页 = `{{p:home}}`），导出时换成 `.html` / `.php`。
- 页面只含 `<main>` 里的内容；导航在 `nav.html`，页脚在 `footer.html`；共用 CSS 在 `library/runtime/site.css`，颜色/字体等通过 `tokens.css` 变量控制。
- 换色换字体：用 MCP `export_site` / `get_page` 的 overrides，或在网站里 Customize 后下载。
