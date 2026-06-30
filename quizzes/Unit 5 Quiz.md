## Unit 5 Quiz — Loops, Strings, and Randomness

### Multiple Choice

**1.** How many times does this loop print something?
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

**2.** What numbers does `range(1, 10, 2)` generate?
- A) 1, 2, 3, 4, 5, 6, 7, 8, 9, 10
- B) 1, 3, 5, 7, 9
- C) 1, 3, 5, 7, 9, 11
- D) 2, 4, 6, 8, 10

**3.** Given `word = "Python"`, what does `word[-1]` give you?
- A) `"P"`
- B) `"o"`
- C) `"n"`
- D) An error, because indexes can't be negative

**4.** What does this code print on the last line?
```python
total = 0
for x in [2, 4, 6]:
    total = total + x
print(total)
```
- A) 0
- B) 6
- C) 12
- D) 246

**5.** After running `roll = random.randint(1, 6)`, which value could `roll` **never** be?
- A) 1
- B) 3
- C) 6
- D) 7

**6.** You want to repeat something an exact, known number of times — say, draw 4 sides of a square. Which is the most natural tool?
- A) An `if` statement
- B) A `for` loop with `range()`
- C) A `while True:` loop with no way to stop
- D) The `random` module

### True / False

**7.** In Python, the first character of a string is at index 0.

**8.** The code `range(1, 5)` produces the numbers 1, 2, 3, 4, 5.

### Short Answer

**9.** What does this code print? (Write it exactly as it would appear.)
```python
word = "dog"
for letter in word:
    print(letter.upper())
```

**10.** What does this code print?
```python
city = "Portland"
print(city[0:4])
```
