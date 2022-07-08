import asyncio

from cleo import Command

from services.formaters.table import TableFormat
from services.formaters.csv import CsvFormat

from .controllers.loans import Loans as LoansController
from .controllers.roomie_expenses import RoomieExpenses as RoomieExpensesController

FORMATERS = {
    None: TableFormat,
    "table": TableFormat,
    'csv': CsvFormat
}


class ShowLoans(Command):
    """
    Show the loans in the specific format

    show_loans
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
        print(formater().exec(entries))


class ShowRoomieExpenses(Command):
    """
    Show the roomie expenses that yet are unpayment in the indicate format

    show_roomie_expenses
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
        print(formater().exec(entries))
