from aiogram import types
from .auth import auth_middleware
from re import search
from toshl_manager.utils import date
from toshl_manager.controllers.entries import show, clean
from toshl_manager.utils.cleaners.roomie_expenses import RoomieExpensesCleaner
from services.formatters.table import TableFormat

from config import (BOT_TOKEN, DEBTOR_TAG_ID, LOAND_CATEGORY_ID, ROOMIE_TAG_ID,
                    SEPARATOR, UNPAYMENT_TAG_ID)

REGEX_PATTERN = r'(?P<command>(show)|(clean))(\s+from\s+(?P<from>\d{1,2}\/\d{1,2}\/\d{1,2}))?(\s+to\s+(?P<to>\d{1,2}\/\d{1,2}\/\d{1,2}))?'
COMMANDS = {
    'show': show.ShowEntriesController
    # 'clean': clean.CleanUnpaymentEntriesController
}
ESCAPE_CHARS = ('_', '*', '[', ']', '(', ')', '~', '`', '>', '#', '+', '-', '=', '|', '{', '}', '.', '!')


@auth_middleware
async def start_handler(event: types.Message):
    await event.answer(
        ("Hi Boss🤓. How can I Help you?👀")
    )

@auth_middleware
async def entries(event: types.Message):
    # TODO: Refactor this function
    kwargs = resolve_args(event.text)
    print(f"TELEGRAM - {kwargs}")
    if not kwargs.get('command'):
        return await event.answer(
            'Sorry😥.\n\nThe message should be like as "show|clean [from dd/mm/aa] [to dd/mm/aa]".\n\n'
            f"*By Default 'from' is {date.begin_month()} and 'to' is {date.end_month()}*",
            parse_mode=types.ParseMode.MARKDOWN_V2
        )
    entries = await kwargs['command'](
        RoomieExpensesCleaner,
        kwargs['date_from'] or date.begin_month(),
        kwargs['date_to'] or date.end_month(),
        tags=SEPARATOR.join((ROOMIE_TAG_ID, UNPAYMENT_TAG_ID)),
        includes=["category", "tags"]
    ).execute()
    message = TableFormat().execute(entries)
    for char in ESCAPE_CHARS:
        message = message.replace(char, f"\{char}")
    # TODO: Show this message like as image
    return await event.answer(
            f"```{message}```",
            parse_mode=types.ParseMode.MARKDOWN_V2
        )

def resolve_args(message: str):
    matches = search(REGEX_PATTERN, message)
    if not matches:
        return {}

    return {
        'date_from': matches.group('from'),
        'date_to': matches.group('to'),
        'command': COMMANDS.get(matches.group('command'))
    }
