# Stacking cards（scroll-stack-cards）

- 名称：Stacking cards / 卡片堆叠
- 分类：scroll（`scroll`）
- 对应词汇：Scroll-linked 滚动连动 / Sticky 固定置顶
- 需要：CSS + JS
- 说明：Scroll-linked: each card sticks near the top and the card beneath slides over it while the covered card shrinks and dims, so the stack builds up like a deck.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`），改变量就能换观感。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。变量放进 Site Settings › Custom CSS 可全站共用。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作。
