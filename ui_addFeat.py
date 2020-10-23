
import tkinter as tk


class AddFeat:
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
