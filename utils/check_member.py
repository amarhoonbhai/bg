from aiogram import Bot
from config import REQUIRED_CHANNELS

async def check_all_membership(bot: Bot, user_id: int):
    for ch in REQUIRED_CHANNELS:
        try:
            mem = await bot.get_chat_member(ch, user_id)
            if mem.status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False
    return True
