# Colab Notebooks (Units 8 & 9)

The Colab notebooks referenced from the Unit 8 and Unit 9 lessons, downloaded here for local editing. Each is provided as both the original `.ipynb` (as pulled from Google Drive) and a `.qmd` (Quarto markdown — easier to read and diff).

## Editing workflow

Edit the `.qmd`, then regenerate the notebook:

```bash
quarto convert unit8-l07-bar-charts.qmd      # -> unit8-l07-bar-charts.ipynb
```

It's lossless both ways, so you can also pull Colab edits back with `quarto convert <file>.ipynb`. (Conversion drops cell outputs and the Colab cell metadata, which is what you want for editing.)

> **Modernized (2026):** these notebooks were cleaned up for current pandas/matplotlib (verified to run on **pandas 3.0 / seaborn 0.13**). Changes: data now loads automatically from a URL (`pd.read_csv("https://drive.google.com/uc?export=download&id=…")`) instead of Colab's `files.upload()` / "drag the file in", so they run anywhere with no download; charts use **seaborn** (`countplot`, `histplot`, `scatterplot`, `heatmap`) with the object-oriented `ax.set(...)` style; and several patterns that broke on pandas 2.0+ were fixed (the `value_counts().reset_index()` bar idiom, `groupby().sum()` on mixed columns, `df.corr()` with text columns). Pie/donut charts stayed as Matplotlib (seaborn has none) but were modernized to use `wedgeprops`. The Unit 9 ML notebook was restructured from one big `main()` into a narrated cell-by-cell flow and now uses `train_test_split` instead of a positional slice.

## Notebooks

| File | Source lesson | Colab id | Likely dataset |
|------|---------------|----------|----------------|
| `unit8-l05-data-science-tools` | U8 L05 – Data Science Tools | `11A_yAiWweUhNVrI3eOpoxXLMIyj0vGQ-` | — |
| `unit8-l07-bar-charts` | U8 L07 – Bar Charts | `1uHCW-aGbJrGkMOCIfWRzy5X_T_zIVe1l` | dog-breed data |
| `unit8-l08-histograms` | U8 L08 – Histograms | `1qhxeARIxWPbV6iwTPjQJkvnZBb_yXQR2` | — |
| `unit8-l09-beatles-cleaning-data` | U8 L09 – Cleaning Data | `1H-00nzogW9W4fWYg8p_GQzM24quc7ejg` | `beatles.csv` |
| `unit8-l10-scatter-dogs` | U8 L10 – Scatter Plots | `1VM4tz72SqlyzZhP5KxWAYDMbcMEKSMDB` | dog data |
| `unit8-l10-scatter-states` | U8 L10 – Scatter Plots | `194L9nhtXEiRuCuwZ8j5Fyg2StsMKQJ03` | `states.csv` |
| `unit8-l11-crosstab-dogs` | U8 L11 – Cross Tabulation | `1DezeP54woxTGzAP72jqMNh-Xw0Maj4pc` | dog data |
| `unit8-l11-crosstab-words` | U8 L11 – Cross Tabulation | `12QZ6cpJGa_HR7HW-TD5yfBi5fhR5fBHZ` | — |
| `unit8-l12-beatles-choosing-chart` | U8 L12 – Choosing a Chart | `1c89X4YZlDavvXIqEQnUW4TlMi19Fc09l` | `beatles.csv` |
| `unit8-l13-sample` | U8 L13 – A05 Sample | `1iNEAtjchcz7GxStdH3Ooks3E_80f9DMU` | — |
| `unit8-l13-qr-sample` | U8 L13 – A05 Sample (QR) | `1BG8IW4Pzgx3qwskQGMq4maP3txGergzS` | `qr-sample-dogs.csv` |
| `unit9-l13-simple-ml-example` | U9 L13 – Simple ML Example | `1R0s74BuJjADzmDAJwLqTCRHVBM_17v6z` | `housing.csv` |

Open any original in Colab at `https://colab.research.google.com/drive/<colab id>`.

## datasets/

Local copies of the data the notebooks use. (The notebooks now load these straight from Drive URLs, so these files are here mainly for reference and offline running.)

- `dogs.csv` — dog breeds (life span, height, weight, breed group, …)
- `beatles.csv` — Beatles tracks (album, popularity, danceability, …)
- `states.csv` — US states (population, area, median household income, …)
- `words.csv` — English words (part of speech, length, frequency)
- `qr-sample-dogs.csv` — dog-breed adoption counts (the QR / Assignment 4 sample)
- `housing.csv` — California housing data (for the Unit 9 ML example)
- `8-types-of-bias-in-data.pdf` — a 9-page article linked from U8 L05 (reference reading, not a dataset)

*Note: `unit8-l11-crosstab-words` originally had a large pasted screenshot (a base64 PNG) embedded in its markdown — it was dropped during the modernization. Re-add it if it mattered.*
