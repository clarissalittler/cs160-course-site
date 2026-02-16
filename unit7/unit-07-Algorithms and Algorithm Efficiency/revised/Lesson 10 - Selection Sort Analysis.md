# Lesson 10 --- Selection Sort Analysis

> **What you'll be able to do after this lesson:**
>
> - Perform worst case analysis on an algorithm, and derive formulas for counting comparisons and swaps.

## Analysis

In our last lesson, we saw that the measured time efficiency of a sorting algorithm can change depending on the order of the items being sorted. Because of this, it's common to measure sorting performance using the *worst possible* conditions.

> **The worst case is the particular order of items that will require the greatest number of comparisons and swaps to sort.**

Think of it this way: if you can guarantee the algorithm finishes in a certain amount of time even under the absolute nastiest conditions, you've got a solid performance guarantee. That's why computer scientists love worst case analysis --- it's the pessimist's approach, and it works.

## Walking Through Selection Sort on 4 Items

This video walks you through exactly how much work Selection Sort does on a list of just 4 items:

[Video: Selection Sort Efficiency](https://www.youtube.com/watch?v=zm75IhDgO-Y)

*Animation used by permission of Virginia Tech*

## The Formulas

Here are the formulas we derived for the number of comparisons and swaps Selection Sort requires in the worst case. We're using *n* to represent the number of items being sorted.

> **# of swaps** = (*n* - 1)
>
> **# of comparisons** = (*n* - 1) + (*n* - 2) + ... + 1

Notice that the formula for comparisons is a **summation** --- a series of terms added together. Each term represents the comparisons from one step of our sort. As we increase the number of items to sort, we also increase the number of terms in the formula. That's the key insight here.

## A Worked Example

Let's say we're sorting six items and we want to know the maximum number of comparisons needed --- the worst case. Here's how we'd figure it out.

First, we write out the correct number of terms. Remember that *n* = 6 in this example. The last term is (*n* - 5) because that equals 1.

> **# of comparisons** = (*n* - 1) + (*n* - 2) + (*n* - 3) + (*n* - 4) + (*n* - 5)

Now we substitute 6 for *n* and sum the values:

> **# of comparisons** = (6 - 1) + (6 - 2) + (6 - 3) + (6 - 4) + (6 - 5)
>
> **# of comparisons** = 5 + 4 + 3 + 2 + 1
>
> **# of comparisons** = 15

So when sorting six items with Selection Sort, the algorithm will need to perform at most 15 comparisons. Since we computed the worst case, we know Selection Sort will *never* need more than 15 comparisons for six items, no matter how they're originally ordered. That's the beauty of worst case analysis --- it's an upper bound you can count on.

---

*Materials on this page adapted from: Online Interactive Modules for Teaching Computer Science by Osman Balci et al.*
