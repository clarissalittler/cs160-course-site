# Lesson 05 --- Selection Sort

> **What you'll be able to do after this lesson:**
>
> - Understand how selection sort works and write code that performs it.

## Selection Sort

Selection sort works by splitting a list into two portions --- a **sorted** part and an **unsorted** part. At the start, everything lives in the unsorted part. Then, one item at a time, we find the smallest thing remaining in the unsorted section and move it to the end of the sorted section. Rinse, repeat, done.

If you've ever organized a hand of playing cards by scanning for the lowest card and pulling it to the front, you've already done selection sort. You just didn't know it had a name.

Here's that card-sorting idea written out as an algorithm:

> ### Selection Card Sort Algorithm
>
> 1. Get a hand of unsorted cards
> 2. Set a marker for the unsorted section at the front of the hand
> 3. Repeat steps 4 through 7 until one card remains in the unsorted section
> 4. Compare all unsorted cards
> 5. Select the smallest unsorted card
> 6. Swap this card with the first card in the unsorted section
> 7. Advance the marker to the right one card
> 8. Stop

## Watching It in Action

To see how the Selection Card Sort Algorithm actually plays out, watch the video below. As the sort progresses, the current step of the algorithm gets highlighted in the bottom-left panel of the animation.

A few things to look for: we use a black vertical bar to divide the sorted section from the unsorted section. On each pass through steps 4--7, a pair of hands tracks what's happening --- the left hand points to the smallest card found so far, and the right hand points to the card currently being considered.

[Video: 160 Reader SelectionSort](https://www.youtube.com/watch?v=TfOBNNNZPbM)

*Animation used by permission of Virginia Tech*

---

Materials on this page adapted from:
[Chemeketa CS 160 Reader](https://computerscience.chemeketa.edu/cs160Reader/Algorithms/SelectionSort.html)
