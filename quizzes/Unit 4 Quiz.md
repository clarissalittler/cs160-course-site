## Unit 4 Quiz — Making Decisions: Booleans, Conditionals, and Logic

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

**4.** A food cart gives a discount only to customers who are students **and** are buying before noon. Which condition matches that rule?
- A) `if is_student or before_noon:`
- B) `if is_student and before_noon:`
- C) `if not is_student and before_noon:`
- D) `if is_student == before_noon:`

**5.** In Python, the `else` at the end of an `if-elif-else` chain runs when…
- A) every condition above it was true
- B) the first condition was true
- C) none of the conditions above it were true
- D) exactly two conditions above it were true

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

**8.** Writing `if x or y or z == 2:` correctly checks whether any one of the variables `x`, `y`, or `z` is equal to 2.

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

**10.** In one sentence, explain the difference between `=` and `==` in Python.
