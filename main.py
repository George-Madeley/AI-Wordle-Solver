from LinkedList import LinkedList
from AlphabetStat import AlphabetStat

class main:
    def __init__(self):
        self.possibleWords = self.InitAllWords()
        self.alphabetStats = self.InitAlphabetStats()
        self.CalculateAlphabetStats()
        # self.alphabetStats.sort(key=lambda x: x.GetStatTotal(), reverse=True)

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

    def InitAlphabetStats(self):
        alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        alphabetStatArray = []
        for character in alphabet:
            alphabetStatArray.append(AlphabetStat(character))
        return alphabetStatArray

    def CalculateAlphabetStats(self):
        for alphabetStat in self.alphabetStats:
            self.possibleWords.CalculateTotalCharacterOccurrences(alphabetStat)

    def GetPossibleWords(self):
        return self.possibleWords

    def GetRandomWord(self):
        return self.possibleWords.GetRandomWord()

    def GetGuessWord(self):
        self.InitAlphabetStats()
        self.CalculateAlphabetStats()
        return self.GetBestWord()
        # return self.possibleWords.GetRandomWord()

    def GetBestWord(self):
        self.possibleWords.CalculateBestWord(self.alphabetStats)
        return self.possibleWords.GetBestWord()

    def AddNewWord(self, word):
        self.possibleWords.AddWord(word)

    def UpdatePossibleWords(self, lettersNotInGoal, lettersInGoal, lettersInCorrectPos):
        for letter in lettersNotInGoal:
            self.possibleWords.RemoveNodesWithLetter(letter)
        for index, letter in enumerate(lettersInGoal):
            if letter != None:
                self.possibleWords.RemoveNodesWithLetterAtIndex(letter, index)
        for index, letter in enumerate(lettersInCorrectPos):
            if letter != None:
                self.possibleWords.KeepNodesWithLetterAtIndex(letter, index)
