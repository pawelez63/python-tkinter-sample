import tkinter as tk
from tkinter import ttk

from topbar import Topbar
from navbar import Navbar
from statusbar import Statusbar
from threaded_task import ThreadedTask


class Root:
    def __init__(self, master):
        self.master = master
        super(Root, self).__init__()
        master.title("Exchange Rates 4.07 PROD")
        master.minsize(1200, 800)
        master.iconbitmap('window_icon.ico')
        master.configure(bg='#FFFFFF')

        self.win = tk.Toplevel()
        self.login_popup()

        root.withdraw()

        self.style = ttk.Style(root)
        self.style.configure('lefttab.TNotebook', tabposition='wn', bg='#FFFFFF')

        self.topbar = Topbar(master, self)
        self.navbar = Navbar(master, self)
        self.statusbar = Statusbar(master, self)
        self.threadedtasks = ThreadedTask(master, self)

        self.statusbar.pack(side=tk.BOTTOM, fill=tk.X, pady=2)
        self.topbar.pack(side=tk.TOP, pady=5)
        self.navbar.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

    def login_popup(self):
        self.win.wm_title("Log in - Exchange Rates")
        self.win.attributes('-topmost', 'true')

        user_label = tk.Label(self.win, text="User name:")
        user_textbox = ttk.Entry(self.win, width=30)
        pass_label = tk.Label(self.win, text="Password:")
        pass_textbox = ttk.Entry(self.win, show="*", width=30)

        login_button = ttk.Button(self.win, text="Log in", command=self.login_success)
        cancel_butoon = ttk.Button(self.win, text="Cancel")

        user_label.grid(row=0, column=0, padx=10, ipady=10)
        user_textbox.grid(row=0, column=1, columnspan=3, padx=10, pady=10)
        pass_label.grid(row=1, column=0, padx=10, pady=10)
        pass_textbox.grid(row=1, column=1, columnspan=3, padx=10, pady=10)
        cancel_butoon.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
        login_button.grid(row=2, column=2, columnspan=2, padx=10, pady=10)

    def login_success(self):
        self.win.destroy()
        root.deiconify()


if __name__ == '__main__':
    root = tk.Tk()
    my_gui = Root(root)

    root.mainloop()
