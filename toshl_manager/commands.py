from cleo import Command
from .controllers.exports_loans import ExportLoans as ExportLoansController
import asyncio

class ExportLoans(Command):
    """
    Show the loans in tha specific format

    show_loans
        {from : What time from do you want export data?}
        {to? : What time until do you want export data?}
    """

    def handle(self):
        date_from = self.argument('from')
        date_to = self.argument('to')

        asyncio.run(ExportLoansController(date_from, date_to).execute())
