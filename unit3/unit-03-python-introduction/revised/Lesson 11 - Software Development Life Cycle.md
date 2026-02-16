# Lesson 11 --- Software Development Life Cycle

> **What you'll be able to do after this lesson:**
>
> - Explain the steps of the software development life cycle.

## Software Development Life Cycle

![software development life cycle is iterative: design, code, test, release](images/sdlc.svg)

As you learned in the last unit, programs need to be *designed* before they're written. You don't just sit down and start typing code --- well, you can, but you'll regret it.

Professional software is typically developed using a process called the **Software Development Life Cycle** (SDLC):

1. **Design** the program algorithm
2. **Code** and correct syntax errors
3. **Test** the program and correct logic errors (this is called *debugging*)
4. **Release** your finished product

This is usually done *iteratively* --- meaning you don't do each step once and call it done. You start with a small, simple version of the program, get it working, and then gradually add more features. Each pass through the cycle makes the software a little more complete.

Think of it less like building a house and more like sculpting --- you rough out the shape first, then refine.

## Design

There are two steps in designing a program:

### 1. Figure out what the user wants

Start with the UX (user experience) so you're designing with the end in mind. We'll call this the **sample run**. Here's one for a simple pay calculator:

```
Welcome to the Pay Program!

Enter the number of hours: 40
Enter the hourly pay rate: $15
The gross pay is $600.00
END.
```

Notice that we've filled in sample input values (40 hours, $15 rate) and calculated the correct answer by hand. This gives us something concrete to test against later. Don't skip this step --- it's surprisingly useful to know *exactly* what your program should look like before you write a single line of code.

### 2. Figure out *how* the program will do it

Now you need to determine the actual steps your program will take. This is where you write an algorithm --- step-by-step directions to solve the problem.

We use **pseudocode** for this. Pseudocode is just fake code --- there are no syntax rules, no compiler yelling at you. It's a way to plan your logic in plain language before worrying about Python's specific syntax. Well-written pseudocode translates almost directly into real code.

Here are some questions to guide your algorithm design:

1. **Identify the user input.** How many different inputs do you need?
2. **What data types** do you need for each input?
3. **What calculations** transform inputs into outputs? List all formulas. (If there are no calculations, say so --- that's fine.)
4. **Describe the process** for transforming inputs to outputs using numbered steps. This is where conditionals, loops, functions, &c. would come in if applicable.
5. **Describe the output.** What variables are needed? What data types? What does the user actually see?

After you've planned everything out, *then* you're ready to code. Planning first saves you time by letting you think through your logic informally, without fighting syntax at the same time.

## Code

This is the fun part. Take your algorithm and translate it into Python --- a language the computer actually understands.

If you make mistakes when typing up your program (misspelled keywords, missing colons, unmatched parentheses, &c.), those are called **syntax errors**. The Python interpreter will complain loudly when you try to run it. Don't panic --- just fix each error and try again. This is completely normal, even for experienced programmers.

## Test

You're not done yet! Now you need to test your program to see if it actually works correctly.

Start by using the sample input data from your sample run. Do the results match? If not, you've got a **logic error** --- the program runs, but it gives the wrong answer. These are sneakier than syntax errors because Python won't flag them for you. You'll need to read through your code carefully to find the mistake. This process is called **debugging**.

A fun bit of history: the term "debugging" dates back to 1947, when a literal moth was found stuck in a relay of the Harvard Mark II computer. Grace Hopper's team taped it into the log book and wrote "First actual case of bug being found." We've been "debugging" ever since.

## Release

Once you've tested your program and squashed all the logic errors, you're ready to release it into the world. Congratulations --- you've made software!

Of course, in real life the cycle often loops back around. Users find new bugs, request new features, and the whole design-code-test-release process starts again. That's the "iterative" part. But for now, enjoy the moment.
