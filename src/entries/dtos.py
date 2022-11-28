from datetime import date

from pydantic import BaseModel, Field


class CurrencyDto(BaseModel):
    code: str = Field(description="De currency code. For example: 'USD'")
    rate: float = Field(description="Calculated according to entry account currency")
    main_rate: float = Field(description="Calculated according to entry main currency")


class EntryDto(BaseModel):
    id: int
    amount: float
    currency: CurrencyDto
    date: date
    description: str # TODO: Toshl use desc as this field
    account: int = Field(description="The account ID")
    category: str = Field(description="The category ID")
    tags: list[str] = Field(description="List of the tags names")
