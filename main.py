from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
import sys
from time import sleep
import numpy as np
import data
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
            sleep(0.1)            

class moveButtons(QObject):
    sig = Signal(QEvent)

    def __init__(self,data):
        super().__init__()
        self.status = False
        self.wichbutt = 0
        self.validnumright = 0
        self.validnumleft = 0
        self.validnumup = 0
        self.validnumdown = 0
        self.mouseEventPositions = []
        self.data = data
    def eventFilter(self,o:QPushButton,e:QEvent):
        if self.status and e.type() == e.Type.MouseMove:
            mouse = QMouseEvent(e).position()
            #print(mouse)
            if abs(mouse.x()) != mouse.x():
                return
            self.mouseEventPositions.append(mouse.toTuple())
            if len(self.mouseEventPositions) > 60:

                w = self.mouseEventPositions[-1][0] - self.mouseEventPositions[-59][0] 
                r = self.mouseEventPositions[-1][1] - self.mouseEventPositions[-59][1]
                
                g = [self.validnumright,
                    self.validnumleft,
                    self.validnumup,
                    self.validnumdown]
                if sum(g) == 16:
                    g.sort()
                    print(g)
                    if g[-1] == self.validnumright:
                        self.data.data.right()
                        self.data.setButtons()
                        print("right")
                    if g[-1] == self.validnumleft:
                        self.data.data.left()
                        self.data.setButtons()
                        print("left")
                    if g[-1] == self.validnumup:
                        self.data.data.up()
                        self.data.setButtons()
                        print("up")
                    if g[-1] == self.validnumdown:
                        print("down")
                        self.data.data.down()
                        self.data.setButtons()

                    self.validnumright = 0
                    self.validnumleft = 0
                    self.validnumup = 0
                    self.validnumdown = 0

                if abs(w) > abs(r):
                    if abs(w) != w:
                        self.validnumleft += 1
                        return
                    else:
                        self.validnumright += 1
                        return
                if abs(w) < abs(r):
                    if abs(r) != r:
                        self.validnumup += 1
                        return
                    else:
                        self.validnumdown += 1
                        return
        
            
                
        if e.type() == e.Type.MouseButtonPress:
            if o.isWindowType():
                return
            #if o.windowType() == QFrame:
                #return
            print(o)
            self.sig.emit(e)
            self.status = True

    @Slot()
    def call(self):
        self.mouseEventPositions = []
        self.status = False

class frame(QFrame):
    def __init__(self,parent):
        super().__init__(parent)
        self.setStyleSheet("background-color: black")
        
class ui():
    def __init__(self,main):
        self.nodeButtons = []
        self.data = data.Data()
        self.main = main
        main.resize(600,600)
        self.mainframe = frame(main)
        self.mainframe.resize(main.size())
        self.tableframe = QFrame(self.mainframe)
        sizeWidth = self.main.size().width()/2
        sizeHeight = self.main.size().height()/2
        x = sizeWidth * 0.50
        y = sizeHeight * 0.50
        self.buttList = []
        self.data.validGeometry(sizeWidth,sizeHeight)  
        self.data.buttGeos()
        self.tableframe.setGeometry(x ,y ,sizeWidth,sizeHeight)
        self.tableframe.setStyleSheet("border: 2px solid gray;border-radius:25px")
        for i in self.data.validList:
            j = QPushButton(self.tableframe)
            j.setGeometry(QRect(i[0],i[1],i[2],i[3]))
            j.setStyleSheet("color: gray;font-size: 35px;border:none;")
            self.nodeButtons.append(j)
        self.setButtons()

    def setButtons(self):
        for i in self.nodeButtons:
            i.hide()
        for d in self.data.getGeosButt():
            b = self.data.getGeosButt().get(d)
            but = self.nodeButtons[d]
            but.setText(str(b[1]))
            but.setGeometry(QRect(b[0][0],b[0][1],b[0][2],b[0][3]))
            but.setStyleSheet("color: gray;font-size: 35px")
            but.show()







if __name__ == "__main__":
    app = QApplication()
    
    main = QMainWindow()
    i = ui(main)
    event = moveButtons(i)
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