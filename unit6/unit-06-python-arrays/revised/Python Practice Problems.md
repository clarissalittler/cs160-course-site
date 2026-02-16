# Python Practice Problems

For each of the problems below, write out the steps of your algorithm *first* --- as comments in your file --- and *then* translate those steps into code. You can check yourself against the solutions below!

> **Important!** Learning to code can be frustrating and confusing. Like anything new you're trying to learn --- golf, cooking, karate, piano, &c. --- it takes a lot of time and practice. Be patient with yourself and slow down. You can't speed through this learning process; there are no shortcuts! Take the time to plan out your programs *before* you start coding.

## Question #1

**Design a program** that lets the user enter the total number of hours slept each night for one week (7 days). The program should calculate and display the total hours slept and the average hours slept.

**Solution:**

```python
def main():
    hours_slept = []
    total = 0
    average = 0

    print("Enter your sleep hours for a week!\n")

    for index in range(7):
        prompt = "How many hours did you sleep on day # " + str(index + 1) + ": "
        hours_slept.append(float(input(prompt)))

    for index in range(7):
        total = total + hours_slept[index]
    print("\nYou slept", total, "hours this week.")

    average = total / 7
    print("That is", format(average, ".2f"), "hours a night on average.")

main()
```

Notice how we use a `for` loop with `range(7)` to collect exactly 7 nights of data, then a second loop to add them all up. Clean and straightforward.

## Question #2

**Modify Question #1** to find the maximum and minimum hours slept during the week.

Write code to find the max and min hours slept *after* reading all 7 days of data. Here's the key trick --- when you're searching for the max and min in an array, don't initialize them to zero. Initialize them to the *first element* of the array:

```python
min = hours_slept[0]
```

Why? Because if everyone slept positive hours, initializing `max` to 0 would still work. But what if you had a dataset where all values were negative? (Okay, negative sleep doesn't make much sense here, but the principle matters for other programs.) Starting from cell 0 means your initial value is always a *real* data point, which keeps things correct no matter what the data looks like.
