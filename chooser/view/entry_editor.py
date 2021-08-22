import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
import tkinter as tk


class Editor(tk.Toplevel):
    def __init__(self, title: str = 'edit text', 
                                            text: str = 'default') -> None:
        super().__init__()
        self.title(title)
        self.grid()

