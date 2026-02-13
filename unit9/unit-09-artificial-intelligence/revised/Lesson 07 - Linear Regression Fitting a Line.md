# Lesson 7 -- Linear Regression: Fitting a Line

**At the end of this lesson, you will be able to:**

- Explain what linear regression does and why it's useful
- Use the equation y = mx + b to make predictions from data
- Calculate residuals and explain what they tell you about how good a model is
- Recognize the dangers of extrapolating beyond your data

## The Big Idea

Here's the setup. You've got a bunch of data points -- maybe you surveyed some students about how many hours they studied and what they scored on an exam. You plot those points on a graph. They form a rough cloud, but you can kind of see a trend: more studying generally means higher scores.

Now you want to draw a line through that cloud of points -- the *best* line, the one that gets as close as possible to all the points at once. That's linear regression. That's the whole idea. You're fitting a line to data.

Why would you want a line? Because once you have a line, you have an equation, and once you have an equation, you can make *predictions*. A new student tells you they studied for 7 hours -- you can plug 7 into your equation and get a predicted score. That's incredibly useful.

## Quick Refresher: y = mx + b

You've seen this equation before in algebra. Let's dust it off:

**y = mx + b**

- **m** is the **slope** -- it tells you how steep the line is. More specifically, it tells you how much y changes when x goes up by 1. If m = 6, that means "for every 1 unit increase in x, y goes up by 6."
- **b** is the **y-intercept** -- it's where the line crosses the y-axis. It's the value of y when x is 0.

So if y = 3x + 10, and you plug in x = 2, you get y = 3(2) + 10 = 16. That's it. No tricks here.

The reason we're reviewing this is that linear regression is literally just finding the *best* values of m and b for a given dataset. The computer does the heavy lifting of figuring out what m and b should be, but the underlying equation is the same one you learned in algebra class.

## Independent and Dependent Variables

Before we go further, let's nail down some vocabulary:

- The **independent variable (X)** is the thing you're using to *make* a prediction. It's the input. In our example, it's hours studied.
- The **dependent variable (Y)** is the thing you're *trying to predict*. It's the output. In our example, it's the exam score.

Why "dependent"? Because the exam score *depends* (at least partly) on how much the student studied. The number of hours studied doesn't depend on the exam score -- that would be weird and also time travel.

You'll sometimes hear people call X the **predictor** or **feature**, and Y the **target** or **outcome**. Different fields use different words for the same idea, which is mildly annoying but something you get used to.

## A Worked Example: Study Hours vs. Exam Scores

Let's make this concrete. Here's data from six students:

| Hours Studied (X) | Exam Score (Y) |
|-|-|
| 1 | 52 |
| 2 | 58 |
| 3 | 65 |
| 4 | 70 |
| 5 | 74 |
| 6 | 85 |

If you plotted these on a graph -- with hours on the horizontal axis and scores on the vertical axis -- you'd see the points climbing from lower-left to upper-right. More hours, higher scores. There's clearly a trend, but the points don't fall on a perfectly straight line. Real data basically never does.

So we want to find the line that gets *closest* to all six of these points at once.

### Finding the Line of Best Fit

For this dataset, the line of best fit turns out to be approximately:

**y = 6x + 47**

Let's check that this makes sense. The slope is 6, which means the model predicts that each additional hour of studying adds about 6 points to your exam score. The y-intercept is 47, which would be the predicted score for someone who studied 0 hours. (That's a pretty rough baseline score -- not great, but not zero either. Seems plausible.)

Now let's see what this equation predicts for each of our data points:

| Hours (X) | Actual Score (Y) | Predicted Score (6x + 47) |
|-|-|-|
| 1 | 52 | 6(1) + 47 = **53** |
| 2 | 58 | 6(2) + 47 = **59** |
| 3 | 65 | 6(3) + 47 = **65** |
| 4 | 70 | 6(4) + 47 = **71** |
| 5 | 74 | 6(5) + 47 = **77** |
| 6 | 85 | 6(6) + 47 = **83** |

Not bad! The predictions are pretty close to the actual values. Not exact -- but close. And that brings us to a really important concept.

## Residuals: How Far Off Are We?

A **residual** is the difference between the actual value and the predicted value. It tells you how far off the model was for each data point.

**Residual = Actual Y - Predicted Y**

Let's calculate the residual for every point:

