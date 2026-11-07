# Diamond Shop（菱形商店）v2

> 自有原创母版，授权 ok。v1（白底红色 Hero + Rubik 圆润字）被使用者否决；v2 改为参考 kumpoo.com 的整体气质（暗色、酒红光晕、红色强调、全大写运动字），但**不照抄**：官网是电影感暗色 + 渐变大字 + 斜切球员卡，这里是「暗色页头/Hero + 白底商品区」的商店结构。适合鞋服球拍多品类、鞋服要选尺码、沟通方式以 WhatsApp 为主的店。

- **适合**：Ecommerce / Company；运动用品多品类店

## Feel
暖黑底 + 酒红光晕，商品区是纯白底，商品图放在浅灰「板」上跳出来；一个品牌红；全大写运动感标题。装饰来自 logo 的菱形（旋转 45° 的小方块）和斜切平行四边形。

## 调色
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#0c0809` | 暖黑：页头、Hero、页脚、深色区块、选中状态 |
| Secondary | `#2a0a10` | 酒红：分类轨道、渐变搭档、促销块 |
| Text | `#1a1213` | 白底区正文 |
| Accent | `#ce2128` | 品牌红：公告条、主按钮、价格强调、菱形标记（取自 Kumpoo logo 实测像素值） |
| Surface | `#ffffff` | 白底（商品区、商品页、购物车） |
| Border | `#e3dfdb` | 白底区分隔线 |

另：WhatsApp 按钮 `#1f9d55`（WhatsApp 绿，只用在 Ask on WhatsApp）；深色区的酒红光晕 `#5b0d18` / `#4a0b15` 只做 radial-gradient。

## 字体
标题 Saira 700 全大写（字距 +.01em）；正文 Hanken Grotesk。商品名用正文字体 600 不大写，避免整页全大写太吵。中文内容配 Noto Sans SC，中文标题不要斜体。

## 构图特征（Design signature）
1. 暗色页头：红色公告条 → 左菜单 / 居中 logo / 右搜索·账号·红色购物车 → 酒红分类轨道（带数量）。
2. Hero：暖黑 + 酒红光晕，左大标题（红色词强调），右侧斜切骨白主图板 + 错位的红色斜切板 + 白色标签；底边 6px 红线。
3. 白底区：分类入口和商品卡**不再做白色卡片**——图放在浅灰「板」上（右下角切角），下面是黑色粗线 + 红色斜平行四边形标记 + 名称 / 价格；红色斜角标；hover 时粗线和标记变红、标题变红（不用阴影）；Quick view 滑出（触屏不显示）。
4. 暗色「Find your fit」带：编号菱形列表 + 红色顶线；促销块是酒红渐变 + 红色斜切板。
5. 商品页「尺码优先」：颜色圆点 + 尺码胶囊（缺货划线）+ 数量 + **Add to cart 与 Ask on WhatsApp 双按钮**；规格表 + 「Find your size」尺码表 + 提示框；手机端吸底购买条；页头区暗色，内容区白底。

## 不要
- 不要给商品卡 / 分类牌加白色卡片底和阴影（白底页面上看不出来）；用浅灰板 + 黑色粗线。
- 不要整页黑；暗色只用在页头、Hero、重点带、页脚，商品必须在白底区。
- 不要渐变大字、不要电影感满屏轮播（那是 kumpoo.com 官网的做法，避免过于相似）。
- 不要圆角胶囊按钮（v1 的做法）；按钮用斜切角。
- 不要把红色铺满大块，除了 Hero 的斜切板和促销块。
- 不要斜体字；斜效果只用 clip-path / skew。

## Elementor 落地提示
- 全局色/字体由使用者在 Elementor Site Settings 手动设定，Claude 只读 `design.md` 里登记的值。
- 暗色区用 Container 背景色 + Background Overlay / 渐变；斜切（clip-path）和菱形（rotate 45°）写在 Container / Image 的 Custom CSS，每页不超过 3 类。
- 商品卡、商品页走 WooCommerce 模板（Theme Builder: Product Archive / Single Product）；尺码胶囊用变体 swatch（插件待选）；吸底购买条用 Elementor Sticky（Pro）或 Sticky Add to Cart 插件。
- 动效只用 Elementor 原生 Motion Effects / Entrance Animation，每页不超过两种。
