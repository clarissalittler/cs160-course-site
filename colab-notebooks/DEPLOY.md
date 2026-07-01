# Deploying the modernized notebooks

The Unit 8 / Unit 9 lessons link to Colab notebooks by their Drive URL
(`colab.research.google.com/drive/<id>`). The modernized versions live in this
folder as `.ipynb` files. To get students the modernized versions, the new
content has to reach those Drive files. There are two ways; **Method A keeps the
existing lesson links working untouched** and is the one to try first.

## Method A — replace the file content, keep the same link (preferred)

This swaps in the new notebook *without changing the URL*, so no lesson edits are
needed.

1. In **Google Drive**, find the notebook (search by the id in the table below).
2. Right-click it → **Manage versions** → **Upload new version**.
3. Choose the matching `.ipynb` from this folder.

The share link is unchanged, so every lesson that points at it now serves the
modernized notebook. Do a quick **Runtime → Run all** afterward to confirm it runs
clean (they were all verified on pandas 3.0 / seaborn 0.13).

> If "Manage versions" isn't offered for a given notebook (some Colab-native files
> don't expose it), use Method B for just that one.

## Method B — upload as a new notebook, update the one link

1. In **Colab**: **File → Upload notebook** → choose the `.ipynb` from this folder.
2. Colab saves it to Drive with a **new** URL. Copy that URL (Share → Copy link).
3. Edit the matching lesson file below and replace the old `drive/<id>` URL with the
   new one. There's exactly one link per lesson, so it's a single find-and-replace.

## Mapping: lesson → current link id → modernized notebook

| Lesson file | Current Colab id (in the link) | Upload this notebook |
|---|---|---|
| `unit8/.../Lesson 03 - Data Science Tools.html` | `11A_yAiWweUhNVrI3eOpoxXLMIyj0vGQ-` | `unit8-l05-data-science-tools.ipynb` |
| `unit8/.../Lesson 05 - Bar Charts.html` | `1uHCW-aGbJrGkMOCIfWRzy5X_T_zIVe1l` | `unit8-l07-bar-charts.ipynb` |
| `unit8/.../Lesson 06 - Histograms.html` | `1qhxeARIxWPbV6iwTPjQJkvnZBb_yXQR2` | `unit8-l08-histograms.ipynb` |
| `unit8/.../Lesson 07 - Cleaning Data.html` | `1H-00nzogW9W4fWYg8p_GQzM24quc7ejg` | `unit8-l09-beatles-cleaning-data.ipynb` |
| `unit8/.../Lesson 08 - Scatter Plots.html` (dogs) | `1VM4tz72SqlyzZhP5KxWAYDMbcMEKSMDB` | `unit8-l10-scatter-dogs.ipynb` |
| `unit8/.../Lesson 08 - Scatter Plots.html` (states) | `194L9nhtXEiRuCuwZ8j5Fyg2StsMKQJ03` | `unit8-l10-scatter-states.ipynb` |
| `unit8/.../Lesson 09 - Cross Tabulation Charts.html` (dogs) | `1DezeP54woxTGzAP72jqMNh-Xw0Maj4pc` | `unit8-l11-crosstab-dogs.ipynb` |
| `unit8/.../Lesson 09 - Cross Tabulation Charts.html` (words) | `12QZ6cpJGa_HR7HW-TD5yfBi5fhR5fBHZ` | `unit8-l11-crosstab-words.ipynb` |
| `unit8/.../Lesson 10 - Choosing a Chart.html` | `1c89X4YZlDavvXIqEQnUW4TlMi19Fc09l` | `unit8-l12-beatles-choosing-chart.ipynb` |
| `unit8/.../Lesson 11 - Data Analysis Examples.html` | `1iNEAtjchcz7GxStdH3Ooks3E_80f9DMU` | `unit8-l13-sample.ipynb` |
| `unit8/.../Lesson 11 - Data Analysis Examples.html` (QR) | `1BG8IW4Pzgx3qwskQGMq4maP3txGergzS` | `unit8-l13-qr-sample.ipynb` |
| `unit9/.../Lesson 03 - Fitting a Line.html` (optional link) | `1R0s74BuJjADzmDAJwLqTCRHVBM_17v6z` | `unit9-l13-simple-ml-example.ipynb` |

## Lesson prose already updated to match

Two lessons described the *old* workflow and have been updated in the repo so they
match the modernized notebooks once deployed:

- **U8 L05 (Bar Charts)** — the "Sorting order" steps no longer tell students to
  edit `value_counts().to_frame('count').reset_index()` / `sort_values('index')`
  (that code is gone). They now change the `order=` argument in `sns.countplot()`.
  The old `notebook1.png` / `notebook2.png` screenshots are now unreferenced.
- **U9 housing notebook** — the old Lesson 13 was archived in the Unit 9 rewrite; the
  notebook is now linked (optionally) from the new **Lesson 03 - Fitting a Line**, and
  loads its data from a URL (no drag-and-drop).
