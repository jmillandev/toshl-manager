from datetime import date
from enum import Enum
from typing import Any
from pydantic import BaseModel
from config import BUGGETS_SHARED

class BudgetFrequency(Enum):
    ONE_TIME = "one-time"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"


class Budget(BaseModel):
    id: str
    name: str
    limit: float
    amount: float
    planned: float
    date_from: date
    date_to: date
    rollover: bool
    rollover_amount: float
    frequency: BudgetFrequency
    categories: list[int]
    shared_with_roomie: bool

    def __init__(self, **data: Any) -> None:
        data["shared_with_roomie"] = (str(data["id"]).split('-')[0] in BUGGETS_SHARED)
        super().__init__(**data)

    @property
    def used(self) -> float:
        return self.amount - self.planned

    @property
    def available(self) -> float:
        return self.limit + self.rollover_amount - self.amount

    @property
    def needed(self)-> float:
        needed = self.limit + self.rollover_amount - self.used
        return 0 if needed < 0 else needed

    @property
    def roomie_limit(self):
        return self._split_shared_with_roomie(self.limit)

    @property
    def roomie_planned(self):
        return self._split_shared_with_roomie(self.planned)

    @property
    def roomie_used(self):
        return self._split_shared_with_roomie(self.used)

    @property
    def roomie_available(self):
        return self._split_shared_with_roomie(self.available)

    @property
    def roomie_needed(self):
        return self._split_shared_with_roomie(self.needed)

    def _split_shared_with_roomie(self, number):
        return (number / 2) if self.shared_with_roomie else number
