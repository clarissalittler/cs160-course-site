# Lesson 8 --- The Need for DNS

**After this lesson, you'll be able to:**

- Explain how URLs like www.pcc.edu are translated into IP addresses.
- Explain how the DNS helps the internet scale.

## Domain Name System (DNS)

Here's a problem. Devices are joining and leaving the internet *all the time*. Your phone gets a new IP address when you walk into a coffee shop. Your laptop might get a different one when you reconnect to a different network. IP addresses aren't permanent --- they shift around constantly.

If every computer tried to keep its own list of which IP address belongs to which website... well, that list would be out of date before you finished writing it. It would be like trying to maintain a phone book for a city where everyone moves every week. Chaos.

So instead of making every device track this on its own, what if there were one big system that kept track of all that information?

That's exactly what the **DNS** --- the **Domain Name System** --- is. When you type a website address like `my.pcc.edu` into your browser, your computer asks a DNS server, "Hey, what's the IP address for this?" And the DNS server looks it up and sends back the answer. It's essentially a giant phone book for the internet.

![DNS lookup - server looks up address in a table](images/dns_phonebook.png)
*Figure 2.13. DNS lookup table*

If we want the internet to scale up to *billions* of devices --- which it has --- we absolutely need a system like this.

## Hierarchy of Servers

Now, you might be wondering: one server can't possibly keep track of every single domain name on the entire internet, right? You're correct. That would be a single point of failure, and engineers hate single points of failure.

Instead, the DNS is organized as a **hierarchy of servers**. When your computer asks its local DNS server for an address and that server doesn't know it, the request gets passed up the chain to bigger, more authoritative servers until someone has the answer. It's like asking a librarian for a book --- if they don't have it, they know which library to call.

![Hierarchy of servers - computer asks DNS for address, if not found, the DNS will ask another DNS](images/dns_example.png)
*Figure 2.14. DNS is a hierarchy of servers*

The video below picks up at 4:09 to finish the discussion of DNS. (We watched the first part in Lesson 6 when we covered IP addresses.) As you watch, take notes on:

- How does the DNS solve the problem of translating names like www.pcc.edu into IP addresses?
- How does the DNS help the internet scale?

[Video: The DNS](https://www.youtube.com/watch?v=5o8CwafCxnU)

## Try a DNS Lookup

Let's see DNS in action. Open the [DNS Lookup](https://mxtoolbox.com/DNSLookup.aspx) tool and type in `www.pcc.edu`.

What IP address did you get?

This is the whole point of DNS. Most humans find it *way* easier to remember words than numbers. If you tell someone to go to `www.pcc.edu`, they'll probably remember that. If you tell them to go to `209.152.46.213`... good luck. DNS bridges that gap --- it lets us use memorable names while computers quietly do their thing with numbers behind the scenes.

## A Note on Security

Here's something worth knowing: the DNS was not originally designed to be secure. It was built in the early days of the internet, when the network was small and people mostly trusted each other. That trust, unfortunately, has led to some major security incidents over time. Attackers have found clever --- and sometimes alarming --- ways to exploit DNS.

In Lab 2, you'll learn about some of these attacks and how they work. It's a good reminder that even the most fundamental systems on the internet can have surprising vulnerabilities.
