# Lesson 02 --- Linear Search

> **After this lesson, you'll be able to:**
>
> - Understand a simple Linear Search algorithm and use it to find a particular value in an unsorted list.

## What Is Linear Search?

Computers spend a *lot* of their time working with large lists of data. And one of the most fundamental things they do with that data is search through it --- say, looking up a particular student record so it can be displayed on screen.

So what's the simplest way to search a list? Check the first item. Then the second. Then the third. Keep going until you either find what you're looking for or run out of list. Because we march through the list in a straight line from start to finish, this is called a **linear search**.

Simple, right? Almost too simple. But to be a proper algorithm, we need to spell it out in terms a computer can actually follow.

### The Algorithm

Assume we have a list called `list` filled with integers. Each integer sits at a unique position --- its **index**. We're searching for the location of a particular value, often called the `key`. Here's how it works:

```
Note: assume that list and key are already set
1   set location = 1
2   repeat until location > (length of the list)
3       if list[location] == key
4           print "Found at " + location
5           end program
6       set location = location + 1    advance to next location
7
8   print "Value not found"
```

Notice that `location` is just a variable storing which index we're currently looking at. And `list[location]` is the standard way of saying "the value in `list` at position `location`."

### Seeing It in Python

If you worked through the previous unit on arrays, this should look familiar --- we're doing exactly the same thing. Here's Python code that creates a list of random numbers and tries to find a specific value in it:

```python
# Demo for Linear Search
import random

# main function
def main():
    value = 6
    numbers = []
    for num in range(1, 10):
        numbers.append(random.randrange(1, 10, 1))
    print(numbers)

    found = False
    for num in range(len(numbers)):
        if numbers[num] == value:
            print("Your number is in index:", num)
            found = True
    if not found:
        print("Number not found!")

# call main
main()
```

### The Big Weakness

Linear search is easy to understand and easy to implement. But it has one glaring weakness --- you potentially have to look at **every single item** in the list.

Imagine trying to find someone's phone number in a phone book using linear search. You'd start at "Aardvark, Aaron" and check every single entry until you found your person. That would be... unpleasant.

While linear search works perfectly fine for small jobs, it doesn't scale well to larger problems at all. We're going to need something smarter --- and that's exactly what the next lesson is about.
