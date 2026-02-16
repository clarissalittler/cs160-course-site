# Lesson 1 --- Selection Structures

> **After this lesson, you'll be able to:**
>
> - Explain how control structures are used to alter the flow of execution in programs.

## Textbook Resource

- Start with [Section 7.1, Boolean Values and Boolean Expressions](https://runestone.academy/runestone/books/published/thinkcspy/Selection/BooleanValuesandBooleanExpressions.html) from [Chapter 7, Selection](https://runestone.academy/runestone/books/published/thinkcspy/Selection/toctree.html) in the Runestone Academy textbook. This is critical for understanding how the selection structure works.
- Read through [Sections 7.4 to 7.6](https://runestone.academy/ns/books/published/thinkcspy/Selection/ConditionalExecutionBinarySelection.html) from [Chapter 7, Selection](https://runestone.academy/runestone/books/published/thinkcspy/Selection/toctree.html). Try some of the programs in the workspace they provide --- it's the best way to make things click.

## Sequential structure

A **control structure** is a logical design that controls the order in which a set of statements execute. So far, we've been using only the simplest kind: the **sequential structure**. It's exactly what it sounds like --- a set of statements that execute in the order they appear, top to bottom. No surprises, no detours.

![Sequential structure --- statements executed one after another](images/sequential.png)
*Figure 4.1. Sequential structure*

There are three basic sequential operations:

- **Computation**: a single numeric calculation
- **Input**: gets data values from outside the algorithm
- **Output**: sends data values to the outside world

That's it. Input, crunch numbers, output. We've been doing this the whole time.

## Selection structure

But here's the thing --- sometimes we want certain statements to execute *only* under certain conditions. "If the user is old enough, let them proceed. Otherwise, show an error." Programs like that need a different kind of control structure.

Enter the **selection structure**.

![Selection structure --- alters the flow of statement execution depending on a condition being true or false](images/selection.png)
*Figure 4.2. Selection structure*

The idea is straightforward:

- First, evaluate a true/false condition (this is called a **conditional expression**)
- If the condition is **true**, do the first set of operations and skip the second
- If the condition is **false**, skip the first set and do the second

After whichever branch runs, execution continues with whatever comes next --- the two paths converge back together, as you can see in Figure 4.2 where the arrows meet up again.

This is a *huge* deal. Up until now, our programs have been like trains on a single track. Selection structures give us a fork in the road. We're finally letting our programs *think* --- well, sort of. They're really just asking yes-or-no questions, but that turns out to be surprisingly powerful.
