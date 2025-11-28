from aiogram import Bot
from aiogram.exceptions import TelegramForbiddenError
from config import REQUIRED_CHANNELS, REQUIRED_GROUP


async def check_all_membership(bot: Bot, user_id: int) -> bool:
    for channel in REQUIRED_CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status in ("left", "kicked"):
                return False
        except:
            return False

    # Group chat enforcement
    try:
        group_id = REQUIRED_GROUP.replace("https://t.me/", "")
        member = await bot.get_chat_member(group_id, user_id)
        if member.status in ("left", "kicked"):
            return False
    except:
        return False

    return True
