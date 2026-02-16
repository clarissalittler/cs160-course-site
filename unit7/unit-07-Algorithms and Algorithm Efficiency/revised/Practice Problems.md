# Practice Problems

These are pen-and-paper problems --- no coding required. The goal is to build your intuition for how these algorithms actually *work* by tracing through them step by step. Try each problem on your own before peeking at the solution. Grab some scratch paper, write out your steps, and then check yourself.

> **Important!** Understanding algorithms takes time and repetition. Like anything new you're trying to learn --- golf, cooking, karate, piano, &c. --- you can't rush it. If a trace doesn't make sense the first time, slow down, go back to the lesson, and try again. The lightbulb *will* come on.

## Question #1 --- Linear Search Trace

Consider the following list of 8 numbers:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|--------|---|---|---|---|---|---|---|---|
| Value: | 14 | 3 | 27 | 8 | 42 | 19 | 6 | 31 |

**(a)** Trace through a linear search for the value **19**. At each step, write down which index you're checking and what comparison you're making. How many comparisons does it take to find the value?

**(b)** Now trace through a linear search for the value **50**. How many comparisons does it take, and what do you conclude?

<details>
<summary>Solution</summary>

**(a)** Searching for **19**:

We start at index 0 and check each element one by one:

| Step | Index Checked | Value at Index | Match? |
|------|--------------|----------------|--------|
| 1 | 0 | 14 | No |
| 2 | 1 | 3 | No |
| 3 | 2 | 27 | No |
| 4 | 3 | 8 | No |
| 5 | 4 | 42 | No |
| 6 | 5 | 19 | Yes --- found it! |

**6 comparisons** to find the value 19 at index 5.

**(b)** Searching for **50**:

| Step | Index Checked | Value at Index | Match? |
|------|--------------|----------------|--------|
| 1 | 0 | 14 | No |
| 2 | 1 | 3 | No |
| 3 | 2 | 27 | No |
| 4 | 3 | 8 | No |
| 5 | 4 | 42 | No |
| 6 | 5 | 19 | No |
| 7 | 6 | 6 | No |
| 8 | 7 | 31 | No |

**8 comparisons** --- we had to check *every single element* in the list before we could conclude that 50 isn't there. This is the worst case for linear search: the value doesn't exist, so we can't stop early. We're forced to examine all *n* items.

</details>

## Question #2 --- Binary Search Trace

Now consider this **sorted** list of 8 numbers:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
|--------|---|---|---|---|---|---|---|---|
| Value: | 3 | 6 | 8 | 14 | 19 | 27 | 31 | 42 |

Trace through a binary search for the value **6**. At each step, show the low index, the high index, the midpoint calculation, and the comparison. How many comparisons does it take? How does that compare to linear search on the same list?

<details>
<summary>Solution</summary>

We start with low = 0 and high = 7. At each step, we compute the midpoint as (low + high) / 2 (using integer division).

**Step 1:**
- low = 0, high = 7
- mid = (0 + 7) / 2 = **3**
- Value at index 3 is **14**
- 6 < 14, so our target is in the *left* half. Set high = mid - 1 = **2**.

**Step 2:**
- low = 0, high = 2
- mid = (0 + 2) / 2 = **1**
- Value at index 1 is **6**
- 6 == 6 --- **found it!**

**2 comparisons** to find the value 6.

If we'd used linear search on this same sorted list, we would have checked index 0 (value 3 --- no match), then index 1 (value 6 --- match). That would also be 2 comparisons in this particular case. But that's a bit of a coincidence --- the target happened to be near the beginning of the list. If we were searching for 42 instead, linear search would need 8 comparisons (checking every element), while binary search would still only need about 3. The real advantage of binary search shows up when targets are deeper in the list or when the list is much larger.

</details>

## Question #3 --- Selection Sort Trace

Consider the following list of 6 numbers:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| Value: | 29 | 10 | 14 | 37 | 3 | 25 |

Trace through the **first two passes** of selection sort. For each pass, identify which portion of the list is "unsorted," find the minimum value in that portion, and show the swap. Write out the state of the list after each pass.

<details>
<summary>Solution</summary>

Remember how selection sort works: on each pass, it scans the unsorted portion of the list, finds the smallest value, and swaps it into the next position in the sorted portion.

