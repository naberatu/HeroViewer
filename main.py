
import tkinter as tk
from tkinter import *
from PIL import Image, ImageTk
from charSheet import CharSheet


class MainMenu:
    def bkgd_resize(self, event):
        image = self.BGI.resize((event.width, event.height), Image.ANTIALIAS)
        self.b_label.image = ImageTk.PhotoImage(image)
        self.b_label.config(image=self.b_label.image)

    def __init__(self, master):
        self.master = master
        self.hero = CharSheet()
        self.BGC = "#724e52"
        self.FGC = "light grey"
        self.FONT = 'NewRocker'
        self.ICON = "hv_icon.ico"

        # ========================================================
        # Main Window Details
        # ========================================================
        self.master.title("Hero Viewer by Nader Atout")    # Window title
        self.master.geometry("1000x500+200+100")      # default window size
        self.minsize = (1000, 500)
        self.master.minsize(self.minsize[0], self.minsize[1])
        self.master.iconbitmap(self.ICON)

        # Handles resizable background.
        self.BGI = Image.open("hv_bg.png")
        self.b_label = tk.Label(self.master)
        self.b_label.place(x=0, y=0, relwidth=1, relheight=1)
        self.b_label.bind("<Configure>", self.bkgd_resize)

        # ========================================================
        # Main Window Labels
        # ========================================================
        tk.Label(self.master, text="Name", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky=tk.NW)
        tk.Label(self.master, text="Lv", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=0, column=6, pady=(10, 0), sticky=tk.NE)
        tk.Label(self.master, text="Class", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=0, column=9, pady=(10, 0), sticky=tk.NE)
        tk.Label(self.master, text="Race", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=0, column=12, padx=(10, 0), pady=(10, 0), sticky=tk.NE)
        tk.Label(self.master, text="Alignment", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=0, column=15, padx=(10, 0), pady=(10, 0), sticky=tk.NE)

        tk.Label(self.master, text="Description", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=1, column=7, columnspan=6, pady=(10, 0), sticky=tk.S)
        tk.Label(self.master, text="Features", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=1, column=13, columnspan=2, pady=(10, 0), sticky=tk.S)

        tk.Label(self.master, text="Attributes", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=1, column=0, columnspan=2, padx=(10, 0), pady=(10, 0), sticky=tk.W)
        tk.Label(self.master, text="Skills", fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=8, column=0, columnspan=2, padx=(10, 0), pady=(10, 0), sticky=tk.W)

        self.refresh_labels()

        # ========================================================
        # Description Text Box
        # ========================================================

        self.tb_feats = tk.Text(self.master, height=13, width=30, font=(self.FONT, 10))
        self.tb_feats.grid(row=2, column=7, rowspan=7, columnspan=6, padx=(10, 0), sticky=tk.N)
        self.tb_feats.config(state=tk.DISABLED)

        # ========================================================
        # Drop Down Lists
        # ========================================================

        # Character Class
        self.class_list = ['Artificer', 'Barbarian', 'Bard', 'Cleric', 'Druid', 'Fighter', 'Monk',
                           'Paladin', 'Ranger', 'Rogue', 'Sorcerer', 'Warlock', 'Wizard']
        self.tkvar_class = tk.StringVar(self.master)
        self.tkvar_class.set(self.hero.get_stat("role"))
        self.ddl_class = tk.OptionMenu(self.master, self.tkvar_class, *self.class_list,
                                       command=lambda x: [
                                           self.hero.set_stat("role", self.tkvar_class.get()),
                                           self.update_hit_dice(True)
                                       ])
        self.ddl_class.config(height=0, width=10, fg=self.FGC, bg=self.BGC, font=(self.FONT, 8))
        self.ddl_class["borderwidth"] = 0
        self.ddl_class.grid(row=0, column=10, columnspan=2, pady=(10, 0), sticky=tk.NW)

        # Character Race
        self.race_list = ['Aarakocra', 'Aasimar', 'Bugbear', 'Centaur', 'Changeling', 'Dragonborn', 'Dwarf', 'Elf',
                          'Firbolg', 'Genasi', 'Gith', 'Gnome', 'Goblin', 'Goliath', 'Halfling', 'Half-Elf', 'Half-Orc',
                          'Hobgoblin', 'Human', 'Kalashtar', 'Kender', 'Kenku', 'Kobold', 'Kor', 'Lizardfolk', 'Loxodon',
                          'Merfolk', 'Minotaur', 'Orc', 'Shifter', 'Simic', 'Hybrid', 'Tabaxi', 'Tiefling', 'Tortle',
                          'Triton', 'Vampire', 'Vedalken', 'Warforged', 'Yuan-Ti']
        self.tkvar_race = tk.StringVar(self.master)
        self.tkvar_race.set(self.hero.get_stat("race"))
        self.ddl_race = tk.OptionMenu(self.master, self.tkvar_race, *self.race_list,
                                      command=lambda x: [
                                          self.hero.set_stat("race", self.tkvar_race.get()),
                                          self.update_box(self.dict_listbox["Spd"], self.hero.get_stat("Spd"))
                                      ])
        self.ddl_race.config(height=0, width=12, fg=self.FGC, bg=self.BGC, font=(self.FONT, 8))
        self.ddl_race["borderwidth"] = 0
        self.ddl_race.grid(row=0, column=13, columnspan=2, pady=(10, 0), sticky=tk.NW)

        # Character Alignment
        self.alignment_list = ['Lawful Good', 'Neutral Good', 'Chaotic Good', 'Lawful Neutral', 'True Neutral',
                               'Chaotic Neutral', 'Lawful Evil', 'Neutral Evil', 'Chaotic Evil']
        self.tkvar_alignment = tk.StringVar(self.master)
        self.tkvar_alignment.set(self.hero.get_stat("alignment"))
        self.ddl_alignment = tk.OptionMenu(self.master, self.tkvar_alignment, *self.alignment_list,
                                           command=lambda x: self.hero.set_stat("alignment", self.tkvar_alignment.get()))
        self.ddl_alignment.config(height=0, width=12, fg=self.FGC, bg=self.BGC, font=(self.FONT, 8))
        self.ddl_alignment["borderwidth"] = 0
        self.ddl_alignment.grid(row=0, column=16, columnspan=2, pady=(10, 0), sticky=tk.NW)

        # ========================================================
        # Listbox
        # ========================================================

        # Listbox for Features List
        self.featList = tk.Listbox(self.master, height=10, width=15)
        self.featList.grid(row=2, column=13, rowspan=6, columnspan=2, sticky=tk.N)
        for i in range(self.hero.get_feat_size()):
            self.featList.insert(tk.END, self.hero.get_feat_name(i))
        self.featList.bind('<ButtonRelease-1>', lambda x: self.write_feat_desc())
        self.featList.bind('<Double-Button-1>', lambda x: self.edit_feat(False))

        # Listbox for Name
        self.dict_listbox = {"name": tk.Listbox(self.master, height=1, width=25, font=(self.FONT, 12))}
        self.dict_listbox["name"].grid(row=0, column=1, columnspan=5, ipady=0, pady=(10, 0), sticky=tk.NW)
        self.dict_listbox["name"].insert(tk.END, self.hero.get_stat("name"))
        self.dict_listbox["name"]["borderwidth"] = 1
        self.dict_listbox["name"].bind('<Double-Button-1>', lambda x: self.set_box("name"))

        # Listbox for Level
        self.dict_listbox["level"] = tk.Listbox(self.master, height=1, width=3, justify='center', font=(self.FONT, 12))
        self.dict_listbox["level"].grid(row=0, column=7, pady=(10, 0), sticky=tk.NW)
        self.dict_listbox["level"].insert(tk.END, self.hero.get_stat("level"))
        self.dict_listbox["level"]["borderwidth"] = 1
        self.dict_listbox["level"].bind('<Double-Button-1>', lambda x: self.set_box("level", False, True))

        # attribute populator loop
        arow = 2
        for attribute in self.hero.get_attributes():
            tk.Label(self.master, text=attribute[0].upper() + attribute[1:], fg=self.FGC, bg=self.BGC,
                     font=(self.FONT, 10)).grid(row=arow, column=0, columnspan=2, padx=(10, 0), sticky=tk.W)

            tk.Label(self.master, text="%+d" % self.hero.get_modifier(attribute), fg=self.FGC, bg=self.BGC,
                     font=(self.FONT, 10)).grid(row=arow, column=2, padx=(10, 0))

            self.dict_listbox[attribute] = tk.Listbox(self.master, height=1, width=3,
                                                      justify='center', font=(self.FONT, 10))
            self.dict_listbox[attribute].grid(row=arow, column=3, sticky=tk.W)
            self.dict_listbox[attribute].insert(tk.END, self.hero.get_stat(attribute))
            self.dict_listbox[attribute]["borderwidth"] = 1

            arow += 1
        # end of loop

        # Sets Listbox Binding for the main Attributes.
        self.dict_listbox["strength"].bind('<Double-Button-1>', lambda x: self.set_box("strength"))
        self.dict_listbox["dexterity"].bind('<Double-Button-1>', lambda x: self.set_box("dexterity"))
        self.dict_listbox["constitution"].bind('<Double-Button-1>', lambda x: self.set_box("constitution"))
        self.dict_listbox["wisdom"].bind('<Double-Button-1>', lambda x: self.set_box("wisdom"))
        self.dict_listbox["intellect"].bind('<Double-Button-1>', lambda x: self.set_box("intellect"))
        self.dict_listbox["charisma"].bind('<Double-Button-1>', lambda x: self.set_box("charisma"))

        # health and armor block populator loop
        arow = 2
        for block in self.hero.get_block():
            if block == "HP":
                self.dict_listbox[block] = tk.Listbox(self.master, height=1, width=8,
                                                      justify='center', font=(self.FONT, 10))
            elif block == "HD":
                self.dict_listbox[block] = tk.Listbox(self.master, height=1, width=5,
                                                      justify='center', font=(self.FONT, 10))
            else:
                self.dict_listbox[block] = tk.Listbox(self.master, height=1, width=3,
                                                      justify='center', font=(self.FONT, 10))
            self.dict_listbox[block].grid(row=arow, column=5, sticky=tk.W)
            tk.Label(self.master, text=block, fg=self.FGC, bg=self.BGC, font=(self.FONT, 10)).grid(row=arow, column=4, sticky=tk.E)
            if block == "HD" and self.hero.get_stat(block):
                self.dict_listbox[block].insert(tk.END, str(self.hero.get_stat("level")) + "d"
                                                + str(self.hero.get_stat(block)))
            elif block == "HP":
                self.dict_listbox[block].insert(tk.END, str(self.hero.get_stat("HP")) + "/"
                                                + str(self.hero.get_stat("Max HP"))),
            else:
                self.dict_listbox[block].insert(tk.END, self.hero.get_stat(block))
            self.dict_listbox[block]["borderwidth"] = 1
            arow += 1
        # end of loop

        # Sets Listbox binding for the Block Stats
        self.dict_listbox["HP"].bind('<Double-Button-1>', lambda x: self.edit_hp())
        self.dict_listbox["AC"].bind('<Double-Button-1>', lambda x: self.set_box("AC"))
        self.dict_listbox["Spd"].bind('<Double-Button-1>', lambda x: self.set_box("Spd"))

        # ========================================================
        # Button(s)
        # ========================================================
        self.bt_add = tk.Button( # our adding button
            master=self.master,
            text="+",
            font=('Comic Sans MS', 12),
            bg=self.BGC,
            fg=self.FGC,
            width=4,
            height=0,
            command=lambda: self.edit_feat(True)
        )
        self.bt_remove = tk.Button( # our removing button
            master=self.master,
            text="-",
            font=('Comic Sans MS', 12),
            bg=self.BGC,
            fg=self.FGC,
            width=4,
            height=0,
            command=lambda: [
                self.hero.del_feat(self.featList.get(self.featList.curselection())),
                self.tb_feats.config(state=tk.NORMAL),      # makes it editable.
                self.tb_feats.delete("1.0", tk.END),        # clears it.
                self.tb_feats.config(state=tk.DISABLED),    # default state
                self.featList.delete(self.featList.curselection()),
            ]
        )
        self.bt_lvlup = tk.Button(
            master=self.master,
            text="U",
            font=(self.FONT, 6),
            bg=self.BGC,
            fg=self.FGC,
            width=5,
            height=2,
            borderwidth=0,
            command=lambda: [
                self.hero.level_up(),
                self.update_box(self.dict_listbox["level"], self.hero.get_stat("level")),
                self.update_hit_dice(False)
            ]
        )
        self.bt_add.grid(row=8, column=13, sticky=tk.NE)
        self.bt_remove.grid(row=8, column=14, sticky=tk.NW)
        self.bt_lvlup.grid(row=0, column=8, padx=(0, 30), pady=(10, 0), sticky=tk.NW)

    # ========================================================
    # Methods
    # ========================================================

    # Refreshes all label objects.
    def refresh_labels(self):

        # List that maps all Skills to their corresponding main Attribute.
        skill_list = ["dexterity", "wisdom", "intellect", "strength", "charisma", "intellect", "wisdom", "charisma",
                      "intellect", "wisdom", "intellect", "wisdom", "charisma", "charisma", "intellect", "dexterity",
                      "dexterity", "wisdom"]

        # Displays Modifiers for the main 6 Attributes.
        arow = 2
        for atr in self.hero.get_attributes():
            tk.Label(self.master, text="%+d" % self.hero.get_modifier(atr), fg=self.FGC, bg=self.BGC,
                     font=(self.FONT, 10)).grid(row=arow, column=2, padx=(10, 0))
            arow += 1

        # Displays scores for all remaining Skills.
        arow, scol, index = 9, 0, 0
        for skill in self.hero.get_skills():
            tk.Label(self.master, text=skill[0].upper() + skill[1:], fg=self.FGC, bg=self.BGC, font=(self.FONT, 10)) \
                .grid(row=arow, column=scol, columnspan=2, padx=(10, 0), sticky=tk.W)

            tk.Label(self.master, text="%+d" % self.hero.get_modifier(skill_list[index]),  fg=self.FGC, bg=self.BGC,
                     font=(self.FONT, 10)).grid(row=arow, column=scol + 2, padx=(10, 0))
            arow += 1
            index += 1
            if arow > 17:
                arow, scol = 9, 4

    # Updates HP Listbox
    def edit_hp(self):

        # Window Settings
        temp_ui = self.master
        temp_ui = tk.Toplevel()
        temp_ui.grab_set()

        temp_ui.title("Edit HP")                # Window title
        temp_ui.geometry("250x100+300+200")     # default window size
        temp_ui.minsize(250, 100)               # default min size
        temp_ui.configure(bg=self.BGC)           # background color
        temp_ui.iconbitmap(self.ICON)

        # Label and Entry Text Field
        tk.Label(temp_ui, text="Enter Hit Points", bg=self.BGC, font=(self.FONT, 12)).grid(row=0, padx=30,
                                                                                           columnspan=2, pady=(10, 0))
        e_input = tk.Entry(temp_ui, justify='center', font=(self.FONT, 10))
        e_input.grid(row=1, column=0, columnspan=2,  padx=30, pady=(5, 0))

        # Button to submit Max HP
        bt_submit_max = tk.Button(
            master=temp_ui,
            text="Max HP",
            font=(self.FONT, 10),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: [
                self.hero.set_stat("Max HP", e_input.get()),
                self.dict_listbox["HP"].delete(0),
                self.dict_listbox["HP"].insert(tk.END, str(self.hero.get_stat("HP")) + "/"
                                               + str(self.hero.get_stat("Max HP"))),
                temp_ui.destroy()
            ]
        )

        # Button to submit Current HP
        bt_submit_current = tk.Button(
            master=temp_ui,
            text="Current",
            font=(self.FONT, 10),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: [
                self.hero.set_stat("HP", e_input.get()),
                self.dict_listbox["HP"].delete(0),
                self.dict_listbox["HP"].insert(tk.END, str(self.hero.get_stat("HP")) + "/"
                                               + str(self.hero.get_stat("Max HP"))),
                temp_ui.destroy()
            ]
        )

        bt_submit_max.grid(row=2, column=1, padx=5, pady=(10, 0), sticky=tk.NW)
        bt_submit_current.grid(row=2, column=0, padx=5, pady=(10, 0), sticky=tk.NE)

    # Updates Feature Listbox
    def edit_feat(self, adding):

        # Window Settings
        temp_ui = self.master
        temp_ui = tk.Toplevel()
        temp_ui.grab_set()

        temp_ui.title("Edit Feat")  # Window title
        temp_ui.geometry("250x110+300+200")  # default window size
        temp_ui.minsize(250, 110)
        temp_ui.configure(bg=self.BGC)  # background color
        temp_ui.iconbitmap(self.ICON)

        # Labels and Text Entry Fields
        tk.Label(temp_ui, text="Feat", fg=self.FGC, bg=self.BGC, font=(self.FONT, 10)).grid(row=0, padx=(10, 0), pady=(10, 0))
        tk.Label(temp_ui, text="Desc", fg=self.FGC, bg=self.BGC, font=(self.FONT, 10)).grid(row=1, padx=(10, 0), pady=(5, 0))
        e_name = tk.Entry(temp_ui, font=(self.FONT, 10))
        e_desc = tk.Entry(temp_ui, font=(self.FONT, 10))
        e_name.grid(row=0, column=1, columnspan=2, pady=(10, 0))
        e_desc.grid(row=1, column=1, columnspan=2, pady=(5, 0))

        position = 0
        if not adding:
            position = self.featList.curselection()
        else:
            position = tk.END

        # Submit Feature to add.
        bt_submit = tk.Button(
            master=temp_ui,
            text="Submit",
            font=(self.FONT, 10),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: [
                self.hero.add_feat(e_name.get(), e_desc.get(), self.featList.get(position), adding),
                self.featList.delete(position) if e_name.get() and not adding else 0,
                self.featList.insert(position, e_name.get()) if e_name.get() else 0,
                self.write_feat_desc() if not e_name.get() and e_desc.get() else 0,
                temp_ui.destroy()
            ]
        )

        # Closes the window.
        bt_cancel = tk.Button(
            master=temp_ui,
            text="Cancel",
            font=(self.FONT, 10),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: temp_ui.destroy()
        )

        bt_submit.grid(row=3, column=2, pady=(10, 0), sticky=tk.N)
        bt_cancel.grid(row=3, column=1, pady=(10, 0), sticky=tk.N)

    # Updates the Description Text Box
    def write_feat_desc(self):
        self.tb_feats.config(state=tk.NORMAL)       # makes it editable.
        self.tb_feats.delete("1.0", tk.END)         # clears it.
        self.tb_feats.insert(tk.END, self.hero.get_feat_desc(self.featList.get(self.featList.curselection())))
        self.tb_feats.config(state=tk.DISABLED)     # makes it un-editable.

    # Updates Hit Dice Box, since the printing is unique.
    def update_hit_dice(self, role):
        self.dict_listbox["HD"].delete(0)

        if role:
            dict_roles = {
                "Barbarian": 12,
                "Sorcerer": 6,
                "Wizard": 6,
                "Fighter": 10,
                "Paladin": 10,
                "Ranger": 10
            }
            if self.hero.get_stat("role") in dict_roles.keys():
                self.hero.set_stat("HD", dict_roles[self.hero.get_stat("role")])
            else:
                self.hero.set_stat("HD", 8)

        self.dict_listbox["HD"].insert(tk.END, str(self.hero.get_stat("level")) + "d"
                                       + str(self.hero.get_stat("HD")))

    # Refreshes a given listbox.
    def update_box(self, listbox, value):
        listbox.delete(0)
        listbox.insert(tk.END, value)

    # Helps update the Armor Class Box when updating Dexterity.
    def dex_peel(self, peeled_ac):
        self.hero.set_stat("AC", peeled_ac)
        self.dict_listbox["AC"].delete(0)
        self.dict_listbox["AC"].insert(tk.END, self.hero.get_stat("AC"))

    # Updates a given stat and the Listbox that displays it.
    def set_box(self, choice, hit_dice=None, level=None):

        # Window Settings
        temp_ui = self.master
        temp_ui = tk.Toplevel()
        temp_ui.grab_set()

        detail = "Edit " + choice[0].upper() + choice[1:]

        temp_ui.title(detail)  # Window title
        temp_ui.geometry("250x125+300+200")  # default window size
        temp_ui.minsize(250, 125)
        temp_ui.configure(bg=self.BGC)  # background color
        temp_ui.iconbitmap(self.ICON)

        # Labels and Entry Text Fields
        n_val = "New Value"
        peeled_ac = 0
        if choice == "AC":
            n_val += ": AC = Input %+d" % self.hero.get_modifier("dexterity")
        elif choice == "dexterity":
            peeled_ac = self.hero.get_stat("AC") - self.hero.get_modifier("dexterity")

        tk.Label(temp_ui, text=n_val, fg=self.FGC, bg=self.BGC, font=(self.FONT, 12)).grid(row=0, padx=30, pady=(10, 0))
        e_detail = tk.Entry(temp_ui, justify='center', font=(self.FONT, 12))
        e_detail.grid(row=1, column=0, padx=30, pady=(5, 0))

        # Button to Submit input.
        bt_submit = tk.Button(
            master=temp_ui,
            text="Submit",
            font=(self.FONT, 12),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: [
                self.hero.set_stat(choice, e_detail.get()),
                self.update_box(self.dict_listbox[choice], self.hero.get_stat(choice)),
                self.update_hit_dice(False) if choice == "level" else 0,
                self.refresh_labels(),
                self.dex_peel(peeled_ac) if choice == "dexterity" else 0,
                temp_ui.destroy()
            ]
        )

        bt_submit.grid(row=2, column=0, pady=(10, 0), sticky=tk.N)


# Main/Driver code
root = tk.Tk()
app = MainMenu(root)
root.mainloop()
