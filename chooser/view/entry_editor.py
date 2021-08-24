import tkinter as tk
import tkinter.ttk as ttk
from tkinter import StringVar
import tkinter as tk

from chooser.view.root import Root


class Editor():
    def __init__(self, master, variable_name: str, title: str = 'edit date format') -> None:
        self.master = master
        self.top = tk.Toplevel(master)
        self.top.title(title)
        self.top.bind('<Return>', self.confirm_for_return_key)
        self.top.bind('<Escape>', self.close_for_escape_key)
        frame = ttk.Frame(self.top)
        frame.grid()

        self.variable_name = variable_name
        self.editor = ttk.Entry(frame, textvariable= Root.get_variable(self.variable_name),
                                width=50, justify=tk.CENTER)
        self.editor.grid(column=0, row=0, columnspan=2)

        ttk.Button(frame, text='CONFIRM', command=self.confirm_for_button) \
            .grid(column=0, row=1)
        ttk.Button(frame, text='CANCEL', command=self.close_for_button) \
            .grid(column=1, row=1)

    def close_for_button(self) -> None:
        self.top.destroy()

    def close_for_escape_key(self, event) -> None:
        self.top.destroy()

    def confirm_for_button(self) -> None:
        self.change_string_variable()
        Root.get_variable(self.variable_name).get()
        self.top.destroy()

    def confirm_for_return_key(self, event) -> None:
        self.change_string_variable()
        Root.get_variable(self.variable_name).get()
        self.top.destroy()

    def change_string_variable(self) -> None:
        Root.update_variable(self.variable_name, tk.StringVar(Root.get_root(), self.editor.get()))
        self.editor.configure(textvariable=Root.get_variable(self.variable_name))
