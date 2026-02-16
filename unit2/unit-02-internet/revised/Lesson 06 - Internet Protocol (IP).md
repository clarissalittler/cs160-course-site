# Lesson 6 --- Internet Protocol (IP)

**After this lesson, you'll be able to:**

- Explain the role addressing plays in transmitting information over the internet.
- Develop an efficient protocol to play the game Battleship.

## Battleship

Have you ever played Battleship? You know --- the game where you call out grid coordinates and try to sink your opponent's hidden fleet? It turns out this simple board game is a surprisingly good way to understand some of the fundamental problems engineers had to solve when building the internet.

Seriously. Stick with me here.

[Video: How To Play Battleship](https://www.youtube.com/watch?v=4gHJlYLomrs)

We're going to play a *wild* version of this game. Instead of playing one cozy game against a single opponent, you'll be playing multiple games against multiple people *at the same time*. For this first round, grab some friends or family and play together. Later, you'll develop a formal protocol with four classmates.

## Rules

For each partner in your group, sketch a copy of the game board on a piece of paper. So if four people are playing, you'll need three boards --- one per opponent. Shade in boxes for your ships' locations in the "My board" sections. Ships are 2 units long and must be horizontal or vertical --- no diagonals allowed. You can place ships differently for each opponent. And obviously, don't show your board to anyone!

Record each hit with an "X" and each miss with an "O."

Watch the video below for a demo of the rules, then play the game several times. Pay close attention to what you actually *say* to the other players. That part matters more than you think.

[Video: Crazy Battleship Rules](https://www.youtube.com/watch?v=6noiQvpzEi0)

## Binary Battleship

Now that you've played a few rounds, here's where it gets interesting. We're going to create an **efficient binary protocol** for playing a 4-person game of Battleship with *no talking*. None. Zero words. Just 0s and 1s.

By "efficient," we mean your protocol should use the smallest reasonable number of bits while still containing all the information needed to actually play the game. Think back to those verbal games you just played --- what did you *have* to say each turn?

Let's brainstorm:

- We need to send all game information using only 0s and 1s.
- How do we standardize recipient and sender addresses?
- Should we encode people's names, or just assign everyone a number? (Spoiler: one of these is way more efficient than the other.)
- How would a recipient know where one address ends and another begins?
- What other information needs to be in each message?

These are exactly the kinds of questions that the designers of the internet had to wrestle with. You're basically doing protocol design right now. Welcome to computer science!

## Group Activity

> **Group Activity**
>
> You're going to develop an efficient protocol to play Battleship without talking --- using only 0s and 1s!
>
> [LMS Activity: Unit 2 Lesson 6 - Battleship Protocol]
>
> - Work with your study group for this discussion.
> - One person from your group will create a post with your 4-person Battleship protocol that uses only 0s and 1s.
> - Add all team member names to the post.
> - Make sure you explain what each of the bits represents.
> - Compare your protocol with the other groups who have posted.
> - Show what you would send using only 0s and 1s for the following plays:
>   - From player 1 to player 3, fire on A 2.
>   - From player 3 to player 1, miss on A 2.
> - Between the people in your study group, determine the "best" protocol --- which could be a combination of different posts.
>
> Please make only one post per team.

## Internet Protocol

So how does any of this Battleship stuff relate to the actual internet?

It turns out that computers on the internet are addressed in a remarkably similar way, for many of the same reasons. The real addresses used on the internet are called **Internet Protocol addresses** --- or **IP addresses** for short.

The Internet Protocol (IP) is a protocol --- a set of rules --- for routing and addressing packets of data so they can travel across networks and arrive at the correct destination. Think of it as the postal system of the internet.

An **IP address** is a unique identifier assigned to a device or domain that connects to the internet. There are two flavors: **IPv4** and **IPv6**. Each IPv4 address is a string of four numbers between 0 and 255, separated by dots --- something like `192.168.1.1`. Each of those numbers is really an eight-bit value, which means an IPv4 address is 32 bits total. (Sound familiar? You just designed something like this for Battleship!)

Nobody wants to memorize strings of numbers to visit a website, though. That's where DNS comes in --- it translates human-readable domain names into IP addresses. But we'll get to that in a couple of lessons.

The routers at every connection point on the internet run IP, which transmits packets from one IP address to another. Watch the video below for more on IP addresses and the difference between IPv4 and IPv6. (The video will stop before DNS at 4:09 --- we'll pick that part up later.)

[Video: IP Addresses & DNS](https://www.youtube.com/watch?v=5o8CwafCxnU)

## Check for Understanding

[LMS Activity: Unit 2 Lesson 6 - Check for Understanding]

## What's Next

We now know that Internet Protocol assigns unique addresses to every device connected to the internet, and routers use IP to move information to the right destination. But how does a large message actually *get* from point A to point B? In the next lesson, we'll dig into Transport Layer Protocols --- the protocols that break all of that information into manageable packets to be sent across the network.
