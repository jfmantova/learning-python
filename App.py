from tkinter import *
    
root = Tk()
root.attributes('-fullscreen', True)
root.configure(background='steel blue')
Button(root, text="Quit", command=root.destroy, width=100, height=5).pack()
root.mainloop()
