#!/usr/bin/env python3
"""Validate that data manifest entries reference real files and notebooks."""

from __future__ import annotations

from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "data" / "manifest.yml"


def parse_manifest_fallback(text: str) -> list[dict[str, object]]:
    datasets: list[dict[str, object]] = []
    current: dict[str, object] | None = None
    in_used_by = False

    for raw_line in text.splitlines():
        line = raw_line.rstrip()
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        if line.startswith("  - name:"):
            current = {"name": stripped.split(":", 1)[1].strip(), "used_by": []}
            datasets.append(current)
            in_used_by = False
            continue

        if current is None:
            continue

        if line.startswith("    path:"):
            current["path"] = stripped.split(":", 1)[1].strip()
            in_used_by = False
            continue

        if line.startswith("    used_by:"):
            in_used_by = True
            continue

        if in_used_by and line.startswith("      - "):
            used_by = current.setdefault("used_by", [])
            assert isinstance(used_by, list)
            used_by.append(stripped[2:].strip())
            continue

        if line.startswith("    ") and not line.startswith("      - "):
            in_used_by = False

    return datasets


def load_manifest() -> list[dict[str, object]]:
    text = MANIFEST_PATH.read_text(encoding="utf-8")

    try:
        import yaml  # type: ignore
    except ModuleNotFoundError:
        return parse_manifest_fallback(text)

    manifest = yaml.safe_load(text) or {}
    return manifest.get("datasets", [])


def main() -> None:
    datasets = load_manifest()
    failures: list[str] = []

    for dataset in datasets:
        name = dataset.get("name", "<unnamed>")
        data_path = ROOT / dataset.get("path", "")
        if not data_path.is_file():
            failures.append(f"{name}: missing data file {data_path.relative_to(ROOT)}")

        for notebook_path in dataset.get("used_by", []):
            path = ROOT / notebook_path
            if not path.is_file():
                failures.append(f"{name}: missing notebook {path.relative_to(ROOT)}")

    if failures:
        for failure in failures:
            print(f"FAIL {failure}")
        raise SystemExit(1)

    print(f"Validated data manifest: {len(datasets)} datasets")


if __name__ == "__main__":
    main()
