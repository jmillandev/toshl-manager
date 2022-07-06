from services.toshl_finances.repository_interface import RepositoryInterface
from .endpoints import List
from aiohttp.helpers import BasicAuth
from aiohttp import ClientSession

from logging import getLogger

logger = getLogger('toshl')

class Entry(RepositoryInterface):
    PARAM_NAMES = [
        'type', 'categories', 'tags'
    ]

    def __init__(self, secret_key) -> None:
        self._secret_key = secret_key
        super().__init__()

    async def list(self, from_date, to_date, **kwargs):
        params = {
            key:kwargs.get(key) for key in self.PARAM_NAMES if kwargs.get(key) != None
        }
        params.update({'from': from_date, 'to': to_date})
        async with ClientSession(auth=BasicAuth(self._secret_key)) as session:
            method = getattr(session, List.METHOD.lower())
            log_msg = f"-X {List.METHOD} {List.URL} --data {params}"
            async with method(List.URL, params=params) as response:
                logger.info(f"Status: {response.status}")

                data = await response.json()

                if response.status < 300:
                    print(log_msg)
                    return data
        # TODO: Create a custom error
        raise Exception(f"ERROR:: Request: {log_msg} -> Response: {data}")
