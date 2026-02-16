# Lesson 10 --- Input

> **What you'll be able to do after this lesson:**
>
> - Make your programs interactive by asking for user input.

## Textbook Reading

Read through [Section 2.8](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/Input.html) from [Chapter 2, Simple Python Data](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/toctree.html) in the Runestone Academy textbook. This section has a video and some really solid examples for user input. Try out the programs in the workspace they provide.

## Input

So far, our programs have only worked with values we've hard-coded. That's fine for learning, but it's not very useful in the real world. We want our programs to be *interactive* --- to ask the user for information and then do something with it.

Python has a built-in function called `input()` that does exactly this. When your program hits an `input()` call, it pauses, waits for the user to type something on the keyboard, and then returns whatever they typed.

Usually, you'll want to store that result in a variable so you can use it later. One single statement can do all three things at once:

- Prompt the user for input
- Read in the input
- Store the input into a variable

Here's the basic format:

```python
variable = input(prompt)
```

One important thing to know: **everything that comes back from `input()` is a string**. Always. Even if the user types `42`, Python sees it as the string `"42"`, not the number `42`. We'll deal with that in a minute.

> **Bug Alert:**
>
> New programmers sometimes forget to assign the result of `input()` to a variable! If you just write `input("Enter your name: ")` all by itself, Python will ask the question, the user will type an answer... and then that answer disappears into the void. You have to put it somewhere!

For example, when this statement runs:

```python
name = input("Enter your name: ")
```

Three things happen:

1. The string `"Enter your name: "` appears on the screen
2. The program pauses and waits for the user to type something and press Enter
3. Whatever the user typed gets returned as a string and stored in the variable `name`

## String Input

Sometimes we'll want to compare string input later in our programs. For example, maybe we want to check if the user entered "Portland" --- but we want to match regardless of how they capitalized it: Portland, portland, PORTLAND, PoRtLaNd, &c.

The trick is to convert the input to a consistent case before comparing. Python gives us methods for this:

```python
city = input("Enter the city you live in: ")
city = city.upper()  # converts string to all UPPERCASE
city = city.lower()  # converts string to all lowercase
```

You'd use one or the other --- not both --- depending on what you're comparing against. This is a really handy pattern you'll use constantly.

## Pseudocode

Back in Lesson 2, we wrote an algorithm for splitting a restaurant bill between four friends. That algorithm was perfectly fine for another human to follow, but computers need a bit more precision. Let's bridge that gap.

Watch the video below to see how we take that bill-splitting algorithm, convert it to pseudocode, and then write a working Python program using everything we've learned so far:

[Video: Pseudocode for Computer Programs](https://www.youtube.com/watch?v=emFkoEFHWVk)

## Numeric Input

Here's the thing that trips people up: if *all* user input comes in as a string, how do we work with numbers?

We wrap the `input()` call with a conversion function. Use `int()` for whole numbers and `float()` for decimal numbers:

```python
quantity = int(input('Enter the quantity: '))
cost = float(input('Enter the cost: $'))
```

Notice the nested parentheses there. `input()` runs first and returns a string, then `int()` or `float()` converts that string into a number. Python will almost always want the same number of left parentheses `(` as right parentheses `)` --- so count them if something looks off.

Let's try a complete program. Run this a few times with different input. (Copy and paste from below or download [input.py](https://drive.google.com/file/d/1tqcFWHkW669shIadXUInWgBEWV8fPllI/view?usp=drive_link).)

```python
def main():
    item = input('Enter item: ')
    cost = float(input('Enter cost $ '))
    quantity = int(input('Enter quantity: '))

    # we can use a math expression because cost
    # and quantity were converted to numbers
    total = cost * quantity

    print("Total: $", format(total, ".2f"))

main()
```

Here's a fun experiment: what happens when you enter non-numeric input (like "hello") when it asks for cost or quantity? Try it! You'll get an error --- and that's totally expected. We don't have the tools to handle that gracefully yet, but we will eventually.
