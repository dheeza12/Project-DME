from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox, QMainWindow
import sys

sys.path.append('./packages')

from loadmenu_ui import *
from ui import PlayUi
from build_present import newTC


class Mainwindow(QMainWindow):

    def Mainmenuui(self, MainWindow1):
        MainWindow1.setObjectName("MainWindow")
        MainWindow1.setFixedSize(600, 800)
        self.centralwidget = QtWidgets.QWidget(MainWindow1)
        self.centralwidget.setObjectName("centralwidget")
        self.background = QtWidgets.QLabel(self.centralwidget)
        self.background.setGeometry(QtCore.QRect(0, 0, 600, 800))
        self.background.setText("")
        self.background.setPixmap(QtGui.QPixmap("resources/bg.jpg"))
        self.background.setScaledContents(False)
        self.background.setObjectName("background")
        self.story1 = QtWidgets.QPushButton(self.centralwidget)
        self.story1.setGeometry(QtCore.QRect(225, 200, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.story1.setFont(font)
        self.story1.setAutoFillBackground(False)
        self.story1.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                  "color: rgb(0, 0, 127);\n"
                                  "border-image: url(./resources/wimpykids.jpg);\n"
                                  "selection-background-color: rgb(85, 255, 255);")
        self.story1.setText("")
        self.story1.setIconSize(QtCore.QSize(100, 200))
        self.story1.setObjectName("story1")
        self.story1.clicked.connect(self.story1clicked)
        self.story2 = QtWidgets.QPushButton(self.centralwidget)
        self.story2.setGeometry(QtCore.QRect(225, 350, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.story2.setFont(font)
        self.story2.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                  "color: rgb(255, 255, 255);\n"
                                  "border-image: url(./resources/ghost2.png);\n"
                                  "selection-background-color: rgb(85, 255, 255);")
        self.story2.setText("")
        self.story2.setObjectName("story2")
        self.story3 = QtWidgets.QPushButton(self.centralwidget)
        self.story3.setGeometry(QtCore.QRect(225, 490, 150, 70))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.story3.setFont(font)
        self.story3.setStyleSheet("background-color: rgb(170, 255, 255);\n"
                                  "border-image: url(./resources/bg4.jpg);\n"
                                  "selection-background-color: rgb(85, 255, 255);")
        self.story3.setText("")
        self.story3.setObjectName("story3")
        self.trend_label = QtWidgets.QLabel(self.centralwidget)
        self.trend_label.setGeometry(QtCore.QRect(30, 120, 120, 20))
        self.trend_label.setObjectName("trend_label")
        self.quitbutton = QtWidgets.QPushButton(self.centralwidget)
        self.quitbutton.setGeometry(QtCore.QRect(450, 730, 150, 50))
        self.quitbutton.setStyleSheet("background-color: rgb(149, 197, 255);\n"
                                      "selection-background-color: rgb(175, 199, 255);")
        self.quitbutton.setObjectName("quitbutton")
        self.quitbutton.clicked.connect(self.quit_clicked)
        self.loadbutton = QtWidgets.QPushButton(self.centralwidget)
        self.loadbutton.setGeometry(QtCore.QRect(0, 730, 150, 50))
        self.loadbutton.setStyleSheet("background-color: rgb(149, 197, 255);\n"
                                      "selection-background-color: rgb(175, 199, 255);")
        self.loadbutton.setObjectName("loadbutton")
        self.loadbutton.clicked.connect(self.load_clicked)
        self.writebutton = QtWidgets.QPushButton(self.centralwidget)
        self.writebutton.setGeometry(QtCore.QRect(225, 730, 150, 50))
        self.writebutton.setStyleSheet("background-color: rgb(149, 197, 255);\n"
                                       "selection-background-color: rgb(175, 199, 255);")
        self.writebutton.setObjectName("writebutton")
        self.writebutton.clicked.connect(self.write_clicked)
        self.titlelabel = QtWidgets.QLabel(self.centralwidget)
        self.titlelabel.setGeometry(QtCore.QRect(120, 40, 391, 91))
        self.titlelabel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                      "font: 63 28pt \"Montserrat SemiBold\";")
        self.titlelabel.setObjectName("titlelabel")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 160, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("color: rgb(255, 255, 255);")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(210, 310, 191, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 460, 311, 21))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("color: rgb(255, 255, 255);")
        self.label_3.setObjectName("label_3")
        MainWindow1.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow1)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 600, 21))
        self.menubar.setObjectName("menubar")
        MainWindow1.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow1)
        self.statusbar.setObjectName("statusbar")
        MainWindow1.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow1)

        QtCore.QMetaObject.connectSlotsByName(MainWindow1)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Message simulator"))
        self.trend_label.setText(_translate("MainWindow", "Recommend Campaign"))
        self.quitbutton.setText(_translate("MainWindow", "Quit"))
        self.loadbutton.setText(_translate("MainWindow", "Load"))
        self.writebutton.setText(_translate("MainWindow", "Write"))
        self.titlelabel.setText(_translate("MainWindow", "Message Simulator"))
        self.label.setText(_translate("MainWindow", "Wimpy Kids"))
        self.label_2.setText(_translate("MainWindow", "Watch your back!"))
        self.label_3.setText(_translate("MainWindow", "Old house on the left street"))

    def load_clicked(self):
        self.openload = QtWidgets.QMainWindow()
        self.openload2 = Loadmenu()
        self.openload2.Loadui(self.openload)
        self.openload.show()

    def write_clicked(self):
        self.close()
        self.writeload = newTC({
            "text": "New_text",
            "main": False,
            "main_img": "img",
            "actor": "Character Name",
            "img": "img",
            "choice_text": "New_choice",
            "path": []
        })

    def story1clicked(self):
        self.close()
        self.story1load = PlayUi(".\saves\IamDME.json")

    def story2clicked(self):
        self.close()
        PlayUi()

    def story3clicked(self):
        self.close()
        PlayUi()

    def quit_clicked(self, event):
        close = QMessageBox()
        close.setWindowTitle("Please don't quit!!")
        close.setText("You sure to quit?")
        close.setStandardButtons(QMessageBox.Yes | QMessageBox.Cancel)
        close = close.exec()

        if close == QMessageBox.Yes:
            event.accept()
        else:
            pass


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow12 = QtWidgets.QMainWindow()
    ui = Mainwindow()
    ui.Mainmenuui(MainWindow12)
    MainWindow12.show()
    sys.exit(app.exec_())
