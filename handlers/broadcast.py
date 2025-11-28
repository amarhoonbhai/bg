from aiogram import Router, types
from aiogram.filters import Command
from utils.database import all_users
from utils.decorators import admin_only

router = Router()


@router.message(Command("broadcast"))
@admin_only
async def ask_broadcast(message: types.Message):
    await message.answer("📢 Send the broadcast message (text or photo).")


@router.message()
@admin_only
async def start_broadcast(message: types.Message, bot):
    users = all_users()
    sent = 0

    for (uid,) in users:
        try:
            if message.photo:
                await bot.send_photo(uid, message.photo[-1].file_id, caption=message.caption)
            else:
                await bot.send_message(uid, message.text)
            sent += 1
        except:
            pass

    await message.answer(f"📣 Broadcast delivered to {sent} users.")
