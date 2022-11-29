import asyncio

from aiogram import types

from libs.formatters import TableFormat
from libs.text_to_image import TextToImageConverter
from src.budgets.services.summary_list import BudgetSumaryListService 
from src.budgets.serializers import BudgetSerializer
from .interfaces import SubscriberIogramInterface
from .utils import parse_regex


class ListBugets(SubscriberIogramInterface):
    """
    List the buggets information(Name, limit, planned, etc)
    """
    # TODO: Apply DRY with (?P<from_date>\d{1,2}\/\d{1,2}\/\d{1,2}))?
    REGEX_PATTERN = r"(\s+from\s+(?P<from_date>\d{1,2}\/\d{1,2}\/\d{1,2}))?(\s+to\s+(?P<to_date>\d{1,2}\/\d{1,2}\/\d{1,2}))?"

    def __init__(self, ) -> None:
        super().__init__()

    async def handler(self, event: types.Message)-> None:
        kwargs = parse_regex(event.text, self.REGEX_PATTERN)
        serializer = BudgetSerializer()

        budgets = asyncio.run(
            BudgetSumaryListService().execute(**kwargs)
        )

        data = (serializer.json(budget) for budget in budgets)
        message = TableFormat().format(data)

        return await event.answer_photo(TextToImageConverter.execute(message))
    
    def command(self) -> str:
        return 'buggets:list'