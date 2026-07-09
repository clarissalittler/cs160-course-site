# Independent Course Audit

**Course:** Exploring Computer Science

**Audit date:** July 9, 2026

**Course context:** A general-education course in a computer science department, intended to give non-specialists a broad taste of computer science concepts.

## Executive summary

This is a genuinely good general-education course. It has an unusually coherent intellectual arc for a broad survey:

> representation → networks → programming → data → algorithms and limits → AI → security and social consequences

The strongest parts treat computer science as a way of thinking rather than merely as vocational coding. Unit 7's computability material, Unit 8's quantitative literacy, and the recurring questions about power, benefit, harm, and design decisions are especially effective.

The course does not need to be redesigned from scratch. It needs a concentrated alignment and accessibility revision. At present, the lessons are substantially better and more current than the administrative shell suggests. The most important issues are:

1. The syllabus, rubrics, schedule, assignment map, and activities no longer describe the same course.
2. Weeks 3 and 4 do not align cleanly with the concepts taught in their respective units.
3. Several visually dependent assignments still lack official, first-class equivalent routes.
4. Units 8–10, especially Unit 9, create a noticeable workload spike.
5. A small number of factual and mathematical claims need correction or qualification.

The course already succeeds at the hard part: it has intellectual personality, humane pedagogy, and worthwhile ideas. Its greatest risks are document drift, uneven assessment alignment, and accessibility alternatives that exist conceptually but are not yet consistently part of the official student route.

## Scope and approach

This was an independent, read-only review of the current repository. The audit examined:

- The overall unit sequence and intended outcomes
- The syllabus, schedule, rubrics, and assignment map
- Weekly assignments, low-stakes activities, and quiz banks
- Representative lesson content in every unit
- Accessibility patterns in assignments, images, embeds, and custom interactives
- Workload distribution and assumptions made of nonmajors
- Claims likely to become stale or requiring factual correction
- The relationship between the course's stated general-education purpose and its actual curricular emphasis

The older `course-review-findings.org` was used only as historical context because it explicitly predates the rewritten Units 9 and 10.

## What is already working

### Voice and approach

The writing is warm, direct, and appropriate for nonmajors. It anticipates anxiety without talking down to students. Programming is presented as experimentation and expression rather than syntax memorization.

The repeated questions—who benefits, who is harmed, and who gets to decide—give the course a consistent ethical and civic dimension. These questions are integrated into the subject matter rather than confined to a standalone ethics unit.

### Intellectual coherence

The progression from bits through the Internet into programming and data has a clear cumulative logic. The course has a recognizable point of view rather than feeling like ten unrelated “cool things about computers.” Its actual identity is approximately:

> Computer science through programming, data, society, and personal agency.

That identity should be stated explicitly in the course introduction.

### Particularly strong material

- Unit 7 makes an excellent case that computer science includes deep questions about what can and cannot be computed.
- Unit 8's chart, correlation, and misleading-data material is excellent civic quantitative literacy.
- Unit 10's scam, harassment, password, and recovery material is practical and humane.
- The quiz banks are generally strong: scenario-based, varied, and focused on interpretation, tracing, and explanation rather than rote vocabulary alone.
- Weekly assignments frequently offer meaningful student choice and authentic products.
- Mastery grading and resubmission are particularly appropriate for a no-prerequisite course.
- The custom AI and cybersecurity interactives already contain thoughtful keyboard controls, labels, and live status text.

### Existing accessibility foundation

An automated pass found alternative-text attributes on all active images. Most empty alternatives appear to be on decorative banners or icons. No broken ordinary local links were found; the apparent exceptions were expected D2L-root links.

The text-based alternatives drafted for Weeks 3 and 4 demonstrate the right philosophy: equivalent intellectual work, full explanatory narrative, and no presumption that the visual version is the “real” assignment.

## Critical issue: the official documents contradict one another

The current curriculum uses ten unified weekly assignments, as documented in `assignments/AssignmentMap.md`. The syllabus and rubrics still describe an earlier structure.

Examples include:

