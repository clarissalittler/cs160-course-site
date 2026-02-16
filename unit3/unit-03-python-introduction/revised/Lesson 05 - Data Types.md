# Lesson 5 --- Data Types

**After this lesson, you'll be able to:**

- Use numeric and string data types in your programs.

## Textbook Reading

- Start with the video in [Section 2.1, Variables, Expressions and Statements](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/intro-VariablesExpressionsandStatements.html) from [Chapter 2, Simple Python Data](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/toctree.html) in the Runestone Academy textbook.
- Read through [Section 2.2, Values and Data Types](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/ValuesandDataTypes.html). This section covers numeric data and strings. Make sure to try some programs in the workspace provided!

## Numeric Data Types

Here's something that might seem obvious but is actually important: not all numbers are the same. The number `3` and the number `3.14` are stored and manipulated differently inside the computer. Python keeps track of this distinction using *data types*.

- When an integer is stored in memory, it's classified as an `int`. These are whole numbers with no decimal point --- things like `3`, `125`, and `-19`.
- When a real number (one with decimals, like `3.24` or `-10.23333`) is stored in memory, it's classified as a `float`.

The name "float" comes from "floating point" --- which refers to the way the decimal point can "float" to different positions. It's a whole thing from the history of computing, and honestly the name is a little weird, but we're stuck with it.

### Formatting Floats

When printing float types, we can specify how many decimal places to show using the `format()` function. Before you run the program below, *predict* what it'll print. Here's the real question: do you think `format()` will **round** or **truncate** decimal values? *(You can [download format.py](https://drive.google.com/file/d/1pC0g5LmNC-AfEE9Sn35ctH4oFF15dCfr/view?usp=drive_link) and run it in your IDE of choice.)*

```python
def main():
    rate = .0755
    weight = 14.5678
    area = 345.44123

    print('rate:', format(rate, '.2f'))
    print('weight:', format(weight, '.3f'))
    print('area:', format(area, '.1f'))

main()
```

The call to `format()` is actually being passed *as an argument* to `print()` --- a function call inside a function call. It looks a little nested, but you'll get used to it:

![print('rate:', format(rate, '.2f')) --- the format function is passed the variable rate and the string '.2f' to direct print() to display rate with 2 decimal places. The arguments to format go inside format's parentheses, and the whole format() call goes inside print()'s parentheses.](images/format_function.png)

## String Data Types

In addition to `int` and `float`, Python has a data type called `str` --- short for *string* --- which is used for storing text in memory.

[Video: String Data Types](https://www.youtube.com/watch?v=18THLg-j2us)

A string is a sequence of characters enclosed in either single `'` or double `"` quotes:

```python
firstName = "Julie"
lastName = 'Green'
```

You can create new strings by combining existing ones using the **concatenation** operator `+`. Both operands have to be strings for this to work:

```python
fullName = firstName + " " + lastName
```

> **Bug Alert:** Numeric literals and string literals can *look* identical when printed, but they're stored completely differently in memory.
>
> ```python
> x = 2.3      # this is a float numeric type
> y = "2.3"    # this is a string with the characters 2 and . and 3
> z = "4"      # this is a string with the character 4, not the numeric value 4
> ```
>
> This distinction matters a lot --- `2.3 + 3.4` gives you `5.7`, but `"2.3" + "3.4"` gives you `"2.33.4"`. Yep, really.

You can't do math on string literals. If you use the `+` operator on two strings, Python performs concatenation instead of addition. Step through the program below and pay close attention to what ends up in the variable `result`:

[Python Tutor: String concatenation vs. addition demo](https://pythontutor.com/iframe-embed.html#code=def%20main%28%29%3A%0A%20%20%20%20num1%20%3D%20%222.3%22%0A%20%20%20%20num2%20%3D%20%223.4%22%0A%20%20%20%20result%20%3D%20num1%20%2B%20num2%0A%20%20%20%20print%28result%29%0A%20%20%20%20%0Amain%28%29&codeDivHeight=300&codeDivWidth=500&cumulative=false&curInstr=8&heapPrimitives=nevernest&origin=opt-frontend.js&py=3&rawInputLstJSON=%5B%5D&textReferences=false)

> **Bug Alert:** If you want to use concatenation with an `int` or `float`, you need to convert it to a string first using the `str()` function.
>
> ```python
> firstName = 'Julie'
> age = 29
> message = firstName + ' is ' + str(age) + ' years old!'
> ```
>
> Without that `str()` call, Python will throw an error because it doesn't know how to glue a string and a number together.

### Fix the Bug!

Run the program below. You should see a red error message that says **`TypeError: can only concatenate str (not "int")`**. This happens because the numeric values need to be converted to strings before they can be concatenated with `+`. Find and fix the errors! *(You can [download data_types.py](https://drive.google.com/file/d/1WAufRSIE7jIYZQKzFNOJf32XeRcxDp0-/view?usp=drive_link) and run it in your IDE of choice.)*

```python
def main():
    item = 'bananas'
    quantity = 2
    cost = 1.34

    receiptItem = "Item: " + item + " Qty: " + quantity \
                  + " Unit cost $" + cost \
                  + " Total $" + cost * quantity

    # print the long string we created
    print(receiptItem)

main()
```

This is one of those things that trips up every beginner --- you'll see this error, you'll fix it, and eventually you'll start catching it before you even run the program.
