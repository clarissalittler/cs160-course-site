# Lesson 8 -- How Data Breaches Happen

**At the end of this lesson, you will be able to:**

- Describe what a data breach is and explain the typical stages of how one unfolds
- Identify the most common causes of real-world data breaches
- Analyze a real breach and explain what went wrong and how it could have been prevented
- Describe what happens after a breach -- for the company and for the people whose data was stolen

## What Is a Data Breach?

A **data breach** is when protected information gets accessed by someone who shouldn't have it. That's it. That's the definition. But the simplicity of that definition hides a lot of variety in how breaches actually happen.

When you hear "data breach" you probably picture a hoodie-wearing hacker in a dark room typing furiously. And sometimes that's roughly what happens -- an attacker deliberately targeting a system. But breaches can also be accidental. A company misconfigures a database and leaves it open to the entire internet. An employee sends a spreadsheet of customer data to the wrong email address. A laptop with unencrypted files gets stolen from someone's car.

Whether it's a sophisticated attack or a careless mistake, the result is the same: data that was supposed to be protected isn't anymore. And once data is out there, you can't un-leak it.

## The Anatomy of a Breach

Let's walk through how a typical *intentional* breach unfolds. Not every breach follows these steps exactly, but this is the general pattern -- and understanding it helps you see where defenses can (and should) be in place.

### Step 1: Reconnaissance

Before attacking anything, an attacker does their homework. This is the research phase. They're figuring out:

- Who works at the target company? (LinkedIn is great for this -- people publicly list their job titles, their skills, what technologies they work with.)
- What software and systems does the company use? What versions are they running?
- Are there any publicly known vulnerabilities in that software?
- What does the company's network look like from the outside?

This might take days, weeks, or months. It's not glamorous. It's basically detective work -- gathering puzzle pieces before you try to put them together.

### Step 2: Initial Access

This is the "getting in" step. There are a bunch of ways this can happen:

- **Phishing** (which we covered in Lesson 03) -- tricking an employee into clicking a malicious link or entering their credentials on a fake login page
- **Exploiting a software vulnerability** (Lesson 04) -- finding a bug in the company's software and using it to gain access
- **Stolen credentials** (Lesson 05) -- using a password that was leaked in a previous breach, or bought on the dark web, or guessed because someone used "Password123"
- **Physical access** -- yes, sometimes people literally walk into a building. Tailgating through a security door behind someone who badges in, plugging a USB device into an unattended computer, &c.

The important thing to notice is that initial access often exploits *people*, not just technology. The most sophisticated firewall in the world doesn't help if someone clicks a phishing link.

### Step 3: Lateral Movement

Getting in the front door is just the beginning. The account or system the attacker first compromises is rarely the one with the valuable data. So now they move *sideways* through the network -- hopping from one system to another, looking for what they actually want.

During this phase, attackers often try to **escalate their privileges** -- going from a regular user account to an admin account. An admin account can access way more systems, install software, create new accounts, and generally do whatever it wants. If the attacker can become an admin, the whole network is essentially open to them.

This step is often surprisingly easy because many organizations don't do a great job of segmenting their internal networks. Once you're inside the perimeter, you can often reach things you shouldn't be able to reach. It's like a building where the front door has a great lock, but once you're inside, none of the internal doors are locked at all.

### Step 4: Exfiltration

Now the attacker has found the valuable data -- customer records, financial information, trade secrets, whatever they were after. The next step is getting it *out*. This is called **exfiltration**, which is a fancy word for "copying the data and sending it somewhere else."

Attackers are usually careful about this step. They don't just download 10 terabytes of data all at once -- that would set off alarms. Instead, they often exfiltrate data slowly, in small chunks, over a long period of time. Sometimes they encrypt it first so that even if someone notices the traffic, it looks like normal encrypted data.

### Step 5: Discovery

Here's the part that should scare you a little: on average, it takes companies about **200 days** to discover that a breach has happened. That's more than six months of an attacker having access to your data before anyone even knows about it.

Sometimes the company discovers the breach themselves -- their security team notices something unusual. Sometimes an outside security researcher finds the stolen data and alerts the company. And sometimes -- and this is grim -- the first sign of a breach is when the stolen data shows up for sale on the dark web.

200 days. Think about that.

## Real-World Case Studies

Let's look at some breaches that actually happened. These are all well-documented, and they illustrate different ways things can go wrong.

