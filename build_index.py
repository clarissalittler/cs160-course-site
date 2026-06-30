#!/usr/bin/env python3
"""Regenerate index.html by scanning the course tree.

Run from the repo root, then serve locally:

    python3 build_index.py
    python3 -m http.server 8000      # then open http://localhost:8000/

Re-run this any time you add, rename, or reorganize lessons and the index
will stay in sync - no hand-editing.
"""
import os, re, html
from urllib.parse import quote

# (directory, sidebar/card title, anchor id) - in display order
UNITS = [
    ("unit0/course-information",                       "Course Information",                              "unit0"),
    ("unit1/unit-01-digital-information",              "Unit 1: Digital Information",                      "unit1"),
    ("unit2/unit-02-internet",                         "Unit 2: Internet",                                 "unit2"),
    ("unit3/unit-03-python-introduction",              "Unit 3: Introduction to Programming",              "unit3"),
    ("unit4/unit-04-python-selection",                 "Unit 4: Selection",                                "unit4"),
    ("unit5/unit-05-python-iteration",                 "Unit 5: Iteration",                                "unit5"),
    ("unit6/unit-06-python-arrays",                    "Unit 6: Lists, Tuples, and Dictionaries",          "unit6"),
    ("unit7/unit-07-Algorithms and Algorithm Efficiency", "Unit 7: Algorithms & the Nature of Computation", "unit7"),
    ("unit8/unit-08-data",                             "Unit 8: Data",                                     "unit8"),
    ("unit9/unit-09-artificial-intelligence",          "Unit 9: Artificial Intelligence",                  "unit9"),
    ("unit10/unit-10-cybersecurity",                   "Unit 10: Cybersecurity",                           "unit10"),
]

# Folders worth browsing directly (http.server renders these as file listings)
MATERIALS = [
    ("assignments/",            "Assignments & Labs"),
    ("assignments/Activities/", "Weekly Activities"),
    ("quizzes/",                "Quizzes (Units 3-7)"),
    ("colab-notebooks/",        "Colab Notebooks (Units 8-9)"),
]

def sort_key(stem):
    """Overview first, then Lessons by number, then other pages, then Summary."""
    if stem == "Overview":
        return (0, 0, "")
    m = re.search(r"Lesson\s+(\d+)", stem)
    if m:
        return (1, int(m.group(1)), stem)
    if stem == "Summary" or stem.endswith("Summary"):
        return (3, 0, "")
    return (2, 0, stem.lower())   # setup pages, practice problems, &c.

def display_title(stem):
    # normalize "Lesson 01" -> "Lesson 1" for readability; leave the rest intact
    return re.sub(r"^Lesson\s+0*(\d+)", r"Lesson \1", stem)

def link(href, text):
    return f'            <li><a href="{quote(href, safe="/")}">{html.escape(text)}</a></li>'

def build_card(directory, title, anchor):
    if not os.path.isdir(directory):
        return ""
    pages = sorted(
        (f for f in os.listdir(directory) if f.endswith(".html")),
        key=lambda f: sort_key(os.path.splitext(f)[0]),
    )
    items = [link(f"{directory}/{f}", display_title(os.path.splitext(f)[0])) for f in pages]

    # tuck any interactive playgrounds in as sub-links
    inter = os.path.join(directory, "interactives")
    if os.path.isdir(inter):
        for f in sorted(os.listdir(inter)):
            if f.endswith(".html"):
                nm = os.path.splitext(f)[0].replace("-", " ").title()
                items.append(link(f"{inter}/{f}", f"▸ {nm} (interactive)"))

    lis = "\n".join(items)
    return f'''    <div class="unit-card" id="{anchor}">
      <h2>{html.escape(title)}</h2>
      <ul>
{lis}
      </ul>
    </div>
'''

