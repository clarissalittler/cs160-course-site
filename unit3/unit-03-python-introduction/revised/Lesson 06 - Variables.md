# Lesson 6 --- Variables

**After this lesson, you'll be able to:**

- Declare and use variables to hold information in your programs.
- Hand trace (also called code trace) the execution of your programs.

## Textbook Reading

- Read through [Sections 2.4 and 2.5](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/Variables.html) from [Chapter 2, Simple Python Data](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/toctree.html) in the Runestone Academy textbook. Try some programs in the workspace provided in Section 2.4.
- Read through [Section 2.10](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/Reassignment.html) about the assignment operator and how reassignment of variables works. These are short sections, but they'll really help you understand how the syntax works.

## Variables

Programs need to store data somewhere so they can work with it. That "somewhere" is the computer's memory, and *variables* are how we give names to specific pieces of data stored there. Think of a variable as a labeled box --- the label is the name, and whatever's inside is the value.

You create a variable using an **assignment statement**:

```python
age = 30
```

This creates a variable called `age` and puts the integer `30` into it. Simple enough.

Here's the important part: when you put a *new* value into a variable, the old value is gone forever. It doesn't get saved somewhere else --- it just vanishes. We'll see this in action shortly.

### Naming Rules

There are rules for what you can name a variable:

- Only `a-z`, `A-Z`, `0-9`, and the underscore `_` are allowed.
- Names **cannot start with a digit**. `score1` is fine; `1score` is not.
- Variables should start with a lowercase letter. If the name has more than one word, you've got two common styles:
  - `num_students` --- words separated by underscores (called *snake_case*)
  - `numStudents` --- each new word starts with a capital (called *camelCase*)

Both styles work. Python programmers tend to prefer snake_case, but you'll see both in the wild.

## Video Lesson

[Video: Variables](https://www.youtube.com/watch?v=xfX8WR051Lc)

## The Assignment Operator `=`

This trips up almost everyone who's new to programming: the `=` sign in code does **not** mean "equals" the way it does in algebra. It means "assign the value on the right to the variable on the left."

![In algebra, x = x + 3 is not true. In coding, the = is the 'assignment operator'. x = x + 3 is an instruction to add 3 to variable x and store the result back in x.](images/not_algebra.png)

In algebra, `x = x + 3` is nonsense --- no number equals itself plus three. But in Python, it's a perfectly reasonable instruction: "take the current value of `x`, add `3` to it, and store the result back in `x`." The variable receiving the value *must* be on the left side of the `=`.

Also, you can only use a variable if it already has a value assigned to it:

![age = 30 assigns the value 30 to age. name = 'sally' assigns the string literal 'sally' to name. age = dog is invalid because dog has not been defined yet.](images/assignment.png)

Remember: when you assign new data to a variable, whatever was previously stored there is lost forever. Before you run the code below, make a *prediction* of what will be displayed. Then step through the program to see how the variables get updated:

[Python Tutor: Variable reassignment demo](https://pythontutor.com/iframe-embed.html#code=def%20main%28%29%3A%0A%20%20%20%20num%20%3D%2020%0A%20%20%20%20print%28'1st%20assignment%20of%20num%3A',%20num%29%0A%20%20%20%20num%20%3D%2030%0A%20%20%20%20print%28'2nd%20assignment%20of%20num%3A',%20num%29%0A%20%20%20%20%0A%20%20%20%20age%20%3D%2029%0A%20%20%20%20name%20%3D%20'Sally'%0A%20%20%20%20age%20%3D%20num%0A%20%20%20%20%0A%20%20%20%20print%28'age%3A',%20age,%20'num%3A',%20num,%20'name%3A%20',%20name%29%0A%0Amain%28%29&codeDivHeight=400&codeDivWidth=600&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

What values were displayed for `num` and `age`? Are these the values you predicted?

## Hand Tracing

Hand tracing is one of the most valuable skills you'll develop in this course. It's a simulation of code execution where you step through instructions one at a time and track what happens to each variable on paper.

Here's how it works: write the names of your variables on a sheet of paper, then mentally execute each line of code and update the variable values as you go.

Watch this video for a hand tracing walkthrough of the program above:

[Video: Hand Tracing Example](https://www.youtube.com/watch?v=L2SLmy8yx24)

> **This is important.** Research shows that learning how to hand trace code is one of the biggest predictors of becoming a successful programmer. Hand tracing helps you learn both the *syntax* (the rules of the language) and the *semantics* (what the rules actually mean) at a much deeper level.
>
> Don't try to do this in your head --- that's cheating yourself. Take the time to trace your code line by line on actual paper. It really works.

## Assignment Operators

Often, we want to perform a calculation on a variable and store the result right back into the same variable:

```python
num = num * 2
```

This is so common that Python gives us shorthand --- **assignment operators** that combine the math and the assignment into one step:

```python
num *= 2
```

These two lines do exactly the same thing. The shorthand version is just tidier. Here's the full list:

| Operator | Example   | Meaning        |
|----------|-----------|----------------|
| `=`      | `x = y`   | Assign --- copy the value of `y` into `x` |
| `+=`     | `x += y`  | `x = x + y`   |
| `-=`     | `x -= y`  | `x = x - y`   |
| `*=`     | `x *= y`  | `x = x * y`   |
| `/=`     | `x /= y`  | `x = x / y`   |
| `//=`    | `x //= y` | `x = x // y`  |
| `%=`     | `x %= y`  | `x = x % y`   |

You don't have to memorize all of these right now. You'll pick them up naturally as we write more programs. The ones you'll use most often are `+=` and `-=`.
