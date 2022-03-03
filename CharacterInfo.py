from ctypes import Array
from numpy import array


class CharacterInfo:
    """
    Holds information of a given character.
    
    Holds the number of occurances of a character in every
    known word in each location in the words.
    
    Attributes:
        statList: List of occurances in each location.
        character: The letter the information is about.
    """
    
    def __init__(self, character: str) -> None:
        """
        Initialises the CharacterInfo object.
        
        Args:
            character: The character to base the stats around.
        """

        self.statList = [0, 0, 0, 0, 0]
        self.character = character

    def GetStatAtIndex(self, index: int) -> int:
        """
        Returns the number of occurances of the character at the
        provided index.
        
        Args:
            index: The index to find the letter at.

        Returns:
            The number of occurances of the character at the provided
            index.
        """

        if index < 0 or index > 4:
            return -1
        return self.statList[index]

    def IncrementStatAtIndex(self, index: int) -> bool:
        """
        Increments the number of occurances of the character at the
        provided index by one.
        
        Args:
            index: The index to increase the occurances by one.

        Returns:
            True if the occurance at the index was successfully
            incremented
        """

        if index < 0 or index > 4:
            return False
        self.statList[index] += 1
        return True
    
    def GetStatList(self) -> list[int]:
        """
        Returns the list of the number of occurances at each index.

        Returns:
            The list of the number of occurances at each index.
        """

        return self.statList

    def GetStatTotal(self) -> int:
        """
        Returns the total amount of times the character has occured.

        Returns:
            The total amount of times the character occured.
        """

        total = 0
        for stat in self.statList:
            total += stat
        return total

    def GetCharacter(self) -> str:
        """
        Returns the stored character.

        Returns:
            The stored character.
        """

        return self.character

    def SetCharacter(self, character: str) -> None:
        """
        Sets the character to a new provided character.
        
        Args:
            character: The new character.
        """

        self.character = character

    def HasZero(self) -> bool:
        """
        Returns True if there is a zero within the statList.
        
        Returns:
            True if there is a zero within the statList.
        """

        return 0 in self.statList

    def GetZeroIndexes(self) -> list[int]:
        """
        Returns the index of position in the statList that equal zero.
        
        Returns:
            The index of position in the statList that equal zero.
        """
        indexes = []
        for index, value in enumerate(self.statList):
            if value == 0:
                indexes.append(index)
        return indexes
