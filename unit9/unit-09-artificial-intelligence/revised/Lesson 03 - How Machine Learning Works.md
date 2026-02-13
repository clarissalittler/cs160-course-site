# Lesson 3 -- How Machine Learning Works

**At the end of this lesson, you will be able to:**

- Explain the fundamental difference between traditional programming and machine learning
- Describe the basic steps of the machine learning pipeline
- Explain why we split data into training and testing sets
- Discuss why data quality matters for machine learning outcomes

## The big idea

Here's the most important thing to understand about machine learning, and once you get this, everything else will make a lot more sense:

**Traditional programming:** You write the rules. You tell the computer "if this, then that." You figure out the logic and you code it up, step by step.

**Machine learning:** You show the computer a bunch of examples, and the computer figures out the rules on its own.

That's it. That's the core distinction. Everything else in machine learning -- all the fancy math, the neural networks, the jargon -- is just different ways of doing that second thing.

## The cat problem

Let's make this concrete with an analogy. Imagine you're trying to teach a small child to recognize cats. You have two options:

**Option A (the traditional programming approach):** You sit the child down and give them a list of rules. "A cat has four legs, fur, pointy ears, a tail, whiskers, and says meow." Sounds reasonable, right? But wait -- what about a cat with a missing leg? What about a Sphynx cat with no fur? What about a Scottish Fold with floppy ears? What about a cat that's sleeping and not meowing? Your rules keep breaking. Every exception requires a new rule, and the exceptions have exceptions, and pretty soon your rulebook is a thousand pages long and *still* doesn't work very well.

**Option B (the machine learning approach):** You show the child hundreds of cats. Fluffy cats, skinny cats, orange cats, black cats, cats sitting in boxes, cats knocking things off tables, cats wearing tiny hats. You don't explain any rules. You just point and say "cat" a lot. Eventually the child just... *gets it*. They can recognize a cat they've never seen before, even if it looks different from all the cats you showed them.

That's basically what machine learning does. Instead of writing rules, you show the computer a huge number of examples, and it figures out the patterns. The computer doesn't "understand" cats the way the child eventually will -- it's doing math, not having a childhood -- but the end result is similar: it can look at a new image and tell you whether there's a cat in it.

This might seem like a small difference, but it's actually revolutionary. There are tons of problems that are incredibly hard to solve by writing rules but relatively easy to solve by showing examples. Recognizing faces. Understanding speech. Translating languages. Detecting spam emails. Predicting the weather. For all of these problems, the patterns are too complex and messy for a human to write down as explicit rules -- but a computer can learn them from data.

## The machine learning pipeline

