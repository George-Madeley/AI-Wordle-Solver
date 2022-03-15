from Agent import Agent

import sys
import time
import keyboard
import json
import pyperclip
from datetime import date

def Main():
    """
    Checks the number of arguments given and runs a given test.
    """

    print(sys.argv)
    if (len(sys.argv) < 3):
        print("\n\tError, program needs three arguments to run\n" )
        sys.exit(1)
    if bool(sys.argv[1]):
        configFile = sys.argv[2]
        Wordle(configFile)
    else:
        TestAllKnownWords()

def CheckForPreviousAttempts(agent: Agent, allColors: list, guessedWords: list) -> any:
    """
    Asks the user if any previous attempts were made and what were those previous attempts.
    
    Args:
        agent: The AI.
        allColors: An array of all previously found colors.
        guessedWords: A list to keep track of all the previous guesses.
    
    Returns:
        The current attempt number.
        A list of all of the previous found colors.
        A list of all of the previous guessed words.
    """
    
    numberOfAttempts = int(input("How many previous Attempts:\t"))
    if numberOfAttempts > 0:
        filePath = agent.GetScreenshot()
        for attemptNumber in range(numberOfAttempts):
            guessWord = str(input(f"What was the {attemptNumber + 1} word:\t"))
            guessedWords.append(guessWord)
            colorList = agent.ReadImage(attemptNumber, filePath)
            allColors.append(colorList)
            incorrectLetters, lettersIncorrectPos, lettersCorrectPos = agent.GetInformation(guessWord, colorList)
            agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)
    return numberOfAttempts, allColors, guessedWords

def CheckWord(guessWord: str, goalWord: str) -> any:
    """
    Compares given word with the goal word and returns any found
    information.
    
    Args:
        guessedWord: The word to be compared to the goal word.
        goalWord: The goal word.

    Returns:
        An array for all the letters not in the goal word,
        An array for all the letters in the goal word but in the incorrect location,
        An array for all the letters in the goal word and in the correct location.
    """

    guessWord = guessWord.rstrip("\n")
    incorrectLetters = []
    lettersIncorrectPos = [None, None, None, None, None]
    lettersCorrectPos = [None, None, None, None, None]

    # Counts how many times each letter appears in the goal word.
    letterCount = {}
    for letter in goalWord:
        if not letter in letterCount.keys():
            letterCount[letter] = goalWord.count(letter)

    for guessIndex, guessLetter in enumerate(guessWord):
        if guessLetter in goalWord:
            letterCount[guessLetter] -= 1
            if guessLetter == goalWord[guessIndex]:
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

def FindPreviousWord(allWords: list) -> int:
    """
    Gets the infex of a given word.
    
    Args:
        allWords: All words from the text file.
        
    Returns:
        The index of the word.
    """

    lastWordTested = input("What was the last tested word:\t")
    try:
        index = allWords.index(f"{lastWordTested}\n")
    except ValueError:
        index = 0
    return index

def isGoalWord(guessWord: str, GOALWORD: str) -> bool:
    """
    Returns True if given word is the goal word.
    
    Args:
        guessWord: The word to be checked if it matches the goal word.

    Returns:
        True if the given word is the goal word.
    """

    return guessWord == GOALWORD
    
def ReadJSON(JSONFilename: str) -> dict:
    """
    Reads the JSON data and returns the data.

    Args:
        JSONFilename: The name of the JSON file.
    
    Returns:
        The data as a dictionary.
    """
    
    data = None
    with open(JSONFilename, "r") as wordleConfig:
        data = json.load(wordleConfig)
    return data

def RecordWordleData(fileName: str, numberOfAttempts: int, guessedWords: list, removedWords: list, addedWord: str, allColors: list, wordleConfig: dict) -> None:
        """
        Records how the last game went and appends it to a file.
        
        Args:
            fileName: The anme of the record file.
            numberOfAttampts: The number of attempts it took the agent to solve the Wordle.
            guessWords: A list of all the guessed words in order.
            removedWords: A lits of all removed words.
            addedWord: The added word.
            allColors: The colors of the previous attempts.
            wordleConfig: The data from the config file.
        """

        # Generates its own emojis if required
        if wordleConfig["makeemojis"] == "True":
            wordleShareData = f"Wordle {numberOfAttempts}/6\r\r"
            for row in allColors:
                for color in row:
                    if color == "grey":
                        wordleShareData += "⬛"
                    elif color == "yellow":
                        wordleShareData += "🟨"
                    elif color == "green":
                        wordleShareData += "🟩"
                wordleShareData += "\r"
            wordleShareData += "\r"
        else:
            wordleShareData = pyperclip.paste()

        # Appends to the record file.
        with open(fileName, 'a', encoding="UTF-8") as recordFile:
            recordFile.write(f"=======================================\n")
            recordFile.write(f"Date: {date.today()}\n")
            recordFile.write(f"\nNumber of attempts: {numberOfAttempts}/6\n")
            for attempt, word in enumerate(guessedWords):
                recordFile.write(f"Attempt {attempt}: {word}\n")
            if removedWords:
                recordFile.write(f"\nRemoved Words:\n")
                for removedWord in removedWords:
                    recordFile.write(f"\t- {removedWord}\n")
            if addedWord:
                recordFile.write(f"\nAdded Words:\n")
                recordFile.write(f"\t+ {addedWord}\n")
            recordFile.write(f"-------------------\n")
            recordFile.write(wordleShareData.replace('\n', '') + "\n\n")

