from aiogram import Bot
from config import REQUIRED_CHANNELS, REQUIRED_GROUP


async def check_all_membership(bot: Bot, user_id: int) -> bool:
    # Check all channels
    for channel in REQUIRED_CHANNELS:
        try:
            m = await bot.get_chat_member(channel, user_id)
            if m.status in ("left", "kicked"):
                return False
        except:
            return False

    # Check required group
    try:
        group = REQUIRED_GROUP.replace("https://t.me/", "")
        m = await bot.get_chat_member(group, user_id)
        if m.status in ("left", "kicked"):
            return False
    except:
        return False

    return True
