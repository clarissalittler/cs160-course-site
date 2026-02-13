# Lesson 9 -- Protecting Yourself Online

**At the end of this lesson, you will be able to:**

- Apply practical security habits to protect your personal accounts and data
- Evaluate your own security practices and identify areas for improvement
- Explain how VPNs and HTTPS protect (and don't protect) your network traffic
- Think about security in terms of proportional threat modeling rather than all-or-nothing paranoia

## The Practical Lesson

We've spent several lessons talking about threats -- phishing, vulnerabilities, breaches, all of it. This lesson is different. This is the "okay, so what do I actually *do* about it?" lesson.

I'm going to be direct here: most of this stuff isn't hard. It's not technically demanding. It doesn't require special skills or expensive tools. The hard part is just... doing it. It's like flossing. Everyone knows they should. Most people don't. So think of this lesson as your cybersecurity dental appointment. Let's get you set up.

## Password Hygiene (A Quick Recap)

We covered this in detail in Lesson 05, but it's important enough to revisit. Here are the three rules:

### Use a password manager

A **password manager** is an app that generates, stores, and auto-fills strong, unique passwords for all your accounts. You only need to remember one password -- the master password for the manager itself. That one password should be long and strong (a passphrase like "correct-horse-battery-staple" is great -- long, random-ish, but memorable).

Good options include Bitwarden (free and open source), 1Password, and the built-in password managers in iOS and Android. Pick one. Set it up. It'll take maybe 30 minutes, and it's the single most impactful thing you can do for your online security.

### Never reuse passwords

If you use the same password for your email and for some random forum, and that forum gets breached, the attacker now has your email password. And from your email, they can reset passwords to everything else -- your bank, your social media, everything. This is called **credential stuffing**, and it works shockingly often because so many people reuse passwords.

With a password manager, every account gets a different random password. If one gets compromised, the damage is contained.

### Enable multi-factor authentication (MFA)

MFA means you need something *in addition to* your password to log in -- usually a code from an app on your phone, or a push notification you have to approve. Even if someone steals your password, they can't get in without that second factor.

Enable MFA on everything important: email, banking, social media, your password manager itself. Most services support it now -- you just have to turn it on. It's usually in Settings under "Security" or "Account Protection."

An authenticator app (like Authy or Google Authenticator) is better than SMS codes, by the way. SMS can be intercepted through a technique called **SIM swapping**, where an attacker convinces your phone carrier to transfer your number to their device. It's not super common, but it happens, and authenticator apps aren't vulnerable to it.

## Software Updates

This one is simple and unglamorous, but it might be the most important section in this entire lesson.

**Keep everything updated.** Your operating system. Your browser. Your apps. Your phone. Everything.

Why? Because many -- maybe most -- breaches exploit **known vulnerabilities that already have patches available**. Remember Equifax? The patch existed for two months before the breach. The attackers didn't need to discover anything new. They just needed to find a system that hadn't been updated.

When you see that "Update Available" notification and click "Remind Me Later," you're leaving a known vulnerability open on your system. Every day you delay is another day that vulnerability can be exploited.

**My advice:**

- **Enable automatic updates** whenever possible. For your OS, your browser, your phone -- just let them update themselves. Yes, it's mildly annoying when your computer restarts at an inconvenient time. You know what's more annoying? Having your bank account drained because you postponed an update for three months.
- **Don't ignore update notifications.** If something can't auto-update, update it manually when prompted. Make it a habit -- like checking your mail or doing the dishes.
- **Yes, this is annoying. Do it anyway.** I know. I hear you. But this is one of those cases where a small amount of friction prevents a potentially enormous amount of damage.

## Recognizing Threats

You've already learned about phishing in Lesson 03, but let's recap the practical skills for spotting threats in the wild.

### Check URLs carefully

Before you click a link -- especially in an email -- hover over it (don't click, just hover) and look at where it actually goes. Does the URL look right? Watch out for:

- Misspellings: `arnazon.com` instead of `amazon.com`
- Extra subdomains: `amazon.security-update.com` -- that's not Amazon, that's `security-update.com`
- Weird domain extensions: `amazon.com.ru`

If you're on your phone and can't hover, long-press the link to see the URL without opening it.

### Be skeptical of urgency

"Your account will be suspended in 24 hours!" "Immediate action required!" "You've won a prize -- claim it now!"

Legitimate companies rarely create artificial urgency like this. When something is demanding you act *right now*, that's often a sign that someone doesn't want you to stop and think. So stop. And think.

### The "too good to be true" rule

This one's been around since before the internet existed, and it still works. If something seems too good to be true -- a free iPhone, an inheritance from a distant relative, a job that pays $5000/week for minimal work -- it's almost certainly a scam. Your skepticism is your best defense here.

### When in doubt, go direct

If you get an email that says "there's a problem with your bank account," don't click the link in the email. Instead, open a new browser tab, type your bank's URL directly, and log in from there. If there's actually a problem, you'll see it in your account. If there isn't, you just avoided a phishing attack.

This simple habit -- going directly to the source instead of clicking links -- defeats the vast majority of phishing attempts.

## Network Security

Let's talk about what happens to your data when it travels across a network.

### Public WiFi

Here's the thing about public WiFi -- the kind you find at coffee shops, airports, hotels, libraries: it's not secure. And I don't mean "a little risky." I mean that anyone on the same network can potentially see your traffic.

On an open (unencrypted) WiFi network, your data is transmitted in the clear. An attacker sitting in the same coffee shop can use freely available tools to intercept what you're sending and receiving. This is called a **man-in-the-middle attack**, and it's not particularly difficult to pull off.

The good news: HTTPS (which we'll talk about in a moment) encrypts the content of your web browsing, so even on public WiFi, the actual data you're sending to HTTPS sites is protected. But an attacker can still see *which sites* you're visiting, and not everything uses HTTPS.

### VPNs (Virtual Private Networks)

A **VPN** creates an encrypted tunnel between your device and a VPN server. All your internet traffic goes through this tunnel, so anyone watching your local network (like that hypothetical attacker at the coffee shop) can't see what you're doing.

VPNs are genuinely useful on public WiFi. But I want to be honest about what they do and don't do, because VPN companies spend a LOT of money on marketing that overpromises.

**What a VPN does:**
- Encrypts your traffic between you and the VPN server
- Hides your browsing activity from your local network (your ISP, public WiFi operators, &c.)
- Can make it appear that you're browsing from a different location

**What a VPN does NOT do:**
- Make you anonymous on the internet. You're still logging into your accounts, still generating cookies, still leaving digital footprints.
- Protect you from phishing, malware, or other attacks.
- Guarantee your privacy. You're trusting the VPN company with your traffic instead of your ISP. You've just moved the trust from one entity to another. And some VPN companies have been caught logging and selling user data despite promising not to.

A VPN is a useful tool, not a magic bullet. If you use one, choose a reputable provider with a clear no-logging policy and a track record to back it up.

### HTTPS

Check the address bar of whatever website you're on right now. See the little padlock icon? That means the connection is using **HTTPS** -- the secure version of the web protocol. Your data is encrypted between your browser and the website's server.

If a site is still using plain HTTP (no padlock, and your browser might warn you about it), **don't enter sensitive information** -- no passwords, no credit card numbers, no personal data. The connection isn't encrypted, which means anyone between you and the server could potentially read what you're sending.

The good news is that HTTPS has become the default for most of the web. Most browsers will warn you if you try to visit an HTTP site. But it's still worth checking, especially if you end up on a site you've never visited before.

## Privacy Tools

Security and privacy are related but different. Security is about keeping attackers out. Privacy is about controlling who knows what about you -- and that includes legitimate companies, not just criminals.

### Browser privacy settings

Every major browser has privacy settings worth configuring. At minimum:

- **Block third-party cookies.** These are the cookies that track you across different websites. Most browsers now block them by default, but check your settings.
- **Consider a privacy-focused browser extension** like uBlock Origin (an ad blocker that also blocks trackers) or Privacy Badger.
- **Use private/incognito mode** when you don't want your browsing history saved locally. But understand what it does and doesn't do -- it prevents your *browser* from saving history, but it doesn't hide your activity from your ISP, your employer's network, or the websites you visit.

### Review app permissions on your phone

Go to your phone's settings and look at what permissions your apps have. You might be surprised.

Does a flashlight app really need access to your contacts? Does a game need to know your location? Does a weather app need access to your microphone?

Many apps request permissions they don't actually need for their core functionality. They're collecting extra data because it's valuable. You can (and should) revoke permissions that don't make sense. If the app stops working, you can always grant the permission back -- but in my experience, most apps work just fine without the extra permissions.

### Be thoughtful about what you share on social media

Remember the PII combination problem from Lesson 02? Individual pieces of information that seem harmless can be combined to build a detailed profile. Your birthday is public on Facebook. Your mother's maiden name is discoverable from family posts. Your first pet's name is in an old photo caption. And now someone has the answers to your security questions.

This isn't about being paranoid or never posting anything. It's about being thoughtful. Before you share something, ask yourself: could this information be used against me? Could it be combined with other information I've shared to reveal something I'd rather keep private?

## Threat Modeling -- Thinking Like a Security Professional

Here's a concept that pulls everything together: **threat modeling**. It sounds technical, but it's really just a structured way of asking "what am I protecting, and from whom?"

Security isn't all-or-nothing. You don't need to be perfectly secure (that's impossible) and you don't need the same security measures as a political dissident or a spy. What you need is security that's **proportional to your actual threats**.

Here's how to think about it:

1. **What are you trying to protect?** Your bank account? Your social media accounts? Your medical records? Your private photos? Your location? Different things have different value.

2. **Who might want to access it?** Random internet criminals running automated attacks? Someone you know personally? A corporation collecting data for advertising? A government? The answer changes what defenses matter.

3. **How much effort would they put in?** A random criminal running automated credential-stuffing attacks will move on if your password is unique and you have MFA. A determined stalker is a different kind of threat. A nation-state intelligence agency is yet another.

4. **What are you willing to do about it?** Security always involves tradeoffs -- convenience, time, money. The question isn't "what's the most secure option?" It's "what level of security makes sense for me given my actual risks?"

For most people -- and I mean this genuinely -- covering the basics will protect you from the vast majority of threats:

- Unique passwords with a password manager
- MFA on important accounts
- Software updates
- Skepticism about links and messages
- HTTPS everywhere

If your threat model includes more targeted risks -- if you're a journalist protecting sources, or an activist in a country with government surveillance, or someone in an abusive situation where a specific person might try to access your accounts -- you'd want to go further. But the basics are called the basics for a reason. They work.

## Activity: Personal Security Audit

Time to put this into practice. This isn't hypothetical -- I actually want you to do this right now (or tonight, if you're reading this and don't have your phone handy).

**Pick three of your most important accounts** -- email, banking, and social media are good candidates.

For each one, check:

1. **Does it have a unique password?** (Not one you use for other accounts.) If you're not sure, that probably means no.
2. **Is MFA enabled?** Log in and check the security settings.
3. **Review the privacy settings.** Who can see your profile? What information is public? Are there connected apps or third-party access you've forgotten about?

Then:

4. **Write down one specific change you're going to make.** Not a vague intention -- a concrete action. "I'm going to set up Bitwarden tonight." "I'm going to enable MFA on my Gmail." "I'm going to revoke that app I don't use anymore that still has access to my Google account."

The goal here isn't to become a security expert overnight. The goal is to make one thing better than it was before.

## Discussion Questions

1. **What was the most surprising thing you found in your security audit?** Did you discover any permissions, settings, or connected apps you'd forgotten about?

2. **What's your threat model?** Without getting too personal, what do you think are the most realistic threats to your digital security? Random automated attacks? Someone you know? How does that affect which security measures matter most to you?

3. **The convenience tradeoff:** Is there a security measure from this lesson that you know you *should* do but probably won't? Why not? What would make it easier? (No judgment here -- understanding why people don't adopt security practices is actually a major area of cybersecurity research.)

4. **Thinking about the breaches from Lesson 08:** If companies aren't even patching known vulnerabilities, how much of the responsibility for security should fall on individuals? Is there a point where personal security habits don't matter because the companies holding your data aren't doing their part?
