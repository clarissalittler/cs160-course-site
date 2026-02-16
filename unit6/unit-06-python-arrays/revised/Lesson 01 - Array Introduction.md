# Lesson 1 --- Array Introduction

![Unit 6 banner](img/banner.jpg)

> **After this lesson, you'll be able to:**
>
> - Explain how arrays (lists) are used in a Python program.

## Runestone Academy --- Textbook Resource

Read through [Section 10.1](https://runestone.academy/runestone/books/published/thinkcspy/Lists/intro-Lists.html) from [Chapter 10, Lists](https://runestone.academy/runestone/books/published/thinkcspy/Lists/toctree.html) in the textbook. This section introduces the *list* --- a sequential collection of Python data values. Try some programs in the workspace they provide while you're there.

## Lists of information

We make lists all the time in everyday life. Shopping lists, playlists, to-do lists, lists of classes we need to take --- our brains just love organizing things into sequences. It's one of the most natural ways we think about data.

In programming, we can do the same thing. A list of information is called an **array**. In Python specifically, arrays are called **lists** --- there are some technical differences between arrays and lists under the hood, but for our purposes, we'll use the two terms interchangeably. Don't worry about the distinction for now.

Once you've created a list, Python gives you some nice built-in tools to work with it. The `append()` function adds items to a list, and the `remove()` function takes items away. Pretty intuitive, right?

Run the program below --- look at the syntax for creating the list and then adding and removing items. (You can copy from here or download [shoppingList.py](https://drive.google.com/file/d/1j08dMQUlB_vDHkv4H2OYNpkrB-iP1nFt/view?usp=drive_link) and run it in your IDE of choice.)

Here's a fun experiment: what happens when you try to remove an item that *isn't* in the list? Try it and see!

```python
def main():
    # create a list called shoppingList, notice the []
    # to create the list of items
    shoppingList = ['apples', 'la croix', 'mango', 'rice']

    print(shoppingList) # print the list

    # add an item to the list and print again
    shoppingList.append('chicken')
    print(shoppingList)

    # remove an item from the list and print again
    shoppingList.remove('mango')
    print(shoppingList)

main()
```

The square brackets `[]` are the key thing to notice here --- that's how Python knows you're making a list. And `append()` always adds the new item to the *end* of the list, which is good to keep in mind.
