# Training a Model: Data and Bias

## Learning Outcomes

By the end of this lesson, you should be able to:

- Describe the basic training loop: feed data, make predictions, measure error, adjust, repeat
- Explain why we split data into training and testing sets, and what happens if we don't
- Define overfitting and recognize it in examples
- Identify how bias in training data leads to biased predictions, with real-world examples

## The Training Process: How a Model Actually Learns

We've talked about the different types of machine learning — supervised, unsupervised, reinforcement — but we've been a little hand-wavy about what "training" actually looks like under the hood. Let's fix that.

Here's the basic loop that makes a supervised learning model get better over time:

1. **Feed the model some training data.** Give it inputs and the correct outputs (the labels).
2. **The model makes predictions.** At first, these predictions are basically random — the model hasn't learned anything yet.
3. **Measure how wrong the predictions are.** This measurement is called the **loss** (sometimes called "error" or "cost"). It's just a number that says "here's how far off you were." Big number = very wrong. Small number = pretty close.
4. **Adjust the model to be less wrong.** The model tweaks its internal settings — nudging things in the direction that would have made it less wrong on this batch of data.
5. **Repeat.** Go back to step 1 with more data. Do this thousands — sometimes millions — of times.

Each time through the loop, the model gets a little better. The loss goes down. The predictions get closer to the real answers. It's not dramatic — it's not like the model has an "aha!" moment — it's more like slowly turning a bunch of knobs until the picture on the TV comes into focus.

That's it. That's training. It's conceptually simple, even though the math behind "adjust the model" can get pretty involved. For this course, the important thing is the big picture: **make predictions, measure error, adjust, repeat.**

## Train/Test Split: Why We Hold Out Data

Okay, here's something that might seem counterintuitive at first. When you have a dataset — say, 10,000 labeled emails — you **don't** use all of them for training. Instead, you split the data:

- Maybe **80%** (8,000 emails) goes into the **training set** — this is what the model learns from
- The remaining **20%** (2,000 emails) goes into the **test set** — this is what you use to evaluate how well the model actually works

Why would you throw away perfectly good training data? Here's the thing: **if you test the model on the same data it trained on, you're not testing whether it learned the pattern — you're testing whether it memorized the answers.**

Think about it. If I give you a list of 100 math problems and their answers, and then I "test" you by asking you those same 100 problems, I haven't learned anything about whether you understand math. I've just learned that you have a good memory.

What I actually want to know is: can you solve *new* problems you haven't seen before? That's why we hold out a test set. The model has never seen those 2,000 emails during training. If it can still correctly classify them as spam or not-spam, then we know it actually learned something generalizable — not just memorized.

## Overfitting: When Memorizing Beats Learning

This brings us to one of the most important concepts in machine learning: **overfitting**.

Overfitting is when a model learns the training data *too well* — including all its noise, quirks, and random weirdness — and as a result, it performs terribly on new data it hasn't seen before.

### The Student Analogy

Here's the analogy I like best. Imagine two students preparing for a math exam:

**Student A** works through all the practice problems and memorizes each one. They can reproduce every solution perfectly. They don't really understand *why* the solutions work — they just remember the steps for each specific problem.

**Student B** works through the practice problems and focuses on understanding the underlying concepts. They might not remember every specific problem perfectly, but they understand the principles well enough to tackle new problems.

Exam day comes, and the problems are new ones they haven't seen. Student A is in trouble — nothing on the exam matches their memorized solutions exactly. Student B does fine, because they learned the *pattern*, not just the examples.

Student A overfit to the practice problems. They memorized, they didn't learn.

A machine learning model can do the exact same thing. If it's too powerful relative to the amount of data you have, or if you train it for too long, it starts memorizing individual training examples instead of learning general patterns. It'll have amazing performance on the training data and terrible performance on the test data. That gap — great on training, bad on testing — is the telltale sign of overfitting.

## Bias in Training Data: Where Things Get Serious

Okay. Everything we've talked about so far — training loops, train/test splits, overfitting — is important for making models that work *technically*. But now we need to talk about something that matters even more: making models that work *fairly*.

