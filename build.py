#!/usr/bin/env python3
"""
Markdown → D2L-style HTML converter for CS 160 course site.

Converts revised markdown lessons back into HTML that matches the original
D2L export structure, suitable for local browsing and copy-pasting back
into D2L's HTML editor.

Usage:
    python build.py                    # Build all units
    python build.py unit3              # Build just unit 3
    python build.py unit5 unit6        # Build units 5 and 6
    python build.py --clean            # Remove all generated HTML
    python build.py --list             # List what would be built
"""

import argparse
import html
import os
import re
import sys
from pathlib import Path

# ── Configuration ────────────────────────────────────────────────────────────

SITE_ROOT = Path(__file__).parent

UNIT_DIRS = {
    "unit1": "unit1/unit-01-digital-information",
    "unit2": "unit2/unit-02-internet",
    "unit3": "unit3/unit-03-python-introduction",
    "unit4": "unit4/unit-04-python-selection",
    "unit5": "unit5/unit-05-python-iteration",
    "unit6": "unit6/unit-06-python-arrays",
    "unit7": "unit7/unit-07-Algorithms and Algorithm Efficiency",
    "unit8": "unit8/unit-08-data",
    "unit9": "unit9/unit-09-artificial-intelligence",
    "unit10": "unit10/unit-10-cybersecurity",
}

# CSS depth from each unit's revised/ dir to site root
CSS_PATH = "../../../local-styles.css"


# ── Lesson Ordering ─────────────────────────────────────────────────────────

def lesson_sort_key(filename: str) -> tuple:
    """Sort key for ordering lessons within a unit.

    Order: Overview (0) → Numbered lessons (1) → Supplements (2) → Summary (3)
    """
    stem = Path(filename).stem
    lower = stem.lower()

    if lower == "overview":
        return (0, 0, "")

    m = re.match(r"lesson\s+(\d+)", lower)
    if m:
        return (1, int(m.group(1)), "")

    if lower == "summary" or ("unit" in lower and "summary" in lower):
        return (3, 0, "")

    # Supplementary material, sorted alphabetically
    return (2, 0, stem)


def collect_all_lessons() -> list[dict]:
    """Build a global ordered list of all lessons across all units."""
    all_lessons = []

    for unit_key in sorted(UNIT_DIRS.keys(), key=lambda k: int(k.replace("unit", ""))):
        unit_rel = UNIT_DIRS[unit_key]
        revised_dir = SITE_ROOT / unit_rel / "revised"
        if not revised_dir.exists():
            continue

        md_files = sorted(revised_dir.glob("*.md"), key=lambda f: lesson_sort_key(f.name))

        for md_file in md_files:
            html_name = md_file.with_suffix(".html").name
            html_file = revised_dir / "html" / html_name
            html_rel = os.path.relpath(html_file, SITE_ROOT)
            all_lessons.append({
                "unit_key": unit_key,
                "unit_rel": unit_rel,
                "md_file": md_file,
                "html_file": html_file,
                "html_rel": html_rel,
            })

    return all_lessons


# ── HTML Template ────────────────────────────────────────────────────────────

HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <link rel="stylesheet" href="{css_path}">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/styles/github.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/highlight.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/highlight.js/11.9.0/languages/python.min.js"></script>
    <script>hljs.highlightAll();</script>
    <title>{title} - PCC CS 160</title>
    <style>
        /* D2L-style colored boxes */
        .box {{
            padding: 1rem 1.25rem;
            margin: 1rem 0;
            border-radius: 6px;
        }}
        .blue-box {{
            background-color: #dce8f5;
            border-left: 4px solid #2d4b73;
        }}
        .red-box {{
            background-color: #fde8e8;
            border-left: 4px solid #c0392b;
        }}
        .green-box, .green2-box {{
            background-color: #e4f2b2;
            border-left: 4px solid #5a8a2a;
        }}
        .gray-box {{
            background-color: #e8e9e9;
            border-left: 4px solid #666;
        }}
        .info-box {{
            background-color: #e8f4fd;
            border-left: 4px solid #2563eb;
        }}
        .important-box {{
            background-color: #fff3cd;
            border-left: 4px solid #d4a017;
        }}
        /* Video embed container */
        .video-container {{
            text-align: center;
            margin: 1rem 0;
        }}
        .video-container iframe {{
            max-width: 100%;
            border-radius: 4px;
        }}
        .video-text {{
            color: #1c507e;
            font-size: 0.9rem;
            margin-top: 0.25rem;
            text-align: center;
        }}
        /* LMS placeholder */
        .lms-placeholder {{
            background: #f0f0f0;
            border: 2px dashed #aaa;
            padding: 0.75rem 1rem;
            margin: 1rem 0;
            border-radius: 4px;
            color: #666;
            font-style: italic;
        }}
        /* Python Tutor link */
        .pythontutor-link {{
            display: block;
            background: #e8f4fd;
            border: 1px solid #b3d4fc;
            padding: 0.75rem 1rem;
            margin: 1rem 0;
            border-radius: 4px;
            text-align: center;
        }}
        /* Figure captions */
        figcaption, .fig-caption {{
            color: #1c507e;
            font-size: 0.9rem;
            border-bottom: none;
            margin-top: 0.25rem;
        }}
        /* Details/summary styling */
        details {{
            margin: 0.75rem 0;
            padding: 0.5rem;
            border: 1px solid #ddd;
            border-radius: 4px;
        }}
        details summary {{
            cursor: pointer;
            font-weight: bold;
            padding: 0.25rem 0;
        }}
        details[open] summary {{
            margin-bottom: 0.5rem;
        }}
        /* Banner */
        .banner-img img {{
            width: 100%;
            max-height: 200px;
            object-fit: cover;
            border-radius: 8px;
            margin-bottom: 0.5rem;
        }}
        /* Blockquote styling for callout boxes */
        blockquote {{
            margin: 1rem 0;
            padding: 0;
            border: none;
        }}
    </style>
