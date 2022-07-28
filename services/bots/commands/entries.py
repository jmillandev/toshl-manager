from aiogram import types
from .auth import auth_middleware
from re import search
from toshl_manager.utils import date
from toshl_manager.utils.cleaners.roomie_expenses import RoomieExpensesCleaner
from services.formatters.table import TableFormat
from services.bots.utils import ScaperSpecialChars
from services.text_to_image import TextToImageConverter
class EntriesCommand:

    REGEX_PATTERN = r"(?P<command>(show)|(clean))(\s+from\s+(?P<from>\d{1,2}\/\d{1,2}\/\d{1,2}))?(\s+to\s+(?P<to>\d{1,2}\/\d{1,2}\/\d{1,2}))?"

    def __init__(self, commands, cleaner, **kwargs) -> None:
        self._commands = commands
        self._cleaner = cleaner
        self._commands_kwargs = kwargs

    @auth_middleware
    async def handler(self, event: types.Message):
        kwargs = self._resolve_kwargs(event.text)
        print(f"TELEGRAM - {kwargs}")  # TODO: Set logger
        if not kwargs.get("command"):
            return await self._bad_request(event)

        entries = await self._get_entries(**kwargs)
        message = TableFormat().execute(entries)
        TextToImageConverter.execute(message)
        return await event.answer(
            # TODO: Show this message like as image
            f"```{ScaperSpecialChars.clean(message)}```",
            parse_mode=types.ParseMode.MARKDOWN_V2,
        )

    def _bad_request(self, event: types.Message):
        return event.answer(
            f"Sorry😥\.\n\nThe message should be like as '{self._available_commands()} [from dd/mm/aa] [to dd/mm/aa]'\.\n\n"
            f"*By Default 'from' is {date.begin_month()} and 'to' is {date.end_month()}*",
            parse_mode=types.ParseMode.MARKDOWN_V2,
        )

    def _resolve_kwargs(self, message: str):
        matches = search(self.REGEX_PATTERN, message)
        if not matches:
            return {}

        return {
            "date_from": matches.group("from"),
            "date_to": matches.group("to"),
            "command": self._commands.get(matches.group("command")),
        }

    def _available_commands(self):
        return "|".join(self._commands.keys())

    def _get_entries(self, command, date_from, date_to):
        return command(
            self._cleaner,
            date_from or date.begin_month(),
            date_to or date.end_month(),
            **self._commands_kwargs
        ).execute()
