## Unit 3 Quiz — Python: Algorithms, Variables, and Functions

### Multiple Choice

**1.** A friend asks you to plan out a program *before* writing real Python by listing the steps in plain English. What is this plain-English plan called?
- A) Source code
- B) Pseudocode
- C) A comment
- D) An escape sequence

**2.** After these lines run, what value does `points` hold?
```python
points = 10
points = points + 5
points *= 2
```
- A) 10
- B) 15
- C) 30
- D) 25

**3.** A program asks `age = input("How old are you? ")` and the user types `25`. What type of value is now stored in `age`?
- A) An int (whole number)
- B) A float (decimal number)
- C) A str (string of text)
- D) Nothing — input doesn't return a value

**4.** Which expression uses the remainder (modulus) operator to check whether the number in `n` is even?
- A) `n // 2 == 0`
- B) `n % 2 == 0`
- C) `n ** 2 == 0`
- D) `n / 2 == 0`

**5.** You write `def cheer():` with two indented `print` lines underneath, but when you run the file nothing appears on screen. What did you most likely forget?
- A) To put the code inside quotes
- B) To *call* the function by writing `cheer()`
- C) To convert the output with `str()`
- D) To add a comment above it

**6.** In the code below, which value is the **argument** being passed in?
```python
def square(n):
    return n * n

print(square(7))
```
- A) `n`
- B) `square`
- C) `7`
- D) `return`

### True / False

**7.** In Python, the statement `total = 0` means "total is equal to 0" — it is checking whether the two sides are the same.

**8.** A function that uses `print(...)` to show its answer can have that answer stored in a variable and reused later in a calculation, exactly like a function that uses `return`.

### Short Answer

**9.** What does this program print? (Watch the `//` and `%` operators.)
```python
def main():
    cookies = 17
    kids = 5
    print(f"Each kid gets {cookies // kids} cookies.")
    print(f"There are {cookies % kids} left over.")

main()
```

**10.** In one sentence, explain why programmers use a **named constant** like `TAX_RATE = 0.0875` instead of just typing the number `0.0875` directly into their calculations.
