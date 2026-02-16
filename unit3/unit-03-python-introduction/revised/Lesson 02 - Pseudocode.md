# Lesson 2 --- Pseudocode

![Unit 3 banner](img/banner.jpg)

> **After this lesson, you'll be able to:**
>
> - Use pseudocode to plan out your programs before writing code.

## What is pseudocode?

In the previous lesson, you learned how to write an algorithm for solving a problem. The next step is to express that algorithm in a language a computer can understand. But before you write a single line of actual code, let's talk about the importance of *planning* --- using something called **pseudocode**.

Pseudocode is basically writing out your program's logic in plain English. It's not a real programming language --- you can't run it, and no computer will understand it. That's the whole point. It's for *you*, the human. Think of it the same way you'd think about making an outline before writing a paper. You wouldn't just start typing an essay from the first word to the last without knowing where you're headed, right? (Okay, maybe you would at 2am the night before it's due, but it's not the *ideal* approach.)

[Video: U3L2 Pseudocode](https://www.youtube.com/watch?v=jw6TFKhUTZo)

The video introduced you to the purpose of pseudocode, and the example works well for giving steps to another *human* to follow. But there are details missing that a computer would need to solve the problem! In Lesson 10, we'll come back and modify this algorithm to work for writing an actual Python program.

## Why bother with pseudocode?

Programs can get complex and long, and preparation is the key to not losing your mind halfway through. Pseudocode makes creating programs easier because it lets you think about the *logic* without getting bogged down in the specific rules of a programming language.

To write pseudocode, you just describe what you want your program to do in your own words, using short statements. There are no special commands. It's not standardized. You can write it however you want. The big advantage is that writing out your plan *before* you start coding lets you organize your thoughts and spot gaps in your logic --- places where you might have left out a needed step.

> **Important!** Don't skip this step when writing programs. Seriously. Read the problem, and think about how you'd explain the solution to someone. Don't worry about phrasing things perfectly --- just make sure your steps are detailed enough that someone could follow them to solve the problem. Think of it like writing a recipe for cookies: "mix the dry ingredients" is a step, but a more helpful step is "combine 2 cups flour, 1 tsp baking soda, and 1/2 tsp salt in a bowl."

## Examples of pseudocode

Let's look at a few examples to get the feel for it.

**Adding two numbers and displaying the result:**

```
Input two numbers, A, B
Compute sum = A + B
Print sum
```

**Computing the area of a rectangle** (the asterisk `*` means multiplication):

```
Input the length
Input the width
Compute area = length * width
Display area
```

**Computing the perimeter of a rectangle:**

```
Input length
Input width
Compute perimeter = (2 * length) + (2 * width)
Display perimeter
```

See how readable that is? You don't need to know any programming language to understand what's happening. That's the beauty of pseudocode.

## A note about syntax

Here's a word you'll hear a lot: **syntax**. Syntax is a set of rules for how to use and organize statements in a programming language --- kind of like grammar rules in English. "The cat sat on the mat" follows English syntax; "mat the on sat cat the" doesn't.

Basic pseudocode doesn't have strict syntax rules --- you can write it however makes sense to you. But some companies do use specific pseudocode conventions so that everyone on the team writes pseudocode the same way. That way more people can study the algorithm, and errors are easier to find and fix.

In the next lesson, you'll be introduced to **Python**, the programming language we'll use for the rest of this course. Python has a very specific set of syntax rules that *must* be followed for the computer to understand and execute your program. No wiggle room. But don't worry --- we'll take it step by step.
