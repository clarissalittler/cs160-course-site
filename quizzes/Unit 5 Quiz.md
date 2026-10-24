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

### Multiple Choice (continued)

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
- A) `A`, then `C`, then `Matches: 2`
- B) `A`, then `B`, then `C`, then `Matches: 3`
- C) `North`, then `North`, then `Matches: 2`
- D) `A`, then `Matches: 1`

**10.** A form requires every user to provide a middle name and stores an empty string when they do not. Which redesign models the data most clearly?
- A) Keep the required field because an empty string always means the person has no middle name
- B) Replace every missing middle name with the person's first name
- C) Make the field optional and document a value such as `None`, or omit the field when the task does not need it
- D) Store a single space so the missing value is invisible to users

**11.** A program applies a rule to 200,000 applications. The rule gives the right answer 99% of the time. About how many applications does it get wrong?
- A) None, because 99% is close enough to 100%
- B) About 20
- C) About 2,000
- D) It's impossible to say anything without seeing the code

**12.** A spam filter flags any message containing the word "urgent." A school sends "Urgent: school is closed tomorrow because of ice," and the filter flags it. Which kind of mistake is this, and who is harmed by it?
- A) A scam that slipped through; the school is harmed because it receives more scams
- B) A wrongly flagged message; the parents who miss the closing notice (and the school trying to reach them) are harmed
- C) No mistake; any message containing "urgent" should be treated as suspicious
- D) A syntax error; the filter should have crashed
