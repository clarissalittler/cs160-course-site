# Lesson 5 -- Passwords and Authentication

**At the end of this lesson, you will be able to:**

- Explain what makes a password strong and why length matters more than complexity
- Describe the main ways attackers crack passwords
- Explain what a password manager is and why you should use one
- Describe multi-factor authentication and why it's important

## Your password is the lock on the door

Let's start with something that might feel obvious but is worth saying out loud: your password is often the *only* thing standing between your accounts and someone who wants to break into them. Your email, your bank, your social media, your school accounts -- if someone gets your password, they're in. No alarm goes off. No security guard shows up. They just... log in as you.

And unlike a physical lock, where a thief has to be standing at your door, password attacks can come from anywhere in the world, run automatically, and try millions of combinations without getting tired.

So let's talk about what actually makes a password good -- because a lot of the "common wisdom" about passwords is wrong.

## What makes a password strong?

Here's something that surprises most people: **length beats complexity**. By a lot.

The password `P@ssw0rd!` looks fancy, right? It's got uppercase, lowercase, numbers, and special characters. It must be secure! Except... it's not. It's short, it follows predictable substitution patterns (@ for a, 0 for o), and password cracking tools already know about all of those substitutions. It's one of the first things they try.

Now consider: `correct horse battery staple`. Four random common words strung together. No special characters, no weird substitutions. But it's 28 characters long, and the combination of those four words is genuinely hard to guess. A brute-force attack would take astronomically longer to crack it.

