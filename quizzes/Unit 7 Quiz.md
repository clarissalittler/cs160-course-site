## Unit 7 Quiz — The Nature of Computation

### Multiple Choice

**1.** Throughout this unit, the "big idea" is that an algorithm is best understood as which of the following?
- A) A feature that only exists once it's written in Python
- B) An idea or step-by-step method that exists on its own, separate from any language, person, or machine
- C) A piece of computer hardware
- D) A list of instructions that only counts if a computer runs it

**2.** A friend gives you a recipe whose final step reads "season until it tastes good." Which of the five requirements of a good algorithm does this step most clearly break?
- A) It's well-ordered
- B) It produces a result
- C) Every step is unambiguous
- D) It halts

**3.** Lesson 2 shows the "find the biggest number" algorithm written in Python, JavaScript, and Common Lisp. What is the point of showing all three?
- A) Lisp is the fastest of the three languages
- B) Only Python can express this particular algorithm
- C) The colons, braces, and parentheses are just "costumes" — the same underlying algorithm shows through all of them
- D) Different languages compute different answers for the same list

**4.** Why does binary search work on a sorted list but not on an unsorted one?
- A) Sorted lists are stored in faster memory
- B) The "throw away half" trick depends on knowing which half the value must be in, which only makes sense if the list is in order
- C) Binary search needs the list to contain only numbers
- D) Unsorted lists are always too long to search

**5.** Lesson 4 describes selection sort as scanning the rest of the list to find the smallest item, then the next smallest, and so on — a loop inside a loop. Which Big-O class does this give it?
- A) O(1)
- B) O(log n)
- C) O(n)
- D) O(n²)

**6.** According to Lesson 5, what kind of limit is the halting problem?
- A) A temporary limit that faster chips or quantum computers will eventually overcome
- B) A limit on computation itself — no machine or language can ever build a perfect, always-correct "Halts" program
- C) A limit that only applies to programs written in Python
- D) A limit caused by computers not having enough memory

### True / False

**7.** Because binary search is so much faster than linear search, you should always use binary search no matter what the list looks like.

**8.** Conway's Game of Life is "Turing-complete," meaning that with the right starting pattern it can compute anything an ordinary computer can compute.

### Multiple Choice (continued)

**9.** Grabbing the first item of a list takes the same amount of work whether the list has 10 items or 10 million. What Big-O class describes that operation?
- A) O(1), constant time
- B) O(log n), logarithmic time
- C) O(n), linear time
- D) O(n²), quadratic time

**10.** Binary search checks the middle value, 68, while searching a sorted list for 95. What does it do next?
- A) Keep the left half because 95 is lower than 68
- B) Keep the right half because 95 is higher than 68
- C) Search both halves because binary search cannot compare numbers
- D) Stop immediately because the middle value was not 95
