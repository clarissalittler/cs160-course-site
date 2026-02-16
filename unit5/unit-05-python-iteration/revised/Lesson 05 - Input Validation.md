# Lesson 5 --- Input Validation

> **What you'll be able to do after this lesson:**
>
> - Make your programs more robust by adding input validation.

## Textbook Reading

- Read through [Section 8.8.1, Other uses of while loop](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/SentinelValuesAndValidation.html) from the Runestone Academy textbook. This section covers sentinel values and how they're used to end a loop.
- [Section 8.8.2, Validating Input](https://runestone.academy/runestone/books/published/thinkcspy/MoreAboutIteration/SentinelValuesAndValidation.html) talks about how to make sure the user has entered valid input.
- You don't need to be experts here, but watching the video and writing some simple programs in the workspace provided will definitely help.

## Garbage In, Garbage Out

There's a classic saying in computer science: **garbage in, garbage out**. If your program reads in bad data, it's going to produce bad results. That's just math.

So we need to design our programs to accept only *good* data. The idea is simple --- inspect all input before you process it. If something's invalid, reject it and prompt the user to try again. This approach is called **defensive programming**, and it's all about anticipating errors --- both the obvious ones and the sneaky ones you wouldn't think of at first.

## Types of Errors

Here are the kinds of problems you should be thinking about when you design your programs:

- **Invalid string input** --- You ask for "yes" or "no" and the user types "cat." Thanks, user.
- **Unreasonable values** --- Someone enters -5 or 250 when you ask for their age. Unless they're a time traveler or a vampire, that's not valid.
- **Empty input** --- The user doesn't enter any values at all, and then your program tries to calculate an average and divides by zero. Boom.

## Lesson Video

[Video: Input Validation](https://www.youtube.com/watch?v=5EAQ6-JFk0s)

## String Validation

Run the program below. *(You can copy or download [string.py](https://drive.google.com/file/d/1YJ4pOoFh9MkFBYYUCSvTKKPFtVgabPCn/view?usp=drive_link) and run it in your IDE of choice.)*

What are the user input problems with this program? One of the big ones: if the user enters "Yes" (with a capital Y), it doesn't work as intended! We'd have to compare against every possible capitalization --- YES, yes, YEs, &c. --- and that's a nightmare.

```python
def main():
    response = ""

    response = input("Do you like coding? (yes/no): ")

    if response == 'yes':
        print("Yay!")
    else:
        print("Oh no!")

    print("\nGoodbye!")

main()
```

The fix? Use `lower()` or `upper()` to convert the string to a single case before comparing. Modify the code above to accept all versions of "yes":

```python
if response.lower() == 'yes':  # add the . between the variable and lower()
    print("Yay!")
else:
    print("Oh no!")
```

Using `lower()` and `upper()` is great for handling case, but what happens if the user enters "cat"? If they type something other than "yes" or "no," we want to give them an error message and keep asking until they finally enter valid input. That's what a **validation loop** does --- it keeps prompting until the input is acceptable.

Run the program below for an example. *(Copy or download [string_case.py](https://drive.google.com/file/d/1ojsWTNktFBNj2MSBXqnNk3hepnz9KXsA/view?usp=drive_link) and run it in your IDE of choice.)*

```python
def main():
    response = ""

    response = input("Do you like coding? (yes/no): ")
    # Loop while their response is not 'yes' AND is not 'no'.
    # When user enters 'yes' or 'no' one of the conditions will
    # be false, so the AND will be false and the loop will exit
    while response.lower() != 'yes' and response.lower() != 'no':
        print("Invalid response!")
        response = input("\nDo you like coding? (yes/no): ")

    # When we get here - we are guaranteed to have 'yes' or 'no' !!
    if response.lower() == 'yes':
        print("Yay!")
    else:  # if it is not 'yes', it has to be 'no', since we validated
           # the user input
        print("Oh no!")

    print("\nGoodbye!")

main()
```

Notice the logic in that `while` condition --- it keeps looping while the response is not "yes" **and** not "no." The moment the user enters either valid option, one of those conditions becomes false, the whole `and` expression becomes false, and we break out of the loop. When we reach the `if` statement afterward, we're *guaranteed* to have valid input. That's a nice feeling.

## Unreasonable Input

Another potential problem is unreasonable input. Say you're writing a program that asks for the user's age. You probably don't want to accept -7 or 942. A reasonable range might be 0 to 120, inclusive. If they enter anything outside that range, give them an error and prompt again before continuing.

## Empty Input

Here's a sneaky one. What happens when you run a program that asks for a list of numbers and then calculates the average, but the user doesn't enter any values at all?

Run the program below *(copy or download [empty_input.py](https://drive.google.com/file/d/1cbsx4pUCa_YBRtR8dcCUqKAT7fNe0ac7/view?usp=drive_link) and run it in your IDE of choice)* and provide 0 as the first input. What happens?

```python
def main():
    num = -1
    sum = 0
    count = 0

    while num != 0:
        num = int(input("Enter integer (0 to quit): "))
        sum = sum + num
        if num != 0:
            count = count + 1

    print("\nSum is:", sum)
    print("Average is:", sum / count)

main()
```

If `count` is still 0 when we try to divide, Python throws a `ZeroDivisionError`. Not great. You can avoid this by adding an `if/else` statement to check whether `count` is greater than 0 before attempting the division --- meaning the user actually entered some values to average.