### Equifax (2017)

Equifax is a credit reporting agency -- they hold financial data on hundreds of millions of Americans. In 2017, attackers exploited a known vulnerability in a piece of web software called Apache Struts. The critical word there is "known." A patch for this vulnerability had been available for **two months** before the breach happened. Equifax just hadn't applied it. The result: personal data -- names, Social Security numbers, birth dates, addresses -- for **147 million people** was stolen. That's nearly half the US population. All because a known fix wasn't installed.

### Target (2013)

This one is a great example of lateral movement. The attackers didn't go after Target directly. Instead, they first compromised a third-party HVAC vendor -- a company that serviced Target's heating and cooling systems. That vendor had network access to Target's systems (for maintenance and billing purposes). The attackers used that access to move from the HVAC vendor's credentials into Target's payment systems, where they stole **40 million credit card numbers** during the holiday shopping season. The lesson: your security is only as strong as the weakest link in your supply chain.

### SolarWinds (2020)

This is the one that keeps security professionals up at night. SolarWinds is a company that makes network management software used by thousands of organizations, including US government agencies. Attackers compromised SolarWinds' software build process -- the system that creates the updates sent to customers. So when those customers installed a routine software update (the kind you're supposed to install!), they were actually installing malware.

This is called a **supply chain attack** -- instead of attacking the target directly, you attack a supplier that the target trusts. It's diabolical because the victims were doing the *right thing* by keeping their software updated. The breach affected at least 18,000 organizations and wasn't discovered for months.

## The Common Thread

Here's the thing that becomes obvious when you study real breaches: most of them involve something preventable. An unpatched system. A phished employee. A reused password. A misconfigured server. A third-party vendor with too much access.

The sexy, Hollywood version of hacking -- someone discovering a brilliant new exploit that nobody's ever seen before -- does happen. Those are called **zero-day exploits**, and they're real. But they're also rare and expensive. Most attackers don't need them. Why bother finding a new exploit when there are millions of unpatched systems running software with known vulnerabilities? Why write sophisticated malware when you can just send a convincing phishing email?

Most breaches exploit boring, known problems. That's both depressing (we know how to prevent this!) and hopeful (we know how to prevent this!).

## What Happens After a Breach

Once a breach is discovered, a lot of things start happening -- mostly unpleasant.

**For the company:**

- **Notification laws** require them to tell you. Most US states have laws requiring companies to notify affected individuals when their data is compromised. The specifics vary by state -- how quickly they have to notify, what information they have to include, &c. -- but the general principle is that you have a right to know.
- **Credit monitoring offers.** You've probably seen the news stories: "Company X is offering two years of free credit monitoring to affected customers." This has become the standard response.
- **Lawsuits.** Major breaches almost always result in class-action lawsuits. Equifax eventually paid a settlement of up to $700 million.
- **Regulatory fines.** Depending on the industry and what laws apply, companies can face significant fines. Under the EU's GDPR, fines can be up to 4% of a company's global annual revenue.
- **Reputation damage.** Hard to quantify, but real. Would you trust a company with your data after learning they left a known vulnerability unpatched for months?

**For you, the individual:**

If your data is involved in a breach, here's what you should do:

- **Change your passwords** -- for the breached service and for any other service where you used the same password (which, after Lesson 05, shouldn't be any of them, right?)
- **Monitor your financial accounts** for suspicious activity
- **Consider a credit freeze** -- this prevents anyone from opening new credit accounts in your name. It's free and you can lift it temporarily when you need to
- **Take advantage of the credit monitoring** if it's offered
- **Be extra vigilant about phishing** -- after a breach, attackers often use the stolen data to craft very convincing phishing emails targeting the affected people

## Discussion

Look up a recent data breach in the news. (You can search for "data breach 2024" or "data breach 2025" -- unfortunately, there will be no shortage of results.) Then answer these questions:

1. **What happened?** Describe the breach in your own words. What data was compromised? How many people were affected?
2. **How did it happen?** Which of the steps we discussed (reconnaissance, initial access, lateral movement, exfiltration, discovery) can you identify in the story? What was the initial point of entry?
3. **Could it have been prevented?** Was this a case of a known vulnerability, a human error, a sophisticated attack, or something else? What could the company have done differently?
4. **Who was affected?** Not just how many people, but who -- customers, employees, patients, students? What kind of data was exposed? How might that data be misused?
