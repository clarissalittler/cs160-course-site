# Lesson 1 -- What is AI?

**At the end of this lesson, you will be able to:**

- Describe what artificial intelligence actually means in practice -- as opposed to science fiction
- Give a brief account of the history of AI, including the "AI winters"
- Explain the Turing Test and discuss its limitations
- Identify the relationship between AI, machine learning, and deep learning

## So what *is* artificial intelligence?

Let's start with what AI is *not*. It's not a sentient robot. It's not HAL 9000 from *2001: A Space Odyssey*. It's not Skynet. If you came into this lesson picturing a humanoid robot that thinks and feels -- that's totally understandable, because that's what movies and TV have been telling us AI is for decades. But the reality is both more boring and more interesting than that.

AI, as it exists today, is software that finds patterns in data and uses those patterns to make predictions or decisions. That's it. That's the core idea.

You've already been using AI today, probably before you even opened this lesson:

- Your phone's autocomplete? AI.
- Spotify or YouTube recommending songs and videos? AI.
- The spam filter that kept junk out of your inbox? AI.
- Google Maps picking a route for you based on traffic? AI.

None of these things are "thinking" in any meaningful sense. They're programs that have been fed enormous amounts of data and have learned to spot patterns in that data. When your phone suggests the next word in your text message, it's not understanding what you're saying -- it's predicting what word is statistically likely to come next based on patterns it learned from billions of sentences.

## A brief history of AI

The story of AI is a story of big dreams, spectacular failures, and eventual -- if messy -- success.

### The beginning: Turing and the question of machine thought

In 1950, the British mathematician Alan Turing published a paper called "Computing Machinery and Intelligence." This is one of the most important papers in computer science, and it starts with a deceptively simple question: *Can machines think?*

Turing was a fascinating person -- he was instrumental in breaking the Enigma code during World War II, which is widely credited with shortening the war. He was also a gay man in a time when that was criminalized in Britain, and he was prosecuted for it. His story is both brilliant and tragic, and if you're interested, the movie *The Imitation Game* covers parts of his life (though, like all movies, it takes some liberties with the facts).

What matters for us is that Turing proposed a test -- which we now call the Turing Test -- for determining whether a machine could be said to "think." We'll come back to that in a minute.

### The birth of AI as a field

In 1956, a group of researchers gathered at Dartmouth College for a summer workshop. One of the organizers, John McCarthy, coined the term "artificial intelligence" for the event. The researchers were wildly optimistic. They basically thought they'd have human-level AI figured out within a generation. (Spoiler: they did not.)

### The AI winters

Here's where it gets interesting -- and a little cautionary. After that initial burst of optimism, the field of AI went through repeated cycles of hype and disappointment. These periods of disappointment are called **AI winters**.

What happened was: researchers would make big promises ("we'll have thinking machines in 10 years!"), governments and companies would pour money into AI research, the promises wouldn't pan out on schedule, and then everyone would pull their funding. This happened at least twice -- once in the 1970s and again in the late 1980s and early 1990s.

The lesson here -- and it's one we'll keep coming back to in this unit -- is that hype can be dangerous. When people overpromise and underdeliver, it doesn't just hurt the people who wasted money. It can set back an entire field by making everyone skeptical of legitimate progress.

### The current boom

So what changed? Why is AI suddenly everywhere? Two things, mainly:

1. **Data.** The internet happened. Social media happened. Smartphones happened. We now generate absolutely staggering amounts of data every single day. And as we'll learn later, AI -- especially machine learning -- is hungry for data. The more data you feed it, the better it gets.

2. **Computing power.** The hardware got dramatically faster and cheaper. In particular, graphics processing units (GPUs) -- originally designed for rendering video game graphics -- turned out to be incredibly well-suited for the kinds of math that AI requires. This was a bit of a happy accident, honestly.

The combination of massive datasets and powerful hardware is what's driving the current AI boom. It's not that we suddenly got smarter about AI theory (though there have been some important breakthroughs). It's mostly that we finally have the raw materials -- data and compute -- to make decades-old ideas actually work at scale.

## The Turing Test

Let's come back to Turing's big idea. The Turing Test works like this: a human judge has a text conversation with two hidden participants -- one human and one computer. If the judge can't reliably tell which is which, the computer is said to have "passed" the test.

It's an elegant idea. Instead of trying to define what "thinking" means (which is a philosophical nightmare), Turing sidestepped the whole question. He basically said: if it *looks* like thinking to a reasonable observer, that's good enough.

### Why some people think the Turing Test isn't great

The Turing Test was groundbreaking in 1950, and it's still historically important. But over the decades, a lot of people have pointed out problems with it:

- **It only tests conversation.** A machine could be terrible at everything else -- reasoning, learning, understanding the world -- but if it's good enough at text chat, it passes. Is that really intelligence?
- **It rewards trickery.** Some programs have "passed" versions of the Turing Test by being evasive, changing the subject, or pretending to be a non-native English speaker. That's not intelligence, that's social engineering.
- **It's anthropocentric.** It assumes intelligence has to *look human*. But couldn't a program be intelligent in a way that's very different from how humans think? A chess AI is extraordinarily good at chess, but it wouldn't pass the Turing Test because it can't chat about the weather.
- **Modern chatbots have kind of broken it.** Large language models like ChatGPT can fool people in casual conversation. Does that mean they're intelligent? Most AI researchers would say no -- they're very good at producing human-sounding text, but that's not the same as understanding.

The Turing Test is a great starting point for *thinking about* machine intelligence, even if it's not a great *test* of machine intelligence. And honestly, the fact that we're still arguing about it 75 years later tells you something about how hard this question is.

## The AI family tree

One thing that can be confusing about AI is that people use a bunch of terms -- AI, machine learning, deep learning -- and sometimes use them interchangeably, which is technically wrong. Here's the actual relationship:

- **Artificial Intelligence** is the big umbrella. It covers any technique that allows computers to mimic human-like capabilities -- making decisions, recognizing speech, translating languages, &c. Some AI techniques don't involve learning at all. The AI in early video game enemies, for example, was just a set of hand-written rules ("if player is within 10 feet, attack").

- **Machine Learning (ML)** is a *subset* of AI. It's the specific approach where instead of programming rules by hand, you feed the computer a bunch of examples and let it figure out the patterns on its own. We'll spend a lot of time on this in the next few lessons.

- **Deep Learning** is a *subset* of machine learning. It uses structures called neural networks (loosely inspired by the human brain, though calling them "brain-like" is a pretty big stretch). Deep learning is what powers most of the flashy AI stuff you've seen lately -- image generation, voice assistants, ChatGPT, &c.

So: all deep learning is machine learning, and all machine learning is AI, but not all AI is machine learning, and not all machine learning is deep learning. It's a nesting-doll situation.

## Discussion questions

Take a few minutes to think about these -- and feel free to discuss them with classmates:

1. **Where have you encountered AI in your daily life?** Make a list. You might be surprised how long it gets. Think about your phone, your email, streaming services, shopping websites, social media, navigation apps, &c.

2. **Before this lesson, what did you think AI was?** Has your understanding changed? If so, how?

3. **Do you think the Turing Test is a good measure of intelligence? Why or why not?** If you had to design a better test, what would it look like?

4. **The AI field has gone through cycles of hype and disappointment before.** Do you think the current AI boom is different from previous ones? Why or why not? (There's no wrong answer here -- this is genuinely debated by experts.)
