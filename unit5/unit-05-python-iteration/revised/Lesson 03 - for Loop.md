# Lesson 3 --- for Loop

![Unit 5 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Use the `for` loop to repeat statements a specific number of times.

---

## Textbook reading

- The `for` loop shows up in a couple of different sections in the textbook. They're short and well worth the read.
- Read through [Sections 4.4 and 4.5, The for loop](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/TheforLoop.html) from Chapter 4 in the Runestone Academy textbook. Then have some fun drawing graphics in Section 4.6 --- change the program and run it to see how the graphics change.

## The `for` loop

The `for` loop is a **count-controlled loop** --- it iterates a specific number of times. In Python, the `for` statement is designed to work with a **list of values** or a **range of values**. Each time the loop executes, it grabs the next item from the list.

![for loop syntax: for variable in (list of values): followed by statements to execute during each iteration. Statements must be indented. Variable contains the list values, one at a time.](images/for_loop.png)
*Figure 5.3. for loop syntax*

We'll call the first line the **for clause**. In the for clause, `variable` is the name of a variable. Inside the brackets, you've got a sequence of values separated by commas. Starting on the next line is a block of statements that executes each time the loop iterates.

Here's how it works:

- The `variable` is assigned the **first** value in the list, then the statements in the block execute.
- Then `variable` gets the **next** value in the list, and the block executes again.
- This continues until `variable` has been assigned the **last** value in the list.

That's it. Once there are no more values, the loop is done and execution continues with whatever comes after it.

## Stepping through a `for` loop

Step through the program below and watch the contents of the variable `index`:

[Python Tutor: for loop iterating over a list](https://pythontutor.com/iframe-embed.html#code=for%20index%20in%20%5B0,%201,%202,%203,%204%5D%3A%0A%20%20%20%20print%28index%20*%202%29%0A%20%20%20%20%0Aprint%28%22Done%20with%20for%20loop!%22%29&codeDivHeight=400&codeDivWidth=350&cumulative=false&curInstr=0&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

## Lesson video

[Video: for Loop](https://www.youtube.com/watch?v=6UWuEiFsCTw)

## Fun with Python!

Here's something neat --- lists in Python don't have to contain just one type of value. You can mix strings, integers, floats, booleans, &c. all in the same list. Copy the code below into your favorite Python environment and see what it does:

```python
# print a variety of value types in a list
for x in ["hello", 3, 5.5, True, "there!"]:
    print(x)
```

Personally, I think it's kind of wild that Python just lets you throw all those different types together. Most languages would yell at you for that.

In the next lesson, you'll learn how to use the `range()` function to generate a list of numbers to use with the `for` loop --- so you don't have to type them all out by hand.
