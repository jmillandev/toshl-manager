from aiogram import types
from config import BOT_OWNER


def auth_middleware(handler):
    async def wrapper(event: types.Message):
        user = event.from_user
        if user.username != BOT_OWNER:
            return await event.answer(
                (
                    f"Hello, *{user.full_name}* 👋\!\n"
                    "I'm sorry😥, but\.\.\. I'm a Jesús Millán's Bot🤖\. Only him can talk me\!😕"
                ),
                parse_mode=types.ParseMode.MARKDOWN_V2,
            )
        await handler(event)

    return wrapper
