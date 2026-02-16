# Lesson 11 --- Worst Case Comparisons

> **What you'll be able to do after this lesson:**
>
> - Use formulas to describe and compare the worst case time efficiency of sorting algorithms.

## Putting Our Formulas to Work

Now that we've got formulas to describe worst case time efficiency, let's see how our sorting algorithms actually perform as we crank up the number of items. First, a quick review of the formulas. Notice that the swap formulas have been converted to **copies** by multiplying by 3 --- this lets us do a fair apples-to-apples comparison between the two sorts.

| Algorithm | Comparisons | Copies |
|---|---|---|
| Insertion Sort | (*n* - 1) + (*n* - 2) + ... + 1 | 3 * [(*n* - 1) + (*n* - 2) + ... + 1] |
| Selection Sort | (*n* - 1) + (*n* - 2) + ... + 1 | 3 * (*n* - 1) |

## Comparisons Required

Using our formulas, let's compute the number of comparisons needed for lists of increasing size --- each one ten times bigger than the last:

| # of Items | Insertion Sort | Selection Sort |
|---|---|---|
| 10 | 45 | 45 |
| 100 | 4,950 | 4,950 |
| 1,000 | 499,500 | 499,500 |
| 10,000 | 49,995,000 | 49,995,000 |

From this table, we can see that both sorts require the **exact same number of comparisons**. We can also rewrite the summation formula in a much friendlier way:

> (*n* - 1) + (*n* - 2) + ... + 1 = (*n* * (*n* - 1)) / 2

This closed-form expression is way easier to work with than writing out the whole summation, especially when *n* is large.

Both sorts require a *tremendous* number of comparisons as the number of items grows. Going from 10 items to 10,000 items doesn't just multiply the work by 1,000 --- it explodes.

## Copies Required

Now let's compare the number of copies each algorithm needs:

| # of Items | Insertion Sort | Selection Sort |
|---|---|---|
| 10 | 135 | 27 |
| 100 | 14,850 | 297 |
| 1,000 | 1,498,500 | 2,997 |
| 10,000 | 149,985,000 | 29,997 |

Whoa. Look at that Insertion Sort column --- it's growing *fast*. That makes us suspect the formula contains an *n*^2 term. And it does! We just have to rewrite the formula to see it. Using the relationship we discovered earlier, we can replace the summation with the closed form and simplify:

> **# of copies** = 3 * [(*n* - 1) + (*n* - 2) + ... + 1]
>
> **# of copies** = 3 * [(*n* * (*n* - 1)) / 2]
>
> **# of copies** = (3/2) * [*n* * (*n* - 1)]
>
> **# of copies** = (3/2) * [*n*^2 - *n*]

There it is --- the *n*^2 term we suspected. Notice that the Selection Sort's copy formula only has an *n* term (not *n*^2), which is why it grows so much more slowly as the list gets bigger.

## Worked Example: Selection Sort

> **Example problem using Selection Sort:**
>
> The summation (*n* - 1) + (*n* - 2) + ... + 1 can be written as (*n* * (*n* - 1)) / 2, and the formula for copies is 3 * (*n* - 1).
>
> Given *n* = 5, the worst case performance is the sum of comparisons and copies:
>
> - comparisons = (*n* * (*n* - 1)) / 2 = (5 * 4) / 2 = **10**
> - copies = 3 * (*n* - 1) = 3 * 4 = **12**
>
> **Total number of operations = 22**

## Discussion Activity

> **Complete on your own!**
>
> The sorting algorithms we've learned so far --- Insertion Sort and Selection Sort --- are both **quadratic** time algorithms. They require a worst case amount of work proportional to *n*^2 to sort *n* items. But there are sorting algorithms out there that do *much* better. A common feature of most of them is some kind of reliance on a **divide and conquer** strategy.
>
> Find a better sorting algorithm online and, in your own words, explain why it's better than the Insertion Sort and Selection Sort we've seen so far.

[LMS Activity: Post your algorithm to Unit 7 Lesson 11 - Sorting Efficiencies discussion]

---

*Materials on this page adapted from: Online Interactive Modules for Teaching Computer Science by Osman Balci et al.*
