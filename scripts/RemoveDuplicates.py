def RemoveDuplicateWords():
    """
    Removes and duplicate words from the list of words text file.
    """

    allWords = []
    with open("ListOfWords.txt", "r") as allWordsFile:
        for line in allWordsFile:
            word = line.strip('\n').lower()
            if len(word) == 5 and word not in allWords:
                allWords.append(word)
            elif len(word) > 5 and word not in allWords:
                word = word[:5]
                allWords.append(word)
    allWords.sort()
    with open('ListOfWords.txt', 'w') as wordFile:
        for word in allWords:
            wordFile.write(f"{word}\n")

if __name__ == "__main__":  
    RemoveDuplicateWords()
