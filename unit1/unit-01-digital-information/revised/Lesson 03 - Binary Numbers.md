# Lesson 3 --- Binary Numbers

![Unit 1 banner](img/banner.jpg)

**After this lesson, you'll be able to:**

- Explain how computers store information as 0's and 1's.

---

## Circles and squares, revisited

In the last lesson, you developed a number system using only circles and squares. With 3 place values, you came up with 8 different patterns. We can map a quantity to each of those patterns, like in the figure below. When we want to express the number 2, we use the pattern circle-square-circle.

Notice how the quantities start at **0** --- that's how computer scientists count! Starting from zero instead of one is going to come up again and again in this course. It feels weird at first, but you'll get used to it. (And eventually you'll start defending it to your friends, which is when you know you've truly arrived.)

![Circle square patterns mapped to quantities 0 through 7](images/circle_square_patterns.png)
*Figure 1.3. Circle and square patterns mapped to quantities.*

Using only circles and squares, we developed "rules" to help us count. We have two shapes: circle first, square second. As we iterate through them, we start with a circle, then the next quantity gets a square. Take a careful look at Figure 1.3 --- each time we move from a square *back* to a circle, the place value to the left also needs to advance to its next shape.

Sound familiar? That's exactly how carrying works in regular arithmetic. When you count past 9, you roll back to 0 and bump the tens column up by one. Same principle, different shapes.

## Decimal numbers

Number systems help us express and reason about quantities. Early number systems were basically glorified tally marks --- they let humans record things and do simple arithmetic, but they weren't exactly elegant. The number system we use today --- decimal --- uses the concept of **place value** to let us express any value we want by combining just 10 symbols: 0, 1, 2, 3, 4, 5, 6, 7, 8, and 9. Since there are 10 symbols, we call it a "base 10" number system.

And just like our circle-and-square rules: you count starting at the symbol "0", and when you hit "9", you roll back to "0" but the place value to the left goes to its next symbol.

0, 1, 2, 3, 4, 5, 6, 7, 8, 9 ... then back to 0, but the next place value ticks up to give us 10.

Those 10 symbols --- they're really just *shapes*, when you think about it. There's nothing inherently "three-ish" about the shape "3." We all just agreed it means three. Which, honestly, is kind of wild if you sit with it for a second.

## Binary numbers

So where is all of this heading? **Binary!**

The binary number system uses just 2 symbols --- 0 and 1 --- just like circles and squares. Instead of the shape "circle," we'll use "0." Instead of "square," we'll use "1."

![Mapping circle and square to 0 and 1](images/circle_square_0_1.png)
*Figure 1.4. Circle square patterns mapped to 0 and 1*

That's it. That's the whole trick. Everything you figured out about counting with circles and squares? It works exactly the same way with 0's and 1's. You already understand binary. You just didn't know it yet.

## Language of the computer

Binary is the language of the computer. The word "binary" literally means "two states." Those two states get called different things depending on context --- "1" and "0," "true" and "false," "on" and "off" --- but the essential idea is always the same: a single binary device can be in exactly one of two possible states. That's it. No middle ground, no "maybe."

A good example is a light switch. You can flip it on or off, but not --- under normal operation --- anything in between. A single light switch holds one **bit** of information.

![On/off circuit animation](images/circuit.gif)
*Figure 1.5. On/Off circuit (Image Source: [BJC Curriculum](https://bjc.edc.org/))*

Computers hold the state of electricity as a bit --- either 1 (on) or 0 (off), just like a toggle switch. Tiny on/off switches are easy, cheap, and reliable to manufacture, and *millions* of them make up the circuits that fit into the small area of a silicon chip. Modern processors have *billions* of these transistors. Billions! On a chip smaller than your thumbnail!

It might be hard to imagine right now, but we can represent numbers, text, sounds, and images with just these on/off switches. That's what the rest of this unit is all about.

## Circuits

Before we look at how information gets stored as binary signals, let's peek under the hood and see how a circuit actually works.

[Video: How Computers Work: Circuits and Logic](https://www.youtube.com/watch?v=ZoqMiFKspAA)

In the next lesson, you'll learn how to convert decimal numbers to binary --- and we'll actually do the math. Don't worry, it's friendlier than it sounds.
