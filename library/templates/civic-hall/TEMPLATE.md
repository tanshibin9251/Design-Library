# Civic Hall（市政厅）

Municipal service directory: accessibility toolbar with text size and high contrast, task-first hero search, bin-day lookup and council meeting list.

- **字体**：标题与正文 Atkinson Hyperlegible

## 页面（21）
- Home（`home`）
- About（`about`）
- Services（`services`）
- Single Service（`service`）
- Fees & Permits（`pricing`）
- Contact（`contact`）
- Testimonials（`testimonials`）
- Team（`team`）
- Community Projects（`projects`）
- Single Project（`project`）
- Gallery（`gallery`）
- News & Notices（`blog`）
- Single post（`post`）
- FAQ（`faq`）
- Council meetings（`schedule`）
- Report an issue（`booking`）
- Notices by email（`newsletter`）
- Careers（`careers`）
- Privacy policy（`privacy`）
- 404 error（`404`）
- Coming soon（`coming-soon`）

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。
