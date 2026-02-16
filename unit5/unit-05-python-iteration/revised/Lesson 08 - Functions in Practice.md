# Lesson 8 --- Functions in Practice

![Unit 5 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Build programs from multiple functions that call each other.
- Explain how variable scope works inside functions.
- Use default parameter values.
- Decide when to break code into a separate function.

---

## Quick review

In the last lesson, we learned that `def main():` --- the thing you've been typing since Unit 3 --- is a function definition. We learned how to write our own functions, pass in values using parameters, and send values back using `return`. Here's the short version:

- **`def function_name(parameters):`** defines a function.
- **Calling** a function (writing `function_name(arguments)`) actually runs it.
- **Parameters** receive values from the caller. **Return values** send values back.
- Functions that *return* a value produce a result. Functions that just *print* perform an action but don't give anything back.

Now let's put these ideas to work.

## Functions calling other functions

So far, we've been calling our functions from inside `main()`. But functions can call *other* functions too. In fact, that's how real programs are structured --- `main()` calls a few high-level functions, each of those calls a few more, and so on.

Let's look at an example. Say we're writing a program that gets a test score from the user, but we want to make sure the score is valid (between 0 and 100). We could write it all in one place, but let's decompose it into pieces:

```python
def main():
    score = get_score()
    grade = letter_grade(score)
    print("You entered: {}".format(score))
    print("Your grade: " + grade)

def get_score():
    score = int(input("Enter your test score (0-100): "))
    while not is_valid(score):
        print("Invalid! Score must be between 0 and 100.")
        score = int(input("Enter your test score (0-100): "))
    return score

def is_valid(score):
    return score >= 0 and score <= 100

def letter_grade(score):
    if score >= 90:
        return "A"
    elif score >= 80:
        return "B"
    elif score >= 70:
        return "C"
    elif score >= 60:
        return "D"
    else:
        return "F"

main()
```

Look at what's happening here:

- `main()` calls `get_score()` and `letter_grade()`.
- `get_score()` calls `is_valid()`.
- Each function does *one thing* and does it well.

Read through `main()` by itself. It's almost like reading a to-do list: get the score, figure out the letter grade, print the results. You don't need to know *how* any of those things work to understand the overall flow. That's the beauty of decomposition --- you can think about the big picture and the details separately.

The word for this kind of design is **top-down** --- you start with the big picture (`main`) and break it down into smaller and smaller pieces. We've actually been doing top-down design in our pseudocode exercises all along. Functions are how you translate that same thinking into actual code.

## Scope --- where variables live and die

Here's something that trips people up. Try to predict what this program will do:

```python
def main():
    name = "Alice"
    print_greeting()

def print_greeting():
    print("Hello, " + name)

main()
```

If you guessed it would print "Hello, Alice" --- nope. You'll get an error:

```
NameError: name 'name' is not defined
```

Wait, what? We *just* defined `name` two lines above! What's going on?

This is **scope**. A variable created inside a function only exists inside *that function*. The variable `name` was created in `main()`, so only `main()` can see it. When `print_greeting()` tries to use `name`, Python has no idea what you're talking about. As far as `print_greeting()` is concerned, `name` doesn't exist.

This is actually a *good* thing, even though it feels annoying right now. It means each function is its own little world. You can use the variable name `x` in five different functions and they won't interfere with each other. Imagine the chaos if every variable was visible everywhere --- you'd accidentally overwrite things constantly.

Here's a clearer example:

```python
def main():
    x = 10
    do_stuff()
    print("x in main:", x)

def do_stuff():
    x = 99
    print("x in do_stuff:", x)

main()
```

Output:

```
x in do_stuff: 99
x in main: 10
```

These are *two different variables* that happen to share the same name. The `x` in `do_stuff()` is completely separate from the `x` in `main()`. Changing one has no effect on the other. Each function has its own **local** variables.

So how *do* you get information from one function to another? You already know --- **parameters and return values**. That's the proper way to share data between functions:

```python
def main():
    name = "Alice"
    print_greeting(name)   # pass it as an argument

def print_greeting(person):
    print("Hello, " + person)

main()
```

This works perfectly. We're not sneaking data around behind the scenes --- we're passing it through the front door.

> **A note about global variables:** There *is* a way to make a variable visible everywhere in your program --- it's called a *global variable*. But global variables are almost universally considered a bad idea. They make programs harder to understand, harder to debug, and harder to modify. We won't be using them in this course. Just pass your data through parameters and return values, and you'll be in good shape.

## Default parameters

Sometimes you want a function to have a "standard" behavior but also allow the caller to customize it. Python makes this easy with **default parameter values**.

```python
def main():
    greet("Alice")
    greet("Bob", "Hey there")
    greet("Carol")

def greet(name, greeting="Hello"):
    print(greeting + ", " + name + "!")

main()
```

Output:

```
Hello, Alice!
Hey there, Bob!
Hello, Carol!
```

The `greeting="Hello"` in the function definition means: "If the caller doesn't provide a second argument, use `"Hello"` as the default." When we call `greet("Alice")`, there's no second argument, so `greeting` gets the default value `"Hello"`. When we call `greet("Bob", "Hey there")`, we *do* provide a second argument, so it overrides the default.

A couple of rules about default parameters:

- Parameters *with* defaults must come **after** parameters *without* defaults. So `def greet(name, greeting="Hello"):` is fine, but `def greet(greeting="Hello", name):` would be an error. Python needs to know which argument goes where, and it matches them left to right.
- You can have multiple defaults: `def greet(name, greeting="Hello", punctuation="!"):` is perfectly valid.

Default parameters are really convenient for functions where most of the time you want the same behavior, but *occasionally* you need something different.

## A real-ish program: tip calculator

Let's build something fun that brings together everything we've learned. We'll make a tip calculator that:

- Asks for the bill amount
- Asks how many people are splitting it
- Shows tip amounts at 15%, 18%, and 20%
- Shows what each person owes

Here it is, broken into functions:

```python
def main():
    bill = get_bill_amount()
    people = get_num_people()

    print()
    print("=" * 35)
    print("  TIP CALCULATOR")
    print("=" * 35)
    print("Bill amount: ${:.2f}".format(bill))
    print("Splitting between: {} people".format(people))
    print("-" * 35)

    show_tip_option(bill, people, 15)
    show_tip_option(bill, people, 18)
    show_tip_option(bill, people, 20)

    print("=" * 35)

def get_bill_amount():
    amount = float(input("Enter the bill amount: $"))
    while amount <= 0:
        print("Bill must be a positive number!")
        amount = float(input("Enter the bill amount: $"))
    return amount

def get_num_people():
    people = int(input("How many people are splitting the bill? "))
    while people <= 0:
        print("Must be at least 1 person!")
        people = int(input("How many people are splitting the bill? "))
    return people

def calculate_tip(bill, tip_percent):
    return bill * (tip_percent / 100)

def show_tip_option(bill, people, tip_percent):
    tip = calculate_tip(bill, tip_percent)
    total = bill + tip
    per_person = total / people
    print("  {}% tip: ${:.2f} (${:.2f} each)".format(
        tip_percent, tip, per_person))

main()
```

Let's walk through the design:

- **`main()`** handles the overall flow --- get input, display results. It reads like a story.
- **`get_bill_amount()`** handles getting and validating the bill amount. Notice the input validation loop --- just like we learned in Lesson 5!
- **`get_num_people()`** does the same for the number of people.
- **`calculate_tip()`** does *one tiny thing* --- it calculates the tip amount. It returns the value rather than printing it, which makes it flexible.
- **`show_tip_option()`** handles displaying one row of the output. It calls `calculate_tip()` internally. We call it three times from `main()` with different tip percentages --- DRY in action.

Here's a sample run:

```
Enter the bill amount: $75.50
How many people are splitting the bill? 3

===================================
  TIP CALCULATOR
===================================
Bill amount: $75.50
Splitting between: 3 people
-----------------------------------
  15% tip: $11.32 ($28.94 each)
  18% tip: $13.59 ($29.70 each)
  20% tip: $15.10 ($30.20 each)
===================================
```

Notice how each function is short and focused. If you wanted to add a 25% tip option, you'd add *one line* in `main()`. If you wanted to change how tips are calculated (say, to round up to the nearest dollar), you'd change *one function*. That's the payoff of good decomposition.

## When should you make something a function?

Now that you *can* write functions, you might be tempted to turn everything into one. Let's talk about when it actually makes sense.

**Make a function when:**

- **You're repeating code.** If you've copied and pasted a block of code, that's a strong signal. Pull it out into a function.
- **A chunk of code does "one thing."** If you can describe what a block of code does in a short phrase --- "validate the input," "calculate the tax," "print the receipt" --- it's probably a good candidate for a function.
- **You want to give a name to a concept.** Even if you only call it once, wrapping code in a well-named function can make your program easier to read. `total = calculate_total(subtotal, tax_rate)` is clearer than three lines of arithmetic.
- **Your `main()` function is getting long.** If `main()` is more than about 20--30 lines, consider breaking pieces out into their own functions.

**Don't overdo it, though.** A function that's just one line of code usually isn't worth the overhead. And a program where every single operation is its own function can be *harder* to read, not easier --- you'd spend all your time jumping between tiny functions trying to follow the logic. Use your judgment. There's no magic rule.

Personally, I think the best test is this: if you can read your `main()` function and *understand what the program does* without scrolling through all the details, you've decomposed well.

## Practice exercises

### Exercise 1: Temperature converter

Write a program that displays a conversion table from Fahrenheit to Celsius. Use a `for` loop to go from 0F to 100F in steps of 10. Use a function called `to_celsius(fahrenheit)` that takes a Fahrenheit temperature and *returns* the Celsius equivalent.

The formula is: `C = (F - 32) * 5 / 9`

Your output should look something like:

```
Fahrenheit    Celsius
----------    -------
     0         -17.8
    10         -12.2
    20          -6.7
    ...
   100          37.8
```

<details>
<summary>Solution</summary>

```python
def main():
    print("Fahrenheit    Celsius")
    print("----------    -------")

    for f in range(0, 101, 10):
        c = to_celsius(f)
        print("{:>10}     {:>6.1f}".format(f, c))

def to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9

main()
```

</details>

### Exercise 2: Quiz game

Write a quiz game with at least 3 questions. Use a function called `ask_question(question, correct_answer)` that:

- Prints the question
- Gets the user's answer
- Returns `True` if correct, `False` if not

Your `main()` function should call `ask_question()` for each question, keep score, and print the final result at the end.

<details>
<summary>Solution</summary>

```python
def main():
    score = 0

    if ask_question("What planet is closest to the sun? ", "mercury"):
        score += 1
    if ask_question("What is the capital of Oregon? ", "salem"):
        score += 1
    if ask_question("How many legs does a spider have? ", "8"):
        score += 1

    print()
    print("You got {} out of 3 correct!".format(score))

    if score == 3:
        print("Perfect score!")
    elif score >= 2:
        print("Nice job!")
    else:
        print("Better luck next time!")

def ask_question(question, correct_answer):
    answer = input(question)
    if answer.lower() == correct_answer.lower():
        print("Correct!")
        return True
    else:
        print("Sorry, the answer was: " + correct_answer)
        return False

main()
```

</details>

### Exercise 3: Number cruncher

Write a program that asks the user for a positive integer and then displays:

- Whether it's even or odd
- Its factorial (e.g., 5! = 120)

Use two functions: `is_even(number)` (returns `True` or `False`) and `factorial(number)` (returns the factorial). Your `main()` should handle input, call both functions, and display the results.

<details>
<summary>Solution</summary>

```python
def main():
    num = int(input("Enter a positive integer: "))

    while num <= 0:
        print("Must be positive!")
        num = int(input("Enter a positive integer: "))

    if is_even(num):
        print("{} is even.".format(num))
    else:
        print("{} is odd.".format(num))

    result = factorial(num)
    print("{}! = {}".format(num, result))

def is_even(number):
    return number % 2 == 0

def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result

main()
```

</details>
