# Velocity Skew（scroll-velocity-skew）

- 名称：Velocity Skew / 滚动速度倾斜
- 分类：Scroll & Parallax（`scroll`）
- 需要：纯 CSS + 约 12 行 JS（无第三方库）
- 说明：Scroll speed (not position) drives a skew on a stack of cards: the faster you scroll, the more they tilt and stretch, and a spring settles them upright when you stop. Pictures inside move the opposite way for depth.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- JS 只算「速度」：每帧取滚动位移，平滑后乘 `-0.14` 得到目标倾斜角（上限 ±9°），再用弹性追随写入 `--sk`；CSS 里 `skewY(var(--sk)deg)`，并用 `sk²` 做一点纵向拉伸。想更猛改 `-.14` 和 `9`；想更软改 `.14` 的追随系数。
- 图片内部反向位移 `translateY(sk*-3px)` 并放大 1.1，避免倾斜时露出边。
- 只在有速度时才跑 `requestAnimationFrame`，静止时不耗电。
- 没有 JS / 减少动态：保持平直，内容完全正常。倾斜有最大 9°，不影响阅读；建议只用于图片卡片列表，不要用在大段正文上。
- 与 `scroll-parallax-layers`（位置驱动的分层位移）不同：这个由速度驱动，停下就回正。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
