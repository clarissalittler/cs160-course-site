# Midterm Exam — Units 1–4

**20 questions · 60 minutes · One attempt**

This exam contains 12 multiple-choice questions, 4 true/false questions, and 4 short-answer questions drawn from the Unit 1–4 quizzes. Read each question carefully. For short-answer questions, include the requested explanation or work.

## Multiple Choice

**1.** Your microwave, your phone, and a supercomputer are all computers because they all do the same four basic things with information. Which list names those four processes?
- A) Typing, printing, saving, deleting
- B) Input, storage, processing, output
- C) Hardware, software, input, output
- D) Reading, writing, arithmetic, logic

**2.** A friend asks why computers bother with just 0's and 1's instead of using all ten digits like we do. What's the real reason?
- A) Binary numbers take fewer digits to write than decimal numbers
- B) Binary keeps stored information secret unless you have the key
- C) A tiny switch that is either on or off is easy, cheap, and reliable to build by the millions
- D) Early programmers preferred binary and the tradition stuck

**3.** You need to shrink your term paper's text file to email it, and you must be able to get every character back exactly. Which compression should you use?
- A) Lossy — essays have plenty of vowels you can drop
- B) Lossless — the dictionary key lets you rebuild the exact original
- C) Either one — all compression can be reversed
- D) Neither — text files can't be compressed

**4.** Your cousin insists the internet is one giant computer owned by a single company. Which description is accurate?
- A) A single supercomputer that every device connects to
- B) A system of independently operated networks that exchange data through shared protocols
- C) A program pre-installed on a computer
- D) Another name for a web browser

**5.** Two teams build networking software without sharing their source code, but their programs can still communicate. What makes that possible?
- A) Every network program is owned by one company
- B) The government manually translates every message
- C) Both teams implemented the same published protocol specifications
- D) IP addresses tell programs the meaning of every payload

**6.** Which statement about HTTPS is most accurate?
- A) It makes any site using it honest and safe
- B) It protects web content in transit and helps authenticate the requested domain, but the destination site can still receive and log the content
- C) It hides all packet addresses, sizes, and timing from every network
- D) It is a content delivery network that caches pages near users

**7.** A plain-language, step-by-step plan written before the exact Python syntax is called:
- A) source code
- B) pseudocode
- C) a traceback
- D) an f-string

**8.** The user types `25` in response to this line. What type of value is stored in `age`?
```python
age = input("How old are you? ")
```
- A) `int`
- B) `float`
- C) `str`
- D) No value is stored

**9.** Which values does `range(1, 6)` provide to a loop?
- A) 0, 1, 2, 3, 4, 5
- B) 1, 2, 3, 4, 5
- C) 1, 2, 3, 4, 5, 6
- D) 0, 1, 2, 3, 4, 5, 6

**10.** This program runs without an error but displays nothing. Why?
```python
def cheer():
    print("Keep debugging!")
```
- A) A function cannot contain `print()`
- B) The function was defined but never called
- C) The message must be stored in a variable first
- D) The function needs a `while` loop

**11.** A function calculates a number that the rest of the program must store and use in another calculation. Which statement should the function normally use?
- A) `input`
- B) `print`
- C) `return`
- D) `range`

**12.** What does this code print?
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

## True / False

**13.** Emoji like 🐶 can't be stored using the every-character-gets-a-number trick — that only works for the English letters in the ASCII table.

**14.** An IP address in a log always identifies exactly one device and proves which individual person performed an action.

**15.** Formatting a value with `f"${price:.2f}"` changes the number stored in `price` so it permanently has exactly two decimal places.

**16.** A `while` loop is guaranteed to stop as long as its body contains at least one assignment statement.

## Short Answer

**17.** When you sample a black-and-white image in the pixelation widget, you choose how big each pixel is. In 1–2 sentences, what's the trade-off between using lots of small pixels and using a few big ones?

**18.** Name one everyday task that relies on internet access. Then name two different barriers—such as availability, affordability, device suitability, skills, accessibility, reliability, safety, or trust—that could exclude someone even if an internet signal exists in their area.

**19.** Predict every line of output and the final value of `total`:
```python
total = 0
for number in range(1, 4):
    total = total + number
    print(f"After {number}: {total}")
print(f"Final: {total}")
```

**20.** The intended rule is “keep asking until the user types yes or no.” Explain why the condition below never becomes false, then write a corrected condition.
```python
while reply != "yes" or reply != "no":
    reply = input("Type yes or no: ").strip().lower()
```
