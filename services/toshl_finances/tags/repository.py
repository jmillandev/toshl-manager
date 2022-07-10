from services.toshl_finances.repository_interface import RepositoryInterface
from .endpoints import List
from ..client import make_request

class Tag(RepositoryInterface):

    def __init__(self, secret_key) -> None:
        self._secret_key = secret_key
        super().__init__()

    async def list(self, **params):
        response = await make_request(List.METHOD, List.URL, self._secret_key, params=params)
        return response
