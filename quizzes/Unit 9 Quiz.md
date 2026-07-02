## Unit 9 Quiz — Artificial Intelligence

### Multiple Choice

**1.** You want a program that can tell cat photos from dog photos, and Lesson 2 argues that writing the rules by hand ("dogs have pointy ears...") is hopeless — every rule has a thousand exceptions. What does machine learning do instead?
- A) Uses a much longer, more carefully written list of if-statements
- B) Shows the computer thousands of labeled example photos (the training data) and lets it figure out the pattern itself
- C) Stores every cat photo on the internet so new photos can be matched against them exactly
- D) Asks a human to double-check each photo as it comes in

**2.** In the gradient-descent playground from Lesson 4, you drag the step size slider all the way up and press Run. What happens, and what does that teach you about the learning rate?
- A) The ball reaches the bottom faster — bigger steps are always better
- B) The ball leaps clear over the bottom of the valley and bounces back and forth without settling — a learning rate that's too big overshoots
- C) Nothing changes — step size only matters for networks with many knobs
- D) The ball starts rolling uphill toward higher wrongness

**3.** When a chatbot like ChatGPT answers your question, what is it actually doing underneath, according to Lesson 8?
- A) Looking your question up in a giant database of verified facts and copying out the answer
- B) Predicting, over and over, the most plausible next word, based on patterns learned from enormous amounts of text
- C) Following topic-by-topic rules that engineers wrote out by hand
- D) Consciously reasoning through the question the way a person would

**4.** Lesson 6 compares backpropagation to a head chef tracing a too-salty dish backward through the kitchen, station by station. What problem does backpropagation solve for a network with millions of knobs?
- A) It figures out which way (and how much) to nudge *every* knob at once, by passing the blame for the mistake backward through the layers
- B) It wiggles each knob one at a time and measures whether the wrongness went up or down
- C) It finds the neurons that caused the mistake and deletes them from the network
- D) It memorizes the training examples so the same mistake can't happen twice

**5.** Neural networks had been around since the 1950s, but around 2012 — AlexNet's blowout win in the ImageNet contest — they suddenly worked spectacularly. According to Lesson 7, what changed?
- A) Gradient descent and backpropagation were invented that year
- B) Three things finally collided: oceans of labeled data from the internet, computing power from GPUs originally built for video games, and learning methods that at last had enough of both
- C) Computers became conscious enough to start learning on their own
- D) Programmers wrote much better hand-coded rules for recognizing images

**6.** A chatbot with web search gives you an answer complete with citation links. Lesson 9 says you should still click a link and check it. Why?
- A) Web links expire quickly, so citations go stale within days
- B) The model is still *generating* text, not retrieving verified facts — search results are just more raw material it can garble, so the link can be real while the "fact" attributed to it is not
- C) Citations are only trustworthy in the paid versions of these tools
- D) Chatbots deliberately lie when they aren't sure of an answer

### True / False

**7.** According to Lesson 9, the first answer a chatbot gives you is usually its best one, so asking for revisions ("make it shorter," "more formal") is a waste of time.

**8.** A neural network is built out of many simple units that each weigh their inputs, add them up, and decide whether to fire — so the whole network, however fancy, is really just a giant pile of adjustable knobs.

### Short Answer

**9.** Using the unit's "knobs" and "wrongness" language, describe in one to three sentences what is actually happening when people say a model is being "trained."

**10.** Joy Buolamwini's "Gender Shades" research found that commercial face-analysis systems made their worst errors on darker-skinned women. According to Lesson 10, where did that bias come from — did someone program it in? (One to three sentences.)
