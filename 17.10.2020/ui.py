import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import TextAndChoice


class PlayUi(QScrollArea):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.mainLayout = QVBoxLayout()
        self.mainLayout.setAlignment(Qt.AlignTop)
        self.setWidgetResizable(True)
        self.setLayout(self.mainLayout)
        self.setCenter()
        self.setWindowTitle("Play demo")
        self.show()
        self.play(self.root)
        # set up for the image and line label
        """img = QLabel()
        actor_label = QLabel("Papika")
        line_label = QLabel("Best waifu in the world")
        pixMap = QPixmap('2020105104225.png')
        smaller_pixMap = pixMap.scaled(64, 64, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        img.setPixmap(smaller_pixMap)
        line.setMinimumHeight(smaller_pixMap.height())
        hbox = QHBoxLayout()
        hbox.addWidget(img)
        hbox.addWidget(line)
        hbox.setAlignment(Qt.AlignLeft)
        self.mainLayout.addLayout(hbox)"""

    def play(self, root):
        root = self.root

        hbox = QHBoxLayout()
        vbox = QVBoxLayout()

        if root.actor:
            actor_label = QLabel(root.actor+':')
            vbox.addWidget(actor_label)
        line_label = QLabel(str(root))
        vbox.addWidget(line_label)

        if root.img:
            pix_label = QLabel()
            pixMap = QPixmap(root.img)
            pixMap = pixMap.scaled(64, 64, Qt.IgnoreAspectRatio, Qt.FastTransformation)
            pix_label.setPixmap(pixMap)
        else:
            pix_label = QLabel()
            pixMap = QPixmap('default_avatar.png')
            pixMap = pixMap.scaled(64, 64, Qt.IgnoreAspectRatio, Qt.FastTransformation)
            pix_label.setPixmap(pixMap)
        if root.actor == 'main':
            hbox.setAlignment(Qt.AlignRight)
            hbox.addLayout(vbox)
            hbox.addWidget(pix_label)
        else:
            hbox.setAlignment(Qt.AlignLeft)
            hbox.addWidget(pix_label)
            hbox.addLayout(vbox)

        if not root.is_end():
            if len(root) > 1:
                vbox = QVBoxLayout()
                for i, choice in enumerate(root.path):
                    button = QPushButton(choice.choice_text)
                    root = button.clicked.connect(lambda i, root: root.path[i])
                    vbox.addWidget(button)

        self.mainLayout.addLayout(hbox)

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
