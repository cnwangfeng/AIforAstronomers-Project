# 中文书稿来源、许可证与 AI-use QA 记录

本文件记录当前课程包在 bibliography、数据来源、许可证、外部材料边界和 AI-use statement 方面的发布前审查状态。

## 当前快照

- `data/manifest.yml` 已通过 `python scripts/validate_data_manifest.py`，当前登记 `52` 个教学数据集。
- `data/manifest.yml` 中登记的 `52` 个数据路径当前均存在。
- 当前所有教学数据集的 license 字段统一为：`Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International (CC BY-NC-SA 4.0)`.
- 当前仓库已包含顶层 `LICENSE`、`NOTICE.md`、`CITATION.cff` 和 `AI_USE_STATEMENT.md` 文件。
- `book/references.bib` 已有 `4` 个基础参考条目：Acquaviva、Ivezic et al.、astroML、Python for Astronomers。
- 当前中文主线 `book/main_zh.tex` 已接入 bibliography 入口，并使用 `\nocite{...}` 输出参考文献；当前版本没有把外部教材段落作为逐章改写来源，若未来需要逐章精确归因，再补正文 `\cite{...}`。
- 当前中文主线未使用外部图片 `\includegraphics`；正文图表主要由 TikZ、PGFPlots 或 LaTeX 内嵌教学数据生成。
- `scripts/check_publication_blockers.py` 已建立，用于把上述来源、许可证、引用和 AI-use 状态转成可运行报告；默认信息模式不阻塞技术 QA，`--strict` 现已可作为最终发布 gate。

## 当前 QA 结论

- 教学数据结构、路径和字段登记已进入可验证状态；数据许可证已经统一并写回 `data/manifest.yml`。
- Python for Astronomers、astroML 和相关教材目前主要作为项目路线图与参考书目条目存在；中文正文没有直接复制外部教材段落的显式迹象。当前发布路径按项目级 bibliography、NOTICE 和 AI-use statement 收口。
- AI-use statement 主线已经进入第 38 章和 Part VI delivery / rubric / project workflow；项目级发布声明现已补齐。
- 许可证、引用、归属和 AI-use 文件已闭环，当前不再是发布前阻塞项。
- 最近一次 `python scripts/check_publication_blockers.py` 信息模式报告 `0` 个开放项；`python scripts/check_publication_blockers.py --strict` 可作为最终发布 gate。

## 发布前状态

- 顶层 `PUBLICATION_DECISIONS.md` 已记录当前发布路径、许可证和 AI-use 决策。
- 顶层 `LICENSE`、`NOTICE.md`、`CITATION.cff` 和 `AI_USE_STATEMENT.md` 已补齐。
- 正文 bibliography 已接入 `references.bib`，当前通过 `\nocite` 输出参考文献；若后续需要逐章归因，可继续补 `\cite{...}`。
- 当前最终发布 gate 已可以使用 `python scripts/check_publication_blockers.py --strict`。
- 最终发布 gate：完成上述决策后，运行 `python scripts/check_publication_blockers.py --strict`，确认开放项已经关闭。

## 后续维护

1. 如果后续调整发布路径或许可证范围，先更新 `PUBLICATION_DECISIONS.md`，再同步 `LICENSE`、`NOTICE.md`、`CITATION.cff`、`AI_USE_STATEMENT.md` 和 `data/manifest.yml`。
2. 如果正文继续补充外部来源或改写引用，再同步 `book/references.bib` 和相应章节的 `\cite{...}`。
3. 继续把这份 QA 台账当作发布维护记录，而不是新的决策入口。
