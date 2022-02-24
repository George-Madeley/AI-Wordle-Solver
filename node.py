class Node:
    def __init__(self, word):
        self.word = word
        self.nextNode = None

    def SetWord(self, word):
        self.word = word

    def GetWord(self):
        return self.word

    def SetNextNode(self, node):
        self.nextNode = node

    def GetNextNode(self):
        return self.nextNode

    def IsWordValid(self):
        return len(self.word) == 5

    def IsLetterInWord(self, letter):
        letterIndex = self.word.find(str(letter))
        return letterIndex >= 0