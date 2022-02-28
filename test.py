from Agent import Agent

GOALWORD = ""
agent = Agent()

def CheckWord(guessedWord: str) -> any:
    """
    Compares given word with the goal word and returns any found
    information.
    
    Args:
        guessedWord: The word to be compared to the goal word.

    Returns:
        An array for all the letters not in the goal word,
        An array for all the letters in the goal word but in the incorrect location,
        An array for all the letters in the goal word and in the correct location.
    """

    incorrectLetters = []
    lettersIncorrectPos = [None, None, None, None, None]
    lettersCorrectPos = [None, None, None, None, None]
    for guessIndex, guessLetter in enumerate(guessedWord):
        letterInWord = False
        for goalIndex, goalLetter in enumerate(GOALWORD):
            if guessLetter == goalLetter and guessIndex == goalIndex:
                lettersCorrectPos[guessIndex] = guessLetter
                letterInWord = True
                continue
            elif guessLetter == goalLetter and guessIndex != goalIndex:
                lettersIncorrectPos[guessIndex] = guessLetter
                letterInWord = True
        if not letterInWord:
            incorrectLetters.append(guessLetter)
    return incorrectLetters, lettersIncorrectPos, lettersCorrectPos

def isGoalWord(guessWord: str) -> bool:
    """
    Returns True if given word is the goal word.
    
    Args:
        guessWord: The word to be checked if it matches the goal word.

    Returns:
        True if the given word is the goal word.
    """

    return guessWord == GOALWORD

gameOver = False
GOALWORD = agent.GetRandomWord()
numberOfAttempts = 0

while not gameOver and numberOfAttempts < 6:
    print("<><><><><><><><><><><>")
    print("Goal Word: " + GOALWORD)
    numberOfAttempts += 1
    guessedWord = agent.GetGuessWord()
    incorrectLetters, lettersIncorrectPos, lettersCorrectPos = CheckWord(guessedWord)
    print("Guessing: " + guessedWord)
    print("===================")
    agent.UpdatePossibleWords(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)
    gameOver = isGoalWord(guessedWord)

if numberOfAttempts >= 6:
    agent.AddNewWord(input("New Word >? "))

print("YOU WON!")