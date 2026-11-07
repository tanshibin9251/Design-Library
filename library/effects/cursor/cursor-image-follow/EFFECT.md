# Image Follow List（cursor-image-follow）

- 名称：Image Follow List / 列表悬停图片跟随
- 分类：Cursor Effects（`cursor`）
- 需要：纯 CSS + 约 25 行 JS（无第三方库）
- 说明：A list of projects: while the pointer moves across a row, that row's picture floats after the cursor with smooth lag and a slight tilt from its speed, cross-fading as you move between rows while the other rows dim. Touch gets an inline preview instead.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 结构：`<ul class="cf-list">` 里每行一个 `<a class="cf-row" href="项目链接">`；`.cf-float` 里按同样顺序放每行对应的图（`.cf-a`，里面的 `.ap-art` 换成真实 `<img>`）。
- 浮动图用 `position:fixed` + 每帧 lerp（0.16）追光标，倾斜角来自水平速度；`--speed` 影响过渡速度。
- **键盘**：Tab 到某一行时，图会固定出现在该行右侧（不依赖鼠标），离开即隐藏。
- **触屏**（没有悬停）：浮动图不显示，改为点一行在行内展开预览图，再点一次才跳转链接（`href="#"` 的演示里再点则收起）。
- 减少动态：不追随延迟、不倾斜，图直接跟到光标位置。
- 与 `cursor-follower-dot` / `cursor-trail` / `cursor-spotlight` 不同：它们是装饰性的光标图形；这个是把光标变成「内容预览」，图随所悬停的行切换。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