**Pass 1** --- find the minimum of the *entire* list (indices 0 through 5):

- Start scanning: index 0 has 29. That's our current minimum.
- Index 1 has 10. 10 < 29, so 10 is the new minimum.
- Index 2 has 14. 14 > 10, no change.
- Index 3 has 37. 37 > 10, no change.
- Index 4 has 3. 3 < 10, so 3 is the new minimum.
- Index 5 has 25. 25 > 3, no change.
- The minimum is **3** at index 4. Swap it with the value at index 0 (which is 29).

**5 comparisons**, 1 swap.

List after Pass 1:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| Value: | **3** | 10 | 14 | 37 | 29 | 25 |

Index 0 is now sorted. The unsorted portion is indices 1 through 5.

**Pass 2** --- find the minimum of indices 1 through 5:

- Start scanning: index 1 has 10. That's our current minimum.
- Index 2 has 14. 14 > 10, no change.
- Index 3 has 37. 37 > 10, no change.
- Index 4 has 29. 29 > 10, no change.
- Index 5 has 25. 25 > 10, no change.
- The minimum is **10** at index 1. It's already in the correct position --- no swap needed!

**4 comparisons**, 0 swaps.

List after Pass 2:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| Value: | **3** | **10** | 14 | 37 | 29 | 25 |

Indices 0 and 1 are now sorted. Notice the pattern: each pass requires one fewer comparison than the last (5, then 4, then 3, &c.), because the sorted portion keeps growing and we don't need to look at it anymore.

</details>

## Question #4 --- Insertion Sort Trace

Using the **same original list** from Question #3:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| Value: | 29 | 10 | 14 | 37 | 3 | 25 |

Trace through the **first three passes** of insertion sort. For each pass, identify the value being inserted, show how it compares against the sorted portion, and show any shifts that occur. Write out the state of the list after each pass.

<details>
<summary>Solution</summary>

Remember how insertion sort works: we treat the first element as already "sorted." Then for each subsequent element, we pick it up, compare it against the sorted portion from right to left, shift bigger elements over to make room, and insert it into the correct spot. Think of it like sliding a card into the right place in your hand.

**Pass 1** --- insert the value at index 1 (which is **10**) into the sorted portion (just index 0):

- Pick up 10. Compare with 29 at index 0.
- 29 > 10, so shift 29 one position to the right (from index 0 to index 1).
- No more elements to compare. Insert 10 into index 0.

List after Pass 1:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| Value: | **10** | **29** | 14 | 37 | 3 | 25 |

**Pass 2** --- insert the value at index 2 (which is **14**) into the sorted portion (indices 0-1):

- Pick up 14. Compare with 29 at index 1.
- 29 > 14, so shift 29 to the right (from index 1 to index 2).
- Compare 14 with 10 at index 0.
- 10 < 14, so we stop. Insert 14 into index 1.

List after Pass 2:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| Value: | **10** | **14** | **29** | 37 | 3 | 25 |

**Pass 3** --- insert the value at index 3 (which is **37**) into the sorted portion (indices 0-2):

- Pick up 37. Compare with 29 at index 2.
- 29 < 37, so we stop immediately. 37 is already in the right spot --- no shifts needed.

List after Pass 3:

| Index: | 0 | 1 | 2 | 3 | 4 | 5 |
|--------|---|---|---|---|---|---|
| Value: | **10** | **14** | **29** | **37** | 3 | 25 |

Notice something interesting: when the next value is already bigger than everything in the sorted portion, insertion sort gets lucky and does almost no work on that pass. This is one advantage insertion sort has over selection sort --- it can sometimes finish a pass very quickly. Selection sort always scans the *entire* unsorted portion regardless.

</details>

## Question #5 --- Big-O Classification

For each of the following algorithm descriptions, identify whether it's **O(1)**, **O(log n)**, **O(n)**, or **O(n^2)**. Explain your reasoning.

**(a)** An algorithm that checks every element in a list once to find the largest value.

**(b)** An algorithm that, given a sorted list, repeatedly cuts the remaining search space in half until it finds the target.

**(c)** An algorithm that uses a nested loop --- for every element in the list, it compares that element to every other element in the list.

