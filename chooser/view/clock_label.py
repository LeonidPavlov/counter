import tkinter.ttk as ttk
from datetime import datetime as dt
import tkinter as tk

from chooser.view.entry_editor import Editor
from chooser.view.root import Root

class ClockLabel(ttk.Label):

    def __init__(self, master: ttk.Frame, text: str = 'something wrong',
                 column: int = 0, row: int = 0) -> None:
        super().__init__(master, text=text)
        self.grid(column=column, row=row)
        Root.set_variable('date_time_format_string', 
                tk.StringVar(Root.get_root(),'%A  %d %B  %H:%M:%S  %Y  week %W'))
        self.going_watch_in_label(Root.get_variable('date_time_format_string')\
                                                                        .get())
        self.bind('<Button-3>', self.change_format_string)

    def going_watch_in_label(self,
                             format_string: str = '%S') -> None:
        def count() -> None:
            time: dt = dt.now()
            self.config(text=time.strftime(format_string))
            self.after(1000, count)

        count()

    def change_format_string(self, event) -> None:  
        Editor(self)