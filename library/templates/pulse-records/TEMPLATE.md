# Pulse Records（脉冲唱片）

Record-label shop with a CSS turntable that spins with 33/45 RPM, a sideways scroll record crate with price stickers and catalogue-number rows.

- **字体**：标题 Rubik Mono One · 正文 Chivo

## 页面（24）
- Home（`home`）
- About（`about`）
- Merch（`services`）
- Single Merch（`service`）
- Subscribe（`pricing`）
- Contact（`contact`）
- Releases（`shop`）
- Single Release（`product`）
- Cart（`cart`）
- Checkout（`checkout`）
- Testimonials（`testimonials`）
- Artists（`team`）
- Artists（`projects`）
- Single Artist（`project`）
- Gallery（`gallery`）
- News（`blog`）
- Single post（`post`）
- FAQ（`faq`）
- Shows（`schedule`）
- Submit a demo（`booking`）
- Careers（`careers`）
- Privacy policy（`privacy`）
- 404 error（`404`）
- Coming soon（`coming-soon`）

## 高清外链摄影版本（2026-11-07）
已添加按行业选择的外链示意摄影，来源、作者、原始宽高见 images.json。首图/特色图维持比例、按位置裁切，非首屏延迟加载；加载失败显示缺图。照片不保存在仓库或导出包内，预览及导出需要联网。库存图不代表实际产品、人员、房源、客户项目或成果；未找到对应真实资产的占位保留，不冒用照片。

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。
