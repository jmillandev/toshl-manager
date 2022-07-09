from services.toshl_finances.toshl_app import ToshlApp
from services.toshl_finances.entries import types
from config import TOSH_SECRET_KEY, SEPARATOR, ROOMIE_TAG_ID, UNPAYMENT_TAG_ID
from toshl_manager.utils.formatters.roomie_expenses import RoomieExpensesFormatter

toshl_app = ToshlApp(TOSH_SECRET_KEY)


class ShowRoomieExpensesController:
    def __init__(self, from_date, to_date) -> None:
        self._from_date = from_date
        self._to_date = to_date

    async def execute(self):
        data = await toshl_app.entries().list(
            from_date=self._from_date,
            to_date=self._to_date,
            type=types.EXPENSIVE,
            tags=SEPARATOR.join((ROOMIE_TAG_ID, UNPAYMENT_TAG_ID))
        )
        return RoomieExpensesFormatter.format(data)
