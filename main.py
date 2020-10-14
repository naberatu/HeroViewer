
import tkinter

window = tkinter.Tk()
frame = tkinter.Frame(window)
frame.pack()

window.title("My First GUI")
# label = tkinter.Label(window, text="Henlo").pack()
bt = tkinter.Button(window, text="Exit", command=quit)
bt.pack(side=tkinter.TOP)   # centers towards top

window.mainloop()