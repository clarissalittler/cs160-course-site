#!/usr/bin/env python3
"""Regenerate index.html and viewer.html by scanning the course tree.

Run from the repo root, then serve locally:

    python3 build_index.py
    python3 -m http.server 8000      # then open http://localhost:8000/

Both pages are generated from the same filesystem scan, so they never drift
out of sync after you add, rename, or reorganize lessons - just re-run this.

  * index.html  - static link directory with a Course Materials section
  * viewer.html - dark single-pane reader (iframe + prev/next + keyboard nav)
"""
import os, re, html, json
from urllib.parse import quote

# (directory, sidebar/card title, anchor id) - in display order
UNITS = [
    ("unit0/course-information",                       "Course Information",                              "unit0"),
    ("unit1/unit-01-digital-information",              "Unit 1: Digital Information",                      "unit1"),
    ("unit2/unit-02-internet",                         "Unit 2: Internet",                                 "unit2"),
    ("unit3/unit-03-python-introduction",              "Unit 3: Introduction to Programming",              "unit3"),
    ("unit4/unit-04-python-decisions-and-loops",       "Unit 4: Decisions and Loops",                      "unit4"),
    ("unit5/unit-05-python-collections",               "Unit 5: Collections",                              "unit5"),
    ("unit6/unit-06-python-real-data",                 "Unit 6: Working with Real Data",                   "unit6"),
    ("unit7/unit-07-Algorithms and Algorithm Efficiency", "Unit 7: Algorithms & the Nature of Computation", "unit7"),
    ("unit8/unit-08-data",                             "Unit 8: Data",                                     "unit8"),
    ("unit9/unit-09-artificial-intelligence",          "Unit 9: Artificial Intelligence",                  "unit9"),
    ("unit10/unit-10-cybersecurity",                   "Unit 10: Cybersecurity",                           "unit10"),
]

# Folders worth browsing directly (http.server renders these as file listings)
MATERIALS = [
    ("assignments/",            "Assignments & Labs"),
    ("assignments/Activities/", "Weekly Activities"),
    ("quizzes/",                "Quizzes (Units 1-10)"),
    ("colab-notebooks/",        "Colab Notebooks (Units 8-9)"),
]

# ---------------------------------------------------------------- scanning ----

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

def interactive_label(stem):
    return "▸ " + stem.replace("-", " ").title() + " (interactive)"

def collect_pages(directory):
    """Return ordered (href, stem, is_interactive) for one unit directory."""
    if not os.path.isdir(directory):
        return []
    pages = sorted(
        (f for f in os.listdir(directory) if f.endswith(".html")),
        key=lambda f: sort_key(os.path.splitext(f)[0]),
    )
    out = [(f"{directory}/{f}", os.path.splitext(f)[0], False) for f in pages]
    inter = os.path.join(directory, "interactives")
    if os.path.isdir(inter):
        for f in sorted(os.listdir(inter)):
            if f.endswith(".html"):
                out.append((f"{inter}/{f}", os.path.splitext(f)[0], True))
    return out

# ------------------------------------------------------------- index.html ----

def link(href, text):
    return f'            <li><a href="{quote(href, safe="/")}">{html.escape(text)}</a></li>'

def build_card(directory, title, anchor):
    pages = collect_pages(directory)
    if not pages:
        return ""
    items = []
    for href, stem, is_inter in pages:
        items.append(link(href, interactive_label(stem) if is_inter else display_title(stem)))
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

def build_index():
    sidebar = "\n".join(
        f'        <li><a href="#{a}">{html.escape(t)}</a></li>'
        for _, t, a in UNITS
    ) + '\n        <li><a href="#materials">Course Materials</a></li>'

    cards = "\n".join(build_card(d, t, a) for d, t, a in UNITS)
    cards += "\n" + build_materials_card()

    return f'''<!DOCTYPE html>
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
      <p class="subtitle">Local course shell for editing and prototyping. Click any lesson to open it,
      or use the <a href="viewer.html">single-pane reader</a>. Generated by <code>build_index.py</code>
      &mdash; re-run it after adding or renaming lessons.</p>

{cards}    </main>
  </div>
</body>
</html>
'''

# ------------------------------------------------------------ viewer.html ----

def viewer_title(stem, unit_title):
    m = re.match(r"(Unit \d+)", unit_title)
    tag = m.group(1) if m else None
    if stem == "Overview":
        return f"{tag} Overview" if tag else "Overview"
    if stem.endswith("Summary"):
        return stem if stem != "Summary" else (f"{tag} Summary" if tag else "Summary")
    return display_title(stem)

