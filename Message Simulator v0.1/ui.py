import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from main import TextAndChoice
import json


class PlayUi(QMainWindow):
    def __init__(self, root_directory):
        super().__init__()
        file = open(root_directory, 'r')
        file = json.load(file)
        root = TextAndChoice.decode(file)
        self.root = root

        self.show()
        self.mainWidget = QWidget()
        self.box = QVBoxLayout()
        self.box.setSpacing(12)
        self.box.setAlignment(Qt.AlignTop)
        self.mainWidget.setLayout(self.box)
        self.mainWidget.setObjectName("Background")

        self.scroll_area = QScrollArea()
        self.scroll_area.setWidgetResizable(True)
        self.scroll_area.setWidget(self.mainWidget)
        self.scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll_area.setFont(QFont('Arial', 18))

        self.statusBar().showMessage('Message in statusbar.')

        self.setCentralWidget(self.scroll_area)
        self.setFixedSize(600, 800)
        self.setCenter()
        self.setWindowTitle(root_directory.split('.')[0])
        self.setStyleSheet("""  
        QWidget#Background {background-color: Lightcyan}
        
        QLabel#Actor { font: bold; }
        
        QLabel#Chat  { background-color: snow; color: black; font-size: 16px;
            border-style: ridge; border-width: 5px; border-color: Mintcream; border-radius: 10px;
            padding: 6px; padding-right: 12px; padding-left: 12px;
            }
        
        QLabel#Choice { background-color: Deepskyblue; 
            font-size: 18px; color: White; border-radius: 5px;
            border-style: solid; border-width: 4px; border-color: deepskyblue;
            min-width: 377; min-height: 64; padding-left: 20px; padding-right: 20px; padding-top: 10px;
            padding-bottom: 5px;
            } 
                                                    
        QPushButton#Choice { background-color: Azure; font-size: 16px; font-family: Arial; font: bold; 
            border-style: outset; border-width: 6px; border-color: Aqua; border-radius: 15px;
            min-width: 240px; min-height: 32px;
            }
        
        QPushButton#Choice:hover:!pressed { background-color: Snow; border-color: Chartreuse;
            }
                            """)

        self.play(self.root)

    def play(self, root):
        self.display_text(root)
        if not root.is_end():
            if len(root) > 1:
                hbox = QHBoxLayout()
                vbox = QVBoxLayout()
                vbox.setAlignment(Qt.AlignCenter)

                for i, choice in enumerate(root.path):
                    widget = QWidget()
                    vbox_sub = QVBoxLayout()
                    vbox_sub.setAlignment(Qt.AlignCenter)
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
            pass

        """ STILL NEED TO ADD ACTION AFTER GAME ENDs"""

    def display_text(self, root, text=True):
        hbox = QHBoxLayout()
        vbox = QVBoxLayout()
        if root.actor:  # ADD NAME IF EXISTED
            actor_label = QLabel(root.actor + ':')
            actor_label.setObjectName('Actor')
            vbox.addWidget(actor_label)
            if root.main:
                actor_label.setAlignment(Qt.AlignRight)
        line_label = QLabel(root.choice_text)
        if text:
            line_label = QLabel(str(root))
        line_label.setObjectName('Chat')
        line_label.setWordWrap(True)
        vbox.addWidget(line_label)

        if root.img:
            pix_map = QPixmap(root.img)
        else:
            pix_map = QPixmap('Content/default_avatar.png')
        pix_map = pix_map.scaled(64, 64, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        pix_label = QLabel()
        pix_label.setPixmap(pix_map)
        pix_label.setObjectName('Pixmap')

        if root.main_img:
            main_pix_map = QPixmap(root.main_img)
        else:
            main_pix_map = QPixmap('Content/default_avatar.png')
        main_pix_map = main_pix_map.scaled(64, 64, Qt.IgnoreAspectRatio, Qt.FastTransformation)
        main_pix_label = QLabel()
        main_pix_label.setPixmap(main_pix_map)
        main_pix_label.setObjectName('Pixmap')

        if root.main or text is False:
            hbox.setAlignment(Qt.AlignRight)
            hbox.addLayout(vbox)
            hbox.addWidget(main_pix_label)
        else:
            hbox.setAlignment(Qt.AlignLeft)
            hbox.addWidget(pix_label)
            hbox.addLayout(vbox)
        self.box.addLayout(hbox)

    def choose(self, root, arg):
        clearLayout(self.box.takeAt(self.box.count() - 1))
        self.display_text(root.path[arg], False)
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

    app = QApplication(sys.argv)
    play = PlayUi('IamDME.json')
    sys.exit(app.exec_())
