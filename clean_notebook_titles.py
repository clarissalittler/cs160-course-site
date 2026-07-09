"""Replace exposed Quarto YAML in notebooks with a readable Markdown title.

Run this after ``quarto convert``. Pass notebook files or directories; directories
are searched recursively. With no arguments, the current directory is scanned.
"""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Iterable


FRONT_MATTER = re.compile(r"\A---\s*\n(?P<header>.*?)\n---\s*\n?", re.DOTALL)


def yaml_text_value(header: str, key: str) -> str | None:
    match = re.search(rf"^{re.escape(key)}:\s*(.*?)\s*$", header, re.MULTILINE)
    if match is None:
        return None

    value = match.group(1)
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        value = value[1:-1]
    return value


def notebook_paths(inputs: Iterable[Path]) -> Iterable[Path]:
    seen: set[Path] = set()
    for item in inputs:
        candidates = [item] if item.is_file() else item.rglob("*.ipynb")
        for candidate in candidates:
            if any(part.startswith(".") for part in candidate.parts):
                continue
            candidate = candidate.resolve()
            if candidate not in seen:
                seen.add(candidate)
                yield candidate


def clean_notebook(path: Path) -> bool:
    notebook = json.loads(path.read_text(encoding="utf-8"))
    cells = notebook.get("cells", [])
    if not cells or cells[0].get("cell_type") != "markdown":
        return False

    first_cell = cells[0]
    source = "".join(first_cell.get("source", []))
    match = FRONT_MATTER.match(source)
    if match is None:
        return False

    title = yaml_text_value(match.group("header"), "title")
    if title is None:
        return False

    subtitle = yaml_text_value(match.group("header"), "subtitle")
    readable_header = f"# {title}\n"
    if subtitle:
        readable_header += f"\n_{subtitle}_\n"

    body = source[match.end() :].lstrip("\n")
    first_cell["source"] = f"{readable_header}\n{body}".splitlines(keepends=True)
    path.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=2) + "\n",
        encoding="utf-8",
    )
    return True


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("paths", nargs="*", type=Path, default=[Path.cwd()])
    args = parser.parse_args()

    changed = 0
    for path in notebook_paths(args.paths):
        if clean_notebook(path):
            changed += 1
            print(f"Cleaned {path}")
    print(f"Cleaned {changed} notebook title(s).")


if __name__ == "__main__":
    main()
