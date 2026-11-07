# Pocket App Landing（应用落地页）

Light app landing page with a gradient headline, a CSS-drawn phone with floating cards, feature tiles, monthly/yearly pricing toggle and a changelog.

- **字体**：标题 Onest · 正文 Onest

## 页面（8）
- Home（`home`）
- Features（`features`）
- Pricing（`pricing`）
- Download（`download`）
- What’s new（`changelog`）
- FAQ（`faq`）
- Privacy policy（`privacy`）
- 404 error（`404`）

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。

### 本轮专属修复
App Store / Google Play 明确为演示链接，点击显示配置说明，不假装有安装包。
