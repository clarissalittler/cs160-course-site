## Unit 2 Quiz — The Internet

### Multiple Choice

**1.** Your cousin insists the Internet is one giant computer owned by a single company. Which description is actually accurate?
- A) A single supercomputer in the US that every device dials into
- B) A huge collection of interconnected networks — computers, routers, cables, and wireless links — that no one organization owns
- C) A program that comes pre-installed on your computer
- D) Another name for the World Wide Web browser

**2.** A construction crew accidentally cuts a fiber-optic cable across town, yet your video call doesn't even hiccup. What property of the Internet's design saved you?
- A) Redundancy — there are multiple paths between any two points, so routers just send packets a different way
- B) Compression — the packets shrink small enough to jump the gap in the cable
- C) Bandwidth — a fast enough connection can't be interrupted
- D) Caching — your computer had already downloaded the rest of the call

**3.** A brand-new startup builds a gadget nobody has ever seen before, and it connects to the Internet on day one with no special permission from anyone. What makes that possible?
- A) The gadget maker paid a licensing fee to the company that owns the Internet's rules
- B) The government inspects and approves each new device model
- C) Internet protocols are open standards — anyone can look up the rules and build hardware or software that follows them
- D) The startup got lucky; most new devices are rejected by the network

**4.** Which of these could be a real IPv4 address?
- A) 203.0.113.25
- B) 192.168.300.1
- C) www.pcc.edu
- D) 2, 5, 0, 7

**5.** You email a photo, and its packets travel different routes and arrive at your friend's computer out of order — with one packet missing entirely. Under TCP, what happens?
- A) The transfer fails and the whole photo must be sent again from scratch
- B) The photo arrives scrambled, with the missing chunk left blank
- C) Ordering information in the packet headers lets the message be reassembled, and the unacknowledged packet gets re-sent
- D) The routers along the way guarantee packets always arrive in order, so this can't happen

**6.** You type `www.pcc.edu` into your browser. What job does DNS perform in that moment?
- A) It encrypts your connection so nobody can snoop on it
- B) It looks up the IP address that goes with that name — like a big phone book for the Internet
- C) It breaks your request into packets for transmission
- D) It stores a backup copy of the PCC web page

### True / False

**7.** For your WiFi (a link-layer protocol) to do its job, it needs to understand your whole request — for example, it has to know that the bits it's carrying are part of a web page.

**8.** In HTTP/1.1 — the classic version of the protocol — the request your browser sends to a web server is a plain, human-readable ASCII text message.

### Short Answer

**9.** Your roommate types `www.pcc.edu` into a browser and the page just... appears. In 2–3 sentences, describe what happened behind the scenes — name the jobs that **DNS**, **HTTP**, and **TCP/IP** each did.

**10.** In 1–3 sentences: what principle does "net neutrality" refer to, and where do US net-neutrality rules stand as of the situation described in this unit (after early 2025)?
