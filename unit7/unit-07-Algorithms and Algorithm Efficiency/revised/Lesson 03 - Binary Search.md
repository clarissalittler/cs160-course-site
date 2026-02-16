# Lesson 03 --- Binary Search

> **After this lesson, you'll be able to:**
>
> - Understand a Binary Search algorithm and use it to find a particular value in a sorted list.

## What Is Binary Search?

In the previous lesson, we saw how Linear Search works --- check every item, one by one. And as you probably noticed, that's not terribly efficient. There has to be a better way, right?

There is. And you already know the basic idea.

### Guess the Number

Here's a game: someone is thinking of a number between 1 and 15. The only feedback you get is "correct," "higher," or "lower."

You guess 8. They say "lower."

| 1 | 2 | 3 | 4 | 5 | 6 | 7 | **8** | 9 | 10 | 11 | 12 | 13 | 14 | 15 |
|---|---|---|---|---|---|---|-------|---|----|----|----|----|----|----|

What do you guess next? And what's the *maximum* number of guesses you'd ever need for 15 numbers?

### Using Feedback Smartly

The most efficient strategy is to always guess the **middle** number of whatever range is left.

| 1 | 2 | 3 | **4** | 5 | 6 | 7 | ~~8~~ | ~~9~~ | ~~10~~ | ~~11~~ | ~~12~~ | ~~13~~ | ~~14~~ | ~~15~~ |
|---|---|---|-------|---|---|---|-------|-------|--------|--------|--------|--------|--------|--------|

- If the middle number is correct, you're done!
- If they say "lower," you can throw away everything *above* the middle.
- If they say "higher," you can throw away everything *below* the middle.
- Repeat with whatever's left.

That's it. That's binary search. You cut the problem in half with every single guess. The name "binary" comes from this halving --- *bi* meaning two, as in splitting into two parts each time.

This is a *dramatically* more efficient way to search than checking every item one by one. But there's a catch --- **binary search only works if the data is already sorted** (ordered from smallest to largest). If your data is a jumbled mess, you'll either need to sort it first or fall back to linear search.

### Walking Through an Example

Let's say we're looking for the number **95** in this sorted list:

| Index: | 0 | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | 11 | 12  | 13  | 14  |
|--------|---|----|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|
| Value: | 1 | 12 | 23 | 43 | 55 | 61 | 67 | **68** | 87 | 89 | 91 | 95 | 113 | 114 | 115 |

- The midpoint index of 15 items is 7. The value there is 68. Compare 68 to 95.
- Since 95 > 68, we can ignore everything at index 7 and below.

Now we're only looking at indices 8 through 14:

| Index: | 0 | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  | 10 | **11** | 12  | 13  | 14  |
|--------|---|----|----|----|----|----|----|----|----|----|----|----|-----|-----|-----|
| Value: | 1 | 12 | 23 | 43 | 55 | 61 | 67 | 68 | 87 | 89 | 91 | **95** | 113 | 114 | 115 |

- The midpoint of indices 8 to 14 is 11 (that's (8 + 14) / 2). The value at index 11 is 95. Compare to 95 --- it's a match! We're done.

Two steps. That's it. A linear search might have needed up to 15 checks. Binary search found it in 2.

### See It in Action

Watch the animation below to step through the process visually and see how you can predict every step:

[Animation: Binary Search Visualization](https://yongdanielliang.github.io/animation/web/BinarySearchNew.html)

### Python Program: Guess the Number

Here's a fun Python program that puts binary search into practice. The computer picks a random number between 1 and 1000, and then either *you* try to guess it, or you watch the *computer* guess using binary search. It's a great way to see just how powerful this approach is --- the computer can always find the number in 10 guesses or fewer (out of 1,000 possibilities!).

```python
## CS160 Example: Guess the Number
## August 2022
## J. Abramson

## We need math to compute the log (base 2)
## We need random so the computer can pick a secret number
##
import math
import random

## The range of the number being guessed
## The target is the max number of guesses that it should take
## if the guesser is doing an optimal job.
##
LIMIT = 1000
TARGET = math.ceil(math.log(LIMIT,2))

def userGuesses():

  print("Hello, I have picked a number between 1 and", LIMIT)
  print("You get to try to guess it, hopefully in", TARGET, "guesses or less!")

  secret = random.randint(1,LIMIT)
  numGuesses = 0

  while(True):
    numGuesses = numGuesses + 1
    guess = int(input("Enter your guess: "))
    if (guess < secret):
      print("Your guess is too low, try again")
    elif (guess > secret):
      print("Your guess is too high, try again")
    else:
      print("Nice work!  You got it in ", numGuesses, "guesses!")
      break


def computerGuesses():

  print("Hello, please pick a number between 1 and", LIMIT)
  print("I will guess it in", TARGET, "guesses or less!")

  numGuesses = 0
  low = 1
  high = LIMIT
  while(True):
    numGuesses = numGuesses + 1
    guess = low + int((high-low)/2)
    print("My guess is", guess)
    feedback = int(input("Enter 1 for too low, 2 for too high, or 3 for just right!"))
    if (feedback == 1):
      low = guess + 1
    elif (feedback == 2):
      high = guess - 1
    else:
      break

  print("Congratulations to me, took me", numGuesses, "guesses!  Can you do better?")


def main():
  print("Welcome!")
  print("  1: I guess")
  print("  2: You guess")
  option = int(input("Please pick the option (1 or 2): "))
  if (option == 1):
    userGuesses()
  elif (option == 2):
    computerGuesses()
  else:
    print("Sorry, not a valid option!")

main()
```

### Quick Comparison: Linear vs. Binary Search

**Linear Search**

- *Pros:* Easy to implement. Works on any list, sorted or not.
- *Cons:* Doesn't scale well. For large lists, it's painfully slow.

**Binary Search**

- *Pros:* Blazing fast, even in the worst case. Scales beautifully to huge lists.
- *Cons:* Only works on sorted lists. That's a real limitation.

Here's the key takeaway: binary search is spectacularly efficient, but it demands sorted data. If your list is a mess, you've either got to sort it first (which takes work) or fall back to the humble linear search. And that's exactly why sorting algorithms matter --- which is what we'll dig into next.
