# Week 1 Activity — Mona Lisa Underdrive (Databending an Image)

## What's this all about?

This week's big idea is that **everything inside a computer is the same stuff: numbers.** A photo, a song, a text message: underneath, they're all just long streams of bytes (a byte being a little bundle of eight bits, a number from 0 to 255). The *only* difference between a picture and a sound is which program you open the file with and how it agrees to interpret those numbers.

We're going to prove that in the most fun way I know: we're going to **lie to the computer.** We'll take a picture and open it in an *audio* editor, which will happily treat the picture's bytes as if they were sound. Then we'll apply some audio effects (echo, reverb, distortion), "play" with the image as if it were a song, save it, and open it as a picture again. The effects we did to the "sound" will show up as glorious glitches in the image.

This technique is called **databending**, and artists use it on purpose. You're about to make some cool glitch art *and* see for yourself why it works. The title's a nod to a William Gibson novel, so feel free to ask me about it.

> **No coding this week.** This is point-and-click. You'll need two free programs and about half an hour.

## What you'll need

1. **Audacity**, a free, open-source audio editor. Download it from [audacityteam.org](https://www.audacityteam.org/download/). (Works on Windows, Mac, and Linux.)
2. **An image you don't mind wrecking.** A photo of your pet, a meme, a screenshot, anything. Save a *copy* so you don't lose the original.
3. Five minutes of patience the first time, because the menus are a little fiddly. After that it's quick.

## Getting your image ready

Some image formats glitch beautifully; others just refuse and give you a broken file. Use a **`.bmp`** image if you can. BMP stores every pixel's numbers more or less as-is, so the glitches show up cleanly. A `.jpg` will often glitch in a more dramatic, all-or-nothing way (sometimes the bottom half of the image just dissolves, which is its own kind of cool).

There's a catch: a BMP isn't compressed, so a full-size phone photo saved as one can be around 36 megabytes. So first **shrink it to about 800 pixels wide.** On Windows, Paint can do both: **Resize** the image, then **Save as → BMP picture**. On a Mac, Preview can too: **Tools → Adjust Size**, then **File → Export** and pick BMP. (If BMP isn't in the format list, hold down Option while you click the list to see more formats.) (Any image editor you already like will work.)

And **always keep a backup of your original image.** We are deliberately corrupting a file. Work on a copy.

## The steps

### 1. Import the image *as raw audio*

- Open Audacity.
- Go to **File → Import → Raw Data…**
- Navigate to your image file. (You may need to change the file-type filter to "All files" so the image shows up, since Audacity doesn't expect to see a `.bmp` here.)
- A dialog pops up asking how to interpret the data. The defaults usually work, but if it looks like pure static noise, try setting:
  - **Encoding:** U-Law or A-Law, or "Signed 8-bit PCM"
  - **Byte order:** Little-endian
  - **Channels:** 1 Channel (Mono)
- Click **Import.**

You'll now see a waveform. **That waveform is your picture.** Those wiggles are the exact same bytes that draw your image; Audacity is just showing them to you as a sound. You can even press play and *listen to your photo.* (It'll sound like harsh static. That's what your cat looks like, sonically.)

### 2. Do some effects, but protect the edges

Here's the one trick that makes databending work instead of just destroying the file. **The very beginning of an image file is the *header***, a little label that says "I am a BMP, I am this many pixels wide," and so on. That's *metadata*, data about the data, like we talked about in Lesson 4: it tells the image viewer how to slice the long stream of numbers that follows into rows of pixels. If you scramble the header, no program will recognize the file at all. So:

- Using your mouse, **select a chunk in the *middle* of the waveform**, leaving the first second or so untouched. (Don't select the very start.)
- Now open the **Effect** menu and apply something to your selection. Audacity sorts its effects into submenus, and the exact names have moved around between versions, so poke around until you find these:
  - **Echo** (gives repeating ghost-edges; recent versions keep it with the delay and reverb effects)
  - **Reverb**, **Distortion**, or **Phaser** (warps and smears)
  - **Reverse** (mirrors a chunk, with wild results; it's usually under **Special**)
- Apply one. Apply a few. Select different chunks and stack effects. Experiment! There's no wrong answer, because you're hunting for a happy accident.

### 3. Export it back out as raw data

- Choose **Export Audio** from the **File** menu. (In older versions it's tucked under **File → Export**.)
- Set the format to **"Other uncompressed files."**
- Set the **Header** to **RAW (header-less)** and the **Encoding** to whatever you used when you imported (Signed 8-bit PCM is a safe bet). In recent versions these choices are right there in the export window; in older versions, click **Options** to find them.
- Save it with the **same extension as your original image** (e.g. `glitched.bmp`).

### 4. Open it as an image again

- Find your exported file and **open it in any image viewer** (double-click it, or open it in your computer's Photos or Preview app).
- Behold your glitch art. The audio effects you applied to the "sound" are now visible as tears, smears, echoes, and color shifts in the picture.

If the image won't open at all, you probably nudged the header. Undo in Audacity (Ctrl+Z), make sure your selection started *after* the first second, and try again.

### 5. Convert it for posting

Before you post, open your glitched BMP and **save a copy as a `.png`**, and do the same for your original. PNG uses *lossless* compression (Lesson 5), so the file gets much smaller while every glitched pixel stays exactly as you made it. (A lossy JPG would smudge some of your carefully made mess.)

## Reflection

Write a sentence or two on each (these go in your discussion post):

1. What changed in your image, and what stayed recognizable? Why do you think doing something "to the sound" changed the picture in that particular way?
2. What does that suggest about how the image file is structured? (Think about the header, and about how the viewer turns one long stream of numbers into rows of pixels.)
3. When you opened the image file in Audacity, the bytes didn't change at all. Only the program reading them did. What does that tell you about what a file extension like `.bmp` is really doing?

## What to turn in

Post on the **Week 1 discussion thread**:

1. Your glitched image and the original, for comparison (both as PNGs).
2. One sentence describing your glitch in words, for anyone who can't see the images (for example, "the top third is fine, then the cat repeats four times and turns green").
3. One sentence on which effect made the coolest mess.
4. Your reflection answers.

Then reply to a classmate whose glitch you liked and guess what effect they used.

*Low-stakes — graded on completion. The goal is to ruin a picture on purpose and understand why it worked, and there's no such thing as "doing the glitch wrong."*
