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
def square(side_length):
    print(side_length * 4)

square(7)
```
- A) `side_length`
- B) `square`
- C) `7`
- D) `print`

**3.** A function calculates a number that the rest of the program must store and use in another calculation. Which statement should the function normally use?
- A) `input`
- B) `print`
- C) `return`
- D) `range`

**4.** Which expression asks whether `count` is equal to 10?
- A) `count = 10`
- B) `count == 10`
- C) `count =< 10`
- D) `count != 10`

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

**6.** How many times does this loop print a number?
```python
count = 3
while count > 0:
    print(count)
    count = count - 1
```
- A) 0 times
- B) 3 times
- C) 4 times
- D) It never stops

### True / False

**7.** The condition `grade < 0 or grade > 100` is true for a grade that is outside the range from 0 through 100.

**8.** A `while` loop is guaranteed to stop as long as its body contains at least one assignment statement.

### Short Answer

**9.** What does this program print? Explain how the returned value controls the branch.
```python
def is_even(number):
    return number % 2 == 0

value = 9
if is_even(value):
    print("even")
else:
    print("odd")
```

**10.** The intended rule is “keep asking until the user types yes or no.” Explain why the condition below never becomes false, then write a corrected condition.
```python
while reply != "yes" or reply != "no":
    reply = input("Type yes or no: ").strip().lower()
```
