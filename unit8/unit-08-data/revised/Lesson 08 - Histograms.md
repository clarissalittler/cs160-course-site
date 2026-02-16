# Lesson 8 --- Histograms

> **What you'll be able to do after this lesson:**
>
> - Create a histogram to visualize numeric data when a bar chart would be too cluttered to read.

## Histograms

Histograms look a lot like bar charts, but there's a key difference: before anything gets plotted, all the numbers in a range (called a **bin**) get grouped together first. In Pandas, we can specify how many bins to use. The white space between each bar is just for readability --- it doesn't represent a gap in the data.

Look at the two charts below. What are the differences? Which chart is more useful?

![Histograms of max weights with 5 bins and 10 bins side by side](images/histogram.png)
*Figure 8.14. Histograms with 5 and 10 bins*

The histogram on the left splits the data into 5 buckets --- so weights of 47, 50, 77, and 81 would all land in the same bin between 46 and 83. That's the whole idea: we're trading precision for readability.

**Questions:**

- Why do you think I chose 5 bins for this chart?
- What is the most common range of maximum weights for dog breeds?
- What is the least common range of maximum weights for dog breeds?

<details>
<summary>Show Solution</summary>

- Using 5 bins, I get a good picture of the variety in weights. Using 10 bins doesn't really give me any additional useful information.
- The most common range is around 5--46 pounds. More dogs have weights in this bin than in any of the other bins.
- The least common range is around 124--198 pounds. (Those are some big dogs.)

</details>

## Information from histograms

Histograms can **only** be created with numeric data --- you can't bin text categories. They're especially useful when a normal bar chart would be too cluttered to read (remember that messy Max Weight bar chart from last lesson?).

Here's what we can learn from histograms:

- What range of values are most common in this column?
- What range of values are least common in this column?
- What ranges of values do or don't appear in this column?

Notice how this is subtly different from bar charts. Bar charts tell you about *specific values* --- histograms tell you about *ranges*. It's like the difference between asking "how many people are exactly 5'10"?" versus "how many people are between 5'8" and 6'0"?" The histogram question is often more useful in practice.

## Building a Histogram in Code

Alright, let's actually build one. Here's the code to create a histogram of maximum dog weights:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dogs.csv")

df['Max Weight'].plot(kind='hist', bins=10)
plt.xlabel("Max Weight (lbs)")
plt.ylabel("Number of Breeds")
plt.title("Distribution of Max Weight")
plt.show()
```

Let's walk through what's happening:

- **`df['Max Weight']`** --- we're selecting just one column from our dataframe. Histograms work with a single column of numeric data at a time.
- **`.plot(kind='hist')`** --- this tells pandas "I want a histogram, please." That's it. Pandas and matplotlib handle all the binning and drawing behind the scenes.
- **`bins=10`** --- this tells pandas to split the entire range of weights into 10 equally-sized buckets. Each bar's height shows how many dog breeds fell into that bucket.
- **The `plt` lines** --- these add axis labels and a title. Always label your axes! A chart without labels is like a sentence without a subject --- technically it exists, but nobody knows what it's trying to say.

### Experimenting with Bins

Here's where it gets interesting. Try changing `bins=10` to `bins=5`, or `bins=20`, or even `bins=50`. You'll get very different pictures of the *exact same data*.

- **Too few bins** (like 3 or 5) and you lose detail --- everything gets smashed together and you can't see the shape of the distribution.
- **Too many bins** (like 50) and it starts looking like a messy bar chart again --- the very problem we were trying to solve.
- **Somewhere in the middle** is usually right, but there's no magic formula. Finding the right number of bins is part art, part judgment. You try a few values, look at the results, and pick whichever one tells the clearest story.

This is one of those things where you just have to experiment. Change the number, look at the chart, ask yourself "does this help me see something useful?" If yes, great. If not, try a different number.

### Changing the Column

Want to look at a different column? Same recipe, different ingredient:

```python
df['Max Life Span'].plot(kind='hist', bins=8)
plt.xlabel("Max Life Span (years)")
plt.ylabel("Number of Breeds")
plt.title("Distribution of Max Life Span")
plt.show()
```

That's the nice thing about pandas --- once you know the pattern, you can reuse it. Swap out the column name, update your labels to match, pick a reasonable number of bins, and you've got a brand new histogram. The structure of the code doesn't change; just the specifics.

## Try It Yourself

Open this [Colab Notebook](https://colab.research.google.com/drive/1qhxeARIxWPbV6iwTPjQJkvnZBb_yXQR2?usp=sharing) and make a copy. You've seen how the code works --- now get your hands on it. Try modifying the number of bins to see what happens. There's no single "right" number, but some choices definitely tell a better story than others.

Make a histogram for another column in the Dogs table and decide on the number of bins that helps you find an interesting pattern. Answer the questions in the notebook text box.

> **Need a refresher on the code?** The **Pandas & Matplotlib Quick Reference** has all the pandas and matplotlib functions from this unit in one place --- handy to keep open while you work.
