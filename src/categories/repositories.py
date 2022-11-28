from .dtos import CategoryDto


class CategoryRepositoryInterface:

    async def list(self, ids: list[int])-> list[CategoryDto]:
        raise NotImplementedError
