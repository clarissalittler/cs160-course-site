# Python Practice Problems

For each of the problems below, write out the steps of your algorithm first --- as comments in your file --- and *then* translate those steps into code. You can check yourself against the solutions!

> **Important!** Learning to code can be frustrating and confusing. Like anything new you're trying to learn --- golf, cooking, karate, piano, &c. --- it takes a lot of time and practice. Be patient with yourself and slow down. You can't speed through this learning process; there are no shortcuts! Take the time to plan out your programs *before* you start coding.

## Question #1

Write a program that calculates the amount of money a person would earn over a period of time if their salary starts at one penny on the first day, two pennies on the second day, and continues to double each day. The program should ask the user for the number of days. Display a table showing what the salary was for each day, then show the total pay at the end of the period. The output should be displayed in dollars, not pennies.

This is the classic "would you rather have a million dollars or a penny that doubles every day?" question --- and the answer might surprise you. A penny doubled for 30 days is over *ten million dollars*. Exponential growth is wild.

<details>
<summary>Solution</summary>

```python
def main():
    # Get number of days from user
    days = int(input("Enter the number of days: "))

    # Initialize variables
    total_pay = 0
    daily_pay = 0.01  # Starting with one penny

    # Print table header
    print("\nDay\t\tDaily Pay\t\tTotal Pay")
    print("-" * 45)

    # Calculate and display daily and total pay
    for day in range(1, days + 1):
        total_pay += daily_pay

        # Print daily values formatted as dollars using .format()
        print("{}\t\t${:,.2f}\t\t${:,.2f}".format(day, daily_pay, total_pay))

        # Double the pay for next day
        daily_pay *= 2

    # Print final total
    print("\nTotal pay for {} days: ${:,.2f}".format(days, total_pay))

main()
```

</details>

## Question #2

A rock collector collects rocks every day for five days. Write a program that keeps a running total of the number of rocks collected during the five days. The loop should ask for the number of rocks collected each day, and when the loop is finished, the program should display the total number of rocks collected.

*(Hint: You know you'll loop exactly 5 times, so use a `for` loop.)*

<details>
<summary>Solution</summary>

```python
def main():
    # Initialize total
    total_rocks = 0

    # Loop 5 times to get rocks for each day
    for day in range(1, 6):
        rocks = int(input("Enter number of rocks collected on day {}: ".format(day)))
        total_rocks += rocks

    # Display final total
    print("\nTotal rocks collected: {}".format(total_rocks))

main()
```

</details>

## Question #3

Write a program with a loop that asks the user to enter a series of positive numbers. The user should enter a negative number to signal the end of the series. After all the positive numbers have been entered, the program should display their sum. Don't add the negative number to the sum!

*(Hint: You don't know how many numbers the user will enter, so use a `while` loop.)*

That negative number at the end is called a **sentinel value** --- it's not real data, it's just a signal that says "I'm done." We talked about those earlier in the unit.

<details>
<summary>Solution</summary>

```python
def main():
    # Initialize total
    total = 0

    # Get first number from user
    number = float(input("Enter a positive number (negative to quit): "))

    # Continue loop while number is positive
    while number >= 0:
        total += number
        number = float(input("Enter a positive number (negative to quit): "))

    # Display sum after negative number is entered
    print("\nSum of all positive numbers: {:.2f}".format(total))

main()
```

</details>

## Question #4

In mathematics, the notation **n!** represents the **factorial** of the nonnegative integer n. The factorial of n is the product of all the nonnegative integers from 1 to n. For example:

- 4! = 4 * 3 * 2 * 1 = 24
- 8! = 8 * 7 * 6 * 5 * 4 * 3 * 2 * 1 = 40,320
- 1! = 1

Factorials get big *fast*. 20! is already 2,432,902,008,176,640,000. That's over 2 quintillion. Good luck fitting that on a calculator.

Write a program that lets the user enter an integer greater than 0 and then uses a loop to calculate the factorial of that number. Display the factorial. If the user enters an integer less than or equal to 0, print an error and end the program.

<details>
<summary>Solution</summary>

```python
def main():
    # Get number from user
    num = int(input("Enter a positive integer to calculate its factorial: "))

    # Check if number is valid
    if num <= 0:
        print("Error: Please enter a number greater than 0")
        return

    # Calculate factorial
    factorial = 1
    for i in range(num, 0, -1):
        factorial *= i

    # Display result
    print("{}! = {}".format(num, factorial))

main()
```

</details>
