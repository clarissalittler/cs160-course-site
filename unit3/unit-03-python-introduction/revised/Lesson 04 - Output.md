# Lesson 4 --- Comments and Output

**After this lesson, you'll be able to:**

- Use comments in Python programs.
- Use `print()` to display output.
- Use escape sequences within string literals to format output.

## Textbook Reading

Read through Sections 1.12 and 1.13 from [Chapter 1, General Introduction to the Python Programming Language](https://runestone.academy/runestone/books/published/thinkcspy/GeneralIntro/ThePythonProgrammingLanguage.html) in the Runestone Academy textbook. [Section 1.12](https://runestone.academy/runestone/books/published/thinkcspy/GeneralIntro/ATypicalFirstProgram.html) covers a typical first program --- you'll meet the `print` function here. [Section 1.13](https://runestone.academy/runestone/books/published/thinkcspy/GeneralIntro/Comments.html) is all about comments. Try some code in the workspace they provide!

## The Big Picture: How Programs Work

Computer programs typically follow a three-step process:

1. **Input** is received.
2. Some **process** is performed on the input.
3. **Output** is produced.

That's it. Seriously --- almost every program you'll ever use follows this pattern, from a calculator app to a massive video game. Input, process, output.

![Computer program processes: input from keyboard/mouse, data stored in memory, CPU processes input, output sent to monitor/printer/speaker](images/four_steps.png)
*Figure 3.2. Computer program processes: input, store data, process, and output.*

In this lesson, we're focusing on that last step --- getting output out of a Python program.

## Video Lesson

[Video: Comments and Output](https://www.youtube.com/watch?v=UGI1fq2N32Q)

## Comments: Notes to Yourself (and Future You)

Before we dive into output, let's talk about comments. The output we'll discuss below is for whoever *uses* your program. But what about messages meant for *you* --- or the next programmer who reads your code?

That's what comments are for.

When the Python interpreter sees a `#` character (shift+3 on your keyboard --- called the pound sign, number sign, or hash character) *that isn't inside quotes*, it ignores everything from that `#` to the end of the line. This lets you leave notes inside your program that the user never sees, but anyone reading the actual code can.

Here's an example:

```python
# here's an example of a comment in Python
x = 2           # here we are setting the variable x to have the value 2
y = x * x       # compute x squared, store the result in y
print(y)         # print the value stored in variable y
```

Comments are your friends. Use them to describe what the program does, how it's supposed to work, who wrote it, when it was last changed, &c. Future You will thank Present You --- trust me on this one.

## The `print()` Function

Output in Python happens through `print()`. You send information inside the parentheses, and Python displays it on the screen. You can send multiple items --- each one is called an *argument*.

Here's an example with multiple arguments:

```python
print('a', 'b', 'c')
```

By default, items are separated by a space. We'll see how to change that in a moment.

The program below shows `print()` in action. Don't worry about `name` and `age` being *variables* --- we'll cover those next! *(You can [download the print_name.py file](https://drive.google.com/file/d/1oFJuNpnaG_kx8E176AT4CW4633FRpjuV/view?usp=drive_link) and run it in your IDE of choice.)*

```python
def main():
    name = 'Dahlia'
    age = 20

    print('Hello,', name, 'you are', age, 'years old!')

main()
```

Did you notice the spacing when the sentence printed? There's no space after the comma inside the string `'Hello,'` --- but a space still appeared between the comma and `Dahlia`. That's how `print()` works by default. It automatically puts a space between each argument. Kind of helpful, kind of annoying --- depending on the situation.

![A call to the print function is passed string literal "hello", name variable, string literal "you are", age variable, string literal "years old!" --- these are called arguments.](images/print_arguments.png)

Notice each argument is separated by a comma. We can change the default separator to any character we want --- even *no* character at all. Try modifying the print statement and adding a 6th argument: `sep=''` like this:

```python
print('Hello,', name, 'you are', age, 'years old!', sep='')
```

Run the program. Your output should have problems now! All the spaces between words are gone. Add extra spaces inside the string literals to fix the spacing.

> **What's a character? What's a string literal?**
>
> We learned in Unit 1 that characters are stored in the computer as ASCII values. A *string literal* (or just *string*) is a series of characters enclosed in either single or double quotes. So `'Hello'` and `"Hello"` are both string literals --- Python doesn't care which kind of quote you use, as long as you're consistent within each string.

## Escape Characters

An escape character is a special character preceded by a backslash (`\`), appearing inside a string literal. When Python prints a string containing escape characters, it treats them as special commands embedded in the string.

For example, `\n` is the **newline** escape character. When `\n` is printed, nothing visible shows up --- instead, the output jumps to the next line. And `\t` is the **tab** escape character, which inserts a nice chunk of horizontal space.

Try this program out --- *(or [download the escape_char.py file](https://drive.google.com/file/d/19I-x9VFY1MwfSk_3Fe9J3VBchfMrYzOp/view?usp=drive_link) and run it in your IDE of choice)*:

```python
def main():
    # \n is the newline escape character
    print('One\nTwo\nThree')

    # \t is the tab escape character
    print('One\t\tTwo\t\tThree')

main()
```

Here's a challenge: where can you add another `\n` escape character to print a blank line between the output of the two print statements, so it looks like this?

```
One
Two
Three

One		Two		Three
```

Try it and see!

## Check for Understanding

[LMS Activity: Unit 3 Lesson 4 Quiz]
