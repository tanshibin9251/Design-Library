# 资源来源

> 记录从外部网站得到的模板和动效资源：它是什么、授权如何、怎么用到本库。抓取日期 2026-10-08。**授权不明的只记录、不入库**（见 `library/FORMAT.md`）。

## 总览
| 来源 | 类型 | 授权 | 能否入库 | 状态 |
|---|---|---|---|---|
| [Ultimate Elementor 模板](https://ultimateelementor.com/elementor-templates/?type=free&page-builder=) | Elementor 整站模板（300+） | 页面未写明模板内容的再分发条款 | **只记录灵感，不入库 JSON** | 已记录 |
| [GSAP](https://gsap.com/) | JS 动画库 | GSAP Standard License：商用免费 | 可以引用，**不可内置到可视化动画工具** | 已记录 |
| [anime.js](https://animejs.com/) | JS 动画库 v4 | MIT | 可以入库、可分发 | 已记录 |
| [Motion](https://motion.dev/) | JS/React/Vue 动画库 | MIT（核心）；Motion+ 付费部分不可用 | 核心可入库 | 已记录 |

## Ultimate Elementor 模板
- 来源：https://ultimateelementor.com/elementor-templates/?type=free&page-builder=
- 内容：300+ 个整站模板，大部分免费，少数标 Premium。例：Martial Arts School（本地商家类）。
- 交付方式：**不提供文件下载**，要在 WordPress 里装 **Starter Templates** 插件，在后台 Appearance › Starter Templates 里选模板导入。兼容 Elementor 免费版、Pro、Block Editor、Beaver Builder；官方称配 Astra 主题 + Ultimate Addons for Elementor 效果最好。
- 授权：页面只说明「可导入到其他主题，可能需要微调」，**没有写明模板内容能否导出后再分发**。按 FORMAT 规则，授权不明的不入库。
- 怎么用：
  1. **当灵感**：按行业看版式、区块顺序，借鉴手法，不抄文字和配色。
  2. **要导出 JSON 前**：先查 Starter Templates 的服务条款，确认可复用再放进 `_work/inbox/`。
  3. 免费模板依赖 Astra 与 Ultimate Addons 时，要在 KIT.md 里标明。

## GSAP
- 来源：https://gsap.com/　文档：https://gsap.com/docs/v3/　示例：https://demos.gsap.com/
- 现状：由 Webflow 支持，**现在对所有人免费，含商用**。包含 ScrollTrigger、ScrollSmoother、ScrollTo、DrawSVG、MorphSVG、MotionPath、SplitText、ScrambleText、Flip、Draggable、Inertia、Observer、Physics2D、GSDevTools。
- 授权：GSAP Standard License（https://gsap.com/standard-license/）。商用免费；**禁止用于与 Webflow 竞争的「无代码可视化动画工具」**；不得修改版权声明；知识产权归 Webflow。
- 适合本库：用 GSAP 做网站上的动效是允许的。**但不要把 GSAP 打包进一个让用户用界面拖拽做动画的产品里。** 本库的效果是「复制代码到网站」，属于正常使用。
- 可做的效果（待入库）：ScrollTrigger 滚动显现与固定、SplitText 逐字标题、Flip 布局切换、DrawSVG 描线、横向滚动区。
- 引用方式：CDN 或 npm，写进每个效果的 EFFECT.md「需要」一栏。

## anime.js
- 来源：https://animejs.com/　GitHub：juliangarnier/anime
- 现状：v4.0.0，约 24.5 KB，模块化。含 Timeline、Scroll Observer、Draggable、Stagger、SVG（形变、描线、运动路径）、Scope（响应式动画）、弹簧物理。
- 授权：**MIT（2025，Julian Garnier）**。商用、修改、再分发都允许，须保留版权声明。
- 适合本库：最适合直接内置到可下载的模板和效果里。
- 可做的效果（待入库）：Stagger 网格入场、Timeline 序列动画、SVG 描线与形变、可拖拽卡片。

## Motion（原 Framer Motion）
- 来源：https://motion.dev/　文档：https://motion.dev/docs　示例：https://motion.dev/examples
- 现状：支持 React、JavaScript、Vue。核心 API：独立 transform、滚动动画（ScrollTimeline）、hover/press/drag、布局动画、弹簧、退出动画、stagger 与时间线。
- 授权：**核心 MIT 免费**。Motion+（付费）含 Gallery、AI Kit、480+ 高级示例，**不可使用**。
- 适合本库：Custom Site Builder 的纯 JS 效果用 Motion 的 vanilla API；React/Vue 部分用不到。
- 可做的效果（待入库）：scroll 联动、inView 显现、hover 弹簧、拖拽。

## 入库规则（执行时）
1. 每个新效果的 EFFECT.md 必须写：来源 URL、库名与版本、授权、CDN 地址。
2. **默认使用 CSS 或本库自写的轻量 JS**；需要 GSAP、anime.js、Motion 才放进「需 JS（库：…）」。
3. 所有效果带 `prefers-reduced-motion` 降级，炫技型默认在移动端简化。
4. 每个效果先在示例页实测再标「已实测」。

## 待办
- [ ] 用 GSAP、anime.js、Motion 各做第一批效果（每库 6–8 个，共约 20 个），写进 `library/effects/`
- [ ] 逐个核对 Ultimate Elementor 免费模板，挑 5–10 个行业记录灵感
- [ ] 确认 Starter Templates 的模板内容授权后，再决定要不要导出 JSON
