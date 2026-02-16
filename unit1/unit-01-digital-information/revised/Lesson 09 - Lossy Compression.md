# Lesson 9 --- Lossy Compression

**After this lesson, you'll be able to:**

- Examine the effects of lossy compression on text and images
- Decide whether to use lossy or lossless compression based on the needs of a given situation

## Lossy Text Compression Widget

Last lesson, we learned about lossless compression --- where you can always perfectly reconstruct the original from the compressed version. Now we're going to do something that might feel a little reckless: we're going to *throw information away on purpose*.

Here's the claim: you can take a word, keep the first letter, remove all the vowels, and the result will still be readable. That sounds wild, right? Bt y cn prbbly rd ths sntnc jst fn.

Let's test it. Open the [Lossy Text Compression Widget](https://studio.code.org/projects/applab/hxXJIEGg2yza_Q7t9W04xg), compress a sentence, and show the result to your family or friends. Can they guess the original message?

![Animated demonstration of lossy text compression removing vowels from a message](images/lossy.gif)
*Figure 1.13. Lossy compression widget*

Here's the critical difference from last lesson: with the lossless widget, we could always reverse the process and get back the original text, character for character. With this widget, those vowels are *gone*. We can't get them back. The process is **not reversible**. That's what makes it **lossy** --- some information is permanently lost.

And yet... the message is still *mostly* understandable. That's the magic trick of lossy compression: it exploits the fact that not all information is equally important. Your brain is remarkably good at filling in gaps, so we can throw away the "less important" bits and trust that the human on the other end will figure it out.

## Lossy Image Compression

This is where lossy compression really shines --- and where you've almost certainly encountered it before, whether you knew it or not. Every JPEG image you've ever seen online has been lossy-compressed.

Here's an image of a silky bantam chicken at high quality, alongside the same image compressed down to nearly the minimum quality:

![A normal, high-quality picture of a white fluffy bantam chicken](../Silky_bantam.jpg) ![The same chicken image heavily compressed, looking distorted and blocky](../Silky_extracrunch.jpg)

The one on the left looks fine --- nice fluffy chicken, living its best life. The one on the right looks like that chicken went through a blender and got reassembled by someone who only vaguely remembers what chickens look like. But here's the thing: that second image takes up *dramatically* less storage space. We're talking potentially 10x or 20x smaller.

If you download both files, you can see how enormous the difference in file size really is. And if you want to go deep down this rabbit hole --- including learning how to make glitch art by intentionally messing with JPEG encoding --- check out this fantastic interactive article: [Unraveling the JPEG](https://parametric.press/issue-01/unraveling-the-jpeg/). It's one of the coolest pieces of tech journalism on the internet, in my opinion.

## Compression Decisions

So now we've seen both sides of the coin. Lossy compression can *dramatically* shrink file sizes, but we lose information along the way. Lossless compression preserves everything perfectly, but can't compress nearly as aggressively.

Which one should you use? Well... it depends. And "it depends" is the most honest answer in all of computer science.

Think about it this way:

- Sending a photo to a friend on Instagram? Lossy is probably fine. Nobody's zooming in on your lunch with a magnifying glass.
- Storing medical X-rays? You probably want lossless. Doctors need every pixel.
- Archiving your master recordings if you're a musician? Lossless, absolutely. You can always make lossy copies later.
- Thumbnail images on a webpage that need to load fast? Crank that lossy compression up.

The choice always comes down to: *what are you using this for, and how much quality can you afford to lose?*

Let's practice making these decisions.

[LMS Activity: Unit 1 Lesson 9 - Compression Decisions]

---

Next up, we're shifting gears from the technical side of digital information to the *human* side. Once you've created something digital --- an image, a song, a piece of writing --- who owns it? What can other people do with it? We'll explore intellectual property, copyright, and Creative Commons in the next lesson. It's where bits meet law, and things get interesting.
