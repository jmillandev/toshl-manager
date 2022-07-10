from asyncio import Semaphore, events, gather
from copy import deepcopy

from config import TOSH_SECRET_KEY, UNPAYMENT_TAG_ID
from services.toshl_finances.entries import types
from services.toshl_finances.toshl_app import ToshlApp

toshl_app = ToshlApp(TOSH_SECRET_KEY)
PARALLEL_REQUEST = 3


class CleanUnpaymentEntriesController:
    def __init__(
        self, cleaner, from_date, to_date, entry_type=types.EXPENSIVE, **filters
    ) -> None:
        self._from_date = from_date
        self._to_date = to_date
        self._type = (entry_type,)
        self._filters = filters
        self._cleaner = cleaner
        self.__sem = None

    async def execute(self):
        data = await self._entries_list()
        response = deepcopy(data)
        await gather(*map(self._remove_unpayment_tag, data))
        return self._cleaner.clean(response)

    def _entries_list(self):
        return toshl_app.entries().list(
            from_date=self._from_date,
            to_date=self._to_date,
            type=self._type,
            **self._filters
        )

    async def _remove_unpayment_tag(self, entry):
        entry["tags"] = list(set(entry["tags"]) - {UNPAYMENT_TAG_ID})
        async with self._sem:
            await toshl_app.entries().update(**entry)

    @property
    def _sem(self):
        if not self.__sem:
            self.__sem = Semaphore(PARALLEL_REQUEST, loop=events.get_event_loop())
        return self.__sem
