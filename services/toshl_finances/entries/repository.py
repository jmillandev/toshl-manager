from services.toshl_finances.repository_interface import RepositoryInterface
from .endpoints import List
from aiohttp.helpers import BasicAuth
from aiohttp import ClientSession

class Entry(RepositoryInterface):
    PARAM_NAMES = [
        'type', 'category_ids', 'tag_ids'
    ]

    def __init__(self, secret_key) -> None:
        self._secret_key = secret_key
        super().__init__()

    async def list(self, from_date, to_date, **kwargs):
        async with ClientSession(auth=BasicAuth(self._secret_key)) as session:
            async with getattr(session, List.METHOD.lower())(List.URL) as response:
                print("Status:", response.status)
                print("Content-type:", response.headers['content-type'])

                html = await response.text()
                print("Body:", html[:15], "...")    