def RunGame(goalWord: str) -> list:
    """
    Runs the game with the given goal word.
    
    Args:
        goalWord: the goal word the agent has to guess.
        
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
        gameOver = isGoalWord(guessedWord, goalWord)
        if gameOver:
            continue
        incorrectLetters, lettersIncorrectPos, lettersCorrectPos = CheckWord(guessedWord, goalWord)
        agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)

    if numberOfAttempts >= 6 and not gameOver:
        # agent.AddNewWord(input("New Word >? "))
        return False, numberOfAttempts
    return True, numberOfAttempts

def TestAllKnownWords() -> None:
    """
    Tests the agent against all known words.
    """

    numberOfWords = 0
    totalAttempts = 0
    totalTime = 0

    # Gets all known words.
    with open("assets/ListOfWords.txt", "r") as allWordsFile:
        allWords = allWordsFile.readlines()

    # Finds were the test left off
    index = FindPreviousWord(allWords)
    numberOfWords = len(allWords)
    while index < numberOfWords:
        word = allWords[index]
        GOALWORD = word.replace('\n', '').lower()
        if len(GOALWORD) != 5:
            print("ERROR: " + GOALWORD + " has a length of more than five")
        else:
            # os.system('cls' if os.name == 'nt' else 'clear')
            startTime = time.perf_counter()
            result, attempts = RunGame(GOALWORD)
            endTime = time.perf_counter()

            totalAttempts += attempts
            with open("assets/TestRecord.txt", "a") as testRecordFile:
                if result:
                    testRecordFile.write(f'{str(GOALWORD)}\t{str(attempts)}\n')
                    print(f"number: {str(index)}, Goal Word: \033[0;32;40m {GOALWORD} \033[0;0m attempts: {str(attempts)}")
                else:
                    testRecordFile.write(f'\t\t{str(GOALWORD)}\t{str(attempts)}\n')
                    print(f"number: {str(index)}, Goal Word: \033[0;31;40m {GOALWORD} \033[0;0m attempts: {str(attempts)}")
        diffTime = endTime - startTime
        print(f"Time: {diffTime}\n")
        totalTime += diffTime
        index += 1

    with open("assets/TestRecord.txt", "a") as testRecordFile:      
        testRecordFile.write(f"Average Number of Attempts:\t{str(totalAttempts / numberOfWords)}\n")
        testRecordFile.write(f"Total Time Taken:\t{totalTime}, Average Time:\t{totalTime / numberOfWords}\n")

def Wordle(configFileName: str):
    """
    Tests the AI against actually Wordle games.
    
    Args:
        configFile: The name of the config file to use.
    """

    wordleConfig = ReadJSON(configFileName)

    isLooping = wordleConfig["infiniteloop"] == "True"
    checkPreviousAttempts = wordleConfig["checkpreviousattempts"] == "True"
    addWords = wordleConfig["addwords"] == "True"

    

    setLooping = True
    while setLooping:
        setLooping = isLooping
        agent = Agent(wordleConfig)

        gameOver = False
        numberOfAttempts = 0
        guessedWords = []
        removedWords = []
        addedWord = None
        allReadColors = []

        if checkPreviousAttempts:
            numberOfAttempts, allReadColors, guessedWords = CheckForPreviousAttempts(agent, allReadColors, guessedWords)

        print("Press ESC to continue...")
        keyboard.wait('esc')
        print("PRESSED ESC")
        # Plays the Game
        while not gameOver and numberOfAttempts < 6:
            guessWord = agent.GetGuessWord(numberOfAttempts)
            keyboard.write(guessWord)
            print("Press ENTER to continue...")
            keyboard.wait('enter')
            print("PRESSED ENTER")
            time.sleep(float(wordleConfig["turndelay"]))
            screenShotFilePath = agent.GetScreenshot()
            readColorsList = agent.ReadImage(numberOfAttempts, screenShotFilePath)
            allReadColors.append(readColorsList)
            # Checks if the word was invalid
            if readColorsList.count("black") == 5:
                removedWords.append(guessWord)
                agent.RemoveWord(guessWord)
                for i in range(5):
                    keyboard.press_and_release('backspace')
                continue
            guessedWords.append(guessWord)
            # Checks if an error was raised due to the win screen.
            try:
                incorrectLetters, lettersIncorrectPos, lettersCorrectPos = agent.GetInformation(guessWord, readColorsList)
            except ValueError:
                gameOver = True
                break
            # Checks if the goal word was found.
            if None not in lettersCorrectPos:
                gameOver = True
                continue
            agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)
            numberOfAttempts += 1
        # Checks if the AI lost due to not knowing the Goal Word.

        if addWords:
            if numberOfAttempts >= 6:
                isValid = str(input("Do you want to add a word? (Y/N)\t")).lower() != "y"
                while not isValid:
                    newWord = str(input("Enter new Word:\t")).lower()
                    if len(newWord) == 5:
                        isValid = True
                        addedWord = newWord
                        agent.AddNewWord(newWord)
                        continue
                    print("The word you have entered is invalid. Please try again.")

        keyboard.press_and_release('enter')
        location = agent.FindShareButton()
        agent.ClickShareButton(location)
        fileName = wordleConfig["recordfile"]
        RecordWordleData(fileName, numberOfAttempts, guessedWords, removedWords, addedWord, allReadColors, wordleConfig)
        time.sleep(0.5)


if __name__ == "__main__":  
    Main()
