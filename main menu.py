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
    browse = tk.Button(master=bg, text='Browse', command=passes, bg="white", height = 100, width = 25)
    browse.place(relx = 0.15, rely = 0.5, anchor = "center")
    top10image = tk.PhotoImage(file="top10gif.gif")

    top10 = tk.Button(master=bg, text='HOT TOP 10!!!!', command=passes, bg="white", height = 100, width = 25)

    #top10.config(image=top10image, compound="center", width="30", height="30")
    top10.place(relx = 0.5, rely = 0.5, anchor = "center")
    categories = tk.Button(master=bg, text='Search by categories', command=passes, bg="white", height = 100, width = 25)
    categories.place(relx = 0.85, rely = 0.5, anchor = "center")
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


if __name__ =="__main__":
    window = tk.Tk()
    window.title("Message Simulator")
    # window.option_add("*Button.Background", "black")
    # window.option_add("*Button.Foreground", "red")

    window.geometry("600x900")
    window.resizable(0, 0)

    bg = tk.Frame(master=window, bg='black')
    bg.pack_propagate(0)
    bg.pack(fill=tk.BOTH, expand=1)

    start = tk.Button(master=bg, text='Read new novel!!', command=startgame, bg="white", height = 6, width = 15)
    start.place(relx = 0.5, rely = 0.1, anchor = "center")
    text = tk.Label(window, text="This is prototype build, no decoration yet.", fg="red")
    text.place(relx = 0.5, rely = 0.05, anchor = "center")
    load = tk.Button(master=bg, text="Load readed novel", command=load, bg="white", height = 5, width = 17)
    load.place(relx = 0.5, rely = 0.3, anchor = "center")
    write = tk.Button(master=bg, text="Write your own Story!", command=load, bg="white", height = 4, width = 18)
    write.place(relx = 0.5, rely = 0.5, anchor = "center")
    option = tk.Button(master=bg, text="Option", command=load, bg="white", height = 4, width = 16)
    option.place(relx = 0.5, rely = 0.7, anchor = "center")
    close = tk.Button(master=bg, text='Quit', command=window.destroy, bg="white", height = 5, width = 14)
    close.place(relx = 0.5, rely = 0.9, anchor = "center")

    window.mainloop()