from aiogram import Router, types
from utils.database import add_user, init_db
from utils.check_member import check_all_membership
from utils.buttons import start_menu, verify_buttons

router = Router()

init_db()


@router.message(commands={"start"})
async def start_cmd(message: types.Message, bot):
    user_id = message.from_user.id
    add_user(user_id)

    ok = await check_all_membership(bot, user_id)
    if not ok:
        return await message.answer(
            "🔐 <b>To use the bot, please join all required channels.</b>",
            reply_markup=verify_buttons()
        )

    await message.answer(
        "<b>✨ Welcome to Instant BG Remover Bot!</b>\nChoose a tool below:",
        reply_markup=start_menu()
    )

