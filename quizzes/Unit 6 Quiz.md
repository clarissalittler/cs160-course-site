## Unit 6 Quiz — Python Project Studio: Putting the Pieces Together

### Multiple Choice

**1.** Given `schedule["repair"]["tags"][0]`, what does Python look up first?
- A) The item at index 0
- B) The `repair` key
- C) Every tag in the schedule
- D) The `tags` key

**2.** You want to build a "what should I cook tonight?" helper. Your ideas: ask for one ingredient and suggest a matching recipe from a short list, user accounts with saved favorites, a photo of every dish, and a way to export a shopping list. Following Lesson 1, what should you get working first?
- A) All four features at once, so they can be tested together at the end
- B) One thin path from start to finish (show the prompt, read an ingredient, suggest a recipe, quit cleanly), with the other ideas saved for after that path works
- C) The dish photos, since the display is what people notice first
- D) The accounts system, since every other feature depends on knowing who is using the program

**3.** When an event may or may not contain a `location` key, which expression safely supplies a fallback?
- A) `event["location"]["not listed"]`
- B) `event.get("location", "not listed")`
- C) `event.append("location")`
- D) `"not listed" in event["location"]`

**4.** You ask a friend to try your text adventure without any coaching. They pause, then type `grab lamp`, but your program only understands `take`. What does Lesson 5 suggest you do with that moment?
- A) Jump in and tell them the right word, since the program itself works fine
- B) Ignore it, because your own test table already showed that `take lamp` works
- C) Treat the pause as useful evidence, and revise something, like showing the command list
- D) Rename your variables so the code is easier for the next reader to follow

**5.** What does `", ".join(event["tags"])` produce?
- A) A readable string containing the tags separated by commas
- B) A new event for every tag
- C) A sorted dictionary
- D) A Boolean value

**6.** A function cannot advance to another valid selection. What is a reasonable value to return?
- A) The current selection, unchanged
- B) A random selection
- C) The first dictionary key
- D) An empty list, regardless of the input type

### True / False

**7.** Moving a title from an `available` list to a `borrowed` list changes the running program's state.

**8.** According to Lesson 1, planning a program completely before writing any code is the correct way to program, and bricolage (tinkering as you go) is a sloppy habit that strong programmers grow out of.

### Multiple Choice (continued)

**9.** A playlist starts with `current_index = 0`. A function returns `(1, "Moving to the next song.")`, and the caller assigns both returned values. What is `current_index` afterward?
- A) `0`, because functions cannot change values outside themselves
- B) `1`, because the caller assigns the first returned value back to `current_index`
- C) `2`, because two values were returned
- D) `"Moving to the next song."`, because the message is returned last

**10.** Which option is the strongest manual test for an interactive program's "play next" command?
- A) Start with an empty queue, choose play next, and expect a clear empty-queue message with the queue still empty
- B) Run the program once and confirm that no red text appears
- C) Read the function name and assume it behaves correctly
- D) Start from an unspecified state, press several keys, and accept any message that appears
