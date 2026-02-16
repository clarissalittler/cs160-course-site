# Lesson 7 --- Writing Your Own Functions

![Unit 5 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Define and call your own functions in Python.
- Use parameters to pass information into a function.
- Use `return` to send a value back from a function.

---

## The big reveal

Okay. Remember this?

```python
def main():
    print("Hello, CS160!!")

main()
```

You've been typing some version of this since Unit 3. We told you it was the structure your programs need to follow --- `def main():` at the top, your code indented underneath, `main()` at the bottom. And you've been dutifully doing it ever since, probably without thinking too hard about *why*.

Well --- surprise. `def main():` is a **function**. You've been writing one this whole time.

Let's break it down piece by piece:

- **`def`** stands for *define*. It tells Python "I'm about to describe a new function."
- **`main`** is just a *name*. We called it `main` because that's a convention --- it's the "main" part of our program. But we could have called it `start` or `go` or `banana`. Python wouldn't care. (Your instructor would, though.)
- **`()`** are the parentheses where you'd put *parameters* --- inputs to the function. We've been leaving them empty because `main()` doesn't take any inputs. More on this soon.
- **`:`** starts the function body --- everything indented below it belongs to this function.
- **`main()`** at the bottom is the **function call**. This is the line that actually *runs* the function. Without it, Python would read your function definition and say "cool, noted" --- and then do absolutely nothing.

That last point is important, so let me say it again: **defining a function doesn't run it**. Defining is like writing down a recipe. Calling is like actually cooking the food.

## Why bother with functions?

So if we've been getting by just fine with everything inside `main()`, why learn about functions at all?

Here's a scenario. Let's say you're writing a program that prints a greeting for three different people, and each greeting has the same pattern:

```python
def main():
    print("=" * 30)
    print("Welcome, Alice!")
    print("We're so glad you're here.")
    print("=" * 30)
    print()

    print("=" * 30)
    print("Welcome, Bob!")
    print("We're so glad you're here.")
    print("=" * 30)
    print()

    print("=" * 30)
    print("Welcome, Carol!")
    print("We're so glad you're here.")
    print("=" * 30)
    print()

main()
```

Look at all that repeated code. Three blocks that are almost identical --- the only difference is the name. Now imagine you want to change the greeting from "We're so glad you're here" to "Thanks for joining us." You'd have to change it in *three places*. And if you had 50 people? Nightmare.

There's a principle in programming called **DRY** --- **Don't Repeat Yourself**. The idea is simple: if you're writing the same code more than once, there's probably a better way. Functions are that better way.

But DRY isn't the only reason to use functions. They also help you:

- **Organize** your code into logical chunks. Instead of one giant blob of code, you break it into named pieces.
- **Break big problems into small ones.** Instead of solving everything at once, you solve each piece separately. This is called **decomposition**, and it's one of the most important skills in programming.
- **Test pieces independently.** If something breaks, you know exactly which function to look at.

## Your first function (beyond `main`)

Let's start simple. Here's a function that prints a horizontal line of dashes:

```python
def main():
    print("Here's my program!")
    print_line()
    print("That line looked nice.")
    print_line()

def print_line():
    print("-" * 30)

main()
```

A few things to notice:

- We **defined** `print_line()` with `def print_line():` --- just like we define `main()`.
- We **called** it by writing `print_line()` inside `main()`. We called it twice, in fact, and it did the same thing both times.
- The function definition can go *above or below* `main()` --- Python reads all the function definitions before it starts executing anything. As long as the function is defined somewhere before `main()` is *called* at the bottom, you're fine.

Run this program and see what happens. Then try calling `print_line()` a few more times. Each call runs the entire function body again from the top.

## Parameters --- giving functions information

Our `print_line()` function always prints the same 30 dashes. That's fine, but what if sometimes we want 20 dashes and sometimes 50? We don't want to write a separate function for each length.

This is where **parameters** come in. A parameter is a variable that receives a value when the function is called. Think of it like a vending machine --- you put something *in* (your selection), and the machine does something with it.

```python
def main():
    print_line(30)
    print("Welcome!")
    print_line(10)

def print_line(length):
    print("-" * length)

main()
```

Here, `length` is a **parameter** --- a placeholder that gets filled in when the function is called. When we write `print_line(30)`, the value `30` gets assigned to `length` inside the function. When we write `print_line(10)`, the value `10` gets assigned to `length` instead.

The value you pass in when you *call* the function --- like `30` or `10` --- is called an **argument**. So: *parameters* are in the definition, *arguments* are in the call. Honestly, most people use these words interchangeably and nobody gets too upset about it.

Now let's fix that greeting program from earlier:

```python
def main():
    greet("Alice")
    greet("Bob")
    greet("Carol")

def greet(name):
    print("=" * 30)
    print("Welcome, " + name + "!")
    print("We're so glad you're here.")
    print("=" * 30)
    print()

main()
```

Look how much cleaner that is. Three lines instead of eighteen. And if you want to change the greeting message? You change it in *one place* --- inside the `greet` function --- and every call benefits automatically.

## Multiple parameters

Functions can take more than one parameter. You just separate them with commas:

```python
def main():
    greet("Alice", "Howdy")
    greet("Bob", "Hey there")
    greet("Carol", "Greetings")

def greet(name, greeting):
    print("=" * 30)
    print(greeting + ", " + name + "!")
    print("=" * 30)
    print()

main()
```

**Order matters.** When you call `greet("Alice", "Howdy")`, `"Alice"` gets assigned to `name` (the first parameter) and `"Howdy"` gets assigned to `greeting` (the second parameter). If you accidentally swap them --- `greet("Howdy", "Alice")` --- Python won't complain, but your output will say "Alice, Howdy!" which is... not what you wanted.

This is a common source of bugs. If your function's output looks weird, double-check that your arguments are in the right order.

## Return values --- functions that give something back

So far, our functions have *done* things --- they've printed text to the screen. But sometimes you don't want a function to *do* something; you want it to *calculate* something and give you the answer.

Think about it this way: `input()` is a function that *gives you back* a value (whatever the user typed). `int()` is a function that *gives you back* a value (the integer version of what you passed in). You've been using functions with return values since Unit 3 --- you just didn't know the terminology.

Here's how you write one:

```python
def main():
    result = add(3, 5)
    print(result)

def add(a, b):
    return a + b

main()
```

The `return` keyword sends a value *back* to wherever the function was called. So `add(3, 5)` doesn't just do some work and disappear --- it evaluates to `8`, and that `8` gets stored in `result`.

Here's a way to think about it. Some functions are like a *toaster* --- you put bread in, toast comes out. The toast is the return value. Other functions are like a *firework* --- you light it, something happens (pretty explosions), but nothing comes back to you. Both are useful, but they're doing different things.

- **Functions that return values** produce a result you can store in a variable, use in a calculation, or pass to another function.
- **Functions that just print** (or do other actions) perform a side effect. They don't give anything back.

Let's look at a more practical example --- a function that converts a temperature from Fahrenheit to Celsius:

```python
def main():
    temp_f = float(input("Enter temperature in Fahrenheit: "))
    temp_c = to_celsius(temp_f)
    print("{:.1f}F is {:.1f}C".format(temp_f, temp_c))

def to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

main()
```

The `to_celsius` function takes a Fahrenheit temperature, does the math, and *returns* the Celsius value. It doesn't print anything --- it just hands the answer back. The `main()` function decides what to do with it (in this case, print it). This separation is a good habit. Functions that return values are more flexible than functions that print, because the caller gets to decide how to use the result.

## Combining functions with loops

Here's where things get fun. You already know how to write loops. You now know how to write functions. Let's put them together.

Say you've got a simple grading program. You want to ask for five scores and convert each one to a letter grade:

```python
def main():
    for i in range(1, 6):
        score = int(input("Enter score {}: ".format(i)))
        grade = letter_grade(score)
        print("  Grade: " + grade)
        print()

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

Look at how clean `main()` is. You can read it almost like English: "For each of five scores, get the score, get the letter grade, print the grade." All the messy details of *how* to convert a score to a letter grade are tucked away inside `letter_grade()`. If the grading scale changes, you only need to update one function.

This is decomposition in action. You're breaking a problem into smaller, named pieces. Each function does one thing, does it well, and has a clear name that tells you what it does.

## Try it yourself

Write a program that asks the user for two numbers and an operation (add, subtract, multiply, or divide). Use a function called `calculate` that takes three parameters --- two numbers and the operation as a string --- and *returns* the result. Your `main()` function should handle the input and output.

Here's a skeleton to get you started:

```python
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (add/subtract/multiply/divide): ")

    result = calculate(num1, num2, op)
    print("Result: {}".format(result))

def calculate(a, b, operation):
    # Your code here!
    # Use if/elif/else to check the operation
    # Return the result
    pass

main()
```

<details>
<summary>Solution</summary>

```python
def main():
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    op = input("Enter operation (add/subtract/multiply/divide): ")

    result = calculate(num1, num2, op)
    print("Result: {}".format(result))

def calculate(a, b, operation):
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        if b != 0:
            return a / b
        else:
            print("Error: cannot divide by zero!")
            return 0
    else:
        print("Unknown operation!")
        return 0

main()
```

</details>
