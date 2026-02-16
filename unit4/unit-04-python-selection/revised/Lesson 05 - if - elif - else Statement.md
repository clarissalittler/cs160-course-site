# Lesson 5 --- if-elif-else Statement

> **By the end of this lesson, you'll be able to:**
>
> - Use the `if-elif-else` statement to write chained conditional structures

## Textbook Reading

- Read through [Section 7.7 --- Chained Conditionals](https://runestone.academy/runestone/books/published/thinkcspy/Selection/Chainedconditionals.html) from [Chapter 7, Selection](https://runestone.academy/runestone/books/published/thinkcspy/Selection/toctree.html) in the Runestone Academy textbook. This section covers *chained conditional statements*. Try some of the programs in the workspace they provide --- it's a great way to build intuition.

## The `if-elif-else` Statement

So far we've handled situations with one or two possible paths. But what about when you've got *several* conditions to check? That's where `if-elif-else` comes in.

Here's how it works: when the statement executes, Python tests `condition_1` first. If it's true, the block of statements right below it runs, and then Python *skips everything else* in the structure. If `condition_1` is false, Python jumps down to the first `elif` and tests `condition_2`. If *that's* true, its block runs and the rest is skipped. This keeps going --- testing each `elif` in order --- until either a condition comes back true, or we run out of `elif` clauses. If nothing matched, the `else` block at the bottom catches everything that fell through.

The key thing to remember: once Python finds the *first* true condition, it runs that block and bails out. No more testing happens. It's like a series of trapdoors --- you fall through the first one that opens, and you're done.

![if-elif-else statement syntax: if condition : followed by the statements to execute if the condition is true. Followed by one or more elif condition: and the statements to execute if the conditions are true. Followed by an optional else: as a 'catch all' if none of the conditions above are true. The statements are indented under the if, elif, else. The first condition to evaluate to True will execute. The remaining will not be tested.](images/if_elif_else.png)

Step through the code below and try different grades to test each condition --- don't forget to test the *fenceposts* (the boundary values like 90, 80, 70, &c.). Refresh your browser after each run to start over:

[Interactive: Python Tutor --- Grade checker with if-elif-else](https://pythontutor.com/iframe-embed.html#code=grade%20%3D%20float%28input%28%27Enter%20final%20grade%20percentage%3A%20%27%29%29%0A%20%0Aif%20grade%20%3E%3D%2090%3A%0A%20%20%20%20print%28%27%5CnYour%20grade%20is%20%5C%27A%5C%27.%20Please%20register%20for%20CIS233Y.%27%29%0Aelif%20grade%20%3E%3D%2080%3A%0A%20%20%20%20print%28%27%5CnYour%20grade%20is%20%5C%27B%5C%27.%20Please%20register%20for%20CIS233Y.%27%29%0Aelif%20grade%20%3E%3D%2070%3A%0A%20%20%20%20print%28%27%5CnYour%20grade%20is%20%5C%27C%5C%27.%20Please%20register%20for%20CIS233Y.%27%29%0Aelif%20grade%20%3E%3D%2060%3A%0A%20%20%20%20print%28%27%5CnYour%20grade%20is%20%5C%27D%5C%27.%20You%20did%20not%20pass.%20Please%20register%20for%20CS160%20again.%27%29%0Aelse%3A%0A%20%20%20%20print%28%27%5CnYour%20grade%20is%20%5C%27F%5C%27.%20You%20did%20not%20pass.%20Please%20register%20for%20CS160%20again.%27%29%0A%20%20%20%20%0Aprint%28%27%5CnTime%20to%20register%20for%20next%20term%20now.%27%29&codeDivHeight=400&codeDivWidth=600&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Input Validation

Here's something to think about: what if the user enters a percentage of 104? Or -99? Those aren't real grades, but our program would happily accept them and give a result. That's... not great.

We should plan for user input errors and *validate* that we've got good input before doing anything with it. In the code below, try moving the first `if` condition (the one that tests if the grade is >= 90) down to the first `elif`, and replacing it with a validation check:

```python
if grade < 0 or grade > 100:
     print("Invalid. Grades must be between 0 - 100.")
```

Run the program and test with both valid *and* invalid grades! Copy the code below or download [grades.py](https://drive.google.com/file/d/1bF16U8ZZ-Z5AM07ZZyaesAYOsFQzBn3T/view?usp=drive_link) and run it in your IDE of choice:

```python
def main():
    grade = float(input('Enter final grade percentage: '))

    if grade >= 90:
        print('\nYour grade is \'A\'. Please register for CS161.')
    elif grade >= 80:
        print('\nYour grade is \'B\'. Please register for CS161.')
    elif grade >= 70:
        print('\nYour grade is \'C\'. Please register for CS161.')
    elif grade >= 60:
        print('\nYour grade is \'D\'. You did not pass. Please register for CS160 again.')
    else:
        print('\nYour grade is \'F\'. You did not pass. Please register for CS160 again.')

    print('\nTime to register for next term now.')

main()
```

## Lesson Video

[Video: if-elif-else Statement](https://www.youtube.com/watch?v=u8O2HfVrIrA)

## Partner Activity

> **Partner Activity**
>
> With a partner, you'll design and code a program of your choice!
>
> - Start with a sample run and pseudocode.
> - Your program must have at least one input and one output.
> - Your program must use at least one `if`, `if-else`, or `if-elif-else` structure.
> - Keep it simple!
>
> When you're finished, post your code (with partner names) to the [LMS Activity: Unit 4 Lesson 5 --- Practice Program discussion topic].
>
> After you've posted, open other students' programs and evaluate them. Leave comments with suggestions for improvement and any kudos!
