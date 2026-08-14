# Week 7 Assignment — Algorithm and Algorithm Efficiency

There are 4 questions in this lab. Make a copy of this document for your work, and submit your work to the **Week 7 Assignment Assignment in D2L**. Solutions will be posted the day after the lab is due, and only for students who submit work. Check your answers — learning to self-assess is super important and will help you become a better computer scientist!

---

## Question 1: What Makes a Good Algorithm?

Here is someone's "algorithm" for making a cup of tea:

1. Put some water in a pot.
2. Heat it up.
3. Add tea.
4. Wait until it's ready.
5. Keep adding sugar.

This is a mess. For each problem below, name **which requirement of a good algorithm** it breaks (well-ordered, unambiguous, every step doable, produces a result, or halts), and say in a sentence why.

**a.** Step 2 says "heat it up," but never says for how long or how hot.

> *Your answer:*

**b.** Step 4 says "wait until it's ready" — but how would you *know* when it's ready?

> *Your answer:*

**c.** Step 5 says "keep adding sugar," with no stopping point.

> *Your answer:*

**d.** Now **rewrite step 5** so that this part of the algorithm will actually finish (halt).

> *Your answer:*

> 💡 **Hint:** Check the five requirements of a good algorithm in **Lesson 1**.

---

## Question 2: One Algorithm, Two Languages

Below is the same algorithm written twice — once in Python, once in JavaScript. They look different, but they do the exact same thing.

**Python:**

```python
numbers = [4, 7, 10, 3, 6]
count = 0
for number in numbers:
    if number % 2 == 0:
        count = count + 1
print(count)
```

**JavaScript:**

```javascript
let numbers = [4, 7, 10, 3, 6];
let count = 0;
for (let number of numbers) {
    if (number % 2 === 0) {
        count = count + 1;
    }
}
console.log(count);
```

**a.** In one sentence, what does this algorithm compute? (What single number does it print, and what does that number mean?)

> *Your answer:*

**b.** These two versions share the same "skeleton." For the **Python** version, write down which line: (1) sets up the counter, (2) loops through the numbers, (3) checks whether a number is even, (4) prints the answer. Then, for each one, point to the matching line in the **JavaScript** version.

> *Your answer:*

**c.** In your own words, what does it mean to say these are "the same algorithm" even though the code looks different?

> *Your answer:*

> 💡 **Hint:** Check **Lesson 2** — the costumes (colons, braces) differ, but the skeleton (a counter, a loop, a comparison) is identical.

---

## Question 3: Binary Search Trace

Consider the sorted list:

```
[3, 7, 12, 19, 24, 31, 38, 42, 55, 67, 72, 85, 91]
```

You are searching for the value **72** using binary search. Show each step of the search:

- What is the middle element?
- Is the target higher or lower?
- What portion of the list remains?

Continue until you find the target. **How many comparisons did it take?**

> *Your answer:*

> 💡 **Hint:** Check the binary search algorithm in **Lesson 3**. Remember, at each step you look at the middle element of the remaining portion. If the target is bigger, you throw out the left half (and the middle); if it's smaller, you throw out the right half. Keep going until you find it! If the remaining portion has an even number of items, there's no exact middle — round **down** and use the lower of the two middle spots.

---

## Question 4: Big-O Classification

For each scenario below, classify the algorithm's efficiency as **O(1)**, **O(n)**, **O(log n)**, or **O(n²)**. Briefly explain your reasoning — a sentence or two is fine.

**a.** Looking up a student's grade by their ID number in a dictionary/hash table.

> *Your answer:*

**b.** Searching through an unsorted list of 1,000 names to find a specific person.

> *Your answer:*

**c.** Using binary search to find a word in a sorted dictionary of 100,000 words.

> *Your answer:*

**d.** Comparing every student in a class with every other student to find who has the same birthday. (A class of *n* students.)

> *Your answer:*

> 💡 **Hint:** Check the Big-O lesson (**Lesson 4**) for the definitions of each efficiency class. Think about what happens to the number of steps as the input gets bigger — does it stay the same? Grow steadily? Double? Explode?

---

## Grading

This assignment uses a 20-point analytic rubric. Questions 1–4 and the reasoning shown across the assignment are scored independently, including credit for each correct lettered subpart. See the [Week 7 Assignment Rubric](rubrics/Week%2007%20Rubric%20-%20Algorithms%20and%20Efficiency.html).

If you don't receive a 4, read the feedback, revise, and resubmit for full credit — you have unlimited resubmission attempts until the Friday before Final Exam week. You must score at least a 1 on this assignment to unlock the Final Exam.
