# Scene Stack（scroll-scene-stack）

- 名称：Scene Stack / 场景叠换
- 分类：Scroll & Parallax（`scroll`）
- 需要：纯 CSS + 约 30 行 JS（无第三方库）
- 说明：One screen is pinned while you scroll through 4 scenes: the picture of each new scene wipes up over the previous one (and settles from a 1.25x zoom) while the text cross-fades with a small slide. A scene rail lets you jump, and a thin bar shows progress.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 结构：`<section data-ss style="--n:场景数">` > `.ss-stage` > 若干 `<article class="ss-s">`（每个含 `.ss-art` 图 + `.ss-t` 文字）。JS 加 `ss-on` 后，场景变成同一格里的叠层；后面的场景图盖在前面的上面。
- 滚动进度 q = 进度 × 场景数；每个场景的图出现度 `--e`、文字可见度 `--v`、位移 `--y` 由 JS 写入，想改节奏只改 JS 里的 `.6` / `.25`。场景数不限（改 `--n` 即可，JS 自动读 DOM）。
- 底部的圆角数字按钮是场景导航（键盘可用、`aria-current` 标记当前，点击平滑滚到该场景）；顶部细条是总进度。
- 没有 JS / 减少动态：不钉住，4 个场景按普通上下排列，图文并排，内容完整。
- 与 `img-scroll-zoom-pin` 不同：那个是一张图从框放大到满屏；这个是同一屏里连续换 3–4 个场景，且有可点的导航。与 `scroll-sticky-index` 不同：它钉住的是文字目录，图不换。
- 手机：图在上（46svh）、文字在下，导航贴左下。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
