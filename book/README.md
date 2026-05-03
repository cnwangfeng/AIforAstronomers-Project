# Book 目录说明

本目录保存中文教材的 LaTeX 源文件。它是同步到 Overleaf 书稿仓库的唯一来源。

当前采用的命名策略是：

- 教材中文正式题目：面向天文与物理本科生的 AI 科研实战
- 教材英文副标题：Practical AI for Astronomy and Physics
- 仓库名继续保留：AIforAstronomers

说明：当前 `main.tex` 仍沿用英文可编译标题，以避免在正式切换到中文 LaTeX 编译链前影响 Overleaf 稳定性。后续在引入 XeLaTeX/中文支持时，再将封面和元数据切换为中文主标题 + 英文副标题。

中文编译入口准备：

- `main.tex` 继续作为当前稳定入口；
- `main_zh.tex` 作为中文正文主线入口，供 Overleaf/XeLaTeX 试编译；
- `main.tex` 已在本机通过 `latexmk -pdf` 编译验证；
- `main_zh.tex` 已在本机通过 `latexmk -xelatex` 编译验证。

正文结构说明：

- 通用 Python 入门内容正在迁移到 `Part 0` 先修模块；
- `main_zh.tex` 默认不再承载 Python 零基础教学，而是从科研工作流主线进入；
- `Part 0` 更适合以 notebook-first 形式组织，必要时再补充独立文字材料。

推荐的本地编译方式：

```bash
bash scripts/build_book_local.sh main
bash scripts/build_book_local.sh zh
```

编译结果默认写入系统临时目录：

- 英文入口：`/tmp/aifor_book_main/`
- 中文入口：`/tmp/aifor_book_main_zh/`

如果第一次从零开始编译中文入口，`latexmk` 可能需要多轮生成目录和各章辅助文件；脚本已经处理了这类情况。

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

如果准备做一次完整发布或同步收尾，也建议同时查看项目根目录中的：

- `COURSE_PACKAGE_RELEASE_NOTES.md`
- `RELEASE_SYNC_CHECKLIST.md`
