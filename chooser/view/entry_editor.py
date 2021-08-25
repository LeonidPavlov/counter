import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
import tkinter as tk

from chooser.view.root import Root


class Editor:
    def __init__(self, master, variable_name: str, title: str = 'edit date format') -> None:
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title(title)
        self.variable_name = variable_name
        self.old_variable: str = Root.get_variable(variable_name).get()
        x = Root.get_x_y_two_member_list()[0]
        y = Root.get_x_y_two_member_list()[1] - 200
        self.top.geometry(f'+{x}+{y}')
        self.top.bind('<Return>', self.confirm_for_return_key)
        self.top.bind('<Escape>', self.close_for_escape_key)
        frame = ttk.Frame(self.top)
        frame.grid()
        ttk.Label(frame, text='edit format date time\n representation\n' +
                              'Enter -> close\n Esc -> cancel').grid(column=0, row=0)
        self.editor = ttk.Entry(frame, textvariable=Root.get_variable(
            variable_name), width=40, justify=tk.CENTER)
        self.editor.grid(column=0, row=1)
        self.editor.focus()

    def close_for_escape_key(self, event) -> None:
        Root.update_variable(self.variable_name, tk.StringVar(Root.get_root(),
                                                              self.old_variable))
        self.top.destroy()

    def confirm_for_return_key(self, event) -> None:
        self.top.destroy()