Remember the core principle: **a model can only learn patterns that exist in its training data.** We said this about house prices — if you only train on Portland houses, the model won't know about Manhattan. But the same principle applies to people, and the consequences can be much more serious.

### Facial Recognition and Skin Color

In 2018, researchers Joy Buolamwini and Timnit Gebru published a study called **"Gender Shades"** that tested commercial facial recognition systems from major tech companies. What they found was striking but — once you understand how training data works — not surprising:

- The systems were **very accurate** at classifying lighter-skinned male faces (error rates below 1%)
- They were **significantly worse** at classifying darker-skinned female faces (error rates up to 35%)

Why? Because the training data — the sets of labeled face images used to train these models — contained predominantly lighter-skinned faces. The model learned to recognize faces it had seen a lot of, and was worse at recognizing faces it had rarely seen. The model wasn't "racist" in the way a person can be — it didn't have beliefs or intentions. It just found the patterns in the data it was given, and those patterns reflected who was (and wasn't) well-represented in the dataset.

This isn't a hypothetical concern. These systems were being sold to law enforcement agencies and businesses. A facial recognition system that works well for some people and poorly for others is not just a technical failure — it's a system that can cause real harm to real people.

### Hiring Algorithms and Historical Discrimination

Here's another case that actually happened. Amazon built an AI recruiting tool to help screen job applicants. They trained it on the company's past hiring decisions — resumes of people who had been hired and people who hadn't.

The problem? The company's past hiring decisions reflected the company's past biases. In their technical roles, they had historically hired predominantly men. So the algorithm learned that being male was a positive signal. It literally started penalizing resumes that contained the word "women's" — as in "women's chess club" or "women's college."

Amazon scrapped the tool, but the lesson is huge: **if you train a model on biased historical data, the model learns the bias.** It doesn't question the data. It doesn't think "hmm, that doesn't seem fair." It just finds the pattern. If the pattern in your data is "men get hired more," then the model will predict that men should be hired more.

### The Model Doesn't Know It's Being Unfair

This is really worth sitting with for a moment. The model has no concept of fairness. It has no concept of race, gender, justice, or harm. It's a pattern-matching machine. Whatever patterns exist in the data — including patterns of historical discrimination, underrepresentation, and inequality — the model will learn them and reproduce them.

That means the responsibility falls on the **people who build and deploy these systems.** They need to ask hard questions:

- Who is represented in our training data? Who isn't?
- Whose historical decisions are we encoding into this model?
- Who might be harmed if this model makes mistakes, and are mistakes distributed evenly?
- Just because we *can* predict something, *should* we?

## The Takeaway

Building an AI system isn't just a technical task — it's a task with ethical dimensions at every step. The choice of what data to collect, who's in it, who's missing, what you're trying to predict, and who the predictions affect — these are all human decisions that shape what the model becomes.

A model trained on the world as it is will reproduce the world as it is — including its injustices. If we want AI systems that are fair, the people building them have to actively work toward fairness. It doesn't happen automatically.

## Discussion: Bias in Datasets

Think about a dataset that might be used to train a machine learning model. It can be something from the news, something we've discussed, or something you come up with. Then respond to these questions:

1. **What is the dataset?** Describe the data — what information does it contain, and what would a model trained on it be trying to predict?

2. **What bias might exist in it?** Think about who collected the data, who's represented, and what historical patterns might be baked in.

3. **Who might be affected?** If the model makes biased predictions, which groups of people might be helped or harmed?

4. **How could you try to fix it?** This is the hard part — and there aren't always clean answers. But think about it. Could you collect more representative data? Audit the model's predictions across different groups? Decide not to build the model at all? There's no single right answer, but the conversation matters.

### Some Ideas to Get You Started

If you're stuck, here are some real scenarios to think about:

- A model trained on historical crime data to predict where crimes will happen next (used for "predictive policing")
- A model trained on past medical records to predict which patients need extra care
- A model trained on social media posts to predict someone's mental health
- A model trained on school performance data to predict which students are "at risk" of dropping out

Each of these has real-world implications and real potential for bias. Pick one — or make up your own — and dig in.
