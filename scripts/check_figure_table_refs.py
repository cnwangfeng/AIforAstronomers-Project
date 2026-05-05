#!/usr/bin/env python3
"""Check active textbook figure/table captions, labels, and references."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEX_PATHS = [ROOT / "book/main_zh.tex", *sorted((ROOT / "book/chapters").rglob("*.tex"))]

CAPTION_RE = re.compile(r"\\caption(?:\[[^\]]*\])?\{")
LABEL_RE = re.compile(r"\\label\{([^}]+)\}")
REF_RE = re.compile(r"\\(?:ref|pageref|autoref)\{([^}]+)\}")


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def scan_float_envs(path: Path, text: str) -> tuple[int, int, list[str]]:
    figure_count = 0
    table_count = 0
    problems: list[str] = []

    for env_name in ("figure", "table"):
        begin = f"\\begin{{{env_name}}}"
        end_marker = f"\\end{{{env_name}}}"
        pos = 0

        while True:
            start = text.find(begin, pos)
            if start == -1:
                break

            end = text.find(end_marker, start)
            if end == -1:
                problems.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, start)}: "
                    f"{env_name} environment has no closing {end_marker}"
                )
                pos = start + len(begin)
                continue

            block = text[start : end + len(end_marker)]
            if env_name == "figure":
                figure_count += 1
            else:
                table_count += 1

            if not CAPTION_RE.search(block):
                problems.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, start)}: "
                    f"{env_name} environment has no caption"
                )
            if not LABEL_RE.search(block):
                problems.append(
                    f"{path.relative_to(ROOT)}:{line_number(text, start)}: "
                    f"{env_name} environment has no label"
                )

            pos = end + len(end_marker)

    return figure_count, table_count, problems


def main() -> int:
    figure_count = 0
    table_count = 0
    caption_count = 0
    labels: list[tuple[Path, str]] = []
    refs: list[tuple[Path, str]] = []
    problems: list[str] = []

    for path in TEX_PATHS:
        text = path.read_text(encoding="utf-8")
        figures, tables, env_problems = scan_float_envs(path, text)
        figure_count += figures
        table_count += tables
        caption_count += len(CAPTION_RE.findall(text))
        labels.extend((path, match.group(1)) for match in LABEL_RE.finditer(text))
        refs.extend((path, match.group(1)) for match in REF_RE.finditer(text))
        problems.extend(env_problems)

    label_names = [label for _, label in labels]
    ref_names = {ref for _, ref in refs}
    label_set = set(label_names)

    duplicate_labels = sorted(
        label for label in label_set if label_names.count(label) > 1
    )
    unreferenced_labels = sorted(label_set - ref_names)
    undefined_refs = sorted(ref_names - label_set)

    if duplicate_labels:
        problems.append(f"duplicate labels: {', '.join(duplicate_labels)}")
    if unreferenced_labels:
        problems.append(f"labels without a text reference: {', '.join(unreferenced_labels)}")
    if undefined_refs:
        problems.append(f"references without a label: {', '.join(undefined_refs)}")

    print(
        "figure/table refs: "
        f"figures={figure_count} tables={table_count} "
        f"captions={caption_count} labels={len(labels)} "
        f"unique_labels={len(label_set)} refs={len(refs)}"
    )

    if problems:
        print("\nFigure/table reference check failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Figure/table reference check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
