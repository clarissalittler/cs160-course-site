# Unsupervised and Reinforcement Learning

## Learning Outcomes

By the end of this lesson, you should be able to:

- Explain how unsupervised learning finds patterns without labeled data
- Describe clustering and give a real-world example of it
- Explain how reinforcement learning uses rewards and punishments to learn through trial and error
- Choose the right type of machine learning for a given problem

## Unsupervised Learning: Finding Structure Without Labels

Last lesson we talked about supervised learning, where you give the model labeled examples and it learns the mapping from input to output. That's great when you have labels — but what if you don't?

That's where **unsupervised learning** comes in. In unsupervised learning, you give the model a bunch of data with **no labels** — no "right answers" — and ask it to find structure on its own. You're basically saying "here's a pile of data, find me something interesting."

This might sound vague, and honestly, it kind of is. That's part of what makes unsupervised learning both powerful and tricky. You don't always know exactly what you'll get.

### Clustering: Grouping Similar Things Together

The most common unsupervised learning technique is **clustering** — automatically grouping similar items together. The algorithm looks at the data, measures how similar or different things are from each other, and forms groups.

Here's a concrete example that I think makes this really click:

**The music library problem.** Imagine you have a pile of 1,000 songs and you want to organize them — but you have no genre labels at all. No one has tagged anything as "jazz" or "rock" or "electronic." All you have is the raw audio.

An unsupervised clustering algorithm could analyze audio features of each song — things like tempo, key, energy level, how much bass there is, whether there are vocals — and group songs that sound similar together. The clusters that emerge might roughly correspond to what we'd call genres. One cluster might be mostly fast, high-energy songs with heavy bass (probably electronic or hip-hop). Another might be slow, acoustic songs with vocals (maybe folk or singer-songwriter stuff).

But here's the important thing: **the algorithm doesn't know the word "jazz."** It has no concept of genre. It just found a pattern — these songs are similar to each other and different from those songs. You, the human, look at the clusters and go "oh, that's basically jazz." The structure was in the data all along; the algorithm just surfaced it.

### The Laundry Analogy

Here's an even more everyday way to think about it. Imagine you're sorting a big pile of laundry, and nobody has given you any rules about how to sort it. No labels, no instructions. What would you do?

You'd probably start grouping things naturally — darks over here, whites over there, delicates in a separate pile, towels together, &c. Nobody told you those categories. You just looked at the items, noticed similarities and differences, and created groups that made sense.

That's unsupervised learning. You found the structure yourself.

### Real-World Uses of Unsupervised Learning

Unsupervised learning shows up in more places than you might expect:

- **Google News grouping:** When a big news story breaks, Google News groups dozens of articles from different sources under one headline. No one manually labeled those articles as "about the same story." A clustering algorithm figured it out by looking at the content.

- **Customer segmentation:** Marketing teams use clustering to group customers by purchasing behavior. Maybe one cluster is "bargain shoppers who only buy during sales" and another is "loyal customers who buy regularly at full price." These groups weren't pre-defined — they emerged from the data.

- **Anomaly detection:** This one's really cool. If you cluster a million credit card transactions and 999,990 of them fall neatly into normal patterns, but 10 of them are way out in the middle of nowhere — those are your suspicious transactions. The algorithm didn't know what "fraud" looks like; it just found the things that don't fit the pattern. That's anomaly detection, and banks use it constantly.

## Reinforcement Learning: Learning by Trial and Error

