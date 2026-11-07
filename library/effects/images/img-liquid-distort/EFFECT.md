# Liquid Distort（img-liquid-distort）

- 名称：Liquid Distort / 液体扭曲
- 分类：Images & Gallery（`images`）
- 需要：WebGL（浏览器自带）+ 约 60 行 JS，无第三方库
- 说明：A WebGL shader ripples the picture away from the pointer (radial push + travelling wave + a faint red/blue split at the wave front). The strength follows pointer speed and decays to flat when you stop; tap or press gives a burst on touch.
- 授权：自写，无第三方代码，可用于任何客户站

## 怎么用
- **Web（HTML / PHP）**：把 `snippet.html` 整段贴进页面。颜色、字体、圆角、字号、速度全部来自文件顶部 `:root` 的 CSS 变量（`--primary --secondary --text --accent --surface --border --font-heading --font-body --radius --scale --speed`）。
- **Elementor**：贴进 **HTML widget**（或 WPCode）。
- 一个 `<div class="ld" data-ld>` 里放 `<img>`（推荐，同源）或内联 `<svg>`；JS 把它当纹理，上面盖一个 `<canvas>`。成功后 canvas 淡入，原图保留在下面作回退。
- 内联 SVG 会先把 `--primary` 等变量的当前值写进去再栅格化（SVG 当图片用时读不到页面变量）；换主题色后需要刷新才会更新纹理。
- 着色器参数在 `FS` 里：`.022`（波幅）、`.10`（向外推的力度）、`26.`（波的密度）、`.006`（颜色分离）；衰减速度是 JS 里的 `.04`。
- 只在有互动 / 还没衰减完时才跑 `requestAnimationFrame`，静止时不耗电。
- **回退**：不支持 WebGL、着色器失败、跨域图片取不到纹理，或开启「减少动态」时，直接显示原图（不会空白）。
- **触屏**：`touch-action:pan-y`，竖向滑动仍然滚动页面；点按 / 按住拖动触发涟漪，没有悬停依赖。
- 每张图一个 WebGL 上下文，一页放 8 张以内；更多时建议只对首屏几张启用。
- 与 `img-hover-zoom`（放大）、`img-magnifier`（放大镜）、`img-clip-reveal`（遮罩展开）不同：这是对像素本身做位移扭曲。
- 动画都带 `prefers-reduced-motion` 降级；交互元素可键盘操作；没有 JS 时内容直接完整显示。
