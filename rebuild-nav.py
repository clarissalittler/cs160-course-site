#!/usr/bin/env python3
"""
rebuild-nav.py — Regenerate viewer.html and index.html navigation from
the Table of Contents.html files in each unit directory.

Usage:
    python3 rebuild-nav.py

This script reads every unit's "Table of Contents.html" file (the source
of truth for lesson ordering), then rewrites the navigation manifests in
both viewer.html and index.html to match.

It preserves all non-navigation content in those files — only the lesson
lists are regenerated.
"""

import os
import re
import json
from html import unescape
from urllib.parse import quote

SITE_DIR = os.path.dirname(os.path.abspath(__file__))

# Unit metadata: directory name -> display name
# Order matters — this controls sidebar ordering
UNITS = [
    ("unit0",  "course-information",  "Course Information"),
    ("unit1",  None,                  "Unit 1: Digital Information"),
    ("unit2",  None,                  "Unit 2: Internet"),
    ("unit3",  None,                  "Unit 3: Intro to Programming"),
    ("unit4",  None,                  "Unit 4: Selection & Functions"),
    ("unit5",  None,                  "Unit 5: Iteration"),
    ("unit6",  None,                  "Unit 6: Arrays, Tuples & Dictionaries"),
    ("unit7",  None,                  "Unit 7: Algorithms & Efficiency"),
    ("unit8",  None,                  "Unit 8: Data"),
    ("unit9",  None,                  "Unit 9: Artificial Intelligence"),
    ("unit10", None,                  "Unit 10: Cybersecurity"),
]


def find_content_dir(unit_dir):
    """Find the content subdirectory inside a unit directory."""
    for entry in os.listdir(unit_dir):
        full = os.path.join(unit_dir, entry)
        if os.path.isdir(full) and not entry.startswith('.') and entry != 'archive':
            return entry
    return None


def parse_toc(toc_path, unit_dir_name):
    """Parse a Table of Contents.html file and return list of (title, href) tuples.
    href is relative to the site root."""
    with open(toc_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract all <a> tags with href and link text
    # Pattern: href="path" />N. Title</a>
    pattern = r'href="([^"]+)"\s*/?>([^<]*)</a>'
    matches = re.findall(pattern, html)

    lessons = []
    for href, title in matches:
        # Clean up title: remove leading number + period
        title = title.strip()
        title = re.sub(r'^\d+\.\s*', '', title)
        title = unescape(title)

        # href is relative to the unit directory — prepend unit dir
        full_href = f"{unit_dir_name}/{href}"
        lessons.append((title, full_href))

    return lessons


def url_encode_path(path):
    """URL-encode a file path for use in HTML hrefs, preserving /."""
    parts = path.split('/')
    return '/'.join(quote(p) for p in parts)


def build_viewer_js(all_units):
    """Generate the JavaScript units array for viewer.html."""
    lines = ["const units = ["]
    for name, lessons in all_units:
        lines.append("  {")
        lines.append(f'    name: {json.dumps(name)},')
        lines.append("    lessons: [")
        for title, href in lessons:
            encoded = url_encode_path(href)
            lines.append(f'      {{ title: {json.dumps(title)}, href: {json.dumps(encoded)} }},')
        lines.append("    ]")
        lines.append("  },")
    lines.append("];")
    return '\n'.join(lines)


def build_index_html_units(all_units):
    """Generate the unit-card divs for index.html."""
    lines = []
    for i, (name, lessons) in enumerate(all_units):
        unit_id = f"unit{i}" if i < 10 else f"unit{i}"
        # Match the original id scheme
        if name == "Course Information":
            unit_id = "unit0"
        else:
            # Extract unit number from name
            m = re.search(r'Unit (\d+)', name)
            if m:
                unit_id = f"unit{m.group(1)}"

        safe_name = name.replace('&', '&amp;')
        lines.append(f'    <div class="unit-card" id="{unit_id}">')
        lines.append(f'      <h2>{safe_name}</h2>')
        lines.append('      <ul>')
        for j, (title, href) in enumerate(lessons, 1):
            encoded = url_encode_path(href)
            safe_title = title.replace('&', '&amp;')
            lines.append(f'            <li><a href="{encoded}">{j}. {safe_title}</a></li>')
        lines.append('      </ul>')
        lines.append('    </div>')
    return '\n\n'.join(lines)


def build_index_sidebar(all_units):
    """Generate the sidebar nav links for index.html."""
    lines = []
    for name, _ in all_units:
        if name == "Course Information":
            unit_id = "unit0"
        else:
            m = re.search(r'Unit (\d+)', name)
            unit_id = f"unit{m.group(1)}" if m else "unit0"
        safe_name = name.replace('&', '&amp;')
        lines.append(f'        <li><a href="#{unit_id}">{safe_name}</a></li>')
    return '\n'.join(lines)


def update_viewer(all_units):
    """Update viewer.html with the new units manifest."""
    viewer_path = os.path.join(SITE_DIR, 'viewer.html')
    with open(viewer_path, 'r', encoding='utf-8') as f:
        content = f.read()

    new_js = build_viewer_js(all_units)

    # Replace the units array — it starts with "const units = [" and ends with "];"
    # followed by blank line or "// Flatten"
    pattern = r'const units = \[.*?\];'
    content = re.sub(pattern, new_js, content, flags=re.DOTALL)

    with open(viewer_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Updated {viewer_path}")


def update_index(all_units):
    """Update index.html with the new unit cards and sidebar."""
    index_path = os.path.join(SITE_DIR, 'index.html')
    with open(index_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Replace sidebar nav links
    sidebar_pattern = r'(<ul>\s*\n)(        <li><a href="#unit0">.*?)(      </ul>)'
    new_sidebar = build_index_sidebar(all_units)
    content = re.sub(
        sidebar_pattern,
        lambda m: m.group(1) + new_sidebar + '\n' + m.group(3),
        content,
        flags=re.DOTALL
    )

    # Replace unit cards — from first unit-card to last unit-card closing div before </main>
    cards_pattern = r'(    <div class="unit-card" id="unit0">.*?</div>\n    </div>)\s*\n    </main>'
    new_cards = build_index_html_units(all_units)
    content = re.sub(
        cards_pattern,
        new_cards + '\n    </main>',
        content,
        flags=re.DOTALL
    )

    with open(index_path, 'w', encoding='utf-8') as f:
        f.write(content)

    print(f"  Updated {index_path}")


def main():
    print("Rebuilding navigation from Table of Contents files...\n")

    all_units = []

    for unit_dir_name, content_dir_override, display_name in UNITS:
        unit_path = os.path.join(SITE_DIR, unit_dir_name)
        toc_path = os.path.join(unit_path, 'Table of Contents.html')

        if not os.path.exists(toc_path):
            print(f"  WARNING: No Table of Contents.html in {unit_dir_name}, skipping")
            continue

        lessons = parse_toc(toc_path, unit_dir_name)
        all_units.append((display_name, lessons))
        print(f"  {display_name}: {len(lessons)} lessons")

    print()
    update_viewer(all_units)
    update_index(all_units)

    total = sum(len(lessons) for _, lessons in all_units)
    print(f"\nDone! {len(all_units)} units, {total} total lessons.")


if __name__ == '__main__':
    main()
