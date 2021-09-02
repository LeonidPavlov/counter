import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
import tkinter as tk

from chooser.root import Root


class Editor:
    __editor_y_shift = 20
    __editor_number_of_characters = 40

    def __init__(self, master, variable_name: str,
                 title: str = 'edit date format') -> None:
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title(title)
        self.variable_name = variable_name
        self.old_variable: str = Root.get_variable(variable_name).get()
        x = Root.get_x_y_two_member_list()[0]
        y = Root.get_x_y_two_member_list()[1] + Editor.__editor_y_shift
        self.top.geometry(f'+{x}+{y}')
        self.top.bind('<Return>', self.confirm_for_return_key)
        self.top.bind('<Escape>', self.close_for_escape_key)
        frame = ttk.Frame(self.top)
        frame.grid()

        ttk.Label(frame, text='edit format date time representation\n' +
                              'Enter -> close  Esc -> cancel'). \
            grid(column=0, row=0)
        self.editor = ttk.Entry(frame, textvariable=Root.get_variable(
            variable_name), width=Editor.__editor_number_of_characters,
                                justify=tk.CENTER)
        self.editor.grid(column=0, row=1)
        self.editor.focus()
        button = ttk.Button(frame, text='restore default',
                            command=self.set_default_value)
        button.grid(column=0, row=2)

    def close_for_escape_key(self, event) -> None:
        Root.update_variable(self.variable_name,
                             tk.StringVar(Root.get_root(), self.old_variable))
        self.top.destroy()

    def confirm_for_return_key(self, event) -> None:
        self.top.destroy()

    def set_default_value(self) -> None:
        Root.update_variable(self.variable_name,
                             tk.StringVar(Root.get_root(),
                                          Root.default_format_string))
        self.editor.configure(textvariable=Root.get_variable(
            self.variable_name))
