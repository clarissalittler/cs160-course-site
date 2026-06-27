# CS 160 — Weekly Low-Stakes Activities

Short, fun, completion-graded activities — one per week — that give students a reason to *play* with the week's idea. They line up with the course units. Coding activities are authored in [Quarto](https://quarto.org) (`.qmd`) and converted to Jupyter notebooks (`.ipynb`) that students open and run on **Google Colab**. Hands-on / writing activities are plain Markdown handouts.

## The activities

| Week | Unit | Activity | Format | Files |
|------|------|----------|--------|-------|
| 1 | Digital Information | **Mona Lisa Overdrive** — databend an image by opening it as audio in Audacity | Handout | `Week01_MonaLisaOverdrive.md` |
| 1 | Digital Information | **Broken Poetry** — watch text become ASCII numbers, transform them, turn them back | Notebook | `Week01_BrokenPoetry.qmd` → `.ipynb` |
| 2 | Internet & Web | **Make a Web Page** — build & share a real page on Neocities with hand-written HTML | Handout | `Week02_NeocitiesWebPage.md` |
| 3 | Python Intro | **Mad Libs Generator** — `input()`, strings, f-strings | Notebook | `Week03_MadLibs.qmd` → `.ipynb` |
| 4 | Loops / Iteration | **Personality Quiz** — `for` loops + accumulators | Notebook | `Week04_PersonalityQuiz.qmd` → `.ipynb` |
| 5 | Conditionals + Loops | **Text Adventure** — `while` loops + `if`/`elif`/`else` branching | Notebook | `Week05_TextAdventure.qmd` → `.ipynb` |
| 6 | Data Structures | **Collection Tracker** — list of dictionaries; sort/filter/count *(DRAFT — see ideas file)* | Notebook | `Week06_CollectionTracker.qmd` → `.ipynb` |
| 7 | Algorithms | **Beat the Computer** — binary vs. linear search; feel Big-O *(DRAFT — see ideas file)* | Notebook | `Week07_GuessingGame.qmd` → `.ipynb` |
| 8 | Data & Visualization | **Quantified Self** — track yourself in a Google Sheet, chart it (+ optional Python bonus) | Handout (+ notebook) | `Week08_QuantifiedSelf.md`, `Week08_QuantifiedSelf_Analysis.qmd` → `.ipynb` |
| 9 | Artificial Intelligence | **Delighted or Grumpy?** — train a text classifier on reviews, then try to fool it (accessible, text-only) | Notebook | `Week09_TextClassifier.qmd` → `.ipynb` |
| 9 | Artificial Intelligence | **MNIST** — train a neural network to read handwritten digits *(optional companion to the text classifier; image-based with text equivalents)* | Notebook | `Week09_MNIST.qmd` → `.ipynb` |
| 10 | Cybersecurity | **Investigate a Scam** — research one internet scam, write a field-guide post | Handout | `Week10_ScamInvestigation.md` |

**Blank weeks (6 & 7)** had no notes in the source, so each has an ideas file with three pitches plus one drafted starter notebook (the recommended pick): `Week06_IDEAS.md`, `Week07_IDEAS.md`.

## Authoring & converting

These were written as `.qmd` (Quarto markdown) and converted to `.ipynb` with:

```bash
quarto convert Week03_MadLibs.qmd      # produces Week03_MadLibs.ipynb
```

To regenerate every notebook from source:

```bash
for f in Week*.qmd; do quarto convert "$f"; done
```

Edit the `.qmd` (it's much nicer to read and diff than raw notebook JSON), then re-run the convert. The generated `.ipynb` files use a `python3` kernel and open directly in Colab.

## Notes for students (put these wherever you post the activity)

- **Open in Colab:** upload the `.ipynb` to [colab.research.google.com](https://colab.research.google.com), or push it to GitHub and use the Colab "open from GitHub" option.
- **Run a cell:** click it and press **Shift+Enter**. Run cells top to bottom, in order.
- **Share your work:** in Colab, **File → Share → "Anyone with the link can view,"** then post the link to the discussion thread.
- Every activity is **graded on completion**, not polish. If it runs and it's theirs, they're done.

## Design notes (for instructors)

- **Voice** matches the rest of the course: conversational, "smart friend explaining things," fun examples. Tweak freely per section.
- Each activity ends with **reflection questions** and a **discussion-thread share**, which carries the recurring *"who benefits, who's harmed, who decides?"* thread (especially Weeks 8, 9, 10).
- Notebooks lean on **standard Colab-preinstalled libraries** (`matplotlib`, `scikit-learn`, `tensorflow`). The MNIST notebook downloads ~11 MB and trains for a minute or two; the text classifier and everything else train in seconds.
- **Accessibility:** notebooks that produce visuals print a **text equivalent** of every picture and never rely on color alone (digits render as text-pictures; results print as tables with `CORRECT`/`WRONG` in words; the Week 8 "misleading chart" lesson is reproduced as text bars). For Week 9, the **text classifier is the accessible primary** — it's text end to end, so it reads cleanly with a screen reader / Braille / magnification — and **MNIST is an optional image-based companion** with text equivalents added. Charts/images in Colab carry no alt text, so the printed text *is* the equivalent.
