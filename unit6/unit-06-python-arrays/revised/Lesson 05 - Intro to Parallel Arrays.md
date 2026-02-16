# Lesson 5 --- Intro to Parallel Arrays/Lists

> **By the end of this lesson, you'll be able to:**
>
> - Use parallel lists to store related information that has different data types.

## Parallel Lists (Arrays)

Here's the thing about arrays in most programming languages: they can only hold *one* type of data. All ints, all floats, all strings --- pick one. Python lists are actually more flexible (they *can* mix types), but it's generally good practice to keep each list to a single type --- it makes your code cleaner and avoids confusion. Either way, real-world data often involves *different* types that need to be kept together.

Think about a class roster. You've got student *names* (strings) and their *scores* (integers). Those are two different types, so they need two different lists. The trick is that we keep them **lined up by index** --- whatever's at position 0 in the names list corresponds to position 0 in the scores list, position 1 matches position 1, &c.

That's what we call **parallel lists**.

![2 parallel lists related by index number. First list is 'names' with elements 0-4 'Mary', 'Amit', 'Priya', 'Rekha', 'Samir'. List 2 is scores for each student - 98, 99, 95, 99, and 91.](images/parallelIntro.png)

*Figure 6.3. Parallel lists use different lists for related information.*

In the figure above, Mary has a score of 98, Amit has 99, Priya has 95, and so on. The index is what ties them together.

And here's the important part --- if you ever *rearrange* one list, you have to rearrange the other one the exact same way. If you sort alphabetically and move Amit to position 0, you'd better move their score to position 0 too. Otherwise the whole relationship falls apart.

## Parallel Lists in Action

Study the program below. You can also [download students.py](https://drive.google.com/file/d/1UXCj6awjdIvAsN3cvkrq93MG2kaW4WCb/view?usp=drive_link) and run it in your IDE of choice.

This program maintains a list of student names and their corresponding scores. There's also a video at the bottom of the page that walks through it.

```python
#This program demos parallel lists
def main():
  #declare all variables and initialize them
  names = []
  scores = []
  entry = 'y'
  aName = ""
  aScore = 0
  length = 0
  total = 0
  average = 0.0

  #welcome message
  print("Welcome to the Student Database!\n")
  print("Let's get started!\n")

  #loop to add the names and scores.
  while entry == 'y':
    #read a name and score from the user
    aName = input("Enter student's name: ")
    aScore = int(input("Enter the student's score: "))
    #add the name and score to the lists
    names.append(aName)
    scores.append(aScore)
    #ask if they want to add more
    entry = input("Do you want to add more names? (y/n): ")
    while entry.lower() != 'y' and entry.lower() != 'n':
        print("Invalid. Enter 'y' or 'n'.")
        entry = input("Do you want to add more names? (y/n): ")
    print()
  #end while here.
  #print the information
  print("\n-----------------------------------------")
  print("Student Database:\n")
  print("Name\t\t\tScore")

  #calculate the total and the average
  length = len(names)
  for index in range(length):
      print(names[index],"\t\t", scores[index])
      total = total + scores[index]
  average = total / length
  print("-----------------------------------------")
  print ("Class Average: ", format(average, ".2f"))

main()
```

Let's walk through what's happening here:

1. We create two empty lists --- `names` and `scores` --- that will grow in parallel.
2. A `while` loop keeps asking the user for a name and a score, appending each to its respective list.
3. After the user's done entering data, we loop through both lists using the *same index* to print each student alongside their score.
4. We also tally up all the scores and compute the class average.

The key insight? `names[index]` and `scores[index]` always refer to the same student. That's the whole idea behind parallel lists.

Watch the video below, which walks through prompting for student names and scores, printing the lists, and calculating the average class score.

[Video: Parallel Lists](https://www.youtube.com/watch?v=7kQUtUgXvj4)
