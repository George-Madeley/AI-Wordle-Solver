from typing import TypeAlias
from CharacterInfo import CharacterInfo
from random import randint
from Node import Node

AlphabetInfo: TypeAlias = list[CharacterInfo]

class WordList:
    """
    Stores each word within a list.
    
    Holds each word in a list and contains methods
    to remove and/or keep letters based on given conditions.
    Used to calculate the best words to use given a scenario.
    
    Attributes:
        head: The head node.
        length: The length of the list.
    """

    def __init__(self, word: str = None) -> None:
        """
        Initialises the list.
        
        Args:
            word: The word of the first node (default None).
        """

        self.listOfWords = [Node(word)]
        self.__possibleWords = []
        
    def __str__(self) -> str:
        """
        Returns a string of all the words within the list.

        Returns:
            String of all the words concatenated.
        """

        stringList = ""
        for node in self.listOfWords:
            if node != None:
                stringList += str(node) + "\n"
        return stringList
    
    def GetRandomWord(self) -> str:
        """
        Returns a random word from the list of words.

        Returns:
            A random word.
        """

        index = randint(0, len(self.listOfWords) - 1 )
        node = self.listOfWords[index]
        return node.GetWord()

    def GetPossibleWords(self) -> list:
        """
        Returns a list of all the possible words.
        
        Returns:
            A list of all possible words.
        """

        self.__possibleWords = [word for word in self.listOfWords if word.IsPossibleWord()]
        return self.__possibleWords

    def GetPossibleWordsStr(self) -> str:
        """
        Returns a string of all the possible goal words.

        Returns:
            String of all the words concatenated.
        """

        stringList = ""
        possibleWords = self.GetPossibleWords()
        for node in possibleWords:
            if node != None:
                stringList += str(node) + "\n"
        return stringList

    def CalculateTotalCharacterOccurrences(self, characterOccurances: CharacterInfo) -> None:
        """
        Calculates the total number of times a given
        letter occurs within all possible words.
        
        Args:
            characterOccurances: The stats object for the given letter.
        """

        possibleWords = self.GetPossibleWords()
        for node in possibleWords:
            node.CalculateCharacterOccurrences(characterOccurances)
    
    def AddWord(self, newWord: str) -> None:
        """
        Adds a new node to the list of words.

        Args:
            newWord: The value of the new node.
        """

        node = Node(newWord)
        self.listOfWords.append(node)

    def RemoveNodesWithLetter(self, letter: str) -> None:
        """
        Sets the attribute isPossibleWord to False of any
        node in the list where the nodes word contains a
        given letter.

        Args:
            letter: The letter to be removed.
        """

        for node in self.listOfWords:
            if letter in node.GetWord():
                node.NotPossibleWord()

    def RemoveNodesWithLetterAtIndex(self, letter: str, index: int) -> None:
        """
        Sets the attribute isPossibleWord to False of any
        node in the list where the nodes word contains a
        given letter at a given index.

        Args:
            letter: The letter to be removed.
            index: The index of the letter to be removed.
        """

        for node in self.listOfWords:
            if letter == node.GetWord()[index]:
                node.NotPossibleWord()

    def KeepNodesWithLetter(self, letter: str) -> None:
        """
        Sets the attribute isPossibleWord to True of
        any node in the list where the nodes word contains
        a given letter.

        Args:
            letter: The letter to keep.
        """

        for node in self.listOfWords:
            if not letter in node.GetWord():
                node.NotPossibleWord()

    def KeepNodesWithLetterAtIndex(self, letter: str, index: int) -> None:
        """
        Sets the attribute isPossibleWord to True of any node
        in the list where the nodes word contains a given letter
        at a given index.

        Args:
            letter: The letter to keep.
            index: The index of the letter to keep.
        """

        for node in self.listOfWords:
            if not letter == node.GetWord()[index]:
                node.NotPossibleWord()

    def CalculateOccuranceScores(self, alphabetStats: AlphabetInfo) -> None:
        """
        Calculates the occurance scores of all words in the list.
        
        Args:
            alphabetStats: The array of each letters stats within the alphabet.
        """

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

        for node in self.listOfWords:
            node.ResetOccuranceScore()
            for letter in node.GetWord():
                try:
                    index = alphabet.index(letter)
                    score = alphabetStats[index].GetStatTotal()
                    node.IncreaseOccuranceScoreBy(score)
                except:
                    pass

    def CalculateKnowledgeScores(self, knowledgeBase: any) -> None:
        """
        Calculates the knowledge scores for each word.
        
        Args:
            knowledgeBase: The agents knowledge base.
        """

        for node in self.listOfWords:
            word = node.GetWord()
            node.ResetKnowledgeScore()
            for index, letter in enumerate(word):
                # Check if letter is in the correct position in goal word
                if letter in knowledgeBase.correctLetterPos:
                    # Letter is in correct position list
                    pass
                elif letter in knowledgeBase.lettersInGoal:
                    # Letter is in the word
                    if letter in knowledgeBase.incorrectLetterPos[index]:
                        # letter position is already known
                        pass
                    else:
                        # agent knows the letter is in the word but not the position
                        if knowledgeBase.correctLetterPos.count(None) > 1:
                            # agent knows there is more than one place left
                            node.IncreaseKnowledgeScoreBy(1)
                        elif knowledgeBase.correctLetterPos.count(None) == 1:
                            # there is one place left
                            pass
                        else:
                            # no places are left
                            pass
                elif letter in knowledgeBase.lettersNotInGoal:
                    # agent knows the letter is not in the goal
                    pass
                else:
                    # agent knows nothing about this letter
                    if len(knowledgeBase.lettersInGoal) >= 5:
                        # agent knows all the letters
                        pass
                    else:
                        # agent does not know all the letters in the goal
                        if knowledgeBase.correctLetterPos.count(None) > 1:
                            # agent knows there is more than one place left
                            node.IncreaseKnowledgeScoreBy(2)
                        elif knowledgeBase.correctLetterPos.count(None) == 1:
                            # there is one place left
                            node.IncreaseKnowledgeScoreBy(1)
                        else:
                            # no places are left
                            pass

    def GetBestKnowledgeWord(self) -> any:
        """
        Returns the word with the most amount of new knowledge.
        
        Returns:
            The word with the most amount of new knowledge.
        """
        bestScore = 0
        bestNode = None
        for node in self.listOfWords:
            if bestScore <= node.GetKnowledgeScore():
                bestScore = node.GetKnowledgeScore()
                bestNode = node
        return bestNode

    def GetBestOccuranceWord(self) -> str:
        """
        Returns the word with the largest number of letter occurances.

        Returns:
            The best word.
        """

        bestScore = 0
        bestWord = None
        for node in self.GetPossibleWords():
            if bestScore < node.GetOccuranceScore():
                bestScore = node.GetOccuranceScore()
                bestWord = node.GetWord()
        return bestWord

    def CalculateCommonLetters(self, singleLetters: dict, doubleLetters: dict, tripleLetters: dict, quadrupleLetters: dict, quintupleLetters: dict) -> any:
        """
        Calculates which letters are in every single word. Calculates
        if there are any double, triple, quadruple, or quintuple
        letters in all known words.
        
        Args:
            singleLetters: Dictionary of letters all assumed to be in every word once.
            doubleLetters: Dictionary of letters all assumed to be in every word twice.
            tripleLetters: Dictionary of letters all assumed to be in every word thrice
            quadrupleLetters: Dictionary of letters all assumed to be in every word four times.
            quintupleLetters: Dictionary of letters all assumed to be in every word five times.

        Returns:
            Dictionary of all letters that appear in every word once.
            Dictionary of all letters that appear in every word twice.
            Dictionary of all letters that appear in every word thrice
            Dictionary of all letters that appear in every word four times.
            Dictionary of all letters that appear in every word five times.
        """

        possibleWords = self.GetPossibleWords()
        for node in possibleWords:
            word = node.GetWord()
            for letter in singleLetters:
                if letter in word:
                    count = word.count(letter)
                    if count < 1:
                        # Letter does not appear in word
                        singleLetters[letter] = False
                        doubleLetters[letter] = False
                        tripleLetters[letter] = False
                        quadrupleLetters[letter] = False
                        quintupleLetters[letter] = False
                    elif count < 2:
                        # Letter appear in word once
                        doubleLetters[letter] = False
                        tripleLetters[letter] = False
                        quadrupleLetters[letter] = False
                        quintupleLetters[letter] = False
                    elif count < 3:
                        # letter appears in word twice
                        tripleLetters[letter] = False
                        quadrupleLetters[letter] = False
                        quintupleLetters[letter] = False
                    elif count < 4:
                        # letter appears in word thrice
                        quadrupleLetters[letter] = False
                        quintupleLetters[letter] = False
                    elif count < 5:
                        # letter appears in word four times
                        quintupleLetters[letter] = False
                    else:
                        # letter appears in word fivce or more times
                        pass
                else:
                    # Letter does not appear in word
                    singleLetters[letter] = False
                    doubleLetters[letter] = False
                    tripleLetters[letter] = False
                    quadrupleLetters[letter] = False
                    quintupleLetters[letter] = False
        return singleLetters, doubleLetters, tripleLetters, quadrupleLetters, quintupleLetters

    def ContainsWord(self, word: str) -> bool:
        """
        Checks if a given word is in the list.
        
        Args:
            word: The word to be found.
            
        Returns:
            True if the word is found.
        """

        for node in self.listOfWords:
            if node.GetWord() == word:
                return True
        return False