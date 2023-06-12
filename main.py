from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys

import numpy as np

def validGeometry(width,height):
    validList = []
    x,y,buttWidth,buttHeight = 10,10,0,0
    x_num = 0

    buttWidth = (width - 30) / 3
    buttHeight = (height - 30) / 3
    for i in range(9):
        if x_num % 3 == 0 and x_num != 0:
            x = 10
            y += (buttHeight + 5)
        validList.append((x,y,buttWidth,buttHeight))
        x +=  (buttWidth + 5)

        
        x_num += 1 
    print(validList)
    return validList

class frame(QFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.setStyleSheet("background-color: black")
class ui():
    def __init__(self,main):
        self.main = main
        main.resize(600,600)
        self.mainframe = frame(main)
        self.mainframe.resize(main.size())
        self.tableframe = QFrame(self.mainframe)
        sizeWidth = self.main.size().width()/2
        sizeHeight = self.main.size().height()/2
        x = sizeWidth * 0.50
        y = sizeHeight * 0.50
        self.tableframe.setGeometry(x ,y ,sizeWidth,sizeHeight)
        self.tableframe.setStyleSheet("border: 2px solid gray;border-radius:25px")
        randGeos = list(np.random.randint(0,9,3))
        validList = validGeometry(sizeWidth,sizeHeight)
        while True:
            if len(set(randGeos)) == len(randGeos):
                break
            else:
                randGeos = list(np.random.randint(0,9,3))

            
        print(randGeos)
        for i in range(3):
            b = validList[randGeos[i]]
            but = QPushButton(self.tableframe)
            but.setText("2")
            but.setGeometry(QRect(b[0],b[1],b[2],b[3]))
            but.setStyleSheet("color: gray;font-size: 35px")

if __name__ == "__main__":
    app = QApplication()
    main = QMainWindow()
    ui(main)
    main.show()
    sys.exit(app.exec())