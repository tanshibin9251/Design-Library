# Material sample picker（card-material-swatches）

- 名称：Material sample picker / 材质样板选择卡
- 分类：cards（`cards`）
- 需要：CSS + JS
- 说明：A grid of CSS-drawn textures (wood grain, weave, stone, metal). Pick up to four and the card counts them, ready for a free-sample request.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`），改变量就能换观感。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。变量放进 Site Settings › Custom CSS 可全站共用。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作。
