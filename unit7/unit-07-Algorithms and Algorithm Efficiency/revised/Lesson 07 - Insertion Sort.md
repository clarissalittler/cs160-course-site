# Lesson 07 --- Insertion Sort

> **What you'll be able to do after this lesson:**
>
> - Understand how insertion sort works to organize an unsorted list.

## Insertion Sort

Selection sort gets the job done, but it's not the only game in town. **Insertion sort** is another straightforward sorting algorithm --- and if you've ever picked up a hand of cards and slid each new card into its proper place among the ones you're already holding, you've basically done insertion sort without knowing it.

Like selection sort, insertion sort divides the list into a sorted and an unsorted portion. But here's the key difference: instead of scanning for the smallest element and placing it, insertion sort grabs the next unsorted card and **shifts it to the left** until it's bigger than its neighbor --- "inserting" it into the correct spot within the already-sorted section.

It's a subtle but important distinction. Selection sort asks "where does the smallest thing go?" Insertion sort asks "where does *this* thing belong?"

Here's the human-friendly card version:

> ### Insertion Card Sort Algorithm
>
> 1. Get a hand of unsorted cards
> 2. Set a marker for the sorted section after the first card of the hand
> 3. Repeat steps 4 through 6 until the unsorted section is empty
> 4. Select the first unsorted card
> 5. Swap this card to the left until it arrives at the correct sorted position
> 6. Advance the marker to the right one card
> 7. Stop

## Watching It in Action

Watch the video below to see insertion sort at work. Pay attention to a couple of things:

- **Cards don't jump to their final position** --- they keep swapping left, one neighbor at a time, until they settle into the right spot. It's more of a shimmy than a teleport.
- **The sorted portion doesn't necessarily contain the smallest values.** It just contains values that are sorted *relative to each other*. That's a bit counterintuitive compared to selection sort, where the sorted section always has the globally smallest values. Weird, right?

[Video: 160 Reader InsertionSort](https://www.youtube.com/watch?v=zDPNARGL9kY)

*Animation used by permission of Virginia Tech*

---

Materials on this page adapted from:
[Chemeketa Community College CS160 Reader](https://computerscience.chemeketa.edu/cs160Reader/Algorithms/InsertionSort.html)
