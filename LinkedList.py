from node import Node

class LinkedList:
    def __init__(self, value=None):
        self.head = Node(value)
    
    def GetHead(self):
        return self.head
    
    def AddNode(self, newValue):
        newNode = Node(newValue)
        newNode.SetNextNode(self.head)
        self.head = newNode
        
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
            self.head = self.head.GetNextNode()
        currentNode = self.head
        while (currentNode != None):
            if currentNode.GetNextNode().IsLetterInWord(letter):
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
            currentNode = currentNode.GetNextNode()

    def RemoveNodesWithLetterAtIndex(self, letter, index):
        """
        Removes any node in the list where the nodes word contains a given letter at a given index
        """
        while self.head.GetLetterIndex(letter) == index:
            self.head = self.head.GetNextNode()
        currentNode = self.head
        while (currentNode != None):
            if currentNode.GetNextNode().GetLetterIndex(letter) == index:
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
            currentNode = currentNode.GetNextNode()

    def KeepNodesWithLetter(self, letter):
        """
        Keeps any node in the list where the nodes word contains a given letter
        """
        while not self.head.IsLetterInWord(letter):
            self.head = self.head.GetNextNode()
        currentNode = self.head
        while (currentNode != None):
            if not currentNode.GetNextNode().IsLetterInWord(letter):
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
            currentNode = currentNode.GetNextNode()

    def KeepNodesWithLetterAtIndex(self, letter, index):
        """
        Keeps any node in the list where the nodes word contains a given letter at a given index
        """
        while not self.head.GetLetterIndex(letter) == index:
            self.head = self.head.GetNextNode()
        currentNode = self.head
        while (currentNode != None):
            if not currentNode.GetNextNode().GetLetterIndex(letter) == index:
                currentNode.SetNextNode(currentNode.GetNextNode().GetNextNode())
            currentNode = currentNode.GetNextNode()
