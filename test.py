from Agent import Agent


def CheckWord(guessedWord: str, GOALWORD: str) -> any:
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

    guessedWord = guessedWord.rstrip("\n")
    incorrectLetters = []
    lettersIncorrectPos = [None, None, None, None, None]
    lettersCorrectPos = [None, None, None, None, None]

    # Counts how many times each letter appears in the goal word.
    letterCount = {}
    for letter in GOALWORD:
        if not letter in letterCount.keys():
            letterCount[letter] = GOALWORD.count(letter)

    for guessIndex, guessLetter in enumerate(guessedWord):
        if guessLetter in GOALWORD:
            letterCount[guessLetter] -= 1
            if guessLetter == GOALWORD[guessIndex]:
                lettersCorrectPos[guessIndex] = guessLetter
            else:
                lettersIncorrectPos[guessIndex] = guessLetter
        else:
            incorrectLetters.append(guessLetter)

    # Finds all the letters counted more than required and 
    # removes duplicate letters that have already been accounted for.
    for letter in letterCount:
        if letterCount[letter] < 0:
            for i in range(abs(letterCount[letter])):
                index = lettersIncorrectPos.index(letter)
                lettersIncorrectPos[index] = None
    
    return incorrectLetters, lettersIncorrectPos, lettersCorrectPos

def isGoalWord(guessWord: str, GOALWORD: str) -> bool:
    """
    Returns True if given word is the goal word.
    
    Args:
        guessWord: The word to be checked if it matches the goal word.

    Returns:
        True if the given word is the goal word.
    """

    return guessWord == GOALWORD

def RunGame(GOALWORD) -> bool:
    agent = Agent()
    gameOver = False
    numberOfAttempts = 0

    while not gameOver and numberOfAttempts < 6:
        # print("<><><><><><><><><><><>")
        # print("Goal Word: " + GOALWORD)
        guessedWord = agent.GetGuessWord(numberOfAttempts)
        # print("Guessing: " + str(guessedWord))
        # print("===================")
        gameOver = isGoalWord(guessedWord, GOALWORD)
        if gameOver:
            continue
        numberOfAttempts += 1
        incorrectLetters, lettersIncorrectPos, lettersCorrectPos = CheckWord(guessedWord, GOALWORD)
        agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)

    if numberOfAttempts >= 6:
        # agent.AddNewWord(input("New Word >? "))
        return False

    return True

# RunGame('arise')

noDuplicates = []
allWordsFile = open("ListOfWords.txt", "r")
for line in allWordsFile:
    GOALWORD = line.replace('\n', '').lower()
    if GOALWORD in noDuplicates:
        continue
    noDuplicates.append(GOALWORD)
    if len(GOALWORD) != 5:
        print("ERROR: " + GOALWORD + " has a length of more than five")
    else:
        result = RunGame(GOALWORD)
        if result:
            print('\033[0;32;40m ' + str(GOALWORD) + ' \033[0;0m')
        else:
            print('\033[0;31;40m ' + str(GOALWORD) + ' \033[0;0m')
allWordsFile.close()

