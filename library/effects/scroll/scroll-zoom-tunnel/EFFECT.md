# Zoom Tunnel（scroll-zoom-tunnel）

- 名称：Zoom Tunnel / 放大隧道
- 分类：Scroll & Parallax（`scroll`）
- 需要：纯 CSS + 约 15 行 JS（无第三方库）
- 说明：A pinned stage of framed pictures at different depths: scrolling flies you forward, the nearest frame swells past the edges and fades while the next one grows out of the distance, like moving through a tunnel of pictures.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 每个 `.zt-f` 都固定在舞台中心，只靠 `scale` 表示深度：`scale = K^(q - i)`（`K=2.1`，`q` 是 0 到 帧数-1 的滚动进度）。远处的帧小而淡，经过后放大到 3.4 倍并淡出；最后一帧不淡出，停在原尺寸。z-index 近的在上。
- 帧数不限：增减 `<figure class="zt-f">`，把 `--n` 改成 `帧数 - 1`；`.ap-art` 换成真实 `<img>` 即可。
- 淡出后设 `visibility:hidden`，不会挡住下方内容或被读屏重复读取；标题 `.zt-title` 在开头淡出。
- 没有 JS / 减少动态：不钉住，帧按普通卡片竖排。
- 手机：帧改 4:5 竖图。
- 与 `img-scroll-zoom-pin`（一张图放大到满屏）不同：这里是一串帧，前一帧飞过、下一帧从远处长出来，连续的纵深移动。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
