from .value_objects import Budget

class BudgetSerializer:

    def json(self, budget: Budget) -> dict:
        return {
            "Name": budget.name,
            "Bugget (USD)": budget.roomie_limit,
            "Planned (USD)": budget.roomie_planned,
            "Used (USD)": budget.roomie_used,
            "Available (USD)": budget.roomie_available,
            "Needed (USD)": budget.roomie_needed,
            "Shared with rommie": 'Yes' if budget.shared_with_roomie else 'No',
            "ID": budget.id
        }
