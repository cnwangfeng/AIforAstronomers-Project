# Course Package Release Notes

Version date: `2026-05-04`

This note summarizes the current release-ready state of the teaching package in
`AIforAstronomers-Project/`.

## Current Scope

- Chinese textbook title: `面向天文与物理本科生的 AI 科研实战`
- English subtitle: `Practical AI for Astronomy and Physics`
- Main Chinese entry: `book/main_zh.tex`
- Current Chinese PDF output: `/tmp/aifor_book_main_zh/main_zh.pdf`
- Current verified Chinese page count: about `507` pages
- Notebook smoke-test status: `59` notebooks passed
- Data manifest status: `52` datasets validated
- `Part VI` status: `ch39` to `ch59` completed as a continuous capstone package
- Capstone evidence frame: eight shared cards from project definition to
  integrity signoff, with Part VI gate/route language aligned across scoring,
  release, handoff, and maintenance chapters

## Audience Entry Points

- Students:
  - `book/chapters/part6/ch44_capstone_course_calendar_milestones.tex`
  - `book/chapters/part6/ch45_capstone_student_handout_ta_guide.tex`
  - `notebooks/part6_capstone/ch39_capstone_project_workflow.ipynb`
- Teaching assistants:
  - `book/chapters/part6/ch42_capstone_case_template_rubric.tex`
  - `book/chapters/part6/ch45_capstone_student_handout_ta_guide.tex`
  - `book/chapters/part6/ch47_capstone_instructor_handoff.tex`
- Instructors and course maintainers:
  - `book/chapters/part6/ch47_capstone_instructor_handoff.tex`
  - `book/chapters/part6/ch51_capstone_final_package_closure.tex`
  - `book/chapters/part6/ch52_capstone_course_package_directory_release_notes.tex`
  - `book/chapters/part6/ch53_capstone_semester_reboot_preflight.tex`
  - `book/chapters/part6/ch54_capstone_failure_modes_escalation_playbook.tex`
  - `book/chapters/part6/ch55_capstone_contingency_substitute_handoff.tex`
  - `book/chapters/part6/ch56_capstone_shutdown_warmstart.tex`
  - `book/chapters/part6/ch57_capstone_alumni_mentor_relay.tex`
  - `book/chapters/part6/ch58_capstone_community_memory_maintenance_ledger.tex`
  - `book/chapters/part6/ch59_capstone_external_collaboration_guest_intake.tex`
- Public adopters:
  - `book/chapters/part6/ch48_capstone_public_release_maintenance.tex`
  - `book/chapters/part6/ch49_capstone_launch_qa_adoption.tex`
  - `book/chapters/part6/ch52_capstone_course_package_directory_release_notes.tex`

## Verified Commands

Run from repo root:

```bash
python scripts/validate_data_manifest.py
python scripts/check_release_inventory.py
python scripts/smoke_test_notebooks.py
bash scripts/build_book_local.sh main
bash scripts/build_book_local.sh zh
git diff --check
```

Most recent verified state:

- `validate_data_manifest.py`: passed
- `check_release_inventory.py`: passed
- `smoke_test_notebooks.py`: passed (`59` notebooks)
- `build_book_local.sh main`: passed, output `/tmp/aifor_book_main/main.pdf`
- `build_book_local.sh zh`: passed, output `/tmp/aifor_book_main_zh/main_zh.pdf` (`507` pages)
- `git diff --check`: passed
- LaTeX error scan: no `Overfull`, undefined references, `Missing $`, or fatal errors detected in `/tmp/aifor_book_main_zh/main_zh.log`

## Non-Blocking Known Issues

- Chinese build still shows scattered `Underfull \vbox` / `Underfull \hbox`
  warnings in a few chapters.
- `FontAwesome` `ToUnicode CMap` warnings still appear during `xdvipdfmx`.
- These warnings do not currently block PDF generation.

## Release Package Components

- Textbook source: `book/`
- Figure/table QA inventory: `book/FIGURE_TABLE_QA.md`
- Evidence-card QA inventory: `book/EVIDENCE_CARD_QA.md`
- Formula QA inventory: `book/FORMULA_QA.md`
- Source/license QA inventory: `book/SOURCE_LICENSE_QA.md`
- Capstone notebooks: `notebooks/part6_capstone/`
- Small teaching datasets: `data/small/`
- Data registry: `data/manifest.yml`
- Recovery and project state: `Roadmap.md`
- Publication decision tracker: `PUBLICATION_DECISIONS.md`
- Overleaf sync helper: `scripts/sync_book_to_overleaf.sh`

## Immediate Polish Queue

- Continue from `book/FIGURE_TABLE_QA.md`, `book/EVIDENCE_CARD_QA.md`, and
  `book/FORMULA_QA.md`; use `book/SOURCE_LICENSE_QA.md` for bibliography,
  source/license, attribution, and AI-use release decisions. Current
  figure/table labels already have正文 `\ref{...}` entries.
- Reader QA from Part I/II outward is no longer a blank sweep; use targeted
  reader feedback or the QA inventories above to decide the next polish patch.
- Keep Part VI in compression mode only; no new operational chapters are
  planned for the current version.
- Do one controlled `sync_book_to_overleaf.sh` dry-run and, after confirmation,
  one `--apply` cycle when ready to publish the current book state.
