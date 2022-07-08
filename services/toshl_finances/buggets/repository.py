from services.toshl_finances.repository_interface import RepositoryInterface
from .endpoints import List
from ..client import make_request
from ..utils import utc_date

class Bugget(RepositoryInterface):

    def __init__(self, secret_key) -> None:
        self._secret_key = secret_key
        super().__init__()

    async def list(self, from_date, to_date):
        params = {'from': utc_date(from_date), 'to': utc_date(to_date)}
        response = await make_request(List.METHOD, List.URL, self._secret_key, params=params)
        return response
