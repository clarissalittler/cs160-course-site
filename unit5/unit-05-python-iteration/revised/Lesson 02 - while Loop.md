# Lesson 2 --- while Loop

![Unit 5 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Use a `while` loop to repeat statements in a program 0 or more times.

---

## Textbook reading

Read through [Section 8.3, The while statement](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/ThewhileStatement.html) from [Chapter 8, Iteration](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/toctree.html) in the Runestone Academy textbook. This section covers `while` loops and conditions. They mention `for` loops in there too --- you can ignore those for now. We'll get to `for` loops in the next lesson.

## The `while` loop

[Video: Simple while Loop (Pseudocode)](https://www.youtube.com/watch?v=iYmUGU9BpIo)

[Video: Simple while Loop (Python)](https://www.youtube.com/watch?v=_l7r3w493bU)

The `while` loop is a **condition-controlled loop**. It keeps executing the statements inside it *while* some condition is true. The moment that condition becomes false, the loop stops and the program moves on.

A `while` loop has two parts:

- A **condition** to test (true or false)
- A **block of statements** to repeat while the condition is true

![while loop syntax: while condition: followed by statements to execute while condition is true. Statements must be indented.](images/while_loop_syntax.png)
*Figure 5.2. While loop syntax*

Some important things to keep in mind:

- In order for the loop to *stop*, something has to happen inside the loop that eventually makes the condition false. Otherwise you've got a loop that runs forever --- more on that in a second.
- One pass through the loop body is called an **iteration**.
- The `while` loop is a **pretest loop** --- it checks the condition *before* each iteration. If the condition is false right from the start, the body never executes at all. Zero times. It just skips right over it.

## Stepping through a `while` loop

Step through this program and watch what happens to the variable `a` at each iteration:

[Python Tutor: while loop stepping through values of a](https://pythontutor.com/iframe-embed.html#code=def%20main%28%29%3A%0A%20%20%20%20a%20%3D%201%0A%20%20%20%20%0A%20%20%20%20while%20a%20%3C%2010%3A%0A%20%20%20%20%20%20%20%20print%28a%29%0A%20%20%20%20%20%20%20%20a%20%3D%20a%20%2B%202%0A%20%20%20%20%20%20%20%20%0Amain%28%29&codeDivHeight=500&codeDivWidth=500&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

The `while` loop repeats the body as long as a logical expression is true. The body is whatever's indented under the `while` statement (4 or more spaces). A logical expression is just something that evaluates to `True` or `False` --- like `x > 3` or `name != "quit"`.

`while` loops are typically used when you **don't know ahead of time** how many times you need to loop. Think about playing a game --- you keep playing *while* there isn't a winner. Or musical chairs --- you walk around the chairs *while* the music is playing. You don't know when the music will stop, and that's exactly the kind of situation a `while` loop is built for.

> **Bug Alert:**
>
> If nothing inside the loop ever makes the condition false, the loop runs forever. (Well, not *really* forever --- your program will eventually crash.) This is called an **infinite loop**, and it's one of the most common bugs beginners encounter.
>
> Here's a classic example:
>
> ```python
> num = 1
> while num != 10:
>     print(num)
>     num = num + 2
> ```
>
> See the problem? `num` starts at 1 and goes 1, 3, 5, 7, 9, 11, 13... it *skips right over* 10 and never equals it. So the condition `num != 10` is *always* true, and the loop never stops. This is honestly kind of sneaky --- the code *looks* reasonable at first glance.

## A tricky example

Run the program below. *(Copy or download [while_true.py](https://drive.google.com/file/d/1KIZwN7vn8rmaY-Oa-RIQJXM94MmEppMK/view?usp=drive_link) and run in your IDE of choice.)*

Are there any problems with this program? What changes, if any, would you want to make?

```python
def main():
    num = 0

    while True:
        num = int(input("Enter an integer: "))
        if num == 0:
            print("0 is neither + or -.\n")
        elif num > 0:
            print(num, "is positive.\n")
        else:
            print(num, "is negative.\n")

    print("Goodbye!")

main()
```

<details>
<summary>Show Solution</summary>

The problem is that the program never tells the user how to stop entering integers! The loop condition is `while True:` --- and `True` is *always* `True`. There's no way out. The user is trapped in an endless cycle of integer classification. The `print("Goodbye!")` line will never execute. You'd need to add some kind of exit condition --- like "enter -999 to quit" --- and a `break` statement or a different loop condition to actually escape.

</details>

## Hand trace practice

Hand tracing is where you step through code on paper (or in your head), tracking variable values at each step. It's one of the best debugging techniques you can develop.

[Video: Hand Tracing Example](https://www.youtube.com/watch?v=68CQHpIIwRw)

## Discussion prompt

Write a program that asks the user to enter the amount they've budgeted for a month. Then, a loop should prompt the user to enter each of their expenses for the month and keep a running total. Think: what value should the user enter to signal they're done entering expenses? When the loop finishes, the program should display the amount the user is over or under budget.

Start with a sample run of what the output will look like (as comments). Next, write your program in pseudocode. Finally, write the Python code. Run and test!

> **Complete on your own!**
>
> Open [LMS Activity: Unit 5 Lesson 2 - Budget Program discussion] and:
>
> - Download your `.py` file and a PDF/TXT of your pseudocode. Submit these files to the discussion board.
> - You must post before you can see other student posts.
> - You must review and give feedback to 2 other students. A peer review should include:
>   - Suggestions for improvement.
>   - Kudos for clever code or enhancements.
>   - Remember to always comment using generosity and respect.
>
> You may also work with someone from your study group or post to this topic asking to work on the program with someone from class! Collaboration during programming practice is encouraged.
