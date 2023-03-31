from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Frame(QWidget):
    def __init__(self):
        super(QWidget, self).__init__()
        self.grid = QGridLayout()

        self.grid.setColumnStretch(0, 3)
        self.grid.setColumnStretch(1, 9)

        self.functions = QGridLayout()
        self.functions.setColumnStretch(0, 1)
        self.functions.setColumnStretch(1, 1)
        self.functions.setColumnStretch(2, 1)

        self.openFile = QDialogButtonBox(QDialogButtonBox.Open)
        self.openFile.setCenterButtons(True)

        self.btnReg = QPushButton("Regression", self)
        self.btnReg.setAccessibleName("Regression")
        self.btnReg.setObjectName("Reg")
        self.CNN = QPushButton("CNN", self)
        self.CNN.setObjectName("CNN")

        self.functions.addWidget(self.openFile, 0, 0)
        self.functions.addWidget(self.btnReg, 1, 0)
        self.functions.addWidget(self.CNN, 1, 1)
        self.grid.addLayout(self.functions, 0, 0)

        self.frame = QVBoxLayout()
        self.apply = QPushButton("Apply", self)
        self.frame.addWidget(self.apply)
        self.grid.addLayout(self.frame, 0, 1)
        self.setLayout(self.grid)

class Example(QMainWindow):

    def __init__(self):
        super(Example, self).__init__()

        self.initUI()

    def initUI(self):
        self.setAcceptDrops(True)
        self.booling = False

        self.width = self.frameGeometry().width()
        self.height = self.frameGeometry().height()
        tabs = QTabWidget()
        tabs.setTabPosition(QTabWidget.West)
        tabs.setMovable(True)

        self.grid=Frame()
        self.functions=self.grid.functions
        self.frame=self.grid.frame

        tabs.addTab(self.grid,"Tab "+str(tabs.count()+1))
        self.setCentralWidget(tabs)

        self.showMaximized()

    def mouseMoveEvent(self, e):
        if e.buttons() == Qt.LeftButton:
            if self.booling==False:
                self.xpos=e.pos().x()
                if self.xpos<500:
                    self.begpos=e.pos().y()

                    self.booling = True
                    drag = QDrag(self)
                    mime = QMimeData()
                    drag.setMimeData(mime)
                    drag.exec_(Qt.MoveAction)
                else:
                    self.booling=False
            else:
                
                    self.booling = False

    def dragEnterEvent(self, e):
        e.accept()

    def dropEvent(self, e):
        pos = e.pos()
        widget = e.source()

        point=widget.pos()

        w=point.x()

        w2=w+(self.width//2)

        for n in range(self.functions.count()):
            wid = self.functions.itemAt(n).widget()
            y=wid.y()
            half=self.width//3
            if n==self.functions.count()-1:

                if w == -1 and pos.x() > w2 and y + 23 >= self.begpos and y - 23 <= self.begpos and self.booling == True:
                    e.accept()
                    self.booling = False
                    self.begpos = 0
                    min = self.frame.count()
                    self.frame.insertWidget(min - 1, wid)
                    break

            else:

                if w==-1 and pos.x()>w2 and y+23>=self.begpos and y-23<=self.begpos and self.booling==True:

                    if self.functions.itemAt(n+1).widget().y()<y+46 and self.functions.itemAt(n+1).widget().y()>y-46:
                        if wid.x()+half>=self.xpos:
                            e.accept()
                            self.booling = False
                            self.begpos = 0
                            min = self.frame.count()
                            self.frame.insertWidget(min - 1, wid)
                            break
                        else:
                            e.accept()
                            wid2 = self.functions.itemAt(n+1).widget()
                            self.booling = False
                            self.begpos = 0
                            min = self.frame.count()
                            self.frame.insertWidget(min - 1, wid2)
                            break
                    else:
                        e.accept()
                        self.booling = False
                        self.begpos = 0
                        min = self.frame.count()
                        self.frame.insertWidget(min - 1, wid)
                        break









app = QApplication([])
w = Example()
app.exec_()
