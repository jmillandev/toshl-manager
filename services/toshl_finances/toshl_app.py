from services.toshl_finances.entries.repository import Entry
from services.toshl_finances.buggets.repository import Bugget
from services.toshl_finances.categories.repository import Category
from services.toshl_finances.tags.repository import Tag

class ToshlApp:

  def __init__(self, secret_key) -> None:
    self._secret_key = secret_key

  def entries(self):
    return Entry(self._secret_key)

  def buggets(self):
    return Bugget(self._secret_key)

  def categories(self):
    return Category(self._secret_key)
  
  def tags(self):
    return Tag(self._secret_key)
