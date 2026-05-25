# Book 目录说明

本目录保存中文教材的 LaTeX 源文件。它是同步到 Overleaf 书稿仓库的唯一来源。

当前采用的命名策略是：

- 教材中文正式题目：面向天文与物理本科生的 AI 科研实战
- 教材英文副标题：Practical AI for Astronomy and Physics
- 仓库名继续保留：AIforAstronomers

说明：`main_zh.tex` 是当前中文教材唯一主入口，使用 XeLaTeX 编译。历史 `main.tex` 兼容入口和旧扁平章节文件已经删除，避免 Overleaf 或其他工具误编旧书稿。

当前编译入口：

- `main_zh.tex` 是中文正文主线入口；
- `main_zh.tex` 应使用 XeLaTeX 编译。

正文结构说明：

- 通用 Python 入门内容已经下沉到 `Part 0` 先修模块；
- `main_zh.tex` 默认不再承载 Python 零基础教学，而是从科研工作流主线进入；
- `Part 0` 保持 notebook-first、正文外、短先修定位，不继续扩成第二本 Python 教材。

推荐的本地编译方式：

```bash
bash scripts/build_book_local.sh zh
```

编译结果默认写入系统临时目录：

- 中文入口：`/tmp/aifor_book_main_zh/`

如果第一次从零开始编译中文入口，`latexmk` 可能需要多轮生成目录和各章辅助文件；脚本已经处理了这类情况。

当前主要书稿结构已经整理为：

```text
book/
  main_zh.tex    # 中文主入口
  chapters/
  references.bib
```

旧的扁平章节文件已经删除；中文主书稿统一使用 `chapters/part*/` 结构。当前已经完成：

- `references.bib` 初始建立
- `main_zh.tex` 的 Part I--V 主线接入
- Part 0 Python 先修模块从正文主线中独立
- `FIGURE_TABLE_QA.md` 已建立，用于记录中文主线图表、表格、来源和发布前 QA 状态
- `EVIDENCE_CARD_QA.md` 已建立，用于记录八张项目证据卡的 canonical 名称、桥接状态和发布前 QA 状态
- `FORMULA_QA.md` 已建立，用于记录中文主线公式数量、解释标准和发布前公式 QA 状态
- `SOURCE_LICENSE_QA.md` 已建立，用于记录 bibliography、数据来源、许可证、外部材料边界和 AI-use 发布前 QA 状态
- `scripts/check_figure_table_refs.py` 和 `scripts/check_formula_inventory.py` 已接入聚合发布检查，避免图表、表格和公式台账继续靠人工计数维护

说明：这些 `*_QA.md` 文件是完整项目仓库中的发布维护台账；默认 Overleaf 同步会排除它们，使书稿仓库保持在 LaTeX 源文件、编译资源和必要说明文件范围内。

后续清理顺序建议：

1. 持续更新 `FIGURE_TABLE_QA.md`，统一图表目录和图表来源说明。
2. 持续更新 `EVIDENCE_CARD_QA.md`，避免八张项目证据卡在新增章节中漂移。
3. 持续更新 `FORMULA_QA.md`，确保新增公式有变量、单位、计算角色和适用边界；新增或删除 display math 后运行 `python scripts/check_formula_inventory.py`。
4. 持续更新 `SOURCE_LICENSE_QA.md`，把许可证、引用和 AI-use 决策从正文润色中分离出来。
5. 按路线图继续细读正文、统一术语、补交叉引用和图表说明。
6. 同步到 Overleaf 书稿仓库前运行中文编译检查。

同步到 Overleaf 前，请在项目根目录运行：

```bash
bash scripts/sync_book_to_overleaf.sh
```

确认 dry-run 输出无误后再加 `--apply`。

如果准备做一次完整发布或同步收尾，也建议同时查看项目根目录中的：

- `COURSE_PACKAGE_RELEASE_NOTES.md`
- `RELEASE_SYNC_CHECKLIST.md`
