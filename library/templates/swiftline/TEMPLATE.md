# Swiftline Logistics（迅捷物流）

Logistics site with tracking built into the header, a parcel timeline that responds to the number, and a zone/weight/speed price calculator.

- **字体**：标题 Exo 2 · 正文 Assistant

## 页面（23）
- Home（`home`）
- About（`about`）
- Services（`services`）
- Single Service（`service`）
- Rates（`pricing`）
- Contact（`contact`）
- Testimonials（`testimonials`）
- Team（`team`）
- Customer Stories（`projects`）
- Single Customer story（`project`）
- Gallery（`gallery`）
- News（`blog`）
- Single post（`post`）
- FAQ（`faq`）
- Track a shipment（`tracking`）
- Get a quote（`quote`）
- Our network（`service-areas`）
- Industries we serve（`industries`）
- How shipping works（`process`）
- Careers（`careers`）
- Privacy policy（`privacy`）
- 404 error（`404`）
- Coming soon（`coming-soon`）

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。
