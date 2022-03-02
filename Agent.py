from typing import Any, TypeAlias
from KnowledgeBase import KnowledgeBase
from CharacterInfo import CharacterInfo
from Word import Word
from WordList import WordList

AlphabetInfo: TypeAlias = list[CharacterInfo]

class Agent:
    """
    The AI used to solve Wordle.
    
    Attributes:
        possibleWords: A LinkedList of all words that the goal word could be.
        alphabetOccurances: An array of CharacterInfo objects for each letter in the alphabet.
    """
    
    def __init__(self) -> None:
        """
        Initialises the Agent class instance.
        """

        self.__alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.__knowledgeBase = KnowledgeBase()
        self.__knowledgeBase.wordList = self.ReadAllWords()
        self.__alphabetOccurances = self.InitialiseAlphabetInfo()
        self.CalculateAlphabetOccurances()

    def ReadAllWords(self) -> Any:
        """
        Reads all the words from the ListOfWords.txt
        file and stores them as a LinkedList. Returns
        this LinkedList.

        Returns:
            A LinkedList of all known words.
        """

        try:
            allWordsFile = open("ListOfWords.txt", "r")
            firstWord = allWordsFile.readline().replace('\n', '').lower()
            allWords = WordList(firstWord)
            for line in allWordsFile:
                word = line.replace('\n', '').lower()
                if len(word) != 5:
                    print("ERROR: " + word + " has a length of more than five")
                    raise ValueError
                allWords.AddWord(word)
            return allWords
        except ValueError:
            print("ERROR")

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

    def GetBestKnowledgeWord(self) -> Word:
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

        self.__knowledgeBase.wordList.AddWord(word)

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
