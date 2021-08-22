import tkinter.ttk as ttk
import tkinter as tk

from chooser.view.clock_label import ClockLabel
from chooser.view.root import Root

class Base(ttk.Frame):

    def __init__(self, **kwargs) -> None:
        super().__init__(Root.get_root(), **kwargs)
        self.grid()
        b = ttk.Button(self, text = 'NAHUY', command = Root.destroy_application)
        b.grid()
        
    
