from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMainWindow
from mainmenu_ui import *
import sys



class Loadmenu(QMainWindow):
    def Loadui(self, MainWindow2):
        MainWindow2.setObjectName("Load Menu")
        MainWindow2.setFixedSize(600, 800)
        MainWindow2.setAutoFillBackground(True)
        MainWindow2.setStyleSheet("")
        self.centralwidget = QtWidgets.QWidget(MainWindow2)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(-60, -110, 700, 900))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("resources/bg3.jpg"))
        self.label.setObjectName("label")
        self.loadnovel = QtWidgets.QLabel(self.centralwidget)
        self.loadnovel.setGeometry(QtCore.QRect(210, 30, 211, 101))
        font = QtGui.QFont()
        font.setPointSize(28)
        self.loadnovel.setFont(font)
        self.loadnovel.setStyleSheet("color: rgb(255, 255, 255);")
        self.loadnovel.setObjectName("loadnovel")
        self.loadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loadbutton.setGeometry(QtCore.QRect(200, 170, 220, 100))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.loadbutton.setFont(font)
        self.loadbutton.setObjectName("loadbutton")
        self.loadbutton.clicked.connect(self.loadclicked)
        font = QtGui.QFont()
        font.setPointSize(12)
        MainWindow2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow2)
        self.statusbar.setObjectName("statusbar")
        MainWindow2.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow2)
        QtCore.QMetaObject.connectSlotsByName(MainWindow2)

    def retranslateUi(self, MainWindow2):
        _translate = QtCore.QCoreApplication.translate
        MainWindow2.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.loadnovel.setText(_translate("MainWindow", "Load Novel"))
        self.loadbutton.setText(_translate("MainWindow", "LOAD"))

    def loadclicked(self):
        openfile = QFileDialog.getOpenFileName(self, "Choose file to read", "Enter name", "JSON file (*.json)")
        if openfile[0]:
            self.open = PlayUi(openfile[0])

    def mainclicked(self):
        pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow22 = QtWidgets.QMainWindow()
    ui2 = Loadmenu()
    ui2.Loadui(MainWindow22)
    MainWindow22.show()
    sys.exit(app.exec_())
