from datetime import date
from unittest.mock import patch

from src.budgets.serializers import BudgetSerializer
from src.budgets.value_objects import Budget, BudgetFrequency


@patch('src.budgets.value_objects.BUGGETS_SHARED', {"123"})
def test_roomie_budget():
    budget = Budget(
        id="123",
        name="House",
        limit=300,
        amount=250,
        used=100,
        planned=50,
        available=150,
        needed=50,
        date_from=date(2022, 1, 25),
        date_to=date(2022, 6, 25),
        rollover=True,
        rollover_amount=10,
        frequency=BudgetFrequency.MONTHLY,
        categories=[1, 2, 3]
    )
    assert BudgetSerializer().json(budget) == {
        "Name": budget.name,
        "Bugget (USD)": budget.roomie_limit,
        "Planned (USD)": budget.roomie_planned,
        "Used (USD)": budget.roomie_used,
        "Available (USD)": budget.roomie_available,
        "Shared with rommie": "Yes",
        "ID": budget.id
    }


def test_budget_without_roomie():
    budget = Budget(
        id="123",
        name="House",
        limit=300,
        amount=250,
        used=100,
        planned=50,
        available=150,
        needed=50,
        date_from=date(2022, 1, 25),
        date_to=date(2022, 6, 25),
        rollover=True,
        rollover_amount=10,
        frequency=BudgetFrequency.MONTHLY,
        categories=[1, 2, 3]
    )
    assert BudgetSerializer().json(budget) == {
        "Name": budget.name,
        "Bugget (USD)": budget.roomie_limit,
        "Planned (USD)": budget.roomie_planned,
        "Used (USD)": budget.roomie_used,
        "Available (USD)": budget.roomie_available,
        "Shared with rommie": "No",
        "ID": budget.id
    }
