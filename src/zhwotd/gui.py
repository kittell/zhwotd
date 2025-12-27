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
        if config is None or 'gui' not in config:
            self.config = dict()
        else:
            self.config = config['gui']
        if 'title' not in self.config:
            self.config['gui']['title'] = ''
        if 'size' not in self.config:
            self.config['gui']['size'] = '800x600'

        # Display basic items
        self.title(self.config['title'])
        self.geometry(self.config['size'])
        self.notebook.grid(row=0, column=0, sticky='NESW')
        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)
        self.notebook.columnconfigure(0, weight=1)
        self.notebook.rowconfigure(0, weight=1)

        # TAB START: DASHBOARD
        r_grid_0 = -1; c_grid_0 = -1
        tab_name = 'Dashboard'
        self.tabs[tab_name] = ttk.Frame(self.notebook)
        this_tab = self.tabs[tab_name]
        self.notebook.add(this_tab, text=tab_name)
        # Note: Do not add tab to .grid()
        
        # T1 FRAME START: WORD OF THE DAY

        r_grid_0 += 1; c_grid_0 += 1
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_wotd = ttk.LabelFrame(this_tab, text='Word of the Day')
        this_frame_1 = self.frame_wotd    # tier 1 frame
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=1)
        this_tab.columnconfigure(c_grid_0, weight=1)
        
        # T2 FRAME START: WOTD TEXT
        r_grid_1 += 1; c_grid_1 += 1
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_wotdtext = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_wotdtext
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=1)
        this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: WOTD TEXTBOX
        r_grid_2 += 1; c_grid_2 += 1
        self.textboxscrollbar_wotd = TextboxScrollbar(this_frame_2)
        this_frame_3 = self.textboxscrollbar_wotd
        this_frame_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: WOTD TEXTBOX
        # T2 FRAME END: WOTD TEXT

        # T2 FRAME START: WOTD NAV
        r_grid_1 += 1; c_grid_1 += 0
        self.frame_wotdnav = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_wotdnav
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=1)
        this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: PREVIOUS DAY BUTTON
        # T3 WIDGET END: PREVIOUS DAY BUTTON

        # T3 WIDGET START: WOTD DATE
        # T3 WIDGET END: WOTD DATE

        # T3 WIDGET START: NEXT DAY BUTTON
        # T3 WIDGET END: NEXT DAY BUTTON
        # T2 FRAME END: WOTD NAV
 
        # T1 FRAME END: WORD OF THE DAY
        
        # TAB END: DASHBOARD


        # Go
        self.mainloop()
        return
    
class TextboxScrollbar(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)
        # TODO

        return
