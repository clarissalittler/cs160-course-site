# Proposed Revised Course Outline

**Course:** CS 160 — Exploring Computer Science

**Document date:** July 9, 2026

**Status:** Planning document; no revisions implemented

**Assumed format:** Ten-week, four-credit course with 30 lecture hours and 30 lab hours

## Executive recommendation

CS 160 should remain a broad, humane introduction to computer science for nonmajors. It should not become a compressed version of the first course in the CS-major programming sequence, nor should it become a disconnected tour of fashionable technologies.

The course should instead make one sustained argument:

> Computer science is the study of how information and processes can be represented, automated, scaled, connected, and governed—and of what those choices do in the world.

The revised course should retain the current ten-unit arc while reducing the number of required lesson pages from 78 to approximately 50. Each week should contain five core lessons and one synthesis studio. Optional “deeper dive” material can preserve worthwhile technical detail without making every student responsible for every mechanism.

The recommended arc is:

1. Computers, Information, and Representation
2. The Internet as a Designed System
3. Programming as Problem Solving
4. Decisions, Repetition, and Testing
5. Collections, Data Models, and Interfaces
6. Files, Databases, and Software in the Real World
7. Algorithms, Efficiency, and the Limits of Computation
8. Data as Evidence
9. Artificial Intelligence and Automated Decisions
10. Security, Privacy, and Responsible Computing

This preserves the course's existing strengths while making the coverage promised by PCC's official course description more visible: computer architecture, software-development engineering, data organization, problem solving, ethics, theory of computation, careers, and rudimentary software development.

## What this design is trying to accomplish

### Keep a spine, not a buffet

A broad survey still needs accumulation. Every unit should add one layer to a shared model of computing:

- A computer represents information.
- A program represents a process.
- A collection or database represents a part of the world.
- An algorithm determines how work scales.
- A network connects independently controlled systems.
- A machine-learning model represents patterns learned from examples.
- Security asks what happens when people, software, and incentives do not behave as hoped.

Later units should explicitly call back to earlier ones. An AI model is data represented as numbers, processed by algorithms, stored and run on computer systems, reached over networks, and embedded in institutions. Cybersecurity should similarly revisit representation, networking, software, data, and human behavior.

### Give students a real taste without pretending they have completed a specialist course

For a general-education course, a successful “taste” means students can:

- Explain the central question a subfield asks
- Work through one representative example
- Recognize the subfield in systems they encounter
- Identify important tradeoffs and social consequences
- Know what a more advanced course or career in the area might involve

It does not require mastery of every notation, API, chart type, neural-network mechanism, or attack category.

### Treat accessibility as both course design and computer science

Accessibility should not appear only as a service students request. It should be:

- Built into every lesson and assignment route
- Presented as a central HCI and software-quality concern
- Included in evaluation rubrics
- Demonstrated through text alternatives, keyboard operation, meaningful sequence, and multiple ways to express understanding

