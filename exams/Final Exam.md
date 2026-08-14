# Final Exam — Units 1–10

**30 questions · 90 minutes · One attempt**

This comprehensive exam contains 18 multiple-choice questions, 6 true/false questions, and 6 short-answer questions drawn from the weekly quizzes. Read each question carefully. For short-answer questions, include the requested explanation or work.

## Multiple Choice

**1.** You press the letter A on your keyboard while writing an email. According to the ASCII encoding scheme, what does the computer actually store?
- A) A tiny black-and-white picture of the letter A
- B) The letter A itself, kept in a special text-only part of memory
- C) The binary representation of the number 65, the number ASCII assigns to 'A'
- D) A sound recording of the letter being spoken

**2.** A provider has two physically separate routes between two cities. A fiber cut closes one route, routing information updates, and packets continue over the other. What made continued service possible?
- A) Redundancy provided an alternate path, and routing systems selected it
- B) Compression made packets small enough to cross the broken fiber
- C) High throughput made the cut irrelevant
- D) Caching downloaded the rest of every live conversation in advance

**3.** Which line correctly reads a price that may contain a decimal and stores it as a number?
- A) `price = input("Price: $")`
- B) `price = int(input("Price: $"))`
- C) `price = float(input("Price: $"))`
- D) `float = input("Price: $")`

**4.** Which expression asks whether `count` is equal to 10?
- A) `count = 10`
- B) `count == 10`
- C) `count =< 10`
- D) `count != 10`

**5.** Starting with `snacks = ["chips", "salsa"]`, what is the list after `snacks.append("guac")`?
- A) `["guac", "chips", "salsa"]`
- B) `["chips", "guac", "salsa"]`
- C) `["chips", "salsa", "guac"]`
- D) The list does not change

**6.** Which operation is a **filter**?
- A) Add every price to a total
- B) Build a new list containing only prices below $10
- C) Convert every temperature from Fahrenheit to Celsius
- D) Find the largest score

**7.** Given `schedule["repair"]["tags"][0]`, what does Python look up first?
- A) The item at index 0
- B) The `repair` key
- C) Every tag in the schedule
- D) The `tags` key

**8.** What is a useful reason to write a string with triple quotation marks?
- A) It automatically repeats forever
- B) It can contain several lines of text
- C) It converts every value to a number
- D) It creates a dictionary

**9.** Why does binary search work on a sorted list but not on an unsorted one?
- A) Sorted lists are stored in faster memory
- B) The "throw away half" trick depends on knowing which half the value must be in, which only makes sense if the list is in order
- C) Binary search needs the list to contain only numbers
- D) Unsorted lists are always too long to search

**10.** Lesson 4 describes selection sort as scanning the rest of the list to find the smallest item, then the next smallest, and so on — a loop inside a loop. Which Big-O class does this give it?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

**11.** According to Lesson 5, what kind of limit is the halting problem?
- A) A temporary limit that faster chips or quantum computers will eventually overcome
- B) A limit on computation itself — no machine or language can ever build a perfect, always-correct "Halts" program
- C) A limit that only applies to programs written in Python
- D) A limit caused by computers not having enough memory

**12.** A dataset of students includes a column of zip codes (97214, 97202, ...). A classmate says the column must be quantitative, since the values are all made of digits. What does Lesson 1 say?
- A) They're right — any value made of digits is quantitative
- B) The column is categorical: zip codes are numbers used as labels, and doing math on them (like averaging two zip codes) doesn't mean anything
- C) The column is quantitative and continuous, since there are so many possible zip codes
- D) The column is quantitative and discrete, since zip codes come in whole numbers

**13.** An ad shows two food carts' monthly orders as bars: Cart A sold 1,000 orders and Cart B sold 1,020 — about a 2% difference — yet Cart B's bar is drawn three times as tall as Cart A's. Which chart trick from Lesson 2 is at work?
- A) A cherry-picked time window
- B) A dual y-axis with two different scales
- C) A truncated y-axis that starts near 990 instead of at zero
- D) A 3-D pie chart tilted toward the viewer

