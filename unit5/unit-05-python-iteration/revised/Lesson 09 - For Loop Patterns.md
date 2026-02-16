# Lesson 9 --- For Loop Patterns

![Unit 5 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Use different `for` loop patterns to iterate over collections in Python.
- Choose the right loop pattern depending on whether you need the item, the index, or both.
- Write nested `for` loops.

---

## Where we are

You already know how to write `for` loops with `range()` and with a list of values. That's great --- those tools alone can carry you pretty far. But as your programs get more interesting (especially once we start working with lists in Unit 6), you're going to run into situations where you need to loop through data in different ways. Sometimes you just want each item. Sometimes you need to know *where* each item is. Sometimes you need both.

This lesson covers the main patterns for writing `for` loops in Python. Think of it as building up your loop vocabulary --- more ways to say the same kind of thing, but each suited to a different situation.

## Pattern 1: `for item in collection`

This is the one you already know, but let's make sure we really appreciate it, because it's the most important one.

```python
for fruit in ["apple", "banana", "cherry"]:
    print(fruit)
```

**Output:**
```
apple
banana
cherry
```

That's it. Each time through the loop, `fruit` takes on the next value in the list. You get the *item itself* --- not its position, not some number you then have to use to look something up. Just the thing.

Personally, I think this is the best loop pattern in Python, and you should reach for it first whenever you can. It's clean, it's readable, and it does exactly what you'd expect. If someone reads your code, they immediately understand: "Oh, we're doing something with each fruit."

Here's another example --- adding up some numbers:

```python
total = 0
for score in [88, 92, 75, 100, 63]:
    total = total + score

print("Total:", total)
print("Average:", total / 5)
```

**Output:**
```
Total: 418
Average: 83.6
```

No index variable, no `range()`, no fuss. We just wanted each score, and we got each score.

**When to use this pattern:** Whenever you just need the items and don't care about their positions. Which is honestly most of the time.

## Pattern 2: `for i in range(len(collection))`

Okay, so Pattern 1 is great --- but what if you *do* need to know where each item is? What if you need to say "Item #1 is apple, Item #2 is banana," &c.? Then you need the **index** --- the position number.

Here's what that looks like:

```python
fruits = ["apple", "banana", "cherry"]

for i in range(len(fruits)):
    print("Item", i, "is", fruits[i])
```

**Output:**
```
Item 0 is apple
Item 1 is banana
Item 2 is cherry
```

Let's break this down, because there's a lot going on in that first line:

- `fruits` is a list with 3 items.
- `len(fruits)` gives you the length of the list --- that's `3`.
- `range(3)` generates the numbers `0, 1, 2`.
- So `i` takes on the values `0`, `1`, and `2`, one at a time.
- Inside the loop, `fruits[i]` grabs the item at position `i`. (The bracket notation `fruits[0]`, `fruits[1]`, &c. is how you access individual items in a list --- you'll learn all about this in Unit 6.)

Is this clunkier than Pattern 1? Absolutely. You've got `range(len(...))` cluttering up the first line, and you have to write `fruits[i]` every time you want the actual item instead of just using a nice variable name like `fruit`. It's not pretty.

But sometimes you genuinely need the index. Here are a few situations where this pattern earns its keep:

**Numbering items in a list:**

```python
colors = ["red", "green", "blue", "yellow"]

for i in range(len(colors)):
    print(str(i + 1) + ".", colors[i])
```

**Output:**
```
1. red
2. green
3. blue
4. yellow
```

(We used `i + 1` because humans like to start counting at 1, but Python starts at 0. This mismatch never stops being slightly annoying.)

**Comparing adjacent items:**

```python
temperatures = [72, 75, 68, 70, 73]

for i in range(len(temperatures) - 1):
    diff = temperatures[i + 1] - temperatures[i]
    if diff > 0:
        print("Day", i + 1, "to Day", i + 2, ": went up by", diff)
    elif diff < 0:
        print("Day", i + 1, "to Day", i + 2, ": went down by", abs(diff))
    else:
        print("Day", i + 1, "to Day", i + 2, ": no change")
```

**Output:**
```
Day 1 to Day 2 : went up by 3
Day 2 to Day 3 : went down by 7
Day 3 to Day 4 : went up by 2
Day 4 to Day 5 : went up by 3
```

Notice that we used `range(len(temperatures) - 1)` there --- we stop one short of the end, because we're comparing each item to the *next* one, and the last item doesn't have a next one. If we didn't subtract 1, we'd get an error when `i + 1` tried to go past the end of the list. This is the kind of detail that trips people up, so keep an eye out for it.

**When to use this pattern:** When you need the index number and don't mind the extra verbosity. Or when you need to modify items in the list or compare neighbors.

## Pattern 3: `for i, item in enumerate(collection)`

What if you need *both* the index and the item? You could use Pattern 2 and write `fruits[i]` everywhere, but Python gives us something nicer.

```python
fruits = ["apple", "banana", "cherry"]

for i, fruit in enumerate(fruits):
    print(i, fruit)
```

**Output:**
```
0 apple
1 banana
2 cherry
```

Isn't that nice?

The `enumerate()` function takes a list and gives you back pairs of `(index, item)`. Each time through the loop, `i` gets the index and `fruit` gets the item. Best of both worlds --- you get the position *and* a clean variable name for the item, without having to write `fruits[i]`.

Let's redo that numbered list example from Pattern 2:

```python
colors = ["red", "green", "blue", "yellow"]

for i, color in enumerate(colors):
    print(str(i + 1) + ".", color)
```

**Output:**
```
1. red
2. green
3. blue
4. yellow
```

Same result, but the loop body is cleaner. We get to write `color` instead of `colors[i]`, which is just easier to read.

Here's a fun trick --- you can tell `enumerate()` to start counting from a number other than 0:

```python
colors = ["red", "green", "blue", "yellow"]

for i, color in enumerate(colors, start=1):
    print(str(i) + ".", color)
```

**Output:**
```
1. red
2. green
3. blue
4. yellow
```

Now we don't even need the `i + 1` --- `enumerate` starts at 1 for us. Small thing, but it makes the code that little bit tidier.

**When to use this pattern:** Whenever you need both the index and the item. It's almost always better than `range(len(...))` for this situation.

## Pattern 4: Dictionary iteration (a preview)

We haven't talked about **dictionaries** yet --- they're coming later in the course. But I want to mention this now so it doesn't catch you off guard when you see it.

A dictionary is like a list, except instead of accessing items by position number (0, 1, 2, ...), you access them by a **key** --- like a word in a real dictionary. Here's a tiny preview:

```python
ages = {"Alice": 20, "Bob": 22, "Charlie": 19}

for name, age in ages.items():
    print(name, "is", age, "years old")
```

**Output:**
```
Alice is 20 years old
Bob is 22 years old
Charlie is 19 years old
```

Don't worry about the details here --- just notice that the pattern looks a lot like `enumerate()`. You get two variables each time through the loop, one for the key and one for the value. When we get to dictionaries later, this will already feel familiar.

## Pattern 5: Nested for loops

Sometimes you need a loop *inside* a loop. This is called a **nested loop**, and it's one of those things that sounds complicated but makes perfect sense once you see it.

Here's the key idea: **the inner loop runs completely for each single iteration of the outer loop.**

Let's build a multiplication table:

```python
for row in range(1, 4):
    for col in range(1, 4):
        print(row * col, end="\t")
    print()
```

**Output:**
```
1	2	3
2	4	6
3	6	9
```

Let's trace through this carefully:

1. `row` starts at `1`.
   - The inner loop runs with `col` = `1`, `2`, `3` --- printing `1`, `2`, `3`.
   - Then `print()` moves us to a new line.
2. `row` becomes `2`.
   - The inner loop runs *again from the beginning* with `col` = `1`, `2`, `3` --- printing `2`, `4`, `6`.
   - Then `print()` moves us to a new line.
3. `row` becomes `3`.
   - The inner loop runs *again from the beginning* with `col` = `1`, `2`, `3` --- printing `3`, `6`, `9`.
   - Then `print()` moves us to a new line.

The outer loop ran 3 times. Each time, the inner loop ran 3 times. That's 3 x 3 = 9 total multiplications. If the outer loop ran 100 times and the inner loop ran 100 times, you'd get 10,000 iterations. Nested loops can add up fast --- something to keep in mind.

(The `end="\t"` in the print statement tells Python to put a tab character after each number instead of the usual newline. That's how we get everything on the same row. The `print()` by itself after the inner loop finishes gives us the newline to start the next row.)

Here's another example --- printing a little grid of stars:

```python
rows = 4
cols = 6

for r in range(rows):
    for c in range(cols):
        print("*", end=" ")
    print()
```

**Output:**
```
* * * * * *
* * * * * *
* * * * * *
* * * * * *
```

Same idea: the outer loop handles each row, and the inner loop prints each column within that row. Once the inner loop finishes a row of stars, the `print()` drops down to the next line.

**When to use this pattern:** Whenever you're working with data that has two dimensions --- grids, tables, rows and columns, &c. You'll also see nested loops used to compare every item in a list against every other item.

## Choosing the right pattern

Here's a quick decision guide:

**Do you need the index (position number)?**

- **No** → Use `for item in collection:` (Pattern 1). It's the simplest and most readable.
- **Yes** → Do you also need the item itself?
  - **Yes** → Use `for i, item in enumerate(collection):` (Pattern 3). You get both.
  - **No** → Use `for i in range(len(collection)):` (Pattern 2). You just get the index.

And if you need to work through every combination of two sets of values, that's a nested loop (Pattern 5).

When in doubt, start with Pattern 1. It's the most Pythonic way to iterate, and it covers the majority of situations. Only reach for the others when you genuinely need an index.

## Practice exercises

**Exercise 1:** Write a program that has a list of at least 5 names. Use a `for` loop (Pattern 1) to print a greeting for each name, like `"Hello, Alice!"`.

<details>
<summary>Show Solution</summary>

```python
names = ["Alice", "Bob", "Charlie", "Diana", "Eli"]

for name in names:
    print("Hello, " + name + "!")
```

**Output:**
```
Hello, Alice!
Hello, Bob!
Hello, Charlie!
Hello, Diana!
Hello, Eli!
```

</details>

**Exercise 2:** Write a program that has a list of at least 5 test scores. Use `enumerate()` to print each score with its number, like `"Test 1: 88"`, `"Test 2: 92"`, &c.

<details>
<summary>Show Solution</summary>

```python
scores = [88, 92, 75, 100, 63]

for i, score in enumerate(scores, start=1):
    print("Test " + str(i) + ": " + str(score))
```

**Output:**
```
Test 1: 88
Test 2: 92
Test 3: 75
Test 4: 100
Test 5: 63
```

</details>

**Exercise 3:** Write a program that uses nested `for` loops to print this triangle pattern:

```
*
* *
* * *
* * * *
* * * * *
```

Hint: the outer loop controls which row you're on (1 through 5). The inner loop prints that many stars.

<details>
<summary>Show Solution</summary>

```python
for row in range(1, 6):
    for col in range(row):
        print("*", end=" ")
    print()
```

The trick is that the inner loop uses `range(row)` --- so on row 1 it prints 1 star, on row 2 it prints 2 stars, &c. The inner loop's upper limit changes with each iteration of the outer loop. That's a pattern worth remembering.

</details>
