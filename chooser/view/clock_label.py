import tkinter.ttk as ttk
from datetime import datetime as dt
import tkinter as tk

from chooser.view.entry_editor import Editor
from chooser.view.root import Root
from chooser.view.elements import PopUp

class ClockLabel(ttk.Label):
    def __init__(self, master: ttk.Frame, text: str = 'something wrong',
                 column: int = 0, row: int = 0) -> None:
        super().__init__(master, text=text)
        self.master = master
        self.grid(column=column, row=row)
        self.variable_name = 'date_time_format_string'
        self.format_string = '%A  %d %B  %H:%M:%S  %Y  week %W'
        Root.set_variable(self.variable_name,
                          tk.StringVar(Root.get_root(), self.format_string))
        self.going_watch_in_label()
        self.bind('<Button-3>', self.run_format_sting_editor)

        popup: PopUp = PopUp('edit format of date\n right button click')
        self.bind('<Enter>', popup.open)
        self.bind('<Leave>', popup.close)

    def going_watch_in_label(self) -> None:
        def count() -> None:
            time: dt = dt.now()
            self.config(text=time.strftime(Root.get_variable(self.variable_name).get()))
            self.after(1000, count)

        count()

    def run_format_sting_editor(self, event) -> None:
        Editor(self, self.variable_name)
