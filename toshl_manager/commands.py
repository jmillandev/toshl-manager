import asyncio

from cleo import Command

from config import (DEBTOR_TAG_ID, LOAND_CATEGORY_ID, ROOMIE_TAG_ID, SEPARATOR,
                    UNPAYMENT_TAG_ID)
from services.formatters.csv import CsvFormat
from services.formatters.table import TableFormat
from services.outputs.file import FileOutput
from services.outputs.terminal import TerminalOutput

from .controllers.buggets import Buggets as BuggetsController
from .controllers.entries.clean import CleanUnpaymentEntriesController
from .controllers.entries.show import ShowEntriesController
from .utils import date
from .utils.cleaners.loans import LoansCleaner
from .utils.cleaners.roomie_expenses import RoomieExpensesCleaner

FORMATERS = {"table": TableFormat, "csv": CsvFormat}
OUTPUTS = {"terminal": TerminalOutput(), "file": FileOutput("txt")}


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

        coroutine = ShowEntriesController(
            LoansCleaner,
            date_from,
            date_to,
            categories=LOAND_CATEGORY_ID,
            tags=SEPARATOR.join((UNPAYMENT_TAG_ID, DEBTOR_TAG_ID)),
        ).execute()
        entries = asyncio.run(coroutine)
        output.out(formater().execute(entries), "Loans")


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

        coroutine = CleanUnpaymentEntriesController(
            LoansCleaner,
            date_from,
            date_to,
            categories=LOAND_CATEGORY_ID,
            tags=SEPARATOR.join((UNPAYMENT_TAG_ID, DEBTOR_TAG_ID)),
        ).execute()
        entries = asyncio.run(coroutine)
        output.out(formater().execute(entries), "Loans")


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

        coroutine = ShowEntriesController(
            RoomieExpensesCleaner,
            date_from,
            date_to,
            tags=SEPARATOR.join((ROOMIE_TAG_ID, UNPAYMENT_TAG_ID)),
        ).execute()
        entries = asyncio.run(coroutine)
        output.out(formater().execute(entries), "Rooming expenses")


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

        coroutine = CleanUnpaymentEntriesController(
            RoomieExpensesCleaner,
            date_from,
            date_to,
            tags=SEPARATOR.join((ROOMIE_TAG_ID, UNPAYMENT_TAG_ID)),
        ).execute()
        entries = asyncio.run(coroutine)
        output.out(formater().execute(entries), "Rooming expenses")


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
        output.out(formater().execute(entries), "Buggets")
