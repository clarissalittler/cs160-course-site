# Lesson 09 --- Algorithm Analysis

> **What you'll be able to do after this lesson:**
>
> - Define algorithm efficiency and identify the two different ways we measure how efficient an algorithm is.

## Algorithm Efficiency

Here's a question worth sitting with: if there are multiple correct algorithms that solve the same problem, how do we decide which one to use?

Sorting is a perfect example. Dozens of different sorting algorithms exist --- we've already looked at two of them --- and they all produce the same result: a sorted list. So what makes one "better" than another?

The answer is **efficiency**. We analyze our algorithms to measure how much work they do, and then we compare those measurements. The algorithm that does less work wins.

We can actually measure efficiency in two different ways: **space efficiency** and **time efficiency**.

| Type of Efficiency | What It Measures |
|---|---|
| Space | Amount of computer memory used |
| Time | Number of copies, swaps, and comparisons performed |

An algorithm that's space-efficient uses the least memory. An algorithm that's time-efficient does the fewest operations. Since most of what sorting algorithms do is compare values, copy values, and swap values, we can just count those operations and use the totals as our measure of time efficiency.

Let's put our two sorts head-to-head.

## Space Efficiency

We'll start with space. How much memory does each algorithm need?

For simplicity, we'll say one memory cell holds one number. So if you're sorting five numbers, you need at least five cells just to store them. The question is: how many *extra* cells does the algorithm need on top of that?

Both insertion sort and selection sort are equally space-efficient. They sort items *in place* using the swap operation. The only extra memory they need is one temporary cell for swapping. That's why, for 7 numbers, both algorithms use 8 memory cells --- the 7 you're sorting plus 1 temp cell for swaps.

| Algorithm | Memory Cells |
|---|---|
| Insertion Sort | 8 |
| Selection Sort | 8 |

A tie. Fair enough.

## Time Efficiency

Now the more interesting question: which sort is faster?

To measure this, we count the number of operations each sort performs. Most operations in sorting fall into two buckets: **comparing** numbers and **copying** numbers. The algorithm that requires the least comparing and copying will execute the fastest.

For insertion sort and selection sort, it's easier to count **swaps** rather than individual copies. Remember, each swap is really three copies under the hood (value into temp, second value into first slot, temp into second slot). So you can always multiply swaps by three to get your copy count.

### Comparing the Two Sorts

Let's look at how they perform on this specific list of 7 numbers:

> **7, 8, 5, 2, 4, 6, 3**

| Algorithm | Copies | Comparisons |
|---|---|---|
| Insertion Sort | 45 | 19 |
| Selection Sort | 15 | 21 |

Interesting. Selection sort does way fewer copies (15 vs. 45) but slightly more comparisons (21 vs. 19). For this particular list, selection sort comes out ahead on time efficiency overall.

But --- and this is a big "but" --- **that result depends on the input data**.

Consider this nearly-sorted list instead:

> **2, 3, 4, 5, 7, 6, 8**

If we use insertion sort here, we'd only need **7 comparisons and 1 swap**. But selection sort would still grind through **21 comparisons and 1 swap**. In this case, insertion sort is way more efficient.

This is one of the genuinely fascinating things about algorithm analysis: there isn't always a single "best" algorithm. The answer can change depending on the data you're working with. Selection sort doesn't care whether your list is nearly sorted or totally scrambled --- it always does the same number of comparisons. Insertion sort, on the other hand, gets a huge advantage when the data is already close to sorted, because elements don't have to shift very far.

So the real answer to "which sort is better?" is the classic computer science answer: *it depends*.
