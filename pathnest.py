import json



class CreateNew:
    def __init__(self, name):
        self.name = name
        self.main = {}
        self.nest = self.main


    def append_text(self, text):
        res = 0
        for i in self.nest.values():
            if type(i) is dict:
                res = 1
                break
        if res:
            print("Denied: cannot append text after choices")
        else:
            self.nest[str(len(self.nest))] = text


    def append_choice(self, choice):
        self.nest[str(len(self.nest))] = {"0": choice}


    def dig_in(self, index):
        lin_n = 0
        for n in self.nest.values():
            if type(n) is str:
                lin_n += 1
        if lin_n + index < len(self.nest):
            self.nest = self.nest[str(lin_n + index)]
        else:
            print("Index out of range.")

    
    def at_start(self):
        self.nest = self.main


    def change_text(self, index, new_text):
        if index > len(self.nest) - 1:
            print("Index out of range")
        elif type(self.nest[index]) is dict:
            print("changing choices not allowed")
        else:
            self.nest[str(index)] = new_text
    
    
    def pop_index(self, index):
        if index > len(self.nest) - 1:
            print("Index out of range")
        else:
            self.nest.pop(str(index))

            pard = 0
            for i in self.nest:
                if int(i) == pard:
                    pard += 1
                else:
                    break

            for n in range(len(self.nest) - pard):
                self.nest[str(pard + n)] = self.nest.pop(str(pard + n + 1))


    def display(self):
        print("\nCurrent nest\n")
        n = 0
        for lib in self.nest.values():
            if type(lib) is dict:
                print(n, lib["0"])
                n += 1
            else:
                print(lib)
        print("\n---\n")
    
    
    def display_main(self):
        for lib in self.main.values():
            print(lib)
    
    
    def nest_save(self, save_name):
        f = open(save_name + ".json", "w")
        json.dump(self.main, f)
        f.close()
 
 
    def load_nest(self, file_name):
        f = open(file_name + ".json", "r")
        data = json.load(f)
        f.close()
        self.main = data
        self.nest = self.main


def show_inputs():
    print('''
    
    a. append text to current nest
    b. change text in index of the current nest
    c. append choice to current nest
    x. remove text or choice from current nest
    (remmoving the choice will remove all path inside the choice)
    i. proceed into a choice(to append text and more choice to create path)
    g. go back to the start of the nest
    d. display the texts and choices of the current nest
    s. save game present(Same file name will override the )
    l. load game present
    h. to show commands.
    q. to quit
    
    ''')


def create_menu():
    game_name = input("Game name: ")
    game = CreateNew(game_name)
    show_inputs()
    while True:
        u_in = input("Input: ")
        if u_in == "q":
            break
        
        elif u_in == "h":
            show_inputs()

        elif u_in == "a":
            u_text = input("Append Text: ")
            game.append_text(u_text)
        
        elif u_in == "b":
            u_index = int(input("Index Position to change: "))
            u_text = input("Change Text: ")
            game.change_text(u_index, u_text)

        elif u_in == "c":
            u_choice = input("Append choice: ")
            game.append_choice(u_choice)
        
        elif u_in == "x":
            u_index = input("Remove in index('c' to cancel): ")
            if u_index == "c":
                print("Canceled")
            else:
                u_index = int(u_index)
                game.pop_index(u_index)
        
        elif u_in == "i":
            u_index = int(input("Choice index to proceed into: "))
            game.dig_in(u_index)
        
        elif u_in == "g":
            game.at_start()

        elif u_in == "d":
            game.display()
        
        elif u_in == "s":
            u_text = input("file name(without extension): ")
            u_in = input("Confirm save?(Y/N) ")
            if u_in.lower() == "y":
                game.nest_save(u_text)
            else:
                print("cancel saving")
        
        elif u_in == "l":
            u_text = input("load file name(without extension): ")
            u_in = input("Confirm load file?(Unsaved Progress will be lost.)\n(Y/N) ")
            if u_in.lower() == "y":
                game.load_nest(u_text)
            else:
                print("Cancel loading file")


if __name__ == "__main__":
    create_menu()
