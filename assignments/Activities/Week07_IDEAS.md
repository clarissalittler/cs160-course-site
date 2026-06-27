# Week 7 Activity — Ideas (BLANK WEEK — needs your pick)

Clarissa — Week 7 was blank too. It lines up with **Unit 7 (algorithms, searching, sorting, Big-O)**, which you just did a big voice-pass/consolidation on, so I aimed these at making "why algorithm *efficiency* matters" something students *feel* rather than just read. My recommendation is **Idea A**, drafted as `Week07_GuessingGame.qmd`. The other two are sketches.

---

## ⭐ Idea A — "Beat the Computer: Linear vs. Binary Search" (RECOMMENDED, drafted)

**The pitch:** Two-parter, built around a number-guessing game. **Part 1:** the *student* thinks of a number 1–100 and the *computer* guesses, using binary search ("is it higher or lower?") — and it always wins in 7 guesses or fewer, which feels like a magic trick. **Part 2:** flip it — show a "dumb" guesser that tries 1, 2, 3, 4… in order (linear search) and count how many guesses *it* needs. Then race them and watch the guess-counts diverge as the range grows from 100 to 1,000 to 1,000,000.

**Why it works for this unit:** this is Big-O you can feel in your gut. Binary search is O(log n); linear is O(n); and the whole point of the unit is that those grow *wildly* differently. Doubling the range adds *one* guess for binary search but *doubles* the work for linear. Students watch that happen with their own eyes instead of taking it on faith from a formula. It directly reinforces the Big-O scaffolding you added to the unit.

**Shareable:** yes — they report the biggest range they tried and how the two methods compared; great discussion fuel.

**Status:** fully drafted in `Week07_GuessingGame.qmd`. Ready to use.

---

## Idea B — "Race the Sorts"

**The pitch:** Give students a shuffled list and let them watch (and time) two sorting algorithms — say the bubble/selection sort from your unit vs. Python's built-in `sorted()` — on lists that grow from 100 to 10,000 items. Print the number of comparisons and the wall-clock time so they can see the slow one fall off a cliff.

**Why it works:** it's the sorting companion to the searching idea — same "watch efficiency diverge" payoff, but for the sort algorithms you already teach (selection, insertion). You've already got the animations in the unit; this lets them generate the *numbers* behind the animations themselves.

**Watch out for:** keep the slow-sort sizes modest (a true bubble sort on 100k items will hang Colab). Cap it, and that cap is itself a teachable moment ("notice we *couldn't* run the slow one on a million — that's the whole point").

**Effort to finish:** ~1.5 hours. Mostly making sure the timing/counting cells are clean and the sizes are safe.

---

## Idea C — "Everyday Algorithm" (unplugged + a little code)

**The pitch:** Students write out, in plain English, the step-by-step algorithm for something they do without thinking — making coffee, getting dressed for rain, the route they walk to the bus. Then they swap with a partner and try to follow each other's algorithm *literally*, robot-style, finding every ambiguous or missing step ("you didn't say to open the door"). Light code component: encode one such algorithm as a Python function with `if`/`else` steps.

**Why it works:** it gets at what an algorithm fundamentally *is* — a precise, unambiguous recipe — before any efficiency talk. It's very low-stakes, very funny, and accessible to the most code-anxious students. Great as the *gentle* option if your section is struggling.

**Watch out for:** lightest on actual Python of the three. Best if you want a breather week or have a less technical cohort.

**Effort to finish:** ~1 hour. Mostly prose; the code part is small.

---

### My recommendation
Go with **A (Beat the Computer)** — it produces a genuine "whoa" moment (the computer guessing your number in 7 tries) and then cashes that delight in for the single most important idea in the unit (efficiency classes grow differently). **B** is the natural follow-up or alternate if you'd rather center *sorting*, since you already have the sort animations. The draft for A is ready in `Week07_GuessingGame.qmd`.
