# Lesson 2 -- Personally Identifiable Information

**At the end of this lesson, you will be able to:**

- Define personally identifiable information (PII) and give examples beyond the obvious ones
- Explain how combining seemingly harmless data points can uniquely identify individuals
- Describe how cookies and location tracking work at a basic level
- Identify steps you can take to protect your own PII

## What is PII?

**Personally Identifiable Information (PII)** is information that identifies, links, relates, or describes a specific individual. That definition is a little broad on purpose -- because the range of data that can identify you is a lot wider than most people realize.

In the last lesson, we talked about what data gets collected and how it's used. This lesson is about a more specific -- and more personal -- question: what data can be used to figure out who *you* are?

## The Obvious Stuff

Some PII is straightforward. If someone has any of the following, they can pretty directly identify you:

- **Full name**
- **Social Security number**
- **Home address**
- **Phone number**
- **Email address**
- **Date of birth**
- **Driver's license number**

No surprises there. If your Social Security number gets leaked, you know that's bad. If someone has your home address, you understand why that's sensitive.

But PII goes way beyond this list.

## The Less Obvious Stuff

Here's where it gets more interesting. All of the following can also count as PII, even though they might not seem like it at first:

- **Your IP address** -- remember from our internet unit, your IP address is like a return address on every packet your computer sends. It can be used to roughly identify your location and, with a little effort from your internet provider, to identify you personally.
- **Your device fingerprint** -- your specific combination of browser, operating system, screen resolution, installed fonts, and other settings is surprisingly unique. Websites can use this combination to identify you even without cookies.
- **Location data** -- your GPS coordinates over time
- **Browsing history** -- the specific pattern of websites you visit
- **Purchase history** -- what you buy, when, and where
- **Biometric data** -- fingerprints, face scans (like Face ID), voice recordings, even your typing pattern (the rhythm of your keystrokes is surprisingly distinctive)

Any one of these might seem harmless on its own. Your screen resolution? Who cares? But the key word there is "on its own."

## The Combination Problem

This is one of the most important concepts in data privacy, and it's genuinely surprising.

Your name alone might not uniquely identify you -- there are a lot of people named Maria Garcia or James Smith in the world. Your zip code alone definitely doesn't identify you -- thousands of people share the same zip code. Your date of birth alone doesn't identify you -- roughly 9,000 Americans share your birthday.

But here's the thing. In 2000, a computer scientist named **Latanya Sweeney** demonstrated that just three pieces of information -- **zip code, date of birth, and sex** -- are enough to uniquely identify **87% of Americans**. Three data points that almost nobody considers sensitive, and together they're basically as good as your name.

Think about that. You'd probably give any of those three pieces of information to a stranger without thinking twice. But together, they pinpoint exactly who you are.

This is called the **combination problem**, and it's why data privacy is so much harder than it looks. You can't just protect the "sensitive" data and assume everything else is fine. Data that seems completely harmless can become identifying when combined with other harmless data.

## When "Anonymized" Data Isn't Anonymous

The combination problem has some serious real-world consequences. Companies often claim they've "anonymized" data before sharing or selling it -- they've removed names, email addresses, and other obvious identifiers. But if the remaining data is detailed enough, it can be de-anonymized. And this has happened, repeatedly.

### The AOL Search Data Leak

In 2006, AOL released a dataset of 20 million search queries from 650,000 users for research purposes. They replaced usernames with random numbers. Totally anonymous, right?

It took reporters at the New York Times about three days to identify specific individuals from their search patterns. One user -- labeled only as "No. 4417749" -- had searched for things like "landscapers in Lilburn, GA," "homes sold in shadow lake subdivision," and a specific person's name. The reporters tracked her down: she was a 62-year-old widow in Lilburn, Georgia. From "anonymous" search data.

People search for their own symptoms, their own addresses, their own names, their friends' names, their embarrassing questions. The pattern of searches is like a fingerprint.

### The Netflix Prize De-anonymization

In 2006 (a big year for data privacy failures, apparently), Netflix released a dataset of 100 million movie ratings from about 500,000 users to power a competition to improve their recommendation algorithm. The data was anonymized -- no names, just anonymous user IDs and their ratings.

Researchers at the University of Texas took that dataset and cross-referenced it with public movie reviews on IMDb. If an anonymous Netflix user rated the same set of movies with similar ratings around the same time as a public IMDb reviewer -- well, that's probably the same person. They were able to de-anonymize a significant number of users, potentially revealing their complete Netflix viewing history, including movies they might not have wanted to be publicly associated with.

The lesson from both of these cases: **removing names doesn't make data anonymous if the remaining data is detailed enough to re-identify people.**

## Geolocation: Your Phone Knows Where You Are

Let's talk about one of the most powerful -- and most invasive -- forms of PII: your location data.

