# Python Practice Problems

For each problem below, write the steps of your algorithm as comments in your IDE *first*, then try to solve it before peeking at the solution. Seriously --- the learning happens when you struggle with it, not when you read the answer.

The example video below walks you through this process.

> **A quick pep talk:**
>
> Learning to code can be frustrating and confusing. Like anything new you're trying to learn --- golf, cooking, karate, piano, &c. --- it takes time and practice. Be patient with yourself and slow down. There are no shortcuts here! Take the time to plan out your programs BEFORE you start coding.

## Example Video

**Read the question below first, then start the video. Pause it and duplicate the work in your IDE for practice.**

**Question #1:** A company has determined that its annual profit is typically 27 percent of total sales. Write a program that asks the user to enter the projected amount of total sales, then displays the profit that will be made from that amount.

[Video: Question #1 Walkthrough](https://www.youtube.com/watch?v=6GKAw2spy3U)

Solution:

```python
PROFIT_MARGIN = 0.27

def main():
    total_sales = float(input("Enter the projected amount of total sales: $"))
    profit = total_sales * PROFIT_MARGIN
    print("The profit will be: ${:,.2f}".format(profit))

main()
```

> **Should your code look exactly like the solutions below?** ABSOLUTELY NOT! Coding is creative, and everyone thinks about solving problems differently. Think about how *you* would solve it, then check the solution for another approach. They should be similar, but you're the programmer --- you get to decide how to format what the user sees!

## Question #2

A customer at Target in Vancouver, WA is purchasing five items. Write a program that asks for the price of each item, then displays the subtotal of the sale, the amount of sales tax, and the total. Vancouver, WA sales tax is 8.4 percent. Hint: use `.084` for 8.4%.

Solution:

```python
TAX_RATE = 0.084

def main():
    # Get prices for all five items
    item1 = float(input("Enter price of item 1: $"))
    item2 = float(input("Enter price of item 2: $"))
    item3 = float(input("Enter price of item 3: $"))
    item4 = float(input("Enter price of item 4: $"))
    item5 = float(input("Enter price of item 5: $"))

    # Calculate subtotal
    subtotal = item1 + item2 + item3 + item4 + item5

    # Calculate tax and total
    tax = subtotal * TAX_RATE
    total = subtotal + tax

    # Display results
    print("Subtotal: ${:,.2f}".format(subtotal))
    print("Sales Tax: ${:,.2f}".format(tax))
    print("Total: ${:,.2f}".format(total))

main()
```

## Question #3

Write a program that calculates the total amount of a meal purchased at PDX Sliders. The program should ask the user to enter the charge for the food, then calculate the amounts of an 18 percent tip and 7 percent sales tax. Display each of these amounts and the total.

Solution:

```python
TIP_RATE = 0.18
TAX_RATE = 0.07

def main():
    # Get the food charge
    food_charge = float(input("Enter the charge for the food: $"))

    # Calculate tip and tax
    tip = food_charge * TIP_RATE
    tax = food_charge * TAX_RATE
    total = food_charge + tip + tax

    # Display all amounts
    print("Food Charge: ${:,.2f}".format(food_charge))
    print("Tip (18%): ${:,.2f}".format(tip))
    print("Sales Tax (7%): ${:,.2f}".format(tax))
    print("Total: ${:,.2f}".format(total))

main()
```

## Question #4

A cupcake recipe calls for the following ingredients:

- 1.5 cups of sugar
- 1 cup of butter
- 2.75 cups of flour

The recipe produces 12 cupcakes with these amounts. Write a program that asks the user how many cupcakes they want to make, then displays the number of cups of each ingredient needed for that quantity.

Solution:

```python
# Original recipe amounts for 12 cupcakes
SUGAR_FOR_12 = 1.5
BUTTER_FOR_12 = 1.0
FLOUR_FOR_12 = 2.75
RECIPE_SIZE = 12

def main():
    # Get desired number of cupcakes
    desired_cupcakes = float(input("How many cupcakes do you want to make? "))

    # Calculate scaling factor
    scaling_factor = desired_cupcakes / RECIPE_SIZE

    # Calculate needed ingredients
    sugar_needed = SUGAR_FOR_12 * scaling_factor
    butter_needed = BUTTER_FOR_12 * scaling_factor
    flour_needed = FLOUR_FOR_12 * scaling_factor

    # Display the required amounts
    print("To make {} cupcakes, you need:".format(desired_cupcakes))
    print("{:,.2f} cups of sugar".format(sugar_needed))
    print("{:,.2f} cups of butter".format(butter_needed))
    print("{:,.2f} cups of flour".format(flour_needed))

main()
```
