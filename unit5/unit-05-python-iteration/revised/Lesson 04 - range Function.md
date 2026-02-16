# Lesson 4 --- range() Function

![Unit 5 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Use the `range()` function to generate a sequence of numbers to use with the `for` loop.

---

## Textbook reading

Read through [Section 4.7, The range function](https://runestone.academy/runestone/books/published/thinkcspy/PythonTurtle/TherangeFunction.html) in the Runestone Academy textbook. This section covers the `range()` function and how it works with `for` loops. You don't need to be an expert on this yet --- but watching the video and writing some simple programs in the workspace will definitely help.

## The `range()` function

In the last lesson, we wrote `for` loops with lists like `[0, 1, 2, 3, 4]`. That works fine for small lists, but what if you need to loop 1,000 times? You're not going to type out a list with 1,000 numbers in it. (Well, you *could*, but... no.)

That's where `range()` comes in. Instead of writing the list of values ourselves, we let `range()` generate them for us. And it turns out `for` loops can do more than just count up by one --- they can:

- Increment by more than one
- Count *backward* by decrementing
- Let the user control the number of iterations

You can pass 1, 2, or 3 arguments to `range()`. Let's look at each.

### 1 argument

```python
for num in range(5):    # generates: 0, 1, 2, 3, 4
    print(num)
```

This is equivalent to:

```python
for num in [0, 1, 2, 3, 4]:
    print(num)
```

Notice it starts at 0 and gives you 5 values. Not 1 through 5 --- it's 0 through 4. This is honestly kind of annoying when you first encounter it, but it's consistent with how Python (and most programming languages) count things. You'll get used to it.

### 2 arguments

```python
for num in range(start_value, stop_value):
    print(num)    # all numbers from start_value to one less than stop_value
```

Run this program. *(Copy or download [for_loop_1.py](https://drive.google.com/file/d/1FxBEBCTEw3KBuIIrxBJoE_FFrOfIXaYH/view?usp=drive_link) and run in your IDE of choice.)* Try other integers as arguments. Try negative values. Try values where the first argument is greater than the second. What happens?

```python
def main():
    for index in range(2, 10):
        print(index)

main()
```

> **Bug Alert:**
>
> Remember, `for num in range(2, 10)` generates the sequence 2, 3, 4, 5, 6, 7, 8, 9 --- it does **NOT** include 10! The stop value is always excluded. This trips people up constantly, and honestly it never stops being a little weird. Just remember: the stop value is the number you stop *before*.

### 3 arguments

```python
for num in range(start_value, stop_value, step_value):
    print(num)    # starts at start_value, adds step_value each iteration,
                  # stops before reaching stop_value
```

The third argument is the **step** --- how much to add (or subtract!) each time. This is where things get fun.

Run this program. *(Copy or download [for_loop_2.py](https://drive.google.com/file/d/1YGPL6_dSU81Pces1PPl_09Pa-zF4HFKw/view?usp=drive_link) and run in your IDE of choice.)* Try other integers as arguments. Can you step backward from 10 to 1?

```python
def main():
    # step up by 2
    for index in range(2, 10, 2):
        print(index)

    print()

    # step down by 1
    for index in range(10, 1, -1):
        print(index)

main()
```

That negative step value is the key to counting backwards. `range(10, 1, -1)` gives you 10, 9, 8, 7, 6, 5, 4, 3, 2 --- like a countdown. And yes, it still excludes the stop value, so you get down to 2 but not 1. Consistent? Yes. Intuitive? Debatable.

## Discussion prompt

At one college, the tuition for a full-time student is $8,000 per semester. It's been announced that tuition will increase by 3 percent each year for the next 5 years. Write a program with a loop that displays the projected semester tuition amount for the next 5 years.

Use a top-down design --- start with a sample run of the output. Next, plan out and identify the variables (data) you'll need. Write the steps of your logic (algorithm). Then write the Python code. Run and test!

> **Complete on your own!**
>
> Open [LMS Activity: Unit 5 Lesson 4 - Tuition Program discussion] and:
>
> - Post your code.
> - You must post before you can see other student posts.
> - You must review and give feedback to 2 other students. A peer review should include:
>   - Suggestions for improvement.
>   - Kudos for clever code or enhancements.
>   - Remember to always comment using generosity and respect.
>
> You may also work with someone from your study group or post to this topic asking to work on the program with someone from class! Collaboration during programming practice is encouraged.
