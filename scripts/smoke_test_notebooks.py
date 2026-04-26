#!/usr/bin/env python3
"""Execute notebook code cells as a lightweight smoke test."""

from __future__ import annotations

import json
import os
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_ROOT = ROOT / "notebooks"


def iter_notebooks() -> list[Path]:
    return sorted(
        path for path in NOTEBOOK_ROOT.rglob("*.ipynb")
        if ".ipynb_checkpoints" not in path.parts
    )


def run_notebook(path: Path) -> None:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    namespace = {"__name__": "__main__"}
    old_cwd = Path.cwd()
    os.chdir(path.parent)
    try:
        for index, cell in enumerate(notebook.get("cells", []), start=1):
            if cell.get("cell_type") != "code":
                continue
            source = "".join(cell.get("source", []))
            if not source.strip():
                continue
            code = compile(source, f"{path.name}:cell-{index}", "exec")
            exec(code, namespace, namespace)
    finally:
        os.chdir(old_cwd)


def main() -> None:
    notebooks = iter_notebooks()
    failures: list[tuple[Path, Exception]] = []

    for path in notebooks:
        try:
            run_notebook(path)
            print(f"PASS {path.relative_to(ROOT)}")
        except Exception as exc:  # noqa: BLE001
            failures.append((path, exc))
            print(f"FAIL {path.relative_to(ROOT)}: {exc}")

    if failures:
        raise SystemExit(1)

    print(f"All notebook smoke tests passed: {len(notebooks)} notebooks")


if __name__ == "__main__":
    main()
