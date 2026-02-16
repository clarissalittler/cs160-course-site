# Lesson 2 --- Internet Issues

**After this lesson, you'll be able to:**

- Identify the communities of people who control how the internet works.
- Describe 3 different societal issues: net neutrality, internet censorship, and the digital divide.

## Who owns the internet?

Some people think nobody's in charge of the internet --- that everyone just cooperates freely with no central organization. And there's a grain of truth to that! Free cooperation plays a huge role. But you can't just pick any IP address or hostname you want, or there'd be conflicts everywhere. *Someone* has to keep the trains running on time.

For most of the internet's history, the domain name hierarchy --- that's the system of website names --- was controlled by the United States government, with the details delegated to **ICANN** (the Internet Corporation for Assigned Names and Numbers).

> **More on the ICANN agreement:** In 2009, the US Department of Commerce signed a new agreement with ICANN recognizing it as a more independent, multinational organization. Then in 2016, the US government completed the **IANA stewardship transition**, formally handing control of core internet functions to the global ICANN community. Whether ICANN is truly independent of US influence is still debated. It's... complicated.

The growth of the internet has been fueled by **open protocols** --- standards that aren't owned by any company. That's a big deal. Examples of open protocols include:

- Standards for sharing information and communicating between browsers and servers on the web
- Standards for packets and routing information

These protocols change over time, and the **Internet Engineering Task Force (IETF)** are the experts in charge of developing and approving them.

> **More on the IETF:** Here's something kind of remarkable. The work of the IETF is done largely by email, and anyone with the necessary expertise can join the mailing lists. Decisions are made by *consensus* --- everyone has to agree --- never by voting. The idea is that if a proposal is controversial enough to need a vote, it should be improved until everyone's objections are satisfied. Unlike ICANN, the IETF has been remarkably free from political pressure, even though it's historically been dominated by US experts. The **Internet Society (ISOC)** is a worldwide nonprofit membership society that anyone can join for free. It's now officially in charge of the IETF and also promotes government policies supporting an open internet.

If you think it's strange for one country to control a worldwide network, you're not alone. Other countries have never been happy about US control of the internet. The formal US stewardship didn't end until 2016, and according to many critics, US influence remains dominant even now.

Here's a fun example of how that played out: until 2010, all DNS domain names had to use the English alphabet, despite constant requests to accommodate other languages. Imagine trying to navigate a global network that only speaks one language's characters. Not great.

The issue of US control became much more heated in 2013 when [Edward Snowden](https://en.wikipedia.org/wiki/Edward_Snowden) exposed the US National Security Agency (NSA) for spying on internet traffic worldwide. How these concerns will eventually be resolved is still an open question.

## How did the US end up in charge?

Here's the short version of a very interesting story.

In 1968, the **Advanced Research Projects Agency (ARPA)** of the US Department of Defense announced they were developing a large-scale packet-switched network. In 1969, the first connections were made among four university research groups. At its peak, the ARPANET reached a few hundred computers. (All of them were owned either by military installations or by computer science research labs, mostly at universities. This was *not* something regular people had access to.)

![The evolution of ARPANET, 1969-1982](../images/arpanet.png)
*Figure 2.2. The evolution of ARPANET, 1969--1982 (Image Source: [The Daily Swig](https://portswigger.net/daily-swig/arpanet-anniversary-the-internets-first-transmission-was-sent-50-years-ago-today))*

The ARPANET was tiny, but it inspired the protocols that became the foundation of the internet. And it belonged to the US military. So there you go --- that's how one country ended up with the keys.

The **Internet Protocol (IP)** was defined in 1981, and on January 1, 1983 --- a date sometimes called "flag day" --- the ARPANET officially switched to TCP/IP, the protocol suite the internet still uses today. That made the ARPANET just one network among many, and it was decommissioned in 1990. Meanwhile, in 1981, the **National Science Foundation (NSF)** had built the core of a new cross-country network. At that time, businesses still weren't allowed on the network, but the demand was clearly there. So commercial IP-based networks were created, and the rest is --- well, the internet as we know it.

## Societal issues

There are many societal issues with the internet. Some are related to people taking advantage of the very open protocols that make the internet function, and they present us with genuinely tricky dilemmas. We'll learn more about protocols later in this unit, but for now, here are three big ones to think about:

### Net Neutrality

A raging legal debate about the principle that internet service providers should enable access to *all* content and applications regardless of the source --- without favoring or blocking particular products or websites.

> **Dig deeper into Net Neutrality:** Internet users love services like streaming movies, video chatting, and online gaming. All of this content needs to travel over the internet, and the companies that build and maintain networks are complaining about the increased demands on their infrastructure.
>
> - [How the end of net neutrality could change the internet](https://www.youtube.com/watch?v=HqXKEgTYZBQ) (video)
> - [Net Neutrality is ending. Here's how your internet could change](https://www.pbs.org/newshour/nation/net-neutrality-is-ending-heres-how-your-internet-use-could-change) (article)
> - [Wikipedia --- Net Neutrality](https://en.wikipedia.org/wiki/Net_neutrality)

### Internet Censorship

The attempt to control or suppress what can be accessed, published, or viewed on the internet by certain people. This can be used to protect people (preventing access to illegal content, for instance), but it can also be used to limit free speech. The line between "protecting people" and "silencing people" is blurrier than you might think.

> **Dig deeper into Internet Censorship:** While the internet is used to share many useful services and information, there are growing concerns about how it can spread damaging information --- from national secrets to calls for violence. Censoring this information may provide some people with increased security, but potentially risks free speech and the safety of social and political activists.
>
> - [Free Speech Or Hate Speech: When Does Online Hate Speech Become A Real Threat?](https://www.npr.org/2018/11/19/669361577/free-speech-or-hate-speech-when-does-online-hate-speech-become-a-real-threat) (audio article)
> - [Internet Censorship Explained](https://www.youtube.com/watch?v=6ohH-RkSLo4) (video)
> - [Wikipedia --- Internet Censorship](https://en.wikipedia.org/wiki/Internet_censorship)

### Digital Divide

While technology is increasingly woven into daily life, there are still many people who lack access to the internet or digital technology. In rural areas, there are real challenges building networks to connect geographically sparse populations. But even in cities, some communities have relatively less access to the internet --- or less knowledge of how to use it effectively.

> **Dig deeper into the Digital Divide:**
>
> - [Eliminating the Digital Divide](https://www.pbs.org/video/eliminating-digital-divide-ihdcln/) (video)
> - [Internet/Broadband Fact Sheet](https://www.pewresearch.org/internet/fact-sheet/internet-broadband/) (article)
> - [Wikipedia --- the Digital Divide](https://en.wikipedia.org/wiki/Digital_divide)

## Check for understanding!

[LMS Activity: H5P Check for Understanding]

To have an informed opinion on these issues, it really helps to understand the technical underpinnings of how the internet works. So let's get into it!
