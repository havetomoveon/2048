import numpy as np
import random
class Data():
    def __init__(self):
        self.gameType = 5
        self.validList = []
        #self.validDirectories = []
        self.validDiretions = []
        self.geometrysTaken = []
        self.geosButt = {}
        self.index = list(np.random.randint(0,9,3))
        while True:
            if len(set(self.index)) == len(self.index):
                break
            else:
                self.index = list(np.random.randint(0,9,3))
        self.index.sort()
    def addNewButtonPositions(self):
        er = [0,2,6,8]
        inValidNums = list(self.geosButt.keys())
        i = random.choice(er)
        if not i in inValidNums:
            if i % 4 == 0:
                self.geosButt.update({i:[self.validList[i],2]})
                self.geometrysTaken.append(self.validList[i])
                return 

    def buttGeos(self):
        for i in self.index:
            self.geosButt.update({i:[self.validList[i],2]})
            self.geometrysTaken.append(self.validList[i])
    def validGeometry(self,width,height):
        x,y,buttWidth,buttHeight = 10,10,0,0
        x_num = 0
        buttWidth = (width - 30) / self.gameType
        buttHeight = (height - 30) / self.gameType
        for i in range(self.gameType * self.gameType):
            if x_num % self.gameType == 0 and x_num != 0:
                x = 10
                y += (buttHeight + 5)
            self.validList.append((x,y,buttWidth,buttHeight))
            x +=  (buttWidth + 5)       
            x_num += 1 
    def getGeosButt(self):
        return self.geosButt
    def changeButtonPosition(self, i, t):
        self.geosButt.update({i + t : [self.validList[i + t],self.geosButt.get(i)[1]]})
        self.geosButt.pop(i)
        self.geometrysTaken.remove(self.validList[i])
        self.geometrysTaken.append(self.validList[i + t])
    def changeButtonPositionEqual(self, i, t):
        firstButton = self.geosButt.get(i)[1]
        secondButton = self.geosButt.get(i + t)[1]
        if firstButton == secondButton :
            self.geosButt.pop(i)
            self.geosButt.update({i + t : [self.validList[i + t],firstButton + secondButton]})
            self.geometrysTaken.remove(self.validList[i])
    def down(self):
        old  = list(self.geosButt.keys())
        for i in reversed(old):
            if  abs(i + self.gameType) < len(self.validList):
                if not self.validList[i + self.gameType] in self.geometrysTaken:
                    self.changeButtonPosition(i, self.gameType)
                else:
                    self.changeButtonPositionEqual(i, self.gameType)
    def up(self):
        old  = list(self.geosButt.keys())
        for i in reversed(old):
            if abs(i - self.gameType) == i - self.gameType:
                if not self.validList[i - self.gameType] in self.geometrysTaken:
                   self.changeButtonPosition(i, -self.gameType)
                else:
                    self.changeButtonPositionEqual(i, -self.gameType)
    def right(self):
        old  = list(self.geosButt.keys())
        for i in reversed(old):
            if not (i + 1) % self.gameType == 0:
                if abs(i + 1) < len(self.validList):
                    if not self.validList[i + 1] in self.geometrysTaken:
                        self.changeButtonPosition(i, 1)
                    else:
                        self.changeButtonPositionEqual(i, 1)
    def left(self):
        old  = list(self.geosButt.keys())
        for i in reversed(old):
            if not (i) % self.gameType == 0:
                if abs(i - 1) == i - 1:
                    if not self.validList[i - 1] in self.geometrysTaken:
                        self.changeButtonPosition(i, -1)
                    else:
                        self.changeButtonPositionEqual(i, -1)              
        