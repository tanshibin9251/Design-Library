# Commit Camp

> 自有原创母版，授权 ok。

- **适合**：Landing / Company；在线编程训练营、技术课程平台、编程学校

## Feel
像打开了一个 IDE：左侧文件树、顶部标签、底部状态栏。深色、等宽、绿色一点点亮。

## 调色
| 角色 | HEX | 用在哪 |
|---|---|---|
| Primary | `#e6edf3` | 浅灰白：标题 |
| Secondary | `#8b949e` | 注释灰：注释行、元信息 |
| Text | `#c9d1d9` | 正文 |
| Accent | `#3fb950` | 提交绿：按钮、选中、状态栏、进度 |
| Surface | `#0d1117` | 编辑器底 |
| Border | `#30363d` | 分隔线 |

## 字体
标题与界面 Geist Mono；正文 Geist。中文可换 Noto Sans SC。
中文内容配 Noto Sans SC / Noto Serif SC，中文标题不要斜体。

## 构图特征（Design signature）
1. 左侧固定 250px 文件树就是导航，页面名以文件名呈现（index.html、roadmap.log…）；顶部有标签条，底部 28px 绿色状态栏（分支、错误数）。手机上折叠成顶部菜单。
2. 注释行（`// ...`）当作小标题；标题里的关键词用绿色。
3. 首屏有「终端」窗口，光标闪烁。
4. 路线图页是 `git log --graph` 文本：提交哈希、分支线、标签，每条是一门课。
5. Playground 页：左边编辑、右边沙盒 iframe 实时预览，不执行脚本。

## 不要
- 不要紫色渐变、霓虹光晕（neon-nexus / aurora-cowork 已用）。
- 不要卡通插画、Emoji。
- 不要圆润大圆角（上限 10px）。
- 不要超过三个字号层级。
