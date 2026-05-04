# 中文书稿来源、许可证与 AI-use QA 记录

本文件记录当前课程包在 bibliography、数据来源、许可证、外部材料边界和 AI-use statement 方面的发布前审查状态。

## 当前快照

- `data/manifest.yml` 已通过 `python scripts/validate_data_manifest.py`，当前登记 `52` 个教学数据集。
- `data/manifest.yml` 中登记的 `52` 个数据路径当前均存在。
- 当前所有教学数据集的 license 字段统一为：`Repository educational content; verify final project-wide license before publication.`
- 当前仓库没有顶层 `LICENSE`、`NOTICE` 或 `CITATION` 文件。
- `book/references.bib` 已有 `4` 个基础参考条目：Acquaviva、Ivezic et al.、astroML、Python for Astronomers。
- 当前中文主线 `book/main_zh.tex` 未接入 bibliography，也未出现 `\cite{...}` 调用；参考文献仍是发布前待接入项。
- 当前中文主线未使用外部图片 `\includegraphics`；正文图表主要由 TikZ、PGFPlots 或 LaTeX 内嵌教学数据生成。

## 当前 QA 结论

- 教学数据结构、路径和字段登记已进入可验证状态；数据许可证仍依赖最终项目级许可证决策。
- Python for Astronomers、astroML 和相关教材目前主要作为项目路线图与参考书目条目存在；中文正文没有直接复制外部教材段落的显式迹象，但正式发布前仍需做最后一次人工抽查。
- AI-use statement 主线已经进入第 38 章和 Part VI delivery / rubric / project workflow；当前缺的是项目级发布声明，而不是章节教学内容。
- 许可证是当前发布前的真实阻塞项：教材文字/图表、代码、教学数据和外部材料引用边界需要分别确认。

## 发布前必须补齐

- 顶层 `PUBLICATION_DECISIONS.md`：集中确认发布路径、许可证拆分、引用归属和项目级 AI-use statement 的选择。
- 顶层 `LICENSE`：说明教材文字、代码和教学数据是否采用同一许可证，或分别采用不同许可证。
- 顶层 `NOTICE` 或 `ATTRIBUTION`：如继续保留 Python for Astronomers、astroML、Acquaviva、Ivezic et al. 等参考来源，应说明引用、改写和授权边界。
- 顶层 `CITATION.cff` 或 `CITATION.md`：说明课程包如何被引用。
- 正文 bibliography：决定是否在 `book/main_zh.tex` 中接入 `references.bib`，以及哪些章节需要显式引用。
- 项目级 AI-use statement：说明本课程包中 AI 辅助写作、代码生成、检查和人工确认的边界。

## 建议决策顺序

1. 先确定项目是否计划公开教学发布、非商业共享、商业出版，或三者分流。
2. 再分别确定教材文字/图表、代码、教学数据的许可证。
3. 随后补 `LICENSE`、`NOTICE` / attribution、`CITATION` 和项目级 AI-use statement。
4. 最后再接入正文 bibliography，避免先写引用格式、后改授权边界。
