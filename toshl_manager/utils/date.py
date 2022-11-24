import calendar
from datetime import date

def _today():
    return date.today()


def begin_month()-> str:
    return _today().replace(day=1).strftime('%d/%m/%y')


def end_month()-> str:
    current_date = _today()
    return date(
        current_date.year,
        current_date.month,
        calendar.monthrange(current_date.year, current_date.month)[1]
    ).strftime('%d/%m/%y')
