# Lesson 10 -- Large Language Models

**At the end of this lesson, you will be able to:**

- Explain what a large language model (LLM) is and how it's trained
- Describe the core mechanism behind LLMs: next-token prediction
- Identify what LLMs are good at and what they're bad at
- Explain what "hallucination" means and why it matters

## You've Already Used One

If you did Lab 5, you've already had a conversation with a large language model. You typed something into ChatGPT, it generated code for you, you debugged that code together -- the whole loop. You saw that it could be genuinely useful and also genuinely wrong.

But here's the thing: at that point, you were using it as a tool without knowing how it works. That's fine for a hammer, but LLMs are shaping up to be one of the most significant technologies of our lifetimes. You should know what's going on under the hood. So let's pop the hood.

## What Is an LLM?

A large language model is a type of deep neural network -- the kind we talked about in Lesson 09 -- trained on an *enormous* amount of text from the internet. We're talking books, websites, Wikipedia, code repositories, forum posts, news articles, &c. Billions and billions of pages of text.

The "large" in "large language model" refers to two things: the massive amount of training data, and the massive number of parameters (remember, parameters are the numbers the model adjusts during training -- the knobs it tunes to get better at its task). These models have billions of parameters. GPT-2, released in 2019, had 1.5 billion parameters. GPT-3, released just a year later, had 175 billion. Current models are even larger. The scale is genuinely hard to wrap your head around.

## The Core Trick: Next-Token Prediction

Here's the part that surprises a lot of people. The fundamental thing an LLM is trained to do is incredibly simple:

**Given everything that's been said so far, predict the next word.**

That's it. That's the whole trick. (Well, technically it predicts the next "token," which is a word or a piece of a word -- the model breaks text into chunks called tokens rather than whole words. But "predict the next word" captures the idea.)

When you're chatting with ChatGPT and it's writing a response to you, it's generating one token at a time. It looks at the entire conversation so far -- your messages, its previous responses, everything -- and asks: "given all of this, what's the most likely next token?" It generates that token, appends it to the conversation, and then asks the same question again. And again. And again. Until it decides it's done.

It's like the world's most sophisticated autocomplete.

### Why This Is Deceptively Powerful

"Predict the next word" sounds too simple to produce the kind of output you've seen from these models. And I get that reaction -- it does seem like there should be more to it. But think about what it takes to be *really good* at predicting the next word across billions of pages of text.

To predict the next word accurately, the model ends up learning:

- **Grammar and syntax** -- because grammatically incorrect sentences are unlikely
- **Facts about the world** -- because factually accurate text is more common than inaccurate text in the training data
- **Reasoning patterns** -- because logical conclusions follow from premises in well-written text
- **Coding syntax** -- because valid code follows predictable patterns
- **Writing styles** -- because different contexts call for different tones
- **Multiple languages** -- because the training data includes text in many languages

Nobody explicitly taught the model any of these things. Nobody said "here are the rules of English grammar" or "here are the facts about the solar system." The model learned them because knowing those things helps it predict the next word better. It's a bit like how you might learn a lot about cooking just by watching thousands of hours of cooking shows -- nobody sat you down with a textbook, but the patterns soak in.

### Scale Matters

This trick only works because of the sheer scale involved. A small model trained on a small amount of text would just learn to parrot back common phrases. But as you make the model bigger (more parameters) and feed it more data, something interesting happens: it starts exhibiting capabilities that nobody explicitly programmed. It can write poetry. It can translate between languages. It can debug code. It can explain complex topics in simple language.

Researchers call these **emergent capabilities** -- abilities that emerge from scale rather than being specifically trained. It's one of the more fascinating (and honestly, slightly eerie) aspects of these models. We built a system to predict the next word, and somewhere along the way it learned to write sonnets.

Though -- and this is important -- there are diminishing returns. Making a model twice as big doesn't make it twice as good. You get less and less improvement for each additional dollar you spend on training. This is an active area of research.

## What LLMs Are Good At

Let's be clear-eyed about this. LLMs are genuinely impressive at certain tasks:

