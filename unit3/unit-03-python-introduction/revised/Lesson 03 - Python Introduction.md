# Lesson 3 --- Python Introduction

![Unit 3 banner](img/banner.jpg)

> **After this lesson, you'll be able to:**
>
> - Write your first Python program: "Hello World."

## Textbook resource

Read through [Chapter 1, General Introduction to the Python Programming Language](https://runestone.academy/runestone/books/published/thinkcspy/GeneralIntro/ThePythonProgrammingLanguage.html) from Runestone Academy. You don't need to become an expert on every section --- just read through it, try the activities, and watch the videos. The goal is to get a general understanding of what a programming language is and what the Python programs we'll be writing look like. There are self-check questions built in to test your understanding. If something doesn't click right away, don't stress --- you can always come back to it later.

## Hello World!

There's a tradition in programming that goes back decades: the very first program you write in any new language should just print the words "Hello, World!" to the screen. It's kind of like a rite of passage. The tradition dates all the way back to a 1978 book about the C programming language, and it stuck because it's the simplest possible proof that your setup is working and you can actually make the computer do something.

Let's try it. Copy the code below (or download the [hello.py file](https://drive.google.com/file/d/15tYG9RToucpVx7wXh9Ag_H-xZ8BNfxyD/view?usp=drive_link)) and run it in your IDE of choice:

```python
def main():
  print('Hello, CS160!!')

main()
```

Did it work? You should see `Hello, CS160!!` appear in your console window.

Now try changing the message --- put something different inside those single quotes and run it again. Maybe `'I am a programmer now'` or `'Computers fear me'`. Whatever makes you smile. You've just written your first program --- congratulations!

## Python rules (yes, there are rules)

Python is picky. *Really* picky. Spacing and indentation aren't just cosmetic --- they actually matter to the language. We'll get into all the details over the upcoming lessons, but for now, here's what you need to know about the structure of your programs.

Every program you write will start with this line at the top:

```python
def main():
```

This line must have **no indentation** --- it sits all the way at the left edge. And at the very bottom of your program, you'll have:

```python
main()
```

Also **not indented**. Everything *between* these two lines --- the actual stuff your program does --- gets indented. That indentation is how Python knows which code belongs inside `main()`.

Okay, that's kind of strange, right? In most writing, indentation is just about looking nice. In Python, it's part of the language's grammar. Forget to indent, or indent when you shouldn't, and Python will yell at you with an error message. It's one of the most common frustrations for people learning to code, so don't feel bad if it trips you up.

> **A word of encouragement:** Learning to code can feel difficult and confusing at first --- and that's completely normal. You're learning to speak a new language with a lot of rules. Remember when you learned how to drive? You had to think about *everything* --- adjust the mirrors, foot on the brake, key in the ignition, car in drive, press the gas (but not too hard!), check the mirrors again, &c. But with practice, you got to the point where you just hop in and go without thinking about it. Coding is exactly the same way. Right now every little thing feels like a lot. Give it time.
