from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from time import sleep
import numpy as np
class mouseTracker(QObject):
    sig = Signal()
    def __init__(self,rt:QApplication):
        super().__init__()
        self.rt = rt
    @Slot()
    def run(self,event:QEvent):
        e = QMouseEvent(event)

        while True:
            if self.rt.mouseButtons() == QApplication.mouseButtons().NoButton:
                self.sig.emit()
                break
            sleep(0.01)
            #print("im in")
            

class moveButtons(QObject):
    sig = Signal(QEvent)

    def __init__(self,butt,validDirectories,validList):
        self.validDirectories = validDirectories #[down,up,right,left]
        self.butt:QPushButton = butt
        super().__init__()
        self.status = False
        self.wichbutt = 0
        self.validnumright = 0
        self.validnumleft = 0
        self.validnumup = 0
        self.validnumdown = 0
        self.mouseEventPositions = []
        self.validList = validList


    def eventFilter(self,o:QPushButton,e:QEvent):
        if self.status and e.type() == e.Type.MouseMove:
            mouse = QMouseEvent(e).position()
            #print(mouse)
            if abs(mouse.x()) != mouse.x():
                return
            self.mouseEventPositions.append(mouse.toTuple())
            if len(self.mouseEventPositions) > 50:

                w = self.mouseEventPositions[-1][0] - self.mouseEventPositions[-45][0] 
                r = self.mouseEventPositions[-1][1] - self.mouseEventPositions[-45][1]
                
                q:QPushButton = self.butt[self.wichbutt]
                #self.mouseEventPositions = []

                buttGeoWidth = q.geometry().width()
                buttGeoHeight = q.geometry().height()
                buttGeoXY = self.validList.index((q.geometry().x(),q.geometry().y(),buttGeoWidth,buttGeoHeight))
                g = [self.validnumright,
                    self.validnumleft,
                    self.validnumup,
                    self.validnumdown]
                if sum(g) == 15:
                    g.sort()
                    print(g)
                    self.validnumright = 0
                    self.validnumleft = 0
                    self.validnumup = 0
                    self.validnumdown = 0

                if abs(w) > abs(r):
                    if abs(w) != w:
                        self.validnumleft += 1
                        #if self.validDirectories[self.wichbutt][3]:
                            #self.butt[self.wichbutt].setGeometry(self.validList[buttGeoXY - 1][0],self.validList[buttGeoXY - 1][1]
                                                             #,buttGeoWidth,buttGeoHeight)
                        return#
                    else:
                        self.validnumright += 1

                        #if self.validDirectories[self.wichbutt][2]:
                            #self.butt[self.wichbutt].setGeometry(self.validList[buttGeoXY + 1][0],self.validList[buttGeoXY + 1][1]
                                                              #,#buttGeoWidth,buttGeoHeight)
                        return#
                if abs(w) < abs(r):
                    if abs(r) != r:
                        self.validnumup += 1

                         #if self.validDirectories[self.wichbutt][1]:
                            #self.butt[self.wichbutt].setGeometry(self.validList[buttGeoXY -  3][0],self.validList[buttGeoXY - 3][1]
                                                     #,buttGeoWidth,buttGeoHeight)
                        return#
                    else:
                        self.validnumdown += 1

                        #if self.validDirectories[self.wichbutt][0]:
                            #self.butt[self.wichbutt].setGeometry#(self.validList[buttGeoXY + 3][0],self.validList[buttGeoXY + 3][1]
                        return#
                
                    
            #print(self.mouseEventPositions)
            #self.butt[self.wichbutt].setGeometry(10,10,20,50)
            return
                
        if e.type() == e.Type.MouseButtonPress:
            if o.isWindowType():
                return
            if o.windowType() == QFrame:
                return
            print(o)
            self.wichbutt = int(o.objectName())
            #position = QMouseEvent(e)
            print(o.objectName())
            self.sig.emit(e)
            self.status = True

    @Slot()
    def call(self):
        self.mouseEventPositions = []
        self.status = False
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
        self.validList = validGeometry(sizeWidth,sizeHeight)
        while True:
            if len(set(randGeos)) == len(randGeos):
                break
            else:
                randGeos = list(np.random.randint(0,9,3))
        randGeos.sort()
        self.buttList = []
        self.validDiretions = []
        self.geometrysTaken = []
        for i in range(3):
            b = self.validList[randGeos[i]]
            self.geometrysTaken.append(b)
            but = QPushButton(self.tableframe)
            but.setObjectName(str(i))
            but.setText("2")

            but.setGeometry(QRect(b[0],b[1],b[2],b[3]))
            but.setStyleSheet("color: gray;font-size: 35px")
            self.buttList.append(but)
        default = [] 
        for i in range(len(randGeos)):
            i = randGeos[i]
            if abs(i + 3) < len(self.validList):
                if self.validList[i + 3] in self.geometrysTaken:
                    default.append(False)
                else:default.append(True)
            else:default.append(False)

            if abs(i - 3) == i - 3:
                if self.validList[i - 3] in self.geometrysTaken:
                    default.append(False)
                else:default.append(True)
            else:default.append(False)
            if abs(i + 1) < len(self.validList):
                if self.validList[i + 1] in self.geometrysTaken:
                    default.append(False)
                else:default.append(True)
            else:default.append(False)
            if abs(i - 1) == i - 1:
                if self.validList[i - 1] in self.geometrysTaken:
                    default.append(False)
                else:default.append(True)
            else:default.append(False)
            self.validDiretions.append(default)
            default = []





if __name__ == "__main__":
    app = QApplication()
    
    main = QMainWindow()
    i = ui(main)
    event = moveButtons(i.buttList,i.validDiretions,i.validList)
    thread = QThread()
    motra = mouseTracker(app)
    motra.moveToThread(thread)
    #thread.started.connect(motra)
    event.sig.connect(motra.run)
    motra.sig.connect(event.call)
    thread.start()
    app.installEventFilter(event)
    main.show()
    sys.exit(app.exec())