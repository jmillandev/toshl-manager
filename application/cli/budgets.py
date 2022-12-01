import asyncio

from cleo import Command

from libs.calculators.total_dict import TotalDictCalculator
from libs.formatters import FORMATERS
from libs.outputs import OUTPUTS
from src.budgets.serializers import BudgetSerializer
from src.budgets.services.summary_list import BudgetListService


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
        serializer = BudgetSerializer()

        budgets = asyncio.run(BudgetListService().execute(date_from, date_to))
        data = [serializer.json(budget) for budget in budgets]
        total = TotalDictCalculator(data)

        output.out(formater().format(data.append(total)), "Buggets")
