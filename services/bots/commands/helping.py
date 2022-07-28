from aiogram import types
from .auth import auth_middleware

@auth_middleware
async def start_handler(event: types.Message):
    await event.answer(
        ("Hi Boss🤓. How can I Help you?👀")
    )
