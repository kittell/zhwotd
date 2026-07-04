import tkinter as tk
from tkinter import ttk
from datetime import date


class AdminTab(ttk.Frame):
    def __init__(self, main_window):
        super().__init__()
        self.main_window = main_window
        return