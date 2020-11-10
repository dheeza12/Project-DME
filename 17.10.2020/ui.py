import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import TextAndChoice


class PlayUi(QScrollArea):
    def __init__(self, json_file):
        super().__init__()
        self.json_file = json_file
        mainLayout = QVBoxLayout()
        mainLayout.setAlignment(Qt.AlignTop)
        self.setWidgetResizable(True)
        self.setLayout(mainLayout)
        self.setCenter()
        self.setWindowTitle("Play demo")
        self.show()

        # set up for the image and line label
        """img = QLabel()
        line = QLabel("Best waifu in the world")
        pixMap = QPixmap('2020105104225.png')
        smaller_pixMap = pixMap.scaled(64, 64, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        img.setPixmap(smaller_pixMap)
        line.setMinimumHeight(smaller_pixMap.height())
        hbox = QHBoxLayout()
        hbox.addWidget(img)
        hbox.addWidget(line)
        hbox.setAlignment(Qt.AlignLeft)
        mainLayout.addLayout(hbox)"""


    @staticmethod
    def loadStory(json_loaded):
        pass

    def setCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


if __name__ == '__main__':
    import json
    file = open('IamDME.json', 'r')
    file = json.load(file)
    decoded = TextAndChoice.decode(file)
    app = QApplication(sys.argv)
    play = PlayUi(decoded)
    sys.exit(app.exec_())
