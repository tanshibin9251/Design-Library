# Art Pack（img-art-pack）

- 名称：Art Pack / 图形图片包
- 分类：Images & Gallery（`images`）
- 需要：纯 CSS + 内联 SVG，无第三方库
- 说明：没有照片时用的 6 种自绘「假照片」：流体色球、几何拼贴、等高线、胶片颗粒日落、人像剪影、产品立台。比例 4:5，颜色全部来自主题变量，会跟着换色。
- 授权：自写，可用于任何客户站

## 怎么用
- 把想要的 `<div class="ap-art"> … <svg> … </svg></div>` 复制出来，放进任何图片效果里当图片（Clip Reveal、Liquid Distort、Scroll Zoom 等后续效果都用它）。
- `ap-art` 容器决定尺寸（默认 `aspect-ratio:4/5`）；SVG 用 `slice` 铺满，换比例也不会变形。
- **只是占位**：有真实照片后换掉。需要写实物体（显卡、人物脸）时仍然标「缺图」，这套只给抽象 / 剪影。
- 氛围动画（色球漂移、等高线旋转）带 `prefers-reduced-motion` 降级；纯装饰，已 `aria-hidden`，外层 `role=img` 有说明。
- 颜色靠 `--primary --secondary --accent --surface --border`，圆角 `--radius`，速度 `--speed`。
