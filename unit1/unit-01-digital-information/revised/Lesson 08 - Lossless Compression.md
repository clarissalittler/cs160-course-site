# Lesson 8 --- Lossless Compression

**After this lesson, you'll be able to:**

- Create lossless compressions of text files
- Analyze patterns in data to figure out compression strategies

## The Problem: Everything Is Getting Bigger

As we've been creating images over the last few lessons, you've probably noticed something: the number of bits it takes to represent stuff has been growing and *growing*. A black and white image? Manageable. A color image with 24 bits per pixel? That adds up fast. And we haven't even talked about video yet --- don't worry, we will, and the numbers get wild.

So what do we do about it? We **compress** things. We find clever ways to represent the same information using fewer bits. And that's exactly what this lesson is about.

Here's a thought to get us started: when you're text messaging, you probably use abbreviations like "brb," "lol," "c u soon," &c. Why do we do that? Because we're lazy? Well, partly. But also because we're *compressing* --- we're sending the same meaning with fewer characters. Congratulations, you've been doing data compression your entire texting life.

## Text Compression

Consider this message:

```
pitter_patter_pitter_patter_listen_to_the_rain_pitter
_patter_pitter_patter_on_the_window_pane
```

I want to send this to a friend, but their phone can only accept 80 characters at a time. (Remember when that was a real constraint? Good times.) I notice there's a *lot* of repetition in this pattern, so instead of sending the whole thing, I create a little dictionary and send this instead:

```
Symbol Dictionary:
  green_check  = _the_
  heart        = tter_
  pencil       = pi(heart)
  key          = pa(heart)
  pin          = (pencil)(key)(pencil)(key)

Compressed message:
  (pin)listen_to(green_check)rain_(pin)on(green_check)window_pane
```

See what happened there? We built up symbols that reference other symbols, and we replaced repeated patterns with short stand-ins. The original message was 93 characters. The compressed version --- message *plus* dictionary --- is only 56 characters. That's a significant savings, and we haven't lost a single character of the original. Your friend can reconstruct the full message perfectly using the dictionary.

That's the core idea. Let's go practice it.

## Text Compression Widget

Navigate to the [Text Compression Widget](https://studio.code.org/s/text-compression/stage/1/puzzle/2). Watch the intro video, then try to compress one of the songs --- the higher the compression percentage, the better!

A word of warning: if you see a *negative* percentage, that means your "compression" actually made things bigger. It's like packing for a trip and somehow needing a second suitcase for just the packing cubes. It happens when your dictionary overhead costs more than you save.

Click the drop-down menu in the widget to explore different texts. Before you compress each one, try to predict: will this be "easy" or "hard" to compress? Then test your prediction. You'll start to develop an intuition for what makes text compressible --- spoiler alert, it's all about **repetition and patterns**.

## What Makes This "Lossless"?

This compression strategy is called **lossless** because no information is being lost. None. Zero. The original message can be perfectly reconstructed from the compressed version plus the dictionary. You get back *exactly* what you started with, bit for bit.

There are many different strategies you can use when creating lossless compressions, and there isn't one single "best" way to do it. Your compression rate depends on which strategy you pick *and* on the patterns in the particular text you're compressing. A strategy that works great on English poetry might be terrible on random strings of characters --- because random data, by definition, doesn't have patterns to exploit. (This is actually a deep insight from information theory.)

The most important thing to remember: even though the file gets smaller, we never *actually* lose information. We can always perfectly recreate the original using our dictionary. That's the whole point --- and the whole promise --- of lossless compression.

## Check for Understanding!

[LMS Activity: Unit 1 Lesson 8 - Lossless Compression]

---

Coming up next: what happens when we *do* throw information away on purpose? Turns out, sometimes that's exactly what you want to do. We'll explore **lossy compression** --- where bits are sacrificed for the greater good of smaller file sizes --- and talk about when each approach makes sense.
