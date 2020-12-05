import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import TextAndChoice


class PlayUi(QScrollArea):
    def __init__(self, root):
        super().__init__()
        self.root = root
        self.mainWidget = QWidget()

        self.box = QVBoxLayout()
        self.box.setAlignment(Qt.AlignTop)
        self.mainWidget.setLayout(self.box)
        self.mainWidget.setFont(QFont('Arial', 12))

        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setFixedSize(600, 800)
        self.setWidgetResizable(True)
        self.setCenter()
        self.setWindowTitle("Play demo")
        self.setWidget(self.mainWidget)
        self.setStyleSheet("""  QLabel#Choice { background-color: Turquoise; padding: 10px;
                                    font-size: 16px; font-family: Arial;} 
                                
                                QLabel#Label  { background-color: Mintcream; color: black;
                                    border-style: ridge; border-width: 5px; border-color: snow; border-radius: 10px;
                                    padding: 6px; font-size: 16px; font-family: Arial}
                                
                                QPushButton#Choice { font-size: 16px; font-family: Arial; font: bold;
                                    }""")
        self.show()
        self.play(self.root)

    def play(self, root):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        if root.actor:              # ADD NAME IF EXISTED
            actor_label = QLabel(root.actor+':')
            vbox.addWidget(actor_label)
        line_label = QLabel(str(root))
        line_label.setObjectName('Label')
        line_label.setWordWrap(True)

        vbox.addWidget(line_label)

        pix_label = QLabel()
        if root.img:
            pixMap = QPixmap(root.img)
        else:
            pixMap = QPixmap('default_avatar.png')
        pixMap = pixMap.scaled(64, 64, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        pix_label.setPixmap(pixMap)
        pix_label.setObjectName('Pixmap')

        if root.main:
            hbox.setAlignment(Qt.AlignRight)
            hbox.addLayout(vbox)
            hbox.addWidget(pix_label)
        else:
            hbox.setAlignment(Qt.AlignLeft)
            hbox.addWidget(pix_label)
            hbox.addLayout(vbox)

        self.box.addLayout(hbox)

        if not root.is_end():
            if len(root) > 1:
                hbox = QHBoxLayout()
                vbox = QVBoxLayout()

                for i, choice in enumerate(root.path):
                    widget = QWidget()
                    vbox_sub = QVBoxLayout()
                    widget.setLayout(vbox_sub)

                    btnLabel = QLabel(choice.choice_text)
                    btnLabel.setObjectName('Choice')
                    btnLabel.setAlignment(Qt.AlignCenter)
                    btnLabel.setWordWrap(True)

                    butt = QPushButton("Choose")
                    butt.setObjectName('Choice')
                    butt.clicked.connect(lambda ignore, current_root=root, arg=i: self.choose(current_root, arg))

                    vbox.addWidget(btnLabel)
                    vbox.addWidget(widget)
                    vbox_sub.addWidget(butt)
                hbox.addLayout(vbox)


                self.box.addLayout(hbox)

            elif len(root) != 0:
                self.play(root.path[0])
        else:
            pass            # END

        """ STILL NEED TO ADD ACTION AFTER GAME ENDs"""

    def choose(self, root, arg):
        clearLayout(self.box.takeAt(self.box.count() - 1))
        self.play(root.path[arg])

    def setCenter(self):
        qtRectangle = self.frameGeometry()
        centerPoint = QDesktopWidget().availableGeometry().center()
        qtRectangle.moveCenter(centerPoint)
        self.move(qtRectangle.topLeft())


def clearLayout(layout):    # http://josbalcaen.com/maya-python-pyqt-delete-all-widgets-in-a-layout/
    while layout.count():   # special thank!
        child = layout.takeAt(0)
        if child.widget() is not None:
            child.widget().deleteLater()
        elif child.layout() is not None:
            clearLayout(child.layout())


if __name__ == '__main__':
    import json
    file = open('IamDME.json', 'r')
    file = json.load(file)
    decoded = TextAndChoice.decode(file)
    app = QApplication(sys.argv)
    play = PlayUi(decoded)
    sys.exit(app.exec_())
