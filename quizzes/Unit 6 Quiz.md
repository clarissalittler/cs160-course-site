## Unit 6 Quiz — Collections: Lists, Tuples, and Dictionaries

### Multiple Choice

**1.** You have this list: `pets = ['dog', 'cat', 'parrot', 'hamster']`. Which expression gives you `'parrot'`?
- A) `pets[3]`
- B) `pets[2]`
- C) `pets['parrot']`
- D) `pets(2)`

**2.** Starting from `snacks = ['chips', 'salsa']`, what does `snacks` look like after running `snacks.append('guac')`?
- A) `['guac', 'chips', 'salsa']`
- B) `['chips', 'guac', 'salsa']`
- C) `['chips', 'salsa', 'guac']`
- D) `['chips', 'salsa']` (nothing changes)

**3.** For the list `nums = [10, 20, 30, 40, 50]`, what does `len(nums)` return, and what is the last valid index?
- A) `len` is 5, last index is 5
- B) `len` is 5, last index is 4
- C) `len` is 4, last index is 4
- D) `len` is 6, last index is 5

**4.** You write `point = (3, 5)` and then try `point[0] = 9`. What happens?
- A) `point` becomes `(9, 5)`
- B) `point` becomes `(9,)`
- C) Python raises an error, because a tuple is immutable and can't be changed
- D) `point` becomes `[9, 5]`

**5.** You have `prices = {"coffee": 3, "muffin": 4, "bagel": 2}`. Which expression looks up the price of a muffin?
- A) `prices[1]`
- B) `prices["muffin"]`
- C) `prices.muffin`
- D) `prices[4]`

**6.** Which container is the best fit for a phone's contacts, where you want to look up a number *by* a person's name?
- A) A list, because the contacts are in order
- B) A tuple, because the name and number belong together and never change
- C) A dictionary, because you look things up by a meaningful key (the name)
- D) A single string holding all the contacts

### True / False

**7.** In the loop `for value in nums:`, the variable `value` holds each *element* of the list in turn (not the index numbers like 0, 1, 2).

**8.** When finding the largest value in a list, it's safest to start by setting `max = 0` before looping through the elements.

### Short Answer

**9.** What does this code print? Write the three lines exactly as they would appear.
```python
students = [("Mary", 98), ("Amit", 99), ("Priya", 95)]

for name, score in students:
    print(name, "scored", score)
```

**10.** Look at this dictionary and loop:
```python
ages = {"Dahlia": 20, "Sam": 35}
for name, age in ages.items():
    print(f"{name} is {age}")
```
In one sentence, explain what `.items()` gives you on each pass of the loop.
