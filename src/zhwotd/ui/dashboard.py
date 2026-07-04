import tkinter as tk
from tkinter import ttk
from datetime import date
from zhwotd.ui.widgets import TextScrollbar


class DashboardTab(ttk.Frame):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window

        r_grid_0: int = -1
        c_grid_0: int = -1
        r_grid_1: int = -1
        c_grid_1: int = -1
        
        # T1 FRAME START: WORD OF THE DAY

        r_grid_0 += 1; c_grid_0 += 1
        self.frame_wotd = ttk.Labelframe(self, text='Word of the Day')
        this_frame_1 = self.frame_wotd
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        self.rowconfigure(r_grid_0, weight=0)
        self.columnconfigure(c_grid_0, weight=1)
        
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
        today_str = date.today().isoformat()
        self.main_window.var['wotd_date'] = tk.StringVar(value=today_str)
        r_grid_2 += 0; c_grid_2 += 1
        self.entry_wotddate = ttk.Entry(this_frame_2, textvariable=self.main_window.var['wotd_date'], width=12)
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

        # T1 FRAME START: STATS
        r_grid_0 += 1; c_grid_0 += 0
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_stats = ttk.LabelFrame(self, text='Statistics')
        this_frame_1 = self.frame_stats
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        self.rowconfigure(r_grid_0, weight=1)
        # this_tab.columnconfigure(c_grid_0, weight=1)
        # T1 FRAME END: STATS
        
        # TAB END: DASHBOARD

        return
    
    def _callback_button_wotdprev(self):
        # TODO _callback_button_wotdprev
        return
    
    def _callback_button_wotdnext(self):
        # TODO _callback_button_wotdnext
        return