from datetime import date

from .dtos import BudgetDto


class BudgetRepositoryInterface:

    async def list(self, from_date: date, to_date: date) -> list[BudgetDto]:
        raise NotImplementedError
