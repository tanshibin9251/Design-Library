# Magazine Classic（经典杂志）

Authoritative, read-first. Newspaper columns, rules and hierarchy.

- **站型**：Blog & Magazine, Company Website
- **行业**：News & Magazine
- **风格**：Editorial & Magazine, Typographic
- **字体**：标题 Libre Baskerville · 正文 Source Serif 4

## 色板
| 角色 | 色值 |
|---|---|
| Primary | `#18181B` |
| Secondary | `#991B1B` |
| Text | `#27272A` |
| Accent | `#DC2626` |
| Surface | `#FAFAFA` |
| Border | `#E5E5E5` |

## 形状与字号
圆角 `2px` · H1 `52px` · H2 `34px` · 区块间距 `72px`

## 页面（25）
- **Main**：Home（`home`）、About（`about`）、Subscribe（`services`）、Single service（`service`）、Subscribe（`pricing`）、Contact（`contact`）
- **Shop**：Shop（`shop`）、Single Product（`product`）、Cart（`cart`）、Checkout（`checkout`）
- **Proof**：Testimonials（`testimonials`）、Team（`team`）、Sections（`projects`）、Single Section（`project`）、Gallery（`gallery`）
- **Content**：Latest（`blog`）、Single post（`post`）、FAQ（`faq`）
- **Special**：Section page（`archive`）、Author page（`author`）、Newsletter（`newsletter`）
- **Utility**：Careers（`careers`）、Privacy policy（`privacy`）、404 error（`404`）、Coming soon（`coming-soon`）

## 使用
- 内部链接统一写成 `{{p:slug}}`（首页 = `{{p:home}}`），导出时换成 `.html` / `.php`。
- 页面只含 `<main>` 里的内容；导航在 `nav.html`，页脚在 `footer.html`；共用 CSS 在 `library/runtime/site.css`，颜色/字体等通过 `tokens.css` 变量控制。
- 换色换字体：用 MCP `export_site` / `get_page` 的 overrides，或在网站里 Customize 后下载。
