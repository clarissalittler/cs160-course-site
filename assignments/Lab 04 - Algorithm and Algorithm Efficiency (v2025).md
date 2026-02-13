# Lab 04 - Algorithm and Algorithm Efficiency

You will make a copy of this document for your work. Submit your work to the Lab 04 Assignment in D2L. Solutions will be posted the day after the lab is due and only for students who submit work. Check your answers - learning to self-assess is super important and will help you become a better computer scientist!

1. Consider the following lists of partially sorted numbers using Insertion Sort. The double bars represent the sort marker. **For each show the sorting process step by step until the next number is sorted, like in the supplemental video.**

   1. [**1 3 4 8 9 || 5 2**]
   2. [**1 2 4 7 || 6 10**]

   > *Your answer here*

   ***Hint: Check the insertion sort algorithm in L07 and L08.***

2. Consider the following lists of partially sorted numbers using Selection Sort. The double bars represent the sort marker. **For each show the sorting process step by step until the next number is sorted, like in the supplemental video.**

   1. [**1 3 4 6 7 || 9 8**]
   2. [**2 3 4 || 9 8 7 6 5**]

   > *Your answer here*

   ***Hint: Check the selection sort algorithm in L05 and L06.***

3. Suppose you have the following sorted list:

   [**2, 5, 8, 12, 16, 23, 38, 42, 55, 67, 77, 84, 91**]

   1. Show step by step how **binary search** would find the value **23**. For each step, write down the portion of the list still under consideration and which element you compare against.
   2. How many comparisons did it take?
   3. Now show step by step how **linear search** would find the value **23**. How many comparisons does it take?
   4. For a sorted list of 1,000,000 items, what is the maximum number of comparisons binary search would need? What about linear search?

   > *Your answer here*

   ***Hint: Check the binary search and linear search algorithms in L02 and L03.***

4. For each of the following, state whether the algorithm is **O(1)**, **O(log n)**, **O(n)**, or **O(n²)** and briefly explain why.

   1. Looking up a student's grade by their index number in a list (e.g. `grades[42]`)
   2. Searching for a name in an unsorted list of names
   3. Searching for a word in a sorted dictionary using the "open to the middle, pick a half" strategy
   4. Checking every pair of students in a class to see if any two have the same birthday

   > *Your answer here*

   ***Hint: Check the Big-O notation lesson (L12) and the search efficiencies lesson (L13).***
