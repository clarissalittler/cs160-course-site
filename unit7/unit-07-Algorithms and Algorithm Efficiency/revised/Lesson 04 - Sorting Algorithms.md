# Lesson 04 --- Sorting Algorithms

> **After this lesson, you'll be able to:**
>
> - Describe how sorting algorithms work and identify the two basic operations most sorting algorithms use.

## Introduction to Sorting

Sorting is one of the most common tasks computers handle. Think about your email inbox --- most email programs let you sort messages by date received, subject line, sender, priority, &c. Every time you reorder those messages, the computer is running a sorting algorithm behind the scenes.

Since computers can compare a huge number of items very quickly, they're naturally great at sorting. But *how* they sort --- that's the interesting part.

Over the next few lessons, we'll learn two different sorting algorithms: **Insertion Sort** and **Selection Sort**. These two will give us a foundation for comparing algorithms and figuring out which ones are actually better than others.

### The Card Analogy

We'll illustrate each algorithm by sorting a hand of playing cards.

![Card 1](images/card1.gif) ![Card 2](images/card2.gif) ![Card 3](images/card3.gif) ![Card 4](images/card4.gif) ![Card 5](images/card5.gif) ![Card 6](images/card6.gif) ![Card 7](images/card7.gif)

--- Fun fact: a group of playing cards is traditionally called a "hand," even when nobody's actually holding them. We'll use the term "hand" throughout these lessons to refer to a group of seven cards.

Then we'll show how the same algorithm applies to sorting a list of numbers stored in an array --- memory cells lined up in a row:

| **7** | **8** | **5** | **2** | **4** | **6** | **3** |
|-------|-------|-------|-------|-------|-------|-------|

Same problem, different representation.

## Operations in Sorting Algorithms

The sorting algorithms we'll learn share two fundamental operations. Every sorting algorithm is basically just these two moves, applied over and over in clever combinations.

### The Comparison Operation

This is how the algorithm decides which item should come first. If we're sorting numbers from smallest to largest, the comparison tells us that 3 comes before 7. If we're sorting letters alphabetically, it tells us 'a' comes before 'b'.

Simple idea, but here's the thing --- a sorting algorithm usually has to perform *many* comparisons to get everything in the right order. The number of comparisons is a big part of what makes one algorithm faster or slower than another, as we'll see later.

### The Swap Operation

This is how we actually move items around. By swapping smaller items with larger ones, we gradually get everything into the correct position.

But swapping on a computer is a little trickier than it sounds. You can't just move A into B's spot --- you'd overwrite B and lose it forever. Instead, you need a **temporary holding spot**. Here's how it works:

| **A** | **Temp** | **B** |
|-------|----------|-------|
| 34    |          | 56    |

1. Copy the contents of A into Temp. (Temp now holds 34.)
2. Copy the contents of B into A. (A now holds 56.)
3. Copy the contents of Temp into B. (B now holds 34.)

Three copies to swap two values. It feels like it should be simpler, right? But computers can only copy data from one location to another --- they can't just magically teleport values between memory cells. So we need that temporary variable as a middleman.

This three-step swap is so fundamental that it shows up everywhere in computer science. Once you see it, you'll never unsee it.

---

Now we've got our two building blocks: **compare** and **swap**. In the next lesson, we'll put them together and learn our first real sorting algorithm --- the Selection Sort.
