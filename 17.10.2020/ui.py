import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import TextAndChoice


class PlayUi(QScrollArea):
    def __init__(self):
        super().__init__()
        mainLayout = QVBoxLayout()

        # set up the image and line label
        """img = QLabel()
        line = QLabel("Best waifu in the world")
        pixMap = QPixmap('2020111222132.png')
        smaller_pixMap = pixMap.scaled(64, 64, Qt.KeepAspectRatio, Qt.FastTransformation)
        img.setPixmap(smaller_pixMap)
        line.setMinimumHeight(smaller_pixMap.height())"""


        mainLayout.setAlignment(Qt.AlignTop)
        self.setWidgetResizable(True)
        self.setLayout(mainLayout)
        self.setCenter()
        self.setWindowTitle("Play demo")

        self.show()
    @staticmethod
    def loadStory(fileName):
        pass

    def setCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    play = PlayUi()
    sys.exit(app.exec_())
