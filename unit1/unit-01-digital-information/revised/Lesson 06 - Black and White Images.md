# Lesson 6 --- Black and White Images

**After this lesson, you'll be able to:**

- Explain how bits can represent individual pixels of a black and white image
- Explain how sampling turns an analog image into a digital one

## The Pixelation Widget

Let's get hands-on. Open up the [Pixelation Widget](https://studio.code.org/s/pixelation/stage/1/puzzle/1) --- it's a neat little tool that lets you paint with bits.

Watch the instruction video, then start by building the letter "A" using a 3x5 grid like the one shown below. One important thing to remember: you'll need to add 16 bits of *metadata* to define the width and height of your image. That's right --- before the computer even gets to the picture itself, it needs to know how big the canvas is. The image data doesn't mean anything without those dimensions.

![Pixelation widget showing the letter A built on a 3x5 grid, with metadata bits for width and height](images/pixelation_widget.png)
*Figure 1.9. Pixelation widget --- drawing the letter "A"*

## Sampling a Black and White Image

Now that you've seen how to flip each pixel between black and white, we're going to use the widget to represent an *analog* image --- and to do that, we need to talk about a process called **sampling**.

So what does "analog" actually mean here? It's a term for something with *continuous* representation --- like a picture you draw on a piece of paper with a pencil. Each line smoothly connects to the next, no matter how much you zoom in with a magnifying glass. There are no hard edges, no tiny squares. It's just... smooth stuff all the way down.

But computers don't do smooth. Computers do discrete chunks of information --- ones and zeros. So when we want to represent that smooth analog image digitally, we have to make some choices about *how* to sample it. We're trying to get the smoothest representation we can, while keeping an eye on how many bits we're using.

What does "sampling" mean in practice? We're deciding how small to make each little section of the picture when we look at it and decide: is this chunk black, or white? The smaller we make each sample, the more pixels we need --- which means more bits. Larger samples mean fewer pixels and a smaller file, but the image starts to look blurry and blocky. It's a classic tradeoff, and we'll keep running into tradeoffs like this throughout the course.

Try it out yourself! Use the Pixelation Widget to create the images below.

![Two sample images at different resolutions showing the tradeoff between detail and file size](images/sample_images.png)
*Figure 1.10. Sample images to digitize*

How many bits did it take to build each image? How long did it take you? Which sampling does a better job representing the original image --- and why?

## Discussion Prompt

> **Complete on your own!**
>
> Open [LMS Activity: Unit 1 Lesson 6 - Black and White Digital Images] and upload a copy of the digital images you created in this lesson. Then answer the following questions:
>
> - How many bits did each image take? (Don't forget to count the metadata!)
> - How long did each image take to build?
> - Which image is a better representation of the original? Why?
> - What are the pros and cons of sampling an image more frequently?
>
> When you've submitted your post, you'll be able to open and reply to other students' posts.
