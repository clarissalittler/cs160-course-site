# Week 1 Activity — Mona Lisa Underdrive (Databending an Image)

## What's this all about?

This week's big idea is that **everything inside a computer is the same stuff: numbers.** A photo, a song, a text message — underneath, they're all just long streams of bytes (a byte being a little bundle of eight bits, a number from 0 to 255). The *only* difference between a picture and a sound is which program you open the file with and how it agrees to interpret those numbers.

We're going to prove that in the most fun way I know: we're going to **lie to the computer.** We'll take a picture, and we'll open it in an *audio* editor — which will cheerfully treat the picture's bytes as if they were sound. Then we'll apply some audio effects (echo, reverb, distortion), "play" with the image as if it were a song, save it, and open it as a picture again. The effects we did to the "sound" will show up as glorious glitches in the image.

This technique is called **databending**, and artists use it on purpose. You're about to make some genuinely cool glitch art *and* understand, in your bones, why it works. The title's a nod to a William Gibson novel — feel free to ask me about it.

> **No coding this week.** This is point-and-click. You'll need two free programs and about half an hour.

## What you'll need

1. **Audacity** — a free, open-source audio editor. Download it from [audacityteam.org](https://www.audacityteam.org/download/). (Works on Windows, Mac, and Linux.)
2. **An image you don't mind wrecking.** A photo of your pet, a meme, a screenshot — anything. Save a *copy* so you don't lose the original.
3. Five minutes of patience the first time, because the menus are a little fiddly. After that it's quick.

## A safety note before we start

Some image formats glitch beautifully; others just refuse and give you a broken file. Use a **`.bmp`** or **`.tga`** image if you can — they're "raw" enough that the glitches show up cleanly. A `.jpg` will often glitch in a more dramatic, all-or-nothing way (sometimes the bottom half of the image just dissolves — which is its own kind of cool). If your image is a `.png` or `.jpg`, the easiest move is to open it in any image viewer and **"Save As" / "Export As" a `.bmp`** first.

Also: **always keep a backup of your original image.** We are deliberately corrupting a file. Work on a copy.

## The steps

### 1. Import the image *as raw audio*

- Open Audacity.
- Go to **File → Import → Raw Data…**
- Navigate to your image file. (You may need to change the file-type filter to "All files" so the image shows up — Audacity doesn't expect to see a `.bmp` here.)
- A dialog pops up asking how to interpret the data. The defaults usually work, but if it looks like pure static noise, try setting:
  - **Encoding:** U-Law or A-Law, or "Signed 8-bit PCM"
  - **Byte order:** Little-endian
  - **Channels:** 1 Channel (Mono)
- Click **Import.**

You'll now see a waveform. **That waveform is your picture.** Those wiggles are the exact same bytes that draw your image — Audacity is just showing them to you as a sound. You can even press play and *listen to your photo.* (It'll sound like harsh static. That's what your cat looks like, sonically.)

### 2. Do some effects — but protect the edges

Here's the one trick that makes databending work instead of just destroying the file: **the very beginning of an image file is the "header"** — a little label that says "I am a BMP, I am this many pixels wide," and so on. If you scramble the header, no program will recognize the file at all. So:

- Using your mouse, **select a chunk in the *middle* of the waveform**, leaving the first second or so untouched. (Don't select the very start.)
- Now open the **Effect** menu and apply something to your selection. Good ones to start with:
  - **Effect → Special → Echo** (gives repeating ghost-edges)
  - **Effect → Distortion / Reverb / Phaser** (warps and smears)
  - **Effect → Reverse** (mirrors a chunk — wild results)
- Apply one. Apply a few. Select different chunks and stack effects. Experiment! There's no wrong answer — you're hunting for a happy accident.

### 3. Export it back out as raw data

- Go to **File → Export → Export Audio…**
- Set the format to **"Other uncompressed files."**
- Click the **Options** and choose **Header: RAW (header-less)** and an encoding that matches what you imported (Signed 8-bit PCM is a safe bet).
- Save it with the **same extension as your original image** (e.g. `glitched.bmp`).

### 4. Open it as an image again

- Find your exported file and **open it in any image viewer** (double-click it, or open it in your OS's Photos/Preview app).
- Behold your glitch art. The audio effects you applied to the "sound" are now visible as tears, smears, echoes, and color-shifts in the picture.

If the image won't open at all, you probably nudged the header — undo in Audacity (Ctrl+Z), make sure your selection started *after* the first second, and try again. Glitch art is half accident, half learning where the edges are.

## Reflection

Write a sentence or two on each (these go in your discussion post):

1. You applied an *audio* echo and it came out as a *visual* smear. In your own words: why did doing something "to the sound" change the picture? What does that tell you about what a file actually *is*?
2. The header had to be protected or the whole file became unreadable. What does that suggest about how computers know what kind of file they're looking at?
3. Apps and social platforms often compress or alter uploaded images automatically. Who benefits from smaller files, who might be harmed when detail or control is lost, and who should decide whether the original is preserved?

## What to turn in

Post on the **Week 1 discussion thread**:

1. Your glitched image (just attach it).
2. The original, for comparison (so we can see what you did to it).
3. One sentence on which effect made the coolest mess.
4. Your three reflection answers.

Then reply to a classmate whose glitch you liked and guess what effect they used.

*Low-stakes — graded on completion. The goal is to ruin a picture on purpose and understand why it worked. There is no such thing as "doing the glitch wrong."*
