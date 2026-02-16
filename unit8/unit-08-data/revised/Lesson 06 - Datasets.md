# Lesson 6 --- Datasets

> **What you'll be able to do after this lesson:**
>
> - Look at a dataset and develop a set of meaningful questions you could answer with it.

## Dog data

Let's start with something fun --- dogs. Take a look at the Google Sheets spreadsheet below, which has data on different types of dogs. Browse the columns. What specific questions do you think we could answer with this data?

[LMS Activity: Embedded Google Sheets --- Dog breed dataset](https://docs.google.com/spreadsheets/d/e/2PACX-1vRmkVbKPBfFmBL0smZsVwJcmmUXkVpHDseLyFKXveB9qpMtP-uMbgoMGwAyvMqnpPzCotmDonX4ZouM/pubhtml?gid=921103190&single=true&widget=true&headers=false)

## Visualizations

Hopefully we can answer those questions using visualizations! But why do people bother making visualizations out of data in the first place?

Look at the picture below. What is the intersection of "Max Life Span" and "Australian Shepherd" telling us? It's telling us that Australian Shepherds have a max life span of 16 years. Simple enough when you're looking at one cell --- but what happens when you have hundreds of rows?

![Raw data showing dog breed and max life span, with the intersection of Australian Shepherd and Max Life Span highlighted at 16.0](images/chart1.png)
*Figure 8.7. Raw data of dog breed and max life span*

There's a *lot* of data in that spreadsheet. The bar chart in Figure 8.8 shows us the number of breeds with a specific max life span. The x-axis tells us the number of years, and the height of each bar tells us the count --- how many dog breeds have that max life span. You can estimate the counts by comparing bar heights to the numbers on the y-axis.

From this chart we can see:

- A max life span of 15 years has the highest number of counts at 25 breeds.
- There are only about 2 dog breeds with a max life span of 8 years.
- No breeds have a max life span of 9 years.
- (22 + 13 + 23 + 25 = 83) --- 83 out of 105 total breeds, or 83/105 = 79%, have a max life span between 12 and 15 years.

![Bar chart of dog breed max life spans showing counts per year](images/chart2.png)
*Figure 8.8. Bar chart of dog breed and max life span*

Visualizations help us look at lots of data at once and see patterns that are basically *invisible* if you're just staring at a table of numbers. That's the whole magic trick.

We're going to learn how to make different types of visualizations to answer different types of questions!

## Data analysis process

The data analysis process goes like this:

1. **Collect or choose the data**
2. **Clean the data**
3. **Visualize and find patterns**
4. **Obtain new information**

![The data analysis process: collect or choose data, clean data, visualize and find patterns, gain new information](images/data_analysis_process.png)
*Figure 8.9. Data analysis process*

It's a cycle, really. You'll often find that step 3 sends you back to step 2 when you realize something's messy, and step 4 might inspire you to collect entirely new data. That's normal --- that's how discovery works.

## Check for understanding!

[LMS Activity: Unit 8 Lesson 6 Quiz]

In the next lessons, we're going to focus on how data is used to make new information.
