#!/usr/bin/env python3
"""Check release-facing README inventories against files on disk.

This intentionally avoids third-party dependencies so it can run in the same
minimal environment as the notebook smoke tests.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def mentioned_files(readme: Path, suffix: str) -> set[str]:
    text = readme.read_text(encoding="utf-8")
    matches = re.findall(r"`([^`]+\." + re.escape(suffix) + r")`", text)
    # Ignore cross-references such as `book/main_zh.tex`; inventory bullets use
    # local file names.
    return {match for match in matches if "/" not in match}


def actual_files(directory: Path, suffix: str) -> set[str]:
    return {path.name for path in directory.glob(f"*.{suffix}")}


def check_inventory(label: str, readme: Path, directory: Path, suffix: str) -> list[str]:
    actual = actual_files(directory, suffix)
    mentioned = mentioned_files(readme, suffix)
    missing = sorted(actual - mentioned)
    extra = sorted(mentioned - actual)
    problems: list[str] = []
    if missing:
        problems.append(f"{label}: missing from README: {', '.join(missing)}")
    if extra:
        problems.append(f"{label}: listed but absent: {', '.join(extra)}")
    print(
        f"{label}: actual={len(actual)} mentioned={len(mentioned)} "
        f"missing={len(missing)} extra={len(extra)}"
    )
    return problems


def check_manifest_paths() -> list[str]:
    manifest = (ROOT / "data/manifest.yml").read_text(encoding="utf-8")
    manifest_paths = {
        match.strip()
        for match in re.findall(r"path:\s+(data/small/[^\n]+)", manifest)
    }
    actual_paths = {
        str(path.relative_to(ROOT))
        for path in (ROOT / "data/small").glob("*.csv")
    }
    missing = sorted(actual_paths - manifest_paths)
    extra = sorted(manifest_paths - actual_paths)
    problems: list[str] = []
    if missing:
        problems.append(f"data manifest: missing paths: {', '.join(missing)}")
    if extra:
        problems.append(f"data manifest: paths without files: {', '.join(extra)}")
    print(
        f"data manifest: actual={len(actual_paths)} manifest={len(manifest_paths)} "
        f"missing={len(missing)} extra={len(extra)}"
    )
    return problems


def main() -> int:
    checks: list[tuple[str, Path, Path, str]] = []

    for readme in sorted((ROOT / "book/chapters").glob("part*/README.md")):
        checks.append((
            f"book chapters {readme.parent.name}",
            readme,
            readme.parent,
            "tex",
        ))

    for readme in sorted((ROOT / "notebooks").glob("part*/README.md")):
        checks.append((
            f"notebooks {readme.parent.name}",
            readme,
            readme.parent,
            "ipynb",
        ))

    checks.append((
        "small data README",
        ROOT / "data/small/README.md",
        ROOT / "data/small",
        "csv",
    ))

    problems: list[str] = []
    for label, readme, directory, suffix in checks:
        problems.extend(check_inventory(label, readme, directory, suffix))
    problems.extend(check_manifest_paths())

    if problems:
        print("\nRelease inventory check failed:")
        for problem in problems:
            print(f"- {problem}")
        return 1

    print("\nRelease inventory check passed")
    return 0


if __name__ == "__main__":
    sys.exit(main())
