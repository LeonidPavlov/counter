import tkinter.ttk as ttk
import tkinter as tk

from chooser.view.clock_label import ClockLabel
from chooser.root import Root
from chooser.view.calendar import Calendar


class Base(ttk.Frame):
    def __init__(self, **kwargs) -> None:
        super().__init__(Root.get_root(), **kwargs)
        self.grid()
        ClockLabel(self)
        Calendar(self, row=1)

