from typing import TypeAlias
from CharacterInfo import CharacterInfo

AlphabetInfo: TypeAlias = list[CharacterInfo]

class KnowledgeBase:
    def __init__(self) -> None:
        self.__alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        self.correctLetterPos = [None, None, None, None, None]
        self.lettersInGoal = []
        self.incorrectLetterPos = [[] for i in range(5)]
        self.lettersNotInGoal = []
        self.wordList = None

    def UpdateBasicKnowledge(self, lettersNotInGoal: list[str], lettersInGoal: list[any], lettersInCorrectPos: list[any]) -> None:
        """
        Adds the information gained from the last Wordle attempt to the knowledge base.
        
        Args:
            lettersNotInGoal: The array of the letters not in the goal word.
            lettersInGoal: The array of the letter in the goal word in their incorrect location.
            
        """

        self.lettersNotInGoal += lettersNotInGoal

        for index, letter in enumerate(lettersInGoal):
            if letter in self.__alphabet and not letter in self.lettersInGoal:
                self.lettersInGoal.append(letter)
                self.incorrectLetterPos[index].append(letter)

        for index, letter in enumerate(lettersInCorrectPos):
            # Checks for letter conflict in estimated Goal word.
            if self.correctLetterPos[index] == None:
                self.correctLetterPos[index] = letter
                if letter in self.__alphabet and not letter in self.lettersInGoal:
                    self.lettersInGoal.append(letter)
            elif  self.correctLetterPos[index] == letter or letter == None:
                pass
            else:
                # Prints error is letter conflict has occured.
                print("ERROR: Letter conflict at index " + str(index) + " between '" + str(letter) + "' and '" + str(self.correctLetterPos[index]) + "' in estimated goal word.")

    def UpdatePossibleWords(self) -> None:
        """
        Updates linked list of all possible words based
        on the results of the last entered word.
        """

        # Removes any word with letters that are not in the goal
        for letter in self.lettersNotInGoal:
            self.wordList.RemoveNodesWithLetter(letter)

        # Removes any word with the letters in the goal but at the wrong position
        for index, letterList in enumerate(self.incorrectLetterPos):
            for letter in letterList:
                self.wordList.RemoveNodesWithLetterAtIndex(letter, index)

        # Removes any word that does not contain a letter in the goal word
        for letter in self.lettersInGoal:
            self.wordList.KeepNodesWithLetter(letter)

        # Removes any word that does not contain a letter in the goal in the correct place
        for index, letter in enumerate(self.correctLetterPos):
            if letter != None:
                self.wordList.KeepNodesWithLetterAtIndex(letter, index)

    def UpdateLettersNotInGoal(self) -> None:
        """
        Scans through all possible goal words and find letters
        not in any of the words and adds those letters to the
        'lettersNotInGoal' list
        """

        strLettersInPossibleWords = str(self.wordList.GetPossibleWordsStr())
        strLettersInPossibleWords.replace("\n", "")
        possibleLettersInGoal = []
        # Find all letters that could be in goal word
        for char in strLettersInPossibleWords:
            if not char in possibleLettersInGoal:
                possibleLettersInGoal.append(char)
        # Find all letters that are not in the goal word
        for char in self.__alphabet:
            if not char in possibleLettersInGoal and not char in self.lettersNotInGoal:
                self.lettersNotInGoal.append(char)
            
    def UpdateIncorrectLetterPos(self, alphabetOccurances: AlphabetInfo) -> None:
        """
        Using the character occurances, updates the list of letters
        in the incorrect position if that letter has an occurance
        score of zero in that position.
        
        Args:
            alphabetOccurances: List of each character occurance within all possible words.
        """
        
        for characterOccurances in alphabetOccurances:
            if characterOccurances.HasZero():
                zeroLocations = characterOccurances.GetZeroIndexes()
                for index in zeroLocations:
                    character = characterOccurances.GetCharacter()
                    if not character in self.lettersNotInGoal:
                        self.incorrectLetterPos[index].append(character)

    def UpdateLettersInGoal(self) -> None:
        """
        Creates a list of all the letters in the alphabet. Removes any
        letters that are not in all of the possible words.
        """

        # Creates dictionaries to store information about whether each letter is in all possible words
        singleLetters = {}
        doubleLetters = {}
        tripleLetters = {}
        quadrupleLetters = {}
        quintupleLetters = {}
        for letter in self.__alphabet:
            singleLetters[letter] = True
            doubleLetters[letter] = True
            tripleLetters[letter] = True
            quadrupleLetters[letter] = True
            quintupleLetters[letter] = True

        # Calcualtes which letters appears in all words
        singleLetters, doubleLetters, tripleLetters, quadrupleLetters, quintupleLetters = self.wordList.CalculateCommonLetters(singleLetters, doubleLetters, tripleLetters, quadrupleLetters, quintupleLetters)
        
        pass

        # clears all inforamtion about letters in goal
        self.lettersInGoal = []
        
        # updates information about letters in goal
        for letter in self.__alphabet:
            if singleLetters[letter] == True:
                self.lettersInGoal.append(letter)
            if doubleLetters[letter] == True:
                self.lettersInGoal.append(letter)
            if tripleLetters[letter] == True:
                self.lettersInGoal.append(letter)
            if quadrupleLetters[letter] == True:
                self.lettersInGoal.append(letter)
            if quintupleLetters[letter] == True:
                self.lettersInGoal.append(letter)
            
        
