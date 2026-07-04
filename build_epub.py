#!/usr/bin/env python3
"""Build cs160.epub - an offline e-book of the whole course - from the course tree.

Companion to build_index.py (shares its unit scan, so the book always matches
the site). Re-run after adding, renaming, or reorganizing lessons:

    python3 build_epub.py          # writes cs160.epub in the repo root

What the book contains: every Overview / lesson / practice page / Summary from
units 0-10, in course order, with images embedded. Things an e-reader can't run
(videos, embedded widgets, Python Tutor, check-for-understanding quizzes) are
replaced with a clearly labeled link box pointing at the live URL, so a student
reading on a tablet can still tap through to them.

Requires lxml (used to normalize the D2L HTML into valid XHTML).
"""
import os, re, uuid, zipfile, datetime, mimetypes, posixpath
from urllib.parse import unquote, urlparse
from lxml import html as lhtml
from lxml import etree

from build_index import UNITS, collect_pages, viewer_title

OUT = "cs160.epub"
BOOK_TITLE = "CS 160: Exploring Computer Science"
BOOK_AUTHOR = "Clarissa Littler"
BOOK_LANG = "en"

IMG_EXTS = {".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp"}
DROP_TAGS = {"script", "style", "link", "meta", "noscript", "form", "input", "button"}

# ------------------------------------------------------------------ helpers ----

def youtube_watch(src):
    """Turn an embed URL into a normal watch URL when we can."""
    m = re.search(r"youtube(?:-nocookie)?\.com/embed/([A-Za-z0-9_-]{6,})", src)
    if m:
        return f"https://www.youtube.com/watch?v={m.group(1)}"
    return src

def iframe_replacement(el, page_dir):
    """Build the link box that stands in for an iframe/embed in the book."""
    src = el.get("src", "") or ""
    title = (el.get("title") or "").strip()
    box = lhtml.Element("div")
    box.set("class", "epub-embed")
    label = etree.SubElement(box, "p")
    strong = etree.SubElement(label, "strong")
    if src.startswith("http://") or src.startswith("https://"):
        url = youtube_watch(src)
        kind = "Video" if "youtube" in url or "kaltura" in src else "Interactive content"
        strong.text = f"▶ {kind}: {title or 'open in your browser'}"
        p = etree.SubElement(box, "p")
        a = etree.SubElement(p, "a")
        a.set("href", url)
        a.text = url
    else:
        # relative embed - one of the course's own widgets or a D2L quiz export
        name = posixpath.basename(unquote(urlparse(src).path)) or "widget"
        strong.text = f"▶ Interactive widget: {title or name}"
        p = etree.SubElement(box, "p")
        p.text = ("This hands-on widget can't run inside an e-book - "
                  "open this lesson on the course site or in D2L to use it.")
    return box

def find_content_root(doc):
    """The D2L template wraps real content in a col-sm-10 div; fall back to body."""
    hits = doc.xpath("//div[contains(concat(' ', normalize-space(@class), ' '), ' col-sm-10 ')]")
    if hits:
        return hits[0]
    body = doc.find("body")
    return body if body is not None else doc

# ------------------------------------------------------------- page processing ----

class Book:
    def __init__(self):
        self.chapters = []          # dicts: id, file, title, unit
        self.images = {}            # abs path -> epub-relative name (images/...)
        self.missing_images = []
        self.replaced_embeds = 0
        self.unwrapped_links = 0

    def image_name(self, abspath):
        if abspath in self.images:
            return self.images[abspath]
        base = re.sub(r"[^A-Za-z0-9._-]", "_", os.path.basename(abspath))
        name = f"images/{len(self.images):03d}-{base}"
        self.images[abspath] = name
        return name

    def process_page(self, path, title):
        page_dir = os.path.dirname(path)
        parser = lhtml.HTMLParser(encoding="utf-8")
        doc = lhtml.parse(path, parser=parser).getroot()
        root = find_content_root(doc)

        for el in root.iter():
            if el.tag in DROP_TAGS and el.getparent() is not None:
                el.getparent().remove(el)

        for el in list(root.iter("iframe")) + list(root.iter("embed")) + list(root.iter("object")):
            parent = el.getparent()
            if parent is None:
                continue
            parent.replace(el, iframe_replacement(el, page_dir))
            self.replaced_embeds += 1

        for img in list(root.iter("img")):
            raw = img.get("src", "") or ""
            src = unquote(urlparse(raw).path)
            if not src or raw.startswith(("http://", "https://", "data:")):
                continue
            if src.startswith("/"):
                # D2L server template art (/shared/... banners, icons) - decorative,
                # only exists inside D2L. Drop it silently.
                img.getparent().remove(img)
                continue
            abspath = os.path.normpath(os.path.join(page_dir, src))
            if os.path.isfile(abspath):
                img.set("src", self.image_name(abspath))
            else:
                self.missing_images.append(f"{path} -> {src}")
                alt = img.get("alt", "")
                em = lhtml.Element("em")
                em.text = f"[image: {alt}]" if alt else "[missing image]"
                img.getparent().replace(img, em)

        # links an e-reader can't follow (D2L quicklinks, relative files/widgets):
        # unwrap to plain text - the surrounding prose already says where they live
        for a in list(root.iter("a")):
            href = a.get("href", "") or ""
            if href.startswith(("http://", "https://", "#", "mailto:")):
                continue
            a.tag = "em"
            for attr in list(a.attrib):
                del a.attrib[attr]
            self.unwrapped_links += 1

        # strip event handlers and D2L-only attributes
        for el in root.iter():
            for attr in list(el.attrib):
                if attr.startswith("on") or attr in ("contenteditable",):
                    del el.attrib[attr]

        parts = []
        if root.text and root.text.strip():
            parts.append(root.text)
        for child in root:
            parts.append(etree.tostring(child, method="xml", encoding="unicode"))
        body = "".join(parts)
        return XHTML_SHELL.format(title=escape(title), body=body)

