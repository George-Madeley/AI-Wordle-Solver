import string
from AlphabetStat import AlphabetStat

class Node:
    def __init__(self, word):
        self.word = word
        self.score = 0
        self.nextNode:Node = None

    def __str__(self):
        return self.word

    def SetWord(self, word:string):
        self.word = word

    def GetWord(self):
        return self.word

    def SetNextNode(self, node):
        self.nextNode = node

    def GetNextNode(self):
        return self.nextNode

    def IsWordValid(self):
        return len(self.word) == 5

    def hasLetter(self, letter:string):
        letterIndex = self.word.find(letter)
        return letterIndex >= 0

    def GetLetterIndex(self, goalLetter):
        for index, letter in enumerate(self.word):
            if goalLetter == letter:
                return index
        return -1

    def CalculateCharacterOccurrences(self, characterStats):
        for index, letter in enumerate(self.word):
            if letter == characterStats.GetCharacter():
                characterStats.IncrementStatAtIndex(index)

    def ResetScore(self):
        self.score = 0

    def GetScore(self):
        return self.score

    def IncreaseScoreBy(self, amount):
        self.score += amount