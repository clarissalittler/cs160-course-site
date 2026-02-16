# Lesson 9 --- Modulus

> **What you'll be able to do after this lesson:**
>
> - Use the modulus `%` operator to calculate the remainder of a division operation.
> - Design and develop an inches conversion program.

## Textbook Reading

Read through [Section 2.7](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/OperatorsandOperands.html) from [Chapter 2, Simple Python Data](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/toctree.html) in the Runestone Academy textbook. This section covers the different operators, including integer division and modulus. Try some of the programs in the workspace they provide --- hands-on practice is the best way to make these stick.

## Modulus `%`

In Python, the `%` symbol is the **remainder operator** (also called the modulus operator). It performs division, but instead of giving you the quotient, it gives you the *remainder*. That's it. That's the whole trick.

Let's see how it compares to integer division (`//`):

**`7 // 3`** asks: "How many groups of 3 can we make from 7?"

![7 apples shown, 2 groups of 3 and a single apple left](images/apples1.png)

2 groups of 3 can be created, with 1 left over.

---

**`7 % 3`** asks: "What's left over after we make groups of 3?"

![7 apples, after forming groups of 3, there is one apple left over](images/apples2.png)

There's 1 remaining after creating groups of 3.

---

**`3 // 7`** asks: "How many groups of 7 can we make from 3?"

![No groups of 7 can be created from 3 apples](images/apples3.png)

0 groups. We don't even have enough apples.

---

**`3 % 7`** asks: "What's left over after we make groups of 7 from 3?"

![There are 3 apples left when creating groups of 7 apples out of 3 apples](images/apples3.png)

All 3 are remaining --- we couldn't make even one group of 7, so nothing got "used up." This one feels a little weird at first, but it makes sense if you think about it.

---

### Even or Odd?

One of the most common uses of modulus is checking whether a number is even or odd. Even numbers have a remainder of 0 when divided by 2. Odd numbers have a remainder of 1. Simple as that.

Run this to see it in action (copy from below or download [modulus1.py](https://drive.google.com/file/d/1mXju3y2c81mtANZDsR929DlWQDQ03NlO/view?usp=drive_link)):

```python
def main():
    print(5 % 2) # Is the number odd? Is the remainder 1?
    print(4 % 2) # Is the number even? Is the remainder 0?

main()
```

### Divisibility

Modulus is also great for checking if one integer is evenly divisible by another. If the remainder is 0, it divides evenly. That's the whole test. `9 % 3` is `0` because 3 goes into 9 perfectly.

Here's the pattern --- notice how the *possible* remainders are always 0 up to one less than the divisor:

```
n % 2   -> possible remainders: 0, 1
n % 3   -> possible remainders: 0, 1, 2
n % 10  -> possible remainders: 0, 1, 2, 3, 4, 5, 6, 7, 8, 9
```

Now try predicting: what are the possible remainders when dividing by 100?

## Example: Making Change

Suppose you've got a jar full of pennies and you want to exchange them for the fewest coins possible --- quarters, dimes, nickels, and whatever pennies are left. We can use division and modulus to figure this out!

Let's start with 48 pennies:

```python
cents = 48
```

We'll also want variables to track each coin type:

```python
quarters = 0
dimes = 0
nickels = 0
```

![48 pennies](images/mod3.png)

To minimize coins, we start with the biggest denomination --- quarters. We use integer division `//` to see how many groups of 25 we can make:

```python
quarters = cents // 25
```

That gives us 1 quarter (one group of 25) with 23 pennies left over.

Now we need to update `cents` to reflect what's remaining. We *could* do it with subtraction:

```python
cents = cents - (quarters * 25)
```

But we can also use modulus to get the same result --- and it's cleaner:

```python
cents = cents % 25
```

Both do exactly the same thing. We'll use modulus.

![48 pennies is 1 quarter and 23 pennies](images/mod4.png)

Next up, dimes. How many groups of 10 can we make from 23 pennies?

```python
dimes = cents // 10
```

That's 2 dimes, with 3 pennies left:

```python
cents = cents % 10
```

![23 pennies is 2 dimes and 3 pennies](images/mod5.png)

Now it's your turn! Complete the program below to also calculate nickels and remaining pennies. After it's working, try changing the starting number of cents to test other values. (Copy from below or download [modulus2.py](https://drive.google.com/file/d/124fPMW9_xpZTmPD7m_EMafmf4ZYyp2A2/view?usp=drive_link).)

```python
def main():
    cents = 48 # change this to test different amounts
    quarters = 0
    dimes = 0
    nickels = 0

    quarters = cents // 25 # number of quarters
    cents = cents % 25     # cents remaining

    # add code to calculate dimes, nickels, cents


    # print the results
    print('Quarters:', quarters)

main()
```

## Inches Conversion Tutorial

Watch the video below, which walks through designing and developing a program that converts inches to feet and inches. This is a great example of modulus in the real world --- you'll use `//` and `%` together to split a measurement into its component parts.

[Video: Inches Conversion Program](https://www.youtube.com/watch?v=sip3fBDmNOk)
