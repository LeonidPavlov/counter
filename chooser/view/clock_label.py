import tkinter.ttk as ttk
from datetime import datetime as dt
import tkinter as tk

from chooser.view.entry_editor import Editor

class ClockLabel(ttk.Label):

    def __init__(self, master: ttk.Frame, text: str = 'something wrong',
                 column: int = 0, row: int = 0) -> None:
        super().__init__(master, text=text)
        self.grid(column=column, row=row)
        # self.going_watch_in_label(Vars.get_variable('date_time_format_string')\
                                                        # .get())
        # self.bind('<Button-3>', self.change_format_string)

    def going_watch_in_label(self,
                             format_string: str = '%S') -> None:
        def count() -> None:
            time: dt = dt.now()
            self.config(text=time.strftime(format_string))
            self.after(1000, count)

        count()

    # def change_format_string(self, event) -> None:
    #     Editor('edit date format', 
    #             Vars.get_variable('date_time_format_string').get())
