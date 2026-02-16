# Lesson 5 --- Data Science Tools

> **What you'll be able to do after this lesson:**
>
> - Create a Google Colab computational notebook and start running Python in it.
> - Read basic pandas code and understand what each line does.

## Computational notebooks

Data scientists use something called *computational notebooks* with Python. Think of them as laboratory notebooks, but for scientific computing --- instead of scribbling observations on paper, you're writing code and seeing results right there in the same document.

The most popular flavor is **Jupyter Notebooks**. We'll be using [Google Colab](https://colab.research.google.com/), which stores Jupyter Notebooks in your Google Drive. It's free, it runs in your browser, and you don't have to install anything. Pretty great deal.

Open up [Google Colab](https://colab.research.google.com/) and create a notebook. Click the **New Notebook** button, or if you're already in Colab, go to **File > New Notebook**.

![Creating a Google Colab notebook](images/new_notebook.png)
*Figure 8.4. Creating a Google Colab notebook*

Write a Python statement to print "Hello" and then click the play button to run it.

![Running a Python statement in Google Colab](images/google_colab.png)
*Figure 8.5. Python statement*

All of your notebooks will live in your Google Drive inside a folder called **Colab Notebooks** --- Google Colab creates it for you automatically.

> **Note:** You're not expected to become a Colab expert or master any of the tools in this unit. The goal is to learn how to find patterns in visualizations of data. All the code has been written for you. Your job is to choose the right visualization for the questions you want to answer!

## Pandas

[Pandas](https://pandas.pydata.org/docs/reference/frame.html) is a fast, powerful, flexible, and easy-to-use open-source data analysis tool built on top of Python. Using Pandas, we'll convert comma-separated files (CSV) into *dataframes* --- basically fancy tables that Python can work with. Pandas also has functions to create charts and graphs to visualize data.

To use Pandas, import the library at the top of your notebook and run the cell:

```python
import pandas as pd
```

![Importing the Pandas library](images/pandas.png)
*Figure 8.6. Adding a statement to import Pandas library*

The `as pd` part gives Pandas a short nickname. Whenever you want to use a Pandas function, you'll write `pd.` followed by the function name. Saves a lot of typing!

## Matplotlib

The [matplotlib Python library](https://matplotlib.org/3.1.1/index.html) is used to create high-quality graphs, charts, and figures. Matplotlib will let us add titles and legends to our charts --- the finishing touches that make a visualization actually readable.

Just like we did with Pandas, you need to import the library to use it. Add this to the same code block as your Pandas import:

```python
import matplotlib.pyplot as plt
```

![Importing the Matplotlib library](images/matplotlib.png)
*Figure 8.7. Adding a statement to import Matplotlib library*

Same idea here --- `plt` is just a short nickname for `matplotlib.pyplot`, so we don't have to type that whole mouthful every time.

## A Quick Tour of the Code

Let's walk through the basic steps you'll follow in every Colab notebook this unit. We'll use the dogs dataset (you'll see a lot of it in the coming lessons), so this should feel familiar soon enough.

### Importing libraries

Every notebook starts with these two lines:

```python
import pandas as pd
import matplotlib.pyplot as plt
```

You've already seen these, but let's be precise about what `import ... as ...` actually does. Python has thousands of add-on libraries --- collections of code someone else wrote so you don't have to. The `import` command loads one of those libraries into your notebook. The `as pd` part creates a *nickname* --- an alias --- so that every time you want to call a pandas function, you type `pd.something()` instead of `pandas.something()`. It's purely a shortcut, but it's one that *everyone* uses, so you'll see `pd` and `plt` in basically every data science notebook on the planet.

### Loading data into a DataFrame

```python
df = pd.read_csv("dogs.csv")
```

This line does two things. First, `pd.read_csv("dogs.csv")` tells pandas to open the file `dogs.csv` and read it into a **DataFrame** --- pandas's version of a spreadsheet. Rows and columns, just like Google Sheets. Second, the `df = ` part stores that DataFrame in a variable called `df`.

The name `df` isn't special or required --- it's just a convention. You could call it `dogs` or `my_data` or `potato`. But most data scientists use `df` because it's short for DataFrame and everyone recognizes it instantly.

### Peeking at the first few rows

Once you've loaded your data, the very first thing you want to do is *look at it*. Did it load correctly? Are the columns what you expected?

```python
df.head()
```

`head()` shows you the first 5 rows of your DataFrame. Here's what you might see with the dogs dataset:

| | Name | Breed Group | Max Life Span | Max Weight |
|---|---|---|---|---|
| 0 | Akita | Working | 12.0 | 130 |
| 1 | Beagle | Hound | 15.0 | 30 |
| 2 | Border Collie | Herding | 15.0 | 45 |
| 3 | Boxer | Working | 12.0 | 80 |
| 4 | Bulldog | Non-Sporting | 10.0 | 50 |

That little number on the left (0, 1, 2, ...) is the *index* --- pandas's way of numbering each row. Notice it starts at 0, not 1. Classic computer science move.

### Checking the size of your data

```python
df.shape
```

This gives you a pair of numbers like `(105, 8)` --- meaning 105 rows and 8 columns. It's a quick way to answer "how much data do I actually have here?" Notice there are no parentheses after `shape` --- it's a *property*, not a function call. Don't worry about why; just remember: no parentheses.

### Listing the column names

```python
df.columns
```

This spits out all the column names in your DataFrame. Super helpful when you can't remember if the column is called `'Breed Group'` or `'BreedGroup'` or `'breed_group'`. Spelling and capitalization matter --- get one character wrong and pandas will throw a `KeyError` at you.

### Getting quick statistics

```python
df.describe()
```

This gives you a summary of basic statistics for every numeric column --- mean (average), min, max, standard deviation, &c. It's a fast way to get a feel for your numbers without making a single chart. You might notice, for example, that the average max weight across all breeds is around 60 lbs, or that the max life span ranges from 8 to 20 years.

### The big picture

Here's the thing --- you don't need to *memorize* any of this. The code in your Colab notebooks is already written for you. But understanding what each line does means you won't feel lost when you see it, and you'll have a much easier time making small changes (like swapping out a column name) when the lessons ask you to.

## Activity

Now try it yourself. Open this [Notebook](https://colab.research.google.com/drive/11A_yAiWweUhNVrI3eOpoxXLMIyj0vGQ-?usp=sharing) and **make a copy**. Unlike Replit, Google Colab doesn't automatically make a copy when you start typing --- you need to do it yourself first!

Look around. What do you notice? What do you wonder about? Follow the directions in the notebook and make the changes. You'll see the same kind of code we just walked through --- `import`, `read_csv`, `head()`, &c. --- but applied to a different dataset. See if you can match each line in the notebook to what you learned above.

**Note:** Python has a command called `import` that brings in additional libraries of functions into your program. We'll be using `import` to bring in two libraries --- **pandas** and **matplotlib.pyplot** --- into your Google Colab notebooks.

## Good reading

As you start thinking about analyzing data, interpreting charts, and drawing conclusions, here's an interesting article about [8 types of bias in data and how to avoid them](https://drive.google.com/file/d/1GbaJlPzxJGJ_PwKdRdWarO2cj9MROCBN/view?usp=sharing). Bias is one of those things that sneaks into data analysis in all sorts of subtle ways --- worth being aware of early.

---

For a complete reference of all the pandas and matplotlib code you'll use in this unit, see the **Pandas & Matplotlib Quick Reference** --- it's a handy cheat sheet to keep open while you work.
