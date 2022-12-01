from src.budgets.repositories import BudgetRepositoryInterface
from src.budgets.value_objects import Budget
from datetime import date


class BudgetMockRepository(BudgetRepositoryInterface):

    def __init__(self, budgets: list[Budget]) -> None:
        self.budgets = budgets
        super().__init__()

    def list(self, from_date: date, to_date: date) -> list[Budget]:
        return self.budgets
