## Unit 6 Quiz — Working with Real Data

### Multiple Choice

**1.** You open a file with `open("notes.txt", "w")`, but `notes.txt` already exists and has text in it. What happens?
- A) The new text is added to the end of the old text
- B) The old contents are erased and the file starts fresh
- C) Python raises an error to protect the existing file
- D) Nothing — `"w"` can only read

**2.** When you loop over a file line by line, why do you usually call `.strip()` on each line?
- A) To convert the line into a number
- B) To remove the trailing newline character (and stray spaces) from the end of the line
- C) To split the line at its commas
- D) To make the text uppercase

**3.** When you read a CSV with `csv.DictReader`, what is each row handed to you as?
- A) A list of the values
- B) A single string
- C) A dictionary, with the header row supplying the keys
- D) A tuple

**4.** A value you read out of a file or a CSV always arrives as which type?
- A) An integer
- B) A float
- C) A string (text), even if it looks like a number
- D) Whatever type it was originally

**5.** Which of these must be installed with `pip` because it does **not** ship with Python's Standard Library?
- A) `math`
- B) `random`
- C) `csv`
- D) `pandas`

**6.** Given `dogs = [{"name": "Momo", "age": 2}, {"name": "Rex", "age": 7}]`, which expression gives you the string `"Rex"`?
- A) `dogs["Rex"]`
- B) `dogs[1]["name"]`
- C) `dogs["name"][1]`
- D) `dogs[2]["name"]`

### True / False

**7.** Opening a file in append mode, `open("log.txt", "a")`, keeps whatever is already in the file and adds new text to the end.

**8.** `pip` is a tool for installing third-party packages (like `pandas` or `matplotlib`) that other programmers have shared through PyPI.

### Short Answer

**9.** What does this code print? Write each line exactly as it would appear.
```python
carts = [
    {"name": "Nong's", "cuisine": "Thai"},
    {"name": "Matt's BBQ", "cuisine": "Barbecue"},
    {"name": "Bing Mi", "cuisine": "Chinese"},
]

for cart in carts:
    if cart["cuisine"] != "Barbecue":
        print(cart["name"])
```

**10.** You read a `price` column from a CSV and write `total = total + row["price"]`, but your program crashes or gives a weird answer. In one sentence, explain what's wrong and how to fix it.
