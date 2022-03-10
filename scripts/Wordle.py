import time
from Agent import Agent
import keyboard

def RemoveDuplicateWords():
    """
    Removes and duplicate words from the list of words text file.
    """

    allWords = []
    with open("ListOfWords.txt", "r") as allWordsFile:
        for line in allWordsFile:
            word = line.strip('\n').lower()
            if len(word) == 5 and word not in allWords:
                allWords.append(word)
            elif len(word) > 5 and word not in allWords:
                word = word[:5]
                allWords.append(word)
    allWords.sort()
    with open('ListOfWords.txt', 'w') as wordFile:
        for word in allWords:
            wordFile.write(f"{word}\n")
    

def main():
    agent = Agent()
    gameOver = False
    numberOfAttempts = 6
    guessedWords = []
    removedWords = []
    addedWord = None

    # Allows you to run the AI midway trhough a game.
    numberOfAttempts = int(input("How many previous Attempts:\t"))
    if numberOfAttempts > 0:
        filePath = agent.GetScreenshot()
        for attemptNumber in range(numberOfAttempts):
            guessWord = str(input(f"What was the {attemptNumber + 1} word:\t"))
            colorList = agent.ReadImage(attemptNumber, filePath)
            incorrectLetters, lettersIncorrectPos, lettersCorrectPos = agent.GetInformation(guessWord, colorList)
            agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)

    print("Press ESC to continue...")
    keyboard.wait('esc')

    # Plays the Game
    while not gameOver and numberOfAttempts < 6:
        guessWord = agent.GetGuessWord(numberOfAttempts)
        keyboard.write(guessWord)
        print("Press enter to continue...")
        keyboard.wait('enter')
        time.sleep(5)
        filePath = agent.GetScreenshot()
        colorList = agent.ReadImage(numberOfAttempts, filePath)
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
            gameOver = str(input("Is the game over? (Y/N)\t")).lower() == "y"
            if gameOver:
                continue
            else:
                raise ValueError("The AI could not read the colors of the previously entered word!")
        # Checks if the goal word was found.
        if not None in lettersCorrectPos:
            gameOver = True
            continue
        agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)
        numberOfAttempts += 1
    # Checks if the AI lost due to not knowing the Goal Word.
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

    location = agent.FindShareButton()
    agent.ClickShareButton(location)
    agent.RecordWordleData(numberOfAttempts, guessedWords, removedWords, addedWord)


if __name__ == "__main__":  
    main()
