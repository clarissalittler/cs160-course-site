# Debugging Practice Problems

## What is debugging?

So far in this course, you've been writing code from scratch. That's great --- but in the real world, a huge part of programming is figuring out why code *doesn't* work. This is called **debugging**, and it's a skill all on its own.

The term comes from the early days of computing, when an actual moth got stuck in a relay inside a computer at Harvard and caused it to malfunction. They taped the moth into the logbook and wrote "first actual case of bug being found." The name stuck.

When you're debugging, you're playing detective. Here's a good way to approach it:

1. **Read the code carefully, line by line.** Don't skim. Read it like the computer would --- literally, one step at a time, top to bottom.
2. **Hand-trace the code.** Pick some sample input and walk through what happens to each variable. Write it down! (You've done this before in Lab 03 --- same idea.)
3. **Compare what the code *does* to what it *should* do.** The bug lives in the gap between those two things.
4. **Check the usual suspects.** Typos in variable names, wrong operators, indentation that's off by one level, loops that run one too many or one too few times --- these are the bugs you'll see over and over again.

Don't feel bad when code has bugs. All code has bugs at first. The goal isn't to write perfect code on the first try --- it's to get good at finding and fixing the problems.

---

## The Problems

For each problem below, you'll see some buggy Python code and a description of what the code is *supposed* to do. Your job is to:

- **Identify** the bug(s)
- **Explain** why they cause a problem
- **Fix** the code

Give it an honest try before peeking at the solution!

---

### Problem 1: Temperature Conversion

This program asks the user for a temperature in Fahrenheit and converts it to Celsius. The formula is: C = (F - 32) * 5/9

```python
temperature_f = input("Enter temperature in Fahrenheit: ")
temperature_c = (temperature_f - 32) * 5 / 9
print("That's " + str(temperature_c) + " degrees Celsius.")
```

What's wrong? Find the bug and fix it.

<details>
<summary>Solution</summary>

**The bug:** `input()` returns a string, but we're trying to do math with it on the next line. We need to convert it to a number first.

**The fix:**

```python
temperature_f = float(input("Enter temperature in Fahrenheit: "))
temperature_c = (temperature_f - 32) * 5 / 9
print("That's " + str(temperature_c) + " degrees Celsius.")
```

Wrap the `input()` call in `float()` so that `temperature_f` is a number we can do arithmetic with. (You could also use `int()`, but `float()` is better here since temperatures can be decimals.)

</details>

---

### Problem 2: Splitting a Restaurant Bill

This program is supposed to split a restaurant bill evenly among a group of friends and show how much each person owes. For example, if the bill is $60 and there are 4 people, each person should owe $15.00.

```python
total_bill = float(input("Enter the total bill: "))
num_people = int(input("How many people? "))
each_person = total_bill // num_people
print("Each person owes: $" + str(each_person))
```

Try it with a bill of $50 and 3 people. What goes wrong?

<details>
<summary>Solution</summary>

**The bug:** The program uses `//` (integer division) instead of `/` (regular division). Integer division throws away the remainder, so $50 // 3 gives `16.0` instead of `16.666...`. When you're splitting a bill, you want the actual amount --- not a rounded-down version that leaves money on the table.

**The fix:**

```python
total_bill = float(input("Enter the total bill: "))
num_people = int(input("How many people? "))
each_person = total_bill / num_people
print("Each person owes: $" + str(each_person))
```

Change `//` to `/`. (You might also want to round to two decimal places for a real bill-splitting app, but that's a bonus --- the core bug is the wrong division operator.)

</details>

---

### Problem 3: Voting Eligibility

This program checks whether someone is old enough to vote (18 or older).

```python
age = int(input("Enter your age: "))

if age > 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not old enough to vote yet.")
```

Try it with age 18. What happens, and why is that wrong?

<details>
<summary>Solution</summary>

**The bug:** The comparison uses `>` (strictly greater than) instead of `>=` (greater than or equal to). Someone who is exactly 18 *is* eligible to vote, but the code says they aren't because 18 is not strictly greater than 18.

This is an off-by-one error at a boundary --- one of the most common bugs in all of programming.

**The fix:**

```python
age = int(input("Enter your age: "))

if age >= 18:
    print("You are eligible to vote!")
else:
    print("Sorry, you are not old enough to vote yet.")
```

Change `>` to `>=`.

</details>

---

### Problem 4: Letter Grade Converter

This program takes a numerical score (0--100) and prints the corresponding letter grade. The scale is: A = 90--100, B = 80--89, C = 70--79, D = 60--69, F = below 60.

```python
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
if score >= 80:
    grade = "B"
if score >= 70:
    grade = "C"
if score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is: " + grade)
```

Try it with a score of 95. What grade does it print? Why?

<details>
<summary>Solution</summary>

**The bug:** The code uses a chain of separate `if` statements instead of `if`/`elif`/`else`. Because each `if` is independent, a score of 95 passes *all* of the first four checks: it's >= 90 (grade becomes "A"), then it's >= 80 (grade becomes "B"), then it's >= 70 (grade becomes "C"), then it's >= 60 (grade becomes "D"). So a 95 ends up as a "D"!

The `else` at the end is only paired with the last `if` (the `score >= 60` check), not with the whole chain.

**The fix:**

```python
score = int(input("Enter your score: "))

if score >= 90:
    grade = "A"
elif score >= 80:
    grade = "B"
elif score >= 70:
    grade = "C"
elif score >= 60:
    grade = "D"
else:
    grade = "F"

print("Your grade is: " + grade)
```

Change the second, third, and fourth `if` to `elif`. Now once one condition matches, the rest are skipped.

</details>

---

### Problem 5: Countdown

This program should print a countdown from 5 to 1 and then print "Blastoff!"

```python
count = 5
while count > 0:
    print(count)
print("Blastoff!")
```

What happens when you run this? (Careful --- you might need to hit Ctrl+C to stop it.)

<details>
<summary>Solution</summary>

**The bug:** The loop body never changes `count`. It just prints `5` over and over forever because `count` is always `5`, which is always greater than `0`. This is an **infinite loop** --- the loop condition never becomes false.

The fix is to *decrement* `count` inside the loop body so it eventually reaches 0.

**The fix:**

```python
count = 5
while count > 0:
    print(count)
    count = count - 1
print("Blastoff!")
```

Add `count = count - 1` (or equivalently, `count -= 1`) inside the loop. Now it prints 5, 4, 3, 2, 1, and then exits and prints "Blastoff!"

</details>

---

### Problem 6: Sum of Numbers

This program is supposed to ask the user for a positive integer *n* and then print the sum of all integers from 1 to *n* (inclusive). For example, if the user enters 5, it should print 15 (because 1 + 2 + 3 + 4 + 5 = 15).

```python
n = int(input("Enter a positive integer: "))

for i in range(1, n):
    total = total + i

print("The sum from 1 to " + str(n) + " is: " + str(total))
```

There are two bugs here. Can you find them both?

<details>
<summary>Solution</summary>

**Bug 1:** The variable `total` is never initialized before the loop. The first time the loop tries to do `total = total + i`, Python doesn't know what `total` is yet --- you'll get a `NameError`. The accumulator variable needs to be set to `0` before the loop starts.

**Bug 2:** `range(1, n)` goes from 1 up to *but not including* `n`. So if the user enters 5, the loop adds 1 + 2 + 3 + 4 = 10, missing the 5. This is an off-by-one error. It should be `range(1, n + 1)`.

**The fix:**

```python
n = int(input("Enter a positive integer: "))

total = 0
for i in range(1, n + 1):
    total = total + i

print("The sum from 1 to " + str(n) + " is: " + str(total))
```

Initialize `total = 0` before the loop, and change `range(1, n)` to `range(1, n + 1)`.

</details>

---

### Problem 7: Tip Calculator

This program is supposed to ask the user for a meal cost, let them choose a tip percentage (15%, 20%, or 25%), calculate the tip and total, and print the results. It has multiple bugs --- find and fix them all.

```python
meal_cost = input("Enter the meal cost: $")
print("Tip options:")
print("1. 15%")
print("2. 20%")
print("3. 25%")
choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    tip_percent = 0.15
elif choice == 2:
    tip_percent = 0.20
elif choice == 3:
    tip_percent = 0.25

tip_amount = meal_cost * tip_percent
total = meal_cost + tip_percent

print("Meal cost: $" + str(meal_cost))
print("Tip (" + str(tip_percent * 100) + "%): $" + str(tip_amount))
print("Total: $" + str(total))
```

Test it mentally with a meal cost of $40 and choice 2 (20%). What should the output be, and what does this code actually do?

<details>
<summary>Solution</summary>

**Bug 1:** `meal_cost` is never converted to a number. `input()` returns a string, so `meal_cost * tip_percent` will fail with a `TypeError`. It needs to be wrapped in `float()`.

**Bug 2:** The total calculation says `total = meal_cost + tip_percent` --- it's adding the *percentage* (0.20) to the meal cost instead of the *tip amount*. It should be `total = meal_cost + tip_amount`.

**Bug 3 (edge case):** If the user enters something other than 1, 2, or 3, `tip_percent` is never assigned, and the program will crash with a `NameError` when it tries to use `tip_percent`. A good fix is to add an `else` that handles bad input. (This one is a bit sneaky --- the problem description says "let them choose," so it's reasonable to expect only valid input, but a well-written program handles the unexpected too.)

**The fix:**

```python
meal_cost = float(input("Enter the meal cost: $"))
print("Tip options:")
print("1. 15%")
print("2. 20%")
print("3. 25%")
choice = int(input("Enter your choice (1, 2, or 3): "))

if choice == 1:
    tip_percent = 0.15
elif choice == 2:
    tip_percent = 0.20
elif choice == 3:
    tip_percent = 0.25
else:
    print("Invalid choice, defaulting to 20%.")
    tip_percent = 0.20

tip_amount = meal_cost * tip_percent
total = meal_cost + tip_amount

print("Meal cost: $" + str(meal_cost))
print("Tip (" + str(tip_percent * 100) + "%): $" + str(tip_amount))
print("Total: $" + str(total))
```

Three fixes: (1) `float(input(...))` for the meal cost, (2) `meal_cost + tip_amount` instead of `meal_cost + tip_percent`, and (3) an `else` clause so `tip_percent` always gets a value.

</details>

---

### Problem 8: Password Checker

This program is supposed to let the user try to guess a password. They get up to 3 attempts. If they guess correctly, it prints a success message and stops asking. If they use all 3 attempts without guessing correctly, it prints a lockout message.

```python
password = "python123"
attempts = 0
max_attempts = 3
guess = ""

while guess != password and attempts < max_attempts:
    guess = input("Enter the password: ")
    if guess = password:
        print("Access granted! Welcome.")
    else:
        print("Wrong password.")
        attempts = attempts + 1

if attempts = max_attempts:
    print("Too many failed attempts. Account locked.")
```

There are three bugs here. Try tracing through the code with a wrong guess followed by the correct guess --- what goes wrong?

<details>
<summary>Solution</summary>

**Bug 1:** Inside the loop, `if guess = password` uses `=` (assignment) instead of `==` (comparison). This is a syntax error in Python --- you can't use `=` inside an `if` condition. It should be `if guess == password`.

**Bug 2:** Same problem at the bottom: `if attempts = max_attempts` should be `if attempts == max_attempts`.

**Bug 3:** The `attempts` counter is only incremented in the `else` branch (wrong guesses), which is fine on its own. But the while loop condition checks `attempts < max_attempts` --- so after 3 wrong guesses, `attempts` becomes 3, which is *not* less than `max_attempts` (also 3), and the loop exits. That part works. However, when the user guesses *correctly*, the loop also exits (because `guess != password` is now false), but `attempts` wasn't incremented for the successful guess, so `attempts` is still less than `max_attempts`. The final `if` correctly won't print the lockout message in that case --- *but* the `attempts` counter doesn't get incremented on a correct guess, which means the count of attempts is off. More importantly, you need to actually increment `attempts` every time --- not just on wrong guesses --- if you want to accurately count how many tries were used.

Actually, let's reconsider: the counter tracking is a design issue, but the two `=` vs `==` bugs are the real show-stoppers (they're syntax errors --- the program won't even run). So the critical fixes are the two comparison operators. For a cleaner design, you'd also increment `attempts` on every guess, but the program will work correctly with the two `=` to `==` fixes as-is.

**The fix:**

```python
password = "python123"
attempts = 0
max_attempts = 3
guess = ""

while guess != password and attempts < max_attempts:
    guess = input("Enter the password: ")
    attempts = attempts + 1
    if guess == password:
        print("Access granted! Welcome.")
    else:
        print("Wrong password.")

if attempts == max_attempts and guess != password:
    print("Too many failed attempts. Account locked.")
```

The key changes: (1) `=` changed to `==` in both `if` statements, (2) `attempts` is incremented every time through the loop (not just on wrong guesses), and (3) the final check says `attempts == max_attempts and guess != password` so we only print the lockout message if the user actually failed --- not if they got it right on their third try.

</details>

---

## Final Thoughts

If you got some of these wrong, that's totally fine --- that's the whole point of practice. A few things to take away:

- **`=` vs `==`** is maybe the single most common bug in beginner code. Assignment vs. comparison. Drill it into your brain.
- **`input()` returns a string.** If you want to do math, you *must* convert with `int()` or `float()`.
- **`if` vs `elif`** matters a lot. A chain of `if` statements is *not* the same as `if`/`elif`/`elif`.
- **Off-by-one errors** show up everywhere --- in `range()`, in comparison operators (`>` vs `>=`), in loop conditions. When your code is "almost right but a little off," check your boundaries.
- **Infinite loops** usually mean you forgot to update a variable inside the loop body. If your program hangs, that's the first thing to check.

The more code you read --- especially broken code --- the better you'll get at spotting these patterns. Happy debugging!
