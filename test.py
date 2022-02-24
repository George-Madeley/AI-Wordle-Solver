goalWord = "drink"

def CheckWord(guessedWord):
    lettersNotIncluded = []
    lettersIncluded = []
    lettersInCorrectPos = [None, None, None, None, None]
    for guessIndex, guessLetter in enumerate(guessedWord):
        letterInWord = False
        for goalIndex, goalLetter in enumerate(goalWord):
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

gameOver = False

while not gameOver:
    guessedWord = input(">?")
    lettersNotIncluded, lettersIncluded, lettersInCorrectPos = CheckWord(guessedWord)
    print(lettersNotIncluded)
    print("-------------------")
    print(lettersIncluded)
    print("-------------------")
    print(lettersInCorrectPos)
    print("===================")