| Hours (X) | Actual (Y) | Predicted | Residual (Actual - Predicted) |
|-|-|-|-|
| 1 | 52 | 53 | 52 - 53 = **-1** |
| 2 | 58 | 59 | 58 - 59 = **-1** |
| 3 | 65 | 65 | 65 - 65 = **0** |
| 4 | 70 | 71 | 70 - 71 = **-1** |
| 5 | 74 | 77 | 74 - 77 = **-3** |
| 6 | 85 | 83 | 85 - 83 = **+2** |

Look at those residuals. They're small -- mostly just 1 or 2 points off. That's a sign that our line is doing a good job.

A few things to notice:

- **A residual of 0** means the prediction was perfect for that point. (Student 3 studied 3 hours and scored exactly 65, which is exactly what the line predicted.)
- **A negative residual** means we *overpredicted* -- the model said the score would be higher than it actually was.
- **A positive residual** means we *underpredicted* -- the actual score was higher than what the model predicted.

### What Makes a Line the "Best" Line?

Here's the key insight: the line of best fit is the line that makes the residuals as small as possible *overall*. You don't just want to be close to one or two points -- you want to be reasonably close to *all* of them.

(If you take more statistics or data science courses, you'll learn that the technical approach is called **least squares** -- it minimizes the sum of the squared residuals. We're not going to get into the math of *how* you find the best m and b here, but the intuition is exactly what you'd expect: try to make the errors as small as possible across the board.)

## Making Predictions

OK, so we have our model: y = 6x + 47. Now we can use it!

Let's say a student asks: "I'm planning to study for 8 hours. What score should I expect?"

Plug it in: y = 6(8) + 47 = 48 + 47 = **95**

The model predicts a 95. Nice!

But wait -- should we trust this? Let's think about it.

### The Danger of Extrapolation

Our data only covers students who studied between 1 and 6 hours. We *know* the trend holds in that range because we have actual data points there. But 8 hours is *outside* that range. We're **extrapolating** -- making predictions beyond where our data lives.

Extrapolation is risky because you're assuming the pattern continues, and you have no evidence for that. Maybe studying for 8 hours causes diminishing returns -- you get tired, you can't focus, and the extra hours don't help as much. Maybe the relationship isn't a straight line outside the 1-6 hour range. We just don't know.

As a rule of thumb: **predictions within your data range (interpolation) are much more trustworthy than predictions outside your data range (extrapolation)**.

This isn't just a stats thing, by the way. It comes up everywhere. When weather forecasters are more confident about tomorrow's weather than next week's, or when economists hedge their predictions about what the stock market will do next year -- same basic idea. The further you get from what you've actually observed, the less sure you should be.

## Beyond One Variable

Everything we've done here uses one independent variable (hours studied) to predict one dependent variable (exam score). That's called **simple linear regression** -- "simple" because there's only one predictor.

In the real world, you usually want to use *multiple* predictors. If you're predicting housing prices, you'd want to consider square footage AND number of bedrooms AND what neighborhood the house is in AND whether it has a garage AND when it was built AND... you get the idea.

That's called **multiple linear regression**, and the equation looks something like:

y = m₁x₁ + m₂x₂ + m₃x₃ + ... + b

Each x is a different feature, and each m is its own slope -- telling you how much that feature affects the prediction. It's the same basic idea as y = mx + b, just with more variables. You can't easily visualize it on a 2D graph anymore (you'd need one dimension for each variable), but the math works the same way.

In the next lesson, we'll actually use a computer to do multiple linear regression on real housing data. The concepts are exactly what we covered here -- the computer just handles the messier arithmetic.

## Discussion Questions

1. Go back to the residuals table. If I told you there was a *different* line -- say, y = 5x + 50 -- could you check whether it's better or worse than y = 6x + 47? (Hint: calculate the predicted values and residuals for the new line and compare.) Try it!

2. Can you think of a real-world example where extrapolation would be especially dangerous? What about a case where it might be more reasonable?

3. Our model has a y-intercept of 47, which would be the predicted score for a student who studied 0 hours. Does that seem reasonable? What are the limitations of interpreting the y-intercept literally?

4. Imagine you wanted to predict something in your own life using regression. What would you predict (Y), and what would you use as a predictor (X)? Do you think the relationship would actually be linear, or would a straight line be a bad fit?
