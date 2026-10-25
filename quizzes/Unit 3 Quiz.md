## Unit 3 Quiz — Introduction to Programming

### Multiple Choice

**1.** A plain-language, step-by-step plan written before the exact Python syntax is called:
- A) source code
- B) pseudocode
- C) a traceback
- D) an f-string

**2.** After this code runs, what value is stored in `points`?
```python
points = 10
points = points + 5
points = points * 2
```
- A) 10
- B) 15
- C) 25
- D) 30

**3.** The user types `25` in response to this line. What type of value is stored in `age`?
```python
age = input("How old are you? ")
```
- A) `int`
- B) `float`
- C) `str`
- D) No value is stored

**4.** Which line correctly reads a price that may contain a decimal and stores it as a number?
- A) `price = input("Price: $")`
- B) `price = int(input("Price: $"))`
- C) `price = float(input("Price: $"))`
- D) `float = input("Price: $")`

**5.** A program stops with this traceback. What's the most useful conclusion?
```
Traceback (most recent call last):
  File "program.py", line 4, in <module>
    print(f"Total pages: {totl_pages}")
NameError: name 'totl_pages' is not defined
```
- A) Line 4 uses a name Python has never heard of, probably a misspelling of a variable name
- B) The user typed a word instead of a number, so the conversion with `int()` failed
- C) The program is missing a quotation mark or a parenthesis somewhere
- D) The f-string tried to add a string and a number together

**6.** This program runs without any error message:
```python
hours = 2.5
minutes = hours + 60
print(f"{hours} hours is {minutes} minutes.")
```
What's the best way to catch the problem with it?
- A) Read the last line of the traceback
- B) There's no problem; if Python doesn't complain, the answer is right
- C) Test it with a case where you already know the right answer (2.5 hours should be 150 minutes) and compare
- D) Change `hours` to a whole number so the math comes out even

### True / False

**7.** In `total = 0`, the assignment operator stores the value on the right under the name on the left.

**8.** Formatting a value with `f"${price:.2f}"` changes the number stored in `price` so it permanently has exactly two decimal places.

### Multiple Choice (continued)

**9.** What does this program print?
```python
cookies = 17
kids = 5
print(f"Each kid gets {cookies // kids} cookies.")
print(f"There are {cookies % kids} left over.")
```
- A) `Each kid gets 3 cookies.` followed by `There are 2 left over.`
- B) `Each kid gets 3.4 cookies.` followed by `There are 0 left over.`
- C) `Each kid gets 2 cookies.` followed by `There are 3 left over.`
- D) `Each kid gets 5 cookies.` followed by `There are 17 left over.`

**10.** Which sequence contains every line printed by this program, in order?
```python
total = 0
for number in range(1, 4):
    total = total + number
    print(f"After {number}: {total}")
print(f"Final: {total}")
```
- A) `After 1: 1`; `After 2: 2`; `After 3: 3`; `Final: 3`
- B) `After 1: 1`; `After 2: 3`; `After 3: 6`; `Final: 6`
- C) `After 0: 0`; `After 1: 1`; `After 2: 3`; `After 3: 6`; `Final: 6`
- D) `After 1: 1`; `After 2: 3`; `Final: 3`
