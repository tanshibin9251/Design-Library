# Horizontal scroll (pinned)（scroll-horizontal-pin）

- 名称：Horizontal scroll (pinned) / 纵向滚动驱动横向滚动
- 分类：Scroll（`scroll`）
- 对应词汇：Horizontal Scroll 横向滚动
- 需要：CSS + 少量原生 JS，无第三方库
- 说明：The section pins to the screen and a row of cards slides sideways as you keep scrolling down, then releases the page.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`），改变量就能换观感。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。变量放进 Site Settings › Custom CSS 可全站共用。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作。
