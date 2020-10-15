# Tree Node


class TextAndChoice:
    def __init__(self, text="Welcome to the start", choice_text=None, back=None):
        self.text = text
        self.back = back
        self.choice_text = choice_text
        self.path = []

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
        if self.isEnd():
            print("No choice to change")
        else:
            print("Which path?")
            self.show_choice()
            path = self.selector()
            new_text = input("Enter new choice text: ")
            path.choice_text = new_text

    def isEnd(self):
        if len(self) < 1:
            return True
        return False

    def add_path(self, text, choice_text=None):
        path = TextAndChoice(text, choice_text)
        path.back = self
        self.path.append(path)

    def remove(self):
        if self.isEnd():
            print("No path available")
        elif len(self) >= 1:
            print("Which path?")
            self.show_choice()
            to_del = self.selector()
            for x in self.path:
                if to_del.text == x.text:
                    self.path.remove(x)

    def to_start(self):
        to_start = self
        while to_start.back:
            to_start = self.back
        return to_start

    def next_path(self):
        if self.isEnd():
            print("No path available")
        elif len(self) > 1:
            print("Which path?")
            self.show_choice()
            return self.selector()

    def show_choice(self):
        for n, choice in enumerate(self.path):
            print(f'{n + 1}. {choice.choice_text}')

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
            self.add_path(text, choice)
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
        elif selector == 'q':
            return
        return self

    def menu(self):
        print("{:=^64s}".format(""))
        print(f'The text is: {self}')
        print("The paths currently are:")
        self.show_choice()
        print("""What do you want to do?
            a. Change text
            b. Change/Add choice text for the path
            c. Add new path
            d. Delete path
            e. Next path
            f. Play testing
            g. Back
            h. Go to start
            q. Quit
            """)
        q = self.menu_choice(input(": "))
        if q is None:
            exit()
        q.menu()

    """
        Menu-End
    """

    def play(self):
        print(self)
        if not self.isEnd():
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

# Encode to dict

# Dumping to JSON

# Load from JSON

# Decode from JSON


if __name__ == '__main__':
    root = TextAndChoice()
    root.menu()