This is from a famous [xkcd comic](https://xkcd.com/936/) that's worth looking at -- it explains the math behind why long passphrases beat short complex passwords better than I can in a few paragraphs. The basic insight is that every character you add to a password multiplies the number of possible combinations an attacker has to try, and multiplication adds up fast.

The takeaway: **make your passwords long.** A passphrase of several random words is both easier to remember and harder to crack than a short string of gobbledygook.

## How passwords get cracked

Attackers don't sit at a keyboard typing in guesses one at a time. They use automated tools that can try millions -- or billions -- of combinations. Here are the main approaches:

### Brute force

This is the straightforward approach: try every possible combination until you find the right one.

For a 4-digit PIN, there are 10,000 possible combinations (0000 through 9999). A computer can try all of them in seconds. This is why your phone locks you out after too many wrong attempts -- it's not being dramatic, it's genuinely protecting you from this kind of attack.

For an 8-character password using only lowercase letters, there are 26^8 -- about 208 billion combinations. That sounds like a lot, but modern hardware can chew through it surprisingly fast. Add uppercase letters, numbers, and symbols and the number grows enormously. But the single biggest factor? **Length.** Each additional character multiplies the total number of possibilities by the size of the character set. Going from 8 characters to 12 characters doesn't just make the password a little harder to crack -- it makes it *millions of times* harder.

### Dictionary attacks

Why try every possible combination when you can start with the ones people actually use?

Dictionary attacks use lists of common passwords, common words, common phrases, and known patterns. The password `password123` is among the most common passwords *every single year*. So is `iloveyou`. So is `qwerty`. Attackers try all of these first, along with common variations (capitalizing the first letter, adding a `!` at the end, swapping `a` for `@`, &c.). Those "clever" substitutions you thought of? Attackers thought of them too.

### Credential stuffing

This one is sneaky, and it's why reusing passwords is so dangerous.

Here's how it works: a company gets breached, and millions of username/password combinations leak. (This happens disturbingly often.) Attackers take that list and try each username/password combo on *other* sites -- Gmail, Facebook, your bank, Amazon, everything. If you used the same password on the breached site and your email, they're now in your email. From your email they can reset passwords on your other accounts. And it cascades from there.

**This is why you should never reuse passwords.** Not "try not to." *Never.* Every account should have a unique password. Which brings us to...

## Password managers: the actually practical solution

"Great," you might be thinking. "So I need a unique, long, random password for every single account I have. I have like 80 accounts. How am I supposed to remember all of those?"

You're not. That's what password managers are for.

A password manager is a tool that generates and stores strong, unique passwords for every site you use. It keeps them in an encrypted vault that you unlock with one master password. That master password is the *only* one you need to remember -- make it a good one (maybe a nice long passphrase), and the password manager handles everything else.

When you need to log into a site, the password manager fills in your credentials automatically. You never even need to know what your password for that site is. It could be `k7$mQ9!xLp2&wR5nBv` and you'd never have to type it.

Some good options:

- **Bitwarden** -- free and open source. This is what I'd generally recommend for most people.
- **1Password** -- paid, very polished, popular with families and teams.
- **Your browser's built-in password manager** -- Chrome, Firefox, and Safari all have one. It's better than nothing, but a dedicated password manager is usually more flexible.

I'll be honest with you: **using a password manager is genuinely the single most impactful thing most people can do for their online security.** If you take one practical thing away from this entire cybersecurity unit, let it be this. Go set one up. Today, ideally.

## Multi-factor authentication (MFA)

Passwords are important, but they have a fundamental problem: they're just one thing. One piece of knowledge. If someone gets it -- through a data breach, phishing, a lucky guess, or you writing it on a sticky note -- they're in.

Multi-factor authentication adds another layer. The idea is based on three categories of evidence:

- **Something you know** -- a password, a PIN
- **Something you have** -- your phone, a hardware security key
- **Something you are** -- your fingerprint, your face, your voice

**Two-factor authentication (2FA)** uses two of these. Multi-factor authentication (MFA) uses two or more. The terms are often used interchangeably in practice.

The logic is simple: even if someone steals your password (something you know), they still can't get in without your phone (something you have) or your fingerprint (something you are). An attacker in another country might be able to guess your password, but they can't reach through the internet and grab your phone off your desk.

### Common forms of MFA

Not all second factors are created equal:

- **Text message codes (SMS)** -- the site sends a code to your phone number. This is better than nothing, but it's the weakest form of MFA. Phone numbers can be hijacked through a technique called SIM swapping, where an attacker convinces your phone company to transfer your number to their phone. It happens more than you'd think.
- **Authenticator apps** -- apps like Google Authenticator or Authy that generate time-based codes on your phone. These are better than SMS because they're not tied to your phone number -- they're tied to your physical device.
- **Hardware security keys** -- physical devices like a YubiKey that you plug into your computer or tap against your phone. This is the strongest form of MFA because there's no code to intercept -- the key has to be physically present.

### Please actually do this

I'm going to be direct: **enable MFA on everything important.** Your email (especially your email -- it's the master key to all your other accounts), your bank, your social media, your school accounts. It takes five minutes to set up and it dramatically reduces your risk of being hacked.

It's a slight inconvenience. You'll occasionally need to pull out your phone when logging in. But it's genuinely one of the easiest and most effective things you can do for your security. The slight annoyance is worth it -- I promise.

## Activity: have you been pwned?

Here's something you can do right now. Go to [haveibeenpwned.com](https://haveibeenpwned.com) and enter your email address. This is a legitimate, well-known security tool run by Troy Hunt, a respected security researcher. It checks whether your email address appears in any known data breaches.

Don't be surprised if you find something -- many people do. Major breaches have affected LinkedIn, Adobe, Dropbox, MySpace, and hundreds of other services over the years. If your email shows up, it means your credentials from that site were leaked at some point.

What should you do if you find results?

1. Don't panic. A breach doesn't necessarily mean someone has accessed your accounts.
2. Change the password on any breached site (if you still use it).
3. If you were reusing that password on other sites -- change those too. All of them.
4. Set up a password manager so this doesn't happen again.
5. Enable MFA wherever you can.

## Discussion questions

1. **Check haveibeenpwned.com.** Were any of your email addresses in known breaches? How did that feel? Were you surprised by which services had been breached?

2. **What's your current password strategy?** Be honest -- do you reuse passwords? Do you use short or predictable ones? After reading this lesson, what would you change?

3. **What are the barriers to adopting good password practices?** If password managers and MFA are so great, why doesn't everyone use them? What could make them easier or more accessible?
