
import tkinter as tk
from charSheet import CharSheet

# Creating example item
# ========================================================

hero = CharSheet()
hero.add_feat("warrior", "Once per short rest, you can take a bonus action.")

# Window(s)
# ========================================================

window = tk.Tk()
window.title("My First GUI")    # Window title
window.geometry("1000x500")      # default window size
window.configure(bg="#038387")   # background color
window.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')
window.minsize(500, 300)

# Frame(s)
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

# Listbox(es)
# ========================================================

featList = tk.Listbox(frame)
featList.pack(pady=15)

for i in range(hero.get_feat_size()):
    featList.insert(tk.END, hero.get_feat(i))

# Button(s)
# ========================================================

bt = tk.Button( # our main exit button
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
