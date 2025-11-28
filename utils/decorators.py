from aiogram.types import Message
from config import ADMIN_IDS


def admin_only(func):
    async def wrapper(message: Message, *args, **kwargs):
        if message.from_user.id not in ADMIN_IDS:
            return await message.answer("❌ You are not authorized.")
        return await func(message, *args, **kwargs)
    return wrapper