def build_materials_card():
    rows = []
    for path, label in MATERIALS:
        if os.path.isdir(path):
            n = len([x for x in os.listdir(path) if not x.startswith(".")])
            rows.append(f'            <li><a href="{quote(path, safe="/")}">{html.escape(label)}</a> '
                        f'<span class="muted">&mdash; browse folder ({n} items)</span></li>')
    if not rows:
        return ""
    return ('    <div class="unit-card" id="materials">\n'
            '      <h2>Course Materials</h2>\n'
            '      <p class="muted" style="margin-bottom:.6rem;font-size:.85rem">'
            'These open as browsable folder listings when served with a local web server.</p>\n'
            '      <ul>\n' + "\n".join(rows) + '\n      </ul>\n    </div>\n')

def main():
    sidebar = "\n".join(
        f'        <li><a href="#{a}">{html.escape(t)}</a></li>'
        for _, t, a in UNITS
    ) + '\n        <li><a href="#materials">Course Materials</a></li>'

    cards = "\n".join(build_card(d, t, a) for d, t, a in UNITS)
    cards += "\n" + build_materials_card()

    page = f'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CS 160 - Course Shell (Local)</title>
  <style>
    * {{ margin: 0; padding: 0; box-sizing: border-box; }}
    body {{ font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
           background: #f5f5f5; color: #333; line-height: 1.6; }}
    .layout {{ display: flex; min-height: 100vh; }}
    .sidebar {{ width: 280px; background: #1a1a2e; color: #eee; padding: 1.5rem 1rem;
               position: sticky; top: 0; height: 100vh; overflow-y: auto; flex-shrink: 0; }}
    .sidebar h1 {{ font-size: 1.1rem; margin-bottom: 1rem; padding-bottom: 0.5rem;
                  border-bottom: 1px solid #333; color: #7fdbca; }}
    .sidebar ul {{ list-style: none; }}
    .sidebar li {{ margin-bottom: 0.3rem; }}
    .sidebar a {{ color: #ccc; text-decoration: none; font-size: 0.85rem; display: block;
                 padding: 0.3rem 0.5rem; border-radius: 4px; transition: background 0.2s; }}
    .sidebar a:hover {{ background: #16213e; color: #7fdbca; }}
    .main {{ flex: 1; padding: 2rem 3rem; max-width: 900px; }}
    .main > h1 {{ font-size: 1.8rem; margin-bottom: 0.5rem; color: #1a1a2e; }}
    .main > p.subtitle {{ color: #666; margin-bottom: 2rem; font-size: 0.95rem; }}
    .unit-card {{ background: #fff; border-radius: 8px; padding: 1.5rem 2rem;
                 margin-bottom: 1.5rem; box-shadow: 0 1px 3px rgba(0,0,0,0.1); scroll-margin-top: 1rem; }}
    .unit-card h2 {{ font-size: 1.2rem; color: #1a1a2e; margin-bottom: 0.75rem;
                    padding-bottom: 0.5rem; border-bottom: 2px solid #7fdbca; }}
    .unit-card ul {{ list-style: none; }}
    .unit-card li {{ margin-bottom: 0.3rem; }}
    .unit-card a {{ color: #2563eb; text-decoration: none; font-size: 0.9rem; }}
    .unit-card a:hover {{ text-decoration: underline; color: #1d4ed8; }}
    .muted {{ color: #888; }}
    @media (max-width: 768px) {{
      .layout {{ flex-direction: column; }}
      .sidebar {{ width: 100%; height: auto; position: static; }}
      .main {{ padding: 1rem; }}
    }}
  </style>
</head>
<body>
  <div class="layout">
    <nav class="sidebar">
      <h1>CS 160</h1>
      <ul>
{sidebar}
      </ul>
    </nav>
    <main class="main">
      <h1>CS 160 - Introduction to Computer Science</h1>
      <p class="subtitle">Local course shell for editing and prototyping. Click any lesson to open it.
      Generated by <code>build_index.py</code> &mdash; re-run it after adding or renaming lessons.</p>

{cards}    </main>
  </div>
</body>
</html>
'''
    with open("index.html", "w", encoding="utf-8") as fh:
        fh.write(page)
    n_pages = sum(page.count(f'href="{quote(d, safe="/")}/') for d, _, _ in UNITS)
    print(f"index.html regenerated: {len(UNITS)} units, {n_pages} lesson links.")

if __name__ == "__main__":
    main()