Okay, so how does this actually work in practice? There's a general process -- a pipeline -- that most machine learning projects follow. It's not always this clean and linear in the real world (there's usually a lot of going back and forth between steps), but the basic flow looks like this:

### Step 1: Collect data

You need examples. Lots of them. If you want to build a spam detector, you need thousands (or millions) of emails that have been labeled as "spam" or "not spam." If you want to predict housing prices, you need historical data about houses that sold -- their size, location, number of bedrooms, &c. -- along with the prices they sold for.

Where does this data come from? All over the place. Databases, websites, sensors, surveys, user activity logs, public datasets. The rise of the internet and smartphones means there's more data available now than at any point in human history, which is a big part of why machine learning has taken off in the last decade or so.

### Step 2: Prepare and clean the data

This is the step that nobody talks about in the flashy AI demos, but it's where data scientists spend a *huge* portion of their time. Real-world data is messy. It has missing values, typos, inconsistencies, duplicate entries, and weird formatting. Before you can train a model, you need to clean all that up.

Imagine trying to learn to cook from a recipe book where half the recipes are missing ingredients, some of the measurements are in cups and others are in grams with no conversion, and every third recipe is actually a duplicate of another recipe with a different title. You'd have a rough time. That's what raw data often looks like.

### Step 3: Choose a model

A "model" in machine learning is the mathematical structure that's going to learn from your data. There are many different types -- we'll explore some of them in later lessons -- and different models work better for different kinds of problems. Choosing the right model is part art, part science, and part trial and error.

Don't worry too much about this step right now. The important thing to know is that a model is basically a mathematical machine with a bunch of adjustable knobs (more on this in a moment), and your job is to pick the right kind of machine for your problem.

### Step 4: Train the model

This is the "learning" part. You feed your prepared data into the model and let it adjust itself. The model makes predictions, checks how wrong it was, and tweaks its internal settings to be a little less wrong next time. Then it does this again. And again. And again -- potentially millions of times.

It's like practicing free throws. Each time you shoot, you see where the ball goes, and you adjust your form a tiny bit. Over thousands of shots, you get better. The model is doing the same thing, just with math instead of basketball.

### Step 5: Evaluate the model

Once the model has been trained, you need to check how well it actually works. This is where testing data comes in -- more on this in the next section, because it's important enough to deserve its own discussion.

### Step 6: Use the model for predictions

If the model performs well in evaluation, you deploy it -- you put it to work making predictions on new data it's never seen before. This is the actual *point* of the whole exercise. Your spam detector starts filtering real emails. Your housing price predictor starts giving estimates to real homebuyers.

## Training data vs. testing data

Here's a question that might seem trivial but is actually super important: how do you know if your model is any good?

The naive answer is "test it on your data and see how well it does." But there's a big problem with this: **if you test your model on the same data it learned from, you're not testing whether it learned the *patterns* -- you're testing whether it memorized the *examples*.**

Think of it this way. Imagine a student who prepares for an exam by memorizing the answer key. If you give them the exact same exam they memorized, they'll get 100%. Does that mean they understand the material? Obviously not. Give them a slightly different exam and they'll bomb it.

This problem is called **overfitting** in machine learning, and it's one of the most common pitfalls. A model that has memorized its training data looks amazing on that training data but performs terribly on new data it's never seen.

The solution is simple: you split your data into two parts before you start training.

- The **training set** (usually 70-80% of your data) is what the model learns from.
- The **testing set** (the remaining 20-30%) is held back and *never shown to the model during training*. You only use it at the end, to evaluate how well the model performs on data it's never seen.

It's like giving a student practice problems to study with, and then testing them with *different* problems on the exam. If they do well on the exam, you can be confident they actually learned the underlying concepts -- not just memorized answers.

## What does "learning" actually mean for a computer?

When we say a machine learning model "learns," we're using that word in a pretty different way than when we say a person learns. There's no understanding happening. There's no "aha!" moment. Here's what's actually going on:

A model has **parameters** -- think of them as numbers that control how the model behaves. A simple model might have a handful of parameters. A large language model like GPT has *billions* of them.

During training, the model:

1. Takes some input data and makes a prediction
2. Compares its prediction to the correct answer
3. Measures how wrong it was (this measurement is called the **loss**)
4. Adjusts its parameters slightly to reduce the loss
5. Repeats this process over and over and over

That's it. "Learning" for a computer means "adjusting numbers until the predictions get better." It's mechanical. It's mathematical. It's not thinking, not understanding, and not anything like human learning in any deep sense. But it works remarkably well for a surprising range of problems.

I want to be clear about this because there's a lot of language around AI that anthropomorphizes it -- that treats it as if it's thinking or understanding or wanting things. Some of that language is convenient shorthand, and even AI researchers use it casually. But it can be misleading, especially when companies use it to make their products sound more capable or more human-like than they actually are.

## Garbage in, garbage out

Here's maybe the most important practical lesson about machine learning: **a model is only as good as the data you train it on.**

If your training data is incomplete, your model will have blind spots. If your training data is biased, your model will be biased. If your training data contains errors, your model will learn from those errors. The computer doesn't know the difference between good data and bad data. It just finds patterns in whatever you give it.

This isn't just a theoretical concern. There have been real, consequential cases where biased training data led to biased AI systems:

- Hiring algorithms trained on historical hiring data learned to discriminate against women, because the historical data reflected decades of gender discrimination in hiring.
- Facial recognition systems trained primarily on photos of lighter-skinned faces performed significantly worse on darker-skinned faces.
- Predictive policing algorithms trained on historical arrest data -- which reflected biased policing practices -- recommended sending more police to neighborhoods that were already over-policed.

In each of these cases, the model did exactly what it was designed to do: it found patterns in the data. The problem was that the patterns in the data reflected real-world biases and injustices. The model didn't create the bias -- it learned it and then automated it, often at a larger scale than before.

We're going to dig much deeper into this topic later in the unit, because it's one of the most important issues in AI today. For now, just remember: **the data matters as much as the algorithm, maybe more.** When someone shows you an impressive AI system, one of the first questions you should ask is "what data was it trained on?"

## Activity: the ML pipeline in action

Let's walk through a concrete example to make sure the pipeline makes sense. Imagine you want to build a machine learning model that predicts whether a Portland food cart will still be in business one year from now. (A morbid question, but a practical one if you're thinking about investing.)

Think through the following questions -- jot down your answers or discuss with a classmate:

1. **Data collection:** What data would you need to collect? What information about food carts might be relevant to predicting their survival? (Think about things like location, type of food, hours, reviews, nearby competition, &c.)

2. **Data cleaning:** What problems might you encounter with this data? What might be missing, messy, or inconsistent?

3. **Training and testing:** If you collected data on 1,000 food carts, how would you split it? Why?

4. **Bias concerns:** Can you think of any ways the data might be biased? For example, what if your data mostly covers food carts in certain neighborhoods? How might that affect the model's predictions for carts in other neighborhoods?

5. **The "garbage in" problem:** Suppose you accidentally included data from food carts that closed due to a construction project blocking their street (not because of anything wrong with the business). How might that mess up your model?

## Discussion questions

1. **Can you think of a problem that would be hard to solve by writing rules but easy to solve with machine learning?** What about the opposite -- a problem where rules work better than learning from examples?

2. **We said that ML "learning" is very different from human learning.** Do you agree with that? Is there any sense in which adjusting parameters based on feedback is similar to how humans learn? Where does the analogy break down?

3. **The "garbage in, garbage out" principle applies to human decision-making too.** Can you think of cases where humans make biased decisions because they were "trained" on biased experiences or information?
