import json


class TextAndChoice:
    def __init__(self, text="Welcome to the start", main=False, main_img=None, actor=None, img=None, choice_text=None, back=None):
        self.text = text
        self.main = main
        self.main_img = main_img
        self.actor = actor
        self.img = img
        self.choice_text = choice_text

        self.back = back
        self.path = []
    """ 
        Encode to dict for JSON dump
    """
    def encode(self):
        dict_ = {}
        path = []
        dict_['text'] = self.text
        dict_['main'] = self.main
        dict_['main_img'] = self.main_img
        dict_['actor'] = self.actor
        dict_['img'] = self.img
        dict_['choice_text'] = self.choice_text
        if len(self) > 0:
            path.extend([x.encode() for x in self.path])
        dict_['path'] = path
        return dict_
    """
        Decode from dict to construct the TextAndChoice Obj
    """
    @staticmethod
    def decode(dict_):
        text = dict_['text']
        actor = dict_['actor']
        img = dict_['img']
        choice_text = dict_['choice_text']
        main = None
        main_img = None
        if 'main' in dict_:
            main = dict_['main']
        if 'main_img' in dict_:
            main_img = dict_['main_img']
        root_create = TextAndChoice(text=text,actor=actor, main=main, main_img=main_img, img=img, choice_text=choice_text)
        if len(dict_['path']) > 0:
            for x in dict_['path']:
                root_create.add_path(root_create.decode(x))
        return root_create

    def selector(self):
        selector = input(": ")
        selector = int(selector)
        return self.path[selector - 1]

    # set text for the current node
    def set_text(self):
        new_text = input("Enter new text: ")
        self.text = new_text

    # set choice for the numbered path
    def set_choice(self):
        if self.is_end():
            print("No choice to change")
        else:
            print("Which path?")
            self.show_choice()
            path = self.selector()
            new_text = input("Enter new choice text: ")
            path.choice_text = new_text

    def is_end(self):
        if len(self) < 1:
            return True
        return False

    def add_path(self, node):
        node.back = self
        self.path.append(node)

    def remove(self):
        if self.is_end():
            print("No path available")
        elif len(self) >= 1:
            print("Which path?")
            self.show_choice()
            to_del = self.selector()
            for x in self.path:
                if to_del.text == x.text:
                    self.path.remove(x)

    def to_start(self):
        start = self
        while start.back:
            start = start.back
        return start

    def next_path(self):
        if self.is_end():
            print("No path available")
            return self
        elif len(self) >= 1:
            print("Which path?")
            self.show_choice()
            return self.selector()

    def show_choice(self):
        for n, choice in enumerate(self.path):
            print(f'{n + 1}. {choice.choice_text}')

    def save_present(self):
        x = self.to_start()
        x = x.encode()
        file_name = input("file name to save: ")
        f = open(file_name + ".json", "w")
        json.dump(x, f)
        f.close()
        self.menu()

    @staticmethod
    def load_present():
        file_name = input("file name to load: ")
        f = open(file_name + ".json", "r")
        x = json.load(f)
        f.close()
        read = TextAndChoice.decode(x)
        return read

    """
        Menu-Start
    """

    def menu_choice(self, selector):
        if selector == 'a':
            self.set_text()
        elif selector == 'b':
            self.set_choice()
        elif selector == 'c':
            choice = input("Choice text to connect to the new path: ")
            text = input("Text to show after choosing: ")
            if choice == '':
                choice = None
            add = TextAndChoice(text=text, choice_text=choice)
            self.add_path(add)
        elif selector == 'd':
            self.remove()

        elif selector == 'e':
            return self.next_path()
        elif selector == 'f':
            # return to the start node and call play()
            to_start = self.to_start()
            to_start.play()
        elif selector == 'g':
            if self.back:
                return self.back
            else:
                print("This is the start")
        elif selector == 'h':
            return self.to_start()
        elif selector == 's':
            return self.save_present()
        elif selector == 'l':
            return self.load_present()
        elif selector == 'q':
            return
        return self

    def menu(self):
        print("{:=^64s}".format(""))
        print(f'The text is: {self}')
        print("The paths currently are:")
        self.show_choice()
        print()
        print("""What do you want to do?
            a. Change text
            b. Change/Add choice text for the path
            c. Add new path
            d. Delete path
            e. Next path
            f. Play testing
            g. Back
            h. Go to start
            s. save present
            l. load present
            q. Quit
            """)
        q = self.menu_choice(input(": "))
        if q is None:
            pass
        else:
            q.menu()

    """

        Menu-End

    """

    def play(self):
        print(self)
        if not self.is_end():
            selector = None
            if len(self) > 1:
                self.show_choice()
                selector = input("Input: ")
            if selector == '' or selector is None:
                selector = 1
            self.path[int(selector) - 1].play()

    def __str__(self):
        return self.text

    def __len__(self):
        return len(self.path)


if __name__ == '__main__':
    root = TextAndChoice()
    root.menu()