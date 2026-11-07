# Text Scramble（text-scramble）

- 名称：Text Scramble / 文字解码
- 分类：Text & Typography（`text`）
- 需要：纯 CSS + 约 30 行 JS（无第三方库）
- 说明：Text resolves out of random glyphs from left to right (a decode / hacker-terminal feel). Each letter keeps its exact width while flickering, so lines never jump or re-wrap. Plays when the text enters the screen, on hover or focus of a row, and on a Replay button.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 给任何文字加 `data-sc`。JS 把每个字符包成 `<span class="sc-c">`（词用 `nowrap` 包住），解析前量出每个字的宽度并锁定，所以乱码期间不会抖动、不会换行。
- 时间：总时长 `700 + 字数*16` ms；每个字有随机的开始 / 结束时间；乱码每 55ms 换一次字符，字符集在 JS 的 `G`。乱码字用 `--accent` 色。
- 触发：进入视口（一次）、行 hover / 键盘聚焦、触屏点击、Replay 按钮；列表行的链接在演示里 `href="#"` 被拦截，真实使用时去掉 `data-sc-row` 的拦截逻辑即可正常跳转。
- 无障碍：真实文字放在视觉隐藏的 `.sc-sr` 里（读屏、搜索都读到完整文字），动画出来的字符是 `aria-hidden`。
- 开启「减少动态」/ 没有 JS：保持原文，不拆分。
- 只支持纯文本（行内标签会被拆平）。
- 与 `text-letter-reveal`（字母升起）、`text-typewriter`（逐字打出）不同：这里每个字先是随机字符，再逐个落定为正确字符，且保持宽度不变。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
