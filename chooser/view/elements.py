import tkinter as tk
import tkinter.ttk as ttk

from chooser.view.root import Root


class PopUp:
    def __init__(self, message: str = 'default') -> None:
        self.message = message

    def open(self, event) -> None:
        x_y: list = Root.get_x_y_two_member_list()
        self.top = tk.Toplevel()
        self.top.attributes('-type', 'dock')
        y_plus: int = Root.get_root().winfo_height()
        self.top.geometry(f'+{x_y[0]}+{(x_y[1] + 2 * y_plus )}')
        label = ttk.Label(self.top, text=self.message)
        label.grid()

    def close(self, event) -> None:
        self.top.destroy()


class Sticker(ttk.Label):
    def __init__(self, master: ttk.Frame, text: str = 'label', column: int = 0,
                 row: int = 0, columnspan: int = 1, rowspan: int = 1, **kwargs):
        super().__init__(master, text=text, **kwargs)
        self.grid(column=column, row=row, columnspan=columnspan,
                  rowspan=rowspan)
        