# Book 目录说明

本目录保存中文教材的 LaTeX 源文件。它是同步到 Overleaf 书稿仓库的唯一来源。

当前内容来自原有书稿仓库，后续将逐步整理为：

```text
book/
  main.tex
  chapters/
  appendices/
  figures/
  references.bib
```

短期内保留当前扁平结构，避免一次性大改影响编译。清理顺序建议：

1. 修复 `main.tex` 中的 `\include` 路径和 `Glossary` 拼写。
2. 添加 `references.bib`。
3. 把章节逐步迁移到 `chapters/`。
4. 建立统一图表目录。
5. 将正文全部改写为中文，并按路线图扩展完整内容。

同步到 Overleaf 前，请在项目根目录运行：

```bash
bash scripts/sync_book_to_overleaf.sh
```

确认 dry-run 输出无误后再加 `--apply`。

