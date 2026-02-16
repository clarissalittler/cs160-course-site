# Lesson 3 -- Security Risks: Social Engineering

**At the end of this lesson, you will be able to:**

- Explain why humans are typically the weakest link in any security system
- Identify the major types of social engineering attacks: phishing, spear phishing, pretexting, and baiting
- Recognize the red flags of a phishing email
- Apply your knowledge to identify real-world social engineering attempts

## The Weakest Link

Here's the key insight of this entire lesson, and it might surprise you: **the weakest link in any security system is almost always a human being, not a computer.**

Companies spend millions of dollars on firewalls, encryption, intrusion detection systems, and all kinds of sophisticated technical defenses. And those are important -- we'll talk about technical attacks in the next lesson. But the most common way that security gets breached isn't through some genius hacker typing furiously in a dark room. It's through someone being tricked.

Why bother trying to crack a password when you can just trick someone into telling you? Why try to break through a firewall when you can convince an employee to let you in the front door?

This is **social engineering**: the art of manipulating people into giving up confidential information or taking actions that compromise security. It exploits something that no amount of technology can patch -- human psychology. We're trusting. We want to be helpful. We respond to urgency and authority. And social engineers know exactly how to take advantage of that.

## Phishing

**Phishing** is the most common form of social engineering, and you've almost certainly encountered it. It's a fake message -- usually an email, but also text messages, social media DMs, &c. -- designed to look like it's from a trusted source.

The goal is to get you to do something: click a malicious link, download an infected attachment, enter your login credentials on a fake website, or hand over personal information.

### Anatomy of a Phishing Email

Let's walk through what a typical phishing email looks like and the red flags to watch for. Imagine you get an email that says:

> **From:** support@amaz0n-security.com
>
> **Subject:** URGENT: Your account has been compromised!
>
> Dear Valued Customer,
>
> We have detected unusual activity on your Amazon account. Your account will be suspended within 24 hours unless you verify your identity immediately.
>
> Click here to verify your account: [Verify Now](http://totally-not-suspicious.com/login)
>
> Thank you,
> Amazon Customer Support Team

Looks scary, right? That's the point. But let's break down the red flags:

1. **The sender address is wrong.** It says `amaz0n-security.com` -- notice that's a zero, not an 'o', and it's `amazon-security.com`, not `amazon.com`. Phishing emails often use addresses that *look* right at a quick glance but are slightly off. Always check the actual email address, not just the display name.

2. **Urgent, threatening language.** "Your account will be suspended within 24 hours!" This is designed to make you panic and act without thinking. Legitimate companies sometimes send security alerts, but they rarely threaten you with a deadline to create pressure.

3. **Generic greeting.** "Dear Valued Customer" instead of your actual name. Amazon knows your name -- if they were really emailing you, they'd use it. (Though some phishing attempts do include your name, especially the more sophisticated ones.)

4. **The link doesn't go where it says it goes.** The display text says "Verify Now" but the actual URL goes to `totally-not-suspicious.com`. In a real email, you can hover over a link (without clicking!) to see where it actually points. The display text and the real destination can be completely different. This is one of the oldest tricks in the book, and it still works.

5. **Asking for personal information.** Legitimate companies will almost never ask you to "verify" your password, Social Security number, or credit card information through an email link. If Amazon really thought your account was compromised, they'd ask you to go to amazon.com directly (by typing it in your browser) and check from there.

### What to Do if You Suspect Phishing

- **Don't click any links.** Don't download any attachments.
- **Don't reply to the email.**
- **Go directly to the real website** by typing the URL into your browser (not by clicking any link in the email). If there's really a problem with your account, you'll see it there.
- **Report it.** Most email providers have a "report phishing" option.

## Spear Phishing

Regular phishing is like casting a wide net -- the attacker sends the same generic email to thousands or millions of people, hoping some percentage will fall for it. **Spear phishing** is different. It's targeted.

In a spear phishing attack, the attacker does research on you specifically. They might look at your social media profiles, your company's website, public records, or previous data breaches to gather information. Then they craft a message that's tailored to you.

Instead of "Dear Valued Customer," a spear phishing email might say:

> Hi Jordan,
>
> It was great meeting you at the Portland Tech Meetup last Thursday! I wanted to follow up on our conversation about Python frameworks. Here's that article I mentioned: [link]
>
> Best,
> Alex

If you actually went to a tech meetup last Thursday -- information the attacker found on your public social media posts -- this is going to be a lot more convincing than a generic "your account is suspended" email. It feels personal. It feels real. That's what makes it so dangerous.

Spear phishing is harder to pull off because it requires research, so it's less common than regular phishing. But it's much more effective, and it's often used to target specific people in organizations -- executives, IT administrators, people with access to sensitive systems or money.

## Pretexting

**Pretexting** is when an attacker creates a fabricated scenario -- a *pretext* -- to trick you into providing information or access.

Some examples:

- **"Hi, I'm from IT."** You get a phone call from someone claiming to be from your company's IT department. "We're doing system maintenance and we need your password to make sure your account migrates correctly." This one is devastatingly effective because people generally trust their IT department and want to be cooperative.

- **"This is your bank calling."** Someone calls and says they've detected fraud on your account. They just need you to "verify" your account number and PIN to secure it. They already know your name and maybe even the last four digits of your account (which are often less protected than you'd think). It feels legitimate.

- **"I'm the new employee."** Someone shows up at an office, clipboard in hand, says they just started in another department and were told to come get their building access set up. Social pressure to be helpful and welcoming does the rest.

The common thread is that the attacker creates a believable story that gives them a reason to ask for what they want. They exploit trust, authority, and helpfulness -- qualities that are normally good things! That's what makes social engineering so insidious. It turns your best instincts against you.

