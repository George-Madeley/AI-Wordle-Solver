import time
from Agent import Agent
import keyboard

def main():
    agent = Agent()
    # keyboard.wait('esc')
    gameOver = False
    numberOfAttempts = 6

    # numberOfAttempts = int(input("How many previous Attempts:\t"))
    # if numberOfAttempts > 0:
    #     filepath = agent.GetScreenshot()
    #     for attemptNumber in range(numberOfAttempts):
    #         guessWord = str(input(f"What was the {attemptNumber} word:\t"))
    #         incorrectLetters, lettersIncorrectPos, lettersCorrectPos = agent.GetInformation(guessWord, attemptNumber, filepath)
    #         agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)

    # keyboard.wait('esc')

    # while not gameOver and numberOfAttempts < 6:
    #     guessWord = agent.GetGuessWord(numberOfAttempts)
    #     keyboard.write(guessWord)
    #     keyboard.wait('enter')
    #     time.sleep(5)
    #     filepath = agent.GetScreenshot()
    #     incorrectLetters, lettersIncorrectPos, lettersCorrectPos = agent.GetInformation(guessWord, numberOfAttempts, filepath)
    #     if not None in lettersCorrectPos:
    #         gameOver = True
    #         continue
    #     agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)
    #     numberOfAttempts += 1

    if numberOfAttempts >= 6:
        isValid = str(input("Do you want to add a word? (Y/N)\t")).lower() != "y"
        while not isValid:
            newWord = str(input("Enter new Word:\t")).lower()
            if len(newWord) == 5:
                isValid = True
                agent.AddNewWord(newWord)
                continue
            print("The word you have entered is invalid. Please try again.")


if __name__ == "__main__":  
    main()
