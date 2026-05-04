# 中文书稿图表与表格 QA 记录

本文件记录 `book/main_zh.tex` 当前正文主线的图表盘点状态，用于 Stage C 图表、交叉引用和来源说明收束。

## 当前快照

- 当前中文正文图环境：`10` 个，均位于 `book/chapters/part4` 和 `book/chapters/part5`。
- 当前中文正文表环境：`33` 个，主要位于 `book/chapters/part5` 和 `book/chapters/part6`。
- 当前 caption / label 数：`43` 个，与图表总数一致。
- 当前 `\label{...}` 与正文引用入口已对齐：`43` 个唯一 label 均有对应的正文 `\ref{...}`，未发现引用到不存在 label 的情况。
- 当前中文主线共有 `140` 个 display math block，未使用单独编号的 `equation` / `align` 环境；公式解释 QA 应以逐章正文承接和符号定义为主，而不是编号引用为主。
- 当前 `book/chapters` 未使用外部 `\includegraphics` 图片；正文图主要由 TikZ、PGFPlots 或 LaTeX 内嵌教学数据生成。
- 旧英文/兼容入口 `book/main.tex` 仍引用 `book/VersionControl/*.png`，但这些图片不属于当前中文主线。

## 来源与边界

- Part IV/V 的数据图和流程图均是教学版、仓库内生成或 LaTeX 内嵌示意图，不依赖外部论文图片。
- 教学数据来源与许可证边界统一登记在 `data/manifest.yml`；当前仍需在正式发布前确认项目级教材、代码和教学数据许可证。
- Part VI 的表格是 notebook workflow 对照表，来源于仓库内小型 synthetic teaching datasets，不是外部数据摘录。

## 当前 QA 结论

- 最近一次 `bash scripts/build_book_local.sh zh` 已通过，PDF 输出为 `/tmp/aifor_book_main_zh/main_zh.pdf`。
- 最近一次日志扫描未发现 `Overfull`、未定义引用、`Missing $` 或 LaTeX 错误。
- 已补强 `ch36` agentic workflow 流程图图注，明确 action log、manual review 和 route 边界。
- 已补齐 Part V/VI 所有表格的正文 `\ref{...}` 入口；图表 label 不再停留在孤立 caption 状态。

## 后续发布前检查

- 若新增外部图片或真实数据图，必须在本文件和 `data/manifest.yml` / release notes 中补来源、许可证、下载日期或生成脚本。
- 若新增图表，必须同时满足：正文引用、caption、label、单位/字段说明、解释边界。
- 若新增重要公式，必须在公式前后说明变量含义、单位或量纲、适用条件，以及它在 notebook / 例题中的计算角色。
- 若同步 Overleaf，先运行 `bash scripts/sync_book_to_overleaf.sh` dry-run，确认图表和附属文件路径不会丢失。
