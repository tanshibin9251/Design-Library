# Clip Reveal（img-clip-reveal）

- 名称：Clip Reveal / 遮罩展开图片
- 分类：Images & Gallery（`images`）
- 需要：纯 CSS + 约 15 行 JS（无第三方库）
- 说明：Picture is uncovered by a circle, diamond, blinds or arch mask that follows the scroll position (scroll-linked, reverses when you scroll back), while the image settles back from a 1.35x zoom.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 一个 `<figure class="cr-fig cr-circle|cr-diamond|cr-blinds|cr-arch" data-cr>` 就是一张；里面的 `.ap-art` 换成真实 `<img>`（`object-fit:cover`，加 `position:absolute;inset:0;width:100%;height:100%`）即可。
- 进度由 JS 写到 `--p`（0–1）；形状全部是 CSS 里的 `clip-path` / `mask`，想加新形状只要写一条用 `var(--p)` 的规则。
- 没有 JS 时 `--p` 默认 1，图片直接完整显示（不会空白）。减少动态时同样直接显示，不缩放。
- 触屏没有悬停依赖，滚动驱动，手机上同样有效；窄屏改为单列、1:1。
- 与 `scroll-before-after-wipe` 不同：那个是拖动对比两张图；这个是单张图被形状遮罩揭开，且有 4 种形状。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
