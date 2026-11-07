# Path Draw（scroll-path-draw）

- 名称：Path Draw / 滚动画线
- 分类：Scroll & Parallax（`scroll`）
- 需要：纯 CSS + SVG + 约 30 行 JS（无第三方库）
- 说明：An SVG line is drawn as you scroll, curving through numbered stops placed alternately left and right; each stop and its text light up when the line reaches it. Positions are measured from the real layout, so it works with any content length.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 路径由 JS 按每个 `.pd-dot` 的真实位置生成（竖直切线的三次贝塞尔曲线），所以文案多长、窗口多宽都对得上；窗口变化 100ms 后、字体加载完后会重新生成。
- 画线进度：线头位置 = 视口 62% 高度处；用路径采样表按 y 反查长度，设 `stroke-dashoffset`。
- 站点数量不限：增减 `<article class="pd-i">`；奇数站点在左、文字在点的外侧（左边）；偶数站点在右、文字在右边；这样弯曲的线不会穿过文字（手机统一为左线右文）。
- 没有 JS / 减少动态：整条线直接画满、所有站点都点亮，文字完全可读。
- 与 `scroll-sticky-index`、`timeline-*` 不同：这个是一条随滚动长出来的曲线，按真实布局生成。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
