# Lesson 4 --- `if-else` Statement

> **After this lesson, you'll be able to:**
>
> - Use the `if-else` statement to ask questions and alter the flow of execution for both true *and* false answers.

## Textbook Resource

- Read through [Sections 7.4 and 7.5](https://runestone.academy/runestone/books/published/thinkcspy/Selection/ConditionalExecutionBinarySelection.html) from [Chapter 7, Selection](https://runestone.academy/runestone/books/published/thinkcspy/Selection/toctree.html) in the Runestone Academy textbook. These sections cover *selection statements* (a.k.a. *conditional statements*). Try the programs in the workspace provided!

## The `if-else` statement

Last lesson, we learned the `if` statement --- it lets us run some code *only* when a condition is true. But what if we also want something specific to happen when the condition is *false*? That's where `if-else` comes in.

An `if-else` statement gives us two branches: one for when the condition is true, and one for when it's false. **Exactly one** of those blocks will run. Always. No matter what. It's like a fork in the road --- you *have* to go one way or the other, but you can't go both ways and you can't just stand there.

## Syntax

Here's the general form:

![if-else statement syntax --- if condition: followed by the statements to execute if true, then else: followed by the statements to execute if false. Exactly one block will execute.](images/if_else.png)

Notice a few things:

- The `else` keyword lines up with the `if` --- same indentation level.
- The `else` also ends with a colon (`:`).
- Each block of statements is indented under its respective keyword.
- There's **no condition** after `else`. It doesn't need one --- it just catches everything that *wasn't* true. Think of `else` as the "otherwise" branch.

## Step through it

Here's a classic example: checking whether a student passed a class. Try stepping through this code with grades greater than 70, less than 70, and exactly 70:

[Python Tutor: if-else statement with grade example](https://pythontutor.com/iframe-embed.html#code=grade%20%3D%20float%28input%28%27Enter%20final%20grade%20percentage%3A%20%27%29%29%0A%20%20%0Aif%20grade%20%3E%3D%2070%3A%0A%20%20%20%20print%28%27%5CnYou%20passed!%20Please%20register%20for%20CS161.%27%29%0Aelse%3A%0A%20%20%20%20print%28%27%5CnYou%20did%20not%20pass.%20No%20worries,%20register%20for%20CS160%20again.%27%29%0A%20%20%20%20%20%20%20%0Aprint%28%27%5CnRegister%20for%20next%20term%20now.%27%29&codeDivHeight=300&codeDivWidth=600&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%2270%22%5D&textReferences=false)

Here's the important thing to notice: the last line --- `print('\nRegister for next term now.')` --- runs **no matter what**. It's not indented under `if` or `else`, so it's outside the selection structure entirely. Whether you passed or didn't, you still need to register. Both paths converge back to that final statement.

This is the pattern we saw back in Lesson 1 with the flowchart. The two branches split apart, do their own thing, and then come back together to continue the program. The `if-else` is Python's way of making that fork-in-the-road happen.

And pay attention to that boundary case again: what happens when the grade is *exactly* 70? The condition is `grade >= 70`, so 70 counts as passing. If we'd written `grade > 70` instead, 70 would *not* pass. That one little `=` sign makes a real difference. Details matter!

## Lesson video

[Video: if-else Statements](https://www.youtube.com/watch?v=HW3gDKBuGoU)