</head>
<body>
<div class="container-fluid">
<div class="row">
<div class="col-sm-10 offset-sm-1">
{body}
</div>
<div class="col-12">
<footer>
<p>End of {title}</p>
</footer>
</div>
</div>
</div>
{extra_scripts}
</body>
</html>"""


# ── Markdown → HTML Conversion ──────────────────────────────────────────────

def convert_md_to_html(md_text: str) -> tuple[str, str]:
    """Convert markdown text to D2L-style HTML body. Returns (title, body_html)."""

    lines = md_text.split("\n")
    title = ""
    body_parts = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Skip banner images (we handle them in the template if needed)
        if line.startswith("![") and "banner" in line.lower():
            i += 1
            continue

        # H1 — extract title
        if line.startswith("# "):
            title = line[2:].strip()
            # Convert --- back to – for display, or keep as-is
            display_title = title.replace(" --- ", " — ")
            body_parts.append(f"<h1>{escape(display_title)}</h1>")
            i += 1
            continue

        # Horizontal rule
        if line.strip() == "---" and (i == 0 or lines[i-1].strip() == ""):
            body_parts.append("<hr>")
            i += 1
            continue

        # Fenced code block
        if line.strip().startswith("```"):
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_text = html.escape("\n".join(code_lines))
            lang_attr = f' class="language-{lang}"' if lang else ""
            body_parts.append(
                f'<pre><code{lang_attr}>{code_text}</code></pre>'
            )
            continue

        # HTML details/summary blocks — convert markdown inside them
        if line.strip().startswith("<details"):
            details_lines = [line]
            i += 1
            # Collect summary tag
            while i < len(lines) and "</summary>" not in "\n".join(details_lines):
                details_lines.append(lines[i])
                i += 1
            # Now collect the body content until </details>
            inner_md_lines = []
            while i < len(lines) and "</details>" not in lines[i]:
                inner_md_lines.append(lines[i])
                i += 1
            # Grab closing tag
            closing = ""
            if i < len(lines):
                closing = lines[i]
                i += 1
            # Convert the inner content as markdown
            inner_md = "\n".join(inner_md_lines)
            _, inner_html = convert_md_to_html(inner_md)
            # Rebuild: details open + summary, converted body, details close
            body_parts.append("\n".join(details_lines))
            body_parts.append(inner_html)
            body_parts.append(closing)
            continue

        # Blockquote — detect type and convert to colored box
        if line.startswith(">"):
            bq_lines = []
            while i < len(lines) and (lines[i].startswith(">") or
                                       (lines[i].strip() == "" and
                                        i + 1 < len(lines) and
                                        lines[i + 1].startswith(">"))):
                # Strip leading > and at most one space (preserve indentation)
                stripped = lines[i].lstrip(">")
                if stripped.startswith(" "):
                    stripped = stripped[1:]
                bq_lines.append(stripped)
                i += 1

            bq_text = "\n".join(bq_lines).strip()
            box_class = classify_blockquote(bq_text)
            bq_html = convert_inline_block(bq_text)
            body_parts.append(f'<div class="box {box_class}">\n{bq_html}\n</div>')
            continue

        # H2
        if line.startswith("## "):
            body_parts.append(f"<h2>{convert_inline(line[3:].strip())}</h2>")
            i += 1
            continue

        # H3
        if line.startswith("### "):
            body_parts.append(f"<h3>{convert_inline(line[4:].strip())}</h3>")
            i += 1
            continue

        # H4
        if line.startswith("#### "):
            body_parts.append(f"<h4>{convert_inline(line[5:].strip())}</h4>")
            i += 1
            continue

        # Unordered list
        if line.strip().startswith("- ") or line.strip().startswith("* "):
            list_items, i = collect_list(lines, i, unordered=True)
            body_parts.append(render_list(list_items, ordered=False))
            continue

        # Ordered list
        if re.match(r"^\s*\d+\.\s", line):
            list_items, i = collect_list(lines, i, unordered=False)
            body_parts.append(render_list(list_items, ordered=True))
            continue

        # Table
        if "|" in line and i + 1 < len(lines) and re.match(r"^\s*\|[-:|]+\|", lines[i + 1]):
            table_lines = []
            while i < len(lines) and "|" in lines[i]:
                table_lines.append(lines[i])
                i += 1
            body_parts.append(convert_table(table_lines))
            continue

        # Image
        img_match = re.match(r"^!\[([^\]]*)\]\(([^)]+)\)", line.strip())
        if img_match:
            alt, src = img_match.group(1), img_match.group(2)
            body_parts.append(
                f'<figure><img src="{escape(src)}" alt="{escape(alt)}" '
                f'style="max-width: 100%;">'
            )
            # Check for italic caption on next line
            if i + 1 < len(lines) and lines[i + 1].strip().startswith("*") and lines[i + 1].strip().endswith("*"):
                caption = lines[i + 1].strip().strip("*")
                body_parts.append(f'<figcaption>{escape(caption)}</figcaption>')
                i += 2
            else:
                i += 1
            body_parts.append("</figure>")
            continue

        # Video link → YouTube embed
        video_match = re.match(
            r"^\[Video:\s*(.+?)\]\(https?://(?:www\.)?youtube\.com/watch\?v=([a-zA-Z0-9_-]+)\)",
            line.strip()
        )
        if video_match:
            vtitle, vid = video_match.group(1), video_match.group(2)
            body_parts.append(
                f'<div class="video-container">'
                f'<iframe title="{escape(vtitle)}" width="560" height="315" '
                f'src="https://www.youtube.com/embed/{vid}?rel=0" '
                f'allow="accelerometer; autoplay; clipboard-write; encrypted-media; '
                f'gyroscope; picture-in-picture" allowfullscreen></iframe>\n'
                f'<div class="video-text">{escape(vtitle)}</div></div>'
            )
            i += 1
            continue

        # Python Tutor link → embedded iframe or styled link
        pt_match = re.match(r"^\[Python Tutor:\s*(.+?)\]\((.+?)\)", line.strip())
        if pt_match:
            pt_title, pt_url = pt_match.group(1), pt_match.group(2)
            body_parts.append(
                f'<div class="video-container">'
                f'<iframe title="{escape(pt_title)}" width="1000" height="400" '
                f'frameborder="0" src="{escape(pt_url)}"></iframe></div>'
            )
            i += 1
            continue

        # Animation link
        anim_match = re.match(r"^\[Animation:\s*(.+?)\]\((.+?)\)", line.strip())
        if anim_match:
            a_title, a_url = anim_match.group(1), anim_match.group(2)
            body_parts.append(
                f'<div class="video-container">'
                f'<iframe title="{escape(a_title)}" width="800" height="400" '
                f'frameborder="0" src="{escape(a_url)}"></iframe></div>'
            )
            i += 1
            continue

        # LMS Activity placeholder
        lms_match = re.match(r"^\[LMS Activity:\s*(.+?)\]", line.strip())
        if lms_match:
            lms_desc = lms_match.group(1)
            body_parts.append(
                f'<div class="lms-placeholder">&#x1f517; LMS Activity: {escape(lms_desc)}'
                f'<br><small>(Link to be configured in D2L)</small></div>'
            )
            i += 1
            continue

        # Regular paragraph (or empty line)
        if line.strip() == "":
            i += 1
            continue

        # Collect paragraph lines
        para_lines = []
        while i < len(lines) and lines[i].strip() != "" and not is_block_start(lines[i]):
            para_lines.append(lines[i])
            i += 1

        if para_lines:
            para_text = " ".join(l.strip() for l in para_lines)
            body_parts.append(f"<p>{convert_inline(para_text)}</p>")

    return title, "\n".join(body_parts)


def is_block_start(line: str) -> bool:
    """Check if a line starts a new block element."""
    s = line.strip()
    if s.startswith("#"):
        return True
    if s.startswith("```"):
        return True
    if s.startswith(">"):
        return True
    if s.startswith("- ") or s.startswith("* "):
        return True
    if re.match(r"^\d+\.\s", s):
        return True
    if s.startswith("!["):
        return True
    if s.startswith("[Video:") or s.startswith("[Python Tutor:") or s.startswith("[LMS Activity:") or s.startswith("[Animation:"):
        return True
    if s.startswith("<details"):
        return True
    if s == "---":
        return True
    if "|" in s and s.startswith("|"):
        return True
    return False


def escape(text: str) -> str:
    """HTML-escape text."""
    return html.escape(text, quote=True)


def convert_inline(text: str) -> str:
    """Convert inline markdown to HTML.

    Strategy: replace code spans with placeholders first, then apply
    bold/italic/link conversion on the whole text (so markers that wrap
    code spans work correctly), then restore placeholders.
    """
    placeholders = {}
    counter = [0]

    def _ph(html_str: str) -> str:
        key = f"\x00PH{counter[0]}\x00"
        counter[0] += 1
        placeholders[key] = html_str
        return key

    # Replace code spans (decorated first, then plain) with placeholders
    text = re.sub(
        r"\*\*\*`([^`]+)`\*\*\*",
        lambda m: _ph(f'<strong><em><code>{html.escape(m.group(1))}</code></em></strong>'),
        text,
    )
    text = re.sub(
        r"\*\*`([^`]+)`\*\*",
        lambda m: _ph(f'<strong><code>{html.escape(m.group(1))}</code></strong>'),
        text,
    )
    text = re.sub(
        r"\*`([^`]+)`\*",
        lambda m: _ph(f'<em><code>{html.escape(m.group(1))}</code></em>'),
        text,
    )
    text = re.sub(
        r"`([^`]+)`",
        lambda m: _ph(f'<code>{html.escape(m.group(1))}</code>'),
        text,
    )

    # HTML-escape the remaining (non-code) text
    text = html.escape(text, quote=True)

    # Bold + italic
    text = re.sub(r"\*\*\*(.+?)\*\*\*", r"<strong><em>\1</em></strong>", text)
    # Bold
    text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
    # Italic
    text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
    # Links (brackets and parens survive html.escape)
    text = re.sub(
        r"\[([^\]]+)\]\(([^)]+)\)",
        r'<a href="\2" target="_blank" rel="noopener">\1</a>',
        text,
    )
    # Em-dash
    text = text.replace(" --- ", " &mdash; ")
    text = text.replace("---", "&mdash;")

    # Restore placeholders
    for key, value in placeholders.items():
        text = text.replace(key, value)

    return text


def convert_inline_block(text: str) -> str:
    """Convert a block of text with inline markdown, preserving paragraphs.

    Handles code fences, lists, and regular paragraphs within blockquotes.
    """
    lines = text.split("\n")
    result = []
    i = 0

    while i < len(lines):
        line = lines[i]

        # Code fence inside blockquote
        if line.strip().startswith("```"):
            lang = line.strip()[3:].strip()
            code_lines = []
            i += 1
            while i < len(lines) and not lines[i].strip().startswith("```"):
                code_lines.append(lines[i])
                i += 1
            i += 1  # skip closing ```
            code_text = html.escape("\n".join(code_lines))
            lang_attr = f' class="language-{lang}"' if lang else ""
            result.append(f'<pre><code{lang_attr}>{code_text}</code></pre>')
            continue

        # Skip blank lines
        if not line.strip():
            i += 1
            continue

        # List items
        if line.strip().startswith("- ") or line.strip().startswith("* "):
            result.append("<ul>")
            while i < len(lines) and (lines[i].strip().startswith("- ") or lines[i].strip().startswith("* ")):
                item_text = re.sub(r"^[-*]\s+", "", lines[i].strip())
                result.append(f"  <li>{convert_inline(item_text)}</li>")
                i += 1
            result.append("</ul>")
            continue

        if re.match(r"^\s*\d+\.\s", line):
            result.append("<ol>")
            while i < len(lines) and re.match(r"^\s*\d+\.\s", lines[i]):
                item_text = re.sub(r"^\s*\d+\.\s+", "", lines[i].strip())
                result.append(f"  <li>{convert_inline(item_text)}</li>")
                i += 1
            result.append("</ol>")
            continue

        # Regular paragraph: collect lines until blank or block element
        para_lines = []
        while i < len(lines) and lines[i].strip() and not lines[i].strip().startswith("```") and not lines[i].strip().startswith("- ") and not lines[i].strip().startswith("* ") and not re.match(r"^\s*\d+\.\s", lines[i]):
            para_lines.append(lines[i].strip())
            i += 1
        if para_lines:
            result.append(f"<p>{convert_inline(' '.join(para_lines))}</p>")

    return "\n".join(result)


def classify_blockquote(text: str) -> str:
    """Determine which D2L box class a blockquote should use."""
    lower = text.lower()
    if "after this lesson" in lower or "what you'll be able" in lower or "what we're covering" in lower or "after this unit" in lower:
        return "blue-box"
    if "bug alert" in lower:
        return "red-box"
    if "important" in lower and ("warning" in lower or "!" in text[:30]):
        return "red-box"
    if "try it" in lower or "partner" in lower or "complete on your own" in lower or "activity" in lower:
        return "gray-box"
    if "pep talk" in lower or "encouragement" in lower or "note:" in lower:
        return "info-box"
    return "info-box"


def collect_list(lines: list[str], start: int, unordered: bool) -> tuple[list[str], int]:
    """Collect list items, handling continuation lines."""
    items = []
    i = start
    while i < len(lines):
        line = lines[i]
        if unordered and (line.strip().startswith("- ") or line.strip().startswith("* ")):
            item_text = re.sub(r"^[\s]*[-*]\s+", "", line)
            items.append(item_text)
            i += 1
        elif not unordered and re.match(r"^\s*\d+\.\s", line):
            item_text = re.sub(r"^\s*\d+\.\s+", "", line)
            items.append(item_text)
            i += 1
        elif line.startswith("  ") and items:
            # Continuation of previous item
            items[-1] += " " + line.strip()
            i += 1
        else:
            break
    return items, i


def render_list(items: list[str], ordered: bool) -> str:
    """Render list items as HTML."""
    tag = "ol" if ordered else "ul"
    inner = "\n".join(f"  <li>{convert_inline(item)}</li>" for item in items)
    return f"<{tag}>\n{inner}\n</{tag}>"


def convert_table(table_lines: list[str]) -> str:
    """Convert markdown table to HTML table."""
    rows = []
    for line in table_lines:
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        rows.append(cells)

    if len(rows) < 2:
        return ""

    # First row is header, second is separator (skip it)
    header = rows[0]
    data_rows = rows[2:]

    parts = ['<table>', '<thead><tr>']
    for cell in header:
        parts.append(f"  <th>{convert_inline(cell)}</th>")
    parts.append("</tr></thead>")
    parts.append("<tbody>")
    for row in data_rows:
        parts.append("<tr>")
        for cell in row:
            parts.append(f"  <td>{convert_inline(cell)}</td>")
        parts.append("</tr>")
    parts.append("</tbody></table>")
    return "\n".join(parts)


# ── Build Logic ──────────────────────────────────────────────────────────────

def generate_nav(current: dict, prev_info: dict | None, next_info: dict | None) -> tuple[str, str]:
    """Generate navigation bar HTML and arrow-key script for a lesson page."""
    html_dir = current["html_file"].parent
    home_rel = os.path.relpath(SITE_ROOT / "index.html", html_dir)

    prev_url = ""
    if prev_info:
        prev_url = os.path.relpath(prev_info["html_file"], html_dir)
        prev_name = prev_info["md_file"].stem
        prev_link = f'<a href="{escape(prev_url)}">&larr; {escape(prev_name)}</a>'
    else:
        prev_link = "<span></span>"

    next_url = ""
    if next_info:
        next_url = os.path.relpath(next_info["html_file"], html_dir)
        next_name = next_info["md_file"].stem
        next_link = f'<a href="{escape(next_url)}">{escape(next_name)} &rarr;</a>'
    else:
        next_link = "<span></span>"

    home_link = f'<a href="{escape(home_rel)}">Index</a>'

    nav_html = (
        f'<nav class="lesson-nav" data-prev="{escape(prev_url)}" data-next="{escape(next_url)}">'
        f'<div class="nav-prev">{prev_link}</div>'
        f'<div class="nav-home">{home_link}</div>'
        f'<div class="nav-next">{next_link}</div>'
        f'</nav>'
    )

    script = (
        '<script>\n'
        'document.addEventListener("keydown", function(e) {\n'
        '    var t = e.target.tagName;\n'
        '    if (t === "INPUT" || t === "TEXTAREA" || e.target.isContentEditable) return;\n'
        '    var nav = document.querySelector(".lesson-nav");\n'
        '    if (!nav) return;\n'
        '    if (e.key === "ArrowLeft" && nav.dataset.prev) window.location.href = nav.dataset.prev;\n'
        '    if (e.key === "ArrowRight" && nav.dataset.next) window.location.href = nav.dataset.next;\n'
        '});\n'
        '</script>'
    )

    return nav_html, script


def build_lesson(lesson: dict, prev_info: dict | None, next_info: dict | None) -> None:
    """Build a single lesson HTML file with prev/next navigation."""
    md_file = lesson["md_file"]
    html_file = lesson["html_file"]
    html_file.parent.mkdir(exist_ok=True)

    md_text = md_file.read_text(encoding="utf-8")
    title, body = convert_md_to_html(md_text)
    if not title:
        title = md_file.stem

    nav_bar, nav_script = generate_nav(lesson, prev_info, next_info)
    nav_bottom = nav_bar.replace('"lesson-nav"', '"lesson-nav lesson-nav-bottom"', 1)
    body = nav_bar + "\n" + body + "\n" + nav_bottom

    css_rel = os.path.relpath(SITE_ROOT / "local-styles.css", html_file.parent)

    html_content = HTML_TEMPLATE.format(
        css_path=css_rel,
        title=title,
        body=body,
        extra_scripts=nav_script,
    )

    html_file.write_text(html_content, encoding="utf-8")


def clean_unit(unit_key: str, unit_rel_path: str) -> int:
    """Remove generated HTML files. Returns count."""
    html_dir = SITE_ROOT / unit_rel_path / "revised" / "html"
    if not html_dir.exists():
        return 0
    count = 0
    for f in html_dir.glob("*.html"):
        f.unlink()
        count += 1
    if not any(html_dir.iterdir()):
        html_dir.rmdir()
    return count


def build_index(all_lessons: list[dict]) -> None:
    """Generate an index.html listing all units and lessons in pedagogical order."""
    # Group lessons by unit, preserving order
    units: dict[str, dict] = {}
    for lesson in all_lessons:
        uk = lesson["unit_key"]
        if uk not in units:
            units[uk] = {"unit_rel": lesson["unit_rel"], "lessons": []}
        units[uk]["lessons"].append(lesson)

    parts = [
        '<!DOCTYPE html><html lang="en"><head>',
        '<meta charset="utf-8">',
        '<meta name="viewport" content="width=device-width, initial-scale=1">',
        '<link rel="stylesheet" href="local-styles.css">',
        '<title>CS 160 - Exploring Computer Science</title>',
        '<style>',
        '  .unit-section { margin: 1.5rem 0; }',
        '  .unit-section h2 { font-size: 1.2rem; }',
        '  .lesson-list { list-style: none; padding: 0; }',
        '  .lesson-list li { padding: 0.25rem 0; }',
        '  .lesson-list a { text-decoration: none; }',
        '  .lesson-list a:hover { text-decoration: underline; }',
        '  .count { color: #888; font-size: 0.85rem; }',
        '</style>',
        '</head><body>',
        '<div class="container-fluid">',
        '<h1>CS 160 &mdash; Exploring Computer Science</h1>',
        '<p>Portland Community College &bull; Course Lesson Index</p>',
    ]

    for unit_key, unit_data in units.items():
        unit_rel = unit_data["unit_rel"]
        lessons = unit_data["lessons"]

        unit_name = unit_rel.split("/")[-1].replace("unit-", "Unit ").replace("-", " ").title()
        unit_name = re.sub(r"Unit (\d+) ", r"Unit \1: ", unit_name, count=1)

        parts.append(f'<div class="unit-section">')
        parts.append(f'<h2>{unit_name} <span class="count">({len(lessons)} lessons)</span></h2>')
        parts.append('<ul class="lesson-list">')

        for lesson in lessons:
            parts.append(f'  <li><a href="{lesson["html_rel"]}">{lesson["md_file"].stem}</a></li>')

        parts.append("</ul></div>")

    parts.append('</div></body></html>')

    index_file = SITE_ROOT / "index.html"
    index_file.write_text("\n".join(parts), encoding="utf-8")
    print(f"  index.html written ({index_file})")


# ── CLI ──────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Build D2L-style HTML from revised markdown lessons."
    )
    parser.add_argument(
        "units", nargs="*",
        help="Unit(s) to build (e.g. unit3 unit5). Default: all units."
    )
    parser.add_argument(
        "--clean", action="store_true",
        help="Remove generated HTML instead of building."
    )
    parser.add_argument(
        "--list", action="store_true",
        help="List what would be built without actually building."
    )
    args = parser.parse_args()

    # Determine which units to process
    if args.units:
        target_keys = set()
        for u in args.units:
            u = u.lower().replace(" ", "")
            if u in UNIT_DIRS:
                target_keys.add(u)
            else:
                print(f"Unknown unit: {u}. Available: {', '.join(UNIT_DIRS.keys())}")
                sys.exit(1)
    else:
        target_keys = set(UNIT_DIRS.keys())

    if args.clean:
        total = 0
        for unit_key in sorted(target_keys):
            n = clean_unit(unit_key, UNIT_DIRS[unit_key])
            if n:
                print(f"  {unit_key}: removed {n} HTML files")
                total += n
        print(f"Cleaned {total} files.")
        return

    # Collect all lessons globally (needed for navigation context even when
    # building a subset of units)
    all_lessons = collect_all_lessons()

    if args.list:
        current_unit = None
        for lesson in all_lessons:
            if lesson["unit_key"] not in target_keys:
                continue
            if lesson["unit_key"] != current_unit:
                current_unit = lesson["unit_key"]
                unit_count = sum(1 for l in all_lessons if l["unit_key"] == current_unit)
                print(f"  {current_unit}: {unit_count} markdown files")
            print(f"    {lesson['md_file'].name}")
        return

    # Build lessons with prev/next navigation
    print("Building D2L-style HTML from markdown...\n")
    total = 0
    units_counted: dict[str, int] = {}
    for idx, lesson in enumerate(all_lessons):
        if lesson["unit_key"] not in target_keys:
            continue

        prev_info = all_lessons[idx - 1] if idx > 0 else None
        next_info = all_lessons[idx + 1] if idx < len(all_lessons) - 1 else None

        build_lesson(lesson, prev_info, next_info)
        total += 1
        units_counted[lesson["unit_key"]] = units_counted.get(lesson["unit_key"], 0) + 1

    for uk in sorted(units_counted):
        print(f"  {uk}: {units_counted[uk]} lessons → {UNIT_DIRS[uk]}/revised/html/")

    # Rebuild index using full lesson list (all units, proper ordering)
    if total:
        print()
        build_index(all_lessons)

    print(f"\nDone! Built {total} HTML files.")
    if total:
        print("Open index.html in your browser to browse.")
        print("Use ← → arrow keys to navigate between lessons.")


if __name__ == "__main__":
    main()
