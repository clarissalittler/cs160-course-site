# Lesson 1 --- Iteration Structures

![Unit 5 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Explain how iteration control structures are used to repeat the execution of a group of statements in programs.

---

## Textbook reading

Read through [Section 8.1](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/intro-IterationRevisited.html) from [Chapter 8, Iteration](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/toctree.html) in the Runestone Academy textbook. This section introduces iteration statements (a.k.a. loops). They mention `for` loops in there --- don't worry about those yet. Just focus on the general *concept* of looping for now.

## Lesson video

[Video: Intro to Loops](https://www.youtube.com/watch?v=1sujgJwa0cM)

## What is iteration?

So far, our programs have run straight through from top to bottom --- do this, then that, then the next thing, done. But what if you need to do the same thing 100 times? Or keep doing something until some condition changes? You're not going to write the same line of code 100 times. (I mean, you *could*, but please don't.)

That's where **iteration** comes in. Iteration --- also called **repetition** --- is just the idea of repeating a block of instructions.

![Iteration structure - statements executed zero or more times](images/iteration.png)
*Figure 5.1. Iteration structure*

Here's what you need to know:

- Iteration structures make the computer repeat code as necessary --- this is the whole point.
- There are two flavors: **condition-controlled loops** and **count-controlled loops**.
- A **condition-controlled loop** uses a true/false condition to decide how many times to repeat. ("Keep going *while* the user hasn't typed 'quit'.")
- A **count-controlled loop** repeats a specific number of times. ("Do this exactly 10 times.")

That's it for the big picture. In the next lessons, we'll dig into the actual Python syntax for both kinds --- `while` loops (condition-controlled) and `for` loops (count-controlled). Let's go.
