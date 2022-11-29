from datetime import date

from .value_objects import Budget


class BudgetRepositoryInterface:

    async def list(self, from_date: date, to_date: date) -> list[Budget]:
        raise NotImplementedError
