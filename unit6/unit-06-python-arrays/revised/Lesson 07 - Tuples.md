# Lesson 7 --- Tuples

> **After this lesson, you'll be able to:**
>
> - Create tuples to group related pieces of data together.
> - Access individual elements of a tuple using indexing.
> - Use tuple unpacking (destructuring) to assign tuple elements to individual variables.
> - Explain when to use a tuple versus a list.

## What's a Tuple?

You've been working with lists for a while now. Lists use square brackets, they can hold any kind of data, and you can add, remove, and change elements whenever you want. Lists are flexible --- that's their whole thing.

A **tuple** is like a list's more disciplined sibling. It uses parentheses `()` instead of square brackets `[]`, and once you create it, you *can't change it*. No adding, no removing, no swapping elements around. What you put in is what you get.

```python
# A list (square brackets, changeable)
favorite_foods = ["pizza", "tacos", "ramen"]

# A tuple (parentheses, NOT changeable)
point = (3, 5)
```

Here are a few more tuples:

```python
person = ("Alice", 22, "Portland")
date = (2, 14, 2025)
song = ("Bohemian Rhapsody", "Queen", 1975)
```

Notice something? Each of those tuples groups together pieces of information that *belong together*. A person has a name, an age, and a city. A date has a month, a day, and a year. A song has a title, an artist, and a release year. The pieces are different types --- strings, ints --- but they describe one thing.

That's the key idea: **a tuple bundles related data into a single unit.**

> **Fun tangent:** The word "tuple" comes from mathematics. A pair of things is a "double," three things is a "triple," four is a "quadruple," five is a "quintuple" --- and the general term for *n* things is an "n-tuple." Computer scientists just shortened it to "tuple." It's pronounced either "TUP-ul" (rhymes with "couple") or "TOO-pul" (rhymes with... well, nothing really). People get weirdly passionate about which pronunciation is correct. Use whichever one you like.

## Why Would You Want Something You Can't Change?

This is the question everyone asks. If lists can do everything tuples can do *and* you can modify them, why would you ever pick the less flexible option?

Here's the thing: the immutability isn't a limitation. It's a *feature*.

Think about a point on a graph: `(3, 5)`. That's x = 3, y = 5. If you could accidentally change the x-coordinate without meaning to, that would be bad --- it wouldn't be the same point anymore. You *want* it to stay put.

Same with a date. February 14th, 2025 is February 14th, 2025. You don't want some line of code to accidentally change the month to 37. By using a tuple, you're telling Python --- and anyone reading your code --- "these values go together, and they shouldn't be messed with."

A list says: "Here's a collection. Feel free to add, remove, or rearrange."

A tuple says: "These specific pieces of data belong together as a unit. Don't touch them."

It's a way of communicating your *intent*. And in programming, making your intent clear is worth a lot.

## Accessing Tuple Elements

Good news: indexing works exactly the same as lists. Zero-indexed, same as everything else in Python.

```python
person = ("Alice", 22, "Portland")

print(person[0])   # Alice
print(person[1])   # 22
print(person[2])   # Portland
```

You can also use `len()` on tuples:

```python
print(len(person))  # 3
```

And you can loop through them:

```python
for item in person:
    print(item)
```

But here's what you *can't* do:

```python
person[1] = 23  # ERROR! Tuples don't allow this.
```

Python will yell at you with a `TypeError: 'tuple' object does not support item assignment`. It's not being mean --- it's doing exactly what tuples are designed to do. You said "this data shouldn't change," and Python is holding you to it.

## Tuple Packing and Unpacking

Okay, here's where tuples get *really* nice. This is the part that makes them worth learning.

When you create a tuple by putting values in parentheses, that's called **packing**:

```python
# Packing --- putting values into a tuple
person = ("Alice", 22, "Portland")
```

Three values got packed into one variable. Simple enough.

**Unpacking** (also called **destructuring**) is the reverse --- you pull the values *out* of a tuple and into individual variables, all in one line:

```python
# Unpacking --- pulling values out of a tuple
name, age, city = person
```

After that line, `name` is `"Alice"`, `age` is `22`, and `city` is `"Portland"`. One line, three assignments. Beautiful.

Let's see the whole thing together:

```python
person = ("Alice", 22, "Portland")

# Instead of this:
print(person[0])  # Alice
print(person[1])  # 22
print(person[2])  # Portland

# You can do this:
name, age, city = person
print(name)   # Alice
print(age)    # 22
print(city)   # Portland
```

Both approaches give you the same result, but the unpacking version is *so much more readable*. `name` tells you exactly what that piece of data is. `person[0]`... well, you'd have to go look at where the tuple was created to figure out what's at index 0.

### The Catch

The number of variables on the left side **must match** the number of elements in the tuple. If they don't match, Python raises a `ValueError`:

```python
person = ("Alice", 22, "Portland")

# This works --- 3 variables, 3 elements
name, age, city = person

# This does NOT work --- 2 variables, 3 elements
name, age = person   # ValueError: too many values to unpack
```

Python is pretty clear about what went wrong: "too many values to unpack" means the tuple has more elements than you have variables for. If it were the other way around (more variables than elements), it would say "not enough values to unpack." Fair enough.

## Tuples vs. Lists --- When to Use Which

Here's a handy way to think about it:

**Lists** are for collections of *similar things*. A list of names. A list of scores. A list of temperatures. The items are all the same kind of thing, and the list might grow or shrink as your program runs.

**Tuples** are for grouping *different pieces of information about one thing*. A name AND an age AND a city. A month AND a day AND a year. A title AND an artist AND a release year.

Another way to put it:

- A **list** answers: "What are all the ___?"  (What are all the students? What are all the scores?)
- A **tuple** answers: "What do we know about this one thing?" (What's this student's name, age, and major?)

And here's the punchline --- you can combine them. A **list of tuples** gives you a list where each entry is a bundle of related information. That's like a spreadsheet or a mini database. We'll get into that next lesson, and it's the pattern you'll use for Assignment 3.

## Exercises

**Exercise 1: My Favorite Song**

Create a tuple called `song` that stores three things: a song title, the artist, and the year it was released. Then use unpacking to pull those values into three separate variables (`title`, `artist`, `year`). Print a sentence like:

```
"Bohemian Rhapsody" by Queen was released in 1975.
```

Use an f-string if you'd like.

---

**Exercise 2: Tuple Experiments**

Try each of the following in Python and note what happens. Write a comment explaining *why* each one works or doesn't.

```python
# 1. Create a tuple and try to change one element
colors = ("red", "green", "blue")
colors[0] = "yellow"

# 2. Unpack with the wrong number of variables
point = (10, 20)
x, y, z = point

# 3. Unpack with the right number
date = (7, 4, 1776)
month, day, year = date
print(f"{month}/{day}/{year}")
```

---

**Exercise 3: Parallel Arrays to Tuples**

You're given these parallel lists from a pet adoption center:

```python
names = ["Luna", "Mochi", "Biscuit"]
species = ["cat", "dog", "rabbit"]
ages = [3, 5, 2]
```

Write a program that creates a tuple for each pet (combining name, species, and age), and prints out a sentence for each one using tuple unpacking. Your output should look like:

```
Luna is a cat, age 3
Mochi is a dog, age 5
Biscuit is a rabbit, age 2
```

*Hint: use `range(len(names))` to loop through the parallel lists by index, then build a tuple from the matching elements and unpack it.*
