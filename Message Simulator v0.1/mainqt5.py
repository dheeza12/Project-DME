import sys
from TC import TextAndChoice
from PyQt5.QtWidgets import (
    QApplication, QLineEdit, QComboBox,
    QWidget, QFormLayout, QPushButton
)


class CreateMenu(QWidget):
    def __init__(self):
        super().__init__()
        tc = TextAndChoice()
        self.init_ui(tc)

    def init_ui(self, tc):
        f_layout = QFormLayout()

        self.c_box = QComboBox()
        self.c_box.currentTextChanged.connect(self.cbox_change)
        f_layout.addRow(self.c_box)

        self.choice_line = QLineEdit()
        self.text_line = QLineEdit()
        self.cur_choice_line = QLineEdit()
        self.cur_choice_line.setEnabled(False)

        self.apply_but = QPushButton('Apply change')
        self.add_but = QPushButton('add path')
        self.back_but = QPushButton('Back')
        self.to_start_but = QPushButton('Go to Start')
        self.next_path_but = QPushButton('Go into Path')

        f_layout.addRow(self.cur_choice_line)
        f_layout.addRow(self.choice_line, self.text_line)
        f_layout.addRow(self.next_path_but)
        f_layout.addRow(self.back_but, self.to_start_but)
        f_layout.addRow(self.apply_but, self.add_but)

        self.setLayout(f_layout)
        self.show()
        self.access_node(tc)

    def access_node(self, node):
        self.c_box.clear()
        self.choice_line.setText('')
        self.cur_choice_line.setText(node.choice_text)
        print(node.choice_text)
        self.text_line.setText(node.text)
        if not node.is_end():
            for i in node.path:
                self.c_box.addItem(i.choice_text)
        self.c_box.currentIndexChanged.connect(self.cbox_change)

        self.apply_but.clicked.connect(lambda x, y=node: self.apply_change(y))
        self.add_but.clicked.connect(lambda x, y=node: self.add_choice(y))
        self.next_path_but.clicked.connect(
            lambda x, y=node: self.next_path_line(y)
        )
        self.back_but.clicked.connect(lambda x, y=node: self.back_node(y))
        self.to_start_but.clicked.connect(lambda x, y=node: self.to_start(y))

    def cbox_change(self):
        self.choice_line.setText(str(self.c_box.currentText()))

    def apply_change(self, node):
        i = self.c_box.currentIndex()
        node.path[i].choice_text = self.choice_line.text()
        node.text = self.text_line.text()
        self.c_box.setItemText(i, node.path[i].choice_text)

    def add_choice(self, node):
        add = TextAndChoice(text=None, choice_text=None)
        node.add_path(add)
        self.c_box.addItem(add.choice_text)

    def next_path_line(self, node):
        if node.is_end():
            print("No path available")
        else:
            self.access_node(node.path[self.c_box.currentIndex()])

    def back_node(self, node):
        self.access_node(node.back)

    def to_start(self, node):
        start = node
        while start.back:
            start = start.back
        self.access_node(start)


def main():
    app = QApplication(sys.argv)
    create = CreateMenu()
    print(create.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
