# Number Morph（scroll-number-morph）

- 名称：Number Morph / 数字与形状变形
- 分类：Scroll & Parallax（`scroll`）
- 需要：纯 CSS + 约 35 行 JS（无第三方库）
- 说明：A pinned stage where one big number counts up and one shape morphs (circle → rounded square → triangle → star) while its colour blends through the theme colours; every point is driven by scroll position, so it reverses when you scroll back.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 形状是一个 90 点的 `<polygon>`：每个形状用极坐标半径函数 `r(θ)` 表示，两个形状之间对每个点的半径线性插值（点数相同才能变形）。新增形状 = 在 JS 的 `SH` 数组里加一个 `r(θ)` 函数，并补 `VAL / SUF / COL` 一项、把 `--n` 改成 `状态数 - 1`。
- 数字 `VAL`、后缀 `SUF`、文案（`.nm-l`）、颜色 `COL`（直接写主题变量）按状态一一对应；颜色用 `color-mix()` 按 `--k` 在 `--ca` / `--cb` 之间混合。
- 钉住的舞台高度是 `(n+0.6)*100svh`；文案按与当前状态的距离交叉淡入淡出。
- 没有 JS / 减少动态：不钉住，只显示第一个状态（数字 12 + 圆形 + 第一条文案），内容不丢。
- 手机：形状在上、数字文案在下。数字用 `tabular-nums`，计数时不抖。
- 与 `stat-counter-up` 不同：那个进入视口时数字自己数一遍；这个数字和形状都由滚动位置驱动，可倒放，并且形状会变。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
