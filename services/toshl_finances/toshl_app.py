from services.toshl_finances.entries.repository import Entry

class ToshlApp:

  def __init__(self, secret_key) -> None:
    self._secret_key = secret_key

  def entries(self):
    return Entry(self._secret_key)
