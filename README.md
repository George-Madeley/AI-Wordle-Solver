# AI-Wordle-Solver
An AI that attempts to solve Wordle problems.

## Version History

### v1.1.0

- Added a list of words file containing a list of five letter words
- Redesigned the `InitAllWords` method to read the words from the file and raise an error if a word does not have a length of five.

### v1.0.3

- Fixed any errors
- Finshed Knowledge Base.
- Created an `UpdatePossibleWords` method which removes any words that do not meet the conditions set by the results of the previous entries.
- Created an `IsGameOver` method which runs every time the AI enters a word and returns true if the word enters matches the goal word.

### v1.0.2

- Created main.py file containing a `main` class
- Created test.py with a `CheckWord` function which returns three arrays:
    
    - One for all the letters not in the goal word
    - One for all the letters in the goal word
    - One for all the letters in the goal word and in the correct pos

### v1.0.1

- Created Linked List Class

### v1.0.0

- Created Node Class and populated it with methods.ss