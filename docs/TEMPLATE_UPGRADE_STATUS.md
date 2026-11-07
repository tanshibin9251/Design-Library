# 82 套模板执行记录

2026-11-07：已按用户授权完成本轮全库升级。这里记录实际落地范围；原评审清单保留为基线，不能将所有建议都视为逐页业务验收完成。

## 实际改动

- 保留 Crumb & Co 已批准的摄影、导航、表单和页脚版本。
- 其余 81 套共用导出交互基础：补齐手机菜单、分组页脚、键盘焦点、跳转正文、减少动态效果、无动作表单验证与反馈。已有专属交互保留；有通用商品结构的模板补数量/选择/示例购物车与一致的结账金额。
- 64 套按行业加入外链摄影；另外 17 套保留图解/排版。40 张新增来源已核验原始宽高，另复用两张已核验的 café 图片；不保存原始照片文件。13 套直接融入既有主视觉，其余加入按用途撰写的摄影区块。库存图都有示意标识与折叠署名。
- Modern SaaS、Restaurant Warm、Oakline、Diamond Shop、Enterprise Blue、Peak Performance、Pocket App 另有专属交互或内容修复，见下表及各 TEMPLATE.md。
- 更新 82 张生成的模板预览缩略图，并修正缩略图哈希对共享基础层和专属交互的依赖。截图缩略图不是下载的原始照片。

## 验证范围

- 全部 1,289 个独立 HTML 页面在 390px 浏览器视口进行了几何检查；Windows 滚动条保留 15px，文档实际宽度 375px。
- 82 套首页另检查 768px 平板与 1440px 桌面；修复了施工进度表、保善堂、喫茶店菜单板、民宿搜索框的实际裁切。
- 专门操作：餐饮选菜/数量/结账、家具规格/缺货/购物车、体育用品数量/运费、SaaS 看板/报告、表单演示反馈、手机菜单与导出页面。
- 几何检查不等于所有业务流程、外链、视觉细节或 WCAG 全项验收；有意横向滚动的容器和翻面卡片背面单独排除。结构化记录见 TEMPLATE_UPGRADE_RESULTS.json。另通过 85 个 JavaScript 片段、2 个 JSON 片段、收藏状态与模板回归检查；公开输出为 980 文件、246 个有效 ZIP。

## 保留的真实素材需求

具名商品细节、员工肖像、真实客户网站截图、房源/项目事实、“改造前后”和菜谱逐步照片保留缺图或原有图解；不会用不相关库存图冒充。现有模板仍是前端示范，账户、预订、邮件、付款、实时库存、医疗或服务承诺需要在具体客户项目接入并核实。摄影故障会显示缺图提示，图片与远程字体需要网络。

## 逐模板记录