A good rule of thumb: if someone contacts you and asks for sensitive information, **verify through a separate channel**. If someone calls claiming to be your bank, hang up and call the number on the back of your card. If someone emails saying they're from IT, call your IT department directly. Don't use any contact information provided in the suspicious message itself.

## Baiting

**Baiting** is exactly what it sounds like -- leaving something tempting out and waiting for someone to take it.

The classic example: an attacker drops a USB drive in a company's parking lot, lobby, or break room. Maybe they label it "Salary Information 2026" or "Confidential" -- something irresistible. Someone finds it, thinks "huh, I wonder whose this is" or "ooh, salary information," plugs it into their work computer, and... the USB drive installs malware.

This sounds like it shouldn't work. And yet, security researchers have tested this repeatedly, and the success rate is disturbingly high. In one study, researchers dropped nearly 300 USB drives around a university campus. Almost half of them were plugged into computers. People are curious. People want to be helpful (maybe they'll find out whose drive it is). And people don't think of a USB drive as a weapon.

Baiting can also happen digitally -- a free download that's "too good to be true" (pirated software, free premium content, &c.) that comes bundled with malware. If someone is offering something valuable for free and there's no obvious reason why, that's worth being suspicious about.

## A Real-World Case: The Twitter Hack of 2020

In July 2020, the Twitter accounts of Barack Obama, Joe Biden, Elon Musk, Bill Gates, Apple, and other high-profile accounts were hijacked. The accounts posted messages like: "I'm giving back to the community. All Bitcoin sent to the address below will be sent back doubled!" It was a scam, obviously -- but before it was shut down, people sent over $100,000 in Bitcoin.

Here's the thing: this wasn't a sophisticated technical hack. A 17-year-old in Florida and two accomplices pulled it off using **social engineering**.

The attack started with phone calls. The attackers called Twitter employees, pretending to be from Twitter's internal IT department. They convinced the employees to provide credentials to an internal tool that could access any Twitter account. Once they had access to that tool, the rest was easy.

Let that sink in. One of the biggest social media companies in the world, with some of the most high-profile accounts on the internet, was compromised because someone made some convincing phone calls. Not because of a software vulnerability. Not because of a cryptographic weakness. Because humans are trusting, and a good social engineer knows how to exploit that.

The teenager was arrested and sentenced to three years in juvenile detention, by the way. Social engineering is illegal, even though it doesn't involve "hacking" in the traditional sense.

## Why This Matters for Everyone

You might be thinking: "I'm not a high-profile target. Nobody's going to spear-phish me or call me pretending to be my bank." And it's true that you're probably not going to be individually targeted by a sophisticated attacker.

But basic phishing? That targets everyone. Those mass-sent emails go to millions of people, and they don't discriminate. Phishing is the number one way that personal accounts get compromised, data gets stolen, and malware gets installed. It's how people lose money, have their identity stolen, or get locked out of their own accounts.

And if you ever work at a company -- any company, in any role -- you'll be a potential target. Social engineers don't just go after the CEO. They go after whoever is most likely to help them: the receptionist, the new employee, the person in customer service. Understanding these techniques makes you harder to fool, and that protects not just you but everyone around you.

## Activity: Spot the Phishing

Look at the following emails. For each one, decide whether it's legitimate or a phishing attempt. If it's phishing, identify the specific red flags.

---

**Email 1:**

> **From:** noreply@paypa1.com
>
> **Subject:** Action Required: Confirm your identity
>
> Dear Customer,
>
> We noticed suspicious login activity on your PayPal account from an unrecognized device. To protect your account, we have temporarily limited your access.
>
> Please click below to restore your account within 48 hours, or your account will be permanently disabled.
>
> [Restore Account Access](http://paypal-secure-verify.com/login)
>
> PayPal Security Team

---

**Email 2:**

> **From:** registrar@yourschool.edu
>
> **Subject:** Spring term registration reminder
>
> Hi students,
>
> This is a reminder that Spring term registration opens Monday, November 3rd. You can register through MyPCC as usual. If you have holds on your account, please contact the registrar's office at 971-722-xxxx.
>
> See you next term!

---

**Email 3:**

> **From:** admin@netflix-billing.com
>
> **Subject:** Your Netflix payment failed -- update now
>
> Hi,
>
> We were unable to process your last payment. To avoid losing access to Netflix, please update your billing information using the secure link below:
>
> [Update Billing Info](http://nflix-account-update.com/billing)
>
> If you do not update your information within 24 hours, your account will be cancelled.
>
> Netflix Support

---

**Email 4:**

> **From:** jsmith@coworker-company.com
>
> **Subject:** Quick favor
>
> Hey,
>
> I'm in a meeting right now and can't step out. Can you run to the store and grab some gift cards for a client appreciation thing? I'll reimburse you. Need about $500 in Apple gift cards. Just send me the codes when you get them.
>
> Thanks!
> Jeff Smith, Regional Director

---

For each email, write down: (1) legitimate or phishing, (2) what red flags do you see (if any), and (3) what would you do if you received this email?

## Discussion Questions

1. **Have you ever received a phishing email or suspicious message?** Did you recognize it at the time? What tipped you off -- or what almost fooled you?

2. **Social engineering exploits trust and helpfulness -- qualities we normally consider good.** How do you balance being a helpful, trusting person with being security-conscious? Is there a way to do both?

3. **The Twitter hack was pulled off by a teenager using phone calls.** Does that change how you think about cybersecurity? Did you assume that major hacks required more technical sophistication?

4. **Think about your own online presence.** If someone wanted to spear-phish you, what information could they find about you from your public social media profiles? Is there anything you'd consider making private after thinking about this?
