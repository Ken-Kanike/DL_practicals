#!/usr/bin/env python3
"""Validate notebook JSON, Python syntax, and committed-output hygiene."""

from __future__ import annotations

import sys
from pathlib import Path

import nbformat
from nbformat.validator import ValidationError

ROOT = Path(__file__).resolve().parents[1]
NOTEBOOK_DIR = ROOT / "notebooks"


def iter_code_cells(notebook):
    for index, cell in enumerate(notebook.cells):
        if cell.cell_type == "code":
            yield index, cell


def compile_cell(source: str, filename: str) -> None:
    """Compile a code cell, replacing IPython magics with a harmless pass."""
    lines = []
    for line in source.splitlines():
        if line.lstrip().startswith(("%", "!")):
            lines.append("pass  # IPython magic or shell command")
        else:
            lines.append(line)
    compile("\n".join(lines), filename, "exec")


def main() -> int:
    notebooks = sorted(NOTEBOOK_DIR.glob("*.ipynb"))
    if not notebooks:
        print("No notebooks found yet; nothing to validate.")
        return 0

    errors: list[str] = []
    for path in notebooks:
        try:
            notebook = nbformat.read(path, as_version=4)
            nbformat.validate(notebook)
        except (ValidationError, Exception) as exc:
            errors.append(f"{path.name}: invalid notebook JSON: {exc}")
            continue

        for index, cell in iter_code_cells(notebook):
            if cell.get("outputs"):
                errors.append(
                    f"{path.name}: code cell {index} contains saved outputs; clear them before committing"
                )
            if cell.get("execution_count") is not None:
                errors.append(
                    f"{path.name}: code cell {index} has an execution count; restart and clear outputs"
                )
            try:
                compile_cell(cell.source, f"{path.name}:cell-{index}")
            except SyntaxError as exc:
                errors.append(
                    f"{path.name}: syntax error in cell {index}: {exc.msg} "
                    f"(line {exc.lineno})"
                )

    if errors:
        print("Notebook validation failed:")
        for error in errors:
            print(f"  - {error}")
        return 1

    print(f"Validated {len(notebooks)} notebook(s): JSON, syntax, and outputs are clean.")
    for path in notebooks:
        print(f"  - {path.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
