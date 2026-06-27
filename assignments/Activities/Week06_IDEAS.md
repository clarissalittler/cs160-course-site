# Week 6 Activity — Ideas (BLANK WEEK — needs your pick)

Clarissa — you didn't have anything written for Week 6, so here are three pitches. Week 6 lines up with **Unit 6 (data structures: lists, tuples, dictionaries)**, so I aimed everything at "give students a reason to *want* a dictionary." My recommendation is **Idea A**, and I've drafted it as a real starter notebook: `Week06_CollectionTracker.qmd`. The other two are sketches you can promote if you'd rather.

---

## ⭐ Idea A — "Collection Tracker" (RECOMMENDED, drafted)

**The pitch:** Everyone collects *something* — books, vinyl, sneakers, houseplants, video games, Pokémon cards, recipes, concert ticket stubs. Students build a little catalog of their own collection using a **list of dictionaries**, then ask questions of it: how many do I have, which is the oldest, sort them by price, find all the ones tagged "favorite."

**Why it works for this unit:** it's the most natural possible motivation for a dictionary. A single item ("a book") obviously has *named parts* — title, author, year, rating — and a dictionary is exactly "a thing with named parts." Then a collection is obviously a *list* of those. Lists-of-dicts is the workhorse data structure of the real world (it's basically what every JSON API returns), and this makes students feel why.

**Shareable:** yes — they post their catalog and the most surprising thing they learned about their own collection.

**Status:** fully drafted in `Week06_CollectionTracker.qmd`. Ready to use or tweak.

---

## Idea B — "Group Chat Word Counter"

**The pitch:** Students paste in a chunk of text — song lyrics, a paragraph they wrote, a (consenting, anonymized) group-chat excerpt — and the notebook counts how often each word appears, using a **dictionary** as a tally (word → count). Then it shows the top 10 words. Optionally a quick bar chart.

**Why it works:** the "dictionary as a counter/tally" pattern is *the* classic dictionary use case, and it connects beautifully back to Week 1 (text is data) and forward to Unit 8 (turning data into a chart). Seeing your own most-used words is weirdly revealing and fun.

**Watch out for:** privacy if they use real chats — tell them to anonymize, or just use song lyrics / a famous speech. Also "the" will win every time, which is a nice teachable moment about "stop words."

**Effort to finish:** ~1 hour. The counting loop is short; the payoff is high.

---

## Idea C — "Build-a-Cipher with a Dictionary"

**The pitch:** A callback to the cybersecurity/secret-codes thread. Students build a substitution cipher where a **dictionary** maps each letter to a secret symbol (a → 🦊, b → 🌵, …), then encode a message to a classmate, who decodes it with the reverse dictionary.

**Why it works:** a dictionary *is* a lookup table, and a cipher *is* a lookup table, so the data structure and the activity are the same idea — students build the mental model by building the thing. Pairs naturally for the "share with a classmate" requirement (you literally need a partner to send the secret message to).

**Watch out for:** the encode direction is easy; the decode (reversing the dictionary) is the conceptual stretch — could be the "aha," could be a wall depending on your group. Maybe provide the reverse-dictionary line.

**Effort to finish:** ~1–1.5 hours.

---

### My recommendation
Go with **A (Collection Tracker)** as the core activity — it's the most broadly appealing (everyone collects *something*) and the most honest preview of how data really gets structured in the wild. Keep **B** in your back pocket as an alternate for students who don't feel like they collect anything. The draft for A is ready in `Week06_CollectionTracker.qmd`.