def js_units():
    blocks = []
    for directory, title, _ in UNITS:
        pages = collect_pages(directory)
        if not pages:
            continue
        rows = []
        for href, stem, is_inter in pages:
            t = interactive_label(stem) if is_inter else viewer_title(stem, title)
            rows.append(f'      {{ title: {json.dumps(t, ensure_ascii=False)}, '
                        f'href: {json.dumps(quote(href, safe="/"))} }},')
        body = "\n".join(rows)
        blocks.append(f'  {{\n    name: {json.dumps(title, ensure_ascii=False)},\n'
                      f'    lessons: [\n{body}\n    ]\n  }},')
    return "const units = [\n" + "\n".join(blocks) + "\n];"

VIEWER_SHELL = r'''<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>CS 160 - Lesson Viewer</title>
  <style>
    * { margin: 0; padding: 0; box-sizing: border-box; }
    body {
      font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
      background: #1a1a2e; color: #eee; height: 100vh; overflow: hidden;
    }
    .layout { display: flex; height: 100vh; }
    .sidebar {
      width: 280px; background: #1a1a2e; border-right: 1px solid #333;
      display: flex; flex-direction: column; flex-shrink: 0; transition: margin-left 0.2s;
    }
    .sidebar.collapsed { margin-left: -280px; }
    .sidebar-header {
      padding: 1rem; border-bottom: 1px solid #333;
      display: flex; justify-content: space-between; align-items: center;
    }
    .sidebar-header h1 { font-size: 1rem; color: #7fdbca; }
    .sidebar-toc { flex: 1; overflow-y: auto; padding: 0.5rem 0; }
    .sidebar-toc::-webkit-scrollbar { width: 6px; }
    .sidebar-toc::-webkit-scrollbar-track { background: transparent; }
    .sidebar-toc::-webkit-scrollbar-thumb { background: #444; border-radius: 3px; }
    .unit-group summary {
      font-size: 0.8rem; font-weight: 600; color: #7fdbca;
      padding: 0.5rem 1rem 0.3rem; cursor: pointer; user-select: none; list-style: none;
    }
    .unit-group summary::before { content: "\25B6\00a0"; font-size: 0.6rem; vertical-align: middle; }
    .unit-group[open] summary::before { content: "\25BC\00a0"; }
    .unit-group ul { list-style: none; padding: 0 0 0.3rem 0; }
    .unit-group li { margin: 0; }
    .unit-group a {
      display: block; padding: 0.3rem 1rem 0.3rem 1.5rem; color: #bbb; text-decoration: none;
      font-size: 0.8rem; line-height: 1.4; border-left: 3px solid transparent;
      transition: background 0.15s, border-color 0.15s;
    }
    .unit-group a:hover { background: #16213e; color: #eee; }
    .unit-group a.active {
      background: #16213e; color: #7fdbca; border-left-color: #7fdbca; font-weight: 600;
    }
    .viewer { flex: 1; display: flex; flex-direction: column; min-width: 0; }
    .topbar {
      background: #16213e; border-bottom: 1px solid #333; display: flex; align-items: center;
      padding: 0.4rem 1rem; gap: 0.75rem; flex-shrink: 0;
    }
    .topbar button {
      background: none; border: 1px solid #555; color: #ccc; border-radius: 4px;
      padding: 0.3rem 0.7rem; cursor: pointer; font-size: 0.85rem; transition: background 0.15s;
    }
    .topbar button:hover { background: #333; color: #fff; }
    .topbar button:disabled { opacity: 0.3; cursor: default; }
    .topbar .title {
      flex: 1; font-size: 0.85rem; color: #eee;
      white-space: nowrap; overflow: hidden; text-overflow: ellipsis;
    }
    .topbar .counter { font-size: 0.8rem; color: #888; white-space: nowrap; }
    .topbar .toggle-sidebar { font-size: 1.1rem; padding: 0.2rem 0.5rem; }
    .lesson-frame { flex: 1; border: none; background: #fff; }
    .hint {
      background: #16213e; border-top: 1px solid #333; padding: 0.3rem 1rem;
      font-size: 0.75rem; color: #666; text-align: center; flex-shrink: 0;
    }
    .hint kbd {
      background: #333; border: 1px solid #555; border-radius: 3px; padding: 0.1rem 0.4rem;
      font-family: inherit; font-size: 0.7rem; color: #aaa;
    }
  </style>
</head>
<body>
  <div class="layout">
    <nav class="sidebar" id="sidebar">
      <div class="sidebar-header">
        <h1>CS 160 Lessons</h1>
      </div>
      <div class="sidebar-toc" id="toc"></div>
    </nav>
    <div class="viewer">
      <div class="topbar">
        <button class="toggle-sidebar" id="toggleSidebar" title="Toggle sidebar (S)">&#9776;</button>
        <button id="prevBtn" title="Previous lesson">&larr; Prev</button>
        <button id="nextBtn" title="Next lesson">Next &rarr;</button>
        <span class="title" id="lessonTitle"></span>
        <span class="counter" id="counter"></span>
      </div>
      <iframe class="lesson-frame" id="frame"></iframe>
      <div class="hint">
        <kbd>&larr;</kbd> / <kbd>&rarr;</kbd> prev / next
        &nbsp;&nbsp;
        <kbd>Home</kbd> / <kbd>End</kbd> first / last
        &nbsp;&nbsp;
        <kbd>S</kbd> toggle sidebar
      </div>
    </div>
  </div>

<script>
// ---- Lesson manifest (generated by build_index.py - do not hand-edit) ----
__UNITS__

// Flatten to ordered list
const allLessons = [];
units.forEach((unit, ui) => {
  unit.lessons.forEach((lesson, li) => {
    allLessons.push({ ...lesson, unitIndex: ui, lessonIndex: li });
  });
});

let currentIndex = 0;

// --- Build sidebar TOC ---
const tocEl = document.getElementById('toc');
units.forEach((unit, ui) => {
  const details = document.createElement('details');
  details.className = 'unit-group';
  if (ui === 0) details.open = true;
  const summary = document.createElement('summary');
  summary.textContent = unit.name;
  details.appendChild(summary);
  const ul = document.createElement('ul');
  unit.lessons.forEach((lesson, li) => {
    const flatIdx = allLessons.findIndex(l => l.href === lesson.href);
    const a = document.createElement('a');
    a.href = '#';
    a.textContent = lesson.title;
    a.dataset.index = flatIdx;
    a.addEventListener('click', (e) => {
      e.preventDefault();
      navigateTo(flatIdx);
    });
    const liEl = document.createElement('li');
    liEl.appendChild(a);
    ul.appendChild(liEl);
  });
  details.appendChild(ul);
  tocEl.appendChild(details);
});

// --- Navigation ---
const frame = document.getElementById('frame');
const titleEl = document.getElementById('lessonTitle');
const counterEl = document.getElementById('counter');
const prevBtn = document.getElementById('prevBtn');
const nextBtn = document.getElementById('nextBtn');

function navigateTo(index) {
  if (index < 0 || index >= allLessons.length) return;
  currentIndex = index;
  const lesson = allLessons[index];

  frame.src = lesson.href;
  titleEl.textContent = lesson.title;
  counterEl.textContent = `${index + 1} / ${allLessons.length}`;
  prevBtn.disabled = index === 0;
  nextBtn.disabled = index === allLessons.length - 1;

  tocEl.querySelectorAll('a.active').forEach(a => a.classList.remove('active'));
  const activeLink = tocEl.querySelector(`a[data-index="${index}"]`);
  if (activeLink) {
    activeLink.classList.add('active');
    const details = activeLink.closest('details');
    if (details) details.open = true;
    activeLink.scrollIntoView({ block: 'nearest', behavior: 'smooth' });
  }

  try { sessionStorage.setItem('cs160-viewer-pos', index); } catch(e) {}
}

prevBtn.addEventListener('click', () => navigateTo(currentIndex - 1));
nextBtn.addEventListener('click', () => navigateTo(currentIndex + 1));

document.getElementById('toggleSidebar').addEventListener('click', () => {
  document.getElementById('sidebar').classList.toggle('collapsed');
});

// --- Keyboard navigation ---
function handleNav(e) {
  if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return;

  switch (e.key) {
    case 'ArrowLeft':  e.preventDefault(); navigateTo(currentIndex - 1); break;
    case 'ArrowRight': e.preventDefault(); navigateTo(currentIndex + 1); break;
    case 'Home':       e.preventDefault(); navigateTo(0); break;
    case 'End':        e.preventDefault(); navigateTo(allLessons.length - 1); break;
    case 's':
    case 'S':
      if (!e.ctrlKey && !e.metaKey) {
        e.preventDefault();
        document.getElementById('sidebar').classList.toggle('collapsed');
      }
      break;
  }
}

document.addEventListener('keydown', handleNav);

// Re-attach keyboard listener inside iframe after each load,
// so arrow keys still work even when the iframe has focus.
frame.addEventListener('load', () => {
  try {
    const iframeDoc = frame.contentDocument || frame.contentWindow.document;
    iframeDoc.addEventListener('keydown', handleNav);
  } catch (e) {
    // cross-origin iframe - can't attach, keys won't forward
  }
});

// --- Restore position or start at first lesson ---
let startPos = 0;
try {
  const saved = sessionStorage.getItem('cs160-viewer-pos');
  if (saved !== null) startPos = parseInt(saved, 10);
} catch(e) {}
navigateTo(startPos);
</script>
</body>
</html>
'''

def build_viewer():
    return VIEWER_SHELL.replace("__UNITS__", js_units())

# ------------------------------------------------------------------- main ----

def main():
    with open("index.html", "w", encoding="utf-8") as fh:
        fh.write(build_index())
    with open("viewer.html", "w", encoding="utf-8") as fh:
        fh.write(build_viewer())
    total = sum(len(collect_pages(d)) for d, _, _ in UNITS)
    print(f"index.html + viewer.html regenerated: {len(UNITS)} units, {total} pages.")

if __name__ == "__main__":
    main()
