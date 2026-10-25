## Unit 5 Quiz — Collections, Data Models, and Interfaces

### Multiple Choice

**1.** Given `word = "Python"`, what is `word[-1]`?
- A) `"P"`
- B) `"o"`
- C) `"n"`
- D) An error

**2.** What does this code print?
```python
playlist = ["Song A", "Song B"]
road_trip = playlist
road_trip.append("Song C")
print(len(playlist))
```
- A) 2
- B) 1
- C) An error, because `playlist` was never changed directly
- D) 3

**3.** Which operation is a **filter**?
- A) Add every price to a total
- B) Build a new list containing only prices below $10
- C) Convert every temperature from Fahrenheit to Celsius
- D) Find the largest score

**4.** What values are stored in `x` and `y` after this code runs?
```python
point = (3, 5)
x, y = point
```
- A) `x` is 3 and `y` is 5
- B) `x` is 5 and `y` is 3
- C) Both variables contain the complete tuple
- D) An error because tuples cannot be unpacked

**5.** A form requires every user to provide a middle name and stores an empty string when they do not. Which redesign models the data most clearly?
- A) Keep the required field because an empty string always means the person has no middle name
- B) Replace every missing middle name with the person's first name
- C) Make the field optional and document a value such as `None`, or omit the field when the task does not need it
- D) Store a single space so the missing value is invisible to users

**6.** You ask a classmate to try your catalog program without any help from you. At the prompt `Choose 1 through 5:`, they type `list` and get an error message. What's the most useful conclusion?
- A) The tester made a mistake, so next time you should explain the menu before they start
- B) Usability testing doesn't count unless dozens of people try the program
- C) The program needs color so the menu stands out
- D) The menu didn't make clear how to see the records, so revise one design decision and test again

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

**10.** A benefits agency estimates each person's monthly income as `annual_income / 12` and flags anyone who reported less than that estimate in a month they were on benefits. Which honest person is most likely to be wrongly flagged?
- A) An office worker paid the same salary every month
- B) A summer tour guide who earned the whole year's income from June through August, then went on benefits in the winter
- C) A retiree whose pension arrives in equal monthly payments
- D) A part-time cashier who works the same hours every week

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
