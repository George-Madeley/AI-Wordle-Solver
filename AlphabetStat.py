class AlphabetStat:
    def __init__(self, character):
        self.statList = [0, 0, 0, 0, 0]
        self.character = character

    def GetStatAtIndex(self, index):
        if index < 0 or index > 4:
            return -1
        return self.statList[index]

    def IncrementStatAtIndex(self, index):
        if index < 0 or index > 4:
            return False
        self.statList[index] += 1
        return True
    
    def GetStatList(self):
        return self.statList

    def GetStatTotal(self):
        total = 0
        for stat in self.statList:
            total += stat
        return total

    def GetCharacter(self):
        return self.character

    def SetCharacter(self, character):
        self.character = character