- **Writing and editing text** -- drafting emails, essays, reports, cover letters, &c.
- **Summarizing** -- condensing long documents into key points
- **Translation** -- converting text between languages
- **Answering questions** -- especially about topics that are well-represented in the training data
- **Generating code** -- you've already experienced this in Lab 5
- **Brainstorming** -- coming up with ideas, outlines, approaches to problems
- **Explaining concepts** -- breaking down complicated topics into simpler language (it's pretty meta that an LLM could theoretically explain this lesson to you)

These are all tasks where "sophisticated pattern matching over enormous amounts of text" genuinely gets you a long way.

## What LLMs Are Bad At

And here's where things get important. LLMs have real, fundamental weaknesses that you need to understand if you're going to use them responsibly:

- **Math.** The model is predicting text, not computing. If you ask it to multiply large numbers, it's not doing arithmetic -- it's guessing what the answer *looks like* based on patterns. Sometimes it gets it right (because it's seen similar problems in training data), and sometimes it gets it spectacularly wrong. You wouldn't ask your autocomplete to do your taxes.

- **Factual accuracy.** The model can confidently state things that are completely, verifiably false. We'll talk about this more in a moment, because it's probably the most important thing in this lesson.

- **Real-time information.** LLMs are frozen in time. They were trained on data up to some cutoff date, and they have no idea what happened after that. If you ask about yesterday's news, the model doesn't know -- but it might make something up that sounds plausible.

- **Genuine reasoning about novel problems.** The model is very good at recombining patterns it's seen before. It's much less good at truly novel reasoning -- the kind of thing where you need to think through a problem from first principles in a way that doesn't resemble anything in the training data.

- **Knowing what it doesn't know.** This is a big one. Humans generally have a sense of when they're guessing versus when they're confident. LLMs don't. Everything comes out with the same confident tone, whether the model is giving you a well-established fact or making something up entirely.

## Hallucination: The Most Important Concept in This Lesson

You've probably heard this term already, but let's make sure we're precise about what it means.

**Hallucination** is when an LLM generates text that is factually incorrect, made up, or nonsensical -- but presents it with complete confidence, as if it's stating a well-known fact.

Some examples that have actually happened:

- A lawyer used ChatGPT to write a legal brief, and the model invented fake court cases -- complete with fake case names, fake judges, and fake rulings. The lawyer submitted it to court without checking. It did not go well for them.
- LLMs have been known to fabricate citations to academic papers that don't exist, with plausible-sounding titles and real-sounding author names.
- Ask a model for a biography of a semi-famous person and it might mix up details from different people, or invent awards they never won.

Why does this happen? Remember: the model doesn't "know" things the way you know things. You know Portland is in Oregon because you have experiences, memories, and a mental model of the world. The LLM generates "Portland is in Oregon" because, given the surrounding text, those tokens are statistically likely to come next. Usually that works fine, because the training data is full of accurate statements about Portland. But the model has no internal fact-checker. It has no way to distinguish between "I'm generating this because it's true" and "I'm generating this because it sounds right."

The model is always -- *always* -- just predicting the next token. Sometimes the most likely next token is factually correct. Sometimes it isn't. The model doesn't know the difference.

**The practical upshot:** always verify important claims from LLMs. Use them as a starting point, not as an authority. If an LLM tells you something and it matters whether that thing is true, check it against a reliable source. Treat it like a very confident friend who sometimes just makes stuff up -- helpful, but not to be trusted without verification.

## The Stochastic Parrot Debate

This is a fun one. (Well, "fun" in the sense that it's a genuinely unresolved question about the nature of intelligence. Your mileage may vary on how fun that sounds.)

In 2021, a group of researchers -- including Timnit Gebru, who we'll meet again in Lesson 12 -- published a paper that referred to LLMs as "stochastic parrots." The argument was: these models are doing very sophisticated pattern matching, but they don't *understand* anything. They're just producing sequences of words that are statistically likely to follow each other, like a parrot that's learned to mimic speech without knowing what the words mean. "Stochastic" just means "random" (well, technically it means "involving randomness") -- so a stochastic parrot is a parrot that repeats things back with some random variation.

Other researchers push back on this. Their argument goes something like: at what point does sufficiently sophisticated pattern matching *become* understanding? If a model can explain quantum physics to a five-year-old, translate poetry between languages, and debug code -- at what point do we stop saying it's "just" pattern matching? Isn't the human brain, in some sense, also a very sophisticated pattern-matching system?

This is genuinely an open question, and smart people disagree about it. There's no answer key at the back of the book for this one. But notice that you've seen a version of this debate before -- back in Lesson 01, when we talked about the Turing Test. If a machine behaves indistinguishably from a thinking being, does it matter whether it's "really" thinking? Turing's question is still haunting us, 75 years later.

My opinion -- and this is just my opinion -- is that the answer matters less than the practical question: regardless of whether LLMs "understand" anything in a philosophically meaningful sense, what are the consequences of deploying them? What happens when people treat them as if they understand? That's a question we can actually work with.

## Connecting the Dots

Let's step back for a second. We've spent the last several lessons building up a picture of how AI works:

- Machine learning models learn from data (Lessons 04-08)
- Deep learning uses layers of neurons to discover complex patterns (Lesson 09)
- LLMs are a specific kind of deep learning model, trained on text, using next-token prediction

When you used ChatGPT in Lab 5, you were interacting with the end result of this entire pipeline. The model had been trained on enormous amounts of code and natural language, and when you asked it to help you write or debug a program, it was predicting -- one token at a time -- what a helpful response would look like, based on patterns it had learned from millions of similar interactions in its training data.

That's not magic. It's not thinking. It's not sentient. But it is remarkably useful, and it's worth understanding both its power and its limitations.

## Discussion Questions

1. **Now that you know how LLMs work** (next-token prediction on massive amounts of text), does that change how you think about using them? Think back to Lab 5 -- does knowing the mechanism behind ChatGPT's responses make you more or less confident in its output?

2. **What tasks would you trust an LLM for? What tasks would you NOT trust it for?** Try to come up with at least three examples for each category, and explain your reasoning.

3. **The stochastic parrot question:** Do you think LLMs "understand" language, or are they just very good at predicting patterns? Does it matter? How does this connect to the Turing Test discussion from Lesson 01?

4. **Have you ever caught an LLM hallucinating?** If so, what happened? If not, try this: ask ChatGPT about a topic you know really well and see if it gets anything wrong. What did you find?
