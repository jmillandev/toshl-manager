from .dtos import CategoryDto


class CategoryRepositoryInterface:

    # TODO: Define params type values
    async def list(self, **params)-> list[CategoryDto]:
        raise NotImplementedError
