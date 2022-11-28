from datetime import date
from enum import Enum

from pydantic import BaseModel


class BudgetFrequency(Enum):
    ONE_TIME = "one-time"
    DAILY = "daily"
    WEEKLY = "weekly"
    MONTHLY = "monthly"
    YEARLY = "yearly"


class BudgetDto(BaseModel):
    id: int
    name: str
    limit: float
    used: float
    planned: float
    date_from: date
    date_to: date
    rollover: bool
    rollover_amount: float
    frequency: BudgetFrequency
    categories: list[int]
