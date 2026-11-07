# Scroll Zoom Pin（img-scroll-zoom-pin）

- 名称：Scroll Zoom Pin / 滚动放大钉住
- 分类：Images & Gallery（`images`）
- 需要：纯 CSS + 约 15 行 JS（无第三方库）
- 说明：A small framed picture is pinned while you scroll: the frame grows to fill the screen, the picture scales up from half size with it, a headline fades up over it, then a card rises in with the next idea.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 结构：`<section data-zp>`（滚动轨道，JS 把它撑到 320svh）里放一个 `position:sticky` 的 `.zp-stage`；`.zp-pic` 是会放大的图，`.zp-over` 是图上的标题，`.zp-card` 是后升起的下一幕。
- 进度写入 3 个变量：`--z`（框放大 0→1）、`--o`（标题出现）、`--c`（卡片升起）；想改节奏只改 JS 里 3 行区间。
- 把 `.ap-art` 换成真实 `<img>`（`object-fit:cover`，铺满）；标题下有渐变遮罩保证文字对比度。
- 没有 JS / 减少动态：不钉住，直接显示最终画面（整图 + 标题 + 卡片），内容一个都不少，也没有强制滚动劫持——只是页面里多了一段 3 屏高的滚动区，用户随时可以直接往下滚走。
- 与 `scroll-sticky-index`、`scroll-stack-cards` 不同：它们钉住文字或叠卡片；这个钉住一张图并让图本身从框放大到全屏，再从图里升起下一幕。
- 手机上框更方（22% 内缩），卡片贴底全宽，标题上移避开卡片。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
