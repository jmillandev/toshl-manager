import asyncio

from cleo import Command

from services.formatters.table import TableFormat
from services.formatters.csv import CsvFormat

from .controllers.loans import Loans as LoansController
from .controllers.roomie_expenses import RoomieExpenses as RoomieExpensesController
from .controllers.buggets import Buggets as BuggetsController

FORMATERS = {
    None: TableFormat,
    "table": TableFormat,
    'csv': CsvFormat
}


class ShowLoans(Command):
    """
    Show the loans in the specific format

    loans:show
        {from : What time from do you want export data?}
        {to : What time until do you want export data?}
        {formater? : How do you can see data(table or csv) --default: table}
    """

    def handle(self):
        date_from = self.argument("from")
        date_to = self.argument("to")
        formater_name = self.argument("formater")
        formater = FORMATERS[formater_name]

        entries = asyncio.run(LoansController(date_from, date_to).execute())
        print(formater().execute(entries))


class ShowRoomieExpenses(Command):
    """
    Show the roomie expenses that yet are unpayment in the indicate format

    roomie_expenses:show
        {from : What time from do you want export data?}
        {to : What time until do you want export data?}
        {formater? : How do you can see data(table or csv) --default: table}
    """

    def handle(self):
        date_from = self.argument("from")
        date_to = self.argument("to")
        formater_name = self.argument("formater")
        formater = FORMATERS[formater_name]

        entries = asyncio.run(RoomieExpensesController(date_from, date_to).execute())
        print(formater().execute(entries))

class ShowBugets(Command):
    """
    Show the buggets information(Name, limit, planned, etc)

    buggets:show
        {from : What time from do you want export data?}
        {to : What time until do you want export data?}
        {formater? : How do you can see data(table or csv) --default: table}
    """

    def handle(self):
        date_from = self.argument("from")
        date_to = self.argument("to")
        formater_name = self.argument("formater")
        formater = FORMATERS[formater_name]

        entries = asyncio.run(BuggetsController(date_from, date_to).execute())
        print(formater().execute(entries))
