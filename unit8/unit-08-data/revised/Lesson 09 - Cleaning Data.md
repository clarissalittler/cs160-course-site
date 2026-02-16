# Lesson 9 --- Cleaning Data

> **What you'll be able to do after this lesson:**
>
> - Explain why data needs to be cleaned before you can do anything useful with it.

## Student dataset

We've started exploring how to use charts to process data stored in a table, but there are some real challenges lurking beneath the surface. How we process data depends on how it was collected and the tools we have available.

Let's explore new ways to refine data so we can answer even more questions. Look at the student dataset below. Can we use the data as-is? Do you see any problems?

<details>
<summary>Show Solution</summary>

- Data is of different types in the same column. You can't have a column with "six" and 6 --- the computer doesn't know those are the same thing.
- Some cells are missing data entirely.
- "i like food" is... not a valid major. (Points for honesty, though.)
- Spelling inconsistencies: "Junior" vs "Jr." --- same thing, but the computer sees them as completely different values.

</details>

[LMS Activity: Embedded Google Sheets --- Student dataset](https://docs.google.com/spreadsheets/d/e/2PACX-1vRN8QH5uMAIgprBON4KCVaV5XwMlKb4skX3Y2ZIc0ZPy1PmizIGLPJ-b3V7yOfpVQWskS4uoedqstTY/pubhtml?gid=1598099617&single=true&widget=true&headers=false)

## Cleaning data

Datasets bring challenges no matter what their size. There can be incomplete data, invalid data, or data from multiple tables that doesn't quite line up. All of this requires the data to be *cleaned* before we can work with it.

**When does data need to be cleaned?**

- Data is incomplete
- Data is invalid
- Multiple tables are being combined into one

**What leads to "messy" data?**

- Users enter different types of data for the same thing ("two", 2)
- Users use different abbreviations to mean the same thing ("CS", "Comp Sci", "Computer Science")
- Data may have different spellings or inconsistent capitalization ("math", "Math")

This is one of the dirty secrets of data science --- the glamorous part is making cool visualizations and discovering insights, but data scientists will tell you they spend a *huge* chunk of their time just cleaning data. Some estimates say 60--80% of the work. Wild, right?

You can prevent some of these problems at the collection stage. Try to avoid asking users to type in their answers --- use dropdown menus or checkboxes instead. Every free-text field is an invitation for creative chaos.

## Discussion prompt

> **Partner Activity**
>
> - Open the [Beatles dataset](https://drive.google.com/file/d/1KhZCeU_h8cgLsjgXG1m0lqpykugYC4S_/view?usp=sharing), which contains some information on Beatles songs from Spotify.
> - Verify the data is clean.
> - With your group, brainstorm a list of questions you can answer using one column of this dataset.
> - Open the [Beatles Colab Notebook](https://colab.research.google.com/drive/1H-00nzogW9W4fWYg8p_GQzM24quc7ejg?usp=sharing) and make a copy.
> - Answer the questions in the Part 1 text box.
>
> When you're finished, change the share settings on the notebook so that "anyone with the link can view" and post the link to the [LMS Activity: Unit 8 Lesson 9 --- Beatles Part 1] discussion prompt.
