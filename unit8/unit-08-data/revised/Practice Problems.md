# Practice Problems

These problems cover the key ideas from Unit 8 --- data literacy, chart types, pandas basics, and data cleaning. They're designed to test your *understanding*, not your ability to write code from scratch. Think of them as the kind of questions that might show up on an exam: you'll need to read charts, interpret code, and reason about data.

> **Important!** Try each problem on your own before peeking at the solution. Struggling with a problem --- even getting it wrong at first --- is where the real learning happens. You'll get way more out of these if you give each one an honest shot before clicking "Solution."

---

## Question #1 --- Chart Selection

For each scenario below, decide which chart type would be the **best** choice: **bar chart**, **histogram**, **scatter plot**, or **crosstab**. Explain *why* that chart type fits the question better than the others.

**(a)** You want to see how many dog breeds are in each breed group (Herding, Hound, Sporting, &c.).

**(b)** You want to see if there's a relationship between a dog's maximum weight and its maximum life span.

**(c)** You want to see the distribution of maximum weights across all dog breeds, but there are too many distinct weight values to display individually.

**(d)** You want to know how many breeds in each breed group have each possible maximum life span value.

**(e)** You want to know the average maximum weight for each breed group.

<details>
<summary>Solution</summary>

**(a) Bar chart.** You're looking at one column of categorical data (Breed Group) and counting how many breeds fall into each category. That's exactly what bar charts do --- show counts for discrete categories. A histogram wouldn't work because breed group names aren't numeric. A scatter plot needs two numeric columns. A crosstab *could* work but is overkill when you only care about one column.

**(b) Scatter plot.** You're comparing two numeric columns --- Max Weight (x-axis) and Max Life Span (y-axis). Each dot represents one breed, and you can see whether the dots trend upward (positive correlation) or downward (negative correlation). No other chart type lets you visualize the relationship between two numeric variables this directly.

