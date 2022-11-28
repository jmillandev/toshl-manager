import asyncio

from cleo import Command

from libs.formatters import FORMATERS
from libs.outputs import OUTPUTS
from src.entries.controllers.roomie_expenses import RoomieExpenseController


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
        date_from = self.option("from")
        date_to = self.option("to")
        formater = FORMATERS[self.option("formatter").lower()]
        output = OUTPUTS[self.option("output").lower()]
        
        controller = RoomieExpenseController()
        entries = asyncio.run(controller.list(date_from, date_to))
        asyncio.run(controller.receive_payment(date_from, date_to))
        output.out(formater().format(entries), "Rooming expenses")


class ListRoomieExpenses(Command):
    """
    List the roomie expenses that yet are unpayment in the indicate format

    roomie:expenses:list
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

        entries = asyncio.run(RoomieExpenseController().list(date_from, date_to))
        output.out(formater().format(entries), "Rooming expenses")
