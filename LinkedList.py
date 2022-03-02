from typing import Any, TypeAlias
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
        Returns the head node of the linked list.
        
        Returns:
            Head Node.
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

    def CalculateTotalCharacterOccurrences(self, characterOccurances: CharacterInfo) -> None:
        """
        Calculates the total number of times a given
        letter occurs within all known words.
        
        Args:
            characterOccurances: The stats object for the given letter.
        """
        currentNode = self.head
        while currentNode != None:
            currentNode.CalculateCharacterOccurrences(characterOccurances)
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

        while self.head != None and self.head.GetWord()[index] == letter:
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

    def KeepNodesWithLetterAtIndex(self, letter: str, index: int) -> None:
        """
        Keeps any node in the list where the nodes word
        contains a given letter at a given index.

        Args:
            letter: The letter to keep.
            index: The index of the letter to keep.
        """

        while self.head != None and not self.head.GetWord()[index] == letter:
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

    def CalculateOccuranceScores(self, alphabetStats: AlphabetInfo) -> None:
        """
        Calculates the occurance scores of all words in the list.
        
        Args:
            alphabetStats: The array of each letters stats within the alphabet.
        """

        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        currentNode = self.head
        while currentNode != None:
            word = currentNode.GetWord()
            currentNode.ResetOccuranceScore()
            for letter in word:
                try:
                    index = alphabet.index(letter)
                    score = alphabetStats[index].GetStatTotal()
                    currentNode.IncreaseOccuranceScoreBy(score)
                except:
                    pass
            currentNode = currentNode.GetNextNode()

    def CalculateKnowledgeScores(self, knowledgeBase: any) -> None:
        """
        Calculates the knowledge scores for each word.
        
        Args:
            knowledgeBase: The agents knowledge base.
        """

        currentNode = self.head
        while currentNode != None:
            word = currentNode.GetWord()
            currentNode.ResetKnowledgeScore()
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
                            currentNode.IncreaseKnowledgeScoreBy(1)
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
                            currentNode.IncreaseKnowledgeScoreBy(2)
                        elif knowledgeBase.correctLetterPos.count(None) == 1:
                            # there is one place left
                            currentNode.IncreaseKnowledgeScoreBy(1)
                        else:
                            # no places are left
                            pass
            currentNode = currentNode.GetNextNode()

    def GetBestKnowledgeWord(self) -> str:
        """
        Returns the word with the most amount of new knowledge.
        
        Returns:
            The word with the most amount of new knowledge.
        """
        bestScore = 0
        bestWord = None
        currentNode = self.head
        while currentNode != None:
            if bestScore <= currentNode.GetKnowledgeScore():
                bestScore = currentNode.GetKnowledgeScore()
                bestWord = currentNode.GetWord()
            currentNode = currentNode.GetNextNode()
        return bestWord

    def GetBestOccuranceWord(self) -> str:
        """
        Returns the word with the largest number of letter occurances.

        Returns:
            The best word.
        """

        bestScore = 0
        bestWord = None
        currentNode = self.head
        while currentNode != None:
            if bestScore < currentNode.GetOccuranceScore():
                bestScore = currentNode.GetOccuranceScore()
                bestWord = currentNode.GetWord()
            currentNode = currentNode.GetNextNode()
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

        currenctNode = self.GetHead()
        while currenctNode != None:
            word = currenctNode.GetWord()
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
            currenctNode = currenctNode.GetNextNode()
        return singleLetters, doubleLetters, tripleLetters, quadrupleLetters, quintupleLetters




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