- `unit0/course-information/Course Syllabus.html` labels Unit 5 “Iteration” and Unit 6 “Arrays,” while the current units are Collections and Working with Real Data.
- The syllabus describes four assignments, six labs, a midterm, and a final, with all four assignments acting as gates on the final.
- `unit0/course-information/Course Rubrics.html` still refers to six labs, four programming assignments, and a Week 10 computing-innovation presentation.
- The schedule mostly uses the newer ten-assignment structure, producing contradictions inside Unit 0 itself.
- The syllabus describes cumulative quizzes, while the current quiz banks appear to be unit-specific.
- Activities are described as completion-graded, but their place in the schedule and final grade is unclear.

This is the most consequential defect in the repository because it affects grades, expectations, and potentially student appeals. Before changing more lesson content, the course should establish one canonical specification for:

- The ten current unit names
- Exactly which weekly work is required
- Grade weights
- The status of activities and quizzes
- Resubmission rules
- Any gates on passing or taking the final
- Collaboration rules
- Permitted and prohibited uses of generative AI

The old `course-topics-outline.org` should be regenerated or marked as historical. The same is true of `course-review-findings.org`, which should be clearly labeled as a pre-rewrite review if it remains in the active repository.

## Assessment alignment

### Weeks 3 and 4

The clearest mismatch occurs across Weeks 3 and 4.

The Week 3 lessons cover algorithms, variables, types, input/output, arithmetic, functions, parameters, return values, and debugging. Nevertheless, `assignments/Week 03 Assignment.txt` requires a `for` loop before loops are properly taught.

Unit 4 is explicitly about decisions and loops, but `assignments/Week 04 Assignment.txt` only requires defining and calling a function. A conditional is treated as bonus work. Week 3 therefore prematurely assesses Unit 4, while Week 4 chiefly reassesses Unit 3.

Two coherent repairs are possible:

1. Remove the required loop from Week 3 and require a meaningful conditional or loop in Week 4.
2. Explicitly teach one small, bounded loop pattern in Week 3, while still making decisions and iteration central to the Week 4 rubric.

### Activities

`assignments/Activities/README.md` has drifted from the current sequence. Its Weeks 5 and 6 topics no longer match the live Units 5 and 6. The activities also do not appear clearly in the schedule, so it is difficult to tell whether they are required, optional, or undeployed drafts.

### Assignment consistency

Some earlier handouts—especially Weeks 1, 2, and 9—retain “lab,” “solutions,” or duplicated “Assignment Assignment” language. They also lack the clearer 0–4 grading criteria found in later assignments.

A common assignment template would help every handout state:

- Purpose and unit outcomes
- Required deliverable
- Submission method
- Accessibility alternatives
- Privacy and account requirements
- Evaluation criteria
- Resubmission process

### Week 9 correctness check

The LLM debugging assignment asks students to make a faulty Sieve of Eratosthenes program run, but it does not provide the expected prime-number output. Incorrect code can run successfully. Students need a correctness oracle, such as expected output for a small fixed input.

The assignment should also ask students to verify an LLM answer against an independent credible or primary source, rather than only comparing it to the course text.

## Accessibility and equivalent participation

### Promote the existing alternatives

The Week 3 and Week 4 text-based alternatives in `assignments/drafts/` are promising, but they are not yet linked from the assignment map or the student-facing wrappers. Until they are integrated into the official route, students may not know that they exist or may reasonably interpret them as provisional or lesser work.

Each alternative should be linked directly from:

- The corresponding assignment handout
- `assignments/AssignmentMap.md`
- The D2L assignment description
- Any course accessibility overview

### Other visually dependent work

Additional equivalent routes are needed for:

- Week 1's pixelation task
- Week 2's graph activity
- Week 7's visual Game of Life exploration
- Week 8's chart-based analysis
- Week 10's eight-page mini-zine layout

An equivalent route should preserve the intellectual task rather than waive it. Appropriate alternatives could include structured text representations, data tables with narrative analysis, explicit cell-state tables, audio essays with transcripts, or linear HTML documents.

### Specific technical findings

- Twenty-one active iframes lack `title` attributes, mostly Python Tutor, Logic.ly, and Google Sheets embeds.
- Three substantive images in Unit 7 Lesson 1 have empty alternative text.
- The AI backpropagation interactive announces changes but does not expose all individual “blame” values in a navigable text table.
- Visual simulations need explicit textual state, not merely keyboard-operable controls.

### Accounts, privacy, and tool burden

