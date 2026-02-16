# Lesson 1 --- Algorithms

![Unit 3 banner](img/banner.jpg)

> **After this lesson, you'll be able to:**
>
> - Develop an algorithm to build a Lego structure.
> - Test an algorithm with different input data.

## Textbook resource

Read through [Chapter 1, Section 1.2, Algorithms](https://runestone.academy/runestone/books/published/thinkcspy/GeneralIntro/Algorithms.html) from Runestone Academy. It's a free online textbook and an excellent companion for this class.

## So what's an algorithm?

Computers are designed to do whatever their programs tell them to do. And remember from earlier --- all computers really do four things: take input, store data, process data, and give output. That's it. Everything your phone, your laptop, your game console does boils down to those four operations. Kind of wild, right?

A **program** is a set of instructions --- called an **algorithm** --- that a computer follows to perform a task. Programs are written in programming languages, and people commonly call them "software" or "code."

Here's a great introductory video on what algorithms actually are:

[Video: Computer Science Basics: Algorithms](https://www.youtube.com/watch?v=kM9ASKAni_s)

If problem-solving is the heart of computer science, then the solutions you come up with through that process are just as important. In computer science, we call those solutions **algorithms**.

An algorithm is a step-by-step method for accomplishing some task. In CS, algorithms are precise sequences of instructions for processes that can be executed by a computer, and they're implemented using programming languages.

The word "algorithm" itself comes from the name of a 9th-century Persian mathematician, al-Khwarizmi, who wrote one of the first books on systematic problem-solving. So when you write an algorithm, you're carrying on a tradition that's over a thousand years old.

Let's practice writing an algorithm with virtual Legos!

## Activity: Lego algorithms

You're going to write an algorithm to build a structure you design with a set of Lego "blocks." You'll play the role of **programmer** and write a "program" to build a Lego structure. After you're done, you'll give the "program" to another student who will play the role of **computer** and execute your instructions --- *exactly* as they are written.

This is where it gets fun (and sometimes hilariously frustrating).

![Example of a structure made with Lego blocks](images/legos.png)
*Figure 3.1. Example Lego structure*

**Directions:**

- Open the [Lego slide deck](https://docs.google.com/presentation/d/156FOmQ_zln5wHF8e4O0Vswn_sw9cLaJ5p3kPQ9e1Hx4/copy?usp=sharing). A copy will be made for you. Change the permissions to allow anyone with the link edit access: Share -> "anyone with the link can edit." You'll need to change *Viewer* to *Editor*.
- You can't change the blocks in any way (color, size, shape), but you *can* rotate and move them.
- You can't add more blocks or delete any, but you can move some aside to make more space.
- Design a structure, then write the steps to build it in the speaker notes at the bottom of the slide.
- You must use at least 5 blocks (you don't have to use all of them).
- When you're done writing your algorithm, take a screenshot of your structure, then mix up the blocks --- we shouldn't be able to see your structure anymore.

## Discussion prompt

> **Complete on your own!**
>
> Open [LMS Activity: Unit 3 Lesson 1 - Legos] for the full list of directions. You'll write an algorithm to build a structure you design with Lego blocks, play the role of "programmer," and then hand your program off to another student who will play "computer" and follow your instructions exactly as written.

## Problem-solving with algorithms

Algorithms are steps to solve a problem. Hopefully the Lego activity showed you how important it is to include *detailed* steps and not leave anything for someone (or some*thing*) to guess at!

Here's an example of a problem we can solve with a computer:

**Problem:** Write an algorithm to find and print the minimum of two numbers, x and y.

**Algorithm:**

```
if x is smaller than y
   print x
else
   print y
```

When we look at the numbers 2 and 5 on a piece of paper, we *intuitively* know that 2 is smaller than 5. Behind that intuition is a familiarity with numbers we've built up over years of experience, both in and out of school. Computers don't have that kind of intuition --- they have to perform mathematical calculations to figure out which number is smaller.

After we develop an algorithm, it's crucial to **test** it to make sure it works with all possible cases. When comparing two numbers, what could the outcomes be?

- x could be smaller than y
- y could be smaller than x
- x and y could be the same number

Let's choose some test data:

- x = 2 and y = 4
- x = 4 and y = 2
- x = 2 and y = 2

Run through the algorithm above with all three scenarios. Does it work?

That third case is the interesting one --- what happens when x and y are equal? Our algorithm says "if x is smaller than y, print x; *else* print y." If they're equal, x is *not* smaller than y, so we print y. And that's fine, because they're the same number! But it's exactly the kind of edge case that trips people up if you don't think about it carefully. Get in the habit of asking: "What could go wrong here?"
