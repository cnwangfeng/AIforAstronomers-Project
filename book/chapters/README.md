# Chapters Directory

This directory is the active chapter tree for the Chinese textbook entry point
`book/main_zh.tex`.

Current organization:

- `part0/`: Python prerequisite text kept outside the main book flow.
- `part1/`: scientific computing foundations.
- `part2/`: astronomy and physics data processing.
- `part3/`: machine-learning workflow and scientific inference.
- `part4/`: astronomy and physics case studies.
- `part5/`: deep learning and modern AI.
- `part6/`: capstone project, course package, and handoff materials.

The current Part I--VI synthesis layer uses a shared capstone evidence-card
frame: Project, Data, Baseline, Model, Evaluation, Interpretation,
Reproducibility, and Integrity. New revisions should preserve that handoff
instead of creating isolated reporting templates.

Most active writing now happens inside this tree. The legacy top-level chapter
files under `book/` are retained only for compatibility with older entry points
and should not be treated as the primary source for the Chinese textbook.

When adding or revising a chapter, keep it aligned with the current pattern:

- learning goals and scientific motivation;
- conceptual explanation before code details;
- a clear connection to the paired notebook and teaching data;
- common pitfalls or failure modes;
- basic, advanced, and open exercises;
- a short summary that states what the method can and cannot support.
