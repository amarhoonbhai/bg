from aiogram import Bot
from config import REQUIRED_CHANNELS, REQUIRED_GROUP


async def check_all_membership(bot: Bot, user_id: int):
    # check channels
    for channel in REQUIRED_CHANNELS:
        try:
            member = await bot.get_chat_member(channel, user_id)
            if member.status not in ["member", "administrator", "creator"]:
                return False
        except:
            return False

    # check group
    try:
        member = await bot.get_chat_member(REQUIRED_GROUP, user_id)
        if member.status not in ["member", "administrator", "creator"]:
            return False
    except:
        return False

    return True
