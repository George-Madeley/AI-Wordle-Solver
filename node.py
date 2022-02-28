from CharacterInfo import CharacterInfo

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
        
        self.word = word
        self.score = 0
        self.nextNode = None

    def __str__(self) -> str:
        """
        Returns the stored word.

        Returns:
            The stored word.
        """

        return self.word

    def SetWord(self, word: str) -> None:
        """
        Sets the stored word to the given new word.
        
        Args:
            word: The new five letter word.
        """

        self.word = word

    def GetWord(self) -> str:
        """
        Returns the stored word.

        Returns:
            The stored word.
        """

        return self.word

    def SetNextNode(self, node: 'Node') -> None:
        """
        Sets the next node to the given node.
        
        Args:
            node: The next node in the line.
        """

        self.nextNode = node

    def GetNextNode(self) -> 'Node':
        """
        Returns the next node.

        Returns:
            The next node.
        """

        return self.nextNode

    def IsWordValid(self) -> bool:
        """
        Returns True if the stored word is a valid word.

        Returns:
            True if the stored word is a valid word.
        """

        return len(self.word) == 5

    def HasLetter(self, letter: str) -> bool:
        """
        Returns True if the word contains a given letter.
        
        Args:
            letter: The letter to be found in the word.

        Retuns:
            True if the word contains a given letter.
        """

        letterIndex = self.word.find(letter)
        return letterIndex >= 0

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

        letterIndex = self.word.find(letter)
        return letterIndex
        # for index, letter in enumerate(self.word):
        #     if goalLetter == letter:
        #         return index
        # return -1

    def CalculateCharacterOccurrences(self, characterStats: CharacterInfo) -> None:
        """
        Calculates the number of occurances of a given character.

        Calculates the number of time the provided letter
        occurs within the stored word. Adds this to the provided
        character stats object.
        
        Args:
            characterStats: The letters stats object.
        """

        for index, letter in enumerate(self.word):
            if letter == characterStats.GetCharacter():
                characterStats.IncrementStatAtIndex(index)

    def ResetScore(self) -> None:
        """
        Sets the nodes score to 0.
        """

        self.score = 0

    def GetScore(self) -> int:
        """
        Returns the nodes score.

        Returns:
            The nodes score attribute.
        """

        return self.score

    def IncreaseScoreBy(self, amount: int) -> None:
        """
        Increases the score by the provided amount.
        
        Args:
            amount: The amount to increase the score by.
        """

        self.score += amount