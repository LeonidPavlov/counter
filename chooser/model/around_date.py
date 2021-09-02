from datetime import datetime as dt
import calendar
from typing import Tuple


class OrderOfDays:

    def __init__(self, date: dt = dt.now()) -> None:
        self.date = date

    def week_index_of_firs_day_iso(self) -> int:
        date = dt(self.date.year, self.date.month, 1)
        return date.isoweekday()

    def amount_days_in_month(self) -> int:
        return calendar.monthrange(self.date.year, self.date.month)[1]
    
    def week_numbers(self) -> Tuple[int, int]:
        """ 
            return tuple[int,int] \n
            index 0 -> week number of first day month \n
            index 1 -> week number of last day month
        """
        date = dt(self.date.year, self.date.month, 1)
        first_day: int = date.isocalendar()[1]
        date = dt(self.date.year, self.date.month, self.amount_days_in_month())
        last_day: int = date.isocalendar()[1]
        return (first_day, last_day)

    def obtaining_datetime_instansce(self) -> dt:
        return self.date        
