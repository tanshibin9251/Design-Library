# GitHub → Hostinger 自动部署

## 分支职责

- `main`：维护源文件、构建工具和说明，不提交生成的 public_html。
- `deploy`：GitHub Actions 自动生成的网站文件；根目录就是 index.php、assets、api 等，不再套 public_html 文件夹。不要手动编辑这个分支。

每次 push main → Actions 构建 → 检查输出 → 正常快进 push deploy → 已连接 deploy 的 Hostinger 自动更新。

工作流：`.github/workflows/deploy.yml`，也可以在 GitHub Actions 的 **Build Hostinger deploy branch → Run workflow** 手动重跑 main。首次成功后才会出现 deploy 分支。工作流需要 `contents: write`；不需要额外 FTP 密码或个人 Token。若仓库/组织策略禁止 Actions 写分支，需要在该仓库设置中允许相应权限。

## Hostinger 一次性设置

1. 等 GitHub Actions 首次构建成功，确认 GitHub 有 deploy 分支。
2. Hostinger 的 Git 部署选择本仓库，Branch 选 **deploy**。
3. 服务器目标 root directory 使用该站原有的 **public_html**。这个设置指服务器目录，不是仓库的源码子目录。
4. 部署后打开真实网址，检查首页、模板预览、效果和下载；确认 Auto-deployment 开启。

当前工作流只负责生成和推送分支。Hostinger 的连接、部署历史与线上结果需要在面板另行确认；GitHub 的绿色勾不等于 Hostinger 已经上线成功。

官方操作说明：https://www.hostinger.com/support/1583302-how-to-deploy-a-git-repository-in-hostinger/

## 日常操作

在 main 修改 library 或 build 源码，检查后 commit / push 即可。只修改文档也会触发构建；如果最终网站文件没变化，不会产生新的 deploy 提交。

CI 使用 Python 3.13，无第三方构建依赖。缩略图读取已收录的 library/previews，不在 CI 中启动浏览器重新截图；视觉改动需要在本地生成缩略图再提交其源文件。

`tools/check_public_build.py` 只读检查：网站必要文件、公开 catalog 与源码一致、公开 API 文件、受限条目路径和 ZIP 完整性。它不代替真实浏览器验收，也不证明已检查全部内容许可。

`tools/publish_deploy.py` 只在 Actions 的 main 运行；独立 Git index 构造网站文件树，保留 deploy 历史，不切换源码 checkout、不强推。构建或检查失败时不会更新 deploy；旧版本仍留在分支。过时的 main 构建会跳过，等待新一次运行。

## 排错

- 没看到 deploy：先打开 Actions 查看首次运行结果，成功前 Hostinger 没有该选项。
- Actions 权限错误：检查仓库 Actions 策略和 deploy 分支保护规则；不要把私人 Token 写进 YAML。
- Actions 成功、网站没更新：核对 Hostinger 连接的是 deploy，自动部署已开启，查看其部署历史和缓存。
- 不能手动重跑 main：确认工作流已在 main，账号有 Actions 操作权限。
- 需要旧版本：找到对应 main 提交，恢复所需源码后作为新提交 push；不要直接编辑 deploy，下一次构建会覆盖它。

GitHub 构建不使用 `_work/upload/` 的人工上传基线，不运行 `--mark-uploaded`，也不运行 `build/deploy.py`。人工上传作为备用流程，仍按 HOW_IT_WORKS 执行。
