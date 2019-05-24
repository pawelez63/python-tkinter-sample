import tkinter as tk


class Start(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.image = tk.PhotoImage(file='home.png')
        panel = tk.Label(self, image=self.image)
        panel.pack(side="bottom", fill="both", expand="yes")
