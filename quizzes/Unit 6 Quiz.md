## Unit 6 Quiz — Python Project Studio: Putting the Pieces Together

### Multiple Choice

**1.** Given `schedule["repair"]["tags"][0]`, what does Python look up first?
- A) The item at index 0
- B) The `repair` key
- C) Every tag in the schedule
- D) The `tags` key

**2.** Why might a dictionary be useful for representing connections?
- A) A connection name can be a key whose value identifies the related record
- B) It automatically draws a diagram
- C) It prevents every possible spelling error
- D) Dictionaries can contain only connections

**3.** When an event may or may not contain a `location` key, which expression safely supplies a fallback?
- A) `event["location"]["not listed"]`
- B) `event.get("location", "not listed")`
- C) `event.append("location")`
- D) `"not listed" in event["location"]`

**4.** What is a useful reason to write a string with triple quotation marks?
- A) It automatically repeats forever
- B) It can contain several lines of text
- C) It converts every value to a number
- D) It creates a dictionary

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

**8.** A main command loop is often clearer when it delegates display and action details to small functions with distinct jobs.

### Short Answer

**9.** A playlist starts with `current_index = 0`. The function call returns `(1, "Moving to the next song.")`, and the caller assigns both returned values. What is `current_index` afterward, and why?

**10.** Give one manual test for any small interactive program. State the starting state, the input or action, and the expected state or message afterward.
