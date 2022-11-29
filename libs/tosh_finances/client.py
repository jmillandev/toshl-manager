from logging import getLogger

from aiohttp import ClientSession
from aiohttp.helpers import BasicAuth

from config import TOSH_BASE_URL, TOSH_SECRET_KEY

from .endpoints import EndpointToshInterface
from .errors import RequestToshlError

logger = getLogger('toshl')


class ToshAPIClient:

    def __init__(self, secret_key: str = TOSH_SECRET_KEY, base_url: str = TOSH_BASE_URL) -> None:
        self.secret_key = secret_key
        self.base_url = base_url

    async def make_request(self, endpoint: EndpointToshInterface, **kwargs):
        url = self._make_url(url, kwargs.get('params', {}))

        async with ClientSession(auth=BasicAuth(self.secret_key)) as session:
            method = getattr(session, endpoint.http_method())
            async with method(url, **kwargs) as response:
                resp_data = await response.json()

                if response.status < 300:
                    print(f"-X {endpoint.http_method().upper()} {url} --data {kwargs}") # TODO: Config logger
                    return resp_data

                raise RequestToshlError(endpoint.http_method(), url, kwargs, resp_data, response.status)

    def _make_url(self, endpoint, params):
        return self.base_url  + endpoint.path.format(**params)
