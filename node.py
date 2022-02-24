class Node:
    def __init__(self, word):
        self.word = word
        self.nextNode = None

    def __str__(self):
        return self.word

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

    def GetLetterIndex(self, goalLetter):
        for index, letter in enumerate(self.word):
            if goalLetter == letter:
                return index
        return -1