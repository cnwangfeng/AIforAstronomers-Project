#!/usr/bin/env python3
"""Scan LaTeX logs for release-blocking issues.

The Chinese textbook is the publication-facing entry point, so the default log
is the output produced by `bash scripts/build_book_local.sh zh`.
"""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path


DEFAULT_LOG = Path("/tmp/aifor_book_main_zh/main_zh.log")

BLOCKING_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("LaTeX error", re.compile(r"^! LaTeX Error:|LaTeX Error:", re.MULTILINE)),
    ("package error", re.compile(r"^! Package .* Error:|Package .* Error:", re.MULTILINE)),
    ("fatal stop", re.compile(r"Fatal error|Emergency stop|No pages of output")),
    ("missing dollar", re.compile(r"Missing \$ inserted")),
    ("undefined control sequence", re.compile(r"Undefined control sequence")),
    (
        "undefined reference",
        re.compile(
            r"LaTeX Warning: Reference `[^']+' .* undefined|"
            r"There were undefined references"
        ),
    ),
    (
        "undefined citation",
        re.compile(
            r"LaTeX Warning: Citation `[^']+' .* undefined|"
            r"There were undefined citations"
        ),
    ),
    ("overfull hbox", re.compile(r"Overfull \\hbox")),
]

NON_BLOCKING_PATTERNS: list[tuple[str, re.Pattern[str]]] = [
    ("underfull boxes", re.compile(r"Underfull \\[hv]box")),
    ("FontAwesome ToUnicode", re.compile(r"FontAwesome|ToUnicode CMap")),
]


def line_number(text: str, offset: int) -> int:
    return text.count("\n", 0, offset) + 1


def scan_log(log_path: Path) -> tuple[list[str], list[str]]:
    text = log_path.read_text(encoding="utf-8", errors="replace")
    problems: list[str] = []
    notes: list[str] = []

    for label, pattern in BLOCKING_PATTERNS:
        matches = list(pattern.finditer(text))
        if matches:
            first = matches[0]
            snippet = first.group(0).splitlines()[0].strip()
            problems.append(
                f"{log_path}: {label}: {len(matches)} match(es), "
                f"first at line {line_number(text, first.start())}: {snippet}"
            )

    for label, pattern in NON_BLOCKING_PATTERNS:
        count = len(pattern.findall(text))
        if count:
            notes.append(f"{log_path}: non-blocking {label}: {count}")

    return problems, notes


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Scan LaTeX logs for release-blocking warnings and errors."
    )
    parser.add_argument(
        "logs",
        nargs="*",
        type=Path,
        default=[DEFAULT_LOG],
        help=f"Log files to scan. Defaults to {DEFAULT_LOG}.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    all_problems: list[str] = []
    all_notes: list[str] = []

    for log_path in args.logs:
        if not log_path.exists():
            all_problems.append(f"{log_path}: log file not found")
            continue
        problems, notes = scan_log(log_path)
        all_problems.extend(problems)
        all_notes.extend(notes)

    for note in all_notes:
        print(note)

    if all_problems:
        print("\nLaTeX log scan failed:")
        for problem in all_problems:
            print(f"- {problem}")
        return 1

    print("LaTeX log scan passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
