from cleo import Command
from .controllers.loans import Loans as ExportLoansController
import asyncio
from services.formaters.table import TableFormat
class ShowLoans(Command):
    """
    Show the loans in tha specific format

    show_loans
        {from : What time from do you want export data?}
        {to : What time until do you want export data?}
        {formater? : How do you can see data(table or csv) --default: table}
    """
    FORMATERS = {
        None: TableFormat,
        'table': TableFormat
        #'csv': CsvFormat TODO: Create CsvFormat
    }
    def handle(self):
        date_from = self.argument('from')
        date_to = self.argument('to')
        formater_name = self.argument('formater')
        formater = self.FORMATERS[formater_name]

        entries = asyncio.run(ExportLoansController(date_from, date_to).execute())
        print(formater().exec(entries))