**14.** Ice cream sales and drowning deaths rise and fall together, month after month — a real, strong correlation. According to Lesson 8's four possible explanations, what's actually going on?
- A) A causes B — eating ice cream makes swimming more dangerous
- B) B causes A — drownings drive grieving communities to buy ice cream
- C) A third factor (a confounder) causes both — warm summer weather sends people to the ice cream stand *and* into rivers and pools
- D) Pure coincidence — the two numbers just happen to line up

**15.** You want a program that can tell cat photos from dog photos, and Lesson 2 argues that writing the rules by hand ("dogs have pointy ears...") is hopeless — every rule has a thousand exceptions. What does machine learning do instead?
- A) Uses a much longer, more carefully written list of if-statements
- B) Shows the computer thousands of labeled example photos (the training data) and lets it figure out the pattern itself
- C) Stores every cat photo on the internet so new photos can be matched against them exactly
- D) Asks a human to double-check each photo as it comes in

**16.** A chatbot with web search gives you an answer complete with citation links. Lesson 9 says you should still click a link and check it. Why?
- A) Web links expire quickly, so citations go stale within days
- B) The model is still *generating* text, not retrieving verified facts — search results are just more raw material it can garble, so the link can be real while the "fact" attributed to it is not
- C) Citations are only trustworthy in the paid versions of these tools
- D) Chatbots deliberately lie when they aren't sure of an answer

**17.** A text from "your bank" says a suspicious $480 charge was just made and tells you to call 1-888-555-0134 immediately. You're worried it might be real. What's the safest move?
- A) Call the number in the text — it's the fastest way to sort this out
- B) Reply to the text and ask whether it's really your bank
- C) Call the number on the back of your debit card instead
- D) Ignore it completely — banks never send fraud alerts by text

**18.** Back in 2019 you signed up for a random forum using the same password you use for your email. The forum gets breached, and attackers take the leaked email + password combos and automatically try them on Gmail, banks, and Amazon by the millions. What is this attack called?
- A) Spear phishing
- B) Credential stuffing
- C) Ransomware
- D) Doxxing

## True / False

**19.** Emoji like 🐶 can't be stored using the every-character-gets-a-number trick — that only works for the English letters in the ASCII table.

**20.** Because no single company or government owns the whole internet, no organization has meaningful power over access, names, infrastructure, platforms, or standards.

**21.** An empty list can always be passed safely to `sum()`, `min()`, `max()`, and an average calculation without any special handling.

**22.** Moving a title from an `available` list to a `borrowed` list changes the running program's state.

**23.** A neural network is built out of many simple units that each weigh their inputs, add them up, and decide whether to fire — so the whole network, however fancy, is really just a giant pile of adjustable knobs.

**24.** A long passphrase made of random words (like `correct-otter-battery-stapler`) is generally stronger than a short password packed with symbols and numbers.

## Short Answer

**25.** What does this program print?
```python
cookies = 17
kids = 5
print(f"Each kid gets {cookies // kids} cookies.")
print(f"There are {cookies % kids} left over.")
```

**26.** What does this program print? Explain how the returned value controls the branch.
```python
def is_even(number):
    return number % 2 == 0

value = 9
if is_even(value):
    print("even")
else:
    print("odd")
```

**27.** A form requires every user to provide a middle name, storing an empty string when they do not. Explain one modeling problem with that design and one clearer alternative.

**28.** Give one manual test for any small interactive program. State the starting state, the input or action, and the expected state or message afterward.

**29.** Grabbing the very first item of a list takes the same amount of work whether the list has 10 items or 10 million. What Big-O class is this, and what is the one-word name for that class?

**30.** You want to know whether dog breeds with heavier max weights tend to have shorter max life spans. Which chart type from this unit should you reach for, and why is it the right choice for this question? (One or two sentences.)
