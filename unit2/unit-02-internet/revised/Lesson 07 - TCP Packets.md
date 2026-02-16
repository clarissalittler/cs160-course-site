# Lesson 7 --- TCP Packets

**After this lesson, you'll be able to:**

- Explain the difference between TCP and UDP protocols.
- Describe the information that needs to be included within a "packet."

## Transport Layer Protocols

Last lesson, we learned how IP addresses let computers find each other on the internet. But here's a problem we haven't dealt with yet: what happens when you want to send something *big*? You can't just shove an entire webpage, video, or email through the internet in one giant blob. It would clog everything up.

That's where **Transport Layer Protocols** come in. These protocols manage the breakdown of a message into smaller chunks called **packets**, send them out into the network, and then reassemble them on the other end. Two of the big ones are TCP and UDP.

Take a look at the animation below. Notice the order the packets leave the first computer. Does each packet take the same path? Do they arrive in the order they were sent?

![Packets moving through the network taking different paths](images/network.gif)
*Figure 2.10. Packets moving through the network taking different paths*

The answer to both questions is *no* --- and that's actually by design. Packets can take wildly different routes through the network and arrive completely out of order. This might seem chaotic, but it's what makes the internet so resilient. If one path is congested or broken, packets just find another way. Pretty clever.

Now, we need two different protocols here because sometimes you care more about speed, and sometimes you care more about accuracy. Let's meet them both.

## User Datagram Protocol (UDP)

When the goal is to send information **fast** and you're okay with a few imperfections, you use **User Datagram Protocol (UDP)**. UDP works by firing all the packets out and... that's kind of it. It doesn't check if they all arrived. It doesn't care if they're in the right order. It's the "send it and forget it" approach.

![User Datagram Protocol - communication is one way](images/udp.png)
*Figure 2.11. User Datagram Protocol (UDP) (Image Source: [UDP/Datagram](https://sergeyzhuk.me/2017/07/05/reactphp-udp/))*

This sounds reckless, but it's actually perfect for situations where split seconds matter more than perfection. Think about video conferencing --- if a single frame of video gets lost, you don't want to pause everything and wait for it to be re-sent. That would make the call *way* more annoying than a momentary glitch. Same goes for live streaming and online gaming. A tiny hiccup is better than lag.

## Transmission Control Protocol (TCP)

When accuracy matters --- and it usually does --- we use **Transmission Control Protocol (TCP)**. With TCP, the sender and receiver work together to make absolutely sure that the *entire* message was successfully transmitted and reconstructed. No packet left behind.

![Transmission Control Protocol - communication is two-way](images/tcp.png)
*Figure 2.12. Transmission Control Protocol (Image Source: [UDP/Datagram](https://sergeyzhuk.me/2017/07/05/reactphp-udp/))*

TCP is what you want for things like sending emails, loading photos, or just browsing websites --- situations where getting 95% of the data isn't good enough. You need *all* of it.

Here's how it works: TCP divides a larger message into smaller packets and adds **ordering information** to each packet's header. (Think of it like numbering the pages of a letter before you rip it into pieces and mail each piece separately.) When a packet arrives at the destination, an **acknowledgment** gets sent back to the sender --- basically a little "got it, thanks!" message. If the sender doesn't get that acknowledgment, it knows to re-send that packet.

Once all the packets have arrived, the ordering information in the headers lets the receiving computer put them back together in the right order. Humpty Dumpty, reassembled.

## Design Your Own Packet Protocol

Now it's your turn. You're going to develop your own packet protocol!

> **Complete on Your Own!**
>
> [LMS Activity: Unit 2 Lesson 7 - Packet Protocol]
>
> Develop a protocol so the entire message below can be sent, where both the sender and receiver can be confident the entire message was received:
>
> ```
> Hi Sally! Do you want to meet for lunch?
> ```
>
> **Guidelines:**
> - Each packet can only contain **8 ASCII characters** of the message.
> - The sender and receiver must be sure that the entire message was successfully transmitted and reconstructed.
> - Think about what information needs to be included in each packet. (Hint: you'll need more than just the message text!)
>
> In your post, explain everything you think will need to go into each packet to successfully send the message above.
>
> Between the 4 people in your group, determine the "best" protocol --- which could be a combination of different posts.
>
> You must post before you can see the other people in your group!

After you've given that a shot, watch this video to see how the real internet handles packets, routing, and reliability:

[Video: Packets, Routing & Reliability](https://www.youtube.com/watch?v=AYdF7b3nMto)

## Check for Understanding

[LMS Activity: Unit 2 Lesson 7 - Check for Understanding]

## What's Next

So now we've got IP addresses for finding computers and TCP/UDP for breaking messages into packets and getting them where they need to go. But there's still a nagging question: nobody wants to type `209.152.46.213` into their browser. We want to type `www.pcc.edu`. In the next lesson, we'll learn about the DNS --- a massive system that acts like a phone book, mapping human-friendly URLs to their numeric IP addresses.
