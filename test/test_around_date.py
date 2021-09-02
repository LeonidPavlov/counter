import pytest
from datetime import datetime as dt

from chooser.model.around_date import OrderOfDays

def test_OrderOfDays_init() -> None:
    assert(OrderOfDays() is not None)


def test_first_weekday_index() -> None:
    date = OrderOfDays(dt(2021,9,22))
    assert(date.week_index_of_firs_day_iso() is 3)
    date = None

def test_ordinary_amount_days_in_month() -> None:
    date = OrderOfDays(dt(2021,9,22))
    assert(date.amount_days_in_month() == 30)
    date = None

def test_another_ordinary_amount_days_in_month() -> None:
    date = OrderOfDays(dt(2000, 1, 3))
    assert(date.amount_days_in_month() == 31)
    date = None

def test_amount_days_in_february_leap_year() -> None:
    date = OrderOfDays(dt(2020, 2, 1))
    assert(date.amount_days_in_month() == 29)
    date = None

def test_amount_days_in_february_not_leap_year() -> None:
    date = OrderOfDays(dt(2021, 2, 1))
    assert(date.amount_days_in_month() == 28)
    date = None
    
def test_week_numbers_first_week() -> None:
    order = OrderOfDays(dt(2021,9,10))
    assert(order.week_numbers()[0] == 35)
    assert(order.week_numbers()[1] == 39)
