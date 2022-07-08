from services.toshl_finances.toshl_app import ToshlApp
from services.toshl_finances.entries import types
from config import TOSH_SECRET_KEY, ROOMIE_UNPAYMENT_TAG_IDS, SEPARATOR

toshl_app = ToshlApp(TOSH_SECRET_KEY)


class RoomieExpenses:
    def __init__(self, from_date, to_date) -> None:
        self._from_date = from_date
        self._to_date = to_date

    async def execute(self):
        data = await toshl_app.entries().list(
            from_date=self._from_date,
            to_date=self._to_date,
            type=types.EXPENSIVE,
            tags=SEPARATOR.join(ROOMIE_UNPAYMENT_TAG_IDS),
        )
        return self._format(data)

    def _format(self, data):
        response = []
        sum = 0
        for row in data:
            amount = abs(row["amount"])
            response.append(
                {
                    "Description": row["desc"].replace('\n', ' - '),
                    "USD Amount": str(amount),
                    "Category": row["category"],
                    "Tags": SEPARATOR.join(row["tags"]),
                    "Date": row["date"],
                    "ID": row["id"],
                }
            )
            sum += amount

        response.append(
            {
                "Description": "TOTAL / 2",
                "USD Amount": f"{sum/2:.3f}",
                "Category": "---",
                "Tags": "---",
                "Date": "---",
                "ID": "---",
            }
        )
        return response
