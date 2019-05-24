import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import datetime
import math


class DailyRates(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        self.today = datetime.date.today()
        self.last_day = self.today.replace(day=1) - datetime.timedelta(days=1)
        self.first_day = self.last_day.replace(day=1)
        dates = []
        PAD = 10

        while self.first_day <= self.last_day:
            dates.append(self.first_day.strftime("%d-%m-%Y"))
            self.first_day = self.first_day + datetime.timedelta(days=1)

        self.label_date = ttk.Label(self, text="Select date:")
        self.combo_date = ttk.Combobox(self, values=dates)

        self.label_date.grid(row=0, column=0, padx=PAD, pady=PAD)
        self.combo_date.grid(row=0, column=1, padx=PAD, pady=PAD)

        self.currencies = "THB", "USD", "AUD", "HKD", "CAD", "NZD", "SGD", "EUR", "HUF", "CHF", "GBP", "UAH", "JPY", "CZK", \
                     "DKK", "ISK", "NOK", "SEK", "HRK", "RON", "BGN", "TRY", "ILS", "CLP", "PHP", "MXN", "ZAR", "BRL", \
                     "MYR", "RUB", "IDR", "INR", "KRW", "CNY", "XDR"

        self.label = {}
        self.entry = {}

        i = 0
        for currency in self.currencies:
            self.label[currency] = ttk.Label(self, text=currency+":")
            self.entry[currency] = ttk.Entry(self, width=10)

            column_index = i % 3
            row_index = math.floor(i/3)

            self.label[currency].grid(row=row_index+2, column=column_index*3, padx=PAD, pady=PAD)
            self.entry[currency].grid(row=row_index + 2, column=column_index*3 + 1, padx=PAD, pady=PAD)
            i = i+1

        button_cancel = ttk.Button(self, text="Cancel")
        button_clear = ttk.Button(self, text="Clear")
        button_save = ttk.Button(self, text="Save", command=self.save_values)

        button_cancel.grid(row=math.floor(i / 3) + 3, column=5)
        button_clear.grid(row=math.floor(i / 3) + 3, column=6)
        button_save.grid(row=math.floor(i / 3) + 3, column=7)

        for i in range(0, 8):
            self.columnconfigure(i, minsize=100)

    def save_values(self):

        self.controller.controller.statusbar.set_status_label('Values saved properly!')

        for currency in self.currencies:
            self.entry[currency].delete(0, 'end')

        self.combo_date.set('')
        messagebox.showinfo('Information', 'The values has been saved properly!')
