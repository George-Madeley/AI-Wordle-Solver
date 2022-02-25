import math
import string
from node import Node
from random import randint

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
        self.length = 1
    
    def GetHead(self):
        return self.head

    def GetRandomWord(self):
        index = randint(0, self.length - 1)
        currentNode = self.head
        while currentNode.GetNextNode() != None and index != 0:
            currentNode = currentNode.GetNextNode()
            index -= 1
        return currentNode.GetWord()

    def CalculateTotalCharacterOccurrences(self, characterStats):
        currentNode = self.head
        while currentNode != None:
            currentNode.CalculateCharacterOccurrences(characterStats)
            currentNode = currentNode.GetNextNode()
    
    def AddWord(self, newValue):
        newNode = Node(newValue)
        newNode.SetNextNode(self.head)
        self.head = newNode
        self.length += 1
        
    def __str__(self):
        stringList = ""
        currentNode = self.GetHead()
        while currentNode:
            if currentNode.GetWord() != None:
                stringList += str(currentNode.GetWord()) + "\n"
            currentNode = currentNode.GetNextNode()
        return stringList

    def RemoveNodesWithLetter(self, letter):
        """
        Removes any node in the list where the nodes word contains a given letter
        """
        while self.head != None and self.head.hasLetter(letter):
            # Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        while (currentNode != None and currentNode.GetNextNode() != None):
            if currentNode.GetNextNode().hasLetter(letter):
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
                self.length -= 1
            else:
                currentNode = currentNode.GetNextNode()

    def RemoveNodesWithLetterAtIndex(self, letter, index):
        """
        Removes any node in the list where the nodes word contains a given letter at a given index
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

    def KeepNodesWithLetter(self, letter):
        """
        Keeps any node in the list where the nodes word contains a given letter
        """
        while self.head != None and not self.head.hasLetter(letter):
            # Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        while (currentNode != None and currentNode.GetNextNode() != None):
            if not currentNode.GetNextNode().hasLetter(letter):
                # Remove Node
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode()) 
                self.length -= 1
            else:
                currentNode = currentNode.GetNextNode()

    def KeepNodesWithLetterAtIndex(self, letter:string, index:int):
        """
        Keeps any node in the list where the nodes word contains a given letter at a given index
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

    def CalculateBestWord(self, alphabetStats):
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

    def GetBestWord(self):
        bestScore = 0
        bestWord = None
        currentNode = self.head
        while currentNode != None:
            if bestScore < currentNode.GetScore():
                bestScore = currentNode.GetScore()
                bestWord = currentNode.GetWord()
            currentNode = currentNode.GetNextNode()
        return bestWord
