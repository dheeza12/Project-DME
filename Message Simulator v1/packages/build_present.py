import sys
import json
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QWidget, QFormLayout,
    QHBoxLayout, QLineEdit, QTextEdit, QComboBox, QPushButton,
    QCheckBox, QFileDialog, QAction, QLabel
)
from PyQt5.QtCore import QDir


static_nest = {
    "text": "",
    "main": False,
    "main_img": "",
    "actor": "",
    "img": "",
    "choice_text": "",

    "path": []
}


class newTC(QMainWindow):
    def __init__(self, nest):
        super().__init__()
        self.widget = QWidget()
        self.nest = nest
        self.cur_nest = self.nest
        self.cur_path_index = 0
        self.back = []

        self.init_ui()

    @staticmethod
    def new_line_edit(text="", min_w=100, min_h=10):
        a_line = QLineEdit(text)
        a_line.setMinimumWidth(min_w)
        a_line.setMinimumHeight(min_h)
        return a_line

    @staticmethod
    def new_text_edit(text="", min_w=100, min_h=100):
        t_line = QTextEdit(text)
        t_line.setMinimumWidth(min_w)
        t_line.setMinimumHeight(min_h)
        return t_line

    @staticmethod
    def new_combo_box(min_w=100, min_h=10):
        cbox = QComboBox()
        cbox.setMinimumWidth(min_w)
        cbox.setMinimumHeight(min_h)
        return cbox

    @staticmethod
    def new_button(text="", min_w=20, min_h=5):
        button = QPushButton(text)
        button.setMinimumWidth(min_w)
        button.setMinimumHeight(min_h)
        return button

    def new_present(self):
        self.nest = static_nest
        self.cur_nest = self.nest
        self.cur_path_index = 0

        self.choice_reset()
        self.check_box_reset()
        self.actor_reset()
        self.img_dir_reset()
        self.main_img_dir_reset()

    def json_out(self, file_name):
        f = open(file_name, 'r')
        x = json.load(f)
        f.close()
        self.nest = x
        self.cur_nest = self.nest
        self.cur_path_index = 0

        self.choice_reset()
        self.check_box_reset()
        self.actor_reset()
        self.img_dir_reset()
        self.main_img_dir_reset()

    @staticmethod
    def json_in(file_name, nest):
        f = open(file_name, 'w')
        json.dump(nest, f)
        f.close()

    def init_ui(self):
        f_layout = QFormLayout()

        # init menubar
        bar = self.menuBar()
        file_menu = bar.addMenu("File")
        file_menu.addAction("New")

        save_act = QAction("Save", self)
        save_act.setShortcut("Ctrl+S")
        file_menu.addAction(save_act)

        open_act = QAction("Open", self)
        open_act.setShortcut("Ctrl+O")
        file_menu.addAction(open_act)

        # init buttons combobox and lines
        choice_line_label = QLabel('Inside Choice:')
        choice_label = QLabel('A choice to next path:')
        self.choice = self.new_combo_box(200, 20)
        self.text_line = self.new_text_edit()
        self.text_line.setPlaceholderText(
            "This is the text that will "
            "appear when the player have "
            "chosen this path."
        )
        self.choice_line = self.new_line_edit(
            self.cur_nest['choice_text'], 150, 30
        )
        self.actor_line = self.new_line_edit()
        self.actor_line.setPlaceholderText('Character Name')
        self.main_img_dir_line = self.new_line_edit()
        self.main_img_dir_line.setPlaceholderText(
            'image dir for main character'
        )
        self.img_dir_line = self.new_line_edit()
        self.img_dir_line.setPlaceholderText(
            'image dir for a character'
        )
        self.main_chk_box = QCheckBox('Is Main?')

        self.browse_img_but = self.new_button('Browse')
        self.browse_main_img_but = self.new_button('Browse')
        self.change_choice_but = self.new_button(
            'Apply Change Choice Text(Apply everytime when make changes)'
        )
        self.next_but = self.new_button('Go in to this Choice')
        self.del_but = self.new_button('Delete Selected Choice')
        self.to_start_but = self.new_button('To Start')
        self.add_path_but = self.new_button('Add new Choice')
        back_but = self.new_button('Back')

        self.choice.setEditable(True)
        self.choice_line.setEnabled(False)

        # set formlayout
        f_layout.addRow(choice_line_label, self.choice_line)

        f_layout.addRow(self.actor_line)
        hbox = QHBoxLayout()
        hbox.addWidget(self.main_chk_box)
        hbox.addWidget(self.browse_main_img_but)
        hbox.addWidget(self.main_img_dir_line)
        hbox.addWidget(self.browse_img_but)
        hbox.addWidget(self.img_dir_line)
        f_layout.addRow(hbox)

        f_layout.addRow(choice_label, self.choice)
        f_layout.addRow(self.change_choice_but)

        hbox = QHBoxLayout()
        hbox.addWidget(self.next_but)
        hbox.addWidget(back_but)
        hbox.addWidget(self.del_but)
        hbox.addWidget(self.to_start_but)
        hbox.addWidget(self.add_path_but)
        f_layout.addRow(hbox)
        f_layout.addRow(self.text_line)

        self.change_choice_but.setStyleSheet(
            "background-color: lightgreen"
        )

        # connect functions
        # self.text_line.textChanged.connect(self.change_choice_text)
        self.choice.currentIndexChanged.connect(self.change_choice)
        self.change_choice_but.clicked.connect(self.change_choice_text)

        self.del_but.clicked.connect(self.del_path)
        self.next_but.clicked.connect(self.next_path)
        self.to_start_but.clicked.connect(self.to_start)
        self.add_path_but.clicked.connect(self.add_path)
        self.browse_img_but.clicked.connect(self.get_img)
        self.browse_main_img_but.clicked.connect(self.get_main_img)
        back_but.clicked.connect(self.back_path)

        save_act.triggered.connect(self.write_present)
        open_act.triggered.connect(self.load_present)

        # run functions once
        self.check_box_reset()
        self.actor_reset()
        self.choice_reset()
        self.main_img_dir_reset()
        self.img_dir_reset()

        self.widget.setLayout(f_layout)
        self.setCentralWidget(self.widget)
        self.resize(600, 800)
        self.setWindowTitle('Create Present')
        self.show()

    def check_box_reset(self):
        if self.cur_nest['path']:
            self.main_chk_box.setEnabled(True)
            self.actor_line.setEnabled(True)
            self.text_line.setEnabled(True)
            self.choice.setEnabled(True)
            self.del_but.setEnabled(True)
            self.next_but.setEnabled(True)
            self.to_start_but.setEnabled(True)
            self.browse_img_but.setEnabled(True)
            self.browse_main_img_but.setEnabled(True)
            self.change_choice_but.setEnabled(True)
            self.add_path_but.setStyleSheet(
                "background-color: white"
            )
            index = self.choice.currentIndex()
            if 'main' in self.cur_nest['path'][index]:
                self.main_chk_box.setChecked(
                    bool(self.cur_nest['path'][index]['main'])
                )
            else:
                self.main_chk_box.setChecked(False)
        else:
            self.main_chk_box.setEnabled(False)
            self.actor_line.setEnabled(False)
            self.text_line.setEnabled(False)
            self.choice.setEnabled(False)
            self.del_but.setEnabled(False)
            self.next_but.setEnabled(False)
            self.to_start_but.setEnabled(False)
            self.browse_img_but.setEnabled(False)
            self.browse_main_img_but.setEnabled(False)
            self.change_choice_but.setEnabled(False)
            self.add_path_but.setStyleSheet(
                "background-color: lightgreen"
            )

    def actor_reset(self):
        if self.cur_nest['path']:
            index = self.choice.currentIndex()
            if 'actor' in self.cur_nest['path'][index]:
                self.actor_line.setText(
                    self.cur_nest['path'][index]['actor']
                )
            else:
                self.actor_line.setText(
                    'Actor'
                )

    def main_img_dir_reset(self):
        if self.cur_nest['path']:
            self.main_img_dir_line.setEnabled(True)
            index = self.choice.currentIndex()
            if 'main_img' in self.cur_nest['path'][index]:
                self.main_img_dir_line.setText(
                    self.cur_nest['path'][index]['main_img']
                )
            else:
                self.main_img_dir_line.setText(
                    'img'
                )
        else:
            self.main_img_dir_line.setEnabled(False)

    def img_dir_reset(self):
        if self.cur_nest['path']:
            self.img_dir_line.setEnabled(True)
            index = self.choice.currentIndex()
            if 'main_img' in self.cur_nest['path'][index]:
                self.img_dir_line.setText(
                    self.cur_nest['path'][index]['main_img']
                )
            else:
                self.img_dir_line.setText(
                    'img'
                )
        else:
            self.img_dir_line.setEnabled(False)

    def choice_reset(self):
        self.choice.clear()
        for i in self.cur_nest['path']:
            self.choice.addItem(i['choice_text'])

    def change_choice(self):
        sender = self.sender()
        self.text_line.setPlaceholderText(
            "This is the text that will "
            "appear when the player have "
            "chosen this path({})".format(self.choice.currentText())
        )
        index = sender.currentIndex()
        self.cur_path_index = index
        if self.cur_nest['path']:
            self.text_line.setText(self.cur_nest['path'][index]['text'])
        else:
            self.text_line.clear()
        self.check_box_reset()
        self.actor_reset()
        self.img_dir_reset()
        self.main_img_dir_reset()

    def change_choice_text(self):
        self.text_line.setPlaceholderText(
            "This is the text that will "
            "appear when the player have "
            "chosen this path({})".format(self.choice.currentText())
        )
        index = self.choice.currentIndex()
        self.choice.setItemText(
            index, self.choice.currentText()
        )
        if self.cur_nest['path']:
            self.cur_nest['path'][index]['main'] = \
                self.main_chk_box.isChecked()
            self.cur_nest['path'][index]['main_img'] = \
                self.main_img_dir_line.text()
            self.cur_nest['path'][index]['img'] = \
                self.img_dir_line.text()
            self.cur_nest['path'][index]['actor'] = \
                self.actor_line.text()
            self.cur_nest['path'][index]['choice_text'] = \
                self.choice.currentText()
            self.cur_nest['path'][index]['text'] = \
                self.text_line.toPlainText()
        else:
            print('Add path first!')

    def next_path(self):
        if self.cur_nest['path']:
            self.back.append(self.cur_path_index)
            self.cur_nest = self.cur_nest['path'][self.cur_path_index]
            print(self.cur_nest['choice_text'])
            self.choice_reset()
            self.check_box_reset()
            self.actor_reset()
            self.img_dir_reset()
            self.main_img_dir_reset()
            self.choice_line.setText(self.cur_nest['choice_text'])

    def to_start(self):
        self.cur_nest = self.nest
        # self.choice_line.clear()
        self.check_box_reset()
        self.actor_reset()
        self.img_dir_reset()
        self.main_img_dir_reset()
        self.choice_reset()

    def add_path(self):
        new_nest = {
            "text": "",
            "main": False,
            "main_img": "",
            "actor": "",
            "img": "",
            "choice_text": "",

            "path": []
        }
        self.cur_nest['path'].append(new_nest)
        self.choice_reset()
        self.img_dir_reset()
        self.main_img_dir_reset()

    def del_path(self):
        if self.cur_nest['path']:
            index = self.choice.currentIndex()
            self.cur_nest['path'].pop(index)
            self.choice_reset()

    def back_path(self):
        if self.back:
            self.cur_nest = self.nest
            for n in self.back:
                self.cur_nest = self.cur_nest['path'][n]
            self.check_box_reset()
            self.actor_reset()
            self.img_dir_reset()
            self.main_img_dir_reset()
            self.choice_reset()
            self.back.pop()

    def get_img(self):
        dir_path = QFileDialog.getOpenFileName(
            self, "Choose Image Directory", "D:\\"
        )
        if dir_path[0]:
            self.img_dir_line.setText(dir_path[0])
            print(dir_path)

    def get_main_img(self):
        dir_path = QFileDialog.getOpenFileName(
            self, "Choose Image Directory", "D:\\"
        )
        if dir_path[0]:
            self.main_img_dir_line.setText(dir_path[0])
            print(dir_path)

    def write_present(self):
        dir_now = QDir()
        dir_now = QDir(dir_now.currentPath())
        dir_now.cdUp()
        dir_path = dir_now.path()
        print(dir_path)
        dir_saves = dir_now.path() + "/saves"
        dir_path = QFileDialog.getSaveFileName(
            self, "Choose Image Directory", dir_saves, "Json files (*.json)"
        )
        if dir_path[0]:
            self.json_in(dir_path[0], self.nest)
            print(dir_path)

    def load_present(self):
        dir_now = QDir()
        dir_now = QDir(dir_now.currentPath())
        dir_now.cdUp()
        dir_path = dir_now.path()
        print(dir_path)
        dir_saves = dir_now.path() + "/saves"
        dir_path = QFileDialog.getOpenFileName(
            self, "Choose Image Directory", dir_saves, "Json files (*.json)"
        )
        if dir_path[0]:
            self.json_out(dir_path[0])
            print(dir_path)


def main():
    app = QApplication(sys.argv)
    tc = newTC(static_nest)
    print(tc.isActiveWindow())
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
