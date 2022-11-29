from datetime import date
from unittest.mock import patch

from src.budgets.value_objects import Budget, BudgetFrequency


@patch('src.budgets.value_objects.BUGGETS_SHARED', {"123"})
def test_roomie_budget():
    budget = Budget(
        id="123",
        name="House",
        limit=300,
        amount=250,
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

    assert budget.used == 200.0
    assert budget.available == 60
    assert budget.needed == 110
    assert budget.shared_with_roomie == True
    assert budget.roomie_limit == budget.limit / 2
    assert budget.roomie_planned == budget.planned / 2
    assert budget.roomie_used == budget.used / 2
    assert budget.roomie_available == budget.available / 2
    assert budget.roomie_needed == budget.needed / 2

def test_budget_without_roomie():
    budget = Budget(
        id="123",
        name="House",
        limit=300,
        amount=250,
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

    assert budget.used == 200.0
    assert budget.available == 60
    assert budget.needed == 110
    assert budget.shared_with_roomie == False
    assert budget.roomie_limit == budget.limit
    assert budget.roomie_planned == budget.planned
    assert budget.roomie_used == budget.used
    assert budget.roomie_available == budget.available
    assert budget.roomie_needed == budget.needed