This follows the principle in [WCAG 2.2](https://www.w3.org/TR/WCAG22/) that non-text content needs an alternative serving the same purpose, as well as [CAST's UDL Guidelines](https://udlguidelines.cast.org/action-expression/), which call for multiple means of engagement, representation, and action or expression.

### Use ethics as a method, not a final paragraph

The current course's recurring questions—who benefits, who is harmed, and who decides—should remain. They should be supplemented with a small, repeatable analysis routine:

1. What is the system supposed to do?
2. Who are the stakeholders, including people who do not directly use it?
3. What data, labor, infrastructure, and natural resources does it depend on?
4. Who receives the benefits, risks, costs, and power?
5. What alternatives, safeguards, or forms of recourse exist?
6. What evidence would change our judgment?

The [CS2023 curricular guidance](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm) treats society, ethics, and the profession as cross-cutting across computing knowledge areas, rather than as a topic to silo at the end. That approach is particularly appropriate for a general-education course.

### Make the course about concepts rather than accounts and products

Students should not need to become fluent in a parade of unrelated websites. No learning outcome should depend on a particular commercial product. Every required external tool should have:

- A clear curricular purpose
- A tested keyboard and screen-reader workflow
- A no-sign-in or instructor-provided fallback where feasible
- A private submission route
- A replacement plan if the service changes

Tool instructions should be just-in-time support pages, not core conceptual lessons.

## Proposed course-level outcomes

These operational outcomes are intended to clarify and assess the existing official outcomes, not replace them.

By the end of the course, students should be able to:

1. **Explain a computing system in layers.** Describe how hardware, software, data representations, networks, and people cooperate to produce a computing experience.
2. **Create and explain small programs.** Decompose a problem, express an algorithm, implement it with variables, functions, decisions, loops, and collections, and test the result.
3. **Organize and investigate data.** Explain where data came from, represent structured records, clean or query a small dataset, and use quantitative evidence responsibly.
4. **Reason about algorithms.** Trace algorithms, compare how their work grows, and distinguish practical difficulty from fundamental noncomputability.
5. **Evaluate computing systems.** Explain the basic operation and limits of networks, AI systems, and security mechanisms without relying on product marketing or science-fiction metaphors.
6. **Analyze consequences and choices.** Identify stakeholders, incentives, accessibility barriers, privacy and security risks, environmental costs, and possible mitigations.
7. **Work as a responsible computing collaborator.** Document choices, test artifacts, give and use feedback, credit sources, communicate accessibly, and make justified decisions about AI assistance.
8. **Recognize pathways through computing.** Connect each area of the course to careers, civic participation, creative practice, and further study, including roles that are not primarily programming.

### Alignment with the official PCC outcomes

| Existing outcome | Most direct operational outcomes |
|---|---|
| Create programs that implement problem-solving algorithms | 2, 3, 7 |
| Assess computational complexity and computability | 4 |
| Demonstrate a collaborative and ethical computing culture | 6, 7 |
| Evaluate innovations, systems, and career opportunities | 1, 5, 6, 8 |
| Analyze community or environmental questions using quantitative information | 3, 6 |

## Common weekly architecture

Every content week should use the same predictable rhythm.

### Five core lessons

Each lesson should take approximately 25–35 minutes for a prepared reader, including its formative check. A lesson should contain:

1. A concrete question or situation
2. A plain-language model of the idea
3. One fully worked example
4. An equivalent nonvisual representation of any diagram or interaction
5. A brief “predict or explain” check
6. One connection to a real system, career, or social choice
7. A short statement of what has been simplified

Programming lessons should generally follow a Predict–Run–Investigate–Modify–Make progression rather than asking novices to create a program from a blank page immediately. Research on [PRIMM](https://doi.org/10.1080/08993408.2019.1608781) and on [worked examples in introductory programming](https://jocse.org/articles/6/1/1/) supports using structured examples and explanation before independent construction.

### One synthesis studio

The weekly studio should occupy the substantial guided-lab portion of the course. It should integrate the week's concepts in a supported setting, using checkpoints and partially completed artifacts where appropriate.

Every studio should offer:

- A partner route and an asynchronous individual route
- A visual route and an equally complete text-first route where perception is relevant
- A provided dataset, transcript, or simulator state when an outside account would otherwise be required
- An “on-ramp” version meeting the core outcomes and optional extensions for students who want more challenge

### One weekly artifact

The weekly assignment should assess transfer beyond the worked studio. Each assignment should use a common rubric:

- Conceptual correctness
- Evidence or testing
- Explanation and reflection
- Responsible and accessible communication
- Completion of unit-specific technical requirements

Different media may be offered, but all routes should be held to the same intellectual criteria.

### Low-stakes retrieval and reflection

Each week should end with:

- A short, repeatable scenario-based quiz
- A two-question reflection: “What can you now explain?” and “What remains uncertain?”
- An opportunity to revise the artifact after feedback

## At-a-glance revised sequence

| Week | Unit | Central question | Weekly artifact |
|---|---|---|---|
| 1 | Computers, Information, and Representation | How can one physical machine represent so many different things? | Design and explain a small encoding system |
| 2 | The Internet as a Designed System | How does information cross independently controlled networks? | Explain a packet journey and diagnose a network failure or policy tradeoff |
| 3 | Programming as Problem Solving | How do we turn an intention into precise, reusable instructions? | Build and explain a small function-based program |
| 4 | Decisions, Repetition, and Testing | How can a program respond and repeat without losing control? | Build a tested interactive program using a decision and a loop |
| 5 | Collections, Data Models, and Interfaces | How does software represent many related things and make them usable? | Build an accessible in-memory information tool |
| 6 | Files, Databases, and Software in the Real World | How does information persist, get queried, and survive change? | Build or analyze a small persistent data application |
| 7 | Algorithms, Efficiency, and Limits | Which problems scale, which become impractical, and which cannot be solved at all? | Compare algorithms and explain one limit of computation |
| 8 | Data as Evidence | How can data support a claim without speaking for itself? | Produce an accessible, reproducible community-data analysis |
| 9 | AI and Automated Decisions | What does a learned model do, and how should we evaluate it? | Audit an AI system or set of model outputs |
| 10 | Security, Privacy, and Responsible Computing | How do we reduce harm when systems and people fail or act adversarially? | Create an accessible digital self-defense guide and course synthesis |

## Unit 0 — Orientation and access

Unit 0 should remain outside the ten content weeks, but it should do more than present policies.

### Orientation 1 — What kind of course is this?

**Topics**

- Computer science as representation, process, systems, and consequences
- How the ten units fit together
- Why programming is part of the course but not the whole course
- How the course differs from a computer-literacy or job-training class

**Student action**

Students annotate the course map with one area they already encounter, one area they want to understand, and one concern they have.

### Orientation 2 — How work and access operate

**Topics**

- The repeated weekly structure
- Mastery, feedback, and resubmission
- Equivalent assignment routes and how to choose among them
- Screen-reader, keyboard, caption, transcript, display, and low-bandwidth options
- Private submission and pseudonym options

**Student action**

Students complete a low-stakes access check using the same interaction types the course will later require. This is a course-design diagnostic, not a disclosure requirement.

### Orientation 3 — Collaboration, attribution, and AI

**Topics**

- What students may discuss, share, reuse, and revise
- Pair-programming roles and accessible collaboration norms
- How to credit code, data, media, classmates, and AI assistance
- What information must never be placed in a consumer AI service
- Assignment-specific rules taking precedence over a blanket policy

**Student action**

Students classify short scenarios as permitted collaboration, unattributed reuse, appropriate assistance, or a privacy risk, then explain one judgment.

### Orientation 4 — Tool preflight

Python setup and platform instructions should move here as reference material. Students should verify that they can run, save, retrieve, and submit a tiny program through at least one supported route. A browser-based route, a local route, and a file-upload route should be documented.

## Unit 1 — Computers, Information, and Representation

### Purpose

Give students a mental model of a computer as a layered system, then show that digital information is not naturally binary: people design conventions that let bit patterns stand for numbers, text, images, sound, and metadata.

This unit supplies the computer-architecture coverage promised by the official course description without turning into an electrical-engineering survey.

### Lesson 1 — What a computer does

**Guiding question:** What is happening between an action at an interface and the result we see or hear?

**Core topics**

- Input, processing, memory, storage, and output
- CPU, working memory, persistent storage, and devices
- Hardware, operating system, application, and user interface
- Instructions and data as bit patterns interpreted in context
- Abstraction: using a layer without knowing every detail below it

**Learning activity**

Students trace one familiar action—playing a song, opening a photo, or sending a message—through a text-based system stack. A diagram may accompany it, but the ordered text trace is the canonical representation.

**Reuse and revision**

Retain the approachable opening of the current “Computers and Information” lesson. Add the hardware/software stack that is presently mostly absent.

### Lesson 2 — Bits, bytes, and binary patterns

**Guiding question:** How many distinct things can a fixed number of two-state switches represent?

**Core topics**

- Bit and byte
- Binary place value and small conversions
- (2^n) possible patterns from (n) bits
- Representation versus meaning
- Capacity, range, and the consequences of finite representation

**Learning activity**

Students encode and decode small values using both a tactile/text table and an optional visual token system. Conversion should support the representational idea, not become a long arithmetic drill.

**Reuse and revision**

Merge the current circle/square and decimal-to-binary lessons. Keep the representation invention activity; reduce repetitive conversion practice.

### Lesson 3 — Text, Unicode, and standards

**Guiding question:** How can people exchange writing when languages and writing systems contain far more than 256 symbols?

**Core topics**

- Character encodings as agreements
- ASCII as a historical 7-bit encoding
- Unicode code points and UTF-8 at a conceptual level
- Characters, visual glyphs, and the limits of “one symbol equals one byte”
- Standards, compatibility, and who gets represented first

**Learning activity**

Students use a small provided code table to decode text, then explain why a shared standard matters. An extension can explore emoji sequences, combining marks, or normalization.

**Reuse and revision**

Retain and correct the current encoding lesson. Keep ASCII because it makes the basic idea visible, but present Unicode as the present-day system rather than an appendix.

### Lesson 4 — Images, sound, and compression

**Guiding question:** What is gained and lost when continuous experience becomes finite data?

**Core topics**

- Pixels, dimensions, resolution, RGB channels, and color depth
- Samples, sampling rate, and amplitude for sound
- File size as a consequence of representation choices
- Lossless and lossy compression
- Fitness for purpose: editing, archiving, streaming, medical evidence, art
- Perceptual assumptions and accessibility consequences

**Learning activity**

Students compare text descriptions and numerical samples representing the same image or sound at different resolutions. The task must not require vision or hearing to infer the tradeoff.

**Reuse and revision**

Merge the current black-and-white images, color images, lossless compression, and lossy compression lessons. Add the sound representation already promised in the overview.

### Lesson 5 — Copies, ownership, and permission

**Guiding question:** Being able to copy information is a technical fact; when is copying permitted or responsible?

**Core topics**

- Originality and fixation
- Authorship, employment, transfer, and licensing
- Public domain, Creative Commons, and fair use as different legal concepts
- Attribution as an ethical practice even when legal requirements vary
- Human authorship and current limits on copyright in AI-generated material
- The difference between copyright, platform terms, privacy, and plagiarism

**Learning activity**

Students choose and justify a reuse path for three short scenarios. The scenarios should be refreshed periodically and link to authoritative sources rather than celebrity examples that quickly become stale.

**Reuse and revision**

Retain the current intellectual-property discussion but rewrite its short version using the U.S. Copyright Office as the baseline.

### Synthesis studio — Invent an encoding

Students design a representation for a small domain, such as transit states, musical events, weather observations, or a set of classroom objects. They must:

- Define the possible values
- Specify the encoding and decoding procedure
- Demonstrate at least three examples
- Identify one ambiguity or capacity limit
- Explain how another person or system could access the same information

### Week 1 artifact

An “encoding field guide” in structured text, audio with transcript, or accessible document form. A pixel-art route may remain available, but it should be one route rather than the default against which alternatives are defined.

### Optional deeper dives

- Binary arithmetic and overflow
- Hexadecimal notation
- More detailed image or audio formats
- Error-detecting codes

## Unit 2 — The Internet as a Designed System

### Purpose

Help students explain an ordinary Internet interaction as movement through layers, infrastructure, organizations, and policy. The Internet should appear as both an engineering achievement and a contested human institution.

### Lesson 1 — A network of networks

**Guiding question:** What is the Internet, and what is merely built on top of it?

**Core topics**

- End devices, local networks, routers, ISPs, and interconnected networks
- Clients and servers as roles rather than fixed kinds of machines
- Internet versus web, cloud, app, and Wi-Fi
- Physical infrastructure: fiber, copper, radio, data centers, and undersea cables
- Local and global points of failure

**Learning activity**

Students label each step in a text trace from a phone or computer to a campus service. They identify which steps are local, which are controlled by an ISP, and which belong to the service provider.

### Lesson 2 — Packets, routing, and resilience

**Guiding question:** How can a message arrive when there is no permanent circuit from sender to receiver?

**Core topics**

- Breaking information into packets
- Headers and payloads
- Store-and-forward packet switching
- Multiple routes, congestion, loss, retransmission, latency, and throughput
- Robustness versus guaranteed delivery
- ARPANET resource-sharing history and the later emphasis on survivable internetworking

**Learning activity**

Students route numbered text packets through a small graph expressed both as an edge list and as an optional diagram. Some links fail or become congested; students explain what redundancy can and cannot accomplish.

### Lesson 3 — Addresses, names, and protocols

**Guiding question:** How do independently built systems agree about where information should go and what it means?

**Core topics**

- IP addresses as network-layer identifiers
- Domain names and DNS
- Ports as service endpoints at an introductory level
- Protocols as shared rules
- Layering and encapsulation
- Why an address, a name, and a person's identity are not the same thing

**Learning activity**

Retain a Battleship-style protocol-design exercise, but supply a complete text coordinate system and allow asynchronous protocol exchange. Students experience ambiguity before reading the formal vocabulary.

### Lesson 4 — The web, cloud, and platform stack

**Guiding question:** What happens after a browser receives an address?

**Core topics**

- Request and response
- HTTP and HTTPS
- What encryption in transit protects and what it does not establish
- Web servers, cloud hosting, content-delivery networks, and caching
- Convenience, scale, concentration, and correlated failure
- The difference between a distributed protocol and a centralized service

**Learning activity**

Students reconstruct a web request from shuffled text cards, then identify what an ISP, a cloud provider, and the destination service can each observe.

### Lesson 5 — Who can connect, watch, block, or govern?

**Guiding question:** If the Internet has no single owner, where does power actually collect?

**Core topics**

- Open standards and standards organizations
- ISPs, cloud providers, app stores, platforms, and infrastructure companies
- Digital divides in availability, affordability, devices, skills, and accessibility
- Surveillance, censorship, content moderation, and network neutrality
- Energy, water, materials, and local impacts of infrastructure
- Policy claims as dated claims requiring termly verification

**Learning activity**

Students examine one outage, access gap, or governance dispute. They map technical dependencies and stakeholders before taking a position.

### Synthesis studio — Diagnose a network incident

Students receive a scenario such as a DNS failure, cut cable, overloaded service, blocked domain, or cloud outage. They must:

- Trace the intended packet journey
- Identify the failing layer or organization
- Explain what still works and why
- Propose one technical mitigation and one institutional response

### Week 2 artifact

A network incident explainer or policy brief using a labeled text sequence, optional diagram, and stakeholder analysis. Graphical network maps must always be accompanied by an equivalent edge list or ordered path.

### Optional deeper dives

- Traceroute and routing tables
- IPv4, IPv6, and network address translation
- Detailed TCP reliability
- Tor, VPNs, and anonymity limits

## Unit 3 — Programming as Problem Solving

### Purpose

Introduce programming as the act of making a process precise, testable, and reusable. Students should finish this week able to write and explain a small function-based program, but loops should not yet be required.

### Lesson 1 — From problem to algorithm

**Guiding question:** What must be made explicit before a computer can help?

**Core topics**

- Inputs, outputs, and constraints
- Decomposition into named steps
- Sequencing and state
- Pseudocode
- Tracing an algorithm by hand
- Ambiguity and edge cases

**Learning activity**

Students improve an ambiguous everyday procedure, then trace a short pseudocode algorithm with a state table.

### Lesson 2 — Program anatomy, variables, and types

**Guiding question:** How does running code change a program's state?

**Core topics**

- Source code, interpreter, and execution
- Statements and expressions
- Assignment and variables
- Integers, floating-point values, strings, and booleans as different interpretations
- Output and the difference between displaying and storing a value
- Meaningful names

**Learning activity**

Use a Predict–Run–Investigate sequence with a short program. A text state table must accompany any visual execution tool.

### Lesson 3 — Input, expressions, and conversion

**Guiding question:** How does a program turn user input into a useful result?

**Core topics**

- Text input and explicit numeric conversion
- Arithmetic operators and order of evaluation
- String composition and f-strings
- Rounding and units
- Type errors as information about an incorrect model

**Learning activity**

Students modify a complete unit-conversion or cost-estimation program, first predicting each change.

### Lesson 4 — Functions as named abstractions

**Guiding question:** How can we teach a program a new verb?

**Core topics**

- Function definition and call
- Parameters and arguments
- Return values versus printing
- Local names at an intuitive level
- A function's contract: expected inputs and promised output
- Reuse and decomposition

**Learning activity**

Students trace two calls to the same function with different arguments, then modify and create a closely related function.

### Lesson 5 — Errors, tests, and collaborative debugging

**Guiding question:** How do we learn from a program that does not behave as intended?

**Core topics**

- Syntax, name, type, and value errors
- Reading a traceback from the final line upward
- Observed versus expected behavior
- Normal, boundary, and invalid test cases
- Small changes and reproducible debugging
- Pair roles: driver, navigator, explainer, and tester
- Saving versions rather than destroying evidence

**Learning activity**

Students repair a short program using a provided test table and explain which evidence identified each bug.

### Synthesis studio — Build from a worked program

Students predict, run, investigate, and modify a complete small program before making a related program of their own. Supported contexts should include:

- A text conversation or calculator
- A sound or music-related numerical transformation with text output
- A simple drawing with a narrated command log
- A small community-resource estimator

### Week 3 artifact

A small program containing input, computation, output, and at least one student-defined function with parameters or a return value. Students submit code, a sample run, a test table, and a plain-language explanation.

The graphical route must not require a loop before Unit 4. A text-first route should be listed beside it, not linked as a special accommodation.

### Optional deeper dives

- Multiple return values
- Floating-point representation
- A local development environment
- Additional functions and decomposition

## Unit 4 — Decisions, Repetition, and Testing

### Purpose

Show how programs choose among paths and repeat work. Testing should be taught as part of control flow rather than as cleanup performed after the program is “finished.”

### Lesson 1 — Boolean questions and comparisons

**Guiding question:** How does a program turn a situation into a yes-or-no value?

**Core topics**

- Boolean values
- Equality versus assignment
- Numeric and text comparisons
- Storing and printing Boolean results
- Boundary values
- Simple truth tables

**Learning activity**

Students predict comparisons around boundaries and explain surprising string comparisons.

### Lesson 2 — Choosing with `if`, `elif`, and `else`

**Guiding question:** How can one program produce different behavior in different situations?

**Core topics**

- Conditional execution
- Mutually exclusive branches
- Branch order
- Optional versus exhaustive cases
- Indentation and block structure
- Tracing which branch executes

**Learning activity**

Students trace and modify a complete decision program, then construct a test case for every branch.

### Lesson 3 — Compound decisions and logic

**Guiding question:** How do we express rules involving more than one condition?

**Core topics**

- `and`, `or`, and `not`
- Inclusive versus everyday uses of “or”
- Simplifying rather than deeply nesting conditions
- Truth tables as a debugging aid
- A brief connection to logic gates and digital circuits
- How apparently neutral thresholds encode policy choices

**Learning activity**

Students translate short rules between prose, Boolean expressions, and truth tables, then test for an omitted case.

### Lesson 4 — Counting repetition with `for` and `range`

**Guiding question:** What should a program do when the number of repetitions is known or comes from a sequence?

**Core topics**

- Repetition as repeated state change
- `for` loops and `range`
- Start, stop, and step
- Off-by-one reasoning
- Accumulator and counter patterns
- Tracing repeated updates in a table

**Learning activity**

Students predict a loop's complete output and final accumulator value before changing its range.

### Lesson 5 — Conditional repetition and termination

**Guiding question:** What should a program do when it must continue until something changes?

**Core topics**

- `while` loops
- Loop initialization, condition, and update
- Input validation
- Sentinel values
- Infinite loops and termination arguments
- Choosing `for` versus `while`

**Learning activity**

Students diagnose three nonterminating or incorrectly terminating loops using state tables.

### Synthesis studio — Design an interactive decision system

Students build a small system such as a study planner, accessibility-preference selector, game, questionnaire, or resource recommender. Before coding, they create:

- A branch table
- A loop plan
- Expected outcomes for normal, boundary, and invalid input

### Week 4 artifact

A program that must include:

- At least one meaningful conditional
- At least one meaningful loop
- At least one function
- Input validation or a clearly justified stopping condition
- A test table covering every branch and loop termination

This directly assesses Unit 4 rather than treating decisions as bonus work.

### Optional deeper dives

- Nested loops
- `break` and `continue`
- De Morgan's laws
- More detailed digital logic

## Unit 5 — Collections, Data Models, and Interfaces

### Purpose

Move from isolated values to collections representing a small part of the world. Introduce HCI and accessibility as technical design concerns: a correct internal model can still produce an unusable or exclusionary system.

### Lesson 1 — Strings as sequences

**Guiding question:** What becomes possible when we treat text as an ordered collection?

**Core topics**

- Sequence, index, length, and slice
- Iterating over text
- Common string methods
- Case, whitespace, and normalization
- Why visible characters and Python string positions are not always identical in every writing system

**Learning activity**

Students trace string operations and build a small text transformation while discussing what assumptions it makes about language.

### Lesson 2 — Lists and changing collections

**Guiding question:** How can a program keep track of a changing number of related items?

**Core topics**

- Creating, indexing, slicing, and measuring lists
- Appending, updating, and removing
- Membership
- Mutation and aliasing only at an intuitive level
- Empty collections and invalid indexes

**Learning activity**

Students modify a complete list-based program and predict the list after each statement.

### Lesson 3 — Traversal, transformation, filtering, and aggregation

**Guiding question:** What recurring jobs do programs perform on collections?

**Core topics**

- Processing every item
- Counting and accumulating
- Finding minimum and maximum
- Filtering items meeting a condition
- Building a new collection
- Separating a calculation from input and display

**Learning activity**

Students classify short loops by pattern, then complete one missing step in each pattern.

### Lesson 4 — Dictionaries, records, and nested data

**Guiding question:** When is a name more useful than a position?

**Core topics**

- Key-value mappings
- Lookup, insertion, update, and missing keys
- Dictionary as one record
- List of dictionaries as a table of records
- Choosing a list, dictionary, or nested combination
- Schema as an agreement about fields and meanings

**Learning activity**

Students convert a small parallel-list or tuple representation into records and explain which representation is easier to understand and extend.

### Lesson 5 — Modeling people and designing interfaces

**Guiding question:** What gets lost when software turns people and situations into fields and menu options?

**Core topics**

- Required, optional, unknown, and not-applicable values
- Categories and identities that do not fit a fixed list
- Validation versus exclusion
- User goals, error messages, predictable navigation, and clear labels
- Keyboard and screen-reader access
- Usability testing with another person
- Data minimization: not every collectable field should be collected

**Learning activity**

Students critique and revise a small record schema and text interface for ambiguity, exclusion, privacy, and accessibility.

### Synthesis studio — Build and test an in-memory information tool

Students create a small catalog, tracker, playlist, resource directory, or other information tool using a list of dictionaries. The interface is text-first, with any visual enhancements treated as optional.

A peer or provided persona tests whether the tool makes its actions, state, and errors understandable.

### Week 5 artifact

An in-memory information system that can add, display, search or filter, and summarize records. The submission includes:

- A short schema or data dictionary
- Sample records
- At least two collection-processing operations
- A usability/accessibility observation and resulting revision

Tuples and unpacking should become an optional technique introduced when they naturally help, rather than the organizing concept of the core assignment.

### Optional deeper dives

- Tuples and unpacking
- Sets
- Comprehensions
- Unicode-aware text processing

## Unit 6 — Files, Databases, and Software in the Real World

### Purpose

Show what changes when software must preserve data, use other people's code, answer queries, and remain understandable after its first successful run. This unit supplies a concise taste of data management and software engineering.

### Lesson 1 — Persistence and files

**Guiding question:** What happens to a program's information after the program stops?

**Core topics**

- Volatile program state versus persistent storage
- File paths and text files
- Reading and writing with a context manager
- Append versus overwrite
- Encoding and line endings at an introductory level
- Failure modes: missing file, permission, malformed content

**Learning activity**

Students predict a file's contents after a sequence of program runs, then modify a complete save/load example.

### Lesson 2 — CSV, types, and provenance

**Guiding question:** Why is a table in a file not yet a trustworthy dataset?

**Core topics**

- Header, row, column, delimiter, and record
- Reading CSV as dictionaries
- The fact that file values initially arrive as text
- Missing, malformed, and inconsistent values
- Data dictionaries
- Source, date, unit, license, and collection method
- Formula injection and untrusted data as an optional security connection

**Learning activity**

Students inspect a deliberately imperfect small CSV and create a data-quality log before writing code.

### Lesson 3 — Libraries, documentation, and dependencies

**Guiding question:** What does it mean to build software using code we did not write?

**Core topics**

- Modules, packages, and imports
- Standard library versus third-party dependency
- Reading a function signature and short documentation example
- Version and compatibility
- Source, maintenance, license, and trust
- Using a library without confusing the tool with the underlying concept

**Learning activity**

Students use one small standard-library module from documentation, then identify what their program is trusting.

### Lesson 4 — Querying data: Python and a taste of SQL

**Guiding question:** How can we state what data we want without manually inspecting every record?

**Core topics**

- Selection of rows, selection of fields, sorting, grouping, and aggregation
- Expressing the same simple query with a Python loop and with SQL
- `SELECT`, `FROM`, `WHERE`, and one simple aggregate
- Database tables, rows, columns, and keys
- Why databases exist beyond “a bigger CSV”

**Learning activity**

Students match plain-language questions to Python and SQL queries using a small local dataset. SQL is a conceptual taste, not a second programming language to master.

### Lesson 5 — Software as an evolving artifact

**Guiding question:** What makes a program maintainable rather than merely runnable once?

**Core topics**

- Requirements and acceptance examples
- Functions and separation of concerns
- Regression tests
- Documentation and readable names
- Version history and the purpose of version control
- Code review and constructive feedback
- Refactoring without changing behavior
- Responsible use and attribution of copied or AI-generated code

**Learning activity**

Students revise a working but poorly organized program while a test set protects its behavior. A lightweight version history can be supplied without requiring a GitHub account.

### Synthesis studio — A persistent data tool

Students extend the Week 5 information tool or begin from a provided equivalent. The program loads records, performs at least one query or summary, and saves a meaningful update or report.

### Week 6 artifact

A small persistent data application or analysis containing:

- A documented source or student-created CSV
- Explicit conversion or validation of at least one field
- A list-of-dictionaries representation or simple local database
- At least one filter and one summary
- A test plan and short change log

### Optional deeper dives

- SQL `GROUP BY` or a simple join
- SQLite from Python
- Pandas as an alternative data tool
- Git commits and branches
- JSON and web APIs

## Unit 7 — Algorithms, Efficiency, and the Limits of Computation

### Purpose

Make good on the course's theory-of-computation outcome. Students should leave able to distinguish correctness, efficiency, practical infeasibility, and noncomputability.

### Lesson 1 — Algorithm, program, and specification

**Guiding question:** How can the same process exist independently of a programming language?

**Core topics**

- Problem, input, output, and specification
- Algorithm versus implementation
- Preconditions and guarantees
- Correctness for a defined domain
- Multiple representations: prose, pseudocode, code, and state machine
- Algorithms as designed artifacts with consequences

**Learning activity**

Students recognize one algorithm in three forms and identify an input excluded by its precondition.

### Lesson 2 — Search as a case study

**Guiding question:** How much can prior organization change the work required to find something?

**Core topics**

- Linear search
- Binary search
- Sorted-data precondition
- Best, typical, and worst cases at an intuitive level
- Trace tables
- Cost of preparing and maintaining sorted data

**Learning activity**

Students perform both searches on an ordered text list, count comparisons, and explain when binary search's setup cost is worthwhile.

### Lesson 3 — Measuring growth with Big-O

**Guiding question:** What matters when the input becomes a thousand or a million times larger?

**Core topics**

- Input size and a chosen basic operation
- Constant, logarithmic, linear, quadratic, and exponential growth
- Ignoring machine-dependent constants for a scaling comparison
- Time-space tradeoffs
- Why a faster computer does not rescue every algorithm
- Big-O as a bound on growth, not a stopwatch prediction

**Learning activity**

Students compare small operation-count tables before seeing notation, then match familiar algorithms to growth patterns.

### Lesson 4 — Feasible, expensive, and intractable

**Guiding question:** Can a problem be computable but still practically out of reach?

**Core topics**

- Brute-force search
- Combinatorial explosion
- Exact versus approximate or heuristic answers
- Scheduling or route planning as a representative case
- The broad significance of P versus NP without requiring formal complexity theory
- Resource use and who bears the cost of computation

**Learning activity**

Students count possibilities in a small scheduling problem and choose a justified stopping rule or heuristic.

### Lesson 5 — Problems no general program can solve

**Guiding question:** Are there questions for which no correct all-purpose algorithm can exist?

**Core topics**

- Decision problems
- The halting problem through self-reference
- Difference between “we do not know an algorithm,” “the algorithm is too slow,” and “no general algorithm exists”
- Universal machines and programs as data
- Why these limits matter for program analysis and security

**Learning activity**

Students work through a carefully narrated contradiction without formal proof notation, then classify new examples as unknown, expensive, or undecidable.

### Synthesis studio — Emergence and universal computation

Use Conway's Game of Life as a capstone example of simple local rules producing complex behavior and universal computation. The studio must include:

- A grid route
- A coordinate-list or table route
- A narrated generation-by-generation state
- A distinction between predicting a few steps and deciding every long-term behavior

### Week 7 artifact

An algorithm field report containing:

- A trace of linear and binary search
- A scaling comparison with stated operation counts
- A recommendation based on constraints rather than a universal “winner”
- A plain-language explanation of practical infeasibility or the halting problem

### Optional deeper dives

- Sorting algorithms
- Formal asymptotic definitions
- Recursion
- Reductions and NP-completeness
- Cellular automata constructions

## Unit 8 — Data as Evidence

### Purpose

Teach a complete but modest data-inquiry cycle. The emphasis should be on formulating questions, understanding how data was produced, selecting an analysis, and communicating limits—not on memorizing eleven separate tool and chart lessons.

The design follows the spirit of the [ASA GAISE College Report](https://www.amstat.org/asa/files/pdfs/GAISE/GaiseCollege_Full.pdf): emphasize statistical thinking, use real data, foster active learning, use technology in service of concepts, and use assessment to improve learning.

### Lesson 1 — Data is made, not found

**Guiding question:** What decisions turned part of the world into this dataset?

**Core topics**

- Observation, record, variable, value, and dataset
- Categorical and quantitative variables
- Discrete and continuous measurements
- Units, metadata, and provenance
- Missingness and constructed categories
- Data as an abstraction rather than a neutral copy of reality

**Learning activity**

Students read a small data dictionary and reconstruct what was measured, what was omitted, and what one row means.

### Lesson 2 — Questions, populations, samples, and bias

**Guiding question:** Which claims can this data actually support?

**Core topics**

- Descriptive, comparative, and relationship questions
- Population and sample
- Selection, nonresponse, survivorship, and measurement bias
- Proxy variables
- Privacy, consent, and data minimization
- Distinguishing a question of value from a question data can answer

**Learning activity**

Students critique three proposed claims against a dataset's collection method and rewrite one claim to fit the evidence.

### Lesson 3 — Cleaning and summarizing responsibly

**Guiding question:** What must happen before a dataset can answer even a simple question?

**Core topics**

- Inspecting types, ranges, categories, duplicates, and missing values
- Documenting rather than hiding cleaning decisions
- Count, proportion, rate, minimum, maximum, mean, and median
- Denominators and per-capita comparisons
- Outliers as observations to investigate, not automatically delete
- Reproducibility through a cleaning log

**Learning activity**

Students clean a deliberately small, imperfect dataset and compare how mean and median respond to one extreme value.

### Lesson 4 — Charts, tables, and accessible communication

**Guiding question:** Which representation makes the relevant comparison easiest to understand?

**Core topics**

- Bar chart for category comparisons
- Histogram for a quantitative distribution
- Scatter plot for two quantitative variables
- Crosstab or grouped bar chart for two categorical variables
- Table or structured text when exact values or nonvisual access matter
- Titles, units, labels, scales, color, ordering, and uncertainty
- Truncated axes, dual axes, cherry-picked windows, and decorative distortion
- Text descriptions that state the pattern, evidence, and limitation

**Learning activity**

Students choose among a chart, table, and prose summary for four questions, then repair a misleading example. They must interpret the data without relying on color or visual position alone.

### Lesson 5 — Relationships, uncertainty, and causation

**Guiding question:** When two variables move together, what can we responsibly conclude?

**Core topics**

- Direction, form, strength, and unusual observations in a relationship
- Correlation versus causation
- Confounding and reverse causation
- Random variation and measurement uncertainty
- Generalization beyond a sample
- Honest conclusions and explicit limitations

**Learning activity**

Students compare several causal stories consistent with the same association and identify what additional evidence would distinguish them.

### Synthesis studio — A guided data investigation

Students work through a complete small analysis before beginning the open assignment:

1. State a question
2. Inspect source and metadata
3. Select relevant variables
4. Clean and document
5. Summarize and represent
6. Interpret
7. State a limitation and a next question

Python should be demonstrated as a reproducible route, but a spreadsheet or accessible table tool may be used when it better supports the quantitative outcome. Tool choice must not change the rubric.

### Week 8 artifact

An accessible community-data story using either a student-selected dataset or one of several curated fallbacks. It must include:

- A researchable question
- Source and collection context
- A cleaning log
- At least one quantitative summary
- A chart plus equivalent table and text description, or a justified nonvisual representation
- A conclusion proportional to the evidence
- One limitation and one stakeholder or community implication

### Optional deeper dives

- More advanced chart customization
- Sampling distributions and confidence intervals
- Maps and their accessibility challenges
- APIs or larger datasets
- Statistical modeling

## Unit 9 — Artificial Intelligence and Automated Decisions

### Purpose

Give students a durable model of AI that survives product cycles. Students should understand the training pipeline, see one optimization idea, know what neural and language models do at a useful level, and practice evaluating outputs and consequences.

Detailed gradient and backpropagation mechanics should become optional deeper dives rather than consuming four core lessons.

### Lesson 1 — What counts as AI?

**Guiding question:** Why do systems described as “intelligent” keep changing as they become familiar?

**Core topics**

- AI as a changing umbrella term
- Rules, search, optimization, machine learning, and generative models
- Narrow systems and claims about general intelligence
- Model, product, and institution as different objects of analysis
- Automation versus autonomy
- Anthropomorphic language and marketing
- A short historical timeline including changing expectations

**Learning activity**

Students classify familiar systems by mechanism and task rather than deciding whether each is “really intelligent.”

### Lesson 2 — Learning from examples

**Guiding question:** How does a machine-learning system differ from a program whose rules were directly written by a person?

**Core topics**

- Examples, features, labels, and targets
- Classification, regression, and clustering as different tasks
- Training, validation, and test data
- Generalization rather than memorization
- Data leakage and distribution shift
- Human choices in labels and objectives
- Baselines

**Learning activity**

Students design a tiny classifier on paper, identify ambiguous labels, and predict how an unrepresentative training set will fail.

### Lesson 3 — Models learn by reducing measured error

**Guiding question:** How can repeated feedback adjust a model without a person hand-writing every rule?

**Core topics**

- Model parameters as adjustable values
- Prediction, error or loss, update, and repetition
- Fitting a line as a visible example
- Gradient descent as following local information toward a lower loss
- Learning rate and stopping
- Training objective versus the real-world goal
- Evaluation using held-out examples and more than one metric

**Learning activity**

Students run a small numerical training loop with one consistently defined loss function. The visual curve, readout, prose, and update rule must describe the same objective.

### Lesson 4 — From neural networks to language models

**Guiding question:** What changed when models gained many layers, parameters, and training examples?

**Core topics**

- Artificial neuron as weighted combination plus nonlinearity
- Layers and learned internal representations
- Backpropagation as a method for assigning parameter updates, without full derivation
- Compute, data, and engineering behind deep learning
- Tokens, embeddings, attention, and next-token prediction at a conceptual level
- Causal generation: a model cannot attend to future tokens while producing the next one
- Training versus inference
- Why fluent output is not built-in fact checking

**Learning activity**

Students follow one short sequence through tokenization, candidate next-token probabilities, and selection. A text table is the canonical state representation.

### Lesson 5 — Evaluating use, failure, and impact

**Guiding question:** What evidence should we demand before delegating a task or decision to an AI system?

**Core topics**

- Confabulation, brittleness, prompt sensitivity, and automation bias
- Task-specific testing and comparison with a baseline
- Disparate errors and downstream harm
- Privacy, intellectual property, security, and data provenance
- Human labor in data production, evaluation, moderation, and deployment
- Energy, water, hardware, and material costs
- Human oversight, recourse, and accountability
- Appropriate use as a contextual judgment, not “AI good” or “AI bad”

**Learning activity**

Students test or examine provided outputs for a defined task, record failures, verify claims against independent sources, and recommend whether and how the system should be used.

This human-centered and privacy-aware treatment is consistent with [UNESCO's guidance for generative AI in education](https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research) and the risk-oriented framing of the [NIST Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence).

### Synthesis studio — Audit an AI system

Students choose a supported route:

- Interact with an approved tool without entering personal or private data
- Use an instructor-provided transcript and output set
- Examine a small non-generative classifier

They define a task, create test cases, compare outputs with evidence, identify stakeholders, and recommend use conditions or rejection.

### Week 9 artifact

An AI audit containing:

- A plain-language system and task description
- At least five purposeful test cases
- An expected-result or verification method
- Documented strengths and failures
- Independent sources for factual evaluation
- Discussion of privacy, bias, labor, environmental, or access impacts as relevant
- A justified recommendation and human-oversight plan

The assignment must never require a consumer AI account. AI-generated code must be tested against a correctness oracle, not merely made to run.

### Optional deeper dives

- Detailed gradient-descent mathematics
- Backpropagation interactive
- Confusion matrices and precision/recall
- Transformer architecture
- Reinforcement learning
- Retrieval-augmented generation and tool use

## Unit 10 — Security, Privacy, and Responsible Computing

### Purpose

End by integrating systems and human behavior. Students should leave with practical protective habits and a conceptual taste of technical security: threat modeling, authentication, encryption, integrity, recovery, and the limits of safeguards.

Security should not be framed as “being smarter than the victim next door.” The goals are reducing risk, limiting harm, supporting one another, and recovering effectively.

### Lesson 1 — Think in assets, threats, and risk

**Guiding question:** Security against whom, for what, and at what cost?

**Core topics**

- Asset, actor, vulnerability, threat, likelihood, and impact
- Confidentiality, integrity, and availability
- Authentication, authorization, and accountability
- Attack surface and least privilege
- Security as risk reduction rather than perfection
- People as participants in a system, not “the weakest link”
- How safety needs differ by circumstance and identity

**Learning activity**

Students create a small threat model for an email account or shared document and prioritize safeguards by likelihood and impact.

### Lesson 2 — Manipulation, malware, and verification

**Guiding question:** Why attack a cryptographic system when a message can persuade someone to open the door?

**Core topics**

- Social engineering, phishing, impersonation, urgency, and authority
- Malicious links, attachments, software, and permissions
- Malware and ransomware at a conceptual level
- Synthetic media and AI-assisted scams
- Lateral reading and independent channels of verification
- Separating message content from evidence about its source
- Safe reporting without shame

**Learning activity**

Students analyze realistic but inert messages, identify emotional and technical signals, and write a safe verification plan.

### Lesson 3 — Identity, passwords, MFA, and passkeys

**Guiding question:** How can a system know that a request really comes from the right person?

**Core topics**

- Identification, authentication, and authorization
- Long, unique passwords and password managers
- Password hashing at a conceptual level
- Multi-factor authentication
- Phishing-resistant authentication and passkeys
- Account recovery as part of the security system
- Credential stuffing and breached-password reuse

**Learning activity**

Students compare account-protection plans and identify which attacks each control does and does not address.

### Lesson 4 — Secrets, integrity, and trust on a network

**Guiding question:** How can two parties communicate over a network that others can observe or alter?

**Core topics**

- Encryption versus encoding
- Symmetric and public-key encryption at a conceptual level
- Hashes for integrity and password storage
- Digital signatures and certificates as chains of trust
- HTTPS: protection in transit, not proof that a site is honest
- End-to-end encryption
- VPNs as a shift in trust, not automatic invisibility
- Metadata and what encryption may not hide

**Learning activity**

Students match mechanisms to goals—confidentiality, integrity, authentication, or anonymity—and explain a common misconception.

### Lesson 5 — Privacy, harassment, and recovery

**Guiding question:** What should we do before and after prevention fails?

**Core topics**

- Tracking, permissions, data brokers, and privacy settings
- Data minimization and audience boundaries
- Harassment, stalking, doxxing, and documentation
- Updates and vulnerability repair
- Backups with versioning and an offline or otherwise separated copy
- Synced storage versus backup
- Account, device, and ransomware recovery
- Data exfiltration as harm that restoration cannot undo
- Reporting, trusted support, and victim-centered response

**Learning activity**

Students build a recovery checklist for one realistic incident and identify when technical repair, institutional reporting, financial action, or personal-safety support is needed.

### Synthesis studio — A personal or community threat model

Students analyze a scenario such as a compromised email account, small community organization's shared drive, creator's public profile, or family device. They must prioritize actions rather than list every possible defense.

### Week 10 artifact and course synthesis

Students create a digital self-defense guide for a defined audience. The format may be:

- Linear web page or accessible document
- Mini-zine with a complete reading order and text equivalent
- Audio guide with transcript
- Slide deck with speaker notes and accessible exported version
- Plain-language incident-response checklist

The guide must include:

- A threat model for its audience
- At least three prioritized practices
- Explanation of what each practice protects and does not protect
- A recovery plan
- Authoritative sources
- Accessible structure and descriptions
- A final connection among at least four earlier course units

### Optional deeper dives

- Hands-on public-key cryptography
- Digital signatures and certificate inspection
- Secure software development
- Network scanning in a controlled environment
- Digital forensics

## Assessment progression

The ten artifacts should form a deliberate progression rather than ten isolated assignments.

| Week | Primary intellectual move | Technical or analytical evidence |
|---|---|---|
| 1 | Define a representation | Encoding specification and examples |
| 2 | Explain a system across layers | Packet/path trace and stakeholder map |
| 3 | Implement a precise process | Function-based program and tests |
| 4 | Control behavior over cases and time | Conditional, loop, and branch coverage |
| 5 | Model related information | Schema, collections, and usability revision |
| 6 | Preserve and query information | Persistent data, validation, tests, and change log |
| 7 | Compare computational approaches | Traces, operation counts, and scaling argument |
| 8 | Make an evidence-bounded claim | Provenance, cleaning log, analysis, accessible representation |
| 9 | Evaluate an automated system | Test suite, verification, impact analysis, recommendation |
| 10 | Integrate knowledge for an audience | Threat model, prioritized guide, recovery plan, accessible communication |

### Portfolio checkpoints

At the end of Week 5, students select two artifacts and write a brief explanation of how their view of programs and data has changed.

At the end of Week 10, students select or revise three artifacts demonstrating:

- Making a computational artifact
- Reasoning with algorithms or quantitative evidence
- Evaluating social, ethical, accessibility, privacy, or security consequences

If a cumulative final exam is institutionally required, it should be open-note and scenario-based. It should ask students to apply the layered course model, not reproduce vocabulary definitions from ten units.

## Recurring threads across all ten units

### Accessibility and HCI

Every unit should contain one explicit access question:

- Unit 1: How can the same information be represented in multiple perceivable ways?
- Unit 2: Who can connect and use the protocols or services?
- Unit 3: Are program output and error messages understandable?
- Unit 4: Can every control-flow path be reached and explained?
- Unit 5: Does the data model and interface include the intended users?
- Unit 6: Are documentation and workflows usable by someone other than the author?
- Unit 7: Can the algorithm or simulation be traced without relying on a diagram?
- Unit 8: Can the evidence be understood without color or visual position?
- Unit 9: Whose data and needs shape model performance?
- Unit 10: Do safeguards work for people facing different risks and constraints?

### Careers

Each unit should feature two concise career vignettes: one primarily technical and one interdisciplinary. Examples include:

- Unit 1: computer architect; digital archivist
- Unit 2: network engineer; technology-policy analyst
- Unit 3: software developer; computational artist
- Unit 4: quality engineer; operations analyst
- Unit 5: UX researcher; accessibility engineer
- Unit 6: database administrator; research-data manager
- Unit 7: algorithms researcher; logistics planner
- Unit 8: data analyst; public-interest data journalist
- Unit 9: machine-learning engineer; model evaluator or AI-policy researcher
- Unit 10: security analyst; trust-and-safety specialist

These should emphasize daily questions, collaborators, and preparation rather than salary or hype.

### Sustainability and material infrastructure

Computing should not be presented as immaterial. Short recurring connections should include:

- Materials, energy, repair, and e-waste in Unit 1
- Cables, data centers, energy, and water in Unit 2
- Efficiency and resource use in Units 7–9
- Longevity, updates, and replacement cycles in Unit 10

### Verification

Students should repeatedly practice distinguishing:

- A source from a claim
- Running from correctness
- Correlation from causation
- Fluent output from verified output
- Encryption from legitimacy
- A technical possibility from a justified social decision

## Current-to-proposed content crosswalk

| Current unit | Proposed treatment |
|---|---|
| Unit 1: 9 lessons | Merge binary lessons; merge four image/compression lessons; add system architecture and sound; correct copyright; retain five core lessons |
| Unit 2: 8 lessons | Preserve the distributed-to-centralized narrative; consolidate outages and infrastructure; correct history; retain five core lessons |
| Unit 3: 7 lessons plus setup | Move setup to Unit 0; consolidate syntax topics around worked programs; keep debugging/testing; do not require loops; retain five core lessons |
| Unit 4: 5 lessons | Largely preserve; strengthen testing and align the assignment so a decision and loop are required |
| Unit 5: 7 lessons | Consolidate sequence and loop patterns; make tuples optional; add modeling, HCI, accessibility, and privacy; retain five core lessons |
| Unit 6: 5 lessons | Keep files/CSV; reduce package-install detail; add a small SQL taste and explicit software-engineering lesson |
| Unit 7: 6 lessons | Keep search, Big-O, halting, and Game of Life; add practical intractability; move Game of Life into the synthesis studio |
| Unit 8: 11 lessons | Replace separate tool/chart pages with a five-lesson inquiry cycle; preserve misleading-chart and causation material; require accessible representations |
| Unit 9: 11 lessons | Compress line fitting, optimization, neural networks, and language models; move detailed backpropagation to optional depth; center evaluation and impact |
| Unit 10: 9 lessons | Consolidate scams and misinformation; add threat modeling, encryption, hashing, and network trust; retain privacy, harassment, and recovery |

## Material intentionally kept outside the core

The following topics are worthwhile, but requiring them would make the course less coherent or crowd out more durable concepts:

- Object-oriented programming
- Recursion as a programming technique
- Detailed sorting implementations
- Formal proofs of asymptotic bounds
- Full SQL joins and database normalization
- Pandas syntax as a learning outcome
- Gradient calculations or a detailed backpropagation derivation
- Exhaustive chart taxonomies
- Exhaustive cybersecurity attack catalogs
- Competence with any particular commercial AI product
- Public posting as a course requirement

Optional material should be visibly labeled “Explore further” and should not appear on quizzes unless it is promoted to the core.

## Workload target

The official course guide lists 30 lecture and 30 lab hours across a ten-week term. A reasonable weekly design target is:

- Five core lessons and checks: about 2.5–3 hours
- Guided synthesis studio: about 2–2.5 hours
- Quiz, reflection, and course communication: about 0.5–1 hour
- Independent completion or refinement of the weekly artifact: approximately 2–4 additional hours, depending on the student's route and prior experience

No week should become longer merely because it concerns AI or data. Optional dives should not be necessary to complete a quiz or assignment.

Before release, each unit should be tested by at least one novice reader using a screen reader or text-only presentation and by one novice reader using the ordinary visual route. Time-on-task should be measured rather than inferred from word count alone.

## Revision sequence suggested by this outline

This document is a target architecture, not a recommendation to rewrite all units simultaneously.

1. Reconcile the syllabus, grading, schedule, and official assignment names.
2. Adopt the common five-lesson-plus-studio template.
3. Repair Weeks 3 and 4 first because their assessment alignment is currently inverted.
4. Finish and publish the equivalent assignment routes.
5. Consolidate Units 8–10, where the greatest workload reduction is available.
6. Add architecture to Unit 1, HCI to Unit 5, SQL/software engineering to Unit 6, and cryptography to Unit 10.
7. Rewrite quizzes and assignment rubrics only after each unit's final core outcomes are fixed.
8. Pilot time-on-task and accessibility, then revise before broad deployment.

## Research and policy references

These sources informed the design. CS2023 describes an entire undergraduate discipline and is not treated here as a checklist for a single general-education course; it is used to identify major areas and cross-cutting concerns that the survey should sample.

- [PCC Course Content and Outcomes Guide for CS 160, Summer 2026](https://www.pcc.edu/ccog/cs/160/)
- [ACM/IEEE-CS/AAAI Computer Science Curricula 2023](https://csed.acm.org/wp-content/uploads/2025/11/CS2023-Report.htm)
- [CS2023 Knowledge Areas](https://csed.acm.org/knowledge-areas/)
- [CAST Universal Design for Learning Guidelines 3.0](https://udlguidelines.cast.org/)
- [W3C Web Content Accessibility Guidelines 2.2](https://www.w3.org/TR/WCAG22/)
- [Sentance, Waite, and Kallia: Teaching Computer Programming with PRIMM](https://doi.org/10.1080/08993408.2019.1608781)
- [Vieira, Yan, and Magana: Worked Examples for Programming and Algorithm Design](https://jocse.org/articles/6/1/1/)
- [American Statistical Association: GAISE College Report](https://www.amstat.org/asa/files/pdfs/GAISE/GaiseCollege_Full.pdf)
- [NIST AI Risk Management Framework: Generative AI Profile](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence)
- [UNESCO Guidance for Generative AI in Education and Research](https://www.unesco.org/en/articles/guidance-generative-ai-education-and-research)
- [NIST SP 800-50 Rev. 1: Building a Cybersecurity and Privacy Learning Program](https://csrc.nist.gov/pubs/sp/800/50/r1/final)
