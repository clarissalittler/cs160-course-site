# Lesson 08 --- How Insertion Sort Works

> **What you'll be able to do after this lesson:**
>
> - Turn the insertion sort algorithm into a working Python program.

## How Insertion Sort Works

We've seen the card-sorting intuition for insertion sort. Now let's formalize it --- algorithm, pseudocode, and then real Python.

### Algorithm

Here's the step-by-step logic:

> 1. If it's the first element, it's already sorted. Return.
> 2. Pick the next element.
> 3. Compare it with all elements in the sorted sub-list.
> 4. Shift all elements in the sorted sub-list that are greater than the value to be sorted.
> 5. Insert the value.
> 6. Repeat until the list is sorted.

The mental model here is that we're making room. We pick up a value, scoot everything bigger than it one slot to the right, and then drop our value into the gap we just created. It's like squeezing into a crowded row at the movies --- everyone shuffles over and you slide in.

### Pseudocode

Here's the more detailed pseudocode. Notice the `while` loop inside the `for` loop --- the outer loop picks the next card, and the inner loop figures out where it belongs by shifting elements over:

```
procedure insertionSort( A : array of items )
   int holePosition
   int valueToInsert

   for i = 1 to length(A) - 1 inclusive do:
      /* select value to be inserted */
      valueToInsert = A[i]
      holePosition = i

      /* locate hole position for the element to be inserted */

      while holePosition > 0 and A[holePosition-1] > valueToInsert do:
         A[holePosition] = A[holePosition-1]
         holePosition = holePosition -1
      end while

      /* insert the number at hole position */
      A[holePosition] = valueToInsert

   end for
end procedure
```

The variable name `holePosition` is great --- it really captures what's happening. We're creating a "hole" by shifting elements right, and the hole moves left until we find the right spot to drop our value into.

### Animation

Watch the animation below to see the algorithm in action. Once you get comfortable, try predicting the next step before it happens --- that's the sign you've really internalized it.

[Animation: Insertion Sort (interactive)](https://yongdanielliang.github.io/animation/web/InsertionSortNew.html)

### Python Program

You can watch this video of stepping through insertion sort using [Python Tutor](https://pythontutor.com/) to hand-trace the code. Seeing each variable change in real time is incredibly helpful for building intuition about what the algorithm is actually doing at each step.

[Video: Insertion Sort CS160](https://www.youtube.com/watch?v=9Mo90pTBvr8)

---

Sources:
[Tutorials Point Insertion Sort Algorithm](https://www.tutorialspoint.com/data_structures_algorithms/insertion_sort_algorithm.htm)
