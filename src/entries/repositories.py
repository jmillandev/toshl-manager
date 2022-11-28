from datetime import date

from pydantic import BaseModel, Field

from core.shared.type_of_entry import TypeOfEntry

from .dtos import EntryDto


class EntryListFilters(BaseModel):
    type: TypeOfEntry
    categories: list[int] = Field(description="Category ids", default=[])
    tags: list[int] = Field(description="Tag ids", default=[])

    def filled_values_as_json(self) -> dict:
        return { key: value for key, value in self.json().items() if value }

    
class EntryRepositoryInterface:

    async def list(self, from_date: date, to_date: date, filters: EntryListFilters) -> list[EntryDto]:
        raise NotImplementedError

    async def update(self, entry: EntryDto) -> None:
        raise NotImplementedError
