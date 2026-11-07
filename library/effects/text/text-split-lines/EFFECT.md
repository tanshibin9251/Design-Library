# Split Lines（text-split-lines）

- 名称：Split Lines / 自动分行滚动升起
- 分类：Text & Typography（`text`）
- 需要：纯 CSS + 约 25 行 JS（无第三方库）
- 说明：Any heading or paragraph is split into its real wrapped lines (measured from the layout, rebuilt on resize); each line rises out of its own mask according to where it sits on screen, so long text reveals at reading pace and reverses when you scroll back.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 给任何块加 `data-sl`（标题、段落、引言都行）。JS 把文字拆成「实际换行后的每一行」，每行外面一层 `overflow:hidden` 的遮罩，里面的字从下方升起。
- 每行进度 `--l` 只由它在屏幕里的位置决定（`vh*.94` 到 `vh*.16` 这一段），不用定时器、不用错开延迟；改这两个数字就能调节奏。
- 换行是量出来的：窗口宽度变化 150ms 后自动重新拆分，字体加载完也会重拆一次。
- 无障碍：原文放在视觉隐藏的 `.sl-sr` 里供读屏和搜索；拆出来的行是 `aria-hidden`。没有 JS 或开启「减少动态」时不拆分，保持普通文字。
- 只支持纯文本（行内的 `<a>`、`<em>` 会被拆成纯文本）。需要行内样式的标题，把样式放在整个块上。
- 与 `heading-split-reveal` 不同：那个是手写好行数、页面加载时按延迟依次播放、点击重播，只适合短标题；这个是自动测量换行、适用于任意段落、由滚动位置驱动并可倒放，没有延迟。与 `scroll-linked-text-fill` 不同：那个是整段文字按词点亮颜色，这个是逐行从遮罩里升起。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
