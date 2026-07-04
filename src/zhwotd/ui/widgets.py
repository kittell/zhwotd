import tkinter as tk
from tkinter import ttk
from typing import Literal

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