# Weekly Assignment Rubrics

These analytic rubrics are the grading source of truth for the ten Weekly Assignments.

## Partial-credit policy

- Each assignment has five criteria worth 0–4 points each, for 20 points total.
- Score every criterion independently. A missing or broken component affects only the criterion or evidence it actually touches.
- Half-points are allowed when the evidence falls between two descriptions. Smaller increments may be used when needed to recognize a correct subpart.
- Give credit for visible, relevant work even when the final answer is wrong or code does not run. Examples include a correct setup, useful trace, working function, appropriate chart choice, documented test, or well-supported reflection.
- Do not impose an overall score cap because one requirement is missing. Add the points earned across all five criteria.
- Convert the rubric total to the course's 0–4 scale by dividing by 5. For example, 17.5/20 = 3.5/4.0.
- A completely absent submission earns 0. Work that provides evidence on any criterion is scored on that evidence.
- Students may revise and resubmit for full credit until the course resubmission deadline.

## Rubrics

1. [Week 1 — Digital Information](Week%2001%20Rubric%20-%20Digital%20Information.md)
2. [Week 2 — Understanding Internet Problems](Week%2002%20Rubric%20-%20Understanding%20Internet%20Problems.md)
3. [Week 3 — Creative Programming](Week%2003%20Rubric%20-%20Creative%20Programming.md)
4. [Week 4 — Functions and Decisions](Week%2004%20Rubric%20-%20Functions%20and%20Decisions.md)
5. [Week 5 — In-Memory Information Tool](Week%2005%20Rubric%20-%20Information%20Tool.md)
6. [Week 6 — Persistent Data Tool](Week%2006%20Rubric%20-%20Persistent%20Data%20Tool.md)
7. [Week 7 — Algorithms and Efficiency](Week%2007%20Rubric%20-%20Algorithms%20and%20Efficiency.md)
8. [Week 8 — Quantitative Reasoning](Week%2008%20Rubric%20-%20Quantitative%20Reasoning.md)
9. [Week 9 — Working with Large Language Models](Week%2009%20Rubric%20-%20Large%20Language%20Models.md)
10. [Week 10 — Staying-Safe-Online Mini-Zine](Week%2010%20Rubric%20-%20Staying-Safe-Online%20Mini-Zine.md)

## Maintenance

Edit the Markdown files, then regenerate the student-facing HTML copies from the repository root:

```bash
for rubric_source in assignments/rubrics/Week*.md; do
  pandoc "$rubric_source" --standalone --from=gfm --to=html5 --metadata lang=en \
    --css=../../local-styles.css --css=rubric-styles.css \
    -o "${rubric_source%.md}.html"
done
```
