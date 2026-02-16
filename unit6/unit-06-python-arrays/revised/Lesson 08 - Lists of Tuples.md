# Lesson 8 --- Lists of Tuples

> **After this lesson, you'll be able to:**
>
> - Combine lists and tuples to create a "tuple database" --- a list where each element is a tuple.
> - Use destructuring in a `for` loop to iterate through a list of tuples cleanly.
> - Build a list of tuples from user input.
> - Filter and sort a list of tuples.

## Putting It Together: Lists *of* Tuples

Last lesson we learned that a tuple groups related pieces of data into one unit. And we already know that lists hold collections of things. So what happens when you put tuples *inside* a list?

You get something that looks a lot like a spreadsheet.

```python
students = [
    ("Alice", 95, "CS"),
    ("Bob", 87, "Art"),
    ("Charlie", 92, "Music"),
    ("Diana", 78, "Biology"),
    ("Eli", 91, "CS")
]
```

Each tuple is a row --- one student's complete record. The list holds all the rows. You've basically built a little database.

Compare this to the parallel arrays version of the same data:

```python
# Parallel arrays version
names   = ["Alice", "Bob", "Charlie", "Diana", "Eli"]
scores  = [95,      87,    92,        78,      91]
majors  = ["CS",    "Art", "Music",   "Biology", "CS"]
```

Both approaches store the same information. But with parallel arrays, you have to remember that `names[2]`, `scores[2]`, and `majors[2]` all refer to Charlie. If you ever sort one list without sorting the others, or append to one and forget the rest, your data gets silently scrambled. No error --- just wrong results.

With a list of tuples, Charlie's data is `("Charlie", 92, "Music")` --- all in one place, impossible to separate by accident. I personally think this is *much* nicer.

## Iterating with Destructuring

Here's where the real magic happens. Remember tuple unpacking from last lesson? You can use it directly in a `for` loop:

```python
students = [
    ("Alice", 95, "CS"),
    ("Bob", 87, "Art"),
    ("Charlie", 92, "Music"),
    ("Diana", 78, "Biology"),
    ("Eli", 91, "CS")
]

for name, score, major in students:
    print(f"{name} scored {score} and studies {major}")
```

Output:

```
Alice scored 95 and studies CS
Bob scored 87 and studies Art
Charlie scored 92 and studies Music
Diana scored 78 and studies Biology
Eli scored 91 and studies CS
```

Each time through the loop, Python takes the next tuple from the list and unpacks it into `name`, `score`, and `major`. Three variables, three elements, everything lines up.

Now compare that with the parallel arrays version:

```python
for i in range(len(names)):
    print(f"{names[i]} scored {scores[i]} and studies {majors[i]}")
```

Same output. But look at the difference. The tuple version reads almost like English: "for each name, score, and major in students." The parallel arrays version is all `names[i]`, `scores[i]`, `majors[i]` --- you have to mentally track what `i` is doing and make sure all three lists are in sync.

This is one of those moments where Python really shines. The language lets you write code that says what it *means*.

## Building a List of Tuples from User Input

Alright, here's a pattern you're going to use a *lot* --- especially in Assignment 3. We start with an empty list, ask the user for data in a loop, pack the data into a tuple, and append that tuple to the list.

```python
def main():
    database = []

    while True:
        name = input("Enter student name (or 'quit' to stop): ")
        if name == "quit":
            break
        score = int(input("Enter their score: "))
        major = input("Enter their major: ")

        # Pack the data into a tuple and add it to the list
        student = (name, score, major)
        database.append(student)
        print(f"Added {name}!\n")

    # Display all the records
    print("\n--- Student Database ---")
    for name, score, major in database:
        print(f"{name}: {score} ({major})")

main()
```

Let's trace through what's happening:

1. `database` starts as an empty list: `[]`
2. The `while True` loop keeps asking for input until the user types `"quit"`.
3. Each time through, we collect a name, score, and major, then pack them into a tuple.
4. `database.append(student)` adds that tuple to the end of the list.
5. After the loop, we iterate through the list with destructuring and print each record.

You could also skip the intermediate variable and append the tuple directly:

```python
database.append((name, score, major))
```

Notice the double parentheses --- the outer ones are for `append()`, and the inner ones create the tuple. It looks a little weird at first, but you get used to it.

> **Heads up:** This input-loop-and-append pattern is exactly what you'll need for Assignment 3. You'll pick a topic --- movies, recipes, hiking trails, whatever interests you --- and build a tuple database using this structure. Each tuple will be a record with at least 3 fields, and you'll collect them from the user in a loop just like this.

## Filtering a List of Tuples

Here's another thing you'll need for the assignment: displaying only the records that match some criteria. It's just a loop with an `if` statement inside.

Say you want to find all CS students:

```python
students = [
    ("Alice", 95, "CS"),
    ("Bob", 87, "Art"),
    ("Charlie", 92, "Music"),
    ("Diana", 78, "Biology"),
    ("Eli", 91, "CS")
]

print("CS students:")
for name, score, major in students:
    if major == "CS":
        print(f"  {name}: {score}")
```

Output:

```
CS students:
  Alice: 95
  Eli: 91
```

Or maybe you want everyone who scored above 90:

```python
print("High scorers (above 90):")
for name, score, major in students:
    if score > 90:
        print(f"  {name}: {score} ({major})")
```

Output:

