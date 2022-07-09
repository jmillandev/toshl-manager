import asyncio

from cleo import Command

from services.formatters.csv import CsvFormat
from services.formatters.table import TableFormat
from services.outputs.terminal import TerminalOutput

from .controllers.buggets import Buggets as BuggetsController
from .controllers.loans.show import ShowLoansController
from .controllers.loans.clean import CleanLoansController
from .controllers.roomie_expenses.show import ShowRoomieExpensesController
from .controllers.roomie_expenses.clean import CleanRoomieExpensesController

from .utils import date

FORMATERS = {"table": TableFormat, "csv": CsvFormat}
OUTPUTS = {"terminal": TerminalOutput}


class ShowLoans(Command):
    """
    Show the loans in the specific format

    roomie:loans:show
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
        {--output=terminal : Where do you want get the information?(terminal, file) }
    """

    def handle(self):
        date_from = self.option("from") or date.begin_month()
        date_to = self.option("to") or date.end_month()
        formater = FORMATERS[self.option("formatter").lower()]
        output = OUTPUTS[self.option("output").lower()]

        entries = asyncio.run(ShowLoansController(date_from, date_to).execute())
        output.out(formater().execute(entries), 'Loans')


class CleanLoans(Command):
    """
    Remove unpayment tag from the loan entries. And show the entries modificated

    roomie:loans:clean
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
        {--output=terminal : Where do you want get the information?(terminal, file) }
    """

    def handle(self):
        date_from = self.option("from") or date.begin_month()
        date_to = self.option("to") or date.end_month()
        formater = FORMATERS[self.option("formatter").lower()]
        output = OUTPUTS[self.option("output").lower()]

        entries = asyncio.run(CleanLoansController(date_from, date_to).execute())
        output.out(formater().execute(entries), 'Loans')


class ShowRoomieExpenses(Command):
    """
    Show the roomie expenses that yet are unpayment in the indicate format

    roomie:expenses:show
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
        {--output=terminal : Where do you want get the information?(terminal, file) }
    """

    def handle(self):
        date_from = self.option("from") or date.begin_month()
        date_to = self.option("to") or date.end_month()
        formater = FORMATERS[self.option("formatter").lower()]
        output = OUTPUTS[self.option("output").lower()]

        entries = asyncio.run(
            ShowRoomieExpensesController(date_from, date_to).execute()
        )
        output.out(formater().execute(entries), 'Rooming expenses')


class CleanRoomieExpenses(Command):
    """
    Remove unpayment tag from the roomie expense entries. And show the entries modificated

    roomie:expenses:clean
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
        {--output=terminal : Where do you want get the information?(terminal, file) }
    """

    def handle(self):
        date_from = self.option("from") or date.begin_month()
        date_to = self.option("to") or date.end_month()
        formater = FORMATERS[self.option("formatter").lower()]
        output = OUTPUTS[self.option("output").lower()]

        entries = asyncio.run(
            CleanRoomieExpensesController(date_from, date_to).execute()
        )
        output.out(formater().execute(entries), 'Rooming expenses')


class ShowBugets(Command):
    """
    Show the buggets information(Name, limit, planned, etc)

    buggets:show
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
        {--output=terminal : Where do you want get the information?(terminal, file) }
    """

    def handle(self):
        date_from = self.option("from") or date.begin_month()
        date_to = self.option("to") or date.end_month()
        formater = FORMATERS[self.option("formatter").lower()]
        output = OUTPUTS[self.option("output").lower()]

        entries = asyncio.run(BuggetsController(date_from, date_to).execute())
        output.out(formater().execute(entries), 'Buggets')
