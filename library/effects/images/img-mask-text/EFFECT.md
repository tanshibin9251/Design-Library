# Mask Text（img-mask-text）

- 名称：Mask Text / 文字镂空图片
- 分类：Images & Gallery（`images`）
- 需要：纯 CSS（`background-clip:text`）+ 约 10 行 JS
- 说明：Huge headline letters act as windows onto a picture that is larger than the words and moves with scroll: a sunset landscape slides up through GOLDEN while a conic colour wheel rotates through HOUR.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 图片用 CSS 渐变画出来（太阳圆盘 + 地平线分层 + 圆锥色轮），颜色全来自主题变量；`--mp`（0–1）由 JS 根据元素在视口里的位置写入，驱动 `background-position` 和 `conic-gradient(from …)`。
- 换真实照片：`.mt-a { background-image:url(photo.jpg); background-size:cover … }`，`background-size` 保持比实际文字大（如 `100% 220%`），滚动时才会看到图片在字里移动。
- 字要够大、够粗（`font-weight:800` 以上）才看得出里面的图；字号由 `clamp(3.6em,18vw,11.5em)` 控制，手机上也保持整行可读。
- 不支持 `background-clip:text` 的浏览器回退为 `--primary` 纯色字。没有 JS / 减少动态：`--mp` 固定在 .5，图片不动，字依然是图片填充。
- 文字是真实文本（可选、可被读屏、可被搜索），不是图片。
- 与 `heading-outline-text`（描边字）、`text-gradient-shimmer`（渐变闪光）不同：这里是图片填充，且图片在字里随滚动移动。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
