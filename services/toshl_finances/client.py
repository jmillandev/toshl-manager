from aiohttp.helpers import BasicAuth
from aiohttp import ClientSession
from logging import getLogger
from services.toshl_finances.errors import RequestToshlError

logger = getLogger('toshl')


async def make_request(http_method: str, url: str, secret_key: str, **kwargs):
    async with ClientSession(auth=BasicAuth(secret_key)) as session:
        method = getattr(session, http_method.lower())
        http_method = http_method.upper()
        log_msg = f"-X {http_method} {url} --data {kwargs}"
        async with method(url, **kwargs) as response:
            resp_data = await response.json()

            if response.status < 300:
                logger.info(log_msg)  # TODO: Config logger
                print(log_msg)
                return resp_data

        raise RequestToshlError(http_method, url, kwargs, resp_data, response.status)
