# Lesson 11 -- AI Ethics and Societal Impact

**At the end of this lesson, you will be able to:**

- Identify real-world examples of bias in AI systems and explain how they occur
- Describe how feedback loops can amplify existing biases
- Discuss the tradeoffs between AI-enabled convenience and privacy
- Articulate why questions of accountability in AI are difficult and unresolved

## Why a Whole Lesson on This?

We've touched on ethics a few times already in this unit -- when we talked about biased training data in Lesson 04, when we discussed hallucination in Lesson 10. But the ethical implications of AI are too important to leave scattered across other lessons as side notes. They deserve focused attention.

Here's the thing: the technical stuff we've been learning -- how models are trained, how predictions are made, how next-token prediction works -- that's all about *how AI works*. This lesson is about *what happens when AI meets the real world*. And the real world is messy, unequal, and complicated in ways that purely technical thinking can't account for.

These aren't hypothetical concerns. Everything we're about to discuss has already happened.

## Bias in AI Systems

You already know the foundation from Lesson 04: models learn from data, so biased data produces biased models. Garbage in, garbage out. But let's look at what that actually looks like in practice, because the consequences are a lot more serious than a spam filter making a mistake.

### Facial Recognition

In 2018, researcher Joy Buolamwini at MIT published the **Gender Shades** study, and the results were striking. She tested commercial facial recognition systems from major tech companies and found:

- Error rate for **light-skinned men**: 0.8%
- Error rate for **dark-skinned women**: 34.7%

Read those numbers again. The system was wrong about 1 in 125 times for light-skinned men. It was wrong about 1 in 3 times for dark-skinned women. That's not a small difference. That's a fundamentally different level of reliability depending on who you are.

Why did this happen? The training data. These models were trained primarily on photos of lighter-skinned faces, and primarily on male faces. So the model got very good at recognizing light-skinned men -- because that's what it had the most practice with -- and terrible at recognizing dark-skinned women, because it hadn't seen enough examples to learn the patterns.

This might seem like a problem that's easy to fix -- just get more diverse training data, right? And yes, that helps. But the deeper issue is that nobody caught this before these systems were deployed commercially. Nobody thought to check whether the system worked equally well for everyone. The people building and testing these systems didn't notice the gap, in part because the teams building them weren't diverse enough to think to ask the question.

### Hiring

Amazon built an AI recruiting tool designed to screen resumes and identify top candidates. The model was trained on resumes of people Amazon had previously hired. Sounds reasonable, right?

The problem: Amazon's previous hires skewed heavily male -- especially in technical roles. So the model learned that being male was a predictor of being a good candidate. It started penalizing resumes that contained the word "women's" -- as in "women's chess club captain" or "women's basketball." It literally learned to discriminate against women because the historical data reflected existing discrimination.

Amazon eventually scrapped the tool. But think about how many companies might be using similar systems without realizing what patterns their models have learned.

### Criminal Justice

Here's one that should make you uncomfortable. A system called **COMPAS** (Correctional Offender Management Profiling for Alternative Sanctions) was used across the United States to predict whether defendants were likely to reoffend. Judges used its scores in sentencing decisions.

In 2016, the investigative journalism outlet ProPublica published their **"Machine Bias"** investigation. They found that COMPAS was significantly more likely to falsely label Black defendants as high-risk compared to white defendants. And it was more likely to falsely label white defendants as low-risk. The model wasn't explicitly told about race -- but it was using factors that correlated with race (zip code, employment status, &c.), and it was trained on data that reflected decades of racially biased policing and sentencing.

People's freedom was affected by this. Judges who might have granted bail or a lighter sentence looked at COMPAS scores and made different decisions. This isn't a thought experiment. This is the criminal justice system.

## Feedback Loops: When Bias Feeds on Itself

The examples above are bad enough on their own. But there's a mechanism that can make things even worse: **feedback loops**.

Here's how a feedback loop works. Let's take predictive policing as an example:

