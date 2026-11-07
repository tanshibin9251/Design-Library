# Scroll snap sections（scroll-snap-sections）

- 名称：Scroll snap sections / 滚动吸附分屏
- 分类：Scroll（`scroll`）
- 对应词汇：Scroll Snap 滚动吸附
- 需要：CSS + 少量原生 JS，无第三方库
- 说明：Full-height panels that lock into place one at a time as you scroll, with side dots that show and jump between them.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`），改变量就能换观感。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。变量放进 Site Settings › Custom CSS 可全站共用。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作。
