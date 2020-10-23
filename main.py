
import tkinter as tk
from charSheet import CharSheet


class MainMenu:
    def __init__(self, master):
        self.master = master

        # Example Hero
        # ========================================================
        self.hero = CharSheet()
        self.hero.add_feat("Warrior", "Once per short rest, you can take a bonus action.")
        self.hero.add_feat("Tamer", "Grants +2 Nature")
        self.hero.add_feat("Alert", "+ Gain +5 Initiative\n"
                               "+ Can't be surprised while conscious"
                               "\n+ No stealth advantage for attackers.")

        # Window Details
        # ========================================================
        self.master.title("Hero Viewer")    # Window title
        self.master.geometry("1000x500")      # default window size
        self.master.configure(bg="#038387")   # background color
        self.master.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')
        self.master.minsize(500, 300)

        # Textbox(es)
        # ========================================================
        self.tb_feats = tk.Text(self.master, height=24, width=30, font=('Comic Sans MS', 8))
        self.tb_feats.grid(row=0, column=0, rowspan=6, padx=10, pady=(10, 0), sticky=tk.N)
        self.tb_feats.config(state=tk.DISABLED)


        # Listbox(es)
        # ========================================================
        self.featList = tk.Listbox(self.master, height=20, width=20)
        self.featList.grid(row=0, column=1, columnspan=3, pady=(10, 0), sticky=tk.N)
        self.update_feats()
        self.featList.bind('<Double-Button-1>', lambda x: self.write_feat_desc())

        # Button(s)
        # ========================================================
        self.bt_add = tk.Button( # our adding button
                        master=self.master,
                        text="+",
                        font=('Comic Sans MS', 10),
                        bg="black",
                        fg="white",
                        width=3,
                        height=0,
                        command=lambda: [
                            self.feat_ui()
                        ]
                    )
        self.bt_remove = tk.Button( # our removing button
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

        self.bt_add.grid(row=1, column=2, pady=0, sticky=tk.N)
        self.bt_remove.grid(row=1, column=3, pady=0, sticky=tk.N)

    def feat_ui(self):
        self.master.wait_window(AddFeat(self.master, self.hero.get_feats()).master)
        if self.hero.get_feat(-1) != self.featList.get(tk.END):
            self.featList.insert(tk.END, self.hero.get_feat(-1))

    def update_feats(self):
        for i in range(self.hero.get_feat_size()):
            self.featList.insert(tk.END, self.hero.get_feat(i))

    def write_feat_desc(self):
        self.tb_feats.config(state=tk.NORMAL),  # makes it editable.
        self.tb_feats.delete("1.0", tk.END),  # clears it.
        self.tb_feats.insert(tk.END,  # gets the right description.
                             self.hero.get_feat(self.featList.get(self.featList.curselection()))),
        self.tb_feats.config(state=tk.DISABLED)


# ================================================================================================================
class AddFeat(MainMenu):
    def __init__(self, master, hero_list):
        self.master = master
        self.hero_list = hero_list
        self.master = tk.Toplevel()

        # Window Details
        # ========================================================
        self.master.title("Add Feature or Trait")  # Window title
        self.master.geometry("300x200")  # default window size
        self.master.configure(bg="#038387")  # background color
        self.master.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')
        self.master.minsize(300, 200)
        # Label(s)
        # ========================================================
        self.name = tk.Label(self.master, text="Name", bg="#038387").grid(row=0)
        self.desc = tk.Label(self.master, text="Details", bg="#038387").grid(row=1)
        # Entries
        # ========================================================
        self.e_name = tk.Entry(self.master)
        self.e_desc = tk.Entry(self.master)

        self.e_name.grid(row=0, column=1)
        self.e_desc.grid(row=1, column=1)
        # Buttons
        # ========================================================
        self.bt_submit = tk.Button(  # for finalizing your inputs.
            master=self.master,
            text="Add",
            font=('Comic Sans MS', 10),
            bg="black",
            fg="white",
            width=3,
            height=0,
            command=lambda: [
                self.submit(),
                self.master.destroy()
            ]
        )
        self.bt_cancel = tk.Button(  # for cancelling the request
            master=self.master,
            text="Cancel",
            font=('Comic Sans MS', 10),
            bg="black",
            fg="white",
            width=3,
            height=0,
            command=self.master.destroy
        )
        self.bt_cancel.grid(row=2, column=1, pady=0, sticky=tk.N)
        self.bt_submit.grid(row=2, column=2, pady=0, sticky=tk.N)

    def submit(self):
        self.hero_list.append((self.e_name.get(), self.e_desc.get()))
        return -1


root = tk.Tk()
app = MainMenu(root)
root.mainloop()
