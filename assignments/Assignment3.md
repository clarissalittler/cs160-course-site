# Assignment 3 - Tuple Database

This coding assignment will be a little bit different. This time you'll be writing code to be run by the interpreter you've installed (or replit/onlinegdb, if you chose to go that route) rather than in a colab document.

Your goal is to create a program like the examples shown in lecture/recording where you'll write a program about some topic (music, good dogs you've known, food carts in town, &c.) that will create a database with a list of tuples, each tuple being a "row" of the database.

Each tuple should have **at least 3 fields**. For example, if your topic is music, a single entry might look like:

```python
("Paranoid Android", "OK Computer", "Alternative")
```

That's: (song name, album, genre). You get to pick the topic and the fields --- just make sure there are at least three things per entry and that at least one of them is something you can meaningfully filter by.

## Part 1: Building the database

Write a while loop that lets the user enter in the data for the database one entry at a time. After each entry, ask whether they want to add another. Stop when the user says no.

Here's a sample interaction to give you an idea of what this should look like (yours doesn't need to match this exactly, this is just to show the *shape* of the thing):

```
Welcome to the music database!

Enter song name: Paranoid Android
Enter album: OK Computer
Enter genre: Alternative
Add another entry? (yes/no): yes

Enter song name: Genesis
Enter album: Selling England by the Pound
Enter genre: Progressive Rock
Add another entry? (yes/no): yes

Enter song name: Deacon Blues
Enter album: Aja
Enter genre: Jazz Rock
Add another entry? (yes/no): no
```

## Part 2: Displaying and filtering

Once the user is done entering data, ask if they want to filter the database by some criterion of your choice (e.g. filtering by genre, filtering by album, &c.). If they say yes, ask them what to filter by, then display only the matching entries. If they say no, just display the whole database.

Either way, display the results nicely using a for loop --- don't just `print(database)` and call it a day! Format each entry so it's pleasant to read, something like:

```
--- Your Music Database ---

Song: Paranoid Android
Album: OK Computer
Genre: Alternative

Song: Deacon Blues
Album: Aja
Genre: Jazz Rock
```

or

```
--- Filtering by genre: Jazz Rock ---

Song: Deacon Blues | Album: Aja | Genre: Jazz Rock
```

The exact formatting is up to you, just make it readable.

## Requirements summary

- Your database should be a **list of tuples**
- Each tuple should have **at least 3 fields**
- Part 1 uses a **while loop** for data entry
- Part 2 uses a **for loop** to display results
- The program should ask the user whether to filter and handle both yes and no
- Your output should be **formatted nicely**, not just raw `print()` of the list

## Submitting

Submit your `.py` file. Make sure your code runs without errors before you submit --- try it yourself with at least a few entries!
