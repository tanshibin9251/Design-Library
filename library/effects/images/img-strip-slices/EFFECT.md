# Strip Slices（img-strip-slices）

- 名称：Strip Slices / 条带拼合
- 分类：Images & Gallery（`images`）
- 需要：纯 CSS + 约 20 行 JS（无第三方库）
- 说明：The picture is cut into eight vertical strips. Scrolling it into view makes odd strips rise from below and even strips drop from above, staggered one after another, until the image is whole (scroll-linked, so it reverses).
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- JS 把 `.ap-art` 里的内容复制成 8 条（每条是一个 `overflow:hidden` 的竖条，里面放整图并向左偏移 `-i*100%`）；原图隐藏。条数改 JS 里的 `N`，同时把 CSS 里的 `/8` 一起改。
- 进度 `--p` 来自图片在视口中的位置；每条自己的进度 `--t = clamp(0, --p*1.8 - --i*.1, 1)`，所以按顺序错开；偶数条反方向。
- 没有 JS / 减少动态：直接显示整图。真实照片：把 `.ap-art` 里的 `<svg>` 换成 `<img>`（`object-fit:cover`；JS 复制的是它的内容，`.sp-in img` 需要和 `.sp-in svg` 同样规则）。
- 与 `img-clip-reveal` 不同：那个用一个形状遮罩把图揭开；这个把图切成条，每条各自位移并依次到位。与 `shutter` 转场不同：那是页面转场，这是单张图在滚动中拼合。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
