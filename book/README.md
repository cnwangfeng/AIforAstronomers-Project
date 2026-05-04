# Book 目录说明

本目录保存中文教材的 LaTeX 源文件。它是同步到 Overleaf 书稿仓库的唯一来源。

当前采用的命名策略是：

- 教材中文正式题目：面向天文与物理本科生的 AI 科研实战
- 教材英文副标题：Practical AI for Astronomy and Physics
- 仓库名继续保留：AIforAstronomers

说明：`main_zh.tex` 是当前中文教材主入口，使用 XeLaTeX 编译；`main.tex` 保留为英文/兼容入口，主要用于历史书稿和稳定性检查。

当前编译入口：

- `main_zh.tex` 是中文正文主线入口；
- `main.tex` 继续作为兼容入口；
- `main.tex` 已在本机通过 `latexmk -pdf` 编译验证；
- `main_zh.tex` 已在本机通过 `latexmk -xelatex` 编译验证。

正文结构说明：

- 通用 Python 入门内容已经下沉到 `Part 0` 先修模块；
- `main_zh.tex` 默认不再承载 Python 零基础教学，而是从科研工作流主线进入；
- `Part 0` 保持 notebook-first、正文外、短先修定位，不继续扩成第二本 Python 教材。

推荐的本地编译方式：

```bash
bash scripts/build_book_local.sh main
bash scripts/build_book_local.sh zh
```

编译结果默认写入系统临时目录：

- 英文入口：`/tmp/aifor_book_main/`
- 中文入口：`/tmp/aifor_book_main_zh/`

如果第一次从零开始编译中文入口，`latexmk` 可能需要多轮生成目录和各章辅助文件；脚本已经处理了这类情况。

当前主要书稿结构已经整理为：

```text
book/
  main.tex
  main_zh.tex
  chapters/
  figures/
  references.bib
```

旧的扁平章节文件仍保留在 `book/` 下，用于兼容历史入口；中文主书稿已经转向 `chapters/part*/` 结构。当前已经完成：

- `main.tex` 的 `\include` 扩展名清理
- `Glossary` 引用修正
- `references.bib` 初始建立
- `main_zh.tex` 的 Part I--VI 主线接入
- Part 0 Python 先修模块从正文主线中独立
- `FIGURE_TABLE_QA.md` 已建立，用于记录中文主线图表、表格、来源和发布前 QA 状态
- `EVIDENCE_CARD_QA.md` 已建立，用于记录八张 capstone evidence cards 的 canonical 名称、桥接状态和发布前 QA 状态
- `FORMULA_QA.md` 已建立，用于记录中文主线公式数量、解释标准和发布前公式 QA 状态
- `SOURCE_LICENSE_QA.md` 已建立，用于记录 bibliography、数据来源、许可证、外部材料边界和 AI-use 发布前 QA 状态

后续清理顺序建议：

1. 持续更新 `FIGURE_TABLE_QA.md`，统一图表目录和图表来源说明。
2. 持续更新 `EVIDENCE_CARD_QA.md`，避免八张证据卡在新增章节中漂移。
3. 持续更新 `FORMULA_QA.md`，确保新增公式有变量、单位、计算角色和适用边界。
4. 持续更新 `SOURCE_LICENSE_QA.md`，把许可证、引用和 AI-use 决策从正文润色中分离出来。
5. 清理不再使用的历史扁平章节文件。
6. 按路线图继续细读正文、统一术语、补交叉引用和图表说明。
7. 同步到 Overleaf 书稿仓库前运行中文编译检查。

同步到 Overleaf 前，请在项目根目录运行：

```bash
bash scripts/sync_book_to_overleaf.sh
```

确认 dry-run 输出无误后再加 `--apply`。

如果准备做一次完整发布或同步收尾，也建议同时查看项目根目录中的：

- `COURSE_PACKAGE_RELEASE_NOTES.md`
- `RELEASE_SYNC_CHECKLIST.md`
