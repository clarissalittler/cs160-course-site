# Lesson 6 --- More Parallel Arrays/Lists

> **By the end of this lesson, you'll be able to:**
>
> - Use parallel lists to hold related information of different data types.

## Parallel Lists

Last lesson we had two parallel lists --- names and scores. But there's no reason we have to stop at two. Real-world data often needs *three or more* lists working together.

Think about a shopping receipt. Each item has a **name** (string), a **quantity** (int), and a **unit price** (float). That's three different data types, so we need three parallel lists. The elements at index 0 in each list all describe the first item, index 1 describes the second item, &c.

![3 parallel lists related by index number. First list is 'item' with elements 0-3 'bread', 'apples', 'cookies', 'asparagus'. List 2 is quantity, how many of each item with indexes 0-3: 1, 5, 12, 1, and the 3rd list is 'unit cost', with the cost of each item with indexes 0-3: 4.32, .56, .25, 3.45.](images/parallel_arrays.png)

*Figure 6.4. Parallel lists use different lists for related information.*

In the figure above, the shopper is buying 12 cookies at $0.25 each. The elements at index 2 in each list tie that information together.

## Your Turn --- The Shopping Program

Here's a partially-written shopping program. You can also [download shopping.py](https://drive.google.com/file/d/17Ni5PAkInZIsekEkLRWM7a2xu2XEhgDO/view?usp=drive_link) and run it in your IDE.

Your job: **add the statements to prompt for the item name, quantity, and cost, then append them to the appropriate lists.** Look for the comments on line 22 telling you where to add your code.

A couple things to think about:

- What counts as a valid quantity? Probably not a negative number.
- What counts as a valid cost? Same deal --- add some data validation so the user can't enter negative numbers.

The lists start out empty:

```python
items = []
costs = []
quantities = []
```

Here's what the finished output looks like (note: depending on how long your item names are, the spacing might look a bit different from this):

![shopping receipt with items and totals](images/receipt.png)

And here's the code --- fill in the missing parts:

```python
#This program is yet another example of parallel lists
#Very similar to the students program from last lesson
#you get to add some parts of the code for practice
def main():
  #declare variables
  items = []
  costs = []
  quantities = []
  shop = 'y'
  item = ""
  cost = 0.0
  quantity = 0
  length = 0
  total = 0

  #welcome message
  print("Welcome to PCC Market!\n")
  print("Let's shop!\n")

  #while loop to add items
  while shop == 'y':
    # add the statements to prompt for item, cost and
    # quantity

    # add the statements to add item, cost and quantity
    # to the appropriate arrays

    #ask if they want to add more items.
    shop = input("Do you want to add more items? (y/n): ")
    while shop.lower() != 'y' and shop.lower() != 'n':
        print("Invalid. Enter 'y' or 'n'.")
        shop = input("Do you want to add more items? (y/n): ")
    print()
  #end while loop here
  #calculate total cost of items and print the cost
  length = len(items)  #get the length of the list
  print("\n-----------------------------------------")
  print("Receipt:\n")
  print("Item\t\tCost\t\tQty\t\tItem Total")

  for index in range(length):
    print(items[index],"\t\t", "$", format(costs[index], ".2f"), "\t", quantities[index], " \t$", format(costs[index] * quantities[index], ".2f"))
    total = total + costs[index] * quantities[index]
  print("-----------------------------------------")
  print ("Total $ ", format(total, ".2f"))

main()
```

This program follows the exact same pattern as the student database from Lesson 5 --- it's just got one more parallel list. The structure is the same: loop to gather data, then loop again to display it all and compute a total. Once you've seen this pattern, you can extend it to as many parallel lists as you need.
