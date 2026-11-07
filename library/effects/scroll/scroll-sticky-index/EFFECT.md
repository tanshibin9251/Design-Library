# Sticky section headers（scroll-sticky-index）

- 名称：Sticky section headers / 固定置顶分组列表
- 分类：Scroll（`scroll`）
- 对应词汇：Sticky 固定置顶
- 需要：CSS + 纯 CSS，无 JS
- 说明：An A-Z directory whose letter headers stick to the top while their group scrolls past, then hand over to the next letter. Pure CSS.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`），改变量就能换观感。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。变量放进 Site Settings › Custom CSS 可全站共用。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作。