**(d)** An algorithm that looks up a student's grade using their seat number as a direct index into an array (e.g., `grades[seat_number]`).

**(e)** An algorithm that scans through a list of *n* items, and for each item, scans through the rest of the list. On the first pass it checks *n* - 1 items, on the second pass it checks *n* - 2, and so on.

<details>
<summary>Solution</summary>

**(a)** **O(n) --- Linear.** Finding the largest value requires looking at every element exactly once. If the list has *n* items, you do *n* comparisons. Double the list size, double the work. That's the definition of linear growth.

**(b)** **O(log n) --- Logarithmic.** This is binary search. Each comparison eliminates half the remaining data. If you have 1,000 items, you need about 10 comparisons. If you have 1,000,000 items, you need about 20. The work grows with the *logarithm* of the input size, not the input size itself. That's why it's so efficient.

**(c)** **O(n^2) --- Quadratic.** A nested loop where both the outer and inner loops run roughly *n* times means about *n* * *n* = *n*^2 total operations. If the list has 10 items, that's around 100 operations. If the list has 100 items, that's around 10,000. The work grows with the *square* of the input size.

**(d)** **O(1) --- Constant.** Looking up a value by index is a single operation --- you go directly to that position in memory. It doesn't matter if the array has 10 elements or 10 million. The lookup takes the same amount of work either way.

**(e)** **O(n^2) --- Quadratic.** This is the pattern we see in both selection sort and insertion sort (worst case). The total work is (*n* - 1) + (*n* - 2) + ... + 1, which simplifies to (*n* * (*n* - 1)) / 2. The largest term in that formula is *n*^2, so it's O(n^2). Remember --- Big-O doesn't care about constants or smaller terms. It only cares about the shape of the growth curve, and that shape is quadratic.

</details>

## Question #6 --- Scaling It Up: Linear Search vs. Binary Search

A company has a database of **1,000,000** customer records, sorted by customer ID. They need to search for a specific customer.

**(a)** In the **worst case**, how many comparisons would **linear search** need?

**(b)** In the **worst case**, how many comparisons would **binary search** need? *(Hint: calculate log2(1,000,000). You can figure this out by asking "how many times can I divide 1,000,000 in half before I get to 1?")*

**(c)** Now suppose the database doubles in size to **2,000,000** records. For each algorithm, how does the worst-case number of comparisons change? What does this tell you about how each algorithm scales?

<details>
<summary>Solution</summary>

**(a)** Linear search, worst case: **1,000,000 comparisons.**

In the worst case, the customer we're looking for is the very last record in the list (or isn't in the list at all). Linear search checks every single record, one by one. So for *n* = 1,000,000, we need 1,000,000 comparisons.

**(b)** Binary search, worst case: **20 comparisons.**

Each comparison cuts the search space in half:

| Comparisons | Items Remaining |
|------------|----------------|
| 0 | 1,000,000 |
| 1 | 500,000 |
| 2 | 250,000 |
| 3 | 125,000 |
| 4 | 62,500 |
| 5 | 31,250 |
| ... | ... |
| 10 | ~977 |
| 15 | ~31 |
| 20 | ~1 |

More precisely, log2(1,000,000) = 19.93, which rounds up to **20**. That's it --- 20 comparisons to search through a million records. Compare that to a million comparisons for linear search. The difference is staggering.

**(c)** When the database doubles to 2,000,000 records:

- **Linear search** doubles its work: from 1,000,000 comparisons to **2,000,000 comparisons**. That's because linear search is O(n) --- if you double *n*, you double the work. The relationship between input size and work is proportional.

- **Binary search** adds just **one** more comparison: from 20 to **21 comparisons**. That's because binary search is O(log n). Doubling the input size means one extra "halving" step. log2(2,000,000) = 20.93, which rounds up to 21.

This is the key takeaway about algorithm efficiency. For small datasets, the difference between O(n) and O(log n) might not matter much. But as the data grows, the gap becomes enormous. A linear algorithm that was tolerable at 1,000 records becomes painfully slow at 1,000,000. A logarithmic algorithm barely notices the difference. That's why choosing the right algorithm --- and understanding Big-O --- matters so much in the real world.

</details>
