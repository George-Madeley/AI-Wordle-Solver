from Agent import Agent

import time
import keyboard
import json

def RemoveDuplicateWords():
    """
    Removes and duplicate words from the list of words text file.
    """

    allWords = []
    with open("assets/ListOfWords.txt", "r") as allWordsFile:
        for line in allWordsFile:
            word = line.strip('\n').lower()
            if len(word) == 5 and word not in allWords:
                allWords.append(word)
            elif len(word) > 5 and word not in allWords:
                word = word[:5]
                allWords.append(word)
    allWords.sort()
    with open('assets/ListOfWords.txt', 'w') as wordFile:
        for word in allWords:
            wordFile.write(f"{word}\n")
    
def ReadJSON() -> dict:
    """
    Reads the JSON data and returns the data.
    
    Returns:
        The data as a dictionary.
    """
    
    data = None
    with open("config/UnlimitedWordle.json", "r") as wordleConfig:
        data = json.load(wordleConfig)
    return data

def main():
    wordleConfig = ReadJSON()

    print("Press ESC to continue...")
    keyboard.wait('esc')

    # Plays the Game
    while True:
        wordleConfig = ReadJSON()
        agent = Agent(wordleConfig)
        gameOver = False
        numberOfAttempts = 0
        guessedWords = []
        removedWords = []
        allColors = []
        addedWord = None
        while not gameOver and numberOfAttempts < 6:
            guessWord = agent.GetGuessWord(numberOfAttempts)
            keyboard.write(guessWord)
            keyboard.press_and_release('enter')
            time.sleep(0.1)
            filePath = agent.GetScreenshot()
            colorList = agent.ReadImage(numberOfAttempts, filePath)
            allColors.append(colorList)
            # Checks if the word was invalid
            if colorList.count("black") == 5:
                removedWords.append(guessWord)
                agent.RemoveWord(guessWord)
                for i in range(5):
                    keyboard.press_and_release('backspace')
                continue
            guessedWords.append(guessWord)
            # Checks if an error was raised due to the win screen.
            try:
                incorrectLetters, lettersIncorrectPos, lettersCorrectPos = agent.GetInformation(guessWord, colorList)
            except ValueError:
                break
            # Checks if the goal word was found.
            if not None in lettersCorrectPos:
                gameOver = True
                continue
            agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)
            numberOfAttempts += 1
        keyboard.press_and_release('enter')
        location = agent.FindShareButton()
        agent.ClickShareButton(location)
        fileName = wordleConfig["recordfile"]
        agent.RecordWordleData(fileName, numberOfAttempts, guessedWords, removedWords, addedWord, allColors, wordleConfig)
        time.sleep(0.5)

if __name__ == "__main__":  
    main()
