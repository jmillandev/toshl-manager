import calendar
from datetime import date


def begin_month():
    return date.today().replace(day=1).strftime('%d/%m/%y')


def end_month():
    current_date = date.today()
    return date(
        current_date.year,
        current_date.month,
        calendar.monthrange(current_date.year, current_date.month)[1]
    ).strftime('%d/%m/%y')
