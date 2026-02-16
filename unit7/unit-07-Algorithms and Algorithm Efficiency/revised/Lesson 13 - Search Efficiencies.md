# Lesson 13 --- Search Efficiencies

> **What you'll be able to do after this lesson:**
>
> - Compare the efficiency of Binary Search and Linear Search using Big-O notation.

## Linear Search

Say you've got an unsorted pile of tests and you're looking for one particular student's paper. In the **best case**, it's sitting right on top --- one unit of work and you're done. In the **worst case**, if you go through the pile top to bottom, it's the very last paper. You'd have to look at every single one. And that worst case also applies if the paper isn't even in the stack --- you'd have to check every paper just to figure that out.

On average? Somewhere in between. Sometimes you get lucky, sometimes you don't. In general, you'd have to look at about half the papers.

Here are those three scenarios summarized:

| Model | Work for *n* Papers | Big-O |
|---|---|---|
| Best Case | f(n) = 1 | O(1) |
| Average Case | f(n) = n/2 | O(n) |
| Worst Case | f(n) = n | O(n) |

Notice something here: in terms of Big-O, *f(n) = n/2* is the same as *f(n) = n*. They're both linear functions. Remember, Big-O doesn't care about constants --- it cares about the *shape* of the growth.

And sure, the best case is O(1), but we can't count on always having the one we want sitting right on top. Basing our rating on that rare lucky break would be misleading.

> **Important:**
>
> Linear Search is **O(n)** --- Linear
>
> This demonstrates a common pattern: the best case normally doesn't tell us much --- it's too rare. The average case and worst case are often (though not always) the same Big-O class.

Kind of makes sense that **linear** search is a **linear** algorithm, right?

## Binary Search

Remember that Binary Search relies on jumping to the middle of the unchecked items and --- if it's not what we want --- throwing out half of the remaining items based on what we learned. It's the "guess the number" strategy, and it's devastatingly effective.

In the best case, we jump to the middle and find exactly what we're looking for --- one unit of work. But once again, that's a rare event. Let's look at the worst case instead.

Imagine we're searching a list of 1,000 items. If we have to keep halving until there's just 1 possible item left, here's what that process looks like:

| Items Left to Search | Comparisons So Far |
|---|---|
| 1,000 | 0 |
| 500 | 1 |
| 250 | 2 |
| 125 | 3 |
| 62 | 4 |
| 31 | 5 |
| 15 | 6 |
| 7 | 7 |
| 3 | 8 |
| 1 | 9 |
| 0 | 10 |

Ten comparisons. For a thousand items. That's... kind of amazing.

Instead of counting how many times we divide the starting number by 2, we can calculate it directly using a **logarithm**. Taking the base-2 logarithm of a number asks: *"How many times do I have to divide this number by 2 to reach 1?"*

Calculating log2(1000) gives us 9.96. Since we can't do 0.96 of a comparison (hard to see how you check 96% of a paper), we round up to 10. That matches our table perfectly.

> **Important:**
>
> Binary Search is **O(log n)** --- Logarithmic
>
> Now, go back to Lesson 3. Do you see why we used the log function on line 16 to calculate the TARGET guesses? It all connects.

## Comparison

So how do Binary Search and Linear Search actually stack up against each other? Let's look at worst case work:

| List Size | Linear Search | Binary Search |
|---|---|---|
| 10,000 | 10,000 | 14 |
| 100,000 | 100,000 | 17 |
| 1,000,000 | 1,000,000 | 20 |
| 1,000,000,000 | 1,000,000,000 | 30 |

Read that last row again. One *billion* items, and Binary Search needs just 30 comparisons. Linear Search needs one billion. That's not a typo. That's the power of logarithmic growth.

The graph tells the same story. Next to a linear graph, a logarithmic one appears to barely be growing at all:

![Search algorithm comparison graph](../Searches.jpg)

The catch, of course, is that Binary Search requires your data to be sorted first. But if you're going to search the same data many times, sorting it once and then using Binary Search is a massive win.

---

*Materials on this page adapted from the [Chemeketa Community College CS160 Reader](https://computerscience.chemeketa.edu/cs160Reader/Algorithms/SearchBigO.html).*
