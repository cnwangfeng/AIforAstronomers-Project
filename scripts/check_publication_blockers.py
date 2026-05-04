#!/usr/bin/env python3
"""Report publication blockers without making project-level decisions.

By default this script is informational and exits successfully. Use
`--strict` for the final publication gate, after license, attribution,
citation, bibliography, and AI-use decisions have been made.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
PLACEHOLDER_LICENSE = "verify final project-wide license before publication"


@dataclass(frozen=True)
class CheckResult:
    label: str
    ok: bool
    detail: str


def first_existing(paths: list[Path]) -> Path | None:
    return next((path for path in paths if path.exists()), None)


def count_bib_entries(path: Path) -> int:
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace")
    return len(re.findall(r"@\w+\s*{", text))


def count_data_license_placeholders(path: Path) -> int:
    if not path.exists():
        return 0
    text = path.read_text(encoding="utf-8", errors="replace").lower()
    return text.count(PLACEHOLDER_LICENSE)


def count_includegraphics() -> int:
    tex_files = list((ROOT / "book").glob("*.tex"))
    tex_files.extend((ROOT / "book/chapters").glob("**/*.tex"))
    total = 0
    for tex_file in tex_files:
        text = tex_file.read_text(encoding="utf-8", errors="replace")
        total += len(re.findall(r"\\includegraphics(?:\[[^\]]*\])?{", text))
    return total


def main_zh_text() -> str:
    path = ROOT / "book/main_zh.tex"
    if not path.exists():
        return ""
    return path.read_text(encoding="utf-8", errors="replace")


def build_results() -> list[CheckResult]:
    main_text = main_zh_text()
    bib_entries = count_bib_entries(ROOT / "book/references.bib")
    placeholder_count = count_data_license_placeholders(ROOT / "data/manifest.yml")
    includegraphics_count = count_includegraphics()

    license_file = first_existing([
        ROOT / "LICENSE",
        ROOT / "LICENSE.md",
        ROOT / "LICENSE.txt",
    ])
    notice_file = first_existing([
        ROOT / "NOTICE",
        ROOT / "NOTICE.md",
        ROOT / "ATTRIBUTION",
        ROOT / "ATTRIBUTION.md",
    ])
    citation_file = first_existing([
        ROOT / "CITATION.cff",
        ROOT / "CITATION.md",
    ])
    ai_use_file = first_existing([
        ROOT / "AI_USE_STATEMENT.md",
        ROOT / "AI_USE.md",
        ROOT / "PROJECT_AI_USE.md",
    ])

    has_bibliography_hook = bool(
        re.search(r"\\bibliography{|\\addbibresource{|\\printbibliography", main_text)
    )
    has_cites = bool(
        re.search(r"\\cite[a-zA-Z*]*{", main_text) or re.search(r"\\nocite{", main_text)
    )

    return [
        CheckResult(
            "publication decision tracker",
            (ROOT / "PUBLICATION_DECISIONS.md").exists(),
            "PUBLICATION_DECISIONS.md exists"
            if (ROOT / "PUBLICATION_DECISIONS.md").exists()
            else "PUBLICATION_DECISIONS.md is missing",
        ),
        CheckResult(
            "top-level license",
            license_file is not None,
            str(license_file.relative_to(ROOT))
            if license_file
            else "missing LICENSE / LICENSE.md / LICENSE.txt",
        ),
        CheckResult(
            "notice or attribution",
            notice_file is not None,
            str(notice_file.relative_to(ROOT))
            if notice_file
            else "missing NOTICE / NOTICE.md / ATTRIBUTION.md",
        ),
        CheckResult(
            "citation file",
            citation_file is not None,
            str(citation_file.relative_to(ROOT))
            if citation_file
            else "missing CITATION.cff / CITATION.md",
        ),
        CheckResult(
            "project-level AI-use statement",
            ai_use_file is not None,
            str(ai_use_file.relative_to(ROOT))
            if ai_use_file
            else "missing AI_USE_STATEMENT.md / AI_USE.md / PROJECT_AI_USE.md",
        ),
        CheckResult(
            "data license placeholders",
            placeholder_count == 0,
            f"{placeholder_count} placeholder license field(s) remain in data/manifest.yml",
        ),
        CheckResult(
            "bibliography entries",
            bib_entries > 0,
            f"book/references.bib contains {bib_entries} entr(y/ies)",
        ),
        CheckResult(
            "Chinese bibliography hook",
            has_bibliography_hook,
            "book/main_zh.tex has bibliography hook"
            if has_bibliography_hook
            else "book/main_zh.tex has no bibliography hook",
        ),
        CheckResult(
            "Chinese citation commands",
            has_cites,
            "book/main_zh.tex uses citation commands"
            if has_cites
            else "book/main_zh.tex has no citation commands",
        ),
        CheckResult(
            "external image scan",
            True,
            f"found {includegraphics_count} includegraphics command(s) in book tex files",
        ),
    ]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Report publication blockers for license, citation, and AI-use release decisions."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="Exit non-zero if any blocker is still open.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    results = build_results()
    blockers = [result for result in results if not result.ok]

    print("Publication blocker report")
    for result in results:
        status = "OK" if result.ok else "OPEN"
        print(f"[{status}] {result.label}: {result.detail}")

    print(f"\nOpen publication blocker(s): {len(blockers)}")
    if blockers:
        print("These are expected until PUBLICATION_DECISIONS.md is resolved.")

    if args.strict and blockers:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
