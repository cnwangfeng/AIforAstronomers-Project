#!/usr/bin/env python3
"""Clear outputs and execution counts from project notebooks."""

from __future__ import annotations

import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"


def clean_notebook(path: Path) -> bool:
    data = json.loads(path.read_text(encoding="utf-8"))
    changed = False

    for cell in data.get("cells", []):
        if cell.get("cell_type") != "code":
            continue
        if cell.get("outputs"):
            cell["outputs"] = []
            changed = True
        if cell.get("execution_count") is not None:
            cell["execution_count"] = None
            changed = True

    if changed:
        path.write_text(
            json.dumps(data, ensure_ascii=False, indent=1) + "\n",
            encoding="utf-8",
        )
    return changed


def main() -> None:
    cleaned = []
    for path in sorted(NOTEBOOK_DIR.rglob("*.ipynb")):
        if ".ipynb_checkpoints" in path.parts:
            continue
        if clean_notebook(path):
            cleaned.append(path.relative_to(ROOT))

    if cleaned:
        print("Cleaned notebooks:")
        for path in cleaned:
            print(f"  {path}")
    else:
        print("No notebook outputs found.")


if __name__ == "__main__":
    main()

