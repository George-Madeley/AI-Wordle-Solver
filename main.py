from multiprocessing.sharedctypes import Value
from LinkedList import LinkedList

class main:
    def __init__(self):
        self.possibleWords = self.InitAllWords()

    def InitAllWords(self):
        # allWords = LinkedList("birth")
        # allWords.AddWord("abuse")
        # allWords.AddWord("beach")
        # allWords.AddWord("drink")
        # allWords.AddWord("scale")
        try:
            allWordsFile = open("ListOfWords.txt", "r")
            firstWord = allWordsFile.readline()
            allWords = LinkedList(firstWord)
            for line in allWordsFile:
                word = line.replace('\n', '').lower()
                if len(word) != 5:
                    print("ERROR: " + word + " has a length of more than five")
                    raise ValueError
                allWords.AddWord(word)
            return allWords
        except ValueError:
            print("ERROR")

    def GetPossibleWords(self):
        return self.possibleWords

    def GetGuessWord(self):
        return self.possibleWords.GetRandomWord()

    def UpdatePossibleWords(self, lettersNotInGoal, lettersInGoal, lettersInCorrectPos):
        for letter in lettersNotInGoal:
            self.possibleWords.RemoveNodesWithLetter(letter)
        for letter in lettersInGoal:
            self.possibleWords.KeepNodesWithLetter(letter)
        for index, letter in enumerate(lettersInCorrectPos):
            if letter != None:
                self.possibleWords.KeepNodesWithLetterAtIndex(letter, index)
