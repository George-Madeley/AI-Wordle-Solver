# AI-Wordle-Solver

An AI that attempts to solve Wordle problems.

## Method

I created this AI which attempts to solve Wordle problems.

### What Is Wordle?

Wordle, created by Josh Wardle, is a game in which the play has to guess a five letter word within six attempts. Every time you enter a word, the game tells you how close you are to the goal word via three means:

- If a letter in the word you entered is *not* in the goal word.
- If a letter in the word you entered *is* in the goal word.
- If a letter in the word you entered is in the goal word and is in the correct position.

The game illiustrates this information by the means of three colors: Grey, Yellow, and Green respectfully. (See example Below):

<img src="/images/example01.jpg" alt="Wordle example, by the Guardian" width="200">

**Figure 1** - Wordle Game example. [1]

From this information, the player must figure out the goal word in the least amount of attempts.

### How the AI was designed

The best AI to use is a knowledge-base AI (the same kind used to beat Mine Sweeper) with logical inference. A knowledge-base AI is an AI that builds up a set of condition (termed the Knowledge-base) then checks if a certain outcome meets those conitions. In the example of Wordle, the agent (we call the AI an agent) builds up its knowledge-base from the results of the previously entered words. If, for instance, we enter the word 'broke' and Wordle tells us that the goal word does not contain the letter 'b', then the agent can add that condition to its knowledgfe-base. If the agent then picks the word 'about', even though it is a valid word, it does not meet the criteria within the knowledge nad therefore, is no longer valid. By using a knowledge, we can filter out all the words that do no meet the criteria set by the knowledge-base.

#### Filtering Out Words

To begin, we create a text file containing every five letter word (or as best as possible). We create an agent class which, upon initialisation, reads each word in the text file, verifies that they are a valid five letter word and then stores them within a LinkedList (I chose a LinkedList becuase I am currently taking a Data Structures and Algorithms course in Python and wanted to apply my knowledge). Next, we build a method that gets a random word from this linked list. When we enter this random word, we recieve the information on wether a letter is in the goal word and is that letter in the correct position. We then add this to our knowledge then filter out any words from our linkedlist that do not meet those conditions. We then pull another random word from the linkedlist of all possible goal words and rinse and repeat.

This proves to be effective however, each time, we are just getting a random word, surely we can do better than that.

#### Double Letters

If the agent has inputted a word with two of the same letter and one of the letters in greyed out, this indicates that only one of that letter appears in the final word. [2]

#### Guess Best Word

If you ever look up Wordle strategies, you will come across people talking about using a 'starting word'. This is a word that consists of the most common letters. But there is a lot of debate about what this word is, therefore, our agent will figure it out.

I built a class which holds the following information: a character and an array of length five. The idea is that the agent will create and instance of this class for each letter of the alphabet (storing that letter in the character attribute). It will then search through all known words and not only count up the number of occurances of that letter but also count the occurances of that letter in each position. i.e.

    drank
    about
    trape
    bread

    Total occurances of a = 4
    Total occurances of a in each position = [1, 0, 2, 1, 0]

This way, not only can we find that word with the most commmon letters but also in their most common location within the word.

Once our agent has calculated the number of occurances of each letter in each position, it then runs through each known word and assigns it a score best on those occurances. i.e.

    a = [12, 34, 8, 72, 3]
    b = [5, 23, 4, 16, 47]
    o = [6, 4, 23, 6, 34]
    u = [24, 13, 56, 34, 3]
    t = [57, 37, 8, 16, 78]

    about = 12 + 23 + 23 + 34 + 78 = 170

**NOTE:** These are not the actual values.

The word with the best score is the best word to use. I designed the system so that the agent would recalculate each letter number of occurances and each words score after every time the agent enters a word and recieves the new conditions. This way, the agent picks the best word for each scenario.

This in theory works very effectively however, there is one problem that I have termed the *-IGHT* (pronouced 'ite' or ee-t-ah).

#### The -IGHT problem

First off, what is this problem? This problem occurs when the goal word ends in 'ight'. This is becuase there are a lot of five letter words that end in 'ight' ('light', 'tight', 'might', 'night', 'sight', 'fight', 'right', and 'eight'). Because there are more than six words, our agent, in the worst-case scenario, cannot brute force its way to the goal word. Why though?

In an example, lets say the goal word was 'eight'. In our current system, if the enters 'sight' as the first attempt, the agent builds its knowledge base then filters out any word that does not end in 'ight'. If the agent then enters any of the following words in and order: 'might', 'night', 'light', 'right', and 'fight', they will only filter out itself and eventually the agent will lose (worst-case scenario).

