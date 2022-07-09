from config import LOAND_CATEGORY_ID, LOAND_TAG_IDS, SEPARATOR, TOSH_SECRET_KEY
from services.toshl_finances.entries import types
from services.toshl_finances.toshl_app import ToshlApp

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
            tags=SEPARATOR.join(LOAND_TAG_IDS),
        )
        return self._format(data)

    def _format(self, data):
        response = []
        sum = 0
        for row in data:
            amount = abs(row["amount"])
            response.append(
                {
                    "Description": row["desc"],
                    "USD Amount": amount,
                    "Date": row["date"],
                    "ID": row["id"],
                }
            )
            sum += amount

        response.append(
            {
                "Description": "TOTAL",
                "USD Amount": sum,
                "Date": "---",
                "ID": "---",
            }
        )
        return response
