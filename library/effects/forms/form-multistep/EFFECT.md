# Multi-step form with validation（form-multistep）

- 名称：Multi-step form with validation / 多步表单（带校验）
- 分类：forms（`forms`）
- 需要：CSS + JS
- 说明：A three-step enquiry form with a numbered stepper, per-step validation, slide transitions, a review screen and a success state. Errors are announced to screen readers.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`），改变量就能换观感。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。变量放进 Site Settings › Custom CSS 可全站共用。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作。
