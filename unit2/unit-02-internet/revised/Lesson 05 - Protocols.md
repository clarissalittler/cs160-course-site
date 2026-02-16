# Lesson 5 --- Protocols

**After this lesson, you'll be able to:**

- Explain why protocols are necessary for communication on the internet.

## The protocol suite

![A book with the title 'Rule Book'](images/rule_book.png)

There are *billions* of devices connected to the internet, and hundreds of different *kinds* of devices: laptops, tablets, phones, smart refrigerators, handheld credit card readers, and so on. So how do they all know how to find and talk to each other?

**Protocols** --- communication standards --- ensure that this incredible variety of devices can interact smoothly. Think of protocols as the rule book for communicating on the internet. Everyone agrees to follow the same rules, and that's what makes the whole thing work.

These protocols are **open** (available for anyone to use), which means *anyone* can build systems that connect to the internet. You don't need permission from some gatekeeper. That openness is a huge part of why the internet grew so fast.

Here's the key idea: protocols are organized into **layers**, and each layer handles a different part of the job.

Take a look at Figure 2.9. When a request is made from the device on the left, it gets passed *down* through the different layers, then *across* the network, then *up* the same layers to the destination device on the right. Each layer is an **abstraction** --- it does its specific job and then hands things off to the next layer. Nobody has to worry about what the other layers are doing. It's a beautifully modular design.

![Layers of protocols animation](images/protocols.gif)
*Figure 2.9. Protocol Layers*

Let's take a quick tour of each layer, from the bottom up.

## Link layer protocols

**Link Layer Protocols** (like WiFi) manage the connection between your device and its local network. These are the least abstract layer because they deal directly with your physical hardware --- the actual radio signals, cables, &c. that connect your device to the network in your house or office.

## Internet layer protocols

**Internet Layer Protocols** (like IP) manage the pathways that data packets travel across networks. The routers we just learned about? They're using IP to move information to its destination. These protocols provide an abstraction that makes the internet look like one giant network, even though the physical reality underneath is a patchwork of many smaller subnetworks stitched together.

## Transport layer protocols

Here's something to think about: it would be impossible to send a large file --- like an image or a movie --- in one single packet. The data needs to be broken up into smaller packets, and those packets might even take *different routes* to get to the destination. Wild, right?

**Transport Layer Protocols** (like TCP or UDP) handle this. They manage breaking a message into packets for the lower layers to transmit, and then they reassemble the message from all those packets once they arrive. It's like shipping a jigsaw puzzle in separate envelopes and then putting it back together on the other end.

## Application layer protocols

**Application Layer Protocols** (like HTTP and DNS) are the highest level of abstraction. They manage how data is *interpreted and displayed* to users. These protocols give meaning to the bits sent by the lower layers --- your computer and the server you're talking to need to agree on what those bits actually *mean*, and application protocols handle that agreement.

## The big picture

All of these are **open standards**. Anyone can look up a protocol and write code with it to make new hardware or software --- no permission needed. The internet is probably the largest and most complicated artifact in human history, and it runs on cooperation. That's kind of remarkable when you think about it.

Let's dive deeper into each of these protocol layers in the upcoming lessons.
