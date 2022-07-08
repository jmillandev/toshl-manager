from services.toshl_finances.repository_interface import RepositoryInterface
from .endpoints import List
from ..client import make_request
from ..utils import has_containt_all_tags, utc_date, optional_params

class Entry(RepositoryInterface):

    def __init__(self, secret_key) -> None:
        self._secret_key = secret_key
        super().__init__()

    async def list(self, from_date, to_date, **kwargs):
        includes = kwargs.pop('includes', [])
        params = {'from': utc_date(from_date), 'to': utc_date(to_date)}
        params.update(optional_params(List, kwargs))
        response = await make_request(List.METHOD, List.URL, self._secret_key, params=params)

        if params['tags']:
            response = has_containt_all_tags(params['tags'], response)
        if includes:
            # TODO: Incluces extra information
            # response = add_include_data(response)
            pass
        return response