The course relies on a large collection of external platforms, including D2L, Google Docs/Sheets/Slides, Code.org, Colab, Python Tutor, Logic.ly, dataset sites, consumer LLMs, and creative publishing tools.

For a no-prerequisite general-education course, each required platform should have:

- A clearly documented purpose
- A tested accessibility path
- A no-sign-in or instructor-provided fallback where feasible
- A private submission option
- Technical instructions that do not assume prior platform familiarity

The Colab assignments currently require “Anyone with the link can view.” Students should instead be able to upload an `.ipynb` file or share privately with the instructor. Public-facing projects should explicitly permit pseudonyms and private submission.

The LLM assignment should tell students not to paste personal information, private data, or unrelated graded work into a consumer service. An instructor-provided interaction transcript should be available for anyone unable or unwilling to create an account.

The syllabus's blanket claim that unlisted tools support screen readers is too broad to defend. It would be better to document tested workflows and acknowledge known limitations.

## Workload and curricular balance

The back half of the course is considerably denser than the middle. Units 8–10 contain longer lesson sequences, more complex assignments, and substantial activities.

Unit 9 is the clearest overload point. Within one general-education week, it addresses line fitting, gradient descent, neurons, backpropagation, deep learning, language models, ethics, applications, and careers. This is engaging material, but the amount of required mechanics risks turning memorable metaphors into facts students must memorize rather than models they can reason with.

Recommended response:

- Keep one strong “under the hood” neural-network sequence.
- Make some gradient-descent and backpropagation mechanics optional enrichment.
- Merge overlapping misinformation material in Unit 10.
- Use the recovered space for evaluation practices, data provenance, human labor, and environmental effects.

### Breadth of the survey

Four consecutive units center Python. That is defensible if the course identity is “CS through programming, data, and society,” but it is not a neutral sampling of every CS subfield.

Areas currently thin or absent include:

- Human-computer interaction and accessibility as computer science
- Operating systems and the software stack
- Databases and SQL
- Software engineering and version control
- Technical security, cryptography, and authentication

Adding five more units would overload the course. Short “taste” sections woven into existing units would be sufficient. Career examples should similarly be distributed across networking, HCI, data, systems, and security rather than appearing primarily in the AI unit.

## Factual accuracy and currency

### Gradient-descent objective mismatch

`unit9/artificial-intelligence/interactives/gradient-descent.html` displays total absolute error but updates the slope using the derivative of squared error. The visualization, prose, and algorithm therefore describe different objective functions.

The lesson and curve should either use squared error consistently or the update rule should be replaced with an appropriate subgradient rule for absolute error.

### Overstatement in the AI unit

Several lessons characterize learning as “just adjusting numbers” and everything else as detail or decoration. Gradient descent and backpropagation are central mechanisms in many neural networks, but data construction, objective design, architecture, optimization choices, evaluation, inference systems, and human feedback are not decoration.

The language can retain its approachable metaphor while saying that gradient-based optimization is **one central training mechanism for many modern neural networks**.

The treatment of emergent abilities should acknowledge that apparently sudden abilities can depend on the measurement scale used. Claims about whether models “understand” or possess consciousness should be distinguished from operationally testable claims, such as the fact that next-token prediction does not provide reliable fact-checking.

### Copyright

`unit1-digital-information/Lesson 09 - Intellectual Property.html` overstates ownership and permission requirements and underexplains originality, fixation, employment, transfer, public domain, fair use, and other statutory exceptions.

The short text alternative is especially important because students who cannot watch the videos currently receive the least nuanced version of the law.

The AI-output section should also be qualified. Prompting alone is generally insufficient for copyright protection, but human-authored selection, arrangement, and modification may be protectable, while contracts and other bodies of law may still affect reuse.

The Taylor Swift example is stale: four re-recorded albums were released, and Swift subsequently purchased her original masters in 2025. She did not re-record every early album.

### Internet history and resilience

The Internet unit slightly overstates nuclear survivability as the original purpose of ARPANET. Resource sharing and packet-switching research were central to ARPANET; survivability and robustness became especially important in later internetworking work.

“Resilient” is also more accurate than “antifragile.” A redundant network may survive damage without becoming better because it was damaged.

