# Lesson 6 -- Encryption: Symmetric and the Caesar Cipher

**At the end of this lesson, you will be able to:**

- Explain why encryption is necessary for secure communication
- Describe how symmetric encryption works using the Caesar Cipher as an example
- Encrypt and decrypt messages using a Caesar Cipher
- Explain the key distribution problem and why it matters

## Why encryption matters

Back in Unit 2, you learned about how the internet works -- how data travels in packets from your computer through a series of routers and networks before reaching its destination. Here's the thing about that journey: your data passes through a lot of equipment you don't control. Your ISP's routers, backbone networks, possibly networks in other countries. Without encryption, any of those intermediate points could *read your data*. Your emails, your passwords, your bank information -- all of it, just sitting there in plain text for anyone along the path to see.

Encryption is what prevents this. It scrambles your data so that even if someone intercepts it in transit, all they see is gibberish. Only the intended recipient -- who has the right key -- can unscramble it and read the original message.

This isn't a hypothetical concern, by the way. Before encryption became widespread on the web, there were real attacks where people on the same Wi-Fi network (say, at a coffee shop) could use freely available tools to read other people's web traffic. Your Facebook messages, your login credentials, everything. The tool that made this easy was called Firesheep, and when it was released in 2010, it scared a *lot* of companies into finally encrypting their websites.

## The basic idea

Encryption follows a straightforward pattern:

1. You start with a **plaintext** message -- the thing you actually want to say.
2. You apply a **key** and an encryption algorithm to transform it into **ciphertext** -- scrambled nonsense.
3. The recipient uses the key (and the reverse of the algorithm) to transform the ciphertext back into plaintext.

That's the core of it. The details of step 2 vary enormously depending on which encryption scheme you're using, but the overall shape is always the same: plaintext goes in, ciphertext comes out, and only someone with the key can reverse the process.

Let's start with the simplest possible example.

## The Caesar Cipher

The Caesar Cipher is the oldest known encryption technique. It's named after Julius Caesar, who reportedly used it for military correspondence. (Whether this actually made his messages secure is another question -- we'll get there.)

Here's how it works: you pick a number (the key), and you shift every letter in your message forward by that many positions in the alphabet. If the shift is 3:

- A becomes D
- B becomes E
- C becomes F
- ...
- X becomes A (it wraps around)
- Y becomes B
- Z becomes C

So the message `hello` with a shift of 3 becomes `khoor`.

To decrypt, the recipient just shifts back by the same amount. They know the key is 3, so they shift each letter back 3 positions: K becomes H, H becomes E, &c.

It's delightfully simple. And, as we'll see, delightfully breakable.

## Activity: crack this message

Here's a message that's been encrypted with a Caesar Cipher:

**serr cvmmn va gur ybhatr**

Your mission: figure out what it says. Here are some tips:

- Look for short words first. `va` is only two letters -- how many common two-letter English words are there? `in`, `is`, `it`, `an`, `at`, `on`, `or`, `of`... that's a pretty short list.
- Once you figure out the shift for one word, the same shift applies to every other letter in the message. The alphabet is shifted uniformly, not randomly scrambled.
- Try different shifts on that short word until something looks like English.

Give it a real try before reading the solution below. Seriously -- it's more fun if you work it out yourself.

---

**Solution:** The shift is 13 (each letter has been moved forward 13 positions). This particular shift is so commonly used that it has its own name: **ROT13** (short for "rotate by 13"). It has a fun property -- since the alphabet has 26 letters and 13 is exactly half of that, applying ROT13 twice gets you back to the original. The same operation both encrypts and decrypts.

The message is: **free pizza in the lounge**

(Sorry, there is no actual free pizza. But if there were, I would want to encrypt that information to keep the pizza for myself.)

If you want to play with encryption more interactively, check out the [Code.org encryption widget](https://studio.code.org/s/hoc-encryption/stage/1/puzzle/1) -- it lets you experiment with shifting ciphers hands-on.

## Why the Caesar Cipher is terrible security

Now that you've (hopefully) cracked that message, let's talk about why. The Caesar Cipher has a fatal flaw: **there are only 25 possible keys** (shifts of 1 through 25 -- a shift of 0 or 26 would just give you the original message). An attacker doesn't need to be clever. They can just try all 25 possibilities and see which one produces readable English. That's a brute force attack, and when you only have 25 things to try, it takes about ten seconds by hand and a fraction of a millisecond for a computer.

Even in Caesar's time, this wasn't exactly bulletproof. It worked mostly because a lot of the people intercepting messages were illiterate, and the concept of letter substitution wasn't widely known. Security through obscurity, as they say -- which is not real security at all.

Modern encryption algorithms have keys that are astronomically larger. AES-256, which is the standard used to protect everything from your bank transactions to classified government documents, uses keys that are 256 bits long. That means there are 2^256 possible keys -- a number so large that if every atom in the observable universe were a computer trying a billion keys per second, they still wouldn't get through all the possibilities before the heat death of the universe. *That's* what real brute-force resistance looks like.

But the underlying *principle* is the same as the Caesar Cipher. You have a key, you use it to scramble data, and the recipient uses the same key to unscramble it. Which brings us to...

## Symmetric encryption

The Caesar Cipher is an example of **symmetric encryption**. "Symmetric" because the same key is used on both sides -- to encrypt *and* to decrypt. The sender and the receiver share a secret, and that shared secret is what makes the whole thing work.

Modern symmetric encryption algorithms like **AES** (Advanced Encryption Standard) are vastly more sophisticated than shifting letters around. They chop your data into blocks, run it through multiple rounds of complex mathematical transformations, and produce ciphertext that is -- for all practical purposes -- unbreakable without the key. But the core principle is the same one Caesar used: both parties need to know the same secret key.

AES is what protects your data in a staggering number of places. When your phone encrypts its storage, that's probably AES. When you connect to a secure website, AES is likely doing the bulk of the encryption. When the government classifies something Top Secret, the encryption standard they use is -- you guessed it -- AES. It's been mathematically analyzed for decades, and nobody has found a practical way to break it. It's one of those rare things in technology that genuinely just *works*.

## The key distribution problem

So symmetric encryption is great. AES is basically unbreakable. Problem solved, right?

Not quite. There's a catch, and it's a big one: **how do you share the key?**

Think about it. You want to send an encrypted message to your friend. You both need the same key. But you can't just send the key over the internet -- if someone is eavesdropping (which is the whole reason you're encrypting in the first place), they'll intercept the key. And then they can decrypt everything.

You could meet your friend in person and exchange the key face-to-face. That works! But it doesn't scale. What about websites you've never visited before? What about online stores in other countries? You can't fly to every website's headquarters and do a secret handshake before buying something online.

You could try encrypting the key itself before sending it. But... with what key? You'd need to share *that* key first. It's turtles all the way down.

This is called the **key distribution problem**, and for most of the history of cryptography, it was considered fundamentally unsolvable. If you wanted to use symmetric encryption, you needed a secure way to exchange keys first, and usually that meant physical couriers, diplomatic pouches, or meeting in person.

This problem bugged cryptographers for a long time. And then, in the 1970s, someone figured out an absolutely brilliant solution. But that's the next lesson.

## Discussion questions

1. **Try encrypting a short message with a Caesar Cipher** (pick your own shift) and post it for a classmate to decode. Include a hint if you're feeling generous.

2. **Why do you think the Caesar Cipher was effective in its time but isn't now?** What changed?

3. **The key distribution problem seems simple, but it stumped very smart people for a very long time.** Can you think of any clever solutions before reading the next lesson? (Don't worry if you can't -- the actual solution is genuinely surprising.)
