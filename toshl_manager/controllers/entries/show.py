from config import TOSH_SECRET_KEY
from services.toshl_finances.entries import types
from services.toshl_finances.toshl_app import ToshlApp

toshl_app = ToshlApp(TOSH_SECRET_KEY)


class ShowEntriesController:

    ALLOWED_INCLUDES = {
        "tags": toshl_app.tags().list,
        "category": toshl_app.categories().list,
    }

    def __init__(
        self, cleaner, from_date, to_date, entry_type=types.EXPENSIVE, includes=[], **filters
    ) -> None:
        self._from_date = from_date
        self._to_date = to_date
        self._type = entry_type
        self._filters = filters
        self._cleaner = cleaner
        self._includes = {key: self.ALLOWED_INCLUDES[key] for key in includes}

    async def execute(self):
        data = await toshl_app.entries().list(
            from_date=self._from_date,
            to_date=self._to_date,
            type=self._type,
            includes=self._includes,
            **self._filters
        )
        return self._cleaner.clean(data)