Your smartphone has GPS, and apps with location permissions can access it. Some apps need your location to work -- a maps app is useless without it. But many apps request location access for reasons that are a lot less obvious. Why does a flashlight app need to know where you are? (Answer: it doesn't. It wants to sell your location data.)

Here's what continuous location tracking reveals about you:

- **Where you live** (where your phone spends the night)
- **Where you work** (where your phone spends weekday business hours)
- **Where you worship** (regularly visiting a church, mosque, synagogue, &c. on specific days)
- **Your doctor** (visiting a specific medical office)
- **Who you visit** (your phone spending time at another person's home)
- **Your daily routine** -- coffee shop at 7:30, work at 8:15, gym at 5:30, home at 7

All of this is collected passively. You don't have to do anything. You just have to carry your phone -- which, let's be honest, you do everywhere.

In 2018, the New York Times published an investigation based on a dataset of location data from millions of phones. They were able to track specific individuals' movements in detail, including identifying a person who visited the Pentagon regularly (likely a defense department employee) and tracking their movements to their home. From "anonymous" location data.

## Cookies and Tracking: Why That Ad Follows You Around

You've probably noticed that after you look at a product online -- let's say a pair of headphones -- you start seeing ads for those exact headphones on completely different websites. This isn't a coincidence, and it's not because the internet is reading your mind. It's **cookies**.

### What are cookies?

A **cookie** is a small file that a website stores on your computer. Cookies were originally invented for useful things -- keeping you logged in, remembering your shopping cart, saving your preferences. These are called **first-party cookies**, and they're generally fine.

The privacy issue comes from **third-party cookies**. Here's how they work:

1. You visit a website that sells headphones. That website has an ad from an advertising network embedded in the page.
2. The advertising network places a cookie on your computer.
3. Later, you visit a completely different website -- a news site, maybe. That site also has ads from the same advertising network.
4. The advertising network reads the cookie from step 2 and says "oh, this is the same person who was looking at headphones."
5. You see an ad for those headphones on the news site.

This happens across dozens or hundreds of websites. The advertising network builds up a profile of everywhere you go online, what you look at, what you click on. All through those little cookie files.

The good news is that third-party cookies are being phased out by most browsers -- this has been a slow process, but it's happening. The less good news is that the advertising industry has been developing new tracking technologies to replace them (device fingerprinting, &c.), so the tracking isn't going away, it's just changing form.

## The Right to Be Forgotten

Different countries have taken very different approaches to data privacy.

The **European Union's General Data Protection Regulation (GDPR)**, which went into effect in 2018, is the most comprehensive data privacy law in the world. Among other things, it gives EU residents:

- The **right to access** -- you can ask a company what data they have about you, and they have to tell you
- The **right to deletion** (the "right to be forgotten") -- you can ask a company to delete your data, and in most cases they have to comply
- The **right to data portability** -- you can ask for your data in a format that lets you take it to a competitor
- Requirements for **clear, plain-language consent** -- companies have to explain what they're collecting and why, and you have to actively agree (not just fail to opt out)

That's why, if you've ever visited a European website, you've seen those cookie consent banners. Those exist because of the GDPR.

The United States, as of 2026, does **not** have a comprehensive federal privacy law. Some states have passed their own -- California's CCPA is probably the most well-known -- but there's no national equivalent of the GDPR. What data companies can collect, how they use it, and what rights you have over it varies significantly depending on where you live and which state laws apply.

Whether you think the EU's approach or the US's approach is better is a genuinely interesting policy question, and reasonable people disagree.

## What You Can Actually Do

This lesson has a lot of "here's how you're being tracked" in it, and I don't want to leave you feeling helpless. You have more control than you might think -- not total control, but some. Here are concrete steps:

- **Review app permissions on your phone.** Go into your settings and look at which apps have access to your location, microphone, camera, and contacts. Revoke anything that doesn't make sense. Does that game really need your location? Probably not.
- **Use your browser's privacy settings.** Most browsers let you block third-party cookies, and many now do it by default. Use private/incognito mode when you don't want browsing history saved locally.
- **Be thoughtful about what you share on social media.** Your posts, photos, check-ins, and friend lists are all data that can be combined and used in ways you might not expect.
- **Read (or at least skim) privacy policies for services you use heavily.** I know, I know -- we just talked about how nobody does this. But for the services you use the most (your email, your social media, your phone's operating system), it's worth at least skimming to understand the basics.
- **Use two-factor authentication.** This is more of a security thing than a privacy thing, but if your account gets hacked, all your data goes with it.
- **Know your rights.** If you're in California or another state with privacy laws, you may have the right to request deletion of your data. Use it.

You don't have to become a privacy hermit. You just have to make informed choices about the tradeoffs you're comfortable with.

## Discussion Questions

1. **What's the most surprising kind of data you learned is being collected?** Did anything in this lesson make you think differently about apps or services you use every day?

2. **The combination problem:** Latanya Sweeney showed that zip code + date of birth + sex can identify 87% of Americans. Can you think of other combinations of "harmless" data that might uniquely identify someone? What about your favorite three movies + your approximate age + your city?

3. **De-anonymization:** After hearing about the AOL and Netflix cases, do you think it's possible to truly anonymize detailed data? If not, what does that mean for companies that want to share data for research?

4. **Does knowing this change any of your habits?** Be honest. Are you going to check your app permissions after this lesson? Delete any apps? Change any settings? Or does it feel like the convenience is worth the tradeoff? There's no wrong answer -- I'm genuinely curious about your thinking.
