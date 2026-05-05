#!/usr/bin/env python3
"""Check the active Chinese textbook formula inventory."""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MAIN = ROOT / "book/main_zh.tex"
TEX_PATHS = [MAIN, *sorted((ROOT / "book/chapters").rglob("*.tex"))]

DISPLAY_OPEN_RE = re.compile(r"\\\[")
DISPLAY_CLOSE_RE = re.compile(r"\\\]")
NUMBERED_ENV_RE = re.compile(r"\\begin\{(equation\*?|align\*?|displaymath)\}")


def main() -> int:
    main_text = MAIN.read_text(encoding="utf-8")
    all_text = "\n".join(path.read_text(encoding="utf-8") for path in TEX_PATHS)

    include_count = len(re.findall(r"\\include\{", main_text))
    display_open_count = len(DISPLAY_OPEN_RE.findall(all_text))
    display_close_count = len(DISPLAY_CLOSE_RE.findall(all_text))
    numbered_envs = NUMBERED_ENV_RE.findall(all_text)

    problems: list[str] = []
    if display_open_count != display_close_count:
        problems.append(
            f"display math delimiters are unbalanced: "
            f"open={display_open_count} close={display_close_count}"
        )
    if numbered_envs:
        env_summary = ", ".join(sorted(set(numbered_envs)))
        problems.append(
            "numbered or environment-style display math is present; "
            f"update FORMULA_QA.md if intentional: {env_summary}"
        )

    print(
        "formula inventory: "
        f"includes={include_count} display_math_blocks={display_open_count} "
        f"numbered_formula_envs={len(numbered_envs)}"
    )

    if problems:
        print("\nFormula inventory check failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("Formula inventory check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
