# Publication Decisions

本文件记录正式发布前必须由项目负责人确认的非技术决策。它不替代 `LICENSE`、`NOTICE`、`CITATION` 或 AI-use statement；它只是把这些文件创建前的选择集中到一处。

## 1. 发布路径

当前待确认：

- 是否只做课堂内部使用。
- 是否公开教学发布。
- 是否允许非商业改编与再分发。
- 是否预留商业出版或出版社合作路径。

说明：

- 如果预留商业出版路径，应避免直接依赖 CC BY-NC-SA 材料的改写内容。
- 如果定位为开放教学资源，可以选择更明确的开放许可证组合，但仍需分别处理文字、代码和数据。

## 2. 许可证拆分

需要分别确认：

- 教材文字与 LaTeX 图表许可证。
- 代码、脚本和 notebooks 许可证。
- 小型 synthetic teaching datasets 许可证。
- 外部参考材料、灵感来源、引用和改写边界。

当前状态：

- 顶层 `LICENSE` 尚未创建。
- 顶层 `NOTICE` / `ATTRIBUTION` 尚未创建。
- `data/manifest.yml` 的 license 字段仍使用项目级占位说明。

## 3. 引用与归属

当前参考入口：

- `book/references.bib` 已包含 Acquaviva、Ivezic et al.、astroML、Python for Astronomers 四个基础条目。
- 当前中文正文尚未接入 bibliography，也未使用 `\cite{...}`。

需要确认：

- 哪些来源只是路线图参考，哪些需要进入正文 bibliography。
- 是否需要在 `NOTICE` / `ATTRIBUTION` 中单独说明 Python for Astronomers、astroML 等资源的参考边界。
- 是否创建 `CITATION.cff` 或 `CITATION.md`。

## 4. 项目级 AI-use Statement

章节内已经训练学生写 AI-use statement，但课程包本身仍需要项目级说明。

需要确认：

- 教材正文、notebook、脚本和 QA 过程中是否使用 AI 辅助。
- AI 辅助参与了哪些任务：起草、重写、代码生成、错误检查、摘要、发布 QA。
- 哪些判断由人工确认：科学结论、引用、许可证、数据边界、最终发布。
- 是否把项目级 AI-use statement 放在 README、NOTICE，还是单独文件中。

## 5. 发布前文件清单

完成上述决策后，建议补齐：

- `LICENSE`
- `NOTICE.md` 或 `ATTRIBUTION.md`
- `CITATION.cff` 或 `CITATION.md`
- 项目级 AI-use statement
- 正文 bibliography 接入方案
- `data/manifest.yml` 中最终 license 字段

## 当前建议

在没有确认发布路径前，不创建最终 `LICENSE`，也不把占位 license 改成具体许可证。先保持当前技术包可验证、可同步、可审查；等发布目标明确后，再一次性补齐法律和归属文件。
