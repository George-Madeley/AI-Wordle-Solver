# AI-Wordle-Solver

## Version History

### v1.3.4

- Added the ability to add a new word to the ListOfWords.txt if the agent loses a game due to not knowing the word (Unfortunately, this can not be done automatically as pytesseract has a difficult time detecting letters from screenshjots of Wordle).

### v1.3.3

- IT WORKS!!!
- First successful test of the AI solving a WORDLE with no human interface.
- Created main.py to run the AI after the player has pressed `ESC` informing the AI you are ready.
- Created feature where the player has to press `enter` to enter the word and after a few seconds, the AI will enter the next word (this is to accommodate animation time).
- Created launch.json setting to run the game via CMD (To test if the AI can guess all words), and a Wordle one (To test the AI against an actual Wordle).

### v1.3.2

- Can now infer which letters are in the word and their position using the colors.

### v1.3.1

- Can now read colors from the images.

### v1.3.0

- Created ReadImage branch
- Created global tuple variables used to find wordle game on the screen.
- Created the `ReadImage()` method in Agent.py used to read data from a given image.
- Created `__DivideImage()` method in Agent.py which divides up a given image into 30 smaller images representing each character in Wordle/
- Added a Version History file.

### v1.2.2

- Tested the agent completely.
- Included attempt number and the average number of attempts to Test.py.
- Added docstrings to more classes and methods.

### v1.2.1

- Deleted LinkedList.py
- Redesigned Node.py

### v1.2.0

- Created a Score by knowledge system which scores each word based on how much new knowledge will provide to the agent.
- Created a Knowledge base class that stores the agent's knowledge of letters in and not in the goal word and their correct and incorrect position.
- The agent now finds more letters that are not in the goal word based on if they do not appear in *all* possible goal words.
- The agent now finds more letters in the incorrect position based on if they do not appear at that location in *all* possible goal words.
- LinkedList was removed and replaced with an Array data type.
- An improved test.py script was created to loop through all known words and find which words the agent did not solve.
- Fixed the `CheckWord` function so it can deal with duplicate letters.
- Made all letters in words lowercase.

### v1.1.2

- Added docstring documentation to all methods, functions, and classes.
- Renamed certain classes, methods, and attributes.
- Added Type to methods and arguments.
- Explained reasoning for AI design to README.md.

### v1.1.1

- Fixed an error related to the skipped word after the node was removed

### v1.1.0

- Added a list of words file containing a list of five-letter words
- Redesigned the `InitAllWords` method to read the words from the file and raise an error if a word does not have a length of five.

### v1.0.3

- Fixed any errors
- Finished Knowledge Base.
- Created a `UpdatePossibleWords` method which removes any words that do not meet the conditions set by the results of the previous entries.
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

- Created Node Class and populated it with methods.
