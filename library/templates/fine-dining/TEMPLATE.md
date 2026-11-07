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

## 高清外链摄影版本（2026-11-07）
已添加按行业选择的外链示意摄影，来源、作者、原始宽高见 images.json。首图/特色图维持比例、按位置裁切，非首屏延迟加载；加载失败显示缺图。照片不保存在仓库或导出包内，预览及导出需要联网。库存图不代表实际产品、人员、房源、客户项目或成果；未找到对应真实资产的占位保留，不冒用照片。

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。
