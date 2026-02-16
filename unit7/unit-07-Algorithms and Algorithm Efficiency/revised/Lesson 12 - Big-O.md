# Lesson 12 --- Big-O

> **What you'll be able to do after this lesson:**
>
> - Understand Big-O classification and assign algorithms to a class of functions that describe their growth rate.

## Order Notation

In the last lesson, we discovered that we can represent the efficiency of our sorting algorithms with formulas. We derived those formulas by identifying the most important operations --- comparisons, copies, swaps, &c. --- and counting how many of them were required to sort a specific number of items. Then we found a general pattern and used it to write our formula.

For example, we ended up with something like this for Insertion Sort copies:

**# of copies** = (3/2) * [*n*^2 - *n*]

Since the largest term in this formula is *n*^2, the number of operations grows *very* quickly. We also saw a couple of other formulas whose largest term was just *n*, and those showed much more moderate growth.

Here's the key insight: **the largest term in an algorithm's efficiency formula has an enormous effect on how the algorithm performs as input grows.** Everything else is just noise by comparison.

## Big-O Classification

This is the idea behind what's known as **Big-O** classification: we assign each algorithm to a class of functions that describes how its work grows. Some common categories are:

- **Constant** --- O(1)
- **Logarithmic** --- O(log n)
- **Linear** --- O(n)
- **Quadratic** --- O(n^2)

![Big O Notation](../CommonBigOs.jpg)

In the graph above, the x-axis represents *n* --- the number of items in your list. The y-axis represents the amount of work, *f(n)*, required to finish the algorithm.

An algorithm whose highest term is *n*^2 would be called an **O(n^2) algorithm** (pronounced "order-n-squared"). An algorithm with *n* as its highest term is an **O(n) algorithm** ("order-n"). Two other common classes are O(2^n) and O(log n). The figure shows you how these four classes compare --- and the differences are dramatic.

That's the whole point of Big-O. We don't care about the exact number of operations. We care about the *shape* of the growth curve. An algorithm that does 3*n*^2 + 100*n* + 57 operations is still O(n^2) --- because once *n* gets big enough, that *n*^2 term dominates everything else. The constants and smaller terms just don't matter at scale.

> **Important:**
>
> **Selection Sort** and **Insertion Sort** are both **Quadratic** --- O(n^2)

That's not great, honestly. Quadratic algorithms slow down *hard* as your data grows. But knowing that is the first step toward finding something better.

---

*Materials on this page adapted from: Online Interactive Modules for Teaching Computer Science by Osman Balci et al. and the [Chemeketa Community College CS160 Reader](https://computerscience.chemeketa.edu/cs160Reader/Algorithms/BigO.html).*
