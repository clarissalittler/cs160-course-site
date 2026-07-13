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
points *= 2
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

**5.** What is the value of `17 % 5`?
- A) 2
- B) 3
- C) 3.4
- D) 5

**6.** Which values does `range(1, 6)` provide to a loop?
- A) 0, 1, 2, 3, 4, 5
- B) 1, 2, 3, 4, 5
- C) 1, 2, 3, 4, 5, 6
- D) 0, 1, 2, 3, 4, 5, 6

### True / False

**7.** In `total = 0`, the assignment operator stores the value on the right under the name on the left.

**8.** Formatting a value with `f"${price:.2f}"` changes the number stored in `price` so it permanently has exactly two decimal places.

### Short Answer

**9.** What does this program print?
```python
cookies = 17
kids = 5
print(f"Each kid gets {cookies // kids} cookies.")
print(f"There are {cookies % kids} left over.")
```

**10.** Predict every line of output and the final value of `total`:
```python
total = 0
for number in range(1, 4):
    total = total + number
    print(f"After {number}: {total}")
print(f"Final: {total}")
```