| 模板 / slug | 页面 | 本轮视觉 | 专属改动（其余均含基础升级） |
|---|---:|---|---|
| Modern SaaS<br>`modern-saas` | 23 | 保留原插画 / 排版 | CTA、页面名称、产品看板/15 个图解、交互 demo |
| Enterprise Blue<br>`enterprise-blue` | 21 | 保留原插画 / 排版 | 四阶段交付图解、案例 CTA |
| Fine Dining<br>`fine-dining` | 26 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Boutique Rose<br>`boutique-rose` | 24 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Bold Studio<br>`bold-studio` | 24 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Calm Spa<br>`calm-spa` | 25 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Magazine Classic<br>`magazine-classic` | 25 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Restaurant Warm<br>`restaurant-warm` | 25 | 2 个外链来源 | 米饭组合基础费、选菜/数量/购物车/结账、菜品文案 |
| Construction Pro<br>`construction-pro` | 21 | 2 个外链来源 | 手机首屏/进度表裁切 |
| Fitness Energy<br>`fitness-energy` | 24 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Nexus AI<br>`neon-nexus` | 22 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Estate Prime<br>`estate-prime` | 24 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Lens & Light<br>`lens-light` | 23 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Smile Dental<br>`dental-care` | 19 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Sunny's Diner<br>`retro-diner` | 24 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Bright Academy<br>`bright-academy` | 20 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Gilded Ledger<br>`gilded-ledger` | 22 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Clay Beauty Studio<br>`clay-beauty` | 25 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Nordic Interiors<br>`nordic-interiors` | 21 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Pixel Arena<br>`pixel-arena` | 25 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Aurora Cowork<br>`aurora-cowork` | 22 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Quiet Grace Community<br>`quiet-grace` | 20 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Green Acre Farm<br>`green-acre` | 26 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Swiftline Logistics<br>`swiftline` | 23 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Happy Paws<br>`happy-paws` | 25 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| FixIt Home Services<br>`fixit-home` | 25 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Civic Hall<br>`civic-hall` | 21 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Hope Foundation<br>`hope-foundation` | 18 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Evergreen Weddings<br>`evergreen-weddings` | 23 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Wanderlust<br>`wanderlust-travel` | 23 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Autoline Motors<br>`autoline-motors` | 24 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Lexington & Co<br>`lexington-law` | 19 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Pulse Records<br>`pulse-records` | 24 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Oakline Furniture<br>`oakline-furniture` | 13 | 2 个外链来源 | 木材/尺寸/示例价格/缺货/询价与购物车联动 |
| Loft Industrial<br>`loft-industrial` | 13 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Curve Modern<br>`curve-modern` | 13 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Heirloom Classic<br>`heirloom-classic` | 13 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Sprint Gear<br>`sprint-gear` | 12 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Trailhead Outdoor<br>`trailhead-outdoor` | 13 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Peak Performance<br>`peak-performance` | 13 | 保留原插画 / 排版 | 产品标签/键盘操作、示例购物车 |
| Renovo Studio<br>`renovo-studio` | 12 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Blueprint Build<br>`blueprint-build` | 12 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Casa Makeover<br>`casa-makeover` | 11 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Thai Touch<br>`thai-touch` | 12 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Reflex Point<br>`reflex-point` | 11 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Tuina Heritage<br>`tuina-heritage` | 12 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Crumb & Co<br>`cafe-bakery` | 10 | 保留已批准示范 | 原示范保持 |
| Maison Verde<br>`salon-studio` | 11 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| BrightPath Tuition<br>`tuition-centre` | 11 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Torque Garage<br>`auto-workshop` | 10 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Rumah Singgah<br>`homestay-stays` | 10 | 2 个外链来源 | 手机搜索表单尺寸 |
| Aria Lim Portfolio<br>`folio-portfolio` | 7 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Verde & Co. Accountants<br>`accounting-firm` | 11 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Baoshan Herbal Clinic<br>`herbal-clinic` | 10 | 1 个外链来源 | 手机首屏/药柜裁切 |
| Frame & Vow<br>`wedding-photo` | 9 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Nexus Summit<br>`expo-summit` | 10 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Sparkle Nest<br>`cleaning-service` | 11 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Pawsh Pet Boutique<br>`pet-boutique` | 10 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Pocket App Landing<br>`app-landing` | 8 | 保留原插画 / 排版 | 应用商店演示反馈 |
| Court Line<br>`court-line` | 9 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Aizome Goods<br>`aizome-goods` | 13 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Tsukimi Ryokan<br>`tsukimi-ryokan` | 13 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Diamond Shop<br>`diamond-shop` | 15 | 1 个外链来源 | 数量按钮、运费总额、结账表单反馈 |
| Kissa Maruyo<br>`kissa-showa` | 11 | 1 个外链来源 | 手机菜单板尺寸与虹吸咖啡主图 |
| Ippon Dojo<br>`ippon-dojo` | 12 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Hanabi Matsuri<br>`hanabi-matsuri` | 11 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Commit Camp<br>`commit-camp` | 11 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Plainspeak English<br>`plainspeak-english` | 11 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Nihongo Path<br>`nihongo-path` | 11 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Fermata Piano<br>`fermata-piano` | 10 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Atelier Wall<br>`atelier-wall` | 10 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Pass Lab<br>`pass-lab` | 10 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Wok & Steam<br>`wok-and-steam` | 10 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Washoku Note<br>`washoku-note` | 10 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Sugar & Crumb<br>`sugar-and-crumb` | 10 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Daily Table<br>`daily-table` | 10 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Knack Index<br>`knack-index` | 9 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Mind Notes<br>`mind-notes` | 10 | 1 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Petal Desk<br>`petal-desk` | 9 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
| Job Atlas<br>`job-atlas` | 10 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Blue Hour<br>`blue-hour` | 9 | 2 个外链来源 | 共用导航 / 页脚 / 演示基础 |
| Grow Notic<br>`grownotic` | 11 | 保留原插画 / 排版 | 共用导航 / 页脚 / 演示基础 |
