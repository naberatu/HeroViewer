
import tkinter as tk
from charSheet import CharSheet
from ui_addFeat import AddFeat


class MainMenu:
    def __init__(self, master):
        self.master = master
        self.hero = CharSheet()

        # Window Details
        # ========================================================
        self.master.title("Hero Viewer")    # Window title
        self.master.geometry("960x540+200+100")      # default window size
        self.master.minsize(480, 270)
        self.master.configure(bg="#038387")   # background color
        self.master.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')

        # Labels
        # ========================================================
        self.l_name = tk.Label(self.master, text="Name", bg="#038387", font=('Scaly Sans', 12)).grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky=tk.NW)
        self.l_lvl = tk.Label(self.master, text="Lv", bg="#038387", font=('Scaly Sans', 12)).grid(row=0, column=3, pady=(10, 0), sticky=tk.NE)
        self.l_class = tk.Label(self.master, text="Class", bg="#038387", font=('Scaly Sans', 12)).grid(row=0, column=6, pady=(10, 0), sticky=tk.NE)
        self.l_race = tk.Label(self.master, text="Race", bg="#038387", font=('Scaly Sans', 12)).grid(row=0, column=9, padx=(10, 0), pady=(10, 0), sticky=tk.NE)
        self.l_align = tk.Label(self.master, text="Alignment", bg="#038387", font=('Scaly Sans', 12)).grid(row=0, column=13, padx=(10, 0), pady=(10, 0), sticky=tk.NE)

        # Textbox
        # ========================================================
        self.tb_feats = tk.Text(self.master, height=24, width=30, font=('Scaly Sans', 12))
        self.tb_feats.grid(row=1, column=0, rowspan=6, columnspan=3, padx=10, pady=(10, 0), sticky=tk.N+tk.W)
        self.tb_feats.config(state=tk.DISABLED)

        # Drop Down Lists
        # ========================================================

        # Character Class
        self.class_list = ['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
        self.tkvar_class = tk.StringVar(self.master)
        self.tkvar_class.set(self.hero.get_stat("role"))
        self.ddl_class = tk.OptionMenu(self.master, self.tkvar_class, *self.class_list)
        self.ddl_class.config(height=0, width=10, bg="white", font=('Scaly Sans', 8))
        self.ddl_class["borderwidth"] = 0
        self.ddl_class.grid(row=0, column=7, columnspan=2, pady=(10, 0), sticky=tk.NW)

        # Character Race
        self.race_list = ['Aarakocra', 'Aasimar', 'Bugbear', 'Centaur', 'Changeling', 'Dragonborn', 'Dwarf', 'Elf',
                          'Firbolg', 'Genasi', 'Gith', 'Gnome', 'Goblin', 'Goliath', 'Halfling', 'Half-Elf', 'Half-Orc',
                          'Hobgoblin', 'Human', 'Kalashtar', 'Kender', 'Kenku', 'Kobold', 'Kor', 'Lizardfolk', 'Loxodon',
                          'Merfolk', 'Minotaur', 'Orc', 'Shifter', 'Simic', 'Hybrid', 'Tabaxi', 'Tiefling', 'Tortle',
                          'Triton', 'Vampire', 'Vedalken', 'Warforged', 'Yuan-Ti']
        self.tkvar_race = tk.StringVar(self.master)
        self.tkvar_race.set(self.hero.get_stat("race"))
        self.ddl_race = tk.OptionMenu(self.master, self.tkvar_race, *self.race_list)
        self.ddl_race.config(height=0, width=12, bg="white", font=('Scaly Sans', 8))
        self.ddl_race["borderwidth"] = 0
        self.ddl_race.grid(row=0, column=10, columnspan=2, pady=(10, 0), sticky=tk.NW)

        # Character Alignment
        self.alignment_list = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral', 'True Neutral',
                               'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']
        self.tkvar_alignment = tk.StringVar(self.master)
        self.tkvar_alignment.set(self.hero.get_stat("alignment"))
        self.ddl_alignment = tk.OptionMenu(self.master, self.tkvar_alignment, *self.alignment_list)
        self.ddl_alignment.config(height=0, width=12, bg="white", font=('Scaly Sans', 8))
        self.ddl_alignment["borderwidth"] = 0
        self.ddl_alignment.grid(row=0, column=14, columnspan=2, pady=(10, 0), sticky=tk.NW)

        # Listbox
        # ========================================================
        self.featList = tk.Listbox(self.master, height=20, width=20)
        self.featList.grid(row=1, column=3, columnspan=6, pady=(10, 0), sticky=tk.N+tk.W)
        for i in range(self.hero.get_feat_size()):
            self.featList.insert(tk.END, self.hero.get_feat_name(i))
        self.featList.bind('<ButtonRelease-1>', lambda x: self.write_feat_desc())
        self.featList.bind('<Double-Button-1>', lambda x: self.edit_feat(False))

        self.lb_name = tk.Listbox(self.master, height=1, width=30, font=('Scaly Sans', 12))
        self.lb_name.grid(row=0, column=1, columnspan=2, ipady=0, pady=(10, 0), sticky=tk.NW)
        self.lb_name.insert(tk.END, self.hero.get_stat("name"))
        self.lb_name["borderwidth"] = 1
        self.lb_name.bind('<Double-Button-1>', lambda x: self.ui_mod(0))

        self.lb_level = tk.Listbox(self.master, height=1, width=3, justify='center', font=('Scaly Sans', 12))
        self.lb_level.grid(row=0, column=4, pady=(10, 0), sticky=tk.NE)
        self.lb_level.insert(tk.END, self.hero.get_stat("level"))
        self.lb_level["borderwidth"] = 1
        self.lb_level.bind('<Double-Button-1>', lambda x: self.ui_mod(1))

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
                            self.edit_feat(True)
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
                        command=lambda: [
                            self.featList.delete(self.featList.curselection())
                        ]
                    )

        self.bt_lvlup = tk.Button(
                        master=self.master,
                        text="U",
                        font=('Comic Sans MS', 6),
                        bg="black",
                        fg="white",
                        width=5,
                        height=2,
                        borderwidth=0,
                        command=lambda: [
                            self.hero.level_up(),
                            self.lb_level.delete(0),
                            self.lb_level.insert(tk.END, self.hero.get_stat("level"))
                        ]
        )
        self.bt_lvlup.grid(row=0, column=5, padx=(0,20), pady=(10, 0), sticky=tk.N+tk.W)
        self.bt_add.grid(row=2, column=3, pady=0, sticky=tk.N+tk.W)
        self.bt_remove.grid(row=2, column=4, pady=0, sticky=tk.N+tk.W)

    # Methods
    # ========================================================
    def edit_feat(self, adding):
        temp_ui = self.master
        temp_ui = tk.Toplevel()
        temp_ui.grab_set()

        temp_ui.title("Edit Feat")  # Window title
        temp_ui.geometry("250x100+300+200")  # default window size
        temp_ui.minsize(250, 100)
        temp_ui.configure(bg="#038387")  # background color
        temp_ui.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')

        l_name = tk.Label(temp_ui, text="Feat", bg="#038387", font=('Scaly Sans', 10)).grid(row=0, padx=(10, 0), pady=(10, 0))
        l_desc = tk.Label(temp_ui, text="Desc", bg="#038387", font=('Scaly Sans', 10)).grid(row=1, padx=(10, 0), pady=(5, 0))
        e_name = tk.Entry(temp_ui, font=('Scaly Sans', 10))
        e_desc = tk.Entry(temp_ui, font=('Scaly Sans', 10))
        e_name.grid(row=0, column=1, columnspan=2, pady=(10, 0))
        e_desc.grid(row=1, column=1, columnspan=2, pady=(5, 0))

        position = 0
        if not adding:
            position = self.featList.curselection()
        else:
            position = tk.END

        bt_submit = tk.Button(
            master=temp_ui,
            text="Submit",
            font=('Scaly Sans', 10),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: [
                self.hero.add_feat(e_name.get(), e_desc.get(), self.featList.get(position)),
                self.featList.delete(position) if e_name.get() and not adding else 0,
                self.featList.insert(position, e_name.get()) if e_name.get() else 0,
                self.write_feat_desc() if not e_name.get() and e_desc.get() else 0,
                self.hero.save(),
                temp_ui.destroy()
            ]
        )

        bt_cancel = tk.Button(
            master=temp_ui,
            text="Cancel",
            font=('Scaly Sans', 10),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: temp_ui.destroy()
        )
        bt_submit.grid(row=3, column=2, pady=(10, 0), sticky=tk.N)
        bt_cancel.grid(row=3, column=1, pady=(10, 0), sticky=tk.N)

    def write_feat_desc(self):
        self.tb_feats.config(state=tk.NORMAL),  # makes it editable.
        self.tb_feats.delete("1.0", tk.END),    # clears it.
        self.tb_feats.insert(tk.END,            # gets the right description.
                             self.hero.get_feat_desc(self.featList.get(self.featList.curselection()))),
        self.tb_feats.config(state=tk.DISABLED)

    def ui_mod(self, choice):
        temp_ui = self.master
        temp_ui = tk.Toplevel()
        temp_ui.grab_set()

        detail = "Edit "
        if choice == 0:
            detail += "Name"
        elif choice == 1:
            detail += "Level"

        temp_ui.title(detail)  # Window title
        temp_ui.geometry("250x125+300+200")  # default window size
        temp_ui.minsize(250, 125)
        temp_ui.configure(bg="#038387")  # background color
        temp_ui.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')

        l_detail = tk.Label(temp_ui, text="New Value", bg="#038387", font=('Scaly Sans', 12)).grid(row=0, padx=30, pady=(10, 0))
        e_detail = tk.Entry(temp_ui, justify='center', font=('Scaly Sans', 12))
        e_detail.grid(row=1, column=0, padx=30, pady=(5, 0))

        bt_submit = tk.Button(
            master=temp_ui,
            text="Submit",
            font=('Comic Sans MS', 12),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: [
                self.update_box(e_detail.get(), choice),
                self.hero.save(),
                temp_ui.destroy()
            ]
        )
        bt_submit.grid(row=2, column=0, pady=(10, 0), sticky=tk.N)

    def update_box(self, detail, choice):
        if choice == 0:
            self.hero.set_stat("name", detail)
            self.lb_name.delete(0)
            self.lb_name.insert(tk.END, self.hero.get_stat("name"))
        elif choice == 1:
            try:
                if self.hero.set_level(int(detail)):
                    self.lb_level.delete(0)
                    self.lb_level.insert(tk.END, self.hero.get_stat("level"))
            except:
                return


root = tk.Tk()
app = MainMenu(root)
# root.protocol("WM_DELETE_WINDOW", app.hero.save())
root.mainloop()
