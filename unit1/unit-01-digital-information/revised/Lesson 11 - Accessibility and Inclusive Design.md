# Lesson 11 --- Accessibility and Inclusive Design

**After this lesson, you'll be able to:**

- Explain why accessibility is a core concern in how we design and share digital information
- Identify common barriers that prevent people with disabilities from accessing digital content
- Describe the "curb-cut effect" and how designing for accessibility benefits everyone
- Evaluate a website for basic accessibility issues

---

## Who Actually Gets to Use All This?

We've spent this entire unit learning how information is represented digitally. Binary, text encoding, images, color, compression, intellectual property --- it's been a journey. But here's a question we haven't asked yet: once information is digitized and put out into the world, *who can actually access it?*

The answer, unfortunately, is: not everyone. At least, not unless we're deliberate about it.

About **1 in 4 adults in the United States** has some form of disability. That's roughly 61 million people. We're talking about visual impairments, hearing loss, motor disabilities, cognitive differences --- a wide range of experiences that affect how people interact with technology. This isn't a niche concern or an edge case. It's a quarter of the population.

So when we talk about how computers represent information, we can't stop at "how is it stored?" We also have to ask: "can people actually *get to it*?" Representation only matters if the information is accessible. Otherwise, we've just built a really elaborate system for excluding people.

## Types of Barriers

Disabilities affect technology use in different ways, and it's worth understanding the main categories:

**Visual** --- This includes blindness, low vision, and color blindness. Someone who's blind can't see a website at all --- they rely on software that reads the content aloud. Someone with low vision might need to zoom way in or use high-contrast settings. And someone with color blindness might not be able to distinguish between red and green elements that seem obviously different to you.

**Auditory** --- Deafness and being hard of hearing. If a video doesn't have captions, a deaf user simply can't access that content. The audio might as well not exist.

**Motor** --- Limited fine motor control, tremors, paralysis, or other conditions that make it difficult or impossible to use a mouse. Some people navigate entirely by keyboard. Others use specialized input devices like eye-tracking systems, head switches, or mouth-operated controllers.

**Cognitive** --- Learning disabilities, attention disorders, memory difficulties, &c. Complex layouts, walls of text without structure, or auto-playing animations can make content genuinely unusable for people with these conditions.

Here's the thing: these categories aren't as separate from your life as you might think. Disabilities can be permanent, but they can also be *temporary* (a broken arm) or *situational* (trying to read your phone in bright sunlight). Everyone moves in and out of different ability levels throughout their life.

## How Technology Includes (or Excludes) People

Let's get concrete. Here are some real examples of how digital content can include or shut people out --- and a few of them connect directly to what we've already learned in this unit.

### Screen readers and alt text

Remember the image encoding lessons? We learned that computers store images as grids of pixels --- tiny squares of color data, each one just a set of numbers. A black-and-white image is literally a grid of 0s and 1s. A color image is a grid of RGB values.

Here's the problem: a **screen reader** --- the software that blind users rely on to navigate their computer --- can't interpret those pixels. It doesn't look at an image and think "oh, that's a photo of a sunset." It's software, not a brain. All it sees is a blob of numerical color data that means nothing without context.

That's what **alt text** is for. Alt text is a short written description attached to an image in the underlying code. When a screen reader hits an image, it reads the alt text aloud instead. So a sighted person sees the photo; a blind person hears "a sunset over the Pacific Ocean with orange and purple clouds."

Without alt text? The screen reader either skips the image entirely or announces something useless like "image." The user encounters a blank void where information should be. If that image was important to understanding the page --- a chart, a diagram, a photo that the text refers to --- they've just been locked out.

### Color contrast

If the text on a webpage is light gray on a white background, it might look "clean" and "minimalist" to a designer with perfect vision. But for someone with low vision or color blindness, it's unreadable. The text just... disappears into the background.

This isn't a matter of opinion, either. There are actual numerical standards for it. The **WCAG** (Web Content Accessibility Guidelines) specifies minimum **contrast ratios** --- the mathematical difference in brightness between text and its background. Normal text needs a contrast ratio of at least 4.5:1. Large text can get away with 3:1. These aren't arbitrary numbers; they're based on research about what people with various levels of visual ability can actually read.

### Captions and transcripts

Video without captions excludes deaf and hard-of-hearing users, full stop. And here's a connection back to our text encoding lessons: captions are, at their core, just encoded text synchronized to a timeline. It's text data --- the same kind of stuff we learned to represent with ASCII --- attached to timestamps so the right words appear at the right moment. The technology isn't complicated. There's just no excuse for not including it.

### Keyboard navigation

Some people can't use a mouse. Maybe they have a motor disability. Maybe they use assistive technology that works through the keyboard. Whatever the reason, every interactive element on a website --- every button, every link, every form field, every dropdown menu --- needs to be reachable and usable with just the keyboard.

Try it yourself sometime: put your mouse aside and try navigating a website using only the Tab key to move between elements and Enter to activate them. On a well-built site, you'll be able to get everywhere. On a poorly built one, you'll get stuck almost immediately --- trapped in some section of the page with no way to reach the thing you actually need.

## The Curb-Cut Effect

Here's one of my favorite concepts in all of design.

