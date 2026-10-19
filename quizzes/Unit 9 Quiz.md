## Unit 9 Quiz — Artificial Intelligence

### Multiple Choice

**1.** You want a program that can tell cat photos from dog photos, and Lesson 2 argues that writing the rules by hand ("dogs have pointy ears...") is hopeless — every rule has a thousand exceptions. What does machine learning do instead?
- A) Uses a much longer, more carefully written list of if-statements
- B) Shows the computer thousands of labeled example photos (the training data) and lets it figure out the pattern itself
- C) Stores every cat photo on the internet so new photos can be matched against them exactly
- D) Asks a human to double-check each photo as it comes in

**2.** In the gradient-descent playground from Lesson 3, you drag the step size slider all the way up and press Run. What happens, and what does that teach you about the learning rate?
- A) The ball reaches the bottom faster — bigger steps are always better
- B) The ball overshoots the bottom and oscillates with shrinking swings before settling — larger steps can overshoot and are not always faster
- C) Nothing changes — step size only matters for networks with many knobs
- D) The ball starts rolling uphill toward higher wrongness

**3.** When a chatbot like ChatGPT answers your question, what is it actually doing underneath, according to Lesson 5?
- A) Looking your question up in a giant database of verified facts and copying out the answer
- B) Generating tokens one at a time using a learned probability distribution over possible next tokens
- C) Following topic-by-topic rules that engineers wrote out by hand
- D) Consciously reasoning through the question the way a person would

**4.** Lesson 4 compares backpropagation to a head chef tracing a too-salty dish backward through the kitchen, station by station. What problem does backpropagation solve for a network with millions of knobs?
- A) It computes how the loss changes with each parameter by passing gradients backward; an optimizer uses those gradients and a learning rate to update the parameters
- B) It wiggles each knob one at a time and measures whether the wrongness went up or down
- C) It finds the neurons that caused the mistake and deletes them from the network
- D) It memorizes the training examples so the same mistake can't happen twice

**5.** Neural networks had been around since the 1950s, but around 2012 — AlexNet's blowout win in the ImageNet contest — they suddenly worked spectacularly. According to Lesson 5, what changed?
- A) Gradient descent and backpropagation were invented that year
- B) Three things finally collided: oceans of labeled data from the internet, computing power from GPUs originally built for video games, and improvements in architectures and training methods that made use of both
- C) Computers became conscious enough to start learning on their own
- D) Programmers wrote much better hand-coded rules for recognizing images

**6.** A chatbot with web search gives you an answer complete with citation links. Lesson 5 says you should still click a link and check it. Why?
- A) Web links expire quickly, so citations go stale within days
- B) Search can retrieve real sources, but the model can misrepresent them in its generated answer — a real link does not establish that the source supports the claim
- C) Citations are only trustworthy in the paid versions of these tools
- D) Chatbots deliberately lie when they aren't sure of an answer

### True / False

**7.** According to Lesson 6, an AI agent's mistakes matter about as much as a chatbot's, because both of them only produce text.

**8.** A typical neural network combines weighted inputs and activation functions; training adjusts numerical parameters such as its weights.

### Multiple Choice (continued)

**9.** Using the unit's “knobs” and “wrongness” language, what happens when a model is trained?
- A) The model repeatedly measures how wrong its guesses are and nudges its numerical knobs in directions that reduce that wrongness
- B) A programmer writes one rule for every example the model might ever see
- C) The model stores the training examples unchanged and looks for an exact copy each time
- D) The computer removes all uncertain examples until only perfect data remains

**10.** What did the “Gender Shades” study establish about the evaluated commercial gender-classification systems?
- A) A programmer explicitly wrote a rule telling the systems to make those errors
- B) Error rates differed across the benchmark groups, with higher errors for darker-skinned women; undisclosed training data meant the study did not establish a training-data imbalance as the cause
- C) Darker pixels cannot be represented accurately by digital cameras
- D) Face-analysis systems become unbiased automatically when they process enough people

**11.** Which statement about AI, machine learning, and neural networks matches Lesson 2?
- A) They are three names for the same thing
- B) Every AI system learns from examples, so all AI is machine learning
- C) Machine learning is one part of AI, and neural networks are one family of machine-learning models
- D) Neural networks are the biggest category, and AI is one kind of neural network

**12.** According to Lesson 7, why did Anthropic decide not to release the model behind Project Glasswing to the public?
- A) The model was too slow and expensive for ordinary users
- B) The model was extremely good at finding and exploiting software vulnerabilities, so the company gave access only to organizations that maintain critical software, to help defenders fix flaws before tools like it spread
- C) The model could not write code, so it would not have been useful to the public
- D) A law required all AI models to be kept private
