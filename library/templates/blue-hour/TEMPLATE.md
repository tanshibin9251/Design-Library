# Blue Hour（蓝调时刻）

An immersive photo-expedition site: type that holds a moving picture, a pinned scene stack, an image that follows your cursor, a route that draws itself and prints that ripple. Night-violet ground with first-light gold. All pictures are drawn SVG placeholders; swap in photographs.

- **字体**：标题 Josefin Sans · 正文 Source Serif 4

## 页面（9）
- Home: the blue hour（`home`）
- Departures (list + filter)（`expeditions`）
- Expedition: Lofoten in winter（`expedition`）
- Field journal（`journal`）
- Story: Eleven minutes of blue（`story`）
- Prints (liquid distort)（`prints`）
- The studio（`about`）
- Enquire（`contact`）
- 404 error（`404`）

## 用到的「沉浸式」效果（均来自库里的效果，已改成按页面作用域运行）
- 首页：`img-mask-text`（BLUE HOUR 字里的图）、`text-split-lines`、`scroll-scene-stack`、`img-clip-reveal`、`cursor-image-follow`、`scroll-path-draw`、`scroll-velocity-skew`、`text-scramble`、`button-pointer-fill`
- 出发列表：`img-strip-slices`、`cursor-image-follow`（带季节筛选）
- 出发详情：`img-scroll-zoom-pin`、`scroll-path-draw`
- 日志：`img-rgb-split`、`img-clip-reveal`；文章：`img-mask-text`、`text-split-lines`、`img-clip-reveal`、`text-scramble`
- 作品印刷：`img-liquid-distort`（WebGL，无 WebGL 时回退为原图）
- 关于：`scroll-number-morph`、`scroll-zoom-tunnel`、`text-split-lines`

## 换成真实照片
- 每个 `.ap-art`（里面是 SVG）换成 `<img>`（`object-fit:cover`）即可；`.ss-art`、`.cr-clip`、`.zp-pic`、`.zt-f`、`.cf-a`、`.sp`、`.rs-base`、`.ld` 都是同样的做法。
- 把文字里的占位文案、价格（RM）和日期换成客户的真实内容。
