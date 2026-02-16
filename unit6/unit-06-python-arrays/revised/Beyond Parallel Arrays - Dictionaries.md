# Beyond Parallel Arrays — Dictionaries

*Supplementary material for Unit 6, Arrays*

---

## The Problem with Parallel Arrays

You've been working with parallel arrays (parallel lists, really — Python calls them lists). The idea is straightforward: you keep related data in separate lists, lined up by index. Index 0 in the `names` list goes with index 0 in the `scores` list, index 1 with index 1, &c.

```python
names = ["Alice", "Bob", "Charlie"]
scores = [92, 85, 78]
```

And to print everything out, you loop through by index:

```python
for i in range(len(names)):
    print(names[i], "scored", scores[i])
```

This works. But it's *fragile*. The connection between a name and its score is purely in your head — Python has no idea that `names[2]` and `scores[2]` are supposed to go together. If you accidentally sort one list without sorting the other, or append to one and forget the other, your data gets silently scrambled. No error message, no warning — just wrong results.

That's a rough kind of bug to track down.

---

## Dictionaries: Connecting Keys to Values

Python has a built-in data structure that solves this problem directly: the **dictionary**. A dictionary lets you associate a **key** with a **value** — no index-matching required.

Here's our student scores example as a dictionary:

```python
student_scores = {
    "Alice": 92,
    "Bob": 85,
    "Charlie": 78
}
```

The curly braces `{}` create a dictionary. Each entry is a key-value pair, separated by a colon. `"Alice"` is a key, `92` is its value. The key and value are directly connected — you can't accidentally scramble them the way you can with parallel lists.

### Accessing Values

To look up a value, you use the key in square brackets — similar to how you use an index with a list, but instead of a number you use the key itself:

```python
print(student_scores["Alice"])   # prints 92
print(student_scores["Bob"])     # prints 85
```

This is really nice. Instead of having to figure out that Alice is at index 0 and then looking up index 0 in the scores list, you just ask the dictionary directly: "What's Alice's score?"

### Adding New Entries

Adding a new key-value pair looks just like assigning to a new index — but with a key instead of a number:

```python
student_scores["Diana"] = 95
```

That's it. Now the dictionary has four entries. You didn't have to remember to also add `"Diana"` to a separate names list — the name and score are stored together.

### Looping Through a Dictionary

You can loop through a dictionary with a `for` loop. By default, you iterate over the keys:

```python
for name in student_scores:
    print(name, "scored", student_scores[name])
```

Output:
```
Alice scored 92
Bob scored 85
Charlie scored 78
Diana scored 95
```

Compare that with the parallel arrays version:

```python
names = ["Alice", "Bob", "Charlie", "Diana"]
scores = [92, 85, 78, 95]
for i in range(len(names)):
    print(names[i], "scored", scores[i])
```

Both produce the same output. But the dictionary version has a couple of advantages:
- You don't need to manage two separate lists
- You don't need `range(len(...))` — the loop is cleaner
- The data can't get out of sync because there's only one data structure to manage

---

## When to Use Which

So if dictionaries are so great, why did we learn parallel arrays at all? Good question. Here's the honest breakdown:

**Use a dictionary when** you want to look things up by a meaningful key — a name, an ID number, a word, &c. If your first instinct is "I want to find the score *for* Alice," that's a dictionary problem.

**Use a list when** order matters and you need to access things by position. Lists are great for sequences — a list of temperatures in chronological order, a list of steps to follow, a deck of cards where the order matters.

**Parallel arrays** — honestly, dictionaries (or lists of tuples, which you saw in Assignment 3) are usually better for the kinds of problems that parallel arrays solve. Parallel arrays are taught because they show up in a *lot* of existing code and textbooks — especially in languages that don't have something as convenient as Python's dictionaries. It's important to recognize the pattern when you see it. But in practice, Python gives you better tools.

---

## Connecting to What You Already Know

You've already seen lists of tuples in Assignment 3 — that's another way to associate related pieces of data (keeping them together in a tuple rather than splitting them across parallel lists). Dictionaries are yet another option. Python gives you lots of ways to organize data — the right choice depends on what you're trying to do:

- Need to look something up by a key? Dictionary.
- Need an ordered sequence you can walk through? List.
- Need to group a few related values together (like a name and a score) into a single "thing"? Tuple — or a dictionary entry.

There's no single "correct" choice for every situation. Part of getting better at programming is building intuition for which tool fits which problem.

---

## A Few More Dictionary Details

Before you dive into the practice problems, here are a couple of things worth knowing:

**Checking if a key exists.** If you try to access a key that isn't in the dictionary, Python will give you a `KeyError`. You can check first using `in`:

```python
if "Eve" in student_scores:
    print(student_scores["Eve"])
else:
    print("Eve is not in the dictionary.")
```

**Keys must be unique.** Each key can only appear once in a dictionary. If you assign a new value to an existing key, it overwrites the old one:

```python
student_scores["Alice"] = 97  # Alice's score is now 97, not 92
```

**Keys are usually strings or numbers.** Technically, any "immutable" type can be a key (you'll learn what that means later — for now, just know that strings and numbers work fine as keys, but lists don't).

---

## Practice Problems

**Problem 1: Phone Book**

Create a dictionary that stores the names and phone numbers of three friends. Then ask the user to type a name. If the name is in the dictionary, print their phone number. If not, print `"Not found."`.

Example run:
```
Who do you want to call? Alice
Alice's number is 503-555-1234
```

---

**Problem 2: Word Counter**

Ask the user to enter a sentence. Split it into words (you can use `.split()` — it breaks a string into a list of words at each space). Then build a dictionary where each key is a word and each value is the number of times that word appears.

Print the dictionary at the end.

Example run:
```
Enter a sentence: the cat sat on the mat
{'the': 2, 'cat': 1, 'sat': 1, 'on': 1, 'mat': 1}
```

*Hint: loop through the list of words. For each word, check if it's already a key in your dictionary. If it is, add 1 to its value. If it isn't, set its value to 1.*

---

**Problem 3: Parallel Arrays to Dictionary**

You're given these two parallel lists:

```python
items = ["apple", "bread", "milk", "eggs"]
prices = [1.20, 2.50, 3.00, 4.75]
```

Write a program that converts them into a single dictionary where the item names are keys and the prices are values. Then print each item and its price using a loop over the dictionary.

Expected output:
```
apple: $1.20
bread: $2.50
milk: $3.00
eggs: $4.75
```

*This is a good exercise for seeing exactly how a dictionary replaces parallel arrays — you're literally converting one into the other.*