Now let's talk about a completely different approach to learning. Reinforcement learning isn't about labeled examples (that's supervised) and it isn't about finding hidden structure (that's unsupervised). It's about **learning from experience through rewards and punishments**.

### The Mouse in the Maze

The classic analogy here is a mouse in a maze.

The mouse doesn't have a map. Nobody told it where the cheese is. It just starts wandering. It tries going left — dead end. It tries going right — another dead end. It backtracks, tries a different path, and eventually... cheese! Reward!

Next time through the maze, the mouse remembers a little bit about what worked and what didn't. It still makes some mistakes, but fewer. After running the maze hundreds of times, the mouse has learned the optimal path — not because anyone taught it, but because it experimented, got feedback (cheese = good, dead end = bad), and adjusted its behavior.

That's reinforcement learning in a nutshell:

1. An **agent** (the mouse, or an AI) takes **actions** in an **environment** (the maze)
2. The environment gives back a **reward signal** (cheese!) or a **punishment signal** (dead end)
3. The agent adjusts its **strategy** to get more rewards over time
4. Repeat. A lot. Like, thousands or millions of times.

### This Is How Game-Playing AIs Work

Reinforcement learning is behind some of the most impressive AI achievements you may have heard about:

- **AlphaGo** (by DeepMind) beat the world champion at Go — a board game so complex that brute-force search can't solve it. The AI played millions of games against itself, getting a reward when it won and a punishment when it lost, and gradually developed strategies that surprised even expert human players.

- **OpenAI Five** learned to play Dota 2, a complex team-based video game, at a professional level. Same idea — play millions of games, learn from wins and losses.

- **Robotics:** Reinforcement learning is used to teach robots to walk, pick up objects, and navigate rooms. The robot tries things, falls over a lot (in simulation, thankfully), and slowly figures out how to move without toppling. It's weirdly adorable to watch, honestly — there are great videos of simulated robots learning to walk and they look like baby deer at first.

- **Self-driving cars** use elements of reinforcement learning too — learning how to navigate traffic by getting feedback on safe and unsafe decisions.

### The Key Difference from Supervised Learning

In supervised learning, you explicitly tell the model the right answer for every example. "This email is spam. This one isn't. This house sold for $450,000."

In reinforcement learning, **nobody tells the agent the right answer.** You just give it a reward signal. The agent has to figure out on its own which actions led to good outcomes. It discovers strategies through experimentation, not instruction.

This makes reinforcement learning incredibly powerful for problems where we can't easily provide "right answers" — like games, robotics, and navigation. How would you label the "correct" move at every point in a Go game? There are more possible board positions than atoms in the universe. You can't build a labeled dataset for that. But you *can* say "you won" or "you lost" at the end and let the AI figure it out.

## So When Do You Use What?

Here's a handy mental framework for choosing the right type of machine learning:

| Situation | Type | Example |
|---|---|---|
| You have data **with labels** (known answers) | **Supervised** | Email spam detection, house price prediction |
| You have data **without labels** | **Unsupervised** | Customer grouping, organizing a music library |
| You have an **environment** the agent can interact with | **Reinforcement** | Game AI, teaching a robot to walk |

A few things worth noting:

- **Supervised learning** is the most common in practice, because a lot of business problems come with historical data that has labels (past sales, past decisions, &c.).
- **Unsupervised learning** is great for exploration — when you want to understand the structure of your data before you even know what questions to ask.
- **Reinforcement learning** is the most exciting to watch (robots! games!) but also the hardest to get right. It requires a lot of trial-and-error, which means a lot of computation, and defining a good reward signal is trickier than it sounds.

In the real world, these types often get combined. A self-driving car might use supervised learning to recognize stop signs (classification), unsupervised learning to understand typical traffic patterns, and reinforcement learning to decide when to change lanes. The boundaries aren't always clean — and that's fine.

## Discussion Questions

1. Think about how a streaming service like Spotify or Netflix recommends content to you. Which type(s) of machine learning do you think they're using? Could it be a combination? Explain your reasoning.

2. We said that in reinforcement learning, "defining a good reward signal is trickier than it sounds." Why do you think that is? Can you think of a case where a badly designed reward might cause an AI to learn the wrong thing? (Hint: what if you reward a cleaning robot for not seeing any mess — could it learn to just close its eyes?)

3. Imagine you run a food cart in Portland and you have a year's worth of sales data — date, weather, what you sold, how much you sold. You don't have any labels or categories. What could unsupervised learning help you discover about your business? What patterns might emerge?

## Activity: Classify the Problem

For each scenario below, decide: is this a **supervised**, **unsupervised**, or **reinforcement** learning problem? Explain your reasoning.

1. A bank wants to predict whether a loan applicant will default based on their credit history, income, and employment status. (They have records of past loans and whether each borrower defaulted.)

2. A biologist has collected genetic data from 500 plant samples and wants to see if there are natural groupings among them that might represent different subspecies. No subspecies labels exist yet.

3. A company is building an AI to play chess at a competitive level.

4. An online store wants to predict how much a customer will spend in the next month, based on their past purchases.

5. A city transportation department has GPS data from thousands of bus rides and wants to find routes that are commonly delayed — but they haven't defined what counts as "delayed" vs. "on time."
