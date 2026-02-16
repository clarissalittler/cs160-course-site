# Lesson 7 --- Constants

**After this lesson, you'll be able to:**

- Declare and use constants in your programs.

## Constants

Let's talk about a common problem. You're reading someone else's code and you see this:

```python
amount = balance * 0.075
```

What is `0.075`? An interest rate? A service fee? Some kind of tax? Only the person who wrote it knows for sure --- and if they wrote it six months ago, maybe not even them.

This is what programmers call a **magic number** --- an unexplained numeric value that just appears in the code like it fell from the sky. Magic numbers make code harder to read and *much* harder to maintain. Imagine this value appears in 15 different places and you need to change it. Yikes.

The fix is to use a **named constant** --- a variable whose value you set once and never change. Instead of scattering `0.075` throughout your code, you do this:

```python
INTEREST_RATE = 0.075
```

Now you can use it like:

```python
amount = balance * INTEREST_RATE
```

Much better, right? Anyone reading this code immediately knows what that number represents.

### The Convention

Notice that `INTEREST_RATE` is written in ALL_UPPERCASE with underscores between words. That's the convention in Python for constants --- it's a signal to anyone reading your code that says "don't change this value." Python won't actually *stop* you from changing it (unlike some other languages), but the uppercase naming is a strong "please don't touch this" signal.

Constants should always be created **outside of any functions** --- with no indentation --- so all functions in your program can access them.

### Try It Out

Run this program as an example --- *(copy and paste from below, or [download constants.py](https://drive.google.com/file/d/1jV6ulDPGba8bLz7oDpOeOraug3M6oRwb/view?usp=drive_link) and run it in your IDE of choice)*. `TAX_RATE` is the constant here:

```python
TAX_RATE = 0.0875

def main():
    cost = 10.24
    tax = cost * TAX_RATE
    total = cost + tax

    print('Cost: $', cost)
    print('Tax: $', tax)
    print('Total: $', total)

main()
```

When you run the program, take a look at the output. Notice anything off? Money should *always* be formatted to display exactly 2 decimal places --- we learned how to do that with `format()` back in the Data Types lesson. You might want to fix that up.

## Birth Year Tutorial

Watch the video below, which walks through designing and building a program that prompts the user for their name and age, then calculates and displays the year they were born.

[Video: Birth Year Program](https://www.youtube.com/watch?v=h_JM_2exd0I)

Feel free to follow along in your IDE and create the planning document as the video walks through it.

## Partner Activity

> **Discussion Prompt**
>
> Complete this activity with a partner from your study group.
>
> - Write a program to prompt the user for a cost.
> - Calculate the tax.
> - Print the cost, tax, and total cost of the item.
> - Use a tax rate of `0.0875` as a constant `TAX_RATE`.
> - Format money to 2 decimal places and include a `$`.
>
> Use this sample run to help you plan your program:
>
> ```
> Welcome to the tax calculator program!
> Enter cost of item: $ 10
> Cost: $ 10.00
> Tax: $ 0.88
> Total: $ 10.88
> Goodbye!
> ```
>
> When you're finished, post your code (with partner names) to the [LMS Activity: Unit 3 Lesson 7 --- Tax Rate Program Discussion] topic.
>
> After you've posted, open other students' programs and evaluate them. Leave comments with suggestions for improvement and any kudos!
