# Lesson 4 --- Decimal to Binary

![Unit 1 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Convert decimal numbers to binary.
- Convert binary numbers to decimal.

---

## Place values

Let's start with something you already know, even if you haven't thought about it in a while. In our decimal number system, what does **4036** represent? And *why*?

Each place value is a power of 10, and each digit tells us how many of that power we have:

| 10^3 | 10^2 | 10^1 | 10^0 |
|:----:|:----:|:----:|:----:|
| 1000 | 100  | 10   | 1    |
| **4** | **0** | **3** | **6** |

So 4036 is really:

**(4 x 1000) + (0 x 100) + (3 x 10) + (6 x 1) = 4036**

*Figure 1.6. Decimal place values*

You've been doing this since grade school, but it's worth pausing to notice the *structure*. Each position is worth 10 times as much as the one to its right. The digit in that position tells you how many of that value you've got. That's the whole system. Clean, simple, powerful.

Why does this matter? Because binary works **exactly the same way** --- except each place value is a power of **2** instead of 10, and you can only use 1's and 0's in each position.

## Building a binary calculator

In the video below, you'll create a paper binary calculator with an 8.5 x 11 inch piece of blank paper. Yes, actual paper. Grab a sheet and follow along --- this is one of those things that makes way more sense when you do it with your hands.

[Video: Decimal to Binary](https://www.youtube.com/watch?v=X7qYapwIpWc)

Here's the [Digital Binary Calculator](https://docs.google.com/spreadsheets/d/1DUr3HrVwMHm277F5zCoTxklpUO88-UN88g9Njna2opw/edit?usp=sharing) referenced in the video. You can turn powers of 2 on and off by checking the checkbox. Sum all of the place values with 1's to find the decimal equivalent. It's satisfying in a clicky sort of way.

### Bits and bytes

Each 1 or 0 is called a **bit** (short for "binary digit"). And 8 bits together? That's called a **byte**. We usually write binary numbers in groups of 8, adding leading 0's if needed. So the number 5 in binary isn't just `101` --- we'd write it as `00000101` to fill out the full byte.

Why 8? Honestly, it's a bit of a historical accident that became a standard. But it works out nicely: with 8 bits, you can represent 256 different values (0 through 255). That turns out to be a really useful range --- enough for all the letters, digits, and symbols you'd want for English text, for instance. (More on that in the next lesson.)

## Revisiting circles and squares

Remember the circle-and-square activity from Lesson 2? Let's bring it full circle (pun intended). Watch the video below to see the connection between circles/squares and 0's/1's --- and how finding patterns is really what this is all about.

[Video: Revisiting Circles and Squares](https://www.youtube.com/watch?v=Ts9v2zPc6ws)

## Check for understanding!

[LMS Activity: Unit 1 Lesson 4 Check for Understanding]
