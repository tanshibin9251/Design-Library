# Grow Notic（成长轨道 / Orbit）

为 grownotic.com 定制：品牌 logo 的「开口圆环 + 向右上的箭头」是整套模板的图形语言。近黑与暖白的深浅区块交替，只有一个橙色（#F96405），宽字距大写小标签呼应 logo 字标。

- **字体**：标题 Montserrat（600，正常大小写）· 正文 DM Sans · 小标签 Montserrat 600 大写、字距 .3em
- **色**：primary #141310（近黑，也是深色区块底色）· accent #F96405 · surface #F6F5F2 · secondary #C2410C（只用于浅底上的橙色小字，对比度 ≥ 4.5）
- **授权**：库内自有（圆环 + 箭头是按品牌 logo 重画的 SVG，用 `<symbol id="gn-mark">`，ring 跟随 `currentColor`）

## 页面（11）
Home · Services · About · Contact · Portfolio · Case study · Blog · Single post · Learning · Privacy & Cookies · 404

## 构图特征（这套的灵魂）
1. **圆环 + 箭头是唯一的图形元素**：首屏右侧一个超大的 logo 圆环只露一半，橙色箭头从环里穿出（入场 1.4s 往右上滑入）；其余区块只用细圆环线（`gn-ring`）当背景纹理，不加别的装饰。
2. **深浅交替**：Hero 深 → 工具跑马灯深 → 服务浅 → 作品深 → 流程浅（淡灰）→ 为什么深 → 博客/学习浅 → FAQ 淡灰 → Footer 深。相邻区块不同色。
3. **每页主结构不同**：首页 = 不对称 bento；Services = 五个整屏左右镜像（巨大的描边数字 + Included / Not included 双栏）；Portfolio = 一大二小交错；Blog = 杂志头条 + 侧栏 + 大小不一的卡片；Learning = 三张大卡纵向交替；About = 拱形照片位 + 三条习惯。
4. **流程 = 一条往右上的橙色轨道线**，四个圆形节点，终点是 ↗。
5. **Footer 就是 CTA**：超大一句话 + 超大 WhatsApp 链接，右上角一个大圆环。
6. **按钮全是胶囊**，橙底配近黑字（白字在橙底只有约 3:1，不达标），hover 时箭头 ↗ 往右上走 4px。

## 不要
- 不要把圆环画满整屏或压住文字；标题永远在最上层。
- 不要第二个彩色（没有蓝、紫、渐变紫）；橙色不铺满整个区块。
- 不要把浅灰 GROW 字标放在白底上；浅色区块里不放这个 logo（Header 和 Footer 都是深色）。
- 不要所有区块同一种卡片（等宽三张）；不要全大写的标题（只有小标签用大写宽字距）。
- 不要把文字放进图片（要给中文翻译预留）；中文标题不用斜体、不用大写。
- 不要价格、不要编造数字；缺的写 `[待你填]` / `缺图`。

## 动效（都可关）
- 全部纯 CSS：入场箭头、↓ 提示上下浮动、工具跑马灯、滚动渐入（`animation-timeline: view()`，不支持的浏览器直接显示）、文章页顶部阅读进度条（`animation-timeline: scroll()`）。`prefers-reduced-motion` 下全部停止。

## 手机端
390px 下圆环缩成背景淡影（opacity .28），流程变单列，bento 单列，触摸目标 ≥ 44px。

## 用法
- 这是为一个具体品牌定制的模板：颜色字体可通过导出参数换，但构图围绕 logo 的圆环和箭头，换别的品牌时需要换掉 `#gn-mark`。
- 文案取自 grownotic 项目的视觉稿（`PROJECTS/GROWNOTIC/INHOUSE/grownotic/demo/`），带 `[待你填]` 的都是还没确认的事实。
