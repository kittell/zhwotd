import tkinter as tk
from tkinter import ttk
from datetime import date
from typing import Literal

from zhwotd.ui.dashboard import DashboardTab
from zhwotd.ui.action import ActionTab

class MainWindow():
    '''Handles GUI functions that interface with underlying app functions
    '''
    def __init__(self, app, config=None):
        root = tk.Tk()

        # Basic GUI objects
        self.app = app
        self.tabs = dict()
        self.var = dict()

        # GUI configuration defaults
        if config is None:
            self.config = dict()
        else:
            self.config = config
        if 'title' not in self.config:
            self.config['title'] = ''
        if 'size' not in self.config:
            self.config['size'] = '800x600'

        # Display basic items
        root.title(self.config['title'])
        root.geometry(self.config['size'])
        self.notebook = ttk.Notebook(root)
        self.notebook.grid(row=0, column=0, sticky='NESW')
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)
        # self.notebook.columnconfigure(0, weight=1)
        # self.notebook.rowconfigure(0, weight=1)

        # TAB START: DASHBOARD
        r_grid_0 = -1; c_grid_0 = -1
        tab_name = 'Dashboard'
        self.tabs[tab_name] = DashboardTab(self)
        self.notebook.add(self.tabs[tab_name], text=tab_name)

        # TAB START: ACTION
        r_grid_0 = -1; c_grid_0 = -1
        tab_name = 'Action'
        self.tabs[tab_name] = ActionTab(self)
        self.notebook.add(self.tabs[tab_name], text=tab_name)

        # Go
        root.mainloop()
        return
    
    