# Pointer Fill Button（button-pointer-fill）

- 名称：Pointer Fill Button / 指针位置填充按钮
- 分类：Buttons（`buttons`）
- 需要：纯 CSS + 约 20 行 JS（无第三方库）
- 说明：The button's fill is a circle that grows from the exact point where the pointer enters, covering the whole button, and shrinks back towards the point where the pointer leaves. Label colour switches in sync, and the button leans slightly towards the pointer.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 填充是 `::before` 的圆：圆心 `--x/--y`、半径 `--r`（取入口到最远角的距离，保证一定盖满）由 JS 在进入 / 离开瞬间写入；`--s` 从 0 到 1 做放大 / 收缩。换色只改 `--c`（填充色）和 `--oc`（填充后的文字色）。
- 轻微磁吸：`pointermove` 把按钮向指针偏移 `12% / 20%`。
- **键盘**：`:focus-visible` 时从中心填充，失焦收回；**触屏**：按下时从触点填充，650ms 后收回（没有悬停依赖）。
- 开启「减少动态」：没有过渡、没有磁吸，状态瞬间切换。
- 与 `button-slide-fill`（固定方向滑入）、`button-magnetic`（只有磁吸偏移）不同：填充的起点和终点就是指针进出的位置，方向由用户决定。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
