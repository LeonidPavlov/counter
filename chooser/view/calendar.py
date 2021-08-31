import tkinter.ttk as ttk

from chooser.view.elements import Sticker


class Calendar(ttk.Frame):
    __content = ['# week', ' mon ', ' tue ', ' wed ', ' thu ',
                 ' fri ', ' sat ', ' sun ']

    def __init__(self, master: ttk.Frame, column: int = 0, row: int = 0,
                 **kwargs):
        super().__init__(master)
        for c in range(8):
            Sticker(self, Calendar.__content[c], column=c, row=0)
        self.grid(column=column, row=row)
