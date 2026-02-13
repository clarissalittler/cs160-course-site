# Lesson 7 -- Encryption: Public Key Cryptography

**At the end of this lesson, you will be able to:**

- Explain the key distribution problem that public key cryptography solves
- Describe how public and private keys work together using the mailbox analogy
- Explain how HTTPS uses public key cryptography to secure web browsing
- Discuss the social and political implications of strong encryption

## The problem (recap)

Last lesson we ended on a cliffhanger. Symmetric encryption -- like AES -- is incredibly strong. If both parties have the same key, their communication is effectively unbreakable. But there's a catch that seemed impossible to get around: how do you share the key securely in the first place?

If you send it over the internet, someone could intercept it. If you encrypt it... well, you'd need another key for that, and you'd need to share *that* key, and now you're going in circles. Meeting in person works, but it doesn't scale -- you can't physically visit every website you want to buy something from.

For most of the history of cryptography, the assumption was that secure communication required a pre-shared secret. And then someone had one of the most important ideas in the history of computer science.

## The breakthrough

In the 1970s, Whitfield Diffie and Martin Hellman published a paper describing a way to establish a shared secret over a completely public channel. Around the same time -- actually slightly earlier -- a team at the British intelligence agency GCHQ (James Ellis, Clifford Cocks, and Malcolm Williamson) independently figured out the same thing. But because they worked for a spy agency, their work was classified and they couldn't publish it or take credit for it until decades later. The history of cryptography is full of stories like this -- brilliant ideas locked away because governments wanted to keep them secret.

What they all figured out was this: you don't *need* to share a secret key. Instead, you can use a pair of keys -- one public, one private -- that are mathematically related in a very specific way. This is **public key cryptography** (also called asymmetric cryptography, because the two keys are different from each other, unlike symmetric encryption where both sides use the same key).

## The mailbox analogy

The math behind public key cryptography is genuinely hard -- it involves number theory, modular arithmetic, and some properties of very large prime numbers that are not exactly beginner-friendly. But the *concept* is something you can understand perfectly with an analogy.

Imagine you have a special mailbox with two keys:

- The **public key** can only *lock* the mailbox. It can close the slot and seal it shut, but it cannot open it.
- The **private key** can only *unlock* the mailbox. It's the only way to open it and read what's inside.

Here's the clever part: you make a thousand copies of the public (locking) key and hand them out to everyone. Post it on your website. Put it in your email signature. Shout it from the rooftops. It doesn't matter who has it, because all they can do with it is lock the mailbox -- they can't open it.

Now, anyone in the world can put a message in your mailbox and lock it. But only you -- with your private key -- can open it and read the message.

Even the person who *sent* the message can't get it back. Once they've locked the mailbox with your public key, they can't unlock it. Only the private key can do that.

That's public key cryptography. No secret exchange. No meeting in person. No trusting a courier. You publish your public key for all the world to see, and anyone can send you an encrypted message that only you can read.

## How it works (conceptually)

Let's make this a bit more precise, without getting into the actual math:

- Everyone generates a **key pair**: one public key and one private key. These two keys are mathematically related -- they're created together, and what one does, only the other can undo.
- Your **public key** is shared with the world. Anyone can have it.
- Your **private key** is kept completely secret. You never share it with anyone, ever. It never leaves your device.
- If I want to send you an encrypted message, I take your **public key** and use it to encrypt the message. The result is ciphertext that can *only* be decrypted by your private key.
- You receive the ciphertext and use your **private key** to decrypt it. Now you can read my message.
- **Nobody else can decrypt it** -- not me (even though I encrypted it), not anyone who intercepted it in transit, not even someone who has your public key. Only the private key works.

The beauty of this is that the entire exchange can happen over a completely insecure channel. An attacker can watch every single packet of data you exchange and they *still* can't read the message. They can see your public key (doesn't help them -- it can only encrypt, not decrypt). They can see the ciphertext (doesn't help them -- they'd need the private key to decrypt it). The private key never travels over the network at all.

It's kind of mind-bending when you first think about it. Two people who have never met, who have never exchanged any secret information, can communicate securely over a channel that's being actively monitored. This was a genuinely revolutionary idea.

## HTTPS and TLS: public key crypto in your browser

Remember HTTP from Unit 2? The protocol your browser uses to request and receive web pages? Well, **HTTPS** is HTTP with encryption layered on top. The "S" stands for "Secure." When you see the padlock icon in your browser's address bar, that means the connection between your computer and the website is encrypted.

Here's roughly what happens when you visit an HTTPS website:

1. Your browser says "hi" to the server and they agree on what encryption methods they support.
2. The server sends your browser its **public key** (packaged in something called a certificate, which also proves the server is who it claims to be).
3. Your browser uses the server's public key to encrypt a shared secret and send it back.
4. Now both your browser and the server have the shared secret, and they use it to set up **symmetric encryption** (like AES) for the rest of the conversation.

