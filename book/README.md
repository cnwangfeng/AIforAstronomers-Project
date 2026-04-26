# Book 目录说明

本目录保存中文教材的 LaTeX 源文件。它是同步到 Overleaf 书稿仓库的唯一来源。

当前采用的命名策略是：

- 教材中文正式题目：面向天文与物理本科生的 AI 科研实战
- 教材英文副标题：Practical AI for Astronomy and Physics
- 仓库名继续保留：AIforAstronomers

说明：当前 `main.tex` 仍沿用英文可编译标题，以避免在正式切换到中文 LaTeX 编译链前影响 Overleaf 稳定性。后续在引入 XeLaTeX/中文支持时，再将封面和元数据切换为中文主标题 + 英文副标题。

中文编译入口准备：

- `main.tex` 继续作为当前稳定入口；
- `main_zh.tex` 作为中文草稿入口，供 Overleaf/XeLaTeX 试编译；
- 在本机尚未安装 LaTeX 工具链的情况下，`main_zh.tex` 还没有经过本地编译验证。

当前内容来自原有书稿仓库，后续将逐步整理为：

```text
book/
  main.tex
  chapters/
  appendices/
  figures/
  references.bib
```

短期内保留当前扁平结构，避免一次性大改影响编译。当前已经完成：

- `main.tex` 的 `\include` 扩展名清理
- `Glossary` 引用修正
- `references.bib` 初始建立

后续清理顺序建议：

1. 把章节逐步迁移到 `chapters/`。
2. 建立统一图表目录。
3. 切换到支持中文的 LaTeX 编译链。
4. 将正文全部改写为中文，并按路线图扩展完整内容。

同步到 Overleaf 前，请在项目根目录运行：

```bash
bash scripts/sync_book_to_overleaf.sh
```

确认 dry-run 输出无误后再加 `--apply`。
