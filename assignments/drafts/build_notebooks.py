"""Build clean, Colab-ready notebooks from the accessible assignment QMD files."""

from __future__ import annotations

import json
import re
import subprocess
from pathlib import Path


ROOT = Path(__file__).resolve().parent
SOURCES = (
    "Week03_Alt_MiniZine.qmd",
    "Week03_Alt_PatternPoem.qmd",
    "Week04_Alt_QuizOracle.qmd",
    "Week04_Alt_BranchingRadioPlay.qmd",
)


def front_matter_value(source: str, key: str) -> str:
    match = re.search(rf"^{key}:\s*[\"']?(.*?)[\"']?\s*$", source, re.MULTILINE)
    if match is None:
        raise ValueError(f"Missing {key!r} in QMD front matter")
    return match.group(1)


for source_name in SOURCES:
    subprocess.run(
        ["quarto", "convert", source_name],
        cwd=ROOT,
        check=True,
    )

    notebook_path = ROOT / Path(source_name).with_suffix(".ipynb")
    notebook = json.loads(notebook_path.read_text(encoding="utf-8"))
    first_cell = notebook["cells"][0]
    first_source = "".join(first_cell["source"])

    title = front_matter_value(first_source, "title")
    subtitle = front_matter_value(first_source, "subtitle")
    body = re.sub(r"\A---\s*\n.*?\n---\s*\n", "", first_source, count=1, flags=re.DOTALL)
    first_cell["source"] = f"# {title}\n\n_{subtitle}_\n\n{body}".splitlines(keepends=True)

    notebook_path.write_text(
        json.dumps(notebook, ensure_ascii=False, indent=1) + "\n",
        encoding="utf-8",
    )
    print(f"Built {notebook_path.name}")
