
from tkinter import *
from tkinter.ttk import *

window = Tk()
window.geometry('600x300')  # default window size

window.config

frame = Frame(window)
frame.pack()

window.title("My First GUI")
# label = tkinter.Label(window, text="Henlo").pack()
bt = Button(window, text="Exit", command=quit)
bt.pack(side=TOP)   # centers towards top

window.mainloop()