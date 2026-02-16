# Lesson 2 --- Relational Operators

> **After this lesson, you'll be able to:**
>
> - Create Boolean expressions using relational operators.

## Textbook Resource

- Read through [Section 7.1](https://runestone.academy/runestone/books/published/thinkcspy/Selection/BooleanValuesandBooleanExpressions.html) from [Chapter 7, Selection](https://runestone.academy/runestone/books/published/thinkcspy/Selection/toctree.html) in the Runestone Academy textbook. This covers relational operators (also called comparison operators) and Boolean expressions. Try the programs in the workspace they provide!

## Relational operators

A **Boolean expression** is an expression that, when evaluated, produces a **Boolean value** --- either `True` or `False`. That's it. Two options. Yes or no. On or off.

The term "Boolean" is named after the English mathematician **George Boole**, who in the 1800s invented an entire system of mathematics built on the abstract concepts of true and false. At the time, people probably thought it was a neat but impractical curiosity. Turns out it became the foundation of every computer ever built. Not bad, George.

Typically, you form a Boolean expression using a **relational operator**. A relational operator checks whether a specific relationship exists between two values. For example, the "greater than" operator (`>`) checks whether the value on the left is greater than the value on the right. The "equal to" operator (`==`) checks whether two values are equal.

Here are all the relational operators available in Python:

| Operator | Meaning                  |
|----------|--------------------------|
| `>`      | Greater than             |
| `<`      | Less than                |
| `>=`     | Greater than or equal to |
| `<=`     | Less than or equal to    |
| `==`     | Equal to                 |
| `!=`     | Not equal to             |

A quick heads-up: notice that "equal to" is `==` (two equals signs), not `=` (one equals sign). That single `=` is the *assignment* operator --- it's how we store values in variables. The double `==` is how we *ask a question*: "are these two things the same?" Mixing them up is one of the most common beginner mistakes, and honestly, it trips up experienced programmers too. Don't worry, you'll get used to it.

## Trying it out

Boolean expressions ask a question, and the answer is always `True` or `False`. Run the program below to see different Boolean expressions in action. You can copy and paste the code, or download [boolean.py](https://drive.google.com/file/d/1amKKtm6A9XZs2ESGPU62NclJFMUW8RON/view?usp=drive_link) and run it in your IDE of choice:

```python
def main():
    x = 8
    y = 3
    z = 8

    print('x == y\t', x == y)
    print('x > y\t', x > y)
    print('x < y\t', x < y)
    print('x == z\t', x == z)
    print('y <= z\t', y <= z)
    print('x != z\t', x != z)

main()
```

Take a moment to predict what each line will print before you run it. Seriously --- that habit of predicting-then-checking is one of the best ways to build your intuition for how code works.

## Lesson video

[Video: CS Principles: Conditionals - Part 1 Boolean Expressions](https://www.youtube.com/watch?v=y3rCKJNOwpA)
