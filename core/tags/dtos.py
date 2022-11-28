from pydantic import BaseModel

from core.type_of_entry import TypeOfEntry


class TagDto(BaseModel):
    id: int
    name: str
    type: TypeOfEntry
    category: int | None
    deleted: bool