1. A model is trained on historical crime data. The data shows more arrests in certain neighborhoods.
2. The model predicts that those neighborhoods will have more crime.
3. Police are sent to those neighborhoods in greater numbers.
4. More arrests happen in those neighborhoods -- because there are more police there to make arrests.
5. This new arrest data "confirms" the model's prediction.
6. The model is updated with this new data, and it becomes even more confident that those neighborhoods are high-crime.
7. Even more police are sent. Go back to step 4.

Do you see the problem? The model's predictions are influencing the very data that will be used to train the next version of the model. The system doesn't just reflect existing bias -- it *amplifies* it. Each cycle makes the bias stronger.

This isn't unique to policing. Feedback loops can happen in hiring (if your model preferentially selects certain candidates, those candidates become the training data for the next model), in lending (if your model denies loans to certain neighborhoods, those neighborhoods get poorer, which makes the model even less likely to approve loans there), in content recommendation (if an algorithm shows you content that makes you angry, you engage more, so it shows you more anger-inducing content, and the cycle continues).

Feedback loops are one of the most dangerous aspects of AI systems in the real world, and they're easy to miss if you're only looking at the technical performance of the model.

## Privacy and Surveillance

Let's shift gears. AI has made mass surveillance possible in ways that simply weren't feasible before.

Consider facial recognition in public spaces. Cameras are everywhere -- on streets, in stores, at airports, in schools. Without AI, those cameras produce an overwhelming flood of video that no one can actually watch. But with AI, every face in every frame can be automatically identified, tracked, and logged. A city could, in theory, track your movements throughout your entire day without your knowledge or consent.

Some cities -- including Portland, Oregon, which is close to home for us -- have banned government use of facial recognition technology. San Francisco and Boston have done the same. Other cities have embraced it. This is an active policy debate with strong arguments on both sides.

And it's not just cameras. Every click, every search, every purchase, every "like" can become training data for models that predict your behavior. Your phone tracks your location. Your smart speaker listens for its wake word (and sometimes records more than that). Your email gets scanned to show you relevant ads.

There's a genuine tradeoff here. Many of these technologies provide real convenience and real value. Google Maps is better because it uses everyone's location data to predict traffic. Spotify recommendations get better because the system learns from millions of users' listening habits. Medical AI gets better because it trains on patient data.

But the question is: are you making an informed choice about these tradeoffs? Do you know what data is being collected? Do you know who has access to it? Do you have a meaningful way to opt out?

Mostly, the answer to those questions is "no" or "sort of, but it's really inconvenient." And that's worth thinking about.

## Job Displacement

Let's talk about the elephant in the room. Will AI take your job?

The honest answer -- and I think honesty matters more than reassurance here -- is: it's complicated, and nobody really knows.

Here's what we can say with some confidence:

- **AI will change the job market.** Some tasks that humans currently do will be automated. Some jobs will disappear. Some jobs will change dramatically. Some entirely new jobs will be created.

- **This has happened before.** The printing press put scribes out of work. The assembly line changed manufacturing. ATMs didn't eliminate bank tellers -- but they did change what bank tellers do. Spreadsheet software didn't eliminate accountants -- but it did change what accounting looks like.

- **The transition isn't evenly distributed.** When jobs change, the pain isn't spread equally. People in certain industries get hit harder. People with fewer resources have less ability to retrain. Historically, technological transitions have eventually been net positive for society, but "eventually" and "net" are doing a lot of work in that sentence. The transition period can be brutal for the people caught in it.

- **AI is different in some ways from previous automation.** Past automation mostly affected physical or routine cognitive tasks. AI is increasingly capable of tasks we thought required human creativity, judgment, and communication. That's new, and it means the usual reassurance of "just retrain for a higher-skill job" might not apply in the same way.

Anyone who tells you "AI will definitely take all our jobs" is oversimplifying. Anyone who tells you "don't worry, new jobs always appear" is also oversimplifying. The truth is uncertain, and sitting with that uncertainty -- rather than grabbing for easy answers -- is the mature response.

