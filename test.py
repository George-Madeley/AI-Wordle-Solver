import time
from Agent import Agent

import os

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

def RunGame(GOALWORD) -> list:
    """
    Runs the game with the given goal word.
    
    Args:
        GOALWORD: the goal word the agent has to guess.
        
    Returns:
        True if the agent gets the word within the six attempts.
    """

    agent = Agent()
    gameOver = False
    numberOfAttempts = 0

    while not gameOver and numberOfAttempts < 6:
        # print("<><><><><><><><><><><>")
        # print("Goal Word: " + GOALWORD)
        guessedWord = agent.GetGuessWord(numberOfAttempts)
        numberOfAttempts += 1
        # print("Guessing: " + str(guessedWord))
        # print("===================")
        gameOver = isGoalWord(guessedWord, GOALWORD)
        if gameOver:
            continue
        incorrectLetters, lettersIncorrectPos, lettersCorrectPos = CheckWord(guessedWord, GOALWORD)
        agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)

    if numberOfAttempts >= 6 and not gameOver:
        # agent.AddNewWord(input("New Word >? "))
        return False, numberOfAttempts
    return True, numberOfAttempts

# RunGame('enter')


# Test the function of the agent by testing it against all known words.
def main():
    numberOfWords = 0
    totalAttempts = 0
    lastWordTested = str(input("What was the last tested word:\t"))
    with open("TestRecord.txt", "a") as testRecordFile, open("ListOfWords.txt", "r") as allWordsFile:
        allWords = allWordsFile.readlines()
        try:
            index = allWords.index(f"{lastWordTested}\n")
        except ValueError:
            index = 0
        numberOfWords = len(allWords)
        totalTime = 0
        while index < numberOfWords:
            line = allWords[index]
            startTime = time.perf_counter()
            GOALWORD = line.replace('\n', '').lower()
            if len(GOALWORD) != 5:
                print("ERROR: " + GOALWORD + " has a length of more than five")
            else:
                # os.system('cls' if os.name == 'nt' else 'clear')
                result, attempts = RunGame(GOALWORD)
                totalAttempts += attempts
                if result:
                    testRecordFile.write(f'{str(GOALWORD)}\t{str(attempts)}\n')
                    print(f"number: {str(index)}, Goal Word: \033[0;32;40m {GOALWORD} \033[0;0m attempts: {str(attempts)}")
                else:
                    testRecordFile.write(f'\t\t{str(GOALWORD)}\t{str(attempts)}\n')
                    print(f"number: {str(index)}, Goal Word: \033[0;31;40m {GOALWORD} \033[0;0m attempts: {str(attempts)}")
            endTime = time.perf_counter()
            diffTime = endTime - startTime
            print(f"Time: {diffTime}\n")
            totalTime += diffTime
            index += 1
                
        testRecordFile.write(f"Average Number of Attempts:\t{str(totalAttempts / numberOfWords)}\n")
        testRecordFile.write(f"Total Time Taken:\t{totalTime}, Average Time:\t{totalTime / numberOfWords}\n")
if __name__ == "__main__":  
    main()
    pass
