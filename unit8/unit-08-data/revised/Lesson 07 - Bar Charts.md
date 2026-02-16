# Lesson 7 --- Bar Charts

> **What you'll be able to do after this lesson:**
>
> - Create bar charts to visualize a single column of data.

## Bar charts

The first visualization we'll learn is the **bar chart**. Here's a question for you --- which of the following questions does this chart answer?

1. What is the most common maximum lifespan of a dog?
2. What approximate % of dogs live between a maximum of 12--14 years?
3. What is the fluffiest breed of dog?
4. What is the shortest maximum lifespan of a dog?
5. How long will my dog live?
6. What is the longest maximum lifespan of a cat?

<details>
<summary>Show Solution</summary>

Questions 1, 2, and 4 can be answered with the graph.

1. The most common lifespan of a dog is 15 years. Look for the tallest bar --- it's at position 15 on the x-axis. Now look at the y-axis; it looks like there's a count of either 24 or 25 dogs.
2. If you add up all of the counts, the result is 105 --- there are 105 dogs in the dataset. If you add up the bars for 12, 13, and 14 years, you get 22 + 13 + 23 = 58. Divide 58 by 105 to find the percentage: 58 / 105 = .5524 or ~55%.
4. The shortest maximum lifespan is 8 years. The longest is 20 years.

</details>

![Bar chart showing counts of max life span for dog breeds](images/chart2.png)
*Figure 8.10. Bar chart of counts of max life span*

Notice that questions 3, 5, and 6 can't be answered by this chart at all. Question 3 is about fluffiness --- there's no fluffiness data here. Question 5 asks about *your specific dog*, but the chart only shows breed maximums. And question 6? That's about cats. Wrong animal entirely.

## Information from bar charts

Bar charts are graphs for looking at values in **one column**. Here's what we can learn from them:

- What value(s) are most common in this column?
- What value(s) are least common in this column?
- What's the unique list of values in this column?

That's it. Simple tool, but surprisingly powerful.

## Building a Bar Chart in Code

Alright, let's actually *build* one of these things. We'll use the dogs dataset and create a bar chart of max life spans --- the same chart you've been reading above.

First, we need our two libraries:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

`pandas` is the library that handles the data --- loading it, counting things, sorting, &c. `matplotlib.pyplot` (which we nickname `plt`) is the library that draws the chart.

Next, load the dataset:

```python
df = pd.read_csv("dogs.csv")
```

This reads the CSV file into a DataFrame --- that big table of rows and columns we've been working with. Now here's where it gets interesting. We want to count how many dog breeds have each max life span value:

```python
counts = df['Max Life Span'].value_counts()
```

`value_counts()` looks at every value in the `'Max Life Span'` column and counts how many times each one appears. So if 24 breeds have a max life span of 15 years, it'll record `15: 24`. If 2 breeds max out at 8 years, it'll record `8: 2`. And so on for every unique value in the column.

By default, `value_counts()` sorts the results by count --- most common first, least common last. That's useful sometimes, but for a life span chart we probably want the x-axis to go in numerical order (8, 10, 11, 12, ...). So:

```python
counts = counts.sort_index()
```

`sort_index()` sorts by the values themselves (the life spans) rather than by how frequently they appear. Now 8 comes first, then 10, then 11, &c.

Finally, we plot it:

```python
counts.plot(kind='bar', figsize=(14, 8))
plt.xlabel("Max Life Span (years)")
plt.ylabel("Count")
plt.title("Count of Max Life Spans")
plt.show()
```

`plot(kind='bar')` creates the bar chart. `figsize=(14, 8)` just makes it big enough to read comfortably. The three `plt` lines add labels to the x-axis, y-axis, and the chart title --- without those, the chart would still *work*, but nobody reading it would know what they're looking at.

Here's the whole thing together:

```python
import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
df = pd.read_csv("dogs.csv")

# Count how many times each life span value appears
counts = df['Max Life Span'].value_counts()

# Sort by life span (not by count) so the x-axis goes in order
counts = counts.sort_index()

# Plot it
counts.plot(kind='bar', figsize=(14, 8))
plt.xlabel("Max Life Span (years)")
plt.ylabel("Count")
plt.title("Count of Max Life Spans")
plt.show()
```

What questions does this chart answer? Think about mathematical terms (percents, counts, averages, ranges, &c.) and units of measurement.

<details>
<summary>Show Solution</summary>

Here are a few examples:

- 24 dog breeds have a maximum life span of 15 years.
- The shortest maximum life span for a dog is 8 years.
- 24/105 or ~23% of dogs have a maximum life span of 15 years.
- 83/105 or ~79% of dogs have a maximum life span between 12 and 15 years.

It's important to express your observations in mathematical terms! Instead of thinking *"It looks like not very many dogs have a life span of 15 years"* (no mathematical terms there), try *"Only 24% of dogs have a maximum life span of 15 years."* Much more precise, and much more useful.

</details>

## Sorting order

Compare the two breed count charts below. Which one do you prefer, and why?

![Two bar charts side by side --- one sorted alphabetically by breed, the other sorted by count in descending order](images/barchart_compare.png)
*Figure 8.11. Sorting bar charts by name or by counts*

There may be reasons you prefer one over the other, but the graph on the right is usually preferred. It's sorted by counts in descending order rather than alphabetically by breed group. Sorting by column height makes it way easier to visually pick out the largest and smallest groups at a glance.

Here's how this works in code. When you call `value_counts()`, pandas already sorts by count (most common first). So if you just *don't* call `sort_index()`, you get the chart on the right:

```python
# Sorted by count (most common first) --- this is the default
counts = df['Breed Group'].value_counts()
counts.plot(kind='bar', figsize=(14, 8))
```

If you *do* call `sort_index()`, you get alphabetical order instead --- the chart on the left:

```python
# Sorted alphabetically by breed group name
counts = df['Breed Group'].value_counts().sort_index()
counts.plot(kind='bar', figsize=(14, 8))
```

So which should you use? It depends on what you're trying to show. For categories like breed groups, sorting by count is usually more useful --- you can instantly see which group is biggest and smallest. For numeric values like life spans, sorting by the value itself (`sort_index()`) makes more sense --- you want 8, 10, 11, 12, 13, 14, 15 in order, not jumbled by frequency.

## Breed group

Now try it yourself --- change `'Max Life Span'` to `'Breed Group'` in the bar chart code. Update the labels to match, and run it. What questions does this new graph answer? Think in mathematical terms --- percents, counts, averages, ranges, &c.

<details>
<summary>Show Solution</summary>

Here are a few examples:

- 10% of breeds in this sample are Terriers.
- Working dogs are the largest breed group.
- Mixed breeds have the lowest count of 3 dogs within the breed group.

</details>

## Calculating the sum or average of a column

So far we've been counting things --- how many breeds have each life span, how many breeds are in each group. But sometimes you don't want counts. Maybe you want to know the *average* max weight for each breed group. That's a different question, and it needs a slightly different approach.

```python
# Average max weight per breed group
avg_weight = df.groupby('Breed Group')['Max Weight'].mean()

avg_weight.plot(kind='bar', figsize=(14, 8))
plt.xlabel("Breed Group")
plt.ylabel("Average Max Weight (lbs)")
plt.title("Average Max Weight by Breed Group")
plt.show()
```

The new piece here is `groupby()`. Think of it like this: group all the rows by their breed group, then calculate the mean (average) of `'Max Weight'` within each group. So all the Terriers get averaged together, all the Working dogs get averaged together, &c. The result is one bar per breed group, where the bar height represents the average weight instead of a count.

![Bar chart showing average weights by breed](images/barchart1.png)
*Figure 8.12. Bar chart with weight averages*

Try changing the column name to find the average of other columns --- remember to change the labels to match!

## Try it yourself

Open the [Colab Notebook](https://colab.research.google.com/drive/1uHCW-aGbJrGkMOCIfWRzy5X_T_zIVe1l?usp=sharing) to try this yourself with the full dogs dataset. Make a copy, and experiment with different columns and sorting options.

In the next lesson, we'll learn how to visualize data with too many distinct values. For a sneak peek at the problem, try changing the column in your bar chart code to display `'Max Weight'`. Is the resulting chart easy to read?

![Bar chart of max weights with far too many bars to be readable](images/barchart2.png)
*Figure 8.13. Bar chart of max weights --- too many bars!*

Yeah... that's a mess. We're going to need a different tool for this. Stay tuned.

> **Need a refresher on the code?** The **Pandas & Matplotlib Quick Reference** has all the pandas and matplotlib functions from this unit in one place --- handy to keep open while you work.
