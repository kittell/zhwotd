import tkinter as tk
from tkinter import ttk
from datetime import date
from typing import Literal

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
        this_frame_1 = self.frame_wotd
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=0)
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
        self.textscrollbar_wotd = TextScrollbar(this_frame_2, state='disabled')
        this_frame_3 = self.textscrollbar_wotd
        this_frame_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: WOTD TEXTBOX
        # T2 FRAME END: WOTD TEXT

        # T2 FRAME START: WOTD NAV
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_wotdnav = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_wotdnav
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='S')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: PREVIOUS DAY BUTTON
        r_grid_2 += 1; c_grid_2 += 1
        self.button_wotdprev = ttk.Button(this_frame_2, text='<< Previous', command=self._callback_button_wotdprev)
        this_widget_3 = self.button_wotdprev
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: PREVIOUS DAY BUTTON

        # T3 WIDGET START: WOTD DATE
        # TODO: start as entry; change to date picker later
        r_grid_2 += 0; c_grid_2 += 1
        today_str = date.today().isoformat()
        self.var['wotd_date'] = tk.StringVar(value=today_str)
        self.entry_wotddate = ttk.Entry(this_frame_2, textvariable=self.var['wotd_date'], width=12)
        this_widget_3 = self.entry_wotddate
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        # this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: WOTD DATE

        # T3 WIDGET START: NEXT DAY BUTTON
        r_grid_2 += 0; c_grid_2 += 1
        self.button_wotdnext = ttk.Button(this_frame_2, text='Next >>', command=self._callback_button_wotdnext)
        this_widget_3 = self.button_wotdnext
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='E')
        # this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: NEXT DAY BUTTON
        # T2 FRAME END: WOTD NAV
 
        # T1 FRAME END: WORD OF THE DAY
        
        # TAB END: DASHBOARD


        # TAB START: ACTION
        r_grid_0 = -1; c_grid_0 = -1
        tab_name = 'Action'
        self.tabs[tab_name] = ttk.Frame(self.notebook)
        this_tab = self.tabs[tab_name]
        self.notebook.add(this_tab, text=tab_name)
        # Note: Do not add tab to .grid()

        # T1 FRAME START: ADD WORD
        r_grid_0 += 1; c_grid_0 += 1
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_addword = ttk.LabelFrame(this_tab, text='Add word to dictionary')
        this_frame_1 = self.frame_addword
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=1)
        this_tab.columnconfigure(c_grid_0, weight=1)

        # T2 FRAME START: ADD WORD ROW 1
        r_grid_1 += 1; c_grid_1 += 1
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordrow1 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordrow1
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=1)
        this_frame_1.columnconfigure(c_grid_1, weight=1)
        # T2 FRAME END: ADD WORD ROW 1

        # T2 FRAME START: ADD WORD ROW 2
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordrow2 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordrow2
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=1)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)
        # T2 FRAME END: ADD WORD ROW 2

        # T2 FRAME START: ADD WORD ROW 3
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordrow3 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordrow3
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=1)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)
        # T2 FRAME END: ADD WORD ROW 3

        # T2 FRAME START: ADD WORD ROW 4
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordrow4 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordrow4
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=1)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)
        # T2 FRAME END: ADD WORD ROW 4
        # T1 END: ADD WORD
        # TAB END: ACTION


        # Go
        self.mainloop()
        return
    
    def _callback_button_wotdprev(self):
        # TODO _callback_button_wotdprev
        return
    
    def _callback_button_wotdnext(self):
        # TODO _callback_button_wotdnext
        return
    
class TextScrollbar(ttk.Frame):
    def __init__(
            self, 
            parent: tk.Misc, 
            orient: Literal['vertical', 'horizontal', 'both'] = 'vertical', 
            height: int=3,
            state: Literal['normal', 'disabled'] = 'normal'
            ):
        
        super().__init__(parent)

        # Scrollbar placement and Text word wrapping logic
        vertical = False
        horizontal = False
        wrap='word'
        if orient == 'vertical' or orient == 'both':
            vertical = True
        if orient == 'horizontal' or orient == 'both':
            horizontal = True
            wrap='none'     # no word wrapping with horizontal scrollbar

        # Text widget
        self.text = tk.Text(self, wrap=wrap, height=height, state=state)
        self.text.grid(row=0, column=0, sticky='NESW')
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

        # Scrollbar widget
        if vertical:
            self.scrollbar_vertical = ttk.Scrollbar(self, orient='vertical', command=self.text.yview)
            self.scrollbar_vertical.grid(row=0, column=1, sticky='NS')
            self.columnconfigure(1, weight=0)
            self.text.configure(yscrollcommand=self.scrollbar_vertical.set) # Connect scrollbar to text

        if horizontal:
            self.scrollbar_horizontal = ttk.Scrollbar(self, orient='vertical', command=self.text.xview)
            self.scrollbar_horizontal.grid(row=1, column=0, sticky='EW')
            self.rowconfigure(1, weight=0)
            self.text.configure(xscrollcommand=self.scrollbar_horizontal.set)   # Connect scrollbar to text

        return
