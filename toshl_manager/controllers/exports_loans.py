from services.toshl_finances.toshl_app import ToshlApp
from services.toshl_finances.entries import types
from config import TOSH_SECRET_KEY, LOAND_CATEGORY_ID, LOAND_TAG_IDS

toshl_app = ToshlApp(TOSH_SECRET_KEY)

class ExportLoans:
  def __init__(self, from_date, to_date) -> None:
    self._from_date = from_date
    self._to_date = to_date
  
  async def execute(self):
    data = await toshl_app.entries().list(
      from_date = self._from_date,
      to_date = self._to_date,
      type = types.EXPENSIVE,
      categories = LOAND_CATEGORY_ID,
      tags = LOAND_TAG_IDS
    )
    return data
