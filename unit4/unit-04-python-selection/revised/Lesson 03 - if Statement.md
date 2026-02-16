# Lesson 3 --- `if` Statement

> **After this lesson, you'll be able to:**
>
> - Use the `if` statement to ask questions and alter the flow of execution in your programs.

## Textbook Resource

- Read through [Sections 7.4 and 7.5](https://runestone.academy/runestone/books/published/thinkcspy/Selection/ConditionalExecutionBinarySelection.html) from [Chapter 7, Selection](https://runestone.academy/runestone/books/published/thinkcspy/Selection/toctree.html) in the Runestone Academy textbook. These sections cover *selection statements* (sometimes called *conditional statements*). Try the programs in the workspace provided --- hands-on practice is everything here.

## The `if` statement

The `if` statement is how we create a selection structure in Python. It lets our program have more than one path of execution --- which is where things start getting interesting. The `if` statement causes one or more statements to execute **only when a Boolean expression is true**.

Here's a simple example. Imagine you're writing a program for a car's dashboard. You want to warn the driver when gas is running low:

```python
if tank < 2:
    print('Time to get gas!')
```

That message will *only* print if `tank` is less than 2. If the tank has plenty of gas, the program just skips right past and keeps going. No message, no fuss.

This is genuinely powerful. We're not just running every line anymore --- we're letting the program *decide* what to do based on the current situation.

## Syntax

Here's the general form of an `if` statement in Python:

![if statement syntax --- the keyword if, followed by a condition, followed by a colon (the "if clause"). The statements below, indented under the if clause, execute only if the condition is true.](images/if.png)

A couple of things to notice:

- The line with `if` ends with a **colon** (`:`). Don't forget it --- Python will yell at you if you do.
- The statements that should run when the condition is true are **indented** underneath. This indentation isn't just for looks --- it's how Python knows which statements belong to the `if`. In many other languages, you'd use curly braces `{}` for this, but Python chose indentation instead. Personally, I think it makes the code cleaner, but it does mean you have to be careful about your spacing.

## Step through it

Try stepping through the code below. Test with tank values less than 2, greater than 2, and exactly 2 (refresh your browser after each run to start over):

[Python Tutor: if statement with gas tank example](https://pythontutor.com/iframe-embed.html#code=tank%20%3D%20float%28input%28%27Enter%20gallons%20of%20gas%20in%20tank%3A%20%27%29%29%0Aif%20tank%20%3C%202%3A%0A%20%20%20%20print%28%27Time%20to%20get%20gas!%27%29%0A%20%0Aprint%28%27Keep%20driving...%27%29&codeDivHeight=300&codeDivWidth=500&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%223%22%5D&textReferences=false)

Pay attention to what happens when `tank` is *exactly* 2. Is 2 less than 2? Nope --- so the message doesn't print. That boundary case is the kind of thing that matters a lot in programming. We'll talk more about these "edge cases" as we go.

## Lesson video

[Video: if Statement](https://www.youtube.com/watch?v=DAjNx2_CLow)
