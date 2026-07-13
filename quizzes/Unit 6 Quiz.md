## Unit 6 Quiz — Files, Databases, and Software in the Real World

### Multiple Choice

**1.** What happens when an existing file is opened with `open("notes.txt", "w")`?
- A) New text is added after the old text
- B) The old contents are replaced
- C) Python protects the file by raising an error
- D) The file can only be read

**2.** Which exception specifically represents an attempt to read a file that does not exist?
- A) `ValueError`
- B) `IndexError`
- C) `FileNotFoundError`
- D) `NameError`

**3.** With `csv.DictReader`, each CSV row initially becomes:
- A) a dictionary whose values are text
- B) a dictionary with automatically detected numeric types
- C) a list of integers
- D) one comma-containing string

**4.** Which item belongs in a dataset provenance note?
- A) Only the filename
- B) Source, date, collection method, units, license, and known omissions
- C) Only the number of rows
- D) The programmer's favorite record

**5.** Which module normally ships in Python's Standard Library?
- A) `pandas`
- B) `matplotlib`
- C) `sqlite3`
- D) Every package on PyPI

**6.** In SQL, which clause filters rows according to a condition?
- A) `SELECT`
- B) `FROM`
- C) `WHERE`
- D) `AS`

### True / False

**7.** Supplying user values through SQL parameter placeholders is safer than concatenating the values directly into the query text.

**8.** Refactoring means intentionally changing what users observe while keeping the internal code exactly the same.

### Short Answer

**9.** In one or two sentences, explain what this query asks for:
```sql
SELECT name, cost
FROM resources
WHERE area = 'North' AND cost <= 10
ORDER BY cost DESC;
```

**10.** Give one acceptance example or regression test for a program that loads records from a CSV. State the starting condition and expected behavior.
