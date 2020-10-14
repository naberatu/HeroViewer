
import tkinter as tk

# Creating Window
# ========================================================

window = tk.Tk()
window.title("My First GUI")    # Window title
window.geometry("600x300")      # default window size
window.configure(bg="#038387")   # background color
window.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')

# Creating Frame(s)
# ========================================================

window.columnconfigure(0, weight=2, minsize=150)
window.columnconfigure(1, weight=2, minsize=150)
window.rowconfigure(0, weight=1, minsize=50)

frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )

frame.grid(row=0, column=1, padx=5, pady=5)
bt = tk.Button(
                master=frame,
                text="Exit",
                font=('Comic Sans MS', 12),
                bg="black",
                fg="white",
                width=5,
                height=1,
                command=quit
            )
bt.pack()


window.mainloop()
