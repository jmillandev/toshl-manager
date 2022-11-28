import asyncio

from aiogram import types

from libs.formatters import TableFormat
from libs.text_to_image import TextToImageConverter
from src.entries.controllers.budgets import BudgetController

from .interfaces import SubscriberIogramInterface
from .utils import parse_regex


class ListBugets(SubscriberIogramInterface):
    """
    List the buggets information(Name, limit, planned, etc)
    """
    # TODO: Apply DRY with (?P<date_from>\d{1,2}\/\d{1,2}\/\d{1,2}))?
    REGEX_PATTERN = r"(\s+from\s+(?P<date_from>\d{1,2}\/\d{1,2}\/\d{1,2}))?(\s+to\s+(?P<date_to>\d{1,2}\/\d{1,2}\/\d{1,2}))?"

    async def handler(self, event: types.Message)-> None:
        kwargs = parse_regex(event.text, self.REGEX_PATTERN)
        formater = TableFormat
        controller = BudgetController()

        entries = asyncio.run(controller.list(**kwargs))

        message = formater().format(entries)
        return await event.answer_photo(TextToImageConverter.execute(message))

    
    def command(self) -> str:
        return 'buggets:list'
