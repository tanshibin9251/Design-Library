# Scroll-driven before / after（scroll-before-after-wipe）

- 名称：Scroll-driven before / after / 滚动驱动前后对比
- 分类：scroll（`scroll`）
- 对应词汇：Scroll-linked 滚动连动
- 需要：CSS + JS
- 说明：Scroll-linked: as the section scrolls, a divider sweeps across and the 'after' image is revealed over the 'before'. Scroll back and it rewinds.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`），改变量就能换观感。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。变量放进 Site Settings › Custom CSS 可全站共用。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作。
