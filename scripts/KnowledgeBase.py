from Node import Node

class KnowledgeBase:
    """
    Holds all of the agents known information.
    
    Contains a series of methods used to infer more knowledge
    based on all the known information.
    
    Attributes:
        correctLetterPos: An array of all the letters in the goal word in the correct position.
        incorrectLetterPos: An array of lists containing all the letters in the incorrect position.
        lettersInGoal: All the letters in the goal word.
        lettersNotInGoal: All the letters not in the goal word.
        wordList: A list of all the known words.
    """

    def __init__(self) -> None:
        """
        Initialises the knowledge base with its attributes.
        """

        self.__alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
        
        self.alphabetOccurances = {}
        self.InitialiseAlphabetOccurances()

        self.correctLetterPos = [None, None, None, None, None]
        self.lettersInGoal = []
        self.incorrectLetterPos = [[] for i in range(5)]
        self.lettersNotInGoal = []

        self.listOfWords = []
        self.__possibleWords = []

    def AddWord(self, newWord: str) -> None:
        """
        Adds a new node to the list of words.

        Args:
            newWord: The value of the new node.
        """

        node = Node(newWord)
        self.listOfWords.append(node)

    def CalculateAlphabetOccurances(self) -> None:
        """
        Calculates the number of occurances of each letter
        in all the known words.
        """
        
        allWords = [node.GetWord() for node in self.listOfWords]
        allWords = "".join(allWords)
        for index, character in enumerate(allWords):
            self.alphabetOccurances[character][index%5] += 1

    def CalculateCommonLetters(self, singleLetters: dict, doubleLetters: dict, tripleLetters: dict, quadrupleLetters: dict, quintupleLetters: dict) -> any:
        """
        Calculates which letters are in every single word. Calculates
        if there are any double, triple, quadruple, or quintuple
        letters in all known words.
        
        Args:
            singleLetters: Dictionary of letters all assumed to be in every word once.
            doubleLetters: Dictionary of letters all assumed to be in every word twice.
            tripleLetters: Dictionary of letters all assumed to be in every word thrice
            quadrupleLetters: Dictionary of letters all assumed to be in every word four times.
            quintupleLetters: Dictionary of letters all assumed to be in every word five times.

        Returns:
            Dictionary of all letters that appear in every word once.
            Dictionary of all letters that appear in every word twice.
            Dictionary of all letters that appear in every word thrice
            Dictionary of all letters that appear in every word four times.
            Dictionary of all letters that appear in every word five times.
        """

        possibleWords = self.__possibleWords
        for node in possibleWords:
            word = node.GetWord()
            for letter in self.__alphabet:
                if letter in word:
                    count = word.count(letter)
                    if count < 1:
                        # Letter does not appear in word
                        singleLetters[letter] = False
                        doubleLetters[letter] = False
                        tripleLetters[letter] = False
                        quadrupleLetters[letter] = False
                        quintupleLetters[letter] = False
                    elif count < 2:
                        # Letter appear in word once
                        doubleLetters[letter] = False
                        tripleLetters[letter] = False
                        quadrupleLetters[letter] = False
                        quintupleLetters[letter] = False
                    elif count < 3:
                        # letter appears in word twice
                        tripleLetters[letter] = False
                        quadrupleLetters[letter] = False
                        quintupleLetters[letter] = False
                    elif count < 4:
                        # letter appears in word thrice
                        quadrupleLetters[letter] = False
                        quintupleLetters[letter] = False
                    elif count < 5:
                        # letter appears in word four times
                        quintupleLetters[letter] = False
                    else:
                        # letter appears in word fivce or more times
                        pass
                else:
                    # Letter does not appear in word
                    singleLetters[letter] = False
                    doubleLetters[letter] = False
                    tripleLetters[letter] = False
                    quadrupleLetters[letter] = False
                    quintupleLetters[letter] = False
        return singleLetters, doubleLetters, tripleLetters, quadrupleLetters, quintupleLetters

    def CalculateKnowledgeScores(self, knowledgeBase: any) -> None:
        """
        Calculates the knowledge scores for each word.
        
        Args:
            knowledgeBase: The agents knowledge base.
        """

        for node in self.listOfWords:
            accountedForLetter = []
            word = node.GetWord()
            node.ResetKnowledgeScore()
            for index, letter in enumerate(word):
                # Check if letter is in the correct position in goal word
                if letter in knowledgeBase.correctLetterPos:
                    # Letter is in correct position list
                    pass
                elif letter in knowledgeBase.lettersInGoal:
                    # Letter is in the word
                    if letter in knowledgeBase.incorrectLetterPos[index]:
                        # letter position is already known
                        pass
                    else:
                        # agent knows the letter is in the word but not the position
                        if knowledgeBase.correctLetterPos.count(None) > 1:
                            # agent knows there is more than one place left
                            node.IncreaseKnowledgeScoreBy(1)
                        elif knowledgeBase.correctLetterPos.count(None) == 1:
                            # there is one place left
                            pass
                        else:
                            # no places are left
                            pass
                elif letter in knowledgeBase.lettersNotInGoal:
                    # agent knows the letter is not in the goal
                    pass
                else:
                    # agent knows nothing about this letter
                    if len(knowledgeBase.lettersInGoal) >= 5:
                        # agent knows all the letters
                        pass
                    else:
                        # agent does not know all the letters in the goal
                        if knowledgeBase.correctLetterPos.count(None) > 1:
                            # agent knows there is more than one place left
                            if letter in accountedForLetter:
                                # There was a double of this letter
                                node.IncreaseKnowledgeScoreBy(1)
                            else:
                                # There was a single of this letter
                                accountedForLetter.append(letter)
                                node.IncreaseKnowledgeScoreBy(2)
                        elif knowledgeBase.correctLetterPos.count(None) == 1:
                            # there is one place left
                            node.IncreaseKnowledgeScoreBy(1)
                        else:
                            # no places are left
                            pass

    def CalculateOccuranceScores(self) -> None:
        """
        Calculates the occurance scores of all words in the list. It now
        calculates based on letter position as well.
        """

        for node in self.listOfWords:
            node.ResetOccuranceScore()
            for index, letter in enumerate(node.GetWord()):
                try:
                    if node.GetWord().count(letter) > 1:
                        continue
                    score = self.alphabetOccurances[letter][index]
                    node.IncreaseOccuranceScoreBy(score)
                except:
                    pass

    def ContainsWord(self, word: str) -> bool:
        """
        Checks if a given word is in the list.
        
        Args:
            word: The word to be found.
            
        Returns:
            True if the word is found.
        """

        for node in self.listOfWords:
            if node.GetWord() == word:
                return True
        return False   

    def GetBestKnowledgeWord(self) -> Node:
        """
        Returns the word with the most amount of new knowledge
        and with the largest occurance score out of those words..
        
        Returns:
            The word with the most amount of new knowledge.
        """

        if len(self.__possibleWords) == 1: return self.__possibleWords[0]

        bestScore = 0
        bestNodes = []
        for node in self.listOfWords:
            if bestScore == node.GetKnowledgeScore():
                bestNodes.append(node)
            elif bestScore < node.GetKnowledgeScore():
                bestNodes = [node]
                bestScore = node.GetKnowledgeScore()
        bestScore = 0
        bestNode = None
        for node in bestNodes:
            if bestScore <= node.GetOccuranceScore():
                bestScore = node.GetOccuranceScore()
                bestNode = node
        return bestNode
                        
    def GetBestOccuranceWord(self) -> Node:
        """
        Returns the word with the largest number of letter occurances.

        Returns:
            The best word.
        """

        if len(self.__possibleWords) == 1: return self.__possibleWords[0]

        bestScore = 0
        bestNode = None
        for node in self.__possibleWords:
            if bestScore <= node.GetOccuranceScore():
                bestScore = node.GetOccuranceScore()
                bestNode = node
        return bestNode

    def GetPossibleWords(self) -> list:
        """
        Returns a list of all the possible words.
        
        Returns:
            A list of all possible words.
        """

        self.__possibleWords = [node for node in self.listOfWords if node.IsPossibleWord()]
        return self.__possibleWords

    def InitialiseAlphabetOccurances(self) -> dict:
        """
        Initialises all the stats associated with each
        letter of the alphabet an returns it.

        Returns:
            A dictionary of character stats for each letter
            in the alphabet.
        """
        self.alphabetOccurances = {character: [0, 0, 0, 0, 0] for character in self.__alphabet}
        
    def KeepNodesWithLetter(self, letter: str) -> None:
        """
        Sets the attribute isPossibleWord to True of
        any node in the list where the nodes word contains
        a given letter.

        Args:
            letter: The letter to keep.
        """

        for node in self.listOfWords:
            if not letter in node.GetWord():
                node.NotPossibleWord()

    def KeepNodesWithLetterAtIndex(self, letter: str, index: int) -> None:
        """
        Sets the attribute isPossibleWord to True of any node
        in the list where the nodes word contains a given letter
        at a given index.

        Args:
            letter: The letter to keep.
            index: The index of the letter to keep.
        """

        for node in self.listOfWords:
            if not letter == node.GetWord()[index]:
                node.NotPossibleWord()

    def RemoveNodesWithLetter(self, letter: str) -> None:
        """
        Sets the attribute isPossibleWord to False of any
        node in the list where the nodes word contains a
        given letter.

        Args:
            letter: The letter to be removed.
        """

        for node in self.listOfWords:
            if letter in node.GetWord():
                node.NotPossibleWord()

    def RemoveNodesWithLetterAtIndex(self, letter: str, index: int) -> None:
        """
        Sets the attribute isPossibleWord to False of any
        node in the list where the nodes word contains a
        given letter at a given index.

        Args:
            letter: The letter to be removed.
            index: The index of the letter to be removed.
        """

        for node in self.listOfWords:
            if letter == node.GetWord()[index]:
                node.NotPossibleWord()

    def RemoveWord(self, removeWord: str) -> None:
        """
        Removes a given word from all lists.
        
        Args:
            removeWord: The word to remove.
        """

        self.listOfWords = [node for node in self.listOfWords if node.GetWord() != removeWord]
        self.__possibleWords = [node for node in self.listOfWords if node.GetWord() != removeWord]

    def UpdateBasicKnowledge(self, lettersNotInGoal: list, lettersInGoal: list, lettersInCorrectPos: list) -> None:
        """
        Adds the information gained from the last Wordle attempt to the knowledge base.
        
        Args:
            lettersNotInGoal: The array of the letters not in the goal word.
            lettersInGoal: The array of the letter in the goal word in their incorrect location.
            lettersInCorrectPos: The array of the letters in the goal word in their correct location.
        """
        # letters not in the goal word
        for letter in lettersNotInGoal:
            if letter in lettersInGoal or letter in lettersInCorrectPos:
                continue
            elif letter not in self.lettersNotInGoal:
                self.lettersNotInGoal.append(letter)

        # letters in the goal word but in the incorrect place
        for index, letter in enumerate(lettersInGoal):
            if letter in self.__alphabet and letter not in self.lettersInGoal:
                self.lettersInGoal.append(letter)
            if letter in self.__alphabet and letter not in self.incorrectLetterPos[index]:
                self.incorrectLetterPos[index].append(letter)

        # letters in the goal word and in the correct place
        for index, letter in enumerate(lettersInCorrectPos):
            # Checks for letter conflict in estimated Goal word.
            if self.correctLetterPos[index] == None:
                self.correctLetterPos[index] = letter
                if letter in self.__alphabet and letter not in self.lettersInGoal:
                    self.lettersInGoal.append(letter)
            elif  self.correctLetterPos[index] == letter or letter == None:
                pass
            else:
                # Prints error is letter conflict has occured.
                print("ERROR: Letter conflict at index " + str(index) + " between '" + str(letter) + "' and '" + str(self.correctLetterPos[index]) + "' in estimated goal word.")

    def UpdateIncorrectLetterPos(self) -> None:
        """
        Using the character occurances, updates the list of letters
        in the incorrect position if that letter has an occurance
        score of zero in that position.
        """
        
        for character, occurances in self.alphabetOccurances.items():
            if 0 in occurances:
                # Gets a lsit of all the indexes where the value is equal to 0
                zeroLocations = [index for index, value in enumerate(occurances) if value == 0]
                for index in zeroLocations:
                    if character not in self.lettersNotInGoal:
                        self.incorrectLetterPos[index].append(character)

    def UpdateLettersInGoal(self) -> None:
        """
        Creates a list of all the letters in the alphabet. Removes any
        letters that are not in all of the possible words.
        """

        # Creates dictionaries to store information about whether each letter is in all possible words
        singleLetters = {letter: True for letter in self.__alphabet}
        doubleLetters = {letter: True for letter in self.__alphabet}
        tripleLetters = {letter: True for letter in self.__alphabet}
        quadrupleLetters = {letter: True for letter in self.__alphabet}
        quintupleLetters = {letter: True for letter in self.__alphabet}

        # Calcualtes which letters appears in all words
        singleLetters, doubleLetters, tripleLetters, quadrupleLetters, quintupleLetters = self.CalculateCommonLetters(singleLetters, doubleLetters, tripleLetters, quadrupleLetters, quintupleLetters)
        
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

    def UpdateLettersNotInGoal(self) -> None:
        """
        Scans through all possible goal words and find letters
        not in any of the words and adds those letters to the
        'lettersNotInGoal' list
        """

        possibleWords = [node.GetWord() for node in self.__possibleWords]
        strLettersInPossibleWords = "".join(possibleWords)
        possibleLettersInGoal = []
        # Find all letters that could be in goal word
        for letter in strLettersInPossibleWords:
            if letter not in possibleLettersInGoal:
                possibleLettersInGoal.append(letter)
        # Find all letters that are not in the goal word
        for letter in self.__alphabet:
            if letter not in possibleLettersInGoal and letter not in self.lettersNotInGoal:
                self.lettersNotInGoal.append(letter)

    def UpdatePossibleWords(self) -> None:
        """
        Updates linked list of all possible words based
        on the results of the last entered word.
        """

        # Removes any word with letters that are not in the goal
        for letter in self.lettersNotInGoal:
            self.RemoveNodesWithLetter(letter)

        # Removes any word with the letters in the goal but at the wrong position
        for index, letterList in enumerate(self.incorrectLetterPos):
            for letter in letterList:
                self.RemoveNodesWithLetterAtIndex(letter, index)

        # Removes any word that does not contain a letter in the goal word
        for letter in self.lettersInGoal:
            self.KeepNodesWithLetter(letter)

        # Removes any word that does not contain a letter in the goal in the correct place
        for index, letter in enumerate(self.correctLetterPos):
            if letter != None:
                self.KeepNodesWithLetterAtIndex(letter, index)
        
        self.GetPossibleWords()
