# Unit 2 Summary

## Wrap Up

Over the past several lessons, we've built up a picture of how the internet actually works --- layer by layer, protocol by protocol. The systems that let you connect to any website on the planet are a collection of autonomous, standardized protocols that all work together. No single company or government controls all of it. It just... works, because everyone agreed on the same rules.

Here's the journey your computer takes every time you visit a website: the **DNS** converts the URL you typed --- something like `pcc.edu` --- into a numeric IP address. Using that IP address, your computer knows exactly where to go to connect to, communicate with, and ultimately display the website you're looking for.

These standards and autonomous systems, along with the internet's hierarchical structure, are what allowed it to become truly global in scale. Nowadays there isn't a country in the world without internet access. And the internet keeps growing. Because the protocols are open and standardized, anyone can build something new on top of them, knowing that everyone else will be able to access it immediately --- as long as it follows the rules.

## Summary

Here's everything that happens when you type a website name into your browser, condensed into one tidy list:

- **DNS lookup:** Your browser contacts the DNS to find the IP address for the website name you typed.
- **HTTP request:** Once you have the address, your browser sends an HTTP GET request to the website, asking it to send you its homepage.
- **Server response:** The website's server responds with the HTML code that makes up the web page.
- **Transport layer:** All of these communications happen over the internet, which means TCP or UDP breaks each message into packets and sends them. If TCP is used, error checking ensures nothing gets lost.
- **IP routing:** IP routes the packets back and forth between your computer and the server.
- **Physical layer:** All of this information travels over the physical wires, cables, Wi-Fi networks, and routers that make up the physical infrastructure of the internet.

Every layer depends on the ones below it, and each one solves a specific problem. Together, they give us the internet as we know it.

## Additional Resources
