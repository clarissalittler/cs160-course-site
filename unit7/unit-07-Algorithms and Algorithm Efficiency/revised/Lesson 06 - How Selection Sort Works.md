# Lesson 06 --- How Selection Sort Works

> **What you'll be able to do after this lesson:**
>
> - Turn the selection sort algorithm into a working Python program.

## How Selection Sort Works

Now that we've seen the big picture, let's get into the mechanics. We're going to walk through the algorithm step by step, look at pseudocode, and then write real Python.

### Algorithm

At its core, selection sort is beautifully simple:

> 1. Set MIN to location 0
> 2. Search for the minimum element in the list
> 3. Swap it with the value at location MIN
> 4. Increment MIN to point to the next element
> 5. Repeat until the list is sorted

That's it. We're just sliding a boundary between "sorted" and "unsorted" one position to the right on every pass, each time pulling the smallest remaining value into its final home.

### Pseudocode

Here's a more detailed pseudocode version --- this is closer to what we'll actually code:

```
procedure selection sort
   list  : array of items
   n     : size of list

   for i = 1 to n - 1
      /* set current element as minimum */
      min = i

      /* check for a smaller element */
      for j = i+1 to n
         if list[j] < list[min] then
            min = j
         end if
      end for

      /* swap the minimum element with the current element */
      if min != i then
         swap list[min] and list[i]
      end if
   end for

end procedure
```

Notice the nested loops --- an outer loop that advances through each position, and an inner loop that scans the remaining unsorted elements looking for the smallest one. That nesting is the key structural pattern here.

### Animation

Watch the animation below to see the algorithm in action. Once you get the rhythm, try to predict the next step before it happens --- that's when you know you really understand it.

[Animation: Selection Sort (interactive)](https://yongdanielliang.github.io/animation/web/SelectionSortNew.html)

### Python Program

Here's selection sort in real Python code. Take a look at how the pseudocode maps onto actual syntax --- it's a pretty direct translation.

```python
def selectionSort(arr):
    myList = arr
    n = len(myList)
    tmp = 0 # For swapping
    print("Iteration", 0, ":", arr)

    # Loop through each subarray
    # Guess that the minimum is in the correct place
    # Swap the actual minimum when the guess was wrong
    for i in range(0, n - 1, 1):
        # set minimum to first element in the subarray
        min = i

        for j in range(i + 1, n, 1):
            # Determine if minimum is correct or not
            if myList[j] < myList[min]:
                # Update minimum to the correct index
                min = j
        # Determine if minimum needs to be swapped
        if min != i:
            print("Swap index", i, "and", min)
            tmp = myList[min]
            myList[min] = myList[i]
            myList[i] = tmp

        # remove comment for this print if you want to see it
        # in action
        print("Iteration", i + 1, ":", arr)


## Example
##
arr = [12, 10, 7, 6, 3]

selectionSort(arr)

print("Sorted Array is: ")
for i in range(len(arr)):
    print(arr[i], end="")
    if (i < len(arr)-1):
        print(", ", end="")
print("")
```

The three-line swap pattern (`tmp = ...`, then reassign, then reassign again) is classic. Python actually lets you do `a, b = b, a` as a shortcut, but the explicit version here makes it clearer what's happening under the hood --- and that's worth understanding.

You can watch a video walkthrough of this code using [Python Tutor](https://pythontutor.com/) to hand-trace each step:

[Video: Selection Sort CS160](https://www.youtube.com/watch?v=zcZYjCrv5Hg)

---

Sources:
[Tutorials Point Selection Sort Algorithm](https://www.tutorialspoint.com/data_structures_algorithms/selection_sort_algorithm.htm)
