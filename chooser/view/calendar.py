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
        row: int = 1
        for j in range(order.week_numbers()[0], order.week_numbers()[1] + 1):
            Sticker(self, str(j), 0, row )
            row += 1

        day: int = 1
        col: int = order.week_index_of_firs_day_iso()
        row: int = 1
        amount_days = order.amount_days_in_month()
        self.labels = []
        while (day < amount_days):
            print(day)
            try:
                label = Sticker(self, str(day), column=col, row=row)
                self.labels.insert(day,label)
                self.labels[day].bind('<Button-1>', lambda event : 
                                        self.callback(event, label.cget('text')))
                day += 1
                col += 1
                if col % 8 == 0:
                    col = 1
                    row +=1 
            except IndexError as err:
                print('out of range')
    def callback(self, event, text:str) -> None:
        print(text)
        # date = dt(self.date.year, self.date.month, day)
        # print(date.ctime())