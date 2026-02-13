# Supervised Learning

## Learning Outcomes

By the end of this lesson, you should be able to:

- Explain what supervised learning is and why it's called "supervised"
- Distinguish between classification (predicting a category) and regression (predicting a number)
- Walk through a concrete example of how a supervised learning model gets trained
- Recognize that a model can only learn patterns that exist in its training data

## What Does "Supervised" Mean Here?

So we've talked about what machine learning is in general — a system that learns patterns from data instead of being explicitly programmed. Now let's dig into the most common flavor: **supervised learning**.

The word "supervised" here is doing a lot of work. Think of it like this: you're the supervisor. You give the model a bunch of examples where you already know the right answer, and the model's job is to figure out the pattern connecting the inputs to the outputs. It's like handing a student a stack of solved practice problems and saying "figure out how these work so you can solve new ones."

More formally: you give the model **input-output pairs** — also called **labeled examples** — and it learns the mapping from input to output. The "labels" are the answers. That's the supervision.

## The Two Flavors: Classification and Regression

Supervised learning comes in two main varieties, and the difference is actually pretty simple — it's all about what kind of answer you're predicting.

### Classification: Predicting a Category

In classification, the model's job is to sort things into buckets. The output is a **label** — a category, a group, a type. Some examples:

- **Spam or not spam?** — You look at an email and decide which bucket it falls into. Two categories, one choice.
- **Cat or dog?** — You look at a photo and decide what's in it. (Computers are honestly pretty good at this now, which still kind of amazes me.)
- **Malignant or benign?** — A doctor looks at a medical image and classifies a tumor. This one matters a lot.

Notice that in all of these cases, the answer is one of a fixed set of options. It's not a number on a sliding scale — it's a *category*. Spam or not. Cat or dog. That's classification.

### Regression: Predicting a Number

In regression, the model predicts a **continuous value** — a number that could be anything along a range. Some examples:

- **How much will this house sell for?** — The answer might be $350,000 or $425,750 or anything in between.
- **What will the temperature be tomorrow?** — Could be 58.3 degrees or 72.1 degrees.
- **How many points will a basketball player score next game?** — Maybe 22, maybe 31.5 (in projected averages), maybe 8.

The key difference: classification gives you a label, regression gives you a number. That's really the whole distinction. If someone asks you "is this a classification or regression problem?" just ask yourself: is the answer a category or a number?

## A Classification Example: Spam Detection

Let's walk through a concrete example to make this feel real.

Imagine you work at an email company and you want to build a spam filter. Here's what you do:

1. **Collect labeled data.** You get a big spreadsheet with two columns: the text of the email, and whether a human marked it as "spam" or "not spam." Let's say you have 1,000 of these labeled emails.

2. **Feed it to a model.** You give your supervised learning algorithm all 1,000 examples. The model looks at the spam emails and notices patterns — maybe spam emails tend to have words like "FREE," "WINNER," "click here," and lots of exclamation marks. Not-spam emails tend to have, you know, actual sentences from people you know.

3. **Test it on new data.** Now a brand-new email arrives that the model has never seen before. Based on the patterns it learned, it predicts: spam or not spam?

That's it. That's supervised learning for classification. You gave it examples with answers, it found patterns, and now it can make predictions on new data.

## A Regression Example: House Prices

Now let's do the same thing but for regression.

Imagine you're a real estate company in Portland and you want to predict how much a house will sell for. Here's your setup:

1. **Collect labeled data.** You gather records of past home sales. For each house, you know things like: square footage, number of bedrooms, number of bathrooms, which neighborhood it's in, whether it has a garage, year built, &c. And crucially, you know what it actually sold for. That sale price is your label.

2. **Feed it to a model.** The algorithm looks at hundreds or thousands of past sales and finds patterns. Bigger houses tend to sell for more. Houses in certain neighborhoods command higher prices. An extra bathroom adds roughly $X to the price. The model builds up this web of relationships.

3. **Predict new prices.** Now someone lists a new house: 1,800 square feet, 3 bedrooms, in the Hawthorne neighborhood. Based on patterns from past sales, the model predicts a price — maybe $485,000.

Notice that the answer isn't a category — it's a specific number. That's regression.

## The Big Insight: You Are Your Training Data

Here's something that's easy to miss but really important: **a model can only learn patterns that exist in its training data.**

If you trained your house price model entirely on homes in Portland, Oregon, don't expect it to give you a good estimate for an apartment in Manhattan. The patterns are completely different — the price ranges are different, the factors that matter are different, the whole market is different. Your model has never seen Manhattan data, so it has no idea what to do with it.

This might seem obvious, but it has huge consequences. If your training data is missing something — a whole category of examples, a demographic group, an unusual edge case — the model will be bad at handling those things. We're going to come back to this idea in a big way when we talk about bias in a couple of lessons. For now, just hold onto the idea: **garbage in, garbage out** — but also, **gaps in, gaps out**.

## Activity: Train an AI Yourself

It's time to actually try this. Head over to Code.org's **AI for Oceans** activity:

[**AI for Oceans — Code.org**](https://studio.code.org/s/oceans/lessons/1/levels/1)

In this activity, you'll train a model to classify things as **fish** or **trash** by giving it labeled examples. It's supervised learning in action — you're the supervisor!

As you work through it, pay attention to what happens when:
- You give it lots of good examples
- You give it weird or misleading examples
- The training data doesn't represent all the things the model might encounter

### Reflection Questions

After you complete the activity, think about (and write a short response to) these questions:

1. When your model made mistakes, what kind of mistakes did it make? Did it tend to call trash "fish" or fish "trash"?
2. Did you notice any cases where the model struggled because the training data didn't prepare it well? What was missing?
3. This was a classification task. What were the categories? Could you imagine turning this into a regression task instead? (What number might you predict about ocean debris?)

## Discussion Questions

1. Come up with your own example of a classification problem and a regression problem. For each one, describe: what is the input? What is the output? What kind of training data would you need?

2. A company trains a model to predict whether a student will pass or fail a course, based on data like attendance, homework scores, and participation. Is this classification or regression? What concerns might you have about using a model like this?

3. Why do you think supervised learning is the most common type of machine learning in practice? (Hint: think about what it requires — labeled data — and when that's easy or hard to get.)
