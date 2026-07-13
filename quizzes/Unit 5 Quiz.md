## Unit 5 Quiz — Collections, Data Models, and Interfaces

### Multiple Choice

**1.** Given `word = "Python"`, what is `word[-1]`?
- A) `"P"`
- B) `"o"`
- C) `"n"`
- D) An error

**2.** What does `city[0:4]` produce when `city = "Portland"`?
- A) `"Port"`
- B) `"Portl"`
- C) `"ortl"`
- D) `"land"`

**3.** Starting with `snacks = ["chips", "salsa"]`, what is the list after `snacks.append("guac")`?
- A) `["guac", "chips", "salsa"]`
- B) `["chips", "guac", "salsa"]`
- C) `["chips", "salsa", "guac"]`
- D) The list does not change

**4.** What values are stored in `x` and `y` after this code runs?
```python
point = (3, 5)
x, y = point
```
- A) `x` is 3 and `y` is 5
- B) `x` is 5 and `y` is 3
- C) Both variables contain the complete tuple
- D) An error because tuples cannot be unpacked

**5.** Which operation is a **filter**?
- A) Add every price to a total
- B) Build a new list containing only prices below $10
- C) Convert every temperature from Fahrenheit to Celsius
- D) Find the largest score

**6.** Given `resource = {"name": "Tool Library", "cost": 0.0}`, which expression returns the name?
- A) `resource[0]`
- B) `resource.name`
- C) `resource["name"]`
- D) `resource("name")`

### True / False

**7.** In `for value in numbers:`, `value` receives each element, not the index numbers automatically.

**8.** An empty list can always be passed safely to `sum()`, `min()`, `max()`, and an average calculation without any special handling.

### Short Answer

**9.** What does this code print?
```python
records = [
    {"name": "A", "area": "North", "cost": 0},
    {"name": "B", "area": "Central", "cost": 5},
    {"name": "C", "area": "North", "cost": 10},
]

matches = 0
for record in records:
    if record["area"] == "North":
        matches += 1
        print(record["name"])
print("Matches:", matches)
```

**10.** A form requires every user to provide a middle name, storing an empty string when they do not. Explain one modeling problem with that design and one clearer alternative.
