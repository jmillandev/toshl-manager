from services.toshl_finances.entries.repository import Entry
from services.toshl_finances.buggets.repository import Bugget

class ToshlApp:

  def __init__(self, secret_key) -> None:
    self._secret_key = secret_key

  def entries(self):
    return Entry(self._secret_key)

  def buggets(self):
    return Bugget(self._secret_key)
