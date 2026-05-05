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

All active textbook writing now happens inside this tree. The legacy top-level
chapter files under `book/` and the old `main.tex` compatibility entry have
been removed, so new revisions should target `book/main_zh.tex` and this
chapter tree only.

When adding or revising a chapter, keep it aligned with the current pattern:

- learning goals and scientific motivation;
- a training goal or micro-project / record when the chapter has a paired workflow;
- conceptual explanation before code details;
- a clear connection to the paired notebook and teaching data;
- common pitfalls or failure modes;
- basic, advanced, and open exercises;
- a short summary that states what the method can and cannot support.
