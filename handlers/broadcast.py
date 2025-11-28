from aiogram import Router, types
from utils.database import all_users
from utils.decorators import admin_only

router = Router()

@router.message(commands={"broadcast"})
@admin_only
async def ask_broadcast(message: types.Message):
    await message.answer("📡 Send broadcast (text/photo/video):")

@router.message()
@admin_only
async def do_broadcast(message: types.Message, bot):
    for (uid,) in all_users():
        try:
            if message.photo:
                await bot.send_photo(uid, message.photo[-1].file_id, caption=message.caption)
            else:
                await bot.send_message(uid, message.text)
        except:
            pass

    await message.answer("📢 Broadcast sent.")
