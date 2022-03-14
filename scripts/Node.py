class Node:
    """
    Stores a given word.

    Holds the information surrounding a given word and
    points to the next node. Contains methods to check
    and calculate given pieces of information.
    
    Attributes:
        word: The word it stores.
        score: The words score by letter occurances.
        nextNode: Pointer to the next Node.
    """

    def __init__(self, word: str) -> None:
        """
        Initialise a Node.
        
        Args:
            word: The five letter word to be stored.
        """
        
        self.__word = word
        self.__occuranceScore = 0
        self.__knowledgeScore = 0
        self.__isPossibleWord = True

    def __str__(self) -> str:
        """
        Returns the stored word.

        Returns:
            The stored word.
        """

        return self.__word

    def PrintNodeInfo(self) -> None:
        """
        Prints the word, occurance score, knowledge score,
        and if the word is a possible goal word
        """

        print(self.__word + ", O: " + str(self.__occuranceScore) + ", K: " + str(self.__knowledgeScore) + ", " + str(self.__isPossibleWord))

    def GetWord(self) -> str:
        """
        Returns the stored word.

        Returns:
            The stored word.
        """

        return self.__word

    def IsWordValid(self) -> bool:
        """
        Returns True if the stored word is a valid word.

        Returns:
            True if the stored word is a valid word.
        """

        return len(self.__word) == 5

    def GetLetterIndex(self, letter: str) -> int:
        """
        Gets the index of the given letter in word.

        Returns the index of where the provided letter is
        within the stored word. Returns -1 if letter is not
        in word.
        
        Args:
            letter: The letter to be found in the word.

        Returns:
            The index of provided letter. Returns -1 if
            letter is not in word.
        """

        letterIndex = str(self.__word).find(letter)
        return letterIndex

    def ResetOccuranceScore(self) -> None:
        """
        Sets the nodes score to 0.
        """

        self.__occuranceScore = 0

    def GetOccuranceScore(self) -> int:
        """
        Returns the nodes score.

        Returns:
            The nodes score attribute.
        """

        return self.__occuranceScore

    def IncreaseOccuranceScoreBy(self, amount: int) -> None:
        """
        Increases the score by the provided amount.
        
        Args:
            amount: The amount to increase the score by.
        """

        self.__occuranceScore += amount

    def ResetKnowledgeScore(self) -> None:
        """
        Sets the nodes score to 0.
        """

        self.__knowledgeScore = 0

    def GetKnowledgeScore(self) -> int:
        """
        Returns the nodes score.

        Returns:
            The nodes score attribute.
        """

        return self.__knowledgeScore

    def IncreaseKnowledgeScoreBy(self, amount: int) -> None:
        """
        Increases the score by the provided amount.
        
        Args:
            amount: The amount to increase the score by.
        """

        self.__knowledgeScore += amount

    def IsPossibleWord(self) -> bool:
        """
        Checks if word is a possible goal word.
        
        Returns:
            True if word is a possiible goal word.
        """
        
        return self.__isPossibleWord

    def NotPossibleWord(self) -> None:
        """
        Sets word to not a possible goal word.
        """

        self.__isPossibleWord = False