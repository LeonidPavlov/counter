import tkinter.ttk as ttk
from datetime import datetime as dt
import tkinter as tk


class Base(ttk.LabelFrame):
    
    @staticmethod
    def going_watch_in_label(container, label: ttk.Label,
                             format_string: str = '%H %M %S') -> None:
        def count() -> None:
            time: dt = dt.now()
            label.config(text = time.strftime(format_string))
            label.after(1000, count)
        count()

    def __init__(self, root, **kwargs):
        super().__init__(root, text='pick date and time', **kwargs)
        self.__label = ttk.Label(self, text='something wrong')
        self.pack()
        self.__label.grid(column=0, row=0)
        self.going_watch_in_label(self, self.__label, '%A %d %B  %H:%M:%S  %Y week #%W')