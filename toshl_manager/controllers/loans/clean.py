import imp
from config import LOAND_CATEGORY_ID, SEPARATOR, TOSH_SECRET_KEY, UNPAYMENT_TAG_ID, DEBTOR_TAG_ID
from services.toshl_finances.entries import types
from services.toshl_finances.toshl_app import ToshlApp
from toshl_manager.utils.formatters.loans import LoansFormatter
from asyncio import Semaphore, gather

toshl_app = ToshlApp(TOSH_SECRET_KEY)


class CleanLoansController:
    def __init__(self, from_date, to_date) -> None:
        self._from_date = from_date
        self._to_date = to_date
        self._sem = Semaphore(3)

    async def execute(self):
        data = await self._entries_list()
        await gather(*map(self._remove_unpayment_tag, data))
        return LoansFormatter.format(data)

    def _entries_list(self):
        return toshl_app.entries().list(
            from_date=self._from_date,
            to_date=self._to_date,
            type=types.EXPENSIVE,
            categories=LOAND_CATEGORY_ID,
            tags=SEPARATOR.join((UNPAYMENT_TAG_ID, DEBTOR_TAG_ID)),
        )

    async def _remove_unpayment_tag(self, entry):
        data = entry.copy()
        data["tags"] = list(set(data["tags"]) - {UNPAYMENT_TAG_ID})
        async with self._sem:
            await toshl_app.entries().update(**data)
