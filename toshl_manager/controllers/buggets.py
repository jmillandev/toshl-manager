from config import TOSH_SECRET_KEY
from services.toshl_finances.toshl_app import ToshlApp
from collections import defaultdict

toshl_app = ToshlApp(TOSH_SECRET_KEY)

def zero():
  return 0

class Buggets:
    def __init__(self, from_date, to_date) -> None:
        self._from_date = from_date
        self._to_date = to_date

    async def execute(self):
        data = await toshl_app.buggets().list(
            from_date=self._from_date,
            to_date=self._to_date
        )
        return self._format(data)

    def _format(self, data):
        response = []
        sum = defaultdict(zero)
        for row in data:
            used = row["amount"] - row["planned"]
            overspending = 0
            free = row["limit"] - row["amount"]
            needed = row["limit"] - used
            if free < 0:
                overspending, free = free, overspending
            if needed < 0:
                needed = 0

            response.append(
                {
                    "Name": row["name"],
                    "Bugget (USD)": row["limit"],
                    "Planned (USD)": row["planned"],
                    "Used (USD)": used,
                    "Free (USD)": free,
                    "Overspending (USD)": overspending,
                    "Needed (USD)": needed,
                    "ID": row["id"],
                }
            )
            sum['used'] += used
            sum['overspending'] += overspending
            sum['free'] += free
            sum['limit'] += row["limit"]
            sum["planned"] += row["planned"]
            sum["amount"] += row["amount"]

        response.append(
            {
                    "Name": "---",
                    "Bugget (USD)": sum["limit"],
                    "Planned (USD)": sum["planned"],
                    "Used (USD)": sum["used"],
                    "Free (USD)": sum["free"],
                    "Overspending (USD)": sum["overspending"],
                    "Needed (USD)": sum["amount"],
                    "ID": "---"
                }
        )
        return response
