# Lesson 11 --- Cross Tabulation Charts

> **What you'll be able to do after this lesson:**
>
> - Create a crosstab chart to display counts of how many times combinations of values appear in a dataset
> - Use Seaborn to turn a crosstab into a heatmap for easier pattern recognition

## Crosstab

A crosstab --- short for cross-tabulation --- chart counts how many times *combinations* of values appear. It's like asking "how often do these two things show up together?"

Try answering these questions using the crosstab chart below:

1. How many "Herding" breeds live a maximum of 12 years?
2. What's the most common maximum life span for "Working" breeds?
3. Which breed group lives the shortest?
4. Which breed group lives the longest?
5. How do you know? How confident are you in your answers?

<details>
<summary>Show Solution</summary>

All of the questions can be answered with the graph!

</details>

![Crosstab chart showing breed group for rows and max life spans for columns](images/crosstab.png)
*Figure 8.18. Crosstab Chart --- Counts of Max Life Spans per Breeding Group*

## Information from Crosstab Charts

Crosstab charts count how often pairs of values in two columns appear together. Think of it as a grid where every cell answers "how many times did *this* value from column A show up with *that* value from column B?"

**Useful for:**

- Finding the most or least common combinations of values across two columns
- Spotting patterns between two columns
- Exploring two columns when one or both contain strings (text)
- Discrete data (counts)

**Not so useful:**

- If either column has too many values --- the chart would become enormous and unreadable

## Building a Crosstab Chart in Code

All those bar charts and histograms we've been making use Matplotlib's plotting functions. Crosstabs are a little different --- Pandas can build the entire table for us without needing a charting library at all. Here's the code:

```python
import pandas as pd

df = pd.read_csv("dogs.csv")

ct = pd.crosstab(index=df['Breed Group'], columns=df['Max Life Span'], margins=True)
print(ct)
```

Let's walk through what `pd.crosstab()` is doing:

- It takes two columns and counts how many times each combination appears. Every cell in the resulting grid answers "how many breeds in this group have this life span?"
- `index=` is what goes on the **rows**. Here that's the breed groups --- Herding, Hound, Sporting, &c.
- `columns=` is what goes on the **columns**. Here that's the different max life spans --- 8, 10, 12, &c.
- `margins=True` adds row and column totals --- those are the "All" row at the bottom and the "All" column on the right. They're handy for quick sanity checks and for computing percentages.

That's it. One function call, and Pandas does all the counting for you. No loops, no manual tallying --- just tell it which two columns you're curious about and it builds the grid.

You're not limited to life spans, either. You could swap in any other column to explore different relationships. For example:

```python
pd.crosstab(index=df['Breed Group'], columns=df['Bred For'])
```

That would show you what different breed groups were originally bred for --- herding livestock, hunting, companionship, &c. Same idea, different question.

## Adding a Heatmap with Seaborn

The raw numbers in a crosstab table work fine, but they're not exactly easy to scan at a glance. That's where Seaborn comes in --- it's a Python library that builds on top of Matplotlib and adds some really nice visualization tools. One of the best is the **heatmap**, which color-codes the cells so patterns jump out visually.

```python
import seaborn as sns
import matplotlib.pyplot as plt

ct = pd.crosstab(index=df['Breed Group'], columns=df['Max Life Span'])
sns.heatmap(ct, annot=True, fmt='d')
plt.title("Max Life Span by Breed Group")
plt.show()
```

Here's what's going on with those arguments:

- `sns.heatmap()` takes the crosstab table and turns it into a color-coded grid. Darker or brighter cells represent higher counts.
- `annot=True` puts the actual numbers inside each cell. Without it, you'd just get colors with no labels --- pretty, but not very informative.
- `fmt='d'` formats those numbers as whole numbers (integers). Without this, you'd get numbers like `3.0` instead of `3`, which looks a bit odd for counts.

The big win here is speed of pattern recognition. Scanning a grid of numbers and trying to spot which cells are large or small is tedious. But when the high-count cells are visually distinct from the low-count cells? Much easier to see what's going on --- your eyes do the work for you.

## Activity 1 --- Dogs Crosstab

Open the [Dogs Crosstab Colab Notebook](https://colab.research.google.com/drive/1DezeP54woxTGzAP72jqMNh-Xw0Maj4pc?usp=sharing) and make a copy. Run the program to see how it works. What other questions can you answer about Breed Groups?

Try modifying the column name to investigate different relationships:

![pd.crosstab code showing where to change the column name](images/crosstab1.png)

Swap in a different column and see what the crosstab reveals. Does the heatmap make it easier to spot patterns than the raw table?

## Activity 2 --- Words

![Word cloud with parts of speech](images/word_cloud.png)

On your own or with a partner, you're going to explore a new dataset with data about popular words and parts of speech. Open up the [Words Colab Notebook](https://colab.research.google.com/drive/12QZ6cpJGa_HR7HW-TD5yfBi5fhR5fBHZ?usp=sharing) and make a copy. Build the crosstab chart (fill in the columns to use) and answer the questions in the notebook.

If you have any questions, post them on the Ask Questions! discussion topic.

> **Need a refresher on the code?** The **Pandas & Matplotlib Quick Reference** has all the pandas and matplotlib functions from this unit in one place --- handy to keep open while you work.
