# Lesson 7 --- Color Images

**After this lesson, you'll be able to:**

- Explain how colors are stored in a computer
- Represent different digital colors using RGB values

## Digital Color Images

Digital images are made up of tiny squares of color called **pixels** --- short for "picture elements," which is one of those abbreviations that's so old nobody even thinks about it anymore. In the figure below, you can see what happens when we zoom into a picture of Mario: the image breaks apart into a grid of colored squares. Every image on your screen right now is made of these little guys.

![Mario zoomed in to reveal the individual colored pixels](images/mario_pixels.png)
*Figure 1.11. Mario and Pixels*

Each of those tiny squares gets its color from a combination of three colors: **red**, **green**, and **blue** --- usually called **RGB**. Each color channel is represented with 8 bits, which gives us values from 0 to 255. That's 256 possible levels for each of the three colors.

Here's the fun part: these colors are *light*, not paint. If you've ever mixed paint, you know that mixing everything together gives you a muddy brown. Light works the opposite way. When all three channels are cranked to max --- RGB(255, 255, 255) --- you get **white**. When they're all turned off --- RGB(0, 0, 0) --- you get **black**. Think of it like light switches: 0 means the light is off, 255 means it's on full blast.

This is called **additive color mixing**, and it's genuinely counterintuitive if you grew up finger-painting. Your instincts from art class will betray you here.

Look at the figure below. The RGB values are (255, 0, 150) --- red is cranked to 100%, green is completely off, and blue is at about 59%. The result? A bright pink.

![Color swatch showing RGB(255, 0, 150)](images/rgb_example.png)
*Figure 1.12. RGB(255, 0, 150)*

Now here's a question: what happens if we turn down the lights 50% to RGB(128, 0, 75)? Does the color get brighter or darker? Think about what we're doing to the *light* --- we're dimming it. Less light means... darker. Try it for yourself at the [RGB Calculator](https://www.w3schools.com/colors/colors_rgb.asp) and plug in the values.

Mess around with it! Try making your favorite color. Try making the ugliest color you can. (There's actually a [famous "ugliest color" story](https://en.wikipedia.org/wiki/Pantone_448_C) --- it's called Pantone 448 C, and Australia uses it on cigarette packaging to make them look as unappealing as possible.)

## Binary and Data

You now know how numbers, text, *and* images are stored in a computer. That's a pretty solid foundation! This video gives a nice review of what we've covered and peeks at how other types of information --- like sound and video --- get encoded too.

[Video: How Computers Work: Binary & Data](https://www.youtube.com/watch?v=USCBCmwMCDA)

## Check for Understanding!

Drag the RGB values to the corresponding color swatch.

[LMS Activity: Unit 1 Lesson 7 - RGB Color Matching]
