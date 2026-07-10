# Week 2 Activity — Make Your Own Web Page (Neocities)

## What makes the web, the web
In this unit we've been talking about the technology that underlies the internet, but one thing that's important is a reminder that the internet---and in particular "the web", as someone old enough to remember when there were user-visible parts of the internet not "the web"---is a distributed, untameable thing, and not just, as the joke goes, three social media sites full of screenshots of each other.

To that end, we're going to make a simple website and share it. It doesn't have to be anything fancy. The point is to get your hands a little dirty with **HTML**, the HyperText Markup Language that made the World Wide Web what it is, and allow yourself the joy of making something of your own on the web. This activity is also a small experiment in internet architecture: you will create a resource, give it a URL, link outward, and let other people reach it with ordinary web standards.


> **No special software needed** — Neocities has an editor right in your browser. You'll need about half an hour.

## Step 1: Make a Neocities account

1. Go to [neocities.org](https://neocities.org).
2. Use the **Sign up for free** form. Pick a username — it becomes part of your web address, so `yourname.neocities.org`. Choose something you're comfortable sharing. You can use a nickname; you do not have to use your real name. Neocities sites are public and can appear in its site gallery, so do not put private contact or location information on your page.
3. Complete the sign-up form and any confirmation step it shows. That's it — you now have a website. Genuinely. It's live at `yourusername.neocities.org`, and the free option includes an in-browser HTML editor, so you do not need a credit card, local installation privileges, or special software for this activity.

When you sign up, Neocities gives you a starter page (`index.html`) already filled with example content. We're going to edit it.

## Step 2: Find the editor and look at the HTML

1. From your dashboard, click on **`index.html`** to open it in the editor.
2. You'll see a bunch of text with lots of `<angle brackets>`. Those bracketed things are **tags**. Look for the pattern: almost everything comes in a *pair* — an opening tag like `<h1>` and a closing tag like `</h1>` (the slash means "closing"), with your content sandwiched in between.

Here are the bare basics you need for a simple "we party like it's the '90s" website:

```html
<h1>This is a big heading</h1>
<p>This is a paragraph of normal text. Write whatever you want in here.</p>
<a href="https://www.pcc.edu">Visit the Portland Community College website</a>
<img src="https://upload.wikimedia.org/wikipedia/commons/b/bc/Juvenile_Ragdoll.jpg" alt="a ragdoll kitten">
```

- `<h1>` is a big heading (you also have `<h2>`, `<h3>` for smaller ones).
- `<p>` is a paragraph.
- `<a href="...">` is a link; the address goes in the `href` part. Make the linked words describe the destination instead of saying only "click here."
- `<img src="...">` is an image; the picture's address goes in `src`, and `alt` is a text description (important — it's what screen readers read aloud to blind users).

If you really want a little more to play with there are *lists* given by
- `<li> ... </li>` items in the list inside of either
- `<ul> ... </ul>` which declare a bulleted list **or**
- `<ol> ... </ol>` which are a **numbered** list instead

## Step 3: Make it yours

Delete Neocities' example content and build your own page. **Make it about something you actually care about** — your favorite band, your dog, a hobby, a cause, the best food carts in town, a fan page for a TV show. The more it's *yours*, the better.

Your page must have:

- A **heading** (`<h1>`) with a title.
- At least **two paragraphs** (`<p>`) of your own writing.
- At least **one more heading** (`<h2>`) breaking up a section.
- At least **one link** (`<a>`) to somewhere on the web.
- At least **one image** (`<img>`). You can link to an image already online (paste its address into `src`), or upload your own to Neocities (there's an upload button on your dashboard) and use its filename. Don't forget the alt-text!

**Save** in the editor (there's a save button), then click **View** (or just visit `yourusername.neocities.org` in a new tab) to see it live on the actual internet. Follow your link and check that the image has meaningful alt text. If you navigate by keyboard or use assistive technology, test your page in your usual way; if you do not, try pressing Tab to confirm that you can reach and activate the link without a mouse.

> **Stretch goal (optional):** Neocities lets you add **CSS** — the language that controls how things *look* (colors, fonts, spacing). If you're feeling bold, try adding this near the top of your page and changing the values:
>
> ```html
> <style>
>   body { background-color: #fdf6e3; font-family: sans-serif; color: #333; }
>   h1 { color: #b58900; }
> </style>
> ```
>
> Change the color codes and reload to see what happens. This is a rabbit hole. Enjoy it.

## Reflection

A sentence or two each (these go in your discussion post):

1. Your page lives at *your* address. So what do you get from having your own little corner of the web that you don't get from posting the same stuff on social media?
2. The `alt` text on your image is read aloud to people who can't see the picture. If you don't use a screenreader, have you really noticed alt-text before? If you do use a screenreader, how often do you find images don't have useful alt-text?
3. Free browser-based hosting removes the need to buy a server or install special software. Name one person or group that benefits from that choice, one barrier that can still keep someone from publishing, and one organization or community that could reduce that barrier.

## What to turn in

Start a new discussion topic under the Module 2 weekly thread and post

1. The **link to your live page** (`yourusername.neocities.org`).
2. One sentence on what your page is about and why you picked it.
3. Your three reflection answers.

Then **visit at least two classmates' pages** and leave a friendly reply and share one thing you genuinely liked!
