import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tkinter.filedialog import askdirectory

PAD = 10


class DailyReports(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller


        self.reports = "Average currency rates", "Historical currency rates", "Dossier list", "Internal dossiers", \
                       "Network list", "Cash flows - row data", "Calculated cashflows in EUR", \
                       "Calculated cashflows in USD", "Statements upload", "User defined: Daily report", \
                       "User defined: Monthly report"

        self.label_date = ttk.Label(self, text="Select report:")
        self.combo_date = ttk.Combobox(self, values=self.reports, width=50)
        self.validate_button = ttk.Button(self, text="Generate data", command=self.validate_button)
        self.combo_date.bind("<<ComboboxSelected>>", self.show_options)

        self.label_date.grid(row=0, column=0, padx=PAD, pady=PAD)
        self.combo_date.grid(row=0, column=1, padx=PAD, pady=PAD)
        self.validate_button.grid(row=0, column=2, padx=10, pady=10)
        self.progress_bar = None

        self.label = {}
        self.combobox = {}

    def show_options(self, value):
        options = [
            ["Format", ["xlsx", "xls", "csv", "pdf"]],
            ["Language", ["English", "German", "Finnish"]],
            ["Layout", ["Horizontal", "Vertical"]]
        ]

        print(value)

        i = 0
        for element in options:
            self.label[i] = ttk.Label(self, text=element[0])
            self.combobox[i] = ttk.Combobox(self, values=element[1], width=20)

            self.label[i].grid(row=i+2, column=0, padx=PAD, pady=PAD)
            self.combobox[i].grid(row=i + 2, column=1, padx=PAD, pady=PAD)
            self.combobox[i].set(element[1][0])
            i = i+1

    def validate_button(self):
        print(askdirectory(title="Select destination folder..."))
        self.controller.controller.statusbar.set_status_label('Generating report...')

        self.progress_bar = ttk.Progressbar(self, orient=tk.HORIZONTAL, length=150, mode='determinate')
        self.progress_bar.grid(row=0, column=3, columnspan=2, padx=10, pady=10)
        self.progress_bar['maximum'] = 200
        self.progress_bar.start()
        self.master.after(8000, self.stop_bar)

    def stop_bar(self):
        self.progress_bar.stop()
        self.progress_bar['value'] = 200
        self.controller.controller.statusbar.set_status_label('Report generated successfully!')
        messagebox.showinfo('Information', 'Report generated!')
        self.progress_bar.destroy()
