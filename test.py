from main import main

GOALWORD = "drink"
solverAI = main()

def CheckWord(guessedWord):
    lettersNotIncluded = []
    lettersIncluded = []
    lettersInCorrectPos = [None, None, None, None, None]
    for guessIndex, guessLetter in enumerate(guessedWord):
        letterInWord = False
        for goalIndex, goalLetter in enumerate(GOALWORD):
            if guessLetter == goalLetter and guessIndex == goalIndex:
                lettersInCorrectPos[guessIndex] = guessLetter
                letterInWord = True
                continue
            elif guessLetter == goalLetter and guessIndex != goalIndex:
                lettersIncluded.append(guessLetter)
                letterInWord = True
        if not letterInWord:
            lettersNotIncluded.append(guessLetter)
    return lettersNotIncluded, lettersIncluded, lettersInCorrectPos

def isGoalWord(guessWord):
    return guessWord == GOALWORD

gameOver = False
print(solverAI.GetPossibleWords())

while not gameOver:
    guessedWord = input(">?")
    guessedWord = solverAI.GetGuessWord()
    lettersNotIncluded, lettersIncluded, lettersInCorrectPos = CheckWord(guessedWord)
    print("Guessing: " + guessedWord)
    print("-------------------")
    print(lettersNotIncluded)
    print("-------------------")
    print(lettersIncluded)
    print("-------------------")
    print(lettersInCorrectPos)
    print("===================")
    solverAI.UpdatePossibleWords(lettersNotIncluded, lettersIncluded, lettersInCorrectPos)
    gameOver = isGoalWord(guessedWord)
    print(solverAI.GetPossibleWords())
    print("===================")

print("YOU WON!")