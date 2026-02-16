# Lesson 10 --- Scatter Plots

> **What you'll be able to do after this lesson:**
>
> - Build a scatter plot to compare two columns of numeric data
> - Build a range chart to compare numeric data against categorical data

## Two Columns of Data

Let's take another look at that Maximum Life Span chart. Can you tell what the max lifespan of a 55-pound dog is? What size dog tends to live the longest on average? Is there a *correlation* between a dog's size and how long it'll live?

![Bar chart with counts of Max Life Spans](images/chart2.png)
*Figure 8.15. Bar chart with counts of Max Life Spans*

Here's the thing --- bar charts and histograms are great, but they only show you *one* column of data at a time. If we want to explore the *relationship* between two pieces of information (like weight and lifespan), we're going to need a chart that can handle two columns simultaneously.

## Scatter Plots

Scatter plots show combinations of values from two **numeric** columns. They're especially useful for:

- Seeing patterns and trends between two numeric values
- Numeric data with lots of different values
- Continuous data --- no gaps between whole numbers, like weights

## Building a Scatter Plot in Code

Here's how we build a scatter plot from our dogs dataset:

```python
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("dogs.csv")

df.plot(kind='scatter', x='Max Weight', y='Max Life Span')
plt.xlabel("Max Weight (lbs)")
plt.ylabel("Max Life Span (years)")
plt.title("Max Weight vs Max Life Span")
plt.show()
```

Let's walk through what's happening here:

- We call `df.plot()` with `kind='scatter'` and specify which columns go on the x-axis and y-axis. That's really all it takes --- Pandas does the heavy lifting.
- Each dot on the chart is one dog breed. Its position shows both its max weight AND its max life span at the same time. That's the whole point --- we're plotting *two* pieces of information per data point.
- If the dots trend downward from left to right, that suggests heavier dogs tend to have shorter lifespans. Statisticians call this a **negative correlation**. If they trended *upward*, that'd be a positive correlation.
- One important thing to remember: scatter plots need **two numeric columns**. You can't scatter-plot a breed name against a weight --- that's not what this chart type is for. (We'll handle that case in a minute.)

So what's the plot below telling us about dog weight and lifespan?

![Scatter plot of Max Weight vs Max Life Span](images/scatter1.png)
*Figure 8.16. Scatter plot of Max Weight vs Max Life Span*

Look at the overall shape of the dots. Do they trend upward, downward, or is there no clear pattern? What does that tell you about the relationship between a dog's size and how long it lives?

## Range Charts

We can also use the scatter plot function to make a kind of range chart that shows ranges of values per category. This type of chart compares a **numeric** column with a **categorical** column --- so it covers that case we just said regular scatter plots can't handle.

Here's the code:

```python
df.plot(kind='scatter', x='Max Weight', y='Breed Group')
plt.axvline(x=25, color='r', label='Small - Medium')
plt.axvline(x=55, color='g', label='Medium - Large')
plt.xlabel("Max Weight (lbs)")
plt.ylabel("Breed Group")
plt.title("Max Weight by Breed Group")
plt.legend()
plt.show()
```

Most of this should look familiar by now, but there's a new function here: `plt.axvline()`. It draws a vertical line at a specific x-value. We're using it to mark the boundaries between small, medium, and large dogs --- one line at 25 lbs and another at 55 lbs. The `color` parameter sets the line color, and `label` gives it a name that shows up in the legend.

What does the chart below show?

![Range chart of Max Weight by dog breeds with vertical lines showing small, medium, and large boundaries](images/range.png)
*Figure 8.17. Range Chart of Max Weight of dogs per Breed group*

The vertical lines divide dogs into small (< 25 lbs), medium (25--55 lbs), and large (> 55 lbs) categories. You can see at a glance which breed groups tend to cluster in which size range --- and which groups have breeds all over the map.

## Activity 1 --- Dogs Scatter Plot

Time to try it yourself. Open up the [Dog Scatter Plot Colab Notebook](https://colab.research.google.com/drive/1VM4tz72SqlyzZhP5KxWAYDMbcMEKSMDB?usp=sharing) and make a copy.

Think about a question that might be answered by plotting two columns. Modify the program to use the two columns you chose. What question are you trying to answer? Were the results what you expected, or did something surprise you? What assumptions --- if any --- are you making when you read the plot?

## Activity 2 --- States Scatter Plot

![United States](images/usa.png)

In this activity, you're going to explore a new [dataset](https://drive.google.com/file/d/1VtvtFNBj1lEenTPGqmAiyix1bqxXTNlf/view?usp=sharing) with interesting data about the 50 states. You can work with a partner or tackle it solo.

Open up the [States Colab Notebook](https://colab.research.google.com/drive/194L9nhtXEiRuCuwZ8j5Fyg2StsMKQJ03?usp=sharing) and make a copy. Create the two scatter plots and answer the questions in the notebook.

If you have any questions, post them on the Ask Questions! discussion topic.

> **Need a refresher on the code?** The **Pandas & Matplotlib Quick Reference** has all the pandas and matplotlib functions from this unit in one place --- handy to keep open while you work.
