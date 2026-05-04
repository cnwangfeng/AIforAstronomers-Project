# Publication Decisions

本文件记录正式发布前必须由项目负责人确认的非技术决策。当前这些决策已经完成，并作为后续复核记录保留；它不替代 `LICENSE`、`NOTICE`、`CITATION` 或 AI-use statement。

## 1. 发布路径

当前决策：

- 本项目作为非商业开放教学资源公开发布。
- 当前版本不预留商业出版路径；如果未来需要商业出版，需重新审视是否继续使用与 CC BY-NC-SA 兼容的改写材料。

## 2. 许可证拆分

统一许可证方案：

- 教材文字与 LaTeX 图表：CC BY-NC-SA 4.0。
- 代码、脚本和 notebooks：CC BY-NC-SA 4.0。
- 小型 synthetic teaching datasets：CC BY-NC-SA 4.0。
- 外部参考材料、灵感来源、引用和改写边界：见 `NOTICE.md`。

当前状态：

- 顶层 `LICENSE` 已创建。
- 顶层 `NOTICE.md` 已创建。
- `data/manifest.yml` 的 license 字段已统一为 CC BY-NC-SA 4.0。

## 3. 引用与归属

当前参考入口：

- `book/references.bib` 已包含 Acquaviva、Ivezic et al.、astroML、Python for Astronomers 四个基础条目。
- 当前中文正文尚未接入 bibliography，也未使用 `\cite{...}`。

当前参考入口：

- `book/references.bib` 已包含 Acquaviva、Ivezic et al.、astroML、Python for Astronomers 四个基础条目。
- `book/main_zh.tex` 已接入 bibliography hook，并使用 `\nocite{...}` 输出参考文献；后续如需逐章精确归因，再补正文 `\cite{...}`。

当前状态：

- `CITATION.cff` 已创建。
- `NOTICE.md` 已明确外部来源和授权边界。

## 4. 项目级 AI-use Statement

章节内已经训练学生写 AI-use statement，但课程包本身仍需要项目级说明。

当前状态：

- `AI_USE_STATEMENT.md` 已创建。
- 项目级说明记录了 AI 辅助参与的起草、重写、代码生成、日志摘要和 release QA。
- 人工确认仍承担科学判断、引用选择、许可证、数据边界和最终发布责任。

## 5. 发布前文件清单

已补齐：

- `LICENSE`
- `NOTICE.md`
- `CITATION.cff`
- `AI_USE_STATEMENT.md`
- 正文 bibliography 接入方案
- `data/manifest.yml` 中最终 license 字段

## 当前建议

当前版本已完成非商业开放教学发布收口；后续若修改发布路径或许可证范围，先回到这里更新决策，再同步 `LICENSE`、`NOTICE.md`、`CITATION.cff`、`AI_USE_STATEMENT.md` 和 `data/manifest.yml`。
