# Lesson 8 -- Hands-on: Predicting Housing Prices

**At the end of this lesson, you will be able to:**

- Use a Google Colab notebook to run a linear regression model on real data
- Explain what each step of the machine learning pipeline does (loading data, exploring it, splitting it, training a model, evaluating)
- Experiment with different features and observe how they affect predictions
- Connect the code you're running back to the y = mx + b concepts from Lesson 7

## From Algebra to Real Data

In Lesson 7, we did linear regression by hand on a tiny dataset -- six students, one predictor, nice round numbers. That was great for building intuition, but real datasets have hundreds or thousands of rows and multiple columns. Nobody is calculating that by hand.

This is where we let the computer do what computers are good at: crunching numbers really fast. We're going to use Python and a Google Colab notebook to build a regression model that predicts housing prices. It's the same fundamental idea as y = mx + b -- the computer is just handling the arithmetic for us, and we're using more than one predictor variable.

## Getting Set Up

You'll need two things:

1. **The Google Colab notebook:** [Open the notebook here](https://colab.research.google.com/drive/1R0s74BuJjADzmDAJwLqTCRHVBM_17v6z?usp=sharing)

2. **The housing dataset:** [Download housing.csv here](https://drive.google.com/file/d/1QFm_7cTiYtGDJkxwhPzXKvqYjTnPoHLN/view?usp=sharing)

**Important setup steps:**
- First, make your own copy of the notebook: click **File > Save a copy in Drive**. This gives you a version you can edit and run without affecting anyone else.
- Then drag and drop the `housing.csv` file into the file browser panel on the left side of the Colab notebook.
- You can now run the code cells one at a time by clicking the play button on each cell, or by pressing Shift+Enter.

If you run into problems getting Colab set up, don't panic -- read through this lesson anyway. We'll describe what each step does and what the key results look like, so you can follow along even without running the code.

## What the Notebook Does, Step by Step

Let's walk through what's happening in the notebook. Even if you've never written Python before, the important thing is understanding *what* each step accomplishes and *why* we're doing it -- not memorizing the syntax.

### Step 1: Load the Data

The notebook starts by **importing pandas** and using it to load the housing.csv file.

Pandas is a Python library for working with data in tables -- think of it as a programmable spreadsheet. When we load a CSV file with pandas, we get a **DataFrame**, which is basically a table with rows and columns. Each row is one house. Each column is a piece of information about that house.

If you've ever worked with Excel or Google Sheets, a DataFrame is the same idea, just inside a programming language instead of a GUI.

### Step 2: Explore the Data

Before we build any model, we need to understand what we're working with. The notebook shows you:

- **What columns exist** -- things like square footage, number of bedrooms, location, &c.
- **How many rows there are** -- how many houses are in the dataset
- **Basic statistics** -- the average, minimum, and maximum values for each numeric column
- **Whether there's missing data** -- because real datasets almost always have gaps

This step is sometimes called **exploratory data analysis**, and it's genuinely important. If you try to build a model without first understanding your data, you're going to have a bad time. It's like trying to cook a meal without checking what ingredients you have -- you might get lucky, but probably not.

### Step 3: Pick Features and Target

Here's where we connect back to Lesson 7. Remember:

- **Features (independent variables, X)** = the columns we'll use to make predictions
- **Target (dependent variable, Y)** = the column we're trying to predict

For housing prices, the target is the sale price. The features might include square footage, number of bedrooms, number of bathrooms, lot size -- whatever information we think helps predict the price.

The notebook picks some features for you initially, but -- and this is important -- you can change which features it uses. We'll come back to that.

### Step 4: Split into Training and Testing Sets

This should sound familiar from Lesson 6 (training a model). We take our data and split it into two groups:

- **Training set** (~80% of the data) -- the model learns from this
- **Testing set** (~20% of the data) -- we hold this back and use it to check how well the model does on data it's never seen

Why do we do this? Because we need to know if the model actually *learned* the underlying pattern, or if it just memorized the specific examples we showed it. If the model does well on the training data but terribly on the testing data, it memorized instead of learning. (This is called **overfitting**, and it's one of the most common problems in machine learning.)

The train/test split is like giving a student practice problems to study, and then testing them with *different* problems on the exam. If they truly understood the material, they'll do fine on the new problems. If they just memorized the answers to the practice problems, they'll bomb.

### Step 5: Fit a Linear Regression Model

This is the big moment. The notebook uses a library called scikit-learn (a very popular machine learning library in Python) to fit a linear regression model to the training data.

Under the hood, this is doing *exactly* what we discussed in Lesson 7 -- finding the best values for the slopes and intercept so that the equation gets as close as possible to the actual prices. It's just doing it with multiple features instead of one, and with hundreds of houses instead of six.

Remember: with multiple features, the equation looks like

y = m₁x₁ + m₂x₂ + m₃x₃ + ... + b

where each x is a different feature (square footage, bedrooms, &c.) and each m tells you how much that feature affects the predicted price.

### Step 6: Look at Predictions vs. Actual Values

Once the model is trained, we use it to predict prices for the houses in our testing set -- the ones the model has never seen before.

The notebook compares the predicted prices to the actual sale prices. If the model is doing well, these should be close. You might see a table or a scatter plot where the x-axis is the actual price and the y-axis is the predicted price. If the model were perfect, every point would fall on a diagonal line (predicted = actual). In practice, the points scatter around that line, and the tightness of that scatter tells you how good the model is.

### Step 7: Evaluate the Model

Finally, the notebook calculates some numbers that tell you how well the model performed. The details of these metrics aren't something you need to memorize, but the basic idea is: **how far off were the predictions, on average?**

This is the residuals idea from Lesson 7, scaled up. Instead of looking at 6 residuals by hand, we're summarizing thousands of residuals into a single number.

## Now It's Your Turn: Experiment!

Here's where it gets fun. Go back to Step 3 -- the part where we pick which features to use -- and try changing them. This is the part of the lesson where I really want you to play around.

Some things to try:

- **Start with just one feature** (like square footage alone). How well does the model do?
- **Add more features** one at a time. Does the model get better? By how much?
- **Try using features that seem irrelevant.** Does adding a random or unhelpful column make things worse? Or does it just not help?
- **What single feature is the best predictor of price?** Can you figure this out by trying different ones?

This is how real data scientists work, by the way. A huge part of building good models is figuring out which features actually matter. It's not just math -- it requires thinking about the problem. *Why* would the number of bedrooms affect the price? *Should* the year the house was built matter? You bring your understanding of the world to the model, and the model tells you whether the data supports your intuition.

## Connecting It All Back

I want to make sure the thread from Lesson 7 is clear:

1. In Lesson 7, we learned that linear regression finds the best line through data points -- the line that minimizes the residuals.
2. In this lesson, we're doing the exact same thing, but with a computer handling the computation, more data, and more features.
3. The equation is the same kind of equation -- just with more variables.
4. The evaluation is the same idea -- just with residuals summarized into metrics instead of examined one at a time.

The jump from "do it by hand with 6 points" to "let Python do it with thousands of points" can feel like a big leap, but the concepts are identical. The computer isn't doing anything magical. It's doing the same thing you did in Lesson 7, just faster and with bigger numbers.

## What If You Can't Get the Notebook Running?

If the Colab notebook isn't cooperating -- maybe there's a technical issue, or your internet is being uncooperative, or you just can't get the CSV uploaded -- that's OK. Here's the big picture of what happens:

- The housing dataset has several hundred houses with information like square footage, number of bedrooms, number of bathrooms, and sale price.
- When we train a linear regression model using square footage alone, we get decent but not great predictions. Square footage explains a lot of the price variation, but not all of it.
- When we add more features (bedrooms, bathrooms, &c.), the predictions generally improve -- because the model has more information to work with.
- The model isn't perfect. Some predictions are way off, because house prices depend on factors that aren't in our dataset -- things like the condition of the house, the specific street, whether it has a nice view, the state of the market when it sold, &c.

The takeaway: more relevant information generally helps, but no model captures everything. And that's fine. A model that's *useful* doesn't have to be *perfect*.

## Discussion Questions

1. When you experimented with different features, which combination gave you the best predictions? Why do you think those features mattered most?

2. Were there any features that you expected to be important but turned out not to help much? Or features that surprised you by being useful?

3. Even with the best combination of features, the model's predictions weren't perfect. What factors might affect a house's price that *aren't* captured in this dataset?

4. Think back to the extrapolation warning from Lesson 7. If this model was trained on housing data from Portland, would you trust it to predict prices in San Francisco? What about a different Portland neighborhood that wasn't well-represented in the training data?