```
High scorers (above 90):
  Alice: 95 (CS)
  Charlie: 92 (Music)
  Eli: 91 (CS)
```

The pattern is always the same: loop with destructuring, check a condition, print (or do something with) the matches. You can filter on any field --- or even combine conditions with `and`/`or`.

You could also let the *user* choose what to filter by:

```python
search_major = input("Which major do you want to search for? ")

found = False
for name, score, major in students:
    if major == search_major:
        print(f"{name}: {score}")
        found = True

if not found:
    print(f"No students found in {search_major}.")
```

That `found` flag is a nice trick --- it lets you print a helpful message when the search comes up empty. Nobody likes staring at a blank screen wondering if the program is broken.

## Sorting a List of Tuples

Python's `sorted()` function works on lists of tuples too. By default, it sorts by the **first element** of each tuple:

```python
students = [
    ("Charlie", 92, "Music"),
    ("Alice", 95, "CS"),
    ("Eli", 91, "CS"),
    ("Bob", 87, "Art"),
    ("Diana", 78, "Biology")
]

by_name = sorted(students)
for name, score, major in by_name:
    print(f"{name}: {score}")
```

Output:

```
Alice: 95
Bob: 87
Charlie: 92
Diana: 78
Eli: 91
```

Alphabetical by name --- because the name is the first element of each tuple, and that's what `sorted()` looks at by default.

But what if you want to sort by score instead? You can use the `key=` parameter with a small function (called a **lambda** --- don't worry too much about the syntax, just see the pattern):

```python
by_score = sorted(students, key=lambda s: s[1])
for name, score, major in by_score:
    print(f"{name}: {score}")
```

Output:

```
Diana: 78
Bob: 87
Eli: 91
Charlie: 92
Alice: 95
```

And if you want highest-to-lowest, add `reverse=True`:

```python
by_score_desc = sorted(students, key=lambda s: s[1], reverse=True)
```

The `lambda s: s[1]` part is saying "for each tuple `s`, sort by element at index 1" --- which is the score. You can change `s[1]` to `s[2]` to sort by major, or `s[0]` to sort by name, &c.

> **Don't sweat the lambda.** If the `lambda` syntax looks alien right now, that's totally fine. For Assignment 3, you can always sort by the first element for free (just call `sorted()`), and that might be all you need. The `key=` trick is there when you want it.

## Why This Matters

Let's step back and look at the big picture.

You started this unit with individual lists --- a list of names, a list of numbers. Then you learned about parallel arrays, where multiple lists are held together by matching indexes. That works, but it's fragile --- it relies on *you* keeping everything in sync, and Python won't warn you if things get out of alignment.

Lists of tuples solve that problem. Each record is self-contained. You can loop through them with destructuring that reads like plain English. You can filter them, sort them, and build them from user input. It's the same data, organized in a way that's harder to mess up.

This pattern --- a list of tuples acting as a simple database --- shows up everywhere in real programming. When you read data from a CSV file, it often comes in as a list of tuples (or something very similar). Database queries return rows that look like tuples. Even spreadsheet data, when you pull it into Python, follows this structure.

And in your next assignment, you'll be building exactly this kind of tuple database about a topic you choose. You'll collect records from the user, store them as tuples in a list, display the full database, let the user search and filter, and maybe sort the results. Everything we've covered in this lesson is directly preparing you for that.

## Exercises

**Exercise 1: Pet Database**

Write a program that lets the user build a database of pets. Each pet record should be a tuple with three fields: name (string), species (string), and age (int). Use a `while` loop to keep collecting records until the user types `"done"` for the name. Then print out all the pets.

Example run:

```
Pet name (or 'done' to stop): Luna
Species: cat
Age: 3
Added Luna!

Pet name (or 'done' to stop): Mochi
Species: dog
Age: 5
Added Mochi!

Pet name (or 'done' to stop): done

--- Pet Database ---
Luna the cat, age 3
Mochi the dog, age 5
```

---

**Exercise 2: Filter the Menu**

You're given this list of tuples representing a cafe menu:

```python
menu = [
    ("Latte", 4.50, "drink"),
    ("Croissant", 3.25, "food"),
    ("Espresso", 3.00, "drink"),
    ("Bagel", 2.75, "food"),
    ("Chai Tea", 4.00, "drink"),
    ("Muffin", 3.50, "food")
]
```

Write a program that:

1. Prints the full menu with prices.
2. Asks the user whether they want to see only drinks, only food, or everything.
3. Prints just the matching items.

Example run:

```
--- Full Menu ---
Latte: $4.50
Croissant: $3.25
Espresso: $3.00
Bagel: $2.75
Chai Tea: $4.00
Muffin: $3.50

Show: (d)rinks, (f)ood, or (a)ll? d

--- Drinks ---
Latte: $4.50
Espresso: $3.00
Chai Tea: $4.00
```

---

**Exercise 3: Assignment 3 Warm-Up**

This one is directly preparing you for the assignment. Pick a topic you're interested in --- movies, video games, recipes, hiking trails, albums, &c. Write a program that:

1. Lets the user enter records with at least 3 fields each (e.g., title, genre, and rating for movies).
2. Stores each record as a tuple in a list.
3. After input is done, displays all records.
4. Asks the user for a search term and displays only the matching records.

This is essentially a simplified version of Assignment 3. If you can get this working, you're in great shape for the real thing.
