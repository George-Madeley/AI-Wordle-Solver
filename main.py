import time
from Agent import Agent
import keyboard

def main():
    agent = Agent()
    keyboard.wait('esc')
    gameOver = False
    numberOfAttempts = 0

    numberOfAttempts = int(input("How many previous Attempts:\t"))
    if numberOfAttempts > 0:
        filepath = agent.GetScreenshot()
        for attemptNumber in range(numberOfAttempts):
            guessWord = str(input(f"What was the {attemptNumber} word:\t"))
            incorrectLetters, lettersIncorrectPos, lettersCorrectPos = agent.GetInformation(guessWord, attemptNumber, filepath)
            agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)

    keyboard.wait('esc')

    while not gameOver and numberOfAttempts < 6:
        guessWord = agent.GetGuessWord(numberOfAttempts)
        keyboard.write(guessWord)
        keyboard.wait('enter')
        time.sleep(5)
        filepath = agent.GetScreenshot()
        incorrectLetters, lettersIncorrectPos, lettersCorrectPos = agent.GetInformation(guessWord, numberOfAttempts, filepath)
        if not None in lettersCorrectPos:
            gameOver = True
            continue
        agent.UpdateKnowledgeBase(incorrectLetters, lettersIncorrectPos, lettersCorrectPos)
        time.sleep(1)


if __name__ == "__main__":  
    main()
