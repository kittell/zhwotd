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
        today_str = date.today().isoformat()
        self.var['wotd_date'] = tk.StringVar(value=today_str)
        r_grid_2 += 0; c_grid_2 += 1
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

        # T1 FRAME START: STATS
        r_grid_0 += 1; c_grid_0 += 0
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_stats = ttk.LabelFrame(this_tab, text='Statistics')
        this_frame_1 = self.frame_stats
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=1)
        # this_tab.columnconfigure(c_grid_0, weight=1)
        # T1 FRAME END: STATS
        
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

        self.var['add'] = dict()

        # T2 FRAME START: ADD WORD ROW 1
        r_grid_1 += 1; c_grid_1 += 1
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordrow1 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordrow1
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        this_frame_1.columnconfigure(c_grid_1, weight=1)
        
        # T3 WIDGET START: ADD WORD WORD LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_addword_simplified = ttk.Label(this_frame_2, text='Word:')
        this_widget_3 = self.label_addword_simplified
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD WORD LABEL

        # T3 WIDGET START: ADD WORD WORD ENTRY
        self.var['add']['simplified'] = tk.StringVar(value='')
        r_grid_2 += 0; c_grid_2 += 1
        self.entry_addword_simplified = ttk.Entry(this_frame_2, textvariable=self.var['add']['simplified'], width=10)
        this_widget_3 = self.entry_addword_simplified
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: ADD WORD WORD ENTRY

        # T3 WIDGET START: ADD WORD PINYIN LABEL
        r_grid_2 += 0; c_grid_2 += 1
        self.label_addword_pinyin = ttk.Label(this_frame_2, text='Pinyin:')
        this_widget_3 = self.label_addword_pinyin
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD PINYIN LABEL

        # T3 WIDGET START: ADD WORD PINYIN ENTRY
        self.var['add']['pinyin'] = tk.StringVar(value='')
        r_grid_2 += 0; c_grid_2 += 1
        self.entry_addword_pinyin = ttk.Entry(this_frame_2, textvariable=self.var['add']['pinyin'], width=30)
        this_widget_3 = self.entry_addword_pinyin
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: ADD WORD PINYIN ENTRY

        # T3 WIDGET START: ADD WORD TRADITIONAL LABEL
        r_grid_2 += 0; c_grid_2 += 1
        self.label_addword_traditional = ttk.Label(this_frame_2, text='Traditional:')
        this_widget_3 = self.label_addword_traditional
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD TRADITIONAL LABEL

        # T3 WIDGET START: ADD WORD TRADITIONAL ENTRY
        self.var['add']['traditional'] = tk.StringVar(value='')
        r_grid_2 += 0; c_grid_2 += 1
        self.entry_addword_traditional = ttk.Entry(this_frame_2, textvariable=self.var['add']['traditional'], width=10)
        this_widget_3 = self.entry_addword_traditional
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: ADD WORD TRADITIONAL ENTRY

        # T3 WIDGET START: ADD WORD HSK LABEL
        r_grid_2 += 0; c_grid_2 += 1
        self.label_addword_hsk = ttk.Label(this_frame_2, text='HSK Level:')
        this_widget_3 = self.label_addword_hsk
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD HSK LABEL

        # T3 WIDGET START: ADD WORD HSK ENTRY
        self.var['add']['hsk'] = tk.IntVar(value=0)
        r_grid_2 += 0; c_grid_2 += 1
        self.entry_addword_hsk = ttk.Entry(this_frame_2, textvariable=self.var['add']['hsk'], width=5)
        this_widget_3 = self.entry_addword_hsk
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD HSK ENTRY

        # T2 FRAME END: ADD WORD ROW 1

        # T2 FRAME START: ADD WORD ROW 2
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordrow2 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordrow2
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NEW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: ADD WORD DEFINITION LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_addword_definition = ttk.Label(this_frame_2, text='Definition:')
        this_widget_3 = self.label_addword_definition
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD DEFINITION LABEL

        # T3 WIDGET START: ADD WORD DEFINITION ENTRY
        self.var['add']['definition'] = tk.StringVar(value='')
        r_grid_2 += 0; c_grid_2 += 1
        self.entry_addword_definition = ttk.Entry(this_frame_2, textvariable=self.var['add']['definition'])
        this_widget_3 = self.entry_addword_definition
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        # this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: ADD WORD DEFINITION ENTRY
        # T2 FRAME END: ADD WORD ROW 2

        # T2 FRAME START: ADD WORD ROW 3
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordrow3 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordrow3
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: ADD WORD EXAMPLE LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_addword_example = ttk.Label(this_frame_2, text='Example:')
        this_widget_3 = self.label_addword_example
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD EXAMPLE LABEL

        # T3 WIDGET START: ADD WORD EXAMPLE ENTRY
        self.var['add']['example'] = tk.StringVar(value='')
        r_grid_2 += 0; c_grid_2 += 1
        self.entry_addword_example = ttk.Entry(this_frame_2, textvariable=self.var['add']['example'])
        this_widget_3 = self.entry_addword_example
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        # this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T2 FRAME END: ADD WORD ROW 3

        # T2 FRAME START: ADD WORD ROW 4
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordrow4 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordrow4
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: ADD WORD NOTES LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_addword_notes = ttk.Label(this_frame_2, text='Notes:')
        this_widget_3 = self.label_addword_notes
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD NOTES LABEL

        # T3 WIDGET START: ADD WORD NOTES ENTRY
        self.var['add']['notes'] = tk.StringVar(value='')
        r_grid_2 += 0; c_grid_2 += 1
        self.entry_addword_notes = ttk.Entry(this_frame_2, textvariable=self.var['add']['notes'])
        this_widget_3 = self.entry_addword_notes
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        # this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T2 FRAME END: ADD WORD ROW 4

        # T2 FRAME START: ADD WORD CHECK
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordcheck = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordcheck
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)
        
        # T3 WIDGET START: ADD WORD CHECK BUTTON
        r_grid_2 += 1; c_grid_2 += 1
        self.button_addword_check = ttk.Button(this_frame_2, text='Check word', command=self._callback_button_addword_check)
        this_widget_3 = self.button_addword_check
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD CHECK BUTTON

        # T3 WIDGET START: ADD WORD CHECK RESULTS
        self.var['add']['checkresults'] = tk.StringVar(value='')
        r_grid_2 += 0; c_grid_2 += 1
        self.label_addword_checkresults = ttk.Label(this_frame_2, textvariable=self.var['add']['checkresults'])
        this_widget_3 = self.label_addword_checkresults
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        # this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: ADD WORD CHECK RESULTS
        # T2 FRAME END: ADD WORD CHECK

        # T2 FRAME START: ADD WORD ADD
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_addwordadd = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_addwordadd
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: ADD WORD ADD BUTTON
        r_grid_2 += 1; c_grid_2 += 1
        self.button_addword_add = ttk.Button(this_frame_2, text='Add word', command=self._callback_button_addword_add)
        this_widget_3 = self.button_addword_add
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='E')
        # this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: ADD WORD ADD BUTTON

        # T3 WIDGET START: ADD WORD ADD RESULTS
        self.var['add']['addresults'] = tk.StringVar(value='')
        r_grid_2 += 0; c_grid_2 += 1
        self.label_addword_addresults = ttk.Label(this_frame_2, textvariable=self.var['add']['addresults'])
        this_widget_3 = self.label_addword_addresults
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        # this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: ADD WORD ADD RESULTS
        # T2 FRAME END: ADD WORD ADD
        # T1 FRAME END: ADD WORD

        # T1 FRAME START: EDIT WORD
        r_grid_0 += 1; c_grid_0 += 0
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_editword = ttk.LabelFrame(this_tab, text='Edit word')
        this_frame_1 = self.frame_editword
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=1)
        # this_tab.columnconfigure(c_grid_0, weight=1)

        self.var['edit'] = dict()

        # T2 FRAME START: SEARCH WORD
        r_grid_1 += 1; c_grid_1 += 1
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_searchword = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_searchword
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        this_frame_1.columnconfigure(c_grid_1, weight=1)
        # T2 FRAME END: SEARCH WORD

        # T3 WIDGET START: SEARCH WORD LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_searchword = ttk.Label(this_frame_2, text='Search word:')
        this_widget_3 = self.label_searchword
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: SEARCH WORD LABEL

        # T3 WIDGET START: SEARCH WORD ENTRY
        r_grid_2 += 0; c_grid_2 += 1
        self.var['edit']['searchword'] = tk.StringVar(value='')
        self.entry_searchword = ttk.Entry(this_frame_2, textvariable=self.var['edit']['searchword'], width=20)
        this_widget_3 = self.entry_searchword
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        # this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: SEARCH WORD ENTRY

        # T3 WIDGET START: SEARCH WORD BUTTON
        r_grid_2 += 0; c_grid_2 += 1
        self.button_searchword = ttk.Button(this_frame_2, text='Search', command=self._callback_button_searchword)
        this_widget_3 = self.button_searchword
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='E')
        # this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: SEARCH WORD BUTTON

        # T2 FRAME END: SEARCH WORD

        # T2 FRAME START: SEARCH WORD RESULTS
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_searchwordresults = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_searchwordresults
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)
        
        # T3 WIDGET START: SEARCH WORD RESULTS LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.var['edit']['searchresults'] = tk.StringVar(value='')
        self.label_searchword_results = ttk.Label(this_frame_2, textvariable=self.var['edit']['searchresults'])
        this_widget_3 = self.label_searchword_results
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: SEARCH WORD RESULTS LABEL
        # T2 FRAME END: SEARCH WORD RESULTS

        # T2 FRAME START: EDIT WORD ROW 1
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_editwordrow1 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_editwordrow1
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        this_frame_1.columnconfigure(c_grid_1, weight=1)
        
        # T3 WIDGET START: EDIT WORD WORD LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_editword_simplified = ttk.Label(this_frame_2, text='Word:')
        this_widget_3 = self.label_editword_simplified
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: EDIT WORD WORD LABEL

        # T3 WIDGET START: EDIT WORD WORD ENTRY
        r_grid_2 += 0; c_grid_2 += 1
        self.var['edit']['simplified'] = tk.StringVar(value='')
        self.entry_editword_simplified = ttk.Entry(this_frame_2, textvariable=self.var['edit']['simplified'], width=10)
        this_widget_3 = self.entry_editword_simplified
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: EDIT WORD WORD ENTRY

        # T3 WIDGET START: EDIT WORD PINYIN LABEL
        r_grid_2 += 0; c_grid_2 += 1
        self.label_editword_pinyin = ttk.Label(this_frame_2, text='Pinyin:')
        this_widget_3 = self.label_editword_pinyin
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: EDIT WORD PINYIN LABEL

        # T3 WIDGET START: EDIT WORD PINYIN ENTRY
        r_grid_2 += 0; c_grid_2 += 1
        self.var['edit']['pinyin'] = tk.StringVar(value='')
        self.entry_editword_pinyin = ttk.Entry(this_frame_2, textvariable=self.var['edit']['pinyin'], width=30)
        this_widget_3 = self.entry_editword_pinyin
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: EDIT WORD PINYIN ENTRY

        # T3 WIDGET START: EDIT WORD TRADITIONAL LABEL
        r_grid_2 += 0; c_grid_2 += 1
        self.label_editword_traditional = ttk.Label(this_frame_2, text='Traditional:')
        this_widget_3 = self.label_editword_traditional
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: EDIT WORD TRADITIONAL LABEL

        # T3 WIDGET START: EDIT WORD TRADITIONAL ENTRY
        r_grid_2 += 0; c_grid_2 += 1
        self.var['edit']['traditional'] = tk.StringVar(value='')
        self.entry_editword_traditional = ttk.Entry(this_frame_2, textvariable=self.var['edit']['traditional'], width=10)
        this_widget_3 = self.entry_editword_traditional
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: EDIT WORD TRADITIONAL ENTRY

        # T3 WIDGET START: EDIT WORD HSK LABEL
        r_grid_2 += 0; c_grid_2 += 1
        self.label_editword_hsk = ttk.Label(this_frame_2, text='HSK Level:')
        this_widget_3 = self.label_editword_hsk
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='W')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: EDIT WORD HSK LABEL

        # T3 WIDGET START: EDIT WORD HSK ENTRY
        r_grid_2 += 0; c_grid_2 += 1
        self.var['edit']['hsk'] = tk.IntVar(value=0)
        self.entry_editword_hsk = ttk.Entry(this_frame_2, textvariable=self.var['edit']['hsk'], width=5)
        this_widget_3 = self.entry_editword_hsk
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='EW')
        this_frame_2.rowconfigure(r_grid_2, weight=0)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: EDIT WORD HSK ENTRY

        # T2 FRAME END: EDIT WORD ROW 1

        # T2 FRAME START: EDIT WORD ROW 2
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_editwordrow2 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_editwordrow2
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NEW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: EDIT WORD DEFINITION LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_editword_definition = ttk.Label(this_frame_2, text='Definition:')
        this_widget_3 = self.label_editword_definition
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: EDIT WORD DEFINITION LABEL

        # T3 WIDGET START: EDIT WORD DEFINITION ENTRY
        r_grid_2 += 0; c_grid_2 += 1
        self.var['edit']['definition'] = tk.StringVar(value='')
        self.entry_editword_definition = ttk.Entry(this_frame_2, textvariable=self.var['edit']['definition'])
        this_widget_3 = self.entry_editword_definition
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        # this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T3 WIDGET END: EDIT WORD DEFINITION ENTRY
        # T2 FRAME END: EDIT WORD ROW 2

        # T2 FRAME START: EDIT WORD ROW 3
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_editwordrow3 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_editwordrow3
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: EDIT WORD EXAMPLE LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_editword_example = ttk.Label(this_frame_2, text='Example:')
        this_widget_3 = self.label_editword_example
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: EDIT WORD EXAMPLE LABEL

        # T3 WIDGET START: EDIT WORD EXAMPLE ENTRY
        r_grid_2 += 0; c_grid_2 += 1
        self.var['edit']['example'] = tk.StringVar(value='')
        self.entry_editword_example = ttk.Entry(this_frame_2, textvariable=self.var['edit']['example'])
        this_widget_3 = self.entry_editword_example
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        # this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T2 FRAME END: EDIT WORD ROW 3

        # T2 FRAME START: EDIT WORD ROW 4
        r_grid_1 += 1; c_grid_1 += 0
        r_grid_2 = -1; c_grid_2 = -1
        self.frame_editwordrow4 = ttk.Frame(this_frame_1)
        this_frame_2 = self.frame_editwordrow4
        this_frame_2.grid(row=r_grid_1, column=c_grid_1, sticky='NESW')
        this_frame_1.rowconfigure(r_grid_1, weight=0)
        # this_frame_1.columnconfigure(c_grid_1, weight=1)

        # T3 WIDGET START: EDIT WORD NOTES LABEL
        r_grid_2 += 1; c_grid_2 += 1
        self.label_editword_notes = ttk.Label(this_frame_2, text='Notes:')
        this_widget_3 = self.label_editword_notes
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NW')
        this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=0)
        # T3 WIDGET END: EDIT WORD NOTES LABEL

        # T3 WIDGET START: EDIT WORD NOTES ENTRY
        r_grid_2 += 0; c_grid_2 += 1
        self.var['edit']['notes'] = tk.StringVar(value='')
        self.entry_editword_notes = ttk.Entry(this_frame_2, textvariable=self.var['edit']['notes'])
        this_widget_3 = self.entry_editword_notes
        this_widget_3.grid(row=r_grid_2, column=c_grid_2, sticky='NESW')
        # this_frame_2.rowconfigure(r_grid_2, weight=1)
        this_frame_2.columnconfigure(c_grid_2, weight=1)
        # T2 FRAME END: EDIT WORD ROW 4
        # T1 FRAME END: EDIT WORD

        # T1 FRAME START: UPLOAD CHANGES
        r_grid_0 += 1; c_grid_0 += 0
        r_grid_1 = -1; c_grid_1 = -1
        self.frame_uploadchanges = ttk.LabelFrame(this_tab, text='Upload changes')
        this_frame_1 = self.frame_uploadchanges
        this_frame_1.grid(row=r_grid_0, column=c_grid_0, sticky='NESW')
        this_tab.rowconfigure(r_grid_0, weight=1)
        # this_tab.columnconfigure(c_grid_0, weight=1)
        # T1 FRAME END: UPLOAD CHANGES
        # TAB FRAME END: ACTION


        # Go
        self.mainloop()
        return
    
    def _callback_button_addword_check(self):
        word = self.var['add']['simplified'].get().strip()
        print('word:',word)

        if not word:
            self.var['add']['checkresults'].set("Enter a word first.")
            return

        result = self.app.find_word(word)

        if result is None:
            self.var['add']['checkresults'].set("Word not found. You may add it.")
        else:
            self.var['add']['checkresults'].set("Word already exists.")

        
        return
    
    def _callback_button_addword_add(self):
        data = {
            "simplified": self.var['add']['simplified'].get().strip(),
            "pinyin": self.var['add']['pinyin'].get().strip(),
            "traditional": self.var['add']['traditional'].get().strip(),
            "hsk": self.var['add']['hsk'].get(),
            "definition": self.var['add']['definition'].get().strip(),
            "example": self.var['add']['example'].get().strip(),
            "notes": self.var['add']['notes'].get().strip(),
        }

        if not data["simplified"]:
            self.var['add']['addresults'].set("Word cannot be empty.")
            return

        result = self.app.add_word(data)

        if result is None:
            self.var['add']['addresults'].set("Failed to add word.")
        else:
            self.var['add']['addresults'].set("Word added successfully.")

    
    def _callback_button_searchword(self):
        word = self.var['edit']['searchword'].get().strip()

        if not word:
            self.var['edit']['searchresults'].set("Enter a word to search.")
            return

        result = self.app.find_word(word)

        if result is None:
            self.var['edit']['searchresults'].set("Word not found.")
            return

        # Populate edit fields
        self.var['add']['simplified'].set(result["simplified"])
        self.var['add']['pinyin'].set(result["pinyin"])
        self.var['add']['traditional'].set(result["traditional"])
        self.var['add']['hsk'].set(result["hsk"])
        self.var['add']['definition'].set(result["definition"])
        self.var['add']['example'].set(result["example"])
        self.var['add']['notes'].set(result["notes"])

        self.var['edit']['searchresults'].set("Word loaded for editing.")

    
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
