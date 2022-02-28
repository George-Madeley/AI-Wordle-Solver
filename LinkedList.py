from typing import TypeAlias
from CharacterInfo import CharacterInfo
from Node import Node
from random import randint

AlphabetInfo: TypeAlias = list[CharacterInfo]

class LinkedList:
    """
    Stores each word within a LinkedList.
    
    Holds each word in a LinkedList and contains methods
    to remove and/or keep letters based on given conditions.
    Used to calculate the best words to use given a scenario.
    
    Attributes:
        head: The head node.
        length: The length of the list.
    """

    def __init__(self, word: str = None) -> None:
        """
        Initialises the LinkedList.
        
        Args:
            word: The word of the first node (default None).
        """

        self.head = Node(word)
        self.length = 1
        
    def __str__(self) -> str:
        """
        Returns a string of all the words within the Linked List.

        Returns:
            String of all the words concatenated.
        """

        stringList = ""
        currentNode = self.GetHead()
        while currentNode:
            if currentNode.GetWord() != None:
                stringList += str(currentNode.GetWord()) + "\n"
            currentNode = currentNode.GetNextNode()
        return stringList
    
    def GetHead(self) -> Node:
        """
        Returns the head node.

        Returns:
            The head node.
        """

        return self.head

    def GetRandomWord(self) -> str:
        """
        Returns a random word from the LinkedList.

        Returns:
            A random word.
        """

        index = randint(0, self.length - 1)
        currentNode = self.head
        while currentNode.GetNextNode() != None and index != 0:
            currentNode = currentNode.GetNextNode()
            index -= 1
        return currentNode.GetWord()

    def CalculateTotalCharacterOccurrences(self, characterStats: CharacterInfo) -> None:
        """
        Calculates the total number of times a given
        letter occurs within all known words.
        
        Args:
            characterStats: The stats object for the given letter.
        """
        currentNode = self.head
        while currentNode != None:
            currentNode.CalculateCharacterOccurrences(characterStats)
            currentNode = currentNode.GetNextNode()
    
    def AddWord(self, newWord: str) -> None:
        """
        Adds a new node to the head of the LinkedList.
        
        Args:
            newWord: The value of the new node.
        """

        newNode = Node(newWord)
        newNode.SetNextNode(self.head)
        self.head = newNode
        self.length += 1

    def RemoveNodesWithLetter(self, letter: str) -> None:
        """
        Removes any node in the list where the nodes
        word contains a given letter.

        Args:
            letter: The letter to be removed.
        """

        while self.head != None and self.head.HasLetter(letter):
            # Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        while (currentNode != None and currentNode.GetNextNode() != None):
            if currentNode.GetNextNode().HasLetter(letter):
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
                self.length -= 1
            else:
                currentNode = currentNode.GetNextNode()

    def RemoveNodesWithLetterAtIndex(self, letter: str, index: int) -> None:
        """
        Removes any node in the list where the nodes
        word contains a given letter at a given index.

        Args:
            letter: The letter to be removed.
            index: The index of the letter to be removed.
        """

        while self.head != None and self.head.GetLetterIndex(letter) == index:
            #Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        if currentNode == None:
            return
        while (currentNode.GetNextNode() != None):
            if currentNode.GetNextNode().GetLetterIndex(letter) == index:
                #Remove Node
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
                self.length -= 1
            else:
                currentNode = currentNode.GetNextNode()

    def KeepNodesWithLetter(self, letter: str) -> None:
        """
        Keeps any node in the list where the nodes word
        contains a given letter.

        Args:
            letter: The letter to keep.
        """

        while self.head != None and not self.head.HasLetter(letter):
            # Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        while (currentNode != None and currentNode.GetNextNode() != None):
            if not currentNode.GetNextNode().HasLetter(letter):
                # Remove Node
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode()) 
                self.length -= 1
            else:
                currentNode = currentNode.GetNextNode()

    def KeepNodesWithLetterAtIndex(self, letter: str, index:int) -> None:
        """
        Keeps any node in the list where the nodes word
        contains a given letter at a given index.

        Args:
            letter: The letter to keep.
            index: The index of the letter to keep.
        """

        while self.head != None and not self.head.GetLetterIndex(letter) == index:
            # Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        while (currentNode != None and currentNode.GetNextNode() != None):
            if not currentNode.GetNextNode().GetLetterIndex(letter) == index:
                # Remove Node
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
                self.length -= 1
            else:
                currentNode = currentNode.GetNextNode()

    def CalculateBestWord(self, alphabetStats: AlphabetInfo) -> None:
        """
        Calculates the best word by occurances of all
        words in the list.
        
        Args:
            alphabetStats: The array of each letters stats within the alphabet.
        """

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        currentNode = self.head
        while currentNode != None:
            word = currentNode.GetWord()
            currentNode.ResetScore()
            for letter in word:
                try:
                    index = alphabet.index(letter)
                    score = alphabetStats[index].GetStatTotal()
                    currentNode.IncreaseScoreBy(score)
                except:
                    pass
            currentNode = currentNode.GetNextNode()

    def GetBestWord(self) -> str:
        """
        Returns the word with the largest number of letter occurances.

        Returns:
            The best word.
        """

        bestScore = 0
        bestWord = None
        currentNode = self.head
        while currentNode != None:
            if bestScore < currentNode.GetScore():
                bestScore = currentNode.GetScore()
                bestWord = currentNode.GetWord()
            currentNode = currentNode.GetNextNode()
        return bestWord
