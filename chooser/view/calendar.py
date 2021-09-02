from time import strftime
from tkinter import Event
import tkinter.ttk as ttk
from datetime import datetime as dt
from typing import Tuple

from chooser.view.elements import Sticker, Pin
from chooser.model.around_date import OrderOfDays

class Calendar(ttk.Frame):
    __content = ['# week', ' mon ', ' tue ', ' wed ', ' thu ',
                 ' fri ', ' sat ', ' sun ']

    def __init__(self, master: ttk.Frame, column: int = 0, row: int = 0,
                 **kwargs):
        super().__init__(master)
        self.grid(column=column, row=row)
        self.date = dt.now()
        self.__header()
        self.__month_content()
    
    def __header(self) -> None:
        for c in range(8):
            Sticker(self, Calendar.__content[c], column=c)

    def __month_content(self) -> None:
        order = OrderOfDays(self.date)
        rrow: int = 1
        for j in range(order.week_numbers()[0], order.week_numbers()[1] + 1):
            Sticker(self, str(j), 0, rrow )
            rrow += 1

        day: int = 1
        col: int = order.week_index_of_firs_day_iso()
        rrow: int = 1
        while (day <= order.amount_days_in_month()):
            label = Sticker(self, str(day), column=col, row=rrow)
            label.bind('<Button-1>', self.callback)
            day += 1
            col += 1
            if col % 8 == 0:
                col = 1
                rrow +=1 

    def callback(self, event) -> None:
        print('callback')