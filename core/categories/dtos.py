from pydantic import BaseModel

from core.type_of_entry import TypeOfEntry


class CategoryDto(BaseModel):
    id: int
    name: str
    type: TypeOfEntry
    deleted: bool
