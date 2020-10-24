
import tkinter as tk


class AddFeat:
    def __init__(self, master, hero_list):
        self.master = master
        self.hero_list = hero_list
        self.master = tk.Toplevel()     # Puts this UI front and Center.
        self.master.grab_set()          # Prevents accessing other windows while this is open.

        # Window Details
        # ========================================================
        self.master.title("Add Feature")  # Window title
        self.master.geometry("250x100+300+200")  # default window size
        self.master.configure(bg="#038387")  # background color
        self.master.iconbitmap('C:\\Users\\elite\\Pictures\\Icons\\cog.ico')
        self.master.minsize(250, 100)

        # Label(s)
        # ========================================================
        self.name = tk.Label(self.master, text="Feat", bg="#038387", font=('Scaly Sans', 10)).grid(row=0, padx=(10, 0), pady=(10, 0))
        self.desc = tk.Label(self.master, text="Desc", bg="#038387", font=('Scaly Sans', 10)).grid(row=1, padx=(10, 0), pady=(5, 0))

        # Entries
        # ========================================================
        self.e_name = tk.Entry(self.master, font=('Scaly Sans', 10))
        self.e_desc = tk.Entry(self.master, font=('Scaly Sans', 10))
        self.e_name.grid(row=0, column=1, columnspan=2, pady=(10, 0))
        self.e_desc.grid(row=1, column=1, columnspan=2, pady=(5, 0))

        # Buttons
        # ========================================================
        self.bt_submit = tk.Button(  # for finalizing your inputs.
            master=self.master,
            text="Add",
            font=('Scaly Sans', 10),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=lambda: [
                self.submit(),
                self.master.destroy()
            ]
        )
        self.bt_cancel = tk.Button(  # for cancelling the request
            master=self.master,
            text="Cancel",
            font=('Scaly Sans', 10),
            bg="black",
            fg="white",
            width=5,
            height=0,
            command=self.master.destroy
        )
        self.bt_cancel.grid(row=2, column=1, pady=0, sticky=tk.N)
        self.bt_submit.grid(row=2, column=2, pady=0, sticky=tk.N)

    # Methods
    # ========================================================
    def submit(self):
        self.hero_list.append((self.e_name.get(), self.e_desc.get()))
        return -1
