import tkinter as tk
import csv
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askopenfilename


class Cashflows(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.choose_file_button = ttk.Button(self, text="Import csv file", command=self.load_button)
        self.validate_button = ttk.Button(self, text="Validate data", command=self.validate_button)
        self.clear_button = ttk.Button(self, text="Clear", command=self.clear_button)
        self.choose_file_button.grid(row=0, column=0, padx=10, pady=10)
        self.validate_button.grid(row=0, column=1, padx=10, pady=10)
        self.clear_button.grid(row=0, column=2, padx=10, pady=10)
        self.data = []

        for counter in range(0, 4):
            self.columnconfigure(counter, minsize=150)

        self.label = {}
        self.entry = {}
        self.progress_bar = None

    def load_button(self):
        self.controller.controller.statusbar.set_status_label('Choosing cashflow csv file...')

        source_file = askopenfilename()
        with open(source_file, mode='r') as infile:
            reader = csv.reader(infile)
            self.data = [[rows[0], rows[6], rows[7], rows[8]] for rows in reader]

            for i in range(0, 4):
                self.label[0] = ttk.Label(self, text=self.data[0][i])
                self.label[0].grid(row=2, column=i)

                for j in range(1, max(len(self.data), 48)):
                    self.entry[str(j) + '-' + str(i)] = ttk.Entry(self, width=20)
                    self.entry[str(j) + '-' + str(i)].insert(0, self.data[j][i])
                    self.entry[str(j) + '-' + str(i)].grid(row=j+2, column=i, padx=5, pady=5)

        self.controller.controller.statusbar.set_status_label('Data loaded successfully!')

    def clear_button(self):
        for i in range(0, 4):
            for j in range(1, max(len(self.data), 48)):
                self.entry[str(j) + '-' + str(i)].destroy()

        self.controller.controller.statusbar.set_status_label('Entries have been cleared!')

    def validate_button(self):
        self.controller.controller.statusbar.set_status_label('Data are being validated...')

        self.progress_bar = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=150, mode='determinate')
        self.progress_bar.grid(row=0, column=3, columnspan=2, padx=10, pady=10)
        self.progress_bar['maximum'] = 50
        self.progress_bar.start()
        self.master.after(2000, self.stop_bar)

    def stop_bar(self):
        self.progress_bar.stop()
        self.progress_bar['value'] = 100
        self.controller.controller.statusbar.set_status_label('Validation of data finished!')
        messagebox.showinfo('Information', 'Data validated!')
        self.progress_bar.destroy()
