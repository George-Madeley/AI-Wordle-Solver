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
        while self.head.IsLetterInWord(letter):
            # Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        while (currentNode != None and currentNode.GetNextNode() != None):
            if currentNode.GetNextNode().IsLetterInWord(letter):
                # Remove Node
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
                self.length -= 1
            currentNode = currentNode.GetNextNode()

    def RemoveNodesWithLetterAtIndex(self, letter, index):
        """
        Removes any node in the list where the nodes word contains a given letter at a given index
        """
        while self.head.GetLetterIndex(letter) == index:
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
            currentNode = currentNode.GetNextNode()

    def KeepNodesWithLetter(self, letter):
        """
        Keeps any node in the list where the nodes word contains a given letter
        """
        while not self.head.IsLetterInWord(letter):
            # Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        while (currentNode != None and currentNode.GetNextNode() != None):
            if not currentNode.GetNextNode().IsLetterInWord(letter):
                # Remove Node
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode()) 
                self.length -= 1
            currentNode = currentNode.GetNextNode()

    def KeepNodesWithLetterAtIndex(self, letter:string, index:int):
        """
        Keeps any node in the list where the nodes word contains a given letter at a given index
        """
        while not self.head.GetLetterIndex(letter) == index:
            # Remove Node
            self.head = self.head.GetNextNode()
            self.length -= 1
        currentNode = self.head
        while (currentNode != None and currentNode.GetNextNode() != None):
            if not currentNode.GetNextNode().GetLetterIndex(letter) == index:
                # Remove Node
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
                self.length -= 1
            currentNode = currentNode.GetNextNode()
