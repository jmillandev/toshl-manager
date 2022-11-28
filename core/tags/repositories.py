
from .dtos import TagDto


class TagRepositoryInterface:

    # TODO: Define params type values
    async def list(self, **params) -> list[TagDto]:
        raise NotImplementedError
