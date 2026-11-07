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

## 页面（23）
- **Main**：Home（`home`）、About（`about`）、Product overview（`services`）、Single service（`service`）、Pricing（`pricing`）、Interactive product demo（`demo`）、Contact（`contact`）
- **Proof**：Testimonials（`testimonials`）、Team（`team`）、Customers（`projects`）、Single Customer Story（`project`）、Gallery（`gallery`）
- **Content**：Blog（`blog`）、Single post（`post`）、FAQ（`faq`）
- **Special**：Features（`features`）、Integrations（`integrations`）、Changelog（`changelog`）、Sign up（`signup`）
- **Utility**：Careers（`careers`）、Privacy policy（`privacy`）、404 error（`404`）、Coming soon（`coming-soon`）

## 使用
- 内部链接统一写成 `{{p:slug}}`（首页 = `{{p:home}}`），导出时换成 `.html` / `.php`。
- 页面只含 `<main>` 里的内容；导航在 `nav.html`，页脚在 `footer.html`；共用 CSS 在 `library/runtime/site.css`，颜色/字体等通过 `tokens.css` 变量控制。
- 换色换字体：用 MCP `export_site` / `get_page` 的 overrides，或在网站里 Customize 后下载。

## 2026-11-07 升级
试用 CTA 统一进入 signup；价格选择进入同一路径。Product overview 与 Features 区分；新增 Board / Timeline / Report 产品演示，使用示例数据，不假装有视频或真实 SaaS 后台。signup 为本地验证演示，不创建账户。共享模板基础层提供键盘、手机导航与表单反馈，并随导出保留。

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。

### 本轮专属修复
首页空白产品 mock 改为示例看板，15 个功能占位改为产品原生图解；新增 Board / Timeline / Report 交互演示。导航、页脚与页面名同步区分 Product overview / Features。
