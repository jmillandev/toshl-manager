import asyncio

from aiogram import types

from libs.formatters import TableFormat
from libs.text_to_image import TextToImageConverter
from src.entries.controllers.roomie_expenses import RoomieExpenseController

from .interfaces import SubscriberIogramInterface
from .utils import parse_regex


class CleanRoomieExpenses(SubscriberIogramInterface):
    """
    Remove unpayment tag from the roomie expense entries. And show the entries modificated
    """
    REGEX_PATTERN = r"(\s+from\s+(?P<date_from>\d{1,2}\/\d{1,2}\/\d{1,2}))?(\s+to\s+(?P<date_to>\d{1,2}\/\d{1,2}\/\d{1,2}))?"

    async def handler(self, event: types.Message)-> None:
        kwargs = parse_regex(event.text, self.REGEX_PATTERN)
        formater = TableFormat
        controller = RoomieExpenseController()

        entries = asyncio.run(controller.list(**kwargs))
        asyncio.run(controller.receive_payment(**kwargs))

        message = formater().format(entries)
        return await event.answer_photo(TextToImageConverter.execute(message))
    
    def command(self) -> str:
        return 'expenses:clean'


class ListRoomieExpenses(SubscriberIogramInterface):
    """
    List the roomie expenses that yet are unpayment in the indicate format
    """
    REGEX_PATTERN = r"(\s+from\s+(?P<date_from>\d{1,2}\/\d{1,2}\/\d{1,2}))?(\s+to\s+(?P<date_to>\d{1,2}\/\d{1,2}\/\d{1,2}))?"

    async def handler(self, event: types.Message)-> None:
        kwargs = parse_regex(event.text, self.REGEX_PATTERN)
        formater = TableFormat
        controller = RoomieExpenseController()

        entries = asyncio.run(controller.list(**kwargs))

        message = formater().format(entries)
        return await event.answer_photo(TextToImageConverter.execute(message))
    
    def command(self) -> str:
        return 'expenses:list'
