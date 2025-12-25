import tkinter as tk
from tkinter import ttk

class GUI(tk.Tk):
    '''Handles GUI functions that interface with underlying app functions
    '''
    def __init__(self, app, config=None):
        super().__init__()

        # Basic GUI objects
        self.app = app
        self.notebook = ttk.Notebook(self)
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
        self.title(self.config['title'])
        self.geometry(self.config['size'])
        self.notebook.grid(row=0, column=0, sticky='NESW')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.notebook.columnconfigure(0, weight=1)
        self.notebook.rowconfigure(0, weight=1)

        # TAB START: TAB_1
        r_grid_0 = -1; c_grid_0 = -1
        tab_name = 'TAB_1'
        self.tabs[tab_name] = ttk.Frame(self.notebook)
        this_tab = self.tabs[tab_name]
        self.notebook.add(this_tab, text=tab_name)
        # Note: Do not add tab to .grid()
        
        # T1 FRAME START: FRAME_1
        r_grid_0 += 1; c_grid_0 += 1
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_FRAMENAME = ttk.LabelFrame(this_tab, text='frame_1')
        this_frame_1 = self.frame_FRAMENAME    # tier 1 frame
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=1)
        this_tab.columnconfigure(c_grid_0, weight=1)
        

 
        # T1 FRAME END: FRAME_1
        
        # TAB END: TAB_1


        # Go
        self.mainloop()
        return