import calendar
from datetime import date, datetime

from config import TIME_ZONE


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


def utc_date(string_date: str)-> date:
    date_time = datetime.strptime(string_date, "%d/%m/%y")
    local_dt = TIME_ZONE.localize(date_time, is_dst=None)
    return local_dt.strftime("%Y-%m-%d")
