import tkinter as tk
def passes():

    pass
def startgame():
    started = tk.Tk()
    started.title("Message Simulator")
    started.geometry("600x900")
    started.resizable(0, 0)
    bg = tk.Frame(master=started, bg='black')
    bg.pack_propagate(0)
    bg.pack(fill=tk.BOTH, expand=1)
    browse = tk.Button(master=bg, text='Browse', command=passes, bg="white")
    browse.pack()
    top10 = tk.Button(master=bg, text='HOT TOP 10!!!!', command=passes, bg="white")
    top10.pack()
    categories = tk.Button(master=bg, text='Search by categories', command=passes, bg="white")
    categories.pack()
    started.mainloop()



def load():
    loaded = tk.Tk()
    loaded.title("Message Simulator")
    loaded.geometry("600x900")
    loaded.resizable(0, 0)
    bg = tk.Frame(master=loaded, bg='black')
    bg.pack_propagate(0)
    bg.pack(fill=tk.BOTH, expand=1)
    save = tk.Button(master=bg, text='Save #001 :Story: Conan.The hell kid.', command=passes, bg="white")
    save.pack()
    loaded.mainloop()


window = tk.Tk()
window.title("Message Simulator")
#window.option_add("*Button.Background", "black")
#window.option_add("*Button.Foreground", "red")

window.geometry("600x900")
window.resizable(0, 0)

bg = tk.Frame(master=window,bg='black')
bg.pack_propagate(0)
bg.pack(fill=tk.BOTH, expand=1)

start = tk.Button(master=bg, text='Read new novel!!', command=startgame, bg="white")
start.pack()
load = tk.Button(master=bg, text="Load readed novel", command=load, bg="white")
load.pack()
write = tk.Button(master=bg, text="Write your own Story!", command=load, bg="white")
write.pack()
option = tk.Button(master=bg, text="Option", command=load, bg="white")
option.pack()
close = tk.Button(master=bg, text='Quit', command=window.destroy, bg="white")
close.pack()


window.mainloop()