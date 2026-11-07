# 全部 Website 模板优化候选清单

状态：用户已于 2026-11-07 授权按本清单执行。下表保留原始评审基线；实际改动与验证范围见 [执行记录](TEMPLATE_UPGRADE_STATUS.md)。Crumb & Co 原示范保留。

本清单完整覆盖 82 套模板。按元数据、全部页面源码与既有抽查整理；不是对每套模板逐页进行过浏览器测试。

## 如何判断

- 图片数量只统计 HTML 的 img 引用；SVG、CSS 插画和背景图不等于缺图。不能用“0 张 img”直接判定设计不好。
- 占位数量指 class=ph 的块；表单数量和 return false 仅是静态线索，不代表全部没有 JS，也不证明已接真实后台。
- 摄影类补 Google 找到且核验来源的高清外链图片，按 Crumb & Co 的方式处理裁切、加载、署名和失效回退；不下载照片原文件。
- 数字/图解类保留自己的视觉语言，优先产品截图、示意图和交互完善；不强行插入风景或人物照片。
- 所有待升级模板都应检查主 CTA、移动导航、空/成功/错误状态、页脚布局和导出；这些是验收要求，不是已证实全部有 bug。

## 建议分批

### 已完成示范（1 套）

| 模板 / slug | 页数 | 图片 / 占位 / 表单 | 建议 |
|---|---:|---|---|
| [Crumb & Co · 面包咖啡馆](https://designlibrary.grownotic.com/#/template/cafe-bakery)<br>`cafe-bakery` | 10 | 20 / 1 / 1 | 已批准的高清外链摄影 + 手机导航/表单演示 + 三栏页脚；不重复安排升级 |

### 优先摄影与布局升级（41 套）

| 模板 / slug | 页数 | 图片 / 占位 / 表单 | 建议 |
|---|---:|---|---|
| [Aizome Goods · 藍染](https://designlibrary.grownotic.com/#/template/aizome-goods)<br>`aizome-goods` | 13 | 0 / 0 / 1 | 系列与商品图、材质细节；尺码/颜色/购物车演示保持一致；空间大图、项目案例、材质细节和改造前后；页脚分组对齐 |
| [Blue Hour · 蓝调时刻](https://designlibrary.grownotic.com/#/template/blue-hour)<br>`blue-hour` | 9 | 0 / 0 / 1 | 目的地/房型/设施摄影、行程或入住流程；说明示意与实时数据边界；成套作品、项目封面与画廊；保留一致色调、裁切和作品顺序 |
| [Boutique Rose · 精品玫瑰](https://designlibrary.grownotic.com/#/template/boutique-rose)<br>`boutique-rose` | 24 | 0 / 68 / 2 | 系列与商品图、材质细节；尺码/颜色/购物车演示保持一致 |
| [Calm Spa · 宁静水疗](https://designlibrary.grownotic.com/#/template/calm-spa)<br>`calm-spa` | 25 | 0 / 80 / 3 | 服务场景和空间摄影；预约/计划选择与手机菜单完善 |
| [Casa Makeover · 居家焕新](https://designlibrary.grownotic.com/#/template/casa-makeover)<br>`casa-makeover` | 11 | 0 / 22 / 1 | 服务/项目过程示意图；报价、服务区域与请求反馈；空间大图、项目案例、材质细节和改造前后；页脚分组对齐；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Clay Beauty Studio · 黏土美学](https://designlibrary.grownotic.com/#/template/clay-beauty)<br>`clay-beauty` | 25 | 0 / 74 / 2 | 空间/服务/产品摄影；真实案例须有来源，不冒充库存图为成果；系列与商品图、材质细节；尺码/颜色/购物车演示保持一致 |
| [Curve Modern · 圆润现代](https://designlibrary.grownotic.com/#/template/curve-modern)<br>`curve-modern` | 13 | 0 / 26 / 2 | 家具主图、材质/尺寸细节、场景图；补选项/价格/缺货演示 |
| [Daily Table · 家常餐桌](https://designlibrary.grownotic.com/#/template/daily-table)<br>`daily-table` | 10 | 0 / 11 / 0 | 菜谱成品、食材与分步图片；不把随机菜品当同一道菜 |
| [Smile Dental · 微笑牙科](https://designlibrary.grownotic.com/#/template/dental-care)<br>`dental-care` | 19 | 0 / 42 / 2 | 诊所/服务场景示意图；预约、验证与请求反馈，不宣称已预约；服务场景和空间摄影；预约/计划选择与手机菜单完善 |
| [Estate Prime · 豪宅地产](https://designlibrary.grownotic.com/#/template/estate-prime)<br>`estate-prime` | 24 | 0 / 68 / 3 | 房源封面、室内/户型视觉；筛选、零结果、收藏和询盘演示 |
| [Evergreen Weddings · 常青婚礼](https://designlibrary.grownotic.com/#/template/evergreen-weddings)<br>`evergreen-weddings` | 23 | 0 / 60 / 3 | 活动/婚礼视觉、场地与项目封面；时间、票务与预约状态清楚；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Nexus Summit · 亚洲产品设计峰会](https://designlibrary.grownotic.com/#/template/expo-summit)<br>`expo-summit` | 10 | 0 / 21 / 1 | 活动/婚礼视觉、场地与项目封面；时间、票务与预约状态清楚；文章/内容封面与栏目层级；搜索、空结果、阅读及页脚；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Fine Dining · 高端餐饮](https://designlibrary.grownotic.com/#/template/fine-dining)<br>`fine-dining` | 26 | 0 / 73 / 4 | 首屏餐饮摄影、菜品特色图、制作过程和空间图；商品与图像必须对应 |
| [Aria Lim Portfolio · 设计师作品集](https://designlibrary.grownotic.com/#/template/folio-portfolio)<br>`folio-portfolio` | 7 | 0 / 15 / 1 | 案例主视觉与交付细节；服务/案例/询价流程及页脚；成套作品、项目封面与画廊；保留一致色调、裁切和作品顺序 |
| [Green Acre Farm · 绿野农场](https://designlibrary.grownotic.com/#/template/green-acre)<br>`green-acre` | 26 | 0 / 68 / 3 | 农场、时令食材和产品图；购物与订阅演示 |
| [Hanabi Matsuri · 花火祭](https://designlibrary.grownotic.com/#/template/hanabi-matsuri)<br>`hanabi-matsuri` | 11 | 0 / 0 / 1 | 活动/婚礼视觉、场地与项目封面；时间、票务与预约状态清楚 |
| [Happy Paws · 欢乐爪爪](https://designlibrary.grownotic.com/#/template/happy-paws)<br>`happy-paws` | 25 | 0 / 70 / 3 | 动物/空间/商品摄影；服务或商品选项与请求反馈 |
| [Heirloom Classic · 传世古典](https://designlibrary.grownotic.com/#/template/heirloom-classic)<br>`heirloom-classic` | 13 | 0 / 18 / 1 | 家具主图、材质/尺寸细节、场景图；补选项/价格/缺货演示；空间大图、项目案例、材质细节和改造前后；页脚分组对齐 |
| [Baoshan Herbal Clinic · 保善堂中医诊所](https://designlibrary.grownotic.com/#/template/herbal-clinic)<br>`herbal-clinic` | 10 | 0 / 5 / 1 | 诊所/服务场景示意图；预约、验证与请求反馈，不宣称已预约；服务场景和空间摄影；预约/计划选择与手机菜单完善；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Rumah Singgah · 归栖民宿](https://designlibrary.grownotic.com/#/template/homestay-stays)<br>`homestay-stays` | 10 | 0 / 18 / 2 | 目的地/房型/设施摄影、行程或入住流程；说明示意与实时数据边界；房源封面、室内/户型视觉；筛选、零结果、收藏和询盘演示；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Kissa Maruyo · 喫茶まるよ](https://designlibrary.grownotic.com/#/template/kissa-showa)<br>`kissa-showa` | 11 | 0 / 0 / 0 | 首屏餐饮摄影、菜品特色图、制作过程和空间图；商品与图像必须对应 |
| [Lens & Light · 镜头与光](https://designlibrary.grownotic.com/#/template/lens-light)<br>`lens-light` | 23 | 0 / 60 / 3 | 成套作品、项目封面与画廊；保留一致色调、裁切和作品顺序 |
| [Loft Industrial · 工业阁楼](https://designlibrary.grownotic.com/#/template/loft-industrial)<br>`loft-industrial` | 13 | 0 / 31 / 2 | 家具主图、材质/尺寸细节、场景图；补选项/价格/缺货演示；空间大图、项目案例、材质细节和改造前后；页脚分组对齐 |
| [Mind Notes · 心理学科普](https://designlibrary.grownotic.com/#/template/mind-notes)<br>`mind-notes` | 10 | 0 / 0 / 1 | 保留平静排版与图解；可选自然背景，检查动效降级及阅读体验；服务场景和空间摄影；预约/计划选择与手机菜单完善 |
| [Nordic Interiors · 北欧室内](https://designlibrary.grownotic.com/#/template/nordic-interiors)<br>`nordic-interiors` | 21 | 0 / 52 / 2 | 空间大图、项目案例、材质细节和改造前后；页脚分组对齐 |
| [Oakline Furniture · 橡木线家具](https://designlibrary.grownotic.com/#/template/oakline-furniture)<br>`oakline-furniture` | 13 | 0 / 30 / 2 | 家具主图、材质/尺寸细节、场景图；补选项/价格/缺货演示；空间大图、项目案例、材质细节和改造前后；页脚分组对齐 |
| [Pawsh Pet Boutique · 宠物精品店](https://designlibrary.grownotic.com/#/template/pet-boutique)<br>`pet-boutique` | 10 | 0 / 23 / 1 | 动物/空间/商品摄影；服务或商品选项与请求反馈；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Reflex Point · 足点](https://designlibrary.grownotic.com/#/template/reflex-point)<br>`reflex-point` | 11 | 0 / 2 / 1 | 空间、服务与技法示意摄影；预约选择和演示反馈；服务场景和空间摄影；预约/计划选择与手机菜单完善；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Renovo Studio · 翻新工作室](https://designlibrary.grownotic.com/#/template/renovo-studio)<br>`renovo-studio` | 12 | 0 / 20 / 1 | 空间大图、项目案例、材质细节和改造前后；页脚分组对齐；项目/工序/团队示意摄影；询价表单、项目详情和页脚完善；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Restaurant Warm · 温暖餐饮](https://designlibrary.grownotic.com/#/template/restaurant-warm)<br>`restaurant-warm` | 25 | 0 / 74 / 4 | 已确认：结账总额与明细不符，存在重复页面名；首屏餐饮摄影、菜品特色图、制作过程和空间图；商品与图像必须对应 |
| [Sunny's Diner · 阳光餐厅](https://designlibrary.grownotic.com/#/template/retro-diner)<br>`retro-diner` | 24 | 0 / 68 / 3 | 首屏餐饮摄影、菜品特色图、制作过程和空间图；商品与图像必须对应 |
| [Maison Verde · 绿荫美发沙龙](https://designlibrary.grownotic.com/#/template/salon-studio)<br>`salon-studio` | 11 | 0 / 25 / 1 | 空间/服务/产品摄影；真实案例须有来源，不冒充库存图为成果；系列与商品图、材质细节；尺码/颜色/购物车演示保持一致；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Sugar & Crumb · 烘焙甜点](https://designlibrary.grownotic.com/#/template/sugar-and-crumb)<br>`sugar-and-crumb` | 10 | 0 / 9 / 0 | 菜谱成品、食材与分步图片；不把随机菜品当同一道菜；首屏餐饮摄影、菜品特色图、制作过程和空间图；商品与图像必须对应 |
| [Thai Touch · 泰式触感](https://designlibrary.grownotic.com/#/template/thai-touch)<br>`thai-touch` | 12 | 0 / 12 / 1 | 空间、服务与技法示意摄影；预约选择和演示反馈；服务场景和空间摄影；预约/计划选择与手机菜单完善；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Trailhead Outdoor · 山径户外](https://designlibrary.grownotic.com/#/template/trailhead-outdoor)<br>`trailhead-outdoor` | 13 | 0 / 35 / 1 | 目的地/房型/设施摄影、行程或入住流程；说明示意与实时数据边界；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Tsukimi Ryokan · 月見荘](https://designlibrary.grownotic.com/#/template/tsukimi-ryokan)<br>`tsukimi-ryokan` | 13 | 0 / 0 / 1 | 目的地/房型/设施摄影、行程或入住流程；说明示意与实时数据边界；服务场景和空间摄影；预约/计划选择与手机菜单完善 |
| [Tuina Heritage · 推拿传承](https://designlibrary.grownotic.com/#/template/tuina-heritage)<br>`tuina-heritage` | 12 | 0 / 4 / 1 | 空间、服务与技法示意摄影；预约选择和演示反馈；服务场景和空间摄影；预约/计划选择与手机菜单完善；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Wanderlust · 漫游旅行](https://designlibrary.grownotic.com/#/template/wanderlust-travel)<br>`wanderlust-travel` | 23 | 0 / 68 / 3 | 目的地/房型/设施摄影、行程或入住流程；说明示意与实时数据边界 |
| [Washoku Note · 和食ノート](https://designlibrary.grownotic.com/#/template/washoku-note)<br>`washoku-note` | 10 | 0 / 12 / 0 | 菜谱成品、食材与分步图片；不把随机菜品当同一道菜；首屏餐饮摄影、菜品特色图、制作过程和空间图；商品与图像必须对应 |
| [Frame & Vow · 婚礼摄影](https://designlibrary.grownotic.com/#/template/wedding-photo)<br>`wedding-photo` | 9 | 0 / 20 / 1 | 活动/婚礼视觉、场地与项目封面；时间、票务与预约状态清楚；成套作品、项目封面与画廊；保留一致色调、裁切和作品顺序；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Wok & Steam · 家常中餐](https://designlibrary.grownotic.com/#/template/wok-and-steam)<br>`wok-and-steam` | 10 | 0 / 0 / 0 | 菜谱成品、食材与分步图片；不把随机菜品当同一道菜；首屏餐饮摄影、菜品特色图、制作过程和空间图；商品与图像必须对应 |

### 按行业补视觉与演示流程（22 套）

| 模板 / slug | 页数 | 图片 / 占位 / 表单 | 建议 |
|---|---:|---|---|
| [Atelier Wall · 美术课程](https://designlibrary.grownotic.com/#/template/atelier-wall)<br>`atelier-wall` | 10 | 0 / 0 / 0 | 作品和课程封面；保留画廊构图，补详情与交互反馈；教学环境/课程封面；课程详情、课表与试课请求演示 |
| [Torque Garage · 扭矩车厂](https://designlibrary.grownotic.com/#/template/auto-workshop)<br>`auto-workshop` | 10 | 0 / 2 / 1 | 车型/车间与服务过程；比较/规格/报价和查询演示；服务/项目过程示意图；报价、服务区域与请求反馈；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Autoline Motors · 汽车行](https://designlibrary.grownotic.com/#/template/autoline-motors)<br>`autoline-motors` | 24 | 0 / 68 / 4 | 车型/车间与服务过程；比较/规格/报价和查询演示 |
| [Blueprint Build · 蓝图营造](https://designlibrary.grownotic.com/#/template/blueprint-build)<br>`blueprint-build` | 12 | 0 / 1 / 1 | 项目/工序/团队示意摄影；询价表单、项目详情和页脚完善；服务/项目过程示意图；报价、服务区域与请求反馈 |
| [Bold Studio · 粗犷工作室](https://designlibrary.grownotic.com/#/template/bold-studio)<br>`bold-studio` | 24 | 0 / 86 / 2 | 案例主视觉与交付细节；服务/案例/询价流程及页脚 |
| [Bright Academy · 明亮学院](https://designlibrary.grownotic.com/#/template/bright-academy)<br>`bright-academy` | 20 | 0 / 48 / 2 | 教学环境/课程封面；课程详情、课表与试课请求演示 |
| [Sparkle Nest · 清洁到家](https://designlibrary.grownotic.com/#/template/cleaning-service)<br>`cleaning-service` | 11 | 0 / 0 / 1 | 服务/项目过程示意图；报价、服务区域与请求反馈；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Construction Pro · 工程建筑](https://designlibrary.grownotic.com/#/template/construction-pro)<br>`construction-pro` | 21 | 0 / 48 / 2 | 项目/工序/团队示意摄影；询价表单、项目详情和页脚完善 |
| [Court Line · 球场线](https://designlibrary.grownotic.com/#/template/court-line)<br>`court-line` | 9 | 0 / 7 / 0 | 按本模板用途补主视觉/特色图、导航和核心演示反馈，不统一换成摄影风格 |
| [Diamond Shop · 菱形商店](https://designlibrary.grownotic.com/#/template/diamond-shop)<br>`diamond-shop` | 15 | 0 / 45 / 0 | 按本模板用途补主视觉/特色图、导航和核心演示反馈，不统一换成摄影风格 |
| [Fermata Piano · 钢琴课程](https://designlibrary.grownotic.com/#/template/fermata-piano)<br>`fermata-piano` | 10 | 0 / 0 / 0 | 作品/演出或教学场景视觉；播放/课程/购物演示与触屏反馈；教学环境/课程封面；课程详情、课表与试课请求演示 |
| [Fitness Energy · 活力健身](https://designlibrary.grownotic.com/#/template/fitness-energy)<br>`fitness-energy` | 24 | 0 / 68 / 3 | 训练空间与课程特色图；课程选择/价格/预约状态完善 |
| [FixIt Home Services · 到家维修](https://designlibrary.grownotic.com/#/template/fixit-home)<br>`fixit-home` | 25 | 0 / 68 / 4 | 服务/项目过程示意图；报价、服务区域与请求反馈；项目/工序/团队示意摄影；询价表单、项目详情和页脚完善 |
| [Hope Foundation · 希望基金会](https://designlibrary.grownotic.com/#/template/hope-foundation)<br>`hope-foundation` | 18 | 0 / 42 / 1 | 项目与活动示意图；明确数据和捐赠按钮的演示边界 |
| [Ippon Dojo · 一本道場](https://designlibrary.grownotic.com/#/template/ippon-dojo)<br>`ippon-dojo` | 12 | 0 / 0 / 1 | 训练空间与课程特色图；课程选择/价格/预约状态完善 |
| [Job Atlas · 职业图鉴](https://designlibrary.grownotic.com/#/template/job-atlas)<br>`job-atlas` | 10 | 0 / 0 / 0 | 教学环境/课程封面；课程详情、课表与试课请求演示；文章/内容封面与栏目层级；搜索、空结果、阅读及页脚 |
| [Knack Index · 生活知识](https://designlibrary.grownotic.com/#/template/knack-index)<br>`knack-index` | 9 | 0 / 0 / 0 | 教学环境/课程封面；课程详情、课表与试课请求演示 |
| [Magazine Classic · 经典杂志](https://designlibrary.grownotic.com/#/template/magazine-classic)<br>`magazine-classic` | 25 | 0 / 89 / 2 | 文章/内容封面与栏目层级；搜索、空结果、阅读及页脚 |
| [Pulse Records · 脉冲唱片](https://designlibrary.grownotic.com/#/template/pulse-records)<br>`pulse-records` | 24 | 0 / 62 / 3 | 作品/演出或教学场景视觉；播放/课程/购物演示与触屏反馈 |
| [Quiet Grace Community · 静恩社区](https://designlibrary.grownotic.com/#/template/quiet-grace)<br>`quiet-grace` | 20 | 0 / 42 / 2 | 社区/活动摄影；日程、信息层级、手机导航和页脚；项目与活动示意图；明确数据和捐赠按钮的演示边界 |
| [Sprint Gear · 冲刺装备](https://designlibrary.grownotic.com/#/template/sprint-gear)<br>`sprint-gear` | 12 | 0 / 32 / 1 | 训练空间与课程特色图；课程选择/价格/预约状态完善；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [BrightPath Tuition · 明途补习中心](https://designlibrary.grownotic.com/#/template/tuition-centre)<br>`tuition-centre` | 11 | 0 / 5 / 1 | 教学环境/课程封面；课程详情、课表与试课请求演示；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |

### 保留插画/排版，完善功能（18 套）

| 模板 / slug | 页数 | 图片 / 占位 / 表单 | 建议 |
|---|---:|---|---|
| [Verde & Co. Accountants · 会计师事务所](https://designlibrary.grownotic.com/#/template/accounting-firm)<br>`accounting-firm` | 11 | 0 / 4 / 1 | 优先数据图表和信息排版；补计算边界与咨询演示，摄影可选；保留文档式排版；可选空间图，完善服务详情、咨询和页脚；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Pocket App Landing · 应用落地页](https://designlibrary.grownotic.com/#/template/app-landing)<br>`app-landing` | 8 | 0 / 0 / 0 | 优先产品界面和功能图；修正 CTA、价格/试用演示，不用风景替代产品；产品界面、技术图解或服务成果视觉；核对功能说明与 CTA；页脚 class 与多栏 CSS 需专项核对（静态线索，非已复现 bug） |
| [Aurora Cowork · 极光共享办公](https://designlibrary.grownotic.com/#/template/aurora-cowork)<br>`aurora-cowork` | 22 | 0 / 48 / 3 | 空间、设施与活动摄影；工位/方案选择与看场地请求；产品界面、技术图解或服务成果视觉；核对功能说明与 CTA |
| [Civic Hall · 市政厅](https://designlibrary.grownotic.com/#/template/civic-hall)<br>`civic-hall` | 21 | 0 / 45 / 3 | 任务/目录与可读性优先；可选社区摄影，补查询和无结果状态 |
| [Commit Camp · 编程训练营](https://designlibrary.grownotic.com/#/template/commit-camp)<br>`commit-camp` | 11 | 0 / 0 / 0 | 保留 IDE/代码界面；课程/练习演示、键盘和手机菜单完善；教学环境/课程封面；课程详情、课表与试课请求演示 |
| [Enterprise Blue · 企业蓝](https://designlibrary.grownotic.com/#/template/enterprise-blue)<br>`enterprise-blue` | 21 | 0 / 60 / 2 | 团队/服务/案例示意视觉；服务详情、询盘与整齐页脚；产品界面、技术图解或服务成果视觉；核对功能说明与 CTA |
| [Gilded Ledger · 金边金融](https://designlibrary.grownotic.com/#/template/gilded-ledger)<br>`gilded-ledger` | 22 | 0 / 52 / 2 | 优先数据图表和信息排版；补计算边界与咨询演示，摄影可选 |
| [Grow Notic · 成长轨道](https://designlibrary.grownotic.com/#/template/grownotic)<br>`grownotic` | 11 | 0 / 0 / 2 | 案例主视觉与交付细节；服务/案例/询价流程及页脚；产品界面、技术图解或服务成果视觉；核对功能说明与 CTA |
| [Lexington & Co · 莱克星顿律所](https://designlibrary.grownotic.com/#/template/lexington-law)<br>`lexington-law` | 19 | 0 / 42 / 2 | 保留文档式排版；可选空间图，完善服务详情、咨询和页脚 |
| [Modern SaaS · 现代 SaaS](https://designlibrary.grownotic.com/#/template/modern-saas)<br>`modern-saas` | 22 | 0 / 59 / 2 | 已确认：试用/视频 CTA 目的不一致，Features 重名；优先产品界面和功能图；修正 CTA、价格/试用演示，不用风景替代产品；产品界面、技术图解或服务成果视觉；核对功能说明与 CTA |
| [Nexus AI · 未来科技](https://designlibrary.grownotic.com/#/template/neon-nexus)<br>`neon-nexus` | 22 | 0 / 48 / 2 | 产品界面、技术图解或服务成果视觉；核对功能说明与 CTA；优先产品界面和功能图；修正 CTA、价格/试用演示，不用风景替代产品 |
| [Nihongo Path · にほんごパス](https://designlibrary.grownotic.com/#/template/nihongo-path)<br>`nihongo-path` | 11 | 0 / 0 / 0 | 保留课程/学习界面；可选学习场景，补分级测试与选课反馈；教学环境/课程封面；课程详情、课表与试课请求演示 |
| [Pass Lab · 考证备考](https://designlibrary.grownotic.com/#/template/pass-lab)<br>`pass-lab` | 10 | 0 / 0 / 0 | 保留仪表/学习计划；补测验、解释与空状态，不必强加背景照片；教学环境/课程封面；课程详情、课表与试课请求演示 |
| [Peak Performance · 巅峰科技](https://designlibrary.grownotic.com/#/template/peak-performance)<br>`peak-performance` | 13 | 0 / 14 / 1 | 产品界面、技术图解或服务成果视觉；核对功能说明与 CTA |
| [Petal Desk · 花瓣项目台](https://designlibrary.grownotic.com/#/template/petal-desk)<br>`petal-desk` | 9 | 0 / 0 / 4 | 案例主视觉与交付细节；服务/案例/询价流程及页脚；优先产品界面和功能图；修正 CTA、价格/试用演示，不用风景替代产品；服务/项目过程示意图；报价、服务区域与请求反馈 |
| [Pixel Arena · 像素竞技场](https://designlibrary.grownotic.com/#/template/pixel-arena)<br>`pixel-arena` | 25 | 0 / 73 / 4 | 保留游戏/插画风格；补活动/设备视觉、手机交互和性能检查 |
| [Plainspeak English · 英语课程](https://designlibrary.grownotic.com/#/template/plainspeak-english)<br>`plainspeak-english` | 11 | 0 / 0 / 0 | 保留课程/学习界面；可选学习场景，补分级测试与选课反馈；教学环境/课程封面；课程详情、课表与试课请求演示 |
| [Swiftline Logistics · 迅捷物流](https://designlibrary.grownotic.com/#/template/swiftline)<br>`swiftline` | 23 | 0 / 52 / 2 | 保留流程/轨迹图；可选运营摄影，明确查询和估算的演示数据 |

## 执行规则

建议先从已确认问题的 Modern SaaS、Restaurant Warm，以及摄影回报明显的家具/空间/餐饮模板选小批执行。每批先核对具体页面，再搜图和改版；不依据本清单自动批量替换。

高清标准、图片使用和全站后续工作见 IMPLEMENTATION_PLAN.md。当前完整数据同时保存在 TEMPLATE_IMPROVEMENT_INVENTORY.json；可按 slug 选择要执行的条目。