## Who's Responsible?

When an AI system causes harm, who's accountable?

This sounds like it should have a straightforward answer, but it really doesn't. Let's say a self-driving car hits a pedestrian. Who's at fault?

- The engineers who built the system?
- The company that deployed it?
- The user who turned on autopilot?
- The lawmakers who allowed autonomous vehicles on public roads without sufficient regulation?
- The training data -- and the people who collected it?

Or take the hiring example from earlier. Amazon's AI discriminated against women. Who's responsible? The engineers didn't intend for that to happen. The training data just reflected existing reality. The people who made the hiring decisions years ago didn't know their decisions would become training data for an AI system.

These are genuinely hard questions. Our legal and ethical frameworks were built for a world where a human makes a decision and can be held accountable for it. When a machine makes a decision -- or when a human makes a decision based on a machine's recommendation -- the accountability gets blurry in ways we haven't fully figured out yet.

This is why **AI ethics** and **AI policy** are emerging career fields (we'll talk more about this in Lesson 12). We need people thinking carefully about these questions -- not just engineers, but ethicists, lawyers, policymakers, sociologists, and informed citizens.

Including you. Especially you, actually.

## What Can Be Done

It would be irresponsible to lay out all these problems and then not talk about solutions. So here's what's being done -- and what you can be part of:

- **Diverse teams.** AI systems built by homogeneous teams are more likely to have blind spots. Having people from different backgrounds, experiences, and perspectives on the team helps catch problems before deployment. Joy Buolamwini noticed the facial recognition bias because she personally experienced it -- the system couldn't detect her face.

- **Bias audits.** Testing models specifically for differential performance across demographic groups before deploying them. This should be standard practice. Increasingly, it is.

- **Transparency.** When an AI system makes a decision that affects you -- whether you get a loan, whether your resume gets seen, what content you're shown -- you should be able to understand, at least broadly, how that decision was made. Some jurisdictions are starting to require this.

- **Regulation and policy.** The EU's AI Act is one of the first comprehensive attempts to regulate AI systems based on their risk level. Other countries are developing their own frameworks. This is moving fast.

- **Your voice matters.** This isn't a platitude. AI policy is being shaped right now, and it will affect everyone. As someone who now understands -- at least at a basic level -- how these systems work and what can go wrong, you're better equipped than most people to participate in these conversations. Vote. Write to your representatives. Stay informed. The decisions being made about AI in the next few years will affect the next several decades.

## Activity: Go Deeper

Pick one of the following topics:

1. **Facial recognition bias** (Joy Buolamwini's Gender Shades project)
2. **AI in hiring** (Amazon's resume screening tool, or similar systems)
3. **AI in criminal justice** (the COMPAS system and ProPublica's investigation)
4. **AI and surveillance** (facial recognition in public spaces, data collection)

Do a bit of research beyond what's in this lesson -- even 15-20 minutes of reading will give you more context. Then write a paragraph (4-6 sentences) addressing:

- Who is most affected by this issue?
- What has been done about it so far?
- What do you think *should* be done about it?

There are no trick answers here. I want you to think through this carefully and come to your own conclusions.

## Discussion Questions

1. **The feedback loop problem:** Can you think of another situation -- not one of the examples from this lesson -- where an AI system's predictions could create a feedback loop that amplifies bias? Describe the loop step by step.

2. **Privacy tradeoffs:** Where do you personally draw the line between convenience and privacy? Are there services you use even though you know they collect your data? Are there lines you won't cross? What makes the difference for you?

3. **Accountability:** If you had to design a system for determining who's responsible when an AI causes harm, what would it look like? Who would bear the most responsibility -- developers, companies, users, or regulators?

4. **Connecting to previous lessons:** How does understanding how models learn (from Lessons 04-10) change how you think about the ethical issues in this lesson? Does knowing the technical details make the problems seem more or less solvable?
