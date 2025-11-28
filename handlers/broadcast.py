from aiogram import Router, types
from utils.decorators import admin_only
from utils.database import get_all_users

router = Router()


@router.message(commands={"broadcast"})
@admin_only
async def broadcast_cmd(message: types.Message):
    await message.answer("📢 Send the broadcast message (text/photo/video):")


@router.message()
async def handle_broadcast(message: types.Message, bot):
    """Broadcast forwarder for admin"""
    if message.reply_to_message and message.reply_to_message.text == "📢 Send the broadcast message (text/photo/video):":
        users = get_all_users()
        sent = 0

        for uid in users:
            try:
                if message.photo:
                    await bot.send_photo(uid, message.photo[-1].file_id, caption=message.caption)
                elif message.video:
                    await bot.send_video(uid, message.video.file_id, caption=message.caption)
                else:
                    await bot.send_message(uid, message.text)
                sent += 1
            except:
                pass

        await message.answer(f"📢 Broadcast delivered to {sent} users.")