You know the little ramps at the corners of sidewalks --- the ones that slope down to meet the street? Those are called **curb cuts**. They were originally designed for wheelchair users who couldn't navigate a sharp curb.

But look at who actually uses them: parents pushing strollers. Delivery workers with hand trucks. Cyclists. Travelers pulling rolling luggage. Skateboarders. Runners. People on crutches after a sports injury. *Everyone* benefits from curb cuts, even though they were designed for a specific accessibility need.

The same thing happens with technology, and it happens *constantly*:

- **Captions** were designed for deaf and hard-of-hearing users. But they're also used by people watching videos in noisy environments, people who aren't fluent in the spoken language, people in quiet spaces who can't turn on audio, and people who just process information better when they can read along.

- **Voice assistants** (Siri, Alexa, &c.) grew out of voice-control technology for people with motor disabilities. Now millions of people use them while cooking, driving, or anytime their hands are full.

- **Dark mode** is helpful for people with light sensitivity and migraines. It's also just... wildly popular with everyone.

- **High-contrast and large-text settings** were built for people with low vision. Students studying at 2 AM with tired eyes would disagree that these are "just" accessibility features.

- **Autocomplete and spell-check** help people with dyslexia and other learning disabilities. They also save the rest of us from embarrassing typos in professional emails.

This pattern is called the **curb-cut effect**: when you design for people at the margins, you tend to make things better for *everyone*. It's one of the strongest arguments for accessibility, because it reframes the whole conversation. This isn't about doing something extra for a small group. It's about making better products, period.

## Standards and Guidelines

You don't need to memorize legal specifics for this course, but you should know that accessibility isn't just a nice idea --- it's a professional and legal requirement.

**The ADA (Americans with Disabilities Act)** was passed in 1990 to prevent discrimination against people with disabilities. Courts have increasingly ruled that it applies to websites and digital services, not just physical spaces. If your business has a website (and whose doesn't?), the ADA is relevant.

**WCAG (Web Content Accessibility Guidelines)** is the international standard for web accessibility. It's organized into three levels:

- **Level A** --- the bare minimum. If you don't meet these, your site has serious barriers.
- **Level AA** --- the standard most organizations aim for, and the level most legal requirements reference.
- **Level AAA** --- the gold standard. Not always achievable for all content, but it's the goal to strive toward.

**Section 508** is a federal law requiring that all technology developed, maintained, or used by the U.S. government must be accessible. If you ever work in government, government contracting, or education (hello, that's us!) --- Section 508 matters.

The bottom line: if you go into any tech-related career --- web development, design, IT, project management, really anything --- accessibility will be part of your job. It's not an optional add-on. It's a core professional skill, just like knowing how to write clean code or manage a project timeline.

## Activity: Evaluate a Website

> **Try this out!**
>
> Pick a website you use regularly --- a social media platform, a news site, a shopping site, your school's homepage, whatever interests you. Then evaluate it for accessibility using the tests below.
>
> **Keyboard navigation:** Put your mouse aside and try navigating the site using only the Tab key (to move between elements) and Enter (to activate them). Can you reach everything? Can you tell *where* your focus is on the page? Or does it feel like you're navigating blind?
>
> **Alt text:** Find an image on the page, right-click it, and select "Inspect" (or "Inspect Element"). In the code that appears, look for the `<img>` tag. Does it have an `alt` attribute? If so, what does it say? Is the description actually helpful, or is it something generic like "image1.jpg"?
>
> **Text zoom:** Press Ctrl+ (or Cmd+ on Mac) a few times to increase the page's font size to roughly 200%. Does the layout hold together, or does everything break and overlap?
>
> **Color contrast:** If you want to go further, try a free contrast-checking tool like the [WebAIM Contrast Checker](https://webaim.org/resources/contrastchecker/). Pick a text color and background color from the site and see if they meet the WCAG standards.
>
> Write up a short report of what you found and share it in [LMS Activity: Unit 1 Lesson 11 - Accessibility and Inclusive Design]. What did the site do well? Where did it fall short? Were you surprised by anything?

## Discussion Questions

> **Discuss with your classmates!**
>
> Post your response to *one* of the following questions in [LMS Activity: Unit 1 Lesson 11 - Discussion], then reply to at least one classmate's post.
>
> 1. Have you ever encountered a website or app that was hard to use? What made it difficult --- and do you think the designers were even aware of the problem?
>
> 2. The curb-cut effect shows that features designed for accessibility often end up helping everyone. Can you think of other examples of this, in technology or in everyday life?
>
> 3. Should companies be legally required to make their websites accessible? Where do you draw the line between "it would be nice" and "it should be mandatory" --- and why?

## Bringing It All Together

This lesson is really the capstone of everything we've done in Unit 1. We started by learning how computers represent information --- binary numbers, text encoding, images, color, compression. Then we asked who *owns* that information when it's digital. Now we're asking who can *access* it.

And the answer we should be aiming for is: everyone. The technical knowledge you've built in this unit --- understanding how images are stored, how text is encoded, how data is structured --- is exactly the foundation you need to understand *why* things like alt text, captions, and semantic structure matter. They're not afterthoughts. They're part of doing the job right.

Technology is never neutral. The choices we make about how to design and build digital systems determine who gets included and who gets left out. That's worth taking seriously.
