# Lesson 2 --- Array Structure

![Unit 6 banner](img/banner.jpg)

> **After this lesson, you'll be able to:**
>
> - Access the elements stored in an array and a Python list.

## Runestone Academy --- Textbook Resource

Read through [Sections 10.2, 10.3, and 10.4](https://runestone.academy/runestone/books/published/thinkcspy/Lists/ListValues.html) from [Chapter 10, Lists](https://runestone.academy/runestone/books/published/thinkcspy/Lists/toctree.html) in the textbook. These sections cover **creating lists and accessing values** in a list. Try some programs in the workspace they provide.

## Array and list vocabulary

Let's look at how arrays and lists are actually stored in memory --- and learn some vocabulary that'll come up again and again.

![array vocabulary: name of array, index is the cell number, cell is the memory location, element is the value stored in the cell](images/arrays1.png)
*Figure 6.1. List vocabulary*

When we create a regular variable to hold an integer:

```python
num = 22
```

...memory gets allocated to hold the value 22, and we refer to that location by its name --- `num`. Simple enough.

Arrays work similarly, except when we access a value in an array, we have to tell Python *where* in the array to look. We use the array name plus square brackets `[]` with the **index** (position) of the value we want.

So `nums[1]` refers to the value `-3` located in the **second** position of the array.

Wait --- second? Yes. And here's the thing that trips everybody up at first:

Array indexes always start at **0**. The first value sits at position 0, the second at position 1, &c. This is one of those things in programming that's genuinely annoying until you get used to it. Almost every programmer has been bitten by this at some point --- you're in good company.

> **Bug Alert:** Because indexes start with 0, the last index will ALWAYS be 1 less than the size of the array. An array of size 5 has indexes 0, 1, 2, 3, and 4. For an array or list of size *N*, the last index is at position *N - 1*!!

## Stepping through a program

Step through the program below and *predict* how the variables will change BEFORE you hit *next*. Pay close attention to how we access the variable `n` versus the values in the list `nums` --- they're both locations in memory, just with different naming formats.

[Python Tutor: Array access walkthrough](https://pythontutor.com/iframe-embed.html#code=def%20main%28%29%3A%0A%20%20%20%20nums%20%3D%20%5B1,%20-3,%205,%202,%202%5D%0A%20%20%20%20n%20%3D%2010%0A%20%20%20%20%0A%20%20%20%20n%20%3D%20n%20%2B%20nums%5B0%5D%0A%20%20%20%20nums%5B1%5D%20%3D%20nums%5B2%5D%0A%20%20%20%20nums%5B3%5D%20%3D%20nums%5B4%5D%20%2B%20n%0A%20%20%20%20nums%5B4%5D%20%3D%20n%20*%202%0A%20%20%20%20%0Amain%28%29&codeDivHeight=500&codeDivWidth=550&cumulative=false&curInstr=10&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Check for understanding!

[LMS Activity: Unit 6 Lesson 2 Quiz]
