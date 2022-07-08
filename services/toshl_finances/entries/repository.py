from services.toshl_finances.repository_interface import RepositoryInterface
from .endpoints import List
from aiohttp.helpers import BasicAuth
from aiohttp import ClientSession
from services.toshl_finances.errors import RequestToshlError
from logging import getLogger
from .utils import has_containt_all_tags

logger = getLogger('toshl')

class Entry(RepositoryInterface):
    PARAM_NAMES = [
        'type', 'categories', 'tags'
    ]

    def __init__(self, secret_key) -> None:
        self._secret_key = secret_key
        super().__init__()

    async def list(self, from_date, to_date, **kwargs):
        includes = kwargs.pop('includes', [])
        params = {
            key:kwargs.get(key) for key in self.PARAM_NAMES if kwargs.get(key) != None
        }
        params.update({'from': from_date, 'to': to_date})
        async with ClientSession(auth=BasicAuth(self._secret_key)) as session:
            method = getattr(session, List.METHOD.lower())
            log_msg = f"-X {List.METHOD} {List.URL} --data {params}"
            async with method(List.URL, params=params) as response:
                resp_data = await response.json()

                if response.status < 300:
                    logger.info(log_msg) # TODO: Config logger
                    print(log_msg)
                    if params['tags']:
                        resp_data = has_containt_all_tags(params['tags'], resp_data)
                    if includes:
                        # TODO: Incluces extra information
                        resp_data = add_include_data(resp_data)
                    return resp_data

        raise RequestToshlError(List.METHOD, List.URL, params, resp_data, response.status)
