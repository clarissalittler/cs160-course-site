# Python Practice Problems

For each problem below, start by writing out the steps of your algorithm as comments in your file *before* you write any real code. Then write your program and check yourself against the solutions.

> **Important!** Learning to code can be frustrating and confusing. Like anything new you're trying to learn --- golf, cooking, karate, piano, &c. --- it takes a lot of time and practice. Be patient with yourself and slow down. You can't speed through this learning process; there are no shortcuts! Take the time to plan out your programs *before* you start coding.

## Question #1 --- Restaurant Picker (with video walkthrough)

***Watch the video below to walk through the algorithm and Python code for this problem.***

You've got a group of friends coming to visit Portland, and you want to take them out to eat at a local restaurant. You're not sure if any of them have dietary restrictions, but here are your restaurant choices:

- **Screen Door** --- Vegetarian: No, Vegan: No, Gluten-Free: No
- **Grassa** --- Vegetarian: Yes, Vegan: No, Gluten-Free: Yes
- **Oven and Shaker** --- Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes
- **Verde Cocina** --- Vegetarian: Yes, Vegan: No, Gluten-Free: No
- **Bamboo Sushi** --- Vegetarian: Yes, Vegan: Yes, Gluten-Free: Yes

Write a program that asks whether any members of your party are vegetarian, vegan, or gluten-free, and then displays only the restaurants where you can take the group.

[Video: Question #1 Walkthrough](https://www.youtube.com/watch?v=KPFyFOIsM70)

**Solution:**

```python
def main():
    # Get dietary restrictions
    print("Is anyone in your party...")
    vegetarian = input("Vegetarian? (yes/no): ").lower()
    vegan = input("Vegan? (yes/no): ").lower()
    gluten_free = input("Gluten-free? (yes/no): ").lower()

    # Print header for results
    print("\nHere are your restaurant choices:")

    # Screen Door - no dietary accommodations
    if (vegetarian == "no" and
        vegan == "no" and
        gluten_free == "no"):
        print("Screen Door")

    # Grassa - accommodates vegetarian and gluten-free
    if (vegan == "no"):
        print("Grassa")

    # Oven and Shaker - accommodates all restrictions
    print("Oven and Shaker")

    # Verde Cocina - accommodates vegetarian only
    if (vegan == "no" and
        gluten_free == "no"):
        print("Verde Cocina")

    # Bamboo Sushi - accommodates all restrictions
    print("Bamboo Sushi")

main()
```

## Question #2 --- Day of the Week

Write a program that asks the user for a number in the range of 1 through 7. The program should display the corresponding day of the week, where 1 = Monday, 2 = Tuesday, 3 = Wednesday, 4 = Thursday, 5 = Friday, 6 = Saturday, and 7 = Sunday. If the user enters a number outside that range, display an error message.

This is a classic `if-elif-else` problem --- each number maps to exactly one day, and anything else is invalid.

**Solution:**

```python
def main():
    # Get the number from the user
    day_number = int(input("Enter a number (1-7): "))

    # Determine the day
    if day_number == 1:
        print("Monday")
    elif day_number == 2:
        print("Tuesday")
    elif day_number == 3:
        print("Wednesday")
    elif day_number == 4:
        print("Thursday")
    elif day_number == 5:
        print("Friday")
    elif day_number == 6:
        print("Saturday")
    elif day_number == 7:
        print("Sunday")
    else:
        print("Error: Please enter a number between 1 and 7")

main()
```

## Question #3 --- Age Classifier

Write a program that asks the user to enter a person's age. The program should display a message indicating whether the person is an infant, a child, a teenager, or an adult. If the age isn't between 0 and 120, give an error message. Here are the guidelines:

- If the person is 1 year old or less, they're an **infant**.
- If the person is older than 1 but younger than 13, they're a **child**.
- If the person is at least 13 but less than 20, they're a **teenager**.
- If the person is 20 or older, they're an **adult**.

Notice how we validate the input *first* --- that way, we don't waste time classifying a nonsensical age like -5 or 200.

**Solution:**

```python
def main():
    # Get the age
    age = float(input("Enter the person's age: "))

    # Check if age is in valid range first
    if age < 0 or age > 120:
        print("Error: Age must be between 0 and 120")
    # Then check each age category
    elif age <= 1:
        print("This person is an infant")
    elif age < 13:
        print("This person is a child")
    elif age < 20:
        print("This person is a teenager")
    else:
        print("This person is an adult")

main()
```

## Question #4 --- Leap Year Calculator

The month of February normally has 28 days. But if it's a leap year, February has 29 days. Write a program that asks the user to enter a year, then displays the number of days in February that year.

The leap year rules are a little quirky --- here's how they work:

- First, check whether the year is divisible by 100. If it is, then it's a leap year *only if* it's also divisible by 400. For example, 2000 is a leap year, but 2100 is not.
- If the year is *not* divisible by 100, then it's a leap year if it's divisible by 4. For example, 2008 is a leap year, but 2009 is not.

Why is it so convoluted? Blame the Earth --- it doesn't orbit the sun in exactly 365 days, so we need these corrections to keep our calendars from drifting. The 400-year rule was introduced by Pope Gregory XIII in 1582, which is why we call it the Gregorian calendar.

**Solution:**

```python
def main():
    # Get the year from the user
    year = int(input("Enter a year: "))

    # Check if it's a leap year using the given rules
    if year % 100 == 0:
        # Year is divisible by 100
        if year % 400 == 0:
            print("In", year, "February has 29 days (leap year)")
        else:
            print("In", year, "February has 28 days")
    else:
        # Year is not divisible by 100
        if year % 4 == 0:
            print("In", year, "February has 29 days (leap year)")
        else:
            print("In", year, "February has 28 days")

main()
```
