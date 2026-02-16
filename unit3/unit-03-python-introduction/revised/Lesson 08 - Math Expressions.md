# Lesson 8 --- Math Expressions

**After this lesson, you'll be able to:**

- Use operators to perform mathematical operations in your programs.

## Textbook Reading

- Read through [Sections 2.6 and 2.7](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/StatementsandExpressions.html) from [Chapter 2, Simple Python Data](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/toctree.html) in the Runestone Academy textbook. Try some programs in the workspace provided.
- [Section 2.6](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/StatementsandExpressions.html) covers Python statements and expressions.
- [Section 2.7](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/OperatorsandOperands.html) covers operators, order of operations, &c.
- Now is also a great time to read [Section 2.3](https://runestone.academy/runestone/books/published/thinkcspy/SimplePythonData/Typeconversionfunctions.html) to understand type conversion functions.

## Operators

Most of the algorithms you write will involve calculations of some kind. Here are the Python math operators you'll be using:

| Symbol | Operation            | Description                                                                 |
|--------|----------------------|-----------------------------------------------------------------------------|
| `+`    | Addition             | Adds two numbers.                                                           |
| `-`    | Subtraction          | Subtracts one number from another.                                          |
| `*`    | Multiplication       | Multiplies one number by another.                                           |
| `/`    | Division             | Divides one number by another. The result is always a float.                |
| `//`   | Integer Division     | Divides one number by another. The result is rounded *down* to a whole number (toward negative infinity). |
| `%`    | Remainder (Modulus)  | Divides one number by another and gives the remainder.                      |
| `**`   | Exponent             | Raises a number to a power.                                                 |

Most of these are straightforward, but `//` and `%` deserve a closer look --- we'll get to those in a moment.

You'll use these operators to build **math expressions**. A math expression performs a calculation and produces a value. Here's about as simple as it gets:

```python
12 + 3
```

The values on either side of the `+` are called **operands** --- they're the things the operator operates on.

Variables work in math expressions too, of course:

```python
hours = 40
payRate = 25.35
totalPay = hours * payRate
```

In that last line, `hours * payRate` is the math expression, and the result gets stored in `totalPay`.

## Floating-Point and Integer Division

Python has *two* different division operators, and they behave quite differently. This catches people off guard at first.

- `5 / 2` gives you `2.5` --- the `/` operator performs **floating-point division**, which gives you the full decimal result.
- `5 // 2` gives you `2` --- the `//` operator performs **integer division** (also called **floor division**), which rounds the result *down* to the nearest whole number. For positive numbers, this looks like it just chops off the decimal part.

That's a pretty important distinction! Try experimenting with different values in this program --- *(copy from below, or [download division.py](https://drive.google.com/file/d/1U6uVulMyt2sjxvEmuydolTbIB8IgrFvo/view?usp=drive_link) and run it in your IDE of choice)*. Write down the difference between `/` and `//` in your notebook. And here's a fun one: what happens when `num2` is `0`?

```python
def main():
    num1 = 5
    num2 = 3

    print("num1 / num2 :", num1 / num2)
    print("num1 // num2 :", num1 // num2)

main()
```

Spoiler: dividing by zero causes an error. Python doesn't like it. Math doesn't like it. Nobody likes it. It's just not allowed.

## Order of Operations

If you remember PEMDAS from math class --- good news, the same basic idea applies here. Python follows a specific order when evaluating expressions:

1. **Parentheses** first --- anything in `()` gets evaluated before everything else.
2. **Exponentiation**: `**`
3. **Multiplication, division, and remainder**: `*`, `/`, `//`, `%` --- these all have the same precedence.
4. **Addition and subtraction**: `+`, `-` --- also the same precedence as each other.

When two operators have the *same* precedence and share an operand, they're evaluated **left to right**. So `10 - 3 + 2` is `(10 - 3) + 2 = 9`, not `10 - (3 + 2) = 5`.

When in doubt, just use parentheses to make your intent crystal clear. Nobody ever complained about code being *too* readable.

### Practice Problems

What will each of these expressions evaluate to?

1. `(5 + 2) * 4`
2. `10 / (5 - 3)`
3. `8 + 12 * (6 - 2)`
4. `(6 - 2) * (3 + 8) // 3`

Work them out by hand first --- then check your answers below.

<details>
<summary>Show Solution</summary>

1. `28`
2. `5.0`
3. `56`
4. `14` --- remember, `//` truncates any decimal portion of the answer

</details>

### Verify Your Answers

Calculate the results first, then check them by typing the expressions into the `print()` parentheses in this program. Make sure you have matching open and close parentheses! *(Copy from below, or [download expression.py](https://drive.google.com/file/d/1-v98qh3F1ipH6iNrXgTJw382BU1q5l55/view?usp=drive_link) and run it in your IDE of choice.)*

```python
def main():
    print((9 + 1) // 3)

main()
```
