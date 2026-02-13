# Lab 03 - Evaluating code by hand

You will make a copy of this document for your work. Submit your work to the Lab 03 Assignment in D2L. Solutions will be posted the day after the lab is due and only for students who submit work. Check your answers - learning to self-assess is super important and will help you become a better computer scientist!

*For questions 1-3, create a hand tracing table for each of the variables and state what the code will display. Include a copy of your hand tracing table (take a picture if you complete on paper) and include in your answer document. Each row of the table corresponds to a line of code.*

*If the variable hasn't been initialized yet leave the entry blank. The first row has been filled in for you.*

***Hint: Watch the Hand Trace Video in Unit 5 - lesson 2***

1. For this problem write the value of x, y, z after **each line of code**

   ```python
   x = 0
   y = 5
   z = 4

   x = y - z - 2
   z = z * 2
   y = x * -1

   print("x =", x, "y =", y, "z =", z)
   ```

   |                | x | y | z |
   |:---------------|:-:|:-:|:-:|
   |                | 0 |   |   |
   |                |   |   |   |
   |                |   |   |   |
   |                |   |   |   |
   |                |   |   |   |
   | **Output:**    |   |   |   |

2. For the following code write in the values of sum and count after each iteration of the loop

   ```python
   sum = 2
   count = 20
   while count > 0:
       sum = sum + count
       count = count - 5
   print("sum =", sum, "count =", count)
   ```

   |                | sum | count |
   |:---------------|:---:|:-----:|
   |                |  2  |  20   |
   |                |     |       |
   |                |     |       |
   |                |     |       |
   |                |     |       |
   | **Output:**    |     |       |

3. For the following code write down the value of x at the end of each iteration of the loop and the value printed at the end of the program

   ```python
   x = 0
   for i in range(1, 5):
       if i % 2 == 0:
           x += i
       else:
           x -= i
   print(x)
   ```

   |                | x |
   |:---------------|:-:|
   |                | 0 |
   |                |   |
   |                |   |
   |                |   |
   | **Output:**    |   |
