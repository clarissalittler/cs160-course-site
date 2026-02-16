# Break and Continue — Loop Control

*Supplementary material for Unit 5, Iteration*

---

You already know how to write `while` loops and `for` loops, and you've seen how to control them with conditions and `range()`. But sometimes — especially as your programs get more interesting — you run into situations where the normal flow of a loop isn't quite what you need. Maybe you want to bail out of a loop early because you've already found what you're looking for. Or maybe you want to skip over certain iterations without stopping the loop entirely.

Python gives you two tools for this: `break` and `continue`.

---

## `break` — Exit the Loop Early

`break` does exactly what it sounds like: it *breaks* out of the loop immediately. The loop stops, no more iterations run, and your program continues with whatever comes after the loop.

Here's a concrete example. Say you have a list of names and you want to search for a specific person:

```python
names = ["Alice", "Bob", "Charlie", "Diana"]
search = input("Who are you looking for? ")
found = False
for name in names:
    if name == search:
        found = True
        break
if found:
    print("Found them!")
else:
    print("Not in the list.")
```

Walk through this in your head. If the user types `"Charlie"`, the loop checks `"Alice"` — nope. Checks `"Bob"` — nope. Checks `"Charlie"` — match! It sets `found = True` and then `break` kicks us out of the loop *immediately*. We never bother checking `"Diana"` because there's no point — we already found what we were looking for.

### The same thing without `break`

You *could* write this without `break`. Here's what that looks like:

```python
names = ["Alice", "Bob", "Charlie", "Diana"]
search = input("Who are you looking for? ")
found = False
for name in names:
    if not found and name == search:
        found = True
if found:
    print("Found them!")
else:
    print("Not in the list.")
```

This works, but notice the difference: even after we find `"Charlie"`, the loop keeps running. It checks `"Diana"` for no reason. And we have to add that `if not found` check to avoid doing unnecessary work on every remaining iteration. With a four-element list this doesn't matter much — but imagine searching a list of ten thousand names. The `break` version stops as soon as it finds a match. The no-`break` version always checks every single name.

The `break` version is cleaner, more efficient, and says what it means more directly: "I found it, I'm done."

---

## `continue` — Skip This Iteration

`continue` is `break`'s gentler sibling. Instead of exiting the loop entirely, it just skips the rest of the *current* iteration and jumps to the next one.

Here's an example — printing only the even numbers from 1 to 10:

```python
for i in range(1, 11):
    if i % 2 != 0:
        continue
    print(i)
```

When `i` is 1, the condition `i % 2 != 0` is `True` (1 is odd), so `continue` fires and we skip the `print()`. When `i` is 2, the condition is `False`, so we don't hit `continue` and the `print()` runs normally. The output is `2 4 6 8 10`.

### The same thing without `continue`

Here's the version using just `if`/`else`:

```python
for i in range(1, 11):
    if i % 2 == 0:
        print(i)
```

Honestly? This version is *also* perfectly fine — maybe even clearer. And that's an important thing to know about `continue`: it's useful, but it's easy to overuse. If your logic is just "do something when a condition is true," a plain `if` statement is usually more readable than "skip when the condition is false" using `continue`.

Where `continue` really shines is when you have a lot of code in your loop body and you want to skip *all of it* for certain cases — it saves you from wrapping everything in a big `if` block. But for simple cases like this one, either approach works.

---

## `while True` with `break` — A Pattern for Input Validation

You've already seen input validation loops in Lesson 5 — asking the user for input, checking if it's valid, and asking again if it's not. You probably wrote something like this:

```python
age = int(input("Enter your age: "))
while age < 0 or age > 120:
    print("That doesn't seem right, try again.")
    age = int(input("Enter your age: "))
```

Notice how the `input()` call appears *twice* — once before the loop and once inside it. That duplication is a little annoying. If you later decide to change the prompt message, you have to remember to change it in both places.

Here's the same thing using `while True` and `break`:

```python
while True:
    age = int(input("Enter your age: "))
    if 0 <= age <= 120:
        break
    print("That doesn't seem right, try again.")
```

`while True` creates a loop that runs forever — or at least, it *would* run forever if we didn't have that `break` in there. The logic is: ask for input, check if it's valid, and if so, `break` out of the loop. If not, print an error message and the loop naturally repeats (because the condition is still `True` — it's *always* `True`).

This pattern has a few nice properties:
- The `input()` call only appears once
- The valid-input check is right next to the input itself
- The flow reads top-to-bottom in a natural way: get input, check it, either leave or complain and try again

You'll see `while True` with `break` all over the place in real Python code. It's one of those patterns worth getting comfortable with.

---

## When to Use `break` vs. When to Restructure

`break` is great for two common patterns:

1. **Search until found** — loop through a collection looking for something, and stop as soon as you find it
2. **Get valid input** — keep asking until the user gives you something reasonable (`while True` + `break`)

But here's a word of caution: if you find yourself putting multiple `break` statements in a single loop, or your loop logic is getting tangled with breaks and continues and flags all interacting — that's usually a sign you should step back and rethink the structure. Maybe the loop should be split into two loops, or maybe the condition in the `while` statement itself should be doing more of the work.

`break` and `continue` are tools, not goals. Use them when they make your code clearer. Don't use them just because they exist.

---

## Practice Problems

**Problem 1: First Negative**

Write a program that asks the user to enter numbers one at a time (use a loop). When the user enters a negative number, stop and print that negative number. If they enter `0`, also stop — but print `"No negative number entered."` instead.

*Hint: `while True` with `break` works well here.*

Example run:
```
Enter a number (0 to quit): 5
Enter a number (0 to quit): 12
Enter a number (0 to quit): 3
Enter a number (0 to quit): -7
The first negative number was: -7
```

---

**Problem 2: Skip the Vowels**

Given the string `"programming"`, use a `for` loop with `continue` to print each character on its own line — but skip any vowels (a, e, i, o, u).

Expected output:
```
p
r
g
r
m
m
n
g
```

---

**Problem 3: Password Checker**

Write a program that asks the user to create a password. The password must be at least 8 characters long. If it's too short, print an error and ask again. Use the `while True` / `break` pattern.

Once they enter a valid password, print `"Password set!"`.

Example run:
```
Create a password: cat
Too short! Must be at least 8 characters.
Create a password: hello
Too short! Must be at least 8 characters.
Create a password: mysecurepassword
Password set!
```
