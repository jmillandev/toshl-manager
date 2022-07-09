import asyncio

from cleo import Command

from services.formatters.csv import CsvFormat
from services.formatters.table import TableFormat

from .controllers.buggets import Buggets as BuggetsController
from .controllers.loans.show import ShowLoansController
from .controllers.loans.clean import CleanLoansController
from .controllers.roomie_expenses import RoomieExpenses as RoomieExpensesController
from .utils import date

FORMATERS = {"table": TableFormat, "csv": CsvFormat}


class ShowLoans(Command):
    """
    Show the loans in the specific format

    roomie:loans:show
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
    """

    def handle(self):
        date_from = self.option("from") or date.begin_month()
        date_to = self.option("to") or date.end_month()
        formatter_name = self.option("formatter").lower()
        formater = FORMATERS[formatter_name]

        entries = asyncio.run(ShowLoansController(date_from, date_to).execute())
        print(formater().execute(entries))


class ShowRoomieExpenses(Command):
    """
    Show the roomie expenses that yet are unpayment in the indicate format

    roomie:expenses:show
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
    """

    def handle(self):
        date_from = self.option("from") or date.begin_month()
        date_to = self.option("to") or date.end_month()
        formatter_name = self.option("formatter").lower()
        formater = FORMATERS[formatter_name]

        entries = asyncio.run(RoomieExpensesController(date_from, date_to).execute())
        print(formater().execute(entries))


class ShowBugets(Command):
    """
    Show the buggets information(Name, limit, planned, etc)

    buggets:show
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
    """

    def handle(self):
        date_from = self.option("from") or date.begin_month()
        date_to = self.option("to") or date.end_month()
        formatter_name = self.option("formatter").lower()
        formater = FORMATERS[formatter_name]

        entries = asyncio.run(BuggetsController(date_from, date_to).execute())
        print(formater().execute(entries))
