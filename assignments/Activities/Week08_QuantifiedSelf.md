# Week 8 Activity — Quantified Self

## What's this all about?

This unit is about **data** — collecting it, organizing it, and turning it into charts that reveal something true (or, if you're not careful, something misleading). The best way to really *get* data is to make some of your own. So this week, you become the experiment.

The "Quantified Self" movement is a bunch of people who track measurements about their own lives — steps, sleep, mood, coffee, screen time, miles biked — and look for patterns. Your phone is probably quietly doing some of this to you already. This week you'll do it *on purpose*, by hand, so you understand exactly where the numbers come from and what they leave out.

You'll pick one thing about yourself to track, log it for several days in a **Google Sheet** (a spreadsheet — the humble, powerful workhorse of data), and then look at what you collected.

> **No coding required for the core activity** — just a Google Sheet. There's an *optional* notebook at the end if you want to make a fancier chart with Python.

## Step 1: Pick something to track

Choose **one** thing that's easy to count and that you'll actually remember to log. Some ideas:

- **Movement:** steps, minutes walked, miles traveled, times you left the house.
- **Habits:** cups of coffee/tea, glasses of water, hours of sleep, hours of screen time.
- **Study:** minutes spent on homework, number of times you checked your phone while studying.
- **Mood / energy:** rate your mood 1–10 each day, or your energy in the morning vs. evening.
- **Money:** dollars spent on food, number of times you opened a shopping app.
- **The weird and personal:** times you laughed, songs you skipped, pages you read, dishes you washed.

Pick something **you're genuinely a little curious about.** "I wonder if I actually sleep less on the days I drink more coffee" is a great reason to track two things.

> **A note on privacy — please read.** You'll be sharing a *summary* of this with the class, so **don't track anything you wouldn't want classmates to see.** Track coffee, not anything sensitive. You're always free to fudge the labels ("a personal habit") and just share the shape of the data. This is itself a data-ethics lesson: the moment you measure something, you've created a record that can be shared, leaked, or used in ways you didn't intend. Hold that thought for the reflection.

## Step 2: Set up your Google Sheet

1. Go to [sheets.google.com](https://sheets.google.com) and click the **+ (Blank)** to make a new sheet.
2. In the **first row**, make your column headers. At minimum you want a **date/day** column and a column for **the thing you're measuring**. For example:

   | Date | Cups of coffee | Hours of sleep | Notes |
   |------|----------------|----------------|-------|
   | Mon  | 2              | 7.5            | busy day |
   | Tue  | 4              | 6              | exam tomorrow |

3. That top row of headers matters — it's what turns a wall of numbers into *data* you can read. (We talked about how structure is what makes data usable; this is that idea in miniature.)

## Step 3: Track for at least 5 days

Log your measurement **once a day for at least five days** (a full week is better if you have time). Be honest — messy real data is more interesting than tidy fake data. If you miss a day, leave it blank and note it; gaps in data are themselves a finding.

Add a **Notes** column and jot down anything that might explain a number ("slept badly," "stayed late at work," "rainy"). Those notes are gold when you go looking for patterns.

## Step 4: Make a chart

This is where the spreadsheet earns its keep.

1. Select your data (drag across your columns, including the headers).
2. Go to **Insert → Chart.**
3. Google will guess a chart type. A **line chart** is usually best for "a thing over time"; a **column chart** is great for comparing days. Try a couple and see which tells the story more clearly.
4. Give your chart a real **title** and make sure the axes are labeled. (An unlabeled chart is a riddle, not a finding.)

## Step 5: Look for a pattern

Stare at your chart and your notes together. Ask:

- Did the number go **up or down** over the week? Any reason why?
- Were there **outliers** — one weirdly high or low day? What does your Notes column say happened?
- If you tracked **two things**, do they seem to move together? (Careful — see the reflection. Two things moving together does *not* prove one causes the other.)

You don't need to find a dramatic result. "Nothing much changed" is a perfectly real finding. The skill is *looking honestly* at your own data.

## Reflection

A sentence or two each (these go in your discussion post):

1. The act of measuring changed something, didn't it? A lot of people find that just *tracking* their coffee makes them drink less of it. What does that tell you about the difference between data that passively describes the world and data that quietly *shapes* it?
2. If you noticed two things moving together (more coffee → less sleep, say), explain why you *can't* yet conclude that one **caused** the other. What else could be going on? (This is the famous "correlation is not causation" — your data is a perfect place to feel why it matters.)
3. Your phone and apps track dozens of these measurements about you, all the time, without asking each day. Now that you've felt how revealing even *one* tracked number can be — who benefits from all that collected data, and who might be harmed?

## What to turn in

Post on the **Week 8 discussion thread**:

1. A **screenshot of your chart** (with a real title and labeled axes).
2. One sentence saying what you tracked and for how long.
3. The **most interesting pattern or surprise** you found — even if the surprise is "there wasn't one."
4. Your three reflection answers.

Then reply to a classmate — does their pattern match yours, or is your life shaped completely differently? Compare notes on what surprised you.

*Low-stakes — graded on completion. Five honest days of data and one labeled chart is a complete, successful activity.*

---

## Optional bonus: chart it with Python

If you want to push further and connect this to our Python work, there's a companion notebook — **`Week08_QuantifiedSelf_Analysis.qmd`** (open the `.ipynb` version in Colab) — that walks you through pasting your data in and making a chart with code instead of with the spreadsheet's menus. Totally optional, but a nice flex.
