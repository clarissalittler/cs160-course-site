## Unit 4 Quiz — Functions, Decisions, and Repetition

### Multiple Choice

**1.** This program runs without an error but displays nothing. Why?
```python
def cheer():
    print("Keep debugging!")
```
- A) A function cannot contain `print()`
- B) The function was defined but never called
- C) The message must be stored in a variable first
- D) The function needs a `while` loop

**2.** In the code below, which item is the **argument** supplied by the call?
```python
def print_perimeter(side_length):
    print(side_length * 4)

print_perimeter(7)
```
- A) `side_length`
- B) `print_perimeter`
- C) `7`
- D) `print`

**3.** A function calculates a number that the rest of the program must store and use in another calculation. Which statement should the function normally use?
- A) `input`
- B) `print`
- C) `return`
- D) `range`

**4.** A theater's rule says kids **under 13** get the child price. A programmer writes:
```python
def gets_child_price(age):
    return age <= 13
```
Which single test age would reveal that the code doesn't match the rule?
- A) 6
- B) 12
- C) 20
- D) 13

**5.** What does this code print?
```python
temperature = 55
if temperature < 32:
    print("Freezing")
elif temperature < 60:
    print("Cool")
elif temperature < 80:
    print("Mild")
else:
    print("Hot")
```
- A) Freezing
- B) Cool
- C) Mild
- D) Cool and Mild

**6.** Which task is the best fit for a `while` loop rather than a `for` loop?
- A) Asking for guesses until the player guesses the secret number
- B) Drawing a hexagon with six equal sides
- C) Printing one line for each number from 1 to 10
- D) Repeating a chorus exactly four times

### True / False

**7.** The condition `grade < 0 or grade > 100` is true for a grade that is outside the range from 0 through 100.

**8.** A `while` loop is guaranteed to stop as long as its body contains at least one assignment statement.

### Multiple Choice (continued)

**9.** What does this program print, and why?
```python
def is_even(number):
    return number % 2 == 0

value = 9
if is_even(value):
    print("even")
else:
    print("odd")
```
- A) `even`, because 9 is a whole number
- B) `even`, because `is_even` always returns `True`
- C) `odd`, because `is_even(9)` returns `False` and the `else` branch runs
- D) Nothing, because a returned Boolean cannot control an `if` statement

**10.** The intended rule is “keep asking until the user types yes or no,” but this loop never ends, even when the user types `yes`. Which replacement correctly fixes the loop condition?
```python
reply = input("Type yes or no: ").strip().lower()
while reply != "yes" or reply != "no":
    print("Please type yes or no.")
    reply = input("Type yes or no: ").strip().lower()
```
- A) `while reply != "yes" and reply != "no":`
- B) `while reply == "yes" or reply == "no":`
- C) `while reply != "yes" or "no":`
- D) `while reply == "yes" and reply == "no":`
