import asyncio

from aiogram import Bot, Dispatcher

from config import BOT_TOKEN

from .interfaces import SubscriberIogramInterface
from .loands import ListLoans, CleanLoans
from .budgets import ListBugets
from .roomie_expenses import ListRoomieExpenses, CleanRoomieExpenses

class Application:
    def __init__(self) -> None:
        self.bot = Bot(token=BOT_TOKEN)
        self.dispatcher = Dispatcher(bot=self.bot)

    async def start_listening(self)-> None:
        try:
            print("Telegram Bot🤖 is running!🏃🏾🔥")
            await self.dispatcher.start_polling()
        finally:
            await self.bot.close()

    def add_subscriber(self, subscriber: SubscriberIogramInterface) -> None:
        self.dispatcher.register_message_handler(
            subscriber.handler,
            commands=subscriber.command
        )

if __name__ == "__main__":
    app = Application()
    app.add_subscriber(ListLoans)
    app.add_subscriber(CleanLoans)
    app.add_subscriber(ListBugets)
    app.add_subscriber(ListRoomieExpenses)
    app.add_subscriber(CleanRoomieExpenses)

    asyncio.run(app.start_listening())
