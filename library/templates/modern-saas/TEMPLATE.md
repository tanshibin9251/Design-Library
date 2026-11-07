# Modern SaaS（现代 SaaS）

Clean, confident, product-first. Calm motion.

- **站型**：Landing Page, Company Website
- **行业**：SaaS & Startup, IT & Technology
- **风格**：Minimal & Clean, Corporate & Professional
- **字体**：标题 Inter · 正文 Inter

## 色板
| 角色 | 色值 |
|---|---|
| Primary | `#4F46E5` |
| Secondary | `#0F172A` |
| Text | `#1E293B` |
| Accent | `#0E7490` |
| Surface | `#F8FAFC` |
| Border | `#E2E8F0` |

## 形状与字号
圆角 `14px` · H1 `68px` · H2 `42px` · 区块间距 `96px`

## 页面（22）
- **Main**：Home（`home`）、About（`about`）、Features（`services`）、Single service（`service`）、Pricing（`pricing`）、Contact（`contact`）
- **Proof**：Testimonials（`testimonials`）、Team（`team`）、Customers（`projects`）、Single Customer Story（`project`）、Gallery（`gallery`）
- **Content**：Blog（`blog`）、Single post（`post`）、FAQ（`faq`）
- **Special**：Features（`features`）、Integrations（`integrations`）、Changelog（`changelog`）、Sign up（`signup`）
- **Utility**：Careers（`careers`）、Privacy policy（`privacy`）、404 error（`404`）、Coming soon（`coming-soon`）

## 使用
- 内部链接统一写成 `{{p:slug}}`（首页 = `{{p:home}}`），导出时换成 `.html` / `.php`。
- 页面只含 `<main>` 里的内容；导航在 `nav.html`，页脚在 `footer.html`；共用 CSS 在 `library/runtime/site.css`，颜色/字体等通过 `tokens.css` 变量控制。
- 换色换字体：用 MCP `export_site` / `get_page` 的 overrides，或在网站里 Customize 后下载。
