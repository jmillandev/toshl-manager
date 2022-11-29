import asyncio

from cleo import Command

from libs.formatters import FORMATERS
from libs.outputs import OUTPUTS
from src.budgets.services.summary_list import BudgetSumaryListService 


class ListBugets(Command):
    """
    List the buggets information(Name, limit, planned, etc)

    buggets:list
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

        entries = asyncio.run(BudgetSumaryListService().execute(date_from, date_to))
        output.out(formater().format(entries), "Buggets")
