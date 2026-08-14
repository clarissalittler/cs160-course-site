# Week 6 Rubric — Persistent Data Tool

Score each row independently. Half-points are welcome. Add the five scores (20 points possible), then divide by 5 for the 0–4 assignment score.

| Criterion | 4 — Complete and effective | 3 — Mostly demonstrated | 2 — Partly demonstrated | 1 — Beginning evidence | 0 — No evidence |
|---|---|---|---|---|---|
| Loading and safe startup | Loads UTF-8 CSV records into a consistent list of 4+ field dictionaries and safely starts empty when the file is missing. | Normal and missing-file paths mostly work with one minor model or encoding issue. | One path works and the other is meaningfully attempted. | Contains a relevant file-open/read or missing-file attempt. | No loading evidence. |
| Conversion and data quality | Explicitly converts/validates a numerical field and clearly reports malformed or skipped rows. | Conversion and reporting work with one minor validation gap. | Either conversion or malformed-row handling works and the other is attempted. | Attempts a relevant conversion or quality check. | No conversion/quality evidence. |
| Saving and persistence | Saves the full list after changes, and evidence shows correct data after quitting and reloading. | Save/reload works with a minor timing, formatting, or evidence gap. | Data can be saved or reloaded, but the full persistence cycle is unreliable. | Contains a relevant write/save attempt. | No saving evidence. |
| Operations and program structure | Add, display, filter, numerical summary, and quit work through a while-loop menu; responsibilities are separated into clear functions. | Most actions and separation work with one minor gap. | Several actions work, but an important path or separation is incomplete. | One or two relevant actions/functions show progress. | No relevant tool behavior. |
| Testing, documentation, and responsible reuse | Provides all six acceptance cases, data dictionary, provenance, change log, sample run, and copied/AI-code verification statement. | Most evidence is complete with one thin or missing item. | Several useful artifacts are present, including meaningful tests or provenance. | One useful supporting artifact is provided. | No supporting evidence. |

Partial-credit notes: award separately for load, missing-file handling, conversion, row reporting, save, and reload evidence. A failure late in the persistence cycle must not erase earlier working stages or documentation.
