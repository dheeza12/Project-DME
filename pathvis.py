import json



def play(nest):
    cur_nest = nest
    index = 0
    while True:
        if index < len(cur_nest):
            if type(cur_nest[str(index)]) is dict:
                while True:
                    c_index = len(cur_nest) - index
                    for i in range(c_index):
                        print(i, cur_nest[str(index + i)]["0"])
                    #print(c_index)
                    u_c = int(input("Select Choice: "))
                    cur_nest = cur_nest[str(u_c + index)]
                    index = 0
                    break
            else:
                print(cur_nest[str(index)])
        else:
            break
        index += 1


def load_game(game):
    json_file = open(game + ".json", "r")
    data = json.load(json_file)
    json_file.close()
    return dict(data)

if __name__ == "__main__":
    game = load_game("Game2_MarryLover")
    
    play(game)
