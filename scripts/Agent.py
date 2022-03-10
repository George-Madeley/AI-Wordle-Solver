from datetime import date
import math
from typing import TypeAlias

from KnowledgeBase import KnowledgeBase
from CharacterInfo import CharacterInfo
from WordList import WordList

from PIL import Image
import pyautogui
import pyperclip

AlphabetInfo: TypeAlias = list[CharacterInfo]

class Agent:
    """
    The AI used to solve Wordle.
    
    Attributes:
        possibleWords: A LinkedList of all words that the goal word could be.
        alphabetOccurances: An array of CharacterInfo objects for each letter in the alphabet.
    """
    
    def __init__(self, config: dict) -> None:
        """
        Initialises the Agent class instance.
        """

        self.__config = config
        self.__alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.__knowledgeBase = KnowledgeBase()
        self.__knowledgeBase.wordList = self.ReadAllWords()
        self.__alphabetOccurances = self.InitialiseAlphabetInfo()
        self.CalculateAlphabetOccurances()

    def ReadAllWords(self) -> any:
        """
        Reads all the words from the ListOfWords.txt
        file and stores them as a LinkedList. Returns
        this LinkedList.

        Returns:
            A LinkedList of all known words.
        """

        allWords = WordList()
        with open("assets/ListOfWords.txt", "r") as allWordsFile:
            for line in allWordsFile:
                word = line.strip('\n').lower()
                if len(word) == 5:
                    allWords.AddWord(word)
        allWords.UpdatePossibleWords()
        return allWords

    def InitialiseAlphabetInfo(self) -> AlphabetInfo:
        """
        Initialises all the stats associated with each
        letter of the alphabet an returns it.

        Returns:
            An array of character stats for each letter
            in the alphabet.
        """

        alphabetStatArray = []
        for character in self.__alphabet:
            alphabetStatArray.append(CharacterInfo(character))
        return alphabetStatArray

    def CalculateAlphabetOccurances(self) -> None:
        """
        Calculates the number of occurances of each letter
        in all the known words.
        """

        for characterOccurances in self.__alphabetOccurances:
            self.__knowledgeBase.wordList.CalculateTotalCharacterOccurrences(characterOccurances)

    def GetRandomWord(self) -> str:
        """
        Returns a random word from all the possible words.

        Returns:
            A random word.
        """

        return self.__knowledgeBase.wordList.GetRandomWord()

    def GetGuessWord(self, attemptNumber: int) -> str:
        """
        Initialises and calculates the stats for all the
        letters in the alphabet and returns the best word
        to use given the current set of possible words

        Args:
            attemptNumber: The number of attempts the
            agent has had to solve the puzzle.

        Returns:
            The word with the largest score by letter
            occurances.
        """

        if attemptNumber == 0:
            return self.GetBestOccuranceWord()
        else:
            bestNode = self.GetBestKnowledgeWord()
            # bestNode.PrintNodeInfo()
            if bestNode.GetKnowledgeScore() == 0:
                return self.GetBestOccuranceWord()
            else:
                return bestNode.GetWord()

    def GetWordAtIndex(self, index: int) -> str:
        """
        Gets a word from the list of all words at the index.
        
        Args:
            index: The index to get the word at.
            
        Returns:
            The word.
        """

        return self.__knowledgeBase.wordList.listOfWords[index].GetWord()

    def GetBestOccuranceWord(self) -> str:
        """
        Returns the best word to use given the current set
        of possible words based on the most common letters
        it contains.

        Returns:
            The word with the largest score by letter
            occurances.
        """

        self.__knowledgeBase.wordList.CalculateOccuranceScores(self.__alphabetOccurances)
        return self.__knowledgeBase.wordList.GetBestOccuranceWord()

    def GetBestKnowledgeWord(self) -> any:
        """
        Returns the best word to use given the current set of
        possible words based on the amount of knowledge that
        word will provide.
        
        Returns:
            The word with the largest amount of knowledge.
        """

        self.__knowledgeBase.wordList.CalculateKnowledgeScores(self.__knowledgeBase)
        return self.__knowledgeBase.wordList.GetBestKnowledgeWord()

    def AddNewWord(self, word: str) -> None:
        """
        Adds new word to linked list of possible words.

        Args:
            word: The word to add to all possible words.
        """

        if not self.__knowledgeBase.wordList.ContainsWord(word):
            with open('assets/ListOfWords.txt', 'a') as wordFile:
                wordFile.write(f"{word}\n")

    def RemoveWord(self, removeWord: str) -> None:
        """
        Removes a given word from the list of words.

        Args:
            removeWord: The word to remove.
        """
        if self.__knowledgeBase.wordList.ContainsWord(removeWord):
            self.__knowledgeBase.wordList.RemoveWord(removeWord)
            with open('assets/ListOfWords.txt', 'r') as wordFile:
                words = wordFile.readlines()
            with open('assets/ListOfWords.txt', 'w') as wordFile:
                for word in words:
                    if word.strip('\n') == removeWord:
                        continue
                    else:
                        wordFile.write(word)

    def UpdateKnowledgeBase(self, lettersNotInGoal: list[str], lettersInGoal: list[any], lettersInCorrectPos: list[any]) -> None:
        """
        Updates the information stored within the knowledge base object.

        Args:
            lettersNotInGoal: The array of the letters not in the goal word.
            lettersInGoal: The array of the letter in the goal word in their incorrect location.
            lettersInCorrectPos: The array of the letters in the goal word in their correct location.
        """
        self.__knowledgeBase.UpdateBasicKnowledge(lettersNotInGoal, lettersInGoal, lettersInCorrectPos)
        self.__knowledgeBase.UpdatePossibleWords()
        self.__alphabetOccurances = self.InitialiseAlphabetInfo()
        self.CalculateAlphabetOccurances()
        # print(self.__knowledgeBase.wordList.GetPossibleWordsStr())
        self.__knowledgeBase.UpdateLettersNotInGoal()
        self.__knowledgeBase.UpdateIncorrectLetterPos(self.__alphabetOccurances)
        self.__knowledgeBase.UpdateLettersInGoal()
        pass























    def GetScreenshot(self) -> str:
        """
        Takes a screenshot and returns the file path to the screenshot.
        
        Returns:
            The string of the screenshot filepath.
        """
        pyautogui.screenshot('images\shot.png')
        return 'images\shot.png'

    def GetInformation(self, guessedWord: str, colorList: list):
        guessedWord = guessedWord.rstrip("\n")
        incorrectLetters = []
        lettersIncorrectPos = [None, None, None, None, None]
        lettersCorrectPos = [None, None, None, None, None]
        for index, (letter, color) in enumerate(zip(guessedWord, colorList)):
            if color == "grey":
                incorrectLetters.append(letter)
            elif color == "yellow":
                lettersIncorrectPos[index] = letter
            elif color == "green":
                lettersCorrectPos[index] = letter
            else:
                raise ValueError(f"Color, {color} is not one of the predefined colors")
        return incorrectLetters, lettersIncorrectPos, lettersCorrectPos

    def ReadImage(self, attemptNumber: int, filePath: str) -> list:
        """
        Opens a screenshot of the image and reads the information from it.

        Args:
            attemptNumber: The attempt number.
            filePath: The file path to the screenshot.
        """

        with Image.open(filePath) as screenshot:
            # Wordle box (on my PC) is 500x600 at 1671, 744
            # left, upper, right, lower bounds
            upperX = int(self.__config["pos"]["x"])
            upperY = int(self.__config["pos"]["y"])
            lowerX = upperX + int(self.__config["size"]["x"])
            lowerY = upperY + int(self.__config["size"]["y"])
            cropBoxSize = (upperX, upperY, lowerX, lowerY)
            wordleImage = screenshot.crop(box=cropBoxSize)
            # wordleImage.show()

            dividedImage = self.DivideImage(wordleImage)
            colorList = [self.GetColor(colorImage) for colorImage in dividedImage[attemptNumber]]
            return colorList
            
    def DivideImage(self, wordleImage: Image) -> list:
        """
        Divides up the provided image of Wordle into 30 smaller images of each character.
        
        Args:
            wordleImage: The image of Wordle.
            
        Returns:
            2D-list of Images.
        """
        dividedImage = []
        boxX = math.floor(int(self.__config["size"]["x"]) / 5) + int(self.__config["gap"]["x"])
        boxY = math.floor(int(self.__config["size"]["y"]) / 6) + int(self.__config["gap"]["x"])
        colorBoxSize = int(self.__config["box"]["x"])
        perimeterX = int(self.__config["perimeter"]["x"])
        perimeterY = int(self.__config["perimeter"]["y"])
        for y in range(6):
            dividedRow = []
            for x in range(5):
                    # left, upper, right, lower bounds
                tempBoxSize = (x * boxX + perimeterX, y * boxY + perimeterY, (x * boxX) + colorBoxSize, (y * boxX) + colorBoxSize)
                tempImage = wordleImage.crop(box=tempBoxSize)
                # tempImage.show()
                dividedRow.append(tempImage)
            dividedImage.append(dividedRow)
        return dividedImage

    def GetColor(self, image: Image) -> str:
        """
        Gets the background color of the image.
        """
        # image.show()
        try:
            upperWeight = 160
            colors = image.getcolors()
            colors = [color for color in colors if (color[-1][0] < upperWeight or color[-1][1] < upperWeight or color[-1][2] < upperWeight)]
            finalColor = [0, 0, 0]
            for color in colors:
                finalColor[0] += color[-1][0]
                finalColor[1] += color[-1][1]
                finalColor[2] += color[-1][2]
            finalColor[0] /= len(colors)
            finalColor[1] /= len(colors)
            finalColor[2] /= len(colors)
            
            # print(finalColor)

            margin = int(self.__config["margin"])
            
            colorConfig = self.__config["colors"]
            colorDict = {colorName: [int(color) for color in colorConfig[colorName].values()] for colorName in colorConfig.keys()}
            # colorDict = {"grey": (58, 58, 60), "yellow": (181, 159, 59), "green": (83, 141, 78), "black": (18, 18, 19)}
            for color, colorCode in colorDict.items():
                if ((colorCode[0] - margin) < finalColor[0] and (colorCode[0] + margin) > finalColor[0] and
                    (colorCode[1] - margin) < finalColor[1] and (colorCode[1] + margin) > finalColor[1] and
                    (colorCode[2] - margin) < finalColor[2] and (colorCode[2] + margin) > finalColor[2]):
                    return color
            return None
        except ZeroDivisionError:
            return "green"

    def RecordWordleData(self, fileName: str, numberOfAttempts: int, guessedWords: list, removedWords: list, addedWord: str, allColors: list, wordleConfig: dict) -> None:
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
        if bool(wordleConfig["makeemojis"]):
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

    def ClickShareButton(self, location: tuple) -> None:
        """
        Clicks the share button.
        """

        x, y = location
        pyautogui.click(x, y)

    def FindShareButton(self) -> tuple:
        """
        Finds the share button one the screen then returns the location of the share button.
        
        Returns:
            The location of the share button as a tuple.
        """

        return (int(self.__config["share"]["x"]), int(self.__config["share"]["y"]))
