# Lesson 10 --- The Cloud

**After this lesson, you'll be able to:**

- Explain the difference between "the cloud" and "the internet."

## The Cloud

What *is* the cloud, exactly? Is it the same thing as the internet? People use these terms interchangeably all the time, but they're actually different things. Let's untangle them.

In the early days of the internet, bandwidth was painfully slow. You could send text and small pictures, but video? Forget about it. Meanwhile, computers were enormous and expensive --- we're talking room-sized machines that cost a fortune. So if you needed serious computational power, you went to a **computer center** where the big machines lived.

As technology got smaller, cheaper, and more efficient, those centralized centers became less important. People could do their computing on personal devices --- desktops, laptops, eventually phones. The processing power came to *you*.

But then something interesting happened. Certain kinds of computation --- web searches, voice recognition, machine learning, processing massive datasets --- started requiring more power than any single personal device could provide. So the pendulum swung back. Tech companies built huge **"computer farms"** --- warehouses packed with tens of thousands of servers, all working together on problems.

These computer farms, taken collectively, are what we call **the cloud**.

Here's the key distinction: **the internet** is the network --- the physical wires, routers, and protocols (IP, TCP, DNS, HTTP, &c.) that connect devices together. **The cloud** is a collection of services and storage that live *on* the internet. The internet is the road system; the cloud is the warehouses and offices you drive to.

You've been using the cloud throughout this course. All of Google Docs, for example, is stored and largely processed in the cloud. You still use a computer at your desk, but much of the actual work happens on remote servers somewhere. When you save a Google Doc, you're not saving it to your hard drive --- you're sending it over the internet to be stored on Google's servers in a data center that's probably in Iowa or South Carolina or somewhere equally unglamorous.

[Video: What is the Cloud?](https://www.youtube.com/watch?v=i9x0UO8MY0g)

At this point, you know a *lot* more about the internet than the average person. You understand the physical layer, IP addressing, packets, DNS, HTTP --- the whole stack. Next time someone says "it's in the cloud," you can nod knowingly and think, "Ah yes, a server in a warehouse somewhere, accessible via the standard internet protocol suite." Or you can just enjoy this joke:

![Cloud joke: Son "Daddy, what are clouds made of?" Dad: "Linux servers, mostly."](images/cloud_joke.jpg)
*Figure 2.19. Cloud joke (Image Source: [Reddit](https://i.redd.it/l4bu591x5syy.jpg))*

It's funny because it's true. The vast majority of cloud servers really do run Linux. But that's a story for another course.
