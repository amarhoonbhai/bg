from aiogram import Router, types
from utils.database import total_users, total_processed

router = Router()

@router.message(commands={"stats"})
async def stats_cmd(message: types.Message):
    await message.answer(
        f"📊 <b>Bot Stats</b>\n\n"
        f"👥 Total Users: {total_users()}\n"
        f"🖼 Total Images Processed: {total_processed()}"
    )
