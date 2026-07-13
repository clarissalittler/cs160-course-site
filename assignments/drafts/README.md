# Accessible Creative Coding Alternatives for Weeks 3 and 4

The scaffolded “Understanding Internet Problems” proposal was adopted as the active Week 2 assignment on July 10, 2026, with the Wordle protocol question restored as a required section. `Week02_InternetIncidentExplainer_DenseDraft.html` preserves the earlier, more demanding proposal for comparison and possible reuse.

These are text-first, first-class alternatives to the ColabTurtle Week 3 and Week 4 assignments. A student may use one because of an access need or simply because text is a better creative medium for them. The alternatives should be presented as choices, not as reduced or remedial versions of the visual assignments.

Each notebook provides a complete tutorial and assignment rather than only a replacement final prompt. The artifact, examples, exercises, reflection, submission directions, debugging guidance, and grading language are all included in the notebook.

## Student choices

| Week | Notebook | Creative artifact | Core concepts |
|---|---|---|---|
| 3 | `Week03_Alt_MiniZine.ipynb` | Mini-zine, field guide, poster, museum label, or other short publication | execution order, function calls, variables, strings, numbers, expressions, `input()`, f-strings, `for` loops, indentation, loop counters |
| 3 | `Week03_Alt_PatternPoem.ipynb` | Pattern poem, chant, sound score, monologue, or other rule-based text | execution order, function calls, variables, strings, numbers, string expressions, `input()`, f-strings, `for` loops, indentation, loop counters |
| 4 | `Week04_Alt_QuizOracle.ipynb` | Quiz, oracle, sorting system, recommendation machine, or fortune teller | review of Week 3, function definition and calls, parameters and arguments, return values, `if`/`elif`/`else`, comparisons, `and`, `or`, changing state |
| 4 | `Week04_Alt_BranchingRadioPlay.ipynb` | Radio play, text adventure, dramatic scene, or choose-your-own ending | review of Week 3, function definition and calls, parameters and arguments, `if`/`elif`/`else`, comparisons, input normalization, `and`, `or`, changing state |

## Equivalence with the ColabTurtle notebooks

The media differ, but the instructional progression is deliberately parallel.

| ColabTurtle idea | Text-first equivalent |
|---|---|
| A turtle command changes the canvas | A print, input, assignment, or string operation changes the text artifact or its data |
| Commands execute in sequence | Text instructions execute in sequence |
| Named lengths and angles make a drawing easier to revise | Named words, phrases, counts, and story details make a text artifact easier to revise |
| A loop repeats sides or drawing movements | A loop repeats refrains, notices, beats, questions, or sound cues |
| The loop counter changes movement over time | The loop counter changes numbering or repetition over time |
| A drawing function packages a repeated visual element | A presentation function packages a repeated question, result, scene, or sound cue |
| Position, size, and color parameters vary a drawn element | Question, label, location, sound, dialogue, and count parameters vary a text element |
| Conditions choose a shape or behavior | Conditions choose a score, result, story path, or response |

The alternatives add medium-specific instruction where needed. In particular, important structure is expressed with words and labels rather than only blank space, punctuation, capitalization, or a spatial arrangement. Students submit a sample output along with code so the creative artifact can be assessed directly.

## Source and generated files

The `.qmd` files are the editable source. The matching `.ipynb` files are generated Colab-ready notebooks and should be regenerated after source changes. From the repository root, run:

```bash
python3 assignments/drafts/build_notebooks.py
```

The build script runs Quarto for all four sources and replaces Quarto's source-only YAML header with a readable notebook title. Upload the generated notebook to Google Colab or host it where students can make their own copy. Before publishing, open the notebook in a fresh session and run all cells. Interactive examples will ask for sample responses.

## Instructor notes

- Offer both alternatives at the same time as the corresponding turtle assignment and use the grading scale included in the selected notebook.
- Do not require a student to disclose a disability or obtain separate permission to choose a text-first version.
- Grade intentional use of the programming concepts, not literary polish, drawing skill, typing speed, or the length of the artifact.
- Accept screen-reader-friendly plain text, pasted output, or another accessible equivalent for the sample run.
- If a student needs a different input or output format, preserve the computational requirements while changing the medium.
- Every Week 4 route now has the same core full-credit expectations: define an original function, call it more than once, and use at least one meaningful conditional choice. Parameters and additional branches or loops remain supported style challenges, not requirements imposed by one medium but not another.
