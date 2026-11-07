# Crumb & Co（面包咖啡馆）

Craft café and bakery site with a chalkboard of today's bakes, swing-tag product cards and order-ahead pick-up slots.

- **字体**：标题 Caprasimo · 正文 Outfit

## 高清外链摄影示范（2026-11-07）

首页、Menu、Today’s bakes、Catering、Story、Visit、Order 共 7 个内容页加入摄影；FAQ / Privacy / 404 保持文字页面。首页保留手作纸袋风格，加入拱形晨间摄影、粉笔板和摄影背景 CTA。

- 8 张照片均来自 Unsplash 免费集合。来源、作者及已核验原始尺寸记录在 `images.json`；原图最短边至少 1848px。请求的裁切图最短边至少 1080px，未靠放大低清原图满足要求。
- 仅使用 `images.unsplash.com` 外链，项目和导出 ZIP 不保存照片原文件。预览与导出都需要联网；外链可用性会随来源变化。
- 图片是布局示意，不代表真实门店、员工或精确商品。页脚有摄影来源，正式商用站应替换为品牌自己的实拍。
- 首图优先加载，内容图延迟加载；固定尺寸防止布局跳动，失败时显示缺图文本。Visit 的真实地图仍待用户填写，不能用空间摄影冒充地址证明。
- 小屏新增可键盘操作的 Menu；Order 提供纯本地的验证与请求预览，不发送订单、不收集付款、不预约真实时段。
- 页脚使用独立的品牌介绍 + Café / Visit 三栏网格；手机上品牌独占一行、导航分两栏。版权与隐私归入底栏，图片来源折叠保留；标题和链接显式使用 footer 对比色，避免继承主色后隐没。
- 官网模板规则与后续批次见根目录 `docs/IMPLEMENTATION_PLAN.md`。

## 页面（10）
- Home（`home`）
- Menu（`menu`）
- Today’s bakes（`bakes`）
- Order ahead（`order`）
- Catering（`catering`）
- Our story（`story`）
- Find us（`visit`）
- FAQ（`faq`）
- Privacy policy（`privacy`）
- 404 error（`404`）