Wait -- did you catch that? They use public key cryptography to exchange a symmetric key, and then they switch to symmetric encryption for the actual data. Why? Because symmetric encryption is *much* faster than public key encryption. Public key crypto solves the key distribution problem, and then symmetric encryption handles the heavy lifting. It's the best of both worlds.

This whole process is called **TLS** (Transport Layer Security), and it happens in a fraction of a second, invisibly, every time you visit a secure website. You've probably done it thousands of times today without knowing it.

## Digital signatures: the reverse trick

Here's something cool: public key cryptography can also work in the other direction, and it solves a completely different problem.

We said the public key encrypts and the private key decrypts. But you can also *sign* something with the private key, and anyone with the public key can *verify* that signature.

Why would you want to do this? **Authentication.** When you download a software update, how do you know it actually came from the developer and wasn't tampered with by an attacker? The developer signs the update with their private key. Your computer checks the signature using the developer's public key. If the signature checks out, you know two things: the update really came from the developer (because only they have the private key), and it hasn't been modified in transit (because any change would invalidate the signature).

Digital signatures are everywhere, working quietly in the background. They're how your operating system verifies that software updates are legitimate. They're how your browser knows that a website's certificate is real. They're how cryptocurrency transactions are authorized. It's one of those technologies that does enormous amounts of important work without most people ever knowing it exists.

## Why this matters for your everyday life

Here's the thing -- public key cryptography isn't some abstract academic topic. It's working for you right now, in the background, constantly:

- Every time you buy something online, public key cryptography is protecting your credit card number.
- Every time you log into your bank, it's verifying that you're really talking to your bank and not an imposter.
- Every time you send a private message on a platform that uses end-to-end encryption (like Signal or WhatsApp), public key crypto ensures that only you and the recipient can read it.
- Every time your phone installs a software update, digital signatures verify it's legitimate.

Without public key cryptography, secure commerce on the internet would be essentially impossible. You'd have to physically visit your bank to transfer money. You couldn't safely buy anything online. Every email would be a postcard that anyone could read.

It's no exaggeration to say that public key cryptography is one of the foundations of the modern internet. And it all comes from that one insight in the 1970s: you don't need to share a secret to communicate securely.

## A brief history: the Crypto Wars

Here's an interesting tangent that's also deeply relevant to current events.

When public key cryptography was first developed, the US government was... not thrilled. Strong encryption meant that ordinary people -- and, yes, criminals and foreign governments -- could communicate in ways the government couldn't intercept and read. For decades, the National Security Agency (NSA) had been able to eavesdrop on communications when it needed to (with appropriate legal authority, at least in theory). Strong, widely available encryption threatened that capability.

So the government tried to control it. Certain encryption algorithms were classified as **"munitions"** under US export law -- yes, the same legal category as missiles and tanks. It was literally illegal to export strong encryption software. There's a famous story of a programmer named Phil Zimmermann who created an encryption program called PGP (Pretty Good Privacy) and was investigated by the government for three years because the software spread internationally over the internet.

In an act of delightful protest, people printed the source code of encryption algorithms on T-shirts and in books -- technically making the wearer or reader an "arms dealer" under the law. This period, running through most of the 1990s, is known as the **Crypto Wars**.

Eventually, the export restrictions were relaxed, and strong encryption became available to everyone. This is directly why you can do secure online banking today.

But many people argue we're now in a **second round of Crypto Wars**. Governments around the world -- including the US, UK, EU, and Australia -- have at various times proposed or enacted laws requiring tech companies to build **"backdoors"** into their encryption. The argument is that law enforcement needs to be able to read communications with a warrant, and end-to-end encryption makes that impossible.

The counterargument from cryptographers and security researchers is that there is no such thing as a backdoor that only the "good guys" can use. If you build a weakness into an encryption system, *anyone* who discovers it can exploit it -- including foreign governments, criminals, and hackers. A backdoor for the FBI is also a backdoor for the Chinese government. You can't have it both ways.

This debate is ongoing and genuinely difficult. Both sides have legitimate concerns. It's one of those places where technology, law, ethics, and politics all crash into each other.

## Discussion questions

1. **In your own words, explain how public key cryptography solves the key distribution problem.** Try explaining it to someone who hasn't read this lesson -- if you can explain it clearly, you understand it.

2. **Should governments be able to require backdoors in encryption?** Think about both sides:
   - Law enforcement argues that encrypted communications can shield criminals, terrorists, and child abusers from investigation. Without some way to access communications with a legal warrant, dangerous people can operate with impunity.
   - Security researchers argue that any backdoor weakens security for everyone. A backdoor can be discovered and exploited by malicious actors. And authoritarian governments could use mandated backdoors to surveil journalists, activists, and political dissidents.
   - Where do you come down? Is there a middle ground?

3. **Think about the Crypto Wars.** The government tried to restrict strong encryption, lost, and now we all benefit from secure online communication. Does this story change how you think about government regulation of technology? Why or why not?
