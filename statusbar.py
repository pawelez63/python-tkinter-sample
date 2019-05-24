import tkinter as tk


class Statusbar(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        self['bg'] = 'white'

        self.status = tk.StringVar()
        self.status_label = tk.Label(self, textvariable=self.status, bg='white')

        self.status_label.grid(row=0, column=0, sticky=tk.W, ipadx=10)

        self.set_status_label("Login successful!")

    def get_status_label(self):
        return self.status_label['text']

    def set_status_label(self, text):
        self.status.set(text)
