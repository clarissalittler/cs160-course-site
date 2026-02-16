# Lesson 9 --- HTTP

**After this lesson, you'll be able to:**

- Explain how the HyperText Transfer Protocol works to transmit website information.

## HyperText Transfer Protocol (HTTP)

Alright, let's learn about the last big piece of the puzzle: a protocol called **HTTP**. You've definitely seen these letters before --- they're right there in your browser's address bar every single day:

> **https://www.pcc.edu**
>
> **H**yper**T**ext **T**ransfer **P**rotocol **S**ecure

*Figure 2.15. HTTP*

HTTP stands for **HyperText Transfer Protocol**. It's the underlying protocol used by the World Wide Web, and it defines how messages are formatted and transmitted, and what actions web servers and browsers should take in response to various commands.

Here's the simple version: when you type a URL into your browser, your computer sends an HTTP command to a web server saying, "Hey, send me this page." The server gets the request, finds the page, and sends it back. That's the basic transaction that happens every single time you visit a website.

The other main standard that controls how the web works is **HTML** (HyperText Markup Language), which defines how web pages are formatted and displayed. HTTP gets you the data; HTML tells your browser how to show it.

As you watch the video below, take notes on:

- What problem is HTTP solving?
- What is a GET request, and what are you requesting?
- How does HTTP rely on the other layers of the internet?
- Why are SSL, TLS, and HTTPS necessary?
- What do certificate authorities do, and why are they necessary?

[Video: HTTP & HTML](https://www.youtube.com/watch?v=kBXQZMmiA4s)

When you visit a website, you're actually getting sent a *file* by a server. HTTP solves the problem of how to ask for that file. All of your communications are sent over the internet, so these requests travel inside TCP/IP packets over the physical wires we talked about earlier. Everything we've been learning is layered on top of everything else --- it all works together.

There are also secure ways of sending information beyond plain HTTP, which sends everything as plain text. (Yes, really --- plain text, readable by anyone who intercepts it. Not great.) That's where HTTPS comes in, with encryption. **Certificate authorities** are the organizations that verify you're actually talking to the website you think you're talking to when you start a secure connection. Without them, someone could pretend to be your bank's website, and you'd have no way to tell.

## HTTP Requests --- Under the Hood

Here's something kind of remarkable: HTTP is an **ASCII text-based protocol**. That means at a fundamental level, computers are just sending each other plain text messages back and forth. No special binary encoding --- just structured text. Each protocol simply defines the rules of the "conversation" between two machines.

As we've learned, HTTP is the protocol clients (that's you, on your computer or phone) use to request and receive data like web pages, images, video, audio, and files from the servers that store them.

A client sends a **request** to a server with an identifier for the data it wants, and the server **responds** --- typically by sending back the requested information.

![HTTP client server communication: HTTP request from client, server sends back HTTP response](images/http_1.png)
*Figure 2.16. HTTP Client-Server communication (Image Source: [Code.org](https://code.org/))*

When you type a URL in your browser, your computer (the client) needs to "ask" the server storing the web page to send back its contents so your browser can display it. To do this, your computer sends an ASCII-text message called an **HTTP request**. Here's what a simple request for an image might look like:

![HTTP request includes: method (POST or GET), resource (file location), HTTP version, headers](images/http_2.png)
*Figure 2.17. Simple HTTP request for image (Image Source: [Code.org](https://code.org/))*

When the server receives an HTTP request, it responds with a message of its own. Once again, the response is sent entirely in ASCII text and must be correctly formatted. Here's a sample HTTP response:

![HTTP response includes: HTTP version, status code, headers, and body](images/http_3.png)
*Figure 2.18. Sample HTTP response (Image Source: [Code.org](https://code.org/))*

You might have encountered HTTP status codes before without realizing it. Ever seen a "404 Not Found" error? That's an HTTP status code --- the server is telling your browser, "I looked for what you asked for, and it doesn't exist." There's also the dreaded "500 Internal Server Error" (something broke on the server's end) and the satisfying "200 OK" (everything worked perfectly). These little numeric codes are part of every HTTP response.

## Putting It All Together

HTTP is the protocol for transmitting website information to you. And now we can see how all the layers of the internet work together:

1. You type `www.pcc.edu` into your browser.
2. The **DNS** translates that human-friendly name into an IP address.
3. Your browser sends an **HTTP request** to that IP address, asking for the web page.
4. **TCP** breaks that request into packets, and **IP** routes them to the right server.
5. The server sends back an **HTTP response** with the page content, again via TCP/IP.
6. Your browser reassembles the packets and renders the page.

All of this happens in a fraction of a second. The systems are autonomous, standardized, and layered --- and that's exactly what makes the internet work.
