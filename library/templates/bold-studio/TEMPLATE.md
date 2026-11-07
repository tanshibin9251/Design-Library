# Bold Studio（粗犷工作室）

High contrast, oversized type. Black or white with one coral accent.

- **站型**：Portfolio, Company Website
- **行业**：Agency & Studio
- **风格**：Bold & Brutalist, Typographic, Swiss & Grid
- **字体**：标题 Anton · 正文 Work Sans

## 色板
| 角色 | 色值 |
|---|---|
| Primary | `#18181B` |
| Secondary | `#BE123C` |
| Text | `#18181B` |
| Accent | `#E11D48` |
| Surface | `#FAFAFA` |
| Border | `#E4E4E7` |

## 形状与字号
圆角 `0` · H1 `120px` · H2 `64px` · 区块间距 `100px`

## 页面（24）
- **Main**：Home（`home`）、About（`about`）、Services（`services`）、Single service（`service`）、Rates（`pricing`）、Contact（`contact`）
- **Shop**：Shop（`shop`）、Single Product（`product`）、Cart（`cart`）、Checkout（`checkout`）
- **Proof**：Testimonials（`testimonials`）、Team（`team`）、Work（`projects`）、Single Project（`project`）、Gallery（`gallery`）
- **Content**：Journal（`blog`）、Single post（`post`）、FAQ（`faq`）
- **Special**：Process（`process`）、Showreel（`showreel`）
- **Utility**：Careers（`careers`）、Privacy policy（`privacy`）、404 error（`404`）、Coming soon（`coming-soon`）

## 使用
- 内部链接统一写成 `{{p:slug}}`（首页 = `{{p:home}}`），导出时换成 `.html` / `.php`。
- 页面只含 `<main>` 里的内容；导航在 `nav.html`，页脚在 `footer.html`；共用 CSS 在 `library/runtime/site.css`，颜色/字体等通过 `tokens.css` 变量控制。
- 换色换字体：用 MCP `export_site` / `get_page` 的 overrides，或在网站里 Customize 后下载。
