import asyncio

from aiogram import types

from libs.formatters import TableFormat
from libs.text_to_image import TextToImageConverter
from src.entries.controllers.loans import LoanController

from .interfaces import SubscriberIogramInterface
from .utils import parse_regex


class CleanLoans(SubscriberIogramInterface):
    """
    Remove unpayment tag from the loan entries. And show the entries modificated
    """
    REGEX_PATTERN = r"(\s+from\s+(?P<from_date>\d{1,2}\/\d{1,2}\/\d{1,2}))?(\s+to\s+(?P<to_date>\d{1,2}\/\d{1,2}\/\d{1,2}))?"

    async def handler(self, event: types.Message)-> None:
        kwargs = parse_regex(event.text, self.REGEX_PATTERN)
        formater = TableFormat
        controller = LoanController()

        entries = asyncio.run(controller.list(**kwargs))
        asyncio.run(controller.receive_payment(**kwargs))

        message = formater().format(entries)
        return await event.answer_photo(TextToImageConverter.execute(message))

    def command(self) -> str:
        return 'loans:clean'


class ListLoans(SubscriberIogramInterface):
    """
    List the loans in the specific format
    """
    REGEX_PATTERN = r"(\s+from\s+(?P<from_date>\d{1,2}\/\d{1,2}\/\d{1,2}))?(\s+to\s+(?P<to_date>\d{1,2}\/\d{1,2}\/\d{1,2}))?"

    async def handler(self, event: types.Message)-> None:
        kwargs = parse_regex(event.text, self.REGEX_PATTERN)
        formater = TableFormat
        controller = LoanController()

        entries = asyncio.run(controller.list(**kwargs))

        message = formater().format(entries)
        return await event.answer_photo(TextToImageConverter.execute(message))

    def command(self) -> str:
        return 'loans:list'