<img src="/images/ight_example.jpg" alt="-ight lose example, by the Akilan" width="200">

**Figure 2** - Wordle -ight example. [3]

Now, there is a much more efficient way to go about this problem by using the word 'later'. If after the first guess, the agent entered 'later', Wordle would tell it what letters in 'later' are in the goal word. In this case, it would say that 'l', 'a', 't', and 'r' are not in the goal word but 'e' is, therefore, 'eight' would be the last word in the list of the all possible words be the thrid and final attempt. However, the question is, when would the agent know to pick 'later' and other words in similar situations? (because we cant hardcode this answer into the agent). We do it based on the knowledge each word provides.

Every time the agent enters in a word, it learns a number of things. The first time it enters a word, it learns tne things: 'Is this letter in the goal word?' and 'Is this letter in the correct position?' for all five letters. In the -ight example [3] above, everytime the player entered in 'might', 'fight', 'right'... they were only learning one thing: "Is this letter in the goal word?" (they would not be learning if that letter is in the correct position as there is only one position remaining). However, if instead they entered in 'later', they would learn up to nine things.

I could replace the scoring by occurances system with scoring by knowledge system however, it causes a new problem to efficiency. Using the knowledge method, the agent would use the first five attempts to use every letter possible, then in the final attempt, it would, or would not, guess the goal word.

    abcde
    fghij
    klmno
    pqrst
    uvwxy
    GOAL WORD HERE

This is under the assumption of the best case scenario where the agent knows five words which in total use 25 letters of the alphabet. Even with this method, there is chance that the agent will get the right letters but in the incorrect place. So, how can this issue be solved? We need to improve how the agent scores based on knowledge.

Earlier, I stated that 'later' would get a score of nine, however, that is not the case. In the example [3], there was only one letter that needed to be known, as a result, the agent already knows the position for that letter. therefore, 'later' would get a score, at most, of five. But this still does not solve our problem. So what else needs to be done?

The agent is a knowledge-base AI and the key part about this type of AI is that it infers information based on what it already knows. In this, it already knows every five letter word in the English lexicon (ideally). If the agent guesses the word 'enjoy' and Wordle informs it that 'j' is in the goal word, even though we did not use the letter 'x', we know that 'x' would not be in the goal word because there is no five letter word with both 'j' and 'x'. As a result, if the agent were to guess 'beaux' for its second attempt, the letter 'x' would provide zero knowledge.

So in the -ight example, after the agent guesses sight, the list of possible words would only consist of words ending in -ight. These words are as follows: 'tight', 'might', 'night', 'light', 'fight', 'right', and 'eight'. Each one would get a knowledge score of one. However, because the last letter could be 't', 'm', 'n', 'l', 'f', 'r', or 'e', any other letter such 'b' or 'd' would provide zero knowledge. Therefore, if the agent ranked every word it knew based on its score by knowledge, a word such as later would be placed very high with a score of four (the agent knows 'a' is not one of the possible letters and therefore it does not contribute to that words knowledge score).

## Version History

### v1.2.0

- Created a Score by knowledge system which scores each word based on how much new knowledge that will provide to the agent.
- Created a Knowledge base class which stores the agents knowledge or letters in and not in the goal word and their correct and incorrect position.
- The agent now finds more letters that are not in the goal word based on if they do not appear in *all* possible goal words.
- The agent now finds more letters in the incorrect position based on if they do not appear at that location in *all* possible goal words.
- LinkedList was removed and replaced with an Array data type.
- An improved test.py script was created to loop through all known words and finds which words the agent did not solve.
- Fixed `CheckWord` function so it can deal with duplicate letters.
- Made all letters in words lowercase.

### v1.1.2

- Added docstring documentation to all methods, functions, and classes.
- Renamed certain classes, methods, and attributes.
- Added Type to methods and arguments.
- Explained reasoning for AI design to README.md.

### v1.1.1

- Fixed an error related to skipped word after node was removed

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

- Created Node Class and populated it with methods.

## References

[1] <https://www.theguardian.com/games/2022/jan/11/wordle-creator-overwhelmed-by-global-success-of-hit-puzzle>  
[2] <https://www.nationalworld.com/culture/gaming/can-letters-repeat-in-wordle-rules-does-game-have-double-letters-how-to-find-daily-5-letter-words-answer-3557919>  
[3] <https://twitter.com/alc0der/status/1488046655656050691>
