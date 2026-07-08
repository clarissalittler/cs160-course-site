## Unit 5 Quiz — Collections: Strings, Lists, Tuples, and Dictionaries

### Multiple Choice

**1.** Given `word = "Python"`, what does `word[-1]` give you?
- A) `"P"`
- B) `"o"`
- C) `"n"`
- D) An error, because indexes can't be negative

**2.** You have this list: `pets = ['dog', 'cat', 'parrot', 'hamster']`. Which expression gives you `'parrot'`?
- A) `pets[3]`
- B) `pets[2]`
- C) `pets['parrot']`
- D) `pets(2)`

**3.** Starting from `snacks = ['chips', 'salsa']`, what does `snacks` look like after running `snacks.append('guac')`?
- A) `['guac', 'chips', 'salsa']`
- B) `['chips', 'guac', 'salsa']`
- C) `['chips', 'salsa', 'guac']`
- D) `['chips', 'salsa']` (nothing changes)

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

**7.** In Python, the first character of a string is at index 0.

**8.** In the loop `for value in nums:`, the variable `value` holds each *element* of the list in turn (not the index numbers like 0, 1, 2).

### Short Answer

**9.** What does this code print? Write the three lines exactly as they would appear.
```python
students = [("Mary", 98), ("Amit", 99), ("Priya", 95)]

for name, score in students:
    print(name, "scored", score)
```

**10.** What does this code print?
```python
city = "Portland"
print(city[0:4])
```
