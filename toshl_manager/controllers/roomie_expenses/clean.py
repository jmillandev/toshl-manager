from asyncio import Semaphore, events, gather
from copy import deepcopy

from config import ROOMIE_TAG_ID, SEPARATOR, TOSH_SECRET_KEY, UNPAYMENT_TAG_ID
from services.toshl_finances.entries import types
from services.toshl_finances.toshl_app import ToshlApp
from toshl_manager.utils.formatters.roomie_expenses import RoomieExpensesFormatter

toshl_app = ToshlApp(TOSH_SECRET_KEY)


class CleanRoomieExpensesController:
    def __init__(self, from_date, to_date) -> None:
        self._from_date = from_date
        self._to_date = to_date
        self.__sem = None

    @property
    def _sem(self):
        if not self.__sem:
            self.__sem = Semaphore(3, loop=events.get_event_loop())
        return self.__sem

    async def execute(self):
        data = await self._entries_list()
        response = deepcopy(data)
        await gather(*map(self._remove_unpayment_tag, data))
        return RoomieExpensesFormatter.format(response)

    def _entries_list(self):
        return toshl_app.entries().list(
            from_date=self._from_date,
            to_date=self._to_date,
            type=types.EXPENSIVE,
            tags=SEPARATOR.join((ROOMIE_TAG_ID, UNPAYMENT_TAG_ID)),
        )

    async def _remove_unpayment_tag(self, entry):
        entry["tags"] = list(set(entry["tags"]) - {UNPAYMENT_TAG_ID})
        async with self._sem:
            await toshl_app.entries().update(**entry)
