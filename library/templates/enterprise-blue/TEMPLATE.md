# Enterprise Blue（企业蓝）

Reliable and orderly. Reads like a well-set annual report.

- **站型**：Company Website, Landing Page
- **行业**：Business & Consulting, IT & Technology
- **风格**：Corporate & Professional, Swiss & Grid
- **字体**：标题 Source Sans 3 · 正文 Source Sans 3

## 色板
| 角色 | 色值 |
|---|---|
| Primary | `#1E3A5F` |
| Secondary | `#334155` |
| Text | `#1F2937` |
| Accent | `#2563EB` |
| Surface | `#F9FAFB` |
| Border | `#E5E7EB` |

## 形状与字号
圆角 `6px` · H1 `60px` · H2 `40px` · 区块间距 `88px`

## 页面（21）
- **Main**：Home（`home`）、About（`about`）、Services（`services`）、Single service（`service`）、Engagements（`pricing`）、Contact（`contact`）
- **Proof**：Testimonials（`testimonials`）、Team（`team`）、Case Studies（`projects`）、Single Case Study（`project`）、Gallery（`gallery`）
- **Content**：Insights（`blog`）、Single post（`post`）、FAQ（`faq`）
- **Special**：Industries（`industries`）、Resources（`resources`）、Book a call（`book-call`）
- **Utility**：Careers（`careers`）、Privacy policy（`privacy`）、404 error（`404`）、Coming soon（`coming-soon`）

## 使用
- 内部链接统一写成 `{{p:slug}}`（首页 = `{{p:home}}`），导出时换成 `.html` / `.php`。
- 页面只含 `<main>` 里的内容；导航在 `nav.html`，页脚在 `footer.html`；共用 CSS 在 `library/runtime/site.css`，颜色/字体等通过 `tokens.css` 变量控制。
- 换色换字体：用 MCP `export_site` / `get_page` 的 overrides，或在网站里 Customize 后下载。

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。

### 本轮专属修复
首页空白 Hero image 改为可展开的四阶段交付图解；See case studies 指向实际案例索引。
