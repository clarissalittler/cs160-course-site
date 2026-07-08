## Unit 4 Quiz — Decisions and Loops

### Multiple Choice

**1.** A program that runs straight down the page, one line after the next, with no choices, is using which kind of structure?
- A) A selection structure
- B) A sequential structure
- C) A conditional expression
- D) A logical operator

**2.** You want to ask the program "is the variable `count` equal to 10?" Which line does that correctly?
- A) `if count = 10:`
- B) `if count == 10:`
- C) `if count =< 10:`
- D) `if count != 10:`

**3.** What does this program print?
```python
temp = 55
if temp < 32:
    print("Freezing")
elif temp < 60:
    print("Chilly")
elif temp < 80:
    print("Nice")
else:
    print("Hot")
```
- A) Freezing
- B) Chilly
- C) Nice
- D) Hot

**4.** How many times does this loop print something?
```python
n = 3
while n > 0:
    print(n)
    n = n - 1
```
- A) 0 times
- B) 3 times
- C) 4 times
- D) It runs forever

**5.** What numbers does `range(1, 10, 2)` generate?
- A) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
- B) 1, 3, 5, 7, 9
- C) 1, 3, 5, 7, 9, 11
- D) 2, 4, 6, 8, 10

**6.** What does this program print?
```python
def is_even(n):
    return n % 2 == 0

number = 9
if is_even(number):
    print("even")
else:
    print("odd")
```
- A) even
- B) odd
- C) True
- D) Nothing prints

### True / False

**7.** In the condition `if grade < 0 or grade > 100:`, the code inside runs whenever the grade is below 0 or above 100.

**8.** The code `range(1, 5)` produces the numbers 1, 2, 3, 4, 5.

### Short Answer

**9.** What does this program print? Walk through the nested decision carefully.
```python
year = 2000
if year % 100 == 0:
    if year % 400 == 0:
        print("29 days (leap year)")
    else:
        print("28 days")
else:
    if year % 4 == 0:
        print("29 days (leap year)")
    else:
        print("28 days")
```

**10.** What does this program print?
```python
total = 0
for x in [5, 3, 8]:
    total = total + x
print(total)
```
