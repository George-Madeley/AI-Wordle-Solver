from typing import Any, TypeAlias
from LinkedList import LinkedList
from CharacterInfo import CharacterInfo

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

        self.possibleWords = self.ReadAllWords()
        self.alphabetOccurances = self.InitialiseAlphabetInfo()
        self.CalculateAlphabetOccurances()
        # self.alphabetStats.sort(key=lambda x: x.GetStatTotal(), reverse=True)

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
            firstWord = allWordsFile.readline()
            allWords = LinkedList(firstWord)
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

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        alphabetStatArray = []
        for character in alphabet:
            alphabetStatArray.append(CharacterInfo(character))
        return alphabetStatArray

    def CalculateAlphabetOccurances(self) -> None:
        """
        Calculates the number of occurances of each letter
        in all the known words.
        """

        for alphabetStat in self.alphabetOccurances:
            self.possibleWords.CalculateTotalCharacterOccurrences(alphabetStat)

    def GetPossibleWords(self) -> LinkedList:
        """
        Returns LinkedList of all possible words.

        Returns:
            The LinkedList of all possible words.
        """

        return self.possibleWords

    def GetRandomWord(self) -> str:
        """
        Returns a random word from all the possible words.

        Returns:
            A random word.
        """

        return self.possibleWords.GetRandomWord()

    def GetGuessWord(self) -> str:
        """
        Initialises and calculates the stats for all the
        letters in the alphabet and returns the best word
        to use given the current set of possible words

        Returns:
            The word with the largest score by letter
            occurances.
        """

        self.InitialiseAlphabetInfo()
        self.CalculateAlphabetOccurances()
        return self.GetBestWord()

    def GetBestWord(self) -> str:
        """
        Returns the best word to use given the current set
        of possible words

        Returns:
            The word with the largest score by letter
            occurances.
        """

        self.possibleWords.CalculateBestWord(self.alphabetOccurances)
        return self.possibleWords.GetBestWord()

    def AddNewWord(self, word: str) -> None:
        """
        Adds new word to linked list of possible words.

        Args:
            word: The word to add to all possible words.
        """

        self.possibleWords.AddWord(word)

    def UpdatePossibleWords(self, lettersNotInGoal: list[str], lettersInGoal: list[any], lettersInCorrectPos: list[any]) -> None:
        """
        Updates linked list of all possible words based
        on the results of the last entered word.

        Args:
            lettersNotInGoal: The array of the letters not in the goal word.
            lettersInGoal: The array of the letter in the goal word in their incorrect location.
            lettersInCorrectPos: The array of the letters in the goal word in their correct location.
        """

        for letter in lettersNotInGoal:
            self.possibleWords.RemoveNodesWithLetter(letter)
        for index, letter in enumerate(lettersInGoal):
            if letter != None:
                self.possibleWords.RemoveNodesWithLetterAtIndex(letter, index)
        for index, letter in enumerate(lettersInCorrectPos):
            if letter != None:
                self.possibleWords.KeepNodesWithLetterAtIndex(letter, index)
