# AI-Wordle-Solver

## Version History

### Bonjour

- IT WORKS!!!
- First successful of the AI solving a WORDLE with no human interface.
- Created main.py to run the AI after the player has pressed `esc` informing the AI you are ready.
- Created feature where the player has to press `enter` to enter the word and after a few seconds, the AI will enter the next word (this is to accommodate animation time).
- Created launch.json setting to run the game via CMD (To test if the AI can guess all words), and a Wordle one (To test the AI against an actual Wordle).

### Gutentag

- Can now infer which letters are in teh word and their position using the colors.

### Hi

- Can now read colors form the images.

### Hello

- Created ReadImage branch
- Created global tuple variables used to find wordle game on screen.
- Created `ReadImage()` method in Agent.py used to read data from a given image.
- Created `__DivideImage()` method in Agent.py which divides up a given image into 30 smaller images representing each character in Wordle/
- Added a Version History file.