**(c) Histogram.** When a bar chart would have way too many individual bars (imagine a separate bar for every distinct weight value --- that's a mess), a histogram groups the values into bins and shows you the distribution across ranges. You lose some precision, but you gain readability. This is the classic "too many values for a bar chart" scenario.

**(d) Crosstab.** You're looking at combinations of two columns --- Breed Group (categorical) and Max Life Span (numeric but discrete). A crosstab builds a grid where each cell answers "how many breeds in *this* group have *that* life span?" It's perfect for exploring how two columns interact, especially when at least one is categorical.

**(e) Bar chart (with `groupby().mean()`).** This is a bar chart, but instead of counting breeds per group, you're showing the *average* max weight per group. Each bar represents one breed group, and the bar height shows the mean weight. You'd use `df.groupby('Breed Group')['Max Weight'].mean()` to calculate the averages and then plot them as a bar chart.

</details>

---

## Question #2 --- Reading a Bar Chart

Suppose you run `value_counts()` on the `'Breed Group'` column of the dogs dataset, and you get this result:

| Breed Group   | Count |
|---------------|-------|
| Working       | 19    |
| Sporting      | 18    |
| Herding       | 16    |
| Terrier       | 11    |
| Toy           | 11    |
| Hound         | 10    |
| Non-Sporting  | 10    |
| Mixed         | 3     |

Imagine this data as a bar chart sorted by count (tallest bar on the left, shortest on the right).

**(a)** Which breed group is the most common in this dataset? Which is the least common?

**(b)** What is the range of counts (the difference between the largest and smallest)?

**(c)** What percentage of the total does the "Working" group represent? Round to the nearest whole number.

**(d)** Two pairs of breed groups are tied. Which groups are tied, and at what counts?

<details>
<summary>Solution</summary>

**(a)** The most common breed group is **Working** with 19 breeds. The least common is **Mixed** with only 3 breeds.

**(b)** The range is 19 - 3 = **16**. That's a pretty big spread --- the largest group has more than six times as many breeds as the smallest.

**(c)** First, find the total: 19 + 18 + 16 + 11 + 11 + 10 + 10 + 3 = **98** breeds. Then divide: 19 / 98 = 0.1939, or about **19%**. So roughly one in five breeds in this dataset is a Working dog.

**(d)** **Terrier and Toy** are tied at 11 each, and **Hound and Non-Sporting** are tied at 10 each. On a bar chart, these pairs would have bars of the same height.

</details>

---

## Question #3 --- Histogram Bins

Here are the maximum weights (in pounds) for 15 dog breeds from the dataset:

> 8, 12, 18, 24, 35, 45, 50, 55, 60, 75, 80, 95, 110, 150, 180

The minimum value is 8 and the maximum is 180, so the full range is 172 pounds.

**(a)** If you create a histogram with **3 bins**, each bin covers about 57 pounds. Fill in the counts:

- Bin 1 (8--65 lbs): \_\_\_ breeds
- Bin 2 (66--123 lbs): \_\_\_ breeds
- Bin 3 (124--180 lbs): \_\_\_ breeds

**(b)** Now try **6 bins**, where each bin covers about 29 pounds:

- Bin 1 (8--36 lbs): \_\_\_ breeds
- Bin 2 (37--65 lbs): \_\_\_ breeds
- Bin 3 (66--94 lbs): \_\_\_ breeds
- Bin 4 (95--123 lbs): \_\_\_ breeds
- Bin 5 (124--151 lbs): \_\_\_ breeds
- Bin 6 (152--180 lbs): \_\_\_ breeds

**(c)** What pattern becomes visible with 6 bins that's hidden with 3 bins?

<details>
<summary>Solution</summary>

**(a)** With 3 bins:

- Bin 1 (8--65 lbs): **9** breeds (8, 12, 18, 24, 35, 45, 50, 55, 60)
- Bin 2 (66--123 lbs): **4** breeds (75, 80, 95, 110)
- Bin 3 (124--180 lbs): **2** breeds (150, 180)

With 3 bins, all you can really see is "most dogs are on the lighter end, and the count drops off as weight increases." That's true, but it's pretty vague.

**(b)** With 6 bins:

- Bin 1 (8--36 lbs): **4** breeds (8, 12, 18, 24)
- Bin 2 (37--65 lbs): **5** breeds (35, 45, 50, 55, 60)
- Bin 3 (66--94 lbs): **2** breeds (75, 80)
- Bin 4 (95--123 lbs): **2** breeds (95, 110)
- Bin 5 (124--151 lbs): **1** breed (150)
- Bin 6 (152--180 lbs): **1** breed (180)

**(c)** With 6 bins, you can see that the small-to-medium range (8--65 lbs) isn't just one big lump --- it's actually two clusters. Bins 1 and 2 have the highest counts (4 and 5), while everything above 65 lbs drops off sharply. The 3-bin version hides this by lumping all 9 light-to-medium dogs into one bar. More bins let you see the *shape* of the distribution more clearly --- there's a concentration of breeds in the 37--65 lb range that's invisible with fewer bins.

This is exactly why experimenting with the `bins` parameter matters. There's no single "right" number --- but some choices tell a clearer story than others.

</details>

---

## Question #4 --- Reading a Scatter Plot

A scatter plot of the dogs dataset has **Max Weight** on the x-axis and **Max Life Span** on the y-axis. Here's what the pattern looks like:

- Dogs on the **left** side of the chart (lighter dogs, 5--30 lbs) tend to have dots clustered **high** on the y-axis (around 13--20 years).
- Dogs on the **right** side of the chart (heavier dogs, 80--180 lbs) tend to have dots clustered **low** on the y-axis (around 8--12 years).
- Overall, the dots trend **downward** from left to right.

**(a)** Is this a positive correlation or a negative correlation?

**(b)** In plain English, what does this pattern suggest about the relationship between a dog's weight and its lifespan?

**(c)** A friend looks at this chart and says: "Heavy dogs die younger *because* they're heavy. Being heavier *causes* a shorter lifespan." Is this a valid conclusion from the scatter plot? Why or why not?

**(d)** Can you think of an alternative explanation for the pattern --- something other than "weight directly causes shorter lifespan"?

<details>
<summary>Solution</summary>

**(a)** This is a **negative correlation**. As one variable increases (weight goes up), the other tends to decrease (life span goes down). If the dots trended *upward* from left to right, that would be a positive correlation.

**(b)** The pattern suggests that **lighter dogs tend to live longer than heavier dogs**. Small breeds (like Chihuahuas and Toy Poodles) tend to cluster in the upper-left corner of the chart --- light and long-lived. Large breeds (like Great Danes and Mastiffs) tend to cluster in the lower-right --- heavy and shorter-lived.

**(c)** No, this is **not** a valid conclusion. The scatter plot shows a **correlation** --- two things that tend to go together --- but correlation does not prove **causation**. Just because two variables move together doesn't mean one *causes* the other. The scatter plot can tell you "these things are related," but it can't tell you *why*.

**(d)** There are several alternative explanations. Maybe larger breeds have been selectively bred in ways that introduce health problems (like hip dysplasia in large breeds). Maybe it's a fundamental biological thing --- larger animals' organs have to work harder. Maybe certain genetic factors affect both size and longevity independently. The point is: the data alone can't tell us which explanation is right. You'd need a controlled experiment or a much deeper analysis to start making causal claims. A scatter plot is a starting point for asking better questions, not an ending point for drawing conclusions.

</details>

---

## Question #5 --- pandas Code Reading

For each code snippet below, describe in plain English what it does and what the output would look like. Assume `df` is a DataFrame loaded from the dogs dataset with columns including `Name`, `Breed Group`, `Max Life Span`, `Max Weight`, &c.

**(a)**
```python
df['Max Weight'].value_counts()
```

**(b)**
```python
df.groupby('Breed Group')['Max Life Span'].mean()
```

**(c)**
```python
df.plot(kind='scatter', x='Max Weight', y='Max Life Span')
plt.xlabel("Max Weight (lbs)")
plt.ylabel("Max Life Span (years)")
plt.title("Weight vs Life Span")
plt.show()
```

**(d)**
```python
pd.crosstab(index=df['Breed Group'], columns=df['Max Life Span'])
```

**(e)**
```python
df['Breed Group'].value_counts().sort_index()
```

<details>
<summary>Solution</summary>

**(a)** This looks at every value in the `Max Weight` column and counts how many times each weight appears. The output is a list of weight values paired with their counts, sorted from most common to least common. For example, if 8 breeds have a max weight of 50 lbs, you'd see `50: 8`. It answers the question "how many breeds share each max weight value?"

**(b)** This groups all the rows by their `Breed Group`, then calculates the average (mean) of the `Max Life Span` column within each group. The output is a list of breed groups, each paired with a single number --- the average max life span for breeds in that group. For example, you might see `Toy: 14.8` and `Working: 11.2`. It answers the question "which breed groups live the longest on average?"

**(c)** This creates a scatter plot with `Max Weight` on the x-axis and `Max Life Span` on the y-axis. Each dot represents one dog breed --- its horizontal position shows its weight and its vertical position shows its life span. The three `plt` lines add labels to the x-axis, y-axis, and chart title so a reader knows what they're looking at. `plt.show()` displays the chart on screen.

**(d)** This builds a cross-tabulation table with `Breed Group` as the rows and `Max Life Span` as the columns. Each cell in the grid contains a count --- how many breeds in that group have that particular max life span. For example, the cell at row "Herding" and column "12" would tell you how many Herding breeds have a max life span of 12 years.

**(e)** This counts how many breeds are in each breed group (just like `value_counts()` always does), but then `sort_index()` re-sorts the results alphabetically by breed group name instead of by count. So instead of seeing the most common group first, you'd see them in order: Herding, Hound, Mixed, Non-Sporting, Sporting, Terrier, Toy, Working. The counts are still there --- they're just in a different order.

</details>

---

## Question #6 --- Data Cleaning Scenario

You've been given a dataset of student survey responses. Here are the first few rows:

| Name       | Year      | Major              | GPA  | Credits |
|------------|-----------|---------------------|------|---------|
| Alice      | Sophomore | Computer Science    | 3.5  | 45      |
| Bob        | Jr.       | computer science    | 3.2  | 60      |
| Charlie    | Junior    | CS                  |      | 58      |
| Diana      | Sophomore | Biology             | 3.8  | 45      |
| Eve        | Sophomore | Computer Science    | 3.5  | 45      |
| Alice      | Sophomore | Computer Science    | 3.5  | 45      |
| Frank      |           | Math                | four | 30      |

**(a)** Identify **all** the problems you can see in this dataset. (There are at least five distinct issues.)

**(b)** For each problem, describe how you would clean it --- what would you change and why?

**(c)** Why is it important to clean data *before* creating visualizations or doing analysis? What could go wrong if you skip this step?

<details>
<summary>Solution</summary>

**(a)** Here are the problems:

1. **Inconsistent formatting in the Year column:** "Jr." and "Junior" mean the same thing, but the computer treats them as two completely different values.
2. **Inconsistent formatting in the Major column:** "Computer Science", "computer science", and "CS" all refer to the same major, but they'd show up as three separate categories.
3. **Missing data:** Charlie's GPA is blank, and Frank's Year is blank. These empty cells will cause problems in calculations and charts.
4. **Invalid data type:** Frank's GPA is "four" instead of 4.0. You can't calculate an average when one of the values is a word.
5. **Duplicate row:** Alice's row appears twice (rows 1 and 6 are identical). This would double-count her in any analysis.

**(b)** How to clean each problem:

1. **Year inconsistency:** Pick one standard format and stick with it. Change "Jr." to "Junior" (or vice versa) so all third-year students are represented the same way.
2. **Major inconsistency:** Standardize all variations to one spelling --- "Computer Science" with consistent capitalization. Change "computer science" and "CS" to match.
3. **Missing data:** You have a few options. You could remove the rows with missing data entirely (if you have enough data that losing a couple rows doesn't hurt). You could fill in the missing values if you have another way to look them up. Or you could leave them blank but be aware they'll be excluded from certain calculations (like averages). What you *shouldn't* do is just ignore the problem and hope it goes away.
4. **Invalid data type:** Change "four" to `4.0` so it's a number the computer can work with. The GPA column needs to be entirely numeric for any math to work.
5. **Duplicate row:** Remove one of the two identical Alice rows. Duplicates inflate your counts and skew your averages.

**(c)** If you skip cleaning:

- A bar chart of majors would show "Computer Science", "computer science", and "CS" as three separate bars instead of one --- making it look like fewer students are CS majors than there actually are.
- An average GPA calculation would either crash (because "four" isn't a number) or silently exclude that row, depending on the tool.
- Duplicate rows would make it look like there are more responses than there actually are, inflating counts and skewing percentages.
- Missing data could cause functions to produce unexpected results or errors.

The bottom line: garbage in, garbage out. If your data is messy, your charts and statistics will be misleading --- and you might not even realize it. Cleaning data isn't the fun part, but it's what makes everything else trustworthy.

</details>
