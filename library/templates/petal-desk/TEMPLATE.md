# Petal Desk（花瓣项目台）

Warm project & task desk for web freelancers: floating dock nav, colour-block accordion tasks, scalloped phase path, tickable steps and a hand-drawn how-to guide.

- **字体**：标题 Fraunces · 正文 Hanken Grotesk（便条用 Caveat）

## 页面（9）
- Today (dashboard)（`home`）
- Projects（`projects`）
- Project: phases & tasks（`project`）
- Clients（`clients`）
- Add client & project（`client-new`）
- Task templates（`templates`）
- Template + how-to editor（`template-edit`）
- Sign in（`login`）
- 404 error（`404`）

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。
