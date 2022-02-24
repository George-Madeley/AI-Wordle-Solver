from LinkedList import LinkedList

class main:
    def __init__(self):
        self.possibleWords = self.InitAllWords()

    def InitAllWords(self):
        allWords = LinkedList("birth")
        allWords.AddWord("abuse")
        allWords.AddWord("beach")
        allWords.AddWord("drink")
        allWords.AddWord("scale")
        return allWords

    def GuessWord(self):
        