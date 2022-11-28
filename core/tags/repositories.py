
from .dtos import TagDto


class TagRepositoryInterface:

    async def list(self, ids: list[int]) -> list[TagDto]:
        raise NotImplementedError
