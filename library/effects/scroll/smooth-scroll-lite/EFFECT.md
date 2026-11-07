# Smooth Scroll Lite（smooth-scroll-lite）

- 名称：Smooth Scroll Lite / 平滑滚动（轻量）
- 分类：Scroll & Parallax（`scroll`）
- 需要：约 25 行 JS（无第三方库）
- 说明：Inertia scrolling for a real mouse wheel: each wheel notch moves a target and the page eases toward it (11% per frame). Everything else (keyboard, scrollbar drag, anchor links, touch, trackpads, scrollable inner boxes) stays completely native.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 只拦截「鼠标滚轮」：`deltaMode` 为行 / 页，或像素值是 ≥40 的整数；小数或很小的 delta 视为触控板（自带惯性），不拦截。按 Ctrl（缩放）、横向滚动、内部可滚动元素（`overflow:auto`）都不拦截。
- 追随系数 `.11` 控制手感（越小越飘）；每个滚轮刻度的距离就是原生 `deltaY`，没有额外放大。
- 键盘、滚动条拖动、锚点跳转：`scroll` 事件发现实际位置与目标差 > 2px 就立刻放弃动画并同步，不会跟用户抢。
- 页面里放一个明显的开关（`aria-pressed`），让用户随时关；开启「减少动态」的用户默认关闭。**这类效果会改变滚动手感，请只在营销 / 作品展示页使用，不要用在表单、文档、后台类页面。**
- 与 `scroll-snap-sections` 不同：那个让滚动停在整屏上；这个只改变滚轮的惯性，不改变停靠位置。
- 演示里的 `.sm-bar` 是为了放开关和进度条；真实站点只需复制 JS，并自己放一个开关。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
