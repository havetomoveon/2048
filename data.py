import numpy as np
class Data():
    def __init__(self):
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
    def buttGeos(self):
        for i in self.index:
            self.geosButt.update({i:[self.validList[i],2]})
            self.geometrysTaken.append(self.validList[i])
    def validGeometry(self,width,height):
        x,y,buttWidth,buttHeight = 10,10,0,0
        x_num = 0
        buttWidth = (width - 30) / 3
        buttHeight = (height - 30) / 3
        for i in range(9):
            if x_num % 3 == 0 and x_num != 0:
                x = 10
                y += (buttHeight + 5)
            self.validList.append((x,y,buttWidth,buttHeight))
            x +=  (buttWidth + 5)       
            x_num += 1 
    def validDirectories(self):
        default = [] 
        #[down,up,right,left]
        down = 0
        up = 0
        right = 0
        left = 0
        for i in self.index:
            if  abs(i + 3) < len(self.validList):
                if self.validList[i + 3] in self.geometrysTaken:
                    default.append(False)
                else:default.append(True)
            else:default.append(True)
            down = 0
            if abs(i - 3) == i - 3:
                if self.validList[i - 3] in self.geometrysTaken:
                    default.append(False)
                else:default.append(True)
            else:default.append(True)
            up = 0
            if abs(i + 1) < len(self.validList):
                if self.validList[i + 1] in self.geometrysTaken:
                    default.append(False)
                else:default.append(True)
            else:default.append(True)
            right = 0
            if abs(i - 1) == i - 1:
                if self.validList[i - 1] in self.geometrysTaken:
                    default.append(False)
                else:default.append(True)
            else:default.append(True)
            left = 0
            self.validDiretions.append(default)
            default = []
    def getGeosButt(self):
        return self.geosButt
    def down(self):
        print("im down")
        old  = list(self.geosButt.keys())
        for i in old:
            if  abs(i + 3) < len(self.validList):
                if not self.validList[i + 3] in self.geometrysTaken:
                    self.geosButt.pop(i)
                    self.geosButt.update({i + 3 : [self.validList[i + 3],2]})
                    self.geometrysTaken.remove(self.validList[i])
                    self.geometrysTaken.append(self.validList[i + 3])
    def up(self):
        print("im up")
        old  = list(self.geosButt.keys())
        for i in old:
            if abs(i - 3) == i - 3:
                if not self.validList[i - 3] in self.geometrysTaken:
                    self.geosButt.pop(i)
                    self.geosButt.update({i - 3 : [self.validList[i - 3],2]})
                    self.geometrysTaken.remove(self.validList[i])
                    self.geometrysTaken.append(self.validList[i - 3])
    def right(self):
        print("im right")
        old  = list(self.geosButt.keys())
        for i in old:
            if not (i + 1) % 3 == 0:
                if abs(i + 1) < len(self.validList):
                    if not self.validList[i + 1] in self.geometrysTaken:
                        self.geosButt.pop(i)
                        self.geosButt.update({i + 1 : [self.validList[i + 1],2]})
                        self.geometrysTaken.remove(self.validList[i])
                        self.geometrysTaken.append(self.validList[i + 1])
                    

    def left(self):
        print("im left")
        old  = list(self.geosButt.keys())
        for i in old:
            if not (i) % 3 == 0:
                if abs(i - 1) == i - 1:
                    if not self.validList[i - 1] in self.geometrysTaken:
                        self.geosButt.pop(i)
                        self.geosButt.update({i - 1 : [self.validList[i - 1],2]})
                        self.geometrysTaken.remove(self.validList[i])
                        self.geometrysTaken.append(self.validList[i - 1])              
        