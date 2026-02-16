# Pandas & Matplotlib Quick Reference

*A companion guide for the Unit 8 Colab notebooks*

---

You've been running code in Google Colab notebooks all unit -- loading CSV files, making bar charts, tweaking column names. The code was written for you, and that's fine. But if you've been wondering *what any of it actually means*, this is your reference.

Nothing here is required reading. Think of it as a decoder ring for the Python you've been copy-pasting.

---

## 1. What Are pandas and matplotlib?

At the top of every Colab notebook, you've seen these two lines:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

Here's what's happening:

- **pandas** is a *library* -- someone else's code that you can use in your own programs. pandas is specifically designed for working with tabular data (rows and columns, like a spreadsheet). The `as pd` part just gives it a shorter nickname so you don't have to type `pandas` every time.

- **matplotlib** is another library, this one for making charts and graphs. `matplotlib.pyplot` is the specific piece of matplotlib we use, and `as plt` is -- you guessed it -- just a nickname.

When you write `pd.read_csv(...)` or `plt.show()`, you're calling functions that live inside those libraries. That's it. You didn't write them, you don't need to understand their internals -- you just need to know what they do when you call them.

---

## 2. Loading and Looking at Data

### Loading a CSV file

```python
df = pd.read_csv("dogs.csv")
```

This reads a CSV file (comma-separated values -- the kind of file you can export from Google Sheets or Excel) and stores it in a variable called `df`. That variable holds a **DataFrame**, which is pandas's version of a table. Rows and columns, just like a spreadsheet.

The name `df` isn't special -- it's just a convention. You could call it `dogs` or `my_data` or `potato`. But most notebooks use `df` because it's short for DataFrame and everyone recognizes it.

### Peeking at your data

```python
df.head()
```

Shows the first 5 rows of your DataFrame. This is usually the first thing you do after loading data -- just a quick sanity check. *Does this look right? Are the columns what I expected?*

```python
df.shape
```

Tells you how many rows and columns your DataFrame has, as a pair of numbers like `(105, 8)` -- meaning 105 rows and 8 columns. Notice there are no parentheses after `shape` -- it's a property, not a function call. (Don't worry about the difference right now; just remember: no parentheses.)

```python
df.columns
```

Lists all the column names. Super helpful when you can't remember if the column is called `'Breed Group'` or `'BreedGroup'` or `'breed_group'`. Spelling and capitalization matter.

```python
df.describe()
```

Gives you basic statistics for every numeric column -- the mean (average), min, max, standard deviation, &c. A quick way to get a feel for your numbers without making any charts.

### Selecting a single column

```python
df['Max Life Span']
```

The square brackets with a column name pull out just that one column. You'll use this *constantly* -- almost every chart starts by selecting which column(s) you want to visualize.

The column name has to match *exactly* what's in your data (including spaces and capitalization). If you get a `KeyError`, it almost always means you misspelled the column name. Use `df.columns` to double-check.

---

## 3. Common Operations

### Counting unique values

```python
df['Breed Group'].value_counts()
```

Counts how many times each unique value appears in that column. If your `Breed Group` column has entries like "Working", "Sporting", "Terrier", &c., this tells you *how many dogs are in each group*. This is exactly what the bar chart notebooks do behind the scenes.

### Sorting

```python
df.sort_values('Max Weight')
```

Sorts the entire table by a column. By default it sorts smallest to largest. Add `ascending=False` to flip it:

```python
df.sort_values('Max Weight', ascending=False)
```

You saw this in Lesson 7 when we compared bar charts sorted by count vs. sorted alphabetically.

### Removing missing data

```python
df.dropna()
```

Removes any row that has missing data (empty cells). This is one of those "cleaning" steps from Lesson 9 -- real-world datasets almost always have gaps, and sometimes you need to drop those rows before your chart will work properly.

### Filtering rows

```python
df[df['Max Weight'] > 50]
```

This one looks weird. The inner part -- `df['Max Weight'] > 50` -- creates a True/False value for every row (is this dog's max weight greater than 50?). The outer brackets then keep only the rows where the answer is True.

So `df[df['Max Weight'] > 50]` gives you a new DataFrame containing *only* dogs heavier than 50 pounds. You can use other comparisons too: `<`, `>=`, `<=`, `==` (equals -- note the double equals sign), `!=` (not equal).

The double-bracket syntax is just how pandas does filtering. It's a little odd-looking but you get used to it.

---

## 4. Making Charts

Here's the pattern for each chart type you've used in Unit 8. They all follow the same basic recipe: prepare the data, call a plot function, add labels, show it.

### Bar Chart

**Good for:** Comparing categories. *How many dogs are in each breed group? Which breed group is most common?*

```python
counts = df['Breed Group'].value_counts()
counts.plot(kind='bar')
plt.title("Dog Breeds by Group")
plt.xlabel("Breed Group")
plt.ylabel("Count")
plt.show()
```

Line by line:
1. Count how many times each breed group appears
2. Plot those counts as a bar chart
3. Add a title
4. Label the x-axis
5. Label the y-axis
6. Display the chart

You can also make bar charts that show averages instead of counts (like the average max weight per breed group from Lesson 7) -- the notebook code handles that with a `groupby()`, which just means "group the data by this column and then calculate something for each group."

### Histogram

**Good for:** Seeing the distribution of a numeric variable. *Are most dogs light or heavy? Where do most values fall?* Use this when a bar chart would have too many individual bars (like plotting every unique weight).

```python
df['Max Weight'].plot(kind='hist', bins=10)
plt.title("Distribution of Max Weight")
plt.xlabel("Weight (lbs)")
plt.show()
```

The `bins` parameter controls how many buckets the data gets split into. Remember from Lesson 8 -- 5 bins vs. 10 bins can tell a very different story. Experiment to find what's most useful.

### Scatter Plot

**Good for:** Seeing the relationship between two numeric variables. *Do heavier dogs tend to have shorter lifespans? Is there a connection between a state's population and its area?*

```python
df.plot(kind='scatter', x='Max Weight', y='Max Life Span')
plt.title("Weight vs. Life Span")
plt.show()
```

Notice that scatter plots take *two* columns (x and y) -- that's the whole point. Each dot on the chart represents one row of your data, plotted at the intersection of its x-value and y-value.

### Crosstab Chart

**Good for:** Counting how often combinations of values from two columns appear together. *How many herding dogs have a max life span of 12 years?*

Crosstab charts use a slightly different setup -- they use `pd.crosstab()` plus a library called **seaborn** for the heatmap coloring:

```python
import seaborn as sns

ct = pd.crosstab(index=df['Breed Group'], columns=[df['Max Life Span']], margins=True)
sns.heatmap(ct, annot=True, fmt='d')
plt.title("Breed Group vs. Max Life Span")
plt.show()
```

The `annot=True` puts the actual numbers in each cell, and `fmt='d'` formats them as whole numbers. The `margins=True` adds row and column totals.

---

## 5. Putting It Together

Here's how all of these pieces work as a workflow. Let's say you've got a dataset of dogs and you want to explore it:

```python
# Step 1: Import the libraries
import pandas as pd
import matplotlib.pyplot as plt

# Step 2: Load the data
df = pd.read_csv("dogs.csv")

# Step 3: Take a look
df.head()
```

Running that, you might see something like:

| | Breed | Breed Group | Max Life Span | Max Weight | Max Height |
|---|---|---|---|---|---|
| 0 | Akita | Working | 12 | 130 | 28 |
| 1 | Beagle | Hound | 15 | 30 | 15 |
| 2 | Boxer | Working | 12 | 80 | 25 |
| 3 | Bulldog | Non-Sporting | 10 | 50 | 15 |
| 4 | Chihuahua | Toy | 20 | 6 | 9 |

```python
# Step 4: Check the size and columns
print(df.shape)       # (105, 5) -- 105 dogs, 5 columns
print(df.columns)     # lists all column names
```

Now let's say you're curious: *what's the distribution of max weights?* That's a question about one numeric column, so a histogram makes sense:

```python
# Step 5: Make a histogram
df['Max Weight'].plot(kind='hist', bins=5)
plt.title("Distribution of Max Weight")
plt.xlabel("Weight (lbs)")
plt.ylabel("Number of Breeds")
plt.show()
```

Looking at the histogram, you might notice that most dogs cluster in the lighter range (under 50 lbs) with a long tail stretching out to the heavy breeds. That tells you something: heavy dogs are relatively uncommon in this dataset.

Then maybe you wonder: *do heavier dogs have shorter lifespans?* That's a relationship between two numeric columns -- scatter plot time:

```python
# Step 6: Make a scatter plot
df.plot(kind='scatter', x='Max Weight', y='Max Life Span')
plt.title("Does Weight Affect Life Span?")
plt.xlabel("Max Weight (lbs)")
plt.ylabel("Max Life Span (years)")
plt.show()
```

If the dots trend downward from left to right, that suggests heavier dogs *do* tend to live shorter lives. That's a real pattern you can observe and report on with mathematical language -- exactly the kind of insight Lesson 12 asks you to find.

---

## Quick Troubleshooting

| Problem | Likely cause |
|---|---|
| `KeyError: 'column_name'` | You misspelled the column name. Check `df.columns`. |
| `FileNotFoundError` | The CSV file isn't uploaded to your Colab notebook, or the filename is wrong. |
| Nothing shows up when you run the chart code | You might be missing `plt.show()` at the end. |
| The chart looks squished or unreadable | Try changing `bins` (for histograms) or sorting your data differently (for bar charts). |
| `ModuleNotFoundError: No module named 'pandas'` | Rare in Colab (pandas is pre-installed), but if it happens, run `!pip install pandas` in a code cell. |

---

You don't need to memorize any of this. This is a reference -- come back to it when you're working on Assignment 4 or want to experiment in a Colab notebook. The goal isn't to become a pandas expert, it's to understand enough to not feel lost when you see this code.
