from aiogram import Router, types
from aiogram.filters import Command
from utils.database import total_users, total_processed

router = Router()


@router.message(Command("stats"))
async def stats_cmd(message: types.Message):
    await message.answer(
        f"📊 <b>Bot Stats</b>\n\n"
        f"👥 Total Users: {total_users()}\n"
        f"🖼 Total Images Processed: {total_processed()}"
    )
