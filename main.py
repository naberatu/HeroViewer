
import tkinter as tk
from charSheet import CharSheet

# Creating example item
# ========================================================
hero = CharSheet()
hero.add_feat("Warrior", "Once per short rest, you can take a bonus action.")
hero.add_feat("Tamer", "Grants +2 Nature")
hero.add_feat("Alert", "+ Gain +5 Initiative\n+ Can't be surprised while conscious\n+ No stealth advantage for attackers.")

# Window(s)
# ========================================================
window = tk.Tk()
window.title("My First GUI")    # Window title
window.geometry("1000x500")      # default window size
window.configure(bg="#038387")   # background color
window.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')
window.minsize(500, 300)

# Listbox(es)
# ========================================================
featList = tk.Listbox(window, height=20, width=20)
featList.grid(row=0, column=1, columnspan=3, pady=(10, 0), sticky=tk.N)

for i in range(hero.get_feat_size()):
    featList.insert(tk.END, hero.get_feat(i))

# Textbox(es)
# ========================================================
tb_feats = tk.Text(window, height=24, width=30, font=('Comic Sans MS', 8))
tb_feats.grid(row=0, column=0, rowspan=6, padx=10, pady=(10, 0), sticky=tk.N)
tb_feats.config(state=tk.DISABLED)

# Button(s)
# ========================================================
bt_add = tk.Button( # our adding button
                master=window,
                text="+",
                font=('Comic Sans MS', 10),
                bg="black",
                fg="white",
                width=3,
                height=0,
                command=lambda:[
                ]
            )
bt_remove = tk.Button( # our removing button
                master=window,
                text="-",
                font=('Comic Sans MS', 10),
                bg="black",
                fg="white",
                width=3,
                height=0,
                command=lambda:[
                ]
            )
bt_view = tk.Button( # our viewing button
                master=window,
                text="View",
                font=('Comic Sans MS', 10),
                bg="black",
                fg="white",
                width=4,
                height=0,
                command=lambda:[
                    tb_feats.config(state=tk.NORMAL),       # makes it editable.
                    tb_feats.delete("1.0", tk.END),         # clears it.
                    tb_feats.insert(tk.END,                 # gets the right description.
                                    hero.get_feat(featList.get(featList.curselection()))),
                    tb_feats.config(state=tk.DISABLED)      # makes it un-editable again.
                ]
            )

bt_view.grid(row=1, column=1, pady=0, sticky=tk.N)
bt_add.grid(row=1, column=2, pady=0, sticky=tk.N)
bt_remove.grid(row=1, column=3, pady=0, sticky=tk.N)

window.mainloop()
