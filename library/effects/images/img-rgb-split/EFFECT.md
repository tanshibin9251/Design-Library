# RGB Split（img-rgb-split）

- 名称：RGB Split / 三色错位
- 分类：Images & Gallery（`images`）
- 需要：纯 CSS（SVG 滤镜 + 混合模式）+ 约 20 行 JS
- 说明：Each picture is three colour-channel layers (red, green, blue) blended with screen. At rest they line up exactly; scroll speed pushes red and blue apart vertically, and pointer sweep pushes them apart horizontally, then they spring back.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- JS 把每张图的内容复制成 R / G / B 三层，分别套 `feColorMatrix` 滤镜只留一个通道，用 `mix-blend-mode:screen` 叠回原色（静止时与原图完全一致）。
- `--vy`（滚动速度，上限 ±26px）和 `--vx`（指针横扫速度，上限 ±22px）分别推动红层和蓝层反向位移；改 JS 里的 `26` / `22` 调强度。
- 滤镜定义在 `.rs-defs` 里（`#rs-fr / #rs-fg / #rs-fb`），整页只需要放一份。
- 真实照片：把每个 `.rs-base` 里的 `<svg>` 换成 `<img>` 即可（JS 复制的是 base 的内容，`<img>` 同样能被滤镜处理）；CSS 里 `.rs-l svg` 选择器再加上 `.rs-l img` 同样规则。
- 没有 JS / 减少动态：保持原图，不拆通道。触屏：滚动速度同样触发，指针横扫只对鼠标。
- 与 `img-liquid-distort` 不同：那个用 WebGL 对像素做位移扭曲；这个不移动像素，只把三个颜色通道错开，由滚动速度驱动，纯 CSS 实现，也不耗 GPU 上下文。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