def escape(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

XHTML_SHELL = """<?xml version="1.0" encoding="utf-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
<title>{title}</title>
<link rel="stylesheet" type="text/css" href="style.css"/>
</head>
<body>
{body}
</body>
</html>
"""

STYLE = """
body { font-family: serif; line-height: 1.6; margin: 0.5em 1em; }
h1 { font-size: 1.6em; margin: 0.8em 0 0.5em; }
h2 { font-size: 1.3em; margin: 1em 0 0.4em; border-bottom: 2px solid #7fdbca; padding-bottom: 0.15em; }
h3 { font-size: 1.1em; margin: 0.9em 0 0.3em; }
img { max-width: 100%; }
pre, code { font-family: monospace; font-size: 0.9em; background: #f0f0f0; }
pre { padding: 0.8em; border: 1px solid #ddd; overflow-x: auto; white-space: pre-wrap; }
table { border-collapse: collapse; margin: 0.8em 0; }
th, td { border: 1px solid #999; padding: 0.3em 0.6em; }
th { background: #eee; }
.box { padding: 0.8em 1em; margin: 1em 0; border-radius: 6px; }
.blue-box  { background: #e8f0fe; border-left: 5px solid #1c507e; }
.green2-box, .green-box { background: #e8f5e9; border-left: 5px solid #2e7d32; }
.info-box  { background: #fff8e1; border-left: 5px solid #e6a817; }
.gray-box, .grey-box { background: #eeeeee; border-left: 5px solid #757575; }
.red-box   { background: #fdecea; border-left: 5px solid #c0392b; }
.codebox   { background: #f7f7f7; border: 1px solid #ddd; padding: 0.5em 0.8em; margin: 0.6em 0; }
.epub-embed { background: #f3f7fb; border: 1px dashed #1c507e; padding: 0.7em 1em; margin: 1em 0; }
.epub-embed p { margin: 0.2em 0; }
.banner-img img, .bg-img-wrapper img { max-height: 12em; width: 100%; object-fit: cover; }
details { margin: 0.6em 0; }
summary { cursor: pointer; color: #2b78e4; }
footer { margin-top: 2em; border-top: 1px solid #ccc; color: #777; font-size: 0.85em; }
.titlepage { text-align: center; margin-top: 20%; }
.titlepage h1 { font-size: 2em; border: none; }
.titlepage p { color: #555; }
nav ol { list-style: none; }
"""

TITLEPAGE = XHTML_SHELL.format(title=escape(BOOK_TITLE), body=f"""
<div class="titlepage">
<h1>{escape(BOOK_TITLE)}</h1>
<p>A general-education introduction to computer science<br/>Portland Community College</p>
<p>{escape(BOOK_AUTHOR)}</p>
<p class="note">Generated from the course site by build_epub.py.<br/>
Videos, widgets, and self-check quizzes appear as links - they need a browser.</p>
</div>
""")

# ------------------------------------------------------------------ packaging ----

def media_type(name):
    return mimetypes.guess_type(name)[0] or "application/octet-stream"

def build():
    book = Book()
    toc = []  # (unit_title, [(chapter_id, file, title), ...])

    n = 0
    for directory, unit_title, _anchor in UNITS:
        entries = []
        for href, stem, is_inter in collect_pages(directory):
            if is_inter:
                continue  # widgets can't run in an e-book; lessons link to them instead
            n += 1
            cid, cfile = f"ch{n:03d}", f"ch{n:03d}.xhtml"
            title = viewer_title(stem, unit_title)
            xhtml = book.process_page(href, title)
            book.chapters.append({"id": cid, "file": cfile, "title": title,
                                  "unit": unit_title, "xhtml": xhtml})
            entries.append((cid, cfile, title))
        if entries:
            toc.append((unit_title, entries))

    uid = f"urn:uuid:{uuid.uuid5(uuid.NAMESPACE_URL, 'cs160-course-site-epub')}"
    modified = datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")

    manifest = ['<item id="nav" href="nav.xhtml" media-type="application/xhtml+xml" properties="nav"/>',
                '<item id="ncx" href="toc.ncx" media-type="application/x-dtbncx+xml"/>',
                '<item id="css" href="style.css" media-type="text/css"/>',
                '<item id="titlepage" href="titlepage.xhtml" media-type="application/xhtml+xml"/>']
    spine = ['<itemref idref="titlepage"/>']
    for ch in book.chapters:
        manifest.append(f'<item id="{ch["id"]}" href="{ch["file"]}" media-type="application/xhtml+xml"/>')
        spine.append(f'<itemref idref="{ch["id"]}"/>')
    for i, (abspath, name) in enumerate(sorted(book.images.items(), key=lambda kv: kv[1])):
        manifest.append(f'<item id="img{i:03d}" href="{name}" media-type="{media_type(name)}"/>')

    opf = f"""<?xml version="1.0" encoding="utf-8"?>
<package xmlns="http://www.idpf.org/2007/opf" version="3.0" unique-identifier="uid" xml:lang="en">
<metadata xmlns:dc="http://purl.org/dc/elements/1.1/">
<dc:identifier id="uid">{uid}</dc:identifier>
<dc:title>{escape(BOOK_TITLE)}</dc:title>
<dc:creator>{escape(BOOK_AUTHOR)}</dc:creator>
<dc:language>{BOOK_LANG}</dc:language>
<meta property="dcterms:modified">{modified}</meta>
</metadata>
<manifest>
{chr(10).join(manifest)}
</manifest>
<spine toc="ncx">
{chr(10).join(spine)}
</spine>
</package>
"""

    nav_units = []
    for unit_title, entries in toc:
        lis = "\n".join(f'<li><a href="{f}">{escape(t)}</a></li>' for _cid, f, t in entries)
        first_file = entries[0][1]
        nav_units.append(f'<li><a href="{first_file}">{escape(unit_title)}</a>\n<ol>\n{lis}\n</ol>\n</li>')
    nav = XHTML_SHELL.format(title="Contents", body=(
        '<nav xmlns:epub="http://www.idpf.org/2007/ops" epub:type="toc" id="toc">\n'
        "<h1>Contents</h1>\n<ol>\n" + "\n".join(nav_units) + "\n</ol>\n</nav>"))

    # NCX (flat, for older readers)
    navpoints, order = [], 0
    for unit_title, entries in toc:
        for _cid, f, t in entries:
            order += 1
            navpoints.append(
                f'<navPoint id="np{order}" playOrder="{order}">'
                f'<navLabel><text>{escape(unit_title)} - {escape(t)}</text></navLabel>'
                f'<content src="{f}"/></navPoint>')
    ncx = f"""<?xml version="1.0" encoding="utf-8"?>
<ncx xmlns="http://www.daisy.org/z3986/2005/ncx/" version="2005-1">
<head><meta name="dtb:uid" content="{uid}"/></head>
<docTitle><text>{escape(BOOK_TITLE)}</text></docTitle>
<navMap>
{chr(10).join(navpoints)}
</navMap>
</ncx>
"""

    with zipfile.ZipFile(OUT, "w") as z:
        z.writestr("mimetype", "application/epub+zip", compress_type=zipfile.ZIP_STORED)
        z.writestr("META-INF/container.xml",
                   '<?xml version="1.0" encoding="utf-8"?>\n'
                   '<container version="1.0" xmlns="urn:oasis:names:tc:opendocument:xmlns:container">'
                   '<rootfiles><rootfile full-path="OEBPS/content.opf" '
                   'media-type="application/oebps-package+xml"/></rootfiles></container>')
        z.writestr("OEBPS/content.opf", opf)
        z.writestr("OEBPS/nav.xhtml", nav)
        z.writestr("OEBPS/toc.ncx", ncx)
        z.writestr("OEBPS/style.css", STYLE)
        z.writestr("OEBPS/titlepage.xhtml", TITLEPAGE)
        for ch in book.chapters:
            z.writestr(f"OEBPS/{ch['file']}", ch["xhtml"])
        for abspath, name in book.images.items():
            z.write(abspath, f"OEBPS/{name}")

    size = os.path.getsize(OUT) / 1e6
    print(f"{OUT}: {len(book.chapters)} chapters, {len(book.images)} images, "
          f"{book.replaced_embeds} embeds converted to links, "
          f"{book.unwrapped_links} unreachable links unwrapped, {size:.1f} MB")
    if book.missing_images:
        print(f"  {len(book.missing_images)} image reference(s) missing on disk:")
        for m in book.missing_images[:10]:
            print(f"    {m}")

if __name__ == "__main__":
    build()
