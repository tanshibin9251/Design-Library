# Restaurant Warm（温暖餐饮）

Family kitchen: dotted-stitch header with live open/closed pill, an interactive rice-set builder and a spice-dot menu.

- **字体**：标题 Bree Serif · 正文 Mukta

## 页面（25）
- Home（`home`）
- About（`about`）
- Catering（`services`）
- Single service（`service`）
- Catering Packages（`pricing`）
- Contact（`contact`）
- Order Online（`shop`）
- Single Dish（`product`）
- Cart（`cart`）
- Checkout（`checkout`）
- Testimonials（`testimonials`）
- Team（`team`）
- Our Dishes（`projects`）
- Single Dish（`project`）
- Gallery（`gallery`）
- Stories（`blog`）
- Single post（`post`）
- FAQ（`faq`）
- Menu（`menu`）
- Book a table（`reservations`）
- Catering（`catering`）
- Careers（`careers`）
- Privacy policy（`privacy`）
- 404 error（`404`）
- Coming soon（`coming-soon`）

## 高清外链摄影版本（2026-11-07）
已添加按行业选择的外链示意摄影，来源、作者、原始宽高见 images.json。首图/特色图维持比例、按位置裁切，非首屏延迟加载；加载失败显示缺图。照片不保存在仓库或导出包内，预览及导出需要联网。库存图不代表实际产品、人员、房源、客户项目或成果；未找到对应真实资产的占位保留，不冒用照片。

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。

### 本轮专属修复
移除米饭组合中未显示的 RM 8 基础费；选菜、数量、购物车和结账金额同步。具名菜品的说明随选择更新；移除服饰尺码、洗护、30 天退货等错误文案。结账没有银行卡收集框。
