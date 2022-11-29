from src.budgets.repositories import BudgetRepositoryInterface

from ..client import ToshAPIClient
from .endpoints import List


class BuggetToshlRepository(BudgetRepositoryInterface):

    async def list(self, from_date, to_date):
        params = {'from': from_date, 'to': to_date}
        return await ToshAPIClient().make_request(List, params=params)
