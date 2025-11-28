from aiogram import types
from config import ADMIN_ID

def admin_only(func):
    async def wrapper(message: types.Message, *args, **kwargs):
        if message.from_user.id != ADMIN_ID:
            return await message.answer("❌ You are not allowed to use this command.")
        return await func(message, *args, **kwargs)
    return wrapper
