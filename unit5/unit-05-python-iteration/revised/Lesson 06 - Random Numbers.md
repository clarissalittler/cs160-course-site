# Lesson 6 --- Random Numbers

> **What you'll be able to do after this lesson:**
>
> - Use the `random` module to generate random numbers.

## Textbook Reading

Read through [Section 5.4, The random module](https://runestone.academy/runestone/books/published/thinkcspy/PythonModules/Therandommodule.html) from the Runestone Academy textbook. This section covers random numbers and how Python's `random` module helps with generating them.

## Python Modules

Python comes with a huge collection of pre-built tools called **modules** --- bundles of functions you can import and use in your own programs. They're all listed in the [Python Standard Library](https://docs.python.org/3/library/index.html), which is kind of like a catalog of superpowers you can bolt onto your code.

Here are some frequently used ones:

| Module    | Description                                           |
|-----------|-------------------------------------------------------|
| `math`    | Functions for mathematical operations                 |
| `random`  | Functions for generating random numbers               |
| `decimal` | Functions for working with decimal numbers            |
| `csv`     | Functions for working with comma-separated value files|
| `pickle`  | Functions for persistent data storage                 |
| `tkinter` | Functions for building GUI applications               |

The name `pickle` might seem weird for a programming module, but it's actually a reference to *pickling* --- the process of preserving something so it lasts. In Python, "pickling" means saving data so you can load it back later. Cute, right?

## The `random` Module

The `random` module provides methods for generating random numbers. Here's the basic idea:

- Add `import random` at the top of your program
- Use `random.randint(low, high)` to generate a random integer between `low` and `high` (inclusive --- both endpoints are included)

![Generating random numbers: add 'import random' at the top of the program. The statement number = random.randint(1,100) will generate a random number 1-100 and store in number. print(random.randint(1,10)) will generate a random number 1-10 and it will be printed.](images/random_numbers.png)
*Figure 5.4. Generating random numbers*

The program below demonstrates how to import the `random` module and generate a random number between 1 and 10. Try changing the arguments to generate a number between 1 and 100, and run the program several times --- you should get different results each time! *(Copy from below, or download [random_demo.py](https://drive.google.com/file/d/1w2xPjyIwxWi138v2GTOtuIsvECEsmu7w/view?usp=drive_link) and run it in your IDE of choice. Important: do **not** name your file `random.py` --- that will conflict with Python's built-in `random` module and cause errors!)*

```python
# This program displays a random number
# in the range of 1 through 10.
import random

def main():
    number = 0
    # Get a random number 1-10 and store in 'number'
    number = random.randint(1, 10)
    # Display the number.
    print('The number is', number)

# Call the main function.
main()
```

Fun fact: computers can't actually generate truly random numbers --- these are *pseudorandom* numbers, produced by mathematical formulas that are really good at *looking* random. For a guessing game that's totally fine, but if you were doing cryptography, you'd need something fancier.

## Using a Loop to Print Many Random Numbers

Now that you've got a program that generates a random number, let's practice your `for` loop skills. Put a loop around the lines containing `random.randint()` and `print()` (and their comments --- lines 7-10 in the code above).

Hint: you'll probably want to use the `range()` function with the `for` statement.

Make the `for` loop run somewhere between 5 and 20 times --- you pick! Then count how many numbers were printed. If it's not the right number, you might need to adjust the parameters to `range()`.

<details>
<summary>Solution</summary>

```python
for index in range(5):
    # Get a random number 1-10 and store in 'number'
    number = random.randint(1, 10)
    # Display the number.
    print('The number is', number)
```

</details>

## Game Programs

Random numbers are a staple of game development --- think dice rolls, card shuffles, enemy spawns, loot drops, &c. Let's look at a number-guessing game that brings together several things we've learned: `random`, `while` loops, input validation, and counters.

Take a look at the code below. *(Copy or download [games.py](https://drive.google.com/file/d/1gHKT_tLvPcmty-1Y2a86g8wOQ18CCfEq/view?usp=drive_link) and run it in your IDE of choice.)*

```python
import random  # you must add this at the top of your program to use the random functions

def main():
    answer = random.randint(1, 10)
    guess = 0
    tooHigh = 0
    tooLow = 0
    valid = False

    print("Guess a number between 1 and 10!")
    while guess != answer:
        valid = False  # reset the flag before prompting for guess
        while not valid:
            try:
                guess = int(input("\nEnter guess: "))
                if guess < 1 or guess > 10:
                    print("Guess must be 1-10")
                else:
                    valid = True
            except:
                print("Not an integer!")

        if guess == answer:
            print("Correct!!")
        elif guess > answer:
            print("Too high!")
            tooHigh += 1
        else:
            print("Too low!")
            tooLow += 1

    print(tooHigh, "of your guesses were too high.")
    print(tooLow, "of your guesses were too low.")
    print("\nThank you for playing!")

main()
```

There's a lot going on here, so let's break it down:

- The program generates a random answer between 1 and 10 using `random.randint()`.
- It uses a **nested loop** --- that's a loop inside a loop. The inner `while not valid` loop handles input validation (making sure the guess is actually an integer between 1 and 10). The outer `while guess != answer` loop keeps the game going until you get it right.
- The `try/except` block catches the error that would happen if someone types "abc" instead of a number. We haven't formally covered `try/except` yet, but the idea is straightforward: *try* to do something, and if it blows up, run the `except` code instead of crashing.
- It keeps track of how many guesses were too high and too low, then reports them at the end.

This is a great example of how all these pieces --- loops, conditionals, random numbers, validation --- come together to make something that actually feels like a real program.
