# Floating WhatsApp chat（float-whatsapp-cta）

- 名称：Floating WhatsApp chat / 浮动 WhatsApp 咨询
- 分类：widgets（`widgets`）
- 需要：CSS + JS
- 说明：A corner chat button that opens a mini card with an online/offline status from your opening hours and one-tap quick questions that open WhatsApp with the text pre-filled.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`），改变量就能换观感。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。变量放进 Site Settings › Custom CSS 可全站共用。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作。