Claims that packet routing automatically routes around censorship should be softened. Administrative filtering can create effective chokepoints, and VPNs work by tunneling traffic through routes that remain permitted, not because the Internet has no chokepoints.

The current net-neutrality section accurately reflects the January 2025 Sixth Circuit decision setting aside the FCC's 2024 order, but it should be date-stamped and verified before each term.

### Ransomware and backups

`unit10-cybersecurity/Lesson 09 - When Things Go Wrong.html` implies that a synced drive counts as a backup and that restoration solves ransomware.

Sync can propagate deletion or encryption. A robust backup strategy needs versioning and a separated, offline, or immutable copy. Restoration can recover availability, but it does not undo data exfiltration or eliminate the need for incident response.

### Passwords and authentication

The password guidance is broadly current: long, unique passwords, password managers, and phishing-resistant MFA or passkeys are sound recommendations. The phrase “long beats complicated, every time” should be softened because uniqueness and unpredictability matter as well as length.

### ASCII and Unicode

The Unicode addition is useful and modern. One phrase should be corrected: ASCII did not itself “transition to an 8-bit encoding.” ASCII remains a 7-bit character encoding, although ASCII values are commonly stored in 8-bit bytes with the high bit set to zero.

## Recommended revision order

### Before the next offering

1. Reconcile the syllabus, schedule, rubrics, grading, activities, and unit names.
2. Repair Week 3 and Week 4 assessment alignment.
3. Publish the existing accessible alternatives and add equivalent routes for Weeks 1, 8, and 10.
4. Fix the gradient-descent, copyright, ransomware, Internet-history, and sieve issues.
5. Correct the Activities map and clarify whether activities and quizzes are required.
6. Add an assignment-specific AI and privacy policy.

### Next revision cycle

7. Trim Unit 9 and modestly rebalance Units 8–10.
8. Fix iframe titles, substantive empty alternative text, and text representations for simulations.
9. Add a termly currency checklist for AI products, Internet policy, copyright, and cybersecurity.
10. Adopt a common assignment template with outcomes, deliverables, evaluation, accessibility, privacy, and resubmission information.

### Longer-term curricular development

11. State the course's actual identity explicitly.
12. Weave in brief tastes of HCI, systems, databases, software engineering, and cryptography without adding whole units.
13. Distribute career vignettes across the course rather than concentrating them in AI.

## Suggested termly currency checklist

Before each offering, verify:

- Net-neutrality and Internet-policy status
- Consumer AI tools and product names mentioned in lessons
- AI copyright guidance and prominent legal examples
- Password, MFA, passkey, and ransomware recommendations
- Links to third-party tools, videos, datasets, and simulations
- Whether required platforms still offer the documented accessible and no-cost workflow
- Whether every assignment's stated week, unit, grading criteria, and submission method match the current schedule

## External reference points

- [U.S. Copyright Office: What Is Copyright?](https://www.copyright.gov/what-is-copyright/)
- [U.S. Copyright Office: Copyright and Artificial Intelligence, Part 2](https://www.copyright.gov/newsnet/2025/1060.html)
- [Internet Society: A Brief History of the Internet](https://www.internetsociety.org/internet/history-internet/brief-history-internet/)
- [Sixth Circuit net-neutrality opinion, January 2, 2025](https://www.opn.ca6.uscourts.gov/opinions.pdf/25a0002p-06.pdf)
- [Unicode Standard, Version 17, Chapter 2](https://www.unicode.org/versions/Unicode17.0.0/core-spec/chapter-2/)
- [NIST SP 800-63B: Authentication and Lifecycle Management](https://pages.nist.gov/800-63-4/sp800-63b.html)
- [CISA: More Than a Password](https://www.cisa.gov/more-password)
- [CISA StopRansomware Guide](https://www.cisa.gov/stopransomware/ransomware-guide)
- [NIST AI 600-1: Generative Artificial Intelligence Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [Schaeffer, Miranda, and Koyejo: Are Emergent Abilities of Large Language Models a Mirage?](https://arxiv.org/abs/2304.15004)
- [Vaswani et al.: Attention Is All You Need](https://arxiv.org/pdf/1706.03762)
- [Associated Press: Taylor Swift buys back her catalog](https://apnews.com/article/672dc24782f5b0f04c864a6fd86665d8)
