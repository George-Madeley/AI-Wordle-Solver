from main import main

GOALWORD = ""
solverAI = main()

# for i in range(len(solverAI.alphabetStats)):
#     print(solverAI.alphabetStats[i].GetCharacter() + ": " + str(solverAI.alphabetStats[i].GetStatTotal()))

def CheckWord(guessedWord):
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

def isGoalWord(guessWord):
    return guessWord == GOALWORD

gameOver = False
GOALWORD = solverAI.GetRandomWord()
numberOfAttempts = 0

while not gameOver and numberOfAttempts < 6:
    print("<><><><><><><><><><><>")
    print("Goal Word: " + GOALWORD)
    numberOfAttempts += 1
    guessedWord = solverAI.GetGuessWord()
    incorrectLetters, lettersIncorrectPos, lettersCorrectPos = CheckWord(guessedWord)
    print("Guessing: " + guessedWord)
    # print("-------------------")
    # print(lettersNotIncluded)
    # print("-------------------")
    # print(lettersIncluded)
    # print("-------------------")
    # print(lettersInCorrectPos)
    print("===================")
    solverAI.UpdatePossibleWords(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)
    gameOver = isGoalWord(guessedWord)
    # print(solverAI.GetPossibleWords())
    # print("===================")

if numberOfAttempts >= 6:
    solverAI.AddNewWord(input("New Word >? "))

print("YOU WON!")