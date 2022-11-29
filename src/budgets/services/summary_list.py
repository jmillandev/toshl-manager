from ...shared.dependencies import Container
from dependency_injector.wiring import Provide, inject
from ..repositories import BudgetRepositoryInterface
from ..value_objects import Budget
from collections import defaultdict
from libs.date import begin_month, end_month, utc_date


class BudgetSumaryListService:

    @inject
    def __init__(self, repository: BudgetRepositoryInterface = Provide[Container.budget_repository]) -> None:
        self.repository = repository

    def execute(self, from_date: str | None, to_date: str | None) -> list[Budget]:
        budgets = self.repository.list(
            from_date=utc_date(from_date or begin_month),
            to_date=utc_date(to_date or end_month)
        )
        sum = defaultdict(lambda: 0)
        response = []
        for budget in budgets:
            response.append(budget)
            sum["used"] += budget.used
            sum["overspending"] += budget.overspending
            sum["free"] += budget.free
            sum["limit"] += budget.limit
            sum["planned"] += budget.planned
            sum["needed"] += budget.needed

        return response.append(
            Budget(
                id="---",
                name="- Total -",
                **sum
            )
        )
