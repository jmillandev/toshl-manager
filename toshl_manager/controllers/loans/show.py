from config import LOAND_CATEGORY_ID, SEPARATOR, TOSH_SECRET_KEY, DEBTOR_TAG_ID, UNPAYMENT_TAG_ID
from services.toshl_finances.entries import types
from services.toshl_finances.toshl_app import ToshlApp
from toshl_manager.utils.formatters.loans import LoansFormatter

toshl_app = ToshlApp(TOSH_SECRET_KEY)


class ShowLoansController:
    def __init__(self, from_date, to_date) -> None:
        self._from_date = from_date
        self._to_date = to_date

    async def execute(self):
        data = await toshl_app.entries().list(
            from_date=self._from_date,
            to_date=self._to_date,
            type=types.EXPENSIVE,
            categories=LOAND_CATEGORY_ID,
            tags=SEPARATOR.join((UNPAYMENT_TAG_ID, DEBTOR_TAG_ID)),
        )
        return LoansFormatter.format(data)
