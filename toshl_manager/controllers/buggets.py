from config import TOSH_SECRET_KEY, BUGGETS_SHARED
from services.toshl_finances.toshl_app import ToshlApp
from collections import defaultdict

toshl_app = ToshlApp(TOSH_SECRET_KEY)
BUGGETS_SHARED = set(BUGGETS_SHARED)

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
            if self._is_a_rooming_bugget(row["id"]):
                self._split_amount(row)
            used = row["amount"] - row["planned"]
            overspending = 0
            free = row["limit"] + row['rollover_amount'] - row["amount"]
            needed = row["limit"] + row['rollover_amount'] - used
            if free < 0:
                overspending, free = free, overspending
            if needed < 0:
                needed = 0

            response.append(
                {
                    "Name": row["name"],
                    "Bugget (USD)": row["limit"] + row['rollover_amount'],
                    "Planned (USD)": row["planned"],
                    "Used (USD)": used,
                    "Free (USD)": free,
                    "Overspending (USD)": overspending,
                    "Needed (USD)": needed,
                    "Shared with rommie": str(self._is_a_rooming_bugget(row["id"])),
                    "ID": row["id"],
                }
            )
            sum['used'] += used
            sum['overspending'] += overspending
            sum['free'] += free
            sum['limit'] += row["limit"]
            sum["planned"] += row["planned"]
            sum["needed"] += needed

        response.append(
            {
                    "Name": "---",
                    "Bugget (USD)": sum["limit"],
                    "Planned (USD)": sum["planned"],
                    "Used (USD)": sum["used"],
                    "Free (USD)": sum["free"],
                    "Overspending (USD)": sum["overspending"],
                    "Needed (USD)": sum["needed"],
                    "Shared with rommie": "---",
                    "ID": "---"
                }
        )
        return response

    def _is_a_rooming_bugget(self, bugget_id):
        return (bugget_id.split('-')[0] in BUGGETS_SHARED)

    def _split_amount(self, row):
        for key in ["amount", "limit", "planned"]:
            if not bool(row[key]):
                continue
            row[key] = row[key] / 2
