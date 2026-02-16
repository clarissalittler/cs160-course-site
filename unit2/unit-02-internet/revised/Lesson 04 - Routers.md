# Lesson 4 --- Routers

**After this lesson, you'll be able to:**

- Explain how information travels over the internet through different computers called routers.

## Routers

A **router** is a computer that passes information from one network to another. That's it --- that's the core idea. A router will either deliver a packet to its final destination or forward it to one of the other routers it's connected to. And here's the clever part: by monitoring current network conditions, a router can figure out which of its neighbors will get the packet to its destination fastest.

In Figure 2.6, the routers are the orange circles. Information gets sent from one computer on the internet to another by hopping through these routers.

![Routers moving information through the internet](images/router.gif)
*Figure 2.6. Routers moving information*

There will often be **redundant paths** between two locations on the internet --- remember our last lesson? --- so if one path is congested or out of service, other paths are available. This **redundancy** makes the internet more reliable and also helps it scale, accommodating new users (and new routers!) as they connect to the system.

## Bandwidth

**Routing** is the process of finding a path from the sender to the receiver. As we've seen, there are often many different paths a message might take.

But how *fast* does the message arrive? That's determined by **bandwidth**. In a computing network, bandwidth is the maximum amount of data that can be sent in a fixed amount of time, usually measured in **bits per second**.

If a message arrives quickly, that might be because of high bandwidth --- lots of bits can fly through per second. If it arrives slowly, it could be due to low bandwidth. Think of it like a highway: bandwidth is how many lanes you've got. More lanes, more cars can flow through at once.

## Internet service providers (ISPs)

Your computer probably connects to a router somewhere in your home, and that router connects to your **ISP**. ISPs --- Internet Service Providers --- are the companies that sell internet access to homes and institutions. (Xfinity, CenturyLink, Wave G, &c.) The computers connected to the internet and the connections among them don't belong to any one organization. It's a patchwork of companies and institutions all linked together.

![Internet service providers connect users to the internet](images/isp.png)
*Figure 2.7. Internet Service Providers (Image Source: [TechTerms](https://techterms.com/definition/isp))*

Here's a helpful analogy: think of your ISP like the US Post Office (USPS). You drop off your mail at your local post office, and it gets forwarded to the destination through other distribution centers, finally arriving at the post office closest to where the letter needs to be delivered. Those distribution centers? They're basically routers.

![Letter traveling from post office to destination](images/post_office.png)
*Figure 2.8. Routing Mail (Image Source: [TechTerms](https://techterms.com/definition/isp))*

And just like when we send physical mail, it's important to include a "To" and "From" address. The internet works the same way --- every piece of information needs to know where it's going and where it came from.

In the next lesson, we'll learn about **protocols** and how the Internet Protocol assigns addresses to senders and receivers of information. It's basically the internet's addressing system, and it's surprisingly elegant.
