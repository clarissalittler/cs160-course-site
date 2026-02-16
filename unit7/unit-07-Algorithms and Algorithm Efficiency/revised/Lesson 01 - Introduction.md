# Lesson 01 --- Introduction

> **After this lesson, you'll be able to:**
>
> - Define and write simple algorithms, and discuss what makes a good one.

## What Is an Algorithm?

**Algorithms** are step-by-step instructions for solving a problem, and they're the beating heart of computer science. Any time someone asks a question that starts with "How can I get the computer to...", the answer will be an algorithm.

Part of learning computer science is learning to think in terms of algorithms --- recognizing common patterns that can be solved with known approaches and figuring out how to express new ones.

Let's look at three examples. What do they all have in common?

### Chocolate Cream Pie

![Chocolate cream pie](images/L01_chocolate.jpg)

1. Heat milk, marshmallows, and chocolate in a 3-quart saucepan over low heat, stirring constantly, until the chocolate and marshmallows are melted and blended. Refrigerate about 20 minutes, stirring occasionally, until the mixture mounds slightly when dropped from a spoon.
2. Beat whipping cream in a chilled small bowl with an electric mixer on high speed until soft peaks form. Fold the chocolate mixture into the whipped cream. Pour into a pie shell. Refrigerate uncovered about 8 hours or until set. Garnish with milk chocolate curls and whipped cream.

### Directions to John's House

![Directions](images/directions.jpg)

1. From the Quik Mart, follow Saddle Road for four miles until you reach a stoplight.
2. Make a left-hand turn at the stoplight. Now you're on Hollow Street.
3. Continue driving on Hollow Street for one mile. Drive past four blocks until you reach the post office.
4. At the post office, turn right onto Jackson Road. Stay on Jackson for about 10 miles.
5. Eventually you'll pass the Happy Meadow farm on your right. Just after Happy Meadow, turn left onto Brickland Drive. John's house is the first house on your left.

### How to Change Your Motor Oil

![Motor oil](../motoroil.jpg)

1. Place the oil pan underneath the oil plug of your car.
2. Unscrew the oil plug.
3. Drain the oil.
4. Replace the oil plug.
5. Remove the oil cap from the engine.
6. Pour in 4 quarts of oil.
7. Replace the oil cap.

---

Every single one of these is an algorithm --- a set of instructions for solving a problem. And here's the beautiful thing: once we've created an algorithm, we don't need to think about the underlying principles anymore.

Got directions to John's house? You don't need to pull out a map and figure out every turn yourself. The intelligence needed to find the correct route is *captured in the algorithm*. All you have to do is follow the steps.

That's what makes algorithms so powerful --- they're a way of **capturing intelligence and sharing it**. Once someone encodes the smarts needed to solve a problem into an algorithm, anyone else can use it without becoming an expert in that field. Pretty great, right?

## Algorithm Requirements

For an algorithm to actually be useful, it needs to meet a few requirements. Think of these as the ground rules.

### Algorithms are well-ordered

Since an algorithm is a collection of operations, we need to know the correct order to execute them. If the order is unclear, we might perform the wrong step or not know which step comes next.

This is *especially* important for computers. A computer can only execute an algorithm if it knows the exact sequence of steps.

### Algorithms have unambiguous operations

Every operation needs to be clear enough that it doesn't need further simplification. If you hand a human a list of numbers and say "sort these," they'll figure it out. A computer? Not so much. It needs to be told *how* to find the smallest number, *how* to compare two numbers, &c.

The instruction "sort these numbers" is ambiguous to a computer because the computer doesn't have a built-in "sort" button --- it needs the problem broken down into **primitive operations** (or just *primitives*). When an algorithm is written entirely in terms of these primitives, it's unambiguous, and the computer can actually execute it.

### Algorithms have effectively computable operations

Every operation has to be *doable*. That sounds obvious, but it matters.

Say you're given an algorithm for planting a garden, and step one says "remove all large stones from the soil." Sounds reasonable --- until there's a four-ton boulder buried just below the surface. That step isn't effectively computable (at least not without heavy machinery and a bigger budget).

For computers, things like dividing by zero or taking the square root of a negative number are similarly impossible. These operations aren't effectively computable, so they can't be part of a valid algorithm.

### Algorithms produce a result

Unless an algorithm produces some kind of output, we can never verify whether our solution is correct. You've probably experienced this --- you give the computer a command, nothing visibly changes, and you're left wondering if it actually did anything or just silently ignored you. (Annoying, isn't it?)

Same deal with algorithms. If there's no result, there's no way to tell if it worked.

### Algorithms halt in a finite amount of time

Algorithms need to finish. They should have a finite number of operations and complete in a finite amount of time.

Imagine you wanted to write an algorithm to print all integers greater than 1:

```
Print the number 2.
Print the number 3.
Print the number 4.
.
.
.
```

See the problem? There are infinitely many integers greater than 1, so this algorithm would need infinite steps and run forever. That violates our rule --- every algorithm *must* eventually reach a point where it stops.

An algorithm that runs forever isn't an algorithm. It's a bug.
