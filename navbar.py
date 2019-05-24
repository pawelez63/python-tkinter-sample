import tkinter as tk
from tkinter import ttk
from start import Start
from daily_rates import DailyRates
from cashflows import Cashflows
from daily_reports import DailyReports


class Navbar(ttk.Notebook):
    def __init__(self, parent, controller):
        ttk.Notebook.__init__(self, parent)
        self.controller = controller
        self['style'] = 'lefttab.TNotebook'

        self.tab1_image = tk.PhotoImage(file='start.png', width=60)
        self.tab2_image = tk.PhotoImage(file='daily_rates.png', width=60)
        self.tab3_image = tk.PhotoImage(file='dossiers.png', width=60)
        self.tab4_image = tk.PhotoImage(file='networks.png', width=60)
        self.tab5_image = tk.PhotoImage(file='cash_flows.png', width=60)
        self.tab6_image = tk.PhotoImage(file='statements.png', width=60)
        self.tab7_image = tk.PhotoImage(file='daily_reports.png', width=60)
        self.tab8_image = tk.PhotoImage(file='settings.png', width=60)
        self.tab9_image = tk.PhotoImage(file='audit_trail.png', width=60)

        self.f1 = Start(parent.master, self)
        self.f2 = DailyRates(parent.master, self)
        self.f3 = tk.Frame(self)
        self.f4 = tk.Frame(self)
        self.f5 = Cashflows(parent.master, self)
        self.f6 = tk.Frame(self)
        self.f7 = DailyReports(parent.master, self)
        self.f8 = tk.Frame(self)
        self.f9 = tk.Frame(self)

        self.add(self.f1, text='Start', image=self.tab1_image, compound=tk.TOP)
        self.add(self.f2, text='Daily Rates', image=self.tab2_image, compound=tk.TOP)
        self.add(self.f3, text='Dossiers', image=self.tab3_image, compound=tk.TOP)
        self.add(self.f4, text='Networks', image=self.tab4_image, compound=tk.TOP)
        self.add(self.f5, text='Cash flows', image=self.tab5_image, compound=tk.TOP)
        self.add(self.f6, text='Statements', image=self.tab6_image, compound=tk.TOP)
        self.add(self.f7, text='Daily Reports', image=self.tab7_image, compound=tk.TOP)
        self.add(self.f8, text='Settings', image=self.tab8_image, compound=tk.TOP)
        self.add(self.f9, text='Audit Trail', image=self.tab9_image, compound=tk.TOP)
