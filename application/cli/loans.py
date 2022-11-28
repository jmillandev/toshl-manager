import asyncio

from cleo import Command

from libs.formatters import FORMATERS
from libs.outputs import OUTPUTS
from src.entries.controllers.loans import LoanController


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
        date_from = self.option("from")
        date_to = self.option("to")
        formater = FORMATERS[self.option("formatter").lower()]
        output = OUTPUTS[self.option("output").lower()]

        controller = LoanController()

        entries = asyncio.run(controller.list(date_from, date_to))
        asyncio.run(controller.receive_payment(date_from, date_to))
        output.out(formater().format(entries), "Loans")


class ListLoans(Command):
    """
    List the loans in the specific format

    roomie:loans:list
        {--from= : What time from do you want export data?. By default is begin month}
        {--to= : What time until do you want export data?. By default is end month}
        {--formatter=table : How do you can see data(table or csv)}
        {--output=terminal : Where do you want get the information?(terminal, file) }
    """

    def handle(self):
        date_from = self.option("from")
        date_to = self.option("to")
        formater = FORMATERS[self.option("formatter").lower()]
        output = OUTPUTS[self.option("output").lower()]

        entries = asyncio.run(LoanController().list(date_from, date_to))
        output.out(formater().format(entries), "Loans")
