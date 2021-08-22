import tkinter.ttk as ttk
import tkinter as tk

from chooser.view.clock_label import ClockLabel


class Base(ttk.Frame):

    __root: tk.Tk

    @staticmethod
    def get_root() -> tk.Tk:
        return Base.__root

    def __init__(self, root: tk.Tk, **kwargs) -> None:
        super().__init__(root, **kwargs)
        Base.__root = root
        self.grid()
        ClockLabel(self)
        