
import tkinter as tk
from charSheet import CharSheet


# Creating example item
# ========================================================
hero = CharSheet()
hero.add_feat("Warrior", "Once per short rest, you can take a bonus action.")
hero.add_feat("Tamer", "Grants +2 Nature")
hero.add_feat("Alert", "+ Gain +5 Initiative\n"
                       "+ Can't be surprised while conscious"
                       "\n+ No stealth advantage for attackers.")

class MainMenu:
    def __init__(self, master):
        self.master = master

        # Window Details
        # ========================================================
        self.master.title("Hero Viewer")    # Window title
        self.master.geometry("1000x500")      # default window size
        self.master.configure(bg="#038387")   # background color
        self.master.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')
        self.master.minsize(500, 300)

        # Listbox(es)
        # ========================================================
        self.featList = tk.Listbox(self.master, height=20, width=20)
        self.featList.grid(row=0, column=1, columnspan=3, pady=(10, 0), sticky=tk.N)

        for i in range(hero.get_feat_size()):
            self.featList.insert(tk.END, hero.get_feat(i))

        # Textbox(es)
        # ========================================================
        tb_feats = tk.Text(self.master, height=24, width=30, font=('Comic Sans MS', 8))
        tb_feats.grid(row=0, column=0, rowspan=6, padx=10, pady=(10, 0), sticky=tk.N)
        tb_feats.config(state=tk.DISABLED)

        # Button(s)
        # ========================================================
        bt_add = tk.Button( # our adding button
                        master=self.master,
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
                        master=self.master,
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
                        master=self.master,
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
                                            hero.get_feat(self.featList.get(self.featList.curselection()))),
                            tb_feats.config(state=tk.DISABLED)      # makes it un-editable again.
                        ]
                    )

        bt_view.grid(row=1, column=1, pady=0, sticky=tk.N)
        bt_add.grid(row=1, column=2, pady=0, sticky=tk.N)
        bt_remove.grid(row=1, column=3, pady=0, sticky=tk.N)


class AddFeat(MainMenu):
    def __init__(self, master):
        self.master = master

        # Window Details
        # ========================================================
        self.master.title("Hero Viewer")  # Window title
        self.master.geometry("1000x500")  # default window size
        self.master.configure(bg="#038387")  # background color
        self.master.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')
        self.master.minsize(500, 300)

        # Label(s)
        # ========================================================
        name = tk.Label(self.master, text="Name").grid(row=0)
        desc = tk.Label(self.master, text="Details").grid(row=0)

        # Entries
        # ========================================================
        e_name = tk.Entry(self.master)
        e_desc = tk.Entry(self.master)

        e_name.grid(row=0, column=1)
        e_desc.grid(row=1, column=1)

        # Buttons
        # ========================================================
        bt_submit = tk.Button(  # for finalizing your inputs.
            master=self.master,
            text="Add",
            font=('Comic Sans MS', 10),
            bg="black",
            fg="white",
            width=3,
            height=0,
            command=lambda: [
            ]
        )
        bt_cancel = tk.Button(  # for cancelling the request
            master=self.master,
            text="Cancel",
            font=('Comic Sans MS', 10),
            bg="black",
            fg="white",
            width=3,
            height=0,
            command=quit
        )


root = tk.Tk()
app = MainMenu(root)
root.mainloop()
