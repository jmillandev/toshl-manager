import imp
from config import LOAND_CATEGORY_ID, SEPARATOR, TOSH_SECRET_KEY, UNPAYMENT_TAG_ID, DEBTOR_TAG_ID
from services.toshl_finances.entries import types
from services.toshl_finances.toshl_app import ToshlApp
from toshl_manager.utils.formatters.loans import LoansFormatter
from asyncio import Semaphore, gather, events
from copy import deepcopy

toshl_app = ToshlApp(TOSH_SECRET_KEY)


class CleanLoansController:
    # TODO: Merge Loans and Roomie Expenses Controllers
    def __init__(self, from_date, to_date) -> None:
        self._from_date = from_date
        self._to_date = to_date
        self.__sem = None

    async def execute(self):
        data = await self._entries_list()
        response = deepcopy(data)
        await gather(*map(self._remove_unpayment_tag, data))
        return LoansFormatter.format(response)

    def _entries_list(self):
        return toshl_app.entries().list(
            from_date=self._from_date,
            to_date=self._to_date,
            type=types.EXPENSIVE,
            categories=LOAND_CATEGORY_ID,
            tags=SEPARATOR.join((UNPAYMENT_TAG_ID, DEBTOR_TAG_ID)),
        )

    async def _remove_unpayment_tag(self, entry):
        entry["tags"] = list(set(entry["tags"]) - {UNPAYMENT_TAG_ID})
        async with self._sem:
            await toshl_app.entries().update(**entry)

    @property
    def _sem(self):
        if not self.__sem:
            self.__sem = Semaphore(3, loop=events.get_event_loop())
        return self.__sem
