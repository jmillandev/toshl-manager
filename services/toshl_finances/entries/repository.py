from services.toshl_finances.repository_interface import RepositoryInterface
from .endpoints import List, Update
from ..client import make_request
from ..utils import has_containt_all_tags, utc_date, optional_params
from itertools import chain

class Entry(RepositoryInterface):

    def __init__(self, secret_key) -> None:
        self._secret_key = secret_key
        super().__init__()

    async def list(self, from_date, to_date, **kwargs):
        includes = kwargs.pop('includes', {})
        params = {'from': utc_date(from_date), 'to': utc_date(to_date)}
        params.update(optional_params(List, kwargs))
        response = await make_request(List.METHOD, List.URL, self._secret_key, params=params)

        if params['tags']:
            response = has_containt_all_tags(params['tags'], response)

        included = {}
        for key, resolver in includes.items():
            # TODO: Parallel this
            ids = ",".join(self._get_ids(response, key))
            included[key] = {d["id"]: d for d in await resolver(ids=ids)}
        for entry in response:
            entry["included"] = included

        return response

    async def update(self, id, amount, currency, date, desc, account, category, tags, modified, extra = None, **_trash):
        data = {
            "amount": amount,
            "currency": currency,
            "date": date,
            "desc": desc,
            "account": account,
            "category": category,
            "tags": tags,
            "modified": modified,
            "extra": extra
        }
        params = {
            "id": id
        }
        return await make_request(Update.METHOD, Update.URL, self._secret_key, json=data, params=params)

    def _get_ids(self, entries, key):
        ids = set()
        for entry in entries:
            if isinstance(entry[key], str):
                ids.add(entry[key])
                continue
            if isinstance(entry[key], list):
                ids = ids.union({*entry[key]})
                continue

            raise NotImplementedError

        return ids
