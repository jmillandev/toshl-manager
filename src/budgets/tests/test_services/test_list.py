from unittest import TestCase

from src.budgets.services.summary_list import BudgetListService
from src.budgets.tests.factories import BudgetFactory
from src.budgets.tests.mocks.repository import BudgetMockRepository


class TestSumaryList(TestCase):

    def test_execute(self):
        budgets = BudgetFactory.build_batch(4)
        repository_mock = BudgetMockRepository(budgets)
        result = BudgetListService(repository_mock).execute(None, None)

        self.assertListEqual(budgets, result)
