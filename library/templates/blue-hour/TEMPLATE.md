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

## 高清外链摄影版本（2026-11-07）
已添加按行业选择的外链示意摄影，来源、作者、原始宽高见 images.json。首图/特色图维持比例、按位置裁切，非首屏延迟加载；加载失败显示缺图。照片不保存在仓库或导出包内，预览及导出需要联网。库存图不代表实际产品、人员、房源、客户项目或成果；未找到对应真实资产的占位保留，不冒用照片。

## 共用交互基础（2026-11-07）
构建与 MCP 读取 fragments 时，build/template_enhance.py 将共用键盘焦点、跳转正文、手机菜单补齐、页脚分组、无动作表单的本地验证/反馈和静态购物演示打入 nav/pages/footer；HTML、PHP、JSON 导出与预览共用，不依赖 Live。原有业务专属脚本保留。购物车仅本浏览器示例数据，不是真实库存、税费、支付或订单服务；表单不发送信息，勿填写真实凭据。可选 interactions.js 为本模板专属行为。未提供实际照片的位置保留缺图；具名人员、实际客户项目与效果对比不可用无关库存图替代。
