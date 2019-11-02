from tkinter import *

class Application:
    def __init__(self, master=None):
        master.attributes('-fullscreen', True)
        master.configure(background='green')
        self.frame = Frame(master)
        self.frame.pack(side=RIGHT)
        self.width_label = Label(self.frame, text="Width: " + str(master.winfo_screenwidth()))
        self.width_label.pack()
        self.height_label = Label(self.frame, text="Height: " + str(master.winfo_screenheight()))
        self.height_label.pack()
        self.button_quit = Button(self.frame, text="Quit", command=root.destroy).pack()
    
root = Tk()
Application(root)
root.mainloop()
