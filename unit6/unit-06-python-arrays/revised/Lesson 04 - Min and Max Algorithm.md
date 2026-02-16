# Lesson 4 --- Min and Max Algorithm

![Unit 6 banner](img/banner.jpg)

> **After this lesson, you'll be able to:**
>
> - Implement the min and max algorithms to find the smallest and biggest elements in an array.

## The min and max algorithm

Finding the minimum and maximum values in an array is one of the most classic algorithms out there. The idea is straightforward: we create variables to hold our current `min` and `max`, then we walk through each element of the list, comparing as we go and updating whenever we find something smaller or larger.

Here's the pseudocode --- follow the logic and make sure it clicks before we move to real Python:

```
1. set min to the first element in the list
2. set max to the first element in the list
3. loop through the list looking at each element
4.       if the element is bigger than max
5.            update max
6.       if the element is smaller than min
7.            update min
```

When the loop finishes, `min` and `max` will hold the smallest and largest elements. That's it --- the whole algorithm. Elegant, right?

## The code

Study the program below. (Or download [minimum.py](https://drive.google.com/file/d/1kYWRZ2G0vvLFNfjbQHRsp_UYfy0pCVLz/view?usp=drive_link) and run it in your IDE of choice.) It finds the minimum --- your job is to add code that also finds the maximum.

```python
#This program finds the minimum in a list of numbers
#You write code to find the maximum
def main():
  nums = [3, -2, 4, 10, -6]

  print("array:", nums)
  min = nums[0] # always set min/max to cell 0!
  length = len(nums) # get the number of elements

  # loop through all of the elements
  for index in range(length):
      if nums[index] < min:
          min = nums[index]

  #print the minimum
  print("min:", min)

main()
```

Notice that we set `min = nums[0]` right at the start. The first element is the smallest thing we've seen *so far* (because it's the only thing we've seen). Then as we loop through the rest, we update `min` whenever we find something even smaller. To add `max`, you'd do the same thing but flip the comparison --- check if the element is *greater than* your current `max`.

> **Bug Alert:** When searching for min and max, it's a common mistake to initialize them to some random value. For example, setting `max = 0` --- the thinking is "surely the biggest number will be bigger than 0, right?" But what if *all* of the numbers are negative? Your max would end up being 0, which isn't even in the list! Same problem with setting `min` to some huge number.
>
> The fix is simple: **always set min and max to the first element of the array** (index 0) to start. That element is genuinely the smallest and largest value you've seen so far --- because it's the *only* value you've seen so far. Then you compare everything else against it.
