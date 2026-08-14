# CS 160 — Weekly Activity Discussions

Short, fun, completion-graded activities that give students a reason to *play* with the week's idea, make or investigate something worth showing other people, and then share it in the weekly D2L discussion. Coding activities are authored in [Quarto](https://quarto.org) (`.qmd`) and converted to Jupyter notebooks (`.ipynb`) that students open and run on **Google Colab**. Hands-on / writing activities are plain Markdown handouts.

## The activities

| Week | Unit | Activity | Format | Files |
|------|------|----------|--------|-------|
| 1 | Digital Information | **Choose one:** **Mona Lisa Underdrive** — databend an image by opening it as audio in Audacity | Handout | `Week01_MonaLisaUnderdrive.md` |
| 1 | Digital Information | **Choose one:** **Broken Poetry** — watch text become ASCII numbers, transform them, turn them back | Notebook | `Week01_BrokenPoetry.qmd` → `.ipynb` |
| 2 | Internet & Web | **Make a Web Page** — build & share a real page on Neocities with hand-written HTML | Handout | `Week02_NeocitiesWebPage.md` |
| 3 | Python Intro | **Mad Libs Generator** — `input()`, strings, f-strings | Notebook | `Week03_MadLibs.qmd` → `.ipynb` |
| 4 | Functions, Decisions & Repetition | **Personality Quiz** — define and reuse a question function; score answers with `if`/`elif`; choose a result | Notebook | `Week04_PersonalityQuiz.qmd` → `.ipynb` |
| 5 | Collections, Models & Interfaces | **Catalog a Collection** — list of dictionaries, data dictionary, filter, summary, and minimization reflection | Notebook | `Week05_CollectionCatalog.qmd` → `.ipynb` |
| 6 | Python Project Studio | **Build a Room Someone Else Could Enter** — model one location, format a multi-line room card, and propose connected rooms | Notebook | `Week06_BuildARoom.qmd` → `.ipynb` |
| 7 | Algorithms | **Beat the Computer** — binary vs. linear search; feel Big-O | Notebook | `Week07_GuessingGame.qmd` → `.ipynb` |
| 8 | Data & Visualization | **Quantified Self** — track yourself in a Google Sheet, chart it (+ optional Python bonus) | Handout (+ notebook) | `Week08_QuantifiedSelf.md`, `Week08_QuantifiedSelf_Analysis.qmd` → `.ipynb` |
| 9 | Artificial Intelligence | **Delighted or Grumpy?** — train a text classifier on reviews, then try to fool it (accessible, text-only) | Notebook | `Week09_TextClassifier.qmd` → `.ipynb` |
| 9 | Artificial Intelligence | **MNIST** — train a neural network to read handwritten digits *(optional companion to the primary text-classifier discussion; image-based with text equivalents)* | Notebook | `Week09_MNIST.qmd` → `.ipynb` |
| 10 | Cybersecurity | **Investigate a Scam** — research one internet scam, write a field-guide post | Handout | `Week10_ScamInvestigation.md` |

The former Week 5 text adventure now supplies the seed for the active Week 6 capstone. The previous Week 6 collection tracker and tiny-dataset activity are preserved in `archive/`. Weeks 6 & 7 originally started as blank slots, and their brainstorming notes remain in `archive/Week06_IDEAS.md` and `archive/Week07_IDEAS.md`.

## Authoring & converting

These were written as `.qmd` (Quarto markdown) and converted to `.ipynb` with:

```bash
quarto convert Week03_MadLibs.qmd      # produces Week03_MadLibs.ipynb
```

Quarto preserves the QMD front matter as visible text in the first notebook cell. After conversion, replace that source-only YAML with a readable title by running this from the repository root:

```bash
python3 clean_notebook_titles.py assignments/Activities
```

To regenerate every notebook from source:

```bash
for f in Week*.qmd; do quarto convert "$f"; done
```

Then run the title-cleanup command above. Edit the `.qmd` (it's much nicer to read and diff than raw notebook JSON), re-run the conversion, and clean the titles. The generated `.ipynb` files use a `python3` kernel and open directly in Colab.

## Notes for students (put these wherever you post the activity)

- **Open in Colab:** upload the `.ipynb` to [colab.research.google.com](https://colab.research.google.com), or push it to GitHub and use the Colab "open from GitHub" option.
- **Run a cell:** click it and press **Shift+Enter**. Run cells top to bottom, in order.
- **Share your work:** in Colab, **File → Share → "Anyone with the link can view,"** then post the link to the discussion thread.
- Every activity is **graded on completion**, not polish. If it runs and it's theirs, they're done.

## Design notes (for instructors)

- **Voice** matches the rest of the course: conversational, "smart friend explaining things," fun examples. Tweak freely per section.
- Each activity ends with **reflection questions** and a **discussion-thread share**, which carries the recurring *"who benefits, who's harmed, who decides?"* thread (especially Weeks 8, 9, 10).
- Notebooks lean on **standard Colab-preinstalled libraries** (`matplotlib`, `scikit-learn`, `tensorflow`). The MNIST notebook downloads ~11 MB and trains for a minute or two; the text classifier and everything else train in seconds.
- An unfinished **HTTP-by-hand** demo (raw HTTP over a socket) sits in `archive/HTTPByHand.ipynb` if an instructor ever wants to finish it as an optional Week 2 extension — as-is it's well above course level.
- **Accessibility:** notebooks that produce visuals print a **text equivalent** of every picture and never rely on color alone (digits render as text-pictures; results print as tables with `CORRECT`/`WRONG` in words; the Week 8 "misleading chart" lesson is reproduced as text bars). For Week 9, the **text classifier is the accessible primary** — it's text end to end, so it reads cleanly with a screen reader / Braille / magnification — and **MNIST is an optional image-based companion** with text equivalents added. Charts/images in Colab carry no alt text, so the printed text *is* the equivalent